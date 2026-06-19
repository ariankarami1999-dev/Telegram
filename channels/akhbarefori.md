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
<img src="https://cdn4.telesco.pe/file/TsJG-tXh4zslwA5kyaFRz6zZUfRB7uw_QZrhmkocBYuy7lty-Whvl21f3Wm5nTKdK3B03bMoT-aQU5C2zZrDl0OLvOCze6zp9xWXZ2-yTyoZZPAqB8oxa5keTSnxp-cPkKdICVK4t3FDstZzRgY4v-nxLv05N5fGyjx8yjbHM2ltJenkxVQDtsjYRm86INPNv8FUDgccCJmj-UxAjifGQtYxx4s9bKQB3K6zj3empbw2KpXTyaJqfK55rcXmXaflWHMO9DIcE_1-xmjeUc8cxvbR5JonH8r7vLV2XaOgmrYLeymiN9i-niPFcu5ioDIP0Mu7hJVLm9yIBaAZgSeYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-661193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a54fb01d.mp4?token=ea4H9QKjCPjkrEH636bjrIyvJc4aWY8w4CCdcTuTrQwMrpXg4W7_kvFbVaQ3EKVEvRwOc1KJwYIyZJLZW57I4S1ZSxw8Z-7TVb9EHos8KcHOat6IAfHpnoaE3kItbQb9lGOlZ4mF_rtY1IFJb_0TCQXXzjxU79aXJvWQ4z5KB-cWf6oMT-i6RWOFs-y1VVe1WuGHJYfZB-QyweWR1frl0nvw-OSgxPTi3M3ecSjWJOvbhOqElNP2Z14EYcaL2F4lgFhu46p_OUlX4Q0xeJ_GXjxDbeqNFE0ih-gT1KYbydVW2J4N7OtrgsHiUVuRUiq1C8DiAPYqn1aRPEcmPy_vhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a54fb01d.mp4?token=ea4H9QKjCPjkrEH636bjrIyvJc4aWY8w4CCdcTuTrQwMrpXg4W7_kvFbVaQ3EKVEvRwOc1KJwYIyZJLZW57I4S1ZSxw8Z-7TVb9EHos8KcHOat6IAfHpnoaE3kItbQb9lGOlZ4mF_rtY1IFJb_0TCQXXzjxU79aXJvWQ4z5KB-cWf6oMT-i6RWOFs-y1VVe1WuGHJYfZB-QyweWR1frl0nvw-OSgxPTi3M3ecSjWJOvbhOqElNP2Z14EYcaL2F4lgFhu46p_OUlX4Q0xeJ_GXjxDbeqNFE0ih-gT1KYbydVW2J4N7OtrgsHiUVuRUiq1C8DiAPYqn1aRPEcmPy_vhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ایران ۵ کشور عربی را به آغوش من سوق داد
🔹
اگر ما به ایران حمله نمیکردیم، آنها یک سلاح هسته‌ای داشتند.
🔹
از آن علیه اسرائیل استفاده می‌کردند، همچنین از آن در عربستان سعودی استفاده می‌کردند.
🔹
تقریباً بلافاصله موشک‌ها به سمت این پنج کشور دیگر [قطر، امارات متحدهٔ عربی، کویت، بحرین] پرتاب شدند.
🔹
گفتم، چرا ایران این کار را می‌کند؟ و می‌دانید آن کار چه کرد؟ آن پنج کشور را دقیقاً در دامان من نشاند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/661193" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7980096d80.mp4?token=GrKwVT_ZxSQkt_Y447jtOochv6WEcAb-NMEbEYp5g7uIy_aRPlylA8eyQ08wYDx2vICkCjximX03MaQjEthNVIDGhXTXr9s0tqwGwWE0oLsBPfaQfJjVNQ2JRL5JnUwsdvslnGcyYKf__E3eBTjglh5PPZzR6Xus9ohFGnOdSZyMhsq-XFqgY3iSPYv8uD55hBIkWq7ggDrRlZ6pOrrC7rE4w44NkYVsyTzMcq5OIWEPdG-tTYpxuuJOUzJB4R_tCM3rOFs2TDAz63H1Lg3KZGQGvUt8AObAYUGsLLXdKus3mE_y7daP0yF3mTwMfQoN_n8IiEBvGRLOXLvUilMMGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7980096d80.mp4?token=GrKwVT_ZxSQkt_Y447jtOochv6WEcAb-NMEbEYp5g7uIy_aRPlylA8eyQ08wYDx2vICkCjximX03MaQjEthNVIDGhXTXr9s0tqwGwWE0oLsBPfaQfJjVNQ2JRL5JnUwsdvslnGcyYKf__E3eBTjglh5PPZzR6Xus9ohFGnOdSZyMhsq-XFqgY3iSPYv8uD55hBIkWq7ggDrRlZ6pOrrC7rE4w44NkYVsyTzMcq5OIWEPdG-tTYpxuuJOUzJB4R_tCM3rOFs2TDAz63H1Lg3KZGQGvUt8AObAYUGsLLXdKus3mE_y7daP0yF3mTwMfQoN_n8IiEBvGRLOXLvUilMMGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نانسی پلوسی درباره ترامپ و ایران: ما یک توافق خوب را پاره کردیم. به جنگ رفتیم. متأسفانه جان آمریکایی‌هایی را از دست دادیم
🔹
ترامپ فقط نمی‌تواند با این واقعیت روبرو شود که اوباما در تمام این زمینه‌ها موفقیتی بسیار برتر داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/661192" target="_blank">📅 21:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661182">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHB0y0Va1Ls7gPgYM1Bfrmses8cY3Oywz-4lR5FNhOPF17qUE0KUgg4QsS4VAtfRNudBIEq-_gR3B62jjiKeIIrMSA1HKoa5m_nq_ZNMeDP0XW5uLg-vgUeC26SMMghr7GNPoysBY3KBcnkF6hxSX6wm-Bn5Di8U37ziaYZMDagn0_QXeYob_NV23b3C9KbewX1kppaFeVXwrpJm6slhLGCAxl-y4ncRPDjZ8N-V27aFeyVAtVz5S1vt_eHqYCkfClpIZk2oRISxLJdkq93-W-P9zcG4xt85uDUn4uRFGzbL8HsYZuOvY90GYSDihUbFK206kVQGvkKC7lU3SWAmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILPL_7is-gDDHe7I9xScXAtF9aLkQMZYOvF4w99vkfYOZzY_7bj3ic62SUEocz6X54rrYLrOFN4DGUNrOQSP-5tgaTvvBrBnwQRsK-Nqdavqk4uOgl4c4wCCbcLOLTgKgXJacOtF8mKbDlXB3On-Q8kK8VUzB65_qjntVXXqaIvE0yPAJ_yjhb9-1za6_2aEqkAxlu9E6ztn3wZGo4feCCDmF1l4lZDeMe5sxGXNvr9Ls32V9f0PZj45QRg18bTXqk89WkVj9d9GHvfRvTPYG7V2z1-JrmW7eIYnOhdGK_m88H7RJwwD6w0eDJwqVUNaDERyvL33xMGq87ydygJ5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXjaDW4nzsaUt9gmXQBDhrDSHH6bSnK7w5FIadk27JY19_tm-oqrk9oD5xSB2w1ipnVKIGtlhoD51h9LrUBHvvBD-MDpQPuNx5Mp3nOxTU_cAEvtlHr6KvFqDJv_4ekW34xIGMduo5Y6nAmQu6I7uD0PfKPr_QyXVZehYPdZ4He4-gqch-XTrdlT3FmSNmL-ds7vE17RaVHiAbTsgmaY54LBVLd1m1LvQnohrxflIeVX1pHIRnkAwLsRQpoYwDDJmbGVHBnBIqAUyvRrrNvp28ID4bDLGZv90Jp_Wq0iyPu2ivasaeKdfVs8yM0xH30pEsH3FncJFVUrhZdBV243wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5h4oowO7u7b4NTM3vgH5hIPqKoGmL1kZ4xdF-KPudfu_5RdqZqngD0SWOWH-TMk6o_L9XFes1UmoZb1cY0AscMz4Zhmf5sNNfRWiCqg6aJXghGMpTEVziV1_W0LHhA8huYwpErRfwsEzFaeVuuqJU_VJ6XMnV9YDhCKIxof_PIad4_Y8lG9LUW5fkM6SvpGXLiJeYa-1lG2DMRSAjeiTG92S1rxGSElNH571eps2jsjt2k38RnLNcq942fSQJ1VpCYDACUO5K0FaNZD9T-l7qUCc-9fooynLHuzw44SYdvUGqdXTlbS00vkDpgAqGYZXRrY55_0XBC3DC8DStn-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sE5isTyMUVApgfwtVDKvqF1YcepIEoEF4IHoXeTAhekId61x0dINFbAZOqvz4CtcDYFlpMhaFfjegGRUFXbg0ZB4KYtBKCePnWmCVoWzvOB1R3xaMGws0CuwIUNGQEyMCPddNolv3VSREVHA15Urk8fvhiZt_ngILscUY2ENGp0vniUPsjYGAukZMYPoi5Z-KFWk-o7EZ7jWkOpnS7BnCjcHw-uAYDP2i20PRqmRuWWUuUECAOrVUKjoQnBBe01UniamndQBmXNBg7XkMJFVJ1UsTCWjMl8L-mohhujpezVoAhOrGXwRsWsm-1BJ6dzsObnhMW82HaRgKlkzxMhySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkfLTNGzgng23En8AAh4Jk2iNYDJcA-3qcvM3zyMvVdngEqUvHRgnzW9I5gr-43GwDcTwz5M_Zxoxjp_5X-kN3HwRdfQWYiw9WBqUK-gJsMw8108I5fm9omuNsy5yvc_YIC11Bc8qRK4pG2ibzjK4eEyy_pQ6dzvFDmxyShawp1qFm7tcmgKF1x8_ALHIwxcXpwq3QD_p6REq6-l8ZK0F398AlEpJFpGI5cWBCQISBVHcyODf8WnXVSRzbHewdETtcbHuL4RF5Hl-Gchmjpf-IKzfOCZwBA4KaJDdZ38Zq5nHNYHH7Ij_nfYX_3yZHstdYKnIo_PfHd1xyPcPtqrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfjAmVtFfJ8BWbdhD53eFen3ihbhYnDW_m5LmeDDqhOwL7uASuHy9ZetLkPOlF5xnuYbf5tWeFE-7L0uPU3GQqSwTy7KeyPFbPTkvLKvb0hIl2Ku-ftdAQc-9dDnj34C9LM7cftqku0hR_oBnNIOKZntDTfZ_Lml3alI7312GT-C9SxJK8ojpby_SZFc1TnxBiWiHW0CPsJwTBZwcOCYjZpzRrQ3AONLLO5dHKGV8KdYsQ8ufj3TvhJZLTacO4N7CrurAaosCvXvdlDX1no8eAwViUFqSUzhQb6eq2GBjkROzy9u8ziSJaB2Ic11fRIW2dq0Ss-hHjgq59pT7Kqo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TENVQT761ieyPhiSrkPMzXJhYJRE-99U1q79BoHDrGRa5zih_oEFHFu_qjbn85nZMyCwZMecYxLdZuIEaKgPllX_syiMSx5rTTNIQdCNxWLjEKu9xapmzbBjjqKhURUi9rRkEwsvx5eVDWsjvQWcI4aE7pVFkesC_i_55_10NuZA4mOACBLgUMtcseq8NBSLmZJqrz_aNt4IFESxRmI7BOF4urdi_FIJycEphM8PbwrfjdpFALYSYCeMwbzALhOAXCwjGPTMeIcZe1eygVZ4znSls47ii6GmRlQgOs_tYFhz98HUJvUoJsRckLT-Ff-760ahoCvBX3zjgMIqAO_3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulDuXrxb4eLwDQYpJJjHi02c0i0b57bXTZoylJprXfeVzpzV4R9NPOBew05ZvgdSQfdkabRlGgW5y7Rk9TJ5zT5eDLN1ej6QCDtHIEycTvEGbF6zx_Q5Mu5MlMAUXs1zGTSWcbPAkvTP-TV2EFbn6tIfsC0DfTbZJFR3S1rL8OeDVw92IkfDz6WoDhxQrADzPmG2aW0GotSbBILKNJzR_ANzzPX1y42An37woq4qT7ldlwK0ncrQEnQ1d04t850AmHTtNhVbMAwa32zPCFK2Wa5LPzSwd_30N-30xXsxG5TH30YXG0n2Xf7WqwjiYHCaj1v25nyB_JKfa9XIp5mjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1FYgSNCnAOjB_T7O3jQGn3-c1Rl-v-j0KoU37c9P7wXbwKMwBjf1TGeUG9npfcJ52HJjjGop8V7_g869kS2motZxNh3ng4txcMuoPc9MTM2DNMkc-XfxJINFLjEd8jPJ125y57ZcPQBizjYy6_yNtDt3UfBpGVmvORRrXO1QcapaeOJDdy9cnGTWlZ161YJQxViWUoxqGAJ8w1hM_MKXkx7gy1yVwXVg51Q8HDiaURHztFJRlRTt6J6M1mG9h8GAJs6AZZB_LFfsf7wBmhGsfZwcakeR1FFTyPEieO4h_VmlmMBHz1RIGEIq8_5jTysK-H-Yq5jr_QLZWpCIzGyNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
گوشه‌ای از تصاویر ارسالی مخاطبان عزیز خبرفوری در پویش بزرگ شیرخوارگان حسینی.
🔸
شماهم میتوانید با ارسال عکس فرزندان دلبند خود به این پویش بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/661182" target="_blank">📅 21:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661181">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای سفیر رژیم صهیونیستی در آمریکا: عملیات تهاجمی خود را در لبنان متوقف کردیم
🔹
سفیر رژیم صهیونیستی در آمریکا مدعی شد که این رژیم، عملیات تهاجمی خود را در لبنان از ساعت ۱۱:۳۰ به وقت واشنگتن متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661181" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661180">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwuPCZK8nL77ExwZb4T7z9nBDqWfjmHxuC37DGRDCnouIfoBGRJX8z02BSP-uSq97D9u1ESqA0pwiRUqIbQJS0mCU8cZtqTzl6n-JS1mcvlpoaKLrnAYprgvM3vWSfxIHHeIfIgRSW9jVmBr4GJYwwPGdHkkWgMUeZyvKyzqNRSEMkw3_jM7AmLDBMQxPbivFtY5HoAjJZQfbygEy1COEq_kqJKQXcB5DSVaULBRM3s0EUK8lCubrSlgSauw7Zx4jl6dGGdCLutAjBr0aRSAfBNYMebMdxcIIrnMRygPHUUqWoxGcmQFiQdFAGq-0jvKnMpL7wM9ldz3NgbK4FTu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: غزه هم طوفان دارد، مراقب باشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/661180" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661179">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8f63c4d0.mp4?token=o6BxCegIV6vXCHJwdbawHSwLklTa6eh7p9QUy-Tdk8FcPMs4F_bIGhl1Z1tdrPBvR6nYdr-cFQcOSyNa1lPeLW1zwqSHH31fOLH7aN5MRulc3RhC0muDQYrfxUOQ7dvLy-o9jtQngCdvRMxliWbPOvWde8WSjp_Vve53cWk5gk3sgK38LBVClCscvKIantQ1MznmaPhihxV1WlsJ58h0m78xAFhlbQxYPOPvlGhcZv8ByI25sIMfx8GaMWgaXrcS7RCnPxSFxgYI3DBMy3x7ACbxsC4jeHa82eTwmxcjS0snLGf-gJ3T6IfZTI1SRGXAGNcBFgjTVC2yfUrqGqprYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8f63c4d0.mp4?token=o6BxCegIV6vXCHJwdbawHSwLklTa6eh7p9QUy-Tdk8FcPMs4F_bIGhl1Z1tdrPBvR6nYdr-cFQcOSyNa1lPeLW1zwqSHH31fOLH7aN5MRulc3RhC0muDQYrfxUOQ7dvLy-o9jtQngCdvRMxliWbPOvWde8WSjp_Vve53cWk5gk3sgK38LBVClCscvKIantQ1MznmaPhihxV1WlsJ58h0m78xAFhlbQxYPOPvlGhcZv8ByI25sIMfx8GaMWgaXrcS7RCnPxSFxgYI3DBMy3x7ACbxsC4jeHa82eTwmxcjS0snLGf-gJ3T6IfZTI1SRGXAGNcBFgjTVC2yfUrqGqprYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: از آتش‌بس با ایران خوشحالم/ وضعیت آمریکا بدتر از قبل جنگ است
باراک اوباما:
🔹
خروج دولت دونالد ترامپ از توافق هسته‌ای، ظرفیت هسته‌ای ایران را افزایش داد و با وجود هزینه‌های سنگین جنگ، نتیجه نهایی تفاوتی با گذشته نداشته و حتی ممکن است اوضاع بدتر شده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/661179" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfbc62e7e.mp4?token=vYd7gAZNdR6n-2iC4RwdevX8zWg9DqeKxttlsZ18UJ4gFc30czeIx4WA1sZuM7g4F5EGD-QOV3wWuykfVEu5AmWTgI5P0CJo5hhXKGKiMYNBI9p8avQHvXp4m32Tvsgs-btqJQeAdAey_uXJHeSbth5RNCotiNENOxjNMGRdUEYckMzUIIrLkxkfXKPKBwa0KWqTOsmMLH35YAfDg7DAgMWB8MOBo9gZmkF46MpxTNR8sOY0SGdVdnts53InD41jSCzTQf00I7N4Hj68kIw2-484s6mtPKf3Pn-4OtRH9SZ1hBAJl2tIjBz70RLrzSHbjeGiYwJr-KeY_Y4rv1f6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfbc62e7e.mp4?token=vYd7gAZNdR6n-2iC4RwdevX8zWg9DqeKxttlsZ18UJ4gFc30czeIx4WA1sZuM7g4F5EGD-QOV3wWuykfVEu5AmWTgI5P0CJo5hhXKGKiMYNBI9p8avQHvXp4m32Tvsgs-btqJQeAdAey_uXJHeSbth5RNCotiNENOxjNMGRdUEYckMzUIIrLkxkfXKPKBwa0KWqTOsmMLH35YAfDg7DAgMWB8MOBo9gZmkF46MpxTNR8sOY0SGdVdnts53InD41jSCzTQf00I7N4Hj68kIw2-484s6mtPKf3Pn-4OtRH9SZ1hBAJl2tIjBz70RLrzSHbjeGiYwJr-KeY_Y4rv1f6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: در درون رژیم ایران هنوز عناصر تروریستی وجود دارند، اما در عین حال عناصر عمل‌گرایی هم در آن هستند که واقعاً به دنبال برقراری رابطه بهتر با ایالات متحده هستند
🔹
این ایده که اماراتی‌ها یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، در حالی که ایرانی‌ها رفتارشان را تغییر نداده‌اند؛ به‌کلی پوچ و بی‌معناست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/661177" target="_blank">📅 21:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661176">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
صدراعظم آلمان: آتش‌بس مورد مذاکره ایران و آمریکا باید در جنوب لبنان برقرار شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/661176" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69065e0edc.mp4?token=FwA8OBdAvOfJQRmRTfW5cEwm-3pZAFpiGJgUaXupQL5pLB_EL0PKIY7e0NmQwk_itccatqqzVsoyQbI8kJVZ3VoAa0x-_ckE5MX4I-bJTOEwRIlSxLCxFMbli4pbLcrxYwXQMUKnW4mU6zBaFGehc1AQveLwHSj_QAgU7-NCMp0SiAdKm3hM42bQGTLisNVDsPm9opFeYU8kDWeMVF5xK0C6-c9KCPoiZ5oIgwdCTO9hcdm_wWLaQpIrHjNlgmCr1vePipT_A3qh_Em9joK9ovvTZ0xSBhbEH_wcHu9KRyfJ9V0d1FrhFtOuKMHJHX8C1JvoYKoEOLS6hHhT140D6ScygCJAKh4voQYMIu1FI60bbzZlvd8Xo_67KhksGyfGJTA31EAV87jv5rSyTh-whXFnQKhbrlp9NlbCu02-M20uvW_9ixf0pypobQ0dP3jOA_ffifkINmkF_pPpEIVti2p-YugGcC1faRPEdAuqIji_H9CfsaYyuz9Cy-OmciSOGhtv1mH7TzjGj_WYyLy1juQkCmvWvnyOHZUTXOXRRNh338ZDy34pt80zjwZGMrotAjqBcN4MqTPy90V3591AMlBDactpL4YsQ9hHun9ZsZ5T0utFTuKP2otRkIEv4KYw_TwYEeaeRnEbgLuKBKhztv17vhh36_iUeG62enIw1dY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69065e0edc.mp4?token=FwA8OBdAvOfJQRmRTfW5cEwm-3pZAFpiGJgUaXupQL5pLB_EL0PKIY7e0NmQwk_itccatqqzVsoyQbI8kJVZ3VoAa0x-_ckE5MX4I-bJTOEwRIlSxLCxFMbli4pbLcrxYwXQMUKnW4mU6zBaFGehc1AQveLwHSj_QAgU7-NCMp0SiAdKm3hM42bQGTLisNVDsPm9opFeYU8kDWeMVF5xK0C6-c9KCPoiZ5oIgwdCTO9hcdm_wWLaQpIrHjNlgmCr1vePipT_A3qh_Em9joK9ovvTZ0xSBhbEH_wcHu9KRyfJ9V0d1FrhFtOuKMHJHX8C1JvoYKoEOLS6hHhT140D6ScygCJAKh4voQYMIu1FI60bbzZlvd8Xo_67KhksGyfGJTA31EAV87jv5rSyTh-whXFnQKhbrlp9NlbCu02-M20uvW_9ixf0pypobQ0dP3jOA_ffifkINmkF_pPpEIVti2p-YugGcC1faRPEdAuqIji_H9CfsaYyuz9Cy-OmciSOGhtv1mH7TzjGj_WYyLy1juQkCmvWvnyOHZUTXOXRRNh338ZDy34pt80zjwZGMrotAjqBcN4MqTPy90V3591AMlBDactpL4YsQ9hHun9ZsZ5T0utFTuKP2otRkIEv4KYw_TwYEeaeRnEbgLuKBKhztv17vhh36_iUeG62enIw1dY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اخبار کشتی را از دور پیگیری می‌کنم اما بخواهم درباره‌اش حرف بزنم به پراکنده‌گویی می‌رسد | اول و آخر ورزش ایران کشتی است
مشروح گفتگوی خبرفوری با عباس جدیدی را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223561</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661175" target="_blank">📅 21:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661174">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نظم عجیب و شورانگیز عزاداری یزدی‌ها در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/661174" target="_blank">📅 21:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ان‌بی‌سی: ترامپ خواستار موافقت اسرائیل با آتش بس با حزب الله شد
🔹
ترامپ امروز با طرف اسرائیلی صحبت کرد و خواستار موافقت آن با آتش بس با حزب الله شد.
🔹
ترامپ در گفت‌وگو با ان‌بی‌سی: من همواره رفتار خوبی با نتانیاهو داشته ام، او گاهی باید آرامش خود را حفظ کند و از عقل بهره بگیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/661173" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661172">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geDjnP454EF9-8PEeUVy5mHz_9zmTRvzCs941CMni6NmRQ7LBKCy-ZcwEg8YA4ne25zP-o-5-v1_b8v54mWXrSJihAmeEkaYPGxC_VumJcfCMqGGfbOxF57Ti_aJMA0v94AGoEmE8NICT0o2ejADSWUEVxswplI1tvoizBk58J96O-b5hRypGpyn-Fjx-gOuUDFBCwqyC8LY52pK7eP7iiYjPbL1JO88L134hdhaxVV0Vhea-5wiLFxpMDvkNT-WfMGbhLGwuKq2_-jQbpqPUtZlT4sm1dUCCn_ky4wb9qWUjUxr5MjQS4tKdIjDPXkX3apgDot308n4OFpsQPs8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: آمریکا باید بسیار مراقبت کند تا صلح قربانی شرارت ذاتی طرف سوم نشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661172" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a70075c1.mp4?token=oBDy7nU_r89zHIGGkQ-bmMFGqfzL5SKh7_9oNipWoz4gZQLfPzVwBIgfvqd8C6PbiniAoemwucjY1V5KeVxtH-fscxqHx0-S7-xwivi7hIYPcLrbJq88xcc46D-NVNJb9Bqx2OCyPonOE7P7oKYXZEWQcPZ2eqF1VfSM-hr5IX1zG6F_HdudtquaqQkSO2rkWYNOnzFefOa0s54bTbpfiVf6Ewh8CKL6LbtghfpO5rH4ZQ_TWCuSH158mDTXOZp0Tmsj1tlRUbqpFpNjkNlCAKOIMi-EwpqpKkj-ucJSLXZoSHZkN1Qc7H9qfOon8qzpW9X_xnInFMjbwhELQw4IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a70075c1.mp4?token=oBDy7nU_r89zHIGGkQ-bmMFGqfzL5SKh7_9oNipWoz4gZQLfPzVwBIgfvqd8C6PbiniAoemwucjY1V5KeVxtH-fscxqHx0-S7-xwivi7hIYPcLrbJq88xcc46D-NVNJb9Bqx2OCyPonOE7P7oKYXZEWQcPZ2eqF1VfSM-hr5IX1zG6F_HdudtquaqQkSO2rkWYNOnzFefOa0s54bTbpfiVf6Ewh8CKL6LbtghfpO5rH4ZQ_TWCuSH158mDTXOZp0Tmsj1tlRUbqpFpNjkNlCAKOIMi-EwpqpKkj-ucJSLXZoSHZkN1Qc7H9qfOon8qzpW9X_xnInFMjbwhELQw4IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ایالت می‌سی‌سی‌پی امریکا‌ را درنوردید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/661169" target="_blank">📅 20:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: تماس بین نتانیاهو و روبیو، وزیر خارجه، به زودی، درباره لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/661168" target="_blank">📅 20:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نروژ استفاده از کالاهای تولید شهرک‌های صهیونی را ممنوع می‌کند
وزیر خارجه نروژ:
🔹
شهروندان و شرکت‌های نروژی نباید از فعالیت‌هایی که به ادامه فعالیت شهرک‌‌سازی غیرقانونی اسرائیل در فلسطین کمک می‌کند یا از آن حمایت می‌کند، استفاده کنند.
🔹
ما ممنوعیت داد و ستد کالاهایی را که در داخل شهرک‌های اشغالی در سرزمین‌های اشغالی فلسطین تولید می‌شوند، برای شهروندان و شرکت‌ها اعمال خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/661167" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای نواف سلام، نخست وزیر لبنان: هرگز بر سر حتی یک وجب از خاک لبنان سازش نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661166" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
آیت الله علم الهدی: نقد و بحث کردن هیچ ایرادی ندارد؛ اما ما حق رویارویی با دولت و وزرای دولت را نداریم چراکه مثلاً با وزیر خارجه نظام جمهوری اسلامی ایران برخورد کردن، به مثابه برخورد با خود نظام است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661165" target="_blank">📅 20:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای مشاور نتانیاهو: اسرائیل تا زمانی که لازم باشد نیروهایش را در لبنان نگه می‌دارد
ادعای مشاور دفتر نخست‌وزیر اسرائیل:
🔹
نیروهای اسرائیلی تا زمانی که منافع اسرائیل ایجاب کند، در جنوب لبنان باقی خواهند ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661164" target="_blank">📅 20:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br6O8VpSsHyNv9PKE0mwVwoOe9PMF-dKXfh2TjS70bYNVtlDfdEpaAvtRYEm8pyfWu6rRny0G_pQv8LAU_AGBeW8_jEGJSlgzzQ8_1aKqDDjltDS1HDTGozhhCPKIHLfnW9ZaXIIgo6lLAykgeg3EW1OKjY7H1psHM9hypfzXhlXLIUUHCTsYiCm9TeaTotQB04gAMLCZp90_SxMhbZCMpzRuCsfmcxlx_e_CvXY81Viqw6RUs6MqqNQaCdjfzAOmmBaVnuvhMABPyJp_k0uJd-KG_HMS1v2b4Nvc6oKGJ1bIsM1O0D0bEmSSqOvNllIR52OoVz63z_2L_xZHKfAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باراک راوید: حضور هیات قطری در سوییس؛ بدون حضور ایران و آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661163" target="_blank">📅 20:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXUjjceHr3E0h_IBZDrqxgG8ibuErOSNbfLOUDy4mbxh__f5PRXHKV6nR4APCchNEDqR_LZ7Kx5FY27akei4NoyJHWwLWDxrxiSJ7SILuR2-6GJgs6irlp5LT89y1e9kjSO4pODvD3wAz6GRY0LffEuxxHKGo94JQ4Nx-9SCnMFJ80HbOQKmgugzOEJCN-cpBzCPg65t4WEEx0v2DGJtB9SxKCUxY-g9dmLIjBdW0aU-azEM7DZHV6TB7fhcoFVqUU3OMqKtp6ck5jNi26oGDV9yAvbusNwxqH-tHWW_iKmsMBg93CLKKDilBnHYKHebhIiQKl-LCdcaINtWgEnAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVP1DjfPCl6ucMIcQQbnmGSGxNggRFoWKYOIzBnbr3bxVyHDQgh04C_o4ma9VPQ0BPYEgkKaK6Z-G516_XSa7yJY0oXlmzIFqGIVPjkOHuOX735oJSN5mMEx93U2hd0CWdVf5TQcWdiIxp_tXLgFhleZOtMTNUBt5xKNH9356cKxELY10zVrUNaLlUbRp_2N1zqwVLhkxo7eTkZdPOMHJGtWbZdSGRAD3y5rWUsBZMACcvr_OXx0w55_fNXiOsCl9wG9KHw3uHQEBqVGqVB0qXnjazb1HQYqqOd-mVH_OlKkbLXXA1Lo8YU5bt7VGHWA8LDCNAk_e-nPXSgfOrE7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSKfskEiczIE0h9KfHiIfYVeXQ75iiVzLTkjXU-Z2Mru-cUlK80v7RT545MsEJlAHHFdXEUEmKKQfiW2ujqMQDhP6o2g9W_B5O1vynKqW-P372_CoEigng-WxxZUySjvIpq-8qwtGCTMPWZqTivQ0ZAEvJp0QW0ZneZ69n_QcvqxF4_eEBA42hjdvQXqYIkuRGIcbSp6BhXBFnuMyIU_t_pqTio9--QV_i14CDUzSi9keFPo3cnQk7rrlz3Vez20fbVZZi6BwCXPor1GjcIY1IJ8tesq6WydnNxQd3yQKJaB_OEUkEdeRotqXObPcTw8b8jY06gGXPgqihqSH0OdIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ اسموتی خوشمزه رژیمی
🧋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/661160" target="_blank">📅 20:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661158">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMo_0yErWUO3ne59hX2zIFO_zFWtpTJsNgJajLJ5jRxB6qKBCc4LSb8BnQji42L6RUni9PPOS7U7AVru52ZlyJIIKGaN4vOSms-msjtmpUT6TVhO_bmduTnSAeVOX65bbVDqBg2Okpb09F8eygM8FQHdLEPzCvlIbyyTKJ3dnPkVKnCVynhCSd4BJ2Dl8SY6M1wSsaTWkvu01v_Omr57CDnzCPqrYHFM-vzkM7J5ysroe_HQT2wAsPRbcqPOxzRiHMS_PYbJDGev-lIJ03l6h-iNXhqhbE16rgW-io5Aft-X-dqHbgGKXQxK2ESzyhgBkcXREpZMRSFAb4M_uGy6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت الله علم الهدی: نقد و بحث کردن هیچ ایرادی ندارد؛ اما ما حق رویارویی با دولت و وزرای دولت را نداریم چراکه مثلاً با وزیر خارجه نظام جمهوری اسلامی ایران برخورد کردن، به مثابه برخورد با خود نظام است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/661158" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661157">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حضور ۱۰۰ درصدی کارکنان ادارات هرمزگان از فردا
استانداری هرمزگان:
🔹
از فردا شنبه ۳۰ خرداد ماه ۱۴۰۵، ضمن تداوم فعالیت ادارات در ساعات ۷:۰۰ تا ۱۳:۰۰، تمامی کارکنان ملزم به حضور ۱۰۰ درصدی در محل کار خود هستند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661157" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ماجرای شهادت حضرت عبدالله بن حسن به روایت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661154" target="_blank">📅 19:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
واشنگتن پست: نتانیاهو در پی تضعیف تفاهم ایران و آمریکاست
🔹
مقامات اطلاعاتی آمریکا هشدار داده‌اند که (رژیم) اسرائیل احتمالاً در پی تضعیف تفاهم صلح ایران و آمریکاست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661153" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661152">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMKj8R3RoikmnjBWplLIYZoa0m-v6kzuZY4A2HMKmRdbpP1964Ta6JQ5BGjXeGTGX0xb-nmf0N6UO88OakRK1uRwNTIt7NzhwMH0AYBS_jpUydj0RNHA1yoTdWxp1gO7Ofmrksxne9XJItxMEX4r4F5He0rmQjPOqVRc6R2I-PBnOoLENcriXZUQdcQNpfRM6l3sY_gqtFNB6Ya-XoWbrP7qWMl5IMUoHK-0Gg_nMcYnujORAJRtSPUXnA94VNutiDhestR8aKX9xi3mP2vFbcbpowwBDFRbnjm4DY38c3TPsBjChg3rtB-DRY6qsn5QnVdUtxwnP9VmLkLKeuJLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس نظرسنجی مؤسسه کانتار (Kantar)، میزان محبوبیت ترامپ در اسرائیل طی سه هفته گذشته با یک چرخش دراماتیک همراه بوده و از ۲۳+ به ۲۳- رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661152" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661151">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
کمیسیون امنیت ملی: تحقق کامل شروط رهبری در تفاهم را تا انتها پیگیری می‌کنیم
بیانیه کمیسیون امنیت ملی مجلس:
🔹
ضمن بی‌اعتمادی مطلق به دشمنان، «یادداشت تفاهم اسلام‌آباد» را ترسیم نقشه جدید امنیت منطقه‌ای و بین‌المللی دانسته و از حیث وظیفه نظارتی مجلس با دقت تحقق کامل شروط رهبری معظم را تا انتها پیگیری و مطالبه خواهیم کرد.
🔹
ما معتقدیم استمرار این پیروزی‌ها، تنها در سایه وحدت و انسجام ملی محقق خواهد شد.
🔹
این کمیسیون در بررسی تفاهم‌نامه اخیر، رهنمودهای مقام معظم رهبری را فصل‌الخطاب و نصب‌العین خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661151" target="_blank">📅 19:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661150">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f12180799.mp4?token=vPvw2pijMV7fkYhOgI-HY9TVq97xeh1bTG7k9hArvKymVaR9MwuUMotaux2rO8f4hIGmrWDonXPqYvYYN3ISd3KY23p-8B4zs0BtMk-L0qqzKE0HYyj1h3POoNv6XfgoMj4EmJsBXipykSoymRU-PAlSKVHwXeMIAuu3EHlBj-vztG59p2z8MtWoFxl6qEKrf_KZqdgZBWlYBk2Xf2_GAcxcmPFaYof5dIYLOBtYMDW2Z_DVNZ-jRVyTug7VZQH-oYfMqx8SmhOC9CGKEmuKpB68FBjeCuBiVJs8GEe_wnyiVLUGkZo2EibQXBsQzAM9AI0dLK6YTpaaW4RXoZVmRE8FOkVIz365jGWxDcJuME9gilmN2eB_P2qpjRq__BsRKBzVa1HXjsIvOUfRiCU9q65YlhHZuu6drAkeC8tN2iETECKKvz9wAdf45iO1dFlyeydLEJZOeOhBKcuyDj-SsGyCq7TY2W8_Lgl3ZaIEQYGYLGCisHEWdSDvj_yjNIP4dzZsi1TnltdL7iDZ6wcld6qaF52xEPQnKoAO86evAXC0-mDidzs-Tcjx3f6n6oTPSnI-IVE24zw0DWQDHGwsWWUCSCt3AwEDFBu_3mmEttxidX27Iysu21cSgK_ezzBIg4v5CVR0BSK9A9mNb42Ubv85nhBbuJ7k1I7ZWryRM9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f12180799.mp4?token=vPvw2pijMV7fkYhOgI-HY9TVq97xeh1bTG7k9hArvKymVaR9MwuUMotaux2rO8f4hIGmrWDonXPqYvYYN3ISd3KY23p-8B4zs0BtMk-L0qqzKE0HYyj1h3POoNv6XfgoMj4EmJsBXipykSoymRU-PAlSKVHwXeMIAuu3EHlBj-vztG59p2z8MtWoFxl6qEKrf_KZqdgZBWlYBk2Xf2_GAcxcmPFaYof5dIYLOBtYMDW2Z_DVNZ-jRVyTug7VZQH-oYfMqx8SmhOC9CGKEmuKpB68FBjeCuBiVJs8GEe_wnyiVLUGkZo2EibQXBsQzAM9AI0dLK6YTpaaW4RXoZVmRE8FOkVIz365jGWxDcJuME9gilmN2eB_P2qpjRq__BsRKBzVa1HXjsIvOUfRiCU9q65YlhHZuu6drAkeC8tN2iETECKKvz9wAdf45iO1dFlyeydLEJZOeOhBKcuyDj-SsGyCq7TY2W8_Lgl3ZaIEQYGYLGCisHEWdSDvj_yjNIP4dzZsi1TnltdL7iDZ6wcld6qaF52xEPQnKoAO86evAXC0-mDidzs-Tcjx3f6n6oTPSnI-IVE24zw0DWQDHGwsWWUCSCt3AwEDFBu_3mmEttxidX27Iysu21cSgK_ezzBIg4v5CVR0BSK9A9mNb42Ubv85nhBbuJ7k1I7ZWryRM9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش سوزی جنگلی در شهر اسپوکن در واشنگتن
🔹
آتش‌سوزی جنگلی در شهر اسپوکن در واشنگتن، دست‌کم ۱۲ خانه را تخریب کرده است.
🔹
مقامات آمریکایی اعلام کردند که بقایای احتمالی انسانی در یک اقامتگاه سوخته را کشف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661150" target="_blank">📅 19:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbf1zsHUoqDKoHjka71849RITc-PAgzz8sK4E26mlOOrhKCWhglB8LC3B0BQLPLZ-R4Rt5MRJFW_3xPoKQrR7H9l5kYHZeUOE2yzbGQi8zVAfsWbMYoNi20nVXgd0KJPB2ZyL-jEBD9WVL0C4UtlpgEXyWl449cuwklSZdojo9yLVnHhbqra7wac43qqi4yvT9uHvDFYmsFW-X4jh9e0L5PKkEEoHlG_2a7LzzYLvQcrO0KG1Wing2F08yLOLknDgVPwEJUl-gnKIXG5FQZTojPIU50V7fNgoe7XFGq2NIE-5xKe4MXt35FpTc6O92fZ7yK0uZbJsoDZ2zyRJbdWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک صنعت و معدن در روزهای جنگ رمضان در کنار تولید ایستاد
اعطای تسهیلات برای حفظ تولید، اشتغال و تأمین نیازهای ضروری کشور
:
🔹
۲۰ همت تسهیلات پرداختی به واحدهای تولیدی و صنعتی کشور
🔹
۴همت تأمین مالی تولیدکنندگان کالاهای اساسی و صنایع دارویی
🔹
۱.۴همت تسهیلات پرداختی در دوران جنگ ۱۲ روزه
🔹
۴۰روز تداوم تأمین مالی تولید در دوران بحران
دستاوردهای اصلی:
🔹
حفظ پایداری تولید و اشتغال کشور
تأمین دارو و کالاهای اساسی بازار
حمایت از صنایع راهبردی و زنجیره تأمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661149" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa784dbea.mp4?token=fi9S0sJqYHPX76Hrr3nND89eT3MfuujCAwTxraTIC7UTGsha_9aZghsC5BPIpfy9MyN3A0vBTyZy8Solq9fgzRmdYoLBIVEO7WqFK1O5RYP9qf5oVbzSMuTtSKYbPg9LqdWmnZ2iNPdDQfbEmbolmh8WSLvS7LiNut3QYspyK7KZWz-4SbWb-4T16n81y_w8TtvYC8Tx9Ge3ndPuJAH1ZCSfAHwjljSpryqpi2tKw-4Ycbts3LB3OaukWAC1x6_XzeVAbYG8HSaqF7GDsvlKe4XWG1-cbwlMXxbP7lkfThtbuBqe5C4DvnUiTBSSJXcR3M5gpyaaRE6DSHVnSouWFY77ZuLTwbWWpsU7q-KlEZHIGIjeQGlbGBYMRowQg5S3Ud2EmHeobO3s1mJM6vOHF4I2b2IRUwCQMiZunK4FqYYFUdodI2tcW0hhDdg2JN0iQC6r-9hyWS9Vny_dltQjpOfnuEvl9b9OGwArzfVsUoT5icdTblz0dCQet0cUXJJ8eb6e31LlrUvm7iLbLuzKFmu0jC8TQmruTc2bEQ5TnxrSMWdvEA4PTjoRTNdCbIgTBq8yd8fhsmlfVIaDJTmlroeNSRrHQWZX6If0triT-ezymQfXFM4MaCgLoXS6l_nxkfYKpZn6_AtXq6heK4Cg688hbG2JoVyUIZYl_MDhKF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa784dbea.mp4?token=fi9S0sJqYHPX76Hrr3nND89eT3MfuujCAwTxraTIC7UTGsha_9aZghsC5BPIpfy9MyN3A0vBTyZy8Solq9fgzRmdYoLBIVEO7WqFK1O5RYP9qf5oVbzSMuTtSKYbPg9LqdWmnZ2iNPdDQfbEmbolmh8WSLvS7LiNut3QYspyK7KZWz-4SbWb-4T16n81y_w8TtvYC8Tx9Ge3ndPuJAH1ZCSfAHwjljSpryqpi2tKw-4Ycbts3LB3OaukWAC1x6_XzeVAbYG8HSaqF7GDsvlKe4XWG1-cbwlMXxbP7lkfThtbuBqe5C4DvnUiTBSSJXcR3M5gpyaaRE6DSHVnSouWFY77ZuLTwbWWpsU7q-KlEZHIGIjeQGlbGBYMRowQg5S3Ud2EmHeobO3s1mJM6vOHF4I2b2IRUwCQMiZunK4FqYYFUdodI2tcW0hhDdg2JN0iQC6r-9hyWS9Vny_dltQjpOfnuEvl9b9OGwArzfVsUoT5icdTblz0dCQet0cUXJJ8eb6e31LlrUvm7iLbLuzKFmu0jC8TQmruTc2bEQ5TnxrSMWdvEA4PTjoRTNdCbIgTBq8yd8fhsmlfVIaDJTmlroeNSRrHQWZX6If0triT-ezymQfXFM4MaCgLoXS6l_nxkfYKpZn6_AtXq6heK4Cg688hbG2JoVyUIZYl_MDhKF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: هرگاه دشمن با سلاح با ما روبرو شود، ما نیز با سلاح با او مقابله می‌کنیم
🔹
ما از مرگ نمی‌هراسیم و این، بخشی جدایی‌ناپذیر از پیروزی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/661148" target="_blank">📅 19:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661147">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: هرگاه دشمن با سلاح با ما روبرو شود، ما نیز با سلاح با او مقابله می‌کنیم
🔹
ما از مرگ نمی‌هراسیم و این، بخشی جدایی‌ناپذیر از پیروزی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661147" target="_blank">📅 19:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661146">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
♦️
عراقچی در گفت‌وگو با وزیرخارجهٔ پاکستان: هرگونه نقض تعهدات مندرج در تفاهم متوجه آمریکا خواهد بود
🔹
آمریکا برای پایان‌دادن به جنگ در تمامی جبهه‌ها، از جمله لبنان تعهد داده و در قبال آن مسئولیت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661146" target="_blank">📅 19:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661145">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cd3c6352.mp4?token=M3IRqnhYZFfBtHv-tB-R7EM68SdLhtuteQ8goZDf8xdG5xreXgMHSgFVPrfeiScvN8MOilMBZLi-hHBp3NAoZjYnwogyZRlKhmBY8NWDEHz4VnTXENCf_0WgxboRHdzQwU3i-lIzbpvD6VRq5ZD54GLD_NYYXAXBbQl1sKRtrzdBohEynsLJLkL5ZY5HDlIhZkifUFtNvvi4sEpbauEtC3e39NSY67S2jyqiex-LtjeH7lPH3w8TJilFx5e92FypOTN7hJKQP64crCZ-yWsfjATYdPPZy9cfrpeDzJRgX4y2DUHLVg0mXMqVkR3RJtkCC6REbYKfRUC4SXV1lBp8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cd3c6352.mp4?token=M3IRqnhYZFfBtHv-tB-R7EM68SdLhtuteQ8goZDf8xdG5xreXgMHSgFVPrfeiScvN8MOilMBZLi-hHBp3NAoZjYnwogyZRlKhmBY8NWDEHz4VnTXENCf_0WgxboRHdzQwU3i-lIzbpvD6VRq5ZD54GLD_NYYXAXBbQl1sKRtrzdBohEynsLJLkL5ZY5HDlIhZkifUFtNvvi4sEpbauEtC3e39NSY67S2jyqiex-LtjeH7lPH3w8TJilFx5e92FypOTN7hJKQP64crCZ-yWsfjATYdPPZy9cfrpeDzJRgX4y2DUHLVg0mXMqVkR3RJtkCC6REbYKfRUC4SXV1lBp8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رفاقت دیرینه عباس جدیدی با منصور پورحیدری و ماجرای آن عکس جنجالی!
مشروح گفتگوی خبرفوری با عباس جدیدی را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223561</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661145" target="_blank">📅 19:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661144">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای
سنتکام: بیش از ۲۰ کشتی روز گذشته با امنیت از مسیر تعیین‌شده در تنگه هرمز عبور کردند
🔹
از کشتی‌ها می‌خواهیم دستورالعمل‌های مرکز اطلاعات دریایی مشترک را رعایت کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661144" target="_blank">📅 18:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661143">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjI-eFKPURQ0jBGCm0unuQ-6HxXryX3I9cIDQGeE2D-6XKhzoyf8-GtnV8XKGKPIpF6ZkvMYXWA8QVtYfh-oiLlMDnCqYpjROSt4kbkYDYWMwbGUnARTG1UpZP2n524mqZqVORC6TX7xqJQLLuIDmfUj0HZ_c94VXh_YaE950RkFCkCoZpk0iTmtrsneeHQzo0q6ChXSYA8_fSDAxIKdOyXtc4eop8j1cGshexvNEmS42MtM7HO4yiAMtA-mAWcfHcsZdqSZEVwwP9kXwDunhJXdgREWXv0TSR3wMcHLhGsd8TP1JP0x1ZBBltLYybnc0wpccA42o6JHeag05zxPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/661143" target="_blank">📅 18:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661142">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شکایت ایران به فیفا از محدودیت‌های سفر در جام جهانی
فدراسیون فوتبال ایران:
🔹
درخواست ورود تیم ملی به آمریکا دو روز قبل از بازی با بلژیک از سوی میزبان پذیرفته نشده و این موضوع روند آماده‌سازی تیم را مختل کرده است؛ به همین دلیل ایران به فیفا شکایت کرده است.
🔹
رسانه‌هایی مانند فرانس۲۴، بی‌بی‌سی و گاردین نیز گزارش دادند ایران به‌دلیل محدودیت‌های سفر اعمال‌شده از سوی آمریکا، میزبانی جام جهانی را به چالش کشیده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661142" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661141">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پنتاگون درخواست بودجه از کنگره کرد
🔹
پنتاگون رسماً به کنگره اطلاع داد که برای پوشش هزینه‌های مرتبط با جنگ علیه ایران و غیره باید ۸۰ میلیارد دلار اختصاص دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661141" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661140">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نشست چهار کشور میانجی تفاهم ایران و آمریکا در مصر
سی‌بی‌اس:
🔹
چهار کشور میانجی تفاهم ایران و آمریکا یکشنبه آینده در مصر دیدار می‌کنند.
🔹
وزارت خارجه پاکستان اعلام کرد وزرای خارجه پاکستان، عربستان، ترکیه و مصر در این نشست درباره تحولات منطقه و مسائل مرتبط با صلح، امنیت و ثبات گفت‌وگو خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/661140" target="_blank">📅 18:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661139">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTy1XCru0l-0mRhoMQfdfbpE-fY7Oabuhm-fdgcpMQBG6UGaTyIt72PDTpqz4QGJwiWyTAkzvVMEmJ1bBnAZuWKh2cIKMd_Wh4NWqLKJAJrVkti-dBxAEdxsbZUahKbySqJ4Ki6cDOh9qMYSFFOPJ4lWblnKdZZwaOT65yds0Cb8NKSRqRv9b5v3LprJaKcayu3Ehy9gPoVK57fNvhM8MGYlZ963EfK94UIy35ijlJmvqLC7lJQiA1OQ_GkJuHWz8Ej1UZO6jzO0rNqqPh1IxXeXAZFW2yLoVV7K71eoijk3MgNkhUWczkyhq5H8yrnGBBG7NR9lJkIgNjyyz90vfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام فیفا؛ مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی شناخته شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/661139" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661138">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d0224262.mp4?token=gZ9-EX7XeRLAxrfPdEloSGD_GF62kCclTqUrb3CruUUoxnj5XafiqkYZpgL03uIsqqdLlgR628v_n24zfmMeJtSb1pgPO0XzaUaq-9zPjybAWe38abInVSBGMz2EDRxPG-sB2R7R1Bl9F-yU4SkeybvECSxM7EdVZ2URn9PkTSDELq-1iPdkVkstjlntV5f1c_0GriXd81O0itc-frcjGm9n0B_IttMqcicwWvZ_hTNWvGoxvW81kyipAHChh-F2L7Y_lHtshCHlasKMa8JQKkeVO3vzaPTzPOETloQ4RwWx7GzoHTerg4TOnPUIZXAow69R0jmUGE3dAlKm4MpkTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d0224262.mp4?token=gZ9-EX7XeRLAxrfPdEloSGD_GF62kCclTqUrb3CruUUoxnj5XafiqkYZpgL03uIsqqdLlgR628v_n24zfmMeJtSb1pgPO0XzaUaq-9zPjybAWe38abInVSBGMz2EDRxPG-sB2R7R1Bl9F-yU4SkeybvECSxM7EdVZ2URn9PkTSDELq-1iPdkVkstjlntV5f1c_0GriXd81O0itc-frcjGm9n0B_IttMqcicwWvZ_hTNWvGoxvW81kyipAHChh-F2L7Y_lHtshCHlasKMa8JQKkeVO3vzaPTzPOETloQ4RwWx7GzoHTerg4TOnPUIZXAow69R0jmUGE3dAlKm4MpkTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت خوب سد کرج ۲۸ خرداد ۱۴۰۵
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/661138" target="_blank">📅 18:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661137">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GytfPG_QwnzbwrLWf3Fnik-V5__aBJCcjVUpKWigrIgFo-jFaJP7j5eQjGK8iuabp4J3fef2k-Q240eNg1dt9UR1urnfIzuSHlioSlK2mI6Y5WwpcsUSNM85eJ3N3cCyNgBql_1dZzZlLKoTYKIjjHKo00oKz2IH06rGpAMfPjpyMPWw26GqN9fPb8M4cLiZqna-mh_tGTmPt-i-jXFzyT3vguI2UOJQkOCyHbzVRYQMGYLr5pUFu7VMUSHldlH4VbbACt9ZQfFl0RZnRdvpnf0hN4xR97rEk9weuy3kPAICSJ8fbXfnX4qgz8mqx8EIHAl2vyI1BpSi-eV_4MA2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
رویترز: ایران سلول‌های مخفی جدیدی در عراق برای حملات منطقه‌ای ایجاد کرد
رویترز به نقل از ۸ منبع عراقی:
🔹
سپاه پاسداران چند سلول مخفی کوچک در عراق تشکیل داده که مستقیماً زیر نظر آن فعالیت می‌کنند.
🔹
این واحدها انجام به چند حمله پهپادی علیه اهدافی در کویت، عربستان و امارات هستند. هدف این اقدام حفظ نفوذ منطقه‌ای ایران و کاهش ریسک برای گروه‌های نیابتی شناخته‌شده عنوان شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661137" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661136">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlBxt5MyyjNYehCPP7JumJUO9BIao94TYtBEZYK3UdjrQAWlR9zKNITkj5e9nipvs5-ujraeIkTIuZCHSKp3-PrvuO4uhTQsoT7Hi55eq3yYAutbIL8OR2cRQOU66TSnBl30g81SGe-6EsiLBvSuZgxebgjkLwdY5hmpU_tyaoinDFnF7Ewt3fT8loRCyjdh9anDgLl4fG-9Tw1NG3XmaIuIWzTRMBk1iQbiqthFUP414TMKpImlF5M2ZAcIg9CxKn8yZ7P0UQ2eHDfgLq4Lxz-1GmyYrotFtloclM26jI5-gRzMJ_OodE5hBzJNdeNsabs8x3ko6qMEXzGvuD9znA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکستن طلسم ۳۰ ساله بوکس ایران در جام جهانی
🔹
مهدی حبیبی‌نژاد با شکست نماینده انگلیس مدال برنز خود را قطعی کرد و طلسم ۳۰ ساله بوکس ایران در این مسابقات را شکست.
🔹
او فردا در مرحله نیمه‌ نهایی به مصاف نماینده آمریکا می‌رود.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661136" target="_blank">📅 18:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661135">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wra60tGQ5eS8Ym-zPUSCfrPplYwBpkTWrDAVLpXjALwsd7k_3x5Ic8kv3X_1A2LFMni-kpHFx7lv_mGtt07l2CuoV4LLqOzO6NJ6E80iuSExRxWZ57NH0MXD_e2uTd_0n6HHLPZCZjS29X-zFMXl6rC5hwCBJsk83mLrQMUlrjA2aK4CkgkI-jhVquYWDyT7bDV1A9F25WRMRWlGMSq6qrq4JsYD9g7jRAWGRPqRnk-xrS5lF5Rde49AYPYqLtvvjbPOxWNgqY8wUZuKKNGrtCtpK1Dz92qiUCTLZAdaENKs0lcPWKR0hgf4Kft86Cslv91jVf_ugxs7qKRpESMIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«۶۰ روز سخت» پیش روی ایران و آمریکا/ این ۴ مساله توافق را به جنگ تبدیل می کند
🔹
رفت و آمد کشتی ها در تنگه هرمز، نزدیک بودن ناوهای آمریکایی به تنگه هرمز، رفت و آمد قایق های تندرو سپاه، رفت و آمد پهپادهای ایران و بالگردهای آمریکایی در نزدیکی آب های کشور و ... همه و همه می توانند احتمال درگیری تهران و واشنگتن در جنوب را بالا ببرند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223563</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/661135" target="_blank">📅 18:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661134">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grikuFh94_zL2kp7qbaeMnBqRk3CMsHT5h3OhTC27ixdVNEx3u8oorHlQerYOoUaKv7UCBdFYYCo6XCaxlYxylSspVg8VvwCya30NXkAyc676SWh_o_HbeDXfLSmrGoUq6uB0j0Y3o_R0IbPhhJYwycMVKvAlt7nha90uwrjUk56fZbkqUDowSUDL_UsW7rQjyIE7q_MFOMPE-D_Ge_wbhEt4-2osL8hSYclzd2OfBSpi930u2lf5eJBzmsrjFxEM2zDvePv5FIN9dTqkWH1VCLu2m3dKyPyj-TxtZB1L6Ce419QMna_Ly0Wl9D9Wl1ZGpKKI2XgXuM3rD4rAp31_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661134" target="_blank">📅 18:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پشت پرده حضور تیم ملی در تیخوانا از زبان سفیر ایران در مکزیک
🔹
ابوالفضل پسندیده سفیر ایران در مکزیک در گفتگو با خبرفوری به جزئیات وضعیت کمپ تیم ملی پرداخت.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/661130" target="_blank">📅 17:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تکذیب ادعای بسته‌شدن تنگه هرمز
🔹
سخنگوی وزارت امور خارجه ادعای برخی رسانه‌ها درباره بسته‌شدن تنگه هرمز را بی‌اساس خواند.
🔹
بقائی تأکید کرد نیروهای مسلح ایران طبق یادداشت تفاهم ۲۸ خرداد ۱۴۰۵ تدابیر لازم برای تردد ایمن کشتی‌های تجاری را اتخاذ کرده‌اند و کشتیرانی…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/661129" target="_blank">📅 17:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: آغاز استفاده ایران از منابع مالی مسدود شده
🔹
با شروع اجرای یادداشت تفاهم ایران و امریکا، منابع می‌گویند که ایران تقریباً شروع به استفاده از دارایی‌های مسدودشدهٔ خود کرده است که بر اساس سازوکاری است که میانجی‌گران ارائه داده‌اند.
🔹
روش استفاده و انتقال وجوه در قالب یک خط اعتباری باز تعیین شده است که به ایران اختیار تصرف در آن را می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/661127" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نشست امروز جمعه در سوئیس، به روز دیگری موکول شد‌  سخنگوی وزارت امور خارجه:
🔹
رایزنی‌ها از طریق میانجی‌ها برای آغاز مذاکرات تدوین توافق نهایی در حال انجام است و در صورت فراهم شدن شرایط، اطلاع‌رسانی خواهد شد.
🔹
وی تأکید کرد طبق یادداشت تفاهم،…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/661126" target="_blank">📅 17:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نشست امروز جمعه در سوئیس، به روز دیگری موکول شد‌
سخنگوی وزارت امور خارجه:
🔹
رایزنی‌ها از طریق میانجی‌ها برای آغاز مذاکرات تدوین توافق نهایی در حال انجام است و در صورت فراهم شدن شرایط، اطلاع‌رسانی خواهد شد.
🔹
وی تأکید کرد طبق یادداشت تفاهم، شروع مذاکرات منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است و با توجه به امضای دیجیتالی تفاهم‌نامه در بامداد ۲۸ خرداد، نشست سوئیس فوریت ندارد اما برای برگزاری آن در روزهای آینده برنامه‌ریزی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/661125" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/661124" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661122">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYA82aD45i-avS4k0ztqZcWQqBhqeVHJt5PO7sNw0-ITqQawwTIrmmqcRckJI9AjIumDJ41DbQTycNY5FP3i13JuapMJ0jCe5mCNXYdUbZ-cLOP1jxulWrMN-LtxlhOMnn0VXYNNSyQ5gxOh_RfnSePqv_si01bLQuk_Lv4uYW6VqBpJALmCQDferzDZ5zQINliBr9uCC5OwppXNTIW7iSHHP9i2Zmdsjv6FczGHxwMhHdtoggOjZcpaa47HNLGZxt2B8cqLuuo6jCj4aClQWeoM-WAmcyUlqRqsQZwI-qx1LLaq2RcxA6mWYWU8DnEUjHv1EFxxQQhlpZtTrVupTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت ترافیک دریایی تنگه هرمز پس از توافق تهران ـ‌ واشنگتن
روزنامه فایننشال تایمز:
🔹
پس از امضای یادداشت تفاهم تهران ـ واشنگتن کشتی‌های باری و نقتکش‌های ایران از آب‌های آسیای جنوب شرقی در حال بازگشت به خلیج فارس برای بارگیری مجدد هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/661122" target="_blank">📅 17:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661121">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بانک مرکزی: اختلال ۴ بانک ناشی از حمله سایبری است
بانک مرکزی:
🔹
اختلال در بانک‌های ملی، صادرات، تجارت و توسعه صادرات بر اثر حمله سایبری به زیرساخت ارتباطی این بانک‌ها رخ داده و خدمات پایه کارت با روش‌های جایگزین دوباره فعال شده است.
🔹
این نهاد تأکید کرد سامانه‌های شتاب و شاپرک بدون مشکل فعال‌اند، سقف برخی تراکنش‌ها افزایش یافته و شایعه ایجاد اختلال برای کنترل بازار ارز و طلا کذب است. تیم‌های فنی نیز برای رفع کامل مشکل در حال تلاش هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/661121" target="_blank">📅 17:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ماندگاری نظامیان اسرائیلی در جنوب لبنان با وجود ادعای برقراری آتش‌بس  شبکه ۱۳ اسرائیل به نقل از یک مقام این رژیم:
🔹
نظامیان اسرائیلی در جنوب لبنان باقی می‌مانند و همچنان آزادی عمل برای مقابله با تهدیدات را حفظ خواهند کرد.
🔹
این مقام با وجود ادامه حملات، مدعی…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/661119" target="_blank">📅 16:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ادعایی، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/661118" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8UqEoCm9zk__zq9-rz6wJBlpv4gVfdXek_L3oeHJxTe16C06SQIWhlyEXRRFR4W9GeplK3Q045JB6tCElmk6tuv4GM62GMkzh9PSM4xbG3ObIKv8QAlX9Ywxkg58pD5IcYWEpbiFUlNix_R-uYCjwX9i67DY_sy-VjemH5uAHwhp8zA12j5EsqlhSV2rDYSLJT_RYYur4aWUZNnCzqaSV71740sRQy0-y1kSsdq2bNF_n4WIKSDLlv0f2SCaxjN1xd63nGASldivKsPQTNlzsczIWWUaS1mjMM1vHpK9a_GTH-lgCgLyQHTQFS_XgkXhb-NU7QMaZryBCkEMAT8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العرببه به نقل از یک مقام ارشد آمریکایی: توافق آتش‌بس میان اسرائیل و حزب‌الله اکنون وارد مرحلهٔ اجرا شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/661117" target="_blank">📅 16:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بس در ساعت ۴ بعدازظهر به وقت محلی روز جمعه توافق کرده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/661116" target="_blank">📅 16:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661109">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEIR-smtYR3Ly5IPQaYwOKoNiEuXS1pxRdxl2Bj1c6dRlNUrS3mVPrDDSm2y-cdaczy0XiiMCnmgia0XO8GAISPgpR_vjao7-g6D0pSM3UYV_Jk_DkLnNV01olKq-997-dIWkW5Tgsw_efemYfEJvfLbFrvcsVEyN3E75X3HgS1CB22M7td2ZU2AGXP4p93YWsAXSVuyMQWaTb7DTfqmjMyaF8b_XhbRU6oQIyKu1kgZAQ98mLvtDQAm4sZAZNP0PiyljAXDWgEBKdqv7JeB0r3szah1C9N4IFinpVrTR_OHJ2n2iDFHZvxwKaFXMrxs_84S0gOrimrz7qZ9clRp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFyyFcF-t_1iH-repNF5_bR6UNzN8qiZ8A23Tr_-1Ok1m7drZ4OJdEUP14ZCSoGe8v8SxrNKiwxnadkKe8FzBZMeQDiZxAy-BvcdnO-RdJIhsFQ8YZSV33wWFqGjezVZA4vunhDj58_4MJlaN9unGHJGSdf3AE0sxZwsn600EV53E0bX4e9Bp7dFhTjSjKxMa3QsXlOhJbmLbe7u0Ny8ZzB_gGyhRjClpHncbGPJtlgO_3FGtckxN1AOJo_ybzMpEBfkzw4RDHcB4pTMr4rpZixMt4mWwsA5gyabtmi7fANUUKBGIbcF7lPZ2mRW3MM_yBQDaZtyoJxOy0Kt6Jc71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tejiVkms8DN23VsrqhC-zllt2g0Nx83X8PasxyFhH7e994n9-6V1js8f44ZbpdFh3f9JTHwMFpa-8P2YAswwlXXvKgBcvSSDPf3QtZCZcSp3kgWGQGXPXyM0HWuTgHpn1yU_8oeIzM4GqpaZMTV9kMdfr1QWoLLD9Fs2-o5LXcKjwXEt9-idLfpBgSQ_jNLZ0Zw3FuMjkUdE1yLWALdWlk_PGaRXnJ84Y9azCvCVr2UDE5Yac6vYIssfrDz4rlCHgPfEOnTyOoED9SIIk4zfqxfmEjzxhcfxj8udA1miAVktk9Ayc1M7JdB5nYN9Dt4Uc7_cYXSUV4NG0BtI0TpIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0azCYDRZtc0m8gsEaH_2y9LheetxiGE56ma3K8pKT0_QaopzwkLEF8cQ--qITXLhAAza2tm5_gdXzH8aHDbmcBLLHKWuiNLbpike8vdykP-nT1CTv_cFkYZbUoREHp71luUkzfCpvo3KWcNyH8rWmXxF76JQtiqZ1bmItiIEEX5_qe7aiifJVDYFz7HqFt-qohhXO6LvVoenGJ_xzBCgVK_zg8RmsJ_8sL3J_3h3K0zV9osVx_t7kv2zpik8iFa5JAjgJywRjq03IhyzSDm8EAVJqLLoxbRl5TNAY3jdTNISZCgxN805AiWeXkt-vFvUpsuaI17UJUKA1OH67XsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVwbIrR5_BggEG3wSq7ib1L-d3xGOBbgrN2aLHq3pmKYobnUHa2w-tNQ2umw8RCW45S3kE1GIQR-nauyBm4uDIue5o3PNvrXLekAlMikVuP4DQfULLmn2yp24n1f6C-P-kduRMXTt-YfC9opdU5IYwl8YpTK4HB-fsGxHpW7of1CCtBLuJtq7r-nCywkNrrEw_k-GEqpyQqZ1St4P7mel4K8a4QnEWsGaDJ9PYYO6-WFy4bLOZTXpiQ7OXqNo4B3kNUEQy4b6gqpJPHQ0TKQfckWR6WdzLJ2xzxpVDzMktp3d3X6e2iOyjoUDDeZU_mZYJZ4hhsfm5SSb4zZrf9qNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-7clCkZ4VPTHG1W3WcQ54PdMJxDeapOAu2VYuSj-fA89eOMUShF_XYRSXAlE1UWtX_kPHfqCnoXmRYMB8EfBZ9dnjQ5V80NsgjBU_8WGrO88I6V5GOKEcWrluwCoVnHTdtPBs75VYcvCapelQNQSuqxgwqy3T8bNWE9LINLkOvyrW1ZCqCPBaaZnMltaImKLYz4hF0IZO0puiQHYp05bGvvJPl8tL5YGxU90dCNsbsY_SZCEz4PWee7LDUgUzJDaqFcTgLWzvOpPvTiWpdhnFHdDh-PRBxgv7V-Rb4AOSNBcPqJfY7W5jaurgyyFDw7TNyRjruPzNag2bOc2GeAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVlFNySnHChdL1K6JL0a_M7lspBlavHY70OktV1PdQfFP1kPczhwJzJ7aXup1cjdoDBGNALg9UBCt5z5OXrZdxivYlPadwxa91XZ0RYGOMBw7_IREcUiENvYafUULMFnuz9yJzYeZGOm5boWseFx3wUXX4R-Ds2RMUGPHH9Gwl2BwavDILdVvPyJRvWWoxxLmkUPzp562Lgb7UBTcepbCCaEbBpk6qBk6pmbrpLfZhhhKRA5eB48tXV8Vnd9XH2mHgtT__C58JNW7keRUSWZ0fz0hdZbdJ-31j-60hOO8pQ_kDUsVzVEmk5KamjNppOBCNeoBarflCzFFd3hj5qVZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم شیرخوارگان حسینی در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/661109" target="_blank">📅 16:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661108">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ارشد آمریکایی: اسرائیل و حزب‌الله بر سر آتش‌بس در ساعت ۴ بعدازظهر به وقت محلی روز جمعه توافق کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/661108" target="_blank">📅 16:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661106">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEZoc0LzPqIGAnfVytGq97ykzyHYr-743WkKK_Bdoqm7SWLGz12M4bdjiu8uucbKg_2gJOXdf00Tzf0wzR9Gy9h0_l3KQF_h1itqxar6xuoIRLIG7Sh3CN5nd8XVccAwmxp9ZUiN3m2WHvawJC7K_-cqP461tSil_JdtemON8NYo5fuz1a7nrwYU5YtOfVJ8Mb6wF3qjVezWC4jR8e_4GQoxrQAJhaZvwEHZSGg7X0pWrKfET6tg64vKto26o9meVjwzR9yRc1UTTE5cdU0mrHrdWJid2yG3Lp0Q1NnosfOcv41dDHPLUpm2TjZRR81juxax76Y6NDRPmgxeOaxiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: جنگ ایران را تضعیف کرده است! ایران دیگر نیروی هوایی، نیروی دریایی، تجهیزات ضد هوایی، رادار یا عملاً هیچ چیز دیگری ندارد، و با این حال دموکرات‌ها می‌گویند که ایران اکنون بهتر از چهار ماه پیش است. می‌توانید تصور کنید که چنین چیزی را بگویند…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/661106" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661105">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تهدید به سبک سنتکام
ستاد فرماندهی مرکزی آمریکا:
🔹
جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661105" target="_blank">📅 16:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661104">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1r16RB0ncPjKGfOiqK_GUi0_2LBf-mNUUcgEJLwCdJGZYb0ccrvj5xniouiY14bEsDGSBIqMgQa9IH-eqbs8BXGRsNqA_513lJhirfR-n9TJCw8i1vgc8HXzTtKkY-VBHV_TBd2ZvdWG8PvZgBWXV2Fj9xKIg3-YWClBmu-qMiAZ8iMoUhYIZVqerq9NbgW2POL51C_M4-A1NeY9qu6Rq3VYNseJHa6hPIo93Gao8cn8Nw8d-8_LMoYKgHNksjiBBnsA0SOiqQXqmil6NS3y-XAKXSVP0m3KFMDf7DG_Azqx6q_IsECAMX5Vg8ZrGAbDfEqahBl2ew-oEF1tVWQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: جنگ ایران را تضعیف کرده است! ایران دیگر نیروی هوایی، نیروی دریایی، تجهیزات ضد هوایی، رادار یا عملاً هیچ چیز دیگری ندارد، و با این حال دموکرات‌ها می‌گویند که ایران اکنون بهتر از چهار ماه پیش است. می‌توانید تصور کنید که چنین چیزی را بگویند و از آن عبور کنند؟؟؟ بعضی افراد چقدر می‌توانند احمق باشند؟؟؟./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/661104" target="_blank">📅 16:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661103">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
هشدار ایران نسبت به پیامدهای جنگ‌افروزی اسرائیل در لبنان
🔹
سخنگوی وزارت خارجه ضمن محکومیت شدید حملات اسرائیل به لبنان، آمریکا را مسئول مستقیم این وضعیت دانست.
🔹
وی با استناد به توافق ۲۸ خرداد ۱۴۰۵، تأکید کرد ایران برای حفاظت از امنیت و منافع خود و متحدانش، تمامی تدابیر لازم را اتخاذ خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/661103" target="_blank">📅 16:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhw_scRFb_2yiqgewTZE6XqGlzpmpW2JmOgdVlncecl7Ro42nG4xKehElMglDn7B6QiZ5BhgUNFFhopB85AVT8aH4lQIBdm_hq8bktu7tQW5OxBusCj3kf698NfmhiFtnHobGYu89IiywubqkD8jixszRD0k4KeZZI5IM4oReWYZEfnoXu7r7TaXjmFFMkYt2VdfPEkTu4uEF5ETv809NjN9gBWtnAgsbCgYZJTH-2ChOJtCm-ddfOAm1_UeiGo1NNyRnKk6Gh6wbvb-kkdRax7SvG-fvUbAcnyEkBwUrFpucdqP63a7HnWOdLSgElizhATxx5UtIcaptVYOd6cz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به رجزخوانی وزیر امنیت داخلی اسرائیل؛ فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است
🔹
این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی نام و نشان نیست؛ بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔹
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
🔹
ایتامار بن گویر وزیر امنیت ملی اسراییل در پیامی که در حساب کاربری خود در شبکه ایکس منتشر کرده است با به کار بردن عبارات بسیار تند و تحریک‌آمیز  از جمله «در برابر هر قطره اشک یک مادر اسرائیلی، باید هزار مادر لبنانی عزادار و گریان شوند.» یا «تمام لبنان باید بسوزد!» از مجازات جمعی و وارد کردن رنج گسترده به غیرنظامیان لبنانی سخن می‌گوید. وی در این پیام آشکارا ضمن مردود شمردن هرگونه روند دیپلماتیک که منجر به صلح و ثبات در خاورمیانه شود، از اقدامات مبتنی بر کشتار و بی‌پایان حمایت می کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/661101" target="_blank">📅 15:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnSW9QylAs2stp8BRk0B4iOUEuqs8MJvwCUmOvI2m76D_wpkIrRQ15yDkB5eUpjZ_UwmFJfN1HEJU9ELRtXJBHvaH6WEk1cmYkxQbRhVUR48-YqQsnbJ8AyTKWNOX_dQ7cXcZ363IB0LUi0SSk8AmkXJU7_fVGAf55l4ODTYuAqNsK0JLczSxrrN4JfV1Ht5Wqa0Xg4u-cBqm7zCjS7LYeRI-f9ADAHPUWADZw6EGnon8YE1XJgh_PMNpDxak1dWKt2gVz3Hos3DlQ0GOo2yyewHkx0wldCdxuT-X1gXeVY2EIHorzNEN6m8be35KKdekVy38LvOMYSsUDJjGPqihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1nUkghpRsBQEzFH-UrgrtVWgYZogWapCbZvE563NJcec6SMxp9d_G5L283b6CAL3Osd7sY8H4EIjJV3aTRXTZToJec_yv_j-_Da-NOhh8Sd33NPngGtGUl-GR8g8ne8xKF7PpGc6A8jOqVIjRpgERrizrstZi1ccR0Lnfpt0RJ7IMMDHQuiWWCCu3bEOwFkLDdiEBMNlBOLD4f378VRxwNxiqlaI37QUQ0TXRWT3arc8-iZLaRIa2pOdJuy3b5DcjTANNzb5NkrKjvQrfjdRVOM1N17PbOwrwMWs3s46ts4BK8GCDyCEFqZM1sBiP0ZKTwbFz7z0qjavtyEl_dP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9GBqKsSnoH6F2YF8Wu2FtWcLyXUuWyGkDIAyYRPhUdw9yYL2LY6DhSvYC2S3zBQKFt7ar82IF6f6arg41d4JwUP01kqBzCPAMIAFn45wNHZ9igKBhLU0dTCoKjnHvHSRdoeBeP501HB4QYdlEDSxxZxa7NVnQsZu3MwnPcCq6V6Nir2vQBqvVDlbwkwxreRCRqh4x6Q5h_lT8f3rTX9Jkhk5X3hIWq-USZ0rSpy-BuP1Dpigmi9RJjl0UkZ2jQA_XJ7cT8p1KCg5dmYwVBV6H7p_sBlS61nNnkTDBD2g7s0l7N8H2Ybk0RhEdZCKmGX9VVM1IQrr70lEQBxx5g3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsz8p7JLCgQpHy2gvs5BAu_0dt02jDPWrsI9Y4jp9gJ8sVx_DrpnQ3kIJln0umXRI9lKu-2pfOQqlVtp8ynNLalKBsVAR0slRZy4p8U77VceLd2f_lxpkCF1-o0H8V5N5pruG1PhlKL2T7eDgzFwCpDiZF8AsX9veFhI9FtVNEY-YL9lGPSZvXYqNRY-tqVfS68kK-Qp9YSbY-3d1qQJoeklw3n5rWncNq1kB1RPWOmbaGsaMtGw1uR8UjmSij_jkweoCLL7irr27_7FdGkqz5XUOp5lyizB9VEMxU3l7KSmaJ2gYsKCmPJYMf3v1CCbtnMCWrCn_hY3zZcUBbqVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxOhfTPpOLKoQANeHVSCS8RontpiAy23Hf9dwk7xqded_3aBezjZSvKP8wIt411UoETxqwaeP8ccdxYmMkSNQJYuo3jS1T1l0r6rSv65YywReibkwwKOIplEIErKdljAZiUvZzQjl463_X2rjPNtdb-B12u0c0njWTF-aKfT-_woe3cupii3_UdNJPDB_qWd6Msz80tNxTOb9n1hOiSC4hrmF39fhERh4T4oubzlvLVBlVDblkt-y4t8Mj7GCGOPf6V_way45tHN6yMZJN3fwdVPYWFiSKEPSW2NGNuB1oYBVHg0mDS_lzLWYebIXsKPlTomzlWziISDjJqN6ZZL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTuPBviMiz-0nHkExoNd2dPsf5_P_tE2huZa3TB0WFdwdSbf2oKAsPneSBKJ8BmdWyG3FAxeRDF11bJMLmR3_vTDd1FFlsBeVfZN5q22bsHHV19g-w9my6vkA0IIbmewK_2qE9EdAFKinH2wgmH-JH4OoAzQnotThIx_g1sBEU0IqKSwRc2Ttp260D0j3ulzsolSN4o1Z6XP7WAcE9G9l0sK7Cm4jF1q3TYyAqlBXXrndv-4hhD-isJ2DhJCmWs8FfaYLau_csNkun-UrZaPzvRDLMfnmB4bHQk1CxQipQp4x-uRwP7vMMPrcAOWuXxY5MeHNidMxLOFiXLLQqrzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekzTl_QjFPalo9RujKb6wYjIVw1K1cXIjm5h-alcpfWXK8hQol26eNuPYbw2ZHOFJfPuCJVbAJuCT2EkY1zKCB8STy9BmVCDmOpzESLK8xz0DqVEIYpvyCErXeyg2OKCjDx2e0E-0GYaeXxH_HIrIRJU4xGlmU4ryCZYNq5F5N4Vtn4zgywTPcTomVUQO5lVQS01H_ggHEL0mqThK_39pV9UMWzCjXlhddH03tMfMxM1SNDBLmDpJGv3K5ugwnRngSyNXbWg6tmK96CvbcldZ-gY5G_1I6LDe4NGc-cbOXqdRa5dVxitAGRTiGhKRk3nxsZyoJOP8z1cLLwmPnlPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agGNIYeZqWw4VFlZEpof1eJtSAgF9Oumv0Jj5JBvgopZBLymAOrKVYitK3MJ3JNDqLeq4rHS984PWN7ufM6BL31rISqhxxfgwE5jnX_8vddasXi6q2wPM0pyBrcJFnxHTdDb4VDx8JRYxnJaw8cQYj1EDS7Bv3WPF4IlfoNalYLIp57eXvj3z_6no0WEV70EeAoKF4tb1HjsBXdYEGcOc2o1X_-lNiiZje3-HMaF8UiDE_HRxPULb7sNg4V0Kq9nC_NwgKHVW0DBMk862Y31Tz1I46bCf68zgF20nXb_mkwn3Zu16wxjrJ7VorHnUy3N_jkhvfriAnKc-HcGvjX0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhjBBbL5EFtksgRkPQsAYED9ykMLakKrzxr2lYEkXXV5aIDhiQ46rrsBGuOvJPcA3hTAAr6M2negmEzdqI6SuN2cfdyPo6evkL9Rxc9xq1edBExENMwCAkBc8Oe64YuNE6x7AU7DfrS8fjGQsAXSS0Q3FXFv1gTyZXR-4CsREg8gw-Q9R9QqPO3tpi3buEhtF1QWlJ544K6BdKdvjChkDUcJbHLCkX8vU0MwFv73OQtD9u1hk0QG8JmXNW8zA3zm1msD5GK6Uhfb6z1cUPY6qnkdIoAZTI_TxQ4MPdavRxfHxBTNkPdX7Y1MPUyQ5D3sIZyDvYCHUmJfBXatfbB-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmvZT17fIsEdolK4wXzXbuvanmhTiBsEMcFuSJD3w8D6nMZZWiA4D7YtIs1ZkGYWX6GxApFjvyLXqwmDCtvKXsfJ3nPA4oboPAfWE4f6x2Ec9xw2IODc_Xi-fAYX_rj7a5d46il8sMrVVqoWhc1AbI-eneE_rOhjUq-HTNo2dt5BJiQxCHAd-UGa-nvBdB4cyMaovLsmveh9NY1OT6usxUVRzLrNl48KhoDhxr0oez9pWxKELnEgH_NQ3eDSOwSnO3zSNyaWFBySb0MoH3mhjQANy8AyXK1PCizvxiz0TnEJhayYEaMNLS7TSlMeV3V2Gi0ry_QSxdPe6tFyVWhINg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
تصاویری زیبا از مشارکت مخاطبان عزیز خبرفوری  در پویش بزرگ شیرخوارگان حسینی.
🔸
شماهم میتوانید با ارسال عکس فرزندان دلبند خود به این پویش بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/661090" target="_blank">📅 15:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ترامپ در پاسخ به منتقدان توافق با ایران: برخی تندروها دیگر محترم نیستند
🔹
من یک آرزوی اصلی به‌عنوان رئیس‌جمهور دارم؛ هرگز نمی‌خواهم به هربرت هوورِ مرحوم و فقید تبدیل شوم
🔹
بعضی از افرادی که قبلاً به آن‌ها احترام می‌گذاشتم، دیگر برایم محترم نیستند؛ آن‌ها تندرو هستند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661086" target="_blank">📅 15:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1391551f8.mp4?token=AzCYyXwyc3_lhNY1yJOrqCO0jxr7hbI0tferPF_GmC5FRE-17BlO7t64xk6Cd1WkSXS439Km4w2B6g6Sjr1Nla9cQeebxfdXzJVz9RiYazzALoNoFJGOL1vgaW4D4Zt0RxkZe-5PKsx7Qkngc8SKyigjuZ2dELH0lXJ2WV9OmCn8dvj5C7VlKpQUA2KQyqE31gXSn_pE3q6KljZ9XM8q1n3fsgqt5BOIkG_wdBHwL1h3mD8W9SDOGCl01PXKXN7xSEe7VkZS4UXk6SSOK5MuPv6x-N298n4r-8nV1zzjF1yrThNWkm2kNtk5zKF9zpIEKZkaMNbHVrL8Uo6jd9uJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1391551f8.mp4?token=AzCYyXwyc3_lhNY1yJOrqCO0jxr7hbI0tferPF_GmC5FRE-17BlO7t64xk6Cd1WkSXS439Km4w2B6g6Sjr1Nla9cQeebxfdXzJVz9RiYazzALoNoFJGOL1vgaW4D4Zt0RxkZe-5PKsx7Qkngc8SKyigjuZ2dELH0lXJ2WV9OmCn8dvj5C7VlKpQUA2KQyqE31gXSn_pE3q6KljZ9XM8q1n3fsgqt5BOIkG_wdBHwL1h3mD8W9SDOGCl01PXKXN7xSEe7VkZS4UXk6SSOK5MuPv6x-N298n4r-8nV1zzjF1yrThNWkm2kNtk5zKF9zpIEKZkaMNbHVrL8Uo6jd9uJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فصل جدید تاریخ: توافقی که آمریکا را در جهان کوچک کرد!
روزنامه‌نگار و نویسنده باسابقه استرالیایی:
🔹
ایالات متحده با این توافق کاملاً تحقیر شده است!
🔹
به‌نظر من، این یکی از لحظات بزرگ تاریخ جهان در قرن حاضر تا اینجاست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/661085" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QamlW0tRtEsX7HskWFJaQfjjDb068Xhqa9J7EQmokKqFcuwLpXMoid5dbDrsxD4JktJ8RlHURJxk4hZFrlFhv4LnXX09fV05JB9HFJ6od0csrefAVOwtxl9PYBpfu8p7kUpM9nSidETnX-H6NRUIqaJErIHyNox9Wn0OiBlNcA-n43wNcU6KHpA8skcJn89mRXWuoab1XnBfeSwlF3jqmljgikX28FbuFqyp8PZdX7jWDjgoes4CUYa4nsMdJOsnQ1GJe0gt8vLcK0g45RFCWrxrS6k3x_3STeSmey7vU5nkBe-wq9fsj7DxGKZuu1Cw07y9vrvRxhUyetYOjuVMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: نگذاریم مردم مقاوم جنوب لبنان قتل عام شوند
🔹
دولت باید از همین الان و از لبنان شروع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/661084" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cA4FlR2AEsAq0-FSRda4p3TshltS2HbFnMI-Y9BESmDbPVtPlYTX9CjvKIsvU7qCyiXnA2lMdShAjHdTk3Wjbj5M1Zx6UkygWHaRpMqEam5gR0eDG5C8-bBqk-dsWMyt7gox4cZJQmbSPidpFxHOTwmNV6Wr-3lJ6LdGbpuaUfvH65C1qlqEcmpi42VYeP9KD5V1s95AOk5aEVEdu-MitS92B__FddzDzakG9TV6TvrgfkvqYTamXs1FmlWvsDRe0UgpnXdK4rjzxPztpvVklhEMMUoeOMVeaCAMknSCtq7aQtgXu2iM6FW1qHMFvDEJnQ5_-mOK2I6BGOEKvZjIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIQRlgnZS0wyO7HDF46JPtZMeNiHcCMlY0djFSVvvoFOM4EFt-wh3D3wIkDBIG3aiBBri5GL-A2QR3QbsFIpmLD4Anvu9Z4ML3FqITELU0dF4t_nuQuUw7tDAKqgkdAsIUbgANc8WWeO_z4tWY-XsqfBqlq49y7XMx7M3QP-Xo5_W77SrJHHzCEvPZlDRLONqIkjR-96vYhICaM3oTVVm6m-wK2VF2RPqGLzh78bpZzegg45XB0NymZ5PV21Tlg5_W4h23V3eUWHlY3h9aVQ97sllf07Jeo9k7R0blpCE67eD9NCNQ7BbM8XwcVVUJpkV1L8fr0YXcy9LrBVCV-CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtfVmt9siLsTr--Cw6wfRf7uXFzudqRh6r45uiQT0PdGzl1Cc66cRW17skkAywsTWSy5EQ2upb5cYA-cxcIMeneV0WnCtipCp90dujTpZW4ctXqBLaoCL1JMtmLWjivR53EzTmjwAOHAHhHHiVag1yLF-z005rTY8Mu2Tf0ZVc-gXm8tZIbZ9WgqoyOE0I4_FEg9ZYGcTZul47-xva5ir1YJ3Kws-FtwUJ--ZC-RnJzYDG4Jk8MVKZ7RACz744zfajm6A1OtedsMGGlj52vt4Z_uduLm1h1MRYWOLplK2R81QNCUZBNfXNtD4aPjxSDLzsK12NzKd9nk1vmSzXTyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/it3fWRHYefsKKB0Ls-zznqSSyeWkS0jBThS_Thn3WloDsmLCcoQN2rMAjGQBhYBTcOzKf-5LZ3rm3OJ12mQCnP0pVo1FTXVNgenzf3a4JQnupFwmaVuBmI-wC7poJoOELIsyyCElMsq9SwANQ4SLFFzYo9aZFyqMdLCY8aivjcDPK_pVkdV4dxslKytcnKI3OX6eluiHPuLaFLUvoP2lfyE9c9UolIKIVykQbMt_cE2G1dv4D2ZEhP99TkAmkCOeyFY7MdJjMQen9cHB1jYVV91RTZCQIh2AQ-b8CAyMpJcCyDcFDDL-X84941b_dZVSlqXIWOzoWK7S5m_6WDx8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fITMivOW5yWXr6AFNJs0mG7Mo6vycoLCpH5IyBxaDpvE6_tfGJo1-1yI3p7ddqAeaMxWJs-0H7k1m9MKUE9qPjdiearf2HnT04-CGbNlmlKwvpBabaOuK3S9SuhniOlpGNoOwkYaMBR31LS5eRUjUox0Ia0JqoN91T1ku8CB_FVS9TEFxDBcw1Vy4lvAXKr4rVHEvJxJS6wCDrU0FslvfptfNTVTXrS1Ls2B_1n_8QOyJPtjcTbMdFs2eFAkZREJ-5fRw44UBo2twy2vDnESWM2gfMg-Yt_9FX5rXQq58X8vg1RwyEzPFNgaOE3uzm-cObgvKJq1QtW2EUYAcCT-9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور هزاران نمازگزار در نماز جمعه امروز در مسجدالاقصی
🔹
شبکه خبری قدس اعلام کرد که نماز جمعه امروز با وجود محدودیت‌های شدید اعمال شده با حضور ۷٠ هزار نفر در مسجدالاقصی برگزار شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/661079" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای خبرنگار العربیه: مذاکرات میان آمریکا و ایران ممکن است طی چند روز آینده آغاز شود/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/661078" target="_blank">📅 14:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiYiS4N_JaJmnDWWvyO6BfY9KL3hsYB_GDtyDYJ8O-GK8ct5HcNfQRMpSs6MiKYUm5QnGHZGTSx1lYe2deJxcTf7jhThVWSNE946gTI5OADz2ZKQvXJLdd_wX6cG_HQ5Q_6p1Wu41aIQEVUuHNFlq6-QL8pGqD9eLIWaeMKZeTUkyTeGZRSAEU3Zm_wAO9-IOwPzv2qzBppDZJ0G0lVGrlPNqCN5SwgtbHbEUblD9gMY79d35xFtDxPwHPGNwtQNIhXtHMfkyIVNnlwYzvoovoM6_S-jPQs-ODTWvBKYsTbeQ9WFAIlIMG9-108EaK2H5Ll6JScqqSgLQ-HYRMYXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام قاره بیشترین کشور را دارد؟
🔹
آفریقا با ۵۴ کشور مستقل، بیشترین تعداد کشورها را در میان قاره‌های جهان به خود اختصاص داده است.
🔹
آسیا با وجود آنکه پهناورترین و پرجمعیت‌ترین قاره جهان به شمار می‌رود، با ۴۹ کشور مستقل در رتبه دوم قرار دارد.
🔹
در سوی دیگر، آمریکای جنوبی و اقیانوسیه با ۱۵ و ۱۴ کشور مستقل، خلوت‌ترین قاره‌های جهان از نظر تعداد کشورها محسوب می‌شوند.
@amarfact</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/661077" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661074">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbtkMJhWEawklxI7BJWA-kpVnJQ6LIfItuZKPbSnHqi5s4SKGhwQ06N2qGEgWZowB2G9mHW0vo0GCiNVV7clpiGOsQdzsvYbqd2vBOHgPFdgf3rkMv2FPTURhxaYQ65vxhqckUNpdwXfntBcAZt4p2hKfZLewHNn5V28ldtig2PIF4E8M6Y_RKXDSmP5rJkB7X1QiVOxDShebXCLT-YZScAkG59nOL3ejL5BdgCrpwHHyZ7aBEzMpj4hPyhmCjf22BCWqBEucjss5z08FNQfU8eRZbWywCfcaehwpUitBHgZTKa8Hy0Bh3YLGM1cWsEHKwMvfiL1ciZb_QWyG9Aczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پست اینستاگرام اتحادیه جهانی کشتی از پیروزی یزدانی در رقابت های انتخابی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/661074" target="_blank">📅 14:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c2d34ea4f.mp4?token=pc39vxLMQAYdXBKeTu3bW42zpoV35guEoSkHv8IBlywGc72khMHqeoPFeORksspul6Q-tJwjtNz0DjU-dif3PhPdaXWd4XZdx2Hx9Z8eFPsUP_fP0BQ0QRM43o7NQRsKKGWkFZUQxMvkiDESNrbXkD4wKmMn2JKP7FqDAfiF_4xyqEOeMfs5D4bsfRSUAzbdKJ3HZA8nRTssxXByrsIq9JPiyzXJ-GX6hMYN_6-gSyQQtO0Ho73hJCruw-eB-QaVhVTm-AyhVZ59iFnQcwonx53FckmS26pJEZaOobcHipFL63cgGAW9vU7DIaQtCXWj7J-B-o5A6fzSe6_FgVjs_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c2d34ea4f.mp4?token=pc39vxLMQAYdXBKeTu3bW42zpoV35guEoSkHv8IBlywGc72khMHqeoPFeORksspul6Q-tJwjtNz0DjU-dif3PhPdaXWd4XZdx2Hx9Z8eFPsUP_fP0BQ0QRM43o7NQRsKKGWkFZUQxMvkiDESNrbXkD4wKmMn2JKP7FqDAfiF_4xyqEOeMfs5D4bsfRSUAzbdKJ3HZA8nRTssxXByrsIq9JPiyzXJ-GX6hMYN_6-gSyQQtO0Ho73hJCruw-eB-QaVhVTm-AyhVZ59iFnQcwonx53FckmS26pJEZaOobcHipFL63cgGAW9vU7DIaQtCXWj7J-B-o5A6fzSe6_FgVjs_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند جالب برای استفاده مجدد از دورریزها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/661072" target="_blank">📅 14:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
همراهی متا با رژیم صهیونیستی در جنگ علیه ایران
🔹
بنا بر اعلام این اینترسپت، اسرائیل از متا درخواست کرده پست‌های حمایت از ایران و نیز تصاویر اصابت موشک‌ها را در فیس‌بوک و اینستاگرام حذف کند.
🔹
اسناد نشان می‌دهد متا در اقدامی غیرقانونی در برخی موارد با درخواست‌های سانسور موافقت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/661071" target="_blank">📅 14:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-84qhTs2tYaA196qTUuSF04Qj6evZ_vRKx6GPL0grl5G09rfHa-28tPnW2mbtYIrckWb2vZwnEiRbteeK4lnl00dUXPe0DTIJK7p-oX4R7d0QI4fFTc1lmotZkzelOGJA-riSoiP-jNs-_gJmExLMT6f0ok7rFalk7BBh3r5HWX8jVIgJ1bVs3oVAFveqKOd8Lc07YUWymXjU5xFMNYDsuVYwGxc5Z0F2nvmD2g2UfnHPAq4K7iN9g3EsjkxJgSeGhC9cYQibFEOQpWPLDGzcaq-g6VdQIDZNiajw4v9Qc_tB-ynl0sK4N-e9jMlEG0C2Dvnc7zWlu0EuRa-mJlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/661070" target="_blank">📅 14:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTNdrGQnHnMyIS-nMmYuRGKC-QALNO2zUjYthA-hxumgXIJv-sRd_aLRiCv5yB1mGfvso14j_Fz74ZqMNbfGv1NyUDQLp-qNILD6BcsInz4Sq0ycX1krBfgnfSejnZihEcnfk7FNAMZCE6Lww8_FuU8K-TQ0KFQzUeRHsFnTC52Z1I9ZoKV7bdmmGye6RYDOLupk4IRkegArsr_249to8-q2o34EZju4zyrDSBU66At7-4yX2If9ge4KdwISuVv_Pg0z_S11vQ8BFn6ATJ8WOnoqqWhCcxaCKFmyNwf541suxfUVVm_ZVlmoHA2s1Mfq9dEnSsI30QUMBu6Fh60Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدمحمد مرندی: رژیم ترامپ به تعهداتش عمل نمی‌کند؛ ایران تحت این شرایط تفاهم‌نامه را اجرا نخواهد کرد؛ رژیم صهیونیستی به شدت مجازات خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/661069" target="_blank">📅 14:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTq3u_vqIzmJ2ATkTXPgoZDfZrmPPS0-qXaGZgqi6baEQdBBCXMV-4-sjaSEJ-A-A6_34M0dcmCwGdjdXCE1q2G-Uqn4Pvl1U7LahgT6suL2U16R3E8GiFNXKSOVyDIjc37dhwawuN9t98iivy0JfpOm3bpumUT4rzl7voqhT8tVAzm1_bsMILaMhfMQv-F7PcT3AMv90ul2jNLi16wcACIHoQIfW_ksuQrF722G9O-fmWSJdJextrarlGzDNazxLrMq55McFpQhgEMBiiiHEp07PMtPJMjMT5Rwd0X_yq73qmzqK7sFhPjAlnZdBviSHSTVMDr9hRzbRMVvQmSE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه گویی نتانیاهو علیه حزب الله
🔹
نتانیاهو، نخست وزیر رژیم صهیونیستی مدعی شد حملات علیه نیروهای ما را تحمل نخواهیم کرد و حزب‌الله بهای بسیار سنگینی خواهد پرداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/661067" target="_blank">📅 14:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL0vNtIoAaWjA04UKUwC00H8_1EiV8DXxHjBjQ99vOl4E0lSHYuOHxR8keK9YeUlRKZ6nZyxhQGOxhduCwzoayEFljah7W38z7UQGveUBvvtiz5OVRGB7arCOXNPLRXDZEAXTiaXz6-Z7VMJSfTz7x8s6oNAw9koFaoJ3y_uX2G2jlXTTU9eOUl7-B_RibR-Brv33Mg0OKGgg6OO5ORPvcaAqYEFcOaDVWoWAIGuO6KgwB5G39IudYkk_LUAARnodCaXxzBhNYKDicnvGyHGUqPN11BWpBnb8zcQZwfh65jN0dIiLLZvkE_i_JA7MdiooUl8s9x-qacvdSWj4wVH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ حادثه ترسناک که قبل از آخرالزمان رخ می دهند / اگر این نشانه را دیدید بدانید آخرالزمان نزدیک است
🔹
در احادیث آمده است که پیش از ظهور، قحطی و تنگ‌دستی آنچنان فراگیر می ‌شود که انسان‌ ها برای یک لقمه نان حاضر به انجام هر کاری می ‌شوند. امام صادق (ع) می ‌فرمایند: «به خدا سوگند، از فقر و تنگ‌دستی چنان به شما می‌ رسد که چیزی برای خوردن پیدا نمی ‌کنید.» این بحران اقتصادی و گرسنگی، وحشتی مادی و روزمره را به زندگی مردم تزریق می ‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223814</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/661064" target="_blank">📅 14:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fee2527.mp4?token=MO-fxX_1zc48-rqk7TKTik92BBwerXjumc0BhwGeEkqVvyQfsIXvJrrF-Y_tkBGjBy96LQ2uCDVK9UXbfVVK72tZuoGsLvhLBcXv_a0jY2N195FVn8GS-BFcFy9u6Vqt1ic6btlzicePE8PnlOACuoOW9tXkrm-48ZydcWAAO_1Rqjwx-4h6ByRMryYnqj6Ia_35q2T3ln1Jv8EZ0Z3wRMEouOKTjrSO9ihgp1J6295RoXZG0usf2dyzxsECM2I4N5B1mVfK-f4KNc8pmpc21zqS7UuPxlBMZDkaaCulS865evRY2dKqyQNoFxwiUYcnhXqVvO1lXmEoFqI5ZhRY_6aO-zLWZeg-kfZnLtFF7zePyMHyOEzFJ9LDvUHyCj-DVutbjd4geU3Nyhoahb6z3GEln3n5Y7ePBmx-HKb6WmvE7mgdbvr-C7b9e48zTf1Y6aLOKEB9K7Hjxm8soqa8tqeOSoDv7Wwbyz4ZDX0G0_1aSIBvm8j3w9mDAEcJ8waLlNCeNPb8l8ZSwr5ByJACK0UhNo7AW-Bz9xjFx1SCo0FyN5MXe3rTdIxY4aKZh8CPl16HU5QLA5GZe7TT4biOj0UDJAVvZohBHRDv_VObuwEjWw18O85C5dEMHA8Ko1XZTZiEU-7Gyd4-RND_PXGSIEkCP5sFjX4AUA3HfzG0EgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fee2527.mp4?token=MO-fxX_1zc48-rqk7TKTik92BBwerXjumc0BhwGeEkqVvyQfsIXvJrrF-Y_tkBGjBy96LQ2uCDVK9UXbfVVK72tZuoGsLvhLBcXv_a0jY2N195FVn8GS-BFcFy9u6Vqt1ic6btlzicePE8PnlOACuoOW9tXkrm-48ZydcWAAO_1Rqjwx-4h6ByRMryYnqj6Ia_35q2T3ln1Jv8EZ0Z3wRMEouOKTjrSO9ihgp1J6295RoXZG0usf2dyzxsECM2I4N5B1mVfK-f4KNc8pmpc21zqS7UuPxlBMZDkaaCulS865evRY2dKqyQNoFxwiUYcnhXqVvO1lXmEoFqI5ZhRY_6aO-zLWZeg-kfZnLtFF7zePyMHyOEzFJ9LDvUHyCj-DVutbjd4geU3Nyhoahb6z3GEln3n5Y7ePBmx-HKb6WmvE7mgdbvr-C7b9e48zTf1Y6aLOKEB9K7Hjxm8soqa8tqeOSoDv7Wwbyz4ZDX0G0_1aSIBvm8j3w9mDAEcJ8waLlNCeNPb8l8ZSwr5ByJACK0UhNo7AW-Bz9xjFx1SCo0FyN5MXe3rTdIxY4aKZh8CPl16HU5QLA5GZe7TT4biOj0UDJAVvZohBHRDv_VObuwEjWw18O85C5dEMHA8Ko1XZTZiEU-7Gyd4-RND_PXGSIEkCP5sFjX4AUA3HfzG0EgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت هجدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای شاپور سعدی‌نژاد که به دلیل ایست قلبی به بیمارستان مراجعه کرده و در ۳ مرحله روح ایشان از جسم جدا شده و تمام اتفاقات درون بیمارستان را با جزئیات مشاهده کرده و بعد از احیا شدن صحت آن مشاهدات را با پزشکان می‌سنجند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: شاپور سعدی نژاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/661063" target="_blank">📅 14:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc005a4a3.mp4?token=AGsnyr27EufTctX_MvTf_4RUsRS3ECw_-LC22_w__k92xRvxZEsI-OM3cMLRPAQGRFFZ0A98e5MaWbJA9EgLhFo_9B9tq4TVFknnUWmSxutqdiJkc8OUIXO76zcEx-Y9ZC-fZOm67KALGKTH5R3tztYISW58RDw9Px-jE9q0wDLC5Ncx1L5Kx0_4l7taDtfvSUbgaYUoNVMZB74hedvf7Y5yU91XuHh3unNgXmSYkun4N7Msbw1WtV7MC9EgNcIc8qXHLn9ak_adM9-f0QqozfBKJk-MaNG4PfVIa28WzMu6VAnKq3sVPGeLds9GhFoemhfpbOj3EPnMehA7FYvbvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc005a4a3.mp4?token=AGsnyr27EufTctX_MvTf_4RUsRS3ECw_-LC22_w__k92xRvxZEsI-OM3cMLRPAQGRFFZ0A98e5MaWbJA9EgLhFo_9B9tq4TVFknnUWmSxutqdiJkc8OUIXO76zcEx-Y9ZC-fZOm67KALGKTH5R3tztYISW58RDw9Px-jE9q0wDLC5Ncx1L5Kx0_4l7taDtfvSUbgaYUoNVMZB74hedvf7Y5yU91XuHh3unNgXmSYkun4N7Msbw1WtV7MC9EgNcIc8qXHLn9ak_adM9-f0QqozfBKJk-MaNG4PfVIa28WzMu6VAnKq3sVPGeLds9GhFoemhfpbOj3EPnMehA7FYvbvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران مهیب آتشفشان در فیلیپین؛ قدرت طبیعت بار دیگر به نمایش درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/661062" target="_blank">📅 14:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91afaba5ca.mp4?token=vj2VDZwa5HRq04ssufHMc8VFZqbhY1B3IBbPRuoL4Re6ZMSPa8nVGMgY_zdpEOJu3Wv6p9qM95vfIPlbdrHqFIFGcNUWlGqxwuWe5LOWUsheIcm875vlDoGBbQUklug6dZ8d9uIk17ydabCIjLGDkk1U_M4Nl0NA7OglUbN4B0tN2-VXjZh9wNFsBtrMPAMRPbttZKqVW8FutE1UOeY39vunc_aj0XA32pdwrJ3XWbOa8GnE-XrdgiUgoSvBNvxzemFiEVwhWA5sn5m02uLsGQjRhvRxYONsLKr1jSdoQaFfXb1dyJ9p9_1QmQKc--je5uX8wfILcU_LlXUv5vPzmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91afaba5ca.mp4?token=vj2VDZwa5HRq04ssufHMc8VFZqbhY1B3IBbPRuoL4Re6ZMSPa8nVGMgY_zdpEOJu3Wv6p9qM95vfIPlbdrHqFIFGcNUWlGqxwuWe5LOWUsheIcm875vlDoGBbQUklug6dZ8d9uIk17ydabCIjLGDkk1U_M4Nl0NA7OglUbN4B0tN2-VXjZh9wNFsBtrMPAMRPbttZKqVW8FutE1UOeY39vunc_aj0XA32pdwrJ3XWbOa8GnE-XrdgiUgoSvBNvxzemFiEVwhWA5sn5m02uLsGQjRhvRxYONsLKr1jSdoQaFfXb1dyJ9p9_1QmQKc--je5uX8wfILcU_LlXUv5vPzmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت باهنر از پیام معنادار رهبر انقلاب به سید محمد خاتمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/661061" target="_blank">📅 13:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را تا حدودی عاقل نگه داریم
🔹
اگر دخالت نمی‌کردم، اسرائیل نابود می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/661059" target="_blank">📅 13:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ترکیب تیم ملی ایران برای مسابقات جهانی کشتی مشخص شد
🔹
۵۷ کیلوگرم:
میلاد والی‌زاده
🔹
۶۱ کیلوگرم:
احمد محمدنژاد‌جواد
🔹
۶۵ کیلوگرم:
رحمان عموزاد
🔹
۷۴ کیلوگرم:
امیرمحمد یزدانی
🔹
۷۹ کیلوگرم:
محمد نخودی
🔹
۸۶ کیلوگرم:
کامران قاسم‌پور
🔹
۹۲ کیلوگرم:
امیرحسین فیروزپور
🔹
۹۷ کیلوگرم:
حسن یزدانی
🔹
۱۲۵ کیلوگرم:
امیرحسین زارع
🔹
مسابقات جهانی ۲ تا ۱۰ آبان در قزاقستان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/661058" target="_blank">📅 13:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661056">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ثبت‌نام در قرعه‌کشی ایران‌خودرو بدون نیاز به واریز پول/ تکمیل‌وجه تنها در صورت برنده شدن
🔹
اگر قصد شرکت در جدیدترین دوره قرعه‌کشی محصولات ایران‌خودرو که روز یکشنبه برگزار می شود را دارید، نیازی به واریز وجه، افتتاح حساب وکالتی یا مسدود کردن موجودی در حساب بانکی نیست.
🔹
متقاضیان در این مرحله فقط درخواست خرید ثبت می‌کنند.
🔹
پس از پایان مهلت ثبت‌نام در ساعت ۱۲ روز شنبه، فرآیند قرعه‌کشی روز یکشنبه انجام خواهد شد.
🔹
فقط افرادی که در فهرست منتخبین قرار بگیرند برای واریز وجه و عقد قرارداد فراخوان می‌شوند.
🔹
در این طرح محصولات خانواده ۲۰۷، تارا، دناپلاس، راناپلاس و سورن پلاس عرضه شده‌اند.
🔹
مهلت ثبت درخواست: تا ساعت ۱۲ روز شنبه ۳۰ خردادماه
🔹
ثبت درخواست:
ikcosales.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/661056" target="_blank">📅 13:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661055">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت پیشین در برنامه «وضعیت»: بعثت مردم یعنی مشارکت مردم در رهبری. رفراندوم در قانون اساسی به رسمیت شناخته شده است. برخی می‌خواهند مردم را پایین‌تر از خود نگه دارند تا حکومت کنند؛ قرآن مردمی را که فرعون‌پروری کنند، فاسق می‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/661055" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661054">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cbd488c8.mp4?token=ehjrzwRDkXBePiTWDpIooAU4Q0u-yhZVj-tmpldLRHKRrbwkMeHgoJuwbs27aos2nlOUmgpRALtS_XAdpAxyKxuW868VE61ArbR2VhBsqrpfKz-JyH8R-8yhO877dlhPxttCyJNMSia5c56Uy8EnjINpDmI5pPta_ro5kpY0B4KzvIPw4l4BcKQhe63xDIn5SsJA-ZQsG6abXXhXcbFq0JRnhtAMcrgA7Teg1jX2BqXc-ST2WcB996PaAtdo5d4pPBDV6T_i67_M6u2uqsu8GWbdP6QbTlujooXOHMLXuBrNYRCvcsaSFBGNeqzScfe8qZ4GzwmE-R6UcCMVaqD5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایی شگفت‌انگیزتر از اهرام ثلاثه مصر!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/661054" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/661052" target="_blank">📅 12:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فارس نوشت: یک دیپلمات آگاه از روند رایزنی‌ها اعلام کرد ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/661050" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJugMewMsmZRqgBabj9sweSw5oj_MapDgVybULL0rhAhI90vM4iHBfpxFqYtsaI7FBRnxG8VXC68VAFsSUDyeV8dYRJ7F6pmkrLi0D_FldP3fc8nNfUA5r3jPn5r2-5Rf6ZTAiEgS2vNtfjDdr-ZkvJNNlV1J9vbNjNvRu7pYL-ATpT3Z-e0r4-u1paVwO-K2CMIWhiNhej4hCntECxguDwf31iiJ_hnED6vUj_ZdeTrvExAmQPorQFA43qgiOiGH3z5MjmVPqW6H06piGlmbR74wRWJZnRf9jPPNKSjsGvyx-drDusFTfiN9uGYu1XJ3tSyDn2cwB61FKog_1GHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
فقط تا
شنبه ۳۰  خرداد ماه
فرصت دارید
❗️
اگه بیمه شخص ثالث خودروی شما منقضی شده، الان بهترین زمان برای تمدیده
👇
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود! فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید
✔️
تا ۲ میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
#بخشودگی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661049" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت سیزدهم در برنامه «وضعیت»: اگر آخوندی خارج از چارچوب حکومت از نظام انتقاد کند، به‌تدریج تریبون‌هایش را از او می‌گیرند؛ ما کاری کرده‌ایم که روحانیت مجیزگوی نظام باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/661048" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e99d6354.mp4?token=vMkO-NHrElic5AYtr9qLfC3a2NiQCageUFO1WkYHfDwBn1lQS5zLuA0vXMKe76qFlTP8UJOeDuRFWGJKLoePiGZnMPJK-B014JQuNwsrKHOqiMUhoiOwJSh7iPyro5_4sS-MWML45Iv_lGVmgLOKi3O27pcaQS21_BYH1H5ixKOC0Tua5jlPwG5Xqq_YvdzyuN-5MSemLxxxrJUOoO4X7FVNJ0zDRnVl-e5RArcldWFtwi4MYyUCVVpXVL9p91IfKgVca7NazYDyRF8DtXjcBJNJnBCMDaoiVhH9H3vpodsME9VrMwVCS7t5qNMCc-jhAR5nfSFbJkDfcDuXm4UfCWH40tnW64kMhdbuv_fM_IHlsjLEJqcyWFDsT292WEnXJqLDyVSFrI0yl-6yUexXnLIMIu-ATuRlkXreZaa9oBUFrp4tO3lsxBXspv9s5Vzq5SbobS7Z9uW1Ejz98OiajO72LEWmfkef0zjU7gVLCUSnIFlO-5SjvBlvqd6YAfUJLS34WbDrYzFEA7L7NNFvH4vYeNnI7gvaUIsAEIxVc1UpR_gw1lmsmXkX3Idut8k_nXk6k7GhiER7AYDrPZnGfEi48TmRXMMYzOmJhDA33mSDR3Ru6_8teeTlyPpeeSlKQ0HpjVgSqSrEVow5Y8SQDRfzQ9XINVR_Us386AFY82Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناخن شکسته‌ای که مادر مینابی را به فرزندش رساند
🔹
روایت مادر شهید امین احمدزاده از نحوه شناسایی پیکر کودکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/661047" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f0591.mp4?token=YX5-7hklF1ftyDY3rAkEbNssqJVJ8u_RPAMbJy3kgiwOVzdwQMQq-OJKgICb0lPO_T1C4X83osTxVzeD1RvvJPajljZqcXy1pi4BPJdMGCpgVTKWjFn8m2U0a7HeE1tm3fS0DMMlOUZXSYW99PqXy9B-a3IVgN4JM4F5Ss1cQPTYE1Rwy-kUNOOr1mHMnc9rXB_MfO5YX-gsKbrmj5vWHToKrrLgsEGClOcBXNnFn70bJJxyZI36vvXLc8K_bJoddAu54hwdOXu5MyIBMj6w-oGBPuEixCvysbKpVf_nNWH6b4DYeNzeAOE1vENa_aZrQiLr0_FWlP0M_EJOCMPw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران شدید نبطیه در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/661045" target="_blank">📅 12:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تبلیغ این ۱۹ کالا ممنوع‌ اعلام شد
🔹
دولت فهرست ۱۹ کالاوخدمت آسیب‌رسان به سلامت در سال ۱۴۰۵ را اعلام کرد. تبلیغ این موارد در همه رسانه‌ها ممنوع است و تولید و واردات آن‌ها مشمول عوارض تا سقف ۱۰ درصد خواهد شد.
🔹
این فهرست شامل سوسیس و کالباس، پیتزا و ساندویچ، نوشابه‌های گازدار و انرژی‌زا، برخی نوشیدنی‌ها و سس‌ها، فرآورده‌های سرخ‌شده و حجیم‌شده، سیگار و محصولات دخانی، همچنین خدمات و محصولات مرتبط با تاتو، رنگ و کراتینه مو، کاشت ناخن و برنزه‌سازی پوست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/661044" target="_blank">📅 12:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48403a0d9.mp4?token=M8mj9XHNmdTYUeGyP-XT05jAooClr57xX5Njh3CSCcMp65QrqhxJ2hBeDPTUr128Q2XagVjSVrjWntXKoL0VNdNRvz9NlvHSD4SIqmUCwGXqOXVczDQArEbBVL2hfwh-vKavzpYkf0o1NM9tDs9h0uyUzhE1ik767zdbSIR8OWuapol1muOgOOvQ3MDGTKFd7R8CsKBf2UVuu8ps-thgcJatdziOMJYmXD8iis_-SLr0HGJ6Ihj7RwjfelT7Qc5U-ydYnnAwkMXDH2NwV_dj3_X7MdVj-ldQktC89sFhwmSQS_RfIyR-DFSSdmdYlnaxpQ3tRlP1l8ml99GiTi9A8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل کاتس، وزیر جنگ اسرائیل درباره لبنان: «ما می‌رویم داخل، تخریب می‌کنیم و بیرون نمی‌رویم. این همان کاری است که الان در لبنان انجام می‌دهیم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/661043" target="_blank">📅 12:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ضرغامی، وزیر دولت رئیسی، در «وضعیت»: فضای مجازی آمده است تا انقلاب اسلامی را نجات دهد؛ اگر سکوهای خارجی وجود نداشتند، مردم نه با رذالت پهلوی آشنا می‌شدند و نه از مظلومیت مردم غزه آگاه می‌شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/661040" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکذیب وخامت حال میرحسین موسوی  یکی از نزدیکان خانواده میرحسین موسوی:
🔹
او به‌دلیل سرماخوردگی و با توجه به سابقه آنژیوپلاستی قلب، برای مراقبت بیشتر در بیمارستان بستری شده است.
🔹
به گفته وی، حال موسوی خوب است و خبر وخامت وضعیت او صحت ندارد./ جماران
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/661039" target="_blank">📅 11:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مکرون: درباره توافق پرسش‌های زیادی وجود دارد و معتقدم که جنگ پایان نیافته است. نتانیاهو باید در ارتباط با لبنان «مسؤولیت‌پذیری» نشان دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/661038" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حکم پرونده «کنسرت کاروانسرا» صادر شد؛ شلاق، ممنوع‌الخروجی و محرومیت هنری
🔹
پرستو احمدی و هشت نفر از عوامل «کنسرت کاروانسرا» به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای خلاف اخلاق در فضای مجازی» به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال محرومیت از فعالیت هنری محکوم شدند.
🔹
ویدئوی این کنسرت آذر ۱۴۰۳ در یوتیوب منتشر شده بود./ جماران
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/661036" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_wzokcaXGyuCGpODmPrVeaDypEGdXyNOJbNF8tcOTldvIDnX3NSLUXZakxmlpaYGTMdiBjeM2Vs9cIJAxl_tdF_40GQaRGnHcozdWJKovbWO359UTxqwn4Db8cx6Nwu9_g1Klow9qf9rJ4NjuNHrzmrbakpe-t-sxowvezCiUyJ-gKdj1E4N63Xq_hiCXxtquv4vf54QezZQC6MJrUFCdxPiEg7_Q666eIS3oxU83EtW-wXkQoxAFt9dGuaQJrFbd_i0clJPJn99x9eEaMz2O1Q0vdQ0BNhBvlLUbMniAoY26q80J1fzDfSCy6fZRx48wQ9rNJD16YjFL71j09azQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس: ایرانی‌ها مثل یک کشور عادی مذاکره می‌کنند؛ تبدیل ایران به لیبی به نفع آمریکا نیست
جی‌دی ونس:
🔹
تبدیل ایران به «لیبیِ دیگر» و یک دولت فرومانده، به نفع آمریکا نیست و مشخص نیست که بنیامین نتانیاهو نیز چنین هدفی داشته باشد./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/661035" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZCEkirjWNFrwJitVzEgsjaDJu4ZU-ZZHMfkQF_8jMj0kD3dGr29uEdlChaNBC7aoCQGBiim_IgavwtzPR_ips459QcEmy4sElG3aAUoMByw1DHNWE19vwW6hGEcECXepfvWvaUznGI_mE0Mhpke8y7QxXNo_uDkeS4GV7pMSGG3Y-1sfTOGxogmQe4-9I8THpsPR2BDbfIZPn-XVts5By4jiH11KsyxgPOAC_FJ6L0Bhlcvqb741o35IlkgL4_IVUEO1nKjXW3otbUCvJjIzmj7bBnK4Og9Ov_x_3gi8tEwVIbiEcEkkEJfRBhZmXzUFuVZseSFbCT_nTi6ZNZgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر لغو مذاکرات نفت رو به بالای ۸۰ دلار برگرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/661034" target="_blank">📅 11:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عزت‌اللّه ضرغامی، عضو شورای عالی فضای مجازی، در «وضعیت»: بر سر اینکه معتقد بودم باید برای حمایت از پلتفرم‌های داخلی، سکوهای خارجی محدود شوند، با حسن روحانی دعوا کردیم؛ به‌طوری که جلسات شورا تا شش ماه برگزار نشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/661032" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نرخ عوارض خروج از کشور ( ۱۴۰۵)
‌
🔹
سفر اول: ۹۰۰ هزار تومان
🔹
سفر دوم: ۱ میلیون و ۵۰۰ هزار تومان
🔹
سفر سوم و بیشتر: ۲ میلیون و ۲۰۰ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/661031" target="_blank">📅 11:15 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
