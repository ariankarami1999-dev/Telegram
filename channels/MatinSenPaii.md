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
<img src="https://cdn1.telesco.pe/file/AMgAUP5vnpbUCwS6rV3NIE4UQXMUZHA6eplivzlOgAwceSbjdvGez8va7tDsabdPyBJ4CgUAx6jr5Yhx9h8aYOHW37OPMaNBCGiSzpcHIkHtEE4Z91MHtXjre2ebjMtDiIm1CRpLSnWYoIzvj6jHa11uAD8A646IvmizoXVlJ_X3Fw9wuHRe3ltWAtF3Fx6lQm6LzVvud-EuHDGbQIE9MdRpe-vyspQLT9HPUO7XqymhJ9qCEls_np9tgY9NQPq0zsyHD17uSYdrhjgmBJd8u3RhA_83nio4JxvYxOoxADwLJ0349w7ep57i24xhDMV1B0rxt17Tjetcxdg1jXHSYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeCXiCBrgSJ5EE87DIxiIzev5V0G0bYeThk3Om0vGgVDkCHT0zBTtgMtDaZcrN1APWfB5ywOPR7dqtGU-w8yz9pPqImJUfLpfV1F6ijV7pMUOswD5-X8lXICPmSYcoXg2T5HgS4dFT076SeF6LyRU89-O9r_TsRwVaBHr76Jvj_N962V7RjAiMLdFIoIsBUmynkpz-xWxBv9aM2bimU8VlWDSWcFKnAB7CkFVZ-Fib2R7dMGQivUQRpv22S82MhFTzr0WGuu49_mFI45Gn0HDqzkAmO3qYatN3M3EiKclu9Gatl4GK_mEkpwt0zZ5vqfk7dtwKR-fM5OVFaZQ9K5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UOCQHT1u2BuhNRLed5_R73iUi7P7ei3yMfRWrnpoHgguqVc9o6EbmIvestlUTXqx_BqTph12Amek868PXtllBF5ko4CBJwTuOJtL5h1u14guouwG9M3ZAY_oS6ICV1Dx87sE1LqhpdT_SJvhoZLqnf0EkncDHeX7Znc_yLX8CnuoKucvtE6cc_CNl1sznXo3lBqV4T5KOTboSPde90p8WJSLTta9G6gx3ysEGAXkNpmdQDmklfm37ijgduS59OpmoWHYtGsyO9bInNe1gzn45yogSjVjZiX5-baG2CzEPMYLB70YVePNc_gv7rXSfOtcvFOSYMzBVPTuTWyv6nEVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=vPN25wCEuFccXDd4r821UUAt-eTxA2Awv5pfEMiS2UPXdGAgRg-muCGyGvQy23Ln4Pvu_F2KrXsLJAo7XooKaRyOKnvBQv-WcKCmCTQvkw2wT1xzqXODhMwKBFJe-8uSouiHDaaRc76_aPgJbKmgpP1u6O1E3ovKkSI1Vm1PsUJnSjmEyGazgB120pVNe3gwgZcZLcQ7iuOJ2IZia-PP-2GHThgGIMxY3tVFOnCUhvytOarQs1w1PJ7WGpU2pV56xgAdY3yWreocgh5zelamzOEi_BIj3kOVZdE6azdRpBOlcCW7YcJbbdwq0mV122FS6EYPZLx0iHdIKMRU-v5F5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=vPN25wCEuFccXDd4r821UUAt-eTxA2Awv5pfEMiS2UPXdGAgRg-muCGyGvQy23Ln4Pvu_F2KrXsLJAo7XooKaRyOKnvBQv-WcKCmCTQvkw2wT1xzqXODhMwKBFJe-8uSouiHDaaRc76_aPgJbKmgpP1u6O1E3ovKkSI1Vm1PsUJnSjmEyGazgB120pVNe3gwgZcZLcQ7iuOJ2IZia-PP-2GHThgGIMxY3tVFOnCUhvytOarQs1w1PJ7WGpU2pV56xgAdY3yWreocgh5zelamzOEi_BIj3kOVZdE6azdRpBOlcCW7YcJbbdwq0mV122FS6EYPZLx0iHdIKMRU-v5F5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVcHMMoNiC0m_-cuZ8B071jq6YRt_Tq8UvbL-ZA1ZURDOGDYJPO6Tjk29DKAHgoSrgiLbQPfMYqIjV7M-dGw2_JlcPWO6NPysqOKDwG3mgiGm22wfAd3WkML3YQPvFeIIqFvYhQi6yyW87ylUM4kf5bHgameYcnvyW9GiexO2qLk2v69aUYrvgqnG9UZMHss5ASh0DRBDX3m88CRX4X0cvYtJhVuh--8X4zElBdv0y9j1Ie2xHXZh88FK8lS2fW1ODaRsF2K3BJVXijm_z67s7f6X5DUYi2RdWbu1jksiAX_4D4jGpsNPMiQ-OVI2NwT0piaKiXEWnjICKXybGYWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WnuMpfShb6Wt0mljQSKkHy6ulseMNNa-925Z0-VR27NWJqjPuZujABQnLlm48bl4qlYEodoM55XU301PV0bU5qPkvC2VOA0caYpI01pWLwvLESb__O7f-pES0bxC7z_1jA2Hgr60hmsir0LdIyqajnGwEFp7DKsOzCiY4vFMGC22ykS56YTLp8nI76obozHNC8nABZkvJGaOQ4stDf-vP-WIe6Z4U00_bZ1PrWvXOcW54mY-5_wNOfRw__XrpVKkT0H9JGTbzuuf7jd8851WVtk2_ok-ftUfUbAZxoh0A-mOIiBT5fy7x8bR5ExcA_lcsDIuNl06WP-LqU_xx5lcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm8Ff0tztu7RkdJJGt12oFoLad2OwGrEzTBFYoGiGLiCoZkqZwIEbjk4wrQW4zR94HHeKYoENv_SfAi3ylNWfsqmnDJe0CpDYFKLGKidKv5mKB9tcof8L-F5Til4xWbKPKxN4zD03h5QvFa7ruC6ep6m1zOIp0HVv3Q7IYqVU-SAlzrEoO9D4stmiLehfIW34MhCS9i_Y4kn1Lw1w2NYCHY-xvhV1Oh5po_kvmCmcfTJgE85dILeOUWlIX9ppQrzfoyrGONot3UgWKlTjyTWyeN3ZKdOUcO1xzt2tW5jeM96OheAWX-c1SlkEJHuScUgIgkSy7E7S8um9KOLX76Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxYgrulchQQ2S8OBTtSvkd2o9WOfwjSQ8V7hQ85qIM-omgtK90ffTizE8h_5weNyaRP1bLd5tA3_9JFjXGTZKJ9mrq5Oj4BV8TepIX-hSXAecL_Sx94Yw9XSCzIoLLrRcKueCVLbbNDcP8n0tjPdx896KpDqolqUNPq4Oar3rE3XyVmuv5KuZhr6je4by5ZiTQxMAtkoYr_uUps63qyzofZZZQ74BW3b-K7vEwpfdOgKf51MW6BMs8cbnC6X7a1HYlK5Lcnr_ykXd5yCiHB0nseCvmIiedmRosE6Xsy5NFmHXpCL8G4us3fUGidNLN4kHoQGHmVxe-LirFRttK10mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WcWjBNRukNj40fedtjToUQmJvmWY7fZTJhn75HGLL-Syn9k3L__2MBk0fTisdf6PfoYWsiU0wyQJAOcUvUkkF-Ben5NnG6GRaNdC1wY4hs2b67b3WaPPHDtL5vmnJ7JSQtd-XVEfgOHnyFrz_WcmUkR2TEy_7c--7yhV5MM8MVB0wD6PhqkIs6mLDWXHjSY3zBmIJpSl_w-bpVQzdSIh3uLtkJDHySOWpaFstLINf7sxjWWjnuhT6sKJykHdjCwYAvrtZRwbHpYu5jy-vrerEZm1oimoKv5LVc-4p2WWtwsSGkq4fKsW2qNBIS5UPVPW36YEchZW3TnALl_y4RBcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K17w3i-BMl9oIbzWxrzt6_yHyQd--d5qhBdoH605pDKzh-di3jK8ZxH5X3qtWJzY04kY8PdCIuBUzPeYEioMvMZ-dzsRVtS15metbaKyg-Ck9_DnVScTi_dQUb53ScrmRRpN21peeruA1sifEgonPf4Idjd9UylC_OSfa9PKaMrdd1jfg91YCvWFmv0kbrS2vKN2FLjgv3F0t7BPEQU98g2ZvJrr1E__1Vw56AFwyDVGed2oNhpoUaDD_QaQ4nZpHdtBWtrUxXC1i-W8GlrkDBzz8RcWj9ruETRikW0W9NlSw5KyH0F8M2WmTYQD8Gq69JvdT1Bx4yDpgvi0vsYcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m61XPRz5uRnvaoGvPw7TkVoP933WgTcMkFZNhZ1YrqUZDvMdrlGigC2m9WzTzaUBCNAJe5ThR49N0xQYFls3BAyno2J35twTirPF6o3isasQR0NXSiDeMRO_Xc36iUayFyQ83SSjDgOLsPcVpmptKrhs_0r5SSGKmS6uon-3eNeZ6A3ZKpuZFbM42M9KeQI43MgF0Ndz_VPHdmDFQQuHYQtwzHd9o7X4wy71ZVz9LkkHX8O3hkQ6j7ZKhGj9ZTsLi98WUozJHywy-_PviXiVP-Vn4B1DTQuOr6h5xgxKrXnLNOXCiCkzOwOJfuKqx6zTUALGkev9OdwgdJwlfQRNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQPLcxQlpf-_bLi3gzoWw3K-hG7W-5hMQFIDmcSDKCJG0ULr-fp8Jh6GJ6lo-X4Rp40-y53Sh3oQikeAAHOrpUVQF0X5rXXNgDC9qKCMnF3zGnj__DrnNMTgwowyRT0qXmUrRtldb2S-BWmex0c0lZVrnynurtR7rVI0aX3Idf9N2ZymJbVOHwQtzgaWSTsrfPYhfi4DpNdW5jbJqwClVFvG6Z_4KEcEEscmS3JZOvu6v7P9hKdOvwDCmsvnOzPFdqWjFojyAD5R89TLkGCrNFcF8RnF2J5HkSkIfHMCFz7MtGFiAsHv0N3Hffh0JrxVdq7t2Uj7XsKZSjxhFSec_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L9Zq-QyemOcXH-PIh_inZkV_7J-1a2IQjoW2_0caAf5hh2EwZJEUNjcFRvbG60q_jd_G6nGgfvOgElF3k-gaTpn_mKdU_UzX6OYrEf1FZrE1gFDkp9aTiKP_oVCF5L0_qV5cxxauvKdWmiyRQkuZcP34G4Rx-Im8ZzNvnE7D6c_3h75d_x6j3WZXo5-VVsHu2d5RURDN6vHLWo1zBBmoVMPEnYw_XfOQWcIsgzHhpG__Xf8zPMbGQbg9y2KnqOEMcE_ZA65k0eEujMIGcudKyWbl3a4GzvWegDae7-2055pAGxSh4ClBRNhJwhqGpZTo6iKojkMC-CBnc0NXyCVRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UiZdzC7zj7asOZ9vokxd8SrKVLli8hXM5G7MJlsvBHjCk1BbVv3Et-a5TLg4cNxPnmBSMLaZJDHTiqaGcW5nrWi3t7beGvn00jW-0VxATXr2zBGDdcDRXVhd3GJ-r3KMpmR4hsQ4s7wZd26sl8-mDobKC7IUj68SagGu_HZib27o5FEAHOXD_RxBxy9uac6LLEXMqbrquk-L093Qh4v9ZrlQsbzdEu1KfyZr_Iq__F9Ex1dK4z7QCvLt-6dUNHammJDtzuWKMQSwZrDXBRpZ5cvDjLi_QsMuG-BE_S5CwKmaWjDUxPHKrEGeg8aCnD1Ir2gW5KXqiVooXwzmOBp2mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICP49KkqafFH6OAiQ0NR9nriC4Z8z0DLZ6cnxbF__ycoXlX2w7CRdh0-GwIWQLC5PnkzDwIvg4bvJLg_iiMODu2GH5o0oRhaZSx45D8KhvA7mA7fd2To3yp3Ft9c5YuuyiuGVbEHulSc_eEg5i7lepAHW4P9V9Jk8Argt_8VQPiAhTc_e4Hq_QUdl8g20SuoQpTSGOVCsVBDuTAxU-PWZiCvX-YfxOuO6n-NrYpqJ-1jTyMepp-HJzaBF-hTyg7j1xtXbHy1kRBVdO75dWYWayLwrarDBhF7W_WElsnGtslNr_7npuz_VMxdVHK422PL7dKSN-9LqM5k-eIo0WuIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=TRGquyDmpIph6ZhUF9E_ZMMa-5EX1e1ud_9qL2fcF7uZcwDIXNNloFkcOoFOqH4P_u4bb9ITnl-nEoEDHeoFJmpM_kv1ga3201JGH3PlvRs7fLssyalwCvrhXY0IyWDesw6NfQoEbdzlclu3RiPrnZk8VhM76X3jeX5xGSUxRAEgiHzIU51ywtLcXjChBb73HgJExAHgF1Bedd4zydpX9LUXetYOMh7PKJLJVpYI5cXwvG2zIEj36P-YL5LL7GchtvHK-zr8Y0pnrbSRSw6H0YrB6BgFjCPCLXGbLjH24mmQVEF14F5_1tvlDuGq0bQ0TUoCT9p9_4RKQ-6Ba4Ri3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=TRGquyDmpIph6ZhUF9E_ZMMa-5EX1e1ud_9qL2fcF7uZcwDIXNNloFkcOoFOqH4P_u4bb9ITnl-nEoEDHeoFJmpM_kv1ga3201JGH3PlvRs7fLssyalwCvrhXY0IyWDesw6NfQoEbdzlclu3RiPrnZk8VhM76X3jeX5xGSUxRAEgiHzIU51ywtLcXjChBb73HgJExAHgF1Bedd4zydpX9LUXetYOMh7PKJLJVpYI5cXwvG2zIEj36P-YL5LL7GchtvHK-zr8Y0pnrbSRSw6H0YrB6BgFjCPCLXGbLjH24mmQVEF14F5_1tvlDuGq0bQ0TUoCT9p9_4RKQ-6Ba4Ri3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPNNc5T39cpHnBFTsnFPRYeEOv3ORPkPhrLjJ-zHEVlguq04HZT_ydAJ82sE2uHC7IRD_gIFrjh8hJak93WEgCRHTWe_9FW7ZK37R4HzHKkPAQVQ1JMO74ajbPgQVY7jgBVTyOP6n_K_wIlHj7xaiptwmAaC5s8OZ3azfbDap7zS-ZQczzYqcmxqzOPtHz_go6erVpGxkq3eLnKgTxOgyts5O6acHSfsnw89pV6oRiI7p9Ns5amAE5h7unPUYd5TKC0KjjhbW7Sae0v2qI0pd-mb8rsa6UM3GOi945Ij3lRBvldRHiWN_Wd_9zOgXA9L0F9qxEoYcrsCO4WUhGZ97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c15fi8dPmby02yCLqMWr816Jo6yWkKyC59WMulMsZfG59yE7g2sh-X1J0pLdyds2AcBvTdLGeXmtAYXLmDwsCnSWmH1gYDsHOb0b6ur-lcbPv_7z8cfV9A_jyaD4vFop7b6HyPPGXRLvwy-aqfQF1B8pr6BHy2FK4ClYAH0TimaJ7aueNVTgUbwOlw4hV-drQlYfLIMdVixvmOadOaAL-MzQH0L-A3V2lDtNzOeZPWi6JhFeZfYMERTKNGXPxytIklKFBuZu-PciZjNDruH4K_qr5if3lLtiwYDAeAiS3TyuFrbYG3LCdfFrbJpZ4JUbJhkivbbIinUV1WHNKmRBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOR0vu-wkXiX3YIuwavlPVPIo4oE0xybDnlB6B4L_LIIbLQWTXoaxY_pLk-Ax8ivAAyYdfxXiwt7P21BC0WWQcRB-ftYwL6xpgQ4QlIB-wwj9SCCWiozsyHNP8fY7ZgZBxhequtr3kqfV1Vou5w4GoUpYUpMfpPYoCpZmlc2JuD16uzVCPL4ZydXSRycThHgGlFmrmFScOaMk137FC2udrG8rEYzsJ5CiOQ4u0LQt_CTiw6ebDITj8FdaduPdu7UUY1jvcdU5-vIdC-BAmXM3s-7bX_09C5wnbKmp4DZXCkHGawf57dPnfk6WYYUlxgvXGCsRv27QHo0vdLdhCIayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWamkbt9yOzZ1KU8-ic0liMxjnV__C1QEkTKUsroLereVBUoaNg_YSpnlMOFhz4nz2T804gG_wPFTdftoI_OE5iToTYnEsjfVv0IdQevwcKTGUJKDS6KErQGmfncxaOxvcScxxWnB8gP0Aepu0pMWQ_Exl0O4JaBJvVU3SoI8bt5m48sXjdmFnDGSW-NA4n7oaDUoSlXIh_A-V9Z129Pul1NYehOgsoyyjT8OvenTOAT3Dekc5_IZz6nkqv4qeuP08c-vG6F9I1H3iwQf_VZsJzNG8vRrG7__5Oold8iOVUEen9oGKa5wKSTM7I1e0ozfhIQ5-BScTSNy74xmj1C3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aBtS5ZCFSjgu4nVeGCMiNKxK-jdeID5-JB8Fpra7UhqHh7iotlVeKDp-uC-ohnfu1YZ1aAJbW59aXC5ARQ2P6UwCVoThajOwzKpcWbRHo6bXgVPhyCb9Y4E-MpKwX4v1mDkCLe3LM9KYfWEoaEKMeN6KRtJJNDJHXJ6htFIHXIYmgeSl1rDyt2vGHqh7PiUkoqmDqzsEMDg6xn47eYOzZL4DkSt7ntJ-U-4iXhGYKYik9Vs-pIcWL0yFfbrMxbNk0tp48HH52ZHJbpp2F4LcFGvh4TWImFBcWB6jo9--TfZpoGwhLl_dxBuzKE6iikQcaBOLNzQu8tHUWESgO0aG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvmshbzSX5ABOTcajlD_oJ3f3_uaOqsvXSyu8fcHGgA_8dmCphU8diG9rk88zv4oA6hp6UmJ-qHwLtSBzl7kasvigUTOXmYwomLLhZY5kLePtlfMR4uGgtREk63FyzPg9vo_IUym87aCOoOIsOUmk_HFvM3DydTh-RQKtxXQVGJU1vxLIv2_7Cqfsrjn1qe8yqHTlN3xjVEIr_Hkgc8L7CCc_kPJkacbXP4PcxUOy8IykycWr5t73L73K1VDw-HYA9TI0TI1uQ6Tp57FWBZERZT6DG8aph9_-EPH29VGqpMV02qb4QiX85J08mfCLj9RaQivrd8ZrDyDzBynpbx7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iQt-YkyGJ1zE1ScJazAzH3s_5yRyInzb9aNbQEk7sAFOG7fObpzML14n9oavNGMKlzaMIddnH66P2VvValKc2FkevRTShL7W7ejD2GKhwYvpS3lXEh_OAuA2miX8ocx2jou2g9TEgn2LoQNYEiNFtpdk_tck6zBHjYtKwhF7kI1x9K9v821bp7w3K2ILKq4LdjqtVmrMO6ccGWE5Q3ul59NFf4ZF8iEJS5Wvsi8w3vf5enZi8_WwZi-e6lT0Q9s6yl9LdU0gCvQdJFc6AXH8azUsUq-BbyqMRFfNf3a0aI48iRl-EE-pO3vqq52yXGnLBa76TRQEYzK2Q8ajVfmd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A8n7vZyU0c8-2NKBWj6cM_xPDSTkQzhoABVtJNcLTQmmTrHglr6nwRtWbnnbaifHb0u1edAjkJYYVWPQSu1vejnYCkJj2HJxbIGwubJddtXlcqpa7IGQ0T4xd59386qg_R3vzQ8EtyHnIQ1jvbCr_Y8sJmzApWFrl8GkWi4C3E6enn67_yB1qtWt7DcO7i1ALSxphkq5qu_ex1j10zHkzBVJm8mKhHjXWnONlmZ2A3AVWX9lzEQmCLA5CuWUqonmQdgmGnoiU1wfPIG-d4J2xUdJX3f5S3d1D8tyLTYOrXo1eg4eVKuz5nYgZILvxw9L5kv16q465I1Ae7qTvO-rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HNfmeiSpyHECB8itvTzcgsco-dLmsGEBxuL1Z59bnXNL6WM3UbOj5ilQGvBvt7bexj9xMhIjRU_3f98h_gQtHoFbnRigeu24wpk1Heic8H-P4v1u7ahCFn4CXKNPdy7A2QNaTb_D5jilSQwhEJEI7MmaV5EWsVxUSW6dZ7sGhZHYi3RkSZa0LAIYE0UrjmTqPvjyl_ifbcx1H8AfDgQhv7EecPc0iS8JiRLDCWoZ7C-fqjVdioTJiSY29NfTqRZ7Gfl6h6PusQD7Hew_YuZsATQ52J9HCr6sSszRxClYX0n1wvdwBlSVI4NzSnv_Plo9wxm5xM8i6iz4YgOfh_qzLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u05Iwca0LeJRwcHUojzlYaYCW_Q3ZIwdppfNKpC_VKAol6xmoLq2mvf4SN6ipIUAhhpsOD0GMftic_PoHOrfkv7T3r77c7Q7VPgZCriOEcTFlPKqkn86MKBBKbxWA1vTw_xrLPGovRaSzRF7GcVr6CTEXskvbvjzpff4N-vLeBexSVl-jHcvgdIi0acu0HKaAs_s9qnjL8gl2uNGIR-CZgu7A30LvEcI0mUS6qXhxQywSApU2R65cJVmMkLz4HUfuusO0Vdof6Ev7KX_wYU13kOs-RTgLJwbqiM-O1HYE7ioQnVF10BMVOeSwOFGLF9QBJ6Ql6KUVnzSbDJiOQy-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EXqT3mUHMt0NN1ERVgIbcM8pMCcsV9qDhm2068Lk72pnSk6NooP22HIW5lzPnEEpa2MEczJ5CMON_NyyM4NdpF_mCUj8Tzc1TbxsJdeHyJ4yLumK-aKxY_U6SDCR4H-VG2yVzuvFhF8j1OgU62dEAtleDNQ2GJU7yTEm0Rrm7u8jZMoBgr1ENjDWr1XIJEJnyFm2GplLXNAmfeSAnjxMcCWsjGgCGdGGviwym07_UTq1PbhjLItOwb3iCbFlYk2RQbFLJePnidb3tjI-4Vgjsk-3zL5OAK_QVOoX_900d8bS9v1YzEclQ2CCCm-7ZdRjY87T1g4Iomq4sb-47BoiDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ngxnz1gcrxjWTFyY_l_z0zDDMn32-HJRHFqNacn9TrsoUYi8fCwb0IJCnouPUsRqxltNuuoTZMjx7BWgwdQYjB1aLWqlRh6gVUs7KEOJRwpNl-TZGZfNT9dtAQaMZkena4oa3Gw7gTitn-4YOF7r388N_K0nbKrnCfDcndUGKw7HIkO04uPcO84g18KzWtsLwrpaMBnQHpa5cwDL2BRH8Ox087AuPwXkFUILLlfXOJBYWiq2DGF35aritAeChjYk5JPZlBjiXgapI17_yPsefoX4kzBqvoER8ycvecYr3v3IVaS1CuuDdF1j22eivyPAxZ-aoztqKcq10l1zhEzcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HcZ5uTRWDfthi56Q8KaRSkBDIREEcYxu4V1ADVzJKFW-ew8b_Nn78DScwnXTXsM1oHuM0fODxoL7h1716-h3eeT5JWsvhOtFTNuKVkbx5TiKJNIMkL7BAMSwJRbD3sLr6r7vMw1LUbqNW1UI9twySmpbWdbp6ivWvKbxg0IwU4RjqnRMnOqVVaPRfA3KjKG6BgLSTcHggSksYWjhHESdt74t8fw-Lr5RgTgA63t1TkLVJ5PlgWtyEgsbGi5B7Oah3OKpQVobuaYk8OLF69ZJjRvNgzAQcaZFeqjdiqcu1qu7bwVu4saCSM2UMx7VFn1IGQZQIEJu9iNPXBIyp5aHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZIZWueAcBvWxYg-kunfXEw9RCIfkVRXGw9-eZGbjW0HyoKkHgBTDPCOt-5OKeDSNcefrLCVvGXiayC-nltC2Opxw2oJAnfjPsK53DBVIhhYJNSGZ3mA-yfuunJ7Hgg6MZd6hNPOvhhBW2g5XMunMqOo32gESIYMWaBv5MiJEibQTmz9PRP2ndR4YyRgvm2T9z-Iiwx4YSn7gx1u4ORTNu90C4_7qwOXxj3Z5v1uqS_LiQqDScvOqlpWS99BnXzH4rc1o-x-Wk9it81BnCyfQlLe9WaUTeCO7PLCMyGaKwIISuT4ZKCX9DdPBwTAvKcqvumPlO8P6NIY6IPy2hfk8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k2P1Wn8uyTm1gu1k64BxyJZeToa0UUdman3seI3gp864fj6A74fPWsbdE5FVVsFsxANJiEkh7HFRHXTgqC5Vl0Tqc6yh0HdBwnymL5DKS56qgB_6VwudNUz7SXSufovBVcrFb6TWXXDFt3YuTUZReOuz24txwG9kKAm8h-BQHBfDPxilTp_r1pgaA_HMQGI4glWSbXQu4IgQE30VhFy0dIWbD3NxpSi3mZnz-AtKcP7vvNpQMF7k2jtD9xSxrsLfEsThM0U9WpQzaIABEZWAhHR-BUModUYE3ljfgkoXhcPuDKAN16b7_yW8QKCDeRYjWLomyzLgQTE1O2GWQ0mXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o6bHhZ4wnsas7vCVS_e-dbnb0Ioo5rmvBKG6gjLgBcNTEk18X1S2NuphOl0_1eq99TCZi9RZFQsinaJ3ZUxkWK-ENIur9XYYch7z4Drc4hw124i7foDIjhPmWuVhWpxKIzHbgjt_In8_ac8C9tyUJYeXTLNbOshN6sRFWjyd84Xa-Kl2qA3U6ad6pmWYxo_D0YcSCCPG3EVSRuxt2CEAotCDy2e6FUB0odjM9PCr2Sp0ngIh_5TIIIBc0bgdehQsOBxs6KEB_9kKO2qFHF-GEoJ6sFhHCvem_lPrplb9JBt1l1dM8aErGBx1cz-ICIZGwceeqrPePj4mzcgAVEgtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFTFLyvGyQANogitNh5c9SX3opxsGtSj4y0oVf3ZgTtxWb2WzB2b-v0IuiOoRHU7T5RGry_gKI5pZvKOSeksXddMrI9JDzOhZA7aidhy-AkipAyayjuDRqBofka_3-hoeDYV5T6W0I-CyJN3vvxuasEe1W4EVC8iAc5ErLs0sQPIs8V82KWCWF91WqA2WqlJQxcywoiOi-SsmQ5A87F1uREYLfj2MCiycGBIUEEAlLtD9JJG81rkHgTf5HlV8IWu1CevigUm2nuLFQsOWUwigP4LDHpCMrUT8Cb3doz4vPR4YqG59EKL5tn32dS57YJVX0fG-k04ZabZx9OCtEQLOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BTwpmybhOLeX9_XvdplI__mI7tsSG3HiqpuW0ThaIlkGQEG_f0TsSZdb29ImtCA8Sg7nysOyuHCKBeFDG5NhcVqryXYclXobJN2IrFxNh42vCJhyZHPgO46y0gZa8_tCDofe9OzGY4LZA8DAzdo6CwbndWt3hKRrlPo8yjPdji-pb2-WSQNJoroNsSbVW_mXL36wLlrgLqMPvd8U9QYKDSj5inWuLUBeEz4MLoke72o6KzooBEV1pM_sBvl-jtOWZkr3Bv6r4SWiIAZg4UQHguPAL71XWvofvJMhIXZyeE4Y0PntkdQFj5P-WTo8zUM_MhKskK_Mf5essAzvww-RkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ry4JiuhNswpA5hAQRM4ShYUXosiC8A331XtwYeEHRVdhvNpXZH-CUQnSPRQzyCZTs9BefvTzrJxJOJNOaWSaTeYFjedUj_QbFvc3XgB0KA9CbGDfJwIcuJOj1ZoYCO22D9nbu8UY7RCa_SWRq8KYWiBWR8dHsI6oHI6VEkR2Ky-LaApc3frWq8g49NKpJwHWQ_-wiCh7eDVEhuu02kcw1QnqHkbB4s-HQLfOzXQtLeInRhmZ164Rm480XwjwcMxTdGgZdWINU_vhu3yJWnuJqnwlSADoLMQhozBQqaOOaeXjm_aAHOP4wgG6WiwRBukhUudtrC4nmuXkHloDSaAl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5Lx-6ARJupTAj08n3Z2tXd0uQ-Xs4ry34v80Ws0DGDNaLgh5hoeIchr_5KUtfnZ3P2Ji4sg_8KqmPSGL9k07gb78393mXW-IB89RXO_mhN2vWXQBJQEnIXwYTZy6uJy6XKScjcalFPkncqWDkgO4e7RBkWMkYrOjdlTRUHlZrbB2rBLmGHD6CKrgSSvul3LaqJbjXvt7dVc2dNbIXklPalWJcfw38AyoE8lRb4dqkbApvJjl--zyUgZfPl650y92F0uhQMhDhdweVcwjbREhYd9WOnIr3atmvES9tcAxGeCx429v6Q-muiIaP2gGrC4K_J0T49o6LF0lTw9NFxlcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OkvaTLOTMJVtBlKAUbD29_1K9ZUFjQRHaWJYfkb48fDJEMRaODm55a4P9OFqJp_cWYgkh1KwUSZrHf7Mfk8CwujmAn6PBkMXa8hQpdxOSCFHLPCwocBXC89ZIRi1MuadkEKxay5GbUocX8G8V52H1Ac-DNN84gEZ8SOD2Gmlh7Kk4TLi7H1y0_PZbBuWp72TmdF7woy7QL_2IKj5sWeuxY8m3l7-2BTZE_vETlk-AO_yvG2_2NmAxh8dmnithYW0GAM0dBjq3h0RbwfnoShBUwOvJzuWzyr-2Z9ReKwWXFeWFnMK0sqH5U-0HwIAcyUVKLMilMnu0Y5dqn12aRQvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g7TT9e1L16jKREBr99C-cbJdo53VehEzdm9d86MaRKS0eCrNvA_AELKsOEhzWFp1uL5S9PjvSR8kO_ZCUFa5XIcyx-HDJ6afE_DdNPiVFSeBfTTfwmZh7sdFr5j28lWwy1Mk6dBZK0kRxjJm0rb2aNrWdQ1pQQYoqi3KwqklnU_x3bLEI9fSh4KBB8XPrD4--1BWjt96mZCf7_IcGGqmsL5KVGaIDRMvCkuVO5YzkR0QEShT_veRZJq7ZpdD3jWoy2dK8CnCJUrK1z6KhM47vvhoAdLTC-gPKkfLDIXTcqmkjYRK6WQKnMTwqY4QtuHwpFRWDr1qli4lFi6rxHdHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y60TCkgM4rjozbO57eSBJ1Bf4t2bsPoCJ-OM0B_SRkS3qe7OkkP1Rtm_qOCJejIISLXRajYEcfK3F4QnGdosfxub1y9gLFs_k6bs-WZZwitNpJfM4sh4qA1d6OlalZfdPRw-9eR-rDxXZaVw9RUc4jN7ntVg3gJUzCGLICJ7eNt4r_AbCn-VYJ3h0U2w3Gg4HwoBGwaoOpnEZRwzgsoiVX5xmLxIkPkeSz1UMkgetZioMncnAhdTnP_2NJyOASfw0LgrBfOB8cpWFzpnq0UdUw8ip5S9Vr-XgaQzKIzINYfkFv8JBNUkFC1Gyrtb3tznfQEJUFk1024Ah9FDuVpuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMYqopwyrWTQ2qhsEYWrRGOT2OA-bhYGBa_P1xukUilGYYYZI2GgBVrBVAhknrnIINQyqg7HZeEhXN2ZYvNrvm3ydEBCSYzym34yxTn4VlVoyRooCW886ozhgtmf_CALvUNw2kQHq948KkceDTYnrAPWovzmUbJlX2xKXjSGuKHxz05zrOUvSbzTM9yeKreHePKRrihNvnO9ysI3Q0GGxiOKA5_O57TsaSdt7ShWXZ8AOuitnsyTBtLx9B-xzTouXvJEhcQdiCQTC1_mpmpthIMY4KK6eIWvin0rbS4aypS5997XgtOFc0r4tfk9YkdhEedilU7B3SdxcIVwNDsX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXFxune0il6-dLPtAFqk-5X6_EbHopGoCnB1ZNO2e8d1pr4Cwk4htQMlqpVyP76gYjvMTidNvP0dAPQ9dRSQNgzVFaEbxiqafneFKcfUXZH26MrjExXlPIy-Txj27ypjuY3HjSbrLFCLYecv6RDcy7Q2oLnReK06oCqDyIPQtt3G7S37ZguW5967DNeM7NPcm0WD2j-l0lK48R1uNUmXflA1Pnq2QB4042lcVgIJAayisLV7UsnCpl0PE8RbOpJpN7qn5Pha_WsM20T8doZO7nnlo2JxpH3ifFHSr1SOkOzc2awk9Ts3dNFHo0WAltqH6SragCoDiE60L_-3YWGlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MHX825KFxB6IkImBevF0whQjdQscthv4FuZdSbhVRDFTcwHkDEtYjJbUtnAjbNbgr4F7Vpf6L0pu73f86Q5escETepSgczXGp77Qy78Uus1RHjPWo-6poe2NOk-oNpDWKBd-20L2qhoRMaDNXTYhtXxlEWjnV7078kV2bItmIm8USyA3qFTwf_wMAGoDJOx6rXI1n2hJLmwHEP9ixueiIktErN5gADkFuZV3gJrUlVrD8NA1TYzMBkg1YLUBuH-gwfTjYAn5ul5-v6llItTDc2dK9FS36AUOSO7yjiqGy9K82-dFI5m9B7C__q2KRzxgai3_O9vYLcIRPhZ1XFjqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dlpdkbdnq0JvEi0G4Wz0eQYZC3E2XnksfoVHA3f3o3Umy0c1Gjje0Yt9pxYO9f-BimKfNeISce2WRahw1X_5t15ANGveUQgFjL-n0vC6flBqmYVQuKfnlF31FvFZyUmjUHcnGurd2saTQICGR0kfUO0T8Y4l6z8tXl1J_-V41cmCJcIeSTx7S7gha6ii07zz7Bv0fA9LsNTBEHK7_Hb1HAOfZo0ulXMVTwAjFltwzn7pKU20bTdPFe_h1sKUZWZQJa6eBs-F8l0Lcn7yo1pxA7vGbSLrJi2OqSiAt_u5dszdQ2QlTNHqPTK-Q1JCNARVn10L2dN_OsEjC7sERhSKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UlX88-Q5r8q2QJQHbPNyWnG6DoenN8AuMH34tLcNZQu8dmSKpAzXtS4rfuAoyxYXK3ZnT3tIKXx4of4XVaXH85HeKOjvCNrb8vFqz2TJ3cIWrp5LyH4KKZkMjPxECvkkL0SIDZatddIaQiBtELaUEi1_O5yevJqH1Df0i5AK-95RHRSvymfU_5JmNljURAxFzvFGF_lfTotmRKqReXcjdpfzHGF1fKaCiNoGqHVo21L3MIa1dIAO9EhV8DDqx_SNkY_PqlJNH4dL2v9J19JBWGSrlEP8FMRBDJ1NfIyMAIU9cQFBwThX0jp7azhiIYFO8Z9QDP0seZQSiSkCc6k9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A_6tiEj4RPHHQ8a5IXGaMzKV34nkZWl6CsuAh5Ko-nqFPKRK3RZs6iFzxnAXU-slU-2QA351eEC8FQRuJWSimrmQ_x7YWKdnptHiMWtW1uEqyckiQe71bZYkuI31wiJ6rivpOZh0XeRIh0sBar-dBysRs10w1BTy5h9gqqwxf2dmizUPhCJ6ryOYFMWhKfAhe_p9LWgGlY5p6JneCVJiwxBh6gtF2OATTZNknOoN3BTGqUfdLEjqzpcJPrzuVRMiW86mspxG-yEk3Lx2sXIOJpdYve-ZutbKdMvRCh0-DmCoqlzrMj-hvVTVqXMol2C7dyMAFwpaBzUbpZEvsxk0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WsD6rT3Eq8SJdbpXt-CZ4_wcfzjYQJsBz_Q3k9dQLtm1zilcVVUo1zaDK_opq4wGm1dIg5HlrkhK6irlQ0ABkQhzZq3DLkARVs9BS9uG15zHzDw3Y1E_VKVbw85lfcHC_5xzBUgx4aaoyKDB5LWnweCPiJmGYlj7xDzeMyXNQhKau0UbBHTIryHaOXpPHdau5aH1WVUxL4UaLQVJteNUBah177wr8XnJkHT1-MERlXBiY8r-A-oj04lifUpMSm_fgOe1ZFAtc4g-zGVK4uUz0Fi5jHHf5V5dCkG0cc61J_VgQFvjktN6i_ilKnKVKClze-jGatqwAd567JB9waCtIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QmZ0YxRL3EYsQJ-d82OnVNNIBz852TPzlI0-c6iXQAkFQZ79lpDUgNdDVzxHBV79-tctNfh_UbW1N54Zku5LY7ibuM9dD_VQYo-3g0h8xH8m74b4H8Hqb1a9w2xs1rYeKokDjSVHcmWAMfndaCYa_FmDRdSrfQKuU63tlmKmpsEiBnJgOOYdm3gqwtXm-kV_RdODNg1Fiv3SHFaQkp_ASMbqcVKn4iFpNDEMx5LVUFcwZTokp5Fyxr-0rghYHwSUyjiDd3g4D-Mog7A3lGJJ2zb87mVcuRFrpaatZttoabTbxa8r0qUMWubOK6u5xh5FHJGBh4EMiOeI6YwfLPV96g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enGmfJDZpX8_60suWaF88NW6W0fw4rtnUgo03_BOhPJCJFnkNgRAoyMOe3kZo_3LbUSUYy9tmtu2x2KwHw7mYETZ-I2FADRzXlrsdLb7L2JXvk93TI9sbqIXm1ANdld8Nn9SxJq9AMktliiolS3LYTjzVpmUNJ2HLwfpJG-ie4tWzxEnCDdt3VIg6LOWBGVLDa7pfAu69bFSxm3Z-dblf6EZ5vSZpkMTri-m-KzZNkj_p81pY9JVwRwj6he3MvIBjXuFjubl--rsq5-WpdvKKUk-tDBZFerJ1dLaDgxM8kKD8gLg7EHylp7hZKm3b4zREMnaQCEc_ERHvhtcvMW2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrIQDjxPOw6N5JNEh9_aL2DX4-R6Jd6VtHb8Tie_95LAAdednId7olOmVqFfHm1paMafcKq0FAuDz6Qagz0EHrN38ANyum_7Vt40PjYbYWbY8jTEmUwIjJZtAt_AzS4l0FPHQv1KXMvkSYOu0r0m8A9qeEfXRBVCYq7ca4jZewpetegIg73eoClk6zxKkRXJnGBcksu-PMeMJa-4vSfyw5qJoq5RI9NGfDSmJzgwOKOWGyBQMOnjLI0CsNMBFH4SQKyke8W7FLCYr_nUYdqpKd5QaHm99YCFV63DWiMUUyhbnxlzcV6hUhAH74YD5VCrVmZ3Od6wzsl-SxaWn9cbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbK8uM2C29I5ZKKNIx7O88h9zRuX8cdQwEXYpQqKnSvuI87NU8L8Kh157F_wTPmApS1SwsnSC9V2tU0maECLZiSZ642anQGFf6_DP4jBvh-IkfYKp_JLwYJoy30aL3rjv97L7kgWnnRzRUPIGX0dNCYCl_NvIZhc-rJdMoW_FTOdBvu9xebVVZb7Vugj2e_IYPVu8F7rTVtefosgBC1kPe5Zky1JgMmekOejVHyQLiRf_EXoTuJRR1AZiwqEGT7vXXVBCUvAU9z2fK5xspxyJ4d90BN4bFpgyQGvMD95JhdN74Y9N2pKtiJoFSSkivhMmTTbIvIq69BIOtHc5714Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/szfVPLSRVLsoGGmAQG2QsIrZLHjadGWgCB5KaVJLt8AYh4Q-W-cYN3hgVRf0TerbNyrFX004dbR8yVr-k0QFreeHULunsi5tYGlBuo_uURoTOINoyD4h6NM6CtrmuJ3rbOKG2vb95m1ewNEKwvRu9TLzaMyrdeyhxk2OfJcZATf8QgMsg87CW3l-Y_WCxw-WKqrGuwL41PdnGyt3O-RPyeGSnHCJImtCPaTwU25T_NdkS0qXVRL__4sKtVM7wDRsl7NRvodDNwHvdJjBlzQmW2a7S2GpO4bZtK-N02jebuHIdK2AMux3mF82U-W_-Tu0QeSY6QB2NMjPqHRdQls65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SMUbRmeg4NCrBPoY4eDk5TvNk2oynuEnIz4rBLlUTpbJs43oPHd2SbWuqveysqK6B4YZu__wTrgFYcpsosH34puYbEdst6jQSCbPwQEaTMmfQI6RFOARw3Z-bM_3vJ6KysMlEReiAhN6ic1zz3jVrU6Xt0x3dfEcDF_GOSAIjr_I_cpbRhEOEvPz8BRjsEFcI0Bq7cgM8q8JZENlGDagDpYi80hUsAyEYgse67TA5h3R1-lzio3_s4WZWPE-_giAq05PLFLWR97j0_9wyY1e2UxQ2ltQI-pDmeVZfuOLm2HtTc_ITyJy5NHRo9msqItz7IpTiVwYVAPUJE0jBlki5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/enq8SE1fnCq6CRWSIZalMYbeuMqkrWBmWr_b4KGNC9I_0CDI6tVywtDIK5QpzVSGeIWzRyRACkQRJfL9bfIjRAJbss_U5BPP1sLzc64dLoUzwmQXXUvO6Ox3uTsQPDod8aXHToAjopuK_QDMQWGjoIvHBdRTcvkNIdxd-MdDo-V0gSCf4Yij56qtUM8uRj07SI9QeQsgQNajQ4Fit29aUsbbT4EyrTBuXu4NUJgR1jlCyfl_xQFTqRn33N4_jMfgvRyZCiQnimpnhzApzbMqtXheJIQImspwOrLnSn3AFRpVbj4WivCl4idurcDgzo2pR3eBDX1Yiz4dpPpGeHab1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MxP3AJPq4F1WA9TOBlgyxKjUhOy-36mv6gDcfS9JLuaEqSdrbuoaH0UeX1L6nd3xv97r7LfyxmBQmcrzzqjLEYDJpsge27aFOkEco8hhQZQYFADntZUkZwLEDThzT58c9GUiFhClYirdEqs9GPu_3KMXssT0DOKyN24S6qawQa4YHBz5X0GPj10Z7vDJ8jhR8wcTExfog9mMee6BpvwCF6LXZFYX4vAEm8ptCTIpSe1pBYhiPbOF9bCxGK2n4qDhcerV5E-azC4EqO8AipwBeMTmqqrfL9z3xIDc2xElHomvDz10p-jzyH-V3SAP2m0phc9rcRed64up-AEeZ6P3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-ff5q7eREU2-6Lv3Ddz65KaakV5rboAWcfwK612vu7AXCtjEPcBBoAcLK5CpYHM9Fgpks9o00tD-22XU_Rt3ipjsjxIgrjGHyrAtUFVdM3LsXA3BgIibny1cWQLy1jgvOyDFnAswLYVlWBh4fNU0eBlLOl7bVQ_AQxTO3tIwgt4hLdqdV6bwJ7KqL-jOVZTAnSWhyCVzQi03XKiQTeo9c22z2xY7b-9hOQB3ZpY-6N4fqUzOwnbuY1_Arxchdr7DldQs3dqOrD1cFZ5DljKaale0-dyFlUO7ika2MwZDTAALqDiInnbleORura4zNWBwrlKTWXA7s8FHOeZBEHOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5OPuliLNSdDctHrmIk_zNzpzNQl25GkX6ZoJgPLdhKnRO_9huFVedIPL-NfMq0OGNfum8kkEyt47nRZPK3o4J7zqJgRfV_BCjIWimrunRMzfMZpedIfmqvCpAzsEYF9DzGmpuB4yq1VtlfLj_WlhS3JGB-QR7TzGtQWH5LZfBcSwTFkN1TucHEbEq4dA5himBFK-dmOTYYBfAgebWPO8mI2lYDViDooUSXMsp3plmDzg-8LONWHbfvGKRMOPdTX2Wgk6ek8iZG_OJHAW2fYwSEtEYPuXQQSmIOgsz_Sp1X1UEwzm9rGQkd0jx1akvEDKVMWnkz1ultl6B1-NPx9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZnk30rsgAEuSrWFrBjcsazMAeem2-owfhlplX-YZRDgBYNGQo5DB2ibLVLurEmw-kWKgaFcgZC-_yd1JRUN_kZEruzAkwsnYZ47JjZnVgIKqKOkb5EbLC29VoU9_fd2UCma6eHzAesXvft9Eu5g_ppRqEECfLmUnZW_qeU03R59_bJ2HuBbqLGz6sHtQxUxKVT9dpnIRQZfTDTHFnNvGM9vlmGMRZnzWJIO8CYPAK14HvhPMp42ZmOTsBSd_BjBmcY4IC62pNsmMhxQxqlebtSNcwkFHuEABAGiao4aLCvGDhhVImBoXdf5ApT-NU7RFLFG8egxsdQvNiH2GY3gxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eTPaJiKFIRC2rW3WtaOCnYi9k9CbMAWAXdNLXyBhG54UgEirP0gnYLzlu38EvVe6z3VicPANns0zghDUtwn_FkjCouBc9iMkI3x-_15s4_5V4LWYE3H3a2yuGN-P3iRdSctehLZ5V9aw6cKE1ZOWMT0wSO9U0x2SSUBDfdV9C2moH9DB72jKAE3w5EQf3TN5OY2k0jmaw55A4TxMMqJbaGTXwLvRrJt2oRroh_KW3-llerFC_tPIK4uw1dEzoRohQgd1qMGLTa7TIssKTJQvzEFUvwFajjN0JLYAxEN2L2vAL8NGH7Lu8Tuy2-9WdLyHzg2IElS9u9yj42bnfc-uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_qnzlXraaZ4ltYebRO5R5tEJ68uuZELlnWA26qdUCK6rGlddK6pmB1sxVaT3fNYhC90Ubn8-AMgM5orVzNbbcJ980H9NvhsPhcYmURKLqtSPnox-EbwliLf_ZvhDZQTFDtBG7_NcfQ9fYlfel_dQkCegZFZeZoUKys9p33o-xvwB_l2awT3mkeoN7vxKa0YHGhbXRDrmi704NNcYrMLB4engJM_8Hgkqxdcr01fl8JdIy5ke2nm4r48KO7m_qCgRlijla3vfhz_WKy-TZh8pjCF1hTdGHegNUP09Q-rzBIeTAw5uHlNwnS5pV2Uu0NPKHBto3Bk1N1dEzlxjx5Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMz9kGpYyhy_s7ngjbXF-rV6jzdYecPTGXcRfKP6UcgedVn8rY2LXx0beUblk2ICJX1KD5CukXVNAYN9Z8JFXm-bcnkzwvnwX1pKbX7IbyguQF_UfuF_yiYNiyUu22BnyAmsAIrIyyq5xNlpAW0zEuG7SW-qKHngPez2E7M-UjdAX2i0YcNX4SDcz7ZZ-X4Jn80wSpzV3zbKGS4TFd3qQaaDqQC173vIw0aH4gRGX6YItNUArNTZYDvYUK97beQihpkuV8zD-CtUbktp42Q5na24o0q4-ZmRUcnUPq7pfYydTUJZFTTz_ndDJO-cqjVBCJFMHuPZYsS0Rtv7lpwxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NBrQQM8AmI_C8wQBVk7VZva8HkOaREVoiLsVGyb7WGbV0n2kOalt8cVu1zwRN1gQEcbm0OlFbMRDVFojHA8QNMEN8sm88OcmQKOU1jo9XoHaAzmFK3OL9VyMgLMA_zlyWGEFK3EkPzMm3-FH1goKax9dRGCs5SrqreU3jBpDuTFjvzjFDWPGNpTbXxCdAHL9gFbyrHyUcH120y2SJ_HcR6l9xPVWlWy5pCoDtRIUd0K0-0n2vMWAUrFN6XyjdZRyyINNv0YZHQ31GFH9gYZAQoDwRNmJsLJXv3_9rPV3iA9uZ0QfVvtd3Xt5BBrqu9A4hCN15MQ16Cj30IkPKsik0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGgCYKVvKx4HEiqawZex3tQ7QaXXLzzO9EjrpJsVBDyjY7XHS7cGhilTuoZlTULO7ollAbEuVAGhEJ2BiJmBahJ0qfn7T1NWV56NTkW1kqAsO8c6AeuYQbIq0oyEMD6J56PcDBfz_IK_rRIisapvP8H0Tb1jQ2U_eaM4aUAu679Wl9n7f4GsluoVK9tuW1cI8pvx_tqFoxo8vIOir2ltxKX6gpbsGAZi_27KAKY9YtZMXR7kRCM84HA90mpv3cQODfY3lB_YNN9OSN0bdpdabKiW_hF5Mh8TC9fVhHEB_PER3KPzr88-zPepJEG7tCJepGVILiEHQU4iOFl-L66DGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0gwXEJcodMBtLFRwbbzDJLDYCagEb1J8iSGY9HjEY8n0aQK_4UCETuxL9q0anX-MlRJM17EsmWt7yOJGou5c6MwI9uCRmAanSuDXqWJfjOuY-xAdM01hEsb1bEK5ICkxGGtugKOjq5BXsMhVYPFT_Itn3Uyj6F4s5QSR4yndZ9SfPamGYmv0w1UF6nX_rmfOpW1loP7OBYS0PhXL_HsBkNXfaSkrDIlvBxd2Ix8uxyGC4WY74Ydhs3eJATypU8QYehvxO9h6ti23OgNAEUdpIZDg3S6sYbba6PHM2ZdTXfnmFz00gybgcuBqm8j-08HR4o4EOnLNecBNGMebXnJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgMfhAtRMoA3GZ3YaSHFarPbhA0CV2gO4JEBSHG8uHyfb81SstYyuUxqdwisadMKBh4VSS-lSzAYkOqBo480edUHSEFpwEilRVzYiLXKq8WKwCIv0-vEkCUqkdOdBFq84rvrRJK5jJu8jUB_HN0TPj5fDQs87j4SbK4LnmKzMFrTT_rhC90g07u12vbFAK22WYrEDp5j3OEX3zLnFff7fZbmauZXazy0UW8RXwPtfhZBKjwJh91J_tJ6nTZIrm9hzZlcgiFMhyw0e3Uu1zZFS_eKxVptM6GsZCOKUtJRLGVt4QFs4OnTRRVyzSS9f8H4zk8WFYagd2qutu-96T6PXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxG86uXFHo8enQfz1b7GZRYZBO_tA3-bfqzokoisTJmDqt157wEIl181ssLz80FpZavLaDSuk9-giIeLp05Mdcgq2wVPUPZ4DD6Nokac1YSHbPcNpzztO6HdCngHSp9-AOl2xoSiucB0FIiw4XVtcohv2SWwBIb0S03peSr0XVdCBBTHUg76zB_qTTFG0ZS_EppW2ub2wPZ8wuKAyauh20l-csrCsOMrRw_9uggM5a1n7QzL8S8JBaLoTS2TzpECeLBmU132rzWibu4TG9Q0pD939r8B9X7C9M0dtet6F-cAoBC70TcR2-iWAw-AUV0WW-9F1uIlTbp23gfiNmaqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
