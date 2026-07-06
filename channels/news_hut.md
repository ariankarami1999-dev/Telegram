<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/JkcmrJKE4WdavYJdmHBxrv6Bp0Ih1wPm_zhMBBiRFxmXFdPqKrI9Hs0LCRTbuq8jmWGp22wmfaoB3QSUCokxRQ07kOUj-ewfSbbRmZsDtXP6cX3ZPndaEVi3mPtQ2XCPq5AXkNs7uewLNks24EURkn-RKCAmVHsbaxrkp52rAQqFyZeyI-WXCASKY5_pR8nTMfK86EAWJM6ROudzAKsJbDONWA8CVQ_N0GEF_S4x-iMUEzMSgfjhBT0FO7rsKRfYXtcxYqh9CCHPAw2i9cax9DT-HpWaLWevug27rAtM_IeKlzX042F87o2dKfrZlkTmbsm1GEl7YxRJKGEpGif-rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 201K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=g24nHF4OoOlFlidOh7RLSIvdATp7d7I7fJ_LAXMg4iE7A7S_DMgvpeKRJjGkjW5b2otyadtbs6qf7xgMclJycJJUC9ZLEZYFzgHkQotCn4CKfgiuhlxC-_IA2r7wxVDmjGF1Ck4eCosmhZWHLmBVxLqr1yCyHocJ4f84007XjJG7mE2wOTihUaLcHsVNRxEbIuqrMPGZK9WUH8eNz2ALQMq6O227hMK_gQm1zfH_OeelNpoBweDyHX_dJ7YujzRWDWWI0PHt7oXKMzsBkZ_p_wbsyt4CE010bkI7gMJpnONtQXuucw1A1zfpb0vq6iHf5DGb2PSTPlPpA_RBcFMKKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=g24nHF4OoOlFlidOh7RLSIvdATp7d7I7fJ_LAXMg4iE7A7S_DMgvpeKRJjGkjW5b2otyadtbs6qf7xgMclJycJJUC9ZLEZYFzgHkQotCn4CKfgiuhlxC-_IA2r7wxVDmjGF1Ck4eCosmhZWHLmBVxLqr1yCyHocJ4f84007XjJG7mE2wOTihUaLcHsVNRxEbIuqrMPGZK9WUH8eNz2ALQMq6O227hMK_gQm1zfH_OeelNpoBweDyHX_dJ7YujzRWDWWI0PHt7oXKMzsBkZ_p_wbsyt4CE010bkI7gMJpnONtQXuucw1A1zfpb0vq6iHf5DGb2PSTPlPpA_RBcFMKKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SOPetZW1U6ZERDhJ2XYo8jPVtFiLY2lzhZYBxdQMKxsXRztt_e3ymCIq-D7seMUOWzEQcPzNMnhc05OeK7vqQw8lVpyAcuEbHBntHWOavfo7wODi2DeN_3S5BpQLBMnfH28ALMEEgP2T7EfE_h_qCds_P2XdGifzm1-Ae6atiE0YbOeYGNQ84M3EZUQsQLKhIJIMUgQQgy-1bFpOqLkzg_GPPAqqcuURiTwRZ73tOkkGujYK3IZ4XyCHHba4QBZv0Iqr01o8Pfxa9YOxTwLSojRCBa7kfL3Rddp-qnAKSAoNroMgYDPK3ebJcDekIJ0eiU5ytMFUUJMMVEweFGY5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SOPetZW1U6ZERDhJ2XYo8jPVtFiLY2lzhZYBxdQMKxsXRztt_e3ymCIq-D7seMUOWzEQcPzNMnhc05OeK7vqQw8lVpyAcuEbHBntHWOavfo7wODi2DeN_3S5BpQLBMnfH28ALMEEgP2T7EfE_h_qCds_P2XdGifzm1-Ae6atiE0YbOeYGNQ84M3EZUQsQLKhIJIMUgQQgy-1bFpOqLkzg_GPPAqqcuURiTwRZ73tOkkGujYK3IZ4XyCHHba4QBZv0Iqr01o8Pfxa9YOxTwLSojRCBa7kfL3Rddp-qnAKSAoNroMgYDPK3ebJcDekIJ0eiU5ytMFUUJMMVEweFGY5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=Ns-Gqi_5XHS31UagR8AY_7yPEHLj5Y3y8x1fnv7tZVPM7cx_PG4FbAzPN9XsvjJi_M0454UBfGHsC8myUPRrdOqb6310s9RWHAILGqOvaP1-CiZZtY2qdiC4odyj8IEE8J0OC1KugVNJPgjJbL-DIVJZxiqXD4ia5XLNckLehb24qFthlqCHjPsToCoLJDntX7VJqV7TqrTPoTsJu-OXnyb9h86afhQl3BT79Tah03LgCBAbwSFKOTp9KmqzXh39dkATWLoilGx-WIoSVnVDW84dQ0CEsApyR43JPOxWMYZ3MfVFxbIigdGkF0xbGLRfFyKYZDQTr3l5x9VDfWem1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=Ns-Gqi_5XHS31UagR8AY_7yPEHLj5Y3y8x1fnv7tZVPM7cx_PG4FbAzPN9XsvjJi_M0454UBfGHsC8myUPRrdOqb6310s9RWHAILGqOvaP1-CiZZtY2qdiC4odyj8IEE8J0OC1KugVNJPgjJbL-DIVJZxiqXD4ia5XLNckLehb24qFthlqCHjPsToCoLJDntX7VJqV7TqrTPoTsJu-OXnyb9h86afhQl3BT79Tah03LgCBAbwSFKOTp9KmqzXh39dkATWLoilGx-WIoSVnVDW84dQ0CEsApyR43JPOxWMYZ3MfVFxbIigdGkF0xbGLRfFyKYZDQTr3l5x9VDfWem1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=k31tpFgMCjly3Qa-I8lXtIeb-HWBlQBW1Q_b17lu8VB-de2XsAdq2XGaogfUqVEJO-kVlJw4EYy12qQ6_cdX5DBbiSHixoCCOk3OqbmlLS1eaQP8m6i-VCwGgxUggxqvoe3c_ryK_6cwROTavY7QaNVXORL_9dYHKJhVnbRsqeXgCZUW9Hi_cA2BPDpTUfBbgXVms3ANI1uIXCaTzNSKAhCl1u8Ng646r9vlGrfHsJE6w2xeSqgCXDk2ox5yowPyqvKzB0I22KGuUqI2qP36lo440q4WvKVtWaFc3YTM6HmLI5eVFCgTaDmN67kUN3hcH-Jf3ror26FXiGBcs33jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=k31tpFgMCjly3Qa-I8lXtIeb-HWBlQBW1Q_b17lu8VB-de2XsAdq2XGaogfUqVEJO-kVlJw4EYy12qQ6_cdX5DBbiSHixoCCOk3OqbmlLS1eaQP8m6i-VCwGgxUggxqvoe3c_ryK_6cwROTavY7QaNVXORL_9dYHKJhVnbRsqeXgCZUW9Hi_cA2BPDpTUfBbgXVms3ANI1uIXCaTzNSKAhCl1u8Ng646r9vlGrfHsJE6w2xeSqgCXDk2ox5yowPyqvKzB0I22KGuUqI2qP36lo440q4WvKVtWaFc3YTM6HmLI5eVFCgTaDmN67kUN3hcH-Jf3ror26FXiGBcs33jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J__UM0vRWzdUx8buMz0w6fTQXWoC-BtIi5aquNRBkQz2XKksehrJZgfTpZeHKGGJAHH8vNrlDVHZ5F_q02_CFeAsBIINZZRPDq8Eb9BYSUVSaxSrMArJKkoE3kuhIxbY-n_Wbi6MK7FoqM9_1xXe0jij0qkVA59zitYTL-XfFnKtAmWOVth4Dj60wQReJTyiQ73UfyDy2JemZLchNBlENl4Aig6IlA70KIV7T7bIvLSCTnMnlKA4uTckwAhXRPOO20yX-S9LkX3xa_UfXSPl7_U6KM5q5PffqpQpETedSxWgIEOKdgCWqzaflnoVPmo5_f2XviNJACGTY7dMXaTAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E93PNiVU_9hhOJCexaJcs1_s3yy62SMIQXJMdX1lvOHEdgjOADHvM42atm04YT90mU0AeUMX3IXhWeWu2Q7s8M7tlccmTDs7nvHbkDMBwuuzKR5dKRVGCTGvxKYyz_T3ARxyk7h5cQVxacbxU5acOrcX1B_jKyhf9DFi0pZZP3wNrQmtygc_cAeJKk179jbG5jIgwH56QDgHClR9p4pMnxhFSG100hxVLqHOL38t-Ar4tWrZY3Zlvq7DH4lznphiUHmHZCWT0lh2WJJ8eLhkbhWy7O45-BhTQLHXR2oXsECdD7UTz5x4Vhu0qH5_yLu0vbI9SCt1Jf4M_t0aEz-OdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWjtWBUPbO7Ui-NAOQmhny9_Cq__42jgHDoI-ZQ7CcBMoDXpAS3dg0LtJIThAbFHQ1bEzKLRX0eoRqiFLvrIGBQ4ygHg7vSgLy92y3RETBU-YEkrq7hz2_Je5hwLl8D4-IV8An9cZsZefhqGWWlqje_FKeOIUou0kvml1sbrky-YYV1Ng3Ise2J23NtK9-GV86iVFS0mjP0F4uLBmHKxRFv51yjITW5-64Bo8Zj2wYh91szAGbxOEykaDSdiQl4shnihcmCMR08ggE2orKvU87jMnb7dzn2hzkqCi3vlrMgvzCnlMGEhWf7nMH_5dxvibbovah8CEf2LHOzp3MR5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW7Z8yWGz-97GTyWZj9uziA2dqsMLHsUFd471aia2isyuBEFBrKjeJdD-5GNDfvd7DYOpS6Nhpc1e-KgPB8yEQPXJvXRJWj41kh1iUqlavpGL12Gmqctn-zXHS6LyYAYPDH9plJN3jbiin9eHqm1J1oCok4C8HgjNoTSb3FhgJcZvK6e6tRQItJae8seYWld8h1SEpZyc5ay48KCwcaALOrYAwjfzH5SxDoO8IDquBAFxwk7iw4f8YDPoapri2UA6ynwCEJK_7LTBHJCf9JneZnp7UaZ81tFjBhw5IePgZBb_cKtIiaUlwdTvT_ur-JaiZbKDpTSv_L5aKhZ7gecww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvCkDSZ8O863B7T78ELG3EhQzhDfvnNJQSnpR4h0jE4soCC8mrfgK0yjBGzrr2BBTMx5ssu5gdazMGqRyL8jCwQOvGwURNXnNQc1inVeht6fzr3tOLfBMX1HFuFu5LK56h46HHT5iY_3EbfSosbttSEHhHRNvH_Er04azq-hTL43VfctQu5o07mpXVW_35lwzR3cY0KdwXCPMvR4eaRdSmRqaQ-mh2xyxc_GOU_hh_nwL9Lwh1Hp1aAHfoFkxfUS05ulbDEKLr8a3VvE41hiI8f7vieMIoBzKOfWcRXFYNHPNgzfLfqH-tS3RkfJda_aqgS3A-OB4JLAWII0FRn8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fssQ0jhqkUsS6dfJyUxUUlXdDK6hYuhPFnmDF9V0mRTIY4F8cH4KoeyR0LapBV_yHBg2t5AgfsuRxSG1odzogHO09x9fLrVZ_GNaNKMPhQlOybzYVneZagPykJ1dFRHuO495tPqupZgwqIhxFTkPpMcrqUVVMlISJyOTc_yFTYtO4vmUjqJIIeaFo2k5pBRAqo_9xtqQzYZlQtJ5NSLIv_owdN5e76fYo-0A4OqQYnHQNx2KMPYOnXwmd7NO7dsBszJNwdFq3twDz3AzTHAymX2DmpwoUdZlA36NOqJQSer-ctKf_1Elo8EIxdErY-7cCC26iavtENrB5Dtb4XaavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=bMm_uIC3uyHZHav5t3dtz-Wq8vZjgftGvn0ikf1waiCSGzaH1sja91aLTbQC2YiXYro-yiQSG6mRVmLT3eQKRMzrnfxpmMlSUmWBXQoNgRMjnzUK9XQOStCjHimFyHw73IchXqeZe0HCcMVlm8DSTWTqOUVmmN_X1Ohjg3scFOtONwrRCu17nAuE2q4V4O6B3nctdv_cZJOsw3m8FqZMzaMHTnZ8LlXisQ4asfYKQfgBPS1p9oYP6cYMKCWHoainT6C1_rssRa7h2ITsBgSxgnsGU2PxeXXTFTPjRFlagRnbFy5SjMS94xrqxJ9VEZdf6IauQokNO4AJxkICUgXeBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=bMm_uIC3uyHZHav5t3dtz-Wq8vZjgftGvn0ikf1waiCSGzaH1sja91aLTbQC2YiXYro-yiQSG6mRVmLT3eQKRMzrnfxpmMlSUmWBXQoNgRMjnzUK9XQOStCjHimFyHw73IchXqeZe0HCcMVlm8DSTWTqOUVmmN_X1Ohjg3scFOtONwrRCu17nAuE2q4V4O6B3nctdv_cZJOsw3m8FqZMzaMHTnZ8LlXisQ4asfYKQfgBPS1p9oYP6cYMKCWHoainT6C1_rssRa7h2ITsBgSxgnsGU2PxeXXTFTPjRFlagRnbFy5SjMS94xrqxJ9VEZdf6IauQokNO4AJxkICUgXeBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=s0ojebqwmOEJIVoNOhdlt0q7QiDD_QJJpWXhLI35dH73Zt8D4vhzgcRSI7goTzfCgtzvuIW_0hE7XBNjukN2mpbIlQMzbxfYpYwz3JJBNoN53ZD2HsvQcOJthe3y2wEXOG1BfU5q3xBKotsjQuRB8-sgEab5OqaVt7KMNiZK28a2VCdly_q7x7AJZOtL9jS_9Ev9asDKFqB91xb5WxWuIhbvTfgKBkRnkPp6g57U_XTYqmcPnPiid-X76Oq22l8M2tS9YWkaBFNK-KWLBYpsaVhnPgAwdKXw2JyshkPnkTF74Co_WJ6fLoUQY8G1SHrTUFe9aMYmoPMSvci4coZawg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=s0ojebqwmOEJIVoNOhdlt0q7QiDD_QJJpWXhLI35dH73Zt8D4vhzgcRSI7goTzfCgtzvuIW_0hE7XBNjukN2mpbIlQMzbxfYpYwz3JJBNoN53ZD2HsvQcOJthe3y2wEXOG1BfU5q3xBKotsjQuRB8-sgEab5OqaVt7KMNiZK28a2VCdly_q7x7AJZOtL9jS_9Ev9asDKFqB91xb5WxWuIhbvTfgKBkRnkPp6g57U_XTYqmcPnPiid-X76Oq22l8M2tS9YWkaBFNK-KWLBYpsaVhnPgAwdKXw2JyshkPnkTF74Co_WJ6fLoUQY8G1SHrTUFe9aMYmoPMSvci4coZawg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCGmu_G7lKVEjBQbjDGNK9EKoiF3o8wE6vhI4efs_lNVrll75pb1C4rfdBxML7TqNjIDRhyg2IYrn_W_0HJD9y1R2fhT0wJu3ll1O8fVwPP7rf4f-Zrj8lVybwQFx7axDUeHhRR8UeJtqmSv64ahdeDjuF4pUoghUzyyi4Hp8EuKIXd1d9ESKWmVizX0bKH85qFNSRWzIHMc3RY9sGaQVb-olUEhLfVjwYvO7jZELGfMKee8OR47shZ5RQwwBV1674VzyoSW-1t4KjwtviJLdjE96YE5l12D5jT008uUTeljloE6syj1lZoOnBFmyiSY0rVIs8I3p4-1YXpsFWbc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InBe6CyMcedOzNWnh8cTop-GOT0XTTR4aUzGS99NfZwPrD-6dWJkWz2sjc6996UWW7NNnQZEsmRRuwJQOe0jE7ElFI6TzONmlQ101p8Ui31RUQNIXia1rnn7RMmYzBGv_FcdyXAjXSo-n-jHeEbQLG69QhZy9PC13MDg5YXo7BTkRuOhxpzjjSPOGf9r9ZaXQ6jxuWBMKdE2mz9Gg7D-QP0ARSc_1Q45UzgQiSwXIDUf_h5N2hLuGk3vt4l2oViNq9vgoCE4DIP06b7gN4trAV7HfYTu3De1kZXxHm4uGwv8oQX9xGtI60edh1mmPbLNEuN2AyZR-ICdOC7OywagHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb60kppNtGUbRxgL1M0jKjiAdO22VNs5mlwzt8WUtf3pAZLVoOWy7G92d64OKOg-cFL_RtjQBV0QRP9uQjSGH3wTuzzoU9XABDOc1RIBp18kU9p1tBAV37TVgnIgG5n3oSC2z5E1cw_ugP1PR4d_qf7Movvx2vmNXWkv9INkZA15yb51ObV6w8UZAiVRTBr-viY5ymilp9dIS135sTTP8kI7FAe3c1KvTgp5C0TbdIvp7-oeIdmIA_ugtl7mUujIF7R1NZsIPYNS76Zz1qvmfldQcBnlZXppwJxKySyOAQEBmkXKNbX70etdE6y5KtdSVWLAPxOpWq8rq8mQqkQn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaPT6RWhqkjXN-jyalnLJmnY73C10zKmf_aUKn0nCBhGp_M8m0GyscTMAzmfOe2ER8cw7QU5yrriXAN2Oi13jnnllXjTkrGkwf2ceUXWHCYTEtlwQ_OzoMERXimQA_5nx8xyUFQd1dakNrpE8pnibOgMtpsYfYynwmLoV4rdZ-Wdeq06MZD5qDlFkFnt4RPV-LOXVUaSh35a478xG1PnE1hGEEIUx48VVbt68LTUNOdar4QtnlCBuN6e2SoXm3uhCPMrUYB-83wG4HC7FnuI1FAeOGwA_o2c3eKsyfiWa0nTayBnSooBChqjkX0BRPnGYOecb2EyNz1RYb5DDbhCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhJBO20txXNK-eJMxl80OtCM6OkOkmy1I5mIrlYyCNMLXudaDRCgz6kruFnNLrWuypjbI8HOSlwOMeQ3333R86WLA9sXAnxmxG0h5ZHymNV6iiP59HkHPv8b7S09CWB1qKZ6P8ysTOhezXL4PAml1QXgr639F4Rjiq71cJYkmCSakrtSSbRs8N_Dlem9S0_4UrRY5tZdxhOHxt1QJOpe--UBEraHOCLW4y93CUL-g2GxgCoQ6AjUoYood3H0qBbIJBcwdTyEKZRrWqTjiDUm52ou83HnGk6shSZkygK2p34opp8IgVVyiK6yXvtuhNchO0bU6XUDC_pwbZVU_z9q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=YvjmhSZihxA0-FIuLPRtNpkDKdN-GGgbRnHTadgUbqglH_hSM5Yh5Zc7nuiS02kV8lHtJ_bxaGeVuzBJoeESxARa_TMJKSgOMzXbYRJ_q2R62O9Hrn9e_x7hcRFg8qNSni4v183VMK592hdLhe4dCE5QCxemt9rwsFSHa9SFbKA1JDOdwKTJ75pGl5oXCpL33v_mIDxVF3X9yFwaM3lDEl9K__8j1iA3_Xospyj77X2mLYDLvgL_nxVHMAk2Mau60IYtg1OxzTIroXeasATcCnyFmXROQ7yyTuE7yDdHUcV30KG3ylrIDAzMqk9UMpNP4OrrayzBsHyMzR_I4_dlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=YvjmhSZihxA0-FIuLPRtNpkDKdN-GGgbRnHTadgUbqglH_hSM5Yh5Zc7nuiS02kV8lHtJ_bxaGeVuzBJoeESxARa_TMJKSgOMzXbYRJ_q2R62O9Hrn9e_x7hcRFg8qNSni4v183VMK592hdLhe4dCE5QCxemt9rwsFSHa9SFbKA1JDOdwKTJ75pGl5oXCpL33v_mIDxVF3X9yFwaM3lDEl9K__8j1iA3_Xospyj77X2mLYDLvgL_nxVHMAk2Mau60IYtg1OxzTIroXeasATcCnyFmXROQ7yyTuE7yDdHUcV30KG3ylrIDAzMqk9UMpNP4OrrayzBsHyMzR_I4_dlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsAvuRmsWZ7Ez1ViAqQ4ezqi1_AzXyhSpR3NF7sKuYAfIRsDR14bFkFIzGGSXt7FK3VtDwDAyf6iY8vL6Pei9Wjk0iZajy57Ewuf20bsqw5FkKYwefgKVrucJTyCheSLRqikXRSJLcXxOc8XWqHfuOXztkd8F4E7iaIBNe91NyXKu-jjoY8ycERJqLaYvkqJNB4ke5IgdobjTc1t434T5EqER0oO0obUM65gdub4UI-4HlW5wk3FdXENxjgB816T_qeGRSutLi089Vuc0y7aFlyGryPidJRZRrZwckV0Qb9FaTPEOXj1yUlV3wWKio_CVkbLsNOib9K_dK4aeVLaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tZ5sCffD7WCct99py9GLIs9TDpasW9Tr2jORH_MfxTnwqoyeVRQyb1M9CUeZ7UDIRd8HAJ8oKY1xmiLuVDcK_cMpS5YGDgdUBrm5rq61XI5cUHvP0fqGOkUo24luq4WeFbmajax5J06w1AqZz_JNnRfPsQVWzlF0L6Sa-yr8x4qns2Ypk31xGeqTPOHiZbhr1AQz08d6QD-nCtbmC83YIjTdWmE-lkCTa8cxYMGflcYbKxTkjHQtYlk5SpFLOYDXxHTUzrbnNXHAZwi2uu7KBDPvh-cHLKgqoMyut2_Zq8X6rafxgdqoVilwgonkHoFJbS95HrgpQV0v9ySCWuBbCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tZ5sCffD7WCct99py9GLIs9TDpasW9Tr2jORH_MfxTnwqoyeVRQyb1M9CUeZ7UDIRd8HAJ8oKY1xmiLuVDcK_cMpS5YGDgdUBrm5rq61XI5cUHvP0fqGOkUo24luq4WeFbmajax5J06w1AqZz_JNnRfPsQVWzlF0L6Sa-yr8x4qns2Ypk31xGeqTPOHiZbhr1AQz08d6QD-nCtbmC83YIjTdWmE-lkCTa8cxYMGflcYbKxTkjHQtYlk5SpFLOYDXxHTUzrbnNXHAZwi2uu7KBDPvh-cHLKgqoMyut2_Zq8X6rafxgdqoVilwgonkHoFJbS95HrgpQV0v9ySCWuBbCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4upekQoej-XpbxK0uss2szlCe612a4HUkZ6PZBm4cpAOUVroCflrdQ-AdFjKZnUF45l5TJi110f1SUXcUEhpz5aEKo-VJt9yLHhf2642zHabF-Cse9-GKudFc-Lu6ehEmPY2Zd-mvBjfA0gdKg5Rie_R-I3fC_TOlwKzRni1A_4LMw-IPB02LdKKd4M1oS6RWX7CKXSwt6M2TGNIkSfR4e0QGHdayzQeKs0lFLHrb0Opzf3eQyeGwhf9_ZiTMK9IRK-Hdn5B2CcgvowSKF9_fU4Z9gNSxqfF-rNBbVzGYymVtSzXW2SOB162uV0cVSJjGc742jJb-JcdqFxUqFRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=DWNJelCDRgMyxMwGGJzJiBQT3uzKfin-za-RnnibAl-j7VuasWnbCDk01vb9F2W7RA2DlCmvlfwYsBeGuOrKPT5HOAwOJ87nB-WL7a-D_YJNHVLMV0Wl1BNVaZslkRzHutpSzxYyn3dUWRi0ZXxvuyPF4Pbkv67X9YxTlz3GSNSIkWlJSjnBKv1EO5SOfpyJ3jK2peRnztZgU7Osa9EjooTyZ48MEWl7nB19oqJPej79EGgaPzrT75AJH4lklaXGzeu8QZ7fXQzorpbKD4SaJqX9Lpw5NBtV0LGNOzNGBboDuHouttEvyD5WyJw3Kuus-LqXwnSr7ioIoRYLBuMJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=DWNJelCDRgMyxMwGGJzJiBQT3uzKfin-za-RnnibAl-j7VuasWnbCDk01vb9F2W7RA2DlCmvlfwYsBeGuOrKPT5HOAwOJ87nB-WL7a-D_YJNHVLMV0Wl1BNVaZslkRzHutpSzxYyn3dUWRi0ZXxvuyPF4Pbkv67X9YxTlz3GSNSIkWlJSjnBKv1EO5SOfpyJ3jK2peRnztZgU7Osa9EjooTyZ48MEWl7nB19oqJPej79EGgaPzrT75AJH4lklaXGzeu8QZ7fXQzorpbKD4SaJqX9Lpw5NBtV0LGNOzNGBboDuHouttEvyD5WyJw3Kuus-LqXwnSr7ioIoRYLBuMJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=dii31jfEwmJ4FaNvfrN3SGRJCYlMEDIZp_p5-MuXjqJIRupm0tRYebBbZH1AdTsXrgZC6-s4Z0moWViE1OZ7x0GZKIGi_IA56CjTaMXx1BPS9hHuAqNLWA8BZnPyXI_6dWJm0c7SV9qyHUKplqiIdP1xa4Np7Lhq1X-ymz2SqrRlhMTA_LLIJ9z6ZM-0OfwEC8wCOZeYN_0YJW7N5gFCuHqZUWVonrY7bhE-0IjL0HrEJt6m_tZ8lAX2GqOF-u9ZNFmVHmIBSOLx2FJR3Evd9frK9pHF6fYeT6ctgEozNILzVW8dl1dqBXW-KIDgiwrRVAdwpILTVqM9WF4eHEv1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=dii31jfEwmJ4FaNvfrN3SGRJCYlMEDIZp_p5-MuXjqJIRupm0tRYebBbZH1AdTsXrgZC6-s4Z0moWViE1OZ7x0GZKIGi_IA56CjTaMXx1BPS9hHuAqNLWA8BZnPyXI_6dWJm0c7SV9qyHUKplqiIdP1xa4Np7Lhq1X-ymz2SqrRlhMTA_LLIJ9z6ZM-0OfwEC8wCOZeYN_0YJW7N5gFCuHqZUWVonrY7bhE-0IjL0HrEJt6m_tZ8lAX2GqOF-u9ZNFmVHmIBSOLx2FJR3Evd9frK9pHF6fYeT6ctgEozNILzVW8dl1dqBXW-KIDgiwrRVAdwpILTVqM9WF4eHEv1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTPhuvSE5b-e9DKIz4S6Ujs4AuqnpllnbBJUFbLFdiwxVmp8aHuNQ8nNhDOZb6LOtCBG2eGRc7-XXejmnHZtpf7rvjdMnWuNgP5UsvvHEf5Y9SZ46QC2vjqvm3Is7L5i6Yi3bF365gBOynE45JT08VYH45QHBWgDIdDQ6ucHIoH_gIkEhQLv7H1-PYevXS4H9qtlHjUMPpfBR3SkKCOfJIfV9uX-eOBmt4Z9abTqr09K4rKVUbUqcfGzUQvJrzY7Sm6jVqmsyLoXYpwUWZBWJRDaQ319iOGptgMPL9Hcwbe0-At66INuixsjBEXNObOAG_kH1M0Icxd1jK3bHmsPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egMDAUTfNJgsfPq048HlQAjhMOEq_3vDTYU782DIu8aRKWsfZ2Bc8or4uCLZZpx_QNk6c6Tjm6gMqKbBvhlZ3oZEMyMH5r3WQtxZsFCaj2wqB4yRgFLlwjaeQh1wAtv6VSR5xoL-jqbShCMEeGf9pP796tO4D1xORxmJOoX48wG08tdy-_XS3U_G5tNfXMndFO-OG_Y7em5ErDm7y6bGSks6z035HfkIxIDK2mVRTsozd51NpekccUJchgKhGaytOOgfUwTJ5UmTvV3vA9T8T2cIwKiueY26YJzvmCSasRgW2P49ZidunH2HGerzdnGTuXvUHZO_SAjPCRntm2KeEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=U3joaOb4oAOtMU2e8Q0Gpd8bxV6_6P9Lztz7se6R9AL2XuWWYMNX1limuZzcq3xZjrfy3HfSicWaT8ZSmmT-mHfSUD3P9t2im2ngvpptnKrO27na_9vfftg_zXDOD3p6baIge0ujY7zuyifkU1UYwFFEHjj-FyZ5jZTpwIynzLxuS6liN53nCRdmWGRvH0uI38fecQX_gn8EDMak1rJS1XoAH6s4ORH_91VbEV60S4Dx5RZdInVNhPdjWnvwGTalSYtOtPgG7dOrzQ1EOFLKU6vXQR02lIosP0h4Oo-sW6C3MYA36ogBPFlhwu8KIwMyg0bJjojXR5gbPIjINocCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=U3joaOb4oAOtMU2e8Q0Gpd8bxV6_6P9Lztz7se6R9AL2XuWWYMNX1limuZzcq3xZjrfy3HfSicWaT8ZSmmT-mHfSUD3P9t2im2ngvpptnKrO27na_9vfftg_zXDOD3p6baIge0ujY7zuyifkU1UYwFFEHjj-FyZ5jZTpwIynzLxuS6liN53nCRdmWGRvH0uI38fecQX_gn8EDMak1rJS1XoAH6s4ORH_91VbEV60S4Dx5RZdInVNhPdjWnvwGTalSYtOtPgG7dOrzQ1EOFLKU6vXQR02lIosP0h4Oo-sW6C3MYA36ogBPFlhwu8KIwMyg0bJjojXR5gbPIjINocCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hXVLhMKAKXyV5g-izkJF6qn7zG4fsRvBopwIFTMyqaLciR_enlSv2zHdmsheyoBuWrfPVqoCr2W-a2xp6sBbyQ9aB-mEl_Vx4Dt3u1dAg1eWtgvVmuBm0_wXcDJlOonu-3uZSZx8TqDNLc4IbZlnHE7L99an_olSnXJaGm7_nqwLcX_SA9PedCdhJnUiGBVGBo32hjV_KSeW3hzie-NpNGLiWHBvQsliHxkT0qRs00AxNx5mQ_SW96ZK8ITferVvmioj3pOd9uHfTiWlFHgWnRWiA-3scxbinaoFM1OrpAncQUxkeumjBBtcQ9pG04Y8citYmpBlxsNMJuuvFifPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hXVLhMKAKXyV5g-izkJF6qn7zG4fsRvBopwIFTMyqaLciR_enlSv2zHdmsheyoBuWrfPVqoCr2W-a2xp6sBbyQ9aB-mEl_Vx4Dt3u1dAg1eWtgvVmuBm0_wXcDJlOonu-3uZSZx8TqDNLc4IbZlnHE7L99an_olSnXJaGm7_nqwLcX_SA9PedCdhJnUiGBVGBo32hjV_KSeW3hzie-NpNGLiWHBvQsliHxkT0qRs00AxNx5mQ_SW96ZK8ITferVvmioj3pOd9uHfTiWlFHgWnRWiA-3scxbinaoFM1OrpAncQUxkeumjBBtcQ9pG04Y8citYmpBlxsNMJuuvFifPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=PmekmtM0Gtsgvqwwu1k0SCmW63IaScKYLZi7BV1wEILZqK-5UK-dED8BKWYOo-OsdbK_c5ihJexurjbBVkhfHqHeEC19WQ0_5GVneJQZUw8Y-NnXeJTngfb_vMU6A7aU0fBUmgFP8QWL6WjnxF1rHHtdbltrBJ5FA11wSSMuSWiZKyEKHJvkSegI2VE7p2dYxBFytVS4gle40ywft8ir20ZDrFtdt-Pn5FjuzyM48vBNnuls2osKMiZbcRccadnjWHKthkmMVmUeQBxxSrMvfqLf7GDiDjn_k226KjQoijCAyMS0GXMKyxs_xgp_4_SxQwdhbEmXVRwo-2WjCZNaCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=PmekmtM0Gtsgvqwwu1k0SCmW63IaScKYLZi7BV1wEILZqK-5UK-dED8BKWYOo-OsdbK_c5ihJexurjbBVkhfHqHeEC19WQ0_5GVneJQZUw8Y-NnXeJTngfb_vMU6A7aU0fBUmgFP8QWL6WjnxF1rHHtdbltrBJ5FA11wSSMuSWiZKyEKHJvkSegI2VE7p2dYxBFytVS4gle40ywft8ir20ZDrFtdt-Pn5FjuzyM48vBNnuls2osKMiZbcRccadnjWHKthkmMVmUeQBxxSrMvfqLf7GDiDjn_k226KjQoijCAyMS0GXMKyxs_xgp_4_SxQwdhbEmXVRwo-2WjCZNaCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=mwQeOkLoji4_XGt4dElFRDOu2bUaeL0cDJfVxw4TILBCJrrW6FN31StgMzmddE6Ob0vchBw5RP0hEQ04VEn6pKEN95ZV1M44wIWgYSl4YBaSIs6kKvd4YWdqguPbUROpvMJHZpXKd6mC5lFkrPKtYN5BzXDUTG4YlFkxB9yYgeLF4W6dTtZpfttlwE9qE8I8EMgwa6WoyHkiDzwhDP-y3Vx-uz8By6QK6l-CiVmliLUt5SrU0sY3_2ioP0Hj43d83MdpwCgJIy0QhpUe-OemlvsICrcNnh6KlfzTK6ZXnOzjMoNHvghVBOo5gfP2PC95ZYjTP_p0CMkXHp1sd5997w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=mwQeOkLoji4_XGt4dElFRDOu2bUaeL0cDJfVxw4TILBCJrrW6FN31StgMzmddE6Ob0vchBw5RP0hEQ04VEn6pKEN95ZV1M44wIWgYSl4YBaSIs6kKvd4YWdqguPbUROpvMJHZpXKd6mC5lFkrPKtYN5BzXDUTG4YlFkxB9yYgeLF4W6dTtZpfttlwE9qE8I8EMgwa6WoyHkiDzwhDP-y3Vx-uz8By6QK6l-CiVmliLUt5SrU0sY3_2ioP0Hj43d83MdpwCgJIy0QhpUe-OemlvsICrcNnh6KlfzTK6ZXnOzjMoNHvghVBOo5gfP2PC95ZYjTP_p0CMkXHp1sd5997w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=OVpnxy6-CwlpdjUuwYXpEPH5L_ecRp5pkbMGgmPfJc3bz5AaVqBW1Okvs7kcnmFSgMpEyL_ukNSVl3wTfV-ROXVRFXfa2YB8Ke-r-kSoZ7E_R58ByGZ_B4BYP2Zi8mwYm9eHB-N1eBaiFX_0UmLZ4rOUCB0-fHMOBewju-nXM-Kre4xumRCwrA_7jxuNHpKPIqYL31FLlTpD_09YDauDxDomQcJDDHXKHh3Hzo7lgD95DwTUi89_mOWe_1H2kYTLyJSBGLcB9XC2FoGzsLRSrWpU5Vd7jNI1VchC24u7ZnClPfuF7t8cI2o3ToDVwAt0KRCF8Wtz5tuYcr1QFx-wDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=OVpnxy6-CwlpdjUuwYXpEPH5L_ecRp5pkbMGgmPfJc3bz5AaVqBW1Okvs7kcnmFSgMpEyL_ukNSVl3wTfV-ROXVRFXfa2YB8Ke-r-kSoZ7E_R58ByGZ_B4BYP2Zi8mwYm9eHB-N1eBaiFX_0UmLZ4rOUCB0-fHMOBewju-nXM-Kre4xumRCwrA_7jxuNHpKPIqYL31FLlTpD_09YDauDxDomQcJDDHXKHh3Hzo7lgD95DwTUi89_mOWe_1H2kYTLyJSBGLcB9XC2FoGzsLRSrWpU5Vd7jNI1VchC24u7ZnClPfuF7t8cI2o3ToDVwAt0KRCF8Wtz5tuYcr1QFx-wDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syev0Yd0fSShz7EdxCf8FLrtvfGam8_cHQQoOlOZg6jcPHF28x1B7Fu4gfOTYQlLNIprgXFavF4Rb18mPqnU2jwNq9mJkHsTXnGoDSRSeBSylGht-PAlmovg4EaLbYj8tZrfOcI0WysSF0YYLmAOUMaAzD9cHUUKSF327awt50t6GYWmDz4GYiYY1JnuCcKpvXjoHL6jNVvGOzH7mQebrRqzpYj996rBiVUvuKui_wKsI5FzD5foIwdsf8fZ3Auhyp3L6dm1dm0Aacb6jIJGqdDSFqSolRR-oDZ5FxqAjNW9HlYvqfoNsPUTS014QNPY1j_PgWnyksz_Fxoc7ocLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=tKs-XWNenRvdhC3k9rYUkjN4eI9RMNVSrx99q5220z_z0fLI9Ar1EKEKiiIgDpu9vt2T4Qs3BXgjz67lm6tk-OFwvlgpVSMmQIQvptpq03YDT9Q3dX1m_Hiu6ZbBOYc1-bcMpuz_2SjpdP-56vlpdC5zLDo81ZoIf4ASfdwYCawMilB5JBRqFTjxeusysHGA_yZCXVQZSAUIAwAdIHb6KxKViy8xd7dsjo8vAainoYc5UrMMzNcWa1lU5sShjc398VO4mdy8_Z1p7BfS1SU9YJW6jqARsOAlGIiBNtk4cI718LLviAv5eh2lSj0y6F1Wd4Zfm3NgXm8mgAzp8l9ZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=tKs-XWNenRvdhC3k9rYUkjN4eI9RMNVSrx99q5220z_z0fLI9Ar1EKEKiiIgDpu9vt2T4Qs3BXgjz67lm6tk-OFwvlgpVSMmQIQvptpq03YDT9Q3dX1m_Hiu6ZbBOYc1-bcMpuz_2SjpdP-56vlpdC5zLDo81ZoIf4ASfdwYCawMilB5JBRqFTjxeusysHGA_yZCXVQZSAUIAwAdIHb6KxKViy8xd7dsjo8vAainoYc5UrMMzNcWa1lU5sShjc398VO4mdy8_Z1p7BfS1SU9YJW6jqARsOAlGIiBNtk4cI718LLviAv5eh2lSj0y6F1Wd4Zfm3NgXm8mgAzp8l9ZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzKHdiY1u6otfgYgisAOrD5FqiCij52kSxpoBefcVCW0MzjtRMsJ59drPbz5vhB8C5DVrS0xoF3yD933SbzPtSbusK4LmfFVNBUMQl-1qzhYkN-KhKo5I4HCdUAm3-SPuwdzqG8F0avYZygCDm3YXL3E8iy7aDq15S8L30Rmb7CLGuQitRkD7zpQS4IIeynfdCN0yvpMNkgHf6Js-2y7ylb8t2CF3abFrRJkLHuffn3RIx1mJhds_APwtN_2C8ttiwk3PQ_ObD31bczQgasT3m8SuNIGaMCfFg-n4wHqDcG38Vj0yEckc7Sk_jxi8Wa43ARQw_zghjXmBaVDd0ChhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=mCiUn4RP4ZNWi1Tpw51ho7i54gjclT4oVcaHiPBNmVFNdAuiheUyxX8gn-lASwkcFRyV7_rlE_ufNxS1wTlk0ViJlFGCFT_1rCaMczvGl6SJcG9SC3e1hBuv5WwxcNhSJxCBgpzXxnLs1MHCtlQgkdjrXdVXgHMsR882CzSnC-Z5nP1ju3dzPwm4IKTq6VfU0ow9Cg8eXBixca16f8HV3lDAGH2LE7sOX8_eC1ockw5ED2rvVnEU2fj-hJDzc7i_uXuNKKwj-4tz3-Uhj1hqhL7Yy0OXxOu3hg8K29FwjgAzCRcTrYbuWxPlAzHlUKI_yOTNBAAXVRn_gG1f06H8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=mCiUn4RP4ZNWi1Tpw51ho7i54gjclT4oVcaHiPBNmVFNdAuiheUyxX8gn-lASwkcFRyV7_rlE_ufNxS1wTlk0ViJlFGCFT_1rCaMczvGl6SJcG9SC3e1hBuv5WwxcNhSJxCBgpzXxnLs1MHCtlQgkdjrXdVXgHMsR882CzSnC-Z5nP1ju3dzPwm4IKTq6VfU0ow9Cg8eXBixca16f8HV3lDAGH2LE7sOX8_eC1ockw5ED2rvVnEU2fj-hJDzc7i_uXuNKKwj-4tz3-Uhj1hqhL7Yy0OXxOu3hg8K29FwjgAzCRcTrYbuWxPlAzHlUKI_yOTNBAAXVRn_gG1f06H8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN_yQHijUkEfr6UNQ6cD-ZyFpGBWU-29pyYtvhccXovsxyMy17Ke4ioNAxuajHp2wh0hEEGgv0zbQehr6F-n7ell2QFXkJ2PuB_nod431_arrZOmp3qBbDVvV2qVsVQvb2zpM672_NpZUDcXLK_sqBEwoERAYsh940r31IG_qvRc1_vSPt-lYMq2Q0HA_XM0wq_BtFhraOGZr6sGodHhq6XmBeMEjSyorrGam_B5nRXpa0X0a94RyZF6oJj3Y-6OTlW5bfy-tpBZkV350HQJ8R3Rn8tuzhYVa8n6fj0mG3a39RTywuLxKmTxVfRsE-Y_LthN_5C_QyvJXHK9IQYcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPjtVtlwYWZXfLR0X5rPBCwxKywoeZJcoa83k5JMHSEdFAkS8SRsFAHBAETGl4xPUDc2ff8ydSSULPuKQisLj2kqbCp4qw7FBAlSzG0YZyLJPhNkO8c6SkgcVX2Snx_71JsBI9Zyd79VMrtaQTghdDRah84iWLhnAhayeWYqrEImWZ5dOJLQK2Mvdhzau8WVHyZIzo58VkIzLKIOnH6Zd41rzhxVhrRio4RUIotKEnDYCQIZT5vDaMcPqqAXgvJwImz4fmfCx39Woc2BnPB5R0XsE4vvh08Mmo0K8XdthDebudHIO74PdYuAFUckIDgR2Kffzadk85c5GQ12xsylKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFR4qePpFS3hY08A6wtxYX793-9C1l-GxMjKeMdJi_UX01JtDfzVpUIYY3W1JB83G_S6NuMDcppZcawQ00Gw-rirxP07unA-N5TesNnbD8Y0pd2sG6nqRWu4x8Kqnv4SZySXJrnXfOr-0nDpBm4SZ7hxUXN9vC6CQxdnbfaPIyMYjASHrKFLuIvdSp_CrRIeb4c5jsVdrXg5QXCll8CTYcIM-_AKHZGsAE-xfCM2RTkj2ECvMMyNd-Z99hMNajHhDumOtnh_5grhFXRLkMmQQw1rrY-O1uwceo43HrIg4l3GufotGE3pfEsaVko_jLsYN78C_w7ppMF6ZMqHVMUZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7vd5VNmzgNtDlsPiHSrnt5xZ2asI6f8_12GCxHMLSTu5aMG4PiXnkvg4sAbVUzmO6zBhcSG0zTSLaJIXT382LS1wsfEG5ANg37_Rm9Zl7TSWkNwiTaSM0Dj_RD3mDlPyu1L4WJo9EdTVhD4CpgvciZrgr8WBAgmHAIqsqPP9lEUHqzQXQJqcrdPSe-zj9UtDszQYJkU7tTdkPGhjUU7gWosNYjTb70Ig3YJ6K1KM7P9BPSuA3Gg6_GlfD5H8qEQ9oXbhk5sBY-SmxNUmeFwGUm6JttVFJilMurUJ3UjrmrZI1PVC7LabTYSHiFCFJq837muNrmBif5CATDVE9bkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=Ir3hLOpDmHxh9wUlOHlzmXgm-0iCC6JHC28ExgZULvSeFHdXqbUWpLfvOK3zsVpqoMCKymnO20chu1urB_rSYFdRCf7u3QHLPmCVFpTFaRcVqHIfckjcXUBMJzKn44h3yk5tNrY27YK7dwiAZQ1Saq5ZXhW3bvCu2eIMopjTp_oCpcqb1YmfLu4udOgA8M1eIocxeLwHlxZhL09eyO200NeGsBEXrrgup-N-9Om1T-jwoeck3ok9p1L-KYB03lD196iBKgWFND1_4p4diqPNeW7-DRSlYkaPGv9zoKazZ4qdNr2rKrQu-8hhyEga_Suxn6pNLiACwoKxc7UYJPt1pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=Ir3hLOpDmHxh9wUlOHlzmXgm-0iCC6JHC28ExgZULvSeFHdXqbUWpLfvOK3zsVpqoMCKymnO20chu1urB_rSYFdRCf7u3QHLPmCVFpTFaRcVqHIfckjcXUBMJzKn44h3yk5tNrY27YK7dwiAZQ1Saq5ZXhW3bvCu2eIMopjTp_oCpcqb1YmfLu4udOgA8M1eIocxeLwHlxZhL09eyO200NeGsBEXrrgup-N-9Om1T-jwoeck3ok9p1L-KYB03lD196iBKgWFND1_4p4diqPNeW7-DRSlYkaPGv9zoKazZ4qdNr2rKrQu-8hhyEga_Suxn6pNLiACwoKxc7UYJPt1pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=LKflitiVKNL85aH1X0WLSZ4jqA7tN8AJFJer2-dQb3dAuNBdhvpNv9qBYIUq5Dp-apPfK5u179enGSNpnkqpy7dlEZihXwxTFoGd7ZnKMg7nL4vgjMynmCwlJQo68Ho6bgPwfBvyiXlr7cxvyb72gVE2794SrRYGKdKSxTFR5zjObRVI5pZsLTZbPnz8G9daC4aUEfezkDumAjoK1AqkUjsDviRjikX8J2H0zEi0NSPL41Nhc4KVX256-Wlw-a9GXRHqSBsioEvsHOteLBfSoGgRTl76kNum6AlQGf5Ynb9WKkaFWchRm9e90XGyW7wF9Puu_R9tYY7HhuxRnE716w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=LKflitiVKNL85aH1X0WLSZ4jqA7tN8AJFJer2-dQb3dAuNBdhvpNv9qBYIUq5Dp-apPfK5u179enGSNpnkqpy7dlEZihXwxTFoGd7ZnKMg7nL4vgjMynmCwlJQo68Ho6bgPwfBvyiXlr7cxvyb72gVE2794SrRYGKdKSxTFR5zjObRVI5pZsLTZbPnz8G9daC4aUEfezkDumAjoK1AqkUjsDviRjikX8J2H0zEi0NSPL41Nhc4KVX256-Wlw-a9GXRHqSBsioEvsHOteLBfSoGgRTl76kNum6AlQGf5Ynb9WKkaFWchRm9e90XGyW7wF9Puu_R9tYY7HhuxRnE716w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqYen12qLlBGH9atrCqA8XZZ11CVBbU4sAGXPrfcIOqxMhgog9VMamHNTwbXqolJJ5aXlsqe_sqT9SA-d1PXL0d9xOaEibJoI4ga1b7bFf_LaFub4AHGC2Ikad9MtjlkQXDGGC2wqSEFUB4JANNZ8coWUZ5VD8do-eG3CUHJ-SxY5djae94NmugM8MIxcfyVT-keigIkAwjOGxNvZ5VSG0H6LENzO9LDoJyZRV8xWthI8nPvDvtFXi710zYT_arpnnqKhijDgmylVVgafMcWc6ab1crNFPE0qG1MY5yvB5sK57YSvvg3amkTHhd-kfGZbbdzsd_5VWj8kBPklv7Wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEcoJOgLQw0tsKN1F-6xOAk1uvfXc5B5OvgArSTHX1bj1YwlfE2ZW3nGisQtOBGJThAdVDku2R70j1-vsVMJDN6P4j4SucPSd-74P86RHYnbiwPbr0jCvFx_aHfdeh2f3aSSVMzMIjij84Kh_0-RQLw6stiZz_axiFAd7rGmcJV1HChIDcd3_jtwUCNQL2qnZC23DF5-t5kmReEVtybdPB9TYr6Cjc0YJ4lgwF41P2j9o1w_jxludZhh0ZLOgzf3xbNX4GL-jjOreOW4jsYJucBm4ekH32nsLRpX-vgNmDYPEPXyLHYyUBAHlfJacU8cimojZZ_T39_55oq9m97-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=mSZzU_MK3rTBXLjgUhyfYqWsntJ_BylLCZGvMT-SskZNY2P8tx_IjXxsa3wjQvXKRJwS8Vxmswj1UMYx2-0N7pBJ1HL-Qc6d4t5XPOmSES-KQXkuKI_eNf_OTh0ALLdfC0U26BSIg6ZTPyO6AiIuWMb9SpgyiZwqx6UmSaWYWsA1zDT3ckIyz0OV3QqzOgJ8FLJKlP7xUEv-aXAeB4MaVzhvQoRD5oRB9X1jhcEGUndL2dNxv1x3PxocX3LVmwK0u_j2fnpAb5SDVLMZAjFeY8dUPKoR7VKuaydKHxwhHTWkmAkxGv_tW060f9On9sz3mt_g7udc7qZDHrofx1G3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=mSZzU_MK3rTBXLjgUhyfYqWsntJ_BylLCZGvMT-SskZNY2P8tx_IjXxsa3wjQvXKRJwS8Vxmswj1UMYx2-0N7pBJ1HL-Qc6d4t5XPOmSES-KQXkuKI_eNf_OTh0ALLdfC0U26BSIg6ZTPyO6AiIuWMb9SpgyiZwqx6UmSaWYWsA1zDT3ckIyz0OV3QqzOgJ8FLJKlP7xUEv-aXAeB4MaVzhvQoRD5oRB9X1jhcEGUndL2dNxv1x3PxocX3LVmwK0u_j2fnpAb5SDVLMZAjFeY8dUPKoR7VKuaydKHxwhHTWkmAkxGv_tW060f9On9sz3mt_g7udc7qZDHrofx1G3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=mctWAdDK8_kl6bF9fjCFIVdd9GhessShNzEvyuKXruojEdnCPT72aUHwYww_gF9JVGVO25K3nnTd87Y-LTS3BZDbDg4cuVNk20wnOhgotkBMft0qmhpBoqt1pfkHtHj8C-EwSgfKV7r8QPYIK_aaiX-clWjzhwgrTNzzVlc5vTRc6ROZV0TDrKD77VjXOMSvVnkzYqWT6SDNBnPGwktrOHa5_rmNJI51C02vSV1B6EuUBZGx5fHP6s7Nkn4IhcFAM4xKXJI7ZNXzL58u8GkZifUC1HNexyizTVQkw-RHk8OHzthh1BWOGLY2fjtUspLOB0nWW5QtxCYF_VF0-h1jow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=mctWAdDK8_kl6bF9fjCFIVdd9GhessShNzEvyuKXruojEdnCPT72aUHwYww_gF9JVGVO25K3nnTd87Y-LTS3BZDbDg4cuVNk20wnOhgotkBMft0qmhpBoqt1pfkHtHj8C-EwSgfKV7r8QPYIK_aaiX-clWjzhwgrTNzzVlc5vTRc6ROZV0TDrKD77VjXOMSvVnkzYqWT6SDNBnPGwktrOHa5_rmNJI51C02vSV1B6EuUBZGx5fHP6s7Nkn4IhcFAM4xKXJI7ZNXzL58u8GkZifUC1HNexyizTVQkw-RHk8OHzthh1BWOGLY2fjtUspLOB0nWW5QtxCYF_VF0-h1jow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qwFTT0EZUzJ26G6tIfjH017HGBEthBeyZY-5g1YouqF_j-V2YvRlR8uxnbcO05WbwuEg2wiMzlYMCgYn824F9wIiZ6gNAtHFxUSV4PRmI7cnDYZm5wH6TysA3FMx3_xggxzjWM39_eYUKkaEr5tIzh8LiR4mp-Px1OZx9pJSOv_pZGd-RhRL0Wd-3P9hFm1Z2gyNdL1Ch98VV_ZMxSP4eAcJtHO-CHS5ylF7boOEh9z5vuMdHpn9UEhQmNOPMhB8SyyS9emIWN0EWZ6Sgq2uQnYwHFpSWoKnvB5XBlxe8shMRZU5nmWGTUMigwH3YFK8wIG9-dfQX6Xj1-WUMriYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qwFTT0EZUzJ26G6tIfjH017HGBEthBeyZY-5g1YouqF_j-V2YvRlR8uxnbcO05WbwuEg2wiMzlYMCgYn824F9wIiZ6gNAtHFxUSV4PRmI7cnDYZm5wH6TysA3FMx3_xggxzjWM39_eYUKkaEr5tIzh8LiR4mp-Px1OZx9pJSOv_pZGd-RhRL0Wd-3P9hFm1Z2gyNdL1Ch98VV_ZMxSP4eAcJtHO-CHS5ylF7boOEh9z5vuMdHpn9UEhQmNOPMhB8SyyS9emIWN0EWZ6Sgq2uQnYwHFpSWoKnvB5XBlxe8shMRZU5nmWGTUMigwH3YFK8wIG9-dfQX6Xj1-WUMriYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=XYkADJtxqrkt5qHQRZBlc_IRizG_thHCHOBSc7wMtgP33UAjX2h4yXQ9iHIibNX6m8x-hyRvhktI7Ef4VLnkOxh5oEu7lND54kB3SxcpDkAj6IGkSS6O11ZYx1v6nfRiG1GEwq44TPVofxZfldhUo3614iEPgtFRbe6dNR00snsEKmeBU4bZAMlQ2yx3GWn8LJ51OiKIDI-0IsnHxkpz-BlJyD-9o799C6T34XrwH18NpKUVVdWl0ZBQWoZ0QgWhUCJUmHqAUTqMT3ScB7JQumcpNTs5sATOQUiRpF-wp2uL8l_fPIYNw4ICSZ-s0JJaRw3Zag7nG5CYjJyiy7_mdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=XYkADJtxqrkt5qHQRZBlc_IRizG_thHCHOBSc7wMtgP33UAjX2h4yXQ9iHIibNX6m8x-hyRvhktI7Ef4VLnkOxh5oEu7lND54kB3SxcpDkAj6IGkSS6O11ZYx1v6nfRiG1GEwq44TPVofxZfldhUo3614iEPgtFRbe6dNR00snsEKmeBU4bZAMlQ2yx3GWn8LJ51OiKIDI-0IsnHxkpz-BlJyD-9o799C6T34XrwH18NpKUVVdWl0ZBQWoZ0QgWhUCJUmHqAUTqMT3ScB7JQumcpNTs5sATOQUiRpF-wp2uL8l_fPIYNw4ICSZ-s0JJaRw3Zag7nG5CYjJyiy7_mdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=Rbbamn7v6b4ZLCn1-SniLrGtzROtigQcxNIFAlIOwDdbrmUKB0iZDePFEdqVxsc8-HhEgN_T58cpXxirfM0-XvImvreeKkfNv56_UjZA_WunYcqrqW0XbRcaUJMJ93tsxv2x7toFGarcxVM8IjQqmb3hON1sMKn7XHyBTSF0pHeWFOU3XMIPY0pY1D8pE8Jv2Mz1rSdS5__n7KlAmpq5zW1sKV6BVxKNHPVy61lqtWH81BtBFBL2uUIn6-RFCtFPmflIKJYvf42heYfT6FP8wGrchmqMXLaOaVyl34YCXbr8MtffWohhdhTgJ8cAroAB4XT6G5TB3jQPYg-81zW01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=Rbbamn7v6b4ZLCn1-SniLrGtzROtigQcxNIFAlIOwDdbrmUKB0iZDePFEdqVxsc8-HhEgN_T58cpXxirfM0-XvImvreeKkfNv56_UjZA_WunYcqrqW0XbRcaUJMJ93tsxv2x7toFGarcxVM8IjQqmb3hON1sMKn7XHyBTSF0pHeWFOU3XMIPY0pY1D8pE8Jv2Mz1rSdS5__n7KlAmpq5zW1sKV6BVxKNHPVy61lqtWH81BtBFBL2uUIn6-RFCtFPmflIKJYvf42heYfT6FP8wGrchmqMXLaOaVyl34YCXbr8MtffWohhdhTgJ8cAroAB4XT6G5TB3jQPYg-81zW01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=LshBvwytX_5nINLHE9WB3EeWsMNos7N4ztmEmr_L0y7b_WX2kbNMvDinRR_B-vhCXRUztZFwDzLVbdl1T5V05VwibGPc1L_cr4VB77wwmv8QHbNSRXT_YOxm1QGSB5ANPZzMrGmnjf-NTJsaBaK_IGmVtiibXTtisEzxnTpyremesTVC-etZdMFK1ea-5idPoPPZVOkdnl94KFT-pkaNtYjFWjNrAwX_Vafg2aATqWspTYgLcrW7chPF8oW-Pyc9h1f2g3BIrF5bQ5sXQ-P57mwPuH5LwXCiRPHBtZxZXHsK9nULXsbAdsI1tcRJVrZnlJxgm0W9IrntJ4WbCjWprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=LshBvwytX_5nINLHE9WB3EeWsMNos7N4ztmEmr_L0y7b_WX2kbNMvDinRR_B-vhCXRUztZFwDzLVbdl1T5V05VwibGPc1L_cr4VB77wwmv8QHbNSRXT_YOxm1QGSB5ANPZzMrGmnjf-NTJsaBaK_IGmVtiibXTtisEzxnTpyremesTVC-etZdMFK1ea-5idPoPPZVOkdnl94KFT-pkaNtYjFWjNrAwX_Vafg2aATqWspTYgLcrW7chPF8oW-Pyc9h1f2g3BIrF5bQ5sXQ-P57mwPuH5LwXCiRPHBtZxZXHsK9nULXsbAdsI1tcRJVrZnlJxgm0W9IrntJ4WbCjWprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjajo9h0h5baaz01sn9Hl-h8epFPr7STgeq5fLJ0ju1BgJqdTfwf0GuRA4nEXPeR0rOIp27zHrhOi2_oXptv_7YY8xmqTD6RgSMfJAhub-BQ9_xToHaF3zU50ULq4TIA4nKLVkiMnKsXBDzSFZe9kH4VODCnPrjaXha5kWzNkNnS-xFGO6XtKFWmonedF_kLKEmYhxRFUKk2TQWyYEms8fWlDnuXAZxvN_NieS29xlzVJL5toxA4MJQOSQ9bzHR1-3Ml-YQ3LB_HRqRZ5mVU3wHy4IkanJmDvjIoH6SarVF-tqt5uA10vwQtzB4YRyIA30iyRkKoaSIIZZZkjnM-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drxquaP6HQVLzQPmsTdaKbSemnrGA5sgFhkyATpEq8W0gKNseAel5vuiZoZjCHcYRnhzwkkTBHDHDU_wjuzZXoBQNE12kPFNX26Q5NsItIoPb-gYymLcW1lgf6DWnKcpLPmvH0TRoB236-G0ht-Luqc10ORc4tWwIN18ftb_fMdXnPakl5COkZ1MlCss3q1e3dufRSldZA30ZGrZRhqm-D0cXoNKbOHOieKOkj5QsKqJ_nDn97mSco09kn8tgvfMrMip4sCVL52OR5kV6s0mnamlb6X8tewLni57LQJjDSK3FwtoPjhWnBe7YX9yzjd0XaqTLWCVV_Yx3ZquYXLzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v84G0TVdXYm2bc0jgs2pFM2aOSjyh1OWxakwbeof-7zr7uM8BNjPoe6kI_qkmTs03qFLLFnwui4ScT92-wkuvx0ToaWsHY4V3Cwqbi7-fiDjlGZijlPTmJRWiGAMrkMD0M5esXg51Ow75Mi8t-OLbI2cIG90tj-fKyEmotx-1YJX4VJlBN6DLg7NIaaI7U6AB_NN5_At0xZRK6GtACBnh6kLPbp7J8i9dqZmmFQRSS8fq_OpAEw75nDsSgk8HYcWmfKjs70k6P-Q18eL3DIeoxCNRO1IPILuIXfo6N2HzB6rvG6cskId2R8knvPuFYp_VmfqySDSDXmGjiwd9As1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Duxtsi597ZCsLZiIKHB8xguJPB-6w-IUlzFgkgrjWWQJOe7kcyWfHY-nUZ2zlvwhXhHcIHZ16f_7cEU19uG5RYDawt-LMc9Lsb3qI5gyDU3AP3CMMPwGzcrfGuW8QQshW1nhkqGM8olKF7wt4rKI6AgkMvm7Crh2iH89Z5V33EFt_X-obkXYtt53ZiigPKzWQe33UERWcSfXob0jkp6bg6KhcC5azypss3TfzyfhyDctUo9rVO_9hfmmUQVHPFpOClOuIDiTR4O52JJUdCjj_g9l0keGdbcXO2b5O8n8dACKM_v3_iFeBEYLVEUS4h10o5Lp2EMttNdl70ZEeIwfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Duxtsi597ZCsLZiIKHB8xguJPB-6w-IUlzFgkgrjWWQJOe7kcyWfHY-nUZ2zlvwhXhHcIHZ16f_7cEU19uG5RYDawt-LMc9Lsb3qI5gyDU3AP3CMMPwGzcrfGuW8QQshW1nhkqGM8olKF7wt4rKI6AgkMvm7Crh2iH89Z5V33EFt_X-obkXYtt53ZiigPKzWQe33UERWcSfXob0jkp6bg6KhcC5azypss3TfzyfhyDctUo9rVO_9hfmmUQVHPFpOClOuIDiTR4O52JJUdCjj_g9l0keGdbcXO2b5O8n8dACKM_v3_iFeBEYLVEUS4h10o5Lp2EMttNdl70ZEeIwfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-qiBUfDcFxoUBdK8LjQ_YU-yo8frpBuRaYJ4yWBNn4m8zzdBxxzS2XaDLHq5sYdt8otAVKl521zTjt0HdekOnVOLbCU_lgn5Q2D2cEioSuRL6A7tqiyjvpZ2KAA_MKrmIldmDCG3odZ2M0v4IfEBljmkgdcMpwYLN4E9VYzqlUlbhJKVb8ryVgLUCUGIPxiZynJm-NQOehe_YVxmas9QC-0air9rp1mZeuoiSQ_1zstE5cVYUUy9CB-WoRy9aCILIimEWfS8Fly0lKkQWH2_a5BVjkAb8BpC0f-fjcjUS-EoGZRi4RQtpenvQY3v63aF0vHrXgMyltNlRwAQmCF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=iEcECOwsquHfBWVDduXMFWxBt2ZFZlVyzilae0RzU1QBRzEy-8oB0zJc8O8L1ulhc3cbbIxUcAQjtbDw8bUySP_58K-cRfE23Cgn7Y5wJvi0GCVXhNge5Bn29ygdbuTwFvptgl9MAIOsP8wcCUEeLnjTRcs0Z6xlE_7FQmHuD2OwrXH-Fq4WyPdKEM82g0NjgbET_PmaOgsZFVu6DGnC3OZu05ph6pp9PBLFuidwKsWTXy0SbUinVBxnf3xV_6jiAbqwcCpEGoNlx0_O6rUk4GnTCguraIvvn3vwRqYuUOxoxu9MqFwvfDhrYPnWX_iKlzyAaSMxfq5enkHX6-jQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=iEcECOwsquHfBWVDduXMFWxBt2ZFZlVyzilae0RzU1QBRzEy-8oB0zJc8O8L1ulhc3cbbIxUcAQjtbDw8bUySP_58K-cRfE23Cgn7Y5wJvi0GCVXhNge5Bn29ygdbuTwFvptgl9MAIOsP8wcCUEeLnjTRcs0Z6xlE_7FQmHuD2OwrXH-Fq4WyPdKEM82g0NjgbET_PmaOgsZFVu6DGnC3OZu05ph6pp9PBLFuidwKsWTXy0SbUinVBxnf3xV_6jiAbqwcCpEGoNlx0_O6rUk4GnTCguraIvvn3vwRqYuUOxoxu9MqFwvfDhrYPnWX_iKlzyAaSMxfq5enkHX6-jQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ed12w3giL1pF3VF4wyNs3CpFMiaKqS1MDl09GoFdgOiyZMV2k8-KTWin62VL1dk8d6YHnoOH77loJh5SWNG7iouoz10aFf14SAFyhzqTXw7znGIZgxhwwhCeI8jf7FqdukyMgdABGP7kDe_80p1w9570AZeDfo46KwcDznp1ZwGzjK0IyK4Na4qtkGvVm11rBJAF4owVVjF_D_vN-kwLON3ZIuKxEta-lwhVQ-2O2n_js-mkwvjmt76009IF5xSaaQf78MoJ1Z8eE9Yx16LpWvoEjAuieH38_XvHNXnTk8sCRVFSGteEI-KJJ-sJOuKbYhRHMi1c4YBMhp8TqlTDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=dDhv7I_b6xZA-vWSfLpfn24g3-XzFfCtFpC6-Af6CrM12G0iRWFNo9RgS9PjSp7wWPWY8vlPqowhxyJRgxKfIoybtMed8_eIbF0T2UV62CS1BMfxicYAqqFZ-ZOEbBVEwJfNDWgjPuRV0nnpBwMdlsox-yssGTuEk0KA5sjR_FH_Z_tbMlaxzjmVgTW8XUnOf8lJv3KK3CLT1WjdJOXDevyoFMpUAQ-z89qXFMsoZbvG5ATyQ9E1n-amvTTJfEZBiAlTt5Vhfo9vJSgDNonhNEhXPwXCgxFDUFCkBd6Yb8vjJom16FsANd22pmZ2XKz8rKQS3UEdx0hPTzhWC6Bd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=dDhv7I_b6xZA-vWSfLpfn24g3-XzFfCtFpC6-Af6CrM12G0iRWFNo9RgS9PjSp7wWPWY8vlPqowhxyJRgxKfIoybtMed8_eIbF0T2UV62CS1BMfxicYAqqFZ-ZOEbBVEwJfNDWgjPuRV0nnpBwMdlsox-yssGTuEk0KA5sjR_FH_Z_tbMlaxzjmVgTW8XUnOf8lJv3KK3CLT1WjdJOXDevyoFMpUAQ-z89qXFMsoZbvG5ATyQ9E1n-amvTTJfEZBiAlTt5Vhfo9vJSgDNonhNEhXPwXCgxFDUFCkBd6Yb8vjJom16FsANd22pmZ2XKz8rKQS3UEdx0hPTzhWC6Bd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SESM99qkTNtN6VI1M1xfFQiXflllPz57UB6EhJOg2-yeP6hWGlucT35WrFdcAtKFwHV2Lyt3W4exX9rO0KNeMDAf05P6IlHrOZLnqxjpka8EyklcbbhB9zdKRNw2mfpk10qK6FAdR18HkX1G2Z_Q27YzFa3C1GrDDKsJtburShr-oybKfK1ghifLlgPKLA9_yaugWK71rRyvunMAIuA7DA_sCxrtcy5KTnxKA-_8RoME_v_Ddh1r3j1Ez_8l87M92WKXF9zAFsHVq-v_p8bK-_Na7d7HDrw91V2orFKBVeSJwvEzItwUdtjjqlL6q8UH2jCCGQsQFvOka2wenVa2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=Rks7QDH0gJ5LM1H-fjdDqUu2F3ZBrXWVGN_HCPmyHP1eVev6ooR62UKfuZ-VCkj-_0aQArJbaewAgV3Hw3LMK9k9oWumOfZKxiAOhsk8lMUH1av8GxofIvkz43T58C1B1dUZbZmdVSrS0HmfPQjbCTYXEDutnG6jEBo97KjGlREJVGyJ-wVZUFBfuK99yA6IfNXlcTQrIhadNCf4EUgL21K8Ll7939pYcs68V-ENQXU6p1Qs2M06Lb9cTe-wwPwbEsNWATK3GrsZt6etqxdCsHW53JlRTOAiAu6bQpWfeLqyTG57llDWZUCYQnrhjt6prOBWSF99ApaQ1Q6K-dCenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=Rks7QDH0gJ5LM1H-fjdDqUu2F3ZBrXWVGN_HCPmyHP1eVev6ooR62UKfuZ-VCkj-_0aQArJbaewAgV3Hw3LMK9k9oWumOfZKxiAOhsk8lMUH1av8GxofIvkz43T58C1B1dUZbZmdVSrS0HmfPQjbCTYXEDutnG6jEBo97KjGlREJVGyJ-wVZUFBfuK99yA6IfNXlcTQrIhadNCf4EUgL21K8Ll7939pYcs68V-ENQXU6p1Qs2M06Lb9cTe-wwPwbEsNWATK3GrsZt6etqxdCsHW53JlRTOAiAu6bQpWfeLqyTG57llDWZUCYQnrhjt6prOBWSF99ApaQ1Q6K-dCenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=EoLs_jiWrhNcGSjVYmX5yVA3WJ1ibWDcmm-9G724XPoyuUpLSVftp0iRbRQNYeH9m_XzBEICAAI8L46Py_GjxkudwBwKeJdyn6mHHJHQiZn3N7-WdBgPv8lIRUQHpo8HIhBzfxOyCTObz8rMFygXEhHzZ_S26YAGNJiWVTjQlDy3O3F2vjs_9blL65yB--qgsJCuzLkus_j35twnECjp2DuwfJU6WKN25CYe13-ndMfWQ6LeLTBUAEn8F9HcCMt8YmShQlLRkWwrIfe_Qe7byz9oRsnBYRPqRW2VDyWqUr4QlfizHjpgB7dPooEZP9UFymufVw7VtFyXz-gqp6tHtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=EoLs_jiWrhNcGSjVYmX5yVA3WJ1ibWDcmm-9G724XPoyuUpLSVftp0iRbRQNYeH9m_XzBEICAAI8L46Py_GjxkudwBwKeJdyn6mHHJHQiZn3N7-WdBgPv8lIRUQHpo8HIhBzfxOyCTObz8rMFygXEhHzZ_S26YAGNJiWVTjQlDy3O3F2vjs_9blL65yB--qgsJCuzLkus_j35twnECjp2DuwfJU6WKN25CYe13-ndMfWQ6LeLTBUAEn8F9HcCMt8YmShQlLRkWwrIfe_Qe7byz9oRsnBYRPqRW2VDyWqUr4QlfizHjpgB7dPooEZP9UFymufVw7VtFyXz-gqp6tHtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auwKg50bAAPUKVpKsd9ja8S2cfKTa2IrO5jK3xqpiqAD93xK3UGu6op9hReC3LVNkuqPjvuDOHaTz0D4jI2Q0vRIOyNzWBzxldyBDrVj9BUHtMQL6fAAqyU7Zf46EYE9SmX0pXZynoJPgKyfiaQpyOtABh_47Ia1Rqs_RUKh-jh2H2Sn3MZ6hhrdH_DvQBW6RjClJXWTX_BJp40OI84-LAkrcu4Ilm5daZQhHqFtYRQtlWwZfHQ51ke3A3zcVtkS73lTXlaZEc7r0SU0zZDBQh51q5DlCd3usDFAHDn-pGfyZ5LR50jTzlNtWL-y-6xiqFRKMwQJsgK8xGed5I6Zog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tm7hxGrdilnGTQCXflCe4IWBifqwqUQabug1QDoC5G3BUFtkKA1sEWlyGr_CcTlKK714BlHDjdC1KHDEXjygTPJsPGY-q7GiwBepIC6VMFZGNzkOvyMk4UB7eu32NpwFU0CAAo_hwunnFQj_3VPt_SrOvtFC7XaTXt89YeJSp8TgaOGrgxEJg4VAT_SJCTBgoXoKlsElBTNiT09Xn3XL5wREMBwo0CXvfA7mAqpg03K1r1xlWEEJOGaMTHNa3ChFGK6vkjSoEdmKqKBK7K1SESzlaEOTtW57t-d56Yzg2io8ZsbfReTBgciGYEPobFUlY-Y29ptLKYc170RdolJueQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxz2Ue57TiMuUEYuSOczwdmpx6RjVHIwOxKwqulRXj1JUkGvJmIEviGyhDVUdu-n3_842t4gVnX07rMxoV5GHhlmqg8moCJfXXsv30peGBSH41cquak_GQeAl-5NjXDlPmJBy-I0Y4HhBTgXT9p45UKGlSYFIo8wkF9iEO8I--meES3kWs6acu9ff9X0DpHSIJUDyA4yUjI3RiudDTFz8sT_Mt9TpVrsfcpBfUvIqqmvyfPN_ZKQaE0G_LjXhiBtl2J2IfAHS_I0gWc5AbsKfCVLJvsbzgQa0qRuJHPrHGE72KOzFwMJkj9TBeUGD_dGoupF4PjEq4Ni6QXqVZeysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=fwDb1KlRy1aMhy1VevRKELuhE3nfNd3gsFio207foOhny1w40XrLPDXpmWo4sVIetN_VTyc-QKiQZmr0Fb23_SjaOYxn_UeGnOq3vUQ0k7GPF4VwwAWm9e1jjlFKXnzvYYNYve7eBXAHSSxZt_3KEzOhz7o0QTSWrGBvku8M3CWjZmOQH7YN0P7rzUicRvl2mF13ibvhngjt614aDdX_YISCYZg8G4XPYyCtAcwlgLAZSXfnBIKz5OdatzUEOJf_qTLvn5CsXNOSCiEmXF4fXjRkx7JFY6YSQQ7lr6_T70c1kWzoY6T6xIw3XznvPRnVU57_pOVru-UkZUjg7kzt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=fwDb1KlRy1aMhy1VevRKELuhE3nfNd3gsFio207foOhny1w40XrLPDXpmWo4sVIetN_VTyc-QKiQZmr0Fb23_SjaOYxn_UeGnOq3vUQ0k7GPF4VwwAWm9e1jjlFKXnzvYYNYve7eBXAHSSxZt_3KEzOhz7o0QTSWrGBvku8M3CWjZmOQH7YN0P7rzUicRvl2mF13ibvhngjt614aDdX_YISCYZg8G4XPYyCtAcwlgLAZSXfnBIKz5OdatzUEOJf_qTLvn5CsXNOSCiEmXF4fXjRkx7JFY6YSQQ7lr6_T70c1kWzoY6T6xIw3XznvPRnVU57_pOVru-UkZUjg7kzt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=F-eX6CsooyHq3fX_Un1mSsGL3m1bmKuHEA8TbU52er8K7P2U6uz7jGfK0ktM0GuvyF0g7Ktk_dV8mXWSNE-gVLsPMrMj6Ut1zx1f9CmJKEoDZuNQnmJxj-L5RJLGy7tqH3oGs8X_MJhGOw2EbpoRI6KnjjP68CvSXbAQcZmoU5exsaP3B2s4kmqr6YrKXTZTM8HK2Nf0PH-eYlXi0NaKtLsqoLpn8KIIJx3BWV1NAeKklr2Rexbu6_NOHC_zsuuKJSetBaTOoxZ9va-X4QmBhjtG64Oz3oTWl8DNRNUInYbIgmEcFiJAURiuW-kgpp55HI8MAR6K7rWg8QVzLp1v4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=F-eX6CsooyHq3fX_Un1mSsGL3m1bmKuHEA8TbU52er8K7P2U6uz7jGfK0ktM0GuvyF0g7Ktk_dV8mXWSNE-gVLsPMrMj6Ut1zx1f9CmJKEoDZuNQnmJxj-L5RJLGy7tqH3oGs8X_MJhGOw2EbpoRI6KnjjP68CvSXbAQcZmoU5exsaP3B2s4kmqr6YrKXTZTM8HK2Nf0PH-eYlXi0NaKtLsqoLpn8KIIJx3BWV1NAeKklr2Rexbu6_NOHC_zsuuKJSetBaTOoxZ9va-X4QmBhjtG64Oz3oTWl8DNRNUInYbIgmEcFiJAURiuW-kgpp55HI8MAR6K7rWg8QVzLp1v4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPW5Keye8gD0NrHQOb-liU703OzY4xLSiDsmdYwqUXhxnkuv-4E2xJEY5y9o-jiX8AP2sN5_G5U61GDTrtvGt_955cUIthg2oQ96ZdhjhkQS3yi_4fJHGBKF9vqam9ScD3Ihtx3yUp-q4zqMHpoCOHORCmEaA_H05xKm6HXtFC9yJ-hRu1QYbArCRLsdPbwod1Ds3yTAPkyAdLcpWjU2xmhPK4GcEPpPeGr9AHAXmSWCMcAD03jeXl_YW4onZy95wQNQ34GSjNUm51ekqQ0W4qmQjWw6UQImjb7Sya1N5-PNseE2SGimsH6z-dIAhwSkT4m78X78qIugCgSUlCIwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou0FSGzrwPb42Aa12dE_UaE6y28Ht_dlSelD03QCEtFwiNv9EsWoyfgEJ4DGruRfmFUypi6JgA6WeQU9PEh1_O754fZRQLwniLD8-wVpiWxurj8PxtCNvuNFuDm0zruqhrt_TchBl8afMZV5qR9kAcvdT55buCX5Z3PN5j_YNkIzj1b4D_x6MoNBq6wfZ3-cBwnhaO86cqlM0Q_uPZlWs-QJ_cAN6W8wdxQEdWTs38HKBegcWZAqPOzdmoXLRt9dh6Xgd6eBrTv1rd7OwUQhU7eZY6VvaMgyCwm0zpw6gDttw4hySPpjBvPLwSfyhANdN717FPPdbSD8Rt6CIWbo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYKHo8eWTzzUvdZmLPtzicvVjqxzYho4A8jbGPjPK8QBRT7BuwhvvPRw1ezYNZr7wCuOLleAHJIxbwNXk2FxrBEMuMjRVFyriW8AHFL_bhzAjYVXjO5AkkzYzyZfy75O2ebM-EtT5NmJkfkE_r9F7Cbr9BXZXSeMz0nA9h60VULTKnCyLgpYVKqOwzNdzs-tMUa1BgcbgGUpACQ_PCxi4dcKiH_OdAFWbM3S-3CMhhqYuu_iT5IzLjDf9nDA3oa8Z6PFznLWA1X_ELvnYT2kvrgf50I_RgRy5zwagD9Fc62KHnhJH_A6S--dasx8V-4cKguDvMOkBeiF9bQ2v-1OCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=TGD50u81EBqRBbYY9URvsdLmdZqUtuBBpcm_WEr5kWQQ24xsCzKtWmPlHCHYQ8-YkAEv-6UGwnpsenJLVGQxaw3ByT0nlGy4Yx-cUAcOfMVirDw4bNs0aYzuMXDSP5t6KVq5UgWxi43m0hKNHQnHaDA4bA8Jb1ctEmQOkn35R-ci_sHsxm4oZEcqzFwLuh8q6MOVW3SQEX1I6N8uuOkosqNIXkVE1O43Q6Pdt3sQKNlQN4UGu-J95-Wq85lTDIJoASvF14aMcl9HrUawTo8JOLwEafcWtbgWuYrcqjywkWqY5zTVzYKN2L1z-H2060RPP7nEnTHhWGMRxBuC-IA4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=TGD50u81EBqRBbYY9URvsdLmdZqUtuBBpcm_WEr5kWQQ24xsCzKtWmPlHCHYQ8-YkAEv-6UGwnpsenJLVGQxaw3ByT0nlGy4Yx-cUAcOfMVirDw4bNs0aYzuMXDSP5t6KVq5UgWxi43m0hKNHQnHaDA4bA8Jb1ctEmQOkn35R-ci_sHsxm4oZEcqzFwLuh8q6MOVW3SQEX1I6N8uuOkosqNIXkVE1O43Q6Pdt3sQKNlQN4UGu-J95-Wq85lTDIJoASvF14aMcl9HrUawTo8JOLwEafcWtbgWuYrcqjywkWqY5zTVzYKN2L1z-H2060RPP7nEnTHhWGMRxBuC-IA4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=OdEXaQ6u2nWgJhtPftHpGcL9agI1npQ1PkA_oxRtnKr_jx-6rqJ3sCCM7o51ADLEyr-Ot5iw860kcVHsy_c2jWaU3u7oaUpUTtifabaqoaSrvFsljVmYChoiyhe1Aus4G_BbpUKngWXFasJfwoBTrj295Sbi75u6ee1UplX38w4taiVximgyN4PBpOeEAqRwhhA1J13_VsDXEHaEQHIq_QvEAbuigiyAfXr8KkU_-fsDgBbl76n26R78LTjSCuHWEoDGhIgAvI9SZFEKy9DngswVEdJ2D94eSmh4JRh4REILMm-44T7LqoHpg8BIJuTrinJMXiP6nnhdotYA6-n6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=OdEXaQ6u2nWgJhtPftHpGcL9agI1npQ1PkA_oxRtnKr_jx-6rqJ3sCCM7o51ADLEyr-Ot5iw860kcVHsy_c2jWaU3u7oaUpUTtifabaqoaSrvFsljVmYChoiyhe1Aus4G_BbpUKngWXFasJfwoBTrj295Sbi75u6ee1UplX38w4taiVximgyN4PBpOeEAqRwhhA1J13_VsDXEHaEQHIq_QvEAbuigiyAfXr8KkU_-fsDgBbl76n26R78LTjSCuHWEoDGhIgAvI9SZFEKy9DngswVEdJ2D94eSmh4JRh4REILMm-44T7LqoHpg8BIJuTrinJMXiP6nnhdotYA6-n6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=eKHl_FoLcWQQoUZXDlp7tfP3tgDBo6AyYTfPROiZw1DMHJTDyeMDgpdPmvfLZpS_hHRNfV0GESRsD0sUDnbxMfBkdslo6RQPy--Vcol2S6XWBPPojppiOE3HkL_6mgaf1bcOVJJT6U5KpoP2-BKGyDXH6-3GrhhGvlzNUqDy5iYOSmIwKqBgEjThVsbTa63uY_kCc5uc7qIt9bs5F7Mox6qCY0y7Z_s0GpdxvuU80r9M7XxKOXR-kpkEFOHxQwllJxXH7MaOfyPrQhhqU2WSvTGT6rPaONaElx1cJJ_wbVSAKcovABQB6BTzvjBnGbpcMLkvs8K3cCAXzVdC9uwyXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=eKHl_FoLcWQQoUZXDlp7tfP3tgDBo6AyYTfPROiZw1DMHJTDyeMDgpdPmvfLZpS_hHRNfV0GESRsD0sUDnbxMfBkdslo6RQPy--Vcol2S6XWBPPojppiOE3HkL_6mgaf1bcOVJJT6U5KpoP2-BKGyDXH6-3GrhhGvlzNUqDy5iYOSmIwKqBgEjThVsbTa63uY_kCc5uc7qIt9bs5F7Mox6qCY0y7Z_s0GpdxvuU80r9M7XxKOXR-kpkEFOHxQwllJxXH7MaOfyPrQhhqU2WSvTGT6rPaONaElx1cJJ_wbVSAKcovABQB6BTzvjBnGbpcMLkvs8K3cCAXzVdC9uwyXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIWP6CeV5zZFnJB7q-8TTdAf-JqhS4iXk5QokafwxgyCaZ2A_E2ToZH_r_S8HIoQqQNBnwGqs-RmsYHyxcC8kgKv4pIlWyLiBewYJgTsofqfucqh5-Si-BnLlszhUKugzQkCgiEkDmPRN7hmU-4pFQjuNid4-u7Qg7TdKHRaugrCiC8aDt2kGF581TYWKVMq4icM1z4YacCyH6kqPCSBVTK54hPEZf8Dwb-7HGcbVQiR4O9IQX0Lte5UwnjmWsTJuXFH1l-GPFpdtvqwwpJVjGfvhBDWiOnfjFYzsb0bbOtLwuFZ8AX2qFGX2fGsVR64Qp0_4qAgxBk2Pb1KpqLv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=FLBdw69p2Ceq-TZycdCqd0QyQMS5A-9QyYN86JjYg_8TDv4H57qRR6G3ZcZrelT9F1CFyosCbyIAFUlSD2f0jseSw9VmIfSyw8GiJznOpnKAyfWIE9DNfIBGlIdQ6_TTug3HEL99PdfiGm77dAakKZCYgRZ3zCYRCjWawU3_Vla2So3hAAwfIg3dVwsdyhH1YyeQgctGaPR6zWA38rKs2EzUgdQnrGcGWqnhmMbDqEoHpDDfvnnEvbcfSCHgOeswqEYJJNTVXZLhzRoYI-p90FMbaA2fIfVPA3q3alwem3gnok8TiLQeIioWZum884RaPIWQ6LITrvlIjVLUJ6meqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=FLBdw69p2Ceq-TZycdCqd0QyQMS5A-9QyYN86JjYg_8TDv4H57qRR6G3ZcZrelT9F1CFyosCbyIAFUlSD2f0jseSw9VmIfSyw8GiJznOpnKAyfWIE9DNfIBGlIdQ6_TTug3HEL99PdfiGm77dAakKZCYgRZ3zCYRCjWawU3_Vla2So3hAAwfIg3dVwsdyhH1YyeQgctGaPR6zWA38rKs2EzUgdQnrGcGWqnhmMbDqEoHpDDfvnnEvbcfSCHgOeswqEYJJNTVXZLhzRoYI-p90FMbaA2fIfVPA3q3alwem3gnok8TiLQeIioWZum884RaPIWQ6LITrvlIjVLUJ6meqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=rAaOPZvupBfb7o_xetuO_rtcBT5tsm3B5CJd1msuf2xWmCkn8hV2Z5pxxlA7u2dc_3cVUV0NbGgeI44o44DWFyDzYKglHxXaBBoebDz68jaINbTg_j-IrIT2k9-bZGq0yE4Bi1lf6pRb1vzc53JOYBF8wtaJwAG1ZYRZYea82R07DlLfwXNTnh4r0gTy9ig0jkA7Auj-OIde_HmJ26v-1xW2Io05iqQjiPzht1SeuNsZCYNv99xIpfCirGGsaGHfWPy1Eb4UJIeXNQM9WK3Tld8R7S4gecin9WTBbI4AhxdHJ3Kz_yuX5zpzaLbwSG3rbIopO0zUGef668sH7Mi2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=rAaOPZvupBfb7o_xetuO_rtcBT5tsm3B5CJd1msuf2xWmCkn8hV2Z5pxxlA7u2dc_3cVUV0NbGgeI44o44DWFyDzYKglHxXaBBoebDz68jaINbTg_j-IrIT2k9-bZGq0yE4Bi1lf6pRb1vzc53JOYBF8wtaJwAG1ZYRZYea82R07DlLfwXNTnh4r0gTy9ig0jkA7Auj-OIde_HmJ26v-1xW2Io05iqQjiPzht1SeuNsZCYNv99xIpfCirGGsaGHfWPy1Eb4UJIeXNQM9WK3Tld8R7S4gecin9WTBbI4AhxdHJ3Kz_yuX5zpzaLbwSG3rbIopO0zUGef668sH7Mi2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Hh5KbU2BTMy5C6x9Wu6y2XwKm_Sqm-yZiM4bpl_DM9t8xy7WOYpJoNUjCt7VqWgu_0CLcCKPzg9f9tajFOqOZLZ2A4cvDd6GQopggU6Edv174Bkxc2SWmLWU3fnv3TjJ_UHVFEkIJv0CHoT3x_bwRH3R4XbnLRCtAQXmRjWOCQUbqgW97ECnYK5290hiM2MjHHIPGvWIoBaklRjYfWq4fOeoBLszuM-YmPEwEFWUHHhvBPUsCPW-CuGacQcNVCocwIqmxu7Qyzx6O74P3YSy21qR87ueqeThINDFQ1k7gM1BUzrowVdQyL6gdQZ2syKrB2Rss3nKlCS_BWXDOgaoow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=Hh5KbU2BTMy5C6x9Wu6y2XwKm_Sqm-yZiM4bpl_DM9t8xy7WOYpJoNUjCt7VqWgu_0CLcCKPzg9f9tajFOqOZLZ2A4cvDd6GQopggU6Edv174Bkxc2SWmLWU3fnv3TjJ_UHVFEkIJv0CHoT3x_bwRH3R4XbnLRCtAQXmRjWOCQUbqgW97ECnYK5290hiM2MjHHIPGvWIoBaklRjYfWq4fOeoBLszuM-YmPEwEFWUHHhvBPUsCPW-CuGacQcNVCocwIqmxu7Qyzx6O74P3YSy21qR87ueqeThINDFQ1k7gM1BUzrowVdQyL6gdQZ2syKrB2Rss3nKlCS_BWXDOgaoow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQZY-SAOuLj0WA4FgdKuieJxvJLIHCV5FrXUEcFkFj-UlKjf80JkmEDhMyxpNMj4hyWif8JpQBk6tRLTwRSBKmDUhv40MXcX8HlzKiSw5S78hG4k1WrryOMb8-KJ43bDRX3QR_PwRc8-1HDQDleY7k2qIOPjzO1C0HYbWtiz20WA7yp3D2FC-6Nd_yso1dneyf9cfBLEl41XKo2_cTtx2WtjBOtd6NEbQty7ZwroTuaP-4IupjA4boDb1XWdTMTS_8F5Sx-xkLzXws-LbAl20ceJqaJq6Yzl_99AFpSAEdmhtKy_UpXD5mwpsqrW8fnbtyUYgsu-C-VAB0LdiP9kug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
