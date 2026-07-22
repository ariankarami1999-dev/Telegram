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
<img src="https://cdn4.telesco.pe/file/Ml7TZqxbaiyyDsI-0ITTrK0lpT59cTsxjXnDQHGIjjpeEZ1cYn78JwS_B2gN7Virv6MT1fnrXY2duJxqYAqXYpXCSS2ZTJAr8VIyXcXkZzh4E9kSHEXApyMAqi6xnPB_CvbIBM3VPcAacmKlCVVgyb2XRSCx856OtAeUJZ9VJvJ9ZoUplQUUMU42_bGVlcHyt-HEC71SUox-xU6HBWtUBjkKptXr0BXs24YpNmxAXHKJ-chUNGTQMwZh0kNxwh4I-Z0JEkvcMx9O77u0l5tV9SZszdLkv6plL66TqWXsVzgdyq_JjOYWVvEZTEOWCgeUWOKk5svrnunin8fUSyP3zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-451826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24826791a5.mp4?token=mjQZV5e__Akus2KoA04_C82wXYR_k8P0BgazlGvLfgEuiViYGipmRElItf8QsKS9VDuUBUw6-3fPvqA8t_OhoSvkifzOVA3fIs3urGGkjIHWUnzhVVgIUwaI7oq0449SRMiNI9xcL99mVMBYYxqe1qssfRfTPDRni7MhcZPigzO2NId51_E6ZfSLtxCGoiVgxc_pbv7dka-6HAf_H5G5XcR5ee4pHG3vzqq_QHu-g54CoguY_KmsOrgwKS3RHZJfsqxx29majP6HDzUmiLK2lJwcisy-U-QWwOQa6XMUMKd1HrCspQPrCXrysRVDjEkk6wHpr5jCIaMqC7OJcr0rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24826791a5.mp4?token=mjQZV5e__Akus2KoA04_C82wXYR_k8P0BgazlGvLfgEuiViYGipmRElItf8QsKS9VDuUBUw6-3fPvqA8t_OhoSvkifzOVA3fIs3urGGkjIHWUnzhVVgIUwaI7oq0449SRMiNI9xcL99mVMBYYxqe1qssfRfTPDRni7MhcZPigzO2NId51_E6ZfSLtxCGoiVgxc_pbv7dka-6HAf_H5G5XcR5ee4pHG3vzqq_QHu-g54CoguY_KmsOrgwKS3RHZJfsqxx29majP6HDzUmiLK2lJwcisy-U-QWwOQa6XMUMKd1HrCspQPrCXrysRVDjEkk6wHpr5jCIaMqC7OJcr0rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهدای مدرسۀ شجره طیبه میناب  @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/451826" target="_blank">📅 11:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/451825" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce52e2213.mp4?token=WiCEle5X80Qob-bi5ZjqRdDegpjTQAPiIFutex3iD533H9-aLD7J2Xqe9t6TgO6LxIL0xLAcQmJDCGmLJw3n5nQfRu3ghOSXKoGjB7iKyPuAOEndazZR8bcfmV96qyNeL3HTAe-Ub7R7P_3Oex_cOlz16rF-lL1Rim06W2ZdC5U1lAYArIRa1y4alneotzVMpzwTHhtfhqTvuM1MnuSaG6VFZR-2D5RcgZDVLXvQg1nkvR1Kg11Kbn57V_-yhgL2m6PRz7KRDsWgjPSLeJ2d_JykTgd3gBEWkbdYjLUZ9rtxA20NT77690vE2Jq3bLHHQRG1eof-hS-_xCj3Y7b9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce52e2213.mp4?token=WiCEle5X80Qob-bi5ZjqRdDegpjTQAPiIFutex3iD533H9-aLD7J2Xqe9t6TgO6LxIL0xLAcQmJDCGmLJw3n5nQfRu3ghOSXKoGjB7iKyPuAOEndazZR8bcfmV96qyNeL3HTAe-Ub7R7P_3Oex_cOlz16rF-lL1Rim06W2ZdC5U1lAYArIRa1y4alneotzVMpzwTHhtfhqTvuM1MnuSaG6VFZR-2D5RcgZDVLXvQg1nkvR1Kg11Kbn57V_-yhgL2m6PRz7KRDsWgjPSLeJ2d_JykTgd3gBEWkbdYjLUZ9rtxA20NT77690vE2Jq3bLHHQRG1eof-hS-_xCj3Y7b9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده کل ارتش: ارادۀ خدا پیروزی مردم ایران است
🔹
ما با ارتش‌های سران کفر جنگیدیم، آمریکا جای فرعون نشسته و تصور می‌کرد که هیچ ارتشی در جهان، حریفش نیست ولی ما ایستاده‌ایم، تنگه هرمز را کنترل می‌کنیم.
🔹
ما به آمریکایی‌ها شلیک می‌کنیم، آن‌ها باید بدانند که جمهوری اسلامی ایران یک قدرت معتبر است و به عزت ملت ایران اذعان کنند.
🔹
خیلی‌ها منتظر به ذلت کشیده شدن ملت ایران بودند اما به برکت خون امام شهید و همه شهدا،  اراده خداوند متعال، عزت و پیروزی مردم ایران بوده و هست.
@Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/451824" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e40b4184.mp4?token=M-LluhqRUtperX5o_nOn-ciZELaqLnr6E11VaO8FsaajcvBdm2Uia2ux3-BnylbkAUK-3weDexffQ51ND8MOub2ghl1f5lSjLdP_Q996gogpzJgrqSgBjAL1WFBsb4oZZ-h_5k8kUFKRK4SK7efftG2uh9DVMm-aCme0C1hcdyG5tjqe5rQib4oroNq4vD_wpjdW0Dx5UoRwfrfthIjtRgFpMQbMfkvHNHTV15C4RIYAdIVlb7sdIwtuJ6VFOiLM6u0KRg-UBvnAX5j6l6aeB18EPPfchUiRRp75PAm0gXExLWr-uB_MWJmWiaeU7kL0VMI0hV1retZbcuEXrlS1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e40b4184.mp4?token=M-LluhqRUtperX5o_nOn-ciZELaqLnr6E11VaO8FsaajcvBdm2Uia2ux3-BnylbkAUK-3weDexffQ51ND8MOub2ghl1f5lSjLdP_Q996gogpzJgrqSgBjAL1WFBsb4oZZ-h_5k8kUFKRK4SK7efftG2uh9DVMm-aCme0C1hcdyG5tjqe5rQib4oroNq4vD_wpjdW0Dx5UoRwfrfthIjtRgFpMQbMfkvHNHTV15C4RIYAdIVlb7sdIwtuJ6VFOiLM6u0KRg-UBvnAX5j6l6aeB18EPPfchUiRRp75PAm0gXExLWr-uB_MWJmWiaeU7kL0VMI0hV1retZbcuEXrlS1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض به جنگ با ایران در قلب سنای آمریکا
🔹
معترضان آمریکایی در جلسۀ استماع کمیته تخصیص بودجۀ سنای آمریکا با پلاکارد «نه به جنگ با ایران» و سردادن شعارهایی علیه حملات آمریکا، خواستار پایان فوری جنگ شدند و آن را «غیرقانونی» و «منفورترین جنگ تاریخ آمریکا» توصیف کردند.
🔹
یکی از معترضان با اشاره به مشکلات اقتصادی و معیشتی در آمریکا گفت: «مردم اینجا خانه ندارند، انسولین را به‌صورت سهمیه‌بندی دریافت می‌کنند. ما مخالف این جنگ غیرقانونی هستیم. ما به مراقبت‌های بهداشتی نیاز داریم، نه جنگ. من شاهد هستم که مردم آمریکا دارند می‌میرند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/451823" target="_blank">📅 11:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZJkfy_wDTc9P9Uj1ARDwD7mITi1KIWABDUasQMIRR2VU4iRcqk4H4OgdMY_VlpbH8s8PVzXUiOAzIH1EoixMHpy2bhk4AoX-Uos9uZauQF7g6zvjNsZ7QHqAQ_tQOH-sJ8daZMDST2jvqWA5wLwQrv-lb_uln4vDleKP6nOdFTXBiPUpZkXyl4nzKMsDnnOg4mLHubU6f1TNHyQgehPEX773jyv04CzjaBZJNO4pimdW7fgsPJC_9iUMWvOiDfD6-tXScEgr7YIS--yWk5Qcq0zdvdN5OYEzkKqBtnNNJaL8MVTbDqYog5x0_fWF1Kn9-U-TTEb4vsuy15QRTCABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفهٔ ۲۵ درصدی آمریکا علیه کالاهای وارداتی برزیل
🔹
وزیر خارجهٔ آمریکا اعلام کرد که به‌دستور ترامپ، تعرفهٔ‌ ۲۵ درصدی علیه اکثر کالاهای وارداتی برزیل اعمال می‌شود.
🔹
دیپلمات ارشد آمریکایی در توجیه این جنگ تعرفه‌ای مدعی شد که دولت برزیل در مذاکرات با آمریکا،…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/451822" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR-ePPK0G6xcKTKpQtr9SyK6SnDgNJ6JpyWEXCqwziCNsQ3E5lIubdR3SFxtMt7mib_oVJjQ4vDAhuIlcNib9wtNwbQ1OvvGRJZphTirEtpUiad1_fEgcpuEFrcWIlZIhduk8UI7Lmg5VK_3LOFFt9oTlu4wkKBegX6iHJHpTH3hOyxqyu7u8Gm6o1MwZxF9XCxwOC0GMac8ORLoxEUUCUy1I31y15U3wPYpu09HzFtO-TGk-VLZBPICBshXHOf9ZUA96OmeaUuTNm7DJJDKkB9sQKkJ1fdd4jeeh3HUiIGdJnItvUuYOPkhJSLLs7aa9YBAqkO-1-x9pDcmCXPzMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جراحت» بیش از ۵۰۰ نظامی آمریکا در جنگ با ایران
🔹
خبرگزاری آسوشیتدپرس به نقل از یک مقام آمریکایی گزارش داد که بیش از ۵۰۰ نظامی این کشور در جنگ با ایران زخمی شده‌اند.
🔹
طبق گزارش این رسانه، این رقم بیشتر از آمار رسمی پنتاگون درباره تلفات جنگ است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/451821" target="_blank">📅 10:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام تسلیت رهبر انقلاب به مناسبت درگذشت مادر شهیدان مظفر
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای رهبر معظم انقلاب اسلامی در پیامی درگذشت مادر گران‌قدر و پرهیزکار شهیدان مظفر را تسلیت گفتند.
متن پیام رهبر انقلاب اسلامی:
بسم‌الله الرحمن الرحیم
🔹
جناب آقای حسین مظفر! سلام علیکم؛
درگذشت والدۀ مکرمه و مادر فداکار و صبور شهیدان سرافراز حسن، علی و رضا مظفر (رضوان‌الله‌تعالی‌علیهم) را به جنابعالی و سایر بازماندگان محترم و خانواده‌های معظم شهدا و ایثارگران تسلیت می‌گویم.
🔹
این بانوی گران‌قدر و پرهیزکار با پرورش فرزندانی مؤمن و متعهد به دفاع از حریم انقلاب اسلامی به مقام رفیع قرب الهی نائل آمده است. امید است روح مطهر ایشان درکنار ارواح طیبه فرزندان شهیدش، قرین رحمت و رضوان الهی گردد.
سیدمجتبی حسینی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/451820" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حضور با لباس یامال و پرچم اسپانیا در مراسم عزاداری محرم شهر
🔹
بعد از قهرمانی اسپانیا در برنامه «محرم‌شهر» میدان آزادی پرچم این کشور به پاس حمایت از فلسطین برافراشته و چرخانده شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/451819" target="_blank">📅 10:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏆
🥇
لحظه تماس با نفر اول  جام دی (دی کاپ)
🎬
این ویدئو ساعاتی پس از پایان فینال جام جهانی ضبط شده است
🥈
🥉
🏅
🎖
گفتنی است ویدئوی تماس با سایر برندگان  هم به زودی منتشر خواهد شد.
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/451818" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451817">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/451817" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b84671ec9.mp4?token=VrBh0NAF9Q4LsQ4LUE-7D21NKhlzdejaqnk197bPe1r9pdoIzGyhDKjrLY0BqqyWkcMm-C3e0v2QlPdfYCP4B8m6jfCPD3Ki2jBRXvvjzPnS-UdSJUQ41m5hkcMqHrGgybZqqj034pMi0iWVLfCI9s6YFyev4YYw3eXh_8r3Pe77cVfdN9j_XscEp_Ui8iXCTPQeX5FWM9PK5iagPVIUEigOvHpungL4yhUb0_rBGXX98Z65djG9kwf63ffQvbjUGfNcx2zYIIim0gPJ95LqowqVO8hJCNpzqwFn86dV2otM7CrP4crBd3BR4rOpykwTNcJrGCh4B7gZBWo7nUj_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b84671ec9.mp4?token=VrBh0NAF9Q4LsQ4LUE-7D21NKhlzdejaqnk197bPe1r9pdoIzGyhDKjrLY0BqqyWkcMm-C3e0v2QlPdfYCP4B8m6jfCPD3Ki2jBRXvvjzPnS-UdSJUQ41m5hkcMqHrGgybZqqj034pMi0iWVLfCI9s6YFyev4YYw3eXh_8r3Pe77cVfdN9j_XscEp_Ui8iXCTPQeX5FWM9PK5iagPVIUEigOvHpungL4yhUb0_rBGXX98Z65djG9kwf63ffQvbjUGfNcx2zYIIim0gPJ95LqowqVO8hJCNpzqwFn86dV2otM7CrP4crBd3BR4rOpykwTNcJrGCh4B7gZBWo7nUj_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: تا به امروز یک میلیون و ۳۰۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/451816" target="_blank">📅 10:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451812">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1795ed65.mp4?token=s2QlXLQ7aH5ViWUH4taUbapfR9_tYrIKPddupO29BkK23N_flP5_CwWVQml1WXUoaPHSsDcPwT5djQS1l_gpOcZd7TEO-0p6wMwq0_kbMWl0AGTx3bEnVFn68FASAcbsWiMAZJWYXpOUddkeTfbFyavf1CxgWu7Y5w4fszSShYurIGJpgku0fs6-adceQ8hPDn1MpgDrBZ5YU4D8rQzKtA8SlP4wNFkSVTCv4UA-nPwQNZgbQjIKAUme-2JrA_QgODII6cwg2cR9IKJQqExMqe3TkeHxunarwr_gca913JkzlLPKtrxPTAAGrlTuI09XeKLN5EZsWU8k3YYpqsBTqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1795ed65.mp4?token=s2QlXLQ7aH5ViWUH4taUbapfR9_tYrIKPddupO29BkK23N_flP5_CwWVQml1WXUoaPHSsDcPwT5djQS1l_gpOcZd7TEO-0p6wMwq0_kbMWl0AGTx3bEnVFn68FASAcbsWiMAZJWYXpOUddkeTfbFyavf1CxgWu7Y5w4fszSShYurIGJpgku0fs6-adceQ8hPDn1MpgDrBZ5YU4D8rQzKtA8SlP4wNFkSVTCv4UA-nPwQNZgbQjIKAUme-2JrA_QgODII6cwg2cR9IKJQqExMqe3TkeHxunarwr_gca913JkzlLPKtrxPTAAGrlTuI09XeKLN5EZsWU8k3YYpqsBTqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای جزئیات جنایت میناب توسط اسکای‌نیوز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/451812" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451811">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG8jP76LyBOdiVd3p6VVTwjmXZlHR1LpjirqVXwplBzJ_Fx5YZYXStXxyIHjNeIhHIynwnq-JOW5cZ8ncNebS1XdFIt25SylOhBj_jnlf8C7qyowTbRbEQT6FcBdU-gTSTdlVV82WwATLxBPgjBHr6ljyJ4FKkHqQPz-Mj_0UEX95aaV9zMS4nBiNhTDPg6bP2CJ5EiVrgz-3UF1nbBSF4E-5CYx0bsUnZkmLGkcWS-QJbwHPiRYbiBHiV0Pqn_t2pSh-QTrTJSI9Rvyr1SvubkQfaoRZUbSHotSiDOUBztyl_yGefgMzX9GoEvn3gKzMlRSFnaTj8JMZhOGmCEujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمانی کاهش نفت و بنزین آمریکا با انسداد تنگهٔ هرمز
🔹
داده‌های مؤسسهٔ نفت آمریکا(API) نشان می‌دهد که ذخایر نفت خام، بنزین و فرآورده‌های تقطیری ایالات متحده در هفتهٔ منتهی به ۳ جولای (۱۲ تیرماه) با کاهش مواجه شده است.
🔹
براساس این گزارش، ذخایر نفت خام آمریکا حدود ۳۹۹ هزار بشکه، ذخایر بنزین به میزان ۲.۹۳ میلیون بشکه و ذخایر فرآورده‌های تقطیری(گازوئیل و نفت کوره) نیز حدود ۱.۸ میلیون بشکه نسبت به هفتهٔ قبل کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/451811" target="_blank">📅 10:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451810">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9OjfZxOZqJS_qT4glA0Lvgn5Szr-OpJTzEQ3uITMXX1MmMwq55nfeKXrejErfx_A3wc63bue00qE40dzwcpeKYfe8wcO6WtDXJ9IZ-URDm6a2dqavgf_TGBo9c8a67niQd8KHgxGeaKR-lRPOqQfTrJWdj39VcE2B2ZI0yV_L7pW_DCkRL05nCfvx9XK5cMjYYFhFInYzIRLpRbXMhcnRBo3jyQBL_JPQd-x4pcm4b8I87ZhoK82H5EJha4pevtAhC5zYkwro45JOr3w1Lk9lP2beJgQOmEWMlSm4kmkHjbiK0tDhO0nD1fSHKb69bdNPCqK6V3qbFAgc1oWxhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند تعلیق پرواز به اسرائیل را تا مهر تمدید کرد
🔹
شرکت هواپیمایی هند بار دیگر آغاز مجدد پروازهای مستقیم خود میان تل‌آویو و دهلی نو را به تعویق انداخت و تاریخ جدید آن را تا اول اکتبر ۲۰۲۶ (۱۰ مهر ۱۴۰۵) اعلام کرد.
🔹
این شرکت دلیل اصلی این تأخیر را «ادامهٔ نااطمینانی‌های امنیتی» در منطقه عنوان کرده است.
🔸
ایر ایندیا پیش از آغاز جنگ غزه در اکتبر ۲۰۲۳ (مهر ۱۴۰۲)، هفته‌ای ۷ پرواز رفت‌وبرگشت بین ۲ پایتخت انجام می‌داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/451810" target="_blank">📅 09:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451809">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77fdddf31d.mp4?token=DUgHWmY_J2FBxONPtFMzq12ezsuY8fF4zY-Ya_igjaIeFJQPgkGjBv776Mk5HRX07ewpK-j1KeQOra1UbC0gav9mm7VD8R9-OiddfwxS8oLlVZdYtWPzPT-WuCFXQrQjkM0E2ieRhZ99gHFQna3uxbpnkrkqrtMwjj3OVZKs3am_hlE5qVAcnVO-ZipLNsHCCZnynhbm1io4sJOoTA88S5qdp6AjJMabhigXAG9Nsbw6KsTtX4E1brpn1THo79RQZOp8MO8rPelYrvvxI64aX9a6XD4O7Tu4vYcZxTnF0MCDGbLYePz_NiXs2ZdV2n0IT5bpbjvYLN_JVKm0WzieNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77fdddf31d.mp4?token=DUgHWmY_J2FBxONPtFMzq12ezsuY8fF4zY-Ya_igjaIeFJQPgkGjBv776Mk5HRX07ewpK-j1KeQOra1UbC0gav9mm7VD8R9-OiddfwxS8oLlVZdYtWPzPT-WuCFXQrQjkM0E2ieRhZ99gHFQna3uxbpnkrkqrtMwjj3OVZKs3am_hlE5qVAcnVO-ZipLNsHCCZnynhbm1io4sJOoTA88S5qdp6AjJMabhigXAG9Nsbw6KsTtX4E1brpn1THo79RQZOp8MO8rPelYrvvxI64aX9a6XD4O7Tu4vYcZxTnF0MCDGbLYePz_NiXs2ZdV2n0IT5bpbjvYLN_JVKm0WzieNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه و مراکز مهم آمریکا در کویت هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در پاسخ به تکرار تعدی دشمن خبیث به مناطقی از کشورمان، ارتش جمهوری اسلامی ایران در مرحله بیست‌ویکم عملیات صاعقه، ساعاتی پیش، انبارهای مهمات و  تجهیزات لجستیکی مرکز فرماندهی نیروهای…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/451809" target="_blank">📅 09:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451808">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حکم اعدام عنصر فعال یک گروهک تروریستی در کودتای دی‌ ۱۴۰۴ اجرا شد
🔹
با گزارش مأموران سازمان اطلاعات فراجای البرز مبنی‌بر اینکه شخصی به‌نام «مهدی خانکی» ضمن عضویت در یکی از گروهک‌های تروریستی ضد انقلاب، اقدام به نگهداری اسلحه و مهمات جنگی کرده است با صدور دستور قضایی، ۲۱ بهمن در کرج بازداشت می‌شود.
🔹
در زمان مراجعه ماموران به منزل وی در کرج و در بازرسی به‌ عمل‌آمده، ۵ سلاح کمری، ۹۰ فشنگ، ۹ خشاب، ریموت‌های انفجاری، ۱۱ نارنجک دست‌ساز، ۱۲ منور دست‌ساز، ۳۰ لوله منفجره دست‌ساز دوش پرتاب، بمب‌ها و سه‌راهی‌های انفجاری با قدرت تخریب زیاد و مقادیر قابل توجهی از مواد اولیه ساخت بمب و مواد منفجره کشف و ضبط می‌شود.
🔹
متهم در تحقیقات و بازجویی عنوان می‌کند از سال ۱۴۰۲ عضو یکی از گروهک‌های تروریستی شده و فعالیت علیه کشور را در راستای اهداف گروهک ‌آغاز کرده است.
🔹
در تحقیقات، مشخص شد وی چند روز قبل از شروع کودتای دی سال گذشته، سلاح‌های گرم و مهمات را از مکانی که با ارسال مشخصات و فیلم آن از سوی رابط به وی اعلام شده بود تحویل و تجهیزات ارتباطی را هم از مکان دیگری در ماهدشت کرج به همین روش دریافت کرده است.
🔹
نامبرده به اتهام اقدام عملیاتی به نفع رژیم صهیونیستی و آمریکا و گروه‌های متخاصم و ساخت دوش‌پرتاب آماده ‌به‌کار، ۱۰ پرتابه انفجاری و ۲  ریموت و سه‌راهی‌های انفجاری و نگهداری ۵ کلت کمری به‌همراه ۹۰ فشنگ به استناد «قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی» به اعدام و مصادره کلیه اموال محکوم شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/451808" target="_blank">📅 09:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451807">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار کنترل‌شده در لردگان چهارمحال‌وبختیاری
🔹
سپاه چهارمحال‌بختیاری: احتمال شنیدن صدای انفجار کنترل‌شده تا ساعت ۱۵ امروز در محدودهٔ ریگ لردگان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/451807" target="_blank">📅 09:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451806">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن به بوشهر
🔹
فرماندار بوشهر: دو نقطه از شهر بوشهر مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حملات تاکنون شهید و مجروح به دنبال نداشته است.
🔹
در جریان این حملات پدافند هوایی بوشهر برای مقابله با هواگردهای متخاصم فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451806" target="_blank">📅 09:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451805">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0705c2a9.mp4?token=bgzIwmDhvG1IpKqLQYIhdzeFUPRatG0aUAItL6RJIc_XodfhOCvJL9BX5_-mmAz0EFf80WIJ9lcTdvHVtz1jWL9HZj_9j8Gw146HXTsfGhtjm8ZlvqXvrm0snev_ofWo-ekXPIPsUTDeGgzti42HGytIwIv7MZeyEecHlMDm0_TKYAL7xsivPRB_MCFbqbhPHpuvJc0SODJwUH4DGPoDJ_dsi4T00fkMoDXqyc6oYfcC4Li-H7sFJFBYfC-nOkNsv3LaFfW2uUCmWYipQR5ES-nolxYK8H6JJz9RSMPOFMSv40Yp8tJsQ_wfHwntUV_PaQO2Y7Z4xGcRkI9luzmdKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0705c2a9.mp4?token=bgzIwmDhvG1IpKqLQYIhdzeFUPRatG0aUAItL6RJIc_XodfhOCvJL9BX5_-mmAz0EFf80WIJ9lcTdvHVtz1jWL9HZj_9j8Gw146HXTsfGhtjm8ZlvqXvrm0snev_ofWo-ekXPIPsUTDeGgzti42HGytIwIv7MZeyEecHlMDm0_TKYAL7xsivPRB_MCFbqbhPHpuvJc0SODJwUH4DGPoDJ_dsi4T00fkMoDXqyc6oYfcC4Li-H7sFJFBYfC-nOkNsv3LaFfW2uUCmWYipQR5ES-nolxYK8H6JJz9RSMPOFMSv40Yp8tJsQ_wfHwntUV_PaQO2Y7Z4xGcRkI9luzmdKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر هوایی از تشییع پیکرهای فرشتگان میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451805" target="_blank">📅 09:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451804">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127444c42.mp4?token=i-4pblXWEAYUdYtaPFhtp4z265hHdk44t0eW-T2DYf3JwOwmpyKC30lnQx34xsax4zLUlp0wE5-u8_qlAfS19KLS-Yvy0qucI1zmrpyy9v-Sk2DkMzgeQM2Keb5HPH3C3qzENEJ_XFoMC4FY2pf4khQYI3vwrbhXdqgwq3VWSWx7fTF4iCOULv_51MB0T7gXYK1yGSJ_HdeqNKL8PX0nYtQdsKHWz5utrrR4Eu8gQZux5z8r4RLZw6H_V4Ne58p_ScLdywVY6XeyM92KKrWlGc9Fr9pAWScdnoo8ZmrH2g40R5v_KuqRdABYWIigQ-Vy96wvCkhRxtOVyts5KzzsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127444c42.mp4?token=i-4pblXWEAYUdYtaPFhtp4z265hHdk44t0eW-T2DYf3JwOwmpyKC30lnQx34xsax4zLUlp0wE5-u8_qlAfS19KLS-Yvy0qucI1zmrpyy9v-Sk2DkMzgeQM2Keb5HPH3C3qzENEJ_XFoMC4FY2pf4khQYI3vwrbhXdqgwq3VWSWx7fTF4iCOULv_51MB0T7gXYK1yGSJ_HdeqNKL8PX0nYtQdsKHWz5utrrR4Eu8gQZux5z8r4RLZw6H_V4Ne58p_ScLdywVY6XeyM92KKrWlGc9Fr9pAWScdnoo8ZmrH2g40R5v_KuqRdABYWIigQ-Vy96wvCkhRxtOVyts5KzzsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ میناب دوباره تازه شد
🔹
در کاوش دوبارۀ آوارهای دبستان شجرۀ طیبۀ میناب، ۶۲ پارۀ تن متعلق به ۳۲ شهید که پیش از این به خاک سپرده شده بودند شناسایی و تا دقایقی دیگر تشییع خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451804" target="_blank">📅 09:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451803">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d8875669.mp4?token=mdQj0EAjlCqT_x8PlqugwkzaRTpeplSWC_0B45aVGRVmRWmeufM-yTp5unu7u-fDrZkt6MHsHBQU4U_uLYvT8-xNdkDLhXh7xcS7p_eDURLmF2leNcAlv0y7XY6hb3g1WIkkOY5Y0nkQhtfpw7XgSglQNI5VohsjJqnsNA2pFLHubffRawIIakUBMdoJQe_l1CkyrQRSt6Qw5S_lAD1zbvOs-ObFUK80rpqb6hWN9VDpKVEKZFtqJQLiMWq8zwm5R7vzkNhAeeqsZ4lDcYNmSrXHQ6LbgIhePw59EAYiQ_4IAU0wa-Qh5IXDTpfuePxoHWwHr4za18G9y8YHwhCC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d8875669.mp4?token=mdQj0EAjlCqT_x8PlqugwkzaRTpeplSWC_0B45aVGRVmRWmeufM-yTp5unu7u-fDrZkt6MHsHBQU4U_uLYvT8-xNdkDLhXh7xcS7p_eDURLmF2leNcAlv0y7XY6hb3g1WIkkOY5Y0nkQhtfpw7XgSglQNI5VohsjJqnsNA2pFLHubffRawIIakUBMdoJQe_l1CkyrQRSt6Qw5S_lAD1zbvOs-ObFUK80rpqb6hWN9VDpKVEKZFtqJQLiMWq8zwm5R7vzkNhAeeqsZ4lDcYNmSrXHQ6LbgIhePw59EAYiQ_4IAU0wa-Qh5IXDTpfuePxoHWwHr4za18G9y8YHwhCC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داغ میناب دوباره تازه شد
🔹
در کاوش دوبارۀ آوارهای دبستان شجرۀ طیبۀ میناب، ۶۲ پارۀ تن متعلق به ۳۲ شهید که پیش از این به خاک سپرده شده بودند شناسایی و تا دقایقی دیگر تشییع خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451803" target="_blank">📅 08:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451802">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46a0d7e8f.mp4?token=RWO55SfaymKbSsvcRu3QqhCf3mt5UafS7G53OrbFAOVFgdlt_nW-5dNiRdmVgdF6wnqCEo2yeuA8EtWYaJbPnQcsm1nCfgYW0ij8D1XhhOc4CuJSfvksFyp5eoZMx3BHSdaY2WD8N-YNFKs5ZI0W4tMsBqSP2XY2CMP0_9Q-SORK4u3EG8fvowIKwuyvXtlD-9XcXVEkWPQnZ5U7fAtjNNqRdYlWMP3zTfI2RIubxE1ag-7CtWC572BiUItZKkSHSU94ieEjoN_QEa750n6BV4pCrVjOHEW4apV0D87J1awMByhhZnLOWHIS1xWxNMP0jtzwxyjl-EeRhR9O48nenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46a0d7e8f.mp4?token=RWO55SfaymKbSsvcRu3QqhCf3mt5UafS7G53OrbFAOVFgdlt_nW-5dNiRdmVgdF6wnqCEo2yeuA8EtWYaJbPnQcsm1nCfgYW0ij8D1XhhOc4CuJSfvksFyp5eoZMx3BHSdaY2WD8N-YNFKs5ZI0W4tMsBqSP2XY2CMP0_9Q-SORK4u3EG8fvowIKwuyvXtlD-9XcXVEkWPQnZ5U7fAtjNNqRdYlWMP3zTfI2RIubxE1ag-7CtWC572BiUItZKkSHSU94ieEjoN_QEa750n6BV4pCrVjOHEW4apV0D87J1awMByhhZnLOWHIS1xWxNMP0jtzwxyjl-EeRhR9O48nenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چابهار و کنارک با توجه به شرایط جنگی همچنان ۶۰ درصد از شیلات ایران را تامین می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451802" target="_blank">📅 08:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbV3vPd17tnxDJ4zHuRo1TqwmefjmjrZKjM3U6EnpLPvGdg81xzzKAwiuDb08AH7mImeggvxewDJoy1g5LkZJIbC6NY8JPopawX9kHWdVltuoDIfhczCchuwyZG69qOeUHayInftScQkegOkxPKj9UlLV6PvMBNq_gVRkZxPyRRYdShclZg84EsgrjkJTLJGB9i6OIY4HWOqSMbSg8r6oQ_tf0IPvL-1wvUyH9wHotrBw4cky7ViPxVwBNX4kyN3tz6bABQ9-huHlg7CBYWJpyH6OX7CoOr4I6boFfzieE6UmEhukv_wm17gU5xr4z1cUcSrXVMD6A5OaHThe975Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0EL5r9fsNNPPtNWQcKmo45JqEd5nbUU7GAWv_jSaOy5DzbtHirRErfd9F4YRBWIlkKkYjW3loCy8xa70MZzvcFzPLO9N76Jtk6gmAeh1fiHWTfPR_IGF40PNNnBAq6YmGp0cM6fGFCN0k5eGv5WWA0DOoWUUyEOkCQwQt16t7-hbmBP3JNdE2EZ8u7rvNuv3F-9QPs2ciw3h1fNMAnmligIAKmkf0RqAIpoyC_YBnQGNxrD5Cm1DC659xaCv0CVNU-ZH_xm4S201PQsaW0JGtAZMKAotOdTEJ81CXkU9ihOaZGRVy7nZWR5q_j8T-Rntp6DIjgHvcPLo3qPRHXGPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آماده‌سازی قطعات تازه تفحص‌شدۀ پیکر شهدای مدرسۀ میناب برای تشییع
🔹
این قطعات با تست DNA تشخیص و تفکیک شده‌اند.
◾️
مراسم تشییع و تدفین اعضای پیکر مطهر این شهدا، ساعت ۷:۳۰ امروز در میناب برگزار می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451800" target="_blank">📅 07:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451795">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8azdGQxMFPmYDhcJaeiMqdeIxt1keC-z2TlbKlXzc7xit6fQvVoMHDGIAAi44nP3ryKJY8z9mNlffhtvZZm7rkyRvXIt3gyKYw83qoIh1yNhMzwTSmp139_6SiIS8d4UZAOaA6mdNwDqVE9eFIM3sDCPoXRlWdi7zZt9K4KXRnHgXS-NboFDd4TTrMs1A5DaoXLrmI2iJjKGUR6EDslOVC53IG0cK751dVoLBZRu7LMNS19UbH1wJZ8RYdG192fhHKbycU8hqrchUuj0-XpNc2M139eIY9VuV3sVA1HaDNtbZER4BGhIsDeze5-qs8d4TaYKs4bq73HHKi55Qn_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7j4TtsYA-l7lknaCLL6dztC2STojnG8HgCSvNcf8fW2GMivF4v-yNrqYoRJ0JzNsJMveXUC1f2MhxE14JGvd_Er3Y0XG1TmfAXm-6oVASsm3alhZ3NEMN5TK6gQpRhWRjgAo_oc8_DlbV1NqZmBXjuStztk3JQGi8wQN5MjadqkoONgMDeXH2e6erf8YpCGnPq8btlCGrBDVhwodypgi4CChMhFLm_L3xwWgOT5vNhJqkFALODH4_abVZXOrm5dCi6o8Io-6H6YI4oqVDg-Kku-WEHYjWE-o3aWnBPk6wQaQj-Bv8f1ph3VYh86LlJ1LzFkEaDIufN7HkPgx1demg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVmutTOzBS_cELMy741adOn_MVpYTKpgZ_mwRRCTsO4nYV8kHC5T6hBdD5KKzG1cCeDWWf_PD218s596na79Gbij-vlByDu3-vnBe63WEHAvLuUNhGn_wwKoYeIvfr-Ie6KuSzfDDUorPK9Q2Q1265XkGkKJsmdvX6qfs1vLOew9YM-ml6xaUMFTFBtpTNmO5AQQhRPtzUfrCJoUv2TYniYdRJZxkX1vCRkBU4eYiXI8eM1OBONzEhXM7KtNKDVJLgWMK14iRnilIHE7k9ZK0QmOtS3-13_4UAh_MmzvxcwJ6S_QSYklWkquZCnMZoUXASd7rMM5ztZE3Y7k34WaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNqgYiSmQEeMKRTlu3HRU2tEdPaXw8_IU0b4Yw8FKXnCSFNvkZ_0Rd8NaGMh-hf3IaJ8N3aLiqJpLt7fryqkxPd6U4yWVeZhm_n_snAgqCbuhFOy5aINwd8IfoP-od3vpHH57Y8UgpWw7xgEQzQ68nExG4khC61glxW7oFZ-EKWNGiZYKS0-iAbbYwSvTyMy9NW-mIkSOXX_wJG1N5H0ivpiyNpA99GDUuZLsHYJF0SEJrcKwSu1QvMYxR8V99BVyVaud4Ur4MlbDaVBIlsfa5Rd5MVQzxhweHQn0XhZ7mLLo606F_Oh3Do7bSVwHDJvYT7xtXR74N6j7uUxeQ3T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTLwstDzxsbe5Woj8jGV1p8d2ebggd9eHuyicoLmM5nX2r3puv9xs8_M2IzLcGm8tZKHiw5KfeJ5_08c_oU2C22cnMkDOo239UVHCixzyXMJwT6BE5TQ4w2J4vnqVhdoxK-B7usipGhD2hCzEsKbfJ-2pI53VTzUS1it5VyvgfP3muUh4c-zo4ezrcx-JCnS-IBRW4kWuqJS3ocVhHiJsQkcq33XcWIuOGbRterFLds_IcpuyYCmEBUe6GmA2WuK3yb7jZy2pfcJQO4dktBS6PnKqdwyOwuDDRKq42mKdsTbvXalpM3cVpQY1mctStbnfXNRcbHd42Je9sSKavjyWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزهای داغ تهران
عکس:
عرفان باقری
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451795" target="_blank">📅 07:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrrQEwgULRXU66kCjzt0ZlMjtDrqfpRhcU1lfiberCaLaQd_F09HKx408dg9InwmFo98pZlS9Cs66aFbp8KWpRb7eaH-JHewrhIPA33SUkxaY-Kadt4d9g5qn9NSRljhJIDZmdZaBRIZQNA-xr1p4Fsbb5MSdWbCsLklBIxu46Upw6pS8WOqyMSxVwQ6S4YJ5TxMwOy2qLCKsJU7PYv8rH1HnpKmwp4Pn2KEcGmo2apbx3tQmdtBgws5SDjdncjnMQCLdUd5Ap6XtJ38WUpW4QJcJD5sa1TjkGoAGueVs3_VlJTe9vcQxZ5ERS6V7DLW8guSKxdMReFzTOnlZu-NCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روبیو: ایران برای مذاکرات جدی نیست
🔹
باوجود اینکه واشنگتن طرفی بود که به الزامات خود ذیل تفاهم‌نامه با ایران عمل نکرد، اما وزیر خارجۀ آمریکا ایران را به نقض تعهدات متهم می‌کند.
🔹
روبیو در ادعای خود گفت: می‌خواهم یک بار دیگر تکرار کنم که آمریکا همیشه به دیپلماسی متعهد است. ما به حل و فصل اختلافات از طریق مذاکره باور داریم و این در موضوع ایران نیز صادق است.
🔹
متاسفانه، تاکنون، علی‌رغم تماس‌های مستقیم و غیرمستقیم، اگرچه به توافق رسیده‌ایم، اما آنها به تعهدات خود عمل نکردند.
🔹
اگر آنها جدی نیستند، ما هر کاری که لازم باشد برای محافظت از آن، منافع خود و همچنین منافع متحدانمان انجام خواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451794" target="_blank">📅 06:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451793">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01fd54a95c.mp4?token=KsfUomW2fOzBORbyRMdHNtBLs-5bnl6JUWXwsMJJGPI_eO9wGveLE13Ga52ZtsobTc2pURbU7OWL0Jl6CZQBMcmxQniD0Wi9SChjRDBTgrluIRiu_e5Vu4H1o-RaNYNVRxjVSKvVl7mD1Cyils2vLbrWQTjqVLo7uI69RwdEH9K9As-g-7a9V6YdlyjAp96SJNE-ZKgN5pd4wtq2WKNjaEptHFlVhpFTOSEj8ahrG4hHFol4B7LZ9W1ZpFTnjZTDRaZvMgQR-tT0ENTuz3egg8RBdG3YEN4fDkj_X5opMyg85WAro9PXMnwgqe57_XsUv5vQdeC33z0Q3ALVY6F_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01fd54a95c.mp4?token=KsfUomW2fOzBORbyRMdHNtBLs-5bnl6JUWXwsMJJGPI_eO9wGveLE13Ga52ZtsobTc2pURbU7OWL0Jl6CZQBMcmxQniD0Wi9SChjRDBTgrluIRiu_e5Vu4H1o-RaNYNVRxjVSKvVl7mD1Cyils2vLbrWQTjqVLo7uI69RwdEH9K9As-g-7a9V6YdlyjAp96SJNE-ZKgN5pd4wtq2WKNjaEptHFlVhpFTOSEj8ahrG4hHFol4B7LZ9W1ZpFTnjZTDRaZvMgQR-tT0ENTuz3egg8RBdG3YEN4fDkj_X5opMyg85WAro9PXMnwgqe57_XsUv5vQdeC33z0Q3ALVY6F_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه و مراکز مهم آمریکا در کویت هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در پاسخ به تکرار تعدی دشمن خبیث به مناطقی از کشورمان، ارتش جمهوری اسلامی ایران در مرحله بیست‌ویکم عملیات صاعقه، ساعاتی پیش، انبارهای مهمات و  تجهیزات لجستیکی مرکز فرماندهی نیروهای زمینی ارتش جنایتکار آمریکا در پادگان الدوحه در غرب کویت را هدف پرحجم پهپادهای انهدامی خود قرار داد.
🔸
الدوحه، از مهمترین و اصلی‌ترین پایگاه‌های نظامی آمریکا در غرب کویت و یک مرکز پشتیبانی برای نظامیان آمریکایی حاضر در غرب آسیاست که حجم زیادی از تجهیزات و سربازان نیروی زمینی آمریکا به همراه نیروهای دریایی و هوایی در آن مستقر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451793" target="_blank">📅 06:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451792">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حملۀ بامدادی دشمن آمریکایی به بانه
🔹
فرماندار بانه: دشمن آمریکایی بامداد امروز چهارشنبه یک نقطه در شهرستان بانه را مورد هدف حملات هوایی خود قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451792" target="_blank">📅 06:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451791">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721598e238.mp4?token=e7Kwi3GRbEx3VvMi72dk0LARR5GGj6ygQ7AtVoGwG-YcxsRY5JAvsXRMDA6kWNxxs2EuA7QMNgg1lUkqkn4qhZhKNBvGtgRF_wUmnOYfiNZboUq_bQ_p2PrdNRxjpfTD1L5V8to6XIkOVDpyxJo7hMm3WRi9Gqt1jF0TOPpiReIGuLFn5Mt4sICpkEozaG3m2sy3XrE88wlWtCsqex-mXo3-Ahwegxyi-6iavwfUq6FhYJSCv_tNYY0wwgoi3V6PfsVwbhag1fzKTyQfZ7E5ysViFcCjH6jaA476EydhAoQtcN_ubOVX7FSW1zNqeRqEOTiYUVAyq9S4V9Rlm8CmW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721598e238.mp4?token=e7Kwi3GRbEx3VvMi72dk0LARR5GGj6ygQ7AtVoGwG-YcxsRY5JAvsXRMDA6kWNxxs2EuA7QMNgg1lUkqkn4qhZhKNBvGtgRF_wUmnOYfiNZboUq_bQ_p2PrdNRxjpfTD1L5V8to6XIkOVDpyxJo7hMm3WRi9Gqt1jF0TOPpiReIGuLFn5Mt4sICpkEozaG3m2sy3XrE88wlWtCsqex-mXo3-Ahwegxyi-6iavwfUq6FhYJSCv_tNYY0wwgoi3V6PfsVwbhag1fzKTyQfZ7E5ysViFcCjH6jaA476EydhAoQtcN_ubOVX7FSW1zNqeRqEOTiYUVAyq9S4V9Rlm8CmW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/451791" target="_blank">📅 05:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451790">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT7bwtdo_riwGy-yQmDgOo0m7MaATnj-hSyZ0wi79mfpvy2ntZsDimFkM_n4X8S53Lo_rKGWPLIbI92riM7e5l_tgIZrkjLps-MspvarMZ-nkB7h9qs-J2L6Y319yeyuvgnwyxjgPumz4aj0p-swgesCbSXNPpVEZKP2_X0ERGoygnuH4L7oARHlRuFt5w4ydTZJNTxgVV66jzVZTIg6FXQ0CDyOVYpZhpeZURZIZcoSHKq5HWxcG3Cre1AfiNsjBOMJa5xHD9ScL2IML_8BFm1V6DhQqhpAE-B5tejxbqWVkiFj4_gpU13BahUXQU7xK14tBm9ndVvVFYmAKJaApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت ترامپ با قرارداد همکاری هسته‌ای با سعودی
🔹
مقام‌های آمریکایی از موافقت ترامپ با توافق همکاری هسته‌ای ۳۰ ساله با عربستان سعودی خبر دادند.
🔹
بر اساس این توافقنامه، شرکت‌های آمریکایی می‌توانند تأسیسات غنی‌سازی اورانیوم را در عربستان سعودی بسازند، در صورتی که مطالعۀ مشترک آمریکا و عربستان به این نتیجه برسد که چنین پروژه‌ای موجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/451790" target="_blank">📅 05:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451789">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حملۀ آمریکا به نقاطی در کبودرآهنگ
🔹
معاون‌استاندار همدان: در ادامۀ اقدامات تجاوزکارانه، دشمن آمریکایی ساعتی قبل نقاطی در شهرستان کبودرآهنگ مورد حمله هوایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/451789" target="_blank">📅 04:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451788">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن به بوشهر
🔹
فرماندار بوشهر: دو نقطه از شهر بوشهر مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حملات تاکنون شهید و مجروح به دنبال نداشته است.
🔹
در جریان این حملات پدافند هوایی بوشهر برای مقابله با هواگردهای متخاصم فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/451788" target="_blank">📅 04:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451787">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farsna/451787" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451786">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به بهبهان و امیدیه
🔹
معاون استاندار خوزستان: نقاطی در اطراف شهر بهبهان و امیدیه توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/451786" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451785">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIiEMut_G6_Movwk8iVqUiUUryjXmgOjYpXGvAo96rPRbTHjYgzYD1JMG-DSxTFH2fT0B1u2OkZdOYNh-P7Soh_-MfbzZ14MeBOZ08bBdHgaGNcPehWsKb-_ykzi9S6B48bRadfp-X1LmrP6eSJsZnaKcU4iotvq4wOpqptQPtIwQMJHArOa-SmiPGnxUHttnmDorUxLXNWzoUAzzYYoc1_Sjh3AQDEV3ksz39quQ8waPTb3ZPhx7IENqh4qicMZnaI_gOkYU1ok8aOo47JmC7J68zP9GinJcQbTTU9jQ514UiEj7JKZjxLXj6pBGmILmRYZOo-OkCage3Pb4XGnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/451785" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شمال شرق تهران خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/451784" target="_blank">📅 03:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451783">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در چابهار
🔹
خبرنگار صداوسیما: دقایقی پیش صدای ۴ انفجار، و برای لحظاتی صدای پرواز جنگندۀ‌ دشمن در چابهار شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/451783" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451782">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجارهایی در سیریک
🔹
دقایقی پیش صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
مردم سیریک حدود ساعت ۲:۳۰ دقیقه هم از سمت دریا صدای انفجارهایی شنیده بودند.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/451782" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451781">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/451781" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451780">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در ماهشهر
🔹
دقایقی پیش مردم ماهشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/451780" target="_blank">📅 02:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451779">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار گاز در یک واحد مسکونی در نارمک بدون خسارت جانی
🔹
جلال ملکی، سخنگوی سازمان آتش‌نشانی و خدمات ایمنی شهرداری تهران: ساعت ۲:۰۴ بامداد امروز حادثۀ انفجار در یک واحد مسکونی واقع در محدودۀ میدان ۹۵ نارمک به سامانۀ ۱۲۵ اعلام شد که بلافاصله دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند و آتش‌نشانان در کمتر از چهار دقیقه به محل رسیدند.
🔹
محل حادثه یک منزل قدیمی دو طبقه بود که سقف حیاط آن با ورق‌های ایرانیت پوشانده شده بود. رگولاتور گاز در فضای زیر این سقف قرار داشت و به دلیل تجمع گاز در این بخش، انفجاری بدون حریق رخ داد؛ حادثه‌ای که در اصطلاح آتش‌نشانی از آن به عنوان «کپ» یاد می‌شود.
🔹
بر اثر این انفجار، شیشه‌های همان منزل و ورق‌های ایرانیت و شیروانی دچار شکستگی شدند، اما خوشبختانه این حادثه بدون هیچ‌گونه تخریب بوده و خسارت جانی یا مصدومی در پی نداشته است.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/451779" target="_blank">📅 02:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451778">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c8267b6.mp4?token=e_RhUKQsHs41PfR_RY7gK5ZnvlYxtAgNCdH28cfElCaSrncEQkQAG4myWrbFxuMxNdgSiEQluQBpC7TyThkuLLEQU-g3kr-HnTlFFUiTt6Lm-JlG9IQtDGUuw7d1QOxXFG1eHUgwlbR8Eo1KpWhoQLT5GgZSAVMv0nYQ1nKHnSbwze3S7CNzE46TuJB5xHTi3FODuP5W-vtw4C9DVApb-bREaHVe5p9SIINxff8G1SFiACv_hbtcmRsE8IeEtHuwJSi14jZk8HXgfbg8dRAoVej2A_Y2OXrADy_bQxpnAXNrNcewQMQtFNlBo0XMmrU7RrQHWe8sRKZvdHLALEBTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان حمایت: در ۹۰۰ هزار بازرسی انجام شده طی امسال، ۷۰ هزار میلیارد تومان گران‌فروشی و ۷۰ هزار میلیارد تومان قاچاق و احتکار کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451778" target="_blank">📅 02:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451777">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9171ddf436.mp4?token=AyWPUZffwiuZrIAJUp1NR4eCQG7SlFb649vXeMvA6ZyGSd5IN_PG2aEKorwCkQD4LU0vdyg7hSg8ZiYvV5NAcaRRluA6Tmp-KV8b-xaFjPEFUt2o6g-a2Xr8rApjZG6tCqFizdIOHqdqodGmsWYdwVbUoEo2-88rGgEqLJnIW1Z2TWgtJ9aPDIn_tlZqRMVwo5cxAKDCTWC2xD0mWvrxJhCR_Uhfqd8gfKq3IOlKYClZ07Zz2LbU3vxP8eYhmG9Ckxyu3KaxGEVCtZCZrj7ISVqJNjgN2yKxN_VH9hXrl06g-za-dIjaCgFDDnqEfbc3Tlv1VeOHyhR_PydTikppqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ قطعی برق گسترده در منطقۀ کردستان عراق
🔹
منابع عراقی از قطع برق بخش‌هایی از استان‌های سلیمانیه، اربیل و دهوک خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/451777" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451776">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0a0cb6e0.mp4?token=b3ZEn3fc-Es1OZVBqZmG2g2waf3NoaubbqkIcyBbGB1nPpKv4_dOM4VBB_wWqEdU-7jhhV7k2oxXkPuH52HBPPKQ90Z6GnDpVFcxx2g9tGS13nDBlz9oSMb8ML9b_Mcy9uutKY80ov5a5lkTS8r6rq98AzDyXUpewZIYFBIH961_S7MXWN-WVzGpR9C32xDPEuWlNXp7vvl02F22t3T8JyTPlL-5O5-TvzYjJe9WdCeEhPGvSbJDsToOkFvFCX_tifXBH5JKB2KiKfFRTSSlVlxXV2Cw-5ceY74ZPCFW1fnzSz_BRUy4U6f-mx0ZP6DUhhSDLrQsGok3NfpDtIwNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع صحبت‌های هگزث توسط مترضان ضد جنگ
🔹
در میانه جلسه استماع سنای آمریکا، معترضان ضد جنگ با قطع کردن ادعاهای هگزث، فریاد زدند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451776" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451775">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad125befb.mp4?token=I2eZ9FCAch1imqIYEvANPdaV8OzN0c_jpIhN10JPNZ9xX2y5XcHoy2BbEHxm6J6qMtBptEMf756yWDxHH4l5bbL4iVfQlK9wUqBorDIkrYf4mHhmfVEBVS7equYSamvuOjwnh2bHeZxthGeUtjxJ6DDOD6ODqDPnY9u8-SdHja3cPEyjJi0yxSVDKzdi93goNjK0axOWFr1ll65U57xhGsSRPzvDpRd3loGFoyBT5tECZmFof1lWtdIixTrj3vFjbQ1S1jDTgcGl2M-eznqMt0-xxKvUdv1V_LzxCq3duVFmcW-FAbBAIxg18PMGBsUXHnGa7vQul2Qts-gmRPDbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451775" target="_blank">📅 01:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451774">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLytiPTqOe7LH-NQhS7c38_N2QbKuojCINRlMZ5Hf6-TMmg9GVftWp0u-YPdfPXGr93pph1OLTiLt5DYghyzRpqakZJWKTaKtFX4_kU4ncxn4yxbgcq47aDgC2wiMMuiCKjriV61pI8TTN9C0JORc-AAxIJGJncRSALHisKXQNxWK5B-LVbPHvGEmyxF6AJZiuVxsvb58mNJXWV2IJdeKY-rA-GwVT0KHnN7o7_bf7gVBV7Zpbs31xr6GRHiLznn0-ReyRskFGUk0cAe4UiW8YOTrmRfNwvm3ZtSWtmih1HOhXPNdCi3eN0-BS0OEXwh0WF_-CvKOBfum7lxyeTQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودای رئیس‌جمهور لبنان برای پایان دشمنی با اسرائیل
🔹
جوزف عون در دیدار با ترامپ در کاخ سفید تأکید کرد که هدف نهایی، پایان دادن همیشگی دشمنی بین لبنان و اسرائیل است.
🔹
عون، همتای آمریکایی خود را به ادامۀ حمایت از ارتش لبنان در آغاز اجرای توافق اولیه با اسرائیل ترغیب کرد.
🔹
وی در این خصوص گفت: ما باید از نیروهای مسلح لبنان حمایت کنیم. بدون نیروهای مسلح لبنان، همه چیز از بین خواهد رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/451774" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odpPtarsLtV5vvzXYuNZTlQwm-tembeh2155S6JWEIPoE-_b00ASL6YrN5vUFAf_7DtR-K_ETxM4B8hzPUuWckOOLBnoEpIljobQqHGbeqWw7py2Twh6jn5ItsbJ3ZK6UitTVl-IIV6bhfXiG5bJ7pV9dpag7sB9fSSNOStFrgekZT-3pb-1OgApKBBUOOUAoLp4BGojbSxcwgppPMxb5FKwD6uPtZhPvaQD2u6bEvzbXh60VwEkEu83ZW7PNkq81N5ih4WJEXOmodGFgF7s27M6jYjdqCtNUleQOzWEPggaMJHpukHRdY3A9iIkoO50LpuG-6CIgZZHGinBVjpYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2SCladuotH3TIXIPr9HWyC1Q5Ug_hDzdjmej_ycLXopci3ihcrudoMbb3EolPTJkGrt8UHy92UXpzG-g9YBkou9ba7_ytc1gfI1D8vbe5RaRwO_vJJQLAmoMdiVQGt3GWc1AcOLJJLsah5yLfIAoA5xxyz9lGBgMTq76U6JZUgGaLN5Akp57j1vL19fPCU54hRYHpybBeC8zLL5PS4m8Dc-FSZzaHXoOB7yAoe3X0YlArHK3hYpvjvV-1F566enWnJuKjiipAqB10dUt_uHhN-VPFz5ASDq06ValdhIrdIxFEWSSDYO0XgCs_tXIvurszFgyTAYXSHV3L-HKDS7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5WM6PECjQjd7AKKzqmsrfoM-Fl_UXmpt1hjmKh7tvq6yzkx8XpPoDF7KoGmwbHzVRhEohj2NW2U9GplIL6kaAVzcmSzkjx-xHYlamgfPDnBDSQMBHHS8hLXtfEUw4MEQvtK6ekHC2Vo-OVuZLEWPpLHU8mDNYtk2tetRaJk0qb35hFv-cfRSkJomC3skZk5bRtPvEcRIRPmpw4o6FmdJWiYyFer5pEOQKlzrDtfWpLuOtb6ui0X6Uc8Bs6dhzf36Gq3p8a_A7d85TeoR6UuWeAu-1fywl1xBZ3QU_sZwdly7mPnS_62zb4OK29uMNXzu_utnmltDENdfmjoT1aS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNXUDU4EJHHF9-TrSkh1kKz6-HtVJXbDwkdZ3EiHuE7pFXvFVmupl9TfkzOBpNJMWFHLuPY2y7Y4wizTDBqIem15vGYJ155WdEmVtut5fuazcMKCNuza6nK1H0F1I6R5WAFna_May6DA51fAMiBFMS_sdad49_VUpKTtJ5bV85djEvCh4GraqqLz6unK6tHPeq8DxgjYDTTvlOmrJJAOl-sIy7qkgTx1-4cCLOQvTQGqe4L0RuNgLGHR9WUdDbzZjQqHRCLLzCnQF_goFyIDrvFKtYijkcrE0fAu37OHQecNFsTXNEB8W1a72JgJIKH-A8KrVLPpc8Mj6cQD6-nZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StZrB8U9cEc77YseyUoYc6JlY_3F_4-Ot5DYCh1Ia8rrhKoInu05ywYH7o0ua17UV0IiS2iq57iWKBElvQTcl02NR43I7jogPLYY8HuonzEQmd9wHb0gL-jX8wxgjgFx2sQZqFVTHAjLDeEuFuUqt8u-asYgVzw0jrqHiKLbw5wgNmVwLBgOhaXRFqFc7WPg59_l9G9IC9ITEx5_f0xJ_RRnNy-WLNTuFzer39yPPNXEua9iCDgnlacT-yd3Py0KfAMhJTMafdsKSpOVp-LOCbJGLqQHwVNsaMbRBOAR5oYK-KuM81imu-ULIXwsOKI7sBYq2iCm1xksN1NiNOqE9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۳۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451769" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMHW9-HM-wo2Ti6N0z3nU45GkN9kKIgenDuC0u1Nyzn_YGHy8GLOmEIa_GPteYhpILjQdY_ZsFmJXCr5WKkiR3q5wdNpBWgEYJm1n6VrJZ_nInuRIpQanWPW7MXTdwLsbBfxjPzKe4y7XcnC7pAqvSh-3Ifjz01160yhJf_Vlznb6OhniaAJlKDa23Txv2g9__ncjMX7nS0gnf2F7BokG3ZHTuPo0_tnxBmLG-DMP7sXQWkjAZxJMP8PTL4pJj4AbTDIu9IeqL3kaHdJHnh4bWb0uIlggj2gVXGWFZud5BkVEe7HuMNuH-iFm6vEeoYJCebkzXRAw-gSdhG9X056fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9IJIg9ldf2GdlWff_GLwPHVirAvSHgKzrNuv836UPcKhuBeIWLvApOUfYTgDnCO5RgJQG_q0fbm1rbbrnsDU8VyPedBweYjMqHHdvtV2x4mRnXEzeVLq_XvT_ILFXz5Fsz48Hmh1jDT8gFdbkQNc5Io64-Zy4Bzqwp-5IY2i5ORm5E9TZkcFq6hEVYW7SEgXeiXRksKYGb_67FFqtb9pPWMV8cZpjFuNDYmV0RiW-Ym9JkuIfQumZgZbgyd_fJyvsL3xXFud2MTcbGnNeqKTZ4nxNY39Xji_4vqCE6DHdQutAvn2TSSuK3sHznM-fli4OWGFfMQPKBntE61h0uS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmDQfNC2ICdHHHTPEbeZ5Lf5MHAKgGadcMCGtJULBRrtFEY_NQBHROjU6QbILSreoF7dJEldUe9ScCLH8r852O2X0zi1pOj6IdiXEm_rmwUpa0AGIU9c4pvPUugHiAXWKz-LorZI1Xizzh6XofcZfz7QUhdREeoUNFXAmryRnSgtMDdUxIg144PMuCb-dHQS2Ck6fjJ4P0R7G7kQduULM1KONMZtIPiI7o6ysGF33p-60utrd-CfCqP45nERiupgfcIANSy9ETSW8Too-1tLyGmDcIl23mCe80DvIh1hipO7Qt-UH13n3IYCHG0OtWsCihKVMpZZIw1K-FII7hnHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGaikiqePBmsxfhSzZ_QZPf4D4szwuY8TdMtLDBT6uqGGS2t80kVqoly10-PTHbrNFXvKWz9CopBdEnBua2L19VHa05_yg5xOjNj1ikG7OCBBSVQ60I-AJR35jyVc6CtDeN-4sWFqemfaZMje4s1YlW37GJ8ezVVp5io3mhiuYfWAHKxGAOWK7aq1karbcxPws9iHbhdQz6DI9_-2ZQeJ_5WDuiS62EX_1yZCIEk7A3Mh6WcJirLq3B0VlwIWdi5V9kIj1fHl3VJEKxiLW0vQHHLumEI1_np740l4EdXnulXmv3BEDQ-YCO7sQTUP5UGdLFhzVBmXTXSGJMxkAsQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbXwUfFegpHLzZdWoWRvsM7-DuMLoVpnXlUSoc6wcBY6UceHwIFtyikV4F9b3tndTHSdDQKtdBFxsGcoJXw-UIexHiJGlzRIyQU9B4wBiMmaGEMDI1zevScj2FO80W41oUu7ZtmJhvYCpvDBC0ocQfQBKUQ9kiBu10yTMXwhVgKAYQnvMnugtdOC6zRnCPrD48-3kispTT6LgaoYTo0fskvU4T6ErJEgh0dTOlm3_T61kAnPLqlZ5Jkv2JeNRlQD9y9V_DHEasypmG6BJM6Az8mU2ecbo2maWbHOgDAYJRHiYW9B-KKEArzz_W5XOKVh24k18QgtE7cF_hjRF_34CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKqIwe5Co57VcaXUTtyMMjcSJUPNqhUEyM2Su6WRAQZ9r_Jyo396ecbCqjyiHoZVqA5UYFTyPR8c1Uy_WD2l1Xq0y7V4Q0PsUaB8qKHmD-LNurZesAaJATRUo8Wx-B9UUW3AZu5WIWwYcXdr3r2ipQE5bRy63GeOJT-7y1GS6AV9wZeuMmy7hqatBfchAbY0tBHa4zG_YFM089TLYJTzWrUNat5_dJH0VOMMmoVknPMFtsoNxeCnD01Ld1mqHT7HBYZKdLjvBa_gDkjojshDry04BIEYlptOKQqTgeFFmbBFU6_-NwnSmVroOBYaqhQzklUgQGayiEhUpaOfDyNa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEs2lDb9wKu5Sa-SW2tdtawNS-6ux2B4AQEsF3CdWPe46kW5QFy5bt2b8qUSde-R-nGqrszjwLnTEM_lWEjnWARJh05Qlgzvqcg5peU7m5waNI-hwgZh0hP8lEqSwU4sU2PXtFBqWGBR_8p0Z1swxqXKO0WApDrGeuij6apG_JITtMCEjnLqkIelajtMWr9t_IQft3AjlUFVxf3TI7EopXC2tfkdPdLZWbfLWMSMKF6PGnCHRabH1tcma4usFyySP_LOP_7H_H9UrzHm69jUDfgIdRHA2_gLgGAZ80er2ZoMIQm3blsv9YKdSe0Fh4pVtRmjG4TI48Y1iCgizXMPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LagNz-Tggq2ZXmHIQ0-tAf9Dols7U77j_itVeAqfBtywXb97bQHLcligWnzVtJWoOGL_oobjjKg5cx8ghvbf_rtcFXkxo5kmLupfrLJT374gdrlofoxtkqSQljga0z332kZvxgo61ILx7w9PEOGdR3Bpfo-nZHoEKRxynpFII3egylpu2WoSUKkqrGJI_BRflcKa1CK9neQEwJBUkectU3GaRcx03qbWfzSUi2OTrAC4rNQwK9feYoQnS1xnoKI-6YdWuwA-26vn8xrSZgs-bVcruDMFrGZjgyOKuiFqwdgLEIeWfIOn1W5XCi6vG3Z5xQ59JSdONe5EE7EWjTCwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeudu0e1CzfEoIf0j-k1nTSaqlw91RgxsEDCNT0WaykqxrTJw9T3W8tbRmnWBhtK54hp72d2XTQiQjUSaIZyC6wDLjn8jD7TU3kCTrk_i8Qc-zShuTz82svyOHdKdcThF0hEGXEnARM0OW7ieF3uRdWtnFBNJk_Bl0iOjkfFVdPV7qipXHa1UMJXiQl90r9tJw5hkqntQeNQo2v8EeEZtMgiLairg5L9I6F645Ju9REJqY_adIBVq7vq_AZxVmW_cDLVu7hP4wEYCiXXs4ud38gkQDdGpcnaEPqqpWjPdlAIE1LbgIXeh8esGNu1qu3yDLi1a6hifqhxzOCkaJc3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATL_a7N7SbXgMy4kAtGA1pQu-vhXiW0PwFkTZ5nVRrkiG817J5ct3xJEo8tnBCIO0EgSya5w7KsqUzM2y3DQCM88ZOtiRZJYa94bsF-XtBmwNNLgEA7zXwCZRgJ3YajMVWt0kbTuF42NHWBNCZ7LM3oaA_5QtyL6S1zAN9MQhnzwzfjb0oTll_KZkgE4J72l_gmR3Ny_NmKOU6LJPdg9uSm52_6YGLPJexT8ktoG_i-auawQpTSfGtnxAu_NJy0o_5ETPcJb2CRCSAos_LdRFzLwfB7UMBXcbSeZZGXDI3dzYPfqQ1BPOz2j_4S6nsUyzFgl67nyiNRZbKUDjIVVUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451759" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451758">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451758" target="_blank">📅 01:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451757" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451756">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451756" target="_blank">📅 01:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451755">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmAxh8dL-Jkqv04RmiYCORn0are9X2x-ANFkARhkE2T5R0uIJ5ac5EptN25ZyLMwvbNY-zEmH1NbP1hpId9SzHjNaFAELmD0BjiEeN22988-0z3DVundMP7UYHdbGwLjVv5Mg5icj7VaScwfq7V3E3xL7Q2Mq_LvXIlgydJaziGdgoJ4_dqeXwiPxnbUzKo-GJWIkZQIjX93cPvD9losaddyh8RnN5SXZpZX-4o1KkWd3gEeQxF7CZcoezzLq3mApCo5x-K__q9hp5zVgT56X2Vc2VbCmpFKACQKXpapDphLlF2Yfn9WIp0-FriYYLkzfERMeUyGAAVH3qksWQnzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم دیجیتال سنتکام در بحرین کور شد
🔹
نیروی مسلح ایران در واکنش به تجاوز آمریکا، زیرساخت مرکزی داده آمازون در بحرین که یکی از گره‌های کلیدی تبادل اطلاعات ارتش آمریکا است را هدف قرار دادند.
🔹
منطقه ابری آمازون در بحرین که با شناسه انحصاری me-south-1 شناخته می‌شود، نخستین پایگاه متمرکز پردازش داده شرکت آمازون در خاورمیانه است که در سال ۲۰۱۹ راه‌اندازی شد.
🔹
تاسیسات آمازون در بحرین هرگز یک پروژه صرفاً تجاری نبود؛ بلکه در عمل به شریان اصلی و مغز متفکر پردازش اطلاعاتی واشنگتن و متحدانش در خلیج فارس تبدیل شده بود.
🔹
مهندسان آمریکایی این زیرساخت را بر پایه سه «منطقه دسترس‌پذیری» مجزا و ایزوله در نقاط مختلف بحرین مهندسی کرده بودند.
🔹
آمازون یکی از چهار پیمانکار اصلی وزارت جنگ آمریکا در قرارداد «قابلیت ابری نبرد مشترک»(JWCC) به ارزش ۹ میلیارد دلار است. این قرارداد به پنتاگون اجازه می‌دهد پردازش ابری، تحلیل داده و ابزارهای هوش مصنوعی را در لبه‌های عملیاتی و پایگاه‌های منطقه‌ای مستقر کند.
🔹
جزئیات را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451755" target="_blank">📅 00:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdy2fClS_inf1VKxS80kq4jPFWzbYItBzUmqjcWReT6PmR84ngx2zPRjyGRUEg3FAn8gOV1q5_aNQGpM1xHt-YlqsP5RDDF9O9elm7ofi0nePidDHeL40LqinKdyOa1NmpdUUONk3PmTdOaCgtetiXmHJ3aAdDOdeR6gVMjwqSI9FHCo3xWPmWjSD24XAg9o4MC_Vt8ReASu6vxmb-yF3NMKruac8zxJ__SuO0044usybl-WWfyhBYtWOtNsembpPd7TQo6uJGBAzLoPKH9a-aU5Hs6VsONYZzMC3Y6dbwzfsqq0zhsCitCsFNc_4HmQMFk2r7k-1VFYNrB6u014Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e6c3b61f.mp4?token=GtoGdGd53CbOTXhLG_J-HRSyuHSHbuB28tMXYZ3JVKQz0Q0S9VD7ivSgfgq-oIyii0CaoaC_wlWxPoWTGRNHO986llhGkOyQ_ACmQHvZgrMA8Wq3qTb1Lq83Lg2JfOZAgipM5Hfpz_ei-iMrPP02KbLz1UfrW-uIqQwJ68M8ZExrqxvLmHB9EP0b7Wiq19IeuofI66Qxx8JLRCKSzQ7riI0iGDnKlGpljx7qnBBfH-R2K2xNGs95J5fgUf4T-fMdAqNTpwbTMpn_npQxsnwBsbkbfrS65djbJWWMfHzW0nS1S4s6Y-l3VP5TKK8h1H4MxDLV7GvxI1LAhSLjlU9r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451752" target="_blank">📅 00:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451751" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c48ca5530.mp4?token=P0esqZm26lgoQtXUBLhndWyXitDh1IBa2tDZSxtxG0lcp_ilRH-qVaaI-wtlCoSj70nJwCFpcAs9GGCTHXZS9QCAM4r6NFv-o1ZAF-58_hy_xRcY-hjrOBcFi3xxhn-0329K29S0bnpkOms4k_Lgp23GnSnC88fY6D8SdRdCY4LIB7YqzH_FC2Wov7grI153RF6wkUEu47N6PXKv9_gkJpdLV5iQceukkxlrGdHEyuomv0MGwuixdHlK-3wsdsK8tpagPktbVqTd__Qf1QsU3a6snuEqlgPYOpH48TcX4ZfPGTQMZ_Pjfenp-L9Wn3-SuCTCdrfF925HQKqvAGCZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر جنگ آمریکا: جنگ با ایران تاکنون ۳۷.۵ میلیارد دلار برای ما هزینه داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451750" target="_blank">📅 00:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=oJgf2Ybfr8-3T6CqrFzxmdOrDuDe4EwJD3fQf8EffUUcnVFAgoCZbBWaGHSBaQcaWgMSAFbDH5lL7Vl8gqH7XkV7j1t1d_Arp9L-j4Qrud-qhM_8VgsC_tWo57TT-1qhkUNkeTfVwetlCNDsNzKNtaxJyXsk5yAvNJ47D_ZtmI2pAs8XLq6axbxVnpubpa2ZBxiQu4PG72YnzuoY3HGmSziRPEfqJqVUpJ2N-EzAJ9jyUMXRzMPeO81cF2RdKwEzK95buean50wjoTdFLKWjVXxC-7hIFmiepGL3HLhjYaJO8zxEPEwsZItYks67h4-EKOU0kbulboKpRh7EoIz0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی وزیر جنگ ترامپ را به چالش کشید
🔸
پتی موری: شما ۳ ماه پیش گفتید برنامهٔ موشکی ایرانی‌ها به معنای واقعی کلمه نابود شده، پرتابگرها، تأسیسات تولیدی و ذخایر موجود منهدم و تضعیف شده و تقریباً کاملاً بی‌اثر شده‌اند. آقای وزیر، ایران طی یک هفته گذشته…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451749" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=FVserwFM_INzC0_LLUCiXIdTIUtdoHY-oe4xLBqhsUw-GaHhdulLE_wRjk0mT9DTSaO-2HdXw6qekNmjwLN_kEJ1rQvT5W5j9gnp_U2Ag7hsop4dZaMKhJQIhGoipHlEEJUUiIpbi2i23mSWLnLhO-BPp6QE5W-XPi4cSvCUOGShdcgxPDbJQphVlX8EBGNwW8vKOHCvZ2XpJ0W10NnMhEFFVCSzzgs43nbctzCBdqTevPbdPKuZwUreLqV_kSyQe3RRKlT4Ch_zv2neEpXPkofELsZBjMklf_TWdIoWdEc1RO9Ak4K0uCB2K5EBt_J3kG0XCCFBIx9E8PDP1_SIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: آیا توانایی نابودکردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بخش زیادی از توانمندی‌های ارتش آمریکا طبقه‌بندی‌شده و محرمانه است.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451748" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451747">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVNDI8d-NvaD70Zex7YA-9XBL9Qo0TzrLjj5-Df6RLlDhNSu7y4lTs8DOi1iNFKpH-YQEryfkBPdV3240MlHODeIREUnaBd6IYAHSIuRGa799_708-j77XCHAPfGPmNMzuEaBmo_s2lVKSZ-pZTgA8alyJVuQ9fmsWYk_Z9ewfwEnwPSwtRkoxg--ogZLYOaSSEO-yp_aHeSDD4t3HgfKEB1X7VRsDJPh4hDYN7zJ6LvEXT9n9uv1vtclxYu0XzP5TVz_H8jggZKHrlphvrdSX7czt0WoGpJ-aj1nb4JI3jl2LMLUy6Fn4GZs1T9IvpDOEnU0HbK2JFCnPnuzeL3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش جدید ترامپ برای توجیه تلفات آمریکا در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال، تلفات آمریکا و مدت زمان جنگ علیه ایران را با جنگ‌های قبلی این کشور مقایسه کرد.
🔹
وی در این باره نوشت:
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
جنگ ونزوئلا: ۱ روز، ۰ کشته.
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته
🔸
ترامپ در حالی این آمار را مطرح کرده که در روزهای اول تجاوز نظامی مدعی بود که جنگ با ایران در عرض چند هفته پایان می‌یابد، اما اکنون بیش از چهار ماه از درگیری‌ها گذشته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451747" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451746">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5683a4e5b1.mp4?token=A_fPw-JrK8xkFyhPtT5cIvoPjcCKXeO6WW-dSHRuVuQOMfMJBiXuDUqeq4vkGjzm0aewLy0_B9hAJUrU3B93LaSTB6jf-knzJwZ0WfdudBTdqFftuIEeeYRA3f7EPdPOUWJjaJ-y-sbGuUtTorRLaQUX425x0T0SbaPNQakDV5HqNnNTQVTn1QwdPwuJjh7Dw6b-L_Wqc1n9WQeNK0iLfakiVPZD8Or1_tux9ZVTOLtPy6ESniQWG0WAKI8S7Nv9ZDNRz-Ehw5BDKlpRAxt7PTINr-96TEiusd55MyI44YlUVA5WOd_D5NM7qXMC3UIjUPURy8H_FNoP5hWmM6GT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451746" target="_blank">📅 23:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ab2fe524.mp4?token=bPAtt8cz3TelyALYwX1yEgMLrkZxbvLsuJGZhCThGS2pZz41M50KXZcF48v_x3TplcpElf5YqqkK4pF8Vg49PmjJkwD5aCw7BzcJ4MIC5wFokPKoTa2U54ihS5e6k1SzeWYf72TBlDZv_uZrpyx32SA-cq0TJEBbjdtFLd-Fhw7OqqbxyFSgSTcajW_ehJ-P-mLv1KDf062YiJI3-JBTT5Eh7qz-Eur6-nZfl4jR4f3MBF-1QmUSKiZJ1sJYJGQpnBYrJ7jfOu4MGNjpuJOF_MeMGu_eQR_Df0NRkuMXh6H3QK0r1etpMLetWVMlvWZ0q0l0oZuSXkwRKQtp9x6_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان ضدجنگ در جریان جلسهٔ استماع سنا، سخنان وزیر جنگ آمریکا را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید
.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451744" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-A1awx63txHLN5S06GOKkxOIH541rtYUwyuldIvXKI_vj6YX7WXmP5IYnDPNrPxtT_w5nDLG4nSARSw0aWQQDD73eNGir-lEzUztpfk3CTTGjd52a-ea42BuJ73iETcV3-HKUqRrg7J1xpbaRe3OUNvO_SSiXs2-HOtPBH6WP1EkI-gOrDmQ-XOfqokvQNHMqHW02G4Tl675trpw88zi6HY_lGoJi7ajmdJ_CczMbeqNmUkb53kVgyu3YlE6YsNvAMhJOXSDAgTGP0Ne-x___wZ85M3aUfvd9c4BUMKMUZPnJvKfV4iIh0NTWyZdlujmZ3kS1_tmHV7TRPplfXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: محاسبات غلط، دشمن را به بیراهه برد
🔹
اسماعیل کوثری : مبنای اطلاعاتی دشمنان غلط بود، آن‌ها تصور می‌کردند که می‌توانند در عرض چند روز کار نظام را تمام کنند اما همین اطلاعات نادرست باعث شده است که آن‌ها اکنون در گردابی گرفتار شوند که حقیقتاً راه برون‌رفتی برای آن نمی‌یابند.
🔹
اکنون کارشناسان نظامی و سیاسی آمریکا به‌طور مستمر و علنی اذعان می‌کنند که ترامپ، با آغاز این جنگ مرتکب بزرگ‌ترین اشتباه خود شده است. بی‌تردید اطلاعات غلط، چه در حوزه نظامی و چه در سایر موضوعات، همگان را به بیراهه می‌کشاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451743" target="_blank">📅 23:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6f3ba24d.mp4?token=s-Bd39YYNctyjFc6uIlbpV9s2FwjSv59RgvGqfdOslk-BPtuEqM4vjaNJE_yujdb9ao3yPC24MrvSRt8Z7EaBuwTPSlNWeRP-Jp5-4VjNl6czIpHJBqkvHE6KTgpZq01usq7Ubt-hAGC74g4M4AYWuTd3mFVsSnbqxC-S-GNg-7TEzz2PraJ4nse_6Wc05AJG-q_PWV1MAPdmXbASqB1pRi1ww_FIKKls28Um_BFmvu_CHsJuHnTHEnDLuX1gEFQFRdQeTcHVcuAuM-OEdSypmOENOMQAZptWsCXjcvmXcTqrNSKJxrQOdH6rq3Kj7ZQizQls1vSOKlQigUxIL-SkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع پرشور بروجردی‌ها در حماسهٔ ۱۴۳ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451742" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323a6a4a89.mp4?token=IgZiSa9l6hSMMtp9oUIcu6UWbVyprcgWcJPbWsER_2ZttaXCjIWTNAtBlBRSRDT4xbf6dd6ow49KYNK3RORdG4EikeAAxXT_G4FPHdv2gJsgL3FqjKdn0MK5T1cU5m7YDrheOLM6Ie1kR3h05QUQfKaJR2ngzmRnnX5TeBUAXjnUGjehiPJLBqte55yogbxj4Os_J-bCVQWuviH3jF0PVR6Msjzye_WON5Jt-nW8wshXeXHxmwFZEhLiLh4ufhOgDVrkoYeT2sU5oBr0MwU23BFsllxI5XD6-GHOVOKXr4AYpOE_Oej7SNUo54tfN2-SSNNYhd417joDZPRzDXObQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات بانوی ۴۰ ساله از عمق ۱۵ متری چاه فاضلاب در کاشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451741" target="_blank">📅 23:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c74d42d8a.mp4?token=K-AFidC5RsxDsZ4TF2YC_p9c1DrPIgNUJp2EtGAlc1tFmWRxZF-mtQw46G93HcrOd0UAAesflkuf9u5MJA0fsaOrAnOFPOElT9zlCYzF-aoOtoC5tW3uLpBdcB1FB5abCeuKQ47tISUoLNHi6KuWYnoV3rI2zkrOACGHQTMVHfI_DNknp8Q4rsedmVYYoevNxurftogMZdwmQGT5MWv7floNmKhtxE1FytLroQehDyh-d6AO9Rn5ZUuJj1QMZW5ardQb3czqaxnqlQk7rhauULDdfLwID9Jzr2sMpm4QSLThtpX1gyD0iSBw8nCvRrDQgK-oo4uja35NuhOC4YeQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c74d42d8a.mp4?token=K-AFidC5RsxDsZ4TF2YC_p9c1DrPIgNUJp2EtGAlc1tFmWRxZF-mtQw46G93HcrOd0UAAesflkuf9u5MJA0fsaOrAnOFPOElT9zlCYzF-aoOtoC5tW3uLpBdcB1FB5abCeuKQ47tISUoLNHi6KuWYnoV3rI2zkrOACGHQTMVHfI_DNknp8Q4rsedmVYYoevNxurftogMZdwmQGT5MWv7floNmKhtxE1FytLroQehDyh-d6AO9Rn5ZUuJj1QMZW5ardQb3czqaxnqlQk7rhauULDdfLwID9Jzr2sMpm4QSLThtpX1gyD0iSBw8nCvRrDQgK-oo4uja35NuhOC4YeQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451740" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b146be1c.mp4?token=uhn2OmO-Oimm7xpkhCJI7VHpEqwnsyW4Tgrh1dmoc67AKHnK3d5yVEy5gUUQRmiORLj-dFNlmu43IgsA1zP0cB2fJ6sup4Mqa-c7SaFrjXZYgV8G_OKdFoNRduuxQCF_xoV_s60H3XXDh8VSZcRbBoLgkZDVLp4p8sNdWfnFN6HcTCKoZ24lEKtqogml5tcjprfc8uCBo5RQ-Yi4T8MGns_GzCTmZmGJT8ZnMuMbt8Z2lLzAGOevtJVWzgUpIUoWmtaQRf2tKp3PSdOUVvXsZ2pDCB1yNrbQDygQZD5Qb-Za274KvDb07VOR4mTLzPqBbDbiJpWKWX_yHlGUsQFkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b146be1c.mp4?token=uhn2OmO-Oimm7xpkhCJI7VHpEqwnsyW4Tgrh1dmoc67AKHnK3d5yVEy5gUUQRmiORLj-dFNlmu43IgsA1zP0cB2fJ6sup4Mqa-c7SaFrjXZYgV8G_OKdFoNRduuxQCF_xoV_s60H3XXDh8VSZcRbBoLgkZDVLp4p8sNdWfnFN6HcTCKoZ24lEKtqogml5tcjprfc8uCBo5RQ-Yi4T8MGns_GzCTmZmGJT8ZnMuMbt8Z2lLzAGOevtJVWzgUpIUoWmtaQRf2tKp3PSdOUVvXsZ2pDCB1yNrbQDygQZD5Qb-Za274KvDb07VOR4mTLzPqBbDbiJpWKWX_yHlGUsQFkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ایستگاه پشتیبانی زمینی و مرکز نگهداری یک بالن جاسوسی آمریکایی در فرودگاه اربیل
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451739" target="_blank">📅 23:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b385fa4aee.mp4?token=lgXwPCfiTf0u4jjTSZ7Gwxp8ubQtWvC7v1CxMBSaPXslLa4exbfPWrmxn4FOj-ee6y9snv4xG0O4hNPk9iG2RyraUtjcP5wUbmw7dXlvd6iiG-twK_nZoZ6Mlpm3S6ljzxXsX46aYSC2wS2a2HpES9lQq96HJhXkctwX-4ZJz7TF5VlWKr16-q2Gkk8GePXYBjD0q2aaZAxlneIo_2Xuhp8aOiPOMhZ6WwgBxWnylE8Se4Hek7K1KvH5IjU10IpVMWCB1nJDuvThdRORXzL0qv7iY8gwxZBekFr5XYuk6mQ7g2ggGMkKf6GVW4q3lth_XdLedKTvvPVsKP_3TJc8yWeFanpXojdqL6gLhMzp8hD7bokfDZMaNs9R_ez6b6e4W2dx5UcezDm1t7K8XXUVdxswqBnIH2O9Be5jry6zux59vhzw3mSgSZtso5nUUFuNVhll2rjroZ1xRTTKdfS-RQiJi7LFcKl7wd93seI5R_FnA8XNb7SSemKIhIrWPKSDkyy0-t-BrT2T8DAQeVAhnzBdd8Cr91u8hIrXIVAEyJd4p2t61Gw4R_T5eKIeHVoMeLxx48mRk1OBTXJi3xKat6Nv0yN2yVtdIhOvvKAogBUbYf5d-XyhhephvsUh-YuVqOva5DmFZW1bXc0pcecHK1I5lXIjgPcZAgMvmhRI_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b385fa4aee.mp4?token=lgXwPCfiTf0u4jjTSZ7Gwxp8ubQtWvC7v1CxMBSaPXslLa4exbfPWrmxn4FOj-ee6y9snv4xG0O4hNPk9iG2RyraUtjcP5wUbmw7dXlvd6iiG-twK_nZoZ6Mlpm3S6ljzxXsX46aYSC2wS2a2HpES9lQq96HJhXkctwX-4ZJz7TF5VlWKr16-q2Gkk8GePXYBjD0q2aaZAxlneIo_2Xuhp8aOiPOMhZ6WwgBxWnylE8Se4Hek7K1KvH5IjU10IpVMWCB1nJDuvThdRORXzL0qv7iY8gwxZBekFr5XYuk6mQ7g2ggGMkKf6GVW4q3lth_XdLedKTvvPVsKP_3TJc8yWeFanpXojdqL6gLhMzp8hD7bokfDZMaNs9R_ez6b6e4W2dx5UcezDm1t7K8XXUVdxswqBnIH2O9Be5jry6zux59vhzw3mSgSZtso5nUUFuNVhll2rjroZ1xRTTKdfS-RQiJi7LFcKl7wd93seI5R_FnA8XNb7SSemKIhIrWPKSDkyy0-t-BrT2T8DAQeVAhnzBdd8Cr91u8hIrXIVAEyJd4p2t61Gw4R_T5eKIeHVoMeLxx48mRk1OBTXJi3xKat6Nv0yN2yVtdIhOvvKAogBUbYf5d-XyhhephvsUh-YuVqOva5DmFZW1bXc0pcecHK1I5lXIjgPcZAgMvmhRI_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشکی که در عملیات اخیر سپاه رونمایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451738" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">موافقت نخست‌وزیر جدید انگلیس با تداوم همکاری‌های نظامی با آمریکا در جنگ علیه ایران
🔹
بلومبرگ: نخست‌وزیر جدید انگلیس، استفاده از پایگاه‌های نظامی این کشور توسط آمریکا برای آن‌چه لندن «حملات دفاعی» علیه ایران می‌نامد را تأیید کرده است.
🔹
این اقدام ادامهٔ سیاست نخست‌وزیر پیشین انگلیس کی‌یر استارمر محسوب می‌شود، کسی که بارها به خاطر عدم حمایت کافی از حملات به ایران مورد انتقاد ترامپ قرار گرفته بود.
🔹
برنهام احتمالاً با انتقاداتی از سوی حزب سبز  و لیبرال دموکرات‌ها روبرو خواهد شد.
🔹
این احزاب با استفاده از این پایگاه‌ها مخالف‌اند، چرا که به نظر آن‌ها این اقدام، انگلیس را در یک جنایات جنگی شریک می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451737" target="_blank">📅 23:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8060ff907.mp4?token=gM8oWfpGSQmrNbkq7F-aHD3aNQ3OPxftiK_tnzHhiNHRkrxiQF2MX5YN6dq3RnoPWEdbLI8yvxfDyfkdoXGmJuoeyqZ3TQdn6KR-bmzHSv2rrPBsJmqj0OyA_xECcFRlu4wxlR_xttORnJ16LIXegdCFqw3V_SCxKIfe8hQnmesjYANaYNQsVCXXVX1-wZJ0lY6akA4TQdOr-eQ1u7KteFiH_FE8ZE1lQX0RZ2t7J0Cz88vI3zh9aBothpoTFzhHWNdTJdIAzHU9MIDTyTl_D83cjzy5ZasylQP7XbIAuXGxccdlIqFBoDOBeAXpRCr7t9J23riXq-LzpZTYMmDytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8060ff907.mp4?token=gM8oWfpGSQmrNbkq7F-aHD3aNQ3OPxftiK_tnzHhiNHRkrxiQF2MX5YN6dq3RnoPWEdbLI8yvxfDyfkdoXGmJuoeyqZ3TQdn6KR-bmzHSv2rrPBsJmqj0OyA_xECcFRlu4wxlR_xttORnJ16LIXegdCFqw3V_SCxKIfe8hQnmesjYANaYNQsVCXXVX1-wZJ0lY6akA4TQdOr-eQ1u7KteFiH_FE8ZE1lQX0RZ2t7J0Cz88vI3zh9aBothpoTFzhHWNdTJdIAzHU9MIDTyTl_D83cjzy5ZasylQP7XbIAuXGxccdlIqFBoDOBeAXpRCr7t9J23riXq-LzpZTYMmDytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۳ قرار شبانهٔ تربتی ها
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451736" target="_blank">📅 23:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a70c08ba.mp4?token=DFcR-XQJPaFD7bW5NVuCgJODOY6U67PlhFbl7GV-09Gf9vsh7ERN7mDTeyaPW6xb-NcroSd3P9h1oGlBQoE6DqY9hMjN7DsOnqgjYhSH4iYjqMW5lbSiUCJ_Dk_gtJ0FD1mFG4MR0lomBK1ASKbg3NpyKNpuL1rdSP3tNRUo-UmKKlPBTFce9JPigVgZGdp0SGNHDe4ixxRzkFKyTTqntNOoFOD3M1ph5oea6_pR8AsQMHDmPHlC8yVoOnx1AdgCOW-LLTTbAv_KlAnBa5r5Wkc1f8BqiP8pTATyC-RqSiVAB-RrBi6qmpd_SrWm0aHsLac9e9MQ2ErV4JqFSQ_t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a70c08ba.mp4?token=DFcR-XQJPaFD7bW5NVuCgJODOY6U67PlhFbl7GV-09Gf9vsh7ERN7mDTeyaPW6xb-NcroSd3P9h1oGlBQoE6DqY9hMjN7DsOnqgjYhSH4iYjqMW5lbSiUCJ_Dk_gtJ0FD1mFG4MR0lomBK1ASKbg3NpyKNpuL1rdSP3tNRUo-UmKKlPBTFce9JPigVgZGdp0SGNHDe4ixxRzkFKyTTqntNOoFOD3M1ph5oea6_pR8AsQMHDmPHlC8yVoOnx1AdgCOW-LLTTbAv_KlAnBa5r5Wkc1f8BqiP8pTATyC-RqSiVAB-RrBi6qmpd_SrWm0aHsLac9e9MQ2ErV4JqFSQ_t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع ۶۲ قطعه از پیکر تازه تفحص‌شده شهدای دانش‌آموز میناب در بندرعباس  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451735" target="_blank">📅 23:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c339993d87.mp4?token=gS0PVIbKXknxJ5DY-R-6ZIgFQVkQIIopQMPfbjvU8SHaU8729aWlPQaPo1nQQ9SvnEYFCJKwbf9zQ8AAiHjAj4je1KnZcj17s2FvjMwFLJiUMvoJn58V6VVdeYJASNw7wjbJ4WD1_hcZ4QzJpOUipLoCrIkD66or8yFhaL1sZTmEzy5TV5b5yTonaqiuLkwkIT8LwykrCj14y_CgC1spWwlSz_Mpx6EcBQPwN6PuTnvfB_bGRHLFGCMM-xp2kYSeVAQWlb_IlfTQ0YddcWrxxeU_QbWx29kzH_w3lzceFD1AneuI4WycL-LWZB3umCzCHGV9FfvfCewVfiziO81nEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c339993d87.mp4?token=gS0PVIbKXknxJ5DY-R-6ZIgFQVkQIIopQMPfbjvU8SHaU8729aWlPQaPo1nQQ9SvnEYFCJKwbf9zQ8AAiHjAj4je1KnZcj17s2FvjMwFLJiUMvoJn58V6VVdeYJASNw7wjbJ4WD1_hcZ4QzJpOUipLoCrIkD66or8yFhaL1sZTmEzy5TV5b5yTonaqiuLkwkIT8LwykrCj14y_CgC1spWwlSz_Mpx6EcBQPwN6PuTnvfB_bGRHLFGCMM-xp2kYSeVAQWlb_IlfTQ0YddcWrxxeU_QbWx29kzH_w3lzceFD1AneuI4WycL-LWZB3umCzCHGV9FfvfCewVfiziO81nEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از فرمانده‎ای که از سال ۶۳ به‌دنبال اقتدار موشکی ایران بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451734" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سپاه: مجموعۀ تاکتیکی رادارها در پایگاه علی السالم و جزیرۀ بوبیان از رده عملیاتی خارج شدند
🔹
سپاه پاسداران: ملت قهرمان و ستم ستیز ایران اسلامی با عنایت خداوند متعال و دعای خیر شما مردم ایستاده در میدان، رزمندگان غیور سپاه در ادامه موج ۲۴ عملیات نصر۲ و در ادامه پاک‌سازی منطقه از رادارها، با تهاجم به یک رادار هشدار اولیه ، یک مجموعه رادار تاکتیکی در اطراف پایگاه علی السالم و یک سامانه راداری دیگر در جزيره بوبیان کویت، این رادارها را منهدم کرده و از رده عملیات خارج کردند.
🔹
عملیات تنبیه متجاوز ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451733" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc98b2e8d.mp4?token=nuFgd5Oxf-Vqa9f-zqaV1TUYXg5zrNarInqlNv2Lc3WnjqaUETEUr-LRh7f24SJPYv_TRO5RzJN4p0Fp63Dl1Clu1JfLIfprV-zsHD6GrTWF-li9Icuf7EPcbLPgyWTnEgOjfiG5zF76VUKAxcJ_PqchldT5L388nOtK9bWcNH2xfUmB4PkxgtIWgA1MAi6hH28_3_2INMw5f0ScKS82uEszFfo8ModYpo1HgaWEOT9gRrQvsPqwuOqjTynP-AxHrPY_69YOqIDW8VrScxgSJhuQj78O7zvyqlcaI0WfXbuXz3lbfgDK7dE2AS144T3D9vYFeEkOcxEqVDQ8wz2E7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc98b2e8d.mp4?token=nuFgd5Oxf-Vqa9f-zqaV1TUYXg5zrNarInqlNv2Lc3WnjqaUETEUr-LRh7f24SJPYv_TRO5RzJN4p0Fp63Dl1Clu1JfLIfprV-zsHD6GrTWF-li9Icuf7EPcbLPgyWTnEgOjfiG5zF76VUKAxcJ_PqchldT5L388nOtK9bWcNH2xfUmB4PkxgtIWgA1MAi6hH28_3_2INMw5f0ScKS82uEszFfo8ModYpo1HgaWEOT9gRrQvsPqwuOqjTynP-AxHrPY_69YOqIDW8VrScxgSJhuQj78O7zvyqlcaI0WfXbuXz3lbfgDK7dE2AS144T3D9vYFeEkOcxEqVDQ8wz2E7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه در شب ۱۴۳  فریاد حمایت از وطن و نیرو‌های مسلح
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451732" target="_blank">📅 22:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9wF89djpRAKQDUvoJDvHTJDrm0-RWxzf4QNCgZ9YzRAQ5Nlhdw3hi8-gWqT92Ju8R8m6inOfITVUhpPpKYGGeKdeu_-m22iLZA6xu5QXHQ4Aeax-lMwB89UZESEjxBsr7saIiWZoLLyTEZCJ4hQzryFuUhIyz9GYIJo0-1OLF02TcP6gSgYNAVtiaUgsisQhbvhhtzwFdr3S7MvT8JlRmdqEG3gDsISASx1GbmvQzgFULbSlLghsZw4HzVFQDokxs59bJVEvqCTvvNhhesS830OyGSz4vAzdT_0zGM318NnhldKh_SKTI2TDo2z9PichrayQiB84_V6c9BGD2EOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت شهید مصباح‌الهدی باقری‌کنی به میزبانی خانواده شهید
◾️
فردا؛ از ساعت ۱۷؛ مجتمع امام صادق(ع)؛ شهرک غرب، بلوار دریا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451731" target="_blank">📅 22:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPXI5YahjY34lHaYT0RvKtIitCnj-51vqAhLL3INUhdXzfFbm-_kFoeyB5aM0tcXKKujB6c6Car0q1tnxidgYNezsomfVio6bixDxVM7vJ6eHLhKf_c4DPRHeJDGiI9Tpz6RIhzPjLAuU4nb2Afw0SZd4E_Pm-nJge4nJU-Ztk_9EKVM2CNDgAkD1opDB8buH2Wu2_BeztG2gbSaojw5abxc7qzpLdTeiLU61tKnIu_vcXasQsbXT8aDqcCOM1N8NZzfUS-jWgP6rOAjLeK5IoeZhdbQkANpT8DuF60xB6mo0eS1T8AYme5EUEvFMJmW8fktZPo3-tWsFaCTkIlYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اسناد اعلان قرمز اینترپل علیه سران گروه‌های تروریستی کُردی
🔹
برای نخستین‌بار اسناد مربوط به اعلان‌های قرمز اینترپل، احکام قضایی و درخواست‌های استرداد شماری از سران و اعضای گروه‌های تروریستی کُردی منتشر شد.
🔹
براساس این اسناد، درخواست‌های ایران در پلیس بین‌الملل پذیرفته شده و برای تعدادی از متهمان اعلان قرمز صادر شده است.
🔹
این پرونده‌ها در چارچوب همکاری‌های قضایی و پلیسی بین‌المللی درحال پیگیری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451730" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
لطفاً در خصوص پرداخت معوقات بازنشستگان تأمین اجتماعی پیگیری لازم را انجام دهید. با توجه به وعده‌های پرداخت معوقات در ماه‌های گذشته و عدم تحقق آن، سطح نارضایتی بین این قشر زحمت‌کش به حد اعلا رسیده است. امید است با پیگیری از مسئولین مربوطه، مرهمی بر درد این عزیزان باشد.
🔹
نیروهای شرکتی ظفر کویر دامغان و کومش کار از تأخیرهای مکرر در پرداخت حقوق، بلاتکلیفی معوقات و نبود قراردادهای شفاف و قانونی گلایه‌مند هستند. این کارکنان با وجود نقش مهم خود در حفظ و پایداری شبکه مخابراتی، انتظار دارند حقوق قانونی‌شان به‌موقع پرداخت شود و امنیت شغلی آنان مورد احترام قرار گیرد.
🔸
لطفاً قیمت فیش‌های حج را پیگیری کنید. حدود یک ماه است که پیگیر هستم. حتی با یکی از فروشندگان به نظر می‌رسید به توافق رسیده بودیم اما قیمت‌ها هر روز به شکل عجیبی افزایش می‌یابد و آن شخص هم از فروش با قیمت توافق‌شده منصرف شد. قیمت‌ها از حدود دو ماه پیش حدود ۱۷۵ میلیون تومان بوده که حالا به ۳۰۰ میلیون تومان رسیده است.
🔹
بهمن‌ماه سال گذشته برای پیش‌خرید کامیون ثبت‌نام کردیم. قیمت ثبت‌نام ۴.۸ میلیارد تومان بود اما در زمان تحویل، قیمت را به ۸.۱ میلیون تومان افزایش دادند. وقتی برای اعتراض به افزایش قیمت مراجعه کردیم با ما برخورد نامناسبی شدیم.
🔸
اینجانب ۱۴ سال است متقاضی مسکن مهر شهر پردیس، فاز ۸ پروژه شمس راه ماهان، بلوک ۳۷۰.۱.۱ هستم. پروژه توسط شرکت مادرتخصصی عمران پردیس اجرا می‌شود. پس از ۱۴ سال، تمام وجه را کامل پرداخت کرده‌ام، سند ۵ برگی و سند خرید عرصه را هم در دست دارم، اما هنوز هیچ خانه‌ای تحویل نگرفته‌ام و هیچ مقام مسئولی پاسخگو نیست.
🔹
بنده ساکن منطقه ۱۰ شهرداری تهران، خیابان گلستانی، کوچه صباغ‌زاده هستم. مدت چندین ماه است از تلفن ثابت محرومم. بارها با شرکت مخابرات منطقه تماس گرفته‌ام اما متأسفانه هیچ اقدامی انجام نشده است. با این حال، ماهانه هزینه آبونمان از حسابم کسر می‌شود. لطفاً در این مورد اقدام لازم را انجام دهید.
🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.
🔹
هیچ کدام از سهمیه‌های سوخت اسنپ و تپسی اصلا نه پرداخت شده نه محاسبه نشده است.
🔸
علی‌رغم درست شدن بیشتر موارد سامانه بانک ملی (بام)، ولی سامانه درخواست تسهیلات غیرفعال است. این درحالی است که مردم سرمایه خود را چندین ماه است در این حساب‌ها گذاشتند تا معدل حساب خورده و وام دریافت کنند. لطفاً صدای ما را به گوش مسئولین بانک ملی و بانک مرکزی برسانید.
🔹
خواهشمندیم درباره موضوع خاموشی‌های طولانی‌مدت برق در گلستان صالحیه، بخش بهارستان شهرستان رباط کریم خبررسانی کنید. مشکل بزرگ این است که آب شهرستان بدون پمپ برق تأمین نمی‌شود. هر روز در این گرما زجر می‌کشیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451729" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4iJHQnpNYpUQUq7Myvco7QIeuFlWUXCJHge6HKhkfsGdF11diTmFV7isf8JdeQU_hblm_QKedT8a_hy3Mvc2TQDu0urTzGEF54QTJid34XNYbxVAe3avACE2C33Je7VIKFD9Zuq_99Nwz0HerAztlzjvf9_JYY4Oo0bUNNjxcdOqF27BKIrIqsZgqWVzMsxXuEjeVyzXQWdziRqbCpM9uJcN8C33CezfMkSm-vwyCGvhRYiUmdphx4tZ7B7gZyu-luy5DYD69IzzvWFZ4xgH3IHeZQpqjsWcdol2GSwrBAznTX3IbKDTBVCWfbENT72sf6MxObE1qrdbM7Te8mrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: جولانی مایل است با حزب‌الله مقابله کند
🔹
او مدت‌هاست دارد با حزب‌الله می‌جنگد. فکر می‌کنم کار بسیار مؤثری باشد، بنابراین موضوعی است که من دارم به آن فکر می‌کنم. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451728" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSoO2F8nDwDG5yKFiJHxWuhmTbIY9YyCe6wjr_stIqOMol9cjz4bpXcwyHLyD0t88vFmxO3LgDv4F1crP5UZQZGHy4PX6IzH8XeXNSWOi7CmjOHdhYPHvnsw61dsLFwx0Hs47LGhSshjaSmEt-4NZLVI3lB8LxFTznAp3QGCnPCet2nbyA3R3XX7HM52JYa_6qQO9tRHb6Jd3v3Xiae4h7kNSbydCX7MxEHpY7CCikQqBXH24SYvPRXfJNcOYlx6zBWERzywskdejStmAkkUcVmN0ag48tvdAhl1RZHKRiD6nU3S_DAIlsR1M_Oc9BNRYXI_tYpQQSv8ROYaxNx4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ این بود پاسخ مهمان‌نوازی ایران از کویتی‌ها؟
🔹
سال ۱۹۹۰ و پس از حمله صدام حسین به کویت، شماری از مردم این کشور به ایران پناه آوردند. ایران که تازه از جنگ تحمیلی خارج شده بود، با وجود همه سختی‌ها، از آوارگان کویتی در شهرهای مختلف میزبانی کرد.
🔹
ایران همان…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451727" target="_blank">📅 22:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgWlU7KVBx1WB4Zpvg86HoqIzGrLp2-_XxwuJgvRmdUl7Yseiyp__iqpY9-ddE9PCYs9ZIsXhNfdW91BjqrNk-WBgg-OqTG5CQTSkhEzps-ow-YDyBOPXjHZJR7sbwRcFJFeJrfhHGFDjd6Ic3zQFs9NovlhsqtXDIkBkCPDrQwGaPngSq0NfPOEkUUopNsWDcCqSJUWezy7h5uQnNmvf1wQm9ulYygS2kPIS78r5GVbp2VR8ND_fL8EZzhkVlxFW2LadY_Xe3uFyQcTTb7PulMW-4rx5CDaY6DYGU3X4AKVDjXXXwIj-R3bbX6pM0iLfuNcgJgdTeS0hLlmGQOXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صید ۹ مدال توسط شناگران ایران از آب‌های تایلند
🔹
تیم ملی شنای ایران در دوازدهمین دوره مسابقات قهرمانی رده‌های سنی آسیا به میزبانی بانکوک تایلند موفق به کسب ۹ مدال شد.
🔹
۲ مدال طلای ایران توسط محمدمهدی غلامی در ماده ۱۰۰ متر پروانه و علیرضا عرب در ماده ۵۰ متر قورباغه به دست آمد.
🔹
تیم ۱۰۰×۴ متر آزاد با ترکیب کیارام کیانی، امیرعلی ثابتی، محمدمهدی غلامی و دانیال جهانگیری و تیم ۱۰۰×۴ متر مختلط تیمی با ترکیب پارسا شهشهانی، علیرضا عرب، محمدمهدی غلامی و دانیال جهانگیری، هر ۲ به مدال نقره دست یافتند.
🔹
۵ مدال برنز شنا نیز توسط دانیال جهانگیری در مواد ۲۰۰ متر آزاد و ۱۰۰ متر آزاد، پارسا شهشهانی در ۲۰۰ متر کرال پشت، امیرعلی ثابتی در ۵۰ متر آزاد و ماده ۱۰۰×۴ متر آزاد تیمی با ترکیب کیارام کیانی، محمدمهدی غلامی، امیرعلی ثابتی و دانیال جهانگیری کسب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451726" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت‌پرده فراخوان جعلی «محاکمه رئیس‌جمهور و اعضای شعام»
🔹
در روزهای اخیر، فراخوانی با عنوان «فراخوان ملت مبعوث برای محاکمه رئیس‌جمهور و اعضای شعام» در فضای مجازی در حال انتشار است.
🔹
تحلیل دقیق روندها و شواهد متقن نشان می‌دهد که این جریان، یک سناریوی هدایت‌شده…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451725" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های لبریز از جمعیت، پشتیبان قدرت نظامی ایران
🔹
صحنه‌هایی از حضور پرشور مردم در ایستگاه ۱۴۲ تجمعات  مردمی.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451724" target="_blank">📅 22:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">شبکه ۱۴ اسرائیل از اصابت به سفارت این رژیم در منامه خبر داد و مدعی شد که این خبر قطعی نیست و «این حادثه در دست بررسی است».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451723" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451722">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
منابع عراقی: درپی حملات پهپادی و موشکی امشب، آمبولانس‌ها و خودروهای امدادی وارد کنسولگری آمریکا و فرودگاه اربیل شدند. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451722" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451721">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفحص ۶۲ قطعهٔ دیگر از پیکر شهدای مدرسهٔ میناب؛ ماکان هنوز مفقود‌الاثر است
🔹
فرماندار میناب: درپی عملیات تفحص در مدرسهٔ میناب در چند هفتهٔ گذشته، ۶۲ قطعه از پیکر شهدای دانش‌آموز کشف شد که پس‌از آزمایش‌های ژنتیکی مشخص شد که این قطعات متعلق به ۳۲ دانش‌آموز است.…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451721" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451720">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
منابع عربی: صدای انفجارها از نیم ساعت پیش در اربیل قطع نشده و چند موج موشکی مقر تروریست‌های ضد ایران را مورد هدف قرار داده است. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451720" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-zyoUi6O_eh0d78riL4NTT7ck4J0V4_yvmtu-chbCyqw06m4r8NOdstfHNCQ2UUmfyEPnR75oTfXFN7T4IknQlm5iAuYwmoQzNHBgPxXK6p7T1z48Z9X5AExiHofHdfhJ_dcO8dSjCuuhbGw1atlhSg3eVoriyG1jwk9QLYq_YW5KOZm1Y6sTdtJBWYrA57HXJkkWajdYiAW1uAb2YPgvS9euy9z5PlJ3Q_iorFl8PfMl3pmp_9mdyFPhIoPts96sCcdApWfvIN3925jQvGrVwvyJCkHgs8-G_5bm5UJup5FwTPxFKc2DoMbbF2J0Ni5yFwlomcKkMSObLkOOnqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: برنت را می‌شود با بلوف تکان داد اما هرمز را نه
🔹
واشنگتن در بازار کاغذی قمار می‌کند ولی تهران «ریسک عبور» را در بازار واقعی قیمت‌گذاری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451719" target="_blank">📅 21:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451718" target="_blank">📅 21:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسئول ستاد مرکزی اربعین: تا به امروز نزدیک یک میلیون و ۲۵۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند
🔹
برخی مردم به‌دلیل حضور در اجتماعات خیابان برای حضور در اربعین تردید داشتند که با پیام رهبر انقلاب مشخص شد حضور در اربعین هم بخشی از میدان است.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451717" target="_blank">📅 21:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام قطعی است
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451716" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451715">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451715" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451714" target="_blank">📅 21:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fpa_rLA1ggZvBl0Y4xNdykVxaBnc4Lwed6hoSOg-1BJgVPFjVz0WKlV1_qMIgcV_YR9taAPlXK6NyMi6CU3tVpCY1pjl1qGXrs1YxRbDA1Go9sXH7an3KYYAjPRnCDIXQ2Zco4LXNa0ekKOpXo2XUlPCZtNaVr8FlDKK8KBZlc3KiJf59Mh6pM4F05xA6MmLSJlvIvJ56xKe93A_ye8sZiwXWmFYjz7IQ-VFESrMFiGdHHTR2UGa6g5qznpktK0jZ4i5YMX2DwddBtecCTUUYwBdy35Vx1rFHaxiSsiJ51719HPf5a3cjs9FEgXONPk_5Ykm8OZYArvPIdbD3teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔸
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارزش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451713" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دلیل پلمب چند کافه‌ در تهران چیست؟
🔹
درپی انتشار تصاویر و خبر پلمب چند کافه در مرکز شهر تهران شایعاتی با موضوع برخورد مرتبط با امنیت اخلاقی در مورد این کافه‌ها منتشر شد.
🔹
کافه‌های مورد اشاره هم با عدم اظهارنظر در مورد علت پلمب خود به شایعات پیرامون این موضوع دامن زدند.
🔹
باتوجه به اخبار موثق دریافتی تمام کافه‌های مورد اشاره به‌دلیل مشکلات صنفی پلمب شده‌اند و پلمب آن‌ها هیچ ارتباطی با مسائل مربوط به امنیت اخلاقی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451712" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی کل کشور: اگر براساس گزارش مردم، فسادی کشف شود، به افرادی که گزارش را ارائه داده‌اند پاداش پرداخت می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451711" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451710" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم دنیا باز است
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451709" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیتهٔ حمایت از جمعیت: برای ۵۰ درصد خانواده‌هایی که فرزند سوم آن‌ها متولد شده، زمین تخصیص یافته و می‌توانند ساخت‌وساز را آغاز کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451708" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451707" target="_blank">📅 21:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451706">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451706" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451705">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uufVX5YTurHK0-_XiZpaYKHLd9zWjc_peUNEmN-ngDBKIn9W7arG6AxX_Ftkoq8UJaAkJs-JDm4cjuVrJGwmR0jJVC-J8thuTyWFaA6tN3K5ZZzOdMe5i0X7tYd4bh0vqDmkNroc91NMbEOYaBTnTqfpfqFt8c8VD6H4RQkvM_75tevATBteATHsBvAK9OuiRs5W3G84SP3wCNUpABUKwY6KNYuTIj4dmpsuR3F_rXNwDK4bCfBmYAsKDU8RRJxKWYaIG568TaQAKwbwV8hMnr93P0rM6AOxYjlnxzFm26BdXT7mtC-zv_f9k54aohG8OiTvadCNMS93VfWg_JMnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
🔹
از زمان جنگ ۱۲ روزه برای احتمال حملۀ زمینی دشمن همواره آمادگی داشته‌ایم.
🔹
اگر جنگ به روی زمین کشیده شود، نبرد چشم در چشم خواهد شد و به دلیل ناآشنایی دشمن با جغرافیای منطقه آسیب‌پذیری آن‌ها به شدت افزایش خواهد یافت.
🔹
اقدامات نیروهای مسلح به شکلی است که نیروهای مهاجم زمینی حتی توان نزدیک‌شدن به مرزهای کشور را پیدا نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451705" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451704">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451704" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451703">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به عشق مردم جنوب؛ شما چند درجه دمای کولرتان را بالا می‌برید؟
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451703" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
