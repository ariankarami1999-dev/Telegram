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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 577K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 16:44:49</div>
<hr>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O73KE9PPDl3Xx3AKvf1oISzfhWL8H-yVAcM_QdH1UDE1WdZ1mPfWl0OGfs6rtoUpBlkIdKq1CrDFzVMdgzArZJoOnPo1BBOU-BC4E77Wvw6FFy02ur58HrREEMkyT-2oF0iN8yLhM1He51xMO0xhbdcS-QCAY97LF_5FBCHMJDyrtKeSG-HgIvDasfO1XqH_UNy_bVV4Oq-e3d-jyp5t6Js6BD3K6gMvsMgb2Pw7VsNhQvIBxUrgDjK-o0qmT9E3VUb25A4Q9KsSW6fGrsNeBrQmYnyN-YjwF9nHWwJzLuM22m4n-XcTnGAaa6y2X0DN3uYVDjcAltJfVLJtP8vymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDLPVC98ZNwTtNXzH75lgVpMy5yX0TwIOaaci856vj5RxxIDVnYiICmsPW_s_NAKOW79YSVCKMHXywYljyKlrzuQCPtUQ96yzVXymwue6zFAIRRHZ-er7VBZU4u1z3gtCVp4sj6IsdJVFtzFdYwJplmc0dQ2kfPDctPqtcb9I6GdK99FYauJp_tQf9vPQ1Vr_8MmsBBmbsyoJBnDBrSvul2dN7PQQk13OOPECmAk1okhB1emFzIgCBydrn-sWTZswolXXKn9lBSHk2cXxOODsUzCmrRBKmrQb7f83HRpHaWtSI9YiY3TVBto3fSXr5kb2D2LlJ-M0XT4-_5JNVwURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCaudgXtynWKcDVwQO_cIO5I1hjYsD484YXmKZDRpg4OSOARDa306XLo1eW2DHEtiI6TNGfp7ojUbCRDlp788aFNt0OMK-AkLW4ylAkBNraUmPaAcNiF8zPa5qJd2MRFc5QqZwUi-aK2JjuRZUBNDupPVFeloQWskIq_UZMlnVQm4_5nT2O1-3M0xhqxKwdsMZk_Hom8ddtNewPJknLE1ri9tfpddb3jlDEhGWxZ-aRz_Q18L18nWKRzJhpu9PA3_UfkxCEJhTFD7BzXMJDbJIdxEeUrfKwatvqUr7W56w4RdQP66aHH1EmhVNHSzo18Hnti1T9PEJ5CxZ8v-vYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZRunwYAgj53xfMLjTo5zJCfZQHRPW1LTmI4vGqU1diYYx1umkKyFCXGQcqKLFfmFiAwpS7dDrFxuJuEEHIJvIrk7c7LwRZnjSfSuFMbeICo9sMB1DTXsPT3Gu0zb7aizg0YLeCVl1pGK7VHteO58-g0Vfz_VUNdwNoT-ZEff8bUeoha7l9QqOcjITQPNQJGZ0ecE-3H7MruodE1sayjo1LPF1BW-e1grfudt1QnyP6G8uxcyNpVWTFSgR0iUou2G3CoXQt_u7yX0mCHulc2493RdMTDh0_YiAe6eTgiTi7dLv-V6p0xEg3I2pIPlYyrQINbQI7gh39_hW_sV9I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMR_GBF57Tm2NAL5eIXx-GpiK37_hwI02DPel3SWCi5bigbduPcVFYEpnsPAHf8MY7qxaFpxeYJoFWHze3URBbiOlTqROVvMnqj6gbH22EZIYTzWHuBvDbXws7DTE6Dk7Isr5fUyzlycKIU3nq_9N5U5Wjzbu8GbNcYlKeHiNdec-6NTqTXhMu0_TS7sXP-q7ePQcoeWUVdtdTjjVorXF-IHKntkbd-tsP8x_IB1RZQAwEA16Sb8U0WMVWft3Ara2jhiHIoBN1B8Mo7VHzDRx18CVBRwhzp1Eyn46QgAlqYUArijYFgwVpFXy7ghI9jK0X2YVCyO_AKAYveDdlLTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTgbXyh4McUZxwdUtiV1erqQTVGDgM8BK07xBDhJ_kZWmwKhia5mt3lfMHhItXU7c1jcz-SICBtI3kUHv-FTQ-7t_nA5GmCVi8JaBMF0fuwnk20YlLlUdOnBH85Q-d6g1lR7itftdZX0SNqo3ITj239g3ywca8y5xoZSdcR3qu1YlwyIhvg-mMIMDd-bEFrJADNOBV-oBKLJwTjlbG2VwCLbSKEl-xRCsfNAtUy7x0FXoBvNNu1GMoccP1J0mflt1HjRb9PF-lGhiOjY_2iZjLTaWq_bZB_bj8yAtXf6Cau6DJDG3drY_D5CX3mlxtDMy7sGU0eG1mNZkWo9jG4aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUYfEkWxnUQHGMD04LFPT8jOyn6n5Hk7solEEoaHOE_4PzpNMOKQ6fakciqHmvNTGSOrgLAgLyi9HFPEnDYMK-3PpgKle4OlvTG30FU0XwTE8TCGHqip4FMI_BYxdj_189rk8TToWskJQAR9QAyWC_F5OHUgDLe4c4hxWxqs88XP2maWjejoebE4xRtwMKXXZJPGS-nB7_G_r3HAgzmRBHO3tt4HdUJQQ59KbUR1BRd34AYz-Nvo04Wr6mz6LmAYfBvzsfXH7Js2JwV8ytJnWPo3cgFfGz1n6C_jBRL3wBtkyqTt5L0X-0YDA9yNobM-1D4m_RO0-JHh4EVd9yB4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrlnVviZUO5-hDgEniXVnLwSoeT2GiL7x9KhN9bnY5SXs1FaXYsk4smpqQmRIE1YfqAsEh5NdGEI_0RIOTytTqBUwdEgbLfRtg2_4U3vyXLVkA3jI8Fe7a0aXNrmOPU0JfAEHiQcFPUgxVlE39rGFL11wGiLyk5Zo45UeedAHfPHRshD3qq-2wLrDAWi-zm-6CHPeci9emvQS0HSF-qqRRfQqooehx88G_OTS3sVUonl2u_XouO4GWHGtVOZkre_lLPfkaLYiXhllR1UqwpHUQfuIaNOiRrLtQyxvJM7OCimLqHHR-M1q8jQWeT5D-V4PCFdSylGIozJYUi1dakERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUYEmSfCaVfShvj7MY4lzM3MNMlhNawqrHMYq852nAChqa5_AGT-LTin22OXYCA_lczTaruOcZzWIHnIjZpqSuHeRADS85BJJZJYMgNepBRv37GgmM0Cy_J53BcScznmA1yYyxy4WCDG46fJwIhNFwL190NFeEifLDEYwy6aUMr3Lu4pqJiMUa0dRreOQX4-k5F2TrvjZDRFe2i3mNyv2LJZHZ087_9vHVgjiUJ7r-cYwbJQIJhYIPuE2n77ZPj3lwYOX77Xmu1Jyi5O3-mBlvGWnN8ToLfn-YSqvbKwxU4bQsePlcNecyu4JFEAqW20dkgDTc5gGBWieJLMXLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzwrVS5N1D0zkmqsFYaCT1kCdo1-yDMPX9PBpYs2YllicPT4otye9aWm8yComBYLpvscvFhm9Ng3pgjfFVPK3CWTVoEPNdaGN9RrVtteWCZC7sRC_H1Zc4sogyiPBVIhMh_2HTdxKT-FUx8kB-TVqCIL9MPHQ7J-LJ2CeKOlJ8VK1bTzrhar1D5DiPOWqgMu0-m0NbhCYXcWYlu5-RP5xZYZRd0JfdSt2j_m1XYZqhJJXZCU7r--zx4IvTYNWN_jy1Oe6ADMtfQwruZy7w47kp7MYF5qezLXPzIM16hZLON69MuIuCkWUuMv6V9Dbb9W0QnWsWstiwKRqDVuwlUQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIudNl8W9BqEaVz9ho9w62MBe4hIDS4umtz3IvOJ7a9Cwe4d6DCCv5ffiiNPYubJm8l5LSib0cWgl8G-ZfVVweKf85IhrnpX1yw4B9OvwLA5JNQqBC5fhCOfdt4s3mu-HoHeRQva5gv2P3hmOmGd9jB21TQ-pmk6GudXA9NcfIbsnIafmHWAtGC3of6QCBVsI6-CxluT9GXQB9Lz7bTWXAR91-YCo2UZFtU8ho744SE1tgkrAg-kxxf7tuXQB2qreX1ErTvUCewqVDGlXOUZfHPsiUFFF6_2uE86DoGy866Kh4chaNOC3w5uquC_Po0qsM3AwEMciR-4D1jUnF74ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQ-b2P8x_sm_wp-etQcdMJuPH6o49YVvh2wcQpSTtu7PygTBm3YtZ5fGZNyxMXI23o1Z4nKqsZoyg7lPP33XXr6GuXQ3TJ6JgR-5rARrmxXy6J2AlvDy6o4yAGg_p0s_gT3yOTvk166MmfKtz5n2vWs7sVR9y6YPVBU9RAwJI9Nc4z0WXwUP8aVUv5Zwg7V3K_hNe2UxNRg7dyKVzNzAox_RWuYhLkWVKGMrjhzjyDINg5AdR3s5tAw3y_mJACtBB1WQ88FVEM5Ys2s1W3Twe6aLyjiHKuzKP2ILyBz7Ln6FNo-9BOhI1P_e2aJTu9xyoq_aHmnmKYcb3alQtUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnPZsOixQe1vgqMH1-dv2moHeQjDB1Sh1yIoKvf9Z05leal180sVW7D5FQWpJUHkcwfzTWBMnW7o7A2jCVIFtbCFI5yQ-DlwIcMl8wqndkMrnNoLytQQA8EKIqJ1w_wxUBvI7pcWXkjNqF8V2f4hicZAgS8ANkDXSP0MZgqYQq6PDdJgYzBvOkqpBBTrOfT7dzViaK78u466uLIxHfKg80HmPqctiM2bUSLnpIlTHnbo4kR2P5fCCYw0f7hQ_Yo_h4GoMzfIHPUiWc2Qhiz5LhcD64CKxb4eWSoAjrAwdbIenjvXS8klWnpXAjBJkDQgm3-gVznssnrv-AfvNV15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8YNcZOhsfs9aYlvmAzjEvhJX2xLrXmTkfGS35MvJQbetYu9DBFhWBbzVUaMtx6pEJHOoEZ0EHdi5j7ajbe7QTYoC5hhSIyKRv_iY2gUvaPsi_dRemOtPJ4Sg6yVEniMLvVWwcfhDaqNYkHdPon94wLfO-vUnYcvb1_uyJLAPp1JRXujc9duiWao3jVcSIqn9gsfZ3lGwcmVDUqs_kT3STy3hKlie3Fk2CWVlkcaWD5BK5O7_ygaKZCWB93A5quaLUoSBk6CSr6sCuvzsDYCh5q6LdoNhYiNEDv_vs-F2m0WTGHh-wyvn7E1TAy1_Yn-xzOSMcgayQLwywcuGoUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cWZ3aNvKTovdK5wlJEtcUFMnFti411znMhfubyNZ0rmv5KltvMUj7AZ2Pomn8ziYfO47amy664yeClYtRNZ7jVzEu-vPmZ3bhhsD5PcCS5IOSfkjSgA9N8We6nuJ-IuXg1N61bmEZOtdESyh869RQSdi3EIDc_HdYh0Wc6bB2GoKTjt-hihZZxzbvc-gHj3rcn84Kmr1rzcyrnpEEn-dLYXi1m_8WudHYq1qA0uvN-SOSNsbzYYLIbpMcWxFrOeMulfG6LoBhD46iC2KZgSbiZN24UqYvb323f5CFHR3_7cB346wZoCJEJXKqbbA7ECt4g2WAyJXrGBl1g667Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhu32fQUsqr3aaTbqNhoxlZTBfE1NEh4i23a5uec7YFls1k_rpaSGAhrOsDiMzwkOBUcGS9m-gDG34zKBUE9cFXWRGjqjlExwBH0ChnCtHZDrsq2ljbWWTJQ7Gy7FlzHv7wpG52gbBrbPZEX2bl7UQhKPMeEwO-YvTeIXISORO6nyy8gSW2FOwxBm_1yK5XKAWCCm8N6U8m841h1eTVN3VOlqf-Xvk00DAbStpO5iyaBbip6T5CaVg7LJQUWbjFnX2dP97LW5-34gdm_L0cBo_pNdnpewcj0iqa_l0UWAjc5ypu-lcckdDv64I5wFNFv2MlXuQju4euS5QqhUwrQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwn37v3DdiJDyOkrVEzE7DZE9vGhIUi4kHMUgOIHA11nTAf2VpuBzdvo5T0Mu4Wj2JZwUcl0W4UTSYWqGwhvMRmYhOtLOUUMg81NIXAQwh9BwOpJMxmtZRYAqnaz0NMxNw2v0fzCw_YG4Of83-xCPoGmula7_ZKT50YJxP2R2Qv04E_I54yEuY1FmQFaCvJRBuiB_g1m28Aq2KfnsLlYcOECiGC6YjWJwnh3SZy6AHmXP2Dm9qzmU_VJ94ABAnBRJVRaEv8QjVMEznUNokwq8iDdY3Q3zeAYoecKEDbarQi8o8O4WBPreoi5tWpsb5b8fwRfhgV1hjQb3sDw3nFtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe2lWaQ_JE_LuZKxw3SCFSg6-lNNG72W6Lxx7jF8jsGXA-JkxiLC_vegZaEsn0UfTbQ2AqxKO8VKs0tsy4S91lNcLEppagjEdCDx9gE-eOFVooAijNVDgPtG44u_KAI23ATDzLVAVJTBHVpXWr33h_Ezdrhn2PFRMMXt7vN-5p5VorbpTN7t4glVKKIEzXwOBJWRDzJWxxhjDoCev-Z2nr9IcwqouXCvL_NhQ73S0z_E2aLXWy0qKekuIsbuD3BW5Go8Uiisjn2Mc8a6XyIl_9ypJZozPdsiXWgB49qWtys3JenGlrTPrRBnhjYNrvXdL2uQWQMGA1v7vfFDVeHU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6BRmJzHYlamC7mTb4Jf2wjhavujf0jc6PXyQMvgH74ne2JqKQHCrH-cAcna8nH16BWdz8jPlsveLEKH69vSc6fdqlGGp_EoZMQtnbTwOOrY3myaetXOP5G8LErQ7PoBDfUIky9nfg1sBHOsDw8A4T9YQm1aYHfgSZYCnhRA3775ShiwEEt5_xB0fHQc3M1orK1mnxVgbEs0mQVgL1-EHw-fTjhm70UZX3YMsRuKL3yKHaCsZDZCfXNDdKnVoXGpSDEeDKse9LEfYvF51Pv1vDmV1pHANjHJUR9HjOpTgBndtVBoNyOlMZotmYZp33AO17Yzst6VxqAREamGInG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls3SXx8BBSPcU7ijYCAWZePjtV6vDbm7XKbCqRTXRwAZhDqhnkTWNqMdfpfSuxc0HcWTvajby__I09g81YghWpZcC2G47684je1Lrwxn2kvA4RDiOcbrXQCKuasqO2wMGUIGqqvt1yNmrXKqNhtYQi8t9p4ar5cEhNCXLOG34sND4YuwtljOspMGtXp5O44QulS47cjYsdHxnTGQBS45NNFjYyuFVbdaLc3MjtKsTfr1AgwRf8LjLwttAr1FP4uKFrJe9f36OVsLoyGLixU4H0_N1EdJj4jvVD9qvjBUUmpiPDbP8dC4HFweIpCj4pwJ-FeS0pAZgWYfEtTDhJXzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7k1QKQag2XjTp4ulLno-FuLd6V-b1uUbJNOBKpAsZSwZ1q3TH7rmV_MBnoMIZBgrOtUjJm5WkJ-yj3neK99PN6Z7kwXS_Cutt-Q7aRw797m3V-ijDGwnNFakrWqEpqzPMOKxUd9Sh6tCcCJ2c-NeyShNEQGMKvFuLOha35qJHn6BAJTxcz3TZP4xzMDo2ARC1tiPR7Biw8XPTrzQvkmgqoNjcFlQzpNOSnlsIwL70C7kBwoWW_Q8gONQ1wPz2Va9oIaQJeqBTkf6ZZePqIYMQN6kiLGQE8M1Bnbs8HqvHvOSXWFMlWcDQPOITTec7HbrMuW-eN3bYmTqTK6A4nQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBRE-0BRoIkjX-llOnkD-WeoHo9lC_nmCHPUi2kM6uSjU9UDkzrgcNR1vKurfokZun9y6wP583WP0qIwEk1UMapusjvn9XixJ8MGHpTQY9MsSa7kiv-ImspkyXvVo_st22-7UUdk53ycFikKV7CQBxCrkaJhRXW9PETvDok3Gb85yKcyP0mvz4LSbpk-is1mV4dItWpQDMUuQFpCD9uMR2T0kym-dTcTNGfh_4wLR8Eb5ViGUwCtIb4B-7ZmeZC9fvrWeQHcmfOSrYFoYGE3aLUL2NJ_sW7xTIE3mNAUI56dPQcTiz7moqgK1TyGlIK5WAXYGitA06sFHhdYRUw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWmCnxFxVeWAmBFeyAp16CmPxt6BWNWISdPBq3lxC2_sd0_L6ZiJqj5OaxpRQmSrUYAq5PxLUvwVw7i3tg6x1-g3vxlqHOMpGLQ9-FFMccYVa_dS9y-of_C0joALwQ8l8JV2fPhEY0hdafIaR280P9bs7ORwXnc7Iv8NJR-jWo0qeBuNmMQgeCNFPyN5wJ3c8sCxiSEXOWOo6ZRRxn9b6VgkeZofScK23zhREMh00f8J-_FXl0shVxJTmqG_L-qsO9v7mREKkG4qS5uR5FG0MFxIhBOY0fowhU9W16M4B_JsbiDYgb6bB2wENkx807gfoM7jyU5UwVr55nhJLmhRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTCBarOgn4W91dqEPOfYys3i8JxMlfpYGkh90QXabEvWBUtZfObV_rO7kOOrG7UqngHH9ni3ndZtvOsvyg1mrlw0tybfkfP6Pgq3twIg2jqMdWjaZrFfn41W2HBpkRoHdurt7CLMajeSbzJ2L6kRW4Snv_ntmWJNA6w1dnete8hdDaxZNrLW_hdT-LRV2orHgbr2OdGW7XD_nfbyol6TgizLj77vekniicUdNa_ukjO9SxB4_je05G8Ih0rb0_7Ql_DpwxbW16Lo-qT65R_VZKArvKwXXzVrNyxja6S13b8kZZDL_0gUI0KFAOHW2B4lfjgiu7xuf5gn9h2a0jcFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKJWF_HDlWx-SwpskxQPaK4CihyARFex0xfoypA4LDAN1PqTgN291KbU8-kFC8WPhg64beDiySPSVTRN_A2tCo2w2C7kmwyWYPYkJ7U6VFzUYC7FgliJhdSZm_fqQ_mxCc5lnZrpgVhcwOorH3-MgyvJAc4ziWMCn42beFUxoN0LiJqc3nZeUhPQSINmPYPB9giMmXO3DTg2JS-6fc0FtEsLmp9qvtvqn3FiAOQW9Sf2ZHknDsLG2f3qXUi12ygAZxPUhywlIJJcofqzhcQkXnz0Kn2U4hvzIhnWVHmHP40-PPP737DabBhmeDO9BORsaCVXGh86VhCsctf2G-qLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUQTs3OCDNVY7JVLiaZixyiwblPBCMmn16RaH9Ru9-yrKcO4QEWjdzanPsKPN7lTQYeU9ddUVCSuKB3tRAe3V4ki6aWnOjPrSPh-ySn3juWTrYG3HEuEA_1VkXKCdLH3i_I3qomiR-cMiwjqF2XRfkGOMoAck5zQW5Zv3kKWyNV3FnHWpignseCI1auYDk6FztfqSfGDVtiFKNA35QVotGpGlAMt1DmRYc0Ka0nzdil1oZWZsBDqqPIq7jv4jV8SEJTK-cNTNHazDI7AdG7ZO1gAtT7nBgkVTtiCD8eNaDw164elmIUvlAa1VKtz2tYiytCLfewSr4zgCyFJBcYZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wak5bPM91-8rfQw5ldSpeq3Wftt0B1nc8qtUgBJPt2dyU1oavnn9TJ4v061doy_U8vSAbix1RCngp1HJuYNf-Qtkr5x4uy3s3oLF-2tKqUilHnUD6RymgDoBSonKrzRFRrz7WjAzPOpMzQ5f1c0rnqDYSleZ0aAyV-zjQXlDCsTX9WrBqfRAAJ20-p1hc1eKCiGq0HPSy3j6Cx8JYskjMFeVZxB2FHnROm3pfTz6zf7pn4-kpsiuA-zekqdiGYAEkFk_lpTbc4t30ldk8-lgsvh1veMK24ZfquW7QznGMx4Ma4NzpbB2s1SRnwQfthXXjN1SJRUJUQUOR61bHyj6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFm03LkRV7EqzhH2PseiaC0vrDPnelKyGHV6QJ-TKld3QrclgHDAUj6jDrpBQUH10lHf8vP_0N2o_nyHRq7WGedf4ZXA6mzXTO2E91llgp1Lh2Nrr0L1bf6Jg204l0A96s9qRjPCY3WFS8611C4sfOKf5Q_8sqny2-Uz--TgXXMD0jjQBJjiOKebm8eNYLOEdnb6VfeH24nVYyYC9f2d-dxtvbtNGIW-to_0b9-kPX2B8SgwOd2UeIbotiL1fq1-N4a5eVDuuCs_pMMLPgJjcqZxOFjyhEQkki9sraxPCGyZAb20LgceeQ0Gl1Ka0a6wZvdgQwfBLhwB9GZT1BFopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UguR8996BNljfjawu3cCCaBKLRKZjRWalOFoClduF1c3Dxnx6I3nmY7KlRLjNltTlQcKZl33hkasbWi5AddSZh2cw94XfU4nN3afIDTVNtV-0BlQ0I_tSe2l-6afEWU9LAR1CG8rMGg2hS-WJeitIxiNgo9o6nXDGA9y__WZW5VW0fIYprL3y1YSpBnZt-n3mHFqsWr2D-kX2XpiI-CH9fIe2omYwRNZNnNB6R63TiQ2kJgHq7U2BfWtHxslOw_MI6hQcwF0n9dY_Dne0wZyENidPge4CNetJ7p1PvqIZoPf2qu1o9rmRa6emj1UoF6UQD5LiEhSU-hEf2AFZGco6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu7hwE8JVWrDz_qhRl7x7h8_yNiKX9ersxbs3BHzpKXBbWH_2e-MDGZFLz2o7cYkdjMaWyXKAKM6GFORuxu3kReedFpUMXu4IR_147JdPIux_ofI1-43qpguNeLcNvEIJrUQwk7_0fInE1H-JCsGMM88dvTzUfSD6Hb5cyFxEJw_D-jwE9mFwsd59-uJ-Od5kKFkbUnP2161W1KiCmEVchL6OF9ogfy8Cn2Il_5et_vZARXB49S7VpmyGFyvZeiExnO2I29wCJsYHxi46xS_GGgtOpw2F4Y4804YoFyQQ9fRKZMsSGYFvb-7zXG7RCISR-8M1kac5TNaSILRaIMP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbrAnElVO0YaqY2xM7q9LnwGdgXAHzdQLAAQMv-1Bm9HctQg0xgIRHOT9eefgC3VoZSN51r_CdlMsJV_wdTQoc4du3FIkQzyVNkiU60x-87eO6WEBm8XOb3goaIjLqDGqTsIAZWz_l562dz78H6dZhXWtOrAN2oUsnj0e9_8nwlBUrrtjbVxbz48_7BHprRjtG_6J_wF0mZ3OiCPmxqXgsUBxGaNEEQaQa7iNbdx3ZrykvIYWsULKDwribwgisXnyN4tL-7qxn3GysigCDs8LxbYcyPc96YF4xfFSnYAlBm24nnlrZETsT8--5lcUbgH4CPOrAAjHrL3-wbG1a_Z2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv367QyH1t3Gu8PLL-4isoLHNhR32dyw9E6oFsWZMdL_6Brp4Nx0jyslanoEihsfwvANYHAT6q5UuJ3k7pLc6OpZ9IZLerpLNEsK-kzjhaalSKzutrenSkyAWPblquQ5KZPw29Oqk7b0BiHeze_R7Vr_AHyfHsiljyYckoZURtCO9wEJ1pYmlh9iG3UN91_ia8uJ2RRR7X0j7KYb2UISFc03LPJ-C2Eyt1wMojSCutoN8H9m604vyEI1Rt4wOa0kuyL24ChNLITNLTsSBdaM42YanahRaGPikvUL3iVBHXf9yBIhzkoMABmR5DtubCJnLpkR3DpsD7FcaIOhQsenBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j16pIyDaDpFOjO8luSF_s4bY4yyJPDrNrdchZbSyxF91MchYnXfcyrmmaoxpHfrV-LgJ0qQOHqPLMaBnwfkOmABR-3TQcXqsJxbey19bsCAZHoOly6YkOkuVyXdpCOgRWWhDiEAnot3XaoVNE_wPieYkgTQx7Q36DDyAohqdErIRDnpe0bPIqF1r11_luGBFAwCU0WQnB-memdEu74_z3127V5GPNnCu7Y46-q7RIw5Z77mETWNSAd3Unsv9Z_Utkj5Jd4BDgOcAzZYQWJ3Ph9jeR1iQZ3luXg4F7SzTsyO2nG_GxMvD4psFgsfCJPAMOO9Qu4RV8jmm9ctxqMCeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVn9gyna99ZvUFaRhOeZY6WrZGcvglzuPQr3zcHrL1IBMcEzsHEGv3ChZOlcY9v0hAH23valnV_0tZUzitOYWvvz2ZXWSkIP0umqZ_VYEA1LvAx_BtkZDevtBhfT5Vr_kcLJImixgS3WpfFoaymAg1GFjsjpJG-03dGCnlJYHtrWUuFCqj-1tv40pU4Cu_JcpINSDKAgQgNCtcgCdPDWX_mQ4MqCOI3Q5OSyeNVoZ1U4sPuPGOwIi0YI69HOkV2DAZi2dnqGEnliXULTruJ5drV2LCUvSXrt5wwAtLGhccgClaiGh04djif0u0Rb4a4xnZmNfExEFSZqcJd5m_7HRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSxjuqnHFhIfj93MldQ_mjbPS8CxopK4C_Qnx5jUremJBQoE0JocuPRjaEoQlvzIXF3hFS1r7dipXAn5yoyKp92cQj1r48amVMf_zpUORFM95-m7lThuRYmn-hE3VRZhN9P0j1mPsTngRuqjInhFQAsAQIUf4oaJ1TEdbKGWNSEAapjr4jDJQMq6kAEVg9AGSpgtaWw92wvJk7rquZ7QDv-fj00JK4S7NbqIU2n6MZHftrmLhlF2w0_3IsQLVuuN91sYYDmIs6uV3_f2wLTZuw1I7-mTQaeY8thctP84D38myG4JuqFH9GxiZZsPlShQQfonMFod7imgUCL-PLZPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWpVgN0CCP9aJC6keXFr7azq4o6Zm_4ByZz-Jx4rdE6D9abap2teihfk5B01sRX6itB_ovmmA0Pvb-ll9ODDNYv0f1dnIPCwFlOtwyIY4S0m95IUQHu1YlgAR-LYUifjqXoXgaX_3NQZDQayx3Htmip14Zx6i2oTIaaDpFUgSIpbs_2hXdzzJcHAiEd5qSdpeL919wVAEXbu-Z78tWyN9-xTW4XklcccGt6Z_EmMlLsgwQwoJuKebYk91JU3QpO6lx2IHGAtsr41D-PeuJRl3Kom4hCNkhlIt5XFQ_zH9dZgO2iw7a2qvh2czjBNbsMqlf5E6StPuJu7S9K48hfzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwCMTS5LPiIEpHTSwl-x4LfEAza1_b-st6tML9nCxcyNzREbMDmpia8-QYXI6kO5_Z5xRdyrsQDtPeJfXBa1MLfEQOGQcUDoeSbJVsMy0NAxETVt7W_57csbULL1V1990sitx5N9OKgZ-OlzIIWpY06oI_ntFG9wxzIlAtnb_PavXk7HhX7_TXfCopu6XYrk8t011xfgzFe74cRUuuicMlPRwj-QFEIicAAnhVKPGVB05TbUz7eHyvR5kZDMH2s8M3oFotUEWdInLZvFORH8J7J1E8wEXrCAh54aRLUB0OqWxooCfwl022iTAqHfDVrH2joEvv1Y1DnajiuujYJCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=nRZrPqT_r4NSmNG_XFZDuAtL0d_PZOQBqnOV5s6OO-Zh7r7JX7_OEXk6zgumYVYbgYfXB3o_l69FEcl8837JTSJAv-DK2E5gmKFOEmoKOkFLmAJHrRSoAAYuV2Ix5Sf99X-vOdWqfGHBpgBaFCxUbVLs8kEI1MobMDz2_RIwCVgTvskWp1CsiYWRThq39w5qXkhNNpF1sKQMrUckc-khO_UfPfkrhCPEMfX3rCfdC7J2_zQmbAKlvGsah6My1wD9Lf89zF4o-lBue5FQrrOwwR6LDV3osKnq1b1ukGOxfc8SwXb6qsP7dVKWb9BU6dcuY5637Ppqh-AkoSe_zi7ZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=nRZrPqT_r4NSmNG_XFZDuAtL0d_PZOQBqnOV5s6OO-Zh7r7JX7_OEXk6zgumYVYbgYfXB3o_l69FEcl8837JTSJAv-DK2E5gmKFOEmoKOkFLmAJHrRSoAAYuV2Ix5Sf99X-vOdWqfGHBpgBaFCxUbVLs8kEI1MobMDz2_RIwCVgTvskWp1CsiYWRThq39w5qXkhNNpF1sKQMrUckc-khO_UfPfkrhCPEMfX3rCfdC7J2_zQmbAKlvGsah6My1wD9Lf89zF4o-lBue5FQrrOwwR6LDV3osKnq1b1ukGOxfc8SwXb6qsP7dVKWb9BU6dcuY5637Ppqh-AkoSe_zi7ZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPntm9GI2BUJXOjwexLDtoA5sYJoAw8svulpQ75MROXDNT6MvIijCtvSv50Bt_vcrC98guxIMbZvaS7ccJvrySeMddg1QiHZ-eaMClFBGyI1zD8tYyGwNhFI6XhqGRLuzP_oD7E2h1xgi9zlhnexs26rwFyNmdbxo1xGH19Mf3pN3jwLzWARnpZY4OuFBdJyEJAMcBk9L0K4D3XiZKDXjfiCd8AXHkoqZMV1CIRCYTDqtYp28wwaOxcjHDWSijZchG_c_jpZWikgSSB8KSi0Nzog0pAkGcJS02f0EnHzlj-py5259L2cEFMllVhRbUMhEc6gPe2SDTWTYt2pDkGzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM-mgzWRKFyrpjNudWVSPFHahJWhfCj-owrkm5tgciIjdzlIm-IPVKtIPbUJo6-f-8P6OCNKVyXmLneYGyr_cHMbwSmJT2qxstT6lsEdpiOs78jaOGkAk7gB5cKYFpPdwx-qDJ4k_5QuufjGy5zgkusObPV9ZYU_Cz2sVeG2WDLQUumif0Gy3aaQn6v7CA12y30eqVUhpJ5Z_UIRq0hVaVFGlKA6A-hLb5Otz2OL0pvJCK5iQEoa9IMxl8nx25R78k1vNZgjAygjPvWlA8kJSaAdV2gc5ZoxEtJziRvdvMfAaZJUnN4hQM3E04tkWQ9i_b1pVmbtwPIF_8QmYNV5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkVR6zqSMFqI7jcR3cgYg-FvCv9X8sUuYniAXb29JgrN1eyK9ruRK7xOIxzQxDAcivTRN8aLXRfnJLiX3JcelqCYhv-rysYi6HBVjJvsuzQ7K5R4q0urMa1CA-fdlnWJLTe6ylUYi79Tkf7q8AsROrvHSK5JgnkiyaCWDMdY9uBVmMqjBQl5W3WCbGDpt5dd2b59BRoaqWSBiYWftjeRCQIR6MZNNvskslvMOu5XLP0xtZfAJLtd2BqwrKjAET2hu_002I8S53qmMeiHybNyeKcKbOMvIrnxYescXkRHGFKK0zLTp96CddpjcbKMxUGVSjtCk_tdi8ygC9hNM1cffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DttRH5URHarCUe9nSoFFLVzzfk2QzGEP0LRXjR-aV9mGK-BmEQNGFsQB41zioLjas_RX0IYAoS5x-rbPu7Pq8nc8FCJM9aOUCt_01CUCFFV3HxyOH3bEaGE9A1JoMEYB87Ic0UkhrvufMORQP2lZWcBB7hOwHMET4rcXIwk3Lh4oVVZw0q3bP_eEzArahGiw3xeH9r7h8gJKsFR0Y0eWbVZAraJkoksovyoaijMKKPu8bSfMpFzNEOsKi5c0MTLfWvbP4JbFtjyeQw1GNN7m4gI6yFqKWszG2bKCnblrGBzmXuoqdkM5NIU5JlqTyqmmtS4QIewQfKXZN5zdNm8GpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=BMhES4KXzp9zehNdPYFuqkioSFTWCoKE4-BcIhuU7CvsLuuuzCgsmORYVm7t0dir1ZvsHXpVi6wRiaDzQ-uerHtKpsC6wNNHWclLDT7OR1RbGQObuAqzyOVwGZIHYkEF1nTryw_VsTcllqtqnILheG017CHBrzMSZzIGxhe0TCG4FLqrVwu_m3shD8NwmOSWkn0dklvCsGIJx5KR_FB4-fv8sWV9iNapj64qtqMtwfYmUXLyqpjGFQo_Smg101sIw8AKsQjo0z9XyXZG3p0X4EDL9k3hRSAlqFfBLjeqohSC3ft4jIl5dAnfeYgVM3DuOWArz7CeRSXomN3WfDXFOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=BMhES4KXzp9zehNdPYFuqkioSFTWCoKE4-BcIhuU7CvsLuuuzCgsmORYVm7t0dir1ZvsHXpVi6wRiaDzQ-uerHtKpsC6wNNHWclLDT7OR1RbGQObuAqzyOVwGZIHYkEF1nTryw_VsTcllqtqnILheG017CHBrzMSZzIGxhe0TCG4FLqrVwu_m3shD8NwmOSWkn0dklvCsGIJx5KR_FB4-fv8sWV9iNapj64qtqMtwfYmUXLyqpjGFQo_Smg101sIw8AKsQjo0z9XyXZG3p0X4EDL9k3hRSAlqFfBLjeqohSC3ft4jIl5dAnfeYgVM3DuOWArz7CeRSXomN3WfDXFOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXhfVajQBS52VRXpPQdDK_7UKDJo5ulcNGqZ5U4rUBZB8HqSx2SXm6PJMNvh63k6K0JHkXcXPkTAvEUbASszNy-2vb8zwsV_cdcSl8VMNXJApqX-RBzbDp_tvrK0wnoUY-NG4WEo7qI_9g7NmyKi7bN9asODRLpf8EZ4yxV-mdpCT9I7oc5PRCP5uFR_qy1_SsfMUYqiuuh96xS1BwOmentnZFKL6gKNVUwLmX1RsbEAyTuWWZvbIgkIiwtyrCS2e3Ib0qqoNua4L0GzNmsUUvwLh3Kb-dShCFHzcNEMFUKmqdsD3N19akschj7oZWOjoTsnoRcXjW5Ja_ynHrCvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMPGXUEqW96POYSPj-SeO4hfvd31ZvWrc5ke1q05XPLbH0zjC3QrhIa2Q0cyCFuS0Bd7kRkRcIywvsIDWj5MJtL0JOVxzFrcbBkpHqJzoVuF-ZgEI8Q3uWGlrtpItb8JdhAy7AfFmFcZd0xw8toRqGjq8z3MtX645lepa2BuADC18lQ0bhcRN7Qk3-7pl73c9n5PXdgxo7APy1jNgtoaaZd-j1iqtd3zncB5ft0KQ5SkvC2UrDBpEzGvdKFJdL7N8_IAqOwLu7fNTUJVmB6aX2Pr0vzJ4yzkRCFty7KKmNyrmQLvP_FtsPw5pSrF8tIVcXPjyhX2k7ThcOLpklbQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmn97-FQKFnzKGI8p4oX0OKU3RMo8ZIYYv7s74O-_cDSYc39Rysg_y1xuXWjJRQoRif-UNUfmh_aL2T-0ouJ8vZY20xUDQYaWwdtAx2O2hm-Fo4hWQ3MLzfq0vAP90K-DxlgK3gIQWKCB8oqscVgQaDKIKEJjErlCqCeyUE78NV096JT7Hk4KUFP6fGEsVd9aPOrME0v4iBrr4U7HVLyAFf5yPtcaXnDM8PARgleclj5yrN-NQncUO_HL0GUVKXQlBwlp5egP_kq0X1wom5_-0TxMJm61Tj_Hv9cBEqenZ9OWBQikmXfXmRRcd_Zrs6Wm09mY-O8ee6t5IeLKxybwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNSSGTbg5UcA6544yoSw0t-A1gke9bW-TSJeiHTlH0QeCjO-7z2DIIsVSu2NcOlPwdUGnGF7g1nIZTJ-aPWeypu8MrUNIin62fJixlta2FeEZ8uHcLAOmZ39I9AyvPkBcirsRQlDM3TEGsDEGiFV0mz5UNnwkCI7VM0y1Pvqgf2-0po-1I8bynXa39_lqELLbafiUf6HODQsSSSND8lcO2Ja9aQEG0FaxYugX1hW5FVI4qWGWYIKj4ZNKEKv6sqMzxMolG8gOTPAlo7h4RQNyVoJIsjxnlSGODrcE7f0Z2jMbYH6b7rn9d2f5JgpXrOr6xs4c1rhfkxlgfhpZmjJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN53WWUej6H-yPmUCUpMCKnaoT91zntrclMSBsZeazkCL9d5zBWhhXe3CleeBfkoEYxCvb9LZzfcirmcdkneKidfbsCugtPy20RhPDpreQgHll7s_acrGQaUh-947PUfBdlxZcIsT53wxknDBH8zo8CxBdeEQuEXaRPOwTRL9Q6z6RCkLJQKrxEcaBKQ2p7qKp7vej-Zivxq0GZVCbT5Za7uLq9hFk8YxRQ1vCXmKhwSfa6E3411TCEzSbLd9ndjtfnunGTNP6SAQtHKOuNT2OSIHs9dtjXrnb8tu-7Ld-L068EoRkdO007HpV6O2PaUFLA1JKwBqh8gLN_qxR9XPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6mt8bqjeSXdB7gqGC-4FlxtPSBIwkPV3DJw7HZ7CDrWl1bT9HNfDPv_kHl30skq1XARX_mxFNNatWDgHBeL5LGSVDTzzOQE4ZwSlds1RDsreVFYoKQlFz_0lkgcWJeleP7cAm83Wu8kMvwN_0wK4LFEJZDkAe6-_hc6gFXZsNsjcoj5EUnqfGuhIajKTXaWFS8PE0iewjlXIaknGgm5RxGJpoZSXfc0oOD8wDgxTTXGfaNzCx1h3C_ZGAKcS04Dx4AHONfv2tMyrc6lUDdQ9tq3VCyqfZkrgqbLvmKUE03FNia_aDtHr4eDpYxxR7uQHQyAmCtg9GjxJz9ysEkKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlFJvo-ysFwp8CMtK3EpvbSP1WehteAVB_H-5_nx45xXwApyY-u1SOD1pq9LJ7l74asAK90MS1vR-yPe78_zYTnoTwV-jtFoeAkmuVsvS6W5Pi_fjhJGz2_KAjRfK5zOYwlhRVE0JkrSq2fCgq16d2MXQ7h4-RedF_Ceq4K-Go2JTEabR5jZ6FHycmE2sftzHRHdzzJ0jhSJFr-nzh5h1l6hLF9ftiKyk6LmgHiAiLUHGnSJWdRuiSGqpOopxyoF0WBAe4_Fp5eyiw2umCN5_y7SMDboJ5HuIzgY4oz8JKoaK-bs6UaCOlNW_ed8zMi-fxWCHLHMuHMrDuXZTpC1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DALJKFJ0Dqkw-rYyDKeBlV0FzptUhSAo0UDquqEpMPn7cktetOMoLTF_9eeRqGJDSeIAVULdhVgFs8eGWNUjzuZtuMQW3TeH9xcFXm_zqHPJSZTxYi8S4H8mTAjfNX_IekHZMfD7sNe7jRkt26GMn2fuXLBNX4eKXPRc3fJBx1jDUPpftZJkJ08ntY-1YIemfbdIQZBSyZHMzpiq6rATwUWfO7HMmgD9I3frxBMZ_OmnAjiJnuaiitbyXDbtthEt7D0vqT2wBaXFXmfrzete5GAWD2wase5UV_NoRsPWCJ9AmyRAKUGKM5SHmmpHU4riwr0GBbrkGptJvBhBkpVabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEvH1nbJ9BjDERtXKQcFhSfNe6Cj3GkMAPAoyde90QduFBUQsZh4G0XFCwuD55QAowsSCo5WvtmS1eS4WkSmoVFLqSfAdBpUsz8MDO7Ua09DnwQAGMBZGZVwK-ogGW9Ux6I_SQqFpNomxfxXfKiwyl_zsx4fy2TfbboKgHxZowcmCtEQOtssL4IWhhPG0S8vc8-oFeQJitC9MvjMfHV1sp9vsvHu5P-uMtcM0b_DHcLCzDQPUtN9nSNQd3SwbS6o0zyEj0hnEK5mtj2ge1Y689-401b-KiYCx03c3uTP-ZzKFbgrplW-FrYU2WO-PbietryoYFKZXCdB-BNxz3UTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7KzTrsTKrBcGYrfBCKWw9nk6nnJiCHo4UZH8wGspfq0Ni-svPjEIuHl641NHolmrb2BR8G5mnrrObP4bpbqNOodNHutxWAooDswkf4Pkot4IFdCIxHIH3jqduSvOS9RQD4A36Loov_lRf0u0wZ_2FFKrmpw4gL6wLAxDChskCgjwvi4H2hegUyZu68WqiywKTW2PJCeNYCs2VgSQG7GSxgalumrcM0fXKZFfVj_xgV2iTfiXGNvL60hNIHVXIyA4pk94zEZilfGke4SavuFTZy1nkZQ1dFNJpoa07yCnci7xaI12qMKaGwFbIyNR2aZDeXjxMa9q1Q3HhWW31Q44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXt28OUDUtaRpPB_FZOOHmpUntlCaIlHAWIUrLVzmFTYiEGPRfgNypN_we9rkzY6ViAQBUk51QKxZ5idGuKnHVsuB_tgrs5G7Jaaez7R0-EkQE2bxFjk6k27YzzQ9v-ZDyvtjOPCM4sfl5pfbl3WdET9RVsscEH4dRT9-s33CIH8_ZkWd6Z-lypeJaU8eBpM6FJQucGXlnR6HXG9VvuOvdKMItONA3m7OsVHN6mq-I-qZJb0QSlqJa59PZfNTLENC3CLMh6zTYYhhjDidcGOhsRed2-RXGhSJtkWn_DsDWGwNStmpcTlB-yrUfOaTTengp1FfrbozIIS71luBdGdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9HONBMLn4b9cTtVgKgBjR52KO87Zp8EVGl7qrCRBt7Nhekp5AldNUFz_V2Qf6U1-_rNBa7GN_eh4BtEeUhhbjkoYr_tA3FgdZyuRK5Rp4a2pQggZKlQiPYfoRGNrnTTEPaQKbpo7sUNOE0QkAFsjD1El75zThIa-mHIjplwdpQotx9lV9SSqZhSnmJLF3w5SXuF9u8fR6_td2G99_fJhltiC2CtdMP7wu3Ctk6Uo5kilyzbGqls0s8pBITY-nESTNG4Sapy2AeHOg-m5Sna33YOj6QTPoZu_UbJVST4DbkVeu5LiF8jxgQymWx1DY9YB6kB-Vj1y7R86lMJfxZIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYYBzWe2bJuEP6O07pycdPz7kxqoBBy4aj0Jz77SN4dpXfkeCUxQTM3uBOSXDyiVRYmsLxIBptzp32nhY_NCgFLPgBut69Y1Mqwg6magPHAR0-ZPnkXGRsWtRSptuwYGwv11BwxGhG0uR43l70qS0nIjzqwl22auLhZXfVLzT-TYPn1FWkJMfxD7IO2Ap9NHowhNj1NfJrZ0AxtOyx10dgmpKd0vZkn-bK8vu2FtYw1YUAi6zop7IYxUi6SQAixmNAJzJMLJ4w9dHafdaSjP3WEoJDddfaPPEhJA8pX1m0FfLlPZbohz2h3XNnPpQhH6qpkJt7ENiAfHxSsnNoH6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvsdbQc_yJxQ27_PiJVfEj3AwbrPTZv9GbgMV4EffWbuawwDVgdkT6Rho3moC_Zu8zZxWFMQQDgXtKLuDvEBcItvwtu78_01Itz5VTP0jPV1eLjaSbqMWpZN5larjg5D3p_TLbUC_fK_9sFfyP1awf7oJnigRhABvlpp11h7Qyz274TV25jAiBr19kQliZfd0d8yer0uD8AdL4W0ik6uz8qOY8KGojIIWZbqj2pS97c2luxZ9hh1XKNC7cnKJAwCpD0SyxDGRhT_VwcipPZ5WwsRFJMCnjJLxiedBJ_2W1ui4chLd2fY0oHoJJ7ZI-MsmxUQet3iCOmGj11y21j4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-XZ59KO3PXU-NH9a59w6HrKpLGfLIVY3hePHtfsjoCpvG0TeZqyNfIqrkLNG6xIvz-k8bVReMdZ_zEugYq0tSF_IgtXPlcsqE7i3FTcUeb_1BmFWIozXur_TDStP0h1Lke9punvyIz7v4y0AvytrhAp1Z8Qm1Ae1dd_H9QJpTJ_d97LeepmoroWrvhAuAbc0EHrrziE-KCt6YpApv_seZ7urcX3h352BsruJ-xuoXMxLTG6vSHT7XzIQ6WOpw7ikzVpR9ygteLms5s2XaejcjI18pF9pobvJaFZ7QFWIFDdw8YlYs-aTzP4jccT2baSa9APgGKlUHAWRfREOS82-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pubdhf_sDulk3U5USpkYvxKIThq0t2XIypheV29fGWxA0UPF59ifEc1zeWvybV2OOgOYWt9EacTbQZ0_-M0BiB06aCv1ba1gVrM2qogXZXrILqBL1AzapCOiTdP-2_btVznrFzmllNnDX9kGpRO-_TCIumsqzMYbykZfDrYVfxz5u1_Zi0nn7llWkB9RYCcNng80k32kyu-0l-fkRaa9rt_fmjXZOsR2km4h45eD9UL6J-1vkgF50_OkdXcrAGW6cLx6jmr_UQl2zCIBg0d7RwNU8wkzxcgnQbAyBhHSMYp5rLSWH_LDvhxe21qCczG4qtXBh4rDi7MyisVZoJ3ipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKKr3WdS2yLNDgUSLjqGpmLMTCWkhCtw0XRA-s0sR8cc6CmG17yOgRmh-VLaQApYd4DsX1SM6Qmwz35eqU8KysiNuPZPamzS1ZInpL-9-uTIPMNR8yt1oec6pkC2iFHWiV-z9GjaHTcRQIYbqaWc0jkDomXScMKfZ8TWllq3s4dY72r0yzwfMCG2r8tKmJYPVmnGnV6m0DkGJvkI99-yds8ifhNrSGZgNuynORry6RmoAQnCwKOqcvp5W_cVXAw6ItCK1T6yYjMVXJLmG3kbsrz8zK5d3kmPfEgg7zruEu6Bmo0LIpYm5bW9dmwgRfZvu6mLgKTZCWLmqLHR0b9-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA8r8E0nNDv0lpx_wDO7HspMbpZcoRcGgY1PpjS4rHuqe3sGFK6kXVQVyyWGUBvUh43ssBYrstPUxQgEOjbwYbB8_OyBPRYlgmj0cbjPu5XKsxTmy_jmd2DZGqReIUxAzF148NGe7JoYYhqaiqFBYTMVz3hrmhKhXpJAN1JHr9csLFmkEIQ0T9r6XyucvZN_PFMHieQ7Ph_SwpRm3ZB2hCdzd9R4a5PARU8tk1NR9co7Xy28BmlVkkseVxTr872r1BLPWh85OvpgZam0YjmNl6sUgPUz_PwUxPUGtywxI_17liZLg7EpM3JMve2z28vmLOJRlRtOedk4hPszW6KSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXCnHFwSDGj8Afiql_CuB_oZ-wpUG3gV4cr5YfK-46rsTH5jZq86x-vIfQxITbzDoavZHQodHkTu3tB8vcd1mJpGltehp6sSDXvOaUhYjb4rnbbJJ5X7VwLfoxC-gl9ecMZm76VCBv-wkF9W2UYg0et2iLyVu7ouL63V7GTp7lgdQlkr_-tZnCTzhg6ptpb-hMbm53voETYZnOSrcMNsNlk86GckQFCCItak0LNZch25x98v-c6CJcbpJalrvnveSdn_S7g2YiZs0V6cN-OPpMB2MgyxFGRcBhrM_U-bLkba0NxmewBOhl3ZzH72qZjsBy4K7tRBffJcvNqrmeMhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6cxgJ34nHwG_oNX8_FtcS6WTtZxUCwksNADcPqDnCXDShHnuS4KdaLcoeiO6a9L0IPQU3oU_2HpmJfgMmL7Y3QeZjsIMDKATELSvbq9Ee_gfrSro8A5Te1pgm_ow64Z0Sa_eL3JZ9odWyvnpn0RJDH2boQhwUDCpJMEm7sOBByiHa6DpU2KEBzn1da_UJ9WXcnIg0dvt3EWNwWsPFjU9su0OMji01ZUGHfNdmlRJAY7T22-6kHmLeG0TzeqdmsB-YpZvi-QWHcz-4m6uDhYVBROUIzl_4OwMuDeoAig9O5UcLM7tyVZnit7d0vU-sxAjEHtm4pu8uIPVoh7wIQGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxc_Bjb4ulxRmtAgGOyEF4xTqepBrUAO8xwzFWEisLEcLBhf9W5Hanp_e6k4AdODPSb127u_WBrwVu22n-4OPjAf0PwLUS-KdZdePjcFjzjNqPQ-jqkM82WukjaF0gdtwM1uxFzW4wpaaxVCp21Ji8aCTRj3-HLpxuSYQn1oG-ij6lQ8XhKhiMZrzSHV5Rrl7xFu0d3x9rI7Z1ghfsT91x76pktsVSRqchqZ1mJZ-BXgFEt6maSYCFtIzyX_oTXu5b_boYs9BObrpnhh4W2TfPcWHcrqwjEiTOnYXbq9C0zUZLbVhiDixfBcZ2hGgCxFsoiRwsCmBhucU3qRXCCRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8IauiJm6XqpNyy9OgSG2wTgtYphm-osTBbjNoLRCbQl9bngBxN-0hgFW8g2C_hcjrNuPgQVHsfZRzqr4qiklw981sUr6kvY01TSPb3rWu5QrBW_rag48HqH3P9b7fzuLhfVY0PZ31-FbAhQfFeKhYd2o1xwAK3Pb-ZNiOC49tEGpLaDs8cHo5pXvo4Sy4H6KN89UIJ0izstyiRdJgM9nkNiYsWJu4dXKgjutxhwCuU-ox2Irzd42vEGhr6elP_aoG_AzRYgqR3QghXjs5dws9DJPoHkBjWw0XBLDL5VMQZth1lCd2YxSJsyj9d69ygkSAMz3NhQli4yZmIuXvUYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6nfrb8dOrrW2s71vcYHMX1bclsferZbDr0I1BFXUt9VU63m31QViZH5Xjvq83xqXVLDn4InKJTNLuV1FBStuz9gzT8MG8mOLNvfY9UFALO1AZgkDwzHUzbxWakuSAADvyue_ljrMFonr9Ce41yG-e7uRkbH_r2wQm9piHPVElBnfrm16hw1zhujjB5fxN7l3WSHmNoqXZ_IF2gZ-bi8v61Fojo9-EMxkNUmAzyaH0ATmh4YeEFkDQfmjJEmihzMyHcYPHCRTyGwu1CQeQW6yR0Cf5CuqehCasFj3oNhcpxzZB27H_6wydHfOL1aBjruC6FrMqLuZmVBAnq5lZEczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZTOWwNHs_NxtRi60FtOLq9ZWN26uq27ALugAUgB6Fu5CBDAb1wrpe4wZGTmYvDLSnTh-KgtwqNQw1dw95x7wu7QOpAxzICYEwrMR9Wunypu7tBy4B7hEvD3m2pbUTqva_5J2UunsFJPDrgo4KHwtOC8tgOOJlCNuC9ZvQX74NZNWrcFu4CWEc7Y2xNbANhbHHU_5jWqLUsPbwPcCn0O29rrXnaxPDOBuRsjs799YGYdJ08heVYztGqAAzSdjjgCrS1BbJ1XpaAS_49e3nNw1lnOfwUj3x_Im9asj9O7ymDqoxbeOzVojyyU-BjW7HU7En4Z6b06-I0jgww-bjXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=CpV_kmP0u-oou6Kp23janqrbFRO9AUPnBuG3ZCY9TH2ikfZZht9S7baX3PTAxiqLTcg0u-EmUdMD5aDRq0tdPYWsh4dRtckFkMgHn4vB3_iQt5XH8wEEJ5KWzR4OuqT7-5FauqHJ5Favkv8Txfu1ycNmaX13RRZnm5qM22oGNTcntW03tvetfaRlzFwuujCkv1Y4hWtCgODNi5tZKyLR1HzMEesTcwNqI_lLRsqQOJdJ75RaiKhsxqjdhR5fXq0l3OZRVRqHyFZ2AllkXyypjwK_60F9Qna6-cc3f8RZtqFTpeY1HGTe6Zm_nW2C0dNGdBxV9Clc6UJf6K49cXvLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=CpV_kmP0u-oou6Kp23janqrbFRO9AUPnBuG3ZCY9TH2ikfZZht9S7baX3PTAxiqLTcg0u-EmUdMD5aDRq0tdPYWsh4dRtckFkMgHn4vB3_iQt5XH8wEEJ5KWzR4OuqT7-5FauqHJ5Favkv8Txfu1ycNmaX13RRZnm5qM22oGNTcntW03tvetfaRlzFwuujCkv1Y4hWtCgODNi5tZKyLR1HzMEesTcwNqI_lLRsqQOJdJ75RaiKhsxqjdhR5fXq0l3OZRVRqHyFZ2AllkXyypjwK_60F9Qna6-cc3f8RZtqFTpeY1HGTe6Zm_nW2C0dNGdBxV9Clc6UJf6K49cXvLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwNf4GOToVpec4cpqA7C0MLHbF4g6YbIJspVb7BwsjN6V5iEs0hBSWfTcZfvf3DyqNqoUEogkLbNuJfWiY0SwvYUhyvcxT5pKfK_qoRutiwlm3NMTHBmpfp0glQfjZ1p7eQsvLFAqmLBvz-4WVL9ibqUxF3ej8cm9bmlMz7dSMpSJgdsF44nxXI3SnxHi5O9iH7fWpJX6EwsfVav3A-z1SLv3w9as1mHQu7x0uRC-YAvbV1WZrpnakEKSYQC577Pa1CSERh_WPe70JUuveNw7xPVs221BEUecQFH5xRiDMRgDxaLsAVM9yZITi8nR-JrHsdCa3T9jol2ts4WMrPFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WokMQnTscCWZdlCPL6vwnrS9EinoYvHwDM9aHn2y-2InWGELNm863ipUg6H1C3V1WqBlqeQ8Bt7mHl9UdUwgeD8PK6YmoBZPD6SBoyCxYcOtf8FkkrM5KK8KHK-HbaTKxFj_ApJfXf08nQinSnPu6T42zuKaTGdPKvBrYTVJSFZOUCAGVjqHcb4hdkIc-yf-pVS8RSwgtcuYOtHnXcz0pRoEmyMknVmYii38j2m7BZ8tYnasTL9rqa0FdhXsEiP1ZvSZLf3ddi7QP6gkwg1gjsfLo2y2-Vkzz0PQIFochlsfDg_bWoPI_k7ELngj2yKnEidM2PXOQ8f9tGZ42shmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK1z0jANHcQIu71JBgS8bC3WphshY1KAHov9t2BYNCkofxcPnurwErDYwRYC0s1iPYwsg5r07nOTrfP8j0KAkXVPtevOioThIBT3EtmF-rtAUnicNE-LCbeVrXT6hGDqspt_EO4F5xCy6bveNA_kJnntBkrRfnDlWo7ACVW2fNZOF1kxUNdZIxb-V0QnzUUy0gDzcHM3zo1e1HXanBZ2dUudJbJtCly5r9Zkx0_luhS2axf3PqOp29ceAHIzBNp4FT2wUTWekWjtuBqi6g0MScku5wdkscC5bWN9mTqb6PvKpeMfh4qo4j8Shltw6T-6h31EGI1CyKT0mrAuETLSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=YifkbFLHPZ20uVXHcVX4wYq5WHWsFe2InZT0hqQ6cq2BqXmFf4OcmJ8_LdQcTe2a4W_ZgS8wsVvFz_JTCx-b0SP9Q4hjh7CGYBWDF9jOWB_aF89QBzsnbBJAhrw457kuL0QPdvzVOhiXec6sbXrBN9c6m1I5CBqM3BHOkbgG2-1rf9DI5r_vxNYZ49gMJp_t7enkSqmfPyPaIKZ1uuLdRcmTk7IKSAXCwYLPfvtFwTGjpiLx_wrmLA6fjLdlNEmmX3Z6Gg2uMs737vY0Yn3V5elExxdYHGKfD7R-5MnmEapYcPcduw6KySF3NvbBHg3lN7u_sBZx0Bn8YrUqRjFX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=YifkbFLHPZ20uVXHcVX4wYq5WHWsFe2InZT0hqQ6cq2BqXmFf4OcmJ8_LdQcTe2a4W_ZgS8wsVvFz_JTCx-b0SP9Q4hjh7CGYBWDF9jOWB_aF89QBzsnbBJAhrw457kuL0QPdvzVOhiXec6sbXrBN9c6m1I5CBqM3BHOkbgG2-1rf9DI5r_vxNYZ49gMJp_t7enkSqmfPyPaIKZ1uuLdRcmTk7IKSAXCwYLPfvtFwTGjpiLx_wrmLA6fjLdlNEmmX3Z6Gg2uMs737vY0Yn3V5elExxdYHGKfD7R-5MnmEapYcPcduw6KySF3NvbBHg3lN7u_sBZx0Bn8YrUqRjFX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5xx41G9DOvcYCbSDs1kqcGd6uvr7Up0o93cRSuyFofHOrxy7o5O-AGEWRU0e6xV6C7Wc7oATXPBv3ZRDo9WfTPo08SDBDbJuXQ3ZfHjHm2WG7cDBCCRlgRuLjIkcmgiqgMO0B-7SmlSo3-cflLgl8LJQt-rrTaYLn4HDb5C26JWtJpDJriPq3_pC7nj_nnIR28lj-Jsc3PDbJS69UcG0aIzuB5NKzhc0X6s1FfzSA7WeEPh4q1BxOizj2-WJsRQgP7PAfBgWYPi-qk0NbXECV8uaG4uwadJxy5ebKDy6M7QRbJLknPZjCsJYk0Ue-VjYNPXbGG37f-AICCRWCOg9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neDKq8_61IKarbwe53dL0ZqOCd66uZ_gYogMqDv-amAYZBO9MfRNrt4VmkOU0aOAEukecbHuxhEEwRLt8CPJzeNUekngFd4nOdrGJc99GBJDjDSeDWNJQqbLe_xI9Zx2D_B5ozKiYseSpe4B5e4RbOdhi0XTl1TsDLNARRxIDItQbTSSutJGiwKTic4Ng4BqVqDHnrR6sD2uciJ1ykOqsMUJI28HgVsKP44YecSlfnbMnVvqEJWfDNpSrOoG8Do_xzXknRiG6GwyvRojDN6_iNw0-P9pDfv-jYrUJM2Fq7_9TifqKtz-0KWh76cL6-qXJTmenN51puWxM9tJla0cBceM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neDKq8_61IKarbwe53dL0ZqOCd66uZ_gYogMqDv-amAYZBO9MfRNrt4VmkOU0aOAEukecbHuxhEEwRLt8CPJzeNUekngFd4nOdrGJc99GBJDjDSeDWNJQqbLe_xI9Zx2D_B5ozKiYseSpe4B5e4RbOdhi0XTl1TsDLNARRxIDItQbTSSutJGiwKTic4Ng4BqVqDHnrR6sD2uciJ1ykOqsMUJI28HgVsKP44YecSlfnbMnVvqEJWfDNpSrOoG8Do_xzXknRiG6GwyvRojDN6_iNw0-P9pDfv-jYrUJM2Fq7_9TifqKtz-0KWh76cL6-qXJTmenN51puWxM9tJla0cBceM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U467I0-2rlw1bj4-Q43FhSdbujL-kyWXq5A-b3pQJL1mXU4-Q5rj-f0Y6gOPgLwy9cDlHtxCIFNyqjoUuXH5WCudSAbZ-uHXSUfS4w7p2JOy_AyWitsZCUwYY6t64aeYV_2FYv7nzViifeqLseHmoFhdDoExec9vV-v0Q_1LhP9Mh5X7WrtaQbAN7s2_MsupoGVKUgKTdduxmmKo3d1S0uZXCgCE-8fwebHXG5HNeYBAR_o_iGMyYCJTAXzSOM-lAJ_234T6cA50KTrItSIzUjNytZqXEnQTiKwSBXfDatQtyqjd6w2yKRRLYmhllFDIB3Q3hSQ8fYY8XbodZvioaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4WnBS41Qx9KkJg6n8HjnyERyn47XcmeJxj6gco0aMatTpU1rdcOMs4zzw-B0vC4MlBPgyP8fp0EGWmMr2KLdKPnamvS2g0MwxR87VLZaHbRhmqCOxM3ctq8h_TzndLOQjxncBDlUnCE3s4i82Ra-_hKTowGcmI5GUDAp7RFaRzOhHagtgMpTROGqPxovpmn1Twq2XGr1MIsJLHRZ6vSP_NTvqcUpycwRj_T_AlhLmm9H8WBQFigX759UiKj8083v_LU7VsQenaseu7sEz4SvEqpHBaDQhybr1maoSSOFDfUKw0vDuN6N0Bv8-PfWJhryVK4sE4R3pAoPsWvDwpAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM_c-cklYRbZVzmQRj6MaAhk6A5jgbcx3la6QVpjjJhfJ3lNzQw_2zjtEgrEG1wUH_hm_G7eLi8oplLGJZc1Ai-w7aWiY5Y-LDAfc8cNmtGDj_BIntPvj7TnuN2YiG_h6aYEvYSnCeq13yi8FgSgodcFB2KBQcXta-DvT60vq9Ywxq_ahQYmXNvhp8fNyA3oNNOiwYgVXAq9zLlINVZYTyrlyvJsoKWKzyNjRcyiOxF7D54FZi1c_3c5nQW9J5PlFBK1s0BH72sUxr57gtlJ8LZoV7M6MXuCk4gs_iu1G35_UvYgfErvRM5naS148EYDTMCkr0U0Ch2l4iKLRICGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EInMCwACHwAVi3EGR_Cag2YZ34YR4rrmXVntRFJjL1P2FKU0Rv1JjyLbcd2sm6BYhm3yE-k4RYiO4OTIR2aLfnh0pyKL_iGSZIU5ksbVW_5VivwwmIkgmtBrP77MNgpZU_BO1lAw17AIWbEKeMYRw1DbeybMxKRokRZV3l267RCoGShUXOwBH1ln4AAzeUeUcXpKpBGV-5S9Fh_dVCX3URkdewbvKKiOXI24uUneZY615IIB0IyUlr3FRcUfuvt2Vm79HnJ1IGo-mJjoNF9RGuN7J201y90EQPUh_wcNJOUY_vhCN1xIwWLV5B6XGWF44v3BvN-zuv-S8PtDsD2tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdRD10jJ3KLwT5XWIx7AUoB5wXtNm-9z2SEYj0R4NdckVZ1rt6FJVYp78WKWZHpCk5XwErP84Mi5m-gTKIy8CG8OT3s-bnR8lzKNv_qHdlnmzjBExSY-FWZ2Ktdl6k66gwTylgE2uhbYeV1uTCsW7UMo_iRZGmHiFwz-aslA8xiRwBe1khxG-H-J-wd3DM0i5SXW2rD_0oPiQsOmkYYXXvoaUyrfjUnrWBQDbo6qpXdqtKi5fPp8cMiAPDG07Q0IAiQ8IBp2wz5PZhQS4genlRqg6PY1-Pp-arOVgVbPCJmfhfcsUhN6FI-dbakF6ZcFBxUmPTDEY5bPxJjMTe45cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCe6nBJTb1yknJAD4oNTmmrLX4R5XKD0vyi9umcVgY1tXX8d0Zi0kI96RIsGMjzGWy3jmlgPo1oDgzQSLiTN5cMgxsqrYQmCtdVCeRw4WSbOThqGHrgjc8bjtEBEQSVL_fYcsUB_nWM5D6WJ1EktksJX2Rsze1Lif1Hw-9Bsl-aVaEk-bcGiXh2XCQ-NL6EjtZwuWK3gM-mVr3dRQFXQ4jGfOIvgTE0j_LEVd7Xnicgnqr9w1w9aXtMW-dQSZdNglJhVebZsedi_uCtHGbr53ApR1Xj7JFZy2Cc7SwtotwjEERYsOe2-kB6R7tjuO_txBx9g11zqlnbUZVSbubI5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFZ4fUMl2Umz5UFmV2H2-wlFfG6SMqZT_ECSB6BRwL74MX-kyWkYepZUgOiEr_DyH8-F_DzS-jweUaGC-Y6QUP4rty2sll77Drw451jioTGdJOn083i0mJyhnHP8Cfjay-w0umn4QN7nHVHmRMvm_2b845WendZG4daTIYADQ2uQu9JpLZ65nOF23CJz_6wkQiU_iJoG-hZl876GS9Uf8IjnQ6o11k_x1-fmHPW5nRlxKIXjnJuY9NNjSHpf62FlummMrU9h7ePPjyvA2bvywkw0nZoopje2kZsWnvIPPfGCAc8vCfm4YD97yFe-LTv7JbvRE_QEnQ4768okp8FPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCEaWw_AmzvAGV49di8U5Vazhrx0JCV1Iq0jypKEK-N1WgXBddb17WP-83dP2QqSeccRKeVOOwJA0c8QkptV5n1C11HqTiBWUjx8P9N7U3ROc2YQHbdBJyjUj73eAXvg8uNTBUeRqOsCBVYocqxsmmcqLDqkqTBFgl-F2XfjC25xz3Bo-RipmOQr_ZW-jfA4tEpy17VlMNF8pxZExB0S1x3WNqRQAdeIeaHMhuWiIRVMaFt5_hNmlZK91wJUw2ELtgHWWEeG0bpgFy_E9VgfGozpzd-GPdu0UDVDiw53L4Rnc-mXlles3zoOs3z4bCoBqmZMxLWmTyal6sHcz5TFww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHGcpYLr_zqjoXngEE4ZjAg8iY77Ng19C6Od3FZV0hH-UCwvra6ROVre3ujG0BA4idTbphOFSYauo0JIXY2UqxQ3BL-WyrFBvrLP7A5UAV3B-pgsx27sMwWJ7TYe6u83NigUNOfONNsYVkYsYFCYh54QYRaTmDr3pufFZZ0DSEtfcwPkapSUQy8SKapkczx4HJgtPzBd61wRBV8s6t0ZgVUes3Ait1awOerJdZ3dIAcxt5X1u9QnL-Ogm4BVC6xSLeKkyE3nab7YsIFEd1hr_CbNAFiD4_vRd7BRK3KbuEVOT3Z9oTIaQpi8c9pdis4I6pxoN2VgLFtUTSkyFM8Kew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qN1IstRZKAzpwHTqgFoxnlZosmEbWo2rVaWG2hA4nVifZMQXU9QqemhHXR6SvQGgLaJM4ouHiRABzdQN6XyDEg5oZkns68uZ-1s_kPzUYntH9ufp45b4T-lVaIToNYBD9stE2WTc73S-uyi-hbb8bGHz8s3bqhIVfnEXg5eyZ88mGD26YPWQQsyia94k8Dh4YORA5hLpdvEx34Pw0_pMMmlJ0Zu6sVAjZBwGIkpis6OC3lkxriTGkNCdh9dU1yeA6ug_Q5mpZ8cp2LtchP6JAOA9V2iz_8jgNOj9jFlzYG3ISmkdI7oJaPVyBQ9bBmfSE9ONN9nB7CaClQ1kigu7Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCN-1-Sh7EtAFb_2PfX-PCNcJUKFqwzlgol6d3Z3tYFRnlkE5TeJIwmBuy7imagEwo1t2iGIBaD8EzrVg0xhxw0FYzRU-R4YP0CQKJj3LXZQPEmSRd2i3_UqkSrhsii7jzTJbaZYt0mRMt592XOiTYpNV7FA7KZrl-vZOjz2UK-9Npz5HIcpFJzz1UfZ0jTus3Q3KeXG-E--3QbNv2AsCNNQWROLxyd3hZnXE319Ayw5daVH4uQDEIUtlFdVYxyjokal5w5Uzk366y6lAGDBrPDZuK9b8DIVfDqazsaduViB50KfTnApO1pcoLR89rC9sGIq_IGgcT5UbGT-1ELfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHLdrP0rLiYxRwJChXlS-DaP0zQJ_SbWE7BkEEaOY1BRymBuW34swGPtVfDizUNfW5FfJsFxgs7114VOzkjQLqqyPxQyWKAt4Q2axXhWCBIgjWTPhrX0DL32sraHmLl9FTi-MlMC2XdvVRWQE4baLk1Rh8bATmwutjdOVCHdB9A4azBMFEUDiFsd0k_RIntCAtqFtVKiADMp-wKGwsINIa91Sq3k4VbN4Ri9-NNKa7fMjiwecGZT5SnDNq0Ri55gH3F5qC4LPXaYfIZWDk5qyOodQj4pd373foCtNnpS7yBnWu8CVV0-FzaFmhqYlGF9agWvBVELSZe50trtdtEvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEbrj1aKtTOXczfsUd8u1Xx4L_3dCsxBexFw4d7dvxH_vFqkMQvF21QIkpmkC6gWWmHFUgTO4XjCeaVNKNGPYl_wAbbLT42DZCMwCyYBiPuv9DgGyZH6hzxNSkGkbX-KBZe-5BXsbufQropwCb22WIyARZPdZT4-DsZEzKCzCLVQ1BR3N1clGX8uJWoaC4YBVJ0d_zKybb10_iuF1YEo2Vlg2Kk3clmJ5GB6AbfN7ec5-hbfDNZcEy2hJBRwUXTXeZ5wSMqOZ-BO66AHbrkJHLwge7B8-ivJKnkbG5_hZ8QnU8_w9jPgvIIIrljrtoOzaE6K1VeAcHbi6WnmLfpfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBtqYh6LvO19p563iDhEE8GHg7Nc1i2XLv48r-hZr-9lx0vPNKYZPuFw8fGhmUcpVXxGyy14Ctzb8fB0q4FcpyIDPTPE4M_3rYpTLFzfODp5OiJdBUotB3ApOisOo5mfbobgWkUYmKVFUQWbik9jnTpKvurVb45uBW_9FuPjxL5_A25jMj3dSA53F_DP61JMWVjKh9wyd7M4odn5Le9N6UDzStmdF7vSLDTZvRj_3cATGFqYpTRQs_6Pg9LULKn1_EqJm-Al7bek5-ieyUk5TEnCL7ZdrAuSMzOl7OHscPaSwuIF7b4D1TGtkK4tSJ56J9ocRwVGO8SdIs7mTKJoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=D79NrlUudCjNx-awzYaKmMiZtjYUDtSn8uDG90gyL26hry3KNDOJCWpwFTDunuVDOaroi-lRo56Q6_aVyxqzJfupsgPdyOfYpqjylKsomFdYLIOMqMdiKsuX05F7_lEqNFYayfcRVILxrnyUKqXoe3vBozfufl0YeuW5mUK9SjWCm9td5RWSth2-i5NAWrABUw6lkliDN_YlD5iL-YtfZ8Rc157MCuU9aM5pjwzVP8nA24eKpfgCHOMV4DtK81f40wMDJB9CvL15ZfXJGWKP_nZMK3sqPFzDRQYer0_SbpAyeizSgO8-DkgM4XVlYO1DCnGnrL7o_T1yvI0RR68Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=D79NrlUudCjNx-awzYaKmMiZtjYUDtSn8uDG90gyL26hry3KNDOJCWpwFTDunuVDOaroi-lRo56Q6_aVyxqzJfupsgPdyOfYpqjylKsomFdYLIOMqMdiKsuX05F7_lEqNFYayfcRVILxrnyUKqXoe3vBozfufl0YeuW5mUK9SjWCm9td5RWSth2-i5NAWrABUw6lkliDN_YlD5iL-YtfZ8Rc157MCuU9aM5pjwzVP8nA24eKpfgCHOMV4DtK81f40wMDJB9CvL15ZfXJGWKP_nZMK3sqPFzDRQYer0_SbpAyeizSgO8-DkgM4XVlYO1DCnGnrL7o_T1yvI0RR68Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txknZ5l5ta4bVoaZWwt0pIraKIblDFruJ7WRqU2IduKoPVYfOEJgfn4GfNccQKuMT2R6UwPOpm4489FB1BxHVBCWdmaKZKK1FNRmxOb1plPwBsFq_dgmfc2pxXfQMOAy2snzIz_0clT0i0tZY5wu3uITHOB8JLnwTz9UmWYLpgG9HvnwIR5eK4pvw99SjYzQ8U2TjTayhPsaLt7lKWxGxhok-nJH3USxskbJq51PtJXya1UYonE5gjrkkNpGEobEpTZ-GIOxq0Yls7FUcTHtUQUeg09Em8LVxXu6l8wTRntCVF7_EK4FPXvSzZhtZBoD0jDF0apTTxj5HA5KHum0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4LYQbPi0S3X14OFb9U2OSChg5SkTsHkXsRs6gc2NlDWjWsTSNKyoZEq35ZqKXaielyZ1LhI_xeXJy2dABge4dBABa_dYKFtXgWgijOAeTAXUUjAZzjn3hw4wC9WJendXXCzRmFGB0-KfTNF6lFS66xpBH7Rq6RsfzXLDr-qWWeaOHo9pRbLbzXeKpscfet5F6DVlt_p6dgoMarHo9iBRbOXUTaTIx9wPRzp6GAWGo4xWp9iM2-QYsdaN15P3NL8118lJFCX-SXf88Eb7m1Y0e-peTvpFV7VzlQutNY6h2nN_ddoJrhf_EKwezqo2ma2g-4keKot26a2IyktdzpiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxzH2D08u-9eQTtp-ChLH32IZEyj3_ARGx7s3lxIpT4jKCL28F10WNmnKUaOzPlrPq2J69CqZUGn15EZ10-VxAptylnmfthUvgptDXMYT-N2eIGiWUTCgG0Z48_16nGLsFlXtBsz1bIYD8jhE6xDU2hj7XiWgh_PGi0fpQKkrVT2WtNKzgB2RueJWenbWOIfi70QDhZNtVzRMSXxejbEIN961lSh1fYVFnGaiHRcB_b-IAJbO4sq7p1LX5mwb1XRXPH7ct2N4eK0l97D5CWVwLzuOSQwH4vYwLjrmuwAz5MveDXkLSjVQN8PP3mxdec7xeFYlb6B6dizJ3I2oxedhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
