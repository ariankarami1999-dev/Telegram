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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 196K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 01:19:51</div>
<hr>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=d4cQ_joXgBoD-zhdhHbIQoVjnUUrPJaWaEZoRn_sKHyRjObfkywu-cLta2n5kSDCAusqS22zOQKQrXUPpIn7dSuZkZMVcOLvdERLH9POKI4ykY-Li172zPwUTTW3KqPAa6h90tP-oaoYF6EVcP-t1e8ZQEK4KYJCN_zbmphiLVzOwxgBOg22B-J1zqXWMRl85T7ZlIit9a4I6wQExM_q1VR1CuhqbZdP9LFeSS9Gsq89ZR9j5SEC5mdJJHfa8pbQ8Ua5S2H2Pavj5rqaXInAP51WWlrP0r1A_2VEfdMENKlikiUYHhD-DZzIehvndFeMKcIp3yz86o6HyGpnuF9eYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=d4cQ_joXgBoD-zhdhHbIQoVjnUUrPJaWaEZoRn_sKHyRjObfkywu-cLta2n5kSDCAusqS22zOQKQrXUPpIn7dSuZkZMVcOLvdERLH9POKI4ykY-Li172zPwUTTW3KqPAa6h90tP-oaoYF6EVcP-t1e8ZQEK4KYJCN_zbmphiLVzOwxgBOg22B-J1zqXWMRl85T7ZlIit9a4I6wQExM_q1VR1CuhqbZdP9LFeSS9Gsq89ZR9j5SEC5mdJJHfa8pbQ8Ua5S2H2Pavj5rqaXInAP51WWlrP0r1A_2VEfdMENKlikiUYHhD-DZzIehvndFeMKcIp3yz86o6HyGpnuF9eYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=Zr48wTuyfKkIiwZoaolScuoewpAk-63KH0ke4ENevSWtsbSXRIsDLGY7Aa0mF29Ny7esXzZq5BRbfO2g4yw1yFX7zXIdKShjcHIqMop_kU-B43DHPeYzKepfOYSStm8o9dRNi2MLMiImXKxZRDsuBZGbhYRad5qTRanr3T5Y4-QYRvIM2yRFS-L2dbxys4FxXcw1p88LoU5FeE8a2aqbbOpd2T4cA_JtEq0UH0FaeoRjCb8f922BecwGudFU12PMeo40kMjNiF7w7Icci_BuR8GliTnnqMcvIJsBphHiIYLM3VVRpoERXPU28lComN6BIH90vh5pBMFtqeT2DKTDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=Zr48wTuyfKkIiwZoaolScuoewpAk-63KH0ke4ENevSWtsbSXRIsDLGY7Aa0mF29Ny7esXzZq5BRbfO2g4yw1yFX7zXIdKShjcHIqMop_kU-B43DHPeYzKepfOYSStm8o9dRNi2MLMiImXKxZRDsuBZGbhYRad5qTRanr3T5Y4-QYRvIM2yRFS-L2dbxys4FxXcw1p88LoU5FeE8a2aqbbOpd2T4cA_JtEq0UH0FaeoRjCb8f922BecwGudFU12PMeo40kMjNiF7w7Icci_BuR8GliTnnqMcvIJsBphHiIYLM3VVRpoERXPU28lComN6BIH90vh5pBMFtqeT2DKTDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckVu4k7auW6NY0LUnRH33lAjPyiqPM-GGUej_qe97MeNZSEQ5Tc45zwfWDmUV7N4kOO4As2TW7iOesTlJOvlGE0jYP48nMlNRqoSczH1McaSqCrSv3wNtX4lICCeZyZ1O4-3S4QDyC4PF3xOwKk-egma3erUpzd_jTit0UxSOuq2bRO8vkOaydaUfUFxDJ-kYR7Nh0PmqD7rHiDeAvZKN1YTb_r4E4tqUBpPvBcCINy8Ho9GIZXyQupMsKU_wkXK-w-hCb7bBIMqPd-K2_XyiFqL1VO3yqnTVm3eIB13pD35qa2EyMnvAp-U6_O75J03feYzQ1K_to3HZ5cvQEs30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C12DUM9EzqRCCs8eyDQnaeZ__s4EW6xqNiFyUvkl-b4hE2ljMN6D7n_RZc1GlsB0dp_vNjNZxjkkUHYzyU5Tkuc56wSJx7nFiR1oQ_RRyC4NoLZQrhgYQp8cH_AAtWFAD9A9FhfYc_ANNIT-t8GJiS6IXtOitzvmotLXLLggsG5pXtlg-jUbpB3Y974N5ffTirugXRvXN2alN1-XVF9h6V9KGK0ouwN5j6YVUbdnJPtiw8P-SeFCIoqx2UG5-7_PvdcM_hg-Tydbvjxb6vTjGu_HDA1w2QuFhKMKZqp39N9pPYeekyg_qAvUS7TBomdaIHuPBP2HrLzbLQpQgGHykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3qPXmYLn8wGNo5G2KF9O4UadVwLgwXwjffURIUCrs85uz_eKTDKE-U3zO07oXhQsq7cAAW7saFyOwkETyjj_UzfwLGcSwREhj0X3FjJfeajCaQ8SJWL7gLvhk6SXFvJcUjE6T7zLP0NXMqUpEyBJ8ACZ_bxydGWdSEp9knHofr21cdsM8sfmOCe4CB97FK2EQfsi9SE9gjPyatzwvjSHoZtIgGIg0X6TMb6a4ZtVdLUaO7xeipPDVKI9xF0epl9EcHSCMOqXWXNxnAUsy3uQI2MsZbdI5g5Otmap8GL_de6Sgdbf5GFW0FRSecA-lojnWloHhMnLtaDAhjzjWcABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx21IDHhODKk_9ISG5U9KBvhhI_iN1i8DvkpGgCcKDqCfC7nTemgGEVCzzH7hHcRX7eru_ZS0JYTEYcIo-pqfchAm7rsaarM791-GrH1XQRbL4VqXAGjs2ey5FYtTdrB2X2q6_UiH4zdbvM_tr1D3D2in_xrtcnN--3tadIBxTyIrsaLUvARHeNbeWc3MDh5GkQU-T_4sHE1kg-lmym4LMNgkGafPtTWga5L1uTxPp5FAZW-4ZaPPtfrjPbNWlxoy0yBZuhgLqnFE2keHYq-ylO69eE_8q-m-3sDaxBIg19in2xFYxGKV1A-aaIG1mijgAMf9t6AOiWCyOQRktWKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n61HcjhUsqBn1N2lTx5rHoUa7unvji7peyj1R5A2wZltdWD6jwn-5rRDLCo0QCuGva1Ohl4n1PaXw9341nfl8od0v5IH46QhQffvzK9TRf6fu0T_bodY2tl-7Bd2S4m9C7JBUWSnUJLWETOxzEoDUTz3wrXSR9R5k17MwPLQE7HlyZPTzRwVDx-BvYAdi_3MinbVYstmpasYTQ0pWpVwXRa0pwzo9WnQtONnwV59jRrV_sAoLqXZa6ck0kSVW-fVVfyWsNEoFe5WTJTCkBH2rRJ5bzY9lr0p23QD8b0GE6K6L-oW6EI40W8nkULPnw_Yl7ZQvtkfiZb8oA1wlwDw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G07c6pd8g2IMg8O9qLBMCKn791azpepjaiB78czcgWUExlT0eJKkute4ACLk06Ofn4Ey2ONQmfQETB_g9aAcUlI4WmFtPsfo2l1Irbom6JSIzIOcSjoc868-_QxZdahvkSuu9ERoFQ83iO75VUWPXnMil2MgZM0CxSeCQPCJTIBnHKLo3nbpFi7GJS5eGKsx0dth2nqxcSHNs1h656SheYxpWhYU1hQisQ8RYizCl2hyTxUtUMSJpydEws625MfJrSp3JdIUMqB9xG6i8WP5ZM5LPbpSieqBSe6usWwkfkNXXFzJXfVWXdm9ATfld3zmRIAj8SOv8BvvaJeFkndIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=T7A8BtG6hrErdIyPf3b7zREnCmWQp_vrgJK0Vh3Jj3Lu2TQQmH8l0zIPRB1l1NQGx6yMbakQ2QKEAcCnKlVoyZvBc4t2s8U2vXxKDSs4VQpfZZuNh3-11ctr3GTw94k0PKxvCAnfcFqNuaoOjV-fVinregJG1rQiyWnBxmtJMxCxApwc0S_dBbDRA_0CmzA4uftnI6KC6pBUVRCVVF_L8_XJgpZmCvo9klccPyextEmM23_Wj_RQ6tSIwK61CitDtECU0-EjNl-pGNyABhhqmoGrnQlpLjEwYGAxePVidvG9-IBpsWcQ40yN4y_8mromfa_I-RhpKhzAr6PZok9s5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=T7A8BtG6hrErdIyPf3b7zREnCmWQp_vrgJK0Vh3Jj3Lu2TQQmH8l0zIPRB1l1NQGx6yMbakQ2QKEAcCnKlVoyZvBc4t2s8U2vXxKDSs4VQpfZZuNh3-11ctr3GTw94k0PKxvCAnfcFqNuaoOjV-fVinregJG1rQiyWnBxmtJMxCxApwc0S_dBbDRA_0CmzA4uftnI6KC6pBUVRCVVF_L8_XJgpZmCvo9klccPyextEmM23_Wj_RQ6tSIwK61CitDtECU0-EjNl-pGNyABhhqmoGrnQlpLjEwYGAxePVidvG9-IBpsWcQ40yN4y_8mromfa_I-RhpKhzAr6PZok9s5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNy96DAGN8zQsWtX0XqIMaayhualDAR9Kf7UgSo35-s_Df8Q-JeG0Lu78jpmavCpWCuc1x64CgaMmr0ujuk8xYu8Y3Zu7qdPWwYxKQX76jh6TVPqLYyhj9-Ue-RLDU1BsMOjuoe7abB9QMX3TpQNfgpfzFKVNDF-JOVrTWfWUURqqELJo1jzCfR6ZXdNIEKc24VFUQZPEMeP7BimnkPaFd8_A3IzIM2vodxe5M21j3_N0ia2Qngl1q3EQPX1Sq2MaM4wi8fjTwNxGaBFVwka5H4AtxhM9T7gxeanRXlDoKnD1cHw1-NProveNIzAkcBOUOc5biU3Woa-zxVRMI-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=nP8_Jqk6FrMdDTwx3BlAuj_IhLfMZnTzS5yu1H-GHc97fTpBOaio3r0EERoMhC5baTvLpUKMfHZZb_kY7zGwNtjwmTUuK85073-ssZ3nmzHEm5paF1Ge2eF3_joSOPfwcLQ6oNxMhFOWokaY-BFu0P2s2u117DLSQpS9rL_Gsmyiyp4x3Krvyd7DGRkYOF7NyNQnkFVWq0MxElFlfC9ehQCFYXvdkhIKP9O-O0dAwOr13jg8yuj0qWvLVRQpv8PnLuWdQk3kV6yHzl-RVMYTEPK63XSytwOTSvW1-9ibftQGrx9zMJ2uHcIul3TwfwqiWOVPKciplyrPdWkS2O_KqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvBw4QBM_gMZJonbMtT9ETJ8wQn0LRJv-78LPV7XfWyjIB36mwnsrdCPmhsUS58Z8aL-3EZunaWpEdVz9E9irnGEf8870Wyoo4gFw1wmqTMG1ZqYT7pkGQ96Yzf8xKA0ooVP8Mvbkuoi4tjtfuxNmrffWWxtR3VfICdN9sIlVdD5hAosO9NfGs8hY-l6_nq3gyiyUMbNdNuIrFG5gOn4kwkV39DzTk7n90eMGDzTa8nduPs4MqTHKYnIb-KIPmm58F4MD52fF8cUjJLRE5NhtbpA8eFgj4MbFOcKdaYkTZOqAuaNjwkONvqyYHnH9Flheg8eckDZFr23agjwUYBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqbLTE-BTczhtrIIoBKAZ2_6dQWaru8Tsu-6SGzJdeZw4_Uz4HbTFjLc_rJ1YQFm-1aDndtDWS-2IqEOxa0rnlZ8BcN1A_qMUYkhEFqgueeZmJI6CknGwWrvMAk9ir0EsID1y5PIn7VVDAaAMGF2z0OKS67AGCcxs7VQ73yvpbYV8Dwdmd6iD3Av5IKL9GjwRcEI6gQCXk1yn9JjDS0HO81JZIpeFPD8MeIeR44KoOZkJGD251RP47Xp3XvrqoVOmG52wdtjSgluENVQ6WuK3NBCGsHrHJAsHGkLM8s6Vs4E6B8eVDlmMkt8tb5jsc8IC7FXSqAziJD70RKaXmM5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpWhV9hOf7672TONyWDvUCiNIkb824s9mLLUx0KE9r_U_aq7vGRpO6cnjYwANQ8sd_MATEpmCouGorNMhSq6UjquIqyFfgLT9C7Q8op_FzACzrzUJ5wjjIiKEZUlGPF5-cbw-zwp3EVdI9Plmmbb-ct80nSuznQqSRshxot59n5Ul0NoZm1AtZ54Mg9a5VtYX2ajcQKBnxXGUMY9yJ_nt0bo9Z73VQp0Ap1P16FLnsjQngZqReXEqkixnwSubSyTv5_WA21XSA9eCFrvZg2xNiACsQj4cYVc-e9FG4TaLfmZB35HkKffV5JnDkKGY_TB15Bt3rejFTiWtitv16s5rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=qvR_AGW3rXc29IS5zvtBTo4_7GMiCZHz0KVv-sm8Sa8Y_lwAcBsXZP9eqKzHvioDVvNM9h7dPtQ8ofDdzC08vxJqzYqKvW_uY50VeC6BBDrwuYOJ22jwnIQAEbq0GNmnB5ZPphC9gFZhlM-2Xuxdis97tsfhMTTtEcqmz8zdNngDlE9GRIpLxbE24A3PH_MbOAOcRcQw-BWoEwlWOBLs1pCkhVnYi-vQsAIp_hGDD-RYuhG5_LldoGCvtim1Bu1-nH834hg37piLz3KkyuimY6tKhSqh3nBxXC-osaLQpLHtElPj2FuaOsQqlIbQPQGYAf0Qdg895uz4F0m2HXaxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=qvR_AGW3rXc29IS5zvtBTo4_7GMiCZHz0KVv-sm8Sa8Y_lwAcBsXZP9eqKzHvioDVvNM9h7dPtQ8ofDdzC08vxJqzYqKvW_uY50VeC6BBDrwuYOJ22jwnIQAEbq0GNmnB5ZPphC9gFZhlM-2Xuxdis97tsfhMTTtEcqmz8zdNngDlE9GRIpLxbE24A3PH_MbOAOcRcQw-BWoEwlWOBLs1pCkhVnYi-vQsAIp_hGDD-RYuhG5_LldoGCvtim1Bu1-nH834hg37piLz3KkyuimY6tKhSqh3nBxXC-osaLQpLHtElPj2FuaOsQqlIbQPQGYAf0Qdg895uz4F0m2HXaxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOB3J9qdHkd1ZKazpc7lmXW5lY14nQdpWQEDNaorB9T9dizWADwADq_We5BzSqrs5VB08b7Hj00mRbaAsca1KCx2sM7N26IufXlvv5l-2xoqTmV8P7CrKCGEAn10_nGeKLPUarnGKzGEEJ1FyJmRBkst_Sak_LLqwKuGgjCRlls-CAAdcJ44gaFddj5pm05G-1Rj-RyF6tinivRUdzEG0CGRVFGe6J0RYCll-U0rvTz36LjAbjuaMqKK5PYJbg9xBVs1a0bFCxQyQk_MaHuVJ64idDZDLX6t1eOLi4Wrdi9rxQ3nAph3LGOkl4wKiqrkXEcNvtOlLvA9hqYX06JG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLAXqWArnxmMdoLI8Fl8jf_6XaNbwcgmocPEEvBrDIBPt-0PypG0BDgPjr8i_ZEtys3myqXSeUHgAmKYyJNyT_DHJG-GAXJ17mswryhXtHxkDSGQlSFA-9mS7OZqy8iWCOIWhmVD2qPP_rBrlTwSzf1nMZ080sCkNWT51H6XYu0wLvg8P4d12CdtJe1jVoKvMEcfjYE8vSA6W6MgdMamE8hOfPhJfTk6h6UITD788vXgk5ws6OjZj0Z30xVChAP5iXDJ43TrTeqZR8HrIyA2ZJfAxzj6cz70_ILNbyz45J09yL09LKsZDHogvg75O48RmCDYIqkzck9GRThpXg9khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-EsNavPi8ioUicveS8bGTT8T1lU6Nt4ggs0j0yiQkyfXQxAsQ2KImlW1iTMmJ-BnFeTccdvqwRmOQdA3jDL5gURBh64aVwhOAw3zs7XAk3XQP8zKfv1rE6b0_xwGsY11-4kUp-oSzWpoYIL_hz9kFMyNro2kl_GvYqpWmPHH1nlxvNEbjPRWlH563nHsQLUbAsYNGwm-yKvBwWJShIsKqcC6XOjkIpX6clhRYFbElvzUi5JZWXPxtAZu1aF0hGhEy5YDMZvw7ug7-dz9nG-4z6LPgC6SK6maz4QpxlDg5yCxom3MmTlK4cMuuM4ZXcBMmff11Xuk4m8S2I_Wi_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYlP_uxCncPxCbLRD_hf-J3niwf2NZG8kIwQoxINOHOzJah1uwQv3eQ1dPi3NFgh_ntAgz4yX3Y7YkLllfv54cv9_AABve-sL70W5Sss7VhNGlMI2Vz5n8nUEXtaohq97tis50oeQgp05uyW1a9UQC8JXM7DG6VOdDxZMyUzuyMKP_friAOvNAvPmjqrYAmLemgcjd5ZgD54EYQoxnm4ItfDI95euOYGpIcuvOnv3d-BU-yigvV9yotansQp7s0yyGv3vQFejXMz32_y82-EqBXK4W_GiVH7CZ5-3m5dS4_I0PNZf3Sp44rTgfLBjz2TCgmV-8QoBRZr9ebkG6lx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=niuo_6rQ1ZcI2lLPhwikCm-4VhydqV-gFU2CLM2d2GzosGCXVpf2Cm3E1n5OQ0kFQskXHXgc9XpUZdiRbgnjFu8_EMfvx8LMTpdAQnHKjlg2Nz-H7Avq5oCxl70IUittsGuVA9-ZIo29Q7Fh3v0jTYTEVf8AHE6eR40krvdchTmGE6BcotiOKWwkFkLiwHwAnV4r-la9DfjoMFt6eJh20jtWCrAxRzeSGauAX_ntHGLYPbv5FgFMAHPavFwOUBYFHf2gSP6DWsj52n1OHPLgoDaEMFSaVrQjCztszvJg772aQVKzzsaYiwUsHmzX2JDvebQOzMbxDv91L68EdF68UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=niuo_6rQ1ZcI2lLPhwikCm-4VhydqV-gFU2CLM2d2GzosGCXVpf2Cm3E1n5OQ0kFQskXHXgc9XpUZdiRbgnjFu8_EMfvx8LMTpdAQnHKjlg2Nz-H7Avq5oCxl70IUittsGuVA9-ZIo29Q7Fh3v0jTYTEVf8AHE6eR40krvdchTmGE6BcotiOKWwkFkLiwHwAnV4r-la9DfjoMFt6eJh20jtWCrAxRzeSGauAX_ntHGLYPbv5FgFMAHPavFwOUBYFHf2gSP6DWsj52n1OHPLgoDaEMFSaVrQjCztszvJg772aQVKzzsaYiwUsHmzX2JDvebQOzMbxDv91L68EdF68UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=lOlgik0_XL1sMPxiLLHSgifb2MSbyJGLbT2tOywqg0t0RJ9xUHr149WKbK7tU3QaDN0o3zxsayeDpAsjqHxrsO2IhHq6kgYeD22x5idnp4XuQv7gNq3-B7Q_mttD2GmG0r3COhg8NqCn1ps14sMBcWJLZV2wV9oVRd3LNMA_PvXky8vhRsmd0MKgLeaLluMGDMq7yjp2MvVoq9rhAsGO-JQDahyxqunQtHRAC3LKygTRhn2T49Rtq95Zw4QRR_GnPGHdn9HsV3hH7A0tobArIzDa-Q-5u9x1QQvrvjmIGIVM5HgXtYcZcYGJM_yCXV9ElKny__mCVKi7NfxpCl9RygXKBDqmevhqzdYHtJz2WpCiDLBihGm0wtJw5Tpa2v-53JUjpSGVvQzLlRF7q_SU89EC0sfxjG0MOZhCF9E5Yv1JcVcNdNfMcUGqAnv9K52RIR8KYaFwauDluI_ELvblQgdjxKx5Ryo-woJks6laN6CAv-Wy0GKBx7WTO4_KabsjNQscIeCPn4ftfoP2lsSkQbG2yUI6GQShstHl7Kbft4qqLLVC2Wo1ntLQLqs8w9hHppQ2zCaekSlt6pu3M35Z4UpzFsfQDIiSs9PtsEuYs4cHJwWzF4_jsgqqMcItz7GUW3JLoqzNWmy67MI0xhhOD5TI8Sd9U1qS-elxVpqAmk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=lOlgik0_XL1sMPxiLLHSgifb2MSbyJGLbT2tOywqg0t0RJ9xUHr149WKbK7tU3QaDN0o3zxsayeDpAsjqHxrsO2IhHq6kgYeD22x5idnp4XuQv7gNq3-B7Q_mttD2GmG0r3COhg8NqCn1ps14sMBcWJLZV2wV9oVRd3LNMA_PvXky8vhRsmd0MKgLeaLluMGDMq7yjp2MvVoq9rhAsGO-JQDahyxqunQtHRAC3LKygTRhn2T49Rtq95Zw4QRR_GnPGHdn9HsV3hH7A0tobArIzDa-Q-5u9x1QQvrvjmIGIVM5HgXtYcZcYGJM_yCXV9ElKny__mCVKi7NfxpCl9RygXKBDqmevhqzdYHtJz2WpCiDLBihGm0wtJw5Tpa2v-53JUjpSGVvQzLlRF7q_SU89EC0sfxjG0MOZhCF9E5Yv1JcVcNdNfMcUGqAnv9K52RIR8KYaFwauDluI_ELvblQgdjxKx5Ryo-woJks6laN6CAv-Wy0GKBx7WTO4_KabsjNQscIeCPn4ftfoP2lsSkQbG2yUI6GQShstHl7Kbft4qqLLVC2Wo1ntLQLqs8w9hHppQ2zCaekSlt6pu3M35Z4UpzFsfQDIiSs9PtsEuYs4cHJwWzF4_jsgqqMcItz7GUW3JLoqzNWmy67MI0xhhOD5TI8Sd9U1qS-elxVpqAmk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adGwCLx9eEh1FygU73EM_ZoPQJd4VYbC55Ro8NihT-eWJk-YhmKiUqOixndjv_rISnBb9vKlRibov0VIfz8lXZWgjha8XgJG4jZLF8OCylvHL2V2VuJ3D3w39665yW06NGRn0EQGwktP5AM8XfqDYNXDtwESF8l-g3WB7tTs9Uabu9FZ9e0IGzeNEcEUnGbJmjPnFIBP9vB94ZCQ4gJQOJPRjlnXTDRbp2JDX7ybNr1jW8bW68ZFFivPNoetmfnnTNutjyGFLRxwgWtf1-6Tl9-7Tl-kKu6IMXQ0HeNewfW_bn6ffrCtt-IjyFGwThdzlSuc-NMKOAqvfrcLPjgwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdDxFVAJPFPV9UgOaAljGOt6mFXAedCveNtofZ-E0zNERBUzcEj1sBxGeFgGY-njAOpGwFlBINg7i-zz7f6xauj7pFK1z-uiXwTZ8eBRWAqY52JVQ_kbr6NpL0odEcWL2_TUbW32HF3rz4iPYNVG9E4ZxliHpJDwFn4jHazn4wylTWVgVviQU8PMukOGlAdiN7gzWc9_CjxrU5czh2JbMTwVknriFAShRb_C2CVuAYCRmvK9hv5p0bAKGydyMAboPvdyNVMC-3_PjACeCk2hsfqRTDpeBSqtEc4D267RZDrTT4cK9B-d5L4sIhxL8uju8inAqJj1PwwviYQ3okff6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcKnfvUD0Q_wtXR201axM7XEKfyT3veyRPwM1wqyf7uboerwJQwsuUwT8TDp8jcFXEy0jTDALXqyjLeYLXLDqJ5ysxzG8nsGLRmdHyAiSIFguaoTklISlxNU44BsL_MPVWzZXoLr4YdBteWVWKOO8lKM7RRgO_0C4WsKJFXspbHPmKDDpZB48WvMea2GuBXf3GJ2kKkd8Y1uG8kw_WXSbjXF7Dv3T1fQSCkdK4MpNpeHOHyFUPiYsXG2syWEQru8n0q9i37nsB_6np25HJUxEYiBFLFUjHQLPKOWi201ccpPp0RC5UCniwVtSc5iXg887A8IJTNKv7UnrvP2l2JNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Z3D6uDvAGkTzI7MItqs08nAsolMq_msqCzudSx3SIF0Cnbo7FaDgp1nWNMRWF78Hc5lrC4zfw3Tq3aVCM7P1N9aWVlUko8_T-4rdXOrGL2wvPCTWN-NVqQVrc9ZXPC5rcPqJDX5prv8CpreMUBSQCEZvBLdvyd4nll7ZlA8OO4lR4UWuP3M0rENum51fV53OF-M6Xm5y-u8a6HwIUHXNWPp8oWKOnzSbOCf8sB1_Ffql772jDh9_cPpZvgJhtwWBLnkXSHsx9qz0bJqtYSqzkNuJTWI854EeJjrMVdCeDuTInigZfD6hrg1_fjy2WDCcgbYyAb9sNoV_JOiNfW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcU1qfop8hB58JAYWEqjs2IWQ4D8ejCdOVDg7dZE8gh24WG4A11zozzrLzrnHHUpQRTgZMEhPDfGQA9mEAo1X4sRr3SFwDIybIjscaWK4HTqT_Ln7sDHqn9NLGQIAaJ7a43CPMqQp5t6vbUzAfG11EwIWzkRNO2G6JTvind97RplXdBg5G7396xkzsd1wE86rpyXL7UTAEo9WlMbrymshNMFp4213whh_iWmuNVSz3SNO12rOb3yiECmPdzkibgSpcZEgvPx66SG_nfqoVF-LQMmIJ15RWKXsUneLufBhkPBMbEfCCNW1L8df56sM87MI2UDyk0263dleKTRclHtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=KdZDrD2cXFQJHh_jylSidA-SJ0jnQulb3YpsfAlgLfZTUuFeTQoyD5ZYc48vEttXmU6Pps4em7Ofo4Tjpu2E-8HCV2LeKxiPmN_hY4ADrRE1a0qpnDnepS7Zav1AGR5tH_xj8Y_omue54VygWk4y_W6xZ3-q4yK8vFSnD9PrubuD0XHQSHJxkEy6VRlFzz-Rlcn8CHa6_KRESxi3CFvqCzysGO0QK8bixwVQNYBi7SEjep2cqWZmB-3uGmIBhB672_cHgoUzlOoMQ1SBu9pEdRJDTJqpXCVvTa4aOKwOVOgzZXc6RtOWtQPLL5cISBv7sbeFHgnak49LeuGy-qy7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=KdZDrD2cXFQJHh_jylSidA-SJ0jnQulb3YpsfAlgLfZTUuFeTQoyD5ZYc48vEttXmU6Pps4em7Ofo4Tjpu2E-8HCV2LeKxiPmN_hY4ADrRE1a0qpnDnepS7Zav1AGR5tH_xj8Y_omue54VygWk4y_W6xZ3-q4yK8vFSnD9PrubuD0XHQSHJxkEy6VRlFzz-Rlcn8CHa6_KRESxi3CFvqCzysGO0QK8bixwVQNYBi7SEjep2cqWZmB-3uGmIBhB672_cHgoUzlOoMQ1SBu9pEdRJDTJqpXCVvTa4aOKwOVOgzZXc6RtOWtQPLL5cISBv7sbeFHgnak49LeuGy-qy7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=cCeptjnXEsS2LAtm4o7azZFE29p4vLiLtyKnWznZR55_lMdxCFFe664mKhX7MfQKUqZPrhWJ0WX7oq96THLJoWiel-CbZOzNzJmHCveCXUeYmDBEwPcDNyL7NSO9vZ9T0C-BJupzt_e5iD5A4TcIYoUCVUsfBqgj3Hw2tW6ybGOD0cOozlOweCW1vsN39KSf99RflMZbD6dx38ooygE2eudPnqyW0E0_yexSIwAR5FNFo32l1ZJcK4RKr0BNlg-ltHodS18aa5JaUSYObre6eQNckDWNZJzmABbDTv1QgD5uJ8YsDjae1wk_mNaY-b_2XI4dZ9X6kcAXro1VJpcX14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=cCeptjnXEsS2LAtm4o7azZFE29p4vLiLtyKnWznZR55_lMdxCFFe664mKhX7MfQKUqZPrhWJ0WX7oq96THLJoWiel-CbZOzNzJmHCveCXUeYmDBEwPcDNyL7NSO9vZ9T0C-BJupzt_e5iD5A4TcIYoUCVUsfBqgj3Hw2tW6ybGOD0cOozlOweCW1vsN39KSf99RflMZbD6dx38ooygE2eudPnqyW0E0_yexSIwAR5FNFo32l1ZJcK4RKr0BNlg-ltHodS18aa5JaUSYObre6eQNckDWNZJzmABbDTv1QgD5uJ8YsDjae1wk_mNaY-b_2XI4dZ9X6kcAXro1VJpcX14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvDXGhPY3Byfkpjm3NndP0O9j10AdtLQ7UoUdodf4eU1BVL7sJCq1WgU36-QxjDKDx0dpUHVuPpzUiQf9l3atpFUkac-7xw_AnC-tyKGY2hHhSPos6GjV9hySh6u58BIoGpZkfu5J1lacr4VbyhaVJ-UYQw_H243p1wU_nduKrG1IRYbcj_V7FppicVOXIhAcuMhw6cMhCJKw3tCyC2vdGHDNi_qQ1eOcL3lP6XSUs3D9MIgm-qBj6pPYR1wrTxaynZgSL4o6E1e6m-ppxSEOYO18BRuFJC6CPXh7lag4PLDV43kes4YNB9tcKiKfKbiNhMnINFWySrBx60MPACT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjC2DKcoI2DQynG6SCp6Nhx7p5FHE8Y41-bo9kJEBVsYxVVHBYzNP1gxCOTkjPtSIoIFdr_hBrsEBN6rbVL6B7vn2P4Gea1TiwguiIEcFBzhX3BQpjzoxZaVoFrbURw6i8V7B0aZ94Lej6OV7w0YZ3WMcuwz6mfLjKvNMltdT4vGVg2LHzdIqLK3WLCcm_PjUhmDqDFfXsFTosSiMzPWXZG0b9Iqq1dTMZBZS4HXqOZvLPTLkCJtdxD7xvn7At1XcqSPTYcKddjXzVWIKwWd2J3oP6tmJ-Z0rMmo7IIO61Zq4MdEAxOxnu2Of9ztusnZAl1bQxpaWeYd0b0pvCS1Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=MzLFqfQMQnwuETTQR20FkaNdFOGLKJQNozdsJWDNIg5_sR6SbMH3Qd9d7ji2QIueXc94vZSfuLEw9AzA7ci-yHohMZERNr-wDhozuacVmuR59YwLHoFU9xDFh5wEvAoGpPy6lkhI3NP_rNgf9I3IeLabYdbpM5_XtdIq19hJW6SqHbN0tQPcBNWHe9BsSXbExvDsOVC6sksR0WOwoboBC9As1KyTA4iBwaHj4BQT0SWIgFJ15yn_9HrQFWjHBCtmGZseNjsQhr_ntwS8KQhSwKRDaCU29vn0Lls8VFlbejht291Gs3eHOWUKnWsvvEpnBrTAVw7eKUO3aMe7H8LUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=MzLFqfQMQnwuETTQR20FkaNdFOGLKJQNozdsJWDNIg5_sR6SbMH3Qd9d7ji2QIueXc94vZSfuLEw9AzA7ci-yHohMZERNr-wDhozuacVmuR59YwLHoFU9xDFh5wEvAoGpPy6lkhI3NP_rNgf9I3IeLabYdbpM5_XtdIq19hJW6SqHbN0tQPcBNWHe9BsSXbExvDsOVC6sksR0WOwoboBC9As1KyTA4iBwaHj4BQT0SWIgFJ15yn_9HrQFWjHBCtmGZseNjsQhr_ntwS8KQhSwKRDaCU29vn0Lls8VFlbejht291Gs3eHOWUKnWsvvEpnBrTAVw7eKUO3aMe7H8LUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=FfjwBkE8oIcPOrpua7_jE2qbqRVAbthJwLheuVYinO18IfF1n2U40d3n2theucRP0Vbbik-5KV_LpJrXi94lM-51aMUFpkHxArHIBBVflcBt2G34VuwKexPNOXFh7P82MgrVumjCtcwZqe3aZwefbg2Ip0DZHr0JCIwt7QmoawIwnHdPyCfqlL58_3XXZYYUAjzsH8Qa9wVwVqh3WftfFdhL6GFosBp5x1rSThU4rj6m7pv9Ph4JFdg4VXoxLT9LttzLr1XSTL5axLBIUXDtIRtKfIp0e-DPtNcWA2xWhuHcUapbSwtVf5Pv7nL_PcWA8OiKzyzmOrYvLcEZs44grQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=FfjwBkE8oIcPOrpua7_jE2qbqRVAbthJwLheuVYinO18IfF1n2U40d3n2theucRP0Vbbik-5KV_LpJrXi94lM-51aMUFpkHxArHIBBVflcBt2G34VuwKexPNOXFh7P82MgrVumjCtcwZqe3aZwefbg2Ip0DZHr0JCIwt7QmoawIwnHdPyCfqlL58_3XXZYYUAjzsH8Qa9wVwVqh3WftfFdhL6GFosBp5x1rSThU4rj6m7pv9Ph4JFdg4VXoxLT9LttzLr1XSTL5axLBIUXDtIRtKfIp0e-DPtNcWA2xWhuHcUapbSwtVf5Pv7nL_PcWA8OiKzyzmOrYvLcEZs44grQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=P37mJKEW9zjpN98z529P5X_v-iVS-AGykuMC6DJ4K3plYc43au8CQvwAAGgu_6SPhPj96C5d0SybXdpum0HJyUVTPbqcSR6bg_Sfws1PyKn8n561S17s4q4IqQP8h5Sx3Xc2mm_9iXs5uO8Pv_B1AfQN-iHdunMxG8A-gJewMjRFFFEO8kpbNjZhu1uDkqsxKJcHOqNCPaV0-KuTkWj4l0QpqdG-rlI93e6TzhuiSy_ZPxlaDG1MyO26ijknQ_jOrp13pFnTsRTdzniS8X00og66D0tPt0O56ZXnsg_IQwjDOXGQqNr2-_HnO6ETqfIZpzxzdIEiNT5CIUxMJet4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9tYQbAVc3sOy2grJScZXv-VBS4EUdUnWAz63hWDhGa5VUkRLhnMRskJaFXNsfPkiJCezTFPUh-0FkY4VjeOYV_fF-v1hFDFUo643JW63DTM0I_K98aU1N2FK18O_s9JE_xIn6q3wkGOkFzERTQjXzFTl32Muli1GgrWMt8XtVvipAmwhyB0X25QaB5Lx3koe6QNtDc7rp-PaB9vGoPuLHwB9C-c3aZLCVlqieRczDjcBW3Q4UjFJhT7nYBO5psflwVaUOgQxUhKZYLArnNDm_QsUd8ybX8R-7ltHMlA9N8QNl6qOJrOnOlFg1VcUvqBZqVMLZwLp-_uoiaWp6kA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjuEVh4x71SbxjiMBElTq46js2r0-ueIz07XVhwkL3wLUWlxH3mnbhyrMLfQKUrKt33IaJSalTAmDS5YNRXiPaN-cyzo5krxDotto0B3vTLD_7qtMN-Z8lGhOdGDbOZ-0UyDYyt56K1pV43oqQ4cSfcHf1LqEokjFWkcVUbxJdCUoXzBq16UNtGSjhQIcp6VNxXB7hFgUkVRxqzVMXg4g3hSd_rHpLwt7J4AZBckvzMaX1KDrvarG7VuDz0M1ubeJCJZi7XBnMTNmapn4gjrp81HFtxim0i1DVp1pCseM8gUPPooPUHHTLQ2_j60NBL60sCv9Lf0WAjtOHvG8El0Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=mXQTIcpGW0oXizPNF17uOCB-gYsJr4a9dhW-wmhvIaAdjJ4FKMT_qTIztHd7I7IDd4iHl437zaUrv9M23ADNn8Gxs42cPvNck21z2f6pjznYo-XSRAmLdMS4dcbqFn7jgqFDzJq_37aaLBK6MBTCTEatgyXCx55YH17Q4qaxfXyw7GnQdEPrzMKswK3ADjnbGrGqhi_syyvxzaEA4X_J3PyBZofUu2haMriVx4nv4-8epuD0Gm_s1dbCHhPG_OSDJXbJeSAJL5ahPIYH2UJTYE1vthu9Ni_V1rWm5XDJBz9dvvIrrgZzWwkOULSrvi3xhj3j_ckYApO_bKfz9jypPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=mXQTIcpGW0oXizPNF17uOCB-gYsJr4a9dhW-wmhvIaAdjJ4FKMT_qTIztHd7I7IDd4iHl437zaUrv9M23ADNn8Gxs42cPvNck21z2f6pjznYo-XSRAmLdMS4dcbqFn7jgqFDzJq_37aaLBK6MBTCTEatgyXCx55YH17Q4qaxfXyw7GnQdEPrzMKswK3ADjnbGrGqhi_syyvxzaEA4X_J3PyBZofUu2haMriVx4nv4-8epuD0Gm_s1dbCHhPG_OSDJXbJeSAJL5ahPIYH2UJTYE1vthu9Ni_V1rWm5XDJBz9dvvIrrgZzWwkOULSrvi3xhj3j_ckYApO_bKfz9jypPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mLb-vCCAk-y8UWVrEgznpp7uN6D9T0O9kbXfD7yzSh-VxU7vD-fdNDLAbxhtWuDeL5YlMcII71KgNaxubtT08jWrqP6WxOuJrLZiiMf0WYtY8txwOQaF7ofaCrVSMLT1xS3mvnLaAY50UpAupD_7ZW6rg-XszNyOt69qtY_m5Jup9hTrA_3ZGSCMVPKXXYiCT6lmq-rxnjO_fXPrL4HBb-AYUN-a9hpaHdQ-sShjjV3NBdcoKO8_VNzEb7L4uJexlsrVWO9tkxtTR0iNykUzsOWRHJS0k2JoVTrcqEJk3t9ApXvUZUz3w4aCy9HsykrwOL8yL9GSlN21tVwlCRBhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=mLb-vCCAk-y8UWVrEgznpp7uN6D9T0O9kbXfD7yzSh-VxU7vD-fdNDLAbxhtWuDeL5YlMcII71KgNaxubtT08jWrqP6WxOuJrLZiiMf0WYtY8txwOQaF7ofaCrVSMLT1xS3mvnLaAY50UpAupD_7ZW6rg-XszNyOt69qtY_m5Jup9hTrA_3ZGSCMVPKXXYiCT6lmq-rxnjO_fXPrL4HBb-AYUN-a9hpaHdQ-sShjjV3NBdcoKO8_VNzEb7L4uJexlsrVWO9tkxtTR0iNykUzsOWRHJS0k2JoVTrcqEJk3t9ApXvUZUz3w4aCy9HsykrwOL8yL9GSlN21tVwlCRBhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=sH9O7Oh60_5NZqDzzhg3hASG_or0vbO-5vxQoNNjTFATRloGXNqvSmOcNQeAURDXdgSHTTm6Na4SwJIDxPmI1ipRKBD99PupY4mDlxWrRnhaxK9c2NPGzCdmr37h3M_5K-fT_3vwLoDUqS8tObQlZljCUre3E7roQPOHQq5pEGZMm05_UcfZCR9QV_utpLcabYkX8gxmV1Gw6-ndCfVNVmyaxv_-Bf6drWFYcKWbSX0nL3joOBpt_8PxquF9xFJEY-VTKdaz1ExVBFWy99m4HliLU8ruNLJf1v2A706mymry3WAIFu0UQlo5Le73yT7CPVvOWrfcjOxVenvG7iGOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=sH9O7Oh60_5NZqDzzhg3hASG_or0vbO-5vxQoNNjTFATRloGXNqvSmOcNQeAURDXdgSHTTm6Na4SwJIDxPmI1ipRKBD99PupY4mDlxWrRnhaxK9c2NPGzCdmr37h3M_5K-fT_3vwLoDUqS8tObQlZljCUre3E7roQPOHQq5pEGZMm05_UcfZCR9QV_utpLcabYkX8gxmV1Gw6-ndCfVNVmyaxv_-Bf6drWFYcKWbSX0nL3joOBpt_8PxquF9xFJEY-VTKdaz1ExVBFWy99m4HliLU8ruNLJf1v2A706mymry3WAIFu0UQlo5Le73yT7CPVvOWrfcjOxVenvG7iGOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=ozuJHkKofkhjJHtTwxjRX2AInZ0Ems5_4VIEJvZ4ZtcMPoOl2YG-IJujpI91zbNCkyn3vfLBpQ0mjyorRag920E36hetNofXhOPzDVGLBZ0tPIyHz9CS8EwsoMB839U0e-Y6PJLe6DfEjbzLKu4P2t25HTs99jae9MMArX1Pv5IYlZ-3wOSPaMpXv-ECzM7RHDJkbov3-KcU-A_pWn5S9lTXkAFaHNZbWQ-PeUgIsHH99kBCEe3QC5Rpm68OBDNpISHHBq-nHZH07XPdjJyYlZ1sxUE9QyKJjkitZThiZG076UgGfspoNxCHcYAN0S2pQgFZ-hE_GCZMEkz0qJ6k6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=ozuJHkKofkhjJHtTwxjRX2AInZ0Ems5_4VIEJvZ4ZtcMPoOl2YG-IJujpI91zbNCkyn3vfLBpQ0mjyorRag920E36hetNofXhOPzDVGLBZ0tPIyHz9CS8EwsoMB839U0e-Y6PJLe6DfEjbzLKu4P2t25HTs99jae9MMArX1Pv5IYlZ-3wOSPaMpXv-ECzM7RHDJkbov3-KcU-A_pWn5S9lTXkAFaHNZbWQ-PeUgIsHH99kBCEe3QC5Rpm68OBDNpISHHBq-nHZH07XPdjJyYlZ1sxUE9QyKJjkitZThiZG076UgGfspoNxCHcYAN0S2pQgFZ-hE_GCZMEkz0qJ6k6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=F_RqNgwtXlIaQtlb--i5pktj6g6LGWOnqnZwjrMpJMFpt2zcUUEMJVjzBeCdP56G9DDN7r0zbsRM8UTtQYvM9RZdhxFxNwoJHoAST12GkmN9wrtr5zyFeiO2TCpixtt5F9qOUMABpxIQHulKNvfHSfesyQs1mHSPG9MpfCSjtuVRXMA6iqQfuSnWhQz3Zsb6ORcjdLNShtfMUkfEgLewcfBAJhHMecdXQQpBsgX6bPcpoNGDq9c5RrMa1gtpm-fcKdXrF_bHdibP9iucBMT9ZyPatJDkE_xBcxOSQ0I5V01Yfx3eWaC01chO6fcxKlBL6VVzEYyDkTr6bp9DdUNE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=F_RqNgwtXlIaQtlb--i5pktj6g6LGWOnqnZwjrMpJMFpt2zcUUEMJVjzBeCdP56G9DDN7r0zbsRM8UTtQYvM9RZdhxFxNwoJHoAST12GkmN9wrtr5zyFeiO2TCpixtt5F9qOUMABpxIQHulKNvfHSfesyQs1mHSPG9MpfCSjtuVRXMA6iqQfuSnWhQz3Zsb6ORcjdLNShtfMUkfEgLewcfBAJhHMecdXQQpBsgX6bPcpoNGDq9c5RrMa1gtpm-fcKdXrF_bHdibP9iucBMT9ZyPatJDkE_xBcxOSQ0I5V01Yfx3eWaC01chO6fcxKlBL6VVzEYyDkTr6bp9DdUNE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=koo00iQs-E6bJWXJ1O9ZwDOYFKR_RFL_m3WFoQKFgM_vI4y--ajW4wzD_k9Ndk1s9W4lptqPXYWexO2iOuQ7k146poNSfvbU_4d94qSqRJfaZ8WuUr-GvgLTImKik7wJnOdjB4Afd40f-Hym58W73EkiTohTeuNcQR90etzs0L_WH4Wkuwa3o_eOH-Y4RcGgkpA3BKMUTW_A8-uq0EXj2XSPL-a5WsCip1Z7BwR3AqTj-0xTvUVELI34L0gZeY0CyHJuz3hqCuwqJt0y1lE_RQ2swsci1IiNUG3uX2B3ag7srfBVxD_m2FGRatclT1mlhTrlslEPanYZiw2ezKlnJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=koo00iQs-E6bJWXJ1O9ZwDOYFKR_RFL_m3WFoQKFgM_vI4y--ajW4wzD_k9Ndk1s9W4lptqPXYWexO2iOuQ7k146poNSfvbU_4d94qSqRJfaZ8WuUr-GvgLTImKik7wJnOdjB4Afd40f-Hym58W73EkiTohTeuNcQR90etzs0L_WH4Wkuwa3o_eOH-Y4RcGgkpA3BKMUTW_A8-uq0EXj2XSPL-a5WsCip1Z7BwR3AqTj-0xTvUVELI34L0gZeY0CyHJuz3hqCuwqJt0y1lE_RQ2swsci1IiNUG3uX2B3ag7srfBVxD_m2FGRatclT1mlhTrlslEPanYZiw2ezKlnJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=muSBg17Rx6sW8DHvNk2_Hk4DHej7HQCp2UD7KCejftzeblaDw1VrEKHwggbHk12GLjbiA37NVEuhCDX2VTbqhP07_vSX3R68_3I7y30LfKSHxMkeDtFUIeBgBOs9b99WwtZMpNcjr7HMC8NKfJlRKAwoicbo2HVm6vmlndbW8QMRXN2sgbiYaw8w89dVFp7Y_46ES_d2qV1svk1heTIE4lNJG25gH8ReBYZ5CV8CFFHs34h_LZgjtpvMqcjuc-hljiVnT_-AM-DWFHYxQhFxBqvzSAf7fmYxrvwBBESC8oChQzDOQ3oEkhKGbKQnPToP7Z383F8u4egQur_gajurMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=vvtNNbs2N4_s1o3QpCoUbh7oOjX52FvBgLuPjAD_OtRxv0Xml0WpIzZYFKXPuCuZP9GUe2yiXRxbI4Sgzz-73O3g-ni_wrB-tqgseVwO0Dj-e7mVH8gSCq_J_muaJqOwcu6zdbbA-9EkiJW_ZNx_EGg9AHs9p8nsSXhW9y9XR49n4LOJ72X1CIxvYghUCOfN3wCJX3TCiJn4aCQY-u_BJDxUirRLc1f-w1zIjB_3c6h8FJin-XOaBsGKTjGS3Ku-k4YHGEk4eAdmsMQtndzNwCawajEbXfygKf5l5zjBbzSMvdTvlrD93VTML42LYy0ih9-MzELnG9zlfCrL-cbbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=vvtNNbs2N4_s1o3QpCoUbh7oOjX52FvBgLuPjAD_OtRxv0Xml0WpIzZYFKXPuCuZP9GUe2yiXRxbI4Sgzz-73O3g-ni_wrB-tqgseVwO0Dj-e7mVH8gSCq_J_muaJqOwcu6zdbbA-9EkiJW_ZNx_EGg9AHs9p8nsSXhW9y9XR49n4LOJ72X1CIxvYghUCOfN3wCJX3TCiJn4aCQY-u_BJDxUirRLc1f-w1zIjB_3c6h8FJin-XOaBsGKTjGS3Ku-k4YHGEk4eAdmsMQtndzNwCawajEbXfygKf5l5zjBbzSMvdTvlrD93VTML42LYy0ih9-MzELnG9zlfCrL-cbbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=SvVPVpeTHy-bnTLYVcX4ftH-GwMJv7LIQH7DQ7BEJXJLzkG6s5X-OGrBuQV7cVBcWCfSsjponEmrSSbN7trq5R6ZCdN3Haj55ppuRR9Ob1-hvSvouaQbvXOfIDuPbuBxl0wXRYxW8vR4cy8Zug-WoTlB-LFIvFwKnio3-7hHLwvC9YkJFVdvzgaZV_gNpV8zjAgUxxppGnTtlkeJaRmysbQRBvPga8xNfEIyDBrMmv_-GdIWFZKxUNlkH9rEDbI8IfEQEhEQtPOLGQwMtEbxhxprkYBTn5ewjvPyBvUmrPEu0SHeaq5d1uOje8D4Chf53_XnSgbczNkwTS_DapWQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Wa5F9yY2GEeB3AJNIzF2SlzDBXKMpz_SHxDNpZs2LA-c6hjf6oWrTByqMtwvd0ibizTJdceYClmwkrbfXXn63k6yD0DQkelFthzQjQ3j-_WxGDDsZppGSYGnACsQapBrPiEXe9uXRPuzVKmcV_oLESdyT8MzatXrCtYY-zHIg1tHNmkpqVPWSn96er3XIW2bowKdcPtOEgOHHXL4yKsqZM44lT43G3kR_F5pVMilepPQ1GiZADWw0VRP5XV33ZIDtjtS9_I1guwAX9kFzNEONb-9TrS5nfu3dLQUBtBWbbvqqh7trKjZLGpHOV4-rlgw4Wg6SfeqihtBJwfwEzo1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Wa5F9yY2GEeB3AJNIzF2SlzDBXKMpz_SHxDNpZs2LA-c6hjf6oWrTByqMtwvd0ibizTJdceYClmwkrbfXXn63k6yD0DQkelFthzQjQ3j-_WxGDDsZppGSYGnACsQapBrPiEXe9uXRPuzVKmcV_oLESdyT8MzatXrCtYY-zHIg1tHNmkpqVPWSn96er3XIW2bowKdcPtOEgOHHXL4yKsqZM44lT43G3kR_F5pVMilepPQ1GiZADWw0VRP5XV33ZIDtjtS9_I1guwAX9kFzNEONb-9TrS5nfu3dLQUBtBWbbvqqh7trKjZLGpHOV4-rlgw4Wg6SfeqihtBJwfwEzo1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=T3rzK8gbZ8RWSDnfScMkegcbl4fnCyctlBVtJx7tAmlymGvjZRZMwM5rGsC7Vh8kDbw7FW98-tesYWCsrcVrOj7ysRuCa_H5GbwD3CBJlzhZvm4Is_-BmUQvMXBTsohdrTWlRdIl5o_zEX3zv6mq6qTkx1_JSvGHDMBGSs_bMgMRYOdDZluEYj5J5JqK_x11NtUIDxzld8xF-MH8BRjtpi5xmgJHlxAtqmiRNLdkGnRFk9bjfaeDUUUXlccJ8CVHcIvinrdgf3FZle_rKXkquWqlLmK9g7WD24ovyYwrKbt_niN98yuZYGcKO9stKaelUqpqPzIYStg7r1GACSRwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nfGgD2ulUO6ooPGS5Ich4RwAyE_CFQMv_GGK-KT1gsDNJgePKo39zHGU-gwFhqEDIGC71kOYKRM2db5vNAn24R1SGgS72PutWVQ5AJfSaq7CQ7yDgrRwSd5KDlQNo76HLUv9fDqXlw3GzCaLo0jsdKhCbSqlfW-nIUwNJ8poMFAeL8449-0KjTOBwCi2zKpOmvIeFCVNfmhFHIAtvyBspg0tz_Al66079ReUO2rPgGCMAqdUMjp8ZiKexCj6Rix-VkPgQ3AsnoId-HYMIWaAWpiYuTFpvE3vTXavI7r5Dlng6Lq9mD6pirtlA8tMzLJU553_YfKB6gZCSBePzSKxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nfGgD2ulUO6ooPGS5Ich4RwAyE_CFQMv_GGK-KT1gsDNJgePKo39zHGU-gwFhqEDIGC71kOYKRM2db5vNAn24R1SGgS72PutWVQ5AJfSaq7CQ7yDgrRwSd5KDlQNo76HLUv9fDqXlw3GzCaLo0jsdKhCbSqlfW-nIUwNJ8poMFAeL8449-0KjTOBwCi2zKpOmvIeFCVNfmhFHIAtvyBspg0tz_Al66079ReUO2rPgGCMAqdUMjp8ZiKexCj6Rix-VkPgQ3AsnoId-HYMIWaAWpiYuTFpvE3vTXavI7r5Dlng6Lq9mD6pirtlA8tMzLJU553_YfKB6gZCSBePzSKxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfAPBqg--Bh_uVUpwL-mQbHUnfq2sLAeFjS8Hsw508rfZ0A9f-dgAmITwl6tsu8HiETonHLCQ4COy3YwPI6XxbDh_SzKSlhQBIxKb6ubiCciVcuLp-jymkZuSh-Su_EsjQA_RY-xJ1aJmpQ_DKXjwPHiaf03mafM7ARR5ohf8WigrRg1zQwKqlLn41IjqIjmnmHJkQV4AcFwoag08T0b09TpzA_6_eyQB1rEJ51-bNeqtDrh8QVyqRQSgcFyc5exUT233TS1a_rO_3tf4Vfu0gwDCtLkzWQ0MZi8eygn1Sgde-TiCidHFqR0r5AV478hsykVvDh1GjRd2DuURX36yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS-r7y7xC6TgPj97s9JtzMCfgf9jTJwa8aBnOMubSgBRB6xBGF_j8u6iEkL2ag714JicQn-qa0c8yRhiCtRTOlUEAn9HZMHWzET32Mv9PjW-JyyoKJdQY6duPdXqWZRSumt2YmVRpX3XFPfaKcpGXiFFqXsDwsJRXwiblvWC5DNy_hY_brStkML8xbNC7Zr3G3FvGbsRWKOWFdwGIYGTCHX1D5R7AYSPgHvRM7NC1hGEHK2rifIuddW4tAh2zVnTV_dw6oS_jAt7tI5DWvcuN42ldECTLGTjEDWk1-T-YRuTBaBN7FkROs6i9J1uA7DwL4YA_sxa2BRIEgx90TEZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fil4-EzhnkqZXRHk_eklNPL1_2cm_tyI6h7UIQR9OUNuEskm2KFjkafLP3fgW0vFcoNwenblGvhm_9j6k7zEgruwv7P81yxHilWyZbcsd4e4kUiCdy-rLxxCstPr-ziRi9WjfpDPtU-BhT-xCfK1zXoTgF7N2K6O1g4WdE24WzN7GetFs_jotZt-AJNw9OGyCMcPUTCVzj0ytK54TAAFZ9Ugfac5ePNBETjh-Tz-pAZnM6710OJs90XgRDeuYMr5GCi7udD_Em89ZhUd2oCGpImz7siNWENHexdTLExJAh8jeC1G9MHV3w4VrmosuakfNJSWhL-HUv26f33tnTN8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmWphOmT3W9vJ20RVgz97euTRUdWr2iBY8FywFmGuTwyjF4Wed6G-Ekx8RuUb3vIV9PF9i4MFsjTUbnZSl5kmm22CWqRVRCh8tt0hVxtV-2pUnX08AkfYPi7MtRKudd5qgNIup3AOnHZh0SQeVsHRfd-_r8yOznru3jO2ROcUWfKEjQvwwMBouA5R01HyzhtcEUKYN51QrEN-1Muubylb19Kx9PJZTi5h9hkO2c3eH1InigqmGa8s3Me6tEV93hpkoZAXuIVO_J-N8DeS621PDjYZ5S54nHSItCwAPN5-YGTDvQnEbGCaXKxb0CwjvFA5Vsm8CdRHFbNGmFQ0abx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA0y2iGnN3o7bjHReZB_XCjeW4h0fmJt8cQngjUf7wGuOFVLTmfOms7o0aoElvn7A3Qd9VCziqmWh_NFS-AaCgihKk3ngmZNP_NP78znm5Vcf5Y37QKz1tU9mCnp285x5VcA6odj92eZPb86X0yyG0E3tnlWEFGh2At7YyQNJNAj1Nmc-ZJLWcqWmkLcgeZyJimzYumOfdwV877B6JycqiMsPaSECPYry6s4t5bbufxfryoVhP_5SPj0NUEP99J04YqLUJ-BD7GAibwq7Znl1pqO5p6V_8B8e52_bKVtele44ORvUuQn_VQCPGfqPLSmEZbOPnAivZVzGEsnP_kJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgJvHyBR_VFHo5rmwUe_1c1IO1EeTM8Fr6_BQEI1jDqdvg1LxB36UibYtSqw7bnCD4Q7TOFBeQG6IOqGvXc8MSOPB87zCTGJ0th0R-5KE7oLh1xQLBUA4MTFdEVXXIJOK_wUqyAinkFkNauxYQG-lySVW4K3TUYiLm0QyMi6cSG1HibZvlwh9mh3QOw8_wh-cC4psoi117_7mJLOTZO24l4ZwPY0xsBXj9YrhSEKE4qEQlXVNMe1i-9BFVHn3AxyYAn0F22nwX1CxkeiM9NJU99j8Wz-ow7_zxoxDm_faDgQ5OUTKfmNkzK04oJ7MPYimVIuhP67kKEBnwfBsFLFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=gMw4V4wypiQeIVOm9AsyPIpV8-C5ZqWRDgVpCsD4x5oWwaoCuip0VC6ukGbGDE3YlwDgOV69cTpxmtmg6ZxL2-_1h-s8g4kSGX191MW3NdzSlip4W7EyQKW3qQcrqjbx3WOtLzzhHVLd3EzVe6NQ615w5DdiCv_N-XROMoKfwbmtLmJl2S-LZonO6fKIMhyjlwK6pOG0Urz_tTENGie_hu7CS3zVAvvne8ouQ7nMiGyJtsij5-CltVjD7ccqEAWk71-qpd5TbjvA1oa5mQRmKaSEj273L-pta0V0_M8eBJpENAUIDrliOb29QDQMhLjau1hG4XUmFcq-XIZhRqjBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=gMw4V4wypiQeIVOm9AsyPIpV8-C5ZqWRDgVpCsD4x5oWwaoCuip0VC6ukGbGDE3YlwDgOV69cTpxmtmg6ZxL2-_1h-s8g4kSGX191MW3NdzSlip4W7EyQKW3qQcrqjbx3WOtLzzhHVLd3EzVe6NQ615w5DdiCv_N-XROMoKfwbmtLmJl2S-LZonO6fKIMhyjlwK6pOG0Urz_tTENGie_hu7CS3zVAvvne8ouQ7nMiGyJtsij5-CltVjD7ccqEAWk71-qpd5TbjvA1oa5mQRmKaSEj273L-pta0V0_M8eBJpENAUIDrliOb29QDQMhLjau1hG4XUmFcq-XIZhRqjBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=UdpxSYG93TsiUOy5gvB6pjhvDyAtP-QabCLlcD3vqy3hn0tgV-6zwb70_SRs20aUWBcS49yhg5Aeh5MyPDrvGv5yR0iKVH3SWl75Sc65lh89wV2rWS07dNJK3KZC31YL0ey1FPi2ovLhdz8U0z3BvU5l6k0yFO1GvInY6S-4qyjM_yGpjB0EjTrChGv9eFvL6taiSe85XaE7Zbyp1xc1yGgwq4476TTG9_38VBkUxM_qo2SV7DzvV8a4L9FdqHaeGZ9Tbo0-Oi6PEUVuIKn7tS6nMINU4iV77E_J5hvBn_T5Ju3mz2ScN71lxnIiNRY_MVi1RZJmB2fpUbybhiIwKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=UdpxSYG93TsiUOy5gvB6pjhvDyAtP-QabCLlcD3vqy3hn0tgV-6zwb70_SRs20aUWBcS49yhg5Aeh5MyPDrvGv5yR0iKVH3SWl75Sc65lh89wV2rWS07dNJK3KZC31YL0ey1FPi2ovLhdz8U0z3BvU5l6k0yFO1GvInY6S-4qyjM_yGpjB0EjTrChGv9eFvL6taiSe85XaE7Zbyp1xc1yGgwq4476TTG9_38VBkUxM_qo2SV7DzvV8a4L9FdqHaeGZ9Tbo0-Oi6PEUVuIKn7tS6nMINU4iV77E_J5hvBn_T5Ju3mz2ScN71lxnIiNRY_MVi1RZJmB2fpUbybhiIwKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=LnbIou6rBGV-2LNZqd1PfSA1H81J1Qk34dbAp1wOOXyboURXuL_npEMBu2jx2zd8edwZPkUh5zKDFDQT7oR_NzMPTNXjaQLJb42GVgeq8FUN-N2_QGv-8j5vTmF3zt-tWW-b2LZppB3gOsPrls5u-LLX3gAwNCdzcUPVgH4uoMo3ncvE0agDxfCg16sH2Ewwn9cz6aUPgN8BIrNigriqKZxissQWaaFqL7VR8hs3Ds31onbdwWFtRrK37LDnMshn7i4YQluPO2uw6BX8_kZF1dhCDhhnSiJDCzuwPt56B8vCu2UPD2tGCz3GgzDJRuweB1EkBzQR6sVIpHSjXv9X9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=LnbIou6rBGV-2LNZqd1PfSA1H81J1Qk34dbAp1wOOXyboURXuL_npEMBu2jx2zd8edwZPkUh5zKDFDQT7oR_NzMPTNXjaQLJb42GVgeq8FUN-N2_QGv-8j5vTmF3zt-tWW-b2LZppB3gOsPrls5u-LLX3gAwNCdzcUPVgH4uoMo3ncvE0agDxfCg16sH2Ewwn9cz6aUPgN8BIrNigriqKZxissQWaaFqL7VR8hs3Ds31onbdwWFtRrK37LDnMshn7i4YQluPO2uw6BX8_kZF1dhCDhhnSiJDCzuwPt56B8vCu2UPD2tGCz3GgzDJRuweB1EkBzQR6sVIpHSjXv9X9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jKkMZ-1imoVpCqwPMvG82pxydLHDOURAOrUV9eH94vfm0BWL9E8bv80EsFDRkhODcgqEPRmGNLxOWtNuprOer0DbrOiAwu8SPuNjKv5rypm4LRta2i6tFMGT8NrozYJ-ykjBHwriSkuR23CadvlHCeNkuAkERNhK_Wv4yxT9noHIA1RZdhy9Rs2qUN_cIGQyB3Yo1rmBGFllXWXGPZ-2cL54GAqZw6iNLShhwY_Awtky5FydIpWZIWRebAV7Xk3Z94hdd0b9V4_fi1Y-hmTtJrbdx_Do_SZhY2j8i31Jg4GZIOt2FyT9OubNtNPuruBIwOG7QBXlzXXuvzDtIfTuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jKkMZ-1imoVpCqwPMvG82pxydLHDOURAOrUV9eH94vfm0BWL9E8bv80EsFDRkhODcgqEPRmGNLxOWtNuprOer0DbrOiAwu8SPuNjKv5rypm4LRta2i6tFMGT8NrozYJ-ykjBHwriSkuR23CadvlHCeNkuAkERNhK_Wv4yxT9noHIA1RZdhy9Rs2qUN_cIGQyB3Yo1rmBGFllXWXGPZ-2cL54GAqZw6iNLShhwY_Awtky5FydIpWZIWRebAV7Xk3Z94hdd0b9V4_fi1Y-hmTtJrbdx_Do_SZhY2j8i31Jg4GZIOt2FyT9OubNtNPuruBIwOG7QBXlzXXuvzDtIfTuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2JszQxZRnu5qZulK2a8APWPOTUfwlcw9TBq-H9O2H_TZ7fTITSXjgUgbiBzUGiSM7sdp7CK95TFHgFBMq0nHW_pjoDmve_uieDQLh6fqdyqq7PwUKh2IonSLi9A4o3bESMbWfe1gT5V3X6AwjoBN7SOG-VeAMO7kPetTE3wv5s3Sj7OHjjnnX0Y7HYoiWvnWH6xdnxcl58DqNz9LGzrLDaDlwVXWpOoHGXrT17sPEPkUJ3-kGHubM2xBs1ie74ZPNB3meCv6mjmVy93EHDivwanIMJg9t9qGw3VCQNmgAkcrEj2SNQZdJiWquIGrptnOg4k9sbroP8puXwFPMkzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=t4fO6RiG7tE_CReazAqcg9Hg-uZtoZ1WOpofp4edHbfVCMYnS9Yln5t46O_5bz293xr2RQyy0OZjXoB1n22WQmVPXf1MGBAWfNTRQRWEakNC63NQx-T_K-DSbbBTGYghU5MRhpn54ikrJ6XO4OpMUEwrKOpNZREXIILH6rHAmiwCC6KQrw8Z0Z861lpXwGh32grWIkq5k4r6dSKsBydOodsaaEiiGaHtoQoax9Aa4sH2-Nz8F7FOqJEUJHHQ3hHEBaaAGBnulV1xB1LfX6A0eJQfWP25LZGnCtsQ7bTb1yngR3z1JPiIWbibnQXKA-RE-38xQ-K_uuXbMJtrp9XXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=t4fO6RiG7tE_CReazAqcg9Hg-uZtoZ1WOpofp4edHbfVCMYnS9Yln5t46O_5bz293xr2RQyy0OZjXoB1n22WQmVPXf1MGBAWfNTRQRWEakNC63NQx-T_K-DSbbBTGYghU5MRhpn54ikrJ6XO4OpMUEwrKOpNZREXIILH6rHAmiwCC6KQrw8Z0Z861lpXwGh32grWIkq5k4r6dSKsBydOodsaaEiiGaHtoQoax9Aa4sH2-Nz8F7FOqJEUJHHQ3hHEBaaAGBnulV1xB1LfX6A0eJQfWP25LZGnCtsQ7bTb1yngR3z1JPiIWbibnQXKA-RE-38xQ-K_uuXbMJtrp9XXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=SEK2-CXnWrWpDNn6SWNAY6NGhzeB_tVuGrVDgAw7VtZ-MkaNcvlbaXK2UkwSS6E27tg4q6mK3Gdle0TsUVumhaxml196nWw4SuS-V98oiy6fkOwkLlGLyN3gLvkOm0ewg6mQuCc7QNsDmbpMq27qtxvOzgydDSIPLAmFWBXRGHq6skTXgiuBFcV0wgxeFs4BtVSqnHzpdmeroSLXk8QjkjrWA0ueBTm-xmLXvn59CJ4-2TBeWAgyIeP-jK8DFjfRT7WXJc7r1wpSfc03TD8UBdvj6XoQmNcWzPrOyEMbQZhivIvOVqaI1zsheZoqJlxhjpz63Hkad-zY2WVIIqg7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=SEK2-CXnWrWpDNn6SWNAY6NGhzeB_tVuGrVDgAw7VtZ-MkaNcvlbaXK2UkwSS6E27tg4q6mK3Gdle0TsUVumhaxml196nWw4SuS-V98oiy6fkOwkLlGLyN3gLvkOm0ewg6mQuCc7QNsDmbpMq27qtxvOzgydDSIPLAmFWBXRGHq6skTXgiuBFcV0wgxeFs4BtVSqnHzpdmeroSLXk8QjkjrWA0ueBTm-xmLXvn59CJ4-2TBeWAgyIeP-jK8DFjfRT7WXJc7r1wpSfc03TD8UBdvj6XoQmNcWzPrOyEMbQZhivIvOVqaI1zsheZoqJlxhjpz63Hkad-zY2WVIIqg7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoJogMZkCb7ZhmYC2ZPDrF7EvrCrghriYGmqrY0ARW4IAV7JhyRgRs6uPeMeYU1dlWDOPbH2etRgsvjHfo2if4Wv3gK8DdBkXNWhGAx3G2zJZXTlKkM6oi3U3uHGd528UYL8MAmWerjDImhCAZFBNdkWsk8TGGatztVGGkpyM8wr6-uwt_1VVoSQyaEdgSuZ9tq4xGgZ1ABaEPdtYVGyL-skFkDxHV4mbazHtP40U67vBcVsh5F-R9MmM5YIxlH8izaKRssTZvpAukJU8Hf-CljxowJVxr6rilvubw9SlddcUozgiBOMb8ZCTyeQI7q770C4XM3z1KXqd2e6A1rFPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbGbEykjNaecw_ykIHIUq2smmfluIGgVQ52EckMzAPwTea5n7fclaGKak_wMdsunrQPJk9SJJD8NvfFhdQNqWJXLmHIm1ULGQz-8ARE8ZAzE9g8GQlmCd7ZydUN2foBUtd3yXbpDWWIZnDlco5hLHiBBItG0UQhnCV8qXVI90mipl4BUJom0iUQ5w1iT0rzI8j-GV3u7jOVzocfNB3kE0QW0We8hvpmI5f8woCPu1rf-sbpiYQZPgtgYnrY7XiH6nsNgTmKjMYM35YDGFc5CgyRjipW_05P2msSo3zbTE6RLVLpIn24dUs83wA4-luWVPN6ryjjGiwYuGDpGY8DLww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=OR0YupnM0bE6QfsQw8ahW106zsypXtnMhL4sUi_WXTbR-h4txDOa9W4vsv4M9Gh8CslQ6UTqYBVQH5YgN7vy58ZF1vhjvBLLuI7LRaTmJaWrAXNVKf4IHDrnO1qIdh7nh8gyDtqAyl69vj67odyosrnIM0R0a0UPTARPkF7oMcNGNFZGcZWyZnqaoN27rw-wSgqnDQ_fI3b3z0glYUyiHV3ZpkJtb8G0ii0qMdBXRPAac5XUkCHrVyX5TnW85byvwVNydJ8yVtq_rhiYMQ749u1yN94CZgLwdnpBHV_1vxOe8NoZyozPE0giGnkCBh5HlKt_pjRlxri6qzkwtvBv7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=OR0YupnM0bE6QfsQw8ahW106zsypXtnMhL4sUi_WXTbR-h4txDOa9W4vsv4M9Gh8CslQ6UTqYBVQH5YgN7vy58ZF1vhjvBLLuI7LRaTmJaWrAXNVKf4IHDrnO1qIdh7nh8gyDtqAyl69vj67odyosrnIM0R0a0UPTARPkF7oMcNGNFZGcZWyZnqaoN27rw-wSgqnDQ_fI3b3z0glYUyiHV3ZpkJtb8G0ii0qMdBXRPAac5XUkCHrVyX5TnW85byvwVNydJ8yVtq_rhiYMQ749u1yN94CZgLwdnpBHV_1vxOe8NoZyozPE0giGnkCBh5HlKt_pjRlxri6qzkwtvBv7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmHUuQw2dsss8B9V090Xs93XjUhlJRwpoUpNp7Pa_LXCmPq9NBXEVI5yEhEe6wpY1-1xlGnAfkELzRQXEHA3UxrHDPiPLSN3WGvrZPDNcCsEMraW2UNdIdJTR49-79EbbaFV0i1AKiv9MRIIrD77oj5o0aHYIhjlx9sMmm_ZgdypIJQf_0OEKhJZOX4REuhq34cHDj_1pKhO89Z4nQ5HJGhUk_ZSEmvEzIeoeFhYLXFRcy2lZpG8WIbiRH6QCUMoRJ8-PW5Wn32xwoZXgpquvRUkDSGdxbKB9PDAkuuoiSe5q0NkkvnPdg2lhL1vxwx83N3d76Hh7UPIwCJIXV_emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=m-j2z-fXGuXB9H-1K_AiUy1uosJBooPtOs13GeH40KzcWgbHKK59ZD3_hQGSWiGYvVmUSqpIDFAw1HkX7m7Yz94UARRrlQhqaeSrIxeoJvj3_6NuulUpWx3MCzwKRkHvIPUu-JMBTsFILnuJSeWTak36aObboqpH_uOdo1nt31wULMC-073mzfwx9NmgqNctc5x03997DQ8wIDsg2_IXHaGad9m0J0dE-sXfoMY73h8mdAfXsZ59b-NjZcuEYCBQvssbYTBdrF1c3MJlszjvQMOe8DxLWGWuj3xyiKLhgJcHG38GczAMIz3K4GEI_7U6IAco_l3VNWAOY-uRxKpARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=m-j2z-fXGuXB9H-1K_AiUy1uosJBooPtOs13GeH40KzcWgbHKK59ZD3_hQGSWiGYvVmUSqpIDFAw1HkX7m7Yz94UARRrlQhqaeSrIxeoJvj3_6NuulUpWx3MCzwKRkHvIPUu-JMBTsFILnuJSeWTak36aObboqpH_uOdo1nt31wULMC-073mzfwx9NmgqNctc5x03997DQ8wIDsg2_IXHaGad9m0J0dE-sXfoMY73h8mdAfXsZ59b-NjZcuEYCBQvssbYTBdrF1c3MJlszjvQMOe8DxLWGWuj3xyiKLhgJcHG38GczAMIz3K4GEI_7U6IAco_l3VNWAOY-uRxKpARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=ucJ5ym8FEM_O6XR3EOxsWqlrYI-ytpO07Wbej367BFLUUKV5PRBYkEveWA4MJ1oh4BYfOJyM2_UDAiN0FwlZpDDOKF5vkYbuTjWxZe2o1UUe3RUsAa4QMrhA3juD7SYaC9w3KT459K7wBgPau-oFA7xW_MPPNnKd1CHbRMKg_9U8WmRBOC303GQKEULBk6dVVjzsKsZQrs9_eOfDzNf-wKiAK71IlhbsArPitjXMgF7ZTtS-8-kKDpgS7QEGcqrMC3mhIPoMGC6nkVuy_ObYgip6r4Yj18SavpvGIoSuz6yET03Ya4tTFnZeOuv6c75T_2q4MxFY-Q1lYq8yjMLmWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=ucJ5ym8FEM_O6XR3EOxsWqlrYI-ytpO07Wbej367BFLUUKV5PRBYkEveWA4MJ1oh4BYfOJyM2_UDAiN0FwlZpDDOKF5vkYbuTjWxZe2o1UUe3RUsAa4QMrhA3juD7SYaC9w3KT459K7wBgPau-oFA7xW_MPPNnKd1CHbRMKg_9U8WmRBOC303GQKEULBk6dVVjzsKsZQrs9_eOfDzNf-wKiAK71IlhbsArPitjXMgF7ZTtS-8-kKDpgS7QEGcqrMC3mhIPoMGC6nkVuy_ObYgip6r4Yj18SavpvGIoSuz6yET03Ya4tTFnZeOuv6c75T_2q4MxFY-Q1lYq8yjMLmWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnXp63OZ9F9nxN-T7cyrwPmxL6tqW_YdjwqcRZaGsE2O5_HG89_RRFVQXqK6CwJpDAKhN8a6HU1l3zGVSUYQ1XJxAV95aGaS915iCahZ09l2UOafLZA1xbzz8Q6IBbp1auknc15zCN71-rsOYhNYS17fAAWCpyEM_QdCax9BIxWCIQ7N5YDxLPxWzkStV4IlsIBDEqCqNYWD5bTu-89PKdP2KcMEVXaYJLz185MG1qu5Y-TdHcH42EOp-nUy22gDtpcFpEtE5oF-_Wb5LQl8Y7e4kdWWWBExW0ZEHUAyeZetwXkf8M65ATETKA5W4thN3V14Nlrl6EDIZ8QJQfyofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=uiMcrxo4x_lI5zLiwbvrgrLgwfw20AR3k6J6YHqMVZYk9OvZNZv83ljqwvTGI55wapw8mNfLMTih-0GrGwdZF6zPK1F2_52Z71lLqiSw_mfHkDhuVwZgji0bVY_goVJjfDPt0LaZs-EYT4OZidLzJUHB6ZZWb7qA1XhQLBj1Y-imP7Dj7RmkwcXXvPq7JsZVuKP4xPtCnHgIIeA722uMI1jq5c1SQ_hs7UhEQ_s2ofdpmDc3lzAdUpfgIjdCBRGp4-qeLdq8NRdE7PE5Ge1OwXryQSSWWaZjM1qC4DPxbjr_kw2YesZhv14RbLLFvSWeTubWso078ym1wC08U8mYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=uiMcrxo4x_lI5zLiwbvrgrLgwfw20AR3k6J6YHqMVZYk9OvZNZv83ljqwvTGI55wapw8mNfLMTih-0GrGwdZF6zPK1F2_52Z71lLqiSw_mfHkDhuVwZgji0bVY_goVJjfDPt0LaZs-EYT4OZidLzJUHB6ZZWb7qA1XhQLBj1Y-imP7Dj7RmkwcXXvPq7JsZVuKP4xPtCnHgIIeA722uMI1jq5c1SQ_hs7UhEQ_s2ofdpmDc3lzAdUpfgIjdCBRGp4-qeLdq8NRdE7PE5Ge1OwXryQSSWWaZjM1qC4DPxbjr_kw2YesZhv14RbLLFvSWeTubWso078ym1wC08U8mYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNjJZKU9Q21gZr8V2xpd-bNCr3uce6Fn0cvEU9ADM8_z2YhiujKyN3b-tFN4lS0AnVJosMa2QVeemgEHVTk2Su0RISEaS-4eQdEoVFLPB5WB5R1QiuyC1uQjHgw0H5YQJKAguX7nCaCNLe5gpDbCfKaGeCZ8p-n12Ncr4bsZR1rb--Zdan4_NlAM6Gv3ZWaqsK-fCF399_FzFzqYYIxXmpD_ucCfgb9uyg0pl4TT5k-BomSxXIxVEtBS9GFm7GQvC3FGel9x6EFezcG8X0I2iBTMAkZ-v_i64peG6uUXFh3Fg4_z_IPi_5z6FLTRc86eb9RfGp4DczD_FgZ2sEc93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=CGBj6zYW4EzeOaM-7FDkAiU-YGSLPPAaLhe3yvya7PXzSIZa1yin5GHbXK9fOuSVRx9QZplfOnicPa0m0XN0kfLm8PCBwsHc7J8ZOqUuLZtYCsNg4DrOAO5vfFkHXiV-RRLAdas7xeAyytEebkFonywRtuDqxTGyajxerHQas0484spI_Wb8t6Oz7frsGwBVFuexIA1V0--8qlYtUMvxhugSSouaeIAOir1-s025Tue5OM1AbiBdgV-diFQBe7upz990rp85WWL_51KG_nrgKvUoNUH40n83UYKd6D9UwXr5hKbLsLGNIEEgdDVUKVIKGe2eGtVhWOtkZ1EWemnKSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=CGBj6zYW4EzeOaM-7FDkAiU-YGSLPPAaLhe3yvya7PXzSIZa1yin5GHbXK9fOuSVRx9QZplfOnicPa0m0XN0kfLm8PCBwsHc7J8ZOqUuLZtYCsNg4DrOAO5vfFkHXiV-RRLAdas7xeAyytEebkFonywRtuDqxTGyajxerHQas0484spI_Wb8t6Oz7frsGwBVFuexIA1V0--8qlYtUMvxhugSSouaeIAOir1-s025Tue5OM1AbiBdgV-diFQBe7upz990rp85WWL_51KG_nrgKvUoNUH40n83UYKd6D9UwXr5hKbLsLGNIEEgdDVUKVIKGe2eGtVhWOtkZ1EWemnKSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFgTzDQFj4NjlacV5pgICgS3cLx8dELgv4hfKYzNmxIvjPRkGZL3vjXwDyvcqWQ07T3FchMIVhFs0rsrfnA-KKVeX7dTAhcGYKWVK4Eafmc_46eeOkhz2SQ7ySmdf0BFOPz8NkhRTJcPEY7zZY9dXOp8jXHXVmTbVbppr3dajfP5CPNMNZ68PDUhgwRf48Qnj0j8gxqopvP2SADcDXW4pxkY8pTZWGV4yl2klqk2p8EWRvUj8yqa9iSabpE5RJSoopRd7wLXXVxn2fB3U5sS-FnKsX2yTPbpcDFMkENnot2U4owStwbK0iVHuy_MZCPnebFqBjj0jn0XjIgPSRhIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=s8cz5N_GDm5_b_DF1GXV0gfDfyvfx4lvsL14-7rg4-uoAGmlrZF7Q4ncUzRq49rQ6HdMLK4XSt2LtMsUew8AmMVaIPIkyyImbTP-YujAA6pdauycP8iQRsLr5two6yZunqDoPwMviB2QVzeTE_hDOhuezX9W_RUImuNfULiLLc0qb7eMC8wxPTK8fVamRyXDaq2RZbA3px_H1N46Ne1scrPwzhZ7RUif0y5_j6Z_MSCJy_QEqfT6qTeTNGQ_RU1RKbigoMenlbF3XkEN2oFjLLAY-OvzNENW2llXfo6Jlazg8aHHtdxMCpUv1_rSTTE7xdq348bFHnGtlcrciQZ1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=s8cz5N_GDm5_b_DF1GXV0gfDfyvfx4lvsL14-7rg4-uoAGmlrZF7Q4ncUzRq49rQ6HdMLK4XSt2LtMsUew8AmMVaIPIkyyImbTP-YujAA6pdauycP8iQRsLr5two6yZunqDoPwMviB2QVzeTE_hDOhuezX9W_RUImuNfULiLLc0qb7eMC8wxPTK8fVamRyXDaq2RZbA3px_H1N46Ne1scrPwzhZ7RUif0y5_j6Z_MSCJy_QEqfT6qTeTNGQ_RU1RKbigoMenlbF3XkEN2oFjLLAY-OvzNENW2llXfo6Jlazg8aHHtdxMCpUv1_rSTTE7xdq348bFHnGtlcrciQZ1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=vNYxpT-iXuWDAQGbvImJJxXpurRMIP72UpYh-vixvVKWkQGKm2ZAlPv5__gnuAWDM49rVE0P46EqqMvMtiIr16UDBv6cGYO5pfrl1lSzYpbcLyGh7NWc40otTAZNcTTfdlvz743IGluza-Ildzx2BBh4ZVwIzEpvxIJhWRae9ZcgVz_BZ1g9KwCd1YV-BxMZ58wTJoatntI3RbScwgr7QWJ-pnZEeyZuXRVfZxLhCQB-VC_dbqFNJhUys-sj8D480alq8cs7btPnTDYFg0D6JMNlV6bfaU8N3hT0yp-ezJg3G1zRztzgYa_4BiYZXjx9v4Vcq1gfzNh8CNl5p6X8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=vNYxpT-iXuWDAQGbvImJJxXpurRMIP72UpYh-vixvVKWkQGKm2ZAlPv5__gnuAWDM49rVE0P46EqqMvMtiIr16UDBv6cGYO5pfrl1lSzYpbcLyGh7NWc40otTAZNcTTfdlvz743IGluza-Ildzx2BBh4ZVwIzEpvxIJhWRae9ZcgVz_BZ1g9KwCd1YV-BxMZ58wTJoatntI3RbScwgr7QWJ-pnZEeyZuXRVfZxLhCQB-VC_dbqFNJhUys-sj8D480alq8cs7btPnTDYFg0D6JMNlV6bfaU8N3hT0yp-ezJg3G1zRztzgYa_4BiYZXjx9v4Vcq1gfzNh8CNl5p6X8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE3zVKl5Wasi646G23PWGYHIfHg3dnz9VQ7WkxdH27nubz9kGOqvujkI6j_QQi1M6Z70CvGJczDu9mNRSjRunXJ-FbY3FLiwj14ihVeTqEJtVWLT6cNUgaDvxfhA75MrG6raK7gSHMLW_aRpe7iy6tuUKl8wqTtqglnb_d7s0az5idpUDpemEgGVtJVpgPLNXiCDQTCiGQDit3Z-frKUoZ8nsg9Got8excSgv-hYbpA8Gppld4RmdOeuSyDO7fTKGfJmYzP1VXqOZwZWncOSFrBXMGm0AVR2g3nSk9Vcxp0S0FpbmFLL5ordPKFeQVD7_APf71ocCNcwlTGRDVFPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4ct3w2zooIHnPjWoyr0m-C1rQf4Ffady_jtMCXKVgD0s2jiUE-mOiC0L_DaPjOYw9F9Bg5tAFGnDH87_Fu-hO-Ez4bOdHTx8wXyAn98KoxyE6Ijaoir5dBH2dBxR4AW-F3sjViCbxIpIa-YB2HcnxkyW4cOdhV0exHax6Ro8NJivHdJ01X1Mi0wInu4GOQiQl3p5N6J2buf4uxhxmgNwW11ivwJ75-EtDUwQRUi-9TlmBuKP_dp6URn1h5bKQZAnMpNNUKKDt3VivqwIJ9nqKBWDBS94eWy6A24jA5hsFtHpxN4u3wdNhVr27aCdsHtVyUusRWC6d8tcqmlMliUhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=V8wTNxnAIYGAuwGawry6ahp-uN8m9YmNG2jBqYB7KK9fH7o9A7e31Y6oW7vvsKTSLAx5BodzpkEd05UDR9FtF7NoELIicxPTEUsvp0SvNC_yoDFarqrR0FzROJRlYMH7_tr2iLS_Ink05qyqBP73MGH7XKb7bY0dc3_H86THIhK35DK8-E5m4I82PU6XBnfVklYSsFZTMql9-jfpFW36P7IwRMhKiXFUGDVRVQXEa0mhp2lpr8pVl7HOr2o4d8D6Fhh5KnuBWKZ9tzcaAwnR_83FxSEUBO3s6vY9B_4ot8s8zuO0YngciTZoFtm3pVx65ccLlGSxpXWMzYLmWJA1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=V8wTNxnAIYGAuwGawry6ahp-uN8m9YmNG2jBqYB7KK9fH7o9A7e31Y6oW7vvsKTSLAx5BodzpkEd05UDR9FtF7NoELIicxPTEUsvp0SvNC_yoDFarqrR0FzROJRlYMH7_tr2iLS_Ink05qyqBP73MGH7XKb7bY0dc3_H86THIhK35DK8-E5m4I82PU6XBnfVklYSsFZTMql9-jfpFW36P7IwRMhKiXFUGDVRVQXEa0mhp2lpr8pVl7HOr2o4d8D6Fhh5KnuBWKZ9tzcaAwnR_83FxSEUBO3s6vY9B_4ot8s8zuO0YngciTZoFtm3pVx65ccLlGSxpXWMzYLmWJA1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=WM-szLSudbz4jDj6vqeL9kGbBtA3W1g5Y76KkNxom1mSJdeXmPXv1EnKwjfRwXwQw24N2B6naGcvOTYHCLOtD2x7cCO6eWc702uXlE5fW_yCjtyQ9IUJkcV2Knjp5AFOfLa8ZBSNf6_7aYDowYSUh9_r1sQ23Y7gtCBVYblPVsNvbyP9-DJjxl9i3nS_wkCLVw2weS1g1rXar1uN_iHcNwyX-Ju-eWBtN4kUEibTwHZGXRT1HUbmbXQsv-v-kye9aH1Da0XtPA_bAzpkwSd7Ds9952Ja5CKwJ1ao71Viw7KnsUGs2ChLR4s8VD6ni2P35zG6_lWeSrXswsHOeeQ89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=WM-szLSudbz4jDj6vqeL9kGbBtA3W1g5Y76KkNxom1mSJdeXmPXv1EnKwjfRwXwQw24N2B6naGcvOTYHCLOtD2x7cCO6eWc702uXlE5fW_yCjtyQ9IUJkcV2Knjp5AFOfLa8ZBSNf6_7aYDowYSUh9_r1sQ23Y7gtCBVYblPVsNvbyP9-DJjxl9i3nS_wkCLVw2weS1g1rXar1uN_iHcNwyX-Ju-eWBtN4kUEibTwHZGXRT1HUbmbXQsv-v-kye9aH1Da0XtPA_bAzpkwSd7Ds9952Ja5CKwJ1ao71Viw7KnsUGs2ChLR4s8VD6ni2P35zG6_lWeSrXswsHOeeQ89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
