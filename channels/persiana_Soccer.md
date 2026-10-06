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
<img src="https://cdn4.telesco.pe/file/seWo4KNzTNqOLr2RlujRDogO1mhYdUARB6CO1L05YV-_8mUW25AL4HV-r3NIYCujKXJLMihCaSWzhFOT544PywaIffKK2yV_LeBazTX29bClhVFTD5nJPUDx-Ly3Ei_FNy8Y20r6hd0cNHlQBnK_lfJp5iN3Zk7zpoq-pVV555DlrARwVqZcQZOQYM5yW0ud86DDSlfzbLvKfV8L9oybQRQ-lvEE3IcMTS1UyCPsSsQPlGuM9BnRT-tRiVJiYOdRSjsZdJ9DIUm7CI-gJyIf37ZadT3vGVy8qNZfhKXL6rl9hC5JbmYDF57Yw10at5Usl590tAnJvCXk7TjlxTwIgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 494K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFoK6UF5TIpUYVFYEhEfurT1GCb089vDaRs5VhOIz2CYC-FZGZIWolqx5Mt1BOnzKF8e1e8p0OF_iMe0Q2vV8SwpuJHNcb1DUNIAd_htRbCjU9cU9RIURo-g8weuppYyllIKvifMsXqZP231nKt1a0erEt1mESLBzjZ99dlq2jC3bUMMtMy4pNo-jmoCkOpgUoBDdQpbK-rcY1AifcqzehfH1yA4n1_NE9cR7UV6zwD8LFd7GiQr9iwJlx5RBvcAIOP2T1I4BleEWC6FKWmQAHw6c229g8pcV4r2TSBPWS54dlN0-Lc7_bR9oxHwBAHUOZUIkEigPnm7-OzQ-Rv3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe4aB3e-UPo-wmi6Ehn07UY8yO_82vIPJmRAS5OEMtf948fgDOTiUZzfrlWYPXAszqmoU95f49Qm-PEZhwZyTuLehR6tVc6oJ858s_R2W21LGIvvuPpORwmNcgOxniEZ7XInzf0QK9Q8mzJr_iIYzzcfkYIk12JN9ASeVSfUzDYYgOzP1F9lItHKoBYqfSV7o2sezzcOaqEgvabtTOZ7B9MmWV2fikBFmmjaiU2Sa_N2JinSw3tk7kMDK4AQLfusPlVUpb7On7SB5Ht7AlQjE77XTIFuo4n4FMowjtCZMlVV5l0Jajss8LTSCvQPbgfqZEXa3QjRS_PYbJJAX-fbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzm2gzU0CpNMaXz0HqVuKbsitAXKuGpzq7rGaubKW3nRtLEs3KQLfTAeicwfJ6MktdsYh1RUY-yyAGoVcnYfT7EUWhJafgutI-DzibTPhyEpXWUCSAR5fSWJx0q9Bo7cVNk-ixXuhYm_3jKArZ-1XGv8vK-ORJQ-CBmJm7_ZiSj55Ijto3pggvhHza2E6MDBCfFNJ1AQvFmAdRm_PwYLDm9aIWK6LAtUSC59f25gdOb9qNzMqD1Cf1zy07zxV5teSV5EXbPZFQfMMWEnExpxwxImcoWbEqWjU0f42Y58DlVTOpzM9JDmJHZqCQL4WTzztLR2hrWW3qKjCUwVPVVSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxTyUmbpH0X1IIb8Od0aSjbbqtEqPRfcJr8AzswR468aEmRwcCdO7jAYtXZcvBbNYzCBTm-FaeCtCAmq6nNSCDIruKVfCGoaJ9-MGYEcidvt2eTlkpiovgXxhhcmUsjyhrKWa0xUEgY-02i6e7d4w9BfykufhrGBzyZwv3EpbniPynDD7lP5lKlZJhx6-m183SiEB1VJy3P4UuqrEXlB5RwqWwOabXdZcuZI0llOX80-zT4JQVzzzGDl0VKcPmFML6IXHajtYnOXbHCFFtlADvv3FwJha5et9sVGausVXNlqfm5haDtGS5CmKfTkW3u-ZLKu1hhl8j_hsgbu_X3dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3YJIPtQGvS0qyVOvplItJrUSlGcppoEBMEabergEE-lDXDLIwiox41WH1-rHZJcEjwFNdBa_6ZKf_zpAubfBpAZ2bwyMGTREIAmcaOTWTSszTXBsJwSLrvKMKuZpAH7WW2mZHGQVyOSvdE0aObs_Wc7tHJ0Vw3YugmJYyKNHo1t0Amm3_G_dRDJi0DBwMu9FyjPDC1t4bQXsCQWLdo43md-CV8cBxWKJQQl84yEhoUxrDcah8EWXw8NEMpZ0jheGopqomuoSk2yqqDwUY8uyX8Phpguzf9aBTTaj4CA4fHwHruol2bdhmKNMenkoUmbEt02gqaRWItmr-_Tlm0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn2N_-eoutApHdfLUQ-dzjymu_tyd4FNOqbVMX4d4zlP5yH3PbD9Df_EJiqZtRehee-EiKZswzCDauY5MJrsWzmr0h5pruw89oG7-Mg3lq10UkcBgfAFA66-BhFOwxIVASiTI2bAiVu-77KpfCBYa75ITEsyx7Ss2059Mu8go9JqHVnOd1O_ghboKTIj1HOck8znBq8nB-rWOCFDKK0n6x0xQr8a8ozYajI01i8D6WAfbYQvfLumYSAXMDEYjxyLs1Ff6d5aJ6nTfbUAzd67L5dEcFNijFJvAUJ_qPYVbNAEmrd4HCbSP2IrolfweTAoUALr_moT-ANe0Knn_4JE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLVjLFN7sxCGLk795ml7IwnDp6glUfrT5GuXnI_DWGb0Q0XIo35WBFzRum2KhFPFrsuCQEziSQo9Vni9nVwiaNu-3nz8ZQzyBuLHcsqzpuFMQFyFxGAMzEnE3oLB6_skmS341fJ9kwVFKnjmik2-yQWG0EJ7sJz_N1ehj_ZOG5RJ0ne0jyWk2HMMwoILhI_yodMpXnF1t7nhk5n_BVhcfN6lhmjM-2ucqXAtXNiB5A7h3twIGRSXAb4L3EI41VQv18D8rNHyPxdVwqVdDQ3NWMPUhVbdCx5H2INaweHEP26owMhHksd8O4G0stChmPxAQQ4SdGC0SBT0L05wKrKolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn7i1NoFyBf02MFEZ-IkKnQdMGqCg4z1o79MIlXcwz7nkrnmPR-MbD8K1lagYIpQpWHYiCwBQlCrnPTFa5twAwuotH4hsNaZjzl9Dzkh-0PS-Bhks09bsqodCUtnAqZv6-IuDmlbktYL0dNgkEfswnzaB9xJVYfHoeb_lW7d7FV6a2VD9d8_AY2qQYGoiU5OIvZ_5NFzt9X4JaORU6vOYIkSjdUCjBExol_W2RT33OBM_o6z3A0ENf-J1R0PjB_xTYt_yUM6mYf8zt0O1Mrzu4FGCckvl_sYJTE_FXzO-SYHFczJ_g6-7aeJC2VqW-qlXt_Yspw3dKmYkV-Y-Fltzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osrf5ANcsF97BeJd5OXnWa99ONK_3O3y00g1Q1iImmYeRzbav3u-b5ZW-PfHjQEmZicAwARw8YUO3ewB8_PIXf5PWFGAk4-FQC0-3oWq48asHekQXi_ADRjHaw7PKiEeJbfydlsyaXMssmY9jgFjZFKMqahT52QnybPAWviVNgbeInLr2qkHI_eXLqSmFRwT-yPCavgLsICOLKlmkozD-diyI7YeQiUcM7MR0XdrWUTzGw-ba_6sucWaSfsARqkWEe_ApWXkjQaoUeeJygs8LPCUo_ad_F2Y4HcTlKwNHO1RxJKyYBjstYfhFuTMoEMbjg5uSTafNEoJP3sQKv4obA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/31101" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th6YvDfMTuyyngXjUy7PkUqfjFEpBJCh-0USHYVRq8SXNNm_j8pBYBkq1-mO9l5VkEmShtYhxurEwn8xfac7AgHBu-Zp3wO8vgvEwK5w_vPTzf4P-IvikQYEXt3l0z8RWMyZeOct6sabhGzl62q3BHxUmvkxKpDje4ReqCvcg3iVTJw_VPrULzdYPiuVFlJQE94D8fexdsl15Qhn94U0EvNPqbUX16iYYdTTpR72jSDmZd6U0j0QvjGRzp0wtG1GIwIhlCdjDsDryIK3Trw-y_5Tp06Gq6zfnRVVOhUePjs28KBRkC-WouLnjMU1zvPo09BOurolvcjenM60tZnc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmEbqo67Cy99hVEqnoE5cE57DOHBWnKg5GIVnkViOk4TWtjEhv0lGUYXt-AZaak50mR2HWwml_c3juMfnhltA2WuwcivnFdqRsAHSF9xpIjvQFE-RyKUSqOmmYBl6bqH4jl--A2sckGw6bBFjwnDq2hmvMCLzJ_UDQrVAS1fEFnM-Wy2L4Gxr4CRIcrEnIHRAvfSuknPgTJ306PoevWm3kcTC5K-4X-ONPVz3T0UJWkIa5KOZ07Tj45ZKGrY6CAOECo_fSyQQVjkcOQu2v_IFikKJFb4tsSBRykX7mwNmLX8fyz01Z8SSslKD5mGLFnVWjymkGMkQXhOaeRzUHZMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL7T4WXSGeyG1CUyzeFRM4Xc8MoTaNisNH0t2addkPnbN4ZipQYUUPditxUoTlwv90gMp3B6SDsQOoilL4ldAgGOKQwL6YMLFyExITpXu70QAHmp38iaOmdAspneCo0gnKF9SFkfWTfJBfCbdHdfDFxHXB1nKJAuBbpgBXIqO_Fj24voyrcM2fBsBtNzC6dek7ifa9MoHiSA7nUZPouTMtYEM9N6NYfIT1CaVW1AVZh0afPTokVRzjgBf-DW1OyFr7XY5_VN9zCDm-VlojfudlDPKRP1_dDKYxide3yqIIA4fqZ_0MGI20HXKzP-uZK7YX9QGFTdz8OOS0ks2RSPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK-uQj4udSWb4arKT8ROpqYJedQ6FaqaGfxq5ECg9WD43QoBwnoEasCPpo59BYRkJeW4qOE16MOJc9SzVxbPeQLLkhBGLkxDQH2aVo5PvnHsrdXatIG6H2wbqKoZhHrTSX3MSGOcY5LJRCjtCDaDeJ8NsU94ALimUg1Q80uqe0cRNJ-FA6Ns9kIXaivtqDQpWMRTxXz6NTBy_e8jQ5aI9xJteGvA0Eh6YR5g_kOY4iVrDbSa_ow-ZPmj0kheV6DsnXq6FWJ-4mYMJmkxzkdyL6BqYzYtN4eVZ8AjcF89dzHpD99-MogqQklRDf05JILktwjhWsja2pJudle0yfKEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=J2lUef9ygKjnoAAOtnzZb4jc54zFmvBSY4ams_R9-RXWvViLZ8p1Se0y-Q9iDFVq-Z_4GtQtujSmLKiD5qpAeJyrE9_JfLtEx31HIwaJoBOXyGWFzZcRVrWHRSwybK1gTLYyZMXf82TF1cdoBfxZyjBPQLrjloH2I9y6kiWSh6Nq8RNQuYMzfJLuqbZSTfXcvTqru9-fLJQmbB9uDIPOrnDU9DTvu-YnDx5S2sZYnij8ztCGWNKD3CyVjT36KEdttTRAEAMRpOY-3HkqC4xmcHVObKdz-Ig3rtQH_vBbSK-iXLkSFS2Uc1Zw2PT6rInhVphUof75q1ba_j69l_WZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=J2lUef9ygKjnoAAOtnzZb4jc54zFmvBSY4ams_R9-RXWvViLZ8p1Se0y-Q9iDFVq-Z_4GtQtujSmLKiD5qpAeJyrE9_JfLtEx31HIwaJoBOXyGWFzZcRVrWHRSwybK1gTLYyZMXf82TF1cdoBfxZyjBPQLrjloH2I9y6kiWSh6Nq8RNQuYMzfJLuqbZSTfXcvTqru9-fLJQmbB9uDIPOrnDU9DTvu-YnDx5S2sZYnij8ztCGWNKD3CyVjT36KEdttTRAEAMRpOY-3HkqC4xmcHVObKdz-Ig3rtQH_vBbSK-iXLkSFS2Uc1Zw2PT6rInhVphUof75q1ba_j69l_WZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFis50W0d5jx9PuJ8jcNXodJWMLo4bBdw3AW1fMKJmncWUcJj2qYFfUFOmJuNzYubRitYrG6lTKU-RIYfnZCG9_BN5ow8fuVBE4YobOMhXgUs-61VPyV5Coo4teUp60n_Qc44HChsXklwKrXsxX17KfPsJPSAOfR26XCM1RPMJzuLD4bFB2V7jX-kVhjHXsrmeS3dfYvHSFjij8K9nSWYJq9MOOzLrursDHGGTvWgLnHQXE7Cg9PWyCcMWKAqCLZ7b0xmPqpUgTHeHrKcdEJnfKM-2FX6Yccn1OTdH1HpHLT-1K6a_s3M9rATBBeT8sUU7gh8xwNT0HM2rOhPTMlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5T4TzUEEola_lVmH86tyKwmoDNptKuH3P5rz-l54W1qUJ8LA9-Hiw2mwMopF-BkYQpk5bWC2xw4xaCYwRnzbZtiu5okkC_eD1QA6JVyr0qY57Tr6135YxwOrrGAHtYQapp0PwS5fsZUBfyRfDwdf5ggQ7ILXF_086jEdvMK14gird36fR1QTa43SZ3BtVHbt2h7dhDKV_VrPg-soih9hx16rvlVBLCFhaZpYPnBK37aKF9a_b8VFcwTlrDipIYgnHkzBhv_5ITYnU2N1R0dq_x0H36Z1oZ5xXmgRfUgSV80mw_PEhnX_f8dNmUmry3o40Q9KCvq7em4_TdIgpXRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOU7E7-kMpf3QpDlD1cMgDR_kt-73HbiwUF7F2nIegHSrRTa_Nq2PI_4M-htHzE_BmDHq1c1tYQhw6qf7xAjizC6G1LW6IlSBFL3V4Yt-inaCp7adVqIJz3sE06yPt7LMuTyK4kzTfpCFRL__rKaBayOirSEHomYlE5qF92g1K20Hte00JdRN1vvU4B1_Bv0JYKJTDVmIHuZtmB6v-47zHtIfsHSZbmXO8XHXfLt7w_iDkO-7aSZxqZn3mw7RGKhosfgX_7neuZN0zSHT6vhBgxVS_KogRMN7IpNdRdvVVH5gRCcsvdQwdXSe7z770lNCY066R1Mt81M5Q_mRWBQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=KcIigSEASDUmkbujR4EcCAPDWVEr2sDBrWW6N902taaJ9d-Ex4TUHRwl8FHG5HL9vnMioi7XywmndQoKG0SD3b3EvTyOkoKLLuo4Mjq6xc3nNjdt-YcFEL49H-QcRhDhM73eMHLFMHeujXzPkXGGeyUflbJUj-ThO1ExmtQJzIHx8lyeXMMxxE_ske0LA7UjhPp3LittCf9vkpgQp_Abb1tHngd8mypeFz6ATHDZ_BB-rlbSdmChxUqR9lYGYTgEi0QFYb0Rtj2ui5hCc5BgslbEfnvV86NlWhavPTwquKe8w4tnI7Y580B0h9Yf_dTpIgq9mGyzA7YEa7j5G6Qwrmq91ZMDX9wJdgi-234xp8RXdWhTTVawn_-dZkhUSUQc_LwLNhRtKU0QqX1vJCud-vWGeS_Fw-kXHP991nEiYalTCOQ3X-ydFBSyAO2lSbgR362h0GyiiceZhVytvHgjInISwibdj9FFVpn1t70DOTWcOQsMRrRp1B3tp4pD4ikLzvH5c7EwtlGgjqxzbwgSzWR_hYA08q5AXQQVAEDuSRB12J_4t8VxD0xF7GWKqlq-WvnkY6nbr2InZvBdIIbpHD_f45V4UuYpkX9PsUpesOjB8XvWIuMK6vzjXr2ZF9i15XsBlibNeFi_eDQaUzUrEA7nqAmJFrzxPI8zqQJ7vEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=KcIigSEASDUmkbujR4EcCAPDWVEr2sDBrWW6N902taaJ9d-Ex4TUHRwl8FHG5HL9vnMioi7XywmndQoKG0SD3b3EvTyOkoKLLuo4Mjq6xc3nNjdt-YcFEL49H-QcRhDhM73eMHLFMHeujXzPkXGGeyUflbJUj-ThO1ExmtQJzIHx8lyeXMMxxE_ske0LA7UjhPp3LittCf9vkpgQp_Abb1tHngd8mypeFz6ATHDZ_BB-rlbSdmChxUqR9lYGYTgEi0QFYb0Rtj2ui5hCc5BgslbEfnvV86NlWhavPTwquKe8w4tnI7Y580B0h9Yf_dTpIgq9mGyzA7YEa7j5G6Qwrmq91ZMDX9wJdgi-234xp8RXdWhTTVawn_-dZkhUSUQc_LwLNhRtKU0QqX1vJCud-vWGeS_Fw-kXHP991nEiYalTCOQ3X-ydFBSyAO2lSbgR362h0GyiiceZhVytvHgjInISwibdj9FFVpn1t70DOTWcOQsMRrRp1B3tp4pD4ikLzvH5c7EwtlGgjqxzbwgSzWR_hYA08q5AXQQVAEDuSRB12J_4t8VxD0xF7GWKqlq-WvnkY6nbr2InZvBdIIbpHD_f45V4UuYpkX9PsUpesOjB8XvWIuMK6vzjXr2ZF9i15XsBlibNeFi_eDQaUzUrEA7nqAmJFrzxPI8zqQJ7vEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVUZ1-Gpv7nLd_gDan9vzNPHr361-8jDn39Y3viIWro3vxfrOQ7v7ODwBnGVHcnOLqM08kUDcTbhgoYgr9_ITuLVxEGr2psiRZoG5N6VrZnaRjhb3qSCRrZhwr1CGfNzbZg5hkGXlHSkJ-Nu2ksH9zF_SL2-Q5EZElSUrFz3G76r0B-sJADXHcm-kOBcriUEg6BRDeT2rTqR43lJ7XrbjUEL_7Ju6F8_uQyCZjnhOB27fx9q9ZFw02L6gZq8qDrtLaLL0_UhWEoj7US2JQD-DClmXGH0t-O1Njr9wro9c35uVgZrKd79KkCvwb1ERShStyyGgeAL-cYeazLUJRk4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e80_whgCKO_0bOqS5H3fL3Hns_E7iy4S78TtHpdLlvPVpeGUhZBNobJ4CbyvhM2fkRkApLP18IHPcPFUyAr0RrV0CIgmQG5GZWJ-dOakOaMCBpYc7BPIzkRkKTWsMORmr52yHfXmaLUcD7yFMwBLbKUtxgCmRDAkqyX-3KVhFLWgucUYpD1TWOsSDgTKHieHs5Yd9RDOZIsztj0rBgk7ytFiL_MhqwnyJgWJyrSnCZ7YuHss61v8a9B4ckIzrkHUqMNbZxo3SEZvqkeiHsQ3agoxC47rMQlPuez6ven0-Vl8YgAOFo05-tN9RGx8U4Q1xy7huYIY6_GLcbZgwrjrBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKjJk-f2-kcVmzPPZI-DWu9REkm6-Eo2mdjyy28VsKR9MIza6qbfwF2NtPQF8EdyIB6rHIHsSBSMX9yxcGNBlFt-DjyaLPvm1RiY5i0JQFYvG3orOxB7mFew2Qnx4zjfoJBFNaEEXuqPq9RascvruQv-zWrenC8AOZ-kPlcG8YCJFAaakKyBlOoKCiWmLJw-AKdyDWdR6ELs8-tytv4N1sTc5Rd328Brrd7cN5_wF49JLsRBoMtfxfi-2mZMqwsI85yMINeBCumQVaJF0Gu113EtkqonPuhWw2lH_YQNkx9QLjsS4eSLWU3P2HHpTkjZcX95h0wd66Y0OAfYCEr-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnzJSaolw0xIJRX8Ux99qD-pdcty9lDUEVHDktV-mJe9agzAstCmffsCCxuqrWRWE4sbkVOpOFCgkXyqh91XhOPZeA5cfIunVTbr86RzP-JQzGdkSHofqRG9FBDH5h23EM_cJtMqH2btwHmlxnOejSK15vkyYutA84hoqqWHkpWdFXl5KZNkTlkHJGa8OysNZxYxlBiRuvuBZwFl-37VTYRqRvieSTVh9l4VQWpJZdYhPBj70soXuUrRYtDEQJouwYm4hHZ-wBIJ9ShUUNSu4-bYTHar16Q-6nxMZMdrfrTT3yAOC8wX_dGogizqpEe72aXsvOKVA1fVpGl2QHt5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAsGcEIhGKnrxbch-WQ3fUYUoylpSzgdifQlccWZ7a_V_jHuNdhXTGlGi1YqIHxnwVTTYL9qJAW5v5wgff3evzv8PgPUDlO8ugMj8SjRn9MJ45dFENCWILGCwQDRpPQpm7I1Oz_ELsOoTiHr6yJPc04OWfISt7-K3EJ9dxFguCk9EJ7JEQ-VLVNoj3M3ooVmQp5Rw6LiuXn8h-i-vAnZK7lwLgHuXI5lGEyOKzUXbVw6bBA3ziwPPexAXbFCDfVXbSnmB8CxdHTAwb2MhUGG6ZJe5Xn08t_lz3xFTF5hSeamtm_l64RIMStBti0wP__k99jhEt3GZll6R-2OEMIZHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJV1bgGhOB9uSsicBIzZ75AJt4lAnN9ij-WlP0qOtLMZnR7HKZvjDfJMBhO_tX-04_jQghuMMyA_W7fmjLSpel95JhwLhnBzR6iHDBAavh4OA7uQXZJN8wpg3HwWu6TnH7wT6q3PAZNyXjllcbDW6UvZuUeDflzQdHJrXS9nikWTo47VgaksuvNqIVBKHfg7BMcp4cB0jMEqP0l_JKnWgfCb_CrNc1_TrIq2mFzfrv5fRih4K72dAqZy2qf750nb5cNma3oFCfblZU-vsBlRYKE1oPUlsNPGOu1QvCBu7XfOGR9-iND5MaGkWkZGU546Ni-0z77dibg7UvKe2QEdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYU5zEqKWITfO1oYrtxI_ojFPZkw8LPnp66Sxp_PQWFpBTJFbsag4qUA8B7xeZBSKoNcx4Ni-9A8FfJ_Db2bl_UVRRIKuDXmQ4QCayJJPEUVxe9gU1W9ockJBvcpFFGsRAkMwM7kiaW7SOANj3TGF8VefXthZ3ivBJy3tAVNXpBomrCxPP9Gq1JrdpDPw_Vs6krz9Tq5b9FM9B6sVEjzICzoXnuX2Pk-JhCvbo0L2unTVCyjKXyTQMIsJt7_msTPdTnFbRkxXF9vnM1kI5EFyDS92Q24v7iJ_7ZVOMeUbYdQFaXqZn0-Y0W6lOOZSZ8EEvW1hXCgQv2b4_vzZF3ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoXKBBAndpwsBpqaSgNFg6cpLgRsINfebTi5FgaXZhoZMACuFA2u5zKXLuoPumfxReRKoG9FuDQHR4nCwhhk1V1eoPoWEvLikZJc4FiKuxI8pThXnjFUL7iUiLMD3j9bifEr_NoNeJagfGnKKqBoyFKvNBPXoxasPUFa9ZcsFHmkTOAPaJsNoxX1djTutk8RO0oE8H5J-XZiduoQgtyI5W-g_-dd2iBSX68lxm5RsqEapgitQsSyWkgkztZNlXBD8VbncNqjXAcIyr4xwTS4e3ntgbGODfvZMbUfTjQ8ElZESC49ITPAexpQtb7Ab39tvpB5P0O5vqwwRwxPuhF0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=GI6aYwYoY162T3Gwn8C5Wmexuj1fEOhutIdP3yNpOPjmxZqQRYvXcBGupWdsuLzDDi1Dy3cMimyOcHa-wlosd-HstJlGIvZQ_5RVjqn3WGz_dMwh4-mpsO1rjRwWSLHdAgSx4gmQZIK_-DHPocNsXtpS79AlLwtVxdCvDpbWMyhUFSG5Su9aRRswL6BsUwsdxV3dY7Br9Yy_9bt47au5r3kGjTuI8Wx1WTN3Ew-PxFsQDVP5SnBWu_zVjVPPegrXdZAo2O7YkyUUf6cFtdNWyMSm9DXkj0idhRXv0VzprSXDVDKik9dFKjs7VlWENlSX1UIOTZsAgqmaqmh9LvJj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=GI6aYwYoY162T3Gwn8C5Wmexuj1fEOhutIdP3yNpOPjmxZqQRYvXcBGupWdsuLzDDi1Dy3cMimyOcHa-wlosd-HstJlGIvZQ_5RVjqn3WGz_dMwh4-mpsO1rjRwWSLHdAgSx4gmQZIK_-DHPocNsXtpS79AlLwtVxdCvDpbWMyhUFSG5Su9aRRswL6BsUwsdxV3dY7Br9Yy_9bt47au5r3kGjTuI8Wx1WTN3Ew-PxFsQDVP5SnBWu_zVjVPPegrXdZAo2O7YkyUUf6cFtdNWyMSm9DXkj0idhRXv0VzprSXDVDKik9dFKjs7VlWENlSX1UIOTZsAgqmaqmh9LvJj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC0McH7M6qGo4SoIftEe_7HnrMM1G5Mwi9KoCas7gERfXz3htf0N_kcbolypwIf2eOZyZnapg2DoAoeAcOX9RuIY98OsIwedJSm6BAxj7_-b6CJgTmCHrbWipaO38vE5JCrw0eDKjtwEvE1k8-s07shYVgrbwNvuzKOufHPrDUygUsWzCDZv-gq1TXsLjmkFBAXjkDq5mijt2VJyIAgEhnLwrmnSH_6sGmJh3c7G2Z8OGyKTXdrockvoadsjMWTUkQwpeLZvWhYdNeDczeHTf0KIVf7U00qVllW5o3l7XKerVTsBH5kfQdjZinSBDjqvAfHaCV_vVB4awR7jfvCgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=nHGyeItDqT4tJXiTcGVQsFXXfkvB5gblESY9TcvMiBEk0vFTwcdcidkXl8DhdN8lE84U9gSZK6yRChZ31Vg0N9ZzIRSXf9qOBS9cXNzxw8cdNJ5R17BAn9K8sMF-SChkeso7EgazUkYnB4RG1bBPagNoWBufHZU3ZMQJz_B3NOBBgzaF6lLt2bzVTj1lBToD_0-3R1DYo1Vg6z6n_5uRYvnt4Ziw32inQj1y0-QmDuGp86VMeVcsb5KJr9AZD2YGdWiqyOhSZpXBQiPH16ixa3IJSsM1cT8pS70EqgNhLpRrc6s-72M44fvWCeZB8joII4EmaWzMxGbQENbq0bU5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=nHGyeItDqT4tJXiTcGVQsFXXfkvB5gblESY9TcvMiBEk0vFTwcdcidkXl8DhdN8lE84U9gSZK6yRChZ31Vg0N9ZzIRSXf9qOBS9cXNzxw8cdNJ5R17BAn9K8sMF-SChkeso7EgazUkYnB4RG1bBPagNoWBufHZU3ZMQJz_B3NOBBgzaF6lLt2bzVTj1lBToD_0-3R1DYo1Vg6z6n_5uRYvnt4Ziw32inQj1y0-QmDuGp86VMeVcsb5KJr9AZD2YGdWiqyOhSZpXBQiPH16ixa3IJSsM1cT8pS70EqgNhLpRrc6s-72M44fvWCeZB8joII4EmaWzMxGbQENbq0bU5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkHMS-NfgfjmjtXZgidfaWAdSHQp_aTswHuu6Z74K-CLFfmZbddFRC27JO_6weXdMoZtpRYlsIevEdNKUgR5M2FSffbUJwYk7UyEMPpdhi5L2xaEA__LJUdum95mxuayjmzWZVujLrLpfoiFppvGqz3i86f17xfdS2m9RipIZkon1D9FbCmlIhGYMYvedtALXbz2wKXQKYRt7nc_XvxK5Cz6eltDWj6SzyNi1r6cOjQOoJirdofDJYxmfYnC9f_fn-gk-Ky9QJyqpNn2GUKfDcIOgMuk9EVg5cQ8RprAHOkzJsJC0QzRkX1R_hPFLGv9807aww_BEGYwAqdGXFqPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=Oo_YwJUM51Ezr9LO4p68H0E3ai5Bnwnbq3gFf4QPaDGbKs8WveNuDUOzo-FeVhaRCsCI4nzfceSaV2_5wE4asjIJKP6YrkcNvpMtT4ZQn2-Gahyi1C-iqO-SgX8I75D0aBhvNuxFfPDrm5dXvbgYm9dUIs3jOiJwlyThZklqE5ZolHzPYG79-PCWbpz6LGl5rSoCfom53ILPWz8LBWYI5Q3FZ-6YD273Sn_nZipBE0bVwE4TUYQw8NwVSMs54q-2uWW7RYAJ-s0gGfgKk4ta2OMnRYHXzLENUHN8KaqJVvettFTYw0LynIsP504BC9SJHv6a5NAaDytw67_tAElTOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=Oo_YwJUM51Ezr9LO4p68H0E3ai5Bnwnbq3gFf4QPaDGbKs8WveNuDUOzo-FeVhaRCsCI4nzfceSaV2_5wE4asjIJKP6YrkcNvpMtT4ZQn2-Gahyi1C-iqO-SgX8I75D0aBhvNuxFfPDrm5dXvbgYm9dUIs3jOiJwlyThZklqE5ZolHzPYG79-PCWbpz6LGl5rSoCfom53ILPWz8LBWYI5Q3FZ-6YD273Sn_nZipBE0bVwE4TUYQw8NwVSMs54q-2uWW7RYAJ-s0gGfgKk4ta2OMnRYHXzLENUHN8KaqJVvettFTYw0LynIsP504BC9SJHv6a5NAaDytw67_tAElTOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFIJ4Um9q6z7yrRbJg4RSHjK5xg5ZKCtW8BdrsSdZtze74AW99eZqZcNYjKf5gxZCSlwkRRfLIuJIrPWu5zL0ttOtNaelvOnOQ5kGC_dmLZcCpI5S3F6S5MzNf6xen5ig5-_iXTeBTQuzMdkB_DVaw8u-L_GdrFthHMiqGE4KRQWbwykVPSiJpc8sq0Eg88gg1Yfz5o4330dU_v-wU3lYj4YKE-8JFCaKTkV7Xm8skJJLWlSKP3o9RQwvaaR-MBK86qxDit6zMTMRm8jFyXnHY7DQ5s0LD-TBgDy2df_ep7QgiogBcGC3pSGssCyKN80fjYXNyqpwLdeJ7r1KMHJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/31076" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcjgQkIgxeLbmPty_3iYgstigKH7dj9NE4Enr9W3jOCOu9OsK5-WxXnrXdTGOyxXqVJXqtq1wYK0MnzBmow-7oywu5_KmzfshdStw8aedREpJRt1Di5OjiikIzDyUzXVmqBVxy4epfDbfIWjGPoWmI0Pk4RScd1Zu0XCBopdjD9SrAQK7nS88mL9ADMaqgVeQlVMgL5nNpSv4iuewbKEtFrd4ZdUg6bfq9972L5REAIWLXVzumtir-ZhY7Hm3pXsg_Lsr15_B4sd2UV-UvHOmN5SOHiFDjYICVML6I2MvRcBq7aPWeUJP-yg9e0tsFD0CZguxKGvL8QFoxhubl7Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5V6VSFyNjiteZSQDDlD5ZUECJSmruL7H0tv289ESeAj5z5CFAXkTYegHPugZDus6WeiZn8kXzUBtkQ5nb7rn2jBpSw2hCiguioeGfkje8GqgiXGOxNYi33iyPrzffC-ul39hEnn0eX2iD5YyKbTtVfepa7jh4EZbr5Lrjg6Xo8cesU8E6xnvbAN-8DcwCkj3zleiPohzc_GG3FOHtOTd7AiLjNql_xTZcPWA4F1yT39DzIE-t8agKefKOyhoF9WWAomRlT6TDJA50NUCA94hW9jzL02WX3Lkll-Va7rpzbLbjks7xhAh1H6VJa-Vu84G0DGWYUy7gHUBk5leuoM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYoMC5bBImFovqvF1M32Qd3W9SMsW0b4hqRdzWWVa1QpDb_9q2QfsIwJ6jMYOY8ffr1rEny3jsHOIYFhzDG_CFUbDiDPsETpB6u05Y4yvPOdcJJSAsdgY4DROPzWYjOZvEMsmIYm0lrCD8mILMa_1dR-AOHsZTU4Ypzqj2tOuuR4RcwVRuTgbLuEel9igObDwN4HVt_cD6RMOCo0KZcu9qUvGMGq5wAeGsEK-8xBdrnBBs5cSYbh14YNrNg2intSZ9ZoT_iYSaATRbpIvUWiPebVr3Ox-f3PRxjXyXFyA8M2Kwz4u0fvVzL3piEjSFuqQnhEfbtx605ews_eVZTCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9zBCRINAgcwe26CqFQsbOqCRtFFfYi5JWMyHlthS5VhifkA8onRgmlzxWovmINlWgsfEcSYteV6pNSf301ZteVXMWyssNr0R28tyElRdoMTbqEo17r_Ug1cBLePd07R-N8UPJPTEneNIR2n1MZhacHTVtPWC-0TvwRW7Q80x-HuRVv18cSfIa4iRlximy3mRivCA87TYPzF37IPa9e_U-VeMMTf6M4XoCQqKWxL3exXHPMmIBLvG2OUByHNzc8QzoZkLVprAr5sATGr-lxIn_jpKQqyoBIcPLZTMH8kg1U9rpg-52vfJLiNiD65jjhquwngZ2bBAdUiwuMh5K9V8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmRAPtS8F8u3YwECevmhtxF6GLNEB0sNmfcKaXHG55WQ2Or6kyivkHdzqnAj-3l_FJNmmLMDJxvo1fHYPAIinlEENwU1zrmJ095trn-abeBQ2neqLIFKNOfyTF_VTvR_3gXXeirLoUJHaIx_rxy_MON5mcVyYzbjzGygHMnksRF3gMDEiybGyEfg2RLZYtLFqUdeEe7DTkycXs-aFLRC_i3Y-MLx_OKw5NHLnVSk9tgGfj4vXhKOk7tKNQiF1J81OeuwUM-y3Bg-zFHXV-8N8aW2cBAJ7LsiTH9PybY35z9VtTeU7hXlaj8dBGKJwyr_b8ayRSQR3bjCwDthpwbn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd4akD-u4047_r1GkfJKm90TPypFQW1sKamTeeXKkBZ-NErtyxOZZ5mla-9oYf2D9Zw-7rdflNY7UMSMOLvAsyAJUdmZ578tMoJw3sgwUvZbRxCNW2084ULS9bK17XqIHBCUOhfDQJc_irIrmPSzcfs204Vk6koPDgr69izKZ9jh1wJR4Xh9o7hcoNmI94ZJb_Q-aRe84deYCUC0as4eL_wSX03H1tfRSHsBXlDqIKnmsxZ76mox0pe3Hi80t8CRtn9tX_EZME5fpSDsW9qgCvnbrXv097qMy2PFnUbVEIAcKXIzS2CxVqPfBuDVnn6prtTeH0mkYeGcjjxVW2QzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTYsxKJfBQolMiXH63X804GFoi2W4zcBze_tsaQmdCoBGWTX9tc33_gy_bdP-wKBYd9Dl4HJ0O3Bbl72JfFO9fTx5Bgh9fzddLQ400aazkKGqjZlE6uWSsxZ-NoTe5uPORKFAkT_kSWacD2af6VMunP8glh6dliaADHLYkwyYowmKRC_905jdDNd8dNIhnMDSbq2dKxo5ifXehKttFXIsOwu7dY4e4vMDLTFKWT36ji04OU5yoZZvkhrddA29Hta7SNl4MqxbiWYtjRApyiuLqB4kBcpi0t9kk-5DOm_TOox4kXhXMJpIhcj-SBK4LEFwG24qRgCL4gT_Ug4ewdEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=gqteUSbeDkoeWcW_iX-18DFEyXBqde53SvRQTMT9zka1fuUl0QSzQEutwMO20-ComlWawwCzz-4PZs5cGBg41OEsXD7yr1yx92ECXGks__IZJ4EzPMkidCY1uCwJfbRs0d9jrZ1c1WqEkADQsH0bnlyWWmmSEqCofLflD8nM_6RCIZL00yg-b8PdqLwtkiXpMTUKBjroAiZRB2IX9MhIRrBUM1Gf0vbuH4MBf-OHg_6KZ_7l2R8xofv6yD0jYPZvn4lPOj4LZrtFLCfSGoonjwJsSnWyfurOeXHOxr95C4SC4XP7h_EpZj2_81yULxxfIJGkRxf0Y-SDMdavKpiSvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=gqteUSbeDkoeWcW_iX-18DFEyXBqde53SvRQTMT9zka1fuUl0QSzQEutwMO20-ComlWawwCzz-4PZs5cGBg41OEsXD7yr1yx92ECXGks__IZJ4EzPMkidCY1uCwJfbRs0d9jrZ1c1WqEkADQsH0bnlyWWmmSEqCofLflD8nM_6RCIZL00yg-b8PdqLwtkiXpMTUKBjroAiZRB2IX9MhIRrBUM1Gf0vbuH4MBf-OHg_6KZ_7l2R8xofv6yD0jYPZvn4lPOj4LZrtFLCfSGoonjwJsSnWyfurOeXHOxr95C4SC4XP7h_EpZj2_81yULxxfIJGkRxf0Y-SDMdavKpiSvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ztf_MJ9-hTkYgayIf_adJlUbiUIY_XoreTBHDihsYryQ9I96-eHiZ-ARwj-1aSj9q-lIajj7snW0leUxQEIwZvKE-1t2EJo1iqN_8Zxkf2epJUyBmB97k4PO5OQIRIqob30Mvd960v8K7TIxRRbxHg41c_Ypv15y6vQ5bow3hZ1Qlh-AtUmZufdahSMODUP88kzvzSseN2ZKJbZHEYeJe3BUQQ1ZN_Ukhvu_TbwLMreZ7opG2zYPrNXklnmkWOv36kEc7rqE0rh9Yn8KmLiGJUe3tYubB3dLZYkyOBYHytgEItUYv0OnrB8BQdIYJod4NaWtiZJm1RxfeFLLPqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPYTloHwVc5m4J2kXQfg_6eGeTVURCVvW1v6CC9KIXrDtIAcFskHP5Jv0OyWIM9iA-zfyqYuo7uox05Te57mhIhFEHFVGj8QZCSr2a6B8SKC2m_r7gw2YjMsLKTmnTZHgFhP7cjPK78AsHyAUpTbVrV4YWoxhB1G0PN56A9IVtJMcFjrRlZKCQpD_H28WjtmwqpOP5TmDVtYNJhm3JqiPXcmbB0og1uYMLrHrDuIYu-JpnosSecNe0qjijpJLKoE5JDJi0bRIurnuvBO4Zh_UOFQOT8gyEpFDFPUvak57WMmWYGju8ASfrrUVyAf7GNZW2kSFw2Eg6DpFkdjNeaeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=GdjTNsPBvcb7SCzYrTr9WW0n2W-41gmKkXSPKbSPygfWlJub-JipAEo5ohQL1-GuoqKqooUCRIQgwyoUfGXjnRVeGSfwnDmgkvz7AXPn4J3213H4vhIQjHA5zhpta_gjLwVwJH_yWX2kjvYk8rATir6Raomhed9ioJ2MDmoRwrEQaGbz2348OleQG1V1rK_qe_PgytH2pvjEhjuGwHjASOA86gxdA8IZ-rdpWuDgpiJTmE0XWaE02HmIqJPECpIFEnY-puDkvWh75ztlCYB4mqwYzE7L9pUBYgvtvQzvzNIMbZZkfFaThA7tJDDxzwrYKolYwKDY-1TCw1ciyk1qsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=GdjTNsPBvcb7SCzYrTr9WW0n2W-41gmKkXSPKbSPygfWlJub-JipAEo5ohQL1-GuoqKqooUCRIQgwyoUfGXjnRVeGSfwnDmgkvz7AXPn4J3213H4vhIQjHA5zhpta_gjLwVwJH_yWX2kjvYk8rATir6Raomhed9ioJ2MDmoRwrEQaGbz2348OleQG1V1rK_qe_PgytH2pvjEhjuGwHjASOA86gxdA8IZ-rdpWuDgpiJTmE0XWaE02HmIqJPECpIFEnY-puDkvWh75ztlCYB4mqwYzE7L9pUBYgvtvQzvzNIMbZZkfFaThA7tJDDxzwrYKolYwKDY-1TCw1ciyk1qsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4D7iSV6hjkQ590kz17pndZ_ne0Tqs3HCo1nVMdPo4ZGQa4re83TG_UTb_XvN3Xk5R0tDNv6lI8gZp96fQmwx_BrrwHTcMYLssqbKPO3Zoaj-DlK5zAtqnoSv0RP2qPYy6p2zf7CREGwwK1n6RY9PvQtggE8oL5w-ZgcwVAwnBS5vpIofnljf-NeBqambwv-G6fTTK1q4cIK8WYfXQyas6sukQg6KeeRylPwTwYySGGRyRi_LieiYexv5uhtEt-MG6VzNKmPJsQGNSffadW1nKsAIZ2vSTu0MSJXekBhkkLNyBxMXS69uYJ1eomYKsm203RyL6Os8rJs67VpFURSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=Ywr0b-5jpiBsBU4SfzG65pJbcurxuzcmz9c3Zxy3AMpcmP7LUmuEtJglyqbMIHWqS-ZDC9IauERBjRTM1LkyR10UUvNSn65Z5wWpCQTIID2Pnwjp8Eixz1hJ2iYoGPIm9DvnsYjUnm-LKyVh2ARhBQCpWskrGpXdsVh0PHmpoP-xBK4K8a37e-ha4LmPFZtg2yhif5WW8lx6ZSm2eVMDd87__JDiRRSCQlizM8UENjLSn2HCP5_WiIm_hozkKdSMI1oRgrX8jnltJikU3grwHsbmgERiKWA_kZB1u2DCDajISXfN6a64BRANgJcbTZxDuIbWDHiCsgj65Biy-3XMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=Ywr0b-5jpiBsBU4SfzG65pJbcurxuzcmz9c3Zxy3AMpcmP7LUmuEtJglyqbMIHWqS-ZDC9IauERBjRTM1LkyR10UUvNSn65Z5wWpCQTIID2Pnwjp8Eixz1hJ2iYoGPIm9DvnsYjUnm-LKyVh2ARhBQCpWskrGpXdsVh0PHmpoP-xBK4K8a37e-ha4LmPFZtg2yhif5WW8lx6ZSm2eVMDd87__JDiRRSCQlizM8UENjLSn2HCP5_WiIm_hozkKdSMI1oRgrX8jnltJikU3grwHsbmgERiKWA_kZB1u2DCDajISXfN6a64BRANgJcbTZxDuIbWDHiCsgj65Biy-3XMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4QAQ8N1COCobHSdNmmL_gm6qqYOaCN2BVNX-Ey4y5h2UEwSaxt8TxzzHloGB9hChZEW3l3whF406GBeYYdIUiFTaukuHbOUU5Avk5TUWcx3HHiCf_ZgL8kdPXICrmmCLu2aAXpiaqod7AFpXwxq_k1lmhC5Z0lDxbVVrHWQ6fSLJGAwLdGP9CQKYO1w28vzfUaWPcruJbSLSgZuUuZIWTmUmbCFPvecVJvjA-V-X2aZntK6-2QLwKwUZirP9zWy4wI4l6diyUZDcJlgmDXfqltZEmeYhyqMwSybBPAXed2rnTOZHYufmIeQ9Ko0Hd-ZdnIrhtVnykaFjGDa_N3feQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiKp7fGnBwIsM_MPLx6-cX_Lk-l11FlG_s_mlrjDEmDG3W5lhGR_BEnd15YACweAb11IKRj6hTDdrrAD4RjYVZwUnCMxIBi6DJvSXPCY3LauZa1KSN0ogTZ_is9mahKuqBUtF9UzaIQEtFU1MYI5z_JyM7IyhncmfrRVzYgFIDCCKA5P4i8Cjdhnjb5sTNGqv6p5lpzho0K0x9UxP1okp2AutBDbe8-W78Pgl3vq6NxhtmHlwdd7SQSKsThrTmmFw-u_35gD6Q7jVx63vrs4Uc8hW_JdfUF7q_Sp5st2hAZDb2pgrJtaw9jS7aMsZ0dlomrYWX-gj6HRbDq-8DuCMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=FpAzkLWMkdnqGvhcF6HNE_6bm1tZ2OV63KHQ47Tocc1fHqWthPuAi40-OGFoie2UUQ8ZqGnQm2iTGYAdtBwy-Jz54C3TGxKkOOhnVZ8P9hDK7pBQI6u9vAB6srHWRpjDtxXozyJOAAecG1kwMGX9HwYyo-w96_flbcfjBi25tao32P1rlqn0DDO2TpZRCDAd5fPLJ6BDFeVgEieRE1F-e-xRIn1WvJy_WHUNwpW0Ga1OClgL0ze8csNhO7I_o5Sl_nJ7gA2eyPoLGJFJ2kbUiTgvq-opdWtnj3JGTSXglFgsB2e5To9_BaSR0ltu6VCz_3s9rnNkq2-hXc-3FjzP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=FpAzkLWMkdnqGvhcF6HNE_6bm1tZ2OV63KHQ47Tocc1fHqWthPuAi40-OGFoie2UUQ8ZqGnQm2iTGYAdtBwy-Jz54C3TGxKkOOhnVZ8P9hDK7pBQI6u9vAB6srHWRpjDtxXozyJOAAecG1kwMGX9HwYyo-w96_flbcfjBi25tao32P1rlqn0DDO2TpZRCDAd5fPLJ6BDFeVgEieRE1F-e-xRIn1WvJy_WHUNwpW0Ga1OClgL0ze8csNhO7I_o5Sl_nJ7gA2eyPoLGJFJ2kbUiTgvq-opdWtnj3JGTSXglFgsB2e5To9_BaSR0ltu6VCz_3s9rnNkq2-hXc-3FjzP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8g_wRmCMnFcAzJZrgCHzCl29GQc3Q626W7be1bCn_bgDf49WmE_vFelvoXnQgXWCuOH2nv-UpkHU6MvsXN_2EoL0-IDjKhYAN93nw19NVPYPubB5FsusUT1xlxA7ZhOyG6VJqGN-f1yzq4Z-xzYE3aO_J01qLaaD0o60N3rVPFVrqOZv4n0mridtQvOei5FfKOp9Ozx1UorFrSFfQ3ltil6I0j-d2D-mJ-qEG44T0kH1-hVG-RaO5XNJkJnu28R3K2bqKoiK3sgeBTBHoLZj3if9B_DihIpYTdX_RkK8g8pnu0ZDDy8qOeNUXZNnqmXZB6Hfm4IUz8_rMMr9isf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQSwCGtTQbZWsu6SX8XcXbsRNvEjXdgILFHhJck7bnO5LGt7rdv4evu8Pp-5ruziXivIyFg2JoAoId4P3nweVKxpSekJ_BN5hzkx5zbRqsPjzuURUXyXk9pV11AemLAUS6P9CjF8ynodH1KXjA1Y1_AOURuk65SUqV3SJL7jS_BXsHHj35_EiNLK4iHCtgJMbrVuAB1B5qMBLsiva5WAPyDRRIwMrxSz7U-rcHx17XgEIGLl36pp6X2W_H9_qAXgpdj2bgm944y9OMAiH3wbM4JsdTMWSnoupNIniG1igMbvsByRXF2xdqI-38oQOUoCRwJEzyJLJElLvk_QSVUc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=meWokwdiXz2qFLIG7c8FlVpLYRClaMfCdFpbPG7fOh4kfvvC5cJ88fUHkuUtJNGmiq_MESDLpyswEJ9yWV_j4rW-nhglRmmsNG4FWt5Ml5Ms9ksyfes69QsohHdqVNLeVo3-aaIoRuu8T9QrFUtwSSsRYx1dRKQA8MUiCwud2LG0sWV3w7_FW8li_Fwh2wC9J7soLg6lOWcOhUrZJ53L0U1viC7VJ1fqe3wLIckLnWvLBvHvyMCCr-oTdRNrH5DbleDdywIvMGcobNqMPNET_sfGSaTwhmjipMnlRDT7TiaYx8m_MoF_K8tlKQkvYhSzOZiqrs4tvrTz2zRWV01ylg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=meWokwdiXz2qFLIG7c8FlVpLYRClaMfCdFpbPG7fOh4kfvvC5cJ88fUHkuUtJNGmiq_MESDLpyswEJ9yWV_j4rW-nhglRmmsNG4FWt5Ml5Ms9ksyfes69QsohHdqVNLeVo3-aaIoRuu8T9QrFUtwSSsRYx1dRKQA8MUiCwud2LG0sWV3w7_FW8li_Fwh2wC9J7soLg6lOWcOhUrZJ53L0U1viC7VJ1fqe3wLIckLnWvLBvHvyMCCr-oTdRNrH5DbleDdywIvMGcobNqMPNET_sfGSaTwhmjipMnlRDT7TiaYx8m_MoF_K8tlKQkvYhSzOZiqrs4tvrTz2zRWV01ylg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqZmNnGL9Q4RoTv8-lo44zRd9do_zdBm1HRLmWldoo8lyU4bzCtsWYJv4x7vvrgO9yUXp1oyzFKx26YcNetTH_MLZ2MeTYniF0Fqdgvebwm5K_X3dmhh0PSgPIWD95p5WDISgTcxaQ1QYh0MVxvUiv_H6c_57xSD07XMCv8Zy_0eGJbq-OzIzTRDXFG4xfG1mzdPB-mwC8uyH9elRjjOufqXu9oiZJH7J-D-c8SYgw8OVdkmLfUjJWWWByUTsRQOdkxaBWq-EOn5-_yktkvDr-AmRb7iKfNSg8ZVCh3R67dJu56Ix2ERasnqv2IecBKzLTyXsmZ4zdEIhZf_drCS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=THCZO7CI19TXLC5mMNsp2d4uq1nO-Lys86QTiizaV-ioVi3oOTyaij7TVIPFqA8azToC4wAv0ixvARQVYald_Vo6ZPtL-rBOCOy8c4C5CnfcVdPQunOc7vIlo1y_AL8NtGMhz8x2J_PLtMLoQsMHcLI3ViC0UEbu2QaTijb_8bYwjaqo7wltc5sRbaXRl7tGnhLNzqjy-o7dthbiUArWMLVyZd8u8sHY3_1QtnppXqQyiyqItVXQhj4gsWdR6qNHenPfvEF1XKsvUNyPTniJp44esIsRobGwa_2Jt_3ixM6gcSr5YJ1VwZXQi3utkSFljtV97ZnzQL2I8vRP9hKhdZMZmt7M9LI2QKMtn7xZXEDNF7L6zDW_yGUF4mbn0Ry7YMsYU15pCu7PDkE5iqXUymYTU-J-yXsQhOL2b018xDHJQYMa44JO1HtUJ6V9Pwc4tEu3Wc_WbZcs2lz0ewjB7wLLxvh-e3cz18eeRKaHOLoUYQQ9pzCTWLt5Q3Bv4knQC5ebUbSIS-uYJnyn7CworVL68uNSEb2eNIlZG9JBgkHx_hUPTm-DSDgp3oPVcHBjhQG7ZioYDhM20GFBONDMlyU2IJTrHZ-fVVdFuF8wPGrmiLetqiznG_orfjU21tcwawujSehebTlM-dhMX2TGMQqdZUUR5xirRTpZQrpjwT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=THCZO7CI19TXLC5mMNsp2d4uq1nO-Lys86QTiizaV-ioVi3oOTyaij7TVIPFqA8azToC4wAv0ixvARQVYald_Vo6ZPtL-rBOCOy8c4C5CnfcVdPQunOc7vIlo1y_AL8NtGMhz8x2J_PLtMLoQsMHcLI3ViC0UEbu2QaTijb_8bYwjaqo7wltc5sRbaXRl7tGnhLNzqjy-o7dthbiUArWMLVyZd8u8sHY3_1QtnppXqQyiyqItVXQhj4gsWdR6qNHenPfvEF1XKsvUNyPTniJp44esIsRobGwa_2Jt_3ixM6gcSr5YJ1VwZXQi3utkSFljtV97ZnzQL2I8vRP9hKhdZMZmt7M9LI2QKMtn7xZXEDNF7L6zDW_yGUF4mbn0Ry7YMsYU15pCu7PDkE5iqXUymYTU-J-yXsQhOL2b018xDHJQYMa44JO1HtUJ6V9Pwc4tEu3Wc_WbZcs2lz0ewjB7wLLxvh-e3cz18eeRKaHOLoUYQQ9pzCTWLt5Q3Bv4knQC5ebUbSIS-uYJnyn7CworVL68uNSEb2eNIlZG9JBgkHx_hUPTm-DSDgp3oPVcHBjhQG7ZioYDhM20GFBONDMlyU2IJTrHZ-fVVdFuF8wPGrmiLetqiznG_orfjU21tcwawujSehebTlM-dhMX2TGMQqdZUUR5xirRTpZQrpjwT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvFqmiFRkN4SBjObpmA8uFih8f1LrEkkb-yOZYyzj-kqj-RkLrU6l7JFcOfD4u_daUC1srCcdRnfdxdCi7piKms731WAAotf5S5o9Z7EVsSyxCwFtrUb3YeqELV35T5W9TYegKZS2XJpHidfTF6IfLWyMoqpfzRhH7uoGIanwYGDanent6dQh1PwQwHlbN5xmDJmn9cQSLOBnJWDI6Obip0IGrJIrlWfccUkArQo7-JiWvnZEFwxoGB50WuU8s0OqV82uq30nsgO8JxpNH90xiFrB4n48IWe6XFL61vFwNkfv_DzCgbquClBa4ZV_t1k4I8dXxPxYFl3xjkRVR9b4GkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvFqmiFRkN4SBjObpmA8uFih8f1LrEkkb-yOZYyzj-kqj-RkLrU6l7JFcOfD4u_daUC1srCcdRnfdxdCi7piKms731WAAotf5S5o9Z7EVsSyxCwFtrUb3YeqELV35T5W9TYegKZS2XJpHidfTF6IfLWyMoqpfzRhH7uoGIanwYGDanent6dQh1PwQwHlbN5xmDJmn9cQSLOBnJWDI6Obip0IGrJIrlWfccUkArQo7-JiWvnZEFwxoGB50WuU8s0OqV82uq30nsgO8JxpNH90xiFrB4n48IWe6XFL61vFwNkfv_DzCgbquClBa4ZV_t1k4I8dXxPxYFl3xjkRVR9b4GkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-OGN90Oqq8bePH6RfAYs2no4ufdmxgokuOaInnw81M0sE_D32x32Cz4L3X8Sq9oNdCB6ZOYHEIUTmPItufvjN3Pcljo6QwsqtLKSrxWkOMbrngAFQoGp_hBRsQ5jepSPCj21NLGzR0Hj-Ii40fIqj76WNKmWvvrK5bRXVBRyR65fSCvF1v5XfZYxMYjSlJkSpVVodTjtbd294WaT7EaZQ7wqwK8Oy7kOcPgDERPrh8BdT1fpoNHbUJ3ViRNS6DgE13OA2VlkQASqyC-0yYrmeX6_inZOR_TP8pGnsJPoHVRMYLN_J_oVZIb0bW-f8-ZxPzRXS_dEC8kHoZxYUS2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=d-2j_HbgoAUX4LtqMDCFB5_vD_APHuYVINZFjsQ4Ik16HuiQudSTnGX6TCgPZUZqDgBaJaZuC_b-opKX0w7YaS22RyU9AmFgLXf9ypUy-XL2hPMe1QITbXVcPOUBdWoJiJYf7i7ohyU4-chXUwoYpbprAAOsslkaSd81UzbALRBXGLoZZZdTXjOmRqFbmsPrTJDNZZSuU5o8XV_9TbH159_b_VEwPEfOB2lEMCz4BYc4OIIYch4pt33zIP0j25QroUL3PTmQBf-bD_CWluVqplfHFNxR63zl6V5Dg5SGAgn97_I6vUPqnUfSpwydFdVubc3lbu9zj3YswIZWVTQJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=d-2j_HbgoAUX4LtqMDCFB5_vD_APHuYVINZFjsQ4Ik16HuiQudSTnGX6TCgPZUZqDgBaJaZuC_b-opKX0w7YaS22RyU9AmFgLXf9ypUy-XL2hPMe1QITbXVcPOUBdWoJiJYf7i7ohyU4-chXUwoYpbprAAOsslkaSd81UzbALRBXGLoZZZdTXjOmRqFbmsPrTJDNZZSuU5o8XV_9TbH159_b_VEwPEfOB2lEMCz4BYc4OIIYch4pt33zIP0j25QroUL3PTmQBf-bD_CWluVqplfHFNxR63zl6V5Dg5SGAgn97_I6vUPqnUfSpwydFdVubc3lbu9zj3YswIZWVTQJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFnTV4mlXps4kRRCoGlaAC8c6QPFFpdIWCmOEA1w2vAvk7bwTEDadCdQLx8isoCkCx6hKuVo0agZ778woHCQiiv_qKDW3tdGK5IQG196t7LYsXKtUtng5V5pa0bOQl_Re9RYqY6nrigaay8C9InKP26UDTtS4AtP00mmeJDpdEMLfqua7ASt1oxxyypDVeABWmA3XMH9MlPQYDAVhNizUM4RzLnXZk6w25CRypY1V_9I_X5uej7Q2btFH_hSDXYJ7C68OCFll-fOnb0asjpwY8_4bzfZLC9C4U5xwWVgjuYdGP5PlUppA4B3E5KwQLdkTleLfHmMBOTTwXvELlya4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQLOw-d0YlQ_qP5VmjVLRcx6vJ7xX2037Y10EltkKM2dR6Rr3rnkhd38_04judJ6-TXPU7wRz4PrdiNdo9qalIRRB3s0PN-US79cYKhgOFhX0mw6TFf29_EPdwZglB2wrazeZch6mjCjNsz3kOZqiSGuJNHfCDK8O8QPt-UD9bhkZMdVL9YSc6NpxSZHSDTj4VJT9oODThi4rRqYtKwOuo0ghIBJ77uC0CAmrJq8UoEgaQ212Dp8ONijZOlo5rxXw_kO_mQkNbXdzoKt4WE1y-uO8cByEQFsMcY1q7Ut5vxpjLbxBfrZwKUGH4Re2Adyu1QVBaE8wojKVHj2lhamYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDsI_JePaWpgJD5IVKHH3jQV8j9WDpqK9XpH07Zg909HBN2iDYTd7CxsMA4yJVoWGifgYyuqnoriJ4mfx7bBKaT0hrkJu4Axk_eKZlhsTEfeuS2EEOCtSjwiuX3P5VAjzYbCc0zUmyBm4nEEnR1pXdyjsSzh0An4MUwpVX33KpjnD5nWFre0aI6kWgPFkQYKcPGAY9DmMX-odXs5vgKZIgR4e4Tgb6n9CTxjlN7zs7Dxo5C0HsXjuoQJjNu1H6HyfzyfDQx5RzBupPKTL3YqOO26m23F3C2xoFRGOqTmciaCZSQfRObbvXhe9del-Zpu9wUWVsFTlkXXI-7Pg63P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=JxKUQMzrpKE-QkEsrH9VBdYZ6BdN0LGxdi-jOU57FPXbuivPKx8zo-AAaP9UO2uSAP860_R3M8JSzvoq00kCQBPwemd2J2A5LTwFQvz8M_iOUIx8uqB5ONpPaLwtM_FZAs73S6lzpkvSd17CQFe6R4N5gWTaIKCIuIGui3EFfMwsG3g0LdpchdtPb_WihIO_-PLlj_oWf6m3SZdbtYAGBUmWzvSnuORmKZhigmvqmqwiewiZahNzGyBU7S6eK8ZJOBWAoouDejex1bYYmjE1FrJJdhXWQaw-z4K3Eqy4F_n74_wF12-sVLnC7jdcr_luUIrMdMsACNXzyV8jye4nBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=JxKUQMzrpKE-QkEsrH9VBdYZ6BdN0LGxdi-jOU57FPXbuivPKx8zo-AAaP9UO2uSAP860_R3M8JSzvoq00kCQBPwemd2J2A5LTwFQvz8M_iOUIx8uqB5ONpPaLwtM_FZAs73S6lzpkvSd17CQFe6R4N5gWTaIKCIuIGui3EFfMwsG3g0LdpchdtPb_WihIO_-PLlj_oWf6m3SZdbtYAGBUmWzvSnuORmKZhigmvqmqwiewiZahNzGyBU7S6eK8ZJOBWAoouDejex1bYYmjE1FrJJdhXWQaw-z4K3Eqy4F_n74_wF12-sVLnC7jdcr_luUIrMdMsACNXzyV8jye4nBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuTwG5oQF48Vpm792NG5DSAUypdRKimZ-L0-y2O82UXHrwTavW-JE2SYEv5H6fUR9Ih2z4bm7C0MxKbQc2fHKuincMp-N_nyZFB8IEYeiX5tUuNkY85511KpOJnQNA1JAqzV58wsalble2QEOZXeSk4Sss9hzAb0rDLzP4CQcKF2WG9hSpAi34itYMs0ld0DgfkeaMGIc5O_-kMYSgZ3U8Jc5Th_-iBKN3E0w2zBTlSMZP9x1-IPdPCU5B-lSr-skUzT7h1FRTdhbO6dzBxupsFRM99VRs1r_4igVJFlmjNe0Imb88lSdbGIIVOvdcHdY9EarfA0DJ6sLd7LrSwK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce9X5M8dJMxAc-ZTbVqV9CSd43Gz19y8BHKchC80OT9dvpFUkZQtPAyFktDu3OqtNpkd4gUuDRiuZ-UoOZwTIE0cxCwH0gj_Xn2ns7bXgLU230pA7WEZ-8WW45FHXcZ1iqkmpDJXETPgCeEJdlpGtRRNUxxWQLMC5QbaHe8PbfIYzH1ncufTs6Nynm3w0DFJzKGSvik-k34XT8TJ57m2T6OS_XY6XvGONlqQUwZYd81Mc_5tmhxkyBJJ7KgAH25g5g_rykI5fgHVZZqvRzFjprEpsGan-AcLFzb5FLAET_ZEOjP-V73cSq9-UAe5K57J4QqC7F9itVdYQb3Cym7HgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjUtyWUPndqL0FvTHRwkRvIMnOBfgxmbUtlOw_P8K6PEhfRb8xa2WbgyJr58YEIXbLufIj1dz-85Q03ex1jZYf4nGivB8-Bah8JZmjd0QT7tSPNBVYVpO2Vf6rmIqixXryDvGnqIF1zk6X_g-54xNQ0uHTlkDht_uA3g6tpYcXmdkQu6ow904llEQi4CYwzncZJuz_Jb51WHSOGHbkciUj6DST43nvHnTglDjqAZXARmT8j-ApnQl_QHO-_gzEZNy65Hm7LozC4rKYn8iQ0iuFXzIeYuoRrOEkKDfDLc1C6GBD7w6vIjXgUWRmRRfjNVwoimkWxXg2zE_f0sZkEYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5V4Pt96WP4lHG08Lh5U5KjoGw3xjaT3mgBT1PekwBh7VunKAmpDh1xV0zLM5RPidQLe1XFHq_uQAM-BushrZBslteGL30k-EVIDr4hkBCw_uwBuUcCG8wGmzhCwWF29EvcVZagZk4k1mMwm2yy6zjLvnbKKL3Lm_8c20STYZfJiI5DWzWRhAAs8xpBFL4ySTDtM0sBMccZw3_dwJWeR38gz_fqlUt6Jy2263hdup0105adFi4gkSEZFX6xD7FkY5vmBuu9Jag4S62M_H-AxcKPQDFb-BObFjFVqnNSkE4ZzlNdndLIIH0koru41vZVgYmmCag4N03Os1zgPjQYR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uORGdIfLrZO7pYFvzdXxdAqHT2qw214OAaGYy7h863LzjWrWdXTPk05-aBlCqH3923mdGKej1VsKKta3YBuj8M0svEjIz1gZvUXTm-J0c960ggTXufYHNnOKmrNMsW6amy78GnlV76lNT39ymvC2mcoZ0XKF5ZIv8h4lDM6QlhM74ZzCBFGKPEyZwIIG7w_R6Xy_f8K_xtPsjWPsRoIaHQlhjkZFjD7oH5IkCGUzmUKIMSyoxeolX6Ou5JkJW7rudFHf1XYUIHj6DDQvaUXTdohXdgvcm-Vrwt5M2SScaFnV9TuOSMCtw639YMb6wb-iTflTMFgBCkI1jZOxD0C2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROcsnYtAR8DiIQ47RK6lKy9p3TV7fBBBDZ1GQ3XXY38QP4HIncA8ezTLHJVTB7zCelpavKJmPmBI5WdUL586CES6cgcSRP2kQzF9Q1pB3jK2BXkvSiqabEHkM2_lEA753D1DV65wt3jLKf0f6Rb-0Ca9sooEiEuYTAx4ttEbiaENzLTIU1nPk_4pWAvPCQZWdwKBmr9hOtGY8J8RPHNfOaK2eZ1FoREumvxn-h2BMB1w4QhSpltF5Guttzmyt9fg1rca1SG2dnGaLm82s7IuGJfwTvT0FUhuV4jL4Hw09XfSmPMrnG60NcY1FK8ttfQVG7PjNNrKoZe0eBRak21dfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOnee4XkcD9P5yaZsycCq5Ecg1deiphb0cPMVOeszw6e-ttRFBAG1iisZC8SHO00u9I9o1fzmTvag3Qd5c2GqzULVYgjXvsSRD1_BefAn89jHxyGYCyYh7xzemgFTMjvG1k6O3zTaHj7zZXj69SwcW7VC4PXwffMubPUu3zZPM95QyhKKuDA7TMX1b_qY6SuuEe6VqmSKS8DT2VGgkwA1ZZR-xOubVXZWHDTZ5fInMcbI5arGM9HK9uGBqx6HkCrFUSKdZmT4yIco7pSzUgjYrIHevtyRFhz6UUali0U_TJLKwJkRnjYFrS3vfCfEp9uRtKnmXhGMw6h0mijtFoOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvVfkMzWGSXlUSqHmA0Umjqtu-nT3jJD-zIZqZdZbNrgn0sD-ybKPhY3XmOHaNGaw8uTOglGNlJthTUmk_XwlRvdN712od7d86m2xMW28XeTqMJ9rpL36m7kTAR68LvWCJET4etj_6ZYNw4PF3zqBj6tzmJ4D_HcvQzBxCJmFnK-YyyR131Y89mhig430WAXDIw0kWzWv5HY3CaLBIozSdTqrl6CHz7Fja96T0XFUbBLLlKYi7UDvvGl4eFDJGfyYdGFo2v5EzM0ttA5YnRlvdjJscaUcPbgrh-yDVTGt4CjJLGMNq1K5rg0zmUHn4Nty0g_IwP4DDAqG2lmIRW4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZzx29ffjhzd0cOSY2OAwzIOx9KNKOJqISRri6oIvbytOEoxZQ2KH5K7jjnKs-cndcfaBPujWInmRLWLF6Xa5nVaRA0vWWTWSYYX1isR2MgJm1kJ_AO-0PErSVTUf4d0r8gOxtHobaoaEXq4__4ui1n5Ml-SX-_6euHbN29stHHbYctPYsd6OaRm0GNKQ87KE3luljLBrAobEsvWF4f_qvY8LG9qE16Ku_r9UV6DJbzTk-NnTDrjO6re0HCTl27vNPjHZ52bQEnsj2q7i7lJ9YuX4ud8PVcdZYm5lftxKcJCzQlBH9AmTgExCLNLKsCeZknSoP4mwUYBT3gOcaTRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=d922cpDBmSpQg9-FhERJyuKZhGc9dVU5tSjXO2P8G4RetcIbMYKGc_Vxyd5UFQqhBXqiQOpclURIERu6Bf_JwPO8igJWHoYRTrf2qEo_QSpG1Cyg7Lj_GmmlAnh8q_DPcK69NaWYZLKvFJKfxo0uDchDEejW29CfDX-doo1v_oFfGGFC_QhtW_vOyjcrOS6Bb1arhtfh0EzhkiknasCHvjzLtjANUdY7pQiMVS8h97sgmi81RipRZNlPOHM2GVwJWR9qJkKwbJl7tVcRo9oSK9r49PWExwOrDMfeHnyLnd2wmC58h_0hBTwObFrWzz5Wz1GGKgOxtLeGu8LmeTDNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=d922cpDBmSpQg9-FhERJyuKZhGc9dVU5tSjXO2P8G4RetcIbMYKGc_Vxyd5UFQqhBXqiQOpclURIERu6Bf_JwPO8igJWHoYRTrf2qEo_QSpG1Cyg7Lj_GmmlAnh8q_DPcK69NaWYZLKvFJKfxo0uDchDEejW29CfDX-doo1v_oFfGGFC_QhtW_vOyjcrOS6Bb1arhtfh0EzhkiknasCHvjzLtjANUdY7pQiMVS8h97sgmi81RipRZNlPOHM2GVwJWR9qJkKwbJl7tVcRo9oSK9r49PWExwOrDMfeHnyLnd2wmC58h_0hBTwObFrWzz5Wz1GGKgOxtLeGu8LmeTDNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHC0itzgIzJbQrwNi5M4rNJ5wQUYtQTaKzRt8Q8nt8ddS0GDgiii25OKaqDzF7LOjWePfjdAiY8g7WUC8oDV_Py-YUHy-4QXFUlaVMvzFC4rcL2dHUPJJyrWNUPH9Or3JNTautda3qqJicZ3q9-8AzID_907zQrwOMIB-VUt3FUHWtNT31FQnfhM4aRgg8tQ-XLF3AS7Jeue4SWuPcyosR544Ug87mMHzKaN52Pn4SKubF18xKABxZQxflwy0m8WxoCHArgiZvIuTwc1TnpQ-p33Ei6DhcHJ0hF3KKP5kZosuKGoPOE1e1A6NFqqROOG5UAVVWkbEtv8gkbCd6mjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=cXnqQi-nFrUPPPj9wQ1GhFkv_hyA3U8y-9QskTgegzENABNGe6nmcTHUETzkuanjNJMoLfUsClmv4O7n9OsaEdeUh8zRcUpO1DEcrmSSQe64l9LyI19AdlilmOK5ImSPW9ajM-hzML2SmO94ktwt0YvrAIq1my1H11tMBRDkbzI31UNU1IMov2uIGwLy8aKIJC73dQoiyx66_P7-3NlmHiBBKgSmOv1HlK-KE6ObFBEsO7HxzihYDgGzKBQXYC9Bb-GxowDSMYriddpvuFwQ1kzmIaSSSoLI9AsAEbxC9B389NM-ko4p-VC2vg-yxcIoRj-HdJy1lbiRW-NTMm_VBh2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=cXnqQi-nFrUPPPj9wQ1GhFkv_hyA3U8y-9QskTgegzENABNGe6nmcTHUETzkuanjNJMoLfUsClmv4O7n9OsaEdeUh8zRcUpO1DEcrmSSQe64l9LyI19AdlilmOK5ImSPW9ajM-hzML2SmO94ktwt0YvrAIq1my1H11tMBRDkbzI31UNU1IMov2uIGwLy8aKIJC73dQoiyx66_P7-3NlmHiBBKgSmOv1HlK-KE6ObFBEsO7HxzihYDgGzKBQXYC9Bb-GxowDSMYriddpvuFwQ1kzmIaSSSoLI9AsAEbxC9B389NM-ko4p-VC2vg-yxcIoRj-HdJy1lbiRW-NTMm_VBh2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=gDJLNvIZM5P5lX83fhV3JSXnh_0p2rBk6IIHxpJkxicUb2aa21GFxi924xtIPHTpJ1mlRzMBMh6OLI-Va_xAvANKhlIlni2GYMTTEAPmtHMHZ2AUByhf2NY-2JoXoXhObxZUncA4SEBEivAZd1OL7trHK97_TK82KnmEaNUiugAmZpnLSTXlJPenjRo2rw7FAJHcx_lrUsl7A1ZsCKYTP48NGHRHW4Eo6uUf-OwvAp_oCPGBbgkpoixM4ckG4fKh91scYB2IwuXTsNvfwck8HkWIot_vxcM-bJsJkn2s0Z5K9wvuIjQrSUToe-bF-RHxGUv6C8eh5kkuyKnNy4XjrpR9sEZaH-WBesvwogBSaPdbDwVodSsUn3awZBcW92eLU6nmfG_wTtf9BG1DTnEIGHoD8hHVwgEphdirar2i4up75MrvJ5KFWX2WEAbeKwayflC9W8mqECo2PRiw3IjEt6O9KsbVhhctqLcD1fS68XcrMnLguOQWa8kCo-gQIpcAUCRXzFcW5VCxxCC-EGvlqKdfv2Zby9Y9gl4g5dUe48qGLeY311u4qc_JVu5YR3JaBE4MYSWrdKuFmz-mEMQRINrtqqP2FLrQSkMkkJsfq9-XAzo1b6L05pfA10b2bZnJzseQEPRhK6jldhZ7NpnpyC363eAYnD1rKubQFiMbANs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=gDJLNvIZM5P5lX83fhV3JSXnh_0p2rBk6IIHxpJkxicUb2aa21GFxi924xtIPHTpJ1mlRzMBMh6OLI-Va_xAvANKhlIlni2GYMTTEAPmtHMHZ2AUByhf2NY-2JoXoXhObxZUncA4SEBEivAZd1OL7trHK97_TK82KnmEaNUiugAmZpnLSTXlJPenjRo2rw7FAJHcx_lrUsl7A1ZsCKYTP48NGHRHW4Eo6uUf-OwvAp_oCPGBbgkpoixM4ckG4fKh91scYB2IwuXTsNvfwck8HkWIot_vxcM-bJsJkn2s0Z5K9wvuIjQrSUToe-bF-RHxGUv6C8eh5kkuyKnNy4XjrpR9sEZaH-WBesvwogBSaPdbDwVodSsUn3awZBcW92eLU6nmfG_wTtf9BG1DTnEIGHoD8hHVwgEphdirar2i4up75MrvJ5KFWX2WEAbeKwayflC9W8mqECo2PRiw3IjEt6O9KsbVhhctqLcD1fS68XcrMnLguOQWa8kCo-gQIpcAUCRXzFcW5VCxxCC-EGvlqKdfv2Zby9Y9gl4g5dUe48qGLeY311u4qc_JVu5YR3JaBE4MYSWrdKuFmz-mEMQRINrtqqP2FLrQSkMkkJsfq9-XAzo1b6L05pfA10b2bZnJzseQEPRhK6jldhZ7NpnpyC363eAYnD1rKubQFiMbANs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=bdEhqo0ux_JvaPWdSslDbWUMdK3fGUKytkUBqRscZQCNPwmJCdiQPHcJgCQqqWLpBkvxTEyOPBIjm5qrZh7iCD0JJGGYbVuUazxsk0HB7Ej40ghKWjef9vPWK3YpZJT3zrXXmLhXPTGE9zZ8YVd9CsKamONz8w2qSRxbVC78LrWnvU9DGhzfVkzt91qA8b_J0nn50uMjd9Ih4kxQhpTUlQzhOuJl28ZPBK9zt2csWMbuwQgfPO5s4eShMXPZwlZA_odmc7z7zPJib6ZTGh1y2srBiHq9p0OCMt5-rwmE74QU55lKIp_MSjSKwKBC868YXfwfcRwszk6MStIRa8QYrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=bdEhqo0ux_JvaPWdSslDbWUMdK3fGUKytkUBqRscZQCNPwmJCdiQPHcJgCQqqWLpBkvxTEyOPBIjm5qrZh7iCD0JJGGYbVuUazxsk0HB7Ej40ghKWjef9vPWK3YpZJT3zrXXmLhXPTGE9zZ8YVd9CsKamONz8w2qSRxbVC78LrWnvU9DGhzfVkzt91qA8b_J0nn50uMjd9Ih4kxQhpTUlQzhOuJl28ZPBK9zt2csWMbuwQgfPO5s4eShMXPZwlZA_odmc7z7zPJib6ZTGh1y2srBiHq9p0OCMt5-rwmE74QU55lKIp_MSjSKwKBC868YXfwfcRwszk6MStIRa8QYrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0DeMkdnlddZG_ri9uerczpubi4D62GjVFIYZp-4DCYPQ4sS_luo8KSmaeO0ByBMqBP8insJym3_iJXnlBPH0AV-qmFHjjJ7jwDN5Hy51HZHY91zvPnY5FWBNWAAMHI3_2lKgb4SLIFEDEr72ArU1uQBkPAKD0KxCcUwt5PV7XSgVjPFougrO83YLi4ejaJpTsBLhbXcHYhqvFp_npOif2N38L32HjF45R-tp_uE4w1osli0GnaVs8Tcuqj1RvW03oiU60GxLkIWojfI2-vHnc9RXBXya6ibqBGmKBMWFGERe2dttg6FjL_IzhXmw8B46SA7Gyvp1WNa4rN-18sV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaHFOHamjSjybavbljFxD8xilcVPa2Q91--3iKup1zmjaBuPrpiiRQejOejG578_Lb7maAcI07LiCJme8tWnv2kRigU5PmC0lwpllBSV_Llc5Htmf2KIPBJIjQFs3_hT0SD4fQwi_BtPMzQRRv1bmnpsuhWSBdvFfs4Ii7pUgqPdiHRtJYE35doUURNGYg8nf908_geWrJ9x7sQVkejPFm-vqsMmkbcn3kaIbMkf_iiUNUNAf0lkwQ6DcdKTkPW8TdRqqRiimOVRdesK53S-J9gcdU8D6zp-OkGqUC_zeX8sCkSHcdUu68RZ2ULl5DF7BRmPC398zXqsBiuatiPnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuVzoe913YG24SPJiVGy3gE-yIbaGXWDBnkU20gP499xRyQNxPNoTTd9MaYt6eA2gZoFYot5wz90zKb-ibruiS3GWtvWiBTv5LJpDdPEoKEqJBLFX3kkkE5jh_4ein6ggnaxR0NJQbPR8Of4uWPwdC-e66fr41Izzl93YtrK7wUTRa3S6XTUdJHqQo2sQb0q-otFUamjrKoVJHGsRce2_PnkUOPIV7KRZsF0nwlGNVQTVfFo1xG_VyF4rGOwuJdiP8f3k7gFOLv8x9YxQbMRMYN2qI5ZLlXPiPvM2uz-EjJEWCxDDwtpe55zxrEfNUUbBh_r9Go8Laben77xLeLptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnkPGb2WCv96uR-LK1i1-MxAgIYuFQcpsZg6S0inWO7OOxsYC7U4mwM6jCrkHmWDnv0GBgsyMC9HdGV_sUOa26k3-nlp4Eg2M9X1s1t11Le86UIheZ6yVSlcUv_d5kKH-zUjv6tSZrDDZXPET1HpzHv8NjArhFxKPxVyedfuExba2FgQFO-ca6IbKzT-ZvCDo_CsXrJk8Abv7dHQ4Xnd3CSPKEy2hBs6cNVzj1016HD_DXocWrVIMFwD8JNW-cU_kps195l5tA4nwzTr11rtkRYbj5N6NpfaIkjC_qAWFA4lHT6dI-4DmLS8uxPJswoativXpyRjRtKbB-cX1Xt6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYYPH99AUQUZr9BEuFpN-BX4Ltefl6lZAHBCJnMv2BWD2LhNuVwkJywFXd8-i9oxcwnOrfI8iVtTByYXxhjN9h7OlvYg92EBK5WJKmxoJE53C1Akkh39c8amoaNIh_m_-TrVl6EdjskEFHkI8mgagd3FA5Jb-eiUKaGZ4gK92g5ruLw3ebXHY9TZi_yHbzA6Pt7tqZ9b6i1CafXktl7VQNKtHZEtYOiTGViWpQn_xI_bJyuUY2m3GzCtbMQIM2GVDFglbU8YE7EYa-Vw5Ppxcx8JanBLnPc-3gUqcUrWCLgxY_iLbU9bJBJy1Ia2yMTuKSuaS-svdHElBGuskCBmtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9Sy6ZXO-Ma0-F1edxg3XNqQ3N1pBdonla7BZDxnlipltiZqFK3MdMDCRcPRvr7qnaW2kJ0iV1hBllydTdl831bOXqrz2f8bO_n1xpJ-0SvUmkP3jaLe5scfSQqhwmmJIQJEb6E1tSqYq2QCsXCgWKJz_YZ2KzDUldnyyjNV1soDUJFjfzVUbPQ5KPuF3Pl9WnhaHfVqDUHXME0yQKn7FFMnK8UdSvirZhzZlV8d0sjG6kZk_W_QOg4nCeTxsIxXZEgiZAlk8xoqs2DqqZRnEQQOXzD3NNB7gpxCgMjw5NhfZbFoUQReMCh9YKcDws-lUbRoNSe_ZkCcJ_wKjZsOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=d9S6dHEm0NuNz2yw0k9nraoMstk7s_GGkSilSz_7JAMgvPKpj7uad641n1mzqjnKmuaE2nbEkumw7pf9uvcpCDa_MX8qEM-A9pfJLQ-YKkE8sfu79OsvROL6ql4fDEpx9Kb7XZCaFt5dGyhO_tcMCHLwKJSVcIsmuzBe5T5FWgAGyXKo9po8BqaoMLbHx2VUQ4e2DmlHkDiHhFd1K5n0lC5izdpFwtPnQkh1ZH-p-sUbi0DHwIQfoDgN27ITL9uYyo94NOtWFhlIJVstu3uZCAIo_l6SAaZmH4nZ6BLzXzf8a6t-J9V3vsPXN-hnX_gYg1iMc0x4e4teBDsty_lZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=d9S6dHEm0NuNz2yw0k9nraoMstk7s_GGkSilSz_7JAMgvPKpj7uad641n1mzqjnKmuaE2nbEkumw7pf9uvcpCDa_MX8qEM-A9pfJLQ-YKkE8sfu79OsvROL6ql4fDEpx9Kb7XZCaFt5dGyhO_tcMCHLwKJSVcIsmuzBe5T5FWgAGyXKo9po8BqaoMLbHx2VUQ4e2DmlHkDiHhFd1K5n0lC5izdpFwtPnQkh1ZH-p-sUbi0DHwIQfoDgN27ITL9uYyo94NOtWFhlIJVstu3uZCAIo_l6SAaZmH4nZ6BLzXzf8a6t-J9V3vsPXN-hnX_gYg1iMc0x4e4teBDsty_lZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlLlEfGLJBDo-le9mW1AORiJUAP64t6q-PtmGsAFTnYr2nNidodK_YxN2UY7Of2E6MXztqNqDSYSUb9z7XXcfXrWv5K-WMnSqn8Mdo26rrKeCMEmRKy4hx3NofHAxaKWSuOzhXMzJl-KpnLuF0xhdzLGNXxA8Gqq0lTkezRiFJy-NmTy1vytSpUAPZNEi37r3zahAt9HWJppbCI4upV6fWweihZ0y8YXWw3ISynZEfwrOFWXM0IWBmL9sAk0ZWzUekkKpM-djrE7xbcMp6itPjOVmF-MNIslfCIgltrcIg0iETaXUnVd93iaKHayy3i9hst1f6V3Mg5H9-gPIxQSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXhP7ifZfIjfvh5EdkG5O5IJufaHifG4BnQvXs8EBcKS1LUmy5ncWTO0LGt8gMm-xthfXZGicfC_VHW2FjtkjIFrizVsUi_Lv-vFbvCN0UPN17dUxQRsOCns9KLAUByoCVbnfWc1M8toGoUsgUhIwBFe75kIGVDOuyIh8XhUeKPUygq8hTW5XiZkrUWiEnSx_nUTaqk86x9jsTx8sJlGzVRVEQfU9KGXXk6z7azLD5sdr0O9ctC3I-B7rfxFHvGd59Tcs_FnLl8WOJ5yeQMgITCNr47EWrMrNMS9Y4Pbaquc_ECSYlNCMWn7WurZRbZw70kmyUJgQTWA-jSz-JT5UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVDGEdyIUp7Qp19VjlhzYK8yVRAQxqrbMsRkKiORF-_LEVhJFkrarVoQE5TsbK_LUjyPvmH3Cf2EQ_gzUi9j6_IHivQfa5ez5SzPQwuhKBG4w97ex1KqoXRZtUnXpMN5ImYkPY6NOj1-ne8VQs-r5Rh4E77wQ2OGZJBWsSBKAFuc737n1Jl6u1yQvHMeDLkk3W1TPLlGMju5LEeeDqJDvfQroPm5brVmKwkPqFsFEPxb-TlRWCdal0vO7PpIydJG3TBZ99VJNprfqds4qEUCCMbordgnziN2iiznBkRz6oMQ596Toyt1YQCJywJPJol3zixO5PtIsRKEyFNZv2uksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noWaj7sFcRugNkVTGj0Wwrapee5DgIlxVd6L6CgQbaywmPgICNyPc7f9WhSxY4lVjYrdUbRfnIa1WlGUv5cb4JslUo89O60fHTYzzZBMNlnh56IQ-wSoTvUc1gzj4MhqW-vOWyllEm2HWYNS-gC_zV1YDhYdbQA35RQ3_8LfshUe87ZVrIk1_K76g3hwBuIHHACOM9m5pizB6bR0ZCE-CbPsEQWJpDsrhHtX4GK-61BSp28nva4gANgwu-TFzKYq1Cr_b04kCLASluNLERsWj9_olQd79N1sMtafpq32Ccxqg_63PhcGNJ6ZcwxKzMjKiZEQ0CpR4QW1sc0f2oR-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVrl1a_F-4soa9ROhygZtdwG-HhZLM5HeWKkfrP0MXv6aYKMuH2A_BXy1vGY5PETwkVPHUGvwkIUT_hpePvrB7bwXF_ysrhbDO11h6jkLUj7ZOIEPcE9wxcJNvI5vtd5YZh5aIPh2EQV3aNIYhvTmfaF663DwWynMQXKAf611nIGVDlK8vQpSMAHD58CQfBu_itST8X5ysaLFzG97CFDPFIpx7tgJgt4mdqPF4Pp59AyFA6UqNTxw_WLBPCdOE82sdJgQDO9_H4rfG2XwODBr5PhcT7BvqYCZ-ahf7S2K8n6DQy_vI6EdcLfMsbLOTj-YoEU2IsdNxnAWS-3jlCHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hag04fWoQfliqD1JXkrjpmOHU8AHUMMlqXeVILZp24Ey13p60HTRpt-zuYATMaKCwZ53K22JE2ZXWRXHxbcn0RZFlNFUCHR_6Q6MiReBosTITkKzWgyxN8TZGFSK1xzWYFLvIvh62re1XTyphqgGGmU6Bntmpow76uyB39EV7EFo5cul5gfAygrmGWXfBZNRbtACEXLgFkou9xbKJiwmBr8FC7QKrm7rQh92u5IAFbq-XGLd0B2r8ruJpndvjxg15HhK2jrbHUsdc9Bt_JCbt0YgcG-ybJznC9EvKK0SQXw7DArj1ltX4NMwtVu-PwMhPXQtsyy02ysFFHbzpFfDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=Ge3fEk_UhD8FBAYIyrAN9FlFD8eddCVMuJsBoDPb_YXK_P_jNe-3ATtc9YcDHmSGE7tlKBttXbxlWZo1FiyyEBUlq1rLQzNz83qFvlGHJkEC1xytZQKx0Gx7aKCav9aWbyUS5116uTa6dkMkiw1i5Y3w0uh3qpF6DctB0SLZ-CYrxWYOH9oA2S6vbvJWcwCjKBWmI1HygrGR5ND4bSuTPHyFGFoQ9_ZgWWlkhCFTnOCTiSs_SBWNNgHQwnOP3UE9NfwY8GiXC776BUmnN5nI2-UHhbLi--BM8uVWIu12SYBvDRWjuKwUtl-cuV6zwUFrlpz3Z1Ax62ZqrTiwI7NelDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=Ge3fEk_UhD8FBAYIyrAN9FlFD8eddCVMuJsBoDPb_YXK_P_jNe-3ATtc9YcDHmSGE7tlKBttXbxlWZo1FiyyEBUlq1rLQzNz83qFvlGHJkEC1xytZQKx0Gx7aKCav9aWbyUS5116uTa6dkMkiw1i5Y3w0uh3qpF6DctB0SLZ-CYrxWYOH9oA2S6vbvJWcwCjKBWmI1HygrGR5ND4bSuTPHyFGFoQ9_ZgWWlkhCFTnOCTiSs_SBWNNgHQwnOP3UE9NfwY8GiXC776BUmnN5nI2-UHhbLi--BM8uVWIu12SYBvDRWjuKwUtl-cuV6zwUFrlpz3Z1Ax62ZqrTiwI7NelDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvNUFfRgvZrEAzrE2IpoSH9Gw-AewVfP61uHXWOdFm_4U0c0cOGAVDh4x5kdB1ucD-vb9KeFPA9Q_9m7CHELaFw2iVvVrAKy22eyVUNFMVZ7KR-Q0y64_He9IX1pfjeZb9YLbiq6MxM1z9U1COV-o4OVYRDmDxv6fGl4ONdFIdFiCt28QQq7-HtpNxEDAHVDCEdri9VlOza_Nd4IqcdDmUsh7ew_vIRTOo1difDIAasgiUgIWrLHxjwSPmwa9aobOptu1rpOJ8-bA9pQ1tNfg-nusVDismvrVwzHMocJHBmGIaQM8BOwWqhFRMxGlyDYb2OxyIjvURT7A-VYL2fTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAE4Mo8YBsCBFMqNUi2OgsgSnscE_UuMetu1o-P4EbmQGEcMekkC356sY35iIcOIFioheBVAKrxpF4eVLKeAnxWTB1VX-c04d2uJF65KsULDmHD8HjaCge9esmOhPsHZnaN8XF1CHNndqCWPd8nsNcQ7Jo2phOU5EcIpZHa3s2n1xH7_4hFJ3Vx3ksayJrYocR7RLB7SjikYThrwobokbvFivAlTqX6ACnAyRhDgfYWZuYbYU5Tthfy6n8ZtRerV_kIjS1D96bA3FgK2A81p7LsrvMf9_zkhcUnJekHV_apokqzZ-R7C6kiQUil1923uwsGrOBZpPwGq8Z0Q5pyvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=pRCfboRXqTH9LbJcVDibNl7Zz6R9AMYmmR4nMpyTf6xhdriJe_szOUghO5hTbEivRYwyzrgcC0e_wq4uRUoa7pK7JtnYjrCCpqEd7-YwBIsSN5wFN_sKSNDEdb54lV8C9jGWSvbHCg8FivMqndh2DO-LmL9IW4h6ajs4wVla-iLJF41Okmoq2Il2IxOOr6Ep3-critcK5GSv0S4wX1RoNZjqSPvmsj36p1Gc9HQXdu59t2OgflR-UNBUmb8fR0iXP5vicmuO3B_Q9fHM6tcKk7D0cwIWaqjdj5baqvu_yWmezjNMt1F-iPoNC0jbrwZgkPoNMhI5aa3kX6e5DvfpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=pRCfboRXqTH9LbJcVDibNl7Zz6R9AMYmmR4nMpyTf6xhdriJe_szOUghO5hTbEivRYwyzrgcC0e_wq4uRUoa7pK7JtnYjrCCpqEd7-YwBIsSN5wFN_sKSNDEdb54lV8C9jGWSvbHCg8FivMqndh2DO-LmL9IW4h6ajs4wVla-iLJF41Okmoq2Il2IxOOr6Ep3-critcK5GSv0S4wX1RoNZjqSPvmsj36p1Gc9HQXdu59t2OgflR-UNBUmb8fR0iXP5vicmuO3B_Q9fHM6tcKk7D0cwIWaqjdj5baqvu_yWmezjNMt1F-iPoNC0jbrwZgkPoNMhI5aa3kX6e5DvfpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvjAiHUB1Ng168GB3XXgzLMTCfSZmjLEw1qcExRgPJFNDAhoazFYZTy-iKDEanbdePcIg6q0__eJBN576Yr7v11MAtEsh8hZ7SaLOtzq1zXE_y0W4hSc2JbXbHF9647mhyLYEMKAO0281FDhYDuh0FFd66uQD3CGByWdpFI9SbAtKRIIPkYHtgaKi_Hk3K9yZOB-RFdCUMwfDVvJ_NSwYtP06d3YVxfX5jwFWdmOJxiAwLv0av1qJRX5reiFsLfPmxdccbMKn-BCFPLEQnVbBo8puB3i2bq53oD29pnV2hCQklY93uAhV8aCe5R1nrUOoP5-bpIeXiPLn3VyrNg-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzN0meLyqN4GdS250RQ8svZj9Xh_PBWGlfQRgOJkiQTxQVItcnz_mz2y7s7R2IA5DCne0E4KcoHhscy8B4p6gb-UulbXTk3Ix92mfHnPsDdzTpcSk8YdmMPqcDrr63--0Z87Kg7r6k2qcE-9Uoqf5qagD0tJXSEfRxhVVqmZm_dwX29Cy_WFLrr9MFTN1TgcRSaxObXiw5Op7Wc7njcG6Njrv1MVg4taRe67GZHJuAU2S7TFOV8swX7_WgdGdgMs5AGKPWSWO6HHlA3rDbfUy2A6JR6LmoLXAsowL-yiryKxwPYfrXWFQYNMiWTjqcXaBJTTxwWv5AAbJEVrC8DupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODMCThfi8cqBZwbFn7CxJs3WBzuiyEaKO0RJ6Ht4zBfal_-s-9VCB_PNW5uBvWaRM8ghaoRxahhcsA9pbx0h-mBU45l6E4pcAdGWwgvUWoC8M9_bBQE_l3I06_9s5-ggKKh8B-Cqx7HnBs0VeL7oeag7BYe68OggXYp_6HPN2L7oiUFGvgGaKq8QU1urD2vXXQwGf251qC4doD9GdlpyVG4Q_rdiwEXnWplkrSiZZ_mOBGa5lFsD3KJuB657fT476vWNOD1WEWFkv7LmZusn6BtTv2nhzwVIE8HvOk8AICThHKXw_aRAY6jfvDsHF2d21ntNmXOzy-P5jimXuD-pyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgLcyXX3ERgbi7IXmbq5TjVU2ohxXze3oJaIhlfixKR-yLDFDSsAbRknsAZEmDud16aqccTZUgaPTBv9wL2MwHbW0f7QCf-As3Wazz0X84xkNnuUwmqrfkCtmF0syoSsTosdVgjNAjCVPQDZWx2fSZEQYsH5PZlGe_wMu-8SfW_Fvsm_AldZF7jopWV3jufZWsgTjcq3lA97oxAW4l2X5db0ye8MJCyKDk9FFUHxdP1dI2TNxmjibjc3y5NRq-phKyWWVVl0qMgPna16RqJJjMFnUPxXRBbvIst_qxz8JouOA_xKgRP-hM6H47vE-Gu_QtyGNyG198W_r_zSDg93-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyJv7lcY1SybYHbP9HzA_nAc55I8mXSx-Q_S9CD36uMuwY1tm_ZK6tJ5N69hbOwm4YVS5KAdXnJJ2Bx6yKSJ_yEiJMMWBmM0aqj5c3amYLds4NKAEfYYhX7SRA5g2XwdTgT9eqF5524OnlThKOj-R0k2WrLLQPPzFMYqhdIVVNPynECYvFgXkhRi37Jw7vNsdjAgYpGKBy7yFzI4rVv5vdS_HtzL_LIB9s_EDYZKjiiP3oc5ZzpOVVtuwtsu0JNKatkE27ADVDM6K8Y2tqeB1IlbmS8iuxNeuzHPwntHo4x5fGikeWdihEGQ4xDaPSQlNb_2nN_sbKverk0IZcE9yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmQwaJBwMBaWmUu2pS8FUD27zEtCH4ra8SGbFhCo9phxGcBlc4jwzESDvtY7WDD91Ci6ulkXuLx8kQehh0MK2hCnFA-ketuorRrOjMA8ll-IPGHpOBy8fsYvMjzdL7UeUpQrm4fo6Ewmt2PtSgGk22yUzzifVspX-bdQrhCvuC76R3Sw8S67GG1hHO5qOGLA29sQ7qEmvXydmhv80lbQR1ccLN7fPMsXn_L8uDImnSowJOaqAw9nT-2Jg7xhD3E9NxWLfjcSk5gvu46ANhs8GZ3oZhMvtcKFfMZgoDEVJYrkmCwTkSYAFiglmQMrOfyQKzpGADYElWEhcA1y9g4FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMoxHPx_NgIXJ8aQbiFlp7PpR6wo0mSFjnpmngtCL4xT5bsYUHmbaTFMWw0TibIeCYM1it9mGnMVW9o_j0IlNKNQn7NeUuEudUKwoqUA1bKDCD2OBfjGQ3uoYiO6Z06aqxu4rC0FddYrQLLtEIkjkPRQtlBImo05lFr0wEK3usuhQQUKEFm3YmvNoi1mov00jJE1POjvmd3OWDj6QsMVf8iDxeC4OKdSdSWG55t8iyv_B48OTDonUT1-1bxZf8Wr-inynY_LwEFKWFYjUv3qMAFTdKxU9egEN2lEijzc55RpbPA0wJGrLo9RCUF1OswFEDTX4Sp9WdqVAgL3A8V5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
