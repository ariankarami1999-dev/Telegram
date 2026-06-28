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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 329K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=AH1GOFMqhhDdrocvwoCFxbD6_xeJ0d5wCPz_cWtIPaej_K2wifguWa8D3QdD2kbycPaZXzJk1v1RZL30znA4zY_aLrb-NcjZ2Q3_ZXNtwwgghYsGw53VLcnN_V-SpKgzan2Z4Oni8nDnA-OI6VpZLy0njnB43lQq2lRzIerSbZpTNc94f02_cK4ieTMnXgljrl9t5XF2gcew1bpcI5TL1VtSlZAGPOPOouD--v2o7WCfK-7DkEtn6ert8tiC6UPUfeGiKt1pT3ywlWLne5WC5UPaLz0BrzQ2A2KIQ4wpS4vqjSVC0IVyewKhjOVacZTvQscu8gOjpscDnUyOuEA0dpVjuSqx5XeShFwnikG2GRfS0uUIkbpi4HGqlOygxZn3E9tp4amSd42kqg9lipPbV-yz4V7Mb7h2eCgPHU_imxZka6RrQmEw9aY_pX-hyC7r2ZjRp__OX87m7j89Y04URFtsGju1dVGJktpFnvtDrV0t43_5NR5dsTJ-e-zemYMSe8lPrbImcTM7NZFxD9Tt1mkVoGydJaDqc3-FqvHCBeoU7Sf_i_v2SZxd2MLavn2bljbT4odff5hHIIoDCfRve-Yp2x11WdBtZARO-bbE-3uARrDRg3xhp_UoAGsQzkNgu1U1yXO2lMQFTxr23Q48Jap7J0pPgiMTMe6HhcqM8ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=AH1GOFMqhhDdrocvwoCFxbD6_xeJ0d5wCPz_cWtIPaej_K2wifguWa8D3QdD2kbycPaZXzJk1v1RZL30znA4zY_aLrb-NcjZ2Q3_ZXNtwwgghYsGw53VLcnN_V-SpKgzan2Z4Oni8nDnA-OI6VpZLy0njnB43lQq2lRzIerSbZpTNc94f02_cK4ieTMnXgljrl9t5XF2gcew1bpcI5TL1VtSlZAGPOPOouD--v2o7WCfK-7DkEtn6ert8tiC6UPUfeGiKt1pT3ywlWLne5WC5UPaLz0BrzQ2A2KIQ4wpS4vqjSVC0IVyewKhjOVacZTvQscu8gOjpscDnUyOuEA0dpVjuSqx5XeShFwnikG2GRfS0uUIkbpi4HGqlOygxZn3E9tp4amSd42kqg9lipPbV-yz4V7Mb7h2eCgPHU_imxZka6RrQmEw9aY_pX-hyC7r2ZjRp__OX87m7j89Y04URFtsGju1dVGJktpFnvtDrV0t43_5NR5dsTJ-e-zemYMSe8lPrbImcTM7NZFxD9Tt1mkVoGydJaDqc3-FqvHCBeoU7Sf_i_v2SZxd2MLavn2bljbT4odff5hHIIoDCfRve-Yp2x11WdBtZARO-bbE-3uARrDRg3xhp_UoAGsQzkNgu1U1yXO2lMQFTxr23Q48Jap7J0pPgiMTMe6HhcqM8ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp2Yz4_mJgNXgVqQaW_qejN_dVIu0AHs2YaNQVO2NCxUT8AeO9oMVJOz81FpxKDqGz98HrTeKS4V6bJbwZZppOkUBPUoOB9W5lQnmduCojm-4NTk75ms5s59fyP5LtQ2gUhTgtOfTtXwOvquyLuu4WNfsyblxdg6tQa9V4xOiCZZAU4crUk_YgCC9Ei0ksa2TvUnwGAUeX6iZcgNKbAuHbUAl0h9ELqfKh6myh7EfvSG-6u9MLO_Gpmfo9G0ZaL5wQ0KlYYQFxD2EmLFHsRr35Rjj9rrUQEDgay0UMMIFWhUJ5kAGvosuqJBPVgVPVL6ZEzlF-AbGJ_31V5KLst_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnYZ0wfly9rqkh2IDpzvlIWIbQiDYC7onrlXtQU07vR9nf78ApIcxuNYKg2v3gFD03fvCqwIDyN6TqyLXLmMhu6DG2XAnHg8WGtU53tmbwjLs6qRcOyCBbBN94TAQoqOAvoNt33KJxpSLYRLpEqIaMb-hCkswvRkwoe4JxKjTtKk_zQrNd7maRTsWJk2jqKGjtISBuPmpRgk9BJ2_w4OswA3IBH-PrFjHa2JRqwZIuirm4nR6lOxX5sfck33ccXP3MtzjkbqoTT7Lz2MDSP5P_1X_ryRHQYkLdn3NCm6FDB6c5UpRACGlj12jqu5gWHpl49iqv6HZGg0R0n_HxTXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxgrDAi2nU-5CPClgcmPDEnTikTSDnFVBrmj9qDsS24YKN-QPj0DkyAbrjsVyKD83RyrTs39H-sRuD3Sou_lPA00P0dhkYmenTgpoUdENGyKKB6Zflq0TeTXVynQKNiHaV64U9Wx0U3ZDlepXxVArSiCyAVzvKWBHn9XXVR8AAkXPYozl9wlQjN0MJETQ5LLWHeZjk-nIImDCOxYKDKk36LyC_DKHby5d588UyRmPMSVUqT7_CRBBdQLjv6O5KrQs84VY9Ryla9A370_ZfxWoS3OOMQeo7_XvfkUdbC2YzfRfFkQT1wZ0VZt93Wc6WdwIWwhu0sLe8Px_vYxIQkr8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOTqvZbAx0awZs6IvciinhavVKVpw1dnj-DlB6rdo8v7ys_zhohj_IM6O5A8sjr3HWz8_8xsbITrfjyb5UwSzqUKBUlQ9AM9tAJK2lgpbIkEHeF3w1UoRKuP86p1Y-36WQg6Ynr4SnlM8jWWAXPU5ynHBqshkZhmm7iN4GtnRrNz9mpKbuoyaSuUeLd_6kwRCDhlzkzVtilkd_aCn1HfqlE4xbCBdAjQZfpKRXyra9-p6XyDcN1RaGtJNKwlIy6MqWJRdW0NFOuMYd_WPgBiZXdr7bkz64mAV6VnGM0y_SPz8go6RfKoT5gmyvOQSmE4Q0csnO2or9IGM4EkhsyjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-f8Ou3A-13JGpNO3akjw2xIl9tGszRwv7CL9WZ1DCajRd7IXBYIksvTcq4g3p_c6ZqHo9FVH1xtm5iWI50QQGxO29d-npNxCHivaxQHKkxrhriuPMEmX0j9TliO6Vhn9QdQo6HZEa62kWk3Ws8w3zdfEBWv6wYGMmLMZU2IAKNyZ-zLrch22La793K7sYbWV_pyZQM8cqx4H4FEv7MgckL0bNuHG1kkjc_NNfBYIYZDJGG9eRgfSHFzm0tdxrtdRNeKMxZ3nHYtTaLdGeekE5XMzm5qZzlTh_mgr0-Vk28DR-4H1jIQtuIERYcd5jLOCr80YfoWU41YzYykH3u9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERhzFCEdqF3hvMK2ms_zAmuOtI3hUYFefY-ruvKtEabgxPv5MZnIsPiME0JzmLdSBzxK_DMNNknGsfqjP7JFpvAhbgeu4PcC-lvUpkKMi755mATLZmZDWcXOKVC2gTk76z9Hxan22j_BE6-GdupVkbBizTktFU4OX1QHxznHtgNV3DIB_hR6EkSDfs71GnB_mgfEKYgnAwBwhdXft8XaG5nmxFiGJX9U4zNvf3BXYSoWXvyROMUcLw6fHshdkoaaQmhZg0UpfVmTODMyMkm927VWdhto22E-_qcAyouT-C2xG4cmm-GRrN3MbpSNThub8p70hscQ4ryq8gEELVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbUZTsSA-xwyTBW5r_kzNNlbN8IndZab6krLMCGWK5LMQsuUeJHp6ePRS6kuWBNE3zHoCHumKw9S1r1UTid1hr8959QKz7sz45zmBo0PVAQdpnUxgoVs616jmfC8pFsCAddz5ph9JKQt8H13SNdQCkoCMnAMw60LLc2racqRti256i2GjOtUTQw5iAGlXOAqoivbZip1LcG_AOYlcv1gzogtuVe0uil3arUDGgecBPYfBc7LDLnxAcu0wadFErT7Ben-nCnd7OhTYsGspsHS43besqPm4-4BTVrYLsaDNHzRtADLkqZXCzYYuaUMJGlh-HJJgOCKWCWMnNzdU7nBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5hJdSTYsRdgmjPhUxmXY0OxFCAoTwEPi7WCfnbGKfH0uHHQ36FjYyFpH84tI0DorY6FMfIb4wcFFvcr13WDBtqIMsbmeEaQ3nXxbzKo2l_N-DZk0DLFFuYWuWFDYjjvRGoCKZYy3zYTXBpTMIoRT3T2eOxs8Q_LuUAxFqftvBrEJsfpKSdFA7eEMjq07iqMBfhNQHzHVK9o8eEsj-jZkP_2JQtZz93_8t0muLKrIst9ye9SCDpBN4YtxPChlJDV5ag5cd9k_DWOSM8vt6ho9NrVNKmkekP9LKME-DpeZNLfN4QMREiyEhdRuk1BcB2qyW1NDjkuxTcUmKGosLbozPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5hJdSTYsRdgmjPhUxmXY0OxFCAoTwEPi7WCfnbGKfH0uHHQ36FjYyFpH84tI0DorY6FMfIb4wcFFvcr13WDBtqIMsbmeEaQ3nXxbzKo2l_N-DZk0DLFFuYWuWFDYjjvRGoCKZYy3zYTXBpTMIoRT3T2eOxs8Q_LuUAxFqftvBrEJsfpKSdFA7eEMjq07iqMBfhNQHzHVK9o8eEsj-jZkP_2JQtZz93_8t0muLKrIst9ye9SCDpBN4YtxPChlJDV5ag5cd9k_DWOSM8vt6ho9NrVNKmkekP9LKME-DpeZNLfN4QMREiyEhdRuk1BcB2qyW1NDjkuxTcUmKGosLbozPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J98If_Tj7uyLlEfqs_QbHUO9B00JrL2AV7CdL_roRPCx0Kfd4lefrmFQPYtvqHkLLeubtFi7nFf6iGBb9o6iLzzr1sj5AnbYnHasMmoTZ5tsz5flXDXK3O3CwSG4x0pjbAlFFJwHesAiU5kkKSjG8W4NCKCIcGQJPWIJhZs2NpCE6muXmE3LvzJpHShAZlSh80585YdQR9r1PTgfguZyterUn-YWi5g4J2xSqaDhH2kn5-H_eegOZtvQF7DWl3g8XXqDlvOQi19z2tJ6y91XdsFnDBMgU-5PIwaGsHUUKyswVsNYujONQd4E3XrwTo5a8ZipXnZgqnQnZt1Ixz-YKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR_zC17ENOIM3DfmorwCGtJpJhBNSBeS_SElA0j1bBJcWJLT_uyMW-BywHGlauF9ewaTwNkQmFsD6VnXieM47vxhdnjcHqncWJ_jiclXE7oRbJ8hltBBQh3NTB3p6Ri2QPFuFi8gJ9edV7Pejtkzs-Iz2zapjJJ--JNt3IyT2jOCOD00O2M2YMeBB_KYzWy9LpcLCbCoHOGTgXz4AuMkGdZ0lEOWGv48b19dFmyE5j9AFXA7WxRHtu-Aeyo0C0et--8H1x_bS27OVpUj8OadTWEzI3hR_Dy0Maj6usTC-rcJVczzvQ8YybTCCc3TC903BFiylxBcBzl6k5eOtx4A-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/citcQAUscV5xbbZglTg-G-ne6O4sD7zMTFas5J6LWK0DKuNfcQzYu07-bH7pYrwho0-RzSJimgZ5SycWOKrH-XCMWC-KFX1HNKZ5PHQQWxh6DDRi0r0P_2Qix9p5lCPyA3Bajri3SU965i3wyBIxt-Y-nW5J1fuJkAl-JKGbaeig3FguFXAZ2-Fa5hXtabloRO4ywFMskBEFjZaxz3oDLwcDy5NrpRUD1KOK5z-zdXiO0Fm5Ad6TQYAbYsnWw9zSlxUGMRSeK3J4Ya2gti7DQKryPNsE9aTF3EGhdqABzTKDXwYD5HNUIw2QPBieHfNnOA6mUYMMBo1hHrmpAXK9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgFPmy2r-_XDZZI4R2M8gJHQhR0EbZX2ltTQhyDh-SvP4LePK6uVz-Cf_AxEUy3I_9WSLp1GBqclt5mwXwt6S78dB1LTbgokmXXv84GEV7rbw46TncKdN38ybLXrcET3sqhGsRHSJxWewaRIoph9sdugBZI9G5zwrHcSfRI1RrThWkn1ifAnC5gnjmobc4aDaagFKSM1pFJIRjeqdeC5czRfmda6VaPZbAWBavK8SOT67jtB5wv-m_M1Y66dXlG59FeqGofq1ah74Eh92R46-4Jez8lc4JMPeXVXGS-mT0k6a1H1lKX4yW8G9uK91WSnVtPJuI1aqPUI59VegWScfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqmPGL_rrOpcw7BQ_NN49wMXROdGDMSDSS_5ZNQ8VGQTR6AE7EXF8cuJ0Z4t1NFbnNxn9z1aWbr6qWB-z-0u_IbtdzwClz6CpZ8zxdo0aRbX50SHhFxudqSMF1w7vT90fDB1KF99QQW3OnLdVadSea-YywwlsQ8_IfwfdYC1L-Q_v-8GbJHr0OEjfP7Vvhf6RjYWfpdZvCSZKmQZboaKnBjUrJ7kq--5gVLzwXQtzjbufAi-W7nSPQgGXkNkCCOBBlLpiqG33bVFsSwEto2VpnF6soTm1WdeQ7zkz8hT9Dwa2A_N6x9HJXNbHC8G3qYXQBpt_OgtM5X_LM5kLntIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRcrWkUpT1_Rg9GSMMm_lfhMYzsNwFW0Uc1eakw5VRjx2mz_fsTk4t3zblqyQYZDGFV1-3DTK9Xa0k_LzMdogt8dp5Oa_vZTgHk4kZ5UhkcZWvjy-dYn8h9tpxLpACfiuGcxb0AR41dChFw64O5p1mB1WyxV_qpVq1nVmcWJJESL83ImY9fzoM3XHmbaVTFDV6iWPKjVknD0nBmlPwOcESh9lz3PcamftEXk-O_2c8JJ1aVVsiOgaaQrMzwdzI4niZlOp7ek9ZJDnZV29UXvMtb5ITKbaxaKfHbINlWGJxbulBiNLYRdw2zRV1l8ooGrvfwd0wV0Eo5RVWJdb7EL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq5bEDYrw468VjfchIFb5wCOXQCBlKaMoKUTvTExF1vS9MLjXHPn1WLGDmYk2oHGPeGU_-7_apqKj35A-5ma2mbJGT9EAZWmR9BTwwFe5EH07Xgm6PLfGmstT-iusii5O6hUq6-iWpXHLPBPcGj95Rl2phBoxhQEQr7osn01ne2Pxuvmh26sk2_hCc-Zn9j3_8q2wZmsfhH4bab5QgLnTkT75sO09fZRkwd5pk4oTIarBugnJ5QwS-D-ntzxyNi6CxqKt-nutbrViVcijJSCe1b4rZisIIAncwnzi9sSpoQpopueQfTco5aJ-jmF_hhoo7vQHgtWef9y3HQYb3tgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeb7hXk3EwiMKcWbI-1bU1t0SDA_YDZkGno_dVcUFIIKD5MdAHl7yxCK3bGc24RawcCt1Y0D8MxfNfJTyVPgRwJrIvQLKbkRt4Pw4kqlAFZyllOFwMpMmXKnr2xsSHxvgQvS0YIr_4vmUbc3QOCNh53EZg51KzHx3jAKBuo0oxIqHE1U9lMToYIlm7Zh8SKCS44tt-TfjMC2-LLs6lKjZYgxHbpG5faNZeD0u7PXB5wa_DKNO9YKp1WQb6GiPs64hATGAdOLG4P9dffHW7CxcQtfVhoxSdxmmk7fGY92Q9csptDkQJEfnCJWdqiAKtUmzMUt1rIQZLl27EDxI2gHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCMS5wMKmZ0G7DK0ovXrFIyxpV13qG9HZIa1aSpySIFF5lFG9Fa2YVivArsoI9obZTbCinuCrPvcMhEjeExU6V-MsxNB51vTCZdNoTbsNQet7i52g6DHlmXXx3yedYzdUC1IlUiruoa2Q_iB1kfcXKRy2t0gQ7E8obscrvsjDAJnPxBa8S1JVd2IPIWDtcB11Qj6mI6z6tKmqeV55HbQ6iELImIy3MKvci19Zivz6qchmhHOPtV3hFHnMw9XqLcK35b_WiaB4b4au2RvKpxWKEJvMRSdL9GQgb7dRJqNG1BrgySaU91hhsa4Ew_uREeDcCtBvX4-WHeniZiFxPezTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l45UZTHVz3bJIDOieOkFmt4HLUlXFoUwhF_qGI1r-LecV-GRKnv2PYcTWUiYSp_iKSZFczPp8nRdEyRXiCb7gioXJxoeKVnrdfrssIFgSatjpV2Wh9U0PGmRXhxOmuWsr8Y7SbVeXJ5MR6DFI1kz96V1sph17OImEI2PWvmOg99yZAVnR5Dg3yjH8LsjMGym4TxT8J8x5-75kMULvuibYOeNSrSYiXbZgucr-Rus2TCGNKzG-2TRNE_QQ9du8z0-petGuF1DoDfcnP745wcCFtICrt5R-TPky9cXVGHCIQt1Yv-Tn1NO1JLi9mmghq6JB56Mnitf4wEAwkMcs4fBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkBqacVAAXT0TPLkF1a-ymhldOzxHbKgkPrRcL6StbyisgBV43Nw4uKGXECz3SPq-oxzx58l2y06PpmkugiwYF77uJLvfLIg2M4I7jROxs5Uq3otxDMbqeLRbfOQbOei9pqQLr8EnnuRA3G062EefuwuY2beSAhg68W2mXGWo50jCMP2Ziv_GP79rQF9gyBHSBMpLf4dp4aLfjipVQMF0j0BfiqXnqwXZUbZravzJYZvc3uIA4cIVClqVl3bYPBuoy-A2iqOEPFOFfT0nOOSZakqg09hAwDypKvNSaLWcQtTWzhOquE5jsSgPcuOkBu0DGFuo5iDhVHFpgpkgDGsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUf_cmzLhvi-LfLU1vm63U24P0wzrkH-B7ybda6nxyK6EZ982RI3NWb5QjPzXz65nILDye0ObiFwnoEcwryXHFbm_2Hh-l-E1v8yuWj7VoOeTiE-H8KdV5qfqVKuUirZ0l80YBDTrHJ8kmx3qu_ySlsDbArsMqDS-E0gNoO1TIIf_cSC2oRvfD6L6CwOXJ_n1ViNvIAr_5OW-N2qtqvpFQbWnlW5FSzGeAal1w05qitCF-fqrs-1G0H2VXfb-R5xJ6Gtb0Jst3g2ngq-pkQVU2kJQplazPdsu8DoCP6f0T8Q2wAf8xD7bto68hrrpUzmnUHZRwe99x6OTOVuDYawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1fT1baBfZeBAaqurmo0eM0StgsZmlKGfoTXoK8JPswP8WiUMwlssOvMZp8EFz4WRnpfXiJlTILJPEBOxJIO746b0TVlGGGE7vGwbHLEK9dPrTospJva6MCa_m9rNG0uCAKDhuUjqmoi6TmEn3S7CIsjRVANye03pT67-ubxJSwzt6XWyv0rUBR2gncjI_HWeg4RbrA7EAsexnX-frZAOTshYR8TiuUc76L8YSGQOpvnhYXae5SH8vbDQ721mJ7WWe-swW7n_gK_6ahYgGtv-B0787NW6-f7zVl_5CBEnD7tzWToAh-r5qE4kRr5t7cXWRy76F0TCtBm6uLFZljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQSnunTtcKL0vdieXEwMC0XsLji7RJxd4FCdGzQ97LNsDpLWsWeQIEpTEPyR5wpOuORvqyGwThwNTjKkq7mh7JCSoMuLziMhKOX3pokyvmWl9HgTyBOABMOaq_n0_CHBrwIzBZKOTjgbqFXVZOvPSEpGAJ3mvag6XJqF0AHXIrqKN8tBaWjpknjD9T9B9oouoTQAv_tgxawQhD0RbLdx91xplnqDTE9l4lVQCXNFidO0462y4a2BBVPsuXyuzGMInhUhldcyWCDHurVu4d9oKivfaA8vRvej1l2Ai152wtYPtHE0MS947xLvIctb6u-Za3oUVzmLn6hPVvlvkF6GAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLVvR1IxQpsK67wJV7sg0bfl-lNXOtCbzi1pJmmIisD0PUscowFiDQTWbFhOQQujymqcYmZGShE1vO-ha8YWvY8YVKaugLSTZfl_NFNKvfM1bO8IoM3lbww5Y3KYvoNLuq31cOqhnKS2kSbFFoHPhYrAUBSCYh91va08we51DhHBjwQqlkRoWTKdhx_cQ8Py3N25j0Y3NA3G60nC-0LZb0yo7m1sD0gIW5e48GSZxr2GVeJV3wu577IQyXAiWDUHfsNykoWOfSj74dueVHjjm68-4pS6Pgb3rA9MMd4PDX0Ig0T19pWDNGndfwl6n-BW0h-Q_2BlNX_HAVSXfHfvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuoZLpm3sLiIrOxwQ0nrtfHToWpZ0lmG8TluuZ_u-J9158hWClNJQX4CmJCui1k1wmyEeXLtDkShnVRsMR5u_MTXFBl2scUkWDclb6vVhb6wRsPpa0eOV3616FtAjYi_EyKprZczUv3a-LBMT3117cMPQlQQwVdAAxb6P9TrZdVasG_owRyBsWdAyW2MNdXgG1XYUxXmYzHYdvaWGeJNSSRAlEhrhmwfSHPQBYOH5UjFHh6UUyQz-6Ary_u4Exv6WddggXEtvPCQ8VEVOs_Nq0iigLeEL07Pexpclrt8esBur4cRWECYtwFkGR4VMErsP1544GsP0eUNcnDZTOBxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=vRT3d6iN5-rx4M9kKbAwj58eBIzkboBROJGZzzW_Ucc07OjD0CnbS38vYhTycc9AlJHgz9Oi1Q9nnIeYCHMaFHkIavSW5EsnKKTAMAU-G8kmPv7AX1RSzi6AYG-tCsRED5eMeqwxAhpOERYgBVtq1I__udXZhg_DIEK0uLPir6ZiV2zukb3rOeqDWfgAaU8eIts9vUvHFp-CVZlS-i2vNbh9WUQharWI34gdaYZa9t_OOQEE9SXiJ65dfxRX61Um8PREY0Kh53HanSO2_6znbY5fFW-D1uaIr2WNuCmUBl1gGMdYbt7eXBkxO2-aQoW49wd_S4pBkkP7LxBbdHnl5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=vRT3d6iN5-rx4M9kKbAwj58eBIzkboBROJGZzzW_Ucc07OjD0CnbS38vYhTycc9AlJHgz9Oi1Q9nnIeYCHMaFHkIavSW5EsnKKTAMAU-G8kmPv7AX1RSzi6AYG-tCsRED5eMeqwxAhpOERYgBVtq1I__udXZhg_DIEK0uLPir6ZiV2zukb3rOeqDWfgAaU8eIts9vUvHFp-CVZlS-i2vNbh9WUQharWI34gdaYZa9t_OOQEE9SXiJ65dfxRX61Um8PREY0Kh53HanSO2_6znbY5fFW-D1uaIr2WNuCmUBl1gGMdYbt7eXBkxO2-aQoW49wd_S4pBkkP7LxBbdHnl5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrApB1TJCqgNvnBR6loM0-wf-09Rn7YDNB_muLmMxRzhJF9IWa_WCEwDeK6dvPkYU4ytqlGnajRAF-Z69uLvudsscPOniR2tLvJvU5DAIaaQfP2ZBnJtp91MsOkdgTpCqoroxy9r_t_V2qUFTxUePcpRDmVryUG99QbFDV3V7s8CPjMcpgZtzOG5reETbaAbrhbesr8jGHp0OePn-DISis2QDhBVtHARSQAJVg3mG6QBsY9UJooRfJCr4tSPgz8RvLVC4vObNxvhZ1HdfPpJg4hzAKOedAvrKsVGp7I9ZxNwLNcmPuHjwLXpFVKO1JWYWpB9DM-b2c9aq-LjUgqXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhgPWlLCdtgir2QgBfhV3KQWc9Z2gpFztavXN_6zc1B-79jaoIpRhSs2BF-Qigk2kLpsBLlWUvmDVah60BG67hWNACZ6IhkfqWMhoqQg_kEj7s43fXwO2VniDt0ZPcmCHpbSnL6yw_6msQq-vdODvKy-bRgC4yWV07kVt_ut3HRYC4ujNR_eUHT41WoPSfU4jowncO-iBzHppXBlAfMdrSKaPYAzqbXb18svwQm8UPMo51PlOGXQzhvCfRmiiDGQ9xmpDcy1jw86HmASunX0CSauylYHxD4mgNc9v6B493z6mVg_eDCBNys8ctIb_fyGfSLkdKc6Yw2MO9b0X5bN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joLOw4_E0Ai3duOfY7_oCjubWW7BCqyZVgCDws4gpnMRE4ZHvUdkULRShc5hpeyREgITxQMH60aXU78enYh9qlvbEghcT7TckeRprzaq6ySrD7--rRe0RugzCwhan7yU1HOZOanmAMz8mlDH6GA5FmpFYwgYuUrs4C1AqNH_WLPh9rs-etlWj1FAZ3smZjWjDzZYp3CGbwzMP96IrV1l1NHyDxebOb-w4oauBFVUutvrzdkkkyELuKjBZ8qYGY0t5ckgb32Q1jqOG1E94Gj6L-g5pXB-22t2_CfC9HlGizxKXWanKXteFCm7xmThIPSPeLa1IT8K5Eig7PLTl9GUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2IxL-mTR_E21e2b_CkkbPtIVP2QNpcxYTBVSytqpbsdhLL9wW_Z9iuUWtmhLmvQb5hIsaTd5aa02Raprr6tvua_XCiQHwUWMEhf2CvKoY4rT6HF9RlsUGLrFRth-nsd_ObsUWswklsyg1yhKW7A38K8YWbNkzsOQukFM0z8ducqIAwsV-VAw8hfCo5t6bv-BWeo7yjyj9wfxc6Uv-nGf1fOYVmPRYcwjgGAVREswADiNe8Z-sNhEpzAcEdKnaAGKXXtZk-G7_sa6Uw7-5iHhS7ByjZk2-IZ65xw7osuIjQ4l41QgiLvTMK5k-kq0Ts5cZkQAPtXckQJHKqbcRiu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb5fimENuMiKKii6N4Pk2MG2LVvqbRzUAwfUzur5rW2_QhrwiG7Esy96eyP2TcQEjRPncZ5LMntsVRHgEQXLJO5Rg3u5Yhpv0jYy3byL_i1ZvkI6Vkk6vhlIuJdbulUZs0pWGSibQW3vfwqR5sJvTB5e_dH7U7yA6jMkL8syW6yaRmILz9xFRZB1GRwofNgbjjjWXw67aWFbsr8nvpPkDcVGIcwK3hDF-smQID0G57HKA-g6saxm_xZApBvqeJ8gADDQsxZGH0j1eiYgmNLFWEspfbLcq_9txy25SSW0V2OaezBr9JVj1Tpib5MnSonkX-zFJCfd9UoMpq7QilJF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7VrzEdZfmbfFFPaHMz3iVM7RfPA90y0ASYjAxBPydvywbOoHLw9C4eCrkLtT8oqCa0q2FfkG9_w7cvX50C1L4Bp0wNNxtqrfkMtWHMg6ZunH_FnkzA7XHQr6QvF33DSZxNGHU7g1ORhvioulsqYsw94NPHGQ8iN4OSXBrPd2yn7uTNPw4T5AI2G3_u4HhBwg7m0u-ksfrzSYhllCCBNAZdzlNRzplDO9sJ2I1_X0u_VgQyv-oEwZ5NnIe_71PHBQY65KegkYgY5FMWtwAH804MfK3W6hGwsyIami6lii-B6psbv9obXvlfvXCiELShpCSmW8oO1DJjy90sUXw_vLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4LalTv3ZrClMKog1ccUCxb4nBZDqMKaCmFkrbENt_Di6OE8c1Gtpf8gwWsjtZoG_aVql8gF-flmjDVt-MS12UVeZvZ8zFIqNRns3blFjbsZhcqiRYdDei2NDI6wgKC5aoLmYnq1XUaR7zoTDjsiPvIJbtfuiQItrK5d8k4QA-plFRjVPeMpZr3au8yuIjjvV3ycXin-YfOgGVzdqpbxSDHX0FdLEk5iuiZYINovXYhhk7ns3jwkHoMCF9IM5j4XUMoqkuZdZO8PyjFn31caAO1SzY_WyH1Va6R43c8BaY0O86hvSGI1CUadHPcCn1cjR5QE6Qa3Ot848cPQ0LJmVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWeGjjjPhL-qRUnKQlO_Iv1UjACuQaoqeNPmbT19A0PaEfQh4o_xsxYtRwIVxXGqdc74LJpmA_peMV2FRGo8mIBn2vhhwIYsBQqlTs0WJQGjyEbNk8QwGYI6VViaACfH0e8pZObLckZ27XcjdKU0oCKSwUZvrEIW1zSlrfJm6mQXB3IaoOroaSmCv_1eiyIKZVRconMEnVwkrFiQz_tdcp8PF6acA7LT0veVnM3OWrL6IEL5efQV2fYCnC3pgh5ze6Q08oH3PAX1TJvkQcy5bwK-DpLraSf_Zq4f-PgKPFZnY3pBMTxGVGKLzkUUZ5PsnZSXm-K5g3u9EUWYle7ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcFLMw6hYoEE13PWVEifoHifCUG4tswlEeT4TB2-oVe9wRXLg_EAWspjAyLH4Ihdlz72hRHSlqk2ZM6wESOtwu5U6u2vylYPGmSciMhnD0r1JSekJX3TcZzwFtslpOV1QdhlA090y4ir0m7pA8qisRin66xBzGnhBJx6Cz7nYmR3jdX7iWX1cK74hUAYxPg1270YOHQdqtl257p7joFmpKkQKHeGQfoJdKQZomLVKKgPcaqgpAHuD_dd0xXvQH2claGniW3cLmDJ7zK3UYeeYTFW1vWc-4O4Lr83sxAFRKHbrXKbWJ2oVpQHzxTJtH6k1dchMyLcR5VaxZiAH2bF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=O8MeYmisgNtjTzlfBEO-tD1IyTvsjE9GUcKOMqkYeSNWx2FDBps3xFf1rHwEtMYTevIcPSDFf-RJdDLIoCJ4lY9mut2ZcNRxhgRb4DPL6RfSYcyNpMXHaLbc67H1FMX9u5zQ8YgZY-KSYU4GFkq14Z6zjt51maUOnCZH5JbarO_fOVHaPG7XI2Qxev9WcleqhCKj3ywDZn3op4NUPWPnpKGaE7ajyCwSkTSFuMZIBzA4VQ5x7qepKXdtznjfOsIf4k2scp-Y9gDELbSWiytVEsWqjfVH_rQA7XCTWOVzJu6isUA6RVM7Pb5hKR0DL9-CuxJzFm4j9qA8Sj3cG0V0GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=O8MeYmisgNtjTzlfBEO-tD1IyTvsjE9GUcKOMqkYeSNWx2FDBps3xFf1rHwEtMYTevIcPSDFf-RJdDLIoCJ4lY9mut2ZcNRxhgRb4DPL6RfSYcyNpMXHaLbc67H1FMX9u5zQ8YgZY-KSYU4GFkq14Z6zjt51maUOnCZH5JbarO_fOVHaPG7XI2Qxev9WcleqhCKj3ywDZn3op4NUPWPnpKGaE7ajyCwSkTSFuMZIBzA4VQ5x7qepKXdtznjfOsIf4k2scp-Y9gDELbSWiytVEsWqjfVH_rQA7XCTWOVzJu6isUA6RVM7Pb5hKR0DL9-CuxJzFm4j9qA8Sj3cG0V0GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=ag7XEAgLISu-xUteo2pldnN7L5VqfvaD0O7QSs0-4DnTDuwUs3FaRaUBWFpFr36mwHXeFJrn2Q9uaAXaPd2A2N9BwY5vwcf76GBK376jiz4vCp7ZOtV9JBwHH0tsiOzpx2avfpKnbNhVPmj3qJJtFqh-0nQicXyFNbFI9dzL8FXdRFKkhhecZqfPf6jdrW3iQeTrhhek1etDThiyB6-zLhb8B9QlFJHO5t5klz3-sXDhqzP_zKFtcBWefc9_e1-Dc2wOOuAQbTf3UYsEqY2g15bOT0eUQTKpFl-jLR9E_EmjOrg9DgRLe6q9ergGWMk_xQhFn6MtJzpjhogTuk1Zqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=ag7XEAgLISu-xUteo2pldnN7L5VqfvaD0O7QSs0-4DnTDuwUs3FaRaUBWFpFr36mwHXeFJrn2Q9uaAXaPd2A2N9BwY5vwcf76GBK376jiz4vCp7ZOtV9JBwHH0tsiOzpx2avfpKnbNhVPmj3qJJtFqh-0nQicXyFNbFI9dzL8FXdRFKkhhecZqfPf6jdrW3iQeTrhhek1etDThiyB6-zLhb8B9QlFJHO5t5klz3-sXDhqzP_zKFtcBWefc9_e1-Dc2wOOuAQbTf3UYsEqY2g15bOT0eUQTKpFl-jLR9E_EmjOrg9DgRLe6q9ergGWMk_xQhFn6MtJzpjhogTuk1Zqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcWcqFC4VzI92ddncim5WFIgi3i_L9oZcU_x39KN1klgdSPP9CePG9NpCi9imYn63HePciSzx6x8GeNGnj5VZ-XeXeFAM-557EEJykmd0-UiYfbu1TeRLN9oWiN7Thq-csxu8zXSYePrHzPPKU7bNkJVVKM4tSzoRGW8r4FxJXkN-CJdFtnXO1DZHfjaRjAdkYUUkFsePUcw1Ln78EQm1fz49Anuyl3wSc-FyquTBzDAkGK6svW_BpgFP33WE3n2nkbjZbW3B2jKpzuJ-phcLV2-xpH243O2mSP_nPZqRunkXkT6QFrelgr8s_vt0LYAS8ArS5Nw8oAX8W7tzpLzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLuCorxu15r3wBGvwbBesX1Rz3XmsSIuRo7CAbrqBH4FN2ir5k20CVqYnSyFxp6sjnmWeaFXB_MkNTxEOsk16A1F8QKTeTJN2AfrMb988BvYy5JwTnZefKF-SIWP1QPuGqYJ0v-dYLPslv89pQ4vnWlIf_gMqwIntrXaux5y5uBW8CJNLNEEpEEbqihtC2Gb7QJavvavuVumI11H-DW-lawo7UiLIapU-YU8ERZMo1zMYN3usNQCivuJJGFrMkw7TO1BNxgV59I-s_u2xWrxPyTsahQlN09NcqYaZX0erZMhxOudC8kIqPoj4G0yXYkTM2rJje80i0AZZqkn4d9e_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=OVkbBHBeIAhGGFPAVfQrhpfY_iX4ruDyRaUIkzUKqpSEVev-nCzrSzguuGtiZ-FLUPzVDjJacWx0HTTrOkGeGhwOXXl7wpta2JPbtKs8sqiX9OvtgVtv9TlEN0oLU87iIcSuLSAQOH9CujtW7LhtMCPdcdhykd2PmslVUa76s2F9M2CJQibVFuoqrFBqiDmFxXxpeWBVGkhacgKYQBM8E954qBtUuKtBsl7mYVaATV6KAxLhoerO50fDfEXAoMnrkSllCjeaXgZHn5c8pR8UkE70PSGlcQML4zuQA-HM2TL-YpL9_teNGxTUT0kRclPQBkTpnT-IcOgk-v3R9Yimeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=OVkbBHBeIAhGGFPAVfQrhpfY_iX4ruDyRaUIkzUKqpSEVev-nCzrSzguuGtiZ-FLUPzVDjJacWx0HTTrOkGeGhwOXXl7wpta2JPbtKs8sqiX9OvtgVtv9TlEN0oLU87iIcSuLSAQOH9CujtW7LhtMCPdcdhykd2PmslVUa76s2F9M2CJQibVFuoqrFBqiDmFxXxpeWBVGkhacgKYQBM8E954qBtUuKtBsl7mYVaATV6KAxLhoerO50fDfEXAoMnrkSllCjeaXgZHn5c8pR8UkE70PSGlcQML4zuQA-HM2TL-YpL9_teNGxTUT0kRclPQBkTpnT-IcOgk-v3R9Yimeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=aSJb34sLmYfu1Fk4cot8r5nTE6gBTT7jYmyNWLR45pmN0zPXAoBeqvnXhZsJjn5Fk9EFFudETPfSwTlLAdF89mnlAGkVXzrRDybMRwq8kc54mVjMETgS4Ux318IucP__AdkR_znViTL7SR5ZchsJfZECdzi-8FRGWfXyGcT5_YFY4QTw97X5x4rjJsjqNVNW2ibU2yzRI__tZX3rBOK2lLi68YRjQDYDjhrEoDLMnzun_a9PkqcjfJJ1ENiXhhHF_qPeHHfhg6vh0WoiqCOmY1GoA9D8-Lg2FdcF1oHA16HDKtQ9HlVK-0xkQ2qofKxYYXiJHNHtZhzNiX4NfyNzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=aSJb34sLmYfu1Fk4cot8r5nTE6gBTT7jYmyNWLR45pmN0zPXAoBeqvnXhZsJjn5Fk9EFFudETPfSwTlLAdF89mnlAGkVXzrRDybMRwq8kc54mVjMETgS4Ux318IucP__AdkR_znViTL7SR5ZchsJfZECdzi-8FRGWfXyGcT5_YFY4QTw97X5x4rjJsjqNVNW2ibU2yzRI__tZX3rBOK2lLi68YRjQDYDjhrEoDLMnzun_a9PkqcjfJJ1ENiXhhHF_qPeHHfhg6vh0WoiqCOmY1GoA9D8-Lg2FdcF1oHA16HDKtQ9HlVK-0xkQ2qofKxYYXiJHNHtZhzNiX4NfyNzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PII1mx7KOHHOPofIWFq23ypq5xyy_ekKhez40fDb5i36TNy2ku_AgcJRGZI-iCCCbWfLxKHvikFahK4Vkxva9KV_lYUDZ34xbeAuRT8uGETf5cH-AI3LosXTmelSGQOIxVVC27HkaKH83CLFfh-MUT7JiTnL0-jRhIp0YVfnkj90WXKrMuDrOVSpPTY1d8Neox_MhhdOrA84OVHIg9W4AgchKorkBi1mR7XLS4MF_jx4Nd-1z4nI1YPbv7bhLZ8IWyFBefH-0tRFww9-TYJjNrndHN3rAXvqRWomYVT4ab5eN5KToHejwzrfOnbwKoa-RvieZBf0tzJ8U1iNfRKMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTOomS4LoXyFN1h2BNAOZjBleZO6X_mN2f-XnGC_1vCX6brUyddjcJ-Yx1KE64GkQ9EZYmunIbwF0uX8OQEYI0F-YTV33w8e_8NwXP90vf1lkqIUyHlsschUROEs0b6PD5d57GGec4kC1JV5KEjabPYDLashTpAujuzhRnfFyOnNCcU2oyvcv3A0V_RwOCMyh-ndjsmXIWRkszhaBanMO8qEmfkw3R2ZZxrrMpyijJtRO-kIqTLN9-3t8lBNDyZNKoeXRi3kHvP0zd7FMVcRMqNx1XQ65UKbYcij-S7YToSl1uyUkwR7SRkF3qFZVVKU8XhPKnGJFtPwChkraC0fLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBSdwCEFx8VsPM4Xs8gltlFC1iZ3llgXZwdarzg1vd83sBXEtc-xq-XlDkMoUw5IdXf-c7rWJnITmrXBhi0LtM02Eu5JoP0T5yQOBLggSkCF3YJXJ06AGXFU-j5f_Ud6UdOvAG3WHnO82jQXKdif2YMQnIqE3QkluIzvlBYu6C9ipfmximQDX5uk_N_1OL6RngY43mQS3c2J077t5rE1WyG1IxzQC6Lq_aUsq_TVFJYFWWCmzzR60T50OJgN6F6RBhebg0i5Gs0TbmTm8unxXKe8HkfqerwoWGVB51c38aB6Y7AZWyi9rYplDd8ssEpguSUorJKMRSqMrGWF3KQV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLFg3TJ04NB2Ni4WwHg-Q30DzOu4E58YGBh41FgSNC3ILgbNRgiFwwE_0xPKvI2jVgtP3SLFSIA7zG4qV-aPYP9q20PsbP7HuftxGhxcWzNHSYmsgI0ydzGe_Y3-SnCUe_Tsara_IrEy0b7mCbUsVznXVyuLeVLSOAmxK-yhryYxQk46PPw88M26B54zVQyeilYKRi8VO87m2NOWXhGP-JZGZuaUi8fTdFI-v80xAzgNi_Vt4EI7nomVGkTuGZFyKJ43HA5stmgAQKsm6Dg5EI-ijfQdCX6idtaEOZTUJ6aAFVetFGT85JF2DvL7rppnq72-unrajxqlGo6mLi4Oow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJCfYm1sYTatMhosXQbx25v0EknSFvG2iTFP6XeqIOx5wkk55hBqdvpOY9XmlJI7iGxSYa4rai_ArDST6uJMhBpoMStodeQoV6UHPgksraoOc5lR8BJ0OyOumiSGXGmHIIYR4-8X-4Lh2sFw0Q0NAWIusmz5HeHuINb8OGlyrsg9r0HxbA6QjYioecNh8oQw__VNFRiDomWZBs1pgtRJ73joVWubzhjG85opu9qAkyvDNoLz6JuvjOeqjDrBZ5y0wpJarkQG66Be4IXxGECkpRUCN38JpDK1SNyCBfLyv4ofv9PP8oZ0buyQBVSfhlNuHTETehEz2jn5fQwleZ_tew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4wrCYS3s8a69lsKGruOnzNrxbuPPe7eBh_n0db8MoSLA7QxLLB_xnnYoD21PKpmtAWNoLhtYV_yMpMrgssLe2BtJwAEBD8WqCJg3M2JzZFhFEI9VOQtJM1JUd8tKvQT6QB3vqol01MYb_OPiljtXzrYRlqjEbS6u78Hx7mxLUDcSwsxhFq9KuqulFyens4o83A8YZ4SBw0LyGxnuUbcGMPi6mNjhWy17wo4iQVlXXbbAk7vXaI2NdeIURKJJGT1oQVRqyoPVZkAV_gwHtnpqIYa89o4dPwgPolCt9QBnWSLRZ2AbAurm4lQhP4S0KVmfiGLfCTbKxqQpHG0u_oi8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECBV7Sn_zTWUcFyNrUY08sUJoN4hViqewuamd3FMDDjNz5IkBN48VarY9ObLzRGKXGnjRsGtIxhAJXFofC59ptUfmosroxACcKrEI4Ua51xwBihuLLXq1xm5sBan4nevtLsUsIGHnTquv_Ij7-JiP-Fl-EmltWOiTYxknPbG-BHjOF3-Y39OFEI_AxiUdZ5NFhONgEN6ZdbZCY7ay8NWhDlJEdmW3iIzNX0PCL1T4Px_Fm2gByD0IphieEbABlAVSzwc8mVCcHnwXFKXdSjSBykkCWhqZMYZ-Gn0Y4mLpAWWvn5o4xSh-45w4nZNT3ZcH_U2Ol93LB-pUGomab8Y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJOHsBwgQU7uhh9_uRIv9B1YEf8UBN2g5y8wk9RmAOtTqq-E9pWVKw5Kp4MjUrk43apenMoGv5plimUINjdn0IoYZPiE2FsY7CMO1w9AhFlEC4aly5ABrzgxF_3zc_yZYC8o2Mpe2mpYVVenamswazEpHF-i-UyNicxihYXZodgXpjhIy7pYaOA8zyHHjGQKyQpqECXpjwyjJoyA7I4MAQPFWgi4YMixWxNqsg-Ywv3i_YFuUXGcRf1sMm5LYg_GXn7QjWU6fc5Buv5wAIHVrUTCyOso2MXX0iYPGhdPGUrKpq4Zepv5BNWcvsMMRXVEgw2NYdvoIkj2jMzdp2ENEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8M8TssMuhd1dMOLhni5kOqlaNSrgurCDR2tpaICNc69Ndpkc5K0qdTJ63N_hGIOrAmpcOGL_wLB66H7jhr3FoTy0YzLcRjddndxxfVZ1IxrIG7-4pLvlt1IVCZabhOL2VpZs8wnMlyrIdhsTdwG3lt_jR_BERpnFgn4NXleNgZhTYYf7qKmMfemrJhl810zzpykvgOLDhgaWz9l_J_DQKPzpjkDLIEqBk2qvijtW87jc8_We0_akNhy1Xx2Ys7Y-qGcrr3b_1fQtiIIlTk6Ygm1MDsiRKDOZjGjDZjzV1Xv8DJUpRtTHoMvW0ftKVsGZ8HYRFYQm_7p8wwGWlUqcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6x2sgkrZZfw3UP4Mph27YoYaw3EnH-6u--xJwrExqCadBwebJBo6GtJ1d0EzU2jwl7RX4dUSM_VP31rofiKxoXcZecPedCuyO4aDa9TlMVly-p5iOHNqN0OfwXVWQfsrXeoiNdGUghBHFXIdUCgLL73u30GW5W8sXxlyaTgxfTV11FmCQclwqrpxhZ5X7SUFjy9MDZoTSF0_Wp9BNiRyzFkGu7hQRkIyh22u9aTTvi7mj9aDLh81LbdXI284J42ZuTW2nh8GJ0C-FotLjnGJQtLzT9Ra2wcxS32UYaD0hfAcgalvbvlFphFuAdOmViUgvfLo78PGzb6gbE6Fvv7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpbX48JYIlgbHueTUs_iSuHB2Gg153jh5dtHg1jSpr9LFqWLvONypga4I1BSdyV1NrMUuy4bfT7MwNiTgA-DkT3-WZTUBnK-j1JWdOwDVuJ5OQfdgwQx-CWy5yRR9CNUN_1Wvs9MD91N20I6gq-K20vk3XrM_aOUCRs2iGqVR5OoiFsngdTjwzVrmZ4WqC0qO0_W93ZbjDcc2fMHz0vh0uggq_iP-jDPLbA_lC_2yndYrChzCkWgSgMO6YIGDWcNiwGCKrBGdGTbwJ7lR6jmEqL2ga_F9MZ33k6I7zyRsgb7m2P3nDdW-CTu_MQMJ92QI2mmqRkofJDYMpgTCvpTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=aN0sWxq6c_bIbVvuRWoONsaPTxNi3-Xdj-KcX6Lt6tvFUFlFsfG2WE0NivHT8BQQg57RXJbt0GKWfnrdkx-45xiJ-yWIBksyxGAPpkg2WqdTSxRz7LANhcP8Vvz3eyFMg1-D727kJUtJ3Ne-rkCYrujg8PzGvFnLL5ndU10ku3wFr81jy24sGHMYJ0qZCRiVPyCr9uM6k6fpGYMsTIcXpI_3Q74_vURmTN3mD7wRvVshiE2psCj7vvAD0ImOe4qAGj-j7S1LjlLNy40YHS8A-ZBoMzQwjhiBbLMD8jGpWrLe6TDJsjYn7UJqKhB_THir6TdBCA_bVUYuDFP_iTlDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=aN0sWxq6c_bIbVvuRWoONsaPTxNi3-Xdj-KcX6Lt6tvFUFlFsfG2WE0NivHT8BQQg57RXJbt0GKWfnrdkx-45xiJ-yWIBksyxGAPpkg2WqdTSxRz7LANhcP8Vvz3eyFMg1-D727kJUtJ3Ne-rkCYrujg8PzGvFnLL5ndU10ku3wFr81jy24sGHMYJ0qZCRiVPyCr9uM6k6fpGYMsTIcXpI_3Q74_vURmTN3mD7wRvVshiE2psCj7vvAD0ImOe4qAGj-j7S1LjlLNy40YHS8A-ZBoMzQwjhiBbLMD8jGpWrLe6TDJsjYn7UJqKhB_THir6TdBCA_bVUYuDFP_iTlDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opSr7acuUAv5m6Vsp9I7xXANDO21o7OYy0VVrETyVsHt8RmDIfnDF3Jg0hAPoE_cowmnOD_Qa5kxZZQnUASr2jHySOnq6r9yyTgkeTz3z4lvQpxsJwmZAT1h26cze9w0k8ms2DjU-vcm1QyJUPgagm1CubhR8GMQ81XYtl90-mRfH3y5GNFr-0MdkPUkuPDHD9Rdo2I5dOe1QZI5cyw3U6PHcwzTBTVBZjd0t27EJ1_nZwrGSN5BOKkfoJeafK41ZXgjnEIzwAUTn15dyw7CDcmlQ9kmCitW21KPi7ajORCZ2qdZMokn0swCR47jbNAivvOk6H4XGT927wVQXNM68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=BWRHcYN2-q5vy0iuzichI1VtfHXhwTjcxk-lhUWKWNJ6w4-xT10DtWQkOonH86RgfqMb-725RM4cgIKU72fMi-wz_BBm68t3wBNxVLOYX7qfIu6a2zT40jMr6ReJUJOZGeWDrDAZ-c9h96saCGK1-nM-cUtXGuDTpPuRAS5hjDBmva5Sogs4jlOrxZyT5wkV2aDKkyMEyUvL1WpANY5SyR_efflIOBxdt96mbpwQs3IFS8SYJRpHciZTQ5fdfKUAZBQzyU8GFDk-CfX8MeeBOlgPcIZj49uQ3WmiR0pFeRf6VT0sD3pPk-a0c5hxslFSU5yPxJcDdkntMqsEsBBvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=BWRHcYN2-q5vy0iuzichI1VtfHXhwTjcxk-lhUWKWNJ6w4-xT10DtWQkOonH86RgfqMb-725RM4cgIKU72fMi-wz_BBm68t3wBNxVLOYX7qfIu6a2zT40jMr6ReJUJOZGeWDrDAZ-c9h96saCGK1-nM-cUtXGuDTpPuRAS5hjDBmva5Sogs4jlOrxZyT5wkV2aDKkyMEyUvL1WpANY5SyR_efflIOBxdt96mbpwQs3IFS8SYJRpHciZTQ5fdfKUAZBQzyU8GFDk-CfX8MeeBOlgPcIZj49uQ3WmiR0pFeRf6VT0sD3pPk-a0c5hxslFSU5yPxJcDdkntMqsEsBBvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Xyk2BJt5BQ0KaWfjC6RhlT-F9TLOJGDK7prW0UGzuapVidA9zC5H3knjZB4D_5u5nmTuTHUq9Z9qnLduj4746LyvqEu7dAMRynwZXEKATDQG423OZhS5QcXLDiDr1TPPwSuS8l7UNnmyORzGtT-Hqao-6-z8G2n2IQ4XMb7wsBJAEd2pDZRYqKkS7Vcgk_eTet-cpCrkW3hIH0vape8R2ItxEq1kLzehAHvOrxt7ZZU9KmipV5N2BBnLlm7N4TjfvJS82_rF6k_tU88bUgW8N4G_RB0oaKBkDVqF7ovGluzb6RwU_4Cw0TrlLqXoYX7PXMY3WH74FYkskS1A67UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIkGcETio4sGEMSfenbXFKWlY4btxQy7GilkaCjTyuXppEPJP7JqGwZ-u0aYcieeVND4Xj-FPyNbSTKBA4lSPiieR7ABO6Qmi5dbSGK4-EwoYWaz1mzpg7vAY0yCWn3qXpilBueVo17zxE5b2XvVIujLRdMvPY8u_JGJjlNsIkxBbcLentsSnyI_q01gdTILt7ZDrSI0WmDT35nn_S__hnBkqfhAuK1FVPq4WyhS4fyjUDI0UqS6v2tZYxtIjHtFhv1xFVEJhZOT6jf3qVX8FWMIr_irVDL9yIp44vr_VutST0w8fKcUcTjPXhyCdM-m3wFdUFH3gm4UGXiyjHDUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW11sZzYw9T15BgwycfX0QmQQ5NDxsFkXgF3E6Ah6qE9gVdYeAnjh7a3t-63CXVgwIwJQqlxA0beJEWBIFh7CRGg9Ng3Zao3s0Dz72Hkf-pZSkHwUmEUgtzv_U9W_vO5Tjh17sslAj5C4vj2sYAV5ey-4Ag81Yub_00zAxqLIcb2s4g3f6V2UkkCidkriluJB6IqHEgQzLDMNONd3ZfgqBBjgatLYhpJHDOIZxZIDO2DTlkKgi3OqqTmFukh9ltM6CEjtiLjbgorROjhfA16xs0r1GuIi0Xcn88Xqn8AO6alXf198M38jDLDaapPVTNDHLkHUDjOCnXNmXdz9GFt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOSAEpIpxWzifCYRG81esqNRG_0esFW4ag6bRppQYwo5gObXkLCRnpQ2bnRPaYOriL6E3M6eNWK76acDJC7eEb80kOcxcXEb5ZVAovYk8A4xOrCQTx7GqnM3ZlWpKPlpx82KSGNVkT1kaBaGs99LGYKCoGADpYIVVLFnP4wzHWK15ZDONYClJ5nxpr2bVXyJ3cexGBqQcwmclHXJc2k8O_3waR5U8wyJ7dPYzA0HDYJFolYB55JK3vIRONUawYFLPA6mPVcdL9RG0af4Y0kqNV7OsMkNyKqzT7AQyr0f6jKrFR2mnIS32oNcR2FKic8f3_xGxyvJZXoQKje5U_iPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2lr8Dry-ObOuzLr48J7aI5hWtPd5wu0bXWovCXgRlf7QBaBv2Assgwd3vuECf9SXeEsfnGhnBea-Jkj0BtVoZbUM_vCsj5Id0jm_ETeBzuxjivAKg0SQlHg2D1K4A71c4pP8bhDr4ULhCopDG3Dl6qmS-lj-t_aX6OPjJwEipJlmYBTWrULqWT1nHt7dx00u-cvNtw-2xXc5dAbM1e5MDlrx2hEvhv-QpnSetrg-Yg0QuP482tB4zey3x5Mf2xc3tfeovaaL5hK-ngDWUta17wDVK3ZLEwWSIoX-9qZyw80dIjCbfUONhblWuut9zQQ2BBnL74SDhUNmGBGsgHlag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQENMsWoTWkXt9BVuiB5e_injmvaHCTnAj3yo_DQKHZRuIdplWA69ods8CcAazPA9cEFTHy4Tstk34dSlJlF5UNHEFyvN2oXnNocnCuS1rWegIiYAIVExyH9NRvQRV8Gy5XOrrXsDuVK7GVQ99aNzFfpkL_Wha20kofeW_7tX-cLcVfHcbsnABXkN5Gi8F3SUiPgbp9oPRzqarFkyXKsk2vTBIiG1ddkdRQ-VQKuDSkHmewtOs3JFUQ3ojcR1bIsWWYkBcROOxfS5S-pWZCNYGh5vKra9Ij6o2zeaW_PYMDKkyZs5HFW99Jrsp8nFLckkRCbbkrUcOKdBKIxBytHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXN4IpnyKJMts34aS5ax2C0MwED6cKTPUmezuAtl1GpkbXD_KbMGbMeirpJwqPR0duekdSub1YYrCdTFzK89Bkuy35qyISPJUEKtTHWzkv6pavPPpbDywy6rSaywpVR4uEdJ6BH9DaQssJrBUR99pm3mdvBBvT2fNMBwXsx9zdwIcm9phgrdJpkPAOTKV6VUz8yuM06MXFWyYKmm5SR4v5R4klOcHzRvKQLX9tKuQK-sDXZNCFbs9CpM5r-og9R6HkBBtReRHSNRKRk1Xz8jNOhgJETF_1tJqWyi2bMiHLQYjOIj9YSIi7tbIqv0Yh_76_CLv-5XFb8-HkL-xHYAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGriHSJ0ziFJFdWGR0dzHF5hZTXx9HyymmcebAvlf8gkscOx1n2DSK61rZaGSMpwGbCfMYFH1BlpBqwuAonlfBi2R8JpzPVY7YZg71I1staYcMvywoJGBhQ9ArfHIyY4EGmhrcwh5OnVMvFbo_JINeybyxAVF9gzt5P-vwCYiN48ecjsveFS8RBzRwg1yONq6OOQmvOhsyARxbeZFc3NOcVSpdJtOr7TNJRYjcivR9xDe-sCKvhO8xy44IYxuBcRNVYZLsGSZY6iQx4hz6UfNzxEYRQUnap94OeRr3dDqE8-WgYSoxaU-6Os3Gqum9N5vLsWHOnQmhleMykdgGvwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm7jJBY6Cnb_3Nai_PNwvlnNyccTuwYTPzad2YsFYtEWCbMzcUA6oecDSvkl5l21gHQWMaHQ4_Ifc7YNaqGH1tDKnIwC1QzWfdp9nDj3eEcRs110Zbw37w9dK95S0746b7c6gLlPnf8pjVzFvL7-bOKaAYodn8kaOdzOgS-lWT9uFkoElP1GIAeXKuZIpMLEvKOIRYC_LgrtvvizvtMYMBkiVEAExAtigaqYFrNKiDVCv9Wr2DCJuRdm1UHITNP0BiTzcIoXLaP_L1kf5V6EHzIwQizT2VIhUqA16OkdwlHbzQLYxamwU9t19ubApNJCcEUu4cjj1MV7RdbVexAplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCswUuDS5B1unq2V2XmsIsUtZffw6kc5poCsO4rQB2X5l9AKEEQD6JghXOqZvCfL5fvdEhpRAxjVxJsg6OgBmntcCn3u6F9CwpxRwwA_o4BGpwkzDRr5T1IARQ3bcGFn7Y9Fu9lh3sago87knKrhvzL6sSIVwfYDivpPMTftZU3uzVwtvdlzf5KPetwV_PD1Y1YkNxuBrjjMCVeXFssREA1hVI2hu5aQs9-qVyycBDmC1EO80ttRquMCkkTcErPUIWyiHRtXfpMj1MJlKR_T3ZL9a3xjfDre9h4mXkTMxvGmcnMqt6EWLwGEX2Fqha1tJRI733wITYAfwSlHbBg8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnWJM8tf67aceY4ofWvepnZ5pV7JD6NXH5_h1tvpc0V6xYSLGfauGJvtPfOfVLJIPf8AEQRCxwD_FAvVk5JuOvYJprmZIbUc52KKSi2bJqgwGj5S7X75RYTdDSY2Bjuh9cjQZk1atAsd_7VJ7M9GbdxOpkQsgk2puxvyJK2DNTxJoYpqpCaMTXPOVDCmwDQyxLWqpXBAZFg0pau6vXVspvftR4BevoQ53T6U98yM2SGZlbwcY0nOClTq1IGoKx7R3T4zJ-v4oUofVOV1Zcz7fJwzMP_udWT3yr5i8JnAdmOR8GuzXsDBuv4cCG8WIfLeefH1WGRyAdIZG89zb7a4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=gDbj3ucCRCVEEmGDlUAJVVc4f0ZXqJjn1ajhfBKkyGuc1tJlk7sqrJYq0_uE93OVHGAiT_GaaAMagj1xX7qIMCUS8aOC8RN2XGyaF6SZZ2ZZkEBqErCVDYPpEsateiEdnG7FzYhq_YHPXQ_601cg4Pdl3-dOUl7EoUhDUcEw9Y1fT9paJJNg3SZp3kvMmnANuqAG5sMuzxQghRXSsCWxu1hcYzK6wrbkrEXKBUnyb81y4jGk69GyR7lzNA1Dd9MOg1ZMowgvJM3XekAzwDCQtxrtTpwHmsQe2qu179GPu3-sDji6dINA3wUJYb7Pbp4LimrQSTvsmHnDsaHFKU_CrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=gDbj3ucCRCVEEmGDlUAJVVc4f0ZXqJjn1ajhfBKkyGuc1tJlk7sqrJYq0_uE93OVHGAiT_GaaAMagj1xX7qIMCUS8aOC8RN2XGyaF6SZZ2ZZkEBqErCVDYPpEsateiEdnG7FzYhq_YHPXQ_601cg4Pdl3-dOUl7EoUhDUcEw9Y1fT9paJJNg3SZp3kvMmnANuqAG5sMuzxQghRXSsCWxu1hcYzK6wrbkrEXKBUnyb81y4jGk69GyR7lzNA1Dd9MOg1ZMowgvJM3XekAzwDCQtxrtTpwHmsQe2qu179GPu3-sDji6dINA3wUJYb7Pbp4LimrQSTvsmHnDsaHFKU_CrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkyZNnXsI0HHM-RtuK1eMwIn46Dbgp1VX0ZwffBLFTgtLzd1iiiTsHflBMcKRf4h7FEOUdgXc5qlTn5cgM1zRG6RImhj9uXrj_Dt-B2qAHB-4LWrYGplppNLDEjP4WimlCQt5pcLZ8VVnOa2CgREy3NrC5RoN3CmUvd6JiTbNHJhB7OFoW0lVCzqrJlOWG53iovoIGy-CkUqSpig5UGqxjobzADD-Yv3mHBMqlhk1eC3D6JHro6LMu09ByN0OZlKcMoSuvo26158QMhvAhqJ8b85fZHvxbl0OLtN4FrCJMRubLNsI3klgds9g-zhtaPwvCtCO47dXbdHfVYVPAD2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=tR5Wbdho3pLBEIyq8k17btD1H5tC92LTcUdSitXVZrqZfFroH1cGrFLgfczi5UIpzRA_X8dpwNeNx7TG9Bk0Ms3Jnp9HU6866pB5zEOf5nCjHl5OTpIlKjgbVsVKQPXbZBMfXrCAGuXwQhXOdlFMV6RX08WWQdkFpB5268jLOC-TO8UK0wmHO4XTp59-gfujFoEUXa1IE5kfvMODvRp9GLAKE8IYrMHkz91jMZw134v3S-8AfsSALvD8c4wszesRI64t646iLCj7Ity_vxOSTn9n3EB1VM4FvybjebSQx5FaX43kVaHE0kUaPM63oykACfHvk0V0Z-VUsLbw35pybg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=tR5Wbdho3pLBEIyq8k17btD1H5tC92LTcUdSitXVZrqZfFroH1cGrFLgfczi5UIpzRA_X8dpwNeNx7TG9Bk0Ms3Jnp9HU6866pB5zEOf5nCjHl5OTpIlKjgbVsVKQPXbZBMfXrCAGuXwQhXOdlFMV6RX08WWQdkFpB5268jLOC-TO8UK0wmHO4XTp59-gfujFoEUXa1IE5kfvMODvRp9GLAKE8IYrMHkz91jMZw134v3S-8AfsSALvD8c4wszesRI64t646iLCj7Ity_vxOSTn9n3EB1VM4FvybjebSQx5FaX43kVaHE0kUaPM63oykACfHvk0V0Z-VUsLbw35pybg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=pULdWk7WxQHnarOYC8C05nuZ9vTL1Q-9GSd1KuqrTCDpWcHEM0UttAJD10U29MgiACQJ1FinXVTfGsiqxsgX0pC7_v948TUOueJf9MM6xFqb0z4V90HbCbDrGaWg86M9N_gZlvvQdsbfoH7km1-Kv7Ka1tNMLYzzYc9LYAChZWO3_4hQklH3qrv_DsmUeyu9pUkOfpeTbFeBBTmIzlC0X_i6UWErRbw6cUSNkrELvN_FDadtnDHuE_ZRWhzZpGpggFvBLLVPVXTlYgZODXqfaqF6sw73HxHiZqrvEk0j8ejOwoN68aZmJhqKdkSIMDqjo9nxJsReIOe9nc3PP5SM88Aga6Rj71WgS3PSFZB9lR9Q5-3cP0vC_-Fy7qo_-Zsv_zt3X2jKaUWPgt-dAVujpV3kP00lpC33V_X95A0uTIMflm8ohfifjfrW1t9jdQIKO2io1M0-epBlGIIcGICJnjiU2-Sqoim_e75pUJXkqErPzPPZpMxmZB8R6cKD8C2Ku2YovlBIGBCb8K4yHwMVJVqAxmvFwJ--uSqDfDTQ1INzFuoVVRD2o9Alzcvxq7gFxzJDE6xskQVRnw9W-tAt_cymmscqLqLEdNvOFe6nLL_sK-zF7us5kSPlf71hoyMEyjQM7L89Ddm3K6KH8y9gOtCPG-l_gsCi8YMmGWtwiKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=pULdWk7WxQHnarOYC8C05nuZ9vTL1Q-9GSd1KuqrTCDpWcHEM0UttAJD10U29MgiACQJ1FinXVTfGsiqxsgX0pC7_v948TUOueJf9MM6xFqb0z4V90HbCbDrGaWg86M9N_gZlvvQdsbfoH7km1-Kv7Ka1tNMLYzzYc9LYAChZWO3_4hQklH3qrv_DsmUeyu9pUkOfpeTbFeBBTmIzlC0X_i6UWErRbw6cUSNkrELvN_FDadtnDHuE_ZRWhzZpGpggFvBLLVPVXTlYgZODXqfaqF6sw73HxHiZqrvEk0j8ejOwoN68aZmJhqKdkSIMDqjo9nxJsReIOe9nc3PP5SM88Aga6Rj71WgS3PSFZB9lR9Q5-3cP0vC_-Fy7qo_-Zsv_zt3X2jKaUWPgt-dAVujpV3kP00lpC33V_X95A0uTIMflm8ohfifjfrW1t9jdQIKO2io1M0-epBlGIIcGICJnjiU2-Sqoim_e75pUJXkqErPzPPZpMxmZB8R6cKD8C2Ku2YovlBIGBCb8K4yHwMVJVqAxmvFwJ--uSqDfDTQ1INzFuoVVRD2o9Alzcvxq7gFxzJDE6xskQVRnw9W-tAt_cymmscqLqLEdNvOFe6nLL_sK-zF7us5kSPlf71hoyMEyjQM7L89Ddm3K6KH8y9gOtCPG-l_gsCi8YMmGWtwiKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=DfGtBR8CuKai2ETyJMmnN6WUU0y5vmVev7_vHJl_GLh4gaf6Dt2xNJF0BmnWr4MwDiLnv-d6-2yGRyqBJr6rxRXr0RHfr_tGCQ5hXJY4JLWXPWSzcjilo1JVmLAWcX67YhJKI3jPg8Knr8SpqJhjJE0JnmXUhG0xjZC2BJjec2n8sI6L7k-GFiBWrejxz0TZAJC9bUuifEtcnz8U9k_RAmmoJcX-BXlFu4i0CVPVA0r2mbP4wONLdPqdPJgh05ETsY3U7MO6C72iLqUBOV9lyGSxLIcCYRTe_8RwX2ka6eRrBDYKrkH9hpuIQNsOC2PAqlzdx5Amnp3w1i3TIRNtrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=DfGtBR8CuKai2ETyJMmnN6WUU0y5vmVev7_vHJl_GLh4gaf6Dt2xNJF0BmnWr4MwDiLnv-d6-2yGRyqBJr6rxRXr0RHfr_tGCQ5hXJY4JLWXPWSzcjilo1JVmLAWcX67YhJKI3jPg8Knr8SpqJhjJE0JnmXUhG0xjZC2BJjec2n8sI6L7k-GFiBWrejxz0TZAJC9bUuifEtcnz8U9k_RAmmoJcX-BXlFu4i0CVPVA0r2mbP4wONLdPqdPJgh05ETsY3U7MO6C72iLqUBOV9lyGSxLIcCYRTe_8RwX2ka6eRrBDYKrkH9hpuIQNsOC2PAqlzdx5Amnp3w1i3TIRNtrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=T_Vw2UlOrVetJ69OCJfN_V91pznvWQkYBiFXnDJVZ3HJTpjoHBiqYxOJcq60C378whRJiH-RX9jSHMc8TVB02vNKrnkvPVLKvTvXf62q0XmopxNotxgeNthrR498VZ44P69Sz7np7z3tEPLYCOJeFuxCNIKGHKwCKNAH2wMSSsp1gOoAuwCa3gM9cqcsdk8hjYFVtIRPBntl1Wl_rcXhy0lZWgisJAPkjIddLbwpUJt-atVroJygojLO29HQw2eOXWDnuArYdVmsMDiJdsQQts_-Z_KASlv-obljdVr5RsIRn11oNLMsjLzyrlEGMkqxziA2M1BgDMpiR7U35G9FW1nrifExUsCCdL-dDkVvQfNapqZC-okS4iF38TWJA9fReY8rtfQeeBVFROytV2rwWZJj9UcBKYRbJ05sFcUjglJeakhjK1Iq43JU7gKnqD0_IiWkENQhkXJk_ByMTmnId1SmnbdGwkutWCDurTDplCqAsih6F8hJNOUMct2kwE55u3iGqfiVqUPL06m56XU1WmCcaN3PUPVkDUET52rU7OshT-WqzhbWqG5uza0QPogz9Kz-joyA_Cg6sSdSJdYJDfwWaa6zhf-luituMTGem4AvisKlqGlK3iwBLlIJXlQplaLurxQU5_AeUHjRhQP_UNB8DNQe4AxYJ3hHiFV95YU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=T_Vw2UlOrVetJ69OCJfN_V91pznvWQkYBiFXnDJVZ3HJTpjoHBiqYxOJcq60C378whRJiH-RX9jSHMc8TVB02vNKrnkvPVLKvTvXf62q0XmopxNotxgeNthrR498VZ44P69Sz7np7z3tEPLYCOJeFuxCNIKGHKwCKNAH2wMSSsp1gOoAuwCa3gM9cqcsdk8hjYFVtIRPBntl1Wl_rcXhy0lZWgisJAPkjIddLbwpUJt-atVroJygojLO29HQw2eOXWDnuArYdVmsMDiJdsQQts_-Z_KASlv-obljdVr5RsIRn11oNLMsjLzyrlEGMkqxziA2M1BgDMpiR7U35G9FW1nrifExUsCCdL-dDkVvQfNapqZC-okS4iF38TWJA9fReY8rtfQeeBVFROytV2rwWZJj9UcBKYRbJ05sFcUjglJeakhjK1Iq43JU7gKnqD0_IiWkENQhkXJk_ByMTmnId1SmnbdGwkutWCDurTDplCqAsih6F8hJNOUMct2kwE55u3iGqfiVqUPL06m56XU1WmCcaN3PUPVkDUET52rU7OshT-WqzhbWqG5uza0QPogz9Kz-joyA_Cg6sSdSJdYJDfwWaa6zhf-luituMTGem4AvisKlqGlK3iwBLlIJXlQplaLurxQU5_AeUHjRhQP_UNB8DNQe4AxYJ3hHiFV95YU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4JxBsbkhcaaF1XKdDlGl_IMUxtHRwqJ256Ykj3Rdy_o0RUdpK7IJ6nqTLQH7ONVLaZb5fNgxpqNf59z14X56SdWKZtMB3D-lReoV02F6FfaY7bWev6UK0lK5mT3rZa1xWwe3KzPWKQQypfENbnMlPr8-_kZOB8bO-5QVxYyak7rYfpDviamq9eAbXJ--Y4jUagWmLb8g4U9p62WwOVPgmiCCFgCt4oIIULcngKsEkMWEtXponbJnGlIfD4XIMpNT1DdX7FIv_sfooz5tlAZMV7Bx7IQb0nacbTsTEjvsju1WvlzzO-DxzYh3oJ1va28kOhU2SV1VvGJjkkTzoaWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=pA8Ju7Srl3uX2iNxTpxyBOfVmG0vJNTeey8-Ms_bgXz_dAQ5aqJRuPOHzWPfV722efPmqfIwy9H-0XHwqJqQi9jt3FuvQIj6Piemy-D_boqqykSM89Dp1NtUiVbNDFHILDo9aMRUsmW_REw6rGlWt0ctOhgvjliIGgjDsxm8oeNx6ecOMSImF3X0foy9W6PFcMRYjsiZMgTHTmf3GGDa7ee8zmKxC2O7X2vBlZIIhaOigfrwBd-ml1robB0LcfQKWhJDY8qxIXLETzroUH--l1jZ3nf9VTBoHuKBtisco5giVjSavqOwPa5TE93sJ5przRd5tYVsZCyzgvRN2EQsdzevH2k3PjyiCAUkUZP0e3IhkD2MMOuqQeGmGAqvaALUdusCjxo3L0Dlb0NjDzubX-eZkcXVmm256vFdn2lFNCI22ckWnAGmfyp9kixk9m16bbBoIAPbWfSWS1ttCKYUdhRzk1qBPVrKq-Uid_oj_bE8HVrAzI2VywBwds-AO5B21ZMc-c3WoZ_gDqz9vIAKxDHIEp52GEw6eLzN28raVkm4d2GpF8pTaVXBIIy41yhK8M7sAtS1Dbo1sMCO53Qlg9nSFcQXoXEeyCDT4gMBb1BC3LME7A1uw2gdQ4dTW4kbOCpIe8uWQ6HoZ92tSF_KJMjXfK7w7rSN8NihutucYRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=pA8Ju7Srl3uX2iNxTpxyBOfVmG0vJNTeey8-Ms_bgXz_dAQ5aqJRuPOHzWPfV722efPmqfIwy9H-0XHwqJqQi9jt3FuvQIj6Piemy-D_boqqykSM89Dp1NtUiVbNDFHILDo9aMRUsmW_REw6rGlWt0ctOhgvjliIGgjDsxm8oeNx6ecOMSImF3X0foy9W6PFcMRYjsiZMgTHTmf3GGDa7ee8zmKxC2O7X2vBlZIIhaOigfrwBd-ml1robB0LcfQKWhJDY8qxIXLETzroUH--l1jZ3nf9VTBoHuKBtisco5giVjSavqOwPa5TE93sJ5przRd5tYVsZCyzgvRN2EQsdzevH2k3PjyiCAUkUZP0e3IhkD2MMOuqQeGmGAqvaALUdusCjxo3L0Dlb0NjDzubX-eZkcXVmm256vFdn2lFNCI22ckWnAGmfyp9kixk9m16bbBoIAPbWfSWS1ttCKYUdhRzk1qBPVrKq-Uid_oj_bE8HVrAzI2VywBwds-AO5B21ZMc-c3WoZ_gDqz9vIAKxDHIEp52GEw6eLzN28raVkm4d2GpF8pTaVXBIIy41yhK8M7sAtS1Dbo1sMCO53Qlg9nSFcQXoXEeyCDT4gMBb1BC3LME7A1uw2gdQ4dTW4kbOCpIe8uWQ6HoZ92tSF_KJMjXfK7w7rSN8NihutucYRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUHBSgS6MjgdNxMqgs252DmNcZsLN2fCuO34i5q2W1AFn9REF4hqf1t-mokosEaOpYIjHqGaujaumN9hZyHtV1TJ7sbCldUP-fgCYxSY6auAtvK5eRk1l-JgAvnIBaIIPxcyh6EwwmodEtfrFlRr1qs25VC6cyMfpjOruB72ze3yarjv-S1wLq_Ji7iCP6uaZq3tQ6AOYaUfIiyYfEvDtoiMzszm5mFQ2NFK2uSsoMfsixNG_sVrOoPnhxKE9Cy5pRZvnJpXLxkDBoBRrqoBOlCExsHI-cXU6QEQMLGMyfEvIS0vt9ItQYYCM9Kjt6SgLRzbjPsHMrLAQ_L5CCWS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXR1vsYYwhEbyJzdv84z7TRYxtJztLIcgmakbVJNbD-H2HHxJHEFflva8CmqRKdwIKe25MOBIw0YtuRQ6Y-mqj0uiCtAYvtK5bN-lgALiXUpS5vY0EtgZvDeFEcyglcFtlNpR1UfmU_TtbrxHEvdoim5maIf3rwpdYkfvv13g-L0no2tXP8XfFYBMuidtMjSr5ot-KGVwmoKVehHJed4MRgRyPph2csmUo2LZZxqQeA0Kpxudsb5jVwmUFCyZpu0VTeErVBedKzd8SrpVFGN3RAoUZ8zmQkDZNvWVcnXnvj-RMAN5E53dbLG8ioYcSKfATehUgKD2-nOs6Nv50qMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucMuyy4iaVhSvX0w-6342GwvqLy1KONWsJQtWAIB9zWh1ZIglO_yxdsxFUxGDUxbt6aVPm72ALn3xsaOcGW3W0o4PfYP0UPKl6GPVGLRwcYsCzxrHsYR0kse6haWTmKCUaghnnLknIWJA9sqj1-mokZzNX2JfsgtTg_vWvp1APekLj9nEhMkggu5tY3pHXOil8y1mGfLIkCIZzxQ6PvFYGUzykb3tDWVLelyQnWC2fNx2myYCYul2xOA4QtaWtKaNey3m169tBqPlEA1UZJaObBWlzMSPBhoRal0OWdyUPEZCGAty2-C2eZXsSfLyfIps9MWCIepp-3aNbOP0fhSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iy1JueKlRqvEvG-9R7d5e7Sno3O6prm-NpZh-vfLF3GlDLC65H2FT4iCF3F9kf5NErEFFJV1fHm2jVrZjDh102FMac0kRUSbGR8dJGFYl9E-s8iVb7twmfzfQ12togYyH4wWXNhnqPxIeplbuJQWk5_xg9Ner3VaTr2nJtc72CySitDnrTQph9iPQN_P6uKS-a9h2vp8ToOtkd6wgQ0fma__TGwXKshGby7mrx9-TANWR8r6IcXIqLtPuoHVNwKwwr25Mk8EMo1QDEPbbdeuJiUncLCb4z8tE6oz1GEY9Tf0SgTRSAvDL5z_X9BT-FZUu7N-xKzH985PxvSHeF9G2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWHEJR6d_nIwkrJNjpESBSV6C5ipeN5PjaSrS5H4C5wSLbvNHLpOnM7NILnODfFgmCH7CDY0igK4Gjya2uFflwWTkIX6QvT4muu5LlJ7QgWoqJjSl2oZB9WpFbMVbkkhdZsToQggSyl4LlTDtWBhKYsiKR-c-GgsSpv73CxajrM6Ze14JmnCCTdYytE5QjKcgu7T2OFNRIUQAZH-Zr9hkK_G-weSOULV2zUzwVfClLopZPK0rvOBo83qcbjQUnOdLsRk-2uhajt7uwkSYvtLW1gyoLlyatueWggD8_2iibjTD9W2KZaHSprRAUvn4VAU9EZHRlK6YzF0xHj-Lda99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcrTkVknWlHYmvzdyFxHI9rXHFdKV0RxEgGn-cx4_Gg9dXxGbXY7NA1lBI6BINgHwRJiX4bPCwLjF-OYqXxBpcz3ypRF61Cp9HOpgf6iOCuoKyvjyXGyqxvltC--_OoLEP1vAgsaex3qs-kN-l-Y9Mo8mUBlEa9Fl0S5ch9JTJTHou2CbmUn_up85aVIK7d9sAo2zlzb-gZiyv-OTrlOntz9ZIH2pY55tvNZCv0kvZUpX8JG1S0AIdYk2D-oDUd7T4dBOL9Ot0Sjb2U24gxdmjWL9KpvEUXHrucPjZhI0fu7WUAh3BVI44DC4JeuexJpdhG_KHZSh5Ld-isvAFlgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsUknw-7dxzQ2b87sFI-7UxlRIlJQopf-pUZBbNVTKkbZbMvCYAQgj6MNncbr9xi3nVERl4DGKHt0e5uw_hhx328jY-IOqWOrrmavXskSGQGXDVkg859uf6dfvj0offDYhY5gb-C_kFIUKXNoDTdSoFHaZym8xraA0nTwedYwg5WG5wazas1oDshHO6Dqs4uaLNKdKgbWu-GsVUuQv1xNYkgVmD7tpSZTGwTkM27kerQ0vyyeqTCPoU1B-afwoH3NE0ls8dL82vWVhbC1IcER0yYF-UjNp_QCx2kWbuYRxb6QnaTm1WPiClxCv4diirYlNR7C_3jcFY6wY4gLeqSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU0RKnVpo1HERbZAj-IqI-mkX-NTVu5E7ITQ_MVTA_NIoftgQgNj79Q2YLR7Hr-SSL-vHS6N7xy2e7bCrxj7YBDvz0qnCLFs4jXSsMrGPze9yuuDhiWbZZHHKH_NzWn5xp2JtQr48bMEx0Ku6gZPCBLrBoqyq2POeStDHnUqQyeD8jx9GSmIf0mfgs0tolh3i1uhp-2bBK_eB1OdfF792x8QBT1Cscgi98862qx8k9kqunRCZq3DQ85l7gJsgyxH57TzfP5Vm-YTmKvo_ImkyT3IMlWOj_FiP5-yFeWwxUTLnyl8wanAvicDeNT5conKBXB0DGAZ3jqh2BAXftmOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkuE4Cr2b4xNME0r2aWjtGLa1eIOeOdg-sYCtn3kh2OBSshUX_iH674pS4rM61O4oQz_XE8JhbuEnOXHUWDXjOp6PIkB7-YIlck65_Fu05QfmZ-ygG86NahVk_3T2rcZy5YRj4neXPeIXDhfFyUwBo8m_mZEcVmDclJV4Ux7sq3pEnNTa8fOA0i5_-jixVyFymN1yuBD6c1O6oD21qlLBvQ3bl7cUpLCa7PT8niViLdTbdam7TcyznRRzsh_vOM-f6MtVn6kqYYTzE373QhiF_WyFQ1pC_5oHQ1A6o0EgzvLwhHnJc4KtoJuNt1eaBeZ8_cskBHCxNfx_dEibQ9Ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBk8ppAHUpj_4LriOOrw4ttBguV6rmc4M1d1Uq5SEN1bVfrl-fGky3IgRQKKz1DbdZMeD81Vbw5ysTOWxvAHEnxiXAr1MfKYJVT3NE110_WuP7y9oiFAImLmXiVFjruf5obTLQimLfd3pu-7d9uHq9b-5AgbqQqeeziDLKgDGYco5gc_MxevqOEN1WOMlDECpcQOdh5smGoVknA1V3RQcdTPr0O6iXXC0Q1-Q6Bkl4D_n2PWwvl1_R8kxOxtXXL5HNDlwu5JXvsa3nM8F3DjS1nwg5fGhDIeILRYqOpa4d8R9qBEud-6zOXjvq1IGhjViu-9F_-3KPR3hdjUklFe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJG0dM_Re4P7uCGKlzYlnOpeMEySvIvHdxmCUYyBO4Z0D_rSm5NYgkykWKNrnksVHm3GZ2PQ-VcRBy2gpqaPxTuImsYPZvdNXoJfmSlR5jRqbIUOimoXqYyIXJT4qIYOUV1tXfJjsHaFhOLp7PMKrQyK0c1qkYJmbtBII4Dd7s3xK9Quiq9wmGVl0dtoJWWMbsAu_yLKLrLvA6kMx6OULN06mwiSVlmLk4n3I9R-3TkhCxSXxrGF3cISUf3NJdOZKz8e6EJowJ98tgT98_nApxstwD4L6UmaEEmz1lgTZ2XOdfOX6sCZr6lxAOsASYs8yJtuWs1ZmfnBuAobW1ft1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9rNatRvqU-tpE_-GX1sHmp5LbV0Qf8iOfQk_UlmIPrcesbZh4BWtRbjfDwcjmvpnGwJP3YkD8Jeyn3zLRe2NnbI5XK5yfedTPbH8ueyig6T7Bzk5thiAk-_WUBXDKdKhcBcAI2CpySi7f4Gu64uBwjZnbhVqq7RQ_NJiolfJEqhrgQDT2k0DinF9g7tQn0Bhc_Rpq4CKO-ourHlPb9kWq7w7qBacmKAX54p_V5dLYIAl4Gqxh4zVNJ_rjbvPNrPtndBz9O_SEpxq-o6LOLruuFG8ABGTHq3-971KHIzXL6XedS0eIeY1fk8klIaZ1LQEtRE4xIvrLVoM1rjCk7NSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
