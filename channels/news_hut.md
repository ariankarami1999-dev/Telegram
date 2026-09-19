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
<img src="https://cdn4.telesco.pe/file/ZEsrOZOwbW9Zd-V92GXDi9w3tBrWShkLvCVqBT36BMWaC-wOaieo2KfSm6e_9UE4T0PldMdkuig8IBishZmIte7f-lMvvchPCvap8yMiKapcD-eTQcV4EYjJY3X38XaAd6zAYvpU2ckdg4_0htPjuEG1GRimfKzZlwPYr8Zgz53rw8JEE6aYv2ylVHB9E3hrbMxuaY882fSSNJbGqdxG6G0WxtoTAzbBgeT8YxIjVdxlrjNsaWJsEiwVjxT_8Pq5APKjMydbZdtkxt4dykCwE-DaPUTyHwMZVPZK5bSKHefmwsw-2rY7-eTqXZdE6-Y38cpYrYZPLy_Z1NZSf8OvYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
<hr>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apiee6y2ZPrSJbu1xKkiYldxCVUGd6qUJdg3YWe1OKZHoQGil0GapJeX21kBO-Kbbow4m6fYLtPeIozPZ5RFuUvifGXVsR3BfUHXU5qatgMd3nbzUXbVDFXQwdBASlG4Z4FRrdKbZSfY6FboHupM_sOyOzK-iqvF7j5P7UZKPFlciXFWWdvrZX6YX-X65MsJl61Pe316ittdTgX0YIturYuT2PiY96KcraFn2WsXkNBkZZibuXojbIodICSTOMFgtSyJ-sl7ljLZJu0XeAykFHX28VxuxluJttpdBscnT5JPSZFARn1DAkiNZbN1PxlbLkFhMPcZou5WbVIBhw3osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjXEzXm5OpVFVaE_db-WtyWrLeGqJd8nxMYt64JSushTsEihaqeBZRqYQhZOtj213c55grFdIHmBbbX4l2nDGoeS_7Vk1CWFbsZCEW42Gc2Ik4a5iKl1ilGmS_WndW6s4Yps2E__8W56unq6jgF6OO9FcdnoI2CJinh0U16gN1Rjs2OKac0mgEBGqDL0jqn15XF51-675B2QXWb9w4CQRmO9jBU_7pDl1EwPLyq49T4Soq7qvPwwxlAArkuQXek6dEnkEJujHG5AnudO6__M7yrfth1L5hhGtY7d7ad1Veq6jdAVTolKC16XlPeQ5wnFphImzcPDZI3v_TiadBbfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAcPkJOZ8ke2Ek6OATSFXP1eSUXYhiL35catWjo59ej6Mcey9W6G_0VH4yGJryrwVm9rkYu2z2R6aRWL-LhdHqWEIr9Gz7GV-7-NITUMCJlKqwybPvjHvER26_obS53-zcXUzgMBC72nAUNvoBQwgONlpXZoufVh06s5r_m-8jrAztd9BoQMUHxtAZ20v76mCD8imwmOWJH5CZVzoD_-ZzGDrgfXftEkTWWqXBWbb3eEJYQjkFlukY8mFfU7xJ6EGwDsFskKVUdOQddZxcwSoaG-ofD32pxnBeYPoLePPTxULqh3rAkNSei1mQ_Bpu3SlQF-MgwocSj5nfKcwBzctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojR7vSyCB-2nGq7gOgUtstA-guKpfUhftYST-FYRwKofTH9Nlobz3VgK3UPVFX1z_VEwb5bBewbykNzkJrsgL1cwmHq5WGall0QzNtqvdFn3Fhn3LGGmPgayqib3YisGZYCq768lcfadTxoiIbu0k2Yvjdi0lvcWEYl5O8hvLOv7Y84FE3MqfOvLuwPS5zSP4HUCRNn7GVKYw2nk-WUXq5Nq5toYxnTLrvB3t4dQsNZY5hoDxL0PE_krJQumzIux1HtSHx6bt3AU33hH3aGmjU-wX5vYX0LK6P2NWoc2G47KcJ3jd8GChlXuOHLqqPRbNvbnoDt3B865vzpo3r7WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpZHDr4jJVnvyuJtVWgivT3M7jrfJMXzD_NSqH7oqKbRrH901E1YHmLyw2Ybih0fI34fzGanvBlgWZvzeawjMtFk7gCsBz6qyt-mttt9_bFlkgUnEsrBDjXLZ4WhsTg8FwRXvhY_HMmdaYFuJS_8Mvc-8wzZPZKo7LYcihmTkokfiRrJRS73R0dkCRO12oyFycmFkWapNbw2HqL8uOAXQLN7j70H9ywtIEPc9wXHEe4yrNg5kw36ICRlbcAfqwUHY3vygpq8OsiljFK2gaZgi2Do70Yg5zSw43P9RifPYd5z9pmA08ZXXsW0Mo55ZnuZkfsULe3JYy1UENAucmDtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp2YOb79Nlou4tE64usHV5LayFbZxOlBYfkvHYSW8VZsRtXcIyM_aTf5mJelC7jwKZ48AMF8JtmFhLlgQi1AljM23tFPmbccnpf9Q6VcUhPJ-0TfROZYUeWyOQU7pIihMCAvlSBFEhkF-ALAFeAMEZfx5lsdpiYODZ2XtBokfR2bc2dwk5YKiCIqiGB4n9GNbYRtfOFgeAwXo73VI9BoHTmcMEbJa5lyHdZ9GuEkhtb0wq4GTvMDpI5fH4rA_y9qzmrwxO526sbdo6scJoB34u7et1GeHWkfDuVAvgyXTejyUvDEj02NY-jcKaw7EqeVWLgrcqxtkAqhDWRB386mzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=bkn3a06KhFzW4QKmqwt2VMfchXgx7QBkZcwwf6ClKPEXazvIrMGFhDUJ6_L74YVA4rEhpEt-cCmhiGCXYNEW53mAeEvlNnGmUEHzq_VuQCRYznOBvc_Ip8nTsXlktVlL-CAbdNDTO2dNXaz3epOqNQK6Hz29eRDUq8HKzDkPvlWYCbv2-WKavNRB_yi3EHR51mPpKycY_8EMKhrWrmvJino8ohHb198TdPPJZgeggFy436sKL349ozEaX1BN6V2FKqsNZzTDl7oWkc_gSsMyPiflX2T6SrSUqgSbzisKgpeSqDR5KJ-FR19n83CGBNhMLnvVfF3WrlYDMlPGFPdOpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=bkn3a06KhFzW4QKmqwt2VMfchXgx7QBkZcwwf6ClKPEXazvIrMGFhDUJ6_L74YVA4rEhpEt-cCmhiGCXYNEW53mAeEvlNnGmUEHzq_VuQCRYznOBvc_Ip8nTsXlktVlL-CAbdNDTO2dNXaz3epOqNQK6Hz29eRDUq8HKzDkPvlWYCbv2-WKavNRB_yi3EHR51mPpKycY_8EMKhrWrmvJino8ohHb198TdPPJZgeggFy436sKL349ozEaX1BN6V2FKqsNZzTDl7oWkc_gSsMyPiflX2T6SrSUqgSbzisKgpeSqDR5KJ-FR19n83CGBNhMLnvVfF3WrlYDMlPGFPdOpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMULTtC3_8un0139AVoPCzBDTc7gsMUfNkTJpSmQ5x_Hiwu04XuXG2P8VwKL5PdmaGc1QxfBuoUXVQzUqJzjQzGIV_7parcQbg-rvcafVs7Ve8MvKTxYx1UplZ319TKhhf64R2mJ7SXAoTWa-ZiRe6eXuoDHlU28Q1_JlXnucegRGn1XA3EqSaRdg6mS4gqyGYfEqM3Y6bFd6-Y7zOec7qAqtMUUMPguXIXwGXemh95uY3wzlvRS8qbxPXo7SAtUpglTocY3L31wKPHeIvz0rTK-erq0H3RKuCwsmwACPOHEXsMLVbTKD1YVKSR52t-MZ5HTmzVW-GawC5ceRNGqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaMGNr1xAd17aqBzCG_jGb-M3i7BrDHlAYONHrC2kJCRz4Q4Ph4B77tGEU6p_OzRoeyEyD0Y0TGMYKC5VztZBgCiLLFdnKFNb_fx81-ESWkVFPjGWlNK2HVsVwlGlctg86d14zJXXnvZdXxd7tAmp_FR4_ncbEZNPF_cvWq6uUlVcQSoN_4UOUU6VgJAkfM2RjywqCnpm62DV-YgXkXr2Y51tp55a1gUaUFOFvBjcF2dxpk4HtlcCR61JND8sthjza8b2k_JG-xbiyHARWZTUePPEAmX8t5SVn-tqinfnqpmmKaHB3nlcFC13S0eT8PA53au3QT76bMBLe4dMsth1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYFjyFCN9n59r0kxDcTPo4pesMjIYPRP50y5GuyJbpUXmna_d3pBXSO5DinVbsIfIWp4LJorAXSJLIeGeIuOJp2ejP5UdRxWAc91ZHoDm0GER3MB-4dP8ZrG5YzFybEDTPqWyI33m8-HP3LUj_TIkA3XaphZwlAXbRU-zp9mIQssGlsTpI4oJ6lIWlQmQYTwwou6sSSjhQHwS72ITkDrB6tA1uDumfjS5Ca6Tm_hSVoOb2v0SZYrd7uIGGRcaZq2P-SgM8xHKVjfQIdDNWhlcBu-zufFN5TdVp8UbHEQLP-kl01r66-5ERUBubh7hKkwegAoEYu_XqOvXWMfNhi4cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=kDd-FL77X8lD0DCl40Aq8ZIg4o5gDQGAnBQLtxsALNMkNj_dpGgPg8iRMnFu5wRVoez3WgRHGf-Ufkqf51AzOKNWOHvRZ9rVqmKgIBBHt4b0Cq7n1GC2HGyAxfUaQE_NNVZtkrHsV3zbRi2pUnEfNyjn6_mjb1HAcYFKA6l-9xUbSDpu9PclvLzPgZNCwcn2Se-WZ4WdFesJNSsX4FIOzC8oyFkUu8ivmuM_YJ1ExhkY27YBjwHaQjaLt9Evwhtqi-JI91peDR9I69XAIgU1d7hrme-tJYaQ_V8SKyI9pcB_MijgrbFJYc0_YSlouT0NswPDcCJIu1cXNdeUovzRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=kDd-FL77X8lD0DCl40Aq8ZIg4o5gDQGAnBQLtxsALNMkNj_dpGgPg8iRMnFu5wRVoez3WgRHGf-Ufkqf51AzOKNWOHvRZ9rVqmKgIBBHt4b0Cq7n1GC2HGyAxfUaQE_NNVZtkrHsV3zbRi2pUnEfNyjn6_mjb1HAcYFKA6l-9xUbSDpu9PclvLzPgZNCwcn2Se-WZ4WdFesJNSsX4FIOzC8oyFkUu8ivmuM_YJ1ExhkY27YBjwHaQjaLt9Evwhtqi-JI91peDR9I69XAIgU1d7hrme-tJYaQ_V8SKyI9pcB_MijgrbFJYc0_YSlouT0NswPDcCJIu1cXNdeUovzRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CasySSJugveuLCEjW2_Ry27Glj9_zhAfObQ9zTzou7Sd78l_brthCJLFk1EVROVjpz69fEThoGw0ATSAQlFPmdquZdYnbK19TLNz5y4-_wlojK95OsGLKCrOu1a9plUgMyG_7CcIdbbKB6WkN6G0isH3WTyeK9D9KUfL1hq4KRan3folIBGRMTcrrMklaoysQ3R3rF2CeRxttmHJJhsAl17WsFn2us1iOtp7V_le7obRQKLbSKDvvVKnSITcsTeB4Kj-ln4U9N7aFp8TklkEbDp9lzH7OoXQCVTXoAran6DQiwCTbTk3MEUzmNI_43Q8MUTsBzvLOqsTmJ3WMOGUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CasySSJugveuLCEjW2_Ry27Glj9_zhAfObQ9zTzou7Sd78l_brthCJLFk1EVROVjpz69fEThoGw0ATSAQlFPmdquZdYnbK19TLNz5y4-_wlojK95OsGLKCrOu1a9plUgMyG_7CcIdbbKB6WkN6G0isH3WTyeK9D9KUfL1hq4KRan3folIBGRMTcrrMklaoysQ3R3rF2CeRxttmHJJhsAl17WsFn2us1iOtp7V_le7obRQKLbSKDvvVKnSITcsTeB4Kj-ln4U9N7aFp8TklkEbDp9lzH7OoXQCVTXoAran6DQiwCTbTk3MEUzmNI_43Q8MUTsBzvLOqsTmJ3WMOGUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=YZYNVUuPEQjciXiKghlKB8wXaE4XfEPsDrJECn3Np5nZhYsUcCbAWprkLTRt-LpFo4ZhXPaPNFwXAtBPTMBXqAD2lWsDMJMehLRvlP6iZK-J_rI5Pbz9_1sk2nsCVuJ__Nqb4S4E7bv0iO7GT4bbE-fclzeGHZSWlV-c2dca_-MqHIM0YYEgJT2kXAJP2EqbV0XgRBOyrhOZeGPq_Wbw0oGbYXw7xaBONvuQBpQAqGqu0SqI1x8ofUsNnRTZXmKSkU73q8woZniGkpLunIhneTx-VVE3DpEy8ik7gv2fZTYZ_HZEWxE8FFHGgvbk12qetH0avRa33FXAtiqOqDg5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=YZYNVUuPEQjciXiKghlKB8wXaE4XfEPsDrJECn3Np5nZhYsUcCbAWprkLTRt-LpFo4ZhXPaPNFwXAtBPTMBXqAD2lWsDMJMehLRvlP6iZK-J_rI5Pbz9_1sk2nsCVuJ__Nqb4S4E7bv0iO7GT4bbE-fclzeGHZSWlV-c2dca_-MqHIM0YYEgJT2kXAJP2EqbV0XgRBOyrhOZeGPq_Wbw0oGbYXw7xaBONvuQBpQAqGqu0SqI1x8ofUsNnRTZXmKSkU73q8woZniGkpLunIhneTx-VVE3DpEy8ik7gv2fZTYZ_HZEWxE8FFHGgvbk12qetH0avRa33FXAtiqOqDg5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K0XuCmFUZIPN5oY-BYEQ-G3nxh9a7EUH_3PX3EZ4Z2qYFv6Bx2srQlMLW-TlEFEoloQGLlSJXWQwJTJAzMNtJezPrt8rfdTrEry9Z6ymXQJzWq65BsJLizRGKB5sllQ24i2Zp24uCu3tJcOXNgg-M59CBj3Np--lqBWkvI6kPwsVDaSdwoOYyP-OuUAHMC_8UoPdqGxb2ky-RYGrKE8TY8Y3nZ0fvp9NRl38yLke7miYREQdyiOVHFq0Wsy3Y39mCXjurZRWT9qM86M0Sab-RUNmlonNWnGsAfMRqaw14mNYuHzZCqpEawJ9O4KJ2FK1DBKOwVx0q7QCxgRy31AbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gws3pY34YWPQlAzmvRhtQrjgMloYRWVF1nAY9mN43xaFqoUJpNUxfhQ0BdRldAqMYx8h1hAdedXtC-xr5pA3zyCEabE3hGirNK93xdnqixe5AM2ngv0SWMOF-dTKkfHu_8W0pq8bbJyNSnvNheov_WiBLQD4TBepom3E_V6FcecMH5B9ow3woxfVCKTTubaghBHLSPof6ezvQMkFhS7RdvaJpcDE6lBOmEfWkpgibfcLIZleBcpOqRd1yN9wHqtc4pS4T-QaJtiDviIUlMEa21keXqn1BnyiAzeIIsKddoLPSNslsRS__cmGECDxu1Pq5W8dPv4_3aWC92k_sPh2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79Xm2cRyEvTsKHtUTVbGB6k-5cS2aqxiAaAbCUh1Ckojw55ers68mQMaPN1x4kaFJ_Xbw-Vo6YqH36CDEHkC_jCvkp8bWpLeGNcJj3R_-58cQ5Ub1lx_hLyVv2WHiqPy9_P9lcdRr2HnXGc8w9HV4eXP-lNYCQ3nx8_yBY6tHs4r3Bcl0wClIElCC3kvfXiag_5-MrA6qX8hTZ8VgHQP_KzwQ5uKhMH3rFS5QeaUZHUUY-x7UffSdv64UenHjLfzlGR1H51QBIZrGckNY-ptDmN9dJlvU8ju7qF4Hm4yLQ2oxbqP9dn7JlcU30XlYGJd6nSJANKxoPvec0_zNJ98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwwSrDFsdwCN9X2ggC605G0c8JJkrIlrhuV37jRw_R9nI4AQEdpvAHHqSFsgUhuUKCv-vDli2yO17K2k9xudP34oE9K9kF-31mG3uVpV1xkTaKWJc1ZezqTPN-GceggSX53Z_ZAkIAZjN2wu53CcL34hvy4k4-pvqoEecfJC_3NxctOkrWD0SEhxHeYvpKajJaRDg1eAWmeupVyrO9aETj_4XYPiY47OmxnbJXEpW9bacODu3yqCXqh5GuJUwqpic_hoKjpWbZ8D7BcqlZ2gPZdrKCB2QciUqScl8D8A5BdSB_r_cYgfV7uC945LMePLkw3K4n7fHv94zFAtsJ0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71815" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBXGcCRltNh2dRnEbhXBh8jFeapxm1CI8Vws3TlsUv6AOY-AIOa7ITzrHX62X9fYo3FX6jaOSy1-QzFMAM0hFMx2S656cr5yS0aB01vfVAiwDI_vydId-hgmP9-LSpbzHWhCRvYd4KNuVK3jw96jhO3H3BXc1FaaNjWcN2Zbb6W0dHQhqBPFqvugHd8_qGhi-eM7RKN-WcSumFub4wKL73gZJXPhspKTYQupzF914qymnxZTEZHd7UUZ87KHBMO7K9C9lGJJQ4ul22AwzOT43Pdg2ew87kTNwyt1wc9fvzci7V_KAtTTPckYeUOaGlLkjJH39jWjES-jM9D5VKtauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71814" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=l6bxXE2oR6c0TVFLIt8PGwwHa2dvfbWwExnYJ2_gVerdZnFz1qi3-cdhXvnm0TbyONnZrL2FyUFgmPxWPEZNw5FZm0LeIoCEm_38GF1zmAfKux032WgUMbX5AncsarTIQJSyY7XvdV-YvF6IUNV7wmV-AOVROiQIow7tFTR6VuJy9m3zn9O8euPvEu_6pcBAiTAej4ln8XzVBWyHeP6TDkDU-P9SBjHiouRWunNH-M9Uokkevzid1Q5ATeybh3nbkxJKwLoIvuS0GHxtJds3llER-fLMNLW1S7950cItbfjMX-ixIGGspAs0Egy5qr8Lo5SLBlqdkqLVdRSeKDjvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=l6bxXE2oR6c0TVFLIt8PGwwHa2dvfbWwExnYJ2_gVerdZnFz1qi3-cdhXvnm0TbyONnZrL2FyUFgmPxWPEZNw5FZm0LeIoCEm_38GF1zmAfKux032WgUMbX5AncsarTIQJSyY7XvdV-YvF6IUNV7wmV-AOVROiQIow7tFTR6VuJy9m3zn9O8euPvEu_6pcBAiTAej4ln8XzVBWyHeP6TDkDU-P9SBjHiouRWunNH-M9Uokkevzid1Q5ATeybh3nbkxJKwLoIvuS0GHxtJds3llER-fLMNLW1S7950cItbfjMX-ixIGGspAs0Egy5qr8Lo5SLBlqdkqLVdRSeKDjvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9pGGE4p1TkHpsF-pjAaEf1YtbtRB1ViBRcD5mSQqIhcGiSF47jhwwpCFQjQdLZ5bUoWTQKYIoa4uOEyoiIBb1UyMO80ZbSbbiRISOMx4WiZe3nZI12p3oQSsnQXdNuzXlfPPocGhjnV5zVY-Ncgdspyqw-FX_kogDn8cwjxNAJ1wjDXkJMdv3OGln3uMudFUzW0tpnD7lnrAuNuRjGmFA8s-NrHDhY4uuWPhA5H_Gq0aywXwop3T4ung7Wd6ksLFk5hCAgoV5udg7nla3EPyfIjyqgoJljRC1xWYxqkdpV_w17NBCAgsX-Af2lg15-WVubfdTT64Y7pSJhAnlmE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=VytgfnygfD3XLhw5dSkQdF8oRmEYKKFiizmJfLkw-jW-Y-RWrBwfO8bphA71frLL2wfEZZwTiBKSnO52BvkPh6hZt3OWFWps7P7APkd7yPQvPCQz2GjjJRPhtk-J1RWmHCi8OGZDb1_AbTJI-YEvllYMgG5gIRnYpmoKSE2p2I5kupbKMFF7yjwRKKyh8nouV3lFc6B_zoepmpIHz6_QB9fSXo8LrYPbmTBsw3t8xA_poPtkpsiizWPJ24te6qbw48uuxInwH8HPqy77eti98rmr5FqM4Pe_XUomJHA32L9TNLI-X6WgcbjCBA7ivWjL6elT1HAbVWYUFKQBqrc4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=VytgfnygfD3XLhw5dSkQdF8oRmEYKKFiizmJfLkw-jW-Y-RWrBwfO8bphA71frLL2wfEZZwTiBKSnO52BvkPh6hZt3OWFWps7P7APkd7yPQvPCQz2GjjJRPhtk-J1RWmHCi8OGZDb1_AbTJI-YEvllYMgG5gIRnYpmoKSE2p2I5kupbKMFF7yjwRKKyh8nouV3lFc6B_zoepmpIHz6_QB9fSXo8LrYPbmTBsw3t8xA_poPtkpsiizWPJ24te6qbw48uuxInwH8HPqy77eti98rmr5FqM4Pe_XUomJHA32L9TNLI-X6WgcbjCBA7ivWjL6elT1HAbVWYUFKQBqrc4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_XjM34_QeSt7DFPaipR5d6TG2S2xoxfHceLC4ZmAubNwsmBgr2TEwCBBHuWaGiwcoetz9pzyYLRLY38YMx1CZB1GPARHLUezqJBCMaXiN7_EuldGLmKTouWNpOaS5CSqrpZI7lJk_Yrm0ixEFkI908sApLmQQWixNwvutv61GXZFX0lk5OZEUstE5XBOrWhFzuAP3TQ9t_q8VYFJtlF_FOa07E5QS3l9wZHy6brHDf68mWBCDXk2pgC0yFMfCqsro_b6JZfRkVB26dCcw9aCjGCLguscvS9d9qnehGNyMK9-kiPtDJrvvF9TjEMt8_FRJKiyPLr8I5DZ7UZL7xehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=ho0tsGmffaBFiAYjqQd7Z0P6VC6Dycc_C0n1clNP9Zj5QB2cETwrXcOZsg33LvtnnvyZP5M9mYsg8lo2YP9mTte1nzb7B6d0VoFa450QrVSLnaBK6DPkFj4CiiHmr6FfXEGNUFI7fvXcYtYvcpxP6ZosBvl2tEbGP_9rhIeqhIqT-lKc4Vqc0QTzIjtUGeQg9cMsEZe83UScefQaRN7W-8NQbU_B9B3MT2jL7qgc6uJDvGsrfppvb_Hx-9eKWwfLGRcIEtk1UIlfxy4TJdoWmrWJXNMkHw_K4EBGJ_hW3LAVMxN2LENAL2HLjk18k5sF4rIU00E2XvW8SNZBgpkLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=ho0tsGmffaBFiAYjqQd7Z0P6VC6Dycc_C0n1clNP9Zj5QB2cETwrXcOZsg33LvtnnvyZP5M9mYsg8lo2YP9mTte1nzb7B6d0VoFa450QrVSLnaBK6DPkFj4CiiHmr6FfXEGNUFI7fvXcYtYvcpxP6ZosBvl2tEbGP_9rhIeqhIqT-lKc4Vqc0QTzIjtUGeQg9cMsEZe83UScefQaRN7W-8NQbU_B9B3MT2jL7qgc6uJDvGsrfppvb_Hx-9eKWwfLGRcIEtk1UIlfxy4TJdoWmrWJXNMkHw_K4EBGJ_hW3LAVMxN2LENAL2HLjk18k5sF4rIU00E2XvW8SNZBgpkLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71802">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71802" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71801">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71801" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=YoMdKt-tUFRR0FV_x94bOoWaJIpHeSrASJYDwI9wSQSO-68nxnw3mKChUR8v6GlrNDBa25xa7Xdwz-PIMTXbFSvhzMFJNtVPtKFDQVoTfc5Z4ODnwCOQT4ecdCrK5GNoVDtb_k1LK9X9MwTLab86sRk4p7-ubuHOFF7HDq8SUHV5uSwxSo9LvBU8n47XmP9xHjy2lXDfBLCjTOmPJOJzADmkhQhY6bgg_ZND1P5GBWHcLWU9iyRNReyr0u4A8m91-D533xowLksafT3adT7rhB4ZmrFeeTMJouXYLkFUe3NzQ9HEon7c8o2-pWkzKJBsD-WxXMkIJQoIJXWIM1vXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=YoMdKt-tUFRR0FV_x94bOoWaJIpHeSrASJYDwI9wSQSO-68nxnw3mKChUR8v6GlrNDBa25xa7Xdwz-PIMTXbFSvhzMFJNtVPtKFDQVoTfc5Z4ODnwCOQT4ecdCrK5GNoVDtb_k1LK9X9MwTLab86sRk4p7-ubuHOFF7HDq8SUHV5uSwxSo9LvBU8n47XmP9xHjy2lXDfBLCjTOmPJOJzADmkhQhY6bgg_ZND1P5GBWHcLWU9iyRNReyr0u4A8m91-D533xowLksafT3adT7rhB4ZmrFeeTMJouXYLkFUe3NzQ9HEon7c8o2-pWkzKJBsD-WxXMkIJQoIJXWIM1vXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=NXedre8PwFwFRSD6qpoQwv1Ii0unGDtFsOTggYLajNRXay7cnK_nvxZQ-n7m515ZLdA1HuAvBPqwJkp_MsCJuXbd26xRyI31pI5Q8NYncT1WBvJzaBAPIN7yWNRVLNSo5MO2KOk3sej0t4nB2iVbmnQZsbFdJjskzpyz2lIOBPtW_qjNpRBF021d-nAU8cwYB0yWleIo-7j6SCR143O564Gjbjjb_jMXgo-_zCTJgaulJaAFiUAxvzhMEnUkIQca0_6gXww9hlfu5igiXCP1rD2kJUF5X4gRaQb8j-3GAYAbHabkDziSoz7qiVlotjdI3AC2dL_OmVc6_yw5oxUL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=NXedre8PwFwFRSD6qpoQwv1Ii0unGDtFsOTggYLajNRXay7cnK_nvxZQ-n7m515ZLdA1HuAvBPqwJkp_MsCJuXbd26xRyI31pI5Q8NYncT1WBvJzaBAPIN7yWNRVLNSo5MO2KOk3sej0t4nB2iVbmnQZsbFdJjskzpyz2lIOBPtW_qjNpRBF021d-nAU8cwYB0yWleIo-7j6SCR143O564Gjbjjb_jMXgo-_zCTJgaulJaAFiUAxvzhMEnUkIQca0_6gXww9hlfu5igiXCP1rD2kJUF5X4gRaQb8j-3GAYAbHabkDziSoz7qiVlotjdI3AC2dL_OmVc6_yw5oxUL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAuxi9n6HoSV2Hx6NcAj03RYpTCJbv2-AOuQv5mTZVbOkUzaO6D7jjHGqH9505KLCqEx0o7yWwyiQJ7aV_a6fH4RA0xzttXZwKnDlvvgtEMfeD2qTOAS8kFRpjh25WlavjObWbz5sGAHJmDxbRD_hlWZBZW_c0X0NQvASbm4-5K5YEGbS2AiWGhSHb-ede_c24pW3sGmV88gs26FFym1Fz6pVdLPGk3hhGFAxgiz_S88shnbwH9jKB5WhoHGD3gMKxzfBSkYJKD9h35nqT1Ljbu5NHKZC-B0HhKX6_a_PQSlb6u5hkniUEcr6-0tulRYx02fZFfayICMhSX_hB-meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xem6N0r5tRb8RlVlGaXTmzkJ8SpspXUQOgujZIqLb2jHsFp9JuMVCD4Efxo4YSfYPnvkWJWZQ-FfJwsyObLaxczoFveEDu1BMCtVlE21Ndn47tb44n_-T7k3o-SPTkKx4wlLihef8cz5mf64F8_LlZfNgYFKm_ElVz1w7w0rxgO0c1Sq7NwXDelGoYosJf8iRzLnJ-_mYZOJYzjzglKVhRvNBebtfcZxj5anCTIFPcJ1vUe8Zz1to_sjnJskEAKGTdFQv0a1eDWfnO_MIhoKSzq5A4zabWg0SU9daxb1_H04ueTRDAog_tD5dzRdExiK9Tjx7M7tEnj_USMEHJZKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucI_AyJfYZFE4GeEeQoGWdh1EMSVF9XfXw3_iwdYnX5UKURZrPtR6z5rUdBfC0PxrSfqU-fkVS4OLBYAtlJLhwO26JMFG47imfsWGug3Y7XPzIiijAPOpfxZx9HZZr4yB4nAJv6T8mGZFMlAq12KPobwfrhT8QZ5NRehK5bQyMd7029u4AQtHJrGNSKComNz6CI8v08VurcociDP7mJSlPm5YnJBkeCFr9vSA7ekNWiVGUTRZb0iBn57xPXYnLlQoebvCMojNgMift-frtyzIJP1z-oeEVFy_LcAbW-Qdn1I6zaqzRTHH_0_zotJnNkhZnzGjazgvrTqGK3V-ZfL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rF589FVAXEou6SQ8_rhEGgy0ZaXO46MZ3ipFPaopzpE194MAL2-7C1_JJTj0hm-kFGH_lOJugPdlh5dRceTiPYziV9kKQnY9SY_TzHWNb5vBxMO0KQO-HMdYE1Nf7VLuS4ku35djHLBFDrM9Rv4otPrgA8OGBv_ykl9LxfEakNpUn_z7K5rl58DqOF3fwnJRVLli1b30pZEgWm0COkPCtY2OdrQaYrYMR72euzM04kRA9LH5_qm69iW1_osnShdblKTHt0ZmIQPkaDXcq35mguu5e-TgA90uctgZ21VErT7VuqZQPHRPiF4kss4_KsLFPZJ0U6M2hsmwYAdwBqYH0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlA2Auf-dwVFieAj0Py2RLjJiOaM75JdpOqj6iIwyluGE77L48aO9m7uvgEHh6JSQtvDUV8n33u4cQohAnyFroALXLNlj581zLX7mShY1b22aZuQJ3XNLdyXnronM8OTHYa6ccs5IrSpeN9EL7ghqkluibLCYI-6zil2RTTq0p0PAYcN42r6eo-zk1di8WvmgL42f4lFLZrIZGdWRIvqM8lXCZO_rAt4f_nUXmR0Wwvjp91hbktj1g5pnvRJZUN5H3pSsiWmCiA3AZwILia6i5SpNPGgjumjE9nLKiebSaTcFjeEJT1b3ty8I1W4JXXQJjxxR0eXmolUGoKtDGxkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ze9uYkVsicxymie0nej_O96JRPxCdo0cj-DXXNSY76vhZ81eFDXN7za8V9xk69tiWzcnb8JcfUYbkylxaV95aKiZE3dm5T_a1Yr7NPLfIo8KAy0Xg9YKerhdQFgP8OmuumVnRhE69uv-dEtPK46TyZhMgGYLlVV1hi4WqSgNry8prPwAqvE1ejCwEi12-hSjaeLNzoU9wrNee6T-FTBQN9yJnwA8xRLpkJuMGpTXhbkzrIT2zyM3--1ROyzRu4k-Z5yxOfK9Oe2zkxqA3GGpPNUkiPgtirGOrVP2XwPkYada5JVMWXPREwm3cVgNCEM_R9idrF6cte4aHZXt7skLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8ZCF8WmTJtvVJiiNXyhuBpjvwiAjlNYRGQDAL2ylz8NQgC_bofGEUCcnHDooCInvgNbYmuOH9TsKeQ86soEdFiw3qANsp6Lgc9Rs0BQqTcfdlUAvXscNg_jtmoBgaaruaCLpKZiESnSNluadrMgsaZVQUlTow53P1H7lrEbe8kbO0BojfjpQJ4ILMkYMV1VnwLDcymaTfbuzuMukyzPH4R_i-3mM89fY8gY0sWkWqAkhMRdOM437qVwwaiLc6pe0a1IT9J6O9Y5cusE8MmwAajohmudg_XcSxqMyy5MGgQ7GLQK2rN32ZIv-2-RGhoeNdlniAS_EnkhIigSrjFM6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=vY6sxrVpiOVkVo4Cdlt1YC9KWVhyniR-Ei9IcERvwT9eG_8O1Z7OSQd2nl-T1dGhbwzL2hGrVO_tbAjKw1xjEXz0KRJL5CdGv8ZWrMJYeXWc4U38UAnyTa7dGqhvaGM5fB93UwLgXpMM_xDR5eul6020tBeSAq_oZxmizNcM6AbnCLIB3kLKctF5vu4FMGPTOEVKq5QjF0X5sfJIAahc-FNnyUloN5PUjR4GSLc0YlAEc_Br1MSMQM5JcByIIDdJxb_WdB_6Ew7hbYYHWTIlM0DUaKtbJQA6Y-b43BO6a-VGo0ixtzKQh4X4an0ltqFp4louS5Iof-Uc8OkA1ldS-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=vY6sxrVpiOVkVo4Cdlt1YC9KWVhyniR-Ei9IcERvwT9eG_8O1Z7OSQd2nl-T1dGhbwzL2hGrVO_tbAjKw1xjEXz0KRJL5CdGv8ZWrMJYeXWc4U38UAnyTa7dGqhvaGM5fB93UwLgXpMM_xDR5eul6020tBeSAq_oZxmizNcM6AbnCLIB3kLKctF5vu4FMGPTOEVKq5QjF0X5sfJIAahc-FNnyUloN5PUjR4GSLc0YlAEc_Br1MSMQM5JcByIIDdJxb_WdB_6Ew7hbYYHWTIlM0DUaKtbJQA6Y-b43BO6a-VGo0ixtzKQh4X4an0ltqFp4louS5Iof-Uc8OkA1ldS-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-_JU-_Zcm6VKBxXyEhL1g2F5HyP_I0VYnhtmVbhNCiA2lXmIgU0HpCR6at6aOScC9SfOFfU9b0qkHw0jpxftIZOgvpW0xc3RuxANg1fA1XB93YOAFa0uyeHNcXPUD6jYlOeAFeatSDTPMKh-Z2lGFaoBDMWbVwjWXGs7HO961MWIEvg2ydS30deyD1yTCuBcfLzbLoeQFTS3k_76lB4m8np5fwnXJmn3k4hc4UZlNxEQ_e-iTXHnP0jmx00wepsYXdkVSD6wvXYOe6bG3GE13mZZGxghGCzrqcYDxDa4xGxnRKtVK8YPD_kj2OIcgBJxnhrq72Od0slUYxcBYY-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=LqikKuollcdlKNC3xn8cudpqT7O4FDY_GLVZV4S_tiqq61h9hvn60BXKa3l7W2PnJ4QEgPuJV-ulcCS_J3x4ckBL5jW9O7Wat0Ukd87yMWNldUnsUjoHi8m5jwXFWldfJhMQeHCUUUU_0_HSB8lc8qoxqFVVFIZCqmPCEcN1F6PPschttdEXD9jaUEZcUoKLbLKo1Brgwo2xesvULS7nSgk-Fc0T8FbaGburSgho-qFKWhDRJveNdvMl2wkZJ0IOPOrHZnxe5580PQjL94Pyp37bi6q0pZc2iw-AzKs3OSKufdXIfkt1SzdROBK4V7jxNRt2k0ekGqasZNl_b6wKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=LqikKuollcdlKNC3xn8cudpqT7O4FDY_GLVZV4S_tiqq61h9hvn60BXKa3l7W2PnJ4QEgPuJV-ulcCS_J3x4ckBL5jW9O7Wat0Ukd87yMWNldUnsUjoHi8m5jwXFWldfJhMQeHCUUUU_0_HSB8lc8qoxqFVVFIZCqmPCEcN1F6PPschttdEXD9jaUEZcUoKLbLKo1Brgwo2xesvULS7nSgk-Fc0T8FbaGburSgho-qFKWhDRJveNdvMl2wkZJ0IOPOrHZnxe5580PQjL94Pyp37bi6q0pZc2iw-AzKs3OSKufdXIfkt1SzdROBK4V7jxNRt2k0ekGqasZNl_b6wKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEFHKN5yoseNAxQQRMi_Nzg83GOyPRKfMdyLs-jjGhQj42dsemNOhtBKRZJCKSpIsX6yonBK-H5tfGfQAKfgUrlpyek_fgYuTidsmLyDFocvtXs-uNb8q5IQLJkfQiSGy4jBCCWrFVU92c6b2tdk3TLNUq0weeZQlrdDTZCD--Rb-yopHb2uxQ8M7xHfl6JpPxR97buwBHNZcg0eYH8yQHXkKaRYDGQqijyrCfVBeTwcQHc6SCSwbbHf6e3pifCRXcigcJyPBNvk25_SCbrTInr_lD2yBGZrF0nNHqGutoWdGaTNoQXioqmB1KQAFpJCciHjgBkSox28okDfT7k9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=N6va5E_JlQium6F4-IiNmM4sUzTdhV2Z-UM9h_rrJkqBH5NWzp0EBHMMq-CGBe5HJ48SJEncXMTKEiahjywpjun1hmaZSd2yOunlm6xNkLxDqJvuqUdzoO-gIRqytvcAoaBbrJeNVn0crC-X07PfXzGKfl1R4YSDOXsQkCOAEDtBL4Zde0JEOBmmiMJxBqgCk4hTOMGqdxqIlaJip81i3t0C4jCOpKTC5v30ZbNL___hpcmjfKhAgO_k-vGRstDFPkVtG7hYRIDuXHEVMbdGOkK-K2jMLodn9Jetw0dCqKAECrdloWUT4XhnvrwMsKYkNuZnknUNo1NgshhFqZcLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=N6va5E_JlQium6F4-IiNmM4sUzTdhV2Z-UM9h_rrJkqBH5NWzp0EBHMMq-CGBe5HJ48SJEncXMTKEiahjywpjun1hmaZSd2yOunlm6xNkLxDqJvuqUdzoO-gIRqytvcAoaBbrJeNVn0crC-X07PfXzGKfl1R4YSDOXsQkCOAEDtBL4Zde0JEOBmmiMJxBqgCk4hTOMGqdxqIlaJip81i3t0C4jCOpKTC5v30ZbNL___hpcmjfKhAgO_k-vGRstDFPkVtG7hYRIDuXHEVMbdGOkK-K2jMLodn9Jetw0dCqKAECrdloWUT4XhnvrwMsKYkNuZnknUNo1NgshhFqZcLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=bMZw-ckylYlDDcRTK9KB5pvEj1_vI_BIclJi5_VByU0KX_EPiR23YuGDHa5oiQ8IJ79hWE4tbiJ1ZKvFxIndZ5yXx2swLfln_qGkIiqFmVgQFdIaoDn5uSCsNTmfNEOR_7r9aDxTf5NYyjg85Fv65p_3v2M-KcFBy_R-yJGWJdhm13VLcKEb_retn11TrY6vwimmGcR1WbmQzDQ0PCQgjykfVk6SrbrtufQ5K7BlK423R8bUcMtvW-Yn3kZj5lRHaldzJKDJ_s_mqfqYKhho1Zs0jypJBqGhrSJ6RgvkiRngaULb-ZqFtxARhl7OEggyj_8_Stoinf65QwKJMGB2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=bMZw-ckylYlDDcRTK9KB5pvEj1_vI_BIclJi5_VByU0KX_EPiR23YuGDHa5oiQ8IJ79hWE4tbiJ1ZKvFxIndZ5yXx2swLfln_qGkIiqFmVgQFdIaoDn5uSCsNTmfNEOR_7r9aDxTf5NYyjg85Fv65p_3v2M-KcFBy_R-yJGWJdhm13VLcKEb_retn11TrY6vwimmGcR1WbmQzDQ0PCQgjykfVk6SrbrtufQ5K7BlK423R8bUcMtvW-Yn3kZj5lRHaldzJKDJ_s_mqfqYKhho1Zs0jypJBqGhrSJ6RgvkiRngaULb-ZqFtxARhl7OEggyj_8_Stoinf65QwKJMGB2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=NcSEB7M9Q3gQXeGb12DnWb01qnDFaA-kJgZXtgbN-olOBix3V4eKB1zYZVcx3s0yM2uzYYCSSVS6saf6_y6heEs5UVSnWqcUSikAogk73kG5TodcCX4lu9AvXNnopyNeLX4l3HJVbr9JB6cEMkTgYeAhHoOH2c3cNX9pjScw9JZFK2b_vby6vSqWtenkkGqpl4V4sc-1diOFlDMvkURFSS5YxQ2hjaFMuxo1o9eMsxu6aG2Id6WPZE-TzgwDyHIs0iboBUsfvGYqCiwOvTdFlmpgcqAoUc9-IS7nf4LNqWV8AWpkxREqwo5bu8AvPg5v_IE_ttMmbUtSyG0Z0QiLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=NcSEB7M9Q3gQXeGb12DnWb01qnDFaA-kJgZXtgbN-olOBix3V4eKB1zYZVcx3s0yM2uzYYCSSVS6saf6_y6heEs5UVSnWqcUSikAogk73kG5TodcCX4lu9AvXNnopyNeLX4l3HJVbr9JB6cEMkTgYeAhHoOH2c3cNX9pjScw9JZFK2b_vby6vSqWtenkkGqpl4V4sc-1diOFlDMvkURFSS5YxQ2hjaFMuxo1o9eMsxu6aG2Id6WPZE-TzgwDyHIs0iboBUsfvGYqCiwOvTdFlmpgcqAoUc9-IS7nf4LNqWV8AWpkxREqwo5bu8AvPg5v_IE_ttMmbUtSyG0Z0QiLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQdICwimtmN7EkOATaCpHYzgbpR40vV8bBaB8I05fM1j_G_vMtwvkbmHcxmyL1u3jyRz1HpeO8xKLExOMyIb53SDoIECL__1WhPG8qRRodRtlyjfguSTQsCK55rHD75wrKKMjWrjX7KY3NWlO86lJLqiL1NzaT0q9Q7PcG7lakqetLZSTWMBH2_WyUZJr88otuMxy3qioi9CIqS4oaBd6XI-RB5LJbjUqHHsZpQp7lgWj347GJY1pvTCoVMZEhCydmPxmPAVhvL-2mHiIxGeqMnDY0QgzCk9IZPKIGp7_KYuJD4zm3qsyQXPUG7b5APhWX2rD-Y_kpwowRDrFDZK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=inyzFj2F5iiCDMrUmVRKElppxhrB0c-Q7Sbt8SsKL0zutdvf2eb1O3qmDr40EJqCff1vCiNA5kaKJVHtAMSl-ogrqmXoNvbBchbgk5Vs9trtKPYOyRjle6oEQy-CYpC_gTWj2j8nJTaNUM_El29LYT1Hz8JacvPV5MJsxfa7E9va2ywScCSKTpTHSIrXTMqXWzJyIV3WuIe399010Dk0xXe3p4A3wqtVMuB_x8ChW1CdrDqrfBRZ7pKe0eb4t3_aRAHcsIzvxi3mhHnASlMD_bbCIa1_P0jhJzhRa9ng8qQ3lYGwJMNCEXX39e4etaWJDk7f6Vaq20s5ZIiAV1FDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=inyzFj2F5iiCDMrUmVRKElppxhrB0c-Q7Sbt8SsKL0zutdvf2eb1O3qmDr40EJqCff1vCiNA5kaKJVHtAMSl-ogrqmXoNvbBchbgk5Vs9trtKPYOyRjle6oEQy-CYpC_gTWj2j8nJTaNUM_El29LYT1Hz8JacvPV5MJsxfa7E9va2ywScCSKTpTHSIrXTMqXWzJyIV3WuIe399010Dk0xXe3p4A3wqtVMuB_x8ChW1CdrDqrfBRZ7pKe0eb4t3_aRAHcsIzvxi3mhHnASlMD_bbCIa1_P0jhJzhRa9ng8qQ3lYGwJMNCEXX39e4etaWJDk7f6Vaq20s5ZIiAV1FDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=Dh5c07SzBc9BDw1vI9YEXJjPjYpKA8_8UUDiB4HpsqlLoqcIEV7Qxv9Qu9U-bZ_9W6tBDBO_QopEW4k2MLTZpJYC56faT7Tv7ogUkfVsidQNYtKHoIcOH7MVpdYACkKcFud3E3BU5h1GuwFFr9nMKtMqFyDEPMDelSnUVziFY0056dyjXrZEsZXBJ6Jbwefj-ZErZOemqmUPeqx6WF8IWpS6H1EkfQo-ItTWX5686vOfY5VBA89B3o4Rqcvegwi6zX870Wz4cSKHde-8_w0aXLADDgCT7m3VMBLK-cPh4V9n11e2TONLtbk11E5iaKd6HB21IqVsTY67voN1WnH23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=Dh5c07SzBc9BDw1vI9YEXJjPjYpKA8_8UUDiB4HpsqlLoqcIEV7Qxv9Qu9U-bZ_9W6tBDBO_QopEW4k2MLTZpJYC56faT7Tv7ogUkfVsidQNYtKHoIcOH7MVpdYACkKcFud3E3BU5h1GuwFFr9nMKtMqFyDEPMDelSnUVziFY0056dyjXrZEsZXBJ6Jbwefj-ZErZOemqmUPeqx6WF8IWpS6H1EkfQo-ItTWX5686vOfY5VBA89B3o4Rqcvegwi6zX870Wz4cSKHde-8_w0aXLADDgCT7m3VMBLK-cPh4V9n11e2TONLtbk11E5iaKd6HB21IqVsTY67voN1WnH23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=kI9spnseOaTaBXnllXmWrOBhJ-vp4Ky4nLqegKIYXN6STmK-f0YdIupx1OuZdpFjXa0BXhs9_QGGN2Dz_kMT9W9KRRWdnTd0zLdW9ClYCMjmzlKNZH8xdgkhJ9hDtXfMxG80GtRIPW1rASlcTbCw2QuKsbMDu58uCGoFJwhD-ECFk-HOlUN-8ZkyLXXPstLD0TkvD4P8eLTXVxYT-s_P69QAzq8h0o8h92c5dpqGq5ESHmqqK_zG3E0KZwjohYpriArPH4uzkWibF7ur_BEkiZQa5EdoJn8Z2TsnEKGA95UrZpij4QAlX8Qp-x-BjPZltrVfs14rBycs2as0YUB6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=kI9spnseOaTaBXnllXmWrOBhJ-vp4Ky4nLqegKIYXN6STmK-f0YdIupx1OuZdpFjXa0BXhs9_QGGN2Dz_kMT9W9KRRWdnTd0zLdW9ClYCMjmzlKNZH8xdgkhJ9hDtXfMxG80GtRIPW1rASlcTbCw2QuKsbMDu58uCGoFJwhD-ECFk-HOlUN-8ZkyLXXPstLD0TkvD4P8eLTXVxYT-s_P69QAzq8h0o8h92c5dpqGq5ESHmqqK_zG3E0KZwjohYpriArPH4uzkWibF7ur_BEkiZQa5EdoJn8Z2TsnEKGA95UrZpij4QAlX8Qp-x-BjPZltrVfs14rBycs2as0YUB6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Pjo3m9_EzW7erYqSxPoA9yZ2j20e3zqxRHpU2c4Z8DbXkgM1uSq5oYjJPUTKjB-jKT1p7PcBH9wGFH_Dp5Tl6FAbZVBC-sTbS5khMc9ti5lSnWj7z5IIEsf50i0xN-KH70DvMdA59wX5zmTR_G4EuOukGWfpZ4n1Ys8AR0x5NioYnOpdY9lVu-Hu9peASvMEtd9sGwpoyicAm2JelYYD7vulZuY1_mctOdEPgUPxuU_qqD-SMcQWGPYBtFWTsVezosKYoD3KKSb8PGbGQgFpCFVy89xQ0X5hegcHxcENRgNsXqJImmniIwXXixQKuUCtkmk43cOH83mCphjEyg6_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=Pjo3m9_EzW7erYqSxPoA9yZ2j20e3zqxRHpU2c4Z8DbXkgM1uSq5oYjJPUTKjB-jKT1p7PcBH9wGFH_Dp5Tl6FAbZVBC-sTbS5khMc9ti5lSnWj7z5IIEsf50i0xN-KH70DvMdA59wX5zmTR_G4EuOukGWfpZ4n1Ys8AR0x5NioYnOpdY9lVu-Hu9peASvMEtd9sGwpoyicAm2JelYYD7vulZuY1_mctOdEPgUPxuU_qqD-SMcQWGPYBtFWTsVezosKYoD3KKSb8PGbGQgFpCFVy89xQ0X5hegcHxcENRgNsXqJImmniIwXXixQKuUCtkmk43cOH83mCphjEyg6_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=YLCnsfyrOhlbg-mbKaGQcuW1zX5p7x47-dOEItHgKdFbGSIkXoQS97h-GvRkHeC2ooOCZf-uDnznlkC2aCrcufnYhqqAEIfiRJUAiP1iuoSMSZG-K_wD0na5XO2KGO7uU-Oraup8WJRu19tslqCGXEYwgV8UrYuIYXi0jqA71fYJBl7iMa-cgK1D0gToNWGoKTc9thCc7DxKk4KAl5jThoyvi_-9TEokwN9riyl8HIuQsDetkkZImJTV-6kC5ZMUyyvW9VwbzgWVpZ3NQowSGnumEvA8GSma2siD1SQK7qb-46oQxvT9XrMYVwVHCxQ8jX-M6g79mIycjfQk1pkm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=YLCnsfyrOhlbg-mbKaGQcuW1zX5p7x47-dOEItHgKdFbGSIkXoQS97h-GvRkHeC2ooOCZf-uDnznlkC2aCrcufnYhqqAEIfiRJUAiP1iuoSMSZG-K_wD0na5XO2KGO7uU-Oraup8WJRu19tslqCGXEYwgV8UrYuIYXi0jqA71fYJBl7iMa-cgK1D0gToNWGoKTc9thCc7DxKk4KAl5jThoyvi_-9TEokwN9riyl8HIuQsDetkkZImJTV-6kC5ZMUyyvW9VwbzgWVpZ3NQowSGnumEvA8GSma2siD1SQK7qb-46oQxvT9XrMYVwVHCxQ8jX-M6g79mIycjfQk1pkm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=n6YxP_kC_9_t2k6AWcbUk5GezTyygSQpwFYVVRQs_0Sw3hIpWcVq_ojBXJkO4-iry65sz4Qmdxb67AMVf4jScGsr8X3SUowxmX3dNBy7FzPiJz02D7qEEgED2xBmdtPR3e1hIwhJmgjEcZGcdT4T9OYG88tP3HV52IAzjr907Y7QU9N3alXhAEZJosWAuM0BLKp9RdcQ0h8Q7YeVylKr8PbA8BXYU7EtnwvYue1pmSwe8P27ZxfXRKDsKsDg6vznoOpwa6K7yCF7M8qLACTd7y4spsU9K194DS8f10s59humUOgjZIlK-ZHU6V71vPKv4LOViIQrgr8OcCjNy8mi-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=n6YxP_kC_9_t2k6AWcbUk5GezTyygSQpwFYVVRQs_0Sw3hIpWcVq_ojBXJkO4-iry65sz4Qmdxb67AMVf4jScGsr8X3SUowxmX3dNBy7FzPiJz02D7qEEgED2xBmdtPR3e1hIwhJmgjEcZGcdT4T9OYG88tP3HV52IAzjr907Y7QU9N3alXhAEZJosWAuM0BLKp9RdcQ0h8Q7YeVylKr8PbA8BXYU7EtnwvYue1pmSwe8P27ZxfXRKDsKsDg6vznoOpwa6K7yCF7M8qLACTd7y4spsU9K194DS8f10s59humUOgjZIlK-ZHU6V71vPKv4LOViIQrgr8OcCjNy8mi-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcptyzgPQZZELNFOujTpEIXAvc_np1rAM9Jt9MzbDZnhawvvffHILQiLOTVvSYzb126THqIDbc6luw2MQm1Uu2AK3od20-hC4wsij_Z8ItpT-qHGp5jtrwc7S0-xBg-4u2aytNWUH9k0O9PnAzrGATYse5wWfvI3qcigNs2HYsZG25fyTwGD5qczEccTS6f2ujHFlDG-35JHYzNKkWhs7eFV4jtySF4OdEX2hljNhS0SrCsjO-Slwm4fY7-UItuR3sKT4-VTUQer1QurH_hQM-uws8nImAT9oqWy4MVrGWWZHvB2chWhCtt8hXgIwP6evCOm6phr4uxHYqvFsPKO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrFf6OPN1l9AymHZssoJcrtxC9yHQJZVGPLQyyXE9gU_xX-RlRwNYneN8aDO9vTPn3bbR7XVf9Kc28oXd6aRuF4lJ-X1ho7KiZFeaqfyzepgMIgdALAJU_ZQOP4bsSDfioLWP6UXThJFdVaUOETQk5JdnOcPpgOUe2S--1amjvAoEijWttHq_QauEjP1ccswVV-cBDoS7jwWsSJlyKpW_qVmcpc7UB2iVJvPItPXbj6hHV3JCg0R_t5NLfjEPlxvFhf4gn0NIglh-Nm8Rjzba5LOX8ttrWORECrIeKk4DXkti-OxSchl1vGeGHkMqrrPftzUUIWbNq3WMlgUSA4oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSSt7r16sWWJC3AffWw9mvemQblyNAy62LHYhOdJkmMI4jZg1y5ssZgNmkrTvrXijjhY--EtZeC9m7B69cdLmgA430jETaCWhIuedsZSVpDCoEjrCTmZ_BlJbCyvA1T381x19VIroZrOwR0cLxZjWx8mJi5idPWi_rYKR8gSZeB3HVLMdzWK8yYujAojtQVhi3z38CW0WhjkouEK-bkC2kqLA4d_5xQQiHFvGo8kmHaKdicbj9tEoRf1GkDl_Z4dFcjYFRcfwbQj23UmlBEzJWSP50A5pf5U3NtnrDYhvpPP2m4fBJlld18QrOm65U7AIV-NduxydKoVuWycMuKtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpP7NpIPr5NddJVMmGLSZbf_m0JaazaiCa076SiJRZlwubCGH5lQOM5UaTb7ThaaYo9CnxJwImjnsb1BcisrZE9U9zW7O2flaXJBxI_Jebbs6Ph3mRP-EPLsX7m-4gAJimfSuREgJMCWy5-XhIkr-qsFwcCPf4RoZ7DOLvlwcef1ZV02WMAqmGOAVGEXrIdibZHsqYNqrpPnuR58m4CyQ5rrpN8yz9sl3oc8FQcWVKtViNyJQ1cj6czMJPNZfbcTBNy2j7u-GKdplbDFZnS2CRYSPZvC0Eo1zTibzZRkc-NFLxjAqw11OvuVTAfuLlPGyerdTmvyiBEgkyLfzcAt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEK22yz9_SOe-hjJlFRA_o7jQVxwUaRAlPHNPzHQCyM1b0_7p8W0X7ubLv0QBWavH-3sGSRSe_Ni6LWpKoCE18KN8GfBja0NsYX46UQryQ721gdk4ZXAHjSIJA2GaamSyARAPoqNYjmMug5GWACI9ehVjvFb3qnTHegEqkV9LGVEok6Q-rv45wunlHWzjiw2uLLqhXmg4x0DqByDdzsi7k_NkyWwsZhMphteg57ZBbQjidzpvLY8ynRZp4tM4Tg_WOrotIIbmjosiLtXT5Hlb9IufIhFq_4TJvLzbS77BpBZMAYxsJfAWLoy7MHYaDRXXmARjnBMq-_tEcd5TxV1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTu5Yg13q4MD9XGq1MaDfsWqvGZfnFvXm_o5f3CxRvg01J8O0YT-MvyYm3-wUCwxA3ffViotVuyJgYAS7QhkhTu0BHbhH27sqdCu2SsdndwZC0umhKFq_WSxx1D2sgd42_-HS8gTj9C6pOWMBEZ7eampIHHkZpPF_a0ouI_VW10MSoettXJ_JeOPS_3UxSESvmo6py0qQfFyKnDOWeg_-Gz19t33-n9gNtFDM4O0yfIyP3Lo-zWLcBs0NrQqJXILo1PMl-L8Kn4a1eLnRa9fUnYbPmLT1Dc5bJYMqEsv3XwGukKLw1Dz7WO-qu9T9HOSIe3LZojB47RdgZk71KSLew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRmbBbR-dDKbU8KLvVUiTf4WntWmNsPK4NACtiPl0_3qX56PTNsbWMfjrjkZ0ASIXSBfdvNrK-zS-sX_3DIyfxbsdFxgB-brjbJsHG3yGNH-CAJPZO6xFWlojyrKoooWBv1JDAOdFYtuGGj0dlP3JhVMgdqlu4JeiJmJkYC7GFsCNLfE8sWQTIgMohDzTnfSUVs3BX9qlxz14YnmPLj5TszBbKQzl4Ot39qLuLo7RdfrTBLBd3Hy_pTOzPGdMrAn_SptJeoAxNSvuiFkqG_RIdrGxJBrGGjYM4HPWPmf31FtINHWfAkjR-40nrgFtjNB9Llbu6z5Ah-9fzrCWIc-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=f41f3lYYU8X4ZzBg_8HL8Ev28c4nDwf_BP9vPuxZbYVCIASmMdZscfhhNukEUNYgv91tD0ry2Sn_HI1zF0j1ZYujAr2SJ18G9nqfl1H-kM89C00rfYGxth_1C549kdyFnqaLm5Gd2J6mj88r53ZONFI3ptjIIO_iA2DL4pSDxPgqEDPIDvfBH4F1fJ-q3GWfP_IZSBGJyUFXD38N5qqGre8jzAMogiUJr-_QyklB3IYEVQ9HhhPVKmMsTrvAqQWE8Dla5okyqqrpIXpsmke1nxahOaftBh75rV2I4bk7KDLC3MHJJI89Q0x3zi0kR8C__FwdUn1Vdo5XwYEng1e0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=f41f3lYYU8X4ZzBg_8HL8Ev28c4nDwf_BP9vPuxZbYVCIASmMdZscfhhNukEUNYgv91tD0ry2Sn_HI1zF0j1ZYujAr2SJ18G9nqfl1H-kM89C00rfYGxth_1C549kdyFnqaLm5Gd2J6mj88r53ZONFI3ptjIIO_iA2DL4pSDxPgqEDPIDvfBH4F1fJ-q3GWfP_IZSBGJyUFXD38N5qqGre8jzAMogiUJr-_QyklB3IYEVQ9HhhPVKmMsTrvAqQWE8Dla5okyqqrpIXpsmke1nxahOaftBh75rV2I4bk7KDLC3MHJJI89Q0x3zi0kR8C__FwdUn1Vdo5XwYEng1e0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8EftBETt4E6JDnx7MNBE2YFVgNVlmTZyNlsTdjiuhXnmgLEuP1L1S6bFimIG731vZLR3bYJzzGjcNYREvTD0MXLHMLi3AHaF3hCSPBBrtymesIxZi6wI5DpY3joW0L4X3Q7As_I2o__SkrDRJEATGoXPDXjvt4t92YsK1Zeog1QqQcqaaARPvJy-5kFXW-PXMbJEDslEYHGxBa8O8DTAiB8eZOAojNJryR7BbuYEGmOwEZy918NkDCJ1GZhv24Ammtpn9dMKdpZRtgJOdbJ-Tg3suxrAsh0yJgdVT6YjmzDbMTub1prJ-RtJTAsSfu-M8bhu8Hc-6Y27hg-2QnXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=DmVWR-_oy6CP8H2k7v9dWrslXtk-bTgS8kkX7j1PF0RM7nVIYHupq4gM0qG-KGwymM0TKJoUkSHeyWzjs0LipE30S4Nq4bqtaZAJPEhaXepYnHqmaLBGf6VxqQWAFjfHROKb8XcJdS3yvoqZHR5jZZyLrCOWhxj87DTBRvs8CE6jnVrB0aRRnozULvgzAqrPJDfzcNdqBDohaNw-LbLD2syzG7wBnktQJ5EBubdZdVG2Ol9ydUJtuZDxSDuWCGnHnU8IIxP6k_kOJnXPa-pXj4qGkKng03Zx4yoMOC8rX_XU3EgwbJNO2eW-jxKSfExOt72T3_za_xEkegH6JguTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=DmVWR-_oy6CP8H2k7v9dWrslXtk-bTgS8kkX7j1PF0RM7nVIYHupq4gM0qG-KGwymM0TKJoUkSHeyWzjs0LipE30S4Nq4bqtaZAJPEhaXepYnHqmaLBGf6VxqQWAFjfHROKb8XcJdS3yvoqZHR5jZZyLrCOWhxj87DTBRvs8CE6jnVrB0aRRnozULvgzAqrPJDfzcNdqBDohaNw-LbLD2syzG7wBnktQJ5EBubdZdVG2Ol9ydUJtuZDxSDuWCGnHnU8IIxP6k_kOJnXPa-pXj4qGkKng03Zx4yoMOC8rX_XU3EgwbJNO2eW-jxKSfExOt72T3_za_xEkegH6JguTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=BK4-dCgKAXyYZW7L7mQ9bwK_S6ZXs_WzYZENgZstkt4Aj3MMxci61rzJVnK4zPEUai3vpCjLXHSAG2s9ZBw7QU_maO6Snh0t9j2WSznBBKCkb3Vz6t-RWWTSsHNM-9ezMFd9I5d-0UjTuFdSWQg7j4dgObhCwWzuqYkiQQIIrY3ZDJso3gPUdt3xM4UjeHpoioxxD3i8ZRbJPZV0W4CUgUh3L5EuNFw5_5cfTkjLPiHeiW2JxDM4d_l_BOtQYWFjlB9Qrnl9DXCSRB_pBQs69Sfb1h0MgL1AAxLMgDVooWmA5SMeebgXYQJ5v2-ASfTwpLfadW_-h3SPLcf2nF23ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=BK4-dCgKAXyYZW7L7mQ9bwK_S6ZXs_WzYZENgZstkt4Aj3MMxci61rzJVnK4zPEUai3vpCjLXHSAG2s9ZBw7QU_maO6Snh0t9j2WSznBBKCkb3Vz6t-RWWTSsHNM-9ezMFd9I5d-0UjTuFdSWQg7j4dgObhCwWzuqYkiQQIIrY3ZDJso3gPUdt3xM4UjeHpoioxxD3i8ZRbJPZV0W4CUgUh3L5EuNFw5_5cfTkjLPiHeiW2JxDM4d_l_BOtQYWFjlB9Qrnl9DXCSRB_pBQs69Sfb1h0MgL1AAxLMgDVooWmA5SMeebgXYQJ5v2-ASfTwpLfadW_-h3SPLcf2nF23ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=HNJMbl186a5unSLJdGwnw-tZ1mz8bNEWAjQe-G1kqamb35Gl8DXw_7LlvtVtZlRCmKO2L2QiEZ0TB--9ltSWCDGFWhgFqyNm5PdvOs72pSAiomFY65M9YIbf8BBJy4wPRsLFU4OPqaheo9YO8objilUjCJZPIfGDcOUrLJxs9bfKpAO07iTBWY0Rvx2Ue_-cSvcHEJd996DFD1Iwuu9Ipx4KBMpCXR0w-Et6-AkCIsPcTOKZ5LV-rYYIYM00efFMM2NlGUMYKIi9a24V0yr_NN-cu_Of06HiJks1FIO3oV7xrHGnVNFQTykMdvvTk6Sz6fI5bZ85D9eyrV0I58J_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=HNJMbl186a5unSLJdGwnw-tZ1mz8bNEWAjQe-G1kqamb35Gl8DXw_7LlvtVtZlRCmKO2L2QiEZ0TB--9ltSWCDGFWhgFqyNm5PdvOs72pSAiomFY65M9YIbf8BBJy4wPRsLFU4OPqaheo9YO8objilUjCJZPIfGDcOUrLJxs9bfKpAO07iTBWY0Rvx2Ue_-cSvcHEJd996DFD1Iwuu9Ipx4KBMpCXR0w-Et6-AkCIsPcTOKZ5LV-rYYIYM00efFMM2NlGUMYKIi9a24V0yr_NN-cu_Of06HiJks1FIO3oV7xrHGnVNFQTykMdvvTk6Sz6fI5bZ85D9eyrV0I58J_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5b6g_D9lPz55BVFu3t_n5ZnsVHJEYJZfMz6v1fBWYtY9x_SIeR1j7EuKz_eyXQEKGB9_4MPkfY1MfetvId8x6euAYwvHzJ9ZTCarE0P0fBUMF1WRuNFJW2F7PxajwS3_rqAbKznNfppKjbXIWOBIfgEPUak_tOBX9XGr0D_VMq8E1AQg6CNQgoaAIe6qs150Na4Lp-flEV9kyMXyQDuM46p3pqOnmk8S1kxRIJVuv6McrJ7Z8_r1sYhCrbE8XMGfJqxajTuKV4LzJa6jPdIr5HyC8iLO7brTai2PtrhRWyb9Zrpf-z7Y9Yilvmd4sRYV86G4aE_64afAuJzYxqZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=T2-jIEu3xpRQsU1W17jks8RaHN8mLSlbNkSFyNIPZM_LOB7hnml6YdTeosKHb3cciRCMHF4Kgt5KrZu7dKuuYjy5ur7F-QEsxSmM8smEro0iWy4QH3lomvbpIyFX4BpU22T-SeavgcTl8XJOcCr90jY0OPnFmUdjYQmVmDtvU_LfN4D7xWVf089vcWX31eCWSPlLHwGtuolmRpagwxhqiLC1WfgYx-tHUDBizI2Ky4yIQDbt-NVbvPfMnqFHXMYCvEpoi7iXUNytFg8b8v1b4HuOhy03kK7OT6Ud3BuTqa_u2S-lm7kr9YOl8wdCMGz47RI0sSfDl8WI-kMgRoBWF5zjxKkojFddQkQo3VkZzJsWKEsclzTC_nXQS8pGs41SZTaORwe4i3ziZThOxpPiay7-kPukluEsJpP54tSosKMprijIecFOIqT7OFB8vUOp1oBC8O834a1jiQXKVCba7KVfYm6vzHPnSHSX1PBHdF46UfQAgS2HnU0El-yZD-1F_W88j5VO09iH9YdlAXagan-63xUvuf6cKIwSdJFWFpy06Buvw60UxHM3jeBg83kY_wYitm7eCHunJv6Yy6RZ_NM8RbTPksuUU49K10zp85iFHA9ZXTqLkytX8_LJarSrPJgLYp4NsUuqBw4kfaPKMF_TxkUWXMm7ciQn_DVvInQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=T2-jIEu3xpRQsU1W17jks8RaHN8mLSlbNkSFyNIPZM_LOB7hnml6YdTeosKHb3cciRCMHF4Kgt5KrZu7dKuuYjy5ur7F-QEsxSmM8smEro0iWy4QH3lomvbpIyFX4BpU22T-SeavgcTl8XJOcCr90jY0OPnFmUdjYQmVmDtvU_LfN4D7xWVf089vcWX31eCWSPlLHwGtuolmRpagwxhqiLC1WfgYx-tHUDBizI2Ky4yIQDbt-NVbvPfMnqFHXMYCvEpoi7iXUNytFg8b8v1b4HuOhy03kK7OT6Ud3BuTqa_u2S-lm7kr9YOl8wdCMGz47RI0sSfDl8WI-kMgRoBWF5zjxKkojFddQkQo3VkZzJsWKEsclzTC_nXQS8pGs41SZTaORwe4i3ziZThOxpPiay7-kPukluEsJpP54tSosKMprijIecFOIqT7OFB8vUOp1oBC8O834a1jiQXKVCba7KVfYm6vzHPnSHSX1PBHdF46UfQAgS2HnU0El-yZD-1F_W88j5VO09iH9YdlAXagan-63xUvuf6cKIwSdJFWFpy06Buvw60UxHM3jeBg83kY_wYitm7eCHunJv6Yy6RZ_NM8RbTPksuUU49K10zp85iFHA9ZXTqLkytX8_LJarSrPJgLYp4NsUuqBw4kfaPKMF_TxkUWXMm7ciQn_DVvInQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPHdN3mozuqQQ2eW2509jc32Z6G-Ww9iMI7YIozHskMEi1IKPzxeXQs-vlirfq-Ve_PzdyttYO6o3Fmrgllwf9D-Cc3xijVBaZJKwuafp7tbLT5Th8-KJkhTdpZ_jlnzefK3XlXItJDs7Sror9DPKpW99aog6nSx_Vr55Xn8d7tH_sND9RVnv3A4mD7w64Dyi8KuBS6OFtWeRzXABwLRColAo1_cr_asXDgvsUhj0pY_XW4SnsK4Poq_Xu395Roe2XQEHPme9-fl6DIRGKgyi0l6yR4JCI9TXEPl3TNapYM8-v1quWq2OWXvMjv6cjfYB4qYCkPSkuoTp__UHBjPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=fbAsr3VKV_mZdvrc3wYNLH9d2We0UXOjv_xhJ6yc7YwCw69X6xYSZP9E7GmlC7oLsIsddp8AKzuWM-nWiqlZxL3bRWhYQAa5bLz4bJtyojoHX-Uzi4zX3MRmF9orD3VVroo3anHUKmwbeD8u-gJTDc40xGBYRcgLxQQa988HjMPoOl-gyh0VnyP1eL91X1phwm72z5_vg4HeOG7ZewArXxMn86XD0epZ9JoYgnROn1z5ImmcwrB813_TRsbygijjCRokkhMu9OMj1MiMzAZS0y1ahhHCET3F7BwjKpRbETCr7_y7gFrQMuiWyR1JVDq4T_Kat-h9oZRl-yv5DN86Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=fbAsr3VKV_mZdvrc3wYNLH9d2We0UXOjv_xhJ6yc7YwCw69X6xYSZP9E7GmlC7oLsIsddp8AKzuWM-nWiqlZxL3bRWhYQAa5bLz4bJtyojoHX-Uzi4zX3MRmF9orD3VVroo3anHUKmwbeD8u-gJTDc40xGBYRcgLxQQa988HjMPoOl-gyh0VnyP1eL91X1phwm72z5_vg4HeOG7ZewArXxMn86XD0epZ9JoYgnROn1z5ImmcwrB813_TRsbygijjCRokkhMu9OMj1MiMzAZS0y1ahhHCET3F7BwjKpRbETCr7_y7gFrQMuiWyR1JVDq4T_Kat-h9oZRl-yv5DN86Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=jyU__1dGFVWKwwYhq8LLgFpui928F-CMTke3Uv3RCBHV625tE6V5v_ETM6EgcyuJraOirz2jDFRnIpjoR9IV4ucgya5VN7W-TsikbFqI5QsIaTmjsloq-rIQNC5qH8qJl_iB3Ka7DqLc9XI8JaWACFLWAppuehmRUgi1MpMMDHsbfTJAo1TO_Dm35obV53pxbK5_0DvJZcgq_OecvLxM8xe029kAcPTIs9p_k0OuWl0g7p4xvglM8tF14_ISSOtXUqG50gnh-C710UOACL10AjWHHdwF-rTfC001mFci454CjexGfuTrtLDaMe6_yT4sYcUyr8x0QcyeEY67K6wn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=jyU__1dGFVWKwwYhq8LLgFpui928F-CMTke3Uv3RCBHV625tE6V5v_ETM6EgcyuJraOirz2jDFRnIpjoR9IV4ucgya5VN7W-TsikbFqI5QsIaTmjsloq-rIQNC5qH8qJl_iB3Ka7DqLc9XI8JaWACFLWAppuehmRUgi1MpMMDHsbfTJAo1TO_Dm35obV53pxbK5_0DvJZcgq_OecvLxM8xe029kAcPTIs9p_k0OuWl0g7p4xvglM8tF14_ISSOtXUqG50gnh-C710UOACL10AjWHHdwF-rTfC001mFci454CjexGfuTrtLDaMe6_yT4sYcUyr8x0QcyeEY67K6wn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=r1pAtdy5mbBFZi-u02H1KRVnQzlR1P-ZibTTxGUDo0v9OLrkhEct7Z6JjHPCZn4gBNSOkiFaZeMcd29LK-5-_gUhyc_cG9gty-eCBfB4q6my2tsl0PR4czHEdGpNBtfgRr8T0Ua1bzrwfB02PG1faNvb2cfJH97Nl5km1v0XLA-d9mP-EoBQi-zbin3HhHWO7E7qCNSKn5YHG5ZttCqPj13_zIJ9YmWnZttaeWz2dLg-DTW-8URrV-SAwOc4KQZHvmpsFJSZG7K164k_ZfM1xDlJMC20ZIjcKinSEFFj_t4iSdpAwfXYX5OLjvxVhiAooZMbQNpwLRJyqXOk_3xxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=r1pAtdy5mbBFZi-u02H1KRVnQzlR1P-ZibTTxGUDo0v9OLrkhEct7Z6JjHPCZn4gBNSOkiFaZeMcd29LK-5-_gUhyc_cG9gty-eCBfB4q6my2tsl0PR4czHEdGpNBtfgRr8T0Ua1bzrwfB02PG1faNvb2cfJH97Nl5km1v0XLA-d9mP-EoBQi-zbin3HhHWO7E7qCNSKn5YHG5ZttCqPj13_zIJ9YmWnZttaeWz2dLg-DTW-8URrV-SAwOc4KQZHvmpsFJSZG7K164k_ZfM1xDlJMC20ZIjcKinSEFFj_t4iSdpAwfXYX5OLjvxVhiAooZMbQNpwLRJyqXOk_3xxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OToU_mHQ3lqW8brM62sZdYqyC1bdTR6DPH_XNpwMqgOZgn2UqmDqhlxWBEK-lUFxAXG6WU4YXQJXGqEHb3NiGXNPowEyEg9CptK1250sYlS1kOz3eQwvz9CiUdKmRkdJwb59wU5Tfq63JXjE0a2zvHBrnZwuXDkzKNalp_HqBDx-K9aWh6LjgElMci92cTFIoJ5oXo-c3CdiroKGZUuNm868iHCwL2cYAgjT_oM_TMVtvSmECyuGrjbHHQB-bgs6WSz4ngszqoC3DvXTTdsoh1Tcu-uELMhu1gV3d_VMuQ2xVx9-1KVjtVgFA-oh9jKt3scAFET5VBLDSiWjr4-IVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=AjG7OIsKob0un5atzGzqwr4shYdzye4MOU4UAaU7133TzdYemTmn9JWO_AABs8aB5iAe5F-w-jW7X5Y6plL5_0eho6KI5-yvDHkkDlXE9KZ_lTqzbXIXBLaVyt4xZZS2HPKDp8j62RIwQHebvuSgeawDydSUK9ueeBPuQBwnWiapN4aiFNhmYnY92x5avjEvclIQgCv6hF0aHCY3HhsRu4SyQFLjrlCnUc51bhinT1ajfOcy0PKgWPOobruS_RIwU0Crt8ZNuvNrkRWnmuYm1z8BFvnVm9s3sAUh0YklXV4_H3_zGTdpbhqibNmzHoxOnxqWPAUV9vFIK5KiW83Cog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=AjG7OIsKob0un5atzGzqwr4shYdzye4MOU4UAaU7133TzdYemTmn9JWO_AABs8aB5iAe5F-w-jW7X5Y6plL5_0eho6KI5-yvDHkkDlXE9KZ_lTqzbXIXBLaVyt4xZZS2HPKDp8j62RIwQHebvuSgeawDydSUK9ueeBPuQBwnWiapN4aiFNhmYnY92x5avjEvclIQgCv6hF0aHCY3HhsRu4SyQFLjrlCnUc51bhinT1ajfOcy0PKgWPOobruS_RIwU0Crt8ZNuvNrkRWnmuYm1z8BFvnVm9s3sAUh0YklXV4_H3_zGTdpbhqibNmzHoxOnxqWPAUV9vFIK5KiW83Cog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=aWMZwzhOx-DdUL_lXeEPscpRLZmOfpIlqzcH97AGgpNn_rHMUh8yslDvYRlq2yBTTYPs8cMB1Y_ZlVIIbyvLn3PV4AANz6dpPJzh2jSbh4phe5ihxmj26rAUcBfxkkjxJwOAGqd2YkkltKULEFMMbxBs23lKJ1T5JCug6nwRc1u_JmEWmcFj_1BWEjeG4XqlAMlKKSj4TWKfL3sqNT9l2AUYpXAnjWCHGsFgOMjJnxkwKuEJu9jxlzCvmR1_ULeaCxC2c2KUvJMZtpLCHj9tjIdN0oPOfkyQPGhrTHEb7bT-RBpG0qMn8WA_oXgncnKY03de5v-D0K8fipcUFyuAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=aWMZwzhOx-DdUL_lXeEPscpRLZmOfpIlqzcH97AGgpNn_rHMUh8yslDvYRlq2yBTTYPs8cMB1Y_ZlVIIbyvLn3PV4AANz6dpPJzh2jSbh4phe5ihxmj26rAUcBfxkkjxJwOAGqd2YkkltKULEFMMbxBs23lKJ1T5JCug6nwRc1u_JmEWmcFj_1BWEjeG4XqlAMlKKSj4TWKfL3sqNT9l2AUYpXAnjWCHGsFgOMjJnxkwKuEJu9jxlzCvmR1_ULeaCxC2c2KUvJMZtpLCHj9tjIdN0oPOfkyQPGhrTHEb7bT-RBpG0qMn8WA_oXgncnKY03de5v-D0K8fipcUFyuAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=a4_EWvXXo9yZvopA4padbeLctPzkA3w0rOPEOm3QOUgPU3YZj0UGaVH-4g53eJU8tPoHHqrnokRcFuSVQlpEXClBB-tMjCifzZlLiOxFNziHu4eWUjf8NArdOBYEvb8DyWLZvjo0rT-H3k2N56i4ITUNufSkW5V0uNZfjyjkKY6WwR_nchI2QGLB2z1xGP2kaqbgSfzonvj2IDFZ7LC64CC-yMpgy8oL5NtLc-Xrj2Afiy5vnMlfQy_U7X6RinFjXQmJ1i97ThXbNq5gOS-UiotTOJnuRO2rEkQckPXx3suf13b2hd1VYv2O_PACvL-npgPJ4gYmPrrdiDJ4tLWSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=a4_EWvXXo9yZvopA4padbeLctPzkA3w0rOPEOm3QOUgPU3YZj0UGaVH-4g53eJU8tPoHHqrnokRcFuSVQlpEXClBB-tMjCifzZlLiOxFNziHu4eWUjf8NArdOBYEvb8DyWLZvjo0rT-H3k2N56i4ITUNufSkW5V0uNZfjyjkKY6WwR_nchI2QGLB2z1xGP2kaqbgSfzonvj2IDFZ7LC64CC-yMpgy8oL5NtLc-Xrj2Afiy5vnMlfQy_U7X6RinFjXQmJ1i97ThXbNq5gOS-UiotTOJnuRO2rEkQckPXx3suf13b2hd1VYv2O_PACvL-npgPJ4gYmPrrdiDJ4tLWSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=hCpZX7WjjTZljNTSSVnE24S8cDa0cLYp9l4Ic-sNrShhTmoAgUxBB3LOZnmJSyXG0QXy7velvBvrxj_5kJPc6RkjMnu5CXmpv94JdlIvvxcgHaBzhI5P9XKaPgJIxYFi8m7KKnCoybsROpWaKc07Gnh4231-nPv4x__NaUDMhYsKlqYkM_gcPJx5zaopdfthoROYqFVez2rE0yqmmjwvHLtZdtvOVQcXYXi7cGohZJJhqpzpoaqmpA1O0mYNAdX1N6tPZLgQMIPAvQwCkzJ2cRj-bKEDFnmD97-3ARUwAJDViscd2nQ2GlmVSOV-Bzqkb7OVGTnens7dBSJQIOn_zEGWZ1zEqRKrMvl71cFmkBF1UF1z3RgdAK8eR1X6PSgTIANch5tSNebwTFF7d-heCLIMnSoUP5_AxWhleVRBZyNGv2Xx_JIRtXf7ECyaqqf6N-n5ImjKVqinj5Rk-6hNBS1yyaHU-TRi18t9XXsyM60Su1w_4Ky8Ro4QI2wxH5OjVnwyNOZepZNseChL6z8T0PCWgxRc9CQo3XWeTEsDf8aeGJUIaN1qzZfMdqdybwT4L7NoW-5sU3-BDpYrP55PC5FIPyBil93-xxN3uqpNg5XJPIoOVP8eNnN3LQpbpGTXCDOdiQb-FM0-McbmpijKyoqpmW2sCQ-opQwkxQ-eIGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=hCpZX7WjjTZljNTSSVnE24S8cDa0cLYp9l4Ic-sNrShhTmoAgUxBB3LOZnmJSyXG0QXy7velvBvrxj_5kJPc6RkjMnu5CXmpv94JdlIvvxcgHaBzhI5P9XKaPgJIxYFi8m7KKnCoybsROpWaKc07Gnh4231-nPv4x__NaUDMhYsKlqYkM_gcPJx5zaopdfthoROYqFVez2rE0yqmmjwvHLtZdtvOVQcXYXi7cGohZJJhqpzpoaqmpA1O0mYNAdX1N6tPZLgQMIPAvQwCkzJ2cRj-bKEDFnmD97-3ARUwAJDViscd2nQ2GlmVSOV-Bzqkb7OVGTnens7dBSJQIOn_zEGWZ1zEqRKrMvl71cFmkBF1UF1z3RgdAK8eR1X6PSgTIANch5tSNebwTFF7d-heCLIMnSoUP5_AxWhleVRBZyNGv2Xx_JIRtXf7ECyaqqf6N-n5ImjKVqinj5Rk-6hNBS1yyaHU-TRi18t9XXsyM60Su1w_4Ky8Ro4QI2wxH5OjVnwyNOZepZNseChL6z8T0PCWgxRc9CQo3XWeTEsDf8aeGJUIaN1qzZfMdqdybwT4L7NoW-5sU3-BDpYrP55PC5FIPyBil93-xxN3uqpNg5XJPIoOVP8eNnN3LQpbpGTXCDOdiQb-FM0-McbmpijKyoqpmW2sCQ-opQwkxQ-eIGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=SLtAyNEGG5_fRI1yKVo99Gy72mpcwWFLkwaZ4EDFxRIiZZgaDkced_Vw-zdgib5cdmu90mR4kbQsjWJvdMoGlF10h9FI0hVHb8iruIOvCNTfysejLO9DXX3F4Clg__zI69LoO0E0m56R7vRz7IoR9lzzz98-XVG3jm63Sj6aHtVezaQyknjrY0WlmGy0Gi1T4hzMAqsOkb5Jf6dvLXb6rn7iUHInoqCg9f8IFZuK10jZD7lmj6nn0PRdjdTUsCWeSJv3farz7huTh9ig07rX_mL4zQeg5FFoaWFqo6OB5jTRAeojLhSxBtyU2nbF4WOjmfcDz2q0o6FnweVz5voSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=SLtAyNEGG5_fRI1yKVo99Gy72mpcwWFLkwaZ4EDFxRIiZZgaDkced_Vw-zdgib5cdmu90mR4kbQsjWJvdMoGlF10h9FI0hVHb8iruIOvCNTfysejLO9DXX3F4Clg__zI69LoO0E0m56R7vRz7IoR9lzzz98-XVG3jm63Sj6aHtVezaQyknjrY0WlmGy0Gi1T4hzMAqsOkb5Jf6dvLXb6rn7iUHInoqCg9f8IFZuK10jZD7lmj6nn0PRdjdTUsCWeSJv3farz7huTh9ig07rX_mL4zQeg5FFoaWFqo6OB5jTRAeojLhSxBtyU2nbF4WOjmfcDz2q0o6FnweVz5voSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euYvgO3roxG9QNU9qgYFx7Ks6lgx9UZWJVBdrI5_2KzdRLnFAz_0UXhXbG6tlrnGxaIWKyu_OMMOnlq7zYCHyaVHZXtYrZV7cqbkuLZmbljhSNYTnw_1X09-ANVd90ju4lr7--0L3ZUFL1yEQsoD39Gdrd_OwV68qlhdbq-7oBx7f8bs7MaQz352zyptE5XQjW7qaWZL8eS0XBmQZzn5f1rMB7BAV-oHMbzj5m3t-q8quw4jBh8knaNgDxY6aBV6JhrXBUYt09TvJixPyeXblcRsL6_duLmLPopgy409woCM4wxg6Dd1jI42Y6RfPxEqsc8LrkX99DmLWBBnvoYu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz3nM7xKxRZw3gUpZVjmmavVFt4EPtA9xY5h3NY3MCnVPxuBCqJ-psrZI9Pvz2vvA9GfUPvirrYRVc8iTQykddxJOab2aeJKtv7M2hZi8sWnGI0xjvt8lMskhBrKEr2FKMh5OelJ-QMMoyY2ws0KxxIQEt-i6LWZpKsqIbSxOdrQkz_cIEvhXXydE4S1cj8C1uYyoeQJaVYcHl-8-vBtxUoq5NQJzgTCRVc307_gaqR99kt18bsKMRYkyXZ6yaw1l6pWOp3xJxbqYXmCYFhixIqIIuZ7h7Um6luFy32916N2BQQeds5aYvglrIDWgMsDEldCTAcckj5vbOPR8hObDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgRLRUFyetIRzUp0c34LlWfaSKGO8YkBpWkxV_DcWh4Ste_bL7mH1r6JfiqQVRRQU-MBmf6rvIxTRPJkvkg7vk4BBCVgG3k4Z4mZ-lYuwvNoByXOZPHLx7VKfDfVg3VB5iviZi5mEtSMcRnTD-d3P_hNNrMteDO1HaQhxkKjx6Bjt7nfaQlDKHAaJlHuWmfX3ZxEWQbZwCuxDUJHshgdNbq5qxV8HdFFF0GcRCi--EtuZjfwyJekn0oXIzdDv3kXe8AvXhOPdKkpkV86My3rGk2RZczKMngVz8mxIJJGJEgs3UO_gXZoT5ZqoYxcubUaO_7uLmMb7r1gVUJe6TaGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe8xmJivXvGQGfa0-acS5AGDT4xC6iEpe6NPjUw-lvKr1qgBnmWUiYqoI2BBUSPnBq-x-i9lpDMYV0ZyrxXeEyYuKIY8WAqZJgRXkGP2YgGli5FIRRFzZWr_SIwUHPyBif_TnO6iviZmEOWWiFEXKxM_5YB-JPAH5QKwDNXU6xOhPXgiM2LhusDnUdkjg3FCRtUWnqfiHzGzVP5murRpVLmSx-UBYTzav3ZUZiD32QpxO97Jumcyer5qbFGYUEL-rzwD-W_pUkmJEzIZcc6LPpfSDmVC2Q7cVRpLJkD7T3NZ4Ls4BXuZ8ICezuok9AevNAimXKxXVhIGE94uV0S2SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=LE-ukvSQtXKIsO3u6vRVNjqdKnygoJepUocfxQDZ8Tsu7y99DM2Zr4jCUTCxcqICSzFQ970rk75Rx1Wtkhk2M9AlLBr0_Go59Fqhoj9q5VWvFit9DmD1aebO4DdtgYmGWMglZntWsJY3DKCw2ApbY3DAyh4KRCSgaK2Xp3VsmD_p9dKlIW4_ER5JF3i7RNKjR6T6UG8fVBxIq4k60yke4DslERpcbwsCSK-a6-his3oQMAJFEid_JAUVoHNrzeEA_aVpcuTu0oUdnwrbJPae6II5GgsarMrgeRidbtd4kAHldy-QTTOmmQMr6YZ1vNSCzTBdTEaSyr43kWeqtpTa6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=LE-ukvSQtXKIsO3u6vRVNjqdKnygoJepUocfxQDZ8Tsu7y99DM2Zr4jCUTCxcqICSzFQ970rk75Rx1Wtkhk2M9AlLBr0_Go59Fqhoj9q5VWvFit9DmD1aebO4DdtgYmGWMglZntWsJY3DKCw2ApbY3DAyh4KRCSgaK2Xp3VsmD_p9dKlIW4_ER5JF3i7RNKjR6T6UG8fVBxIq4k60yke4DslERpcbwsCSK-a6-his3oQMAJFEid_JAUVoHNrzeEA_aVpcuTu0oUdnwrbJPae6II5GgsarMrgeRidbtd4kAHldy-QTTOmmQMr6YZ1vNSCzTBdTEaSyr43kWeqtpTa6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
