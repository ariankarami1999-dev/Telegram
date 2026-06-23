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
<img src="https://cdn4.telesco.pe/file/qHrhrOlJW0Ab8yBq6dj5CaDMG2WCOrGwMTsCnStIBblnmtpFKlb4tVx5X_UREvm12D95-Qm2Zhr6H_m8XqUi94mW8ffk3ux6fBYWFgISoqq8P01jvOA2zfGfXdTAedF05Yqz6H8vG9fHwlynwFQStGRNGEOwLgyP23uJguvMsCMFjWwqPpXcuGPx4dpaYuFgYcpukv6KBTddlkcFgjnic-GMoes9Q-RQK0FwmYlOUruous5t88J_qQ7r6t5GGunADraZm3m0rFtI31fdTDRAwPB2ABtA7LACC_OPcc-S_fRDESWeQJcMDjZ6jRoI7q_8hQ3ALopkwCMfN6cwqP0u8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=LEJo-047zqMzDz2BgZLury4RijCfD3bOndXhx_e3M2al-sKxdnorTXFch3wnAiC1jCRRJnzeuPLXOhmlgRdVREEgcRHKJlbzoTvCSva0qP9rMHpf6zwAMlZJ6i35GA5acscpS3WgVxrq8hnABEOfiZhAqM3WLaGp1vfN4Q6MT9QfkjEeEJnrBQwVFgMGIeFyCggn46ly6Gm55krHeXHyB9d1TADwVyBQfxLJPkHN56VF4hOIhFkkmx0BSzw6nz7QHE6fR6d6Xl2awBtMJkxnPL4zxhwMHLJfc_AFZBi_PsTBS6m-OHEv57bGV0kB_lUKnWI4mA-a4LDDmAcXnJuB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=LEJo-047zqMzDz2BgZLury4RijCfD3bOndXhx_e3M2al-sKxdnorTXFch3wnAiC1jCRRJnzeuPLXOhmlgRdVREEgcRHKJlbzoTvCSva0qP9rMHpf6zwAMlZJ6i35GA5acscpS3WgVxrq8hnABEOfiZhAqM3WLaGp1vfN4Q6MT9QfkjEeEJnrBQwVFgMGIeFyCggn46ly6Gm55krHeXHyB9d1TADwVyBQfxLJPkHN56VF4hOIhFkkmx0BSzw6nz7QHE6fR6d6Xl2awBtMJkxnPL4zxhwMHLJfc_AFZBi_PsTBS6m-OHEv57bGV0kB_lUKnWI4mA-a4LDDmAcXnJuB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OHWDdal7aTF_owumqZvHRYVKeiJ8P-8Ox6hRcrNdmY3Ceax-eIZfuFPdcabij-hAKBsuEdvPA83oANRcbfhg64bj563XfEBJ7E9B3UB4_MQIEPielSRRZ_0yr-FGUJh19WVfGDRl5sN95khc7Ss4Lrsp2wXsz3ohJj4XnRcMEmv4AAy_yZwXDSbgzf2uuDvJBuMNRHjTTrbVWBlyeKbKyC7kPxV5zs1kqGtwnnoqZllmZWjvqEu25cnDt3ZPfQbwQdOBNRze7EpIJf1TzaoK_a6nuJSRXyfDxOyuLbjw_C3x3tND2H2sM4hJTVnVk04DYbHIf26DL92LdOk5s6DRsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OHWDdal7aTF_owumqZvHRYVKeiJ8P-8Ox6hRcrNdmY3Ceax-eIZfuFPdcabij-hAKBsuEdvPA83oANRcbfhg64bj563XfEBJ7E9B3UB4_MQIEPielSRRZ_0yr-FGUJh19WVfGDRl5sN95khc7Ss4Lrsp2wXsz3ohJj4XnRcMEmv4AAy_yZwXDSbgzf2uuDvJBuMNRHjTTrbVWBlyeKbKyC7kPxV5zs1kqGtwnnoqZllmZWjvqEu25cnDt3ZPfQbwQdOBNRze7EpIJf1TzaoK_a6nuJSRXyfDxOyuLbjw_C3x3tND2H2sM4hJTVnVk04DYbHIf26DL92LdOk5s6DRsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOpzJ5HKaBMIDbWIkXw8bl97g4krXB_J48XlbulvTgFt_tI_8HlP1wUkn8mVfpmp7uGKObP_JwElb4gkfeqam3MIAnd5PlTYuX-m6NC44enz0F7K5BJFHWJ70uaF2-HDRCgjfkmHhJKa2v0ybURWi_1PscfTHJ3uhpBye9wwrSG5T2aooxpgCkfphiNR1CRGIA6zSgzWam3BuKFB7dxh3SEqsKg6hRblkKYs430wGvIKtYUks8FkqpduvG5IVebkaq980yAX1EHMhpYHSdqWQAKw4-mhTJlxwF8Ihe0MWkmMvsPJzqSTNlrHD9zMzFA2hDjRGr4ZwW0_J4mO94pxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=IMKGoOnAnzsjuiTWDmG_pN7JLE9cBcHV4mrFqMmd6MW3jYWmYcjvfu1tWOUZz_K3FNjWlhmxpM-03cc5mTPTVQZ--SVgutaz1QjhJT3eyapPqMHi8cPMsrAfgFZP9XgUyZNFPvMPh_wdibLxfetbE3jC_S0gOtfMc3MBOQIjPxHnXnEnO2qRf--N1BONgP6T3m-rNOHGvHHfrAOvlv9Q-j-WPjBpKxf5WJPM8pZU-kZc43KOMsV6-mptes2iRkJym1u2nEblA7J7hnXs6gR-TyVYGScvREGIP10Et_CzDP9HJIzC5pXZFj9ltPfWF1cmz7EFGQnJzy9Yrcfs4_34xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=IMKGoOnAnzsjuiTWDmG_pN7JLE9cBcHV4mrFqMmd6MW3jYWmYcjvfu1tWOUZz_K3FNjWlhmxpM-03cc5mTPTVQZ--SVgutaz1QjhJT3eyapPqMHi8cPMsrAfgFZP9XgUyZNFPvMPh_wdibLxfetbE3jC_S0gOtfMc3MBOQIjPxHnXnEnO2qRf--N1BONgP6T3m-rNOHGvHHfrAOvlv9Q-j-WPjBpKxf5WJPM8pZU-kZc43KOMsV6-mptes2iRkJym1u2nEblA7J7hnXs6gR-TyVYGScvREGIP10Et_CzDP9HJIzC5pXZFj9ltPfWF1cmz7EFGQnJzy9Yrcfs4_34xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=EJlEov0oOVDo1bjad2KYpouR_xvhpbwInUhXMp8W6fnv4cyLyyT91iakJL0V9Fv8_k9J9l5L9oV_7SwlTyxF9RtZlynJw0PkQvZKoT3fCe_UbQUC8N4zyB7YScrDYan-Z5AHQqlS_VY8DMXVY3sliJxYykLdUoSmCsp6opFAfGeuHsBAllbhaULz2oL0iwfGOCmuVIDC3TL4s51rs67wcFq9l4n4xi0B8Z0j_1QtHexQjDjiSonNzi2y46Crkv2_K33TTzjf_5189ReOnPvshcMnb-m-ga1MUQ-yKFs05JU2lOOzXauENke8aPioS09fs7c1eG7wNgyKNNOuNllhMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=EJlEov0oOVDo1bjad2KYpouR_xvhpbwInUhXMp8W6fnv4cyLyyT91iakJL0V9Fv8_k9J9l5L9oV_7SwlTyxF9RtZlynJw0PkQvZKoT3fCe_UbQUC8N4zyB7YScrDYan-Z5AHQqlS_VY8DMXVY3sliJxYykLdUoSmCsp6opFAfGeuHsBAllbhaULz2oL0iwfGOCmuVIDC3TL4s51rs67wcFq9l4n4xi0B8Z0j_1QtHexQjDjiSonNzi2y46Crkv2_K33TTzjf_5189ReOnPvshcMnb-m-ga1MUQ-yKFs05JU2lOOzXauENke8aPioS09fs7c1eG7wNgyKNNOuNllhMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4J5t8UAY1zgtvNTUZpiLiEqA2IDYivpC5cA2Y3o8Thzd97AxMSYijBP3L_72Q9DgLb8zu_XCcvjGKWXQHjqwvg4cDgWJnEgfZjZ8D-XsBzgMCXaFJoF1ztWXc2HpF7ewNy9XtCMAZW7jkUQGPDPdqVtjj71mJuzgefVfEi490b1RNZ-XkfsRYBaf7wPoHqvnEBphgbYIgMFxPGxWbSBK980u4WqnbAE8LF6fCpag3RRODC1MMErF7ore3KyXKfe8bup7IL-s_YEAzCMoOFf3I1OhTP7gT5RmA8TUX5mETSRV0LlZEQOTp_KctNmWz7xEbgw3vbCAl1A2rXoM6sqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=ZSeJPAWYejX_mmcXmu0FceC-6awamHCwUUJMaHOe8oFEroPcRjjvKA79hPA0xkqCII2SjETEw2dNhFZvBan3wXnNwIMFaYSgKg8wD7F0goM79Rmsa_L3SDF47YprZnTg_rQDUWfLbvwFssaMXHZ-CE6ZMyXWmVxFgPlEG09nPO-BOWUxnkPq5B1kdt_HD2oxsHmvlJujuiHXbwb9Qq-MYw5YmG74_brOBMcRcARHUyHt4T28y_HIfA67AVKv7a5bmw8z_lQLFkgdSzyqDbKMIPwV0kZ4uKi6IHzjBZGEEVewJtoMlDs740avcenyTqx_30QS4vow3qejlZn1ETn6qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=ZSeJPAWYejX_mmcXmu0FceC-6awamHCwUUJMaHOe8oFEroPcRjjvKA79hPA0xkqCII2SjETEw2dNhFZvBan3wXnNwIMFaYSgKg8wD7F0goM79Rmsa_L3SDF47YprZnTg_rQDUWfLbvwFssaMXHZ-CE6ZMyXWmVxFgPlEG09nPO-BOWUxnkPq5B1kdt_HD2oxsHmvlJujuiHXbwb9Qq-MYw5YmG74_brOBMcRcARHUyHt4T28y_HIfA67AVKv7a5bmw8z_lQLFkgdSzyqDbKMIPwV0kZ4uKi6IHzjBZGEEVewJtoMlDs740avcenyTqx_30QS4vow3qejlZn1ETn6qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=SI2zcZjK0KDOQZq8tqz6Y3ke2_XIBC4BiZW9bFEtHMuNv4OPIzCTaObWgim4D8lt-GrcL14UjKHC4J0wjCfL01cwcPiXlHCpQspYiA6wVJ9VHtaHPanULvmIcWteVvAN38kUvY4l-9zvsFV7TpWN_u386kRxKTPqRIp6H5kA-Cvov4hgT21Hqlum9CdAH7W_7gnzT4UnOcOAeo0M_BvUH81BLnWmfA-NQkOHvesFBqwoJAuQ9sY7rHQPGaaFEa6Vvbg1AGVBZn3h9Ll-eIMTTDASgoppSZZYUwEv5fxIgKRecPfEiPs2wxklDxbpoezJ7Ez_sC_HNpVx-cIOGS_4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=SI2zcZjK0KDOQZq8tqz6Y3ke2_XIBC4BiZW9bFEtHMuNv4OPIzCTaObWgim4D8lt-GrcL14UjKHC4J0wjCfL01cwcPiXlHCpQspYiA6wVJ9VHtaHPanULvmIcWteVvAN38kUvY4l-9zvsFV7TpWN_u386kRxKTPqRIp6H5kA-Cvov4hgT21Hqlum9CdAH7W_7gnzT4UnOcOAeo0M_BvUH81BLnWmfA-NQkOHvesFBqwoJAuQ9sY7rHQPGaaFEa6Vvbg1AGVBZn3h9Ll-eIMTTDASgoppSZZYUwEv5fxIgKRecPfEiPs2wxklDxbpoezJ7Ez_sC_HNpVx-cIOGS_4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tvVJPVTsBHivtFdFeYAEvPeGFVNckRuN7bWz1gpZbajKI670afA2nO30tKhuJ3q6vO2PXUAeMMwFkNLvTPCJwQcPsr6WbMqldYXa8BiE77XYMvO-JUu2q36g3Q--3hYD67L_-9Xv6Oh5YN6KODdkGxysYtUAbQr1t2NvNoqmbt_qF2vUvcSyDzlLR56OZ6dgH-URyXdW7tvetWAXtYiiuJZhpCRBFTCYD6BcLwOq0bDBT7wgxV8QYJcY1jbYg2_BBiQj2uRepCrS2aLan00TFhOK3lgYuvYdOd4eHt4LdQ8dfS1QGy2dJkVnm5lRIyQqoje5i6YYe3pE-ICLHf7TFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tvVJPVTsBHivtFdFeYAEvPeGFVNckRuN7bWz1gpZbajKI670afA2nO30tKhuJ3q6vO2PXUAeMMwFkNLvTPCJwQcPsr6WbMqldYXa8BiE77XYMvO-JUu2q36g3Q--3hYD67L_-9Xv6Oh5YN6KODdkGxysYtUAbQr1t2NvNoqmbt_qF2vUvcSyDzlLR56OZ6dgH-URyXdW7tvetWAXtYiiuJZhpCRBFTCYD6BcLwOq0bDBT7wgxV8QYJcY1jbYg2_BBiQj2uRepCrS2aLan00TFhOK3lgYuvYdOd4eHt4LdQ8dfS1QGy2dJkVnm5lRIyQqoje5i6YYe3pE-ICLHf7TFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=t1dZevpQy4-3kFOX5XSMSZbJp0d0uWnZ3NibUKVydYlkUoa4VSP21AgO8Ny7s85_ZXTSnVCRq-R61PL48MibhSGJkwty-FzH9kZCNHYEVhJRBfpDMO7kbg5sNIDxnYPh-DOA29tcBFu2LcAbGCRrQTpmC51huTLx1RQhmlH7mQLgj5PF2YgR54eXLqH3v_wV4gn1RJLVNVV6ZwByrP3rZaJnoBtzuKB59LihxNhOPMDZbUmYBKf9FV9qHAW4k_Z6s1eOhbtiQ0Viebw2eQA5q-HLrCwHG33xafvbFdr7JjNY-HIz6jkHnfnjRMnZ2cG1l51et1JwQ8TyP6r0laq6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=t1dZevpQy4-3kFOX5XSMSZbJp0d0uWnZ3NibUKVydYlkUoa4VSP21AgO8Ny7s85_ZXTSnVCRq-R61PL48MibhSGJkwty-FzH9kZCNHYEVhJRBfpDMO7kbg5sNIDxnYPh-DOA29tcBFu2LcAbGCRrQTpmC51huTLx1RQhmlH7mQLgj5PF2YgR54eXLqH3v_wV4gn1RJLVNVV6ZwByrP3rZaJnoBtzuKB59LihxNhOPMDZbUmYBKf9FV9qHAW4k_Z6s1eOhbtiQ0Viebw2eQA5q-HLrCwHG33xafvbFdr7JjNY-HIz6jkHnfnjRMnZ2cG1l51et1JwQ8TyP6r0laq6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ2pzI2L0dSN8noSw4PxmgeUWvKIsnbwheIGerPaxH-jWyCMxblzRQn4JQj5I8EqxKUL3I8NEBF5_7DB41_EZddEI_uvkoTfe6L-poPcLJ1NHMyXxhLZV1SZxarybDH2IsVdmOi3vQvJzY_MJ8Dj20EpqjMpP8qF25FfmcPspbxGsMm76tFEEgm46Zid5Iqw0M514hb6EkjFvldbJbgM3OzJYAaxcS1ajx8fgBpGETb0DU15J1Q_F4HTIe7Hj9PrFrvSYtdl65os4nJh-M7DOgveIYircOOrMZORzixlmVS3OKmCAiLvCfMOfOUACTdHJe4uO4YLKchuCIB3ykxyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z7qKWIcEkUBmMXMKJx3UK2aCFnvu9hvPL6I3lTVbw_KRwA_-t1BfoR6KF6PWllDJkwlXWy7WIxbwQ733e6QawxKAmvM1qMsIuvqk4ns68TimXaamLoOI6wwgBRa07R4k89cQeISs4-YM7yhoMDzrb9XUP09nN5RJhEmNJ-M_ZCjbHlDkZP5RjrBtPrJGF3UEip51ISbLDze2dB8cH58eyUgS1AYCceVJRC8NI58yoJ2gUMcUW1yFGAcSeAckHp6jGFyKyXmzLxV_KgBwlThLeKF5fZuNVqlbQ8JqseCOCxvfcC07bQrL-LqXz5UxewUtoEvEv1hU142AILI52SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA6jrcoWfgfd8qtqEp8Xyv1bE21ouQg_m5nBzGjCDTdcx-SFMvqdiDvJ4uy7erpF3So5-zjOIKa08uM_BDEIvCndNDY7Vwy8Va72-x-cUENfJTU9XlJ7RzRKH3i7Oxsl3rGzyAKsfGUU_p3z5FtAQDU2KwDAoTPkiMyN8GTmvIc5JeMuW6_R7k_HnS2-E76XIPArBkNHbKiS8JmaVkUWZGEmiJoJdbdWJEpuZCS0tCjX0NC0mFlC3qmLslfqdXBriPQfwsx3THG65EVDbHLZGxNqpuuZwl4n5ViQBp5XAJqkE7rE_P4k_wJ5a7Z7ujCKVGWJqwIPegyKp8O8yIV8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR1eyaN3aN6ortsUIyV6zrmNQebPn95xsQFpIzbW1H0sHRdIrPSGXl3BarTzsEGG7MbCCxc8LkQt9ERXIpRkcRqTcyNX7XJDITPmOaQlaTf_YlYOsqYDMmnESGo5c05g5FfG5ZHQO9aFBK6oCaxKcPv-5P_w2Iq1L8TSj6segIxzzNLO4AKVsehHfhi63zPaDfamyFqJCpMmSQqgxlKCbUzGDaLJIegxB7n3owEelrL-_3h6jne96jQl2kPRrG4P2mlqIoTdww7OceYM-NdnUyTsT7SwlLTW1NFK5MfKLeG6UWX18fOcXFYoUdYSrDBKJVpODzahr6wiGSRTzVLaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTYBJZaaKWwHHlRR1ggS9ygCVUWi98mSlYbLJK_8zaAT2vaLN-E7mYJhT54tprgZ-vlIGQikCD8wRvKp7CO3wQilMj7pDT5E9ULAZxpCW_foACcqOWpD-zET3FwdHP4R-HRDaO5mX1f1vgGXR0jaykVD2lJiOwEIVZn7YRVgGZ-v_PbUlwL1O2Szl1FEIRXBKiqGqT2FfTM1DPMdAj1iXfQPEM47wI5DuPZoRZ2Y-e6DV2oUs2eaZ-OTL3TVAXM6BV5XcDpwQNSjz7m0vvAteoRGNo-q7ORj8oBCE9rw7tNNF03o3qBcK0XHj-rOOMcZrJ53Tx9Pb1G4a8X83PvWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=i9ge3h-Foi9fP3-_qMWd08ZJUib8ffd-LtyPY3qzdPaEour5XTbbhjO09kUD6V58ZlcGcYbzOTQccMaiS1VV3IvbhQBqtZAkhmpvyK_mToIQMZq7MKETcQxXk5cPpLLAvmCowQXvvyKWsBqh4cwgZw3FSKN9N4PvBxvn4Nkgb2XoKUENNHTCiuDKuMHaqqaO_REI8nnghgJFXNJv0hCW4172sGCjqTCzmrpgt29DJ8TAI9X3yJ-oMVSoyiAwoL_hgNxXBbIri9usxczziZcRUzR3MXCK8etelO1OjMcrK6rWK_OIyJkMNl9QQFzCMRZDodCzaE8HWTcyK9nU3Hzt0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=i9ge3h-Foi9fP3-_qMWd08ZJUib8ffd-LtyPY3qzdPaEour5XTbbhjO09kUD6V58ZlcGcYbzOTQccMaiS1VV3IvbhQBqtZAkhmpvyK_mToIQMZq7MKETcQxXk5cPpLLAvmCowQXvvyKWsBqh4cwgZw3FSKN9N4PvBxvn4Nkgb2XoKUENNHTCiuDKuMHaqqaO_REI8nnghgJFXNJv0hCW4172sGCjqTCzmrpgt29DJ8TAI9X3yJ-oMVSoyiAwoL_hgNxXBbIri9usxczziZcRUzR3MXCK8etelO1OjMcrK6rWK_OIyJkMNl9QQFzCMRZDodCzaE8HWTcyK9nU3Hzt0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPphgGDYYPwxvynwc1mAP-uWgqsbsDQi4dTdBhvHZiPZWuyke622u5XnUVXzCDZYmZSEJW_czeIsEPNR_Lpsmkw1l0c5P_rvwMuRxmHzh-3MYRJF3hVxGXdtofP3aJ9CMFu4cBB9kG1KE_dWVl-qOOo3zAEqU1Oai6HvAJ1mh9Cvar70baXCkHvxPKuLSZydwWdPVGCUhYOiZEVZJsecEbFv92adahyEi3SHkqvWYr4hIzG_fhTU6BQarN8aoAAzYynoDElGZe2bc_AGyxjbDUwSe84x_m7O3Nm0PULlSI7Qrom08Xj0Ncn7hV_py-iu4Ia1A6N9StvuFMuVFDiGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=mjJZyWWtAreVtP6netfGvZtPA7Yp8iTR-xUc73kFP0hAz39Mpa30RZpgQR6bDPK9E36oYsozsnSN4E2e2VA36ydFHc9_LVbyMfFn7pkJXbz62uZCEiyZaORL-68zqAGUOzG_qFs7K9KqYlQTwEFoNmzCWjr5ntI-QBtMzq5KQ0fpcV1PgqwwSxdnEFqxNwQQVty45V065z6d_L-Fv9tNtNIsPc1zwE7VcPbQRmenHi2F58BwreTT1Ytb7zd-YPe6hADFCrPABAztAIbc9u6jg0EgsFvXwXaYVvPF0FBcC1DBhfvFZYmmaSj7rT3U0JP_-w9BJ2U3jHJcRLfs7S2UYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=mjJZyWWtAreVtP6netfGvZtPA7Yp8iTR-xUc73kFP0hAz39Mpa30RZpgQR6bDPK9E36oYsozsnSN4E2e2VA36ydFHc9_LVbyMfFn7pkJXbz62uZCEiyZaORL-68zqAGUOzG_qFs7K9KqYlQTwEFoNmzCWjr5ntI-QBtMzq5KQ0fpcV1PgqwwSxdnEFqxNwQQVty45V065z6d_L-Fv9tNtNIsPc1zwE7VcPbQRmenHi2F58BwreTT1Ytb7zd-YPe6hADFCrPABAztAIbc9u6jg0EgsFvXwXaYVvPF0FBcC1DBhfvFZYmmaSj7rT3U0JP_-w9BJ2U3jHJcRLfs7S2UYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=vCZFOEWhVRbR1MgWlEEZeGxIB0HT5ckKtdvg6CVeL2z42bx_biIJigdnQGGsEPJP-UqHtArcpxpjHwBUyWM7vdBsmSdw_CQ5vRqyoBaV9tar9LjPib0Hx5gPhKVv0HhwLUEH4r1219KDHJgKg-Fw30kBrrMTSg_Ix0oS4cs83K5BPM74ol2Ov9OxukfRGhj5wg1Ybw_iFSHanwlRZNBKdFw647_ya7YsoglXLXQbz_L6MTE3i915be5naEV2zn2MubYVOViz7IHAZvfirPBfG2wJNcmrjGGPVyzRzFxFukOPvelUQKY6bk_18KS64-Ugxj9VsHMnMGPLod5sd19lGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=vCZFOEWhVRbR1MgWlEEZeGxIB0HT5ckKtdvg6CVeL2z42bx_biIJigdnQGGsEPJP-UqHtArcpxpjHwBUyWM7vdBsmSdw_CQ5vRqyoBaV9tar9LjPib0Hx5gPhKVv0HhwLUEH4r1219KDHJgKg-Fw30kBrrMTSg_Ix0oS4cs83K5BPM74ol2Ov9OxukfRGhj5wg1Ybw_iFSHanwlRZNBKdFw647_ya7YsoglXLXQbz_L6MTE3i915be5naEV2zn2MubYVOViz7IHAZvfirPBfG2wJNcmrjGGPVyzRzFxFukOPvelUQKY6bk_18KS64-Ugxj9VsHMnMGPLod5sd19lGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=BE1YWs3fPocWJjO-jQ_c8W97TT-zFqBz4HP3Zfxexr8EZXpR13kWmh-blU1uoKqW_fBO80oeq_P7snRNqT6t6luhlJpeuokIKS0BDYsBK7OzLOzpWWl2CPfhtt5skf2UDv-FiA-rBrp5JR6M7BulUCCwVjk15kUSitfotDvCiOeJ_8NOiRM7yLniQURCpgxmg61GThGR_laueJU0mUA2OF6iNXO8gDEgJS05of8ZZictbxkM96oxz4G7c0fZsg4DqlH3e_QXwEqBskI4tXH6Sj13xoO7Ep8VpY-k1QmNyNj5FlAytkm-l_OvPXu6fV7Y40vFRYDrHxTqnV-vQpwHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=BE1YWs3fPocWJjO-jQ_c8W97TT-zFqBz4HP3Zfxexr8EZXpR13kWmh-blU1uoKqW_fBO80oeq_P7snRNqT6t6luhlJpeuokIKS0BDYsBK7OzLOzpWWl2CPfhtt5skf2UDv-FiA-rBrp5JR6M7BulUCCwVjk15kUSitfotDvCiOeJ_8NOiRM7yLniQURCpgxmg61GThGR_laueJU0mUA2OF6iNXO8gDEgJS05of8ZZictbxkM96oxz4G7c0fZsg4DqlH3e_QXwEqBskI4tXH6Sj13xoO7Ep8VpY-k1QmNyNj5FlAytkm-l_OvPXu6fV7Y40vFRYDrHxTqnV-vQpwHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=MF41eBNo3ap0kHk8gLoM5XZ-5AHjKtpU_gLKqWzyhOS3gIFiW7k4SoSHvkhh8dRv3vfoXaK7dA_NBYbPqQQ6yBGBiZXR2VZYpB5juAwohFejjHlm4lr1I-ncZkfqh9lfZtSz-JX2Jt7i8wG8_Jyrkozjgnd6RxxySVxUeUclPCAcQ1-U5wsoA2ZfLfWFkGVX6wMMmnlbtQB09I4s9rRRgJmkoQ34fytQvD1Vi9N3zeXu04F-dS-LlIcF5l_3JIGRUlM7vjTSZB1PT5uBB_zqk9-RcouGwaA1JEQ3wkTMZkuMdl1KBAelrs7IQlXXMi2QCQOTX8z4F5x0wcAhZK9uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=MF41eBNo3ap0kHk8gLoM5XZ-5AHjKtpU_gLKqWzyhOS3gIFiW7k4SoSHvkhh8dRv3vfoXaK7dA_NBYbPqQQ6yBGBiZXR2VZYpB5juAwohFejjHlm4lr1I-ncZkfqh9lfZtSz-JX2Jt7i8wG8_Jyrkozjgnd6RxxySVxUeUclPCAcQ1-U5wsoA2ZfLfWFkGVX6wMMmnlbtQB09I4s9rRRgJmkoQ34fytQvD1Vi9N3zeXu04F-dS-LlIcF5l_3JIGRUlM7vjTSZB1PT5uBB_zqk9-RcouGwaA1JEQ3wkTMZkuMdl1KBAelrs7IQlXXMi2QCQOTX8z4F5x0wcAhZK9uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymq14t1KU6rftUVtB5W0Yb8TRhs1j8dFBCrSzRIwN5oztsqEE8hzYuue87CnabzoUN2Y6mv2Ty8zij6IBXOp-1oj-pFKgpnNoWVawVz_P_ehwjYVEOB3g6nHM-ssREww4-JBadio5okNJnHlU2hpOWRQYW8cCKxV8v9j9kKaiDT26wDuzwmq2vm4x_549peNlQoSfcWTakMXQGGFhhDrxDBwDwtnHCL9Bdgpfwp0OKdoFN9cK_ccmbTxopL-QqXbcGg7R2HLFsoDtAfjpiEjZNKC--ZonpUvtu4dYjJr_hyKcOs6xn1grsJovSw3FNd9GrzdYCNLvnEyPCtXCORBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=vyMJjobkNqXip1B1LOMZRkVFx0DdJEoQ-7s3O_wurPxhUUyZwWgVpOJrbr9DH0mk0y1dEP4IgmC5RAaPXsV93WCMWfzYnJSrf6IX9xOgsFxaan91edtEleGKQcGOkeL63xBA9F6yklyMKyThCMK6LRN8G-13yxC7ENi6GNti2nXgfAWx_X6Loqli7K78-2JpQaXNlQWJdLd6-YNLvVvrYKXWXUwTha4JWPTBVRDi-oUd1Iaysr1OhuVFSXudwKfh4blWjBRa_IgpGpl0d0Xai2IDLVMyvcl4cakwIXElMVmd4rw68fjhNFkr5XnRgtjGtWzz6OcVgoOcbtyyY7ScZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=vyMJjobkNqXip1B1LOMZRkVFx0DdJEoQ-7s3O_wurPxhUUyZwWgVpOJrbr9DH0mk0y1dEP4IgmC5RAaPXsV93WCMWfzYnJSrf6IX9xOgsFxaan91edtEleGKQcGOkeL63xBA9F6yklyMKyThCMK6LRN8G-13yxC7ENi6GNti2nXgfAWx_X6Loqli7K78-2JpQaXNlQWJdLd6-YNLvVvrYKXWXUwTha4JWPTBVRDi-oUd1Iaysr1OhuVFSXudwKfh4blWjBRa_IgpGpl0d0Xai2IDLVMyvcl4cakwIXElMVmd4rw68fjhNFkr5XnRgtjGtWzz6OcVgoOcbtyyY7ScZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=aX0Ceosh_2tmRyHescvIevyy8iCfJx5TzNMOnGAznrwsfv8NL958Vd1X2YHBPsmwRMKbFCUxX-nzJ3c5DxeN6ME4dccbA8F6dKmhYn5uRBVphE4u15w8rKbPGy44PIgMJ4mtbXabw850COuLBeVmyaQirMB6Iy6Lxa-C0GKk-o-L-JcnUL8X0C3QHNYSN4Tz4ry-S3Xbc6Mm8D7mJ6gHe30mueq3nClO1TPugcwxsqIEojbCOn6IGy2nL2Z_EbCFkibE1_oBKkmklQ8eWN10QgVXXQWfj77Kh6m_nZ0JfyhXDkVY_2M-V6t9uKcXC0zriB099GwFDXRlRWSln413Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=aX0Ceosh_2tmRyHescvIevyy8iCfJx5TzNMOnGAznrwsfv8NL958Vd1X2YHBPsmwRMKbFCUxX-nzJ3c5DxeN6ME4dccbA8F6dKmhYn5uRBVphE4u15w8rKbPGy44PIgMJ4mtbXabw850COuLBeVmyaQirMB6Iy6Lxa-C0GKk-o-L-JcnUL8X0C3QHNYSN4Tz4ry-S3Xbc6Mm8D7mJ6gHe30mueq3nClO1TPugcwxsqIEojbCOn6IGy2nL2Z_EbCFkibE1_oBKkmklQ8eWN10QgVXXQWfj77Kh6m_nZ0JfyhXDkVY_2M-V6t9uKcXC0zriB099GwFDXRlRWSln413Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpughdH36K2lWNc-Yg4y_1_MKH6_kt_OnCetBvJTUEu5Jq4yI3DSrlJv0ihI4X5L7PMaiyooiCIVNic5r58zID2igZxAj6_FvqlfBNAH9oZxVIVb2QX04eRJc-qmrROBwTj0wMiVdCzuzW2_F-Bkn-sJcDnyIlWWIj8pyhCOs0bCgZ8v0LRu9vebtllqkqfNOp2SI9-Vy0E3C010Iib9O0mZWfWsDWDDUYJrWze3lSM6Kl4dza4WwID1BWykgPcxf5LncWXX_TlPXSPCLZr0AR9DDd2_ye_FBY7Qxcu590YYPDRlBLF8BtCqlUy7ehmRAVPw_25g5vhIEU8nmQMwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=O3MfVbrzus1iBmSh8JBC9GmutLp9XKa-ObYNIMgXxZl09a2-YnyDhrCh1eDthDHQavS9sVNqH-DGPCj8P7_6kJp_xZyF1mcW8Mg2P6LmfC5nOq_tJNauriPSqieN8tUjcTmrIxmacv2Gmqxc2VlAk-ciKyuANLuc_pyYOY-czyhHDnQuE9LFYkFGGlXj41f0Rcz1f87azh8Nlzv3chwXxE15y9YP73Uh7rM2xz87pxMddirZ2KcMTyp_U5tkKb8jOYtTOfPv0T6vdBqhhrXKDyPci7dB-Jm_X4zgEmwr_44GVWGhvlyvFxjK9Iw7ncr5d55SW3nyub9woypXQPdxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=O3MfVbrzus1iBmSh8JBC9GmutLp9XKa-ObYNIMgXxZl09a2-YnyDhrCh1eDthDHQavS9sVNqH-DGPCj8P7_6kJp_xZyF1mcW8Mg2P6LmfC5nOq_tJNauriPSqieN8tUjcTmrIxmacv2Gmqxc2VlAk-ciKyuANLuc_pyYOY-czyhHDnQuE9LFYkFGGlXj41f0Rcz1f87azh8Nlzv3chwXxE15y9YP73Uh7rM2xz87pxMddirZ2KcMTyp_U5tkKb8jOYtTOfPv0T6vdBqhhrXKDyPci7dB-Jm_X4zgEmwr_44GVWGhvlyvFxjK9Iw7ncr5d55SW3nyub9woypXQPdxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3ICNRjmXAtul1Kt6b1kL6qgphXhbmtWegv0knDLwARf9YqTJQ0yGjG-5LyBl7lJyKlrmbjL1CSyISLN8DbMB3oXAui_LrkROMXuw9y-QeUufeJSsvTsFSzSXj3hZRak742csPhs3GyKRX0cmlNyY_hsNed9gc0nc_sPRGv_Fsqp3NUNMami4plfnq_PbxRptUQHuwpn8aSBUQHm6e5Tqa1zaVXYTaBfLVM0kumWOA7PfNfz5y8ZNS7cQPyNVlfqKaFqml2wKwWBqVNLjAa3fvFZ_BN3h8ii5stPdaOxfx8-mhB-7pWa23VDroKONFsolvz21DCIusohABDDg_f_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMzF4yDzmvK7Y9Y7HyNA8j26tbldonKVqqtqQAp6MFThpJtAh7EVLoU309pLIRzS0vNLkCZRNzurZRq1wDUCVy-wkJXnN1HE47uUNo9FavAkCKpwI6PGyKiRTt4QRhKPhkvTSBbFMASywrwhXYv1TPMq6X3ncSWYhNs5hWvN0KI2MVnSBnrD52FWnKecH3VJ5BHq3d1kkPPTYYX8BHkpNocs9JX8RMS1fUdsqeXeTqnk7B3dXQNsxTT9LQUkMT1bXujSg8wqQ_MbBEp_u-HQ9eChTqdeQlGDxccGlJjhDklXZiGdkO_qwwECMVXJ0puEfmy1L3muzFhMxi54ySEMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E8_a_b-GczL-LLQiKodXPuk3kjIZhLQPJq0RkAIZTVbifRtzK2Or0Egcjx4gtM9GngBZrdJv7P9QUkfYbNp8Qz_qW3dLI6naBmqbL8JYmQXcqiTLXGpAZFF6gNrD134B9-5PG9gsHEvRCBdBJgxE1Jq9D0tvxPLOCq94ws7MnuALwRZ5KfL_9arjO62UqW-Kj6A09fDra1jGv88KMHr47djbqvWDV1kaLTnpiTWKO8KQqsJp8PNtBlKPHRIoLHIWAN_QmftgBmHp_6_lPX7GviCMtnWElHiFuMtMHfVernsS_j4efQ1T_ZME6BBISJ1UZd9l1-CQ_4PL12byLGFV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5hOL6XFrZ65lPatDj4AYD5M7Auk4CtlZvnCIqvAlIE4KkXz2YyI6YwrhPbwGigGIJxoiLKs6xfEe3-QvWHekuyvrlp3sy_wuTflnKqhLUF0J45HyG5b7PxRiV7myFoTJfTtkRglxm8hEdJ7RUH4vsvO0oKo7488KPJZVUFucmsJlDDEiv7xwi0LXwrbIbb0knkE0Jo6g131KztPHmncn4LlB9nrGihylfQBddjWGQbNM6tTQfkoEHbaUd-0FJxe1C5V0ovnV3SpdYM2MIUQZMiVVd_XQeaW8SQ23h4siyir2yOABXT-GZ3lurCW9fJ3LVfZ1JQB4JgeC4jSM-d_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dErKmu17BiCvQp4mF7StGWl4aVUFiZKZ6BjRz-KhJKCJq0IE1YTajtla516jUNdvb6C0vHOIQTrAyDFseZoivKRFOowrnoxkuzrGrn37NIG5zJmC9pLkZ97AGcLFS0-yJdSCCFgbhU2Vowv26EgBdyTqyypLb5ReqCr5CvfwbftDZQ9BIT8YwSUeb8AQwObyK2eqcmFX7i0P4dSOc6ZUW_MTsgh5uoL7EAgFOGv46jfCbmYlXQcwlSlyBISPXlNPK5TvlCDqS-X9_G2f-1ulY6N8_EL-8SvTpMxdCypgK1thTopcNnNk5dY3-B5Z-Dxr6OnsfGZJxPZj_8rfsu50GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=GQ-HWUDIClicyjVFG3Wr9LsxeU2KFFIJZeTaDXbmzZfmnD-pVafbcLmqEZfsraGYoI32SgbJRdhLwBXOyw92237z2ygC1CFjZn0oEAdlM8-BBtXMBdxj_fbqStRdK5RCzBPb1LUMx9UewrdPZ6JKYBqPGEZxHBke5D_M-g9FWSW4TVcP_ovDvpbcZAXDUxX0Vf-o0l4goBjVMgspnjs6GRnzXevPH4vNwvZ6kjm5zsevSfSEJli1ts0kZ4FxKDwLdT4oAnXPBF00R_S-WpDJv1WPMB20cZwCFlVG-gCDF-zEHwdZS10bioZau5eW3t9tzOFdWw-FrNBx2sNA-TI1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=GQ-HWUDIClicyjVFG3Wr9LsxeU2KFFIJZeTaDXbmzZfmnD-pVafbcLmqEZfsraGYoI32SgbJRdhLwBXOyw92237z2ygC1CFjZn0oEAdlM8-BBtXMBdxj_fbqStRdK5RCzBPb1LUMx9UewrdPZ6JKYBqPGEZxHBke5D_M-g9FWSW4TVcP_ovDvpbcZAXDUxX0Vf-o0l4goBjVMgspnjs6GRnzXevPH4vNwvZ6kjm5zsevSfSEJli1ts0kZ4FxKDwLdT4oAnXPBF00R_S-WpDJv1WPMB20cZwCFlVG-gCDF-zEHwdZS10bioZau5eW3t9tzOFdWw-FrNBx2sNA-TI1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQklvYpkJkgSvBCa17-aRkXuGcJjOxzs1V8k2LkXMESyoziw8f5ksXNC_GrF9BfZXOA0LHeRADXb1C8qxm8qHd6v_R50t5_-OceNVC9oKiidwWSKenYpPyW5-z-BWLD_R86Zb2tymDPJ2QiXfzuOrK5SU84DtYsm3xl8GVqP6HyPpSJSZkBy-D_WJMvbNJ9aIWfS_Dtgkj4W9EIIUMepgmkZPd6EJVHYmJXDmEaOyPZAVETm4tHjKdHpYVsw1D1cGhpVHi16-_Uuux_eAhK7JStgQopC-dvXDQPFwOHrqmU6AAukHx0zrt95bIGFtMZJSAWdwubwLp_eOqJoNc-5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyDzUWR9zw3FOmP9VGezQ1EUBiS08hl8xrdeEFiPFSyzXT_5dF-dGynr6-SUL-oQgC2iUucH8kkkZEiBlLQpVV5ugF5zz1FP7ZTYvHDD-YW7OYZcVQlmRrR25P8yfPV2i6lIN6mANj7WksInrZFGDSfpdpNYgzlv2lHwCXsvXYnOH56jgaDLhgai_oh9EJbpAsAmtyzXe0LDT7UrSrBzrO7YkZ6SFNXn1SMhE96pbP_taivGyDjJjMwKL5bYsGuB5ma-eFwQUqcEozBH_3ZvltDa0UQFcu18at8uGl8_8ZoCDfyn_llGLuiWZjbXwObLmir5vKJ_2jedZ90CkjmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=IsWZHXuEFufLF9EI7vnrP0CtI4Uwiv3tCeKpfhAtPtuxvCjnB0OsdrpaCbCMKMVjaM9EDlyw9H8GCoTIEV83vlUERT_EqVWm_tcgtwK5mfSZQDm7w4VZqVMiGxJTeLh6v72KL7Sj2YD7FDHI9DvMWPpiNOhTjUef63epLcbktgWvyE9ozzY4rZSRYsBlBcKtzkko_qlbSG9U_5b9sSz5tPfs3CuQhnlsv8O9MNMmtPCig8Pidl1Afcw-ehL-ScnN70jLabLr_FpAiQWgFD-ygz5NeD-aAh5Fhl1MqJTk1iZsMWljmdcEfLm_h6Q209_aket2S-c30gHNm2C9pUSYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=IsWZHXuEFufLF9EI7vnrP0CtI4Uwiv3tCeKpfhAtPtuxvCjnB0OsdrpaCbCMKMVjaM9EDlyw9H8GCoTIEV83vlUERT_EqVWm_tcgtwK5mfSZQDm7w4VZqVMiGxJTeLh6v72KL7Sj2YD7FDHI9DvMWPpiNOhTjUef63epLcbktgWvyE9ozzY4rZSRYsBlBcKtzkko_qlbSG9U_5b9sSz5tPfs3CuQhnlsv8O9MNMmtPCig8Pidl1Afcw-ehL-ScnN70jLabLr_FpAiQWgFD-ygz5NeD-aAh5Fhl1MqJTk1iZsMWljmdcEfLm_h6Q209_aket2S-c30gHNm2C9pUSYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=gAL9wzid7NUx5IAMk-jzNaYtNPxe1xWT0VpTU-LuSnJpVzQtabRh1wt0hBqjuz4RQTnRLXWnNUBebRMQgL9PH8jqbx5xgCfbx9jLC2RwmvL3FN8Vq5tHqLuebs9vWhCfxH3lW1iuJfvGWMpmTl0zGvfwKOGanshFpl2QGp3pD4LmgSbfuJeUPQZdzBaAZcN2xL3K5qkpf-VhBBYT4X2L3_jy2bpk2DQcvmfOs6Zt38VWj3NzhABKw1G8wWzoD6LG8tir77gRUoHf-FzKumh6rZZN3BEGN2LqM_5FxArdpj_xuHKmuawvsa4gUqmezMS2k-pIOVUT7B_S5bEEYYRjvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=gAL9wzid7NUx5IAMk-jzNaYtNPxe1xWT0VpTU-LuSnJpVzQtabRh1wt0hBqjuz4RQTnRLXWnNUBebRMQgL9PH8jqbx5xgCfbx9jLC2RwmvL3FN8Vq5tHqLuebs9vWhCfxH3lW1iuJfvGWMpmTl0zGvfwKOGanshFpl2QGp3pD4LmgSbfuJeUPQZdzBaAZcN2xL3K5qkpf-VhBBYT4X2L3_jy2bpk2DQcvmfOs6Zt38VWj3NzhABKw1G8wWzoD6LG8tir77gRUoHf-FzKumh6rZZN3BEGN2LqM_5FxArdpj_xuHKmuawvsa4gUqmezMS2k-pIOVUT7B_S5bEEYYRjvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfIMOtgcShCGmt9GSCzCHUuzhVyT2sPz6DqM58nH1gTYFEMwoMMsLyGT3HujxlPFDOwCB6bjsTdCjzbd2t-4p7J2Fv1HeG4_5rilQRapCrTuz7opE8wdHlMQy8PCWz_9acHi8L60BvxVEN7c4g8C8JvZlMQfyeCBfTm2jU_ZsFiep41Q8LzSNEUALRHoAy-olnkL2R5WiPea3_fZEyrYE-ltdw0cthcohmAfX7VTSRd6YqnckgWMQq_wdtynJ5E1kjZj3TYFT93vpLP9Gj9l_ELexg53IKQ4HJlJ2i9iUwjiUYpTzzFtrQkZMV9kw_ioGS4io4oQVQl2rM-7_eZ2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIFHj7hkWA4QQHzIcjoEZyWZ1vNeoEMIYWz5o8-j1LswCwuQKX7uTHp8fCYqK2QnN6GjMuBXz53iUlO02Au3lQxcuuapMIJnOcqiuTSq7ARjL2ws8TPpX2GO5Iy6f31QWZ1EnwLVCaVfEbxNscc2_l0xLqQQNqQP1O-vDTm-VUnoDgY-5oCg0KZGqOG6xA7zB9-w4YMbdopgVsOzHBQMmx2wPD-iQiK_XDD12E8xFelPEmCNjPHSbfHyIn4dz4-k7ddGP8vmKgy23QN50afiikcOgWwQYkS0xXCP6y2FO2Q7U247jDQng10zcC3rVkBQ4r3I4QO-7u-Z0iO9GK4FPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoXnQhUNfH6PPgMGCKPyqnuX72sZb5MxUt4R1pUX-E9IMmn6i8KsJrQoBRI2eOTIQLCr2XBPY0lauLkpoocWq6pU5lx33sNA93Eb3Vtdv3a8ldEFqX9w4gn1Ryo3ReIiefQo9JJf8UzV06Mgt7MIO-3mSVxVOaaqU941cmJ2Flak5UdxZYGiJtFB8or2BYRtud_7kE6fvnwuFrR599JgK0ONhBNGA483027OEpbeLXSfh2lq_uJNQEnefYU0ir5ZXoE0UBEqjazG5Nybz2vwhYCTmR-j4DhRROWmB4kPIeOzkbM7JOVMg2M8BuMCTIQyCFuPjW9iQlby4CeCMNjsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb-yRQ7cNt4Ql1cFh5oyvSq2SwIHmHjuRriDtmMShfgRrxGAi8VESRdzUMJ2k4_cC_ifllENK7U9oLW5acGEa3GJHT7o4nK2oQ2MDoUmQudiS_94Gc9XpyX1CCsN9SQjSwlcYEIPc_3Y1YW1dNUid32TRj_E6sxxGmYQFNQRkz4Zl8_BdA061L1nddmtk226WzkgVwsBoz8TWR3pbxwRMb6r57X-N81nqgFQhAcEMw-SFlTFYZ_jt1hXShueK5oqBJnoQ8wSJFqnnu6L22WaiLbcgtoy7DDzG30bubR6kt0rK89kgIm95Dpm2N9r4IZtli3vph-kJXtlCN-li1nFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5FJd2zfBxpMRIY4FszRQbq5kx2JmDEjx5m9c-vBCbbTamcFkTX5i9rh6Vwf-U5YFfAN8bc645HAvIzKQ2l8gkuLJHd5oztOkOVUAiOA6iJLOpsaZdMXpWbctKbS4_mDnh5LLzVbodwkZqTELSNRmJgsRUr2Wv0taN6MEd2p37O5QzhsjoTLVaDrGo8kPPbmUtDiQX61EqvFAucIE5-WScxEpJbBohVSaCK1WJWKzcq5yjymacArFD3H87KBbX-8aIDLwtVETTOndx6qXc01vRWJI26lyr7P9sQHW_73fjBg37OGTrkyUC6g8SWo3tqxIDkNeqC9Ln48FAaTGq6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9oHKmbHIMLJPhCixLlhMcDBLoggXo3wrxDmcD-dJlcoFIR9ZlO8mG0wjGJ-mDDzKoaSiMzBk5Cw3YbtsyPGnTdoNvA4AI_rXWLQxygcq7LOcHFSYYLMBCQ9CFiu2HuOKhgoWnSkUXX8dzf-5VCEnFGGuIkmdIb9wF6W27TcQN0D75ZO7XBpZ-bS5H4PObM5VWJRatvecx5bPNhbqtrMUwzqSMoIF8G3HdNaCk1fdgGCkFvn2U9PNxP5bKL8il4l-CEDyUm22wsqJeEjdC72Og4d1_5RxX8bmBlY75ucq9Abjx2gpI-c_RIMHF6_P-wBPRjj8L97w6lIVCjdXjDuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV_fcGyJjH8TbqTvMbBrioYPud7ssLbGM0dAmXElpgHkVwFJZyUCZtU2whl9ixc1A_wl0pXndSQVPoIvJs5xkg0fv0xnJ18HdzxD45Z7XeRbnsl0ovr0R9qDr95KZIQeQtkEjSmkLN0VfTt-4jwIJenhQzEFI-oF6osrRwZzq_uIQc_pxhCechQPy399acbOrncmjZgorMRvf3JYtIVSbM-ET8Hu-j5NJuK_wisxEl7qXEnfQUsK6TqIxhz0_ioAGn0Ps5b-R87kW5Bzqaa13771KzmnmCaM4BXa-7_BwLYRuvTK3r09R-LoMjdt2K0o-W_NQdR9xSeJwA3A7otC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avx_pMQOnyEUsrc8ns1jt35wpXng5_Wn_X-l3WeIPDHf5OBgxn46qMNoYn-QLlbVmoT8r0a1aEE4zDC4KrQ3p-ZoxFkDoSMva_NOseVC2nIQRN-bg21CzzeeVYtNLq2D70FzGwYfm5TPUDHyrgEdMLavJS0nItbHGzBwhCTxbWlr_AWetaYKaPCuIkA5xMbE88Tib7mGT55PsPELSAIXwbY89YOU-2D9dU2rWEUz0K4lz76lOZAPzGqy_T3ZaDRq0KDydb7hrdQMWfTgboc9BFwKN5wyUKYRpbR5RL5V0Z9MZaw2J_nu9GTeOExTC8fNSWMYdis2uQHJvv-tEpPW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYcfA_ku6cXnBpkeBNJ1M16V75ynw87B69Yklm7f2p6czDBI-celm6xQCYaNWrKRJ5CLpbQGfOXqwwSKD7YPvF4AF_PXCFZV_LzwqjVyv81JowcrLHUdBgdrcIY04AKdot5v8xJYccj55QL4UQAWpGmxIptWOgD3pEZ0M2vNANYQ2G7voBkQizBId2PS-SRgNnveJi47BjGwXuWANFJ5d_yygScNMRIEO-JtRLkPKurqSJx5b-1-bt79mjfdAPWnBQlb03RroiVfwxWTQgCCH6kVBs2wCddSHumOAdqlADgnyDwJKaRhhGGMCxque9wuPMuf7tOtNAUojWtNNWHmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFVUStPSfbzy_DS5Etv_2bFxPx81b-G95MboEZDskBsdwa36RjIqBG5jmPk9ge1C_YjJvo0RrRnnKsJf5Q1kBck5TKXZnspQIgF8LVSuBd32cdeRaHDlmLcU1JUSBbX_XR5vwiNs78k2--gFdu8v2U2WOYpry95Qv1arr8mh4L8Yfablog6qrnjhZ0Z2BjIPYHpj8-8Yt8Vo4WsCfhzVCMiSUOM1pry6Fi5rQ26n7T4YXuK9xHrHdrHuVasc3MSqdJk57JcF1Cxd0a6tB7Ckx--6LICDbK9Z9cUlzhicmZboeVeAxw8uaWtXvjvkHcsjhlOzwSiMU2eVY-wHZVUoog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKGF0SqdFAg-5e9C9FYsBES86Iy3p0JgXxFzxeYlh8ICkasg7KU9sUkKCNEIw-ynHRtPsU4XBU-6NUAKUUiKMiOZ7qqwlsWrosIqeNMRUxgpbU1FiT5O9SaldTB3OZ0iRt1YoUEEkMzsdNujOYmeIB4Df0y5O9BZuEQKO1iyAedP9xyBP5ziklgGQvliJPblhyNmq1OZ4YCwgM6969Cf7PmrSf8GnffPwjXF0hrsfm0mJw_xRwWus8VOCDAVavSAqaK4zKCE6T92zywOnvVFJM6WmP2TAIrfPoCUPQczB4uV1C6CIMdpgs-BEZ5epvpVzOhjrt138s5xTbdE2O-pVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZHH_fHyBPCRgnmsmYFHXAnNySmQ5mZ5R7_fxDznpbrCWbEbXSrx0lUpgdVHuqCdmWAMBHOmAMjltXntuy6mqxkQRdi0HsIkQKGX_ysZd-iElz_tRtQ61FgL_Mx-PlxXZRbvhxBZpJPOPiou8bjEo2eHTNymDryaq_CdHa2DEKcQtqbr8veioI2fSX2YDZR8OopclORX7ndVOXMGw3CyIqSKle_1WddpS4w4UpN6POuqFPwdNZfo6jP97yNlS5gfAhrnEHrpQTZNDKk1zuSjJ-l0-wti7M28fCbkr_1YA5WtrEN-WMHq9Cd0ecFZ2QrcdYhDUNAg5Q6sgmnkE37mLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=XbM4UUnYYBHDHglweFB0Jeyo-d-XWrBWb2Rmd70dKsJkU--Fw0ccrtedgQLVenI2xXnXr9gMHdwvKcEMuReQmMjtNINF5iAYqgyOdf9tIudIY5kMEVVIjQg_MIdQO-BXVQr7-Z64bjxukd7ozegHQRY0sh1scj72rLZ7ksBFDeTP3JqAAFu9xnz3hCJoKeO1quiMrnG_bdbyJx7mf3bau2JWlv9-q4zq3XqXAcYO5_EdTg3tgLLWa0dUdH1YzVRU46n_ycDzi-831cFIBaXmOMS8Fu_HfhNjd6_5wkYgN99Z2trLTwYCmvTFCAXxG8-OPDA1fWW-HdiKEylQZVEUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=XbM4UUnYYBHDHglweFB0Jeyo-d-XWrBWb2Rmd70dKsJkU--Fw0ccrtedgQLVenI2xXnXr9gMHdwvKcEMuReQmMjtNINF5iAYqgyOdf9tIudIY5kMEVVIjQg_MIdQO-BXVQr7-Z64bjxukd7ozegHQRY0sh1scj72rLZ7ksBFDeTP3JqAAFu9xnz3hCJoKeO1quiMrnG_bdbyJx7mf3bau2JWlv9-q4zq3XqXAcYO5_EdTg3tgLLWa0dUdH1YzVRU46n_ycDzi-831cFIBaXmOMS8Fu_HfhNjd6_5wkYgN99Z2trLTwYCmvTFCAXxG8-OPDA1fWW-HdiKEylQZVEUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=n-A2_O4FweW3_UPF2DH9zpNHoXwDAUK2byIoBfcP2MqJKzMcmuwMG1dKGXJ-c_7aqUTCVn9l45DI4SlI1-ELwAmjwW4HWmMbHwa2WkvsjFp5xZPGFeod4spNKprOIQ4e3cQSxvhzC3IPuhAHhJWrO7sv9aZI4ivxS-dvihIDE9TG0L4HYtkKMT8IC4naPZaZ5xcP0mFczhqzQS9cvIAikMXGonTlmrU0u8jOR8ypp43zLZB_LVarEDHT1etFYzAUjNohIS_BYyGUVwNgRozDH5RIO4Bsu72Nws06OMCPnTTnQTwc2cXaicdLvGP_FXQ75MA1y-xyIjAp2Gf09hthCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=n-A2_O4FweW3_UPF2DH9zpNHoXwDAUK2byIoBfcP2MqJKzMcmuwMG1dKGXJ-c_7aqUTCVn9l45DI4SlI1-ELwAmjwW4HWmMbHwa2WkvsjFp5xZPGFeod4spNKprOIQ4e3cQSxvhzC3IPuhAHhJWrO7sv9aZI4ivxS-dvihIDE9TG0L4HYtkKMT8IC4naPZaZ5xcP0mFczhqzQS9cvIAikMXGonTlmrU0u8jOR8ypp43zLZB_LVarEDHT1etFYzAUjNohIS_BYyGUVwNgRozDH5RIO4Bsu72Nws06OMCPnTTnQTwc2cXaicdLvGP_FXQ75MA1y-xyIjAp2Gf09hthCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyBI5mlrzECdYq8oDBTA-f39-0H4hJcaEGyAS_nEQeWX4Mr2Kka5iM9hfim8aMaJds10Jpn-LokMVy3EPzWjh2tYh1IsPoZ4hz1_sByVuoOks99Ul6ofLl8XcrrNlXKgmYsrO9UYnla8msXXTDteEh4hHSxsHfkVeQDPwJtA3tbyfakd9Mo7_m8fq8BgdR6pCDLMozs-_tKYJ9KmwQcV5gLebcEs5Yftee-cOPEOuEVYmBPst4kmwwUMLOypQWo-y_d6e7cxHZneAn91T7cFaWP0_zO6e83iBpUnWFCMWOpOn1vWYDH3t35q4jPhvmqxOAQJ6JLTW9wpHX_0CBSYOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0jB2fAoELg2JNdU9f-aAe9gVfrCOT9NMdPUk39Dq91rboKBVlFCl-NqL_PTtz-I2WiT1k7cgMgmL1TiTO9tKSIrL95hFKuvUp1rAXS7gd6NccuekGeadZDTKurW4wUq_GFpl7yVQeBUJ8LnbocbBUL1V2v9p83do_KZTHH5Jn8pwqKov040STSmNdMZwCCfEIH__XfZpfgrFyIG4Szj4gZtzt0wO5RpEXgY9opmV-oWianSbOzmpnbuCSf372dWPbfVh1AckFG7psxHtxqeM8Q9V41uaGVt4HT0S9bjIsTYvsu1B2LpLtZlkvIbrPg8l1krd4OFL42QwxydxoFjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FNVp-Cec6Pgn31d6vTK2m9hJCMzzRhM7N9zfBxdSlkuMzdd1ZbgEd01O0WYybxMFAMd9rOW8orpWCaJRYKILUc9AC0Bcawo6UdzVNYqqcoIY3qbjhzUzWBUs3mZjd2k0lylP-5EtWU4zUxxrbBdjxqksB4YF9ZlslMV-dIwyzWh11eqzVYSYvtneoY2nYVzZiILoPbAa0aAYrLaiE060Ber0o6YaP4xdXRYTem0qL21VEmXdzk9_Uu5sQ843MKRI2I3_kDw3iMv3tDmCZoxo3Xg6dOl3lQ_TZY98OmXqd7wpqfO0EyhpK6D3CEwsrh_hY2yyBZWLyL5Y0lQf8XQxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FNVp-Cec6Pgn31d6vTK2m9hJCMzzRhM7N9zfBxdSlkuMzdd1ZbgEd01O0WYybxMFAMd9rOW8orpWCaJRYKILUc9AC0Bcawo6UdzVNYqqcoIY3qbjhzUzWBUs3mZjd2k0lylP-5EtWU4zUxxrbBdjxqksB4YF9ZlslMV-dIwyzWh11eqzVYSYvtneoY2nYVzZiILoPbAa0aAYrLaiE060Ber0o6YaP4xdXRYTem0qL21VEmXdzk9_Uu5sQ843MKRI2I3_kDw3iMv3tDmCZoxo3Xg6dOl3lQ_TZY98OmXqd7wpqfO0EyhpK6D3CEwsrh_hY2yyBZWLyL5Y0lQf8XQxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=lUYACJkf1QwpB9WuATJ43DCFy5gSHBPDagYXIxOt7eWTV8MtDfdUwXDuiuOcad-S2ou6nlk1m9zoKFp8VGNj1S4QmngfPEekQSGQ-MI2861Ah2cAcU5O4Saxkl80gm8rK-lTeo3nD59pkz6Zp2MQdJM4yKZjWLx60FP2RZvp90LxdZqJZLTHrHY76NVXd8Hl8eI25vY_vDlKOnIFgQS9xqp7S-8Sa8yAFowIbplx55KjrShpf7k5RgdCtHlv9U03Q3y642VCZFjr0n2E0yozZhoFFIqpebss1bKsZLbIJaCCugnbZtxb9MbK1BQs7aORi9tLG-OxFjMh7xes6-g95gupi61wjjPYYuUzWgeRrVXycPiJYEtbn5Eea4wVcVZd5kPvE1gHL4oSGTgRsP3sE8R-WnOo2bx3DD7a5KAm-c30VOU7oUgZy7VhzDf3_pJgZRIFFJZ3f_NCtr4CIEknpJM_rX2Sy9B4Ev1uwllXD-7V0cEa5bOR7L2n-PYYeuldpEWrkG4Mq3UpdZbm6gzsc5z2dZigrCW2Fzc1tViYdEf_beJ-lteggGQOAXgBreLsalVCbsPoSdnvRVUo9agMo3Rg1b4ohn6H3He7RBkPejHqxsuQI3XvGG2h2YCtBgAj8sWObrg89cbojzZJcLpO4AQBFSOyRk86fNEOheEamNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=lUYACJkf1QwpB9WuATJ43DCFy5gSHBPDagYXIxOt7eWTV8MtDfdUwXDuiuOcad-S2ou6nlk1m9zoKFp8VGNj1S4QmngfPEekQSGQ-MI2861Ah2cAcU5O4Saxkl80gm8rK-lTeo3nD59pkz6Zp2MQdJM4yKZjWLx60FP2RZvp90LxdZqJZLTHrHY76NVXd8Hl8eI25vY_vDlKOnIFgQS9xqp7S-8Sa8yAFowIbplx55KjrShpf7k5RgdCtHlv9U03Q3y642VCZFjr0n2E0yozZhoFFIqpebss1bKsZLbIJaCCugnbZtxb9MbK1BQs7aORi9tLG-OxFjMh7xes6-g95gupi61wjjPYYuUzWgeRrVXycPiJYEtbn5Eea4wVcVZd5kPvE1gHL4oSGTgRsP3sE8R-WnOo2bx3DD7a5KAm-c30VOU7oUgZy7VhzDf3_pJgZRIFFJZ3f_NCtr4CIEknpJM_rX2Sy9B4Ev1uwllXD-7V0cEa5bOR7L2n-PYYeuldpEWrkG4Mq3UpdZbm6gzsc5z2dZigrCW2Fzc1tViYdEf_beJ-lteggGQOAXgBreLsalVCbsPoSdnvRVUo9agMo3Rg1b4ohn6H3He7RBkPejHqxsuQI3XvGG2h2YCtBgAj8sWObrg89cbojzZJcLpO4AQBFSOyRk86fNEOheEamNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUYXCJV8i2uD4D-cAp2unzebxUZMREQJNzMwq-Uc6SOYWQe9AVIp91A-ns9AVF9IwoD8-dreM7olcHni_YAF5gTIKewYfmU-BiXtc5v1QophkbvUBBxCrKN2ipB8Tv_yWKJOf5EBYKt-M3GZ4sgstw69i61drWzDKnC27-dcIxueASs2GhvdI-liXyNf8m4IfB0rBOHcVruJKIjY61oa1fzE1RPXpMV9rR8IbWzkgm-4KhcVIM7ohK-kUJAGdLdWCxDSk-9bIfiaHCgTvQ47ZcxPKUdgNreGPjI-7ydkuHuXFT6jb_eMavlIKZmCYxR3kG3YJIg5o4KaZjIX3Z38ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=gH1R48orGYtkj7uj81O0jtsHGeHR_OrXG3g7krBvhCF0drrD4Z5rsA6wVcqT3q6M0mNH1n1vy6JKc2dJAtlM796eJB45qICiqmlfCMw8etOGTlVQd3ntnL4SQ-YdsVnLD-8JI6M7n1CP5xUGdT7YYZ5p-csMyIE3qFMNOhBzb2irvBfT_2FXxP78CNeSk49IisnCtqC90nAb1Y93A6-ehfoxGplXgjVW2hMKEvbsHw26AXNJi2BQYgY5unozfqob4mwpnB8nHNhn5qkSmn_tFtXAaqHAivyY629GLTRAMLLkJlqzVwJIDBPB5mSD5pb-ggxGzbr2iWCBT1Ig0LGUYbUSaKIWqKqaL33Rk3tqYTuJnr7c5ztPMbLlZ-4heKavhXiCKpja0mGVGKBUBynWegCYgI3gp49j7u3NxJtbQ20_0DOv9qrqkMaWMK2zm8HRH7AE3WVnYqP9pNw2PVopgjX4ciyRD2uX_BM4nJJt5yFQC2JFkpt45k33VNF0fB1mNBHDAQevSnnID4hZ0V9V8ZfwKfwAFS6pki7nT9-RbRkf_0Hfno6NzXmcoOYpjTeWPBXfof-KQ47uUdNMaeXqQtnCHw_srRMVduYFuXmIZ2JYgvf-qC2fdhGQ6yB9TzfgV58TTTtUS_rDTqt6NVi5f0L2cpW1YhX_b69b5-9_TQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=gH1R48orGYtkj7uj81O0jtsHGeHR_OrXG3g7krBvhCF0drrD4Z5rsA6wVcqT3q6M0mNH1n1vy6JKc2dJAtlM796eJB45qICiqmlfCMw8etOGTlVQd3ntnL4SQ-YdsVnLD-8JI6M7n1CP5xUGdT7YYZ5p-csMyIE3qFMNOhBzb2irvBfT_2FXxP78CNeSk49IisnCtqC90nAb1Y93A6-ehfoxGplXgjVW2hMKEvbsHw26AXNJi2BQYgY5unozfqob4mwpnB8nHNhn5qkSmn_tFtXAaqHAivyY629GLTRAMLLkJlqzVwJIDBPB5mSD5pb-ggxGzbr2iWCBT1Ig0LGUYbUSaKIWqKqaL33Rk3tqYTuJnr7c5ztPMbLlZ-4heKavhXiCKpja0mGVGKBUBynWegCYgI3gp49j7u3NxJtbQ20_0DOv9qrqkMaWMK2zm8HRH7AE3WVnYqP9pNw2PVopgjX4ciyRD2uX_BM4nJJt5yFQC2JFkpt45k33VNF0fB1mNBHDAQevSnnID4hZ0V9V8ZfwKfwAFS6pki7nT9-RbRkf_0Hfno6NzXmcoOYpjTeWPBXfof-KQ47uUdNMaeXqQtnCHw_srRMVduYFuXmIZ2JYgvf-qC2fdhGQ6yB9TzfgV58TTTtUS_rDTqt6NVi5f0L2cpW1YhX_b69b5-9_TQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=WiLKtfH_JJT_ub-MQ-oqubdrl7gGguxCWeUCg92_q5NdSvRx_fENtcSY6jLyyyYuGSfop-NRjYS5TXmDuOqfsohdEwQG5bRM0Arwq4nhnibosxdWKwaHoZoyI1EudMyRdOLDQBlvBo-1AfnTQLAb2B_Noki5COUbuORHPy-27CiCz32I61K6DSbI2nMbUkXqth2F18WeexKXnL5G13aQgtpi0K1LPc2eo8odfmn43LD1Ia_u9E_htWsAq3YkYkyjvGdQXfC_vjRTxcibLUCvUxF5n1Dg5zQcsgVG71Hdyl1Wph5bfhpPnzBy5V5tmXK9LySYIMAVnMVeXI9kYB_Zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=WiLKtfH_JJT_ub-MQ-oqubdrl7gGguxCWeUCg92_q5NdSvRx_fENtcSY6jLyyyYuGSfop-NRjYS5TXmDuOqfsohdEwQG5bRM0Arwq4nhnibosxdWKwaHoZoyI1EudMyRdOLDQBlvBo-1AfnTQLAb2B_Noki5COUbuORHPy-27CiCz32I61K6DSbI2nMbUkXqth2F18WeexKXnL5G13aQgtpi0K1LPc2eo8odfmn43LD1Ia_u9E_htWsAq3YkYkyjvGdQXfC_vjRTxcibLUCvUxF5n1Dg5zQcsgVG71Hdyl1Wph5bfhpPnzBy5V5tmXK9LySYIMAVnMVeXI9kYB_Zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=I9iVr_fxnnuCnBAW1YFAPxmbpScIe5PmAwbVuywob4vRBsPGUCDFUgk-vq9RZI1E1N59Xjt4CIHJ0Ha5ttJ8gSzlkfHbFqWHUslTQKktCM-Uju8jg4RlrxPVn2ILn6E8fyXjUQ6fISBLZiibkJitiixGA5daJQv8bJwLgYA_o28KQ66bP0sOHQGBOOEaCIaUWBzniCo-JsMzO1tkob0ifCAvfZCbTLkrBHBCxLcIPev8aw8Y-2PSuKu1vh0ZYxzgN3ag19BW4n77eY1r5WywY3BK_hAz30eautZhkVRsUKl3GAuPRW3_6VS-a7CJtgfAW1zwtmOHhKgbnyS51lj78A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=I9iVr_fxnnuCnBAW1YFAPxmbpScIe5PmAwbVuywob4vRBsPGUCDFUgk-vq9RZI1E1N59Xjt4CIHJ0Ha5ttJ8gSzlkfHbFqWHUslTQKktCM-Uju8jg4RlrxPVn2ILn6E8fyXjUQ6fISBLZiibkJitiixGA5daJQv8bJwLgYA_o28KQ66bP0sOHQGBOOEaCIaUWBzniCo-JsMzO1tkob0ifCAvfZCbTLkrBHBCxLcIPev8aw8Y-2PSuKu1vh0ZYxzgN3ag19BW4n77eY1r5WywY3BK_hAz30eautZhkVRsUKl3GAuPRW3_6VS-a7CJtgfAW1zwtmOHhKgbnyS51lj78A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=DnmRoUov1sQboRE3yuWu0C-6gc7Uy3ENvo2c5irRy7mi505rCblwMUnm0yCBG9WwpzdAO5OVjgt326VCMKsLgEpz1nCsqgNNjdC7MGWc7Bt9qesnEoGKGH8AosyNC1ZKClnBlFuCAeFVZKIXht395jtld4I4DgQriI-Hd5y50EjoUjVzwuIIRSXB5QYbP32XRO6D85JU_DUb_NPDzdtsEVnVqIgzMYkj9E9G4TGUboL3AzqZ4UAGAJzro-oGvSkn82vU8P6HqF4HeQ00_8QfVkD_NnsDk7NwasFPdMEkAd0FIESFuTC3bI3tXrr7pGZA-_TkllvqCy0PrOZ1Edc0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=DnmRoUov1sQboRE3yuWu0C-6gc7Uy3ENvo2c5irRy7mi505rCblwMUnm0yCBG9WwpzdAO5OVjgt326VCMKsLgEpz1nCsqgNNjdC7MGWc7Bt9qesnEoGKGH8AosyNC1ZKClnBlFuCAeFVZKIXht395jtld4I4DgQriI-Hd5y50EjoUjVzwuIIRSXB5QYbP32XRO6D85JU_DUb_NPDzdtsEVnVqIgzMYkj9E9G4TGUboL3AzqZ4UAGAJzro-oGvSkn82vU8P6HqF4HeQ00_8QfVkD_NnsDk7NwasFPdMEkAd0FIESFuTC3bI3tXrr7pGZA-_TkllvqCy0PrOZ1Edc0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
