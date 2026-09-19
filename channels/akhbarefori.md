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
<img src="https://cdn4.telesco.pe/file/QVXn3d0oSKEdI4e-U-s8biouUjj9p-uqeX4bnbJeDT3t_d-sOkfNgihB2j2qSg6cTe0z7jnqlHGvtB1u1lW2wKJrJxPRplcHoxTVMIjypRJG062sOsFHKOTk4S-nwHMJ9yv22l4anleSmjKf0rg5UwUu_0G8fAtmWyzn533B6kLukAyEENSdx7UAZrdLO4fREmCvPB8AHGk2JXDxEhpzWlINwTiWGyiPsAAczVxupWCBgltZAVUEjeSPrjG3P4JBkJURzOBIA1KvAwb6YqD7A7qCipizHf1Ozg5VFOLBqJlYkSr2amwqijFnrMAZsUayqCLjifnJg4Z1H6a-5CwupQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-691188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت ۲۳ میلیارد دلاری آلودگی هوا
محمد درویش، پژوهشگر و کنشگر حوزه محیط‌زیست:
🔹
سرانه فضای سبز هر ایرانی به ۰.۱۶ هکتار رسیده که کمتر از یک‌چهارم میانگین جهانی است؛ همچنین مدیریت پسماند و شیرابه‌ها کیفیت و کمیت منابع آب را به‌ شدت تنزل داده است.
🔹
وضعیت در تمام حوزه‌ها بحرانی است؛ به‌طوری که فرسایش خاک در ایران تا ۸ برابر میانگین جهانی رسیده و آلودگی هوا هزینه‌های سنگین درمانی بر کشور تحمیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/691188" target="_blank">📅 15:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxevddRvwomw1rtsZ4_bXA7FIRuXew-jMCbdAQtZmi96Al0ZuVihQndRu_BAAUF6tikkUB8snY8Z3CyTzgJmdOk9eRcZcLdwt_LkVRyFNEO675f-kV5Eb62Psr1VBR_ufZc-T-MBAz2ZHNmrBU3gqzFHvlb0v3XWDvx02a24sXkswAv5UrLHR3btZDbZnj0hbpq3XBpdtZrd9f1asOrw2mj5BAdCHrr2592pzCsGTlnoH-l0vH1IHQd1c877Ygigimk5P_CLsnJQH683rjJxWz1hxSJXZTSp9_1mRNSZW1xJ5rzupn5MV0jGTFf-djLyCdjuRBqe2_ICLUivNhpqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش المیرا شریفی‌مقدم به افتتاح بزرگ‌ترین پروژه کشور به همت شهرداری اصفهان
🔹
بزرگ‌ترین پروژه کشور که به همت شهرداری اصفهان در هفته دولت سال ١۴٠۵ افتتاح شد؛ به سال‌ها حوادث تلخ، ناامنی روانی و عذاب تردد مردم پایان داد.
🔹
زیرگذر شهید رئیسی دروازه ورودی شهر اصفهان از سمت شرق این شهر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/691187" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
قیمت برخی موبایل‌های اقتصادی با ورود محموله‌های جدید تا ۳۰ درصد کاهش داشته است
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/691186" target="_blank">📅 15:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگرد جدید کلاهبرداران برای خالی کردن حساب
🔹
پیامک‌های جعلی با وعده واریز معیشتی، کالابرگ، حقوق یا ابلاغیه، یکی از شگردهای کلاهبرداران برای کشاندن مردم به لینک‌های آلوده است.
🔹
اما حالا با ترفندهای جدید، روش‌های دیگری برای کلاهبرداری به کار گرفته می‌شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/691185" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز پاک کردن لکه وایتکس یا دامستوس از روی لباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/691184" target="_blank">📅 15:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
معاون پژوهشی وزیر علوم: سال تحصیلی جدید در مقطع کارشناسی ارشد و دکترا کاملا حضوری خواهد بود
🔹
آزمایشگاه‌های تحقیقاتی فعال خواهند بود.
🔹
در مقطع کارشناسی ظرفیتی وجود دارد که ۲۵ درصد آموزش میتواند غیرحضوری باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/691183" target="_blank">📅 15:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyEe6SuBm09t1UrvPTotaY4SgTDapyUXq49ZNkBUfdXIdGUFVFUqOzagiFLVCXGyod0UYLrrSaBbdlnGIsQhsfVuPTcBafm_ee3hBmhmiQDHBO8WhGqRKp4OCfA9TuHXFFqMLxO0dEUh_oO0lAKbf3eDQal-6IoXsNj6L5Lht7mN_uk6N-ddq2C7QuDoZe1S7TDCWsDFCJVka1HLaQofcQwkkSegxz4M5ab-Z-4TyQjddRUAeQ1-hYowlF1RbPJwEG9QaecGdiu-UFpDbfnRdyUYYXEd9xWfdlw8gF0o08T4T6FmKLI9f22J60apC_dSosGHOZFEJDRVPH6Jb8hVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیان‌‌های هزار میلیاردی در شرکت‌‌های دولتی!
/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/691182" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهندس
اتابک
وزیر
صمت
:
بانک
صنعت
و
معدن
در
ارائه
خدمات
به
واحد‌های
تولیدی
آسیب
دیده
در
شهرک‌های
صنعتی
خدمات
خوبی
ارایه
کرده
است
▫️
این بانک در زمینه راه‌اندازی پروژه‌ها و تأمین تسهیلات سرمایه در گردش مورد نیاز واحدها نیز عملکرد مفیدی داشته است.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/691181" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691179">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1HD6tK470Z9CELReeybUrN2-lY_Bp4d-uGZsZD4TB_Cjfu26QCYYtDuCKCFVUjt3ZQac4u9WRopdWKHe-N1DHmznoClYi6KUMIGL2Z4ZfOIwcVYsj3EDSqVTWbjUwlni683TZRfY1G1CHAnWzYdrH-Cwge4B7rbKriAUi2Id_2keq2pSvFD_Y1VVLO6Li9ZgThjTPKDYTTV2h9ig2c6lnO0wRjoSODXcsJ9mhEVP8F-eDioMYa8vBSIMGFqHRC4T5BmRq5XWwHxnYOxLXg2T15pYMmCunHw2ofqt9fGSPQad1-WoKv1DuLCS8UNAz9lUxCovRKVhKVCKwIfFlKPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXUs5VqRJgnIifvfQsab3FAQwca0MW3QgRG_KU4vSbzKRkS4V_Ft0dBxxMNTlbrnPcDEY9rQTSTq4kNEC6wEmi5YUEF0k18eR0G-GvOvF7v_qmUVhjhOkv6BFFzath4NFwGWDEMndLc7Z4-ju8EejJJmcHNgBhMQo__cfi_9zyKJ739z7zmgV9OtGArzXwrd0F13tN2q-_e1AadegUd-z7bJWYsda38XjFZa5s17JKVX0Cd3g1i7wJ3oPIFREUY1N0wj1i5a7S2m6wWLNcerVMmUUHyGnb8xqrixOfP3SstnwLbdEK2MTqqeAX4c2YdYSPuo7NNB5cRhszO_Al8LHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/691179" target="_blank">📅 14:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691178">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجه سابق آمریکا، ادعای ترامپ در مورد «التماس ایران» را مسخره کرد: اگر منظور از التماس شلیک پرتابه‌های بیشتر است، پس روش جالبی برای التماس دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/691178" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691177">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
فرودگاه ریاض هم‌اکنون/ ستون‌های دود از فاصله چند کیلومتری دیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/691177" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691176">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فؤاد ایزدی: انتظار بازگشت آمریکا به تفاهم‌نامه یک خسارت بزرگ است!
کارشناس مسائل آمریکا:
🔹
توافق یا تفاهم با دولت فعلی آمریکا امکان‌پذیر نیست. انتظار برای بازگشت آمریکا به تفاهم‌نامه‌های قبلی یک خسارت بزرگ است و تنها احتمال حملات گسترده‌تر را افزایش می‌دهد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/yRIXrUwC5Xc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/691176" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691175">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاطم شدید در پرواز
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که یک هواپیمای مسافربری را هنگام عبور از تلاطم شدید نشان می‌دهد. در تصاویر، هواپیما به‌شدت تکان می‌خورد و بال آن نیز از داخل پنجره در حال خم‌شدن و نوسان دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/691175" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691174">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_3CyR_YtimBn3cTErAjWWKp1N_Yn7t3oFacIjWKzUB5m2zhwlH-1XTLPbfaYXqSxYGa1SKW-qxZh4UpH5tcrzngLY0yIKOKeLEidk0TMKaNFtLlcOBxu0sYtlujKCqM-Xfrew3xlTVJouUrRs18q4kY6wVq_3VBrn4_VhbTx_HTMYcURM_b9scH0Ct0LZobWkL1afr9jKbyZa8ik-YcytmbcVJlAerCONlbLhbupZUU8h6qPh6B74sBSxctzhoNX_XTgNLwLO4nPIdwDsqqU1cZZ0W9mgWRX3DSbJBGo6edGjGBoJyNAgP6zNfs5z70VBx53J_zNUhuBEwrGpT73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با همین گل‌های‌ ریز می‌تونی جیب‌هات رو خوشگل کنی
🌼
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/691174" target="_blank">📅 14:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691173">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835123f205.mp4?token=Zc-UEeGmdHHPNzvnzguvhkzk2VUFhX6eOPwXX7WxIFt-e5ehc15oaPyGsFGTKolgaiC9D-mz4hxC-pu1cYLg_05aEjgqm27dDCiGLhO1HZjAsh4GzKxkNWwfmsk-fbTQOv-v7qhhujKnAPCFYZPiGH6oCF4yQWij5JKdQwV6xD6H8HDKZzwcBJHkNKsgG95V1Ps5bwCjoWCuaJpXJ0sboNeueWv8KNcmhf4oCWlFOGAsAg4IEVXGExZqnvfL2ukvdaq2jkVXrmPLocPO7kw-vUmG1fIOB1Qn49zyao6rBwzhWwZSJUqK3qMKr2WKSI21EqRYffHheyFVAiQ2oy_mR0fgFAVkHDSE5j96SU-irc3bJvyqNdQeff-Yjhn8X5tN4iY8AXiHUz5fhxHq_nVzlR2HP4yGbn7xr4ls4BRBBV_8Ci70e1pGdB0FN4q62ku5EObdpL1Dew0J8l9IdJ94cZZSCKMcb4Yts4Aj1miPRZkV03xMPLJ7ucyIFVb2foWPTxvPLPc-ICegBLvfdK0m0hxlnbaE7dYj3uDPxoACuWNWley_KxSSYT6ijjJNqBhedr_IgcihE7N-uQ74_Fa_jUejy501jxfhogHSFmMgENwr0uvMteKvC28OSbF5tx-vLqQQZYuxecdbwsIVHY3JQojVSuKrfGeSWhub8G4NuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835123f205.mp4?token=Zc-UEeGmdHHPNzvnzguvhkzk2VUFhX6eOPwXX7WxIFt-e5ehc15oaPyGsFGTKolgaiC9D-mz4hxC-pu1cYLg_05aEjgqm27dDCiGLhO1HZjAsh4GzKxkNWwfmsk-fbTQOv-v7qhhujKnAPCFYZPiGH6oCF4yQWij5JKdQwV6xD6H8HDKZzwcBJHkNKsgG95V1Ps5bwCjoWCuaJpXJ0sboNeueWv8KNcmhf4oCWlFOGAsAg4IEVXGExZqnvfL2ukvdaq2jkVXrmPLocPO7kw-vUmG1fIOB1Qn49zyao6rBwzhWwZSJUqK3qMKr2WKSI21EqRYffHheyFVAiQ2oy_mR0fgFAVkHDSE5j96SU-irc3bJvyqNdQeff-Yjhn8X5tN4iY8AXiHUz5fhxHq_nVzlR2HP4yGbn7xr4ls4BRBBV_8Ci70e1pGdB0FN4q62ku5EObdpL1Dew0J8l9IdJ94cZZSCKMcb4Yts4Aj1miPRZkV03xMPLJ7ucyIFVb2foWPTxvPLPc-ICegBLvfdK0m0hxlnbaE7dYj3uDPxoACuWNWley_KxSSYT6ijjJNqBhedr_IgcihE7N-uQ74_Fa_jUejy501jxfhogHSFmMgENwr0uvMteKvC28OSbF5tx-vLqQQZYuxecdbwsIVHY3JQojVSuKrfGeSWhub8G4NuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رئیس سابق دستگاه اطلاعاتی مصر: واشنگتن در سال ۲۰۱۶ از من خواست تا مقدمات سفر اوباما به تهران و دیدار با رهبر انقلاب را فراهم کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/691173" target="_blank">📅 14:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درخواست وزیر کشور پاکستان از ایران برای جلوگیری از انصارالله یمن
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در رابطه با سفر وزیر کشور پاکستان به ایران بحث‌هایی انجام شده و درخواست‌هایی نیز در رابطه با اینکه ایران از نفوذ خود استفاده کند و مانع فعالیت انصارالله شود مطرح شده است.
🔹
در این رایزنی‌ها قرار است درباره تنگه هرمز و تنگه باب‌المندب نیز گفتگو شود.
🔹
احتمالاً امروز یا فردا مشخص می‌شود که ایران با سفر وزیر کشور پاکستان موافقت کرده است یا خیر.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/691171" target="_blank">📅 14:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be121f01dd.mp4?token=XLWx45X-tp34k2QboFFGihKpXaEtz-qrpt-z3siOcucA_ztLWZWzdTID_94YlVB08ALUaH9mEh5g00VyO3EfkiZRzKnByTFNFu3Xr9f3QgoMoOWgsZxr5z3vWIgfELg7_elpwzk1V85o_wwrN4PFigzHftcxuFxkMVGGeXGuUxFu3mlo_2EWtD2dQiI1ayGkPDhj9GLsAxXMVcg4KkAVdiDkIlly4DugaKOjCjkQ5yfiWjPrfaPuEH1l92NkFCdIShP4Q7N3uaSHV2erMkygBuSghRuh81upK13RJB98aJEVr-na-g1aOTeOKLLZRU-b6FtEjL9u-_lEvgrwHJgJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be121f01dd.mp4?token=XLWx45X-tp34k2QboFFGihKpXaEtz-qrpt-z3siOcucA_ztLWZWzdTID_94YlVB08ALUaH9mEh5g00VyO3EfkiZRzKnByTFNFu3Xr9f3QgoMoOWgsZxr5z3vWIgfELg7_elpwzk1V85o_wwrN4PFigzHftcxuFxkMVGGeXGuUxFu3mlo_2EWtD2dQiI1ayGkPDhj9GLsAxXMVcg4KkAVdiDkIlly4DugaKOjCjkQ5yfiWjPrfaPuEH1l92NkFCdIShP4Q7N3uaSHV2erMkygBuSghRuh81upK13RJB98aJEVr-na-g1aOTeOKLLZRU-b6FtEjL9u-_lEvgrwHJgJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691170" target="_blank">📅 14:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
عراق محدودیت پروازهای غیرنظامی در مناطق غربی این کشور را لغو و حریم هوایی این مناطق را برای پروازهای غیرنظامی بازگشایی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691169" target="_blank">📅 14:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رویترز: تصاویر نشان می‌دهند که شعله‌های آتش و یک ابر بزرگ از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691168" target="_blank">📅 14:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975513a38.mp4?token=INAEw284je6wNZKXQBP50ix129gX6SFrSLzjJwvDNMZqdX0gGbywyYCMNRM_Q9urLM8RE1nN64dTNG9Rbkan9qPx3VqmQF05lCUqDFXo_ZX4RNjzMdifMdD3kI1x1wpRy3qVOKNh8IrUa3t0lGKptpg_j6LGDsI6ZA01evgDGO1mj-rM9Geasg66D7QKWDuYRziEFKeyVt-6Lgxgy6PP6NF13-sVYw7ZGxQiDjnNFzqIjRSA10O7AnnPUSOxHVUt_dz5uVi_H-2Nq87VcNYJt6r9FkAzXIxbLDIf_XJ4mXmpe-PSitdhp-uxznP3s-tFTs1mfolI4kuDAAZx2ERUdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975513a38.mp4?token=INAEw284je6wNZKXQBP50ix129gX6SFrSLzjJwvDNMZqdX0gGbywyYCMNRM_Q9urLM8RE1nN64dTNG9Rbkan9qPx3VqmQF05lCUqDFXo_ZX4RNjzMdifMdD3kI1x1wpRy3qVOKNh8IrUa3t0lGKptpg_j6LGDsI6ZA01evgDGO1mj-rM9Geasg66D7QKWDuYRziEFKeyVt-6Lgxgy6PP6NF13-sVYw7ZGxQiDjnNFzqIjRSA10O7AnnPUSOxHVUt_dz5uVi_H-2Nq87VcNYJt6r9FkAzXIxbLDIf_XJ4mXmpe-PSitdhp-uxznP3s-tFTs1mfolI4kuDAAZx2ERUdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتی ۲۱۱ میلیارد تومانی (۱.۱ میلیون دلار)؛ ساخته‌ شده از شهاب‌سنگ ۵ هزار ساله در آرژانتین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691167" target="_blank">📅 14:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN5yo4cNRzsDYOd4-HFgeKa2J9J1llvq9IbaScUio6Ty6Jjv0_zIcIecguYZr3K3hSbC586CfMmpwNMiY9xMxj08nRphzVLmHLlrKjbx6K3YEw1JhE7oLN6-N3gxtZgJhxAQbPRjia2gHK-S6o1pla-adXk3eiKpF9IGOG1avlF7kfIRrUhXRapU-0cPf3XxVMomuy8GbhnHF3F8OAdkFjMk2RMq_tmmCnSS1ppShujWW-9UV-jxfU6A2sHZrYp6stRYNYY_sVtju3WcX0hKD7_ctLc1ZaMsRJSXaAUs4QkdIIrR8gsklrgmuACrg6NyIFnssWQe0UdqQpZVYg10Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا خبر داد:
رکوردشکنی بانک کشاورزی با ۵.۳ همت سودآوری/ اضافه برداشت از بانک مرکزی صفر شد
🔻
مدیرعامل بانک کشاورزی با اعلام رکورد ۵.۳ همت سوددهی این بانک در سال ۱۴۰۴، این موفقیت را دستاوردی بی سابقه در تاریخ بانک کشاورزی دانست و از افزایش درآمدها، کاهش هزینه‌ها، صفر شدن اضافه برداشت از بانک مرکزی، بهبود قابل توجه شاخص‌های کلیدی و ثبت رکوردهای جدید توسط این بانک خبر داد.
🔻
وهب متقی‌نیا در جلسه مجمع عمومی عادی سالیانه این بانک که با حضور وزیر امور اقتصادی و دارایی برگزار شد، در تشریح عملکرد سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ اظهار داشت: سال گذشته علیرغم چالش ها و بحران ها توانستیم با انضباط مالی و ریل گذاری درست در مسیر گذار از بانکداری سنتی به بانکداری نوین، دستاوردهای چشمگیری را در زمینه جذب منابع سپرده ای، افزایش سهم از بازار منابع بانکی و بهبود شاخص های کلان مالی کسب کنیم.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691166" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
منابع عربی از چند انفجار در نزدیکی فرودگاه ریاض خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691165" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqgZeJ-2D-lKCt3gWjW6S0nDuGg5PTN1a3XJSZYymRp0BiSegT9O8TjoBRl6jRV2fq4WQssag_rnMfDEMj0msaja02645F0HnFxIZqDO5Ek0aOEIMcAAPgLUVSSCQ9eC9_VvKvtMBf7AWiQGTDxZ6unxwwkAB7nu5lSfzpXsiS8MnkHzppWPtNbK-DnEbBnkYkZq8Yi1QJMK9HBQDUjPoONWvEfgrHzVBSanEjLp927JD_ylbjBiQihYs4h1Kh_UXefcTlYXe-i1Q34bQT-07WPmV4N2QFVyHtZt36S7wX5F_QQSZvuLinx1F5nVmNoH7ra_McZubUwudhq7H3adWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: تصاویر نشان می‌دهند که شعله‌های آتش و یک ابر بزرگ از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691164" target="_blank">📅 14:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21558efae.mp4?token=KI3Kr6KOFo93c4zkv-GdV6Imle8h79ZxRpLTROCH1dz2Of77Y6utQ_EOA7QEDfBOES1k04Q82qsBrP6Bcqva0zH3QhZzH11M6ygsjbgTD1a8mtfVGk7OAoar-Hei_ddOtqsIcbApWc3rK312wpAmFG6UaCkqzLJmInZBRsawq2SvILQqm9dA2eZQWSrY7jLnDfEXT34DhNEApXw2EQ-9JYcQ9M91Hy23rH0WBnl6grBD58NHWihvC9R0h9tk_G5ypzBIr9X-GOFMrX-67bPhlqJH-ps1RmIoQeriavDf94BRuTOOOq4FMC9WBCz5vUNjFLp-bikpii-U2SU1N2vcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21558efae.mp4?token=KI3Kr6KOFo93c4zkv-GdV6Imle8h79ZxRpLTROCH1dz2Of77Y6utQ_EOA7QEDfBOES1k04Q82qsBrP6Bcqva0zH3QhZzH11M6ygsjbgTD1a8mtfVGk7OAoar-Hei_ddOtqsIcbApWc3rK312wpAmFG6UaCkqzLJmInZBRsawq2SvILQqm9dA2eZQWSrY7jLnDfEXT34DhNEApXw2EQ-9JYcQ9M91Hy23rH0WBnl6grBD58NHWihvC9R0h9tk_G5ypzBIr9X-GOFMrX-67bPhlqJH-ps1RmIoQeriavDf94BRuTOOOq4FMC9WBCz5vUNjFLp-bikpii-U2SU1N2vcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها اول روی مذاکره و توافق اصرار دارند چون به نظرشان کم‌هزینه است و بعد وارد حوزه فشار و بحران می‌شوند و به عبارتی بحران را جنگ می‌دانند
🔹
آرزوی آمریکایی‌ها این است که ایران را به سمت تجزیه، تسلیم و براندازی ببرند.
🇮🇷
…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691162" target="_blank">📅 14:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241bc7b57f.mp4?token=kdHIq_m0eq3-wf9Bv76UHAZ5LndTvWZFWuSPNt9nS7RSjFfh-YjLyU6USF7TE5tsOY7L_sZi8GD0rqM_Janu8KhbNIxrcvyoO-0ztJpLrDbbGQ2Yh1N27l_2g_n2mfwQUXuIwidDfOuczsytBn9KJ1rkC3nIgbJP1MvrCwkvL4CVREbSvhlb83iE4SwPnQQ06OGoYpnueJR-lNkWRnjuOLvcUlh32gaipKnOQAnmWCxY9YAMZXuq2o-LY7Y0BLCR4ceJrOWKK7G-40aWycUixMyfNkcvHBQiA7BR3pdIPt4nhsQSF7U0IXgYLXgGynOg-pzUuV1mALoMaHHHa6QxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241bc7b57f.mp4?token=kdHIq_m0eq3-wf9Bv76UHAZ5LndTvWZFWuSPNt9nS7RSjFfh-YjLyU6USF7TE5tsOY7L_sZi8GD0rqM_Janu8KhbNIxrcvyoO-0ztJpLrDbbGQ2Yh1N27l_2g_n2mfwQUXuIwidDfOuczsytBn9KJ1rkC3nIgbJP1MvrCwkvL4CVREbSvhlb83iE4SwPnQQ06OGoYpnueJR-lNkWRnjuOLvcUlh32gaipKnOQAnmWCxY9YAMZXuq2o-LY7Y0BLCR4ceJrOWKK7G-40aWycUixMyfNkcvHBQiA7BR3pdIPt4nhsQSF7U0IXgYLXgGynOg-pzUuV1mALoMaHHHa6QxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقاشی عجیب ۷۵ ساله؛ اثری که در بیمارستان روانی تبریز خلق شد
😳
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691161" target="_blank">📅 14:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e48bb36d3.mp4?token=CEuSiQAaRmbsh5xZlQsKzM6xO79yS61Hwt5SzVmUz0lWDZgXWkFRUnJ0lIc1rOX0_ithr68tHtATOczUXMvwpvdDlqRZIeD2yJZUcsFOojXMceAwy42PXIAXgIOBvQCIWgOpBrhUEWCn7nnAUu9zW0yMo9ulYmdNI8INxd0DdwqSMys1_LVm76yjlk2tq3jLgHlFq8sdj-TokaPancu3-yy-yHYSkelQwE-3JMJUSL7OZKfLfY1O8LG-hgMpdhcubv1SfiTR7z7_ib0PxtsSxAHtXaiHSzn7hlmsGGbYYVwlQVeUMKoBD1tihr3xW8SQ05heZTcror7NG6oK3mT_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e48bb36d3.mp4?token=CEuSiQAaRmbsh5xZlQsKzM6xO79yS61Hwt5SzVmUz0lWDZgXWkFRUnJ0lIc1rOX0_ithr68tHtATOczUXMvwpvdDlqRZIeD2yJZUcsFOojXMceAwy42PXIAXgIOBvQCIWgOpBrhUEWCn7nnAUu9zW0yMo9ulYmdNI8INxd0DdwqSMys1_LVm76yjlk2tq3jLgHlFq8sdj-TokaPancu3-yy-yHYSkelQwE-3JMJUSL7OZKfLfY1O8LG-hgMpdhcubv1SfiTR7z7_ib0PxtsSxAHtXaiHSzn7hlmsGGbYYVwlQVeUMKoBD1tihr3xW8SQ05heZTcror7NG6oK3mT_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عوامل درگیری و قدرت‌نمایی خیابانی در چالوس بازداشت شدند
رئیس کل دادگستری استان مازندران:
‌
🔹
در پی وقوع یک درگیری خیابانی و قدرت‌نمایی در شهرستان چالوس که منجر به اخلال در نظم عمومی شده بود و با انتشار فیلم در فضای مجازی امنیت عمومی و روانی شهروندان نیز خدشه‌دار شده بود، موضوع در دستور کار قضایی قرار گرفت و عوامل این درگیری شناسایی و دستگیر شدند.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691159" target="_blank">📅 14:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها اول روی مذاکره و توافق اصرار دارند چون به نظرشان کم‌هزینه است و بعد وارد حوزه فشار و بحران می‌شوند و به عبارتی بحران را جنگ می‌دانند
🔹
آرزوی آمریکایی‌ها این است که ایران را به سمت تجزیه، تسلیم و براندازی ببرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691158" target="_blank">📅 14:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691157">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJOeocpr1vE6Iv5KYt8qpxJD9wfQGM-X9LLN7phnRUGMLc43HbqoI1iQn3JtOCyZV6ppxdtJTCnAit0rmeXUrKCB5eT9IyXl4aCvU50hVUbMx0q8SxDk4AXlI3PebGmvIC95fzPJSGc9qJf8_gd36J571JOMpeVFSBrHj4Y8ebRwVx8WRcIc8Y1GDFBv31uwxYGbcHJ_JjuePg1XUjsTOZrXnWsMNEJXPA7ucSVm7AyOIekI1ockwjkTwc1VOIeKvlduH23EljX-tidW6TgbjPFhVEd19rNIPaYbyF5HIk6LMv5KWmCOwxjrVZ87pyoJaLKQpBgRP3nUFo-rcJTy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنهایی چیست؟
روایت‌های متفاوت از یک حس مشترک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691157" target="_blank">📅 13:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691156" target="_blank">📅 13:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b00b674dd.mp4?token=iR3WunQewpsXDMTJFNXIMWXEIRuwuZnM2yQBQnCoqK285n1DMeeO3LFPfgaNRAW3sS2O1ByRrZHUoNYiM7eXvVwi2dLXFNsBmcWBjqK2UY2Y-Wuf0ZbMcTION7GjCgQxig4GWYUqYpI3_Aus_u_uffGGwHSoQMVO_dJ8xBqVeuSNUuKKhbwVGSZCQyG7ZUQO0igT9LGJzFkaXQaUy460tqLvg53gvRGwqAzywIMPVlQO6uEn2-Udb0KBne67pOUgWkBgWyieb0lVAjVz5xXVZmt-WUsUnp0hqWDaLklCZ1_aKKzuYtyZoU1jetzhjotvTGq7EZ_kkLh_npx99WNDq5xdqxmRJ1b-E1U8Qltsw1Isge-ejdXY1wQdh4_JZktKg49B1MBsFc8mFCEEF8JyfW9t83VaXI3VIQySXNLfvb5n4RarXOuKHgfMz5PsgbPlUjWjXK_wKx4gYvA8KU-05BFlA0sdQfpg8Q6Aisr_co0R85SBJaFBTaLHcFryS27ZINj2WzNgVoOyFXdvChR-CstM_xsolZqAOjGTqOyAiI2eVmSK4aFCvKG0FQ1KY6vWv2uUo3pxa1bTeE9L-r-JIv-MRvz0q5dD8ZAkK04Ghq3nZ2cy6c5QhiGmZqIRXtyHL0_R9vABsmz84neDy8iGiZ3iLvJorqawjHlH0ad4p5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b00b674dd.mp4?token=iR3WunQewpsXDMTJFNXIMWXEIRuwuZnM2yQBQnCoqK285n1DMeeO3LFPfgaNRAW3sS2O1ByRrZHUoNYiM7eXvVwi2dLXFNsBmcWBjqK2UY2Y-Wuf0ZbMcTION7GjCgQxig4GWYUqYpI3_Aus_u_uffGGwHSoQMVO_dJ8xBqVeuSNUuKKhbwVGSZCQyG7ZUQO0igT9LGJzFkaXQaUy460tqLvg53gvRGwqAzywIMPVlQO6uEn2-Udb0KBne67pOUgWkBgWyieb0lVAjVz5xXVZmt-WUsUnp0hqWDaLklCZ1_aKKzuYtyZoU1jetzhjotvTGq7EZ_kkLh_npx99WNDq5xdqxmRJ1b-E1U8Qltsw1Isge-ejdXY1wQdh4_JZktKg49B1MBsFc8mFCEEF8JyfW9t83VaXI3VIQySXNLfvb5n4RarXOuKHgfMz5PsgbPlUjWjXK_wKx4gYvA8KU-05BFlA0sdQfpg8Q6Aisr_co0R85SBJaFBTaLHcFryS27ZINj2WzNgVoOyFXdvChR-CstM_xsolZqAOjGTqOyAiI2eVmSK4aFCvKG0FQ1KY6vWv2uUo3pxa1bTeE9L-r-JIv-MRvz0q5dD8ZAkK04Ghq3nZ2cy6c5QhiGmZqIRXtyHL0_R9vABsmz84neDy8iGiZ3iLvJorqawjHlH0ad4p5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از رؤیای شهر آینده نئوم تا حراج تجهیزات؛ شکست بزرگ قلب چشم‌انداز ۲۰۳۰ عربستان
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/691155" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رئیس سازمان پزشکی قانونی کشور: هیچ پیکر شناسایی‌ نشده‌ای از شهدای جنگ در پزشکی قانونی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/691154" target="_blank">📅 13:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4156983d65.mp4?token=stSTOD6clEToGrRY4SRemS-Ohxmsj0QpPy6dEhYTmsm68z1LKe6UNv8c-vUKA-VlnaVKSV3B_k9eWFck2NQc7mD-UeW7-hH5_UG7J5jxCZhSACdhQyjHRoGKXHqlAOMEIWX0_6BDPiPjKCtJcy7iJizaTcmz8fMjukR3jHqiIOEQmMyFwcqk_M7qt1c-I12vtKeHck-_6UXO2fbgTSBvtSgqNHMdvKnhIliTjGy-TWAahlx168WWU4ig0UxhcdJFPuKwkiN3R8QmRhLczDjn2LVZb0UTdDGkZUk6rEW4LAarIcuoEW-YM1BHwSqBsYx-6jd8EFRtGHX78RgDy7aDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4156983d65.mp4?token=stSTOD6clEToGrRY4SRemS-Ohxmsj0QpPy6dEhYTmsm68z1LKe6UNv8c-vUKA-VlnaVKSV3B_k9eWFck2NQc7mD-UeW7-hH5_UG7J5jxCZhSACdhQyjHRoGKXHqlAOMEIWX0_6BDPiPjKCtJcy7iJizaTcmz8fMjukR3jHqiIOEQmMyFwcqk_M7qt1c-I12vtKeHck-_6UXO2fbgTSBvtSgqNHMdvKnhIliTjGy-TWAahlx168WWU4ig0UxhcdJFPuKwkiN3R8QmRhLczDjn2LVZb0UTdDGkZUk6rEW4LAarIcuoEW-YM1BHwSqBsYx-6jd8EFRtGHX78RgDy7aDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابزار Claude Code Projects برای مدیریت پروژه‌های طولانی برنامه‌نویسی معرفی شد
🔹
این ابزار می‌تواند دستورهای متنی کاربر را دریافت و آن‌ها را به چند رشته کاری موازی تبدیل کند. تمام شاخه‌ها به یک حافظه اشتراکی متصل هستند و تغییرات و تصمیمات مهم در سراسر فرایند توسعه نگهداری می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691153" target="_blank">📅 13:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
عراقچی: جنگ، تحریم و زور نباید به ابزارهای عادی سیاست تبدیل شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/691152" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e33fef086.mp4?token=pcXheaUVE2EoS8jhY7gqhN2qZItlcx0M-t-iFOUaRtLTQj37ANfrWMbP1E6dXp8JPDn9f8ldnTNNqVPmAaXRZ32Tn-MjAwgMRCO0fCYtSJtTyKTkhUDnv8XoLE2gsT-LOK3_yilrFXVArcHo-t9Jn808j2nqGzAQbGNqaN05zz7TgG_fZiAMqVdNQCRGUG7D41QmOY5g06zA2Cqm9HqmaXpYY3HTT385NrINR3Hletn14RG8P_xroj3M-7aCUI8xthJndFJUrbp7BnNZcbNouFCxtpqc4t0lDwDuH6oVvUIv0BxBiMKEvrB3UHBJbd9p4qkdWp4uQa7oYuT3jfe6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e33fef086.mp4?token=pcXheaUVE2EoS8jhY7gqhN2qZItlcx0M-t-iFOUaRtLTQj37ANfrWMbP1E6dXp8JPDn9f8ldnTNNqVPmAaXRZ32Tn-MjAwgMRCO0fCYtSJtTyKTkhUDnv8XoLE2gsT-LOK3_yilrFXVArcHo-t9Jn808j2nqGzAQbGNqaN05zz7TgG_fZiAMqVdNQCRGUG7D41QmOY5g06zA2Cqm9HqmaXpYY3HTT385NrINR3Hletn14RG8P_xroj3M-7aCUI8xthJndFJUrbp7BnNZcbNouFCxtpqc4t0lDwDuH6oVvUIv0BxBiMKEvrB3UHBJbd9p4qkdWp4uQa7oYuT3jfe6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب دوربین روی لاک‌پشت، سفری دیدنی به اعماق آب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691151" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVmN_IjMV7HFMMyIsDu4X4C65fsnMiqczNvkCqgv7xGwAUifjm6gLIjuK0ZKKFJ5bwvMidQoQ25PeCZkUzWQq4IifDMFDE0rQRWYbcbxJwPaoNy-Wu5hxUUVjK97CVLfmbQosOmDFwSaWZQMe2mh-WxegqrFG1YdIAH1jOfDk9QXBoPl2tFzjjwGGWfk_cfhDUWMGV_T6G_aZ6D_jtCDt3w1f0Lvs8E6Lg_47kJ8PfGoW1HNLurIhYVtfHM0_ly-u-LKIHG83dZjsaBDL9pfnqczi4jHIZM38Ozrm9bO6qQWCRTklrgQGAdyQRMNPN0sidJW2I03ot-MD-NUFkoTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ شهریور ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
همگام با پیشروی دلار به کانال ۲۲۸ هزار تومان، بازارهای طلا و سکه نیز مسیر صعودی را در پیش گرفتند.
🔹
امروز هر گرم طلای ۱۸ عیار با رشد قیمت به ۲۳ میلیون و ۷۴۶ هزار تومان رسید و سکه بهار آزادی با نیز، به قیمت ۲۳۲ میلیون و ۱۶۰ هزار تومان معامله شد؛ روندی که نشان از بازگشت تقاضا به بازارهای دارایی دارد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/691150" target="_blank">📅 13:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf41d4a0d.mp4?token=WtlLb2bm18oxYQgfC7Ds_eaY3fVSoBloo6Y-UtGs6zP0E-uwjKiQdEm2kyU_pX_OqRILLN0JPLzKTxVRf5zp4Fl2n2D6EmUzRaUTOktjnQYBqs-qgcDglMHL9Mw9TyjCMnC698j3LXcacJzlPCFR0OrWLyIU8cWgW1-NfPPYvPwahrXl6NxBYGUWq9Jqu2Rxo6Fwu9UIlXAopiDwkxTg3kJtKGuCoQChxYX8bZ190h3ZlUIPJ3p4zxIWMs7k51mni-bgGFeYBZFU-mSDKf3PF4dGSGzT4_dPVBVse56wttPTaenM86Y0OGHKclWE17I02zpIX6kwLJFgAWhRMl5yJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf41d4a0d.mp4?token=WtlLb2bm18oxYQgfC7Ds_eaY3fVSoBloo6Y-UtGs6zP0E-uwjKiQdEm2kyU_pX_OqRILLN0JPLzKTxVRf5zp4Fl2n2D6EmUzRaUTOktjnQYBqs-qgcDglMHL9Mw9TyjCMnC698j3LXcacJzlPCFR0OrWLyIU8cWgW1-NfPPYvPwahrXl6NxBYGUWq9Jqu2Rxo6Fwu9UIlXAopiDwkxTg3kJtKGuCoQChxYX8bZ190h3ZlUIPJ3p4zxIWMs7k51mni-bgGFeYBZFU-mSDKf3PF4dGSGzT4_dPVBVse56wttPTaenM86Y0OGHKclWE17I02zpIX6kwLJFgAWhRMl5yJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فردی شبیه به آیت‌الله خمینی در یکی از تجمعات شبانه قم؛ فیلمی که مورد توجه قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691149" target="_blank">📅 13:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5119c00ae5.mp4?token=PXVyhKeHWPtD6MJYrHGuJRxa4xx8umNy7P172f5L-q952JGrrQggecAEeNcRpJ8fbUIQgbmrgO9WHEJbi4kGXAVG-N2QR_xwaac3t_KKPO10lhzZ6y69y1PPr90n6DBKdAnd6FCWa9mhI7Ebk1k6XjRSbOM89DggzIu3l2wMfpNk4zauVuw1WBM40PEUy0PNIW49qcxXLMaB3p3j8lrpsQaImDDrrIns3obtzsAal-UIS3PZ47DKQCgrmMYM-WDw0kN-_0C486vqIkGTzCnrSGMRuLsShf2ux0caTLdfM1M6BEYcD0QWJQJCEDzRnmUxA7ihGAhr_qakVHC0OK8_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5119c00ae5.mp4?token=PXVyhKeHWPtD6MJYrHGuJRxa4xx8umNy7P172f5L-q952JGrrQggecAEeNcRpJ8fbUIQgbmrgO9WHEJbi4kGXAVG-N2QR_xwaac3t_KKPO10lhzZ6y69y1PPr90n6DBKdAnd6FCWa9mhI7Ebk1k6XjRSbOM89DggzIu3l2wMfpNk4zauVuw1WBM40PEUy0PNIW49qcxXLMaB3p3j8lrpsQaImDDrrIns3obtzsAal-UIS3PZ47DKQCgrmMYM-WDw0kN-_0C486vqIkGTzCnrSGMRuLsShf2ux0caTLdfM1M6BEYcD0QWJQJCEDzRnmUxA7ihGAhr_qakVHC0OK8_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691148" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f660c917.mp4?token=MOGGnwb3LV_FrR4D-1Auf1KyzDNyMZj2oyvN0MoPaSekZ7OSVMyCrq4X3-r6kA9m2k9JeQB9NGXfXXKLyLCceqYDmpcHWzS7pI5zFDYcT-fp3maqtXkjWfzhYKWD9kH26cm6mJWSRencFHE7U1W5Mkiqq-RjtSDuXZ0ocXztFCOCeK8XTQPB79KAolNWgfyOSg6HDTakNL1zo0wwFwRJFUT__eKv24yEPeelJTq4Q-eM9TLJ2ydmELOXVs6kgNgoGzfQaCuZaiVVnBOM0A9u5SSqoVR5GBg_q5fdUnp_I4UFf1o2x2eZyVMOk_zaGG0eJ1r2vmmMo2XetmAVclf8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f660c917.mp4?token=MOGGnwb3LV_FrR4D-1Auf1KyzDNyMZj2oyvN0MoPaSekZ7OSVMyCrq4X3-r6kA9m2k9JeQB9NGXfXXKLyLCceqYDmpcHWzS7pI5zFDYcT-fp3maqtXkjWfzhYKWD9kH26cm6mJWSRencFHE7U1W5Mkiqq-RjtSDuXZ0ocXztFCOCeK8XTQPB79KAolNWgfyOSg6HDTakNL1zo0wwFwRJFUT__eKv24yEPeelJTq4Q-eM9TLJ2ydmELOXVs6kgNgoGzfQaCuZaiVVnBOM0A9u5SSqoVR5GBg_q5fdUnp_I4UFf1o2x2eZyVMOk_zaGG0eJ1r2vmmMo2XetmAVclf8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی دیپلمات آمریکایی درباره آینده ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/691147" target="_blank">📅 13:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: میانجیگری کشورهای مختلف از جمله پاکستان تعطیل نشده و همچنان در حال انجام است/ حرف ما هم روشن است دشمن باید به تفاهمی که امضاء کرده بازگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691146" target="_blank">📅 13:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691144">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a9b5c0f.mp4?token=kbWn1886bcSzIf__5WaHISviUDb4rHqpUjGRoGYX1_pwxthL3qSKEza-F61dUaw0qNHQD5IFAKxEd7QUFTEfCONweLKUOnrzBnHB_2bdIw8TJrJUccsNrH7E5vpb56dNoys0W0dHJAZBsVvL2Yf0JZ6g6XD2Iw3rd_7d61bgLgoREAb_mO4MXder5wLaBqTpJzNQfoueCE-3nxFXrhn2WB-1eO8qtyFs_03__AEUdQN4_HEz4Benxqxw8JiZ-Yy3eEaOZ6IE3uJIi9bW6v2RbsQn2iTN71thP75K-THY-p2h11TlJYNCdcZ1awDftb8wCi7H76grTR0Fa2COPjGbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a9b5c0f.mp4?token=kbWn1886bcSzIf__5WaHISviUDb4rHqpUjGRoGYX1_pwxthL3qSKEza-F61dUaw0qNHQD5IFAKxEd7QUFTEfCONweLKUOnrzBnHB_2bdIw8TJrJUccsNrH7E5vpb56dNoys0W0dHJAZBsVvL2Yf0JZ6g6XD2Iw3rd_7d61bgLgoREAb_mO4MXder5wLaBqTpJzNQfoueCE-3nxFXrhn2WB-1eO8qtyFs_03__AEUdQN4_HEz4Benxqxw8JiZ-Yy3eEaOZ6IE3uJIi9bW6v2RbsQn2iTN71thP75K-THY-p2h11TlJYNCdcZ1awDftb8wCi7H76grTR0Fa2COPjGbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین
روش‌ برای تشخیص مکمل‌های تقلبی و اصلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/691144" target="_blank">📅 12:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691143">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رسانه فرانسوی: موساد تلفن همراه مشاور ریاست‌جمهوری فرانسه را هک کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/691143" target="_blank">📅 12:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691142">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GteM3y8sq6nlo5eqeHTiba5XIm4WpHnAHFqKmpXBFFS6jgCXyAcBnPWm2xwq981qBivZVpIiFcszzOQgGitMM11Bi8m8X5536JPsTwhA2U1OfJ18HwwTX9PE8wqOq8WqZroCuc02lvYrXeiFnJEews5wUs6UydlGN-_0D0ut-9Az91qePEB_XTczITQEnXo6_rJr1NgA49gXslLSWFu9cT9VdBB4JJzarod5n9V_ea18xThOr1oR6rjPG4KT72YT5pte2DIVAtwhJoIE1MxjE3QQj98-AVlhx3F0wi7C7-YipzqwbExm53w5Tbue-0G3nWpThRVhujxZDuvQ5ejSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه ABC News: هزینه هر باک بنزین شورلت در آمریکا پیش از وقوع جنگ ۸۲ دلار بود و در حال حاضر به ۱۲۵ دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/691142" target="_blank">📅 12:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691141">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
الاخبار: مصر درخواست عربستان برای اعزام نیرو به یمن را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691141" target="_blank">📅 12:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuiBjD-uZXLkTfQkBtFYCixDxIChWQ_bJr_pGD4qVUmmyz5EzN7tEbX8rtV35IaVBFw4SLJuaPhPveHxIevNLn4FBA3nOIQaKbq9uZZ0hVMUJ-4l1lKXvT7_Y2fEVoOpFfbzGese_RMHaQKaah72duk5oR-FqGq70X3E5ZUz4VBx5qNYiaqSt1Y6tTq4sTxB_Xe9yd8Egydus6SuvyuOaMUAg3vIWbyQw-i0ExouEEEkMjgOR9iUwtptS1DcM6jPzugYIKpydTLk3eMTH7JPsNryZwWnsDqEU40ASi9eX1g07I-McPMHWKC92XhHotsBAzkht_42E5g1rQ7AcaUz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری بلومبرگ درباره حمله فاجعه‌بار آمریکا علیه مدرسه میناب
🔹
بلومبرگ به نقل از مسئولان شرکت کننده در تحقیقات داخلی وزارت جنگ آمریکا (پنتاگون) فاش کرد، برخی از کارمندان پنتاگون طی نخستین ساعات حمله آمریکا به مدرسه میناب ایران متوجه شدند که این توسط واشنگتن صورت گرفته است.
🔹
تحقیقات صورت گرفته نشان می‌دهد حمله مذکور نتیجه تنها یک تصمیم فاجعه بار نبود بلکه برآمده از سلسله تصمیمات و اشتباهات و فرصت‌های از دست رفته بوده که می‌توانست مانع این حمله شود.
🔹
کمبود وقت در تثبیت اهداف مورد نظر و اطلاعات ناقص و تکیه بیش از حد بر هوش مصنوعی در وقوع این اشتباه نقش داشته است. این منطقه در داده‌های آمریکا به عنوان یک منطقه نظامی نشان داده می‌شد این در حالی است که تصاویر ماهواره‌ای نشان می‌داد در منطقه مذکور از سال‌ها قبل مدرسه ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691140" target="_blank">📅 12:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffefffeb8.mp4?token=NnwJLTc7B6hgwBY_WYpm1putNfn3wvqgVN7nyUpRNUUtItlDF2SIg09lClMLZCtQ469uP2DKu_lIPeSCeox1T3H-B58cXtqTHKc3BOwAz0AZiZz78whHlsgSUcH2BvCSIwx9lL51jQsrE7hO8D5iF5W61cPQStJdPCtWfALRWvPsPo6UquLkt_hV5uNhEv6AeQQqAhJSBulpZpM0Tu0Nh_NOKOi3-reyB7MUjvBoBCF0tcXzApwhezaF9WZkWYeCxKqyc9-Y39ANu49fht-rVufaw6Vgyg8S1cDu6e1VTYGo1vamJ1SZ30Ii4T_VHR_dTaZGPJpPbPTSAjHNHLSGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffefffeb8.mp4?token=NnwJLTc7B6hgwBY_WYpm1putNfn3wvqgVN7nyUpRNUUtItlDF2SIg09lClMLZCtQ469uP2DKu_lIPeSCeox1T3H-B58cXtqTHKc3BOwAz0AZiZz78whHlsgSUcH2BvCSIwx9lL51jQsrE7hO8D5iF5W61cPQStJdPCtWfALRWvPsPo6UquLkt_hV5uNhEv6AeQQqAhJSBulpZpM0Tu0Nh_NOKOi3-reyB7MUjvBoBCF0tcXzApwhezaF9WZkWYeCxKqyc9-Y39ANu49fht-rVufaw6Vgyg8S1cDu6e1VTYGo1vamJ1SZ30Ii4T_VHR_dTaZGPJpPbPTSAjHNHLSGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه محل برگزاری مراسم افتتاحیه بازی‌های آسیایی و صندلی‌های خالی هنگام شروع مراسم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/691138" target="_blank">📅 12:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عضو ارشد انصارالله: کشتیرانی در باب‌المندب و دریای سرخ به صورت عادی و بدون هیچ مانعی در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691137" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c79a75a.mp4?token=Vp0drqYlDPfMB2f74kTDRrbScK70pOh36nm6D1rPkPnegmQ64SKkAYD7oVNzMvcuupr3TCaa-pXF5s9iTv5ojfiMQJV_OHF8RW-QGi3WVmu6pFCZr5xqCJmdE9VRO91HgUD4tDrkBLDMbu6aUZNl573zPvQM8f6YC8ED2c8FGNu-ueqFI7PCLizDgLyJUwF8PcsvQx03OB6GhcpKo0Hkr7ORAQp9OCyPuJkD3No0qCCm1a3ftqetQXZtirirZBdo1za2UhsjVAagLACIZ4vZTeJXcMwTTgwIjn-hUAWet8vNuQVhofJxuClL7ZjrJ10PpaQhgWn9egIqkuEcGkCY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c79a75a.mp4?token=Vp0drqYlDPfMB2f74kTDRrbScK70pOh36nm6D1rPkPnegmQ64SKkAYD7oVNzMvcuupr3TCaa-pXF5s9iTv5ojfiMQJV_OHF8RW-QGi3WVmu6pFCZr5xqCJmdE9VRO91HgUD4tDrkBLDMbu6aUZNl573zPvQM8f6YC8ED2c8FGNu-ueqFI7PCLizDgLyJUwF8PcsvQx03OB6GhcpKo0Hkr7ORAQp9OCyPuJkD3No0qCCm1a3ftqetQXZtirirZBdo1za2UhsjVAagLACIZ4vZTeJXcMwTTgwIjn-hUAWet8vNuQVhofJxuClL7ZjrJ10PpaQhgWn9egIqkuEcGkCY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اضطراب چه زمانی می‌تونه مشکل‌ساز بشه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691136" target="_blank">📅 12:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04455021b6.mp4?token=AhZ3raaUAOwlVgZ49DkH-GipiNWrWMG6bQgmsHQ4pFnVc1EIrrX33nJ1o1sOvSF-kJBL8-QeGb2VWsCLlOEgev934qyoEnCrzyM3I2UMjofYK-wBtA-ahCoPnHdPU6WgPY1AUnao5Pplx0AliCSXp-q2W74OxZNw4MAl8Uw8Sy57csBbeXG4I0I9784mzvfC-78dn22VJCPA_-K_JidQdaECzS5vYvVwaefcDDkcqyTNafPhgxZzomXl2Xcrx5oBq6ydlRabCBHiRNganesg4AIDsvzmvdOtEFIBpRM3wD8KxFtDf4JnLeA2GJk9FMM5XLGo8UGPiy7iRadSUtyJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04455021b6.mp4?token=AhZ3raaUAOwlVgZ49DkH-GipiNWrWMG6bQgmsHQ4pFnVc1EIrrX33nJ1o1sOvSF-kJBL8-QeGb2VWsCLlOEgev934qyoEnCrzyM3I2UMjofYK-wBtA-ahCoPnHdPU6WgPY1AUnao5Pplx0AliCSXp-q2W74OxZNw4MAl8Uw8Sy57csBbeXG4I0I9784mzvfC-78dn22VJCPA_-K_JidQdaECzS5vYvVwaefcDDkcqyTNafPhgxZzomXl2Xcrx5oBq6ydlRabCBHiRNganesg4AIDsvzmvdOtEFIBpRM3wD8KxFtDf4JnLeA2GJk9FMM5XLGo8UGPiy7iRadSUtyJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر کره جنوبی «سلطان قلب‌ها» را خواند!
🔹
سفیر کره جنوبی به مناسبت شصت‌وچهارمین سالگرد برقراری روابط دیپلماتیک میان ایران و کره جنوبی، به همراه تیم ارکستر، ترانه‌ای فارسی خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/691135" target="_blank">📅 12:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نفت ۱۳۰ دلار شد
🔹
در حالی که قیمت‌های مرجع نفت در محدوده ۱۰۰ الی ۱۰۸ دلار معامله می‌شود، صادرکنندگان فرآورده‌های نفتی از رسیدن قیمت فیزیکی طلای سیاه به بیش از ۱۳۰ دلار خبر می‌دهند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/691134" target="_blank">📅 12:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691129">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyB_eiACycE7--o6Ukx8jWCViSBEc1MsYtDJsM9BOCkrPAf-ruIi6c94iImZUUuFyuZMbWhvliMM37iVm9fcKCaALKk1PLw7caZevVsivHjNCrGmO8uIbfjcBYaiLBZ-VgSFt2vnRvLV5PDEFbHFSVa3yaZQ4kpy4V82kqyklEiPD2zGErPEl_L5KEztnhrC2cDnsVR735PzP15Kux_vBq8yJHmZ9y8f8Z52eBZ47sJgUI_Kt5l8tJY9wOWy13gY1TUeOLL6l8Gn7ShmJg-sAqgBTXMCPZiFMWap-zMm9Z3k9aws-CQ_ZViQYK0_HPhyS4Mtj3d-HO0-1mZWiiHqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEdmX3YoeYnzGz40iCIC3KxuJRRwcyCagunPA66zFqWTIJP_Z1AqwnNljV-hywArwI6FSf2PIGss2HkRGWQpOee_yXCxYXu6tJ-Hnzzw8OL249rtfN_KUZWMROOjUdPfM9uq4PHoEAReBn7RcD-zcdbGqeCh-cwGmkAqUiRiASh7HPYo-DvDP5XMcYAOksL5bfa8O5NhYNP8Akn56SYHgTAFiY622SV-XjnJIgLi_MleUcIk2G0dH4uxSOZhYbcXvVzHldYaGc9Y5P1VKUqgUBp8dyDlpBWSyU_mA1fE8u4ZS5yUzB5j40c9BmlBIQPtbuFUWZ1Bx3ZEApQ33mLSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzHFZhb7z_7mNQ5yAJJwJy2Jgq6LlQStY7GoAjrJCMZdu7RWGYpDZ_CybgtTGm53rNnA7blQmhTno0gLfCSTSR8l4Dces4dHraqIFi7RNEJJKWSPdBE3ojDGebmydCDlDWgUUFXcBIljH4LvedDt5mBDfl-ZZP-CNbsEmAadPHprWarnp4kJsL9Qkz-xX6ATTjIKq2i9Y3ffsr7P0es1YM7h1PV4d29N48zcvHk-ZDFpuNp68hVx7BD4j28U8ZudiX6r7QNkx0pzbRRnuxKZ8c3N4TNSBPuQlnP8im2moQmeZD3ETDnkzZ_XYNi37-waeAHLtGFtrUS6LvnTJWKZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtVTCykOfYg_Pkxx9TneJ8tHEH9Clg1MGpBzRF8ZQU4nei-cwI3eSgub8jmkjOh2h-J6etsBlRWn8FQjxxRew_vbctADfOayuMxNRyyN-uDp_9IZLnvEIWfni9Q5kCs6SMj8knVVdlDsREv_Zpk_Y7E_N6tlWgWEbn19y01JXcbSBicViZjBmrQRIu_mrv0DxO38K_2DcrFd3hmqJsQIk_PQbDUoeDe2TNlX8owum_KA7w_xfrlwWQH0IVcyQLvaSRaVlxYiKtG5XILO2Ma9gAEJZj4tWEg4XgudlcvJfL1wnx1XMNXz7O04SRMJCKlAUHXvp81hAy2LbQLh6ddpew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsHfR9WYZzaVKwKgAY6Lir-PSIb9hwWgJl0jkAlkKUcAnq7-K0n1yCF9khfiuer4RcLuG4wnIJQiE-RyUdTmb-tJw5_r8W3MAl5-X3kgagm4pQDAucC-uhtQE51Pen5yTs6qra-Z0r09E4tfimDaA_NsyHlN4WDszJZ00n7PFl3S0QhmsGxwq-UmASjc4yWNcBNT3wku4ZVb49A-WxmreTYvVaIWciwbb_w7wmYirWkMVz9gIIAQ4hi0MFE_MjQHxFcfKndJowMaXwvWB1x7uGb898s4a24-YRMNmWeWcppxWYgflAG82FWCjz8p4gLkMRC5g0M_aFCSZp8R7Bngzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراری ۸۱۲ منصوری، خودرو تبلیغاتی جدید پلیس دبی
🔹
پلیس دبی یک فراری ۸۱۲ منصوری ۸۰۰ اسب‌بخار به ناوگان گشت توریستی خود اضافه کرد.
🔹
هدف: جلب توجه گردشگران، نه تعقیب مجرمان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/691129" target="_blank">📅 12:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691128">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228e62cfa8.mp4?token=edSsK972uNgRvV4GWDf-nr-cLfImN-0i56XBKkecfsbJ_BzpkVFx6w7DLCaukbKeBNC2k26tudX2NxuicHob5pwT2Pkw1FDCd46cPlVnpI3xzeYGxYvjgPXAIOcsl6o9_C7SM0oxqTLEZKMR2k3owoyQ9fxs-GqN9alKdafGLb2ZecZCNvty574mStzpCfDUXDhJdd-jm5fjxzvH8FTO2xTumW3pUOqyyP1XAHWWZ47NsDJHaXy3jlQwuO3IawHFJpHwkCTWCJyhFmopXFf9aFhhIOpfYW_vv5Ggr3Q_cxlyfovsXHwg9Jf8yZeYThEs97GRiY2kZCmVyFtbqVsc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228e62cfa8.mp4?token=edSsK972uNgRvV4GWDf-nr-cLfImN-0i56XBKkecfsbJ_BzpkVFx6w7DLCaukbKeBNC2k26tudX2NxuicHob5pwT2Pkw1FDCd46cPlVnpI3xzeYGxYvjgPXAIOcsl6o9_C7SM0oxqTLEZKMR2k3owoyQ9fxs-GqN9alKdafGLb2ZecZCNvty574mStzpCfDUXDhJdd-jm5fjxzvH8FTO2xTumW3pUOqyyP1XAHWWZ47NsDJHaXy3jlQwuO3IawHFJpHwkCTWCJyhFmopXFf9aFhhIOpfYW_vv5Ggr3Q_cxlyfovsXHwg9Jf8yZeYThEs97GRiY2kZCmVyFtbqVsc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: هرکس پلیس بکُشد باید اعدام شود
🔹
اگر انتخابات را ببازیم استیضاح می‌شوم
🔹
مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، کشته‌های پلیس حین خدمت به پایین‌ترین سطح در ۸٠ سال گذشته رسید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691128" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آغاز واریز حقوق شهریور بازنشستگان لشکری بدون معوقه  فعال صنفی بازنشستگان لشکری:
🔹
معوقه ۴ ماهه فوق العاده بازنشستگان از طرف سازمان برنامه و بودجه تامین اعتبار نشد و ظاهراً پرداخت آن به ماه‌های بعد موکول شد/ ایلنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/691127" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74e8d5c73.mp4?token=Egepmgs0giXdGVeougSRMykdY7awzRfQ-Hx6wyEnRQzRCiMyUldKLzKoZVO4v9QJqQnDlcoqKUjWQWXKZgPukwbvmo-l1p6boZJc91WqK4cim7FIe7vi9JCdxYJAVQ5yM7vOocwct8GKFzeDbfG8-5OMgPDqDNV6-Ixu3lW7RkjRWoWIAAywXFfSJS9Q49JYYlyQ4etCorfs6460TkjWqkZmB62AA4ryFfB--fBZZgGVQQlGuYmMG_F2EG92yMI79nSR84Kuq0e7iAfSQP8s3mffmtBNYY2LubHiRONJtn7p6yhqEnFSMlBiavvv_NjRsSmkV2wcedfMVrFbsCjwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74e8d5c73.mp4?token=Egepmgs0giXdGVeougSRMykdY7awzRfQ-Hx6wyEnRQzRCiMyUldKLzKoZVO4v9QJqQnDlcoqKUjWQWXKZgPukwbvmo-l1p6boZJc91WqK4cim7FIe7vi9JCdxYJAVQ5yM7vOocwct8GKFzeDbfG8-5OMgPDqDNV6-Ixu3lW7RkjRWoWIAAywXFfSJS9Q49JYYlyQ4etCorfs6460TkjWqkZmB62AA4ryFfB--fBZZgGVQQlGuYmMG_F2EG92yMI79nSR84Kuq0e7iAfSQP8s3mffmtBNYY2LubHiRONJtn7p6yhqEnFSMlBiavvv_NjRsSmkV2wcedfMVrFbsCjwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
تخفیف  50% ویژه هتل مشهد
گروه هتل‌های درویشی مشهد
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
بزرگ‌ترین مجموعه آبی هتلی ایران
🏎️
🛥️
تور های سافاری/ یات‌سواری - رایگان
🕌
✈️
🚆
ترانسفر تمام‌وقت حرم، فرودگاه
🎮
🎱
گیم‌کلاب رایگان
📍
۴ دقیقه تا حرم
⏳
ظرفیت محدود
📞
05138080
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691126" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691125">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK1vChY8e4ZKqr7MiBMEBK5toMagPN8R1cUWbPSBQGgyJzZ_DmtkRiKW52VuUCZE6BWPWfIrx80L9YA1GktqrLP5pY0gk1eAzuyvxUyibgAvrjeOdERPC4G59ciN_Gyv5xMRi1Q-fqaBthcIa7wezMbbX2QfTe7H65G1nT8j_XiRuLgMMbKsYAllZKq1jWEKcATsl8uQo8iMjpmJRj6lJ5mYbgSsjtL9VxA9GjfGssetAePi1zbdhGV7K8knWN1IpvlmXfUGskdX5I1VuN0eKYwb-vQExHm8RarYzcm9-9vmRdU1W5dn5Oq1shk-59D5HCqvoku5_hRXpjmv3TI0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفروش‌ترین کفش جردن در حراج آخر فصل
💯
رفقایی که توی کمپین حراج آخر فصل خریدن، 1.4 میلیون تومن سود کردن
❗️
قیمت قبل: 3,299,000 تومن
❌
قیمت تخفیفی: 1,868,000 تومن
❌
پرداخت درب منزل شما
✅
وجودی محدوده، قبل از تموم شدن سایزت سفارشتو ثبت کن.
مشاهده و ثبت سفارش:
مشکی
🖤
👇
https://memarket24.ir/product/fast/46467/180124/
سفید
🤍
👇
https://memarket24.ir/product/fast/46468/180124/</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/691125" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691124">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c22e0a68d.mp4?token=tJqmpxiYPtKYiDCLCZy9yj9eYfjSfoKSjxi6jvSEaVS54HYoo6NhQ_4V3Pv57BO3R4GUPrvtJeiq7vdJr0sIbOS6Eh6hBpkXw_9MQLaEKRYFAQ4fkuK9iqpylSKtQLI7P0RzgfNDSruLvnhdsohO0zV8W5DpIbgjBUM-SDYp1-TA5ku4d34SLTxyX7jeyM7GO1VvVnxrVn1UNjGV-bsKWuqsHQaZFDNGPzUIRhrBj_pXxTK4mxO8kD2T0jzmTGuMuxKl-81VQa0MspJ-Pr_nOh8Kw6QdgGph-8IMjJ9WqCbXtcqrty5ngcBMZ7L8o0Vk17gVpfTmHf_gf_OQwQTQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c22e0a68d.mp4?token=tJqmpxiYPtKYiDCLCZy9yj9eYfjSfoKSjxi6jvSEaVS54HYoo6NhQ_4V3Pv57BO3R4GUPrvtJeiq7vdJr0sIbOS6Eh6hBpkXw_9MQLaEKRYFAQ4fkuK9iqpylSKtQLI7P0RzgfNDSruLvnhdsohO0zV8W5DpIbgjBUM-SDYp1-TA5ku4d34SLTxyX7jeyM7GO1VvVnxrVn1UNjGV-bsKWuqsHQaZFDNGPzUIRhrBj_pXxTK4mxO8kD2T0jzmTGuMuxKl-81VQa0MspJ-Pr_nOh8Kw6QdgGph-8IMjJ9WqCbXtcqrty5ngcBMZ7L8o0Vk17gVpfTmHf_gf_OQwQTQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورزشگاه نئوم عربستان؛ میزبان جام جهانی ۲۰۳۴ در ارتفاع ۳۵۰ متری
🔹
این ورزشگاه در ارتفاع ۳۵۰ متری از سطح زمین معلق خواهد بود و انتظار می‌رود حدود سال ۲۰۳۲ افتتاح شود.
🔹
همچنین، قرار است میزبان بازی‌های جام جهانی فوتبال ۲۰۳۴ باشد. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/691124" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691123">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آغاز واریز حقوق شهریور بازنشستگان لشکری بدون معوقه
فعال صنفی بازنشستگان لشکری:
🔹
معوقه ۴ ماهه فوق العاده بازنشستگان از طرف سازمان برنامه و بودجه تامین اعتبار نشد و ظاهراً پرداخت آن به ماه‌های بعد موکول شد/ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691123" target="_blank">📅 11:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691122">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4c4d3ed2.mp4?token=Rw6yjUjef7fJewyvrnz1Ww5_GUSeWLdwWoAS0_cKNo2Kh3n-4bAZcaBeO7Z90kY9XsqJho-EL72mhlPBqKzKZM8OByEQKGxk58otCx-S2PP6Ma4wxONJ09sFI-DhwE_oXSbcFzouOmMXMyW2HZbpVerpWZuMQpEHJEGEixqfE_lzIZFC2XUFwxXFMgd8IAczvrj-TOgrSCP0O0JHGD0zicEDnrToGD4VzEzjAD-ayacCL7BUs9uqLdce8tpVw82ab9sisQ1_MGEeVrVLU_fTMKGlSnLxo_kNZylqz6enKJMHbRNiNpmo-Qs5bMrfLXLpnCGyj46Nvn-JBdtTabz9miXaJk2OxRdeCgZYiyaJSDkno16IFjQUDxpR4TyDZPd4finJ2RVxpC5hq8hQVTEHmtLNQFl5qcQCGVTSyJ-vZveH9Ql2bujwbkcsLr7DPzvo2BGVQHw3YjrKH1j5p-zRWAKX67y51MzvCDOCYfwwkksZX6lEI0ieSlSadn-yAYHT824BGerkF6DUAByZFiOoMaCyB-Y3zGbWeL2uCPI4iAeuMkWx3-JIGsFwcULHeQhLdjiF41e6PSbZTOUIOvXnt0Zb6Lt2FRpwGzqZmNxaO5Y4jdW4BX5sSNhU4o5ORwHhxLadibKfDpZ4PH2Eqq3qWDNnmY2y-O2Y4hhHQUIen2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4c4d3ed2.mp4?token=Rw6yjUjef7fJewyvrnz1Ww5_GUSeWLdwWoAS0_cKNo2Kh3n-4bAZcaBeO7Z90kY9XsqJho-EL72mhlPBqKzKZM8OByEQKGxk58otCx-S2PP6Ma4wxONJ09sFI-DhwE_oXSbcFzouOmMXMyW2HZbpVerpWZuMQpEHJEGEixqfE_lzIZFC2XUFwxXFMgd8IAczvrj-TOgrSCP0O0JHGD0zicEDnrToGD4VzEzjAD-ayacCL7BUs9uqLdce8tpVw82ab9sisQ1_MGEeVrVLU_fTMKGlSnLxo_kNZylqz6enKJMHbRNiNpmo-Qs5bMrfLXLpnCGyj46Nvn-JBdtTabz9miXaJk2OxRdeCgZYiyaJSDkno16IFjQUDxpR4TyDZPd4finJ2RVxpC5hq8hQVTEHmtLNQFl5qcQCGVTSyJ-vZveH9Ql2bujwbkcsLr7DPzvo2BGVQHw3YjrKH1j5p-zRWAKX67y51MzvCDOCYfwwkksZX6lEI0ieSlSadn-yAYHT824BGerkF6DUAByZFiOoMaCyB-Y3zGbWeL2uCPI4iAeuMkWx3-JIGsFwcULHeQhLdjiF41e6PSbZTOUIOvXnt0Zb6Lt2FRpwGzqZmNxaO5Y4jdW4BX5sSNhU4o5ORwHhxLadibKfDpZ4PH2Eqq3qWDNnmY2y-O2Y4hhHQUIen2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف یک سارق منزل درباره نحوه یافتن طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/691122" target="_blank">📅 11:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a11c7317a.mp4?token=a72VN31WguTIV8l_HkVLi8mUtxsLynFQ2MdilZfQvFNw8Grp2612LbLeODT4YTYpOoSDxsJ2SnVBRRuZnPmkng81N5plgaEfuCBbvsMlSG4ASNRh1bapUhRYOxIBWGRxAqqWi81P1BLIfhaUnhN104b7bBdygOy81iUXgU52FBmELOIdCNCHVb3SMuprQjpoWEdfLfWuIccVzJzMEVQZsaTkJo1NtvLdl7u8tK8oo6jI8jEf4vHUO2H5ZtMl0QIVfKCMwenUxrfeXjxnOL6PWb6gLBjCWBdaXtPNIGxRNOhafZ931rY-gPyja0rI4ysRSYjqblWyGrx5obNf6QFUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a11c7317a.mp4?token=a72VN31WguTIV8l_HkVLi8mUtxsLynFQ2MdilZfQvFNw8Grp2612LbLeODT4YTYpOoSDxsJ2SnVBRRuZnPmkng81N5plgaEfuCBbvsMlSG4ASNRh1bapUhRYOxIBWGRxAqqWi81P1BLIfhaUnhN104b7bBdygOy81iUXgU52FBmELOIdCNCHVb3SMuprQjpoWEdfLfWuIccVzJzMEVQZsaTkJo1NtvLdl7u8tK8oo6jI8jEf4vHUO2H5ZtMl0QIVfKCMwenUxrfeXjxnOL6PWb6gLBjCWBdaXtPNIGxRNOhafZ931rY-gPyja0rI4ysRSYjqblWyGrx5obNf6QFUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کالری روی بسته‌بندی چجوری حساب میشه؟
🤔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/691120" target="_blank">📅 11:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b360e4bf8.mp4?token=C97cbAop_zQuC7ZwZBYDvt6sDk5CyT2fzh6fu60jBmDXiZtNWWrWHGPqywDOn0WYOTHzJNUl6zE9sr_-h6xcIUDX55AMLuzSZDf7irUUyTEUDZIhnEb8PGnra557DTo1di4oAJECHAFpYVYD6y-bFn2QxjOn0nTDb0gQ-4XAHtOYW8rDn09Ny1miDMThLTCVUcHXsCXIvAzO5cQwSnQEZnsYzU3yxo9acARyZm1ucXLNIW2iMAGzBQLFKu-pka6j9CIhj8k3kBARRTs-Gvg0HghbTNtYPg4nEU6Bs_bfKr_tdlLX0yEM3ZQ9JF6Bvi91-1IvMdXQmAOav9zzcPC2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b360e4bf8.mp4?token=C97cbAop_zQuC7ZwZBYDvt6sDk5CyT2fzh6fu60jBmDXiZtNWWrWHGPqywDOn0WYOTHzJNUl6zE9sr_-h6xcIUDX55AMLuzSZDf7irUUyTEUDZIhnEb8PGnra557DTo1di4oAJECHAFpYVYD6y-bFn2QxjOn0nTDb0gQ-4XAHtOYW8rDn09Ny1miDMThLTCVUcHXsCXIvAzO5cQwSnQEZnsYzU3yxo9acARyZm1ucXLNIW2iMAGzBQLFKu-pka6j9CIhj8k3kBARRTs-Gvg0HghbTNtYPg4nEU6Bs_bfKr_tdlLX0yEM3ZQ9JF6Bvi91-1IvMdXQmAOav9zzcPC2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکم اعدام خائن به کشور(حسین پدران) که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار داده بود، اجرا شد  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/691119" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691118">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f01dadd4.mp4?token=bj66ZJ6IXYSJbqZwpZ4htwc_UYMNYO2PZvx8oGCaELa3rm5R4Iy9SIO2Er-uXDicnR_33uv0f28vvrfHnAj6PCvsG8N2VSsFTE3PYBkAwcaRll4Jo-qZ0LdMZJC04V95J829bMAHIqcUvV44htxU3Z5oIm7W9x8cKBGejqJYI1sPfuxnCJXq9aBPiluxHs5OlSO4HaKh-R-BqFtaxCaaNCCSKVznuyYDF9slgtR5zvhKT9aWQBaSS3Zt2QuXMuz5stbQdeagVLwib4qeHFPmf0HEkYOKgEbihn3Pd4GGzZKTWR2omMF30N3X00xAdnZx3l1vRLhRk5aVSwd4F6L-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f01dadd4.mp4?token=bj66ZJ6IXYSJbqZwpZ4htwc_UYMNYO2PZvx8oGCaELa3rm5R4Iy9SIO2Er-uXDicnR_33uv0f28vvrfHnAj6PCvsG8N2VSsFTE3PYBkAwcaRll4Jo-qZ0LdMZJC04V95J829bMAHIqcUvV44htxU3Z5oIm7W9x8cKBGejqJYI1sPfuxnCJXq9aBPiluxHs5OlSO4HaKh-R-BqFtaxCaaNCCSKVznuyYDF9slgtR5zvhKT9aWQBaSS3Zt2QuXMuz5stbQdeagVLwib4qeHFPmf0HEkYOKgEbihn3Pd4GGzZKTWR2omMF30N3X00xAdnZx3l1vRLhRk5aVSwd4F6L-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آتش نشانی تهران: دود مشاهده شده در آسمان شمال تهران مربوط به حریق انبار یک رستوران در خیابان دولت است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/691118" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691117">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: در صورت تحقق تجمیع، انتخابات مجلس و ریاست‌جمهوری اردیبهشت ۱۴۰۷ همزمان برگزار می‌شود
🔹
دشمن برای امضای خودش اعتبار قائل باشد و به تفاهم اسلام‌آباد برگردد/ کشورهای زیادی در حال تلاش‌اند که این اتفاق بیفتد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691117" target="_blank">📅 11:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfAvvqpSP6Tn0rwrpdodrEe_H8VjtEgVpdonhUsaeg-blu4NT7_oQloBanbXgAKIzl0b4xOFoYRxYbxIvGwcmP2H9yUMmc5LK4y9LtOIlq61Xwx8xPduvke6p5aiik9KEk_yi-ltgLIf6t0HLh7Rjxz8UH1fkKI_6Qe7Xz9iHbxQvl_ZgaZI60uXz1aaoXfEKkwUrDuIZcKxhPo6Gua5wWznkJb4CbbjIg4gc7iqa--MDVwHG2nulbwOrvXO30Jif0RCRAt_0oZS3CjhMtpxIdhLuBIxH_Kd4WxrCF7cIzAsjggsXHCXh8MENeH__85N0Mmdb2qvOeG00NWPffqofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هک ۷۰۰ نیروی امنیتی اسرائیل توسط «حنظله»
‏
🔹
گروه سایبری حنظله در پیامی با اشاره به «نفوذ گسترده سایبری به تلفن‌های همراه صدها نفر از افراد وابسته به ساختارهای امنیتی اسرائیل»، اعلام کرد تصاویر مربوط به حدود ۷۰۰ نفر را در وب‌سایت خود منتشر کرده و مدعی شد این افراد از طریق ابزار «ناعِم» هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/691115" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20581d14c.mp4?token=U1v2Kfa12bcpTRsyDgRlB6KetZ5-7eAiIhz0BSe67XwKYKAD7KD-A2SxA-1-b5M6o0F90NNeNZ6_DD2YP7n32wDToltrTDkIeE2Ye9KrmbozLuJM9ZsbuBYDrvkg9oPa45ZyX8GUdwBT8bmJYimEloz8wWo5q5oI854et30Nrakioqhtu-LHyN6q1wzmT45Td_e8VvdWLbx46S3riH3lHu9hH4vgF4KkbWmXkARut7eY-EPGYFgxVE6Yp29xh6RBYRMzGBrkCip2qiDADtECUOipkDcByqSC-RC9JmkSr5H7ETFWCEXJc2hy8CnbHNeJOAPGK7Xn98ny6GA2xh8ptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20581d14c.mp4?token=U1v2Kfa12bcpTRsyDgRlB6KetZ5-7eAiIhz0BSe67XwKYKAD7KD-A2SxA-1-b5M6o0F90NNeNZ6_DD2YP7n32wDToltrTDkIeE2Ye9KrmbozLuJM9ZsbuBYDrvkg9oPa45ZyX8GUdwBT8bmJYimEloz8wWo5q5oI854et30Nrakioqhtu-LHyN6q1wzmT45Td_e8VvdWLbx46S3riH3lHu9hH4vgF4KkbWmXkARut7eY-EPGYFgxVE6Yp29xh6RBYRMzGBrkCip2qiDADtECUOipkDcByqSC-RC9JmkSr5H7ETFWCEXJc2hy8CnbHNeJOAPGK7Xn98ny6GA2xh8ptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه انواع آیس کافی با ذکر نام آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691114" target="_blank">📅 11:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFqY63RE0XUdncgatehMcfIt8wc1lGKafgkbaLL8TGpfM21MzVKFcZAmq2MtHAIqfJJC41VixHk5rkfG0r3RFvE92yZYRl7ah62jdMpAPOBzhRWlf-0s-4QHi2IbdO82ox__wdPKcoGbt381MKHCinKiJrexC95Fu4DBnVsNxjgBumNwYOyqcWpmsTubo32Kd-_69dPnci0RSq5DIGO2in_swhPBlgYjAUcg9pHT9lb15ZjkIfYKKxzVkfWICfFZxQu1DYXRJDpvXXVrOMwdtiLF1DTdKKT-i3tlCg_BVJtexK9PIp5p4JBYxrzHAoQghRLKjKrn2L5sbzG8pTAtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزم جهادی راهداران برای احیای محور بندر خمیر - بندرعباس؛ بازسازی پل منبع آب در قلب شریان ترانزیتی هرمزگان
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان از اتمام عملیات بازسازی پل بوژی در محور بندرخمیر - بندرعباس خبر داد و گفت: این پروژه با تلاش شبانه‌روزی عوامل اجرایی و بسیج امکانات، بر اساس برنامه زمان‌بندی به پایان رسیده و آماده بهره‌برداری است.
🔹
عباس شرفی با اشاره به تخریب کامل دهانه‌های چهارم و پنجم پل منبع آب در جریان حملات ددمنشانه دشمن متجاوز آمریکایی، افزود: با توجه به اهمیت این محور در تردد وسایل نقلیه و جابه‌جایی کالا و مسافر، روند بازسازی پل بسیج امکانات و فعالیت هفت اکیپ اجرایی، در مدت زمان پیش‌بینی‌شده به اتمام رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/691113" target="_blank">📅 11:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
افزایش ۱۳۱ درصدی قیمت پوشک در ۶ ماه
🔹
قیمت پوشک از ۳۶۷ هزار تومان در آذر ۱۴۰۴ به ۸۵۰ هزار تومان در خرداد ۱۴۰۵ رسیده است که نشان‌دهنده افزایش قیمت ۱۳۱ درصدی در طول این مدت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/691112" target="_blank">📅 10:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: در صورت تحقق تجمیع، انتخابات مجلس و ریاست‌جمهوری اردیبهشت ۱۴۰۷ همزمان برگزار می‌شود
🔹
دشمن برای امضای خودش اعتبار قائل باشد و به تفاهم اسلام‌آباد برگردد/ کشورهای زیادی در حال تلاش‌اند که این اتفاق بیفتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691111" target="_blank">📅 10:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471e910179.mp4?token=oPAiiB8TmY7cezzzutqUAdCIllo_rXUfjpOspx3uiVJ8b8CpQgSzS5FqYiSLUMAW5FEFns73gcbQYhPghpX-9fjEBexAG0-aFbMKod-mXkuzNpdZjtD99UXyOvgFsy5eRYYwpsZ7YQjeGG4B9BbsmLZ6LUcQEcFNseiZUJJOJRaY26HlhKJWbN3GMzUXKmq7RnZnXVyhO9WvEzt2kquTTjAs4l4MidVNX8K9hg0oMgbJ9xKr4fE797jd0ceG4K_mrV5UTI0eYz3fo4YTAbNsWRgHc73-8Qy-467mFYs8BicWiRocmSD36Sne5AAue7dWfIloD9KvDV1ptrxFhLgunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471e910179.mp4?token=oPAiiB8TmY7cezzzutqUAdCIllo_rXUfjpOspx3uiVJ8b8CpQgSzS5FqYiSLUMAW5FEFns73gcbQYhPghpX-9fjEBexAG0-aFbMKod-mXkuzNpdZjtD99UXyOvgFsy5eRYYwpsZ7YQjeGG4B9BbsmLZ6LUcQEcFNseiZUJJOJRaY26HlhKJWbN3GMzUXKmq7RnZnXVyhO9WvEzt2kquTTjAs4l4MidVNX8K9hg0oMgbJ9xKr4fE797jd0ceG4K_mrV5UTI0eYz3fo4YTAbNsWRgHc73-8Qy-467mFYs8BicWiRocmSD36Sne5AAue7dWfIloD9KvDV1ptrxFhLgunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لوکاشنکو، رئیس‌جمهور بلاروس: هدف واقعی آمریکا، ثروت‌ ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691110" target="_blank">📅 10:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ویدیو کالبدشکافی و تست مقاومت آیفون ۱۸ پرو منتشر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/691107" target="_blank">📅 10:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اتحادیه سراسری مرغداران گوشتی کشور: کف قیمت مرغ زنده ۲۰۰ هزار تومان تعیین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/691106" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvgMG_-u22zzENDVgRTbNCTXQNAqiiyKqwzt4O-yfoupem7tOlGnogwSRUwSOg5Rzdnk9zCS5-kO5vSL1waAZKwcL03KmOLWRm3FaXns25Kn7WHpjQt88HF-EqlAlEtupbHvdwDcPO1Q5dtHLjKi1-772lA1adXddqEWRDb1kl1753INd6QDXMCU4q4eOPKpyIcEVZkLMaRbTVdgQ2wUBabpu8cG2QPM8iS98VpwaX7i6FbuwOYktB1OqIjZ4uacyvhbGyjf8v5DbBxCCFdmWAusAmhH8JMpbzsFUH0e_yY7_Oz_MO8_xgEVm8S490UsaYRII75ejZ1DWBLBJYYrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕰
ساعت نگارگری پنج تن
ترکیبی از هنر ایرانی، هویت مذهبی و یک دکور متفاوت برای خانه یا محل کار.
✨
مشخصات:
▫️
قطر: ۳۶ سانتی‌متر
▫️
جنس: پلی‌وود
▫️
طراحی: نگارگری با مضمون پنج تن
💰
قیمت اصلی: ۲٬۱۹۸٬۰۰۰ تومان
🔥
قیمت ویژه: ۱٬۹۴۴٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/691105" target="_blank">📅 10:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c218a009ee.mp4?token=gkNt-hdR-K4vDeYzjPHGaqQaJseRFnyyJ7Qq6NQgcGxZx3I0U1TLynPHfyuxMxrpLNDVscHqc9y_Oz-OB3xzZZtmFFvzDnql5hh2qnedyMFdC4G0OzzfrSpkv4EQEu8pk5NZb5eClKi_BK3YOf3LVgnEHPmWshVRTUlMY5BVN_HDTSzG0b3YU8O46kEIOrYuade15ikEdUDSkNo4WcLHjYcdvqxI3r7BS3FFDzZ3DaQiO5-b1199LOx5EeFwU5JqwHQKB9QR1NWlkTLsgcneFDWbFXJHCPLdW9IxCyuvcUlljm22X8pGt5_CGTF_9dyX1qrAWdJbkSv2omt1NTfSPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c218a009ee.mp4?token=gkNt-hdR-K4vDeYzjPHGaqQaJseRFnyyJ7Qq6NQgcGxZx3I0U1TLynPHfyuxMxrpLNDVscHqc9y_Oz-OB3xzZZtmFFvzDnql5hh2qnedyMFdC4G0OzzfrSpkv4EQEu8pk5NZb5eClKi_BK3YOf3LVgnEHPmWshVRTUlMY5BVN_HDTSzG0b3YU8O46kEIOrYuade15ikEdUDSkNo4WcLHjYcdvqxI3r7BS3FFDzZ3DaQiO5-b1199LOx5EeFwU5JqwHQKB9QR1NWlkTLsgcneFDWbFXJHCPLdW9IxCyuvcUlljm22X8pGt5_CGTF_9dyX1qrAWdJbkSv2omt1NTfSPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین با این سمبوسه اصل بریم به شب‌های آبادان
😍
😋
مواد لازم:
🔹
نمک ۲ قاشق چای‌خوری
🔹
جعفری ۱ پیمانه
🔹
فلفل کناری ۸ - ۴ عدد
🔹
پیاز متوسط نگینی ۲ عدد
🔹
سیب‌زمینی آبپز ۴ عدد
🔹
فلفل سیاه ۱ چای‌خوری
🔹
نان لواش ۵ عدد
🔹
زردچوبه ۱ چای‌خوری #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691104" target="_blank">📅 10:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691103">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJACUtjsqXLyrRyw4dX2SvHrY1577XrKe5OCyGFmiTyOcSWBW_PeRwct7VcPxWcBXC8MNCs2Rk8UdaTOjFH20qiUZP6XWcMmXWG79_k96luWGKwzs2nX1PuoucjRxEXs5LHPNeCTjgkjJNkHy4Q4QWV8cy9KaiqefWlnMHoR0f0q29MYVyj6iSbrh6g-YDeF5f2VonK74qwCkfHqg6mshyyB3b_lWkYVAm-D5-JkzCA4mzBm8PKJutAOnveRLaPTQs1lPPrvWcaYQnk00yEx003qQhEFefjZNfMnBZM3vIDHV0cUsOe98zyRuoRgzVlkYELwxCdhsJn3tLaZ-8Ka-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ۴۰۰ مگاوات ظرفیت برق فجر انرژی خلیج فارس
🔹
فجر انرژی که با حمایت شرکت صنایع پتروشیمی خلیج فارس، بازسازی تأسیسات تولید برق و بخار خود را به‌صورت هم‌زمان در فجر ۱ و ۲ دنبال می‌کند؛ تا پایان سال حدود ۴۰۰ مگاوات از ظرفیت تولید برق را به مدار باز می‌گرداند و با اضافه شدن ۳۶۰ تن ظرفیت جدید تولید بخار، زیرساخت انرژی منطقه پتروشیمی را برای استمرار تولید شرکت‌ها تقویت خواهد کرد.
عبدالله علی‌پناه بهنمیری، مدیر پروژه‌های بازسازی و نوسازی نیروگاه‌های فجرانرژی خلیج فارس:
🔹
احیای واحدهای توربین گازی، بویلرهای بازیاب حرارت و تجهیزات جانبی و مشترک نیروگاه آغاز شده است.
🔹
در فجر ۲ نیز احیای چهار توربین گازی و دو بویلر بازیاب حرارت در حال اجراست.
🔹
نخستین واحدهای احیاشده با ظرفیت تقریبی ۴۰۰ مگاوات، پیش از پایان سال ۱۴۰۵ سنکرون و وارد مدار می شود.
🔹
برای تقویت شبکه بخار، اتصال مسیرهای دریافت بخار از مجتمع‌های منطقه در دستور کار قرار گرفته و با خرید  دو دستگاه بویلر جدید، تا پیش از پایان سال ۳۶۰ تن بخار دیگر به ظرفیت فعلی اضافه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691103" target="_blank">📅 10:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691102">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است  رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691102" target="_blank">📅 10:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691101">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5a05b9e8.mp4?token=VWtjtpRvLqO0ttKS42yzn1UY9OSQw47lwMHgiPZVGP0BKaR-350v6sZ-NhhFR67prYglEs7sNIqZOhGlmxCrjr_HdL9KYkbf-oc6fClM8BEsIYn6XHDJLkPmRjabIhqk9tn4zGNCfECFonXtxQhF2RCcRGkRQQRad43eoAqZZ1P1So6vwyMICCEV4ODeb1SRO6vD3M8CbJBvvpAv3HPZ2H-rzrmEF3TJhyVj3nEedlyLTHYMDDRpGiGfy2YBuwiP2rwIaXOmHnJD2WxhtWYu7coZm60EGfQzm2Gdv7ewAsiSWmXVTERnGqS8BGX2JZxew56HgJRn2QV5rkgHAXE2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5a05b9e8.mp4?token=VWtjtpRvLqO0ttKS42yzn1UY9OSQw47lwMHgiPZVGP0BKaR-350v6sZ-NhhFR67prYglEs7sNIqZOhGlmxCrjr_HdL9KYkbf-oc6fClM8BEsIYn6XHDJLkPmRjabIhqk9tn4zGNCfECFonXtxQhF2RCcRGkRQQRad43eoAqZZ1P1So6vwyMICCEV4ODeb1SRO6vD3M8CbJBvvpAv3HPZ2H-rzrmEF3TJhyVj3nEedlyLTHYMDDRpGiGfy2YBuwiP2rwIaXOmHnJD2WxhtWYu7coZm60EGfQzm2Gdv7ewAsiSWmXVTERnGqS8BGX2JZxew56HgJRn2QV5rkgHAXE2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری ژورنال نویسی کنیم؟ راهنمای کامل ژورنال‌نویسی برای مبتدی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/691101" target="_blank">📅 10:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691100">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvJKYmi2DR1CYf3K1r_2acOEKLsgnGJQbDYnUnitmkar3GrCNRPGhFcOSpCFqmE-z6n6t2zIVc5LXvtp9JtJs9qm1zrReBp0FLHhGQu5eBBCWq-ZDESuCRxTYjlXuJReGBPqTo6OmmR7ILXNTEOf3zQXqGOl6qs29Ogrio5LEfuzwtqjgLRdZenJddVwbMA7pcxUB5i2ahMXZWFswLCaYPsL2QPDm4qlOArWwd6IrniFmaprz4KnFk3Qs-cHFRzig-L12sdIrmY_6efqbRvWzadSHLlwWTQmZV4czpP6fy0tJ4WImv5Obr_u2C5e4Z2F7yHhL31KxcSGVkh1XSngWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت «تلما» و دو توله‌اش به "توران"
مدیرکل حفاظت محیط زیست استان سمنان:
🔹
محیط‌بانان تلاشگر مجموعه حفاظتی توران موفق شدند «تلما»، یوزپلنگ آسیایی ماده، را به همراه دو توله امسالی مشاهده و تصاویر این خانواده یوز را روز جمعه ۲۷ شهریورماه ثبت کنند.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/691100" target="_blank">📅 10:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691099">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
فاز دوم فشار اقتصادی آمریکا علیه ایران؛ آیا مرزهای زمینی می‌توانند جایگزین مرزهای دریایی شوند؟
🔹
آمریکا در فاز دوم فشار اقتصادی، فشارها را از نفت و کشتیرانی به بانکداری، هوانوردی و رمزارزها گسترش داده و دسترسی به بنادر را محدود کرده است؛ در نتیجه استفاده از مرزهای زمینی آغاز شده، اما حمل زمینی گران‌تر و کندتر است و در کوتاه‌مدت جایگزین کامل مسیرهای دریایی نمی‌شود./ دنیای اقتصاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691099" target="_blank">📅 10:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تعویض لاستیک خودرو چقدر هزینه دارد؟
🔹
بررسی قیمت‌ها نشان می‌دهد که شش سایز مختلف از لاستیک‌های ایرانی پرمصرف، حالا بین ۴.۵ میلیون تا ۸ میلیون و ۷۵۰هزار تومان قیمت دارند.
🔹
خرید یک دست لاستیک برای بسیاری از خودروهای داخلی، هزینه‌ای بین ۱۸ تا بیش از ۳۵ میلیون تومان دارد؛ رقمی که برای بخش بزرگی از راننده‌ها از یک هزینه معمولی فراتر رفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691098" target="_blank">📅 10:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691097">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3342a42d47.mp4?token=VxRoGhOX6C_WTFbyNkbUJb03VoRaKklllv2FA-dhu7ReDELIduxBZYodR7Xd_2c3LEDphFK2ryCpXnjlxOL14-blHrJSMEYikjKHVHPmHJDsJG5PR38uuQ__2OLez69pH7uGxxyOpo268bn5m6vUt8rKU3yNdwMprO4YWEXLXQgWXWGeoajdYKrc3hkfvOuFaL5bSSK6MGPUBN6BFFShZU9SsRMaODH5ERm_DGbA2VDFrfbexv_8J1EFM5ZqUSL0k0fBG81sBMNFooD0TRRY0QBUenaHhlrR-adT7aNhHyhpN-38gjqWLPiRvYexeXoEVFmc9ORo3Xx_12JFNkSQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3342a42d47.mp4?token=VxRoGhOX6C_WTFbyNkbUJb03VoRaKklllv2FA-dhu7ReDELIduxBZYodR7Xd_2c3LEDphFK2ryCpXnjlxOL14-blHrJSMEYikjKHVHPmHJDsJG5PR38uuQ__2OLez69pH7uGxxyOpo268bn5m6vUt8rKU3yNdwMprO4YWEXLXQgWXWGeoajdYKrc3hkfvOuFaL5bSSK6MGPUBN6BFFShZU9SsRMaODH5ERm_DGbA2VDFrfbexv_8J1EFM5ZqUSL0k0fBG81sBMNFooD0TRRY0QBUenaHhlrR-adT7aNhHyhpN-38gjqWLPiRvYexeXoEVFmc9ORo3Xx_12JFNkSQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/691097" target="_blank">📅 10:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691096">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnYhl5JxkwCmHp8OOyVlhw9PbPuDVS7_swEdrY6nPLSA9fSIW-4CwYDmqJS1IcaueNAbUuLlBpa_dnxpxx5kWZaB0NuNcVMtf3yrEDE7nYWpPjgIFWUQfKqUj7sjBE2xiJ_QT5wf42PgqJsFeEa8UHcpNeEdlf4SSf_oM9H7Ssk_rivQ_Hsky_V3FZd3gz1R-6Ep4n4pGo12QItR7vNmVOxdPgcsEHU2SmY-OJmd5nNii_J-AExhFgb4nqE2H0vlR9sMQR8dGxIZeLd_iIz0F8-KZ5wthAkSQCyX16U5obwXU-wiUE5_XRWn8AtrW29AcMsTm-Q2JpdK1eqafDN7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ر
ئیس جمهور چین به واشنگتن می‌رود؛ جنگ ایران روی میز مذاکره با ترامپ
به گزارش آسوشیتدپرس؛
🔹
شی جین‌پینگ، رئیس‌جمهور چین، هفته آینده برای یک سفر رسمی به واشنگتن می‌رود و روز ۲۴ سپتامبر با دونالد ترامپ در کاخ سفید دیدار خواهد کرد؛ دیداری که جنگ ایران نیز یکی از محورهای مورد انتظار آن خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/691096" target="_blank">📅 10:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691095">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEkizfgiuKAhxcfmnGVHEZEQrPwPBEhcd9oZP6VHOYanKZXlDrIOOCT5z7zpPl_O2WHnX254sdxwxisSEW0ebdqg-zmGJJCSvvcjWk9ocQhP90-xgr2h8frgnLFvHaYT_A2F4tM9K_brHmG5yRUFGWTjhqaQCbMlQKl-nG8aDCTkdiqboDS5h191gDe1jS4FCf_GKqJfcCA2pxnxvb30gAfep8DkwkvCc-3gt5jQIgAD0ZNi5fTEw3frcaMOrkqmlLYd1D7GD9lyvOCak-gaSQXkqWCDcGDvQ6YOfMn90pBeoBT4txuXKvBUMCoiD5iAFIOHh4HW164ZS0-tRSH_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/691095" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691094">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e03437a32.mp4?token=Nf2XCaOS3AZU44IPOoOUnd6gd5wK-pGb2kQ7JEB2IhFbOOmeviLKpVleSpTX1oYBSIkuJ59SM_3Gr3CrZOlWsqbKwuNpSP3VlK09C1rP5B6k9moPidryVKkExNLmeUUeDKFIkhAKmHvcfhjWl-IhVZpTftHM1qwYxyL0AyacbPOCjjfJ_ov5Bk_KDxAUSNEpT4ItQDA5r7ZRjIgTcMZCGo9Dw-f35mDC8O6ZQ5vRI-9RhWvcgHlqpIxykn1yg53kAYbQJ7cshyubL04oTe38ShM6Wx2WXHYCzByMCYWpM-YxkihkBRJgvu_3neGKSjCEeMxPbFIUFKbkmCKZy02A7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e03437a32.mp4?token=Nf2XCaOS3AZU44IPOoOUnd6gd5wK-pGb2kQ7JEB2IhFbOOmeviLKpVleSpTX1oYBSIkuJ59SM_3Gr3CrZOlWsqbKwuNpSP3VlK09C1rP5B6k9moPidryVKkExNLmeUUeDKFIkhAKmHvcfhjWl-IhVZpTftHM1qwYxyL0AyacbPOCjjfJ_ov5Bk_KDxAUSNEpT4ItQDA5r7ZRjIgTcMZCGo9Dw-f35mDC8O6ZQ5vRI-9RhWvcgHlqpIxykn1yg53kAYbQJ7cshyubL04oTe38ShM6Wx2WXHYCzByMCYWpM-YxkihkBRJgvu_3neGKSjCEeMxPbFIUFKbkmCKZy02A7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار مهندسی چین؛ آسانسور کشتی سد سه‌دره، شناورهای چند هزار تنی را در کمتر از یک ساعت ۱۱۳ متر جابه‌جا می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691094" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691093">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHL1ZuWFLhkA8bRN192Z9WZzAiMLEwh4nl_09uUbHeVkBnDzEm6Ctl5t1CScj2rk-Os480jmBs3Ee0Kgu0uLH-jCeV1oa-b57SQk0uCwzC9h3LDc3yrQLNviBU-YaFgnw-3PP4zYtJz472TWCsTaH0p7djkAX5XlvoOfMNPELAGeS1su0_xmZsRojjSY8mpoccLJSFVz6CA4eBIFZH_Mn21sDE_hgpSA8KlK_HqYWKOXqCUmw7r2NcgY9KJhRnucPBbEKAONnZjWTDthuwI23Gah3Yn_aOaeIHZ9ehwkEepgmJHhOsjS0QchC5KfJITAuFUDc3mkOrDMR3cNM5vZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ صدای شهر
🔹
اگر در محیط زندگی و محله خود با معضلات محیطی، کاستی‌های خدمات عمومی و نقص در زیرساخت‌های شهری مواجه هستید، مشاهدات و مطالبات خود را با ما در میان بگذارید.
🔸
گزارش خود را در قالب عکس یا ویدئو و متن توضیحات ، همراه با نام و نام شهر به آیدی زیر ارسال کنید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/691093" target="_blank">📅 09:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74dcd9335.mp4?token=OH3b2I7cw9am5ZroMr_05K5x7Da0rIDhZ5HdgbEXk1RI0abUOJ_KBEp-XtDrHOy0RcufTC3NI-1wtWzDEhOOvpFwteyrmCkSPxJOMC6AGwTKaGULmzDdXQUfiLhMK3RHC7KEyfV_WX_y5w5iR7g5whRUt-iJSDC2H29TrviEf7q6qD2rrO3xaxLTrcJhZ-1CWzYFEx4xjsTLBB7pgUaXZSJGIlK_qJXY8CyqFxI1aRBnGTNA2vizijZK_3RBPDgLP6Vqi2be5ae17jUsLRPHVFcVpSdCfo0Wbj5gjqzUtkOo4DHWHRzUgWmJuppI6JnpT3haQpDsNLjj_7Ij9U_Wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74dcd9335.mp4?token=OH3b2I7cw9am5ZroMr_05K5x7Da0rIDhZ5HdgbEXk1RI0abUOJ_KBEp-XtDrHOy0RcufTC3NI-1wtWzDEhOOvpFwteyrmCkSPxJOMC6AGwTKaGULmzDdXQUfiLhMK3RHC7KEyfV_WX_y5w5iR7g5whRUt-iJSDC2H29TrviEf7q6qD2rrO3xaxLTrcJhZ-1CWzYFEx4xjsTLBB7pgUaXZSJGIlK_qJXY8CyqFxI1aRBnGTNA2vizijZK_3RBPDgLP6Vqi2be5ae17jUsLRPHVFcVpSdCfo0Wbj5gjqzUtkOo4DHWHRzUgWmJuppI6JnpT3haQpDsNLjj_7Ij9U_Wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگو با دکتر "غلامرضا نوری قزلجه " وزیر جهاد کشاورزی دولت چهاردهم به زودی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/691092" target="_blank">📅 09:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac3403a0e.mp4?token=ANoepvfiPEvR3cKzDXV9r05_p5p7Jy9t50tUIFKeHSeIDs3Bn1whibyawMMJb3dV1dsaNs-Zu440hsci-yojjD6ZYxdFiRVGGmNUKe04_q3rbw7X9CvxWR3uyIHdj2yjSdn129ninlzvxdAhuw8nOPbD6LgAFUKGTL29HtwFV_a8ynqa47MvwrWuYvQhESHV9s-l2BCZS4B7HA6MOj5gA8eYefTZsnsO4QFrP63-V_pLaUpy0w_vSlUFRkE_O6A2n0uFOz1SJMq5WRmq6uM4Rxdix5WgO9S-AkjvvqDYAVLJOg0rowWFlH6UU6A64vyEX2FItDHbG6sgqtsqiTei0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac3403a0e.mp4?token=ANoepvfiPEvR3cKzDXV9r05_p5p7Jy9t50tUIFKeHSeIDs3Bn1whibyawMMJb3dV1dsaNs-Zu440hsci-yojjD6ZYxdFiRVGGmNUKe04_q3rbw7X9CvxWR3uyIHdj2yjSdn129ninlzvxdAhuw8nOPbD6LgAFUKGTL29HtwFV_a8ynqa47MvwrWuYvQhESHV9s-l2BCZS4B7HA6MOj5gA8eYefTZsnsO4QFrP63-V_pLaUpy0w_vSlUFRkE_O6A2n0uFOz1SJMq5WRmq6uM4Rxdix5WgO9S-AkjvvqDYAVLJOg0rowWFlH6UU6A64vyEX2FItDHbG6sgqtsqiTei0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده مرال و شوکا در جنگل‌های لنگرود
🔹
مرال و شوکا از گونه‌های ارزشمند حیات‌وحش جنگل‌های گیلان به شمار می‌روند.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/691091" target="_blank">📅 09:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2c6047ab.mp4?token=TaRdh5Z5VXkrTz1jvMVfy81mxI4wxaY7kCuOJsVDYeAFQ9wryEyu2YHcqF0vGooRaV3UiZCHZKjdCjj1RJpLHPLV99LaO1lXZZUcyryatoggi1iQodW8I6oGsv48o4nzLlTOTJbeBGIHQrcI0yOXCXK8PIdYpY2UB9j80XcU7DxA1m5rL_ed1P1pYCi5rFpFVlH4CZC4_7Xh2ft5Ww8UhAzSbKfkOisQ1miSSrGOzpNiABMPi6NDhUPkyqzURlz2WxEpJibv_LSzOJUmRz3XBrl2p7MIp8tU0ZunhnknLnTe_I42t8z8IEaOuLJECGKlJCF3YJuYj-pN2CHW8WbhPTAYz4e76FEl6yCpv1NJVv1bRf5U1FWi-SWwVH_AmrSqIeml1mCfh_n8jBZiNXVUK4QTU3uf9xqYPu9fK5idzlhaMn3zEyKZ5SB_RfmU9mjszqPFmd1iXMxovT4gS2BEWcQrymVK7ZywqiN7lIha2qBApcf2SpO3DZpUS5fe3YXKr-EOG7PZztM5oPNP-Gnn3dmRu__CJzpf9ZtZttiKkthhvqvJh6k0RYa9mqnkhW7yN53Rb7LANDLvEFAjTdel7sKpDVGaTl3_C_sBcrcU5U5pmDp0Izw1WXsSMgKQ4cZ_OC4BWDQyNKneAzeiWgy8k7ZqA7rEKRFaFCfwP9-tN0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2c6047ab.mp4?token=TaRdh5Z5VXkrTz1jvMVfy81mxI4wxaY7kCuOJsVDYeAFQ9wryEyu2YHcqF0vGooRaV3UiZCHZKjdCjj1RJpLHPLV99LaO1lXZZUcyryatoggi1iQodW8I6oGsv48o4nzLlTOTJbeBGIHQrcI0yOXCXK8PIdYpY2UB9j80XcU7DxA1m5rL_ed1P1pYCi5rFpFVlH4CZC4_7Xh2ft5Ww8UhAzSbKfkOisQ1miSSrGOzpNiABMPi6NDhUPkyqzURlz2WxEpJibv_LSzOJUmRz3XBrl2p7MIp8tU0ZunhnknLnTe_I42t8z8IEaOuLJECGKlJCF3YJuYj-pN2CHW8WbhPTAYz4e76FEl6yCpv1NJVv1bRf5U1FWi-SWwVH_AmrSqIeml1mCfh_n8jBZiNXVUK4QTU3uf9xqYPu9fK5idzlhaMn3zEyKZ5SB_RfmU9mjszqPFmd1iXMxovT4gS2BEWcQrymVK7ZywqiN7lIha2qBApcf2SpO3DZpUS5fe3YXKr-EOG7PZztM5oPNP-Gnn3dmRu__CJzpf9ZtZttiKkthhvqvJh6k0RYa9mqnkhW7yN53Rb7LANDLvEFAjTdel7sKpDVGaTl3_C_sBcrcU5U5pmDp0Izw1WXsSMgKQ4cZ_OC4BWDQyNKneAzeiWgy8k7ZqA7rEKRFaFCfwP9-tN0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی عجیب تکنو با بدنه ۴.۹ میلی‌متری؛ باتری و دوربین را با آهنربا به بدنه بچسبان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691090" target="_blank">📅 09:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2Pd73xNJ6VPOvA_tkvx6Ms0RNDK3q1dkgr5TiCpvROhGg95ekpnS_P_ZjzU7ZyD8ZWY7PvCWYi4x8lY2xM3ocQoqqrgE9FzdkYMP5UU7zvJSyAtFTkqKvRavgC22TY6k-vxrmXvn3y2ZjeHPPgbJ52SwvCmZdhi16aewiE1-b_h0ArEV_syeISqAM0pR0Byb-LShm1AuyvQIAKDdU6UFdgvHqc0oSXbpoIdL1IUSlx1Smf7svYP6sIGUPqgv8ssFkWmreXxzUtfX_IQ2vX1euEIW4zJQWv48jO_tP1Kpc29Mnt7SA43d6i4AZe-zuUBqYbnmb3oTkbhHLEn_Vug8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به وزیر خارجه فرانسه؛ اشک تمساح بس است آقای بارو!!
وزیر خارجه:
🔹
یک و نیم میلیون الجزایری توسط فرانسه قتل‌عام شدند، اما پاریس همچنان از عذرخواهی بابت جنایت‌های استعماری خود سر باز می‌زند. سکوت شما در برابر قتل‌عام کودکان دانش‌آموز ما توسط آمریکا، گویای همه چیز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691089" target="_blank">📅 09:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اسامی ضدآفتاب‌های غیرمجاز اعلام شد
اسامی این محصولات به شرح زیر است:
🔹
ضدآفتاب BIODERMA، ضدآفتاب NEW WELL، اسپری ضدآفتاب SADOER، اسپری ضدآفتاب FRUIT OF THE WOKALI، ضدآفتاب ESTELIN، اسکراب سفیدکننده صورت و بدن SADOER – WHITENING SCRUB FOR BODY & FACE.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691088" target="_blank">📅 09:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pws4xN9CQsxwCB7jk6-ca7WlCMKHBqIzxnM19b_3A6aQoVrbk7vkh2w44upY5t4CADCReNy5_v-cLCLVipJ3hwfpPv4EqV7LNfNOIKySvENn-KoHNeVisxcena2DQPF8OzkMCUzk70DSl0JEr61RliXHkHGg5peAHMwsk6SDAPAJwQe1VwmLyRaNE3hj4Y9u1jTUvqtK-YAoHIUst0EbUmZirYXc6Qb1g1r87BgDAJLGOp4fO9wy9YZU4VJWlnPtmaSr0Ud8t0DnObuXy2W-gMy0xDmaX7_lfM0xNU5_VWmR9lLlSw3fkwxmIHdGyhBVHwQNzx4Jdb_0t7u6thU93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم اعدام خائن به کشور(حسین پدران) که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار داده بود، اجرا شد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691087" target="_blank">📅 09:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فقط ۵ دقیقه بوی قهوه کافی است تا خستگی، تنش و اضطراب کمتر شود
🔹
۵ دقیقه قرار گرفتن در معرض عطر قهوه تازه‌دم، احساسات منفی را کاهش داد و فعالیت مغزی را تغییر داد. پژوهشگران این اثر را به ارتباط نزدیک حس بویایی با احساسات و خاطرات در مغز نسبت می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691086" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a276f0b2b.mp4?token=iKdj59Nhrz6tSzjbiXJn2mfzZXZuUOh0e9lYbGo9OPbdq_MU1_heVjt1iig2PsYn3EMjK3ppdQaqNXWpjs87Q7x_8p3dB_s4yZkMoSXnJnxnO3yUSPIIgRw9vVDdM6TadonmghXsO5_b7T6hUYESwV-G7QDEehfWm08wfZn48Xz8LRPLh32yxFVtv99JslArHCtR5WT4E3baKX6Bv7nMxeV9zB-_Izs7OUX9PgCx1Qv0OJjXcMXlbK5TdfYnCfSUH7GR_8sI6Bjyjr5m4yRWWzfP8gcfsDiZj_Bf8PO2aG-VyjywRSJSQ5riz3fEIC16WboxFMtwZ8vdcLTvWvVYfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a276f0b2b.mp4?token=iKdj59Nhrz6tSzjbiXJn2mfzZXZuUOh0e9lYbGo9OPbdq_MU1_heVjt1iig2PsYn3EMjK3ppdQaqNXWpjs87Q7x_8p3dB_s4yZkMoSXnJnxnO3yUSPIIgRw9vVDdM6TadonmghXsO5_b7T6hUYESwV-G7QDEehfWm08wfZn48Xz8LRPLh32yxFVtv99JslArHCtR5WT4E3baKX6Bv7nMxeV9zB-_Izs7OUX9PgCx1Qv0OJjXcMXlbK5TdfYnCfSUH7GR_8sI6Bjyjr5m4yRWWzfP8gcfsDiZj_Bf8PO2aG-VyjywRSJSQ5riz3fEIC16WboxFMtwZ8vdcLTvWvVYfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد انجام این روتین صبحگاهی بدنتون از شما تشکر میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691085" target="_blank">📅 09:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691084" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bc38c38.mp4?token=ghr74B3Ueh9KLQx5_QyJJnOwBWzra4F_v5x-96ElmGTMHghVngBLoRrejVtNlJELCY3x2igdyRfMTJ6LKwRrUXyloQkg5MgbOlsCuihXxXm9YQ3scw5meC8mAGmx-Imv6mkuwhXbOQ6ViSwYAm09SPQUoKzh6o7HJ0EqLbeTmkYr7Yu0n7s8qbs98cVjxrGB0YwUtKRJyr0at5fLSHR_PNUTiNIosLRiLO4-w5NGESe3rsWi19jP-VKA9YzdlBqyjtqvfhm7_AeG1TIoXFu75kAzPWhAb_jNfbkJf-HR-rslmAT7dTsgocFT4set47kN6O9FEog2ERiPOz17I1BgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bc38c38.mp4?token=ghr74B3Ueh9KLQx5_QyJJnOwBWzra4F_v5x-96ElmGTMHghVngBLoRrejVtNlJELCY3x2igdyRfMTJ6LKwRrUXyloQkg5MgbOlsCuihXxXm9YQ3scw5meC8mAGmx-Imv6mkuwhXbOQ6ViSwYAm09SPQUoKzh6o7HJ0EqLbeTmkYr7Yu0n7s8qbs98cVjxrGB0YwUtKRJyr0at5fLSHR_PNUTiNIosLRiLO4-w5NGESe3rsWi19jP-VKA9YzdlBqyjtqvfhm7_AeG1TIoXFu75kAzPWhAb_jNfbkJf-HR-rslmAT7dTsgocFT4set47kN6O9FEog2ERiPOz17I1BgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهداد اقبالی میلیاردر ایرانی، باشگاه ورزشی چلسی را خریداری کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/691083" target="_blank">📅 08:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2344800b2.mp4?token=tHZQo89hr9sLC3PvoSjqjLqB3aepj-xejuZ4_ISJJV9CjB9vOhGNtY_Y6bHPUH6PxX0d3CbLsbNqPu2X5BooONESVyFIKAxHAio3aKgQRtZtrNz8xn_2cNnF0zSPjGvSqznCT3AMEMRVOw7vnWu1Nl2s2KyuBUZ0n1wYc0OTFcg3zGpKM6pbDYQhD2Q10KcHjG6s0tVPxvYU-_9mZ739kPvJadWtERdNxPbZBPm4JtFBbyPwru8tQDsSyAgBeKX7PXxTEDy8-w8GPu7gE7zG_BILpCQooa0vNee2ZAtETvv1w1bxhMxaa9qpu2GDxbFFwj_fgA7-UAnKz4A4ibdIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2344800b2.mp4?token=tHZQo89hr9sLC3PvoSjqjLqB3aepj-xejuZ4_ISJJV9CjB9vOhGNtY_Y6bHPUH6PxX0d3CbLsbNqPu2X5BooONESVyFIKAxHAio3aKgQRtZtrNz8xn_2cNnF0zSPjGvSqznCT3AMEMRVOw7vnWu1Nl2s2KyuBUZ0n1wYc0OTFcg3zGpKM6pbDYQhD2Q10KcHjG6s0tVPxvYU-_9mZ739kPvJadWtERdNxPbZBPm4JtFBbyPwru8tQDsSyAgBeKX7PXxTEDy8-w8GPu7gE7zG_BILpCQooa0vNee2ZAtETvv1w1bxhMxaa9qpu2GDxbFFwj_fgA7-UAnKz4A4ibdIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا ستاره دریاییِ باردار دیده بودید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/691082" target="_blank">📅 08:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=r5O0K0zPRyMVxWnEHkQLzjxSL92G9A1GqYoBkH1FCMs_5GXrD3vTrCwUQTnVjo2yLTVodSXEaWmF9xybwef0o3pP80ZhiYCWJfMkHjSQLmisAbFMySYdTcm9d0eJVGa69-A6PMOjx91vRYt_K2bZnVYP-7mL03sitYvJlLAHgj3D3JsJzitxa4ifG4kmKLjwgOskJldTXsout1Ayjl-FA8i_vVM_IvHSHVCdRTgnUp7SglvoSOdOvjQBtlodKglB6B8mH1_scHgeqAcH_vOkIVc2Ri5niiu_k8_Vvu2NzuVEf0WSrqD_y5rF2fmqc4eA5iUkODZR6nUw9CIqmUf2QjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=r5O0K0zPRyMVxWnEHkQLzjxSL92G9A1GqYoBkH1FCMs_5GXrD3vTrCwUQTnVjo2yLTVodSXEaWmF9xybwef0o3pP80ZhiYCWJfMkHjSQLmisAbFMySYdTcm9d0eJVGa69-A6PMOjx91vRYt_K2bZnVYP-7mL03sitYvJlLAHgj3D3JsJzitxa4ifG4kmKLjwgOskJldTXsout1Ayjl-FA8i_vVM_IvHSHVCdRTgnUp7SglvoSOdOvjQBtlodKglB6B8mH1_scHgeqAcH_vOkIVc2Ri5niiu_k8_Vvu2NzuVEf0WSrqD_y5rF2fmqc4eA5iUkODZR6nUw9CIqmUf2QjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهمن عظیم در قفقاز روسیه ۱۷ کوهنورد را به کام مرگ کشاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691081" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgYq1XDBxoiKxwfXNjAvGVLWDqZYvZl3ZBlcDWEKReE2q5xAM06ktiHxc64O3M-YLzbXNFB2Xur32Q1Yy4sIgaMuo8CLn10F0DlBUsNHpK4DIc4szp2bjMA6V2lR-UEuWHlEUL4C7TStKTihlzCHho4yXx0cz3BcAvCq4Ovg6IcOEkdwTPhzU9TG_RCgW5Ydqj_FHCnfzJFvPZykUL_6TX_2RkM5kaSiyj7lnk0lDnZTtglwzUaJKvuEYnMykLt3cP4i89RYFeLN22YyPm3KtOj9S8sEi9061LU4vWO4w_SCsxvdnTgexDI2pCu2UEMSPBBwh7eFa2RllKR-uTxorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شارژ حساب ایران در آسیا با برد استقلال
🔹
برد استقلال مقابل السد در لیگ نخبگان آسیا باعث شد ایران جایگاه پنجم آسیا و سهمیه ۳ تیم مستقیم به لیگ نخبگان را حفظ کند. حالا نتایج استقلال و تراکتور مقابل تیم‌های قطری (به‌ویژه الغرافه و الشمال) برای حفظ این برتری و سهمیه‌های آینده ایران حیاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691080" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNv1dReyjgdXtvxNtCqEFCDfhA1tSQfwMUDn8KgI83hPaBZiwp3KgTqubvCsxtI-5wtGU1YEHkHhV2HpkIRHTJmjaLZbrdrd79J-x3YDQkQOH0FsmUgbDjQmHmFnHiMKLvYDpnT7Npi71myk1rEco02GjT8grDvV_bTDwPjpDZEK2DliF-Wqs2-e6A1Qe3Qqfoa7O11q1iiT229vEXkLw9hcrsue9fSh1n40RU5ww18Nhv0wQ-TirPNwUHoV4n16gAEq70jFZR-LVSN3bYG4fn-sypti0GRULBHZmeZTlyp-6-nyS7DkIWai5vwDyVSdS3C_ULlPxPsXsyfOR8HWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از دریاچه قله سبلان که در پی سرمای زودرس، کاملاً یخ زده است
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691079" target="_blank">📅 08:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0928532f0c.mp4?token=B2JztS4Bcz_y59S6UMg4Xj9MNnK2OlFyQdcTGhCjMpiekGSy8cRwy_x2XG5lSmAGZIYE2AWhXPFq1odrA3_tvJIQQtlZ5oQiBHZKutDjIHNcy6DC0Tp_Div__yfxmfOl4JtQ15WQb-o9cgkh5rjRaSISGNcyCx6-IE-fB_2BNdlJK-PG0kiEDEQv2h3CLOI-hV16i6qu8rO8N6rVRpoE_dT9zCxq7uH14aac9q2CaCv2QCWTPniUBbF1bI_rq5kM6ZXYXA0AWBcL-j4F2KZSNc1YlY0u0z5tbg-MfsuWC8XXCfhxPsHZxz_684xLdbIZjsGMiZoL3VDyiGT5qqaOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0928532f0c.mp4?token=B2JztS4Bcz_y59S6UMg4Xj9MNnK2OlFyQdcTGhCjMpiekGSy8cRwy_x2XG5lSmAGZIYE2AWhXPFq1odrA3_tvJIQQtlZ5oQiBHZKutDjIHNcy6DC0Tp_Div__yfxmfOl4JtQ15WQb-o9cgkh5rjRaSISGNcyCx6-IE-fB_2BNdlJK-PG0kiEDEQv2h3CLOI-hV16i6qu8rO8N6rVRpoE_dT9zCxq7uH14aac9q2CaCv2QCWTPniUBbF1bI_rq5kM6ZXYXA0AWBcL-j4F2KZSNc1YlY0u0z5tbg-MfsuWC8XXCfhxPsHZxz_684xLdbIZjsGMiZoL3VDyiGT5qqaOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک وزیر جنگ آمریکا: ویرانی وارد شده از طرف ما به ایران تاریخی بوده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691078" target="_blank">📅 08:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
الجزیره: ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد
🔹
نهاد تنظیم‌گر بانک‌های ترکیه اعلام کرد این تصمیم بر اساس قانون بانکداری این کشور و به دلیل احتمال خطر برای سپرده‌گذاران یا ثبات نظام مالی گرفته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/691077" target="_blank">📅 08:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران: ما در جنگ با ایران به‌ طور قابل‌توجهی پیروز هستیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691076" target="_blank">📅 08:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-C-mGbj9Yv3qCWyr5r6zBM9XiHrucLNDyn6ABzbFS4RMqTAk3aw5__Tbey4AQ25DZ3lqsk-Ld8Uir_QUaF4Jcaqh6_HesuYf1TvUVvGDGW8hOF9DwVDy9RO7HcGx163mK8fpYdGUbNaSi4mQjtKEU1rD8mgEgXI1JbLJgoBWNkgHHvIyLGUvXwhYNRrfHQ7L-6fSqKRdpQCQqhcNdiysEDVgSB8_kXmQ7kDPB4wBMJhQL0jlLvl1_3Jc19PUIzvJNTP45yIvI-Y4HQNJJ1Dl2st2sM88Ygdr_Dgm49yXKDu1Cgpvcc6nszxLTP1SjZNJXRU-2hRGv9-ZP-QNmOhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری منتسب به موشک یمن در آسمان شهر ریاض
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691075" target="_blank">📅 08:08 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
