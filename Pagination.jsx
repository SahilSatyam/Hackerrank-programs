import React, { useState, useMemo } from 'react';

const PaginationComponent = ({ appLevelRetnRemFilteredData }) => {
  const pageSize = 20;
  const totalItems = appLevelRetnRemFilteredData.length;
  const pageCount = Math.ceil(totalItems / pageSize);

  const [currentPage, setCurrentPage] = useState(1);

  const handlePreviousPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 1));
  };

  const handleNextPage = () => {
    setCurrentPage((prevPage) => Math.min(prevPage + 1, pageCount));
  };

  const renderPageNumbers = useMemo(() => {
    const visiblePages = 5;
    const sideDots = 2;

    let startPage = currentPage - Math.floor(visiblePages / 2);
    startPage = Math.max(startPage, 1);
    const endPage = Math.min(startPage + visiblePages - 1, pageCount);

    const pageNumbers = [];
    if (currentPage > sideDots + 1) {
      pageNumbers.push(1);
      if (currentPage > sideDots + 2) {
        pageNumbers.push('dots');
      }
    }

    for (let i = startPage; i <= endPage; i++) {
      pageNumbers.push(i);
    }

    if (currentPage < pageCount - sideDots) {
      if (currentPage < pageCount - sideDots - 1) {
        pageNumbers.push('dots');
      }
      pageNumbers.push(pageCount);
    }

    return pageNumbers.map((pageNumber, index) => {
      if (pageNumber === 'dots') {
        return <span key={`dots${index}`} className="dots">...</span>;
      }

      return (
        <div
          key={pageNumber}
          className={`slider-item ${currentPage === pageNumber ? 'active' : ''}`}
          onClick={() => setCurrentPage(pageNumber)}
          data-testid={`page-${pageNumber}`}
        >
          {pageNumber}
        </div>
      );
    });
  }, [currentPage, pageCount]);

  return (
    <div className="pagination">
      <button onClick={handlePreviousPage} disabled={currentPage === 1}>Previous</button>
      {renderPageNumbers}
      <button onClick={handleNextPage} disabled={currentPage === pageCount}>Next</button>
    </div>
  );
};

export default PaginationComponent;
