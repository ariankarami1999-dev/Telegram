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
<img src="https://cdn4.telesco.pe/file/fZnbjiToV5ruyywVWxuEEifhIqMzYxKQ-Brh1J-UFdNg5l_aX25_ON8NG8Cpm3X8rl74khPXG_8jtuPbMHI9M08EPXJvMmZNscd6j2cMQfpcH7zfFKrLjeDG0idWkqvvOrCGqxe_x1WtVxnlIf4942A-QiG30OoVLAV8AHGC0_Kfb_BBni4PQ5aAYctNVJzptynPjHbVePTsM2rKIPOBjrCSVKqJc29x-LcBzgVsqmwOyIqZIvZf4xn_TL2Db2g1i_dxQEz3-O-puvWj3qXjl5IR9WZblGt9CeTF7TmRe0GqHYWTxaOrCe9z0H3PsrvnhkFh9hThLuatKbGULUdexw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بریم برا تریپل هتریک رونالدو</div>
<div class="tg-footer">👁️ 65 · <a href="https://t.me/funhiphop/78590" target="_blank">📅 20:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCbapY9jeNyXAglDhQTvmySWq80AAmEwVnfE14wEDUGVgYU_6dbfN2Xwb7Wqo2h_4iEd77FgbQTtyztrXI8CwPGa_ow8WxKYAaLXfVsqiSD02bbIB_7A6mJ7i5JqfsJjVIDiTuxCoqlM_pbO_qhcPlMS0aUCKVnZECGQKpkBEIlNAagKkwSp48Ek1S0g7Q1tLmL6XjJxByY2_C21mOEUxVDAwk1M4INj6e7ZYhRPelkUIK7CXSAB4nlud7WZTmwBelKq5vWWN4daB9lZoremLyxElr-up6bUUt9oHGSoAJUB0d6Q6WWYEeZhFs3WxTgVoH2wnExf7b9eykg12ENhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiLUCgzVbNmwGObEvRa1fDRLD5ZC-jCw3PoZoIRujytrUS4mog0WNvaunIaBpcA7KcbhV2Gwt1KFCaYi2QumvBSadaLCiX_8K_FHAozG6Df-x9jSW7jjYFumb2CYBAYvL9IyEz1pxsNJBXauc4v_Zg0DWlxu6AvsbbKJAV160HW0hqr0MaH_1DZ8Zj1ojLJOUCM3AUIWGtJbWHR2EAPSldmek2VrQ5l2RAu7GeIXkv7ERAck7HphmnnJ9ojbVgFv8EG55Av6kjL78Ujk-rRklSQYNWwKFAoL056Ghwz2KNtdYHU324f_ikjo4FH-fwgeDvw5PsojIu6N7tIAbgJOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jj7e9whDb2uBAhqXHMu6SKXS0XdpmrGMTFb57dgHf_QJ3_sxVh8JQgbm3rg2dbFImtEJW5oVZP4wG1ehJpOLBo4j7oFZggudlCDexu6GVei0vA1s8nL84Be31o38ybUyCWYxg-X01kPxHpLoh-YtRzYxwSIKVMI0W2u9gk782V3A6SQgD864FfK-kI9961P-C5xbH_uz1srgJ1j51NXY37sd6xLwjYjBQ_Je5YAM_T31hQmFmXmBDSYxyfV2tYvu4_PyDqLzoGfmaaTn2OhEr83328lmkJhiilDf9KumqSBV6Ri21kV3VFOXKTCF5wzCfbDU9NDZxoZs2jXEeF279g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EORmPVkymle8KlkCK8H3cYKpQ0lXg4QVVFqmyKule1AIfX3wFRdwvz3x5__hUhlf9Y863mPnfXCDhwBtuz-WikXznB-aN0xEGz0ESY2fxJ75tQKLnG8GgmXXB-TJUf3zzj6385mUbvAb4u3PB0pef85M5B76Ijj-Wx1UnJQ4K9Yh3nXXUEj46uXaOdvXqc0_kS_0TxM8gjcMfE87iquHpJoA0HkzeSIAYjOI4vaUjlo9gS7O3M1ffBWslW1ZA6qfHZln5lntXlVjxsf8jCozhqyeH222hr0n9ar87MrrIGyxM-LQnS5hyXWQqdMIWSnbNrGT-R7Jj_nSiptbfHYvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EORmPVkymle8KlkCK8H3cYKpQ0lXg4QVVFqmyKule1AIfX3wFRdwvz3x5__hUhlf9Y863mPnfXCDhwBtuz-WikXznB-aN0xEGz0ESY2fxJ75tQKLnG8GgmXXB-TJUf3zzj6385mUbvAb4u3PB0pef85M5B76Ijj-Wx1UnJQ4K9Yh3nXXUEj46uXaOdvXqc0_kS_0TxM8gjcMfE87iquHpJoA0HkzeSIAYjOI4vaUjlo9gS7O3M1ffBWslW1ZA6qfHZln5lntXlVjxsf8jCozhqyeH222hr0n9ar87MrrIGyxM-LQnS5hyXWQqdMIWSnbNrGT-R7Jj_nSiptbfHYvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo-uU4ZvU1PNTcTNzbMfqGZ8lUN2vnQrnlfzIU6H02z1U2xOPMHGbC66YBiIbH8GdlE6KhQ1Zi2qw46DGQispCGC76L6a81bQnc_BdiGH_UEIA1vsLDUY-Ll3sl2UxstskeP2U4aHrJyQYlBG0nnx4pEUJnhi2zF9N6sWiyz03tXsO9kcnKklZ-TVFtJYSdohi4tHkLsx3sLmcRl7nam5ONEI1yMZvgLOEAf71IOaALigae12XCD8EkxwcX_SFfpHSzqXY7qSrW8Sgra3mFE5MX16lRL0xvHR_oXj0EhxElOposqwXTeDW82VaYa_Ghudv8W90D_0XKwKU1LbwICUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
🅰
g2
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/78579" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR2kUV8PdPwo-sK61EJhn2uxtK7A6CDylq_tXpnbgHSn3lTvDvoLKWwh8AQsH1wtzZVJ0WQARlOdHxbkoB9S3CjkLfb9t6G2dUSldXf83YgREl2SKLMGKxFuu_3A44jfNPprf46p1eMkmUjpgYPh5AdD_jihZK13t1iEmP7TBX-Npqg3NzmNq1pHSMjYj07tLpkFOQwuDXqHSaLmkiuQsDAc4ZOLBXsCYA0mAMOwhYFKK5MTsfhjxXvyEVUmxsFbKgXXzFn0lMPdfnAEBId63BRI1JFuzZ_0-zNviJcn4qo2ZtgA3TTMJkMAjXz5N22okD_nmDzNaMMOL41mbDZtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFOg0iKY1yl1WQznvKc7ILDMcA7q7DgZmXMRVKJv9MS7-RxXeZrJMX4gJ5W_Ay--0Xtj-FF9FOQH0PfYeDSCG-CHSSh7ZJ8vI4U5MZwkwZBkEnb19lRVdTVQO0GelgoyIpcYglU2R4ZI4nyUZzmv6-Bn0E_s96utSWkSvQYpVObFSwsE9MnRbNOkjawjSUjKqCbzHAta4VfsZ_q44x7QFR3_v8WgabWu4EFttOC7v2v4_yQmMMnBSCBtWqzP_54koIya4UNhFCwSZFtrtjIWKiHGBFsclJaIOslfNkZ2Ys1Pm_jmj5Vupzk8Ri25YG_kWVDR0ofn_LTklUnIezAGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8qVhFVNrp07JfXpNG4V3hFY_bnRKtDYpJa9g9kN9Opmvkqq0MO7DZAoe6BOX68no69TYdCu28uzHyZ_AWJRG3VHN2m7lYIAFCb-DXC8nTf5mkFCykvPRVfv36Rtwf_VFrqRWt-1Yt6gDwB3qbBKcBqKcVboldAp9EfGcomG9lvqELabAjUgo7Rv9Euy1XiOfTGXMIs9CnvFlnd7xE3DWr-mMb5nJcsq38Nk9HedXobHanFqF_YtEdHCbDwzfVmFSWQgq-aKBlELAEmHIVCkP3M2rOwfsVGoRjzBqTA5USLQDC42ZJQG5EHCKoJBhWXKoiz94_zkDYXltPXovOx5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbB4gukqBz3hf75XI730WPdgEWQP9tlOZgzmou6Yp0o_hBwkTsr4AAolzUh4hjPmzbxrf2vSLdv96jgfI6MuYAFfA9RDtmUQ3d8txwc-PcJ7GWXScn_SMCH8uT_Q0-0UvsJCSEhIIitmnW0mxNJzCax0pEFHC_3Tw0xggIqxlX_zonKRQy7UmIfwr2zaciEEg-DXua-R08URG8-4dWUmEWNogZ3OBA72HRg26msINSunXQ55WNS28h_I9ZYLRUHXuuUurDubGil2RfXT7o2BNc9r20a67O9xw-9NK0O5-ZwQGozyarAEpyHiWSVKPjFfFN7HH1L2MLzp-1HtIv1bUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht4V4Q_LJx9ZkUPfZG_FvMb9G6ZHqCciu9dIbwNNNBzanUD1GMWMWWc5jm-i8l5coe3f3pDqESgQM2o402GGBkAIqvKHs63KEW0zMbHeQAagqL0V9okGXpq0bgDYtN07PLCHkb7Sh-qt2u6kh9PdEbKpLzPfy7xEDD98PegzCMachgyu9WLlrc145RYuQW4hUiijdYfzJjfwCVMP3p5JUDaeMzmoOFnDntSC6AJyxbWQ8urQt6otcNB4TKSvsVUhvAVnbi2Fp3pBHsacwa8qA5a6PgVg_CiUp-biscvXy8eXgwXoyqNATh_kXyaC4-WTDiCz0fP146lipZb1uICiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA5SL9N0uazfDfEr8JoepLRaVunyyLeNr-ByvEkNY0u--q654Xb0SE6w1evUrU0ZSZ7260aY9z4zwvxMnwqMD_PjoK5llO39D0U8S9_OzPUXAYFn9xVD4f1MonNEAfmzsdO3x2mUrcJCbL_2V2kO7B-l3eobHsVmR-oonz7SbBVsj05sEY5ovgz96DNm1uR09HKPB6L6e1t70vexGmd9zBwk1NWRszs3qID8xF38R2YnVZYWvwVUrZGKOMJMO5_Zj_0P2vg2BlkwfCmXiSLahAeyQbBZnIQpTh4Fircu1HfcnEAZd2WCV1Qv0HAgNOF4nC74VyTgq6Qv-4HHqhFBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwkhhOdMTzJG5-MyHafYX_CJ_QTxFyk4ETjejv4GKUTPP-U4wCjQG5EJ8npZlWr0MvFZ6pQMs9TtFfGxGAgjSMhNlLba5NPjF_C8zvxSwQrddiTNFzMhTlNVyB83UJorZKuura0dliS_gTZEv56Ao6cztwkESXkyaT27yS_8fttSmlLXP_9UsPLxauDIA5niDGX3r35JkcL6ld2jGn4W6lhLdFPj4KH6CVWcROsf4udu9qUcA7r0bAo5fikoMNLhOKUJjgeah2yZz3rl3wPAicKX130zrwj7qv93yITQe2Nx0Uoi53FHc8sbtasqR6TUcdk8ATqZICie3o3Z2I7gLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgVA0gxluxbj1l6-6DoUX7Exz9pWrbHMzz6QZKI-fKOGnyOzEyc4uFtfbGBS7GjAJlCydSp-FXteHjHZM13e70ek_Gs4hGFOkZLfriKD8TDhX8VBb7g6AvwhmsvLksdv7VXcdJ9hB6QPcIeo_zzIavyE30WkKboWowXhL_EV3lyr55X3WCQ1G-_R-8SFt3MBsuFnPbKqIefr2GSC0vGmlpK9P_u4gXN87KpBhNg9If7tQx5HmPmIcReXFW67xsDBXHtB_EhGfEd2Nl-2vQCHvtFhWM5j9f0oSXsGUM3T8t7T4DJL149tljSKLyDgwuvJvM82LIYDTq3LyIKRBU6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW0hnzBUINq0C6Lmw8KGV3MNFHrWqEGFSI1aeXubWkRdeqHR3SJO01IZ_006caTh1BAPaHjh4Nd4NPZKdxbAaB2U5jc2tsBN9-Pu2QDQgbsLDjfILq5p92aNkls4ja6HiiG5ALsu3aaXr357QRM2urzKc450iQvolBcEVkOvvmi9Xl1SNwIpH8D0ogmYn8rm6SI1wxPpSSGTryD_pFJDU_O_xJsYCjBCsGXfUzWrO0494KXfV4qPXrRTx5qoenJ-bwT3h6gXjxIoNSVTw5NIBqurM345mCbJUui25jkQKHRoa-AMbEyGI0cxacJgFDfd7e2sc0P80idf7VK_jxIxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehc5uFF85238ZCGL9wL03FeAX7gqzt-_wOIRyxi0HZ_Lxdjv5KxAX1H_rBf0HWv_S5pJ0u_0XXu3e4S-8AeRBcM7WUx5wAw_GKT8TbeMY8hSyalvCoeaCCTKNi-xVCo7Z3R7sXngZ6ifedDHKZ2XMt0pfmyDgYGvwWFWFQTntVjFz91Zu4LAkOBJZIxmleakOg7wwbkriPeXAGiZFHAhNGE2X_MMBgia5mmAhqpubxGA6JCez4WUAfFtD2O2tdvI6G4j6-qpDi_HgIU7Z6JEcEKZHDoE5Wt9GW6ENFpctC4rd7Hl6eNt4lwBobP8QIEtS4Yg2dojznG_oFNrcvbsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/j20ZnpvuXD6YaxBlNfTwkrCnGSF6EF9naWDz8iAY4GqxV9hM7YJSuzkiHYr1otyHHuaH23Lx2KVXzPkte4ckv77mxDssoEMwm4bXgMMuKq_2F7WCHchU31oWXbjGplsrZ9Rk8pWWAZnh_V73ZqzF7yj3wqHC101-vnGA7B0svxKtoRT4bTMfAq6jiCVmk7wcwd4W4PF932Vt0kUz9nca6ObQ1HEbSV0V4jQ8XfudZBM53lV1LMGCTvuAp_Vr9rklBId8SYisekyhDpK-t1fUilv6cQPidPvEDVvbcvgIP-6biYIj5eK61Jv9ukyHUnnHZHfz-sDtZR922MNAnB9Q9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78547" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7u_n6CojODdpbmsiwW1WwEvAm1UpJWReG6Hmt72zakTifPFmzJ28Re1zchzJbjeEFIxKjhrg6BRHj82LTe2N3w77ec173fmHJYxPcxzL-RAC-XTXtYRAOx_nQ_8eL-Ufrro3yfNfLUyrHKTxqCkkO93abbmRR9A-396zm5OcpIbEwBp81JAT_fSRnWgw0L6S1NIBRX_A-RqeN9JbFToWKzSBdzYC7k53Q2AFcmT82_TGBDlXddCMfXspo4cgDgC9pEX8Cu3W-OGg0ZRnrd1dGNRkl5LK310PQRvlUT45cXYzVwI-_IJCDvl6Ek7HeZtc9DxDzD8_09jRaUbLHJisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
R2
🅰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78546" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKbzVGquxjql8omBAlciUk35uoayiQIKnpw_Zz73_qPVUDDr7tI_SNwhdNQNIA3E546mQ8GCUUBWT1RN5o3pUUmqukir9GaISFH4i2K85rVSznkpvPis0DXlP4Z-4OmrwFRkp93FYXe414Nz4W3U77OWv2gsNuTLSqrVOKiW5LJX3t5XKWvZYZmxIQtAAGQMy73N4ibyy2gprwbqQdW779lWw8S5IpEJwAR7fFMRYsc2R_q3g8UQSWtdA3QqS1hV1pDECgikJaxeCf9OT1aY8Q6F2jf_kSskV5vZTGY_i_WQt0O5lx1-0rmOkUKBBjPrD3M8HPBweIxIN4Ye1Ahdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BitzlMiX4B9G0EAxuMnEtaJY_efwI1A5RWgjvs5RAkH0eDZspNXLBdSXMTz7rIUZmv0Hl2RTCqNinOzWL_AfqiQQGrN8pI0TGjYVj8s30EBy41PlryLYILOspPaKHByoFZFLgJXj3Y0v8yzAfhJ-DjL8gz0ddW0t5sx21_z08L52X5W4u9B9MiZLEPJjX093Pu41hadvr7Wcy8ZYClkUrJNd0hA5NUaJ-dm2zyuawEdBrJr7QEC8dkfuvctf8B3cXKqumEJ8aba4k_cpcpHCmqVQgBCw0J3CAY0XFskK4yn7dh9J9XgnHdPVow7BDhz9-6-JSZ9Utt_KVCnR5sEO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flfFnVJ6FRuPoAD8lWNJRaRjvYJgsHHoS_1OUZ6rYxyzwxWoPWvzlpaguytTh_ylH2-3-OjjkXzog7p3Xdnava0_o8NA9qHyDaFeaWZL0UvNiMM8LrB67xuy5RyxKMcVo9Ylf4op81AlTunEUYKFxQeGMPJ2vyJ4E1ivAd-Gaxf4BMcvDFeTlCk1txd-nN9QH62tlvOTHzVMJphtBmiHwpLGkt8YiKE7u-4vvvys-568PRGxDQeh1kZqqrwdEHTKnnttzF3rgFd5SJ88qdMC8jAIZ0O0tcjRDueLNsvXADYLCdXkWmBK4j8UMz0Wmb758pumBAHtV8kqZMNNP547-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی رئال اولیسه رو بگیره کون بارسا تا چندسال پارس
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78542" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بعد اون همه کارزار گذاشتن و اعتراضات دانش‌آموزان پایه یازدهم و دوازدهم، آموزش پرورش امروز گفت حتی یک روز هم امتحانات نهایی رو عقب نمیندازیم و سر تایمش شروع می‌شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78541" target="_blank">📅 10:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛ یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78540" target="_blank">📅 10:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=obq9EB0pVKQCuddQFgo_wRd8U6TRyFIj_QLmQyX6XMk98ylOcI9jjk5009nDSS42kTudAvIo_tbU_pT8RpOy041khyMLs4JNZgS7qLj0Bdqd0dNU2skCR1PgLLxcgSeCMxe_lx84sTE1lAiamRcRFuuI6DZZ4BfbajLx_WW8cW312uL2uTQBPKzq1CorRAPoxhRkalSAuoKbguks-sU6lPrzteSXr8m2RGAQQqOQWiuWNfrs-FodaWa7U7v4wMW0nHIKtC7rLTZMGgXscjg5BTCQIPLkQYuVdj10N8pleTbAfSGOvhgJQKiMbHdOUlPNM1Ne1XMB5t-my8uuP1eK0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=obq9EB0pVKQCuddQFgo_wRd8U6TRyFIj_QLmQyX6XMk98ylOcI9jjk5009nDSS42kTudAvIo_tbU_pT8RpOy041khyMLs4JNZgS7qLj0Bdqd0dNU2skCR1PgLLxcgSeCMxe_lx84sTE1lAiamRcRFuuI6DZZ4BfbajLx_WW8cW312uL2uTQBPKzq1CorRAPoxhRkalSAuoKbguks-sU6lPrzteSXr8m2RGAQQqOQWiuWNfrs-FodaWa7U7v4wMW0nHIKtC7rLTZMGgXscjg5BTCQIPLkQYuVdj10N8pleTbAfSGOvhgJQKiMbHdOUlPNM1Ne1XMB5t-my8uuP1eK0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛
یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی
یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78539" target="_blank">📅 09:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=t0GcCdhufM7MIpSFSmnoP06fNbwxGa3Drdtnl7O7ZYCKuxuwgWzPW4iWPWNyr1eJCeMjLSZaUhNyLuGt0XIXBXaKkX0JVzXIoCC2wRGtOIOnscX3bFbpNpmBIMw1TEoPHTcHVyhyIGRIoOAvvfacYYm-pyVv9cGrF7WG7ultf1Xhf5wJsPzuoV0i2W7q522Gzqd2qrQT2HYScwsFS6oC1CLndHun8Hx5tDqk_zbxP3bvLkcQylVwrP0xXlmYS7sG5W_lpr3GEPKSTPv_7a-u1jMT3k0AkspSFlLMz0fHgT1m3Lo3UBfiTjTHS7THXaiOLfMA35QQ4B8RWKoYc6RmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=t0GcCdhufM7MIpSFSmnoP06fNbwxGa3Drdtnl7O7ZYCKuxuwgWzPW4iWPWNyr1eJCeMjLSZaUhNyLuGt0XIXBXaKkX0JVzXIoCC2wRGtOIOnscX3bFbpNpmBIMw1TEoPHTcHVyhyIGRIoOAvvfacYYm-pyVv9cGrF7WG7ultf1Xhf5wJsPzuoV0i2W7q522Gzqd2qrQT2HYScwsFS6oC1CLndHun8Hx5tDqk_zbxP3bvLkcQylVwrP0xXlmYS7sG5W_lpr3GEPKSTPv_7a-u1jMT3k0AkspSFlLMz0fHgT1m3Lo3UBfiTjTHS7THXaiOLfMA35QQ4B8RWKoYc6RmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJl5nV4dyto28rRJm4KCIkpmYu9aH-k9_F4U9RMIxd8mu-a3ijKbmjliTyxX4VgFpFfcKmXG3QQ5qoYX4uzcbujMMPyxKXTQSp7EHsO8pJY3D7UVH8v7LROLRBdszHeDR2HXdNM8L3WVeH2aQxTtrjQmVBThB8KTyl_ZJKI-3m8V9mxvJplx_umnYekiWAPxdNNFJRh3KZ2rcbr2CnrtGimUUlJXw2zHT21BIHRUwLUqwVV2MoX0QpfM0fbRtoRnYwJRWuu7BYjPRrzMQoR6XuRG6UMb_rLzqKlPdFJ4tRA0GdO4aQ7BGCNnGWb-NSjoQoXistWIMM7HvdetuNISGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امباپه احتمال زیاد موقع پایان کریرش بهترین بازیکن تاریخ جام های جهانی باشه جلوتر از پله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78532" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کصکشا اینارو من ۴ سال پیش دیدم، چیز جدید ارائه بدید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78531" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امباپه چی زد خارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFdVkNW3LmuAFYl88uX5DDQ-kc0frnWJmc8yZ3nVAQRgSZZKxqyq1qg9zmqmCw94mRS68OCMuMFVg9C-vWOPIqF97CKbYHNpHOZ8bMZr3p9R1HuJuYw5ATOPyc2iV6Es_Q4JpdxgCJ4xOiu8QmeV60tBcrghxfBrVckeFzCgimCgEAhGCNgOiNITnOcFyXF_1CCXtC5a_ocTFDKBOueeSzNR4DRB46I7FNFlvxshZTa84c6EQqDDA95tZUFWQyXM9oiBRUJDkRCl46B_c7F2JOId8b4S_j0ZuZ_HXY4faysSes1Tk5iLd3pd-xxZKib1WLhiuVeQPz_KjSxe-Zmf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دالگخیز:
پسفردا به ناتو اتک دادن کیرمم نیس چون زمانی که ما به ایران حمله کردیم کیرشونم نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78527" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=APavB_LjNuJmk8y90liKl-8vqFwF1Yt-0yV8dwhHMBVVLkFThv6ZEqXF_Yq-sM2bxH7U1aTUuYVNXVAb-xQS0hJweP9dMmruTMybtaCwJAkkv6kWB4pCFjNF6EblhTSRuhe4Iz3WfuF-L3lOL9ImBU8spG8tiVwlk_-FfS1Ln46F5a7TSgle8mFa1-xC-wazuOomh0r-IzUYZ3Jget-cRPaJMyOe11EyLrIpe9jmFtccYG24ZmHSk0RXUYcpSjkGTlIn6OOsDyOuUSjl13npCKept-RVRNMcBAqFvVN5diRIpilZ4xAKwuhg_yjVG1ZVYFJlxzOsy5TEo94HY9Gm2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=APavB_LjNuJmk8y90liKl-8vqFwF1Yt-0yV8dwhHMBVVLkFThv6ZEqXF_Yq-sM2bxH7U1aTUuYVNXVAb-xQS0hJweP9dMmruTMybtaCwJAkkv6kWB4pCFjNF6EblhTSRuhe4Iz3WfuF-L3lOL9ImBU8spG8tiVwlk_-FfS1Ln46F5a7TSgle8mFa1-xC-wazuOomh0r-IzUYZ3Jget-cRPaJMyOe11EyLrIpe9jmFtccYG24ZmHSk0RXUYcpSjkGTlIn6OOsDyOuUSjl13npCKept-RVRNMcBAqFvVN5diRIpilZ4xAKwuhg_yjVG1ZVYFJlxzOsy5TEo94HY9Gm2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناکیا چیه دیگه کیرم دهنت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78526" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه این جمهوری اسلامیه از آمریکا مواد غذایی میگیره میده دست بابک زنجانی که صادر کنه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78525" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: دارایی‌های آزاد شده نزد ایران برای خرید مواد غذایی از کشاورزان ما استفاده خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78523" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMKozlBVZ6m2NwBPWP_WM9HKVLBZp7MIYvGm84CD9NTCGC7sY-DOjS2Zs4If6EBiVrAuegm1ky_rbe7PaxbWbLeAuWbetXoUb4ESnF7bxyiK0VPm3dI-wQsXx39KF_wix4m1PimFd_c15uVJ8xjDokcUwt-3pU45zyL-WcZUTrjgD4OQmGydfSzQ4Qt7lGpfJrYP2lk0upJ89YDYkCLoUVZ23iztV7lcD6qwbU6L7aigtAclvEelJv12ghvbrRnd9T-FQoKo9BiBspP0wW5a5GA4zWiSjtmWuPPfToxuSXa-p6fUagOhmBmt4Zr1nf7E8wIWZm0fLuOTk_L9QrL3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKlX8YwOG6a8pxioI0B-VHsgZlsyLIpEddAuSJY4k0cHhLCCktzSpQgWqnMYSapW5yMZ1blKIxDxXHM_QEZTVTeakPQw3rs7vE6uQy5GCTAdBxjRUYnrM0ZjSgRDJWD5lcyTOs5x5y3W6O3UQAGsvfQeezRrTf9yiCXtZdk3qjVlNq1gxf2MBr5StuHiMhefVFE9pfYOeSo02Z_b33bPeBJgaHeAwmklDF-Uze-7M1aSDKJ4o9OrVDMZPN239A1tURvVy-22ClccvOWiouIv0ORfiVilgqfSPJNYVfqTQTwp5-3sEN4gWNSHcQMhX-k_jihiZWv961_Nf-3vycFdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/va7Su0Pc5WGf66gC2_77YP6VwwC-DYw6eDDb9puLhQIonJhVJBrMv0Fs_LsOoVHM5p8wrtoE_aXef2AfkYo-AnM8fZNTHNjcM73jezXuf5ziQJuBMZ1W9mi1zNpvcJT1Io9umtTaACzPTBsR_HF7j_7VAOSpsavg6D1qP2jqlayALZmp9on-uoXIsRC5fAaY30yja4A5mJEWHSVhDW80_e1JFsRM2LELIor1sNPiUEK6nkkQ75dkR5WK2yfXwX91KsG_l94MsFJKM3cJHl_sMDycqk5hN3hXIovUxDXWPeFKkoCIQnWjQbNmuqAIFMZKFeozWJITXY-2UoSgapZocw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78517" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خداوندا سپاسگزارم در دوره ای زندگی میکنیم که سعادت دیدن بازی اسطوره بی چون و چرای ورزش جهان را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78514" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رونالدو فقط و فقط ۹ تا گل فاصله داره تا آقای گل جام های جهانی بشه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78509" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">متاسفانه نیمه اول تموم شد و قراره به مدت ۱۵ دقیقه از تماشای بازی خداوند اصلی فوتبال محروم بشیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0N7Dte6jdCGZkILmINtpDO1sfH9tcN6QEyp0mjBBr8fA_3fvaLgNMPMcP-a3LNDwOwqnfDq14mkIv3Tvs68MNZ36NH3Je9FEAVoqw4m0pPtb8Nn8OW3ji2WV64IJP8UIEp9vvqAWWgBWLquurKPe0NtvBBu_sFk0isjsZ-nAUJucxWEaM9gwoTDZPkEI6AeCWjBqcWkmQhGtZc0tUjhkvWRClIiZSTdTR0ZbUBAKv6cWJ7mm5-OxGDJE23mo1aDgLO5HUwlfxlGSRMqJp2fHwl9b6ul6zYak63a0iKcx8WWadiD5vuzLN9PLoIDC09UphXkAabtNXhflyb_07-7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Hqt4yOWqt-A5ZntjhClGv6sop9HHi7mRE17av5K2WkTDXVaB-Tk1IsuSPhhTqH0MX5X3BdZhJmg3PM6uyLCcHR83TDuwO6SSoYswEfHB3El-CB5YTuAJwTXDQ5_n8dK6FCeOFDoovc5Ft4HseKDwlFm7-AX3sX2u1SXCQYTrC49BmlssQTkYTLHkupdmLFYDBnZ-nzYkQtQukDHVqTzjd0C7xa77EUnGKyEvcqdEkkFFidnku5Soxwvu9vAxiTIlnRRyMXSBJtfjZyJz8S3eIB7RnJULCFsz76ZThlg4YsQ_uEC_6bsO-zJ-1P8n7Vo2Mjt0CGZATFCoFzJ1Eabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78506" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رکورد کلوزه شکسته شد
سر تعظیم فرود میاوریم به احترام لیونل آندرس مسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78505" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رونالدو اینو میرید رسانه ها عزیزاشو میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78500" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پشمام
چی گرفت بیرانوند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78498" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وقتشه پرتغال یه ستاره بزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78497" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نویسنده کتاب تاریخ فوتبال اوانس داد و پنالتی رو زد بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjVahuqMnt4NbViamjO-WoxJLKY0UdHWkEVbIdfxQ7MA62yHlaiCdV80EAxH0JiMLAsXNvV2geBah8iYVRvqU2kGctO7Rx4dD0W4D9JYrnGXHzXD51Ln94jPSXhA4zZqsAsPGFoReJg8FrPB9tlUgsSCJNQ3ZG_-R1yiNIEhmwHIEgju6SBOBbV7GUelds9LVccopqk74en_giGOrLJCN8iJ2qPsyTWtWX6MYexueGawo7Yps3fLmRrJ9f4G8SvZxNFwwidZZ91ArkkdQ3_mo_tg2c-xJL3ZURXLFKIce9uO_4b39xfQ-MQDVy8d7iondYtIeQYYsV9lNTJw6GQAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=oYmIhjQlNzLWKjerRbCmuPouOMUAqSNGLogvnSDMhttJG-IU_clbzqFRuxdGyd5KS15M9zxRYn-zhDIYaXsL5G4yzVXXXSoR9tGGPz6IM3U-LxCUKP362RI1Ba_2WFiW10AlOBFoVa74Rp4oipG7CNR2Smv4FozbjPmVCnEEbca8PHxhSRpKpgykvfmojiJ8NsjSJ0Kz4KJ9iAlg3hzKXTUFQ9eSN9DM6I0hKNz5pGzgtZiqN_OdS_UA45v1ovR7WsX2OPymlWukOG_Vfk388-C3cwvBeIEcIk3BQ77d9S-Y0VfzSUFHodYlmTwa-06Vwa9ionP6G-NGbXNkU-5SwgdX4towM-kUD9X4M_OSWbs0DxgzUhKIrt4mxK_UWG4kIp2s7Kp7yFM0a1R2f_YvNGKNiHAIV4hUKXQdChnmECV260t_6TUvE9Md5WuKdBDUeFWJrV1NyiJo2Kn9zvp9pBOrjHB7j6t0xMLrHxicDbWOEc8UQX_IOOkELFZSNGdIr3eSiOEIuLi66Czbm8z33J1dZq4j8AHzncxz8dC_5t5hO6X4xZOVUmYg-Ig8a_8-mET4yvXaTPWEHmNKApW44WvulDaxUsQzgfvFewaSggBZIXYlMuXQJ6_8ShyeZ833j5sQPe5G4H0-7jbIBJg3GE-U9T-bJKpKCY6p9rbSAMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=oYmIhjQlNzLWKjerRbCmuPouOMUAqSNGLogvnSDMhttJG-IU_clbzqFRuxdGyd5KS15M9zxRYn-zhDIYaXsL5G4yzVXXXSoR9tGGPz6IM3U-LxCUKP362RI1Ba_2WFiW10AlOBFoVa74Rp4oipG7CNR2Smv4FozbjPmVCnEEbca8PHxhSRpKpgykvfmojiJ8NsjSJ0Kz4KJ9iAlg3hzKXTUFQ9eSN9DM6I0hKNz5pGzgtZiqN_OdS_UA45v1ovR7WsX2OPymlWukOG_Vfk388-C3cwvBeIEcIk3BQ77d9S-Y0VfzSUFHodYlmTwa-06Vwa9ionP6G-NGbXNkU-5SwgdX4towM-kUD9X4M_OSWbs0DxgzUhKIrt4mxK_UWG4kIp2s7Kp7yFM0a1R2f_YvNGKNiHAIV4hUKXQdChnmECV260t_6TUvE9Md5WuKdBDUeFWJrV1NyiJo2Kn9zvp9pBOrjHB7j6t0xMLrHxicDbWOEc8UQX_IOOkELFZSNGdIr3eSiOEIuLi66Czbm8z33J1dZq4j8AHzncxz8dC_5t5hO6X4xZOVUmYg-Ig8a_8-mET4yvXaTPWEHmNKApW44WvulDaxUsQzgfvFewaSggBZIXYlMuXQJ6_8ShyeZ833j5sQPe5G4H0-7jbIBJg3GE-U9T-bJKpKCY6p9rbSAMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس علوم غریبه و جادوگری در شبکه ۱۴ اسرائیل:
دلیل اینکه یهو رفتارای ترامپ ۱۸۰ تغییر کرده اینه که ایرانیا با استفاده از یه سلاح الکترومغناطیسی با فرکانس پایین که توسط ایران و روسیه و کره شمالی ساخته شده، مغز ترامپ رو دستکاری کردن و این افکار مذاکره و امتیاز زیاد دادن و اینا رو تو ذهنش کاشتن؛
از منم خواسته شده که مغز نداشته‌ی ترامپ رو به حالت عادی برگردونم، منم دارم تمام تلاشم رو می‌کنم خواهیم دید چه خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78491" target="_blank">📅 20:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایموند داداش این چه کاری بود کردی</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78490" target="_blank">📅 20:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNOMlezqCB_oiSqddlHCR5UKaI29S89VYtWIa6MddC4SHSlrcxuw-T5d_dXQ2jWYp6W-LVWqGyMcRIEuEjEZ1zQKnGblTcw_PO0Pg0n7X2Xhi96T-vLO7O8cYxDAW41CBouvDl5XJMA6GMF-bpqtUTKb70cInj_6hpnU4br-heT2ZHpbG_yc7iWZpvho_gVJAJMkNtPpEifBKrvu5LbaLzdi8M_Jc5cEnP2qsVOkVT_pBSpziiNL8oXBsqA_QMqaRyjMyqvNEQZTBMDBTyEKLgAk2TmY3aKjM6YgKQrkYTHi5t7N1gbajzd-EFc8K9zxlbOSPIyGSgwFnuBf8iUjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد سوارز جوان شد
بازیکن جدید لینک شده به بارسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78489" target="_blank">📅 18:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78488" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78487" target="_blank">📅 18:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حصین زنشو طلاق داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78485" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW6RvZgk51hKtG4ZfHn2foBZS8JvLJam2zxU4qDw7PiakRBNSI_tlxbpXp2HRSChIipcNMU8GSqA60SCE_4Z1N6XCEkfq0S4itJ7y1TUXMXx_ozxpBzz4T3-cp8xS8P9KzQ5WfoPiHbdr8MK527Q_eD7-d4U-nmpZZ5z6HVkPEZbSJpfnwpQkBem2Sq0GzP610kZXVto6NpICd5zf5Uxw5zLLR1lDVF886xEtIox4BQ_wLey6uQChxdFc0fN_Yxz4fQy2dxAR8ewmHad4BIxQM8h743n1rlWOvQfNx5dgtDZ3QX4lt2kq-F1nA69Ml5oECUxwNUzB-AyKb9phMnPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمونیم ترکیب دیشب ژنرال جلو بلژیک چقد هجومی بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78484" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78483" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ2j5jRUxGhLnU6lH1rcoak_OKiTktcKV8ch1YY-1XK4oLZvXqnYyCQwdViGRhvzO6gOB-YVmYatyHS2An02YXMFAxoQXlkYNXMN9ovdCUZWEpiZebC0Ymu3LAgNcGojoUDzKX9digQDrX31jH3jFQLbry5sDYMFiSpxUMTuIPNTURi2QYi5N0KX_9s1VAqT-y4jWWNp7GbM9Npa7Hc1IUAHfURza0ukngCV77q9vyWQ0UCqMWVJm5PvDEqvFUM5qSDaSZx51etnGv_RdzoOvBQPDWktxCUaCW74LAUGfTsyOTcG3O58_GpZeEgBoyjrt5KDxmtPActjBFUJA2UW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
G1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78482" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رفیقم زنگ زده میگه ضریب عراق جلو فرانسه خوبه ها
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78480" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=cMCaL3M2kfj9BdYvOu6HJCJfiQWTxBgAEZuERmb-b-voLM3bRHeL-pkyljqeKSQp0m2wx1Awhq8Lk1UXQ-Gyw8_J_AHVssfC2kWjm4AP5YKw22JlkQwowgTYPCqTE9a-wcalTZFPQZMmJXEjs78WzHY-4qFy9Dz45yzNPPWnpxmFlBx-PHrr8SzVdtcESXijvgW-FLpqsicJgHNb2ltnyF0EvXTt_RXaZScq34i0ICAh4XA7Oretjnr-4vIPssG6cKehFZAXaWQsOtVCSpF7whAEpcUXUR6hswieTwdyN_2uLc_tiXnmfU98wTazoZfKjFOsOWoghJIglt75bzs-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=cMCaL3M2kfj9BdYvOu6HJCJfiQWTxBgAEZuERmb-b-voLM3bRHeL-pkyljqeKSQp0m2wx1Awhq8Lk1UXQ-Gyw8_J_AHVssfC2kWjm4AP5YKw22JlkQwowgTYPCqTE9a-wcalTZFPQZMmJXEjs78WzHY-4qFy9Dz45yzNPPWnpxmFlBx-PHrr8SzVdtcESXijvgW-FLpqsicJgHNb2ltnyF0EvXTt_RXaZScq34i0ICAh4XA7Oretjnr-4vIPssG6cKehFZAXaWQsOtVCSpF7whAEpcUXUR6hswieTwdyN_2uLc_tiXnmfU98wTazoZfKjFOsOWoghJIglt75bzs-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78479" target="_blank">📅 16:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برنامه ابوطالب فقط اون تیکه هاییش که اینستا میزارن جالبه، بقیشو ندیدید هم ندیدید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78478" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کورتوا حسین کنعانی رو فالو کرده، احتمالا بمب 150 میلیون تومنی پرز کنعانی باشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78477" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پشه مادرجنده مگه قرار نبود فقط شبا نیش بزنی</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78476" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj32lBUgQEzIYMsbXbAjeVcJSrrl46paACdUACZHjlWv4BrE1CRQJcdBOLl7Y8ZHimg6B82oV-FfJrZ-N6ZqhjsHKwDNbKWgc5eNCvEq6liTcNvwokoIPdeca4P4F8on3LWZYtjSBXeF2sTP31_KJTA27pb-p41fQjbF9UuC50l5sPRE6ulmCC9fn9usADaSoGAY7pbgdpHSSGhk7ZAszJjmnvEX6gMkaOoRfgISvXuQECRoRr8YQnjD2f6vEQKI__kQ3I605aCJEjDU8yQIVs-YYTlVodeJsqKddKCRUtOl7eIc7CmNqVoe5Smc6c4paTFOxUyrxFCVKyrZ-6EWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا اینطوری قانع نشده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78475" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تو جام‌جهانی فقط در صورتی که دستشونو بگیرن تو دهنشون فحش بدن اخراج میشن؟ یعنی حالت عادی بگن کص ننت هیچی نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78474" target="_blank">📅 14:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLbjXGAw7G0DO8ZsyXFKvV3o39pKuaE1zcq9yK4z0x7esZyKC4jv6GIg4vNEI07ky_udBS3H_r-b1i_WySu8Pc9AYSTJy0ko8j6poogyal2xDbDS9exLp5vuxXTJDu4KvFSJ1tWGT5r95M9atkmxp5CTBrPYoCVAIs4cUGgAD9U5E3-_iQN4GKuZGDNV9FS5YJ13s4hS4CS7oNtLDOP8x9lw6272HAri0v7YsV5QTRMBQ5qcWtQ8fRTNzjdmm6hBbK7ZuYHeKozY9AsdiZILFTTxU5FpfiOfEnkRxb5g9fzzx0scX2G3dUn4bHF1SuXfCANzq2Z9yup2qaXL89r4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش کبیر از اون دنیا هم رفت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78473" target="_blank">📅 13:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با توجه به اتفاقات اخیر بنظرتون بهترین آرتیست نسل چهار کیه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78472" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کیرم بعد ی دوری بسیار طولانی استعفا داد و برگشت پیش خودم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78471" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
