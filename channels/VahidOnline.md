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
<img src="https://cdn1.telesco.pe/file/caByYYjX8QXRQyeERv_CIvEF4Bzs9vlZdb4Qtyp6LGi7A6yC9qhISzV4BkgvRREbP8X_WGtZiNwqECGaJ2NPXFoLuGOcNaKg0RxOg6wjDktbGrVwg9S6I-bF2g5qxcXPWkxeSu51gA3CfR2k4pegAikg2HmjEbOIJe0UKUWtf23t_n7wx1v1Tbnqhyam6RJA5y7Rue7PKE4QJor_Mecr2qNxh81XWMxP9EFiEZ-lUZb4u3uJtXtsXfYxbDjXNyrpvl3gohYxT6GgRf0tYJ0IDeDtJwjnV2JLwQb2e98ZvSP7SagtFL9ml-VCfGvw2WvPUAAeYRAXn9mxrhEgcuZvTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yqj4NIY9M7KVpQhlZBo97U3GSlAOtt3yVXatQV0ARn1A-VcH0jFKlyIpj-b0GLIqMKLylMbpISzOfwKd3T-QJooHTpLAXrg8sM87d1XhqtqKSfbmTlV9EqAXvW4gm8sQ56Z9kyNNxp8lHYFjCYPVAJRtym7Dm5uD8c5a1FgGS_eY1ow9FmYkRex3U0jKw5Cz1jTapvMZTBvbbwNDGgM31SkeJqcyZhzfqyp32MEm9YmO4FpByYIfW1tetVChKyWdXA6D3NKweMQ5o-5FYhg85LKgTrqBf7lF1xyFctwNCknwT-UCzlO2ulHUYkRztgYXoAueL9wdnUih0aW5_cCLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHZRTGiRj968UiuuLUAPohZGFehw-4r3-n6ii0vi6EC4Tx0pKuyyIxD-v8eW3oifWOilocCdQ3YyPnU0wh_fGGj7GgB9_HcKbkR6kTJGc1Alh50tVNBFI6iJE0kWd1hFyH-XT4-PHpUkEEOMCgSiwliwQ__cl4a6QEjE9jo4F6Y2YfCQCk41_swvfdiFJYiXhy7qsEDUOUrW7yRntmfbZm-RKpWP09Myb4rhyKhVOQ9xjAkTYW9fRlr5cG98nST1xKIUpuFj1fAeF95EtZ_ea9WM5QdUm0S4B0Md0vj9fxQftHbcsxfRB5Y0mrMchgGXwb_X8csZ5pVTdY5SS4YYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgSQFBHj-yiMAXqpKuURQLmw_C7E_bJOe8etnXokkDo6I-bWAe-f6UQnbJbYrqoliynJJyDOtRikTr9gg89dVFZnit1Tl-LF6qVZCLAewsz_6KGPsteZbsnivbrhEfnONCQMKFhbMWpvZ0P3XG3Wca7damHUhvZzDpBqcNX8Xh_Ew-VIjrQzd22MiaZzXh2xG3X6ZjTosSz6-pq3AXIhoCgL7Nho9hdbdkssBQdHzAFN0Va2cCI7oYlKAVKQw1oTSFUVP1ZBNGCRH-UINXDFt_fyTF1nx-2al0TKdTdM7KbRuAdyI8CZLcYkdPt0PPVc7o4ttEMPCyrlKU-Z7MrijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
🔸
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
🔸
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
🔸
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N6RowZi7F80x67_5_cnGlW988wHZfiMcSKeGSdEfoWIIDEmoZCq4Y7l7BtPLAtyDTLX_NbSV9UOxdgmsR6IZiiw7WigePJtTnOF1SedMSTlhOQdpAwnPHzoKkIPzELeaSaiz2iD0kxJYpHzzw-5exbhczR1laRtd9IuRiMYYc9pL1E2gKRXeP3nAG7s7T0FvT8AP7Y_IWcqIIvoV5VKZBWLc7Uf4CUksxhpkL7BxBEQ162jQBHg0jVvU5YLnrm1Wkr1VPo-nmUPKg95_Qa1-TJMSHUQk61xyvRREIyxujFIQjN-LuSoWfnVQ3i8nPY9iJDEXJPEPI-ZfqzbGotoVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gpLO0YeDvgBKg7rtzhPf5-QHLLOD2UJHdCZjhmb2Nx-sDH9U3eitgaQunlAUxCP909TEdarW5jsxa5g8f1fJ2cMDCom8_TsPaP25Mqxz0EOVNido1ypgnJjLh25M4JTDL7XwjyG8rL7GfRcc5TY_UeBo3Xw72XrZey3eXiStptNYcGy4s_iCZIrJl3E8PfhvL_Mln6nPnToPkOZSIgcuo2z88DTDYkmcgY_2GdtOoyuLfYbFFiPcc9YRbhC7dtN78UfyPYlcIc3od2C0iGsT7IkbF8x5f2DXpNp2RLErhr7wmDVa2p9Yqocm2g2sRuJlKT6zpAd6kqoC4fIOQlmD-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t97QpOoqYn-0EbB-mLMY4R6sDHKvZu3FhKsIujf6ZmNvQH0DTUuzIJmnMF_o8NcNgz9CBvpd15DA3nPuANhYj9G-3F0rUp0YzYKxqR2bbJc4LXJ1gsIUwJ5BMpG4qJH-mH2WOnJ9ecmFgf6LG7hDi5J-KHkImt9iR5XTzhKLKYmUbLz36Uzbz2IXzECF16KZVVTRFItCPgjycxXAzWPKf7nsILY1GD6Modw5ty5vdeUDzVEdmLmkMn3IoKHBFzzxFXh3-rOE6kByk7kYnUNSux_PWhxU8OLFqEdfGcS6UzvXqg3vL_CxvN9myz27Jll8GEgUgYAr_RVdaSBMv-Dz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jwvnyv-zJEMlJp1yUDaEyXFJa2mdTOeMx5Spa16k-9xDgAF26Y_pA9SdRnH5_zE2IouaMcEhoEY8d8qvZmuVsR9CG_8d4Qkav5TsPJ7W-TgVqwztgY4U--KYxTBUCVpTBzN6lUmkngYJuPXP64EordAAnF2oBfv7d_KWrWQe4zLvpDpEgcgsiRx28AGmQok528xYnlcHyf71fV77lmGucmda9BeHqr-CDUW2etsYtY5oerxeRVLT3uQWfCKWXY5xoEkl_TWFrIJZLUp5XkqvA4ptsD8gSfW06fOGxQpW7h5NVyiMcNcMwtUQ6QEtHTNL68dnSX98d5fYMjsT5DuH9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vkYj3WLZi_HBWssb73biAFWJ7zOp4Vx-gl5dxt8xcdVKIx1u43dlImSX1L9K-M0FBxBBXesqy6nHVXUEkUJvNlPOQZuGxUZb_l0P8roXQYVPDdThugd8MZ1d3GwFs9UAG4mOf0zG7I_1lgvc5fMYZSQAi_XK1JxyxCMqeqUIJAYy2vK06x3OE9ldCku-eRrPaInOsISUNm8Lxd0vMfPjLzPOuDHsooMvehRPc74h9oyqHarM17r8liiCbBLyuspOfYv1HxFprPGCv3AfpXK-DheebvOc94wZwkp_Ex4PrQsGipqH_Hd_wvO_kwoZWOp7h-80DlLNosAnYW36-qKxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBIW1psR2VAwcik-vWF7IV-lR3P0VIu9USFIQKxV4gXMT0s_UJPh_jwrwXk3yBSn0C889UXzwFHPTuSb4tjQVMhM90jyfysT5BtJZuRCOsYUzL5pY-hjBLgTkF2kT5LAjKx45iNYqEPqzYdKSkMouUCodEVYg_BpnDaqmX1delWLIk-aBdeJOeIcUpZi1HA6Kd812Wl_s9JP7e53Yt8ML1V8FtY_qaOdZ0Zx2ptYFZv-3lxa_0hopOleHZw9ImOXTEzNvLK_RfQ2NwAStW3AqlPkxLqphISvFfcP8tBj9I9E41Eh3wQj9ZPYDueSh2TpdjPX0Eeha2g_RFYZTAJs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr5O1Gw4CVcL4zOxbuOZk7-wpoiAPrX4EJ3jzoMFUGhcykVZIProjwNeAw9vRxthpodCoPKyhNhzlW__dONCInI7idKPBVVWWG7LL2ZXCaKPIwuvimbItDD2XWSjPPj2otlcYn2PXzO3uL-veDobP53yAqaOhxw5alzB4NYEF0BpVrc30aCh12P43KLSkR02mbqgtzpi0cqFmxqCmgP-xPox99q-HFygTSJ5KmiogLdqbhB6yLTXIwwpg7FeV0tP5e65dm1xan44Xi_YssDcQ3fJs6A4g5alhnhZix0q56QefvhlEk6PRLSAdAZU8qxjDM9fpJ2EaDIDaWH5gp0z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=LqHDt1RO0v4XJkLrYYbjDgdWSvZjWKIUM90L6b8OIbf2oqDf7Gp4XQs7nuPeAJ8EHEFTZ50kpViHTeL-Cm2wYhZv3n7apy8MpjZtTQbr7YHgZ968Zg_9lDR9FMjR2vxXt8fb18dneS0C3z3gAg9_8C3_2CcEvNf0DJSFzRDnTvBV5waIDEtsCR3rrDcJsCf11s6IlPDdt4uUo_4FgZ2Q4JU0NMlstQRfjIsLOvV7cIgT48OtjONqUz-MxZFYOii7vezDaSz2N0Jpk2C-cbpahQk54gsK2SGwV-YU45mWY1-WTFoeRddtiunGdtNDicmCwzHYkz_ddPniCsIjgwjE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=LqHDt1RO0v4XJkLrYYbjDgdWSvZjWKIUM90L6b8OIbf2oqDf7Gp4XQs7nuPeAJ8EHEFTZ50kpViHTeL-Cm2wYhZv3n7apy8MpjZtTQbr7YHgZ968Zg_9lDR9FMjR2vxXt8fb18dneS0C3z3gAg9_8C3_2CcEvNf0DJSFzRDnTvBV5waIDEtsCR3rrDcJsCf11s6IlPDdt4uUo_4FgZ2Q4JU0NMlstQRfjIsLOvV7cIgT48OtjONqUz-MxZFYOii7vezDaSz2N0Jpk2C-cbpahQk54gsK2SGwV-YU45mWY1-WTFoeRddtiunGdtNDicmCwzHYkz_ddPniCsIjgwjE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XxtEJRKeSooxDJIcYGtFRXEqVWD8lQ_4N7dklwJfYveYJl5ZEgT3m0HUQ86knC4wN0VGgeOtVs5lNbkduVRFCWNG8WJxU8QHWrt8eO0Cc_FYVMX3kAn4qwFnvAFKGojuGsBt791UCOZmF9D_2eaWpy0312caXG8wPqV82vE_jMKFavdKYLewl-f9g7eIybnoUpV5LWMDMQG9FVSMRiDuwBfGQ9aCv5ISLOL-FkQWvEMnW0fMPP5cYpMdWYfKjyq8H7y3-KkNINW7O4Q_tOsxmES1IrJx72NeWBTEPt0DKruu1lib4Cixz0zJsf_ChltbiIM3up5Ij4Lik_DBnKQKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VlpQtEeondwLkR4SQJlLcRN1saeKepKYQMQeQb3j2RQZuEvKfgc53DqLOpZe0HJ---TCYz_qOZ92jpG6SLTTsaSjs15AXSmjaQhRA5uUf2leV4bXW_3wDc9apJFgC8eXvQWDLGln9Fayzv4v-1aQBgiVzCVpKJwyp4BgaeUupjqbwf5-5tzMy-kJYj3hKGfCYL9ZaHzGQkbqi16GoUl_Qg93KzEatgtwMZPgjc9oY9uQ2-GnwIlRPQ2issorgHsAelta7-OFR_mqi96_PnlYyH5moBbeHhhV0pWMb2d4_bKTJ6cbRkVnTP63ltFwg85IjnGdTLrag3nHfSXuw6bcsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=YFJ5IBX8i0StbH7dw0DtutKXVZK1G-DuR3sTY2hc8bUoKGVTvNTG9dqaoNfv0qbJQ0qkAcEGscxBMYsx7FshtGrj8S2vDwyeJgJMhtoshevH4wWcC5nQePx-W26Zo1EWaTTL4OPlZbvKO1macpYvsd4HIdirUqFmOUug8LoU7d0n0s9zUMHS8caMSokg4BeQgoxlMpeQCt_i087l-Xd1AaUhpcUTxjiQ08VUED3c6TEl_KAN4knqL_wqLVm7Cvbphlm3HpZ5P5OGYS6FY9FqcZZDpnUlQopHJqASh5BUEFkVd06orh1GdUgamxfrpMD-znqOwaWsGDb_0v0rZIF2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=YFJ5IBX8i0StbH7dw0DtutKXVZK1G-DuR3sTY2hc8bUoKGVTvNTG9dqaoNfv0qbJQ0qkAcEGscxBMYsx7FshtGrj8S2vDwyeJgJMhtoshevH4wWcC5nQePx-W26Zo1EWaTTL4OPlZbvKO1macpYvsd4HIdirUqFmOUug8LoU7d0n0s9zUMHS8caMSokg4BeQgoxlMpeQCt_i087l-Xd1AaUhpcUTxjiQ08VUED3c6TEl_KAN4knqL_wqLVm7Cvbphlm3HpZ5P5OGYS6FY9FqcZZDpnUlQopHJqASh5BUEFkVd06orh1GdUgamxfrpMD-znqOwaWsGDb_0v0rZIF2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=J-yffbEo8F7mZtp8Ok5EciiVIEP84a9UxwEj2aFKROong77DMR2LqtuQGqcl6Ci0elldmPuf3ToqSwkKGhaNMDePSZn8TGjoRa9cSKL2PCjwW7FPhYkeGuyTAmnHRDbePv3S7vYcpD31XUX_eDTm-dk5g45o2GFHdaS_HAo60t2E953xSKR5mj6X2E1OnOn6QNWczkKvlbLRn-GwXbYgeqZdE_5g45-Hmjn5YkF3ox9ctFEW4XBjaEFeodhovCxBwcwNVGuBGA5XOH-zGw99Kvwu9oQqDNTKI8RXiWRC8Xwopz5C9BwYUFgGeuuYs0mwE9y4PM8USQufw_QwVeLvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=J-yffbEo8F7mZtp8Ok5EciiVIEP84a9UxwEj2aFKROong77DMR2LqtuQGqcl6Ci0elldmPuf3ToqSwkKGhaNMDePSZn8TGjoRa9cSKL2PCjwW7FPhYkeGuyTAmnHRDbePv3S7vYcpD31XUX_eDTm-dk5g45o2GFHdaS_HAo60t2E953xSKR5mj6X2E1OnOn6QNWczkKvlbLRn-GwXbYgeqZdE_5g45-Hmjn5YkF3ox9ctFEW4XBjaEFeodhovCxBwcwNVGuBGA5XOH-zGw99Kvwu9oQqDNTKI8RXiWRC8Xwopz5C9BwYUFgGeuuYs0mwE9y4PM8USQufw_QwVeLvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AF1MW_zd1y_IacijIrNijclIcgAi3VFEo-3D-vxUJLNVGrWxDP3PjxOWehTaKp-RdArqdURVaHWaC3DPDS4TdCk4A1H30CBpdzuZK_514njRsTZQlDX2UwDy6RJ3Z4uzofYPQ87AXFmKvt4uByn2iFPGy1s2kfcQKBWqJVhewLxV3cWAbVkg7LLMCzNvW16wjF5PidCQ0WSGTfp5-DmR5eG-XCgAfXPSwBFA2UfJUlkqJtjjbP3Oo0KqHjIlLnN18vzFZTapead1EWF18H6LUy140XHYmyQhMbWQ-KmQ932TAA_UdZLZZCrti9R1U5pSUBL5V4l5oZqn-rcmdWWKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HIJMR4hcZNgjmzcGBHVZQOer7SrwSkDOa3LLJ3k3aPZvOHD2ObbyZ5Cb6Ch3dt6tKVJQ38-KRLLNrYuMD54hXNQfCWE3j1dgYkeOjK4V9E5yBH_E6wg-VZgCwYkZXJOYEQG_HbTvfXXOtqmzKdNL5_QI2h0oyVryPalcvarMUKSZx0LAh7m0njp8afzKb2M2meEBbsuOdDxvNqDhs0KjsaWmzaMr0xpLKNDLkpSsqOpk_96DvY1AX3LMzm4fdNXtbeMTVFI62NaBh5ui0ZNpjZMIdIC9yT9mIhULa1VSSQTnlAIaZtDZQWsmjXbzGof9iG1nHlIVACVCw8yxAVoL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=dte4DisypfCtZAZOfdMC1bilcYcM8NHagZYciQBsDDhhNA1Q-voXdR8PNsvlO-68jPPNT4ocoZPgzXZ-uvWmSrmV2mwd6vmuJgkX0wZDHFNvjl0zDl-5BMBlEZNSDCHmbHDEOIAFL7XHn77VO6oFnfSdVXDiBVF_5d7TcUzKKT_xM9i9YFGLvFRjMhfUdnJnfgZ5bku-LQoG1aZqRzspnBfRI2TSLJhUY__hhQMOBDDgzadKR-0S7X6EcOtgNbcNlbJXX5HVbF4BGAOGS8tjkSSd0_tNIX3Oi4KJpAd6ACC0xKOSADOuoPHLZPqXPe29ZavqDygXf8mMGuKkCRWivg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=dte4DisypfCtZAZOfdMC1bilcYcM8NHagZYciQBsDDhhNA1Q-voXdR8PNsvlO-68jPPNT4ocoZPgzXZ-uvWmSrmV2mwd6vmuJgkX0wZDHFNvjl0zDl-5BMBlEZNSDCHmbHDEOIAFL7XHn77VO6oFnfSdVXDiBVF_5d7TcUzKKT_xM9i9YFGLvFRjMhfUdnJnfgZ5bku-LQoG1aZqRzspnBfRI2TSLJhUY__hhQMOBDDgzadKR-0S7X6EcOtgNbcNlbJXX5HVbF4BGAOGS8tjkSSd0_tNIX3Oi4KJpAd6ACC0xKOSADOuoPHLZPqXPe29ZavqDygXf8mMGuKkCRWivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjLFPNSktVda51B0qS9uFEigschMmCdUqUp9dKUsN3sIQOPCArofDUh86Qf8pP__xWR320vGRWmpV4g7b6T8Vx-78PTj1gqcpj_Gg0MXuWcvwIWQaJ0NK7MosGC8JroqoHHopzZ-bfA0-jjwGZdYR_k-uw4d9vchODIcACl_MY7h2jyv5ao1ZKoPQJWnE0KhBny6FcBeIpzq02d4_-yuj3ksX-HSws2VMUABA6518yGk8nqw7yjelp8AdsmkcfANQZx44yuTsKzeKCCKcs7i5PZK-Mb0udCXaSpUMrLPm0mhYnjlfi3cuT_Wd59TmIM-0OyB-k6tn00gl9gNsL1mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD6SBGms6eETITPapsiw28Q1EwlkjzVTNqQ8eekbLsfb662KxkhRmsSRV-KxPdjSSSMN2ezIJz2oeIoKBt6Ii5SJRH2dukg__4DzlYWRoSThPl9TPNR2jz3VTaqB34MsGzPLTdTYCtWqvgEBHyBL2rC9MD0TxQxI_zZBh8P4-k3TwdfC_8Tz-7y-e5sK8OigbHSablZMQ2f-keuvZh6IpjCICe85EDTklVczRCpkdUJ-u_D-dH6HdPkN50506vDTVAWxa3wyWsgHiumBJD2TWvoSj2ZIu55Wu-Ch1iXyOWkxo5Y-_-1xIA1aw3UptRejvuu4pjEBgLteZb7ljRsJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Krf2OnF95wXjF95pQRn-JiWszV_rxGpmffTPf16vgWaQz5lRur7EsmAXJJIFvbmD14t5DX1Qc4UOVGJb4WbevnIw1uN89Ne8o7hrtOTUm1X9cdJnLpjBPDPgbsXUJpRyjqlvSB8YXOUdf4hFefHm9hfw4yaS8b8KdR7Mcr4K_hhi9x30HGd-KYi37ncSlPw7-Jd-WP-4OP--2zSWgBNVZVTzcrqUBVvlZpx2msVxmPguc62pD2WVIEOgimvURC2Zq8RkGjAe76j3LA2-p-1pdFiUrn9XJvvvcAJ8BZOsMdBBlUpo98GoLZ0VpropfmqoOQD3ujLmEDmh7K3-I8VayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y95xYGQSTZJL3nWYkDK_GAXs-mCGIzspgBXmOrlAUa42mEGnMdKiogE0F9VGpe5r35DAEFO1FSEWwJiRd4Pv2dY3MetJV4bnJY_RoGewJi9rkn57UH5HhGvAbQnX_p5KVqYsHeVqoVDQb28x6PuF1TdE3yaEefA0RUT9QbBu87EANB8aJslRFKqQHnk4v1Uf5QzJnzmHerZaZFjfrPfPE26nr7e0cJAb16RPOfuePx5iTFhJK5ZVnxfG1ej_hETpFM3SnGk_E8vjg095jXTwDX7C9jHcByYi1pALhaIkdhXz7soVUggzElYl6gjtFUgTcC0GrvIiYdJHWR8aXguXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EBhgqmFFViLGxuQ_pA9_8IG-pPirvakxri2_jaDmwJsP5K5ufjkaSGNQcnNZDzimT4CyMQnsBb6VbNvhC9CgJ75UmF18tixQ1pFv2d_PC6UK6xTm8EByN64krKOv0wBKbu-tukSTqbvkmIeObDDbpMiVTKerXn8DLBKZKbOCpsP5AAh_kVWhcFsIDcV7Gxjs2cHLKyHRh57F_YCXdvulYya08aoLQDfj-3SxkuGenn9jW_u4NjzNySR3IzN9lqbbu71bat2LKvdfotA5Z9qnRp7VHkOI1WgT4R4rFlA1yZ-QGUuEeQtr27NK23rlW0jpfl-jqoKelbW6qWmKF93dWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqut6yiMg8S7o9KEVkhg3hNub0sZ0KUvA1QmGqRrdWZ8W1N9YacG-auHA2wdfEO9_3ITdXcGogS0JnRl6kSaDZTH351oYPf0-OJvkygJCqQUKJ1XsGYfMM_2uApr2tvqhX8Xr3uK0HL8e_s7iOwh9AnsvnI4olOy9J7xulnMgva-B50Coz-9Oxbk0Ksfi3F0bQHerGOkaPbg1ENtc42mSdk6ym8xEGAo7XWbrZEOaJrof4N2t8MPyk1GveXuiPQDT1gBzX-RHEIaYr4WTta9hUj6Pc8HFE2BfiP9guFPGY_YK4aV7X35fr_tDaNAfP0ukepQt2Ri67JD09vzl8lOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hl21fIhvSaYYKclLJfPsnxnVQqKiV1eCWpAszxh02W0TUpO9KNLBHZZl4g4SepwIgA0lu9rxH3EVJ9KdLzP5bNH5zmFaxqwwohpXqxbiOT5FssSlg5HXz7qffwgA4mwimVaFxk2ky9n5O1fHjbFC0IZYYIgzmwvSGeo86kxlsGFTpVDIn1eMrLvp5Gtu502-OTI_0hIODMn1da6PeA08qv2r323mOZZxAMZMEtM1wZQdmClLUt95eVWtbNOtuVctXG03QFhkY0ul-rFjan-Tf_nICyTHdYh9FM3knmXyk39slq1iSx1Lo3zbRUDEU1g8q9IKqT6ZGDgxhY6AY-ZilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=Jo79qDTskUFOePwVB9B1XaWzsdHMzFXbILfFB6Gt9M6IY6D6QR_zx5qIO-tdBnAwMeAkWP8ogV6CKE8l-zl0goznJGVdF1rZfnhoaAiqa_pPtrMNGOJl4E1vjIGxSttxH9O1aOHYzW9vaXLl9H-7bV6fR4RJ41LDgMHERrMR_x9bc3yyKW1I4jAeW4UzMr1fXswB2s1VMyq8VEjR-9GA5ROAXRWoXM4CuT8s-zAkWYG2ThiepyCMyYNyvn0WtqAvUoYUoYH9jp-6fx0Udan9wawiOij-Ye9LXneK-p5jOrB2AfNtJFIIl-knIqUeGkUpMp7VfYrsNExP6-mP7RbBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=Jo79qDTskUFOePwVB9B1XaWzsdHMzFXbILfFB6Gt9M6IY6D6QR_zx5qIO-tdBnAwMeAkWP8ogV6CKE8l-zl0goznJGVdF1rZfnhoaAiqa_pPtrMNGOJl4E1vjIGxSttxH9O1aOHYzW9vaXLl9H-7bV6fR4RJ41LDgMHERrMR_x9bc3yyKW1I4jAeW4UzMr1fXswB2s1VMyq8VEjR-9GA5ROAXRWoXM4CuT8s-zAkWYG2ThiepyCMyYNyvn0WtqAvUoYUoYH9jp-6fx0Udan9wawiOij-Ye9LXneK-p5jOrB2AfNtJFIIl-knIqUeGkUpMp7VfYrsNExP6-mP7RbBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjyEpJyTd8pNFKxJ-KSqhU_OFvPuJzZNeMxYSMY_f1vi8PzOJDZxurk15i_-xG_cqI8Ohs_ja3osTSZXwtD-_g0CPk5XFCo8VZvZoKEHDOXlbzTfrxMSHbuSF6Xtiq-DBQPY3bQwe33HwYE6RdBdOh905VAds_o_mzq3vwbOlfPcaXx6NIItorD0kXimHpHLHle8Jc391B18rHV-KC5V9ytvT3ZxyHRUOsUrrPyUzNxs_1_naiL69Psh_aclh7BFZDqO_6F71UTimxVkmLz3yvsxcg-VehTqeyktOGRb6NENS7orWOic0ACX4Sb7sIMJo18XK-rjrY6nsJbTtuxG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=u0ANvaZRPs1UXfRJUJAfgnBXFZIwKWObd1dJvlwhqnzTBfYGvvUjUk89fdrDK05U318uCe7YXbedD--jEQqCsE5qWgRJNhmdOudDxBf-VDE5kGib3I8k5woJbzM1riptFbsm5kNEgo8F7-qNfNEt_m7RMo43Lu0Oy_Aqvb-3cE4aNzvg7xH5Exhn7TmsAIbIhmjkQwHji_z7TkSKjZIloHAhNEDOUPeZjm96J8bhZ3oahitubIjiub3UACjq4YExvQKbNeXxBkLQCeM-j8MoWXWTTpfnRxm29NIHB3pzqqa2u0KV4rs1NQCqeF8s9zWjn42FeOAkZxtzEpvc7WUCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=u0ANvaZRPs1UXfRJUJAfgnBXFZIwKWObd1dJvlwhqnzTBfYGvvUjUk89fdrDK05U318uCe7YXbedD--jEQqCsE5qWgRJNhmdOudDxBf-VDE5kGib3I8k5woJbzM1riptFbsm5kNEgo8F7-qNfNEt_m7RMo43Lu0Oy_Aqvb-3cE4aNzvg7xH5Exhn7TmsAIbIhmjkQwHji_z7TkSKjZIloHAhNEDOUPeZjm96J8bhZ3oahitubIjiub3UACjq4YExvQKbNeXxBkLQCeM-j8MoWXWTTpfnRxm29NIHB3pzqqa2u0KV4rs1NQCqeF8s9zWjn42FeOAkZxtzEpvc7WUCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uI3f1pDskdbuEqmTCilMTrR_33GTVlx2UHw7aYjlIenQUhX2g3UXj_tuNT-8hFxM3GFxmr7Puv8dJzg1qyghB2hRjMXmicoy9P1_SXPOXu2V104lwy1uCQSFokLQ_Z96vW8BacfHd1jJhKGaxYU75rRfqNnz2I9qxmrR2UULGw5cd8IRKCwaN3tLlt3sSh6GrrUx9SlD_y7Ykj_gbbsyTf4OIot6ihjn2-xxcpSh_KxuCPH75zYdxuivrF-Xm_LrEq71OSf19v_uywPieT2KzDyPcJ16WsHV1-zgraZG4eSOd5Xigu5iSOcBtSfVFV8IBBMfmh5L_Ks-sBnbe2H61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=lmZhUSu_k2EjyTyJE46J1tjJpvEgVMY09X_BahIMQlzmpnZRZWf3iCxpw-4bY41JtrL4NvdmD84_6Zkp-Oxh0UBQ_dE3AUgI5HT8FlZR7nNFn1x-D3hE2j3HrtOL_9jDqV1FNolQS3IHJCIMmerin-T6C0a9zgsENl-oW1DFnefZXI1qk-3giTgC6mHWF_AD5BqEVr8ta5-cELL3pfr858yTvStpUHcZDlVv1kW4kArs4Xmx1Oaj4w3ax9C2xW7vkEaWIN8sVyIHspXjnoCpItSEuq5gq9RyoAp2qjYGFXTykFrnN0upIthaBn2jVPjWHpg5PDhmIt2C8NRY3M0yfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=lmZhUSu_k2EjyTyJE46J1tjJpvEgVMY09X_BahIMQlzmpnZRZWf3iCxpw-4bY41JtrL4NvdmD84_6Zkp-Oxh0UBQ_dE3AUgI5HT8FlZR7nNFn1x-D3hE2j3HrtOL_9jDqV1FNolQS3IHJCIMmerin-T6C0a9zgsENl-oW1DFnefZXI1qk-3giTgC6mHWF_AD5BqEVr8ta5-cELL3pfr858yTvStpUHcZDlVv1kW4kArs4Xmx1Oaj4w3ax9C2xW7vkEaWIN8sVyIHspXjnoCpItSEuq5gq9RyoAp2qjYGFXTykFrnN0upIthaBn2jVPjWHpg5PDhmIt2C8NRY3M0yfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=ApyiBqUWbOQP1WevtRWSMh6qOJyt2l5Ak3hNU452xTYlC87uO_WPLIxxV_LAcXpyzrZE2xcywhGR2IhAOpThRw3db2W5TMhFFlvJgCNTu2dFHPLqIWNhrf3xXlEtj3mmVB1B-hnpWOkpPYt7Ns82KPtGdRGlMlocEnpex_fNSz8SvrJbrdDyxSO7-unY4VMveezfaYsmsq4CYFETjATuobmwk2eKRSPDrZHOKYEMGdEpZGqs-TjZapi8UZ5UaE2pAac9pBWmbHkpNWginxMPPIN6hu8EN77HhBIboLlC_I8xtyaTI3Ni5aCzCdCfOq13QUqmjFOpb6RJK1u4lrKzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=ApyiBqUWbOQP1WevtRWSMh6qOJyt2l5Ak3hNU452xTYlC87uO_WPLIxxV_LAcXpyzrZE2xcywhGR2IhAOpThRw3db2W5TMhFFlvJgCNTu2dFHPLqIWNhrf3xXlEtj3mmVB1B-hnpWOkpPYt7Ns82KPtGdRGlMlocEnpex_fNSz8SvrJbrdDyxSO7-unY4VMveezfaYsmsq4CYFETjATuobmwk2eKRSPDrZHOKYEMGdEpZGqs-TjZapi8UZ5UaE2pAac9pBWmbHkpNWginxMPPIN6hu8EN77HhBIboLlC_I8xtyaTI3Ni5aCzCdCfOq13QUqmjFOpb6RJK1u4lrKzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=XHsXmcffQZhbJjSpUmCYtdtCMkuEzApNmH6uDF7fLnUEpk2oCmmLIcraR4rYv4BXtUDjUh73crNf3fEwit8YOxKulQ50dFCmkz-9Vb7WL9wrXMWlBGmAZKSGapkLo12HNndihQhHHwsL1t8pcY2TvRNg88x8PoeDMbXnlAOj8Vpdv7hDezGVsptLK1h55LZoAP6XyCJQ4XiTeHNsITk13k1I3dXnp97gjmsfcy0UL4qMytDKOpyXHniK9PL1w-gAm0h721tvjEA8kZ4UGGXDdZPL5mFqaXmmmf5MHCnFINyoiKUUG1rm-c2J5Q052OQ9YQgJ0ciDM7au1CQ9cXsK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=XHsXmcffQZhbJjSpUmCYtdtCMkuEzApNmH6uDF7fLnUEpk2oCmmLIcraR4rYv4BXtUDjUh73crNf3fEwit8YOxKulQ50dFCmkz-9Vb7WL9wrXMWlBGmAZKSGapkLo12HNndihQhHHwsL1t8pcY2TvRNg88x8PoeDMbXnlAOj8Vpdv7hDezGVsptLK1h55LZoAP6XyCJQ4XiTeHNsITk13k1I3dXnp97gjmsfcy0UL4qMytDKOpyXHniK9PL1w-gAm0h721tvjEA8kZ4UGGXDdZPL5mFqaXmmmf5MHCnFINyoiKUUG1rm-c2J5Q052OQ9YQgJ0ciDM7au1CQ9cXsK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jv4qZ2lXUPIOByzDFxc2PusBplEz1Wqoji1thI12FTdP5p8wqXdkB5NKD4bTj0aSDpdM5UNDXJlCuHQV74-YaeSW58Hf7uiSEbg4flghKfdo2yFG4Bi2LxNjgT9cIVJy_qmfgeY20MoG3SlOLZunGUI_LVMKdnlPmmuGc_cq3s2XzqcS0luaiiVjkbHGKdzab8a7bkyLX3yrcR3VD8m-WeY1uWMkH8SDHegrtDhozCd8CVuyd90meOYxRl-MEd12tIn_YE3KR_G2jxrntSFkqDBAU9CzF2teul3FwXcfONpmsddXRLHlg9VTdHKZeK1gtJ1k2nE5TP9KyMGAPGO0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsnKWv_5TcbRdePZqSibFnVT6WXHbroBUFQsYaGIybN_I6dGFnL2BME7EMOTuCnKQBw1sX4p1nr23fqGCZkr7rJO8OVOHcpInO0RDPy9Utl2F0ntPKFIa-JhP2HT4Y81sml7XmCXBMEUZAcZyAtXUBEVUx8svNq6nFMHkURnWqNd8DMM3tUIY9EA_el7BpobdeoSRoM9VNCzS5vZyEtLawh2e9hM7MAuYzluXnwemyqzPXF5f8tc040moVAfdhcDmyehW0EfUxdgr4oPoJ4Vu3jqZZrB2ZbirT4mOZQeSh6PdDNtCePeQWHSEXt8v2lvKPaL3pSmfwc9nfaeQF6y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRL20bJ4tll3-ASUdiKVKeOSmJHefBFrG6Jy15zlVxYxoSjGrjrkuK8wR8muMQv0if6KmX07kmfFBDcGq8mA6xoM8aysyFse-HJvCljSEWrX2k3PLmitx7AdEppraDOEfjfiTq58LczB-RCEz87F8as5L4TtSTVlNUqRMNBPg79mScBAorR371q58WDqQc8eSO91iwstWKhg6sBlj6f9OtB5ZJyUZZsxHrJ2teGWC8epYALjGfwhInUNaJrmFyRCS9SByceRkamx1zBHDnHNOI7LMb_qmNNmYHVdeMHCfpsuZwaPzmlV-JSpJZELWP_zxTdGjzgD20srqEeUCOky4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbsZQvTwlxzU8Jj82J-vVOLmKARRroyIY0If8yx1Ovpr3k_o_ueKXIMMok1mP5KqFXWcTJHMax89mqXh4sjb5HjxSn8PJl2CH1X1HEXTwVPqyiMI06g4XbIl6c3fpmXeU1g4lzFWSyaM5qL6t4yKwUX4FaiZTq3L_wpMD0yBwYxK0T65RcRFS4qVNbqtTpqSPZ1dRvWkwBJQccrXANroWmmNfxqYYJy9ZcU9rlx2FWpFW7a_pBGrWZfti8exPPltVnKjqOJ8UrPxyLRc-JMnqpKXLGQXA8YNAFxlevbtFSMsNDDG0XqxdTsUayWGUtv3v0HrAw1Y0Fo9fLQRMF96bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgigP9TTCqwVqh-UzbnscBEfXTiOX39bPYKPDpn_iaRQ6UDQnycAOXiSLodg4C9G36Kzm7uo3xI5Sa6ckKed5hqOMIHPzksG07fRv3wcOL_BpXXRJqblbrRs7UzWaeUddxxkGZhiqLFkykJQ_yfTC5HgIlXKuf_YOoFW9SNAHGy7MWwPkrjvGJfS84Fk4vT6oSwxRw5-7ARIaDand6Fih3QG_7YknA_1W-47Jlv8eq7N0tqhJK_ubUKbQv90v7MxtZJeLOEhWw2fbISWHCquzUr0aMiMpdkbdDVo6Gjv7iyvmu9qHR1XuOXG1BL-5oR3-2K3L72iN9wtl0zt8qHgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-B42IgPNjqXTK99tdX899jKNq3QErZ4aGOz4GIW8lvauCne7877GFGoJ74gNG2qyE5K_nBTwTN408fLFlbmJe425iUA6QRS05jem2sG9TRabDbiws64aHvfANlrc8DCFXwNbFTSMjTKJ4ZGcfOCZa5keazNh2b3iX2fGdRg4KmslekdtAeTx5adSOaWwkargHUykp3f6haLBN2y_94fj0j-VmFm4jBsv4Yv9Kv8oUZj_16GeI2vf0hg1lMUTC4XwZRfFN8oxtBJ_-VGiL8Ch5gCQfd5hlIf0wL4e1G7VKGBu9xdhBddb_61g_QcPR_8Z2vfDKtgQfM-TxUmZ2Pu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwQUc1HSuv0XrZEundGB0J2nlOpQRZaGJdE620v2UxgEfRunVwFUrAXT0E2Q9viWFVsPKYuWGQWWzKM8KHxNRQlKxMy086QLAulLWnYFUFjBYpoAlt4yvorrw95bFtrpAwcu2AKmWiQNXWAE7DfG4btDfG1M7EHKA7v7BktvnTF9FeHlCbeckaBcvj4_66WgC9pBiHJ7F6rfHrkUJZSL6ANxhffFWWkiJ7fdWQoH_GgblljVOm0tPe0t0r12qm9kw7SdJFip903xOOTeisN-lCMXyTetj3gnmm4lOA1FOZ2TugK75ilotK5Tw_71E1YJ9GjsZyveSPOXcm9riE--Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LeD_obsq6JYw96u9dFwCnaOD3x5fDh5i-_qL1Ew3cCWtwJZihcJZbc54YH_RpXUOW8DgkY8pcBOt94tXORNTl9oYM8GKPU8hNyZGmLIqMWPnU-Wt8Adm9pGzAl0TmtP-X-EdGcP_cPM0O0Q3tpgyU95Lb50f_7haN4Ikp2-F4lisLlvEY2znCf4XDrKUXvBmH42K2ge5guKAGo0z4Aj3PEFYOj7km0kcfzNIx1lj8B3G1KVmgWaZOq_AoyxhEeOPYM49IKPVPoZCc7YG9gdvZ2S8K57EJMpT_VW-mnygcZDrHlvmLOZ6r-Kb7R1z61ypy8YHFYN32y_G9k86ADkDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W5m32fbbxYbajInOHWh57rI2fXjevQ5p6J8p1MfZ-gqyu8Wp0iisS-3o-4ZIIYgWu_kTyQ30GFDcZoIjbXycYxWwNcFJ7vbsPTqFnyyGXR45PmkZ1iKDURcOd-yVI0sLpZ3FgSThg5EpKIjvZnar-c4CUdSvyc0hJqBZ7UrkWAuEFezGhJocCz1bLjBhBqx6eN68E3-ZEf2JYnHPai0lp5k_eebhQSHTPSPzrCzHVXt0fXVne3MHhGyUrbJqOA-vERxcuU_-2h8Jk0oZz_0lVRyG6Nikykzb7ICrzocEyMbkfZcc8GZhcGZBnB7L8fSsrY_gLI2uEkoXp6x8GWKNvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqBVJhL-w88_LB-brC7OdL6LL713RA8yiOchj8TC1M7K4dWk0wItfrXisJ8_ENxTdB4TSEjZrw8TdldFVbQQYK4Zxd8eEyRQXAGrhJrHqkl-R1QDdoFXYPZSlz_PD7xmujKHMaUd-vYhDBmmLPlJFChi-V6JIVz9gfxT7SizOrglvGo62cHlMvGI-WmV3MHLKA0Bgef5vo3RG6NLR6QIZ6Vvn5fAYbjVP_SpUa2TOmGUQKeD4huYx8ggA0AvpagLuY_EKfrEuDS5catSvfsbVtglwiVG5L6E32SzXYvkyLBUo6AkxmeZMaZhuvGoFe1X2bNYhneoFG7bUtuw0xNiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8ywqVUn5-R3dGZjfMw099hUsKqTRzw5XSCqZaAIjR5O_r7bHwutvpU8Ag7rj2Uic9z-S758t5xAXXeB_Bw_LNakoCdCJpMiAkJc7LGFODO8008xO7poAzeu8Z-5DcPuYBZgc8pdsCLBrFoYGRCU0O7qFOHvbelmU12811zYVcpd7KTAQsqhyoWMRDIdV8ShqHLlIV_j67JoO_hd8r8T-Srx0zZb4CMkUVh09OYVilpVen-44VNrfAS4DRL0Tp10bhgpeG0CibC6fo9mcdErNn1syUDMsny0QuWdwzsjVw4PeSIyH-ys7n8VvJ9gZ0v8yVDBMrZFvPTu_ZFBTsgz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FZzycmfBNyYU-THrr3BzdujRzDrPax8sVEK7pggAvMZtrMImYrJ-0WftomdgkKZKvEVcniuC21PO5sNR96CfVqSIr0TmdqYeE_EumoWJhem4ePFvqytDMCF4ZlH6knqMQ5GV2iKUNO1U1fex1N7P6oEmufM3W07AjQLqbTaGE_wsLoDKSguqVnruI5BmZ2x99t73AmJGa8cv6Ysap12Rx9ROtGSJnrMsa3TGrcPaAymXU6FaB1V1cokGxfVZzLR6TMpop605Wowiesg2gb5C-SDd-9DrEewXktKjyd4pXEhOF6h0HM65at_ZTeyMxmCimV_huAddUWJfOKZD7kS9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tn3gWW3Er5byg3jbJKHrwNQ6uwCq6nhb92dsfMIBcQx5OZ1t8xorkWoeEMVEhFGdWZ9j3cLJD_C6HIDrbGvN5RODo8POyjd-QMX4ipZ9E_Vr_jl_6G19Q20G6aziEmQ2aZUvY5osQ_ptSgwmzlayzOuM9MQUhkLCAuFi1BaWy-EPuyGhn_xH57ra0OcRCcxT20Sa8_3-8lYE0_oWaaP8QANP3vdH-DTgtRklnAXwI9P8i1QmfPCtwfZuay8S3ZhkJ_4tDWp5UbbS2OZDNhzk70VIPZAaBJgho2ueCKAe6lzaghp_3MGNfw9-Y67SljWRMkx0x5E1bposdULJCLyUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OrIA4qZqHOPxXTR05h9odQpSPF7emTcc6fiqLgfrkRos7knUyEsz5PY27ev85KFVUVBOnEjlhsVLxNvSeb-yIVVN7PXg8roSXLh48l9Zt-gSzrqytwYVTeTx5A3RD8DgHwAZINkI0IsF9Cw99BsWVz0wiVQ1e4_xiFBRwkHIwPosgK781VQNdV2gj7VpbTiZhHhDIvqTgcOFDjp2GfvFddQ_YljlmADY5beJK4JjuzH56p_aGZ8_FGJOFmJebU_e9AmJ-9bBO34S4Z7r54em5BZaxOpGtXAuDKriN31QYKZxOJKvzYJ5rvJUI4cDDbaRUXVaYIDADomJXmj5P5kiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HQr3MlpeokzGUYLPdKQiqfTOapkQlXWtrBQteiJixSJj9JJFgH09XmC4YsIei1oSY9BkmEezvkKClxZr8kFMkdIcDEB_Lb70U5HhAi_FniZjpe0-JE8Fw9evVfslPoRYA68tk5sG-Wo85f9iqKknGCfCYL_Gin1xrSy2uK_y3Ld28GuPvhVOVFfKlrSqOGkiECS60zmnsrzuTk_VCV_fh4O5SSS0mm-l9z8UIB-J3zAW8thdl48TOdXzsnfOcm_3m-XhuDZv3-1mim9KXV_fQqjNAB674xU3pioOoQaIK9YlPFkM_O6ShekQVM3bKN-yHRH6pFxtYTXrWERtR0XW5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=L5G5UX3Bs09xOCzavXq3h1TM4RuVeaY-44SoSe0g2u_AKopun40ugZbmuPbUT2V10DWM-rqq4zZ7kmXyfsIuTYje9RqM5CoBwVxehP3KuGbqxNn46EfvG-TT-e3kTBFNrpHMIQXwEsCeJ8_7JL3FjUsgHXN8xmgn-BLCVIF3VqRADCL6MhMJVsnLAu9F8Yh9xAtuD6UJuHkhHJeea78NNdUP0D_qXJpx8aV7FYj244uNrPI_I8OcoURRDZBi-V2n2uN1kpWEHB-uxewKzi6xQVNQz2C5cjU7xZtFzERYcaia0enYsRSc92cJgli49BVZzg2PB2ROfM6g08FW0ZJZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=L5G5UX3Bs09xOCzavXq3h1TM4RuVeaY-44SoSe0g2u_AKopun40ugZbmuPbUT2V10DWM-rqq4zZ7kmXyfsIuTYje9RqM5CoBwVxehP3KuGbqxNn46EfvG-TT-e3kTBFNrpHMIQXwEsCeJ8_7JL3FjUsgHXN8xmgn-BLCVIF3VqRADCL6MhMJVsnLAu9F8Yh9xAtuD6UJuHkhHJeea78NNdUP0D_qXJpx8aV7FYj244uNrPI_I8OcoURRDZBi-V2n2uN1kpWEHB-uxewKzi6xQVNQz2C5cjU7xZtFzERYcaia0enYsRSc92cJgli49BVZzg2PB2ROfM6g08FW0ZJZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZdN7t2RrETelv0-32NHqABFA5B8p66WWJwmY5el2nJCRHBbhqQ3E96y5rW4T_1Hq7sNLlOjtubeZPn-T32hDhVVMNrQslnOAaEvZj9TtRhB4TJqV6kbjM67NIUQ86ySL-0Ivi6M0Ad-uBfoSObNdoLvrTzL3k09mfFL6JLVQzSe_DjHujSzzut7VXOCxkv0eJu4PR77NAPCgc6DDMbw7E6SUuM0u3_T5MRI_93FPNeKBumocAj7L7MkXFoOz198k-XLZyJzBNfFf4GwptKQ7McHy9dWtTGz8hCz6UJZlbh6modKVqsXXcG_jMCcd_Kgzgxcq7rGun7dGFXBVK-ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhgBoSLBc78_9JoYXbc9IekYvwNgM3JzwezOMy4h7ZPIr6H-g4ve0F8EWyj3V23QTEfkv3B0jrUqsJChy6YqnxsHoKFokfSOZPwrKTNuSLcMnYoKNBLznPIXKAj5lw1ppJIsImDKQ3Ej0zS1uNKxx-1F9ee-Ecd2xVCE8OhAogAT-FP67HVvDT63c-YVwrhfC55XM9Osskt3SWtW_kqX0IEqockUCXVs_YgRY_KGVy81VZm6oaJeT7d5zUIJikzr9HmdHiRry-4mL0dW84t5ccLSVyAFp1J1baNAYSQVxe_nkR3pqUmcI_oe1db7lrOU_ANrZXeSt5TRzyYGuu5QxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=qqanxFtcnDB36RgLI5FYTit9ezuuBJJXkjsqW-Qp20lVWsBGG3W8whJ1m8VjBwpAvYX2RqEi7OBh4eKPAY5UbB7mhrKgPESaqpWKQIfQZ_txIdaw4lfqPSRU_wqR0hHH-yUIHvrklfa3p7h2Do6XFE7f_Lx0hVHKUEiWFWsd0OPsV7fz1jit9Sp2blwkvBjfwn2QA3T6fLvyM4Ibcv37IiwfqcfWoG3rgSwQ_g84aZ2ZmSvrRapcka-a4UL-iSBV0y5Mgyhkeff2jA9NHViIQEufwKQrAERONDR2yLHAFkajDtQ77GymizRq_DtOq9lu-hEzNOEIZby9Kd4jYD_VRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=qqanxFtcnDB36RgLI5FYTit9ezuuBJJXkjsqW-Qp20lVWsBGG3W8whJ1m8VjBwpAvYX2RqEi7OBh4eKPAY5UbB7mhrKgPESaqpWKQIfQZ_txIdaw4lfqPSRU_wqR0hHH-yUIHvrklfa3p7h2Do6XFE7f_Lx0hVHKUEiWFWsd0OPsV7fz1jit9Sp2blwkvBjfwn2QA3T6fLvyM4Ibcv37IiwfqcfWoG3rgSwQ_g84aZ2ZmSvrRapcka-a4UL-iSBV0y5Mgyhkeff2jA9NHViIQEufwKQrAERONDR2yLHAFkajDtQ77GymizRq_DtOq9lu-hEzNOEIZby9Kd4jYD_VRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VmVnE2Q16F-LI_mbTcYEbtQQlWc8qG3BKUESHTBBynVG2CglbeNguIYUr-I9-GmZdnMw4cSO874F5pjs7AjsskpF6axsIUmitucA676ibn2nf5gGWcb41Bwrj1Fpxy-Of737EGXUgNEKfFQyOd52VugWBLyS6Y1COGMNLdv88FwxOvpBhvIMrx18_EkfyAanDHVBDU6A3uCt8jvnXHRtKFC8w5Kf93iVOYrVDnUD3EdHV7_l3Jc8xkdh5azR7uBVSqK1tUDJhE9zGnVhxxoCAa0vcp-8AliI3a1xhUJ_M4kFRQ8HcMrwtgXdPj9EeliEfGAV9mTcf_AVIgBCKHIjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-Th7QilR9NJrcxZKAQoEYVB0edQSATuRUWjX0VCfc0aZSwD35-edrJ5CymGNRnGdHeIpX_TybQgIrGQlkzs5FsXyV88KOFWSBeIG1Q5Rny96udj0bVTmrtedWspQi4nIpAPPjpX0e7xaFGApOuzGAZXzFQJokkv9Fn9VyDlVzZ-G5oyszdEXTC9DuFCubwBdvBB9j9wnUj8am-12gFKgsCkUeNtdXqToRU2YijaFl71AUsU4SIWcEAAsH_eciuvfB6pkmPjYIvw9J40CV5il0DvGOPpWTnLjO1evVaZuo4MykgM-8lciOtKvmwgpzdLpb-0bD-Uzk8Oxk3Ce6e1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eP2UenuQc3J4lILfUbVdLr5ugVnp2rlv1w-x6YK7oItqqDB0t8MyNzWbfZgVznHcYkYKOImLnAT3XdHdiFy6_nIRjqDwaVprM1c7w36ATzpvNA2s_OKAgBcGP5p4vvZN9kwjsYbgITDfokzCLIlWSHcV-xe21Dve1lKfxADVpczVr9hPdhIaSx8hFVJneVZzvNq7PW91YCMzGvZZxFX3WS0TGb1RdbV5SuOttjEiFMk9rqh2mMSNuFJWrrj-MsSswxQw_oK8bAveA0w_t1lehgbR_MulCYucR3uU_mvQt9knVs5PMa8g9VuAym-i9BQn11ML0Ib1KGM4q1KrZtRvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhwr5db0QObNGjTGEdNNG5axkyAbUgCWTCo9_jc1WisCpkOYl7ZQnquBvHPo3r9HFln5h9JlbsWFgURHRXusBOULSslEHa9ZNx7RX8NdgL7EaZUreJEDM3NQrDrG5XaFkRZ1akTGOKc79Bh8Da5c9qXUZf8_xj6S7VVnYm-IvqYWUrPtzkJVK8KqKOFLgeCocAhVUnZpclqXNEshK7sfDcskW7qNaixyvBLkGTqx6o4GBlFPBRi5iJspb1L0cRbZ00wZaGOPSL1a7AJSubZR_8cPOOJ3OjmauXE2nLUsUsGh8SLU-Tl5iQvGFbmZWRP2SNfGaZSwc2yafY2Kth1CBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=jKfyBeLlLPk9bca0wi8cL0TtsnCC9D_kJbKydOx3515lD4wVrsspF8Eqa1nw6ixAikOC_ju0hQBMs7y9U7ARtZ2bpdEZ2hN5IP0tkCMtiiLgRobXMWm12MZQvIJPwc-f591g9veakUtRwheS-UgyEAC7Up2PFvfEfOinZ34hwOLnd5mSenu2ZmoEeHYMRFWkqOpGF1IpEe9Tiu7cFb4HPTP_9pTDY2GFmDsmbQORRp1IuT5WWaY1e93ToFoY3hXIVUslqnvEYqQWeATGHlhbwtXZZ8nStkrvr3wrHoZVpoVJ4u_DpuGA1eSd7aR2R11s-Wg-XEG30K5LpWqhNXmA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=jKfyBeLlLPk9bca0wi8cL0TtsnCC9D_kJbKydOx3515lD4wVrsspF8Eqa1nw6ixAikOC_ju0hQBMs7y9U7ARtZ2bpdEZ2hN5IP0tkCMtiiLgRobXMWm12MZQvIJPwc-f591g9veakUtRwheS-UgyEAC7Up2PFvfEfOinZ34hwOLnd5mSenu2ZmoEeHYMRFWkqOpGF1IpEe9Tiu7cFb4HPTP_9pTDY2GFmDsmbQORRp1IuT5WWaY1e93ToFoY3hXIVUslqnvEYqQWeATGHlhbwtXZZ8nStkrvr3wrHoZVpoVJ4u_DpuGA1eSd7aR2R11s-Wg-XEG30K5LpWqhNXmA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qIoFs6gdqn_ZSWn8ElKwnHr9CIgvYFClAthcquFLFmalDpQ4wSdMXj5IFGSlLNEKHoCBR9kWmVHJ4I_lfmzL7jepPdigcb4z8OMpeYx6ePNitIWM3ztRzjUb1lc36N2ePJYvwqrLmMwLVUVr1-iEcA8-LgaETGo3-jO8pmpgushd4LYP1D124RHAZK-QjZwV-IS7OPMvJiav32_itBBbCn7N8CA03WSY8XX0bPpdxO187cZXsbguePvsRXqjsmp0ehm2kdzvwhcPZbSAICgiRHFW1XMYWRlzvWKVHbrhFj17Qjnxwb5yCf65pwdvUOlebYJdFqSCW4YH3vAZO7uLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=QnfiqS1FyyubXHQAL3sdiWgT6Bg47f-uh5fX-L3lKZtkXzsHNscpzTa1T2Hkot7aQoiaINiK9nFSfNn60agwtOixO148kyJDMTUAQ2KjXy_V-b4wXkF5Tm98_3Llb5Nf2LBGqAUbj7FcKqyS5FlMPcOUiuqHp4ZdmNorjYid23y97sX8dHhUO0ADOcK_NPuy_H0hIB1kNAEUtRI58nTz_Ccc30JP-gLuOoTePRAsZdx6jrfWI8XBjLEK02AyvY4s9CYdYqo9dNIbLk3nPoOl5w4FiJPKPLVxQWFxhRPzkWAPgL3xGBerXJ8UHjEUgYesQb1DZXlOmqPSdTHBV8Us1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=QnfiqS1FyyubXHQAL3sdiWgT6Bg47f-uh5fX-L3lKZtkXzsHNscpzTa1T2Hkot7aQoiaINiK9nFSfNn60agwtOixO148kyJDMTUAQ2KjXy_V-b4wXkF5Tm98_3Llb5Nf2LBGqAUbj7FcKqyS5FlMPcOUiuqHp4ZdmNorjYid23y97sX8dHhUO0ADOcK_NPuy_H0hIB1kNAEUtRI58nTz_Ccc30JP-gLuOoTePRAsZdx6jrfWI8XBjLEK02AyvY4s9CYdYqo9dNIbLk3nPoOl5w4FiJPKPLVxQWFxhRPzkWAPgL3xGBerXJ8UHjEUgYesQb1DZXlOmqPSdTHBV8Us1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOx4rYjMo1Ef_LRLNPSSATKFDuDxDawH0YUu8YMh28al1kdNzgnR-e29q-9qqT0odJq1P0cm8sMSQl1O7VkTe2d4GVDNPTOWUZMV_DQ0aADNOkkbQFrIjlX6onf_y2OfKO8wZxNOItVqsFAOfaHR3IKQRtqts6FYpmYoRagmTFiN1ciEPtbfs7wUUz7lJCM4W9mpNmpcTow2J1may5wXHNiaaHlE1Fg9cw0A78WvEmqILha9vUKqUCKM6SG7T7cd-_IPKOIWpR7CgGTRiIZiUEk8_pz3Gsc9HHOBy7QOTGMBeMxYZ3J_0bcdgs47RdlgU57JA4FJ4hAxVs3MfzFmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EalSTxNYJNkIrW104XMEiu814S7nOC3EU3oqqJa6-XvzPcpxt7TQke_tmGs-lpG9dBOmfS0wOEizAXpFZATp9-LWk6i_jCqgkWx8V8DsdQDxUUsO3BkPnXYC0TkAm4SORmH8dyAA23T4gq-Aetc5n1-eZgwPOJDnTv_fN7LTyS4IcYA0bY_L-FUd6WACXMFfI0vkH1_M7CBquLHN5GlDiWvwyXTQtA8mnNQBj7Wt-zj0Z4M6wSDV2BIDC1P08o_xu9dpCVDu9IaXqunhGZIgFLaEmmdGgy1i-7XIBnbgcNWfJVQfsQJfUBdsZH5GMbc5NMuHIfMWxGJrV12oKT3zSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkYGBw4ZvyKhbNMVWkVPiSrgvgzp-1gpEA57uF7RVzuX0ZdVNNi2EWxDj4YoZ_r4nTH3W_kV7oYisirv09uo2qDXkTszVNU-4FpRAKsirsT7x_vzNsSZqRVIA2km5_ydhdrpm_8tD9Tad148JdXkQC26mXK27zwYhT-xAHJ1LfswFcJDr10L4iGRaL9WR52PEJMNhAZqKZG-SEpl2KNYChoq3DwkWqfDT1lKBxTS6lRSjibSHaZJgnMp0k63Y4TPdN1w9Kh1h6ICzq5gzzQestlqyUAyO9Dyc-nxuIsLey96GTKJSP_B1jElbW3aHjsqYQtUla4c3z9M6Tmmi6iTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/grPFNi0W0m7PkytIIVR99xmJPVgG5ERUqw8XWaEoCO28XI3nz7bVHOcLw62ttCnERVkR2cVt7SCSnlJ3SL-Pe8cF-E--KSI5XHQz9gr4to-uLXrv6oYfM4xMNHqhVr2zHWsOOI-oT-7MyNGEXzyu5WVLRitdflIsjIBUiy_LNlMU4vwKruJORPeM0xD9Alj8OI2mFIO3qxMmB9tDKLADeV_ZFMixS58Iczu0hhuPhzjANamQ687LW4_bBoGtLsl-BZfaGms9A5aUesotRGgtbjsu-h2PgLx6Qm5pyIO4rfcYOinoSfdOQkFTvY9S9fjhvNIwPie_w6OGAxvd557o9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CpsPYZP3UXutq_JyxtFor40K5kGjGlbAW6Ll78rGHd8IonqoAr2juQovI7S_LV-l65Ha7nX6pMvuMr6XMWwjPhvTx5swkgJSJf58RKloIlHSHA-ea9sZ0lKDGsrQEIN00CDQSHwKN7NbPMvF0yvwAmutwl1PbWTitncdfwNI0g1QvvixI8fQ7xmHD92Dc1Y_TzrzM3HKCehkPwtrpw7k0ZkVxIEFvJ8yDYSX46Z300XAcbfikelV0d2yRM2u_u-Or60x3GtXFmXW4P0C5G1BPPpffhqH2g8ypNNGIpcMhhzHTTONYXLpIUd8BAiIbecW9e0BZjkrY_7n46kmE-90lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qry72T0HhBhMKTZyz7vPBWbr77q4Pb9dvKSQtPDWyKir33AVsEzUqB3WUAIu2pVdK6Qg9lG-L7WUbgFMrG-oaASNvCeEKITFpR7zMhWvwuItCVIVxGCGnFwst686u8HLoJvA2LgYizcE2Z8W53YJAte5I_5u52WSZ3gjSORSaRkoZZRSg0qT983oFWP8PVVnjeyDUpRmFCqlW8eEkN4Mrrs_yBYC96r4P5JSS0HbFE8bL-qhkLzTkzXGTSyM0zDFiouPPn2QKe0cGi2pofDD9pz11hfmAJ_ukZvPKVJnuWdYTScEOrXccjjGYXFE8sEZCwu-zKzQKB7pBBr8eBojpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTOtYqQPfZM84stX5chTwm7KnjyICgWioqQn6jSJWOFCILPNWvtkRfI_vRK-cIHKIQ8-VB6fFrcmDMt2MRFMH0ZrTP1WzYXPx6lXtOsJvpHsFnOJAnv4MGhyRVSgmW02NJRByrPbp-_keq-uSTYrK6QS98g8SFrEop7shPSqKm-96SJwkljanwrSKWmBumlM4V7OO6P2M0Tbz9RPQtKnIeBgKIaJ_c-6AXNOjlhCUchdPKWF5umf6LP_IZuE3_Wmnzfk73A7VhDf2Xnh3B-2knwfkr0MR7kI2P8EhLF8v_q54XHUq4BTXs0FY56Yhv752NAgVOex6DycHNA_5URGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=K8HC_-LiwN1QV-sAQ_AiOtgIJV7WmSPbRChrGKBh1CP1GSLKz4Dwuqvw4yKM_lWUdNVfyG1A75vEUbiIBCuXscM7M2uSMHjz6sdlovWzpSoy6GRZpDtZ_z4NycR0KpRn8jhu9QZXUbUx_VOFEb2iH6LbcwAs92IgboeuBm0cz5CtXc6c7N8oG9vcB6ZoDfI1O1F4mZu9-MH0tSpYPOXLCn2USptl3QqNb88dyRnSQLZpwKHVx7We0dWSvKtOaOqWc58sUGTuQ3OjANVZHUNDqgu4_Gf9M8gFbkwVIJZQRSEa8cnD9EV6fDqkXFlsYe8y4sb-TyZj56avdUXLqwxjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=K8HC_-LiwN1QV-sAQ_AiOtgIJV7WmSPbRChrGKBh1CP1GSLKz4Dwuqvw4yKM_lWUdNVfyG1A75vEUbiIBCuXscM7M2uSMHjz6sdlovWzpSoy6GRZpDtZ_z4NycR0KpRn8jhu9QZXUbUx_VOFEb2iH6LbcwAs92IgboeuBm0cz5CtXc6c7N8oG9vcB6ZoDfI1O1F4mZu9-MH0tSpYPOXLCn2USptl3QqNb88dyRnSQLZpwKHVx7We0dWSvKtOaOqWc58sUGTuQ3OjANVZHUNDqgu4_Gf9M8gFbkwVIJZQRSEa8cnD9EV6fDqkXFlsYe8y4sb-TyZj56avdUXLqwxjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tM4soItAge92sIM7JzCUhzu4kXVKMFLakeMR3xm51RzxXcVAhsKbpoAbx5RTpMySSjJ6mZrvjQkTgy0FVxI4KCJY5gd3A1x8pYoVAkLH2PPYTYa3hyiIaCA7cRn7rBT8I2UxlWaNDgRCBFQr-JvNYUFRCvd7NAJRtTSmvjnifBOfeveh42G5X2OUUkLtb13cTwR20ml5H6PLjK_sncvRem_dqWP9inPDu_Q6tKsj_n3gOzzfEDhpNwEemw3f6AkF7rQGuGg2_MZNfzQOJrjpeqHWLjQV7ZnbpBroipOUtLlq62ejpPSsMZjPMAkOjG7T7RxOojhzAQjjYpx5IzUaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ8TMJMtvliiapEwFO0EKb7mfiWLGwUBj8xRPm4L3iNzu49NYR3QncgOJwDCkFUsOFmYmMyWIEIuPDeRGreM_ddYetDG7i6TCpzLg54FUyLuTd141YpyzzISsIChTcCZBE_VpVQWod67TEFQoEObzzYW3lbzzXOx2rLMAe5CifvXdsaTAJwgU4ovulmBH0T5V_j_judm0nbE6mmRi9fmfPeUmlOrEQKG1PCvP3jxle-16lgU3SmNIKRXFvpsPGVr7aU9Vrr44AIx8d2lp-Xv38NEB5tM2FMa8X502pKgdeCwSxYlbpUq-pTfuzu8bB9jaVqebqY0PnCCMtuuFcIEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=BzmstTtNEdpahSZNI5rpo7sEmHwJY1gOGY34Rw3woC7UllTY2W_4mz2xsYfYRuC5qgF64K0VmyR-P3EUxdd3e7eway6dlvVcIDByHiOAJhjme0jGIcmzfLDScJ_rN9n2wvkMPWq-jaVnrZ-UqCSuN1-RkKniy--aLs9NEMirHAd_qhvuJvWuIvlmLPvOQP3uEbbRflBficdO_bu_8EN_kXgqgDigYR_Kx43shMdKM6lmma4h2iIGrMWG859XnL5zG2_m1AiWr46tMMOfgSZtjCiW961gjSRmDI5CdIiwXNxqC_zT5oKsb4sIij-llkI6QEU6BtwcnyjHK6vyBX6o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=BzmstTtNEdpahSZNI5rpo7sEmHwJY1gOGY34Rw3woC7UllTY2W_4mz2xsYfYRuC5qgF64K0VmyR-P3EUxdd3e7eway6dlvVcIDByHiOAJhjme0jGIcmzfLDScJ_rN9n2wvkMPWq-jaVnrZ-UqCSuN1-RkKniy--aLs9NEMirHAd_qhvuJvWuIvlmLPvOQP3uEbbRflBficdO_bu_8EN_kXgqgDigYR_Kx43shMdKM6lmma4h2iIGrMWG859XnL5zG2_m1AiWr46tMMOfgSZtjCiW961gjSRmDI5CdIiwXNxqC_zT5oKsb4sIij-llkI6QEU6BtwcnyjHK6vyBX6o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWU_wtXADIOGmE_-A5KdPvXYV50ESifIePdQkuUasIkO1rQP9Q_ey88zjXCk__iMloY6YShrwAz3gJuzsxhuF0aGUzswO6DBzWHYpBR3CLOeDE0Xl6X2EKPkZSFH4n0sazlCyq_qWdWzVtihab7OdEEdih7-8CyWKn_0uSAEcpzYFriBS5mSC07VJdhynQJuLfEoAcXlbq8-XwrwvlswBn-jgSuFO1P3yGZvCqWYeycgu3K7PLWj5Tzv2Mku0X3ORZXN6gW7ji-a9-tzcHbmFm7bmtzElfIcluyOWJGfcLLfPBDDCU67p1xG9epXpxIg8eZOjNCumEYTpB6I5Tv34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-eKVgQXHs96JF8Rz4Zbcwg_vnKlcDnGFD5QUf9n07aj6b1ObFVZ98rXQ61hxwZpyupbRQwYm3p1y71cDxWndN0zKBZUOmuME4_Or-iW6FgkhbQJm-4yOBvDeDDcIuAZrvR5mIS8C9sHTOD9Dc_hzDreasbQoVtEiiEjj1bVHRMWtHBeJpBXQvLLOoulVhbzhDtWC3nsO-61F9h-pLObCIp3tK0ALZJUTOsE20qGOsAeitYVlscvpS_8BZpjL2NVqSf3n_1vnkaRJmxMuYz7z2q3Kl7z2kFXHflyHgv_qQXv_UZ6ffnAiI9RPWHd16UWfrpC2_nUNxUMIZjZCwC3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8o5Qv_LdUW4HWuvhevvtU-o3LhuAKF7xhywzyYyUmTRw4tGraCF3UxGhnsumMKtJRhsfl4NhiD9gydH6YKGMZi3LHMvk2D1OV2tQ65pzyVo8MoGbEbuCmselDcyjHdI8lUrekCtF76Gb86xhwkat64ep7oKihic_Fp6DvJh6ObnpOxn0bDE3Si0FnQcqgdSBoHeSrAtN7wkcWQ_vcfM7GhIwMOiHLo-GPZSMDgB0Ux6Ezm607Jd73bwjN_GVJhNT6eSb1te48FBACZJ5awcMC4N9qBL8aGZlDCodx87vhIK1zv8bez3Ma4VrG6gTorWkSTsUBPimyQ7c9rcIiid3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=fMTZIOlWzehhljrj3TTDy_IWPmw5hMK1bmkXRMUc1kkuiYMzbFmeCH7tFjxETLqmg0Io31Zla3PHsta1V4i2eNK6OS6okKDEJqLSuvTRelJJBJiOE1w_R_kwLvq_HGgOhHo3zpJbLyO7e4f3jDfTsFbNK_sd5diKzAl2qST_2Pn1vfr0zfIq2ObZv6mJ3uQurfXBFc-HjVcikvIY_gcjBFnB9W2GtDa-4oEna8GzrL1vYjYIzLFYlwQl-x4QA7tNX1FSHPaVHDGdQ6otbsCCdjpZEv99p-3L8mdSb4hq7Y3v5418SZoK3ilu8LEcO4jiQWPvOeNafM3cq7KKYVtyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=fMTZIOlWzehhljrj3TTDy_IWPmw5hMK1bmkXRMUc1kkuiYMzbFmeCH7tFjxETLqmg0Io31Zla3PHsta1V4i2eNK6OS6okKDEJqLSuvTRelJJBJiOE1w_R_kwLvq_HGgOhHo3zpJbLyO7e4f3jDfTsFbNK_sd5diKzAl2qST_2Pn1vfr0zfIq2ObZv6mJ3uQurfXBFc-HjVcikvIY_gcjBFnB9W2GtDa-4oEna8GzrL1vYjYIzLFYlwQl-x4QA7tNX1FSHPaVHDGdQ6otbsCCdjpZEv99p-3L8mdSb4hq7Y3v5418SZoK3ilu8LEcO4jiQWPvOeNafM3cq7KKYVtyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I5gxY2LzsrBPpW2UnQ_UaCEn12rw_l5gOjqC2Ors0tdbm6zwW36sLjfIIUZwMqNSayekB2yXddYOaUKAxETPx2gY6VlxWieqREqWqi4CqsOWIi54tcwiujQpYMznkT2StOt9X2htqfzRYllugrPYUZBWe0nlHvqtZYta6N5jj-cxXeneCSqPyOnp6t1VO8TzoMERwl_6lm3CzEybWluGpqFoj065fH7ERzvVw5N4350GHzVCtXHr3B6dlkE5qsR_MbgA3en8nAyK83MuzvgrFbWEttIPUDfpP_t3e77JdatbiqkVUnsnHH3e8hgEH_UWhdDch8S5PxCBWT5HRMu7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hkbr7BeeU_OfKu2UCun5IWdNdB8VF3_Tk0_pVey2DJU0kjHhAcD7wiQLzpdqeeFiQ_kT2q7XSJIquiYr44p7TFvbl1_L329rFFCE6HEXOjINJJobXYutZWoBrXizSJrlv3L6KB5JPY48mct7LoKYRFdtBEOWwYNKlaZi1osnswVIxYqMWVVCUvi4MkX4-McoNMO3cuwKZhSP4Y4tHni2VOTxOYJXpoiS3wllOIUJoDtzmEmMr33P1hRTCXVfDPBIQF2rvOqGx7jYNUqBZ-Yth5hzFfDy4rr2Fv7dzNo9Fr9c5rnbw1MzJjZwJ5pWojZHWrzHrlZhwmgz_ypFKzdSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Ok3zmKnDzst8sk4JGHchAkA4d3uc1G126ICxVLx0LWoGX5-3qINA02990JN6fME1-vx72s1br2lp6sD7qSFtLb13JYOSglZt9E-B_SWkr-71fT6u3EWFfTZ0AZs-_QuvfG4x7yWe_GJuP-IX0IHkgKMR6qybxksK50GoagbtdJz0ryicq9g3lmTs3abNh7yyBjNm8SNEUdASauQ5B2MHeJFrNI7fzVARr6an3BY9MEvqrrRWWVBaylHfIRSMVPiaG6fZNtsxE8ewJ3Gr7qDfDNVipUdzH1sATFgtKXBU2kZhnQol6qb02WuIHUjSDbxjojZ0AgXVADPj6fgRU8RaQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Ok3zmKnDzst8sk4JGHchAkA4d3uc1G126ICxVLx0LWoGX5-3qINA02990JN6fME1-vx72s1br2lp6sD7qSFtLb13JYOSglZt9E-B_SWkr-71fT6u3EWFfTZ0AZs-_QuvfG4x7yWe_GJuP-IX0IHkgKMR6qybxksK50GoagbtdJz0ryicq9g3lmTs3abNh7yyBjNm8SNEUdASauQ5B2MHeJFrNI7fzVARr6an3BY9MEvqrrRWWVBaylHfIRSMVPiaG6fZNtsxE8ewJ3Gr7qDfDNVipUdzH1sATFgtKXBU2kZhnQol6qb02WuIHUjSDbxjojZ0AgXVADPj6fgRU8RaQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=hcnAVybU2AhbfylQa9hKG93XmPIsKFX1Cycj3qlEut0nbTcZBWiv3jsVHitMFXJiuM4KdUUZUZ4lV1SmkseRv1_-_0Dy9Tk0UtJmXW1P6YO1qvp_sTs8SnxBpTd8LpxXGFpUPo0ntmGwZbSd0XqcAIF9e5fxgZX1l-4y3Mgbohw-n4PqpjgGUZW_c5f7TQUox31Ap9As2RJcwgeWDitD8nFox00OVWh6Fh7W32__J2HMUuQRBPtw8fHnChP3F8rXVAMtwHwWFR2_tJlqj0fzuSJuX00HFk19oY8IzrfKX8q2hiSBU_lvZ_w1_lF1J5-EeZ-kK6YDGgL6PHPOLF_ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=hcnAVybU2AhbfylQa9hKG93XmPIsKFX1Cycj3qlEut0nbTcZBWiv3jsVHitMFXJiuM4KdUUZUZ4lV1SmkseRv1_-_0Dy9Tk0UtJmXW1P6YO1qvp_sTs8SnxBpTd8LpxXGFpUPo0ntmGwZbSd0XqcAIF9e5fxgZX1l-4y3Mgbohw-n4PqpjgGUZW_c5f7TQUox31Ap9As2RJcwgeWDitD8nFox00OVWh6Fh7W32__J2HMUuQRBPtw8fHnChP3F8rXVAMtwHwWFR2_tJlqj0fzuSJuX00HFk19oY8IzrfKX8q2hiSBU_lvZ_w1_lF1J5-EeZ-kK6YDGgL6PHPOLF_ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C293vlrGsVDQk3ndERC21d6klKO6_RnpkZxNqnJ7dVRN8JGnYUq6KmXzr-86D5Kkw_EGY4NuY57enG7q_6flvrGk8SrBfMxb47ZyKo-mA2IIxktd_WQgEHUWNKpWYRpbSDekEiXOuK9_UtgvoxxQwlHcN_6aJfbAN2wAdJAJqL1esANQrq7J-8ovHBiAEPkX7utWqyQtanx0Qg3ZFL2KH2RJ-KKhcgsrS6J1QqkPgH957mN47FIQlXZIv7IPVVlcVED2D12zk-XRichbMZAtM0KHH64esSr8q39bMvWLcPlCbbhtqdF0ggSB9ZdA9EcgwlpBGMoFtKrYOWJSILo2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E-RQnpkk-HStv6T7US9HygocS48x6du5NT_5yQEAMXQOXdwNQ1ngSVZJ7nyIM_av9Fnb36zXoFHZ83bG8VPiQYuMNJkr_Jfj54HhnrQeeaQDPEtEPNB97_ls2SKWlBm4XTlIs4zwaauFn9i0Mq_zdZMKEiPjP9_Q1QvoyLVz6eT_wuhaP7s5znNzbY1SnZ22crLPU0Q8R3G_pmVuaGrAs8obeSSpLB6Q4AByAnwG-3sWZ05KgVe63oGhBGhI-c5At8GCGfkSo8kZ0OwKQUaGhSkKtm9Hek3WKrmCYawbVffc3NRzU8G4S-xHwYxj7NDz2gxdhxOviC8J8eL11MpXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KuD8e9X8PetyDkb_Z3egyO4PFiqzV76TCP8NUf8r4uD9bBXuB9lBY78DU7x-auYWJRB2YNw5Uh4NZM_egZr6nMYEQMM0QsnkRTIQvH3EJORfeQ0n94o4oe2LQo95SEH2qpu6UVLsCHlNX3clXF00nt11taJ6Ni2PZAVVNKXwQWbE9fTKqxQVGS64D4M3hAXYP5WiuuM_Og7v9LEdnOjv5JWXtVle9ooA1_KAIC2stLUrfx0mFwOIfUfMDYoJijIpFO-_I5GHdBuwvbkBZmqhkmd1YOvs4zF6vH-KhhUVodkRrlNL9XeGNNw27d0vkcxs5u10F5mhaEt2hWb9IvaW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXGe7Ils5-O9TW1HBgiNhmgCrbxiX48lOBxpAdMJwT56vb8G-soe4HLPvjaw_Xd3XxBRjEAAcWc4yjAs87boVkw7Cgl6t6aDQ5-lVmJufS8xp9OSkueF3ytYaPS9Mgo9YOX_6alI-USRmJbzKLg0oaDeQata0PaERH9BJc00BXFR2h3eoWt-E5ADMT_uO-5V75APkAf63urUASBMDCUGeGMgrXk3X6VHoSvO70R1Tw0Kx2SanfPfa5u-HW9tvRV6anO1vJvBHG97meFI4y-Zi3x-1Mx4whJ-n-r9mcoSoGOYLa2HFQf28IVF-sUXg4SxiVCaXZSA_p55QMWUalnwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN3Im4JFRLv-wb7cAhwbfRJmLB2jajw6TBHaAimE0oIDWk6vkeH-CeFiU1VFXM25e2_tsfTqRG_qqBY4YGWvAmCC-EJl1QYx6RBBW8DDmNFF42oJP1Ci78Ps3s7r-a2RqPRxmO524wijkF6aCf8yTylwqCcRLoIqoHo2KdcYocQ9S0iUsrOtlwlOayt5RHOvdalvI5SgEWpNE6c4_9IdlHL2i4RKalRD6xTekxlSMYYUrXSLjzokel0JtdABfLVgr4kwNuoLv8lfiQpdp0fGDfw93ryVbH-WjiffqbO9VKhbj18OfPnlZ6eyqTKi8ULjNR2jK2TTNgHy2NxzqX4ONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhXaN_6lmUwMXc3wAhA3UQUqmDKyzCIRq2hq3_SHQaPqiwFJoHYvBu2W3s_fnJd02TouQ2LhZo1h_gFpKsJ9UQAfg8sp_-TM300lP-nupBWgbcw4ux25I42Ut72W_IjHx4K18z6jbQGnrhdw5icFBtWUMsQqm0STcRvrMU81b1jyc40j-qpGZsLZZGcaEPUyaOR2lHte0bRn-3wYi65VH90b37iptiwiO3HxdjENVp1t9Zl2dIu9Lc1NFWaRNYntcfBjy5VYEJ_oBUcCTw1fFS8UsIYRNo1x53fvAmOf-OhT0Q0_k6-vAAhYUaKEx4pWSAqjFiu8gXboxuYQQSoypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyKZGlIiPVoqxtNLmkFFylh_Rmo2sP9erpIl0EX4nkULkAf84PKtMJl8bc8oc2YZH3XYVC7LgVX9mqtL4NwXRRLJdD6zg_UiT0UxdKXxxl-m1cZuNqBJKgFMmYutCRXAb6lofUuVdrRRf_G_buwVvLtkoy_itXorByN6Ary4uynBueUMzWIVVXFNHXt0ig68jx2nuCNfP4-WrudKgCKUmaXHzUsdjsroEczXBP04Ph9DePfasTJbWNACRUjMzy0QwLUFNFXCxL2nN2Zb-mh9z6rG2Um-i06_SIU_y2MDi_GDr6vMuOcsURqs31domwnZyJU599hz7CQRCPAYolsivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=d9S3d3ei3LEDj9OG4U4jA-WSRxeQ965rm_dkt0RHrjOeXsGX4hLxnfkuJFTsvxfAgtZqkM2dn72qmwrsaRHBL7fsvbgBa8IkDcbikMZ0wPuEtSR1QCrY6Sme2VeN2R34BiRyQpLNfw0ZuCO3M3X5OPNlV2ANccZrOF2MRMsyhS5WQ7VYC39rgAKZa6QO57PvPvEPZLN9-jshoXRYSXqqCb7UrhsELKRHW0vb6OIjBiT0nc6EfQfdBDfF-NAQ4N742EHPg0ku4JCrSrw8eu2ATDCVI5-cx30LR85n4sq2yYYEppWeggKJJzOxhlQtr_A-1J0_qii-W2kvr92010NKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=d9S3d3ei3LEDj9OG4U4jA-WSRxeQ965rm_dkt0RHrjOeXsGX4hLxnfkuJFTsvxfAgtZqkM2dn72qmwrsaRHBL7fsvbgBa8IkDcbikMZ0wPuEtSR1QCrY6Sme2VeN2R34BiRyQpLNfw0ZuCO3M3X5OPNlV2ANccZrOF2MRMsyhS5WQ7VYC39rgAKZa6QO57PvPvEPZLN9-jshoXRYSXqqCb7UrhsELKRHW0vb6OIjBiT0nc6EfQfdBDfF-NAQ4N742EHPg0ku4JCrSrw8eu2ATDCVI5-cx30LR85n4sq2yYYEppWeggKJJzOxhlQtr_A-1J0_qii-W2kvr92010NKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PexjlT0ui9lV12sWJSmC9HQ1P3oakIMApXsxAmYmrRJJy7ZTsrAOzOniy5536J-R-Jij7RJdt3dud5PmWM26ojnqDUw-FCQTm6jyiJ8d-PUuC3KeoHOLCz9zf69E_p9iEDkvpx78R9d3w3loeTRKdITFsGvNpmfnwm_TijaVzmiOHXsml1kq1sb4K0kTzfgWYIQaBYm6A7pXTRM2_wIQAmnicvR0Os450SIFiX4ZfFuDeRdZQBLX4Zv8Qo8SkiRuiX8X7UoMAIdUwuZOqjxy7Hov4-k7HO4Ts2y6TQF_4TYmtcYlYWOyLBM9jhAjgGKiC_XTdzFOcMQx0Hn19LXP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gnuHUSZLYbrtEgZ6oUMwm24FzXIUUDuJY9rvFcWF3E2U5htw0oMvMEhPmEilbU6bvCTzHE8VHzUio5U7JKiseErnlKoHm9vC35WzQNZIDlR2fSEEcCmNA3BGs5UoAiA-nZR9DZJzNKyoGpm6pOhWTJxl6pMHMS6tZmFG8ZTLm_jQqE4VlapJKqjf78Iwg8diyPOxIz7P_k9uFGlhgihlmJ49KY7z52imfEZxVFnhRhQGkl2w0QI2_TzrAZBhrxrtw3jClT8nZkU4DNjuusuPemKTdX8c5jDj-x9whnQyoVicRlsPV6vUXFHOnkCD-Qu-oYuP-dkqsafUAkpHF3hndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gVpsrJXGsNRp8XmOnZvzgOkesaxS9BXKYlQndN0uws4rOrKvFCDIS7VCRRIYRfCnjs5saD_kvpSY2ynb4FdRAxRttbo1BhEGx-Pt6-lg3OEU9lV7xnVs0XtgMw1RJXYaQLtWlbPuQmG7OMJAnF6uN1JAH28j-Ilywx2-_67W7f_qRrSuZI1cGgnyy4qyyNejrOhJdPp5CLfiYE3W6RdGiwULH6IPfT_5RrTJncB8eDeNuii99FBfnm1vySXWpSQE7DAglq8tTcCJQp9EZU6WhK3ldMPYsye-dGWKtrY8odvwNin-QtaSEIKG4_GCnzS-sSUZQUZWb8kOp02r_Pz30g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B1mrpKonKOq-CcrqLTNCCshVAIAZm_6Sakh0gTTO7QKJ28P7aY7VD3iH85tMQicMOlePr4fayis1Mwt1sij7dvcTIyJ4Gsp2P1HKeGLDbW2NGBX8JvMexPub9F29ApKukjfLhpHCooDOXfvcgDndVUl36FQdv-PJBhNMSDn9H5ieDgoZNE3rqfdk2gLKnvKK_3sIhwFgIam1GClOncC5j8xw3Ihd31HgqzR40bhQguo9FmdApXanw_urvqnyDIhxrucDpgnHEvMDELLKwRSHwqR1q9Y1Ks_FyzPDeabMkpyuglsShpU09Qr0H0nXDSYA82zIzH6aBb3VGO-fj7TogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gN1xYXmmRHfcdLcG0nu6NP2TQ9WtM27Zci_zQutY1hSwwcArdMRKHbukasQ1s-sbby-OBhCKW9r04f5EoPI1oHRqAI8S4xJDJoArl94ZlmuZIjqbMs_rxhmm2qI0i5-aagfgZkv-eG5qE9QFQY-uROM4Sn80lLgkbNr-Jsa3lQMxQeku7BDcfq6fZ7513F80TfZJD7sax5FQ3dNoxps_Fc5q20W8V6OLhJ_b7mAp9azWZCyE_6GeOPfN6ubVlPhKi2MFjDvAUJXBk3Zd25eAf8JTl672FJcacXlOY2zqyLfJrATKjt7SR6QvmjL5rwWzl2Vox0RnE1PRrNq6Tcvb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DyZom3E5s4zmkcsKEmgRho3qtApWo_gaeXLJ3ED4vXqGmqidtQcFFGAimdWYty3RrgIstOdYB5gyOY7KV-5OPMkIhhRMI4fdt4oC_R6tTobwCkbzyfZyk4B_Sa2ohT439d-1LvDzoNH37E00tY4srjA36U6BTinjKBpUaQtEgiSIVVqw4BxhhExXn5oB6R-9b7CCn2zvsUES2Xuu_8Zhhx4Xz78DiBQ0xiFewbhitIHDw0UGCoGZLVgmglg0vMVtck90Y-PVPNhiEJpfEj8oTRQ1MtkytjJFtMnXFyrFZ1rl3RRH5x2kllU5ohcrthud_U638ig7zm-gPDg_iR198A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oBmdJbsVLpd1n8KRleKKohrrjI7TsDTAt5kfh-WYtt-gJnPUmUQZbwlRSK-P0WtVNy_eO_RG7ks5VlmU7Z0rNLieuSSYkUXdCoGEdHdbrP-aZ3-GJhkplKNf6GNOtorHwQnwpAihQaDG8ZU8ePXVCdE3MAaqCTMppMXkRqtLWtq_o1qmhY_bfM1vt5mtKRVChsxZjXig9pyxqFU4vvRe3B8Uy2D8IoqyT00r7KACM1_4UImYdC7cvKtUGwgZFkru1lcRM_vdH3kyLXW2hfqP517BnKEBKR95fNF3UG5iDKKq9hdPSYPnFN9P6QnqW9gs9gos091bQra5FeHcCapisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QYhcnGlSfCARnpYyN4QCAL430C8EBrNS_tyXbd8fPpGwml4b4hpUpEFGaYeZbrXVC96U8U0-nwm5YmkJgq20bINrkLPS8Vy-Xj3O8YuJnQ_RHpK0MOe-fH27fXJG3rQsNuWtn1J5QK2imIZXLLgrTEYYf6d55W50dbNUvFeTVb7ICacXFQcLIR7fwsZnlKJcp-n0kKuVraqpDWl5UKM7SmYQ_d11abGqYzqsvoAIWpp09wpWU0fJFj8JSGAURDtTcnHvXUwplbBEqjWuk3vRUzC014wqV5ZXEdePHBKKjoxZOHz2uQ6fZcgReVgz9HYvbSjmoUnLjJBCeH_yGFCnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzmwY6Wt6zskC1hilrT-x_BbZbNZ6Nvt8ob1VhK4WkDtabk53QLgg-RPG43WMPXFOqQoHJ0PB5YLkYKP8YkJ22x8HmlmLccjEIa9ds7kIN-oH5jEThfwbjBSLA9is_v4Amm0mKHnWIpWhRl4AoQxBljYrdmsKLPTGty8Lk8AumFFjdTRqFjSYd7eQHVAVsJTzZ_YHZ5B-pVE-AsJDUoM9jHZXh69-9OiZsqXRyKAZozLgYTBjqW5Xp1IF_RJ3oCRpAXKlO40mtFZ6_D8G-Q03iYfPbWqMT6vF4Go4XNuGhe36OegMFV4AH1hliDeZ4Ni46Lon7SXjTwZ4e4XDXfvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKf8jyil0Zh5vNERQ1btUGpIyZgBAfyN9m-fe65kI0-YY_svuGIKbGm0KQUg1N1I5BB_f3sC-wwiR6OIeRBEmNaWQ2324yiL9qoLNfjyNNynbcGtC2h6BbluLj0RXqe9rrhqQXPmikhDE2tiQ5if0A3kNBuAB7Q5FNO-PkMSZmFX3EDp_7f-rl-czrXOTb6q80YTdKUY8SlC3aPC6V4jJ8_vbDKKzNGxMIEE7p-W7TscywIWeH-vDfokxGNVyH-asoCo9V5Vd4PsgzJFSb0gknETVHkrRD2HEnEnK5TNPmu7FA_jAMjuMKsuYRuTsD2D0lcAAynSvBafI3zqobe_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMEGvpiQ1JIf9M4Xz6ZqFwgNIECF5jTgwrPEkpGoDwYGNHWeD6hgerDdSSOIBPHv2WtFvuELTk-7_u1uEhhsvqtfztkrpu1gorATJf62FYQ8Uth6qVBbKRrZcjlsiv78MZ88oRI1n-cj8VWubUX_0wlbje_LwYn_cmsbb7qbTiu9ahYi9URjZeRaNOWIK5QXK2ejcs0CLfedEYxoL0o7qZ2odnzO_nzCHXTu8UrvFuXOfL97cCBbRYdofjW770YytYd7Pvj9WMb1OM_xIgrsHS12tKZV3xkBLgDFO7feWxbxbLEkRD0l4PN9EiPtvZTQ0ClVFuhPimFK8ATW9tp3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AjqEMmsGIy7NfPtPiQMGNF6pRlV9cwPs_hLyMEV2AYRmZW0Esb3JEK-4zQvkFuRjvXK0zqZ9MaBN1IpybPcQoC0SkRHcZ8upJNiwoDXwT0KN8XGx3pVWCUqfVD0dEmu5U_VhqXuQ5XS8XJl2T5yLZJwOUed2JVVXFrVYQTyzz3mjDF1REztE2cO1tbX61OITQ_BYSQ0PdFIOERup6SHLSw9NknDW9lt_C8lis1cIFXsKRjHjO8mbKF5UWEvF-EtRID8bTonbugHSx_liim9XpZJWGMR_9g5beUrWlgXsLYDlC7WkyZMg_yBGm3WhF8oAKe2ZqReJH4H5DSp8e035_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a5A1IItT8vtI2BZohVhD-WYvdGoKxWGX6vUvfJNtttV9dfNe4BY1_9VRnw1VUh9xC2WtLTKCMmdvOpbO6wCISFBGViv-rVKNAgYd4edpJhxJRDMCrIuXl3RdCHJ90lfaCm9GdNxllA174gUl1J0wJQBfT0-WqHoO1gIhnVO9-LgSRx6eV0K17AhpWBT1EVLaIvVszVmLjdefG4uo-fY9iiReztQpErRBcH2OlKR5vEUIwOhGdCwJMYsWumWI6Z-G8hCilg2acjH9yUThJ41-XRvdcZXzqXJ0_RDke1PTrbbzohIQLMD2sdnW6ZvNoDfkKwhV57Vi_DLXx2FY5SSeyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=Xs1xq1zGLSDZtgD0zEqYjdGOsia8KcFgPlggNo6fwhQBJ2Y-e9LYnJGtsXDsE9nscdfb9D5q5nPsP8H0AhO6hlC_mmr-fv1X_aw5YaA7qqIjqRp0ljDzG-ykOZnDSQzd5KIU2s0u_iBfBTPHUMNvHx-sa2cTjA1YVidpGj2yBeFm3S4_GictcvlQEVEWRQGNIKvLBawmDmLP263deWC_r5x6UccWgddzVg6FPJr_KvGXBiS1mTJZjDc4UV4Ix_Uf2mxR6_bLntP1UzuIwtgCGTsO9NSUjPHApvPD4doBEZi1f4nncyb0mSagBt8hlVxcCF229dYa7UOiK-rFJirkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=Xs1xq1zGLSDZtgD0zEqYjdGOsia8KcFgPlggNo6fwhQBJ2Y-e9LYnJGtsXDsE9nscdfb9D5q5nPsP8H0AhO6hlC_mmr-fv1X_aw5YaA7qqIjqRp0ljDzG-ykOZnDSQzd5KIU2s0u_iBfBTPHUMNvHx-sa2cTjA1YVidpGj2yBeFm3S4_GictcvlQEVEWRQGNIKvLBawmDmLP263deWC_r5x6UccWgddzVg6FPJr_KvGXBiS1mTJZjDc4UV4Ix_Uf2mxR6_bLntP1UzuIwtgCGTsO9NSUjPHApvPD4doBEZi1f4nncyb0mSagBt8hlVxcCF229dYa7UOiK-rFJirkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntGu2s3hfDelCZm0-cRctBX7GKLSiOScFQc3rFEG1fZVt8qeZFU0R-itt99D9hcKMngfNSzC7v6b-Xjy9ErqVlSiXojLrVIl7j7EJhv-_XrsKhma97jcKUcevO92maScgKYBEGAMbWg2K02-kiNCR-McshjBeIx3Ymvsc1Nnd3nHyplhAjtbYMmMEmxJ62E0Lxv9fdp3pGXsc0bMNk7fnaolKHqFNyFsymBP0jrzjNVNIutahUsiEo4gxXiCjs3M0Nl3brz8W9bVnTsfEzvO5bdzHG30UtHqgrvvOyNB3NSZjOAuIzVVsLWRzRpsNvkmKqyUTU1eWHSygbgfmfavOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gpa0bND9nzfGfZsGthEssTf_LoH4gRVFIde-oiHam6cDdRRlR3WD5AQHz_JZsO4T__LdomhbTJbUp1NNZjSUiVVWkw4WNtqTwk0EAurnWOVNGklGko53AMAgrpgZ79HlJrPF4qB1JU_w-C3QZdiQknuzCfjshioMGekLzpIuuqpM8buoRsapkC2UEdcK7ro2TgGVRaOxHHULAWwKMPHFItNAOiW6u3b-wImifGAhmJeZd07o4l9fAqOhO_I75cIREPGsDZajku25zQFXh7e_dB8HzoRvUS72Ozg3TsfXqK4DLec0cf9UG-hH6YjjS8cGJnvpEfye5MtNGw_RgT-jEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXNKR92W24CebtKTMMO_3kL5xH7ytvy4IxLVKhGP0Q4xVJ7hm8rzs4CbKULsqPBpVCKSMrbz4-ku8_vPc1i7VkaUDgGlrDP88qh8P2FCdlNW10p8auNGJrNUGBepmL1k9bLUOK4_mtJiBdeMFQIDz6QBqHgs77zFBa-D_vosN62ehs0MnDceLlLeEgJGOGgaCiEKJr3UTVGzkEStFITnULBnEs1BFt3zoZ9IjkVadphEHDp392e76mDOIpIX_xMafEIBlonzfJaDogGZarIfKlzXHUJ3TgJs77yaUN0yoErzaNFT9kEOa6IRuNgAiGacl0az-OaONy8eYrcu7gfTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpW6YLKAQlJ98NED5zopUyPm-k-Ii82iwjAeSDcTSyBRbOuHSOCuBpt6JOzK8-l9s36It_SuBniWkBDHjNjXPA5RFzJ6kigPmMhPlWXbBVSi_j-TRrjoXS-gXjJ7n8ZisYSSHYuhyQLFChH92MTRBmkwWjfqvc4SC9S-as3GNT3ID8xaCV36RPPaRDezN2U9Dla3j9xOYH3QUnKH_i3IImhcYiMVvM57ocAov7SVL7GQnO4REW_RrobpVT4Q7WOJzp2iQXtNCldgLV1xqNe4oxM3P9fcG_zvUfbyG5g3fOCX86dvj6s9HrmSpVPlruFn87sL04QNQ46mQM6956JR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMZuYV_FFuzaUpMg8zQkchLFx0DG0yp_EsNs4r-UgId1H-KrhLb_2Nxzm7tww4-65Dw__fnKbDO2X7BuOfbG-FD0xdglIEjK084PSLs1b9hWrpAj3OF_RCwqOL0tUx0TqBTgwv9Kwqc7v9LQHC2wCu8AyxW8vuIIFNs_pJUHIhjq6TrrHPGQX8AYDBnBDvuVCUpx2UXQZXBhr1vhNdBaQmpqCEgKatMyhuqFPo9cdoQIEZCzyExZZqcu-vVLOqhBWqwlrb7JlG1JGj0Ayblxq8Vlyp8n0cRIPGHOr92cOziUScT5fJdQ1UfsNspFRswYUIGx4E8NEy3yRoACEqeDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EErAjDfaLAHWoFoI2zc_PUJ0TZLRXTNYfdmV-sZt8GPJj8VDmcpCbcyhh_DvV5dPTAuquIjlx-ap7pl1rLlMlM-kaVxaYJD2HGnj_ylUQaZ4lZDSMJD2WOUdncKswwX_2exTvblQ3CyT-eaDO26lPVOGu2xWOG_rMy4HTmdtAdfxkmotFwTdSQ2mlkieMcszMq7VIzM8jEn2WfHqC0N8PYVgGKgbqbgFfaQY4xt6aTk7axPnM_xl8XsDTzbrhu73j_aTG2qvyVfhEuLTCpjBSnNVuKvCfz2Ca4Pa6SP6aWA7BLIeJKUrwj7fYEFsIxZ6nfTMgIYg53D9GcUwff1Yzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0qi8Jm-4E-u12iG5igIQ_GBSiYKKFWRITgNvZPLs1uPvi-ptLIDGzZrCGcpBpotYHwg8jHlwKMmhawbfsgS3j5YpOyoT8w4GWbq1lUBr0ZeYZDVDKx9PHtcwit1rxVkDTyVg1uMK0Er0xafGUyabhIu3FsWSxAy9s-MaPrZHSAPAz7KegqcWza7D0e0GTkEduIfxaJjY2GwG9tmnu90O7k_aXfF_TrNoDjJ7tyz4Ae7aTVY7StA9Vx6lroZY7vgzHhs535_xmjJGXHuWSxJzIXRoZBZvBE4kE2y7GvpSsQfx9sDKDyc-TiSxl8nfUArk-oP0V-Xwz1hY5BtATRA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXMD09m_2FTwcTszfaVFmAJJ5DjT2kSfKd7hTHu1mE3lCtSL2aimCNf_zO5uHAgMCGnuEZS2tjC7kdo3EIt3IX4NfFlfGMCYIw2c51KhEkPZVgDsIt0YM932D1cqQRFjcNcN5xgFdi1e_ZbpMob5WB0qtuYkuYmzrZOfO28PZBbEfsuLykxIScQ8w3Nl0lF0fyTvJdoFkzxBWAilZ4LuPHqXZvoc1pd1u4VM0rTSVi_8ZAbJEo_v-wU0J4-FD2YK2EgkH1CjZBzR73uQnIplUwfxi70ABLf5_qp_N4xUHmni3E-QULhJzchEqGdneN3T3u3J1SSQvB6JUurLva2lfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-jd3U9pdjwZFOPiGL0hVNbo5tBCvKbxjUJnn-4L8cXD2db7d6M1xeUw6LqwRwxHx5ocOJ1SmIBrEb0qv3-okAofmdKfCadsP8LGEz2get6zVSjT8oV18Z-v1ebxKyJy4i1L7voMjf3Ap2DmuoDpTLHo30xeV9CXRDAHwIs2oxw0UKTqxyfGVbZLEqgfozzeKEuIXzgP76wJGZIFIx7IKCruVIKtoVuvp1N3EXC5PiUk9kLJBchdq1rfBHFtiNP4lKVrOcTYPZoZKlh6F92nQ9cCLhbiJhSkqd8mdbWUS85oQ8llDExpKcKGmvSJvDEEMLwrv53hAa4ascJJvS7bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=k4udHpokFUzeJDKBCRmGhdLZpuWpVvDv-jCYh8icTUGosZQwfNmwTO53an75ymb_j3oCZwnd25uW3Tj5DYb2hhw_pvBrQrLgVWAs-_oUK3EfAATaHNJW1qI3IVJ-_ob0_PwcRxX-Oy_i4wQ0YQGCuIxcMZkI5InxFGVHdlybg8efZ2ucsAEUdrd5a0oJjrR3RjdE2UHR-u_5glJAkTLv5435tX-kYbtiJy-JZKnKhrTOJz8ZL__wralnMi0ilcpcUhiYkgGK_j9wpCaXjRQ2x7P-O0SbuvYwn4OhNu23CjLq21hLTM7rsO7dgr6S6AcPoSAb8eRuq8kiuTMXE1gsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=k4udHpokFUzeJDKBCRmGhdLZpuWpVvDv-jCYh8icTUGosZQwfNmwTO53an75ymb_j3oCZwnd25uW3Tj5DYb2hhw_pvBrQrLgVWAs-_oUK3EfAATaHNJW1qI3IVJ-_ob0_PwcRxX-Oy_i4wQ0YQGCuIxcMZkI5InxFGVHdlybg8efZ2ucsAEUdrd5a0oJjrR3RjdE2UHR-u_5glJAkTLv5435tX-kYbtiJy-JZKnKhrTOJz8ZL__wralnMi0ilcpcUhiYkgGK_j9wpCaXjRQ2x7P-O0SbuvYwn4OhNu23CjLq21hLTM7rsO7dgr6S6AcPoSAb8eRuq8kiuTMXE1gsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FLUtFwycosWnZG6sdNvAEwhs6flc6CQmGF3raDHzdOa_Fhg5sxzMmcYxKS_xkcCcf2k7jNBuIjE-YzkXfKpZ7x8yKKX1PLDcl6Xb9YA7afxsgKURRJUXgAipNUtj9rPWrZ-kJTNwa1wrvzgDnZHAxtZXm13nYun7YU8EM1yBOMcDTS-diDmzXKbYCJWxoLgdOsY_IvQFQKmiyFZk2z6PEPePUjAzqxRq3x-klyHCyVULfS9G1T2PK2TqkiLCGGNhUCNXwxRb--7he1W5xVh0Xc5r6B0pVPQYzcY1fp4XqzD2Xbh119N7_l69-iaq_GvgZko5USm_gZm104KHqQT6kC-IQeq9C1wNOrWaFDTmkh_KeNhMVl4BL7WQOmXxrhnv1BzolFQSkl1wwCiUROFlNpFQvvzwP84RjN15vzNS4O0pP8GUdKJlm-V2V0_3chyKgdyvmJ2aKQYwAH3-yvvBuRvKB9CpGHeCF4EEvfbPicybxpFR7LfxFIaj2Kz8-BIXylvOT8F-JEZL3qHtDoBJnNlxVi8QEbYPaebC-8HnBuayezc6ACJSJijpBgPHxu8cY4GSjTFmc0zxJtKXYYmwnUhjqIWGo_9df1pFExcisXPBM1nFmtD6bTwHoDMtx8RDRzaCoNRVf57pDFVquZmkZvKoTNo6_2h9AjKXYL4_imk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FLUtFwycosWnZG6sdNvAEwhs6flc6CQmGF3raDHzdOa_Fhg5sxzMmcYxKS_xkcCcf2k7jNBuIjE-YzkXfKpZ7x8yKKX1PLDcl6Xb9YA7afxsgKURRJUXgAipNUtj9rPWrZ-kJTNwa1wrvzgDnZHAxtZXm13nYun7YU8EM1yBOMcDTS-diDmzXKbYCJWxoLgdOsY_IvQFQKmiyFZk2z6PEPePUjAzqxRq3x-klyHCyVULfS9G1T2PK2TqkiLCGGNhUCNXwxRb--7he1W5xVh0Xc5r6B0pVPQYzcY1fp4XqzD2Xbh119N7_l69-iaq_GvgZko5USm_gZm104KHqQT6kC-IQeq9C1wNOrWaFDTmkh_KeNhMVl4BL7WQOmXxrhnv1BzolFQSkl1wwCiUROFlNpFQvvzwP84RjN15vzNS4O0pP8GUdKJlm-V2V0_3chyKgdyvmJ2aKQYwAH3-yvvBuRvKB9CpGHeCF4EEvfbPicybxpFR7LfxFIaj2Kz8-BIXylvOT8F-JEZL3qHtDoBJnNlxVi8QEbYPaebC-8HnBuayezc6ACJSJijpBgPHxu8cY4GSjTFmc0zxJtKXYYmwnUhjqIWGo_9df1pFExcisXPBM1nFmtD6bTwHoDMtx8RDRzaCoNRVf57pDFVquZmkZvKoTNo6_2h9AjKXYL4_imk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
