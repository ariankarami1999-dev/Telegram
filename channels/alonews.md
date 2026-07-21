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
<img src="https://cdn4.telesco.pe/file/EPGMXoQXrC5-5zhiPjRnRPVhKyYXdgUulr1Kg31fkBaIE_ko5ovv-ODSrSomEqmS7THtdKPpyVPFlnR_VdcBguP7wo80E4HU1aIFu7kfMHwDhLJg6Yg3Sy3B-OGj_r9Kg6e_RITf5xalzLvvgojXaf9o9Q33rfiqxT2Yn6VFfcDRZayd4d1YjTPv0Irsn-ZjxgOKcCfgIvAYRaTmcdBJ8gmgb6EOqfXFsNalBYIIRN9IGB3Y8eb6qiLZ4iJrc6mq7Ge_cOSlEnKWwUWghcA7SakPR92ZJfY2Po7Gc5vm_71ug_f4jHYMfip22aNOAkpShy5pa-Nmn5LXSAD51nhnMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-136439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: اون‌ها حتی به بچه‌های کوچیک هم رحم نمی‌کنن
مردم معترض رو می‌کشن؛ بیش از ۵۲ هزار نفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/136439" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
دونالد ترامپ: اگر اکنون از جنگ با ایران دست بکشیم و برویم 20 تا 25 سال طول می‌کشد کشورشان بازسازی شود اما کار ما هنوز به اتمام نرسیده است و ما جایی نمی‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/136438" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136437" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: اگر نیروهای ما بودند، حمله مرگبار اردن رخ نمی‌داد
دونالد ترامپ با اشاره به حمله‌ای که به کشته شدن دو نظامی آمریکایی در اردن انجامید، گفت:
🔴
«آن‌ها توانستند از اردن عبور کنند و حمله را انجام دهند. اگر نیروهای دیگری مسئول عملیات بودند، چنین اتفاقی رخ نمی‌داد. وقتی کار خود را به دیگران می‌سپارید، گاهی نتیجه آن‌طور که باید پیش نمی‌رود.»
ترامپ همچنین درباره ونزوئلا اظهار داشت:
🔴
«در ونزوئلا اتفاقی رخ داد که شبیه جابه‌جایی زمین بود و هیچ‌کس تا به حال چیزی مانند آن ندیده بود. فکر می‌کنم بتوان اسمش را زلزله گذاشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136436" target="_blank">📅 19:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل معتقده که ایران نه تنها سانتریفیوژهای پیشرفته خود، بلکه بخشی از ذخایر اورانیوم غنی‌شده خودش رو هم پس از جنگ 12 روزه سال گذشته، به یک مرکز زیرزمینی عمیق در زیر کوه کلنگ منتقل کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/136435" target="_blank">📅 19:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d51992207.mp4?token=B3A_x6F2CuEjem0dFuC8XlzS3QVdcU4zsqvx2IrUXuk-ENsG04hMlLFOljRvO1mcQ49_kG9fLatlqINkPDtr1vUMUBtn4h-Tx7m64PknA6IpiwJOAKBgia47zt6mCOAszv2OvL6Vj5dTVMd8NdPcXtSHVqXdADTZZN8EuSD_x2YafenxzSA74_-8urg-Xyt68Q56vtKnhQ8CQ7_nVungBoBAjl8S-EpuMKGrK8hdSbv1xvea7-h23sNGAaGNNkCS1m-55hQAw6i90VqAVx7HWxKtYztjsFeVaVuLlIp_oKXLqDUht4cpSW2GsKaTCEtK1-dB7do7zqVZ2V1fbzb76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیتر هگستث در مورد جمهوری اسلامی ایران:
ایران هر فرصتی را برای مذاکره و نشان دادن اینکه در تنگه هرمز معقول هستند، داشته است.
اما اگر قصد دارند به کشتی‌های تجایی شلیک کنند، همان‌طور که رئیس‌جمهور گفته است، ده برابر سخت‌تر به آن‌ها ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/136434" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf5a9d4c8.mp4?token=c3hXlmViwHoAgO0CUZsYcyMaInTCTfv-XVNkE5uu3-VAo2IPQ67YOwEdbsjINv3KXbSKOWqyU6DPOiIF1yRTqJzFW-9RzMxEDxkrNG8i28u218o9r6CcY8BUUpZph6MN7I-z9DxSRv3jkV7FPNapovxFXwM_UFXZoVvhow-0jmgmTt3o6GS3v7fVySHTaZE8n1oGQleuxTyS48BFj8fSBwMTNAWRY6x5eqiL2T5EqLwIP--kWCHS92cFnqR9VVPGKTTxNm8T0HZKQDSfzqnst-iFseVjvbnkRyA0M_RRjC40toRwiXx-6YpIqP9wGxNTisCEw4J_Mlaxfwa1HDYizy979Uh9INTzs3QULj1aOvEgh0MNpnZZsflvk79SCEe4s7qJSs7C_WTOoxLOwTPwfos5VomNdrk8uGf8Tx6IYXKzxr7TAtgh-bEcYngO6TmNSpTIbq7oJI4Ro69ycBBRzqzrgTc8Llsq0EujKdFIlzvLAFWz-HfOworCEARgBCHdPemzxrqg3byljbDrG-F7fdQatAkEwEqlEmSW4ABrsUnT2hjGFfo1OyQaYlvN_Bmt0a1v_bnsw2DKJFJDz8Ff50atGOyv5VH0i6Aw9iLnpNa3hzJDK3TE3_1j2vT7DYb_x9lJGCz2mwFTsV56-gcl2aZ6M0YZ4S5pbKg0-lhXg_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آی معتقدید که ایران سانتریفیوژهای هسته‌ای خود را به کوه پیک‌اکس منتقل کرده است؟
🔴
پرزیدنت ترامپ:
ما بر اساس مواد عمل می‌کنیم. آنجا جایی است که اقدامات انجام می‌شود و به احتمال زیاد به زودی به آن منطقه حمله خواهیم کرد. آن‌ها کار زیادی در این باره نمی‌توانند انجام دهند. معمولاً من چنین چیزی را نمی‌گفتم.
🔴
اگر فکر می‌کردم آن‌ها می‌توانند کاری در این باره انجام دهند، هرگز چنین چیزی را نمی‌گفتم. اما به زودی و به شدت به آن منطقه حمله خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/136433" target="_blank">📅 19:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ : هیچ‌کس جز خود ایرانی‌ها نمی‌دونه ما چه آسیب‌هایی به ایران زدیم
اگه فردا از این توافق خارج می‌شدیم، یه پیروزی بزرگ به دست می‌آوردیم؛ اما فردا از توافق خارج نمی‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136432" target="_blank">📅 19:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ:
بدون شک ما «کوه کلنگ» را در ایران بمباران خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136431" target="_blank">📅 19:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ:
هر سایت هسته‌ای که ایرانی‌ها فعال‌سازی مجدد آن را مد نظر قرار دهند، ما دوباره به آن حمله خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/136430" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1c69b0f2.mp4?token=hS4MjrUdKy5dgtQ6sPyXvn3u0HyqQPmdZH7KT3CU01c8m-CvFMGaJ01q3oL-8wiWKnpD4xLp1SEn33IXn5pLhl8g0Y8eADN_uBQ4HC0T0Aj1Xs9sn7_7Tk5CY-tGJi8Ii0otz-X5MV30OEvpD0R3lrox5fg3KtOKaPos1LRROfoCzYlVTonBIPadvZ-4ZE3Uy0CYGLQTvUIZ39V5-mT31PG5rIFVIoUuZHpjhKjyA_mq0u4gCpSB_Et5Hc4033yQjQlUian__k5bsnhh1YZkmQ_ttjv0vR2mKrlZiuncEql3EdR3BWWyx9rJtHDO_zBVuY-IWFARh_qnMDphzG6qGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1c69b0f2.mp4?token=hS4MjrUdKy5dgtQ6sPyXvn3u0HyqQPmdZH7KT3CU01c8m-CvFMGaJ01q3oL-8wiWKnpD4xLp1SEn33IXn5pLhl8g0Y8eADN_uBQ4HC0T0Aj1Xs9sn7_7Tk5CY-tGJi8Ii0otz-X5MV30OEvpD0R3lrox5fg3KtOKaPos1LRROfoCzYlVTonBIPadvZ-4ZE3Uy0CYGLQTvUIZ39V5-mT31PG5rIFVIoUuZHpjhKjyA_mq0u4gCpSB_Et5Hc4033yQjQlUian__k5bsnhh1YZkmQ_ttjv0vR2mKrlZiuncEql3EdR3BWWyx9rJtHDO_zBVuY-IWFARh_qnMDphzG6qGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جام جهانی: این موفق‌ترین جام جهانی تاریخ بود.
🔴
ما حتی یک اعتراض هم نداشتیم. هیچ جرمی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136429" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Qi5vVHpEEwRb3Hu7cHks7S_CpUUflfbOclbmS7oq3NwVD941uMoZmEZ93HaaKbBdWP3d_ZRLNe1JiUs65t5q8QecfCqfC_YCOC9jMoSUyMg1tz4Id_MSgxXj2G0I08KIuC_doU4vztM5ie4O9jYnP52W1jX6ecKSCkg4OnGOTUjmyDrKn6mT5FdYSracvVMWv_ZXEIKcOaXC_c2Hv7pDxDEJholEbrrgXVJ5XMziD_r4lVgN-VXY3YJZLHN1oo96Fjpw9IsXylsDxvtnIQTiWhAZB9vyJV50i66vDad7MrH2q5YdPatk7zRZeyCZG1gS7CacZkvAnQeyfqF_UHyAIVSdsxPeNCxKaLqizmm7FhPAlC28hfpWUS_YxGtd3KSDiN6j_Bs_jVcdvyRRTCiI4DnI6iWYhFzW_a1QI4KSO5Rl2v9OWMWDMdRDZNOeOfz_a5VrbLJHhaQOWMdhrT95TtzqkQs1nAb3nNpS64XGKUBnVha1lY0GomN00b0X3fn4OCviYT-mP2JpyvRj-Ud27pmNCN55AmuZ-owakZeZlonTTpmDdPiEGoBYsQZU5rR225LOtHj5x8v1cPjkiuP1HHoArRW0b4Fvjk8tR1X4T97-HXPGNLEwaysVVbMLySk5MrmiIGDbc_S6MangBXF_owNwDUXm7CPA2PRNuII4F4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Qi5vVHpEEwRb3Hu7cHks7S_CpUUflfbOclbmS7oq3NwVD941uMoZmEZ93HaaKbBdWP3d_ZRLNe1JiUs65t5q8QecfCqfC_YCOC9jMoSUyMg1tz4Id_MSgxXj2G0I08KIuC_doU4vztM5ie4O9jYnP52W1jX6ecKSCkg4OnGOTUjmyDrKn6mT5FdYSracvVMWv_ZXEIKcOaXC_c2Hv7pDxDEJholEbrrgXVJ5XMziD_r4lVgN-VXY3YJZLHN1oo96Fjpw9IsXylsDxvtnIQTiWhAZB9vyJV50i66vDad7MrH2q5YdPatk7zRZeyCZG1gS7CacZkvAnQeyfqF_UHyAIVSdsxPeNCxKaLqizmm7FhPAlC28hfpWUS_YxGtd3KSDiN6j_Bs_jVcdvyRRTCiI4DnI6iWYhFzW_a1QI4KSO5Rl2v9OWMWDMdRDZNOeOfz_a5VrbLJHhaQOWMdhrT95TtzqkQs1nAb3nNpS64XGKUBnVha1lY0GomN00b0X3fn4OCviYT-mP2JpyvRj-Ud27pmNCN55AmuZ-owakZeZlonTTpmDdPiEGoBYsQZU5rR225LOtHj5x8v1cPjkiuP1HHoArRW0b4Fvjk8tR1X4T97-HXPGNLEwaysVVbMLySk5MrmiIGDbc_S6MangBXF_owNwDUXm7CPA2PRNuII4F4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
«ما آن‌ها را در سطحی تضعیف می‌کنیم که هیچ‌کس فکرش را هم نمی‌کرد ممکن باشد. آن‌ها واقعاً به‌شدت در حال تضعیف شدن هستند.
البته آن‌ها توانستند یک مورد را از اردن عبور بدهند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/136428" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b360764631.mp4?token=p0MyktM_VirJ6uD4Wpg_e_OABU4bLHpcey2K_V43ahRLQ_bnNLY3IFpb08f4jJZccYkNNQ71PcEzsIR-QtfHLiN4n7d3jkqxLXeQL7U9vulOg_SWOy6pgwEZKDIEAkljaVNWn6XmzW87vGzARoSI_JaDunefRlyygrhcu5eyLZCkpQGShUR14P_4njoXnpr8TBNiZAPHDttDypexM03igCzWw3psUynQ8lkJeJ0w3RcK3CxQUlgy8mdo8zFl34Ak1HRTMgm4uWiL15cxiz7CgSm7cY6xDSvxbR_W_iODZsUjxSAMsTvEZSy5IZDVBXMVMawDBEWyZvyW-N4xZfxKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b360764631.mp4?token=p0MyktM_VirJ6uD4Wpg_e_OABU4bLHpcey2K_V43ahRLQ_bnNLY3IFpb08f4jJZccYkNNQ71PcEzsIR-QtfHLiN4n7d3jkqxLXeQL7U9vulOg_SWOy6pgwEZKDIEAkljaVNWn6XmzW87vGzARoSI_JaDunefRlyygrhcu5eyLZCkpQGShUR14P_4njoXnpr8TBNiZAPHDttDypexM03igCzWw3psUynQ8lkJeJ0w3RcK3CxQUlgy8mdo8zFl34Ak1HRTMgm4uWiL15cxiz7CgSm7cY6xDSvxbR_W_iODZsUjxSAMsTvEZSy5IZDVBXMVMawDBEWyZvyW-N4xZfxKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: آنها به شدت خواهان ملاقات هستند.
🔴
تا زمانی که آنها آماده ملاقات به شیوه‌ای معنادار نباشند، ما هیچ علاقه‌ای به ملاقات نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/136427" target="_blank">📅 18:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbc828d30.mp4?token=bi504BvQ7EzLVaPbI_3xKHlkt5E_d1NP7bW2M8iMvt7p_FvMqsaWo18ifFC-jPS0XQgaFzlNatqH3Cc8qhuO6Bh0OsxMAgragPy-qMBJ0Ae983ma_2dS3lxIc0MFDbMHz2BLs-a60Tg9rA76LbHavMAqkApZ1XA59oPYMgiePQpocSIZKd062HPYEayGTxRp5kueOt9-YOJk2Dbo26aQJiM5osn2KP_AmaEVI0DTbB2TjmNXEtZSO4ZD45wNP3jOLBhx-rIfSirvhUwtPRAyNjFmAO8SD5mJ9WnezwmheufbG9Jf32xGp67SHrZoSl9qPUgORjA_L_tJ58Mp6kvkkCAf_Xxj9nN-leRs4MI5Bp6AZganQhe5IjyjaApku94ENdk6pFFfOYWvrwdZyYQpgnHD0T8dipHsid9DW4OECBidRc8FayznRvH6OpGyf_8gHaoH17-yoJUCzGSv65f7V59f92WRUQ9lA19SOA4XFFbftDWFrWWtv1uAUDesls7Z6LepK8brimjLYVP4QP4rlbyUK69mWR2UH8UQe5jCNiATpJK3MZtZk24B1Qn1Hr56gS8MgXBOHcka6UIeag86NR7BgaSGD91WRLGCo7f6r0ap0ANcgB9h1_oTds1wpvslmagq1vdn6qyp20U9bPTEd4uvLnyZ8qbqU1Xvhw-zrdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbc828d30.mp4?token=bi504BvQ7EzLVaPbI_3xKHlkt5E_d1NP7bW2M8iMvt7p_FvMqsaWo18ifFC-jPS0XQgaFzlNatqH3Cc8qhuO6Bh0OsxMAgragPy-qMBJ0Ae983ma_2dS3lxIc0MFDbMHz2BLs-a60Tg9rA76LbHavMAqkApZ1XA59oPYMgiePQpocSIZKd062HPYEayGTxRp5kueOt9-YOJk2Dbo26aQJiM5osn2KP_AmaEVI0DTbB2TjmNXEtZSO4ZD45wNP3jOLBhx-rIfSirvhUwtPRAyNjFmAO8SD5mJ9WnezwmheufbG9Jf32xGp67SHrZoSl9qPUgORjA_L_tJ58Mp6kvkkCAf_Xxj9nN-leRs4MI5Bp6AZganQhe5IjyjaApku94ENdk6pFFfOYWvrwdZyYQpgnHD0T8dipHsid9DW4OECBidRc8FayznRvH6OpGyf_8gHaoH17-yoJUCzGSv65f7V59f92WRUQ9lA19SOA4XFFbftDWFrWWtv1uAUDesls7Z6LepK8brimjLYVP4QP4rlbyUK69mWR2UH8UQe5jCNiATpJK3MZtZk24B1Qn1Hr56gS8MgXBOHcka6UIeag86NR7BgaSGD91WRLGCo7f6r0ap0ANcgB9h1_oTds1wpvslmagq1vdn6qyp20U9bPTEd4uvLnyZ8qbqU1Xvhw-zrdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ممنوعیت دریانوردی حوثی‌ها در دریای سرخ برای عربستان سعودی:
🔴
خواهیم دید چه اتفاقی می‌افتد. تاکنون که نیفتاده است. ممکن است بیفتد، اما اگر چنین اتفاقی بیفتد، ما به اوضاع رسیدگی خواهیم کرد.
🔴
ما قبلاً این کار را با حوثی‌ها انجام داده‌ایم و از زمانی که این کار را انجام دادیم، مدتی است که از آنها خبری نداریم.
🔴
آنها مدت زیادی است که با ما مشکلی ندارند، از جمله در طول این درگیری.
🔴
من فکر می‌کنم اگر چنین چیزی وجود داشته باشد، ما فقط باید به کارمان برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/136426" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6229ca593.mp4?token=Q4Ibi5JacpbADlS-ckeQjCLt7JnKuJCRT2n9bomtFDNZUzo0h3GZnd-9ZtLfvgFDm8rVapjJXO4qdzlXAqJRWXVpEL8k08b_YLaj1W1exmsrlGPSqu8IIL2eIDTZ-t8MeNXYz7K4m0ABh_6zxWRUeU7zXIWVjBQ4LDLgaXBz6MVODFm6lCn1qKlEtCRHDrbDxDblQfQNffLqktdhbb36wEu1P2btvE-lGEHQMittKTEtaRBETYDBfU95I4KUaaiwIBQ9zW4tHBJIMsvH0COo5codxJX3xohrztLTC3fYGxU4zJL52-vjY4h48tCUSusPGTUw_eusGOwPWN9s3rGL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6229ca593.mp4?token=Q4Ibi5JacpbADlS-ckeQjCLt7JnKuJCRT2n9bomtFDNZUzo0h3GZnd-9ZtLfvgFDm8rVapjJXO4qdzlXAqJRWXVpEL8k08b_YLaj1W1exmsrlGPSqu8IIL2eIDTZ-t8MeNXYz7K4m0ABh_6zxWRUeU7zXIWVjBQ4LDLgaXBz6MVODFm6lCn1qKlEtCRHDrbDxDblQfQNffLqktdhbb36wEu1P2btvE-lGEHQMittKTEtaRBETYDBfU95I4KUaaiwIBQ9zW4tHBJIMsvH0COo5codxJX3xohrztLTC3fYGxU4zJL52-vjY4h48tCUSusPGTUw_eusGOwPWN9s3rGL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هیچ نشانه‌ای مبنی بر آمادگی ایران برای توقف جنگ وجود ندارد. پس نقشه چیست؟
🔴
ترامپ: از کجا می‌فهمی؟ اگر هیچ نشانه‌ای نباشد از کجا می‌فهمی؟ چرا؟
🔴
چرا چیزی را می‌دانی که من نمی‌دانم؟
🔴
تو نمی‌دانی چه گفتگویی در پشت صحنه در جریان است. آنها به شدت می‌خواهند ملاقات کنند تا به آن پایان دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/136425" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdedce66bb.mp4?token=V6FbB9cpmm-_StSX47FPBzClUEd76SW8dLWaNSSjDS3H2MWu-mYr1ZPLwONRohFLpLZ2Ge7-o7V7ERzVWyklUG4__3f9mW_ooIuZqw1-T3ZPfY2_MtEg-7JV-lqhcntcyskz3UclcExf2cCRSJN7lvix_JkJrEIPD5I3jwA8g8MNSlQJsAedevA83eJi1k9c9CcKoKAMBdHa7Bnb1RQaGj8KTSOCWssgv3kvmbF5ivLLLiAKNh9ZUecDQwcHDNDOvi517QAFCDxH7cKCMe5KcU7X4kImyPupJlkq2EzvznfTEuhmMfF6QFGvzWIfi0IABxs-0NK_0q6OhNgyON58JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdedce66bb.mp4?token=V6FbB9cpmm-_StSX47FPBzClUEd76SW8dLWaNSSjDS3H2MWu-mYr1ZPLwONRohFLpLZ2Ge7-o7V7ERzVWyklUG4__3f9mW_ooIuZqw1-T3ZPfY2_MtEg-7JV-lqhcntcyskz3UclcExf2cCRSJN7lvix_JkJrEIPD5I3jwA8g8MNSlQJsAedevA83eJi1k9c9CcKoKAMBdHa7Bnb1RQaGj8KTSOCWssgv3kvmbF5ivLLLiAKNh9ZUecDQwcHDNDOvi517QAFCDxH7cKCMe5KcU7X4kImyPupJlkq2EzvznfTEuhmMfF6QFGvzWIfi0IABxs-0NK_0q6OhNgyON58JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ
:
ما مشکلات زیادی را حل خواهیم کرد. ما قبلاً برخی از این مشکلات را برای لبنان حل کرده‌ایم.
همانطور که می‌دانید، مسئله حزب‌الله وجود دارد. اما ما کارهایی انجام داده‌ایم که فکر می‌کنم جهان به آن‌ها توجه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/136424" target="_blank">📅 18:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335c9d8392.mp4?token=ASTuKNq9cgNIRG6f-KUTNwxGpUUdbWmT7zBoKEZpRgjBGKGLpJGwHdcpl3yv86lI88EUGhlGoOpbqH5QthDEcFkPpuRzasbAjNhmnxMsQydbtapKAczmGhDhPQVDr3TgviQs6cRTXJLa-vq16f65C9peIntieu_vZO2bp6TIdls5439q2-5fAkXKp9rw0RQQQy1wJr9snWoo-YEpYX1Vi5g9ZVDVIG3y11yK0wErw9UiLg9by0tzaqmkHKhQBEQXzDgQPAvbJQm6y9M-FyIwoU_k2RY-6p_z033mwFqvuaVFe8-3CeyuRjck8qndFDcxhfAXKFYorLvZ2VwZMeawzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335c9d8392.mp4?token=ASTuKNq9cgNIRG6f-KUTNwxGpUUdbWmT7zBoKEZpRgjBGKGLpJGwHdcpl3yv86lI88EUGhlGoOpbqH5QthDEcFkPpuRzasbAjNhmnxMsQydbtapKAczmGhDhPQVDr3TgviQs6cRTXJLa-vq16f65C9peIntieu_vZO2bp6TIdls5439q2-5fAkXKp9rw0RQQQy1wJr9snWoo-YEpYX1Vi5g9ZVDVIG3y11yK0wErw9UiLg9by0tzaqmkHKhQBEQXzDgQPAvbJQm6y9M-FyIwoU_k2RY-6p_z033mwFqvuaVFe8-3CeyuRjck8qndFDcxhfAXKFYorLvZ2VwZMeawzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
به احتمال زیاد، لبنان از بسیاری جهات، مکانی خطرناک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/136423" target="_blank">📅 18:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ecbd3e1f.mp4?token=S1xmiFwyP1Hx52pL01zwA33fJ0Gjla_F6kzDlGOCJ8quPe_d2ESnc6eSAG2PXRPwkfQpolD2rCdmzr8tcMwMvkILI8J5c3u-h9OA1brx2sfO3xwlSPIdqXtjFBwPY0zSFbEYRdlXNZD_1yuL3YZ8adM0-8iEQWqOxYrZcgLC-6FPtkXMpfeU5eDOCuRGdebqq9lpDRY6ZfuCa5ClBCUJuY_Z6N6KvzTKHWO7TKMNaBs8MsBw6j-i5evUVSJWfFt5ruxe-LqSbCxsg86bidYmTVh6URPnBMIJ5Yagn-M0kogLrv-8epzzpoAR7xlz7phVxtHUa5OO_TjJ0edr44SSKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ecbd3e1f.mp4?token=S1xmiFwyP1Hx52pL01zwA33fJ0Gjla_F6kzDlGOCJ8quPe_d2ESnc6eSAG2PXRPwkfQpolD2rCdmzr8tcMwMvkILI8J5c3u-h9OA1brx2sfO3xwlSPIdqXtjFBwPY0zSFbEYRdlXNZD_1yuL3YZ8adM0-8iEQWqOxYrZcgLC-6FPtkXMpfeU5eDOCuRGdebqq9lpDRY6ZfuCa5ClBCUJuY_Z6N6KvzTKHWO7TKMNaBs8MsBw6j-i5evUVSJWfFt5ruxe-LqSbCxsg86bidYmTVh6URPnBMIJ5Yagn-M0kogLrv-8epzzpoAR7xlz7phVxtHUa5OO_TjJ0edr44SSKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
بسیار خوشحالم که در کنار رئیس‌جمهور لبنان هستم، شخصیتی که در این کشور و حتی فراتر از آن، از احترام فراوانی برخوردار است.
ما قبلاً در موارد متعددی از طریق نمایندگان با یکدیگر صحبت کرده‌ایم و روابط ما بسیار خوب است.
به نظر من، لبنان برای مدت طولانی مورد بی‌عدالتی و سوءرفتار قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/136422" target="_blank">📅 18:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1a209c97.mp4?token=nEpa8ncH-4jzCwRpBQO3oiNBn4OvT9feFhgPtWmkwRQyrOfmof1ocsDacDTvhwBCzTIEcpia3YHlAKNenYsphHCWH4vpn68zvfjguUinXHeEDRSmn3K-0YRoCIzIlCt9whYvopFIQ-9T1xfLwAtpk1OKM64dFYJ9W4oeXTSNhu8dHZyRZJOvTTw4GfBYmAqle8xoIjvSz0ARKzPQcq4sdaVGsVgjriuPDvL3hgRoFg7t1EFU1Ctg2EzcyqV00eldhdSFsvQ2YnUiFz-ovRZftqUSMmR0KB-ETmfC7kv57pS4t60xMRJnv37aG-zAwq7383qDzid8wR68Zh2nw0MjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1a209c97.mp4?token=nEpa8ncH-4jzCwRpBQO3oiNBn4OvT9feFhgPtWmkwRQyrOfmof1ocsDacDTvhwBCzTIEcpia3YHlAKNenYsphHCWH4vpn68zvfjguUinXHeEDRSmn3K-0YRoCIzIlCt9whYvopFIQ-9T1xfLwAtpk1OKM64dFYJ9W4oeXTSNhu8dHZyRZJOvTTw4GfBYmAqle8xoIjvSz0ARKzPQcq4sdaVGsVgjriuPDvL3hgRoFg7t1EFU1Ctg2EzcyqV00eldhdSFsvQ2YnUiFz-ovRZftqUSMmR0KB-ETmfC7kv57pS4t60xMRJnv37aG-zAwq7383qDzid8wR68Zh2nw0MjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس جمهور لبنان با ترامپ | کاخ سفید
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136421" target="_blank">📅 18:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قیمت هر بشکه نفت برنت به ۹۱ دلار رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/136418" target="_blank">📅 18:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSi8BhN6UFmogB_MMBJBw4IA6BujvHytyLRGD7rxzjoEJmXUiGt1kJlVDzR1JR67d7QkF60XTw5ppsLfOfVKoqViEQQNGlTXTIFf0XLFsa05NY53ngI4bzILWaxkxV97-tLwxR0Q8SD2hFDY389UlUU2zSYQXf2t8q0NUTK3hO88-c_AftnzYSOiSeLxE-3ZSmhjEzYlMumhabJMaC8_Gqr9osnc5r9KMmJdsIGSJsLYv6Ce42VktxFnOWVyx6rIsHoE7jDk4VEXF2K_4XZJW9062pX1m3D2f71JP89XINPpuoopggOQJFQBl1IOwjwxhrbgSRs9ZMvDowjTOkuFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پستی دیگه‌ای که ترامپ از یه دختر ایرانی منتشر کرده :
(کشتار مارِو متوقف کنید)
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136417" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFLAQxW3hUY9YF6ZKxxwotdCn3tFLBqzUm5U9dyXICDYouqxVTGTbiwONMSn9xPwG9Ut1YXzuKQmlZChxMdWBfNRShwq8hB-NLtbqm_28pE5EEo7D8DET1rPkmWl74GR-IsGgsdZT5V0qjTg2cn8u0b2JrnNmCZ7XAB4tV8P8AFCt79Z0Y3zAwYwkUkQ2fPy0l28uq8EpB7KaSclazQdBo3gH8yo7J7_N4pcRS9K_91rmGQIPfvaz4nrg65S5BQo_9mE36-p_BhY3edRBrhRckCIfV0_ZhYd5fHSUOCrBPcKkSTYnK7_nLSK1S0bpe3WUlDUSpj_Z-JDwFL7g0hrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
تو جام ملت‌ها ایشالا جزو ۴تا تیم‌میریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136416" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41df0c99ee.mp4?token=C27LFV5F4VL3jiZ4LgdMahcRYc6Euw7DtrWqRlgOjy_2rWIOHASEmapc18sysvs5Pub3VUe5vMZ3tw4pOP95pqkMCnkLCY7MuUrTiyHEeT4fw_CVxj6BCVSEWg7GAvii-iPkUTSFNjxmkxomTpNW4_FiMa1sdE12FDE9QRDjOzFE-w_SjSAJM8rybirrrfiqQVLlmpt5ojMmxK95gitmyDeMBOjMcZFSRtBLzavdufzRzLniviGhfrENGPJZVq76bLpgo03NIVqFNf0ph3pn3xPBwSzFfBQo3qJeHh-jkTRV-kePfaUUu6bSuxI1GCTsDBXyg2MnG9Qs21P5dQTqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41df0c99ee.mp4?token=C27LFV5F4VL3jiZ4LgdMahcRYc6Euw7DtrWqRlgOjy_2rWIOHASEmapc18sysvs5Pub3VUe5vMZ3tw4pOP95pqkMCnkLCY7MuUrTiyHEeT4fw_CVxj6BCVSEWg7GAvii-iPkUTSFNjxmkxomTpNW4_FiMa1sdE12FDE9QRDjOzFE-w_SjSAJM8rybirrrfiqQVLlmpt5ojMmxK95gitmyDeMBOjMcZFSRtBLzavdufzRzLniviGhfrENGPJZVq76bLpgo03NIVqFNf0ph3pn3xPBwSzFfBQo3qJeHh-jkTRV-kePfaUUu6bSuxI1GCTsDBXyg2MnG9Qs21P5dQTqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرق شرافت و خایمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136415" target="_blank">📅 18:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اساس گزارش وزارت انرژی آمریکا، کل ذخائر استراتژیک نفت این کشور به 311.4 میلیون بشکه رسیده است که پایین‌ترین سطح در 43 سال گذشته از مارس 1983 است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136414" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc6dbe157.mp4?token=SYjJ_5NzqXx5jBgvpbX6oeHK-m4f5AWD7M7T46k5bl56-JFJ1zcEjGQmkUbG2ECKUZCmhi0w_E-U1ueTDorHzHCtcWKBY16eDrMziDo8u7nmA4B-3npF0uSktZf6Sxi9IxNVb-L4Y2sPKipJ4h8EQnjRtX_ZO4Py1VGpd8mo9hBNngC-6dNwtqS01nEbfcAJzATA6j0arvh1jUnihhS_0PO5Yzb8q4VvUd4xkrBZrF6276LibyjkzK9nG_faieQ--1i6A8uvrx8ngohYIVqdr44KqK6DpMsG1jKJSNB-5NRVqTW062bbfW-3TEu6NdxD4IIGj4Kxygw9XJYWXtUYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc6dbe157.mp4?token=SYjJ_5NzqXx5jBgvpbX6oeHK-m4f5AWD7M7T46k5bl56-JFJ1zcEjGQmkUbG2ECKUZCmhi0w_E-U1ueTDorHzHCtcWKBY16eDrMziDo8u7nmA4B-3npF0uSktZf6Sxi9IxNVb-L4Y2sPKipJ4h8EQnjRtX_ZO4Py1VGpd8mo9hBNngC-6dNwtqS01nEbfcAJzATA6j0arvh1jUnihhS_0PO5Yzb8q4VvUd4xkrBZrF6276LibyjkzK9nG_faieQ--1i6A8uvrx8ngohYIVqdr44KqK6DpMsG1jKJSNB-5NRVqTW062bbfW-3TEu6NdxD4IIGj4Kxygw9XJYWXtUYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های وسیع در استان سکیکده الجزایر که از پنج روز پیش آغاز شده است، همچنان ادامه دارد و نیروهای امدادی در سراسر این کشور با ده‌ها حریق فعال مبارزه می‌کنند.
🔴
سازمان دفاع مدنی الجزایر از ثبت ۱۷۲ مورد آتش‌سوزی طی بازه زمانی ۲۰ تا ۲۱ ژوئیه ۲۰۲۶ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136413" target="_blank">📅 18:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا اعلام کرد نیروهای این کشور از اوایل ماه مه تاکنون به تسهیل عبور حدود ۹۰۰ کشتی تجاری و انتقال نزدیک به ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/136412" target="_blank">📅 18:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مرکز مشترک اطلاعات دریایی سطح تهدید در آب‌های خاورمیانه را «شدید» اعلام کرد
🔴
مرکز مشترک اطلاعات دریایی در به‌روزرسانی شماره ۷۴ خود اعلام کرد از ۱۷ تا ۲۱ ژوئیه چهار حادثه امنیتی تأییدشده برای نفت‌کش‌ها ثبت شده است؛ سه نفت‌کش ناشناس در نزدیکی عمان و امارات هدف پهپاد یا پرتابه ناشناس قرار گرفته‌اند و نفت‌کش «Wen Yao» نیز در اقیانوس هند توسط نیروهای آمریکایی متوقف و بازرسی شده است.
🔴
خدمه دو نفت‌کش آسیب‌دیده ناچار به ترک شناورها شدند و خدمه یکی از آن‌ها به‌وسیله یک یدک‌کش عمانی نجات یافتند. در این گزارش تلفات انسانی یا آلودگی زیست‌محیطی اعلام نشده، اما سطح تهدید دریایی منطقه همچنان «شدید» ارزیابی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136411" target="_blank">📅 18:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
منبع نظامی یمنی: ۶ کشتی در ۲۴ ساعت گذشته پس از هشدار نیروهای مسلح و اعمال محاصره دریایی علیه عربستان متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136410" target="_blank">📅 17:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شهباز شریف: ما به نقش خود در میانجی‌گری ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136409" target="_blank">📅 17:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نفت برنت از ۹۱ دلار هم عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136408" target="_blank">📅 17:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / کانال ۱۴ اسرائیل: ارتش آمریکا به دلیل احتمال وقوع رویداد های مهم در روز های آینده، در حال تخلیه فوری پایگاه های خود در نزدیکی ایران می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136407" target="_blank">📅 17:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eriOYCGSPfqIf_yp3Z6dKj4vMRVB9-f1NBRa5E0iw5Dye6E9QzXj8hi52hkELga-zm196G4eTzNZhaMeTlx2GShClCKuXFdMnhwglNnwq7eFiF-6lD_evst_iOuD5qlU28kIrjU0VYLBgAN2RtdUWr91ZfqdeL7renZKBJW757hJtsmQpe84n9F0P7Okcru2tELXWXz4JJjhtJwv2b1yPLe1Zy4Zb8tr-zif8mDCh5dxc9h00G3_fG-qalSDMhebEuWUbLhCU--NCO9lD6oTtZyY7tLQeZtZSmJ2rUmcn94TWVSHWPFXpT86dqWqzgBYQrwXEA9t84NIQYn_ZMH07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رویترز، کنسرسیوم خط لوله قفقاز (CPC) به دلیل توقف عملیات بارگیری در پایانه دریای سیاه خود، که در پی حملات پهپادی اوکراین به تانکر‌های نفتی صورت گرفته بود، از دریافت نفت از قزاقستان خودداری می‌کند.
🔴
در حال حاضر، مخازن ذخیره سازی در این پایانه کاملاً پر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/136406" target="_blank">📅 17:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز: صادرات نفت خام عربستان به پایین‌ترین حد خود رسید
🔴
صادرات نفت خام عربستان سعودی در ماه مه (اردیبهشت-خرداد) برای سومین ماه متوالی کاهش یافت و به پایین‌ترین سطح تاریخی خود رسید.
🔴
این داده‌ها که روز سه‌شنبه از سوی ابتکار مشترک داده‌های سازمانی (JODI) منتشر شد، نشان می‌دهد درگیری آمریکا و ایران، تولید محموله‌های نفتی را در سراسر خلیج فارس مختل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136405" target="_blank">📅 17:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مجمع تشخیص مصلحت سازوکار برگزاری جلسات مجلس در شرایط اضطرار را تأیید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136404" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
«منابع آگاه» به شبکه خبری العربیه گفتند که واشنگتن به نخست‌وزیر عراق، علی الزیدی، چراغ سبز نشان داده تا در تلاش‌ها برای پایان دادن به جنگ بین آمریکا و ایران مشارکت کند.
🔴
به گفته منابع مذکور، بغداد به دنبال این است که با استفاده از روابط خود با هر دو طرف و توانایی‌ برقراری ارتباط با آنها، در زمره کشورهایی باشد که در پرونده کاهش تنش بین واشنگتن و تهران ایفای نقش می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136403" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجار مجدد در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136402" target="_blank">📅 17:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارتش کویت اعلام کرده است که سامانه‌های پدافند هوایی این کشور در حال حاضر در حال مقابله با موجی از موشک‌ها و پهپادهای تهاجمی ایرانی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136401" target="_blank">📅 17:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل پس از نشست مشورتی امنیتی پنج ساعت و نیمه‌ی نتانیاهو: وضعیت کنونی، یعنی یک درگیری محدود همراه با محاصره دریایی اعمال‌شده از سوی آمریکا، بهترین وضعیت برای ماست
🔴
تل‌آویو تمایلی به پیوستن در جنگ علیه ایران ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136400" target="_blank">📅 17:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
العربیه: ترامپ از نخست‌وزیر عراق برای میانجیگری میان ایران و آمریکا کمک خواست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136399" target="_blank">📅 17:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
صدای آژیر خطر در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136398" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp4hHwLwex2BMYwwxOgA2L1RTS1yCXNYVjy3kaNUx0bmfh0QugKDc2MaaeAf7OCmdMaJGp91tYbSdnBwpepwEVJzglzmPGitcvQlvGT1lYJM74FYS2j4D4ZD9rGo2X1zkP1rTaw-7LLpdvSRa5mVNLmck9ScJFcOCea4RKSbgbjHWXjOegtYTOAK-kONqmimf76fT22rPj0yjCo6_SHfqhtr8LarTYvjYGqBQs-nA_edLPgaJptfRwItVc16XlEGFj7A4zTM4iB8VwOUI3v7t2vpzKzSp4C_t1y0leLceZ52ach6mrm8cX6aQ6cfMsT7eFtGJKSZ1hjCpRl-l7UFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOvQE3ODijlImvqnpergIhqW6AR74l0h_IVn7VksbMSmJ63S59vZg3_DnIp39EzqNYoWqflfMPkAzjTRRir9Q3WEbgKMu9xCB9EYCl2mbKl0NJf6WmNs5CvuVH_WjvsIA9-nay1XSxbyI5ngEXUe7IE9Q9kBlMGoq2goxxeKAfw4bkZmu5npvHmsfBR99J82ctQEBd1-nt0hhT0q7VPVg2C3JhKsTYSD5_amfGgLgg_0NV77ky5RaBSMIS7WKlEVJ_fiOu8OJ1bETQaaFdLwowLpJj4V-pnzGY1g-_UtrT7DqDQgEXpIynvO8_c-jc5_KTmcAXusK8RIHSiNZ-Ze1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcde05073f.mov?token=C94crZba8yiF3g3ssiZi_6Bl8Pky0FsFOxM8eavQjjPxhX4_gJgprBuoC4ihQ7pDeVIBM5QrlHgp-UEyZ2pUxTuBookLo9p-uxwLBnP5nkduAdMMISnFUIO-QTOmLYqmmqMvSfCYmOpi9qEQrKzD6LfH96QBpbUDZhzXXbPP--t-tIUtvfO7zoV62ZBtheOUUng0iqyRTEe9necmTfvvr05zhSVy73nO2qFQlqEJKJHSUmD4TyPDjxNOZ15XMII_GfeTlG3D2wpEQ8TOwB4sXEayUoUxSJWN0eElUIyBXJDuewebcWMLtSQ4xARwS2cUZ21hs-ESRhJk2MXHuhLK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcde05073f.mov?token=C94crZba8yiF3g3ssiZi_6Bl8Pky0FsFOxM8eavQjjPxhX4_gJgprBuoC4ihQ7pDeVIBM5QrlHgp-UEyZ2pUxTuBookLo9p-uxwLBnP5nkduAdMMISnFUIO-QTOmLYqmmqMvSfCYmOpi9qEQrKzD6LfH96QBpbUDZhzXXbPP--t-tIUtvfO7zoV62ZBtheOUUng0iqyRTEe9necmTfvvr05zhSVy73nO2qFQlqEJKJHSUmD4TyPDjxNOZ15XMII_GfeTlG3D2wpEQ8TOwB4sXEayUoUxSJWN0eElUIyBXJDuewebcWMLtSQ4xARwS2cUZ21hs-ESRhJk2MXHuhLK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن ستون دود در معالی آباد شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136395" target="_blank">📅 17:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قیمت نفت خام آمریکا با ۳ درصد افزایش به ۸۵.۵۵ دلار در هر بشکه رسید که بالاترین سطح از ۱۲ ژوئن تاکنون است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136394" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فعال‌شدن آژیر هشدار در بحرین و درخواست از مردم برای پناه‌گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136393" target="_blank">📅 17:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فعال‌شدن آژیر هشدار در بحرین و درخواست از مردم برای پناه‌گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136392" target="_blank">📅 17:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اسکات بسنت: چین، به‌طور کلی، به دلیل شرایط قیمتی و همچنین برخورداری از ذخایر راهبردی بسیار بزرگ، طی چند ماه گذشته خرید نفت خام خود را حدود ۴۰ درصد کاهش داده است و این موضوع به‌طور مستقیم حکومت ایران را تحت فشار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136391" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صدای آژیر خطر در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136390" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsXM7TZ12ZAXCIwI4i1iLMDAUnajFS51kcOy1pFZK5WMWvawiF4iy-QTLEpmqgZl_hwEkyeeDb26s2Lo1OjhvMDzF89NylXcSSm9y9lhRuaZW-aC3hnNEW_lNRjxXmFmF2nmaaQzIJr7DeArt1l_zDRhzjdAJyHoRzJwuxj480iZ7mQfrHPQCJBghj1nN6fDO7ou8T8jnN4bORd1BaEeekin_5loKzFMZK-V-wFs-hQ3wwiPHmD6FWNBcwpG-b8clHc4q_oQUDZUk7tpsXxwnOOV_zup6Hh51YDMzZgKIK_mbmDG286QTuvzfIg-MOyVNKEEu5khriRAXrUGARrlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: آخرین نفر کشته شده از ۵۲هزار معترض بی‌گناه. وحشیا!!! کی دموکرات‌ها از خواب پا میشن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136389" target="_blank">📅 16:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو در حال برگزاری جلسه‌ای درباره مسئله غزه‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136388" target="_blank">📅 16:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت امور خارجهٔ فرانسه از احضار کاردار سفارت ایران در پاریس به این وزارتخانه خبر داد؛ این احضار درپی ادعای بازداشت کارکنان سفارت فرانسه در تهران انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136387" target="_blank">📅 16:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تشدید درگیری میان آمریکا و ایران می‌تواند باعث لغو ۳۰ پرواز مسافری اسرائیل در روز شود؛ حتی بدون آنکه ایران مستقیماً اسرائیل را هدف حمله قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136386" target="_blank">📅 16:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کابینه عربستان سعودی: ما بار دیگر همبستگی خود را با کویت، بحرین و اردن در رابطه با اقداماتی که آنها علیه حملات ایران انجام می‌دهند، اعلام می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136385" target="_blank">📅 16:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جروزالم پست به نقل از منابع: هدف از پیشنهاد آتش‌بس ۱۰ روزه، یافتن راه‌حلی درباره تنگه هرمز است
🔴
یکی از این ایده‌ها، ایجاد یک «دالان میانی» در تنگه هرمز است؛ منطقه‌ای میان آب‌های تحت کنترل عمان و آب‌های تحت کنترل ایران که کشتی‌های تجاری بتوانند از طریق آن با امنیت عبور کنند
🔴
واشنگتن اصرار دارد پیش از اجرایی شدن هرگونه آتش‌بس، دست‌کم درباره برخی اصول مربوط به آزادی کشتیرانی در تنگه هرمز به توافق برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136384" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136383">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=E-noulBIiyw_dECUiNkjoNfZxLQ7lo0ysSjQLJKCeEAYFjwvDbE0CfCVRw88LUkn6QGgfrRc7g_J7WrNkvTTUXNEZ5hMY21ndyzwYydkRclPi7frpMdx7H4jmJp-iai0xA8sHZM1LRHZzwmW4z_jcMKbs6ZTCnFCjpNlZjlIPw4FgsD_4pVAg0fvffbKKx7_kQuSfOwv7Y128chcuYJXRO96CgYQvYW8IijSISm9tZsREDO9yZALVsxqE8nD6IWEG-sm1cJBMhY2hWyhYOp8HoQf73cBrFE9I15e8bl3mM1wWKCJ0cyJECRjyIwLR4u_VajWZJKTJKOofuPFG7PBXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=E-noulBIiyw_dECUiNkjoNfZxLQ7lo0ysSjQLJKCeEAYFjwvDbE0CfCVRw88LUkn6QGgfrRc7g_J7WrNkvTTUXNEZ5hMY21ndyzwYydkRclPi7frpMdx7H4jmJp-iai0xA8sHZM1LRHZzwmW4z_jcMKbs6ZTCnFCjpNlZjlIPw4FgsD_4pVAg0fvffbKKx7_kQuSfOwv7Y128chcuYJXRO96CgYQvYW8IijSISm9tZsREDO9yZALVsxqE8nD6IWEG-sm1cJBMhY2hWyhYOp8HoQf73cBrFE9I15e8bl3mM1wWKCJ0cyJECRjyIwLR4u_VajWZJKTJKOofuPFG7PBXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از خسارت گسترده به پایانهٔ صادرات نفت بندر الاحمدی کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136383" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136382">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر کشور پاکستان:
در کنار ایران برای صلح منطقه تلاش می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136382" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کاخ سفید : رئیس‌جمهور چهل‌وهفتم آمریکا اهل بازی کردن نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/136381" target="_blank">📅 16:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان: هگست قرار است امروز بعدازظهر در برابر یکی از کمیته‌های مهم سنای این کشور حاضر شود  و درباره درخواست میلیاردها دلار برای جنگ با ایران پاسخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136380" target="_blank">📅 16:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دو تانکر نفتی حامل نفت خام عربستان، با توجه به تهدید انصار الله یمن مسیر خود را در دریای سرخ تغییر دادند و به سمت کانال سوئز حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136379" target="_blank">📅 16:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بلومبرگ: مالکان کشتی‌ها به خدمه‌ای که حاضر شوند خطر عبور از تنگه هرمز را بپذیرند، پاداش‌های بسیار قابل توجهی پیشنهاد می‌کنند
🔴
شرکت «سینوکور» به خدمه‌ای که یک سفر یک ماهه را انجام دهند، معادل شش ماه حقوق اضافه پیشنهاد کرده
🔴
این رقم برای کم‌ درآمدترین خدمه ۹ هزار دلار است و برای کاپیتان‌ها تا ۹۰ هزار دلار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136378" target="_blank">📅 16:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7g4Pj6bncKfxD62PIdTp0QjnZqGglMLE2mH_Hfp-Ppvg272qkajvSWvyCuLm3arZJ7O1-bgZtmyZ3-9kxolhrAzG9GWtX6CQBie6xgfhcNlUguTy91ME3vyLeZQXp-uH6U_9y1bCFyJOd72vufpk85qXM6ADQGbBOyWTotiHKanNeWJXgeC9ujUJe7c-_6jNbOAw3-ZTgrPLYgb7zOi0HHwBpmcgOzeRqO6GcQD0BzYAENGQbjoXCfnHkAQbJDehnSpFEFMBqrHxvbV72YdnSRW-p3llJSWc_b-eLHSOghvyLaTOQdiJIF2d2qAwxrYDmiJ_491OrQ7fE1nN05fPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه هوایی الامیر سلطان در عربستان سعودی شاهد اعزام هواپیماهای جنگی است، به احتمال زیاد به منظور گسترش نقش خود در جنگ علیه ایران. در همین حال، عملیات نظامی آمریکا در پایگاه علی‌السلام در کویت همچنان محدود است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136377" target="_blank">📅 16:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرنگار شبکه «العربیه»: یک کارگاه تولید و ساخت پهپاد در شهر بغداد کشف و ضبط شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136376" target="_blank">📅 16:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr4g9umPV9b6fBUtfNtjVEqDcEdk1Tis3dMA9TXeQrUAwR7uKTwJWPGqyQRQZTnE3hECAOTs_t9oE76Olc76_nlCMgPNB71omWSI8HBhiIqWtAbLH5VIik1KYYhr_PvHz1OYBk6J1_2FQ-mYvJ2yVzntBotQgDw7SLcQ5ER5yhv3rPn-zcVpkFqScL54W0WzFVPXHslD9fUasS0FxdCE23v6VFYVs0ImUIUbjuDZFTZPCDqY_qmUrOYYBS3MY9jCbQfRFx0uZOR8XjFZD7eKytKHSpR-Cx2NwBr0Fj7dKuHmpeizx0lctHIRmgcrhf7zKz9WMsT6ag--jXVQXbr8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: افراد ثروتمند و شرکت‌ها به طور بی‌سابقه‌ای از ایالت‌های آبی که توسط دموکرات‌ها اداره می‌شوند، خارج می‌شوند.
🔴
اگر این روند ادامه یابد، این ایالت‌ها به "محله‌های فقیرنشین" آینده تبدیل خواهند شد - بدون مردم، بدون پول، بدون امید. "آمریکا را دوباره بزرگ کنیم!"
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136375" target="_blank">📅 16:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-I9KSasshnFH66OFFNwE1B5VPdl_4kCksYiLIUEEBA-zRao_VPJYEjLCwaxHXMc7M1GXvtGH55rLpH4jhDryAib5IMjG4d2B9YI4FvEHY1nezFPjzpEWm0G17GPWLrOTa9IvZbqixTKQZjRKEhpSgazqQS678hLdkL7zIRFXWR_KrV5TcsqXqZBbzfIc2fHUuF6rz9V6Y7K52CADacQ7MAEh5mELXdnEEZCNzTCWmyh0oCPIl0CRJe13wITIHlFcZLOk2HcASsVnPA-zxay2stxRzAN3f18H1z3OpJceKTR5qim9uX9ahYuqUCTQSHZVpQQqL2y2YD6sJlqAJEP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت از مرز 91 دلار به ازای هر بشکه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/136374" target="_blank">📅 16:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: این مملکت را دانشمندان و دانشجویان نخبه ما می‌توانند بسازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136373" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: اگر هزار بار هم ما را بمباران کنند، ما می توانیم به اهدافمان برسیم. به هر آنچه وعده داده بودیم، عمل کردیم و حتما در آینده قوی تر به وعده هایمان عمل خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136372" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اسکندر مومنی، وزیر کشور ایران، امروز با میانجیگران در پاکستان دیدار کرد، در حالی که تلاش‌های دیپلماتیک برای احیای توافق موقت از بین رفته بین تهران و واشنگتن، با وجود ده روز متوالی درگیری، تشدید شده است. (خبرگزاری آسوشیتدپرس گزارش داد.)
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136371" target="_blank">📅 16:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فریدریش مرتز، صدراعظم آلمان: قصد داریم از سال بعد همکاری های خود را به ویژه در حوزه انرژی با جمهوری آذربایجان گسترش دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136370" target="_blank">📅 15:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پنتاگون اعلام کرد که سرجوخه مایکل امانوئل سوینتون، ۳۰ ساله، اهل فاییتویل، کارولینای شمالی، در جریان عملیات شنبه گذشته، در اثر انفجار کنترل‌شده یک پهپاد تهاجمی ایرانی سرنگون شده در پایگاه هوایی اربیل در عراق، جان خود را از دست داد.
🔴
سوینتون در گردان D، تیپ دوم، رژیم توپخانه‌ی هوایی ۵۵، در واحد توپخانه‌ی هوایی ۱۰۸، واقع در فورت براگ، خدمت می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136369" target="_blank">📅 15:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136368">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMXpCAvsrYKhpNsKLvj-QNDuF21UhM532g9nu9lkZ9DPKE5DSl92oah3g7oSBJt_EgOZhShxxCa15bqA1E1aId7PtjYsfSoscO5lg9g6T2YFOhXcV9GPrR3pywWhmsjohiG1pN8dGfgn8GN8WSlWoZymyVZ1j6bIcvQxkUimaIxIa3EMCKq2bannSrbvP_I4BCA9y4y5d5Ru7IZ53xLsYW-ZRg2TW4N9YAbSF5N609UXXdZWDKlHc_tjSkRYindO7QIsAadh6APmj36_e5AFY6vzUdXdwVnKILnZ8ka9HpW-sdP-Ua_t-Kwdw0wiHsy2uAgYzMLFjQix7bxApHxKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وزارت دفاع بریتانیا، ناو جنگی روسی به نام "نستراشیمی" روز دوشنبه، در آب‌های بین‌المللی، حدود ۴۰ مایل دریایی جنوب شهر پلیموث، یک تمرین شلیک زنده به مدت ۳۰ دقیقه انجام داد، در حالی که ناوهای نیروی دریایی سلطنتی بریتانیا، حرکات آن را زیر نظر داشتند.
🔴
این کشتی قبل از شروع تمرین، به کشتی HMS Tyne اطلاع داد و درخواست کرد که این کشتی گشت‌زنی بریتانیایی به فاصله‌ای امن‌تر حرکت کند، در حالی که نیروی دریایی سلطنتی بریتانیا به نظارت بر فعالیت‌های آن ادامه داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136368" target="_blank">📅 15:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شرکت کانادایی «شاماران پترولیوم» از تعلیق تولید نفت در میدان‌های نفتی استان دهوک در اقلیم کردستان عراق به دلیل تشدید تنش‌های امنیتی در منطقه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136367" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما یک کیف پول ارز دیجیتال به ارزش 130 میلیون دلار که به سپاه پاسداران مرتبط است، مسدود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136366" target="_blank">📅 15:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / حمله به ارتفاعات خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136365" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136364">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نیویورک تایمز:  در حملات چندین باره ایران به اردن حداقل ۲۴ سرباز آمریکایی مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136364" target="_blank">📅 15:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136360">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffxZQvHMpaCPVwJ0gZlP6uP3CwohlhksnPp77ogL8UvLl9WydNc8xBeeK56aWJkV5at-CEvGO52f5tpXwcyp5lvB9Es9OELmEQZwTYdk6pPIVtOZgb8h1Nh08L4WO5OJczVM9knmxlOiKvSqrMjVcLoY0vo0KgEgYUmjmrHWb0_Ifpt650AJ3_AhxCjDvNv4yo5L0DkortD_JwLyLXynICJ8fcJi9xPqtiOWsLpPKfifmFXwy359z3gWAlLVCnKjN-Ok3AoaildiMRD4oiHS0fi3YLpYD49iyYgM3beXCXjJyOkrkMYJxMblzswb6iNpzskXqll5U6XDNE5BXpcGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCd22JOGrBrOqDuL1hHYJ2dqG85t4siW-5Q2_GZziqimCCQdZKXIGCPV53s-23Zw3V-9Hjnd-i51kBWJtbf86LX_0uiTGFaEtra-J6loEnvDnaNVUxDZ0Y0XOcXmuBME67WgzsnNIvt30eaRq9jsDCdE_dfQusYWVsxbJE2tkfJWLFvj_cfy7-Xg88CvA-GBk-8rGmvC2_K9hLnUztUbMN0SxDa4Ap2jIg0zFRyuMKzGzCvU7XRu9AA5JTYg28SlFqua_is1b9PQ0wXwNCSNJrf_bHnlQeL_Mc-gPk9ts2DW_e5If9X2sXGhbXLxZLp-GBIMRhHhZVXcygSkaneT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWXFi961zts7IljDmWNQ1M7kFMmnw7Ynd9n8KnzITjF8MwEEG6jIACrX2JVAdHzk3_SEZHH6BW9yT5b6veNLdW1qHepylQDbsxgyKHRTGFLtbl4rP7klCwAIg3UItv11QrVmOvTePWIgYJuBzcPS0umXOkpw3aDtteig8G0YUAV_YKVaJpTzeCvEVEIDl1AQwiiWumClsinICeg6zwzSHcpkSvQD_anhDkxklvnkMn6KH1mA7M-7F3fxMHTBHMA3St2iu1yduEBC6nlHQhJnZxMupry2PAmu0Fcln4PmtbVPEoMnJRx6N0UHwTt5RNUUgEM82KBY49FTjLnOyCZcVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d35a2500.mp4?token=UGa5FT9Az9-pM5SYoRjkmJkeG4iO2vc-GhF_qTwjvRrn5Z18ixKG8XVMiNiKEodGg3P0xzKFvVkKrmfLcLGogpB_cHZB-RNJvyg-5M5eQebdUN_GaHsvASjeds2rxhyj4x3GpW424IRv1Wpw7Zn2E9W0xFe_tOT2TMb-iTTPljdB5aR2Q2Co66YiB0rwUMnBYbtjsAunbNbYGhWSxmVVQvLoPLMc6kfUBlMZfvHRg1FBrV5HoRMhswlPxHllm4PBmU-ndn7UEt3ijxgwdDStQ5eADWYMQyudTO8xpcjzwAJLyVNhRKCDzwNUxePeJzrfeoLzyHFmlea9_xDv6gPnUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d35a2500.mp4?token=UGa5FT9Az9-pM5SYoRjkmJkeG4iO2vc-GhF_qTwjvRrn5Z18ixKG8XVMiNiKEodGg3P0xzKFvVkKrmfLcLGogpB_cHZB-RNJvyg-5M5eQebdUN_GaHsvASjeds2rxhyj4x3GpW424IRv1Wpw7Zn2E9W0xFe_tOT2TMb-iTTPljdB5aR2Q2Co66YiB0rwUMnBYbtjsAunbNbYGhWSxmVVQvLoPLMc6kfUBlMZfvHRg1FBrV5HoRMhswlPxHllm4PBmU-ndn7UEt3ijxgwdDStQ5eADWYMQyudTO8xpcjzwAJLyVNhRKCDzwNUxePeJzrfeoLzyHFmlea9_xDv6gPnUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای حمله موشکی ایران به یکی از پایگاه‌های نظامی آمریکا در منطقه، که توسط سربازان آمریکایی فیلم‌برداری شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136360" target="_blank">📅 15:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136359" target="_blank">📅 15:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136358" target="_blank">📅 15:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIa1wRj212wu3Mx7-I9Tq2JttsJENMbQxMpLCG0xqXSTG9L2A_ePtjZHZIK9J8dW6iMkgV0jDl9uuxloGn0CrOEJ94-r7WVShlbtFdyNyw6zz7prAqP6B_xGDl215wS4SZKZGN3abuGlWJ4dJIbw8u3Aq3aBP3LiC7b3dJlhUTI9bD4Phr5kIg6nOP1qsFSnEOBK85IaM7puys1cRTi8WA2vKVrzSddnGMvvu8ZEhQZ4Yd740Mw3xovUBcyer63T1T7RB_rR4fvQn-2Q3DQAEjvRicvHh2Jp6zVJ9-ArmEN8hSXMJSHFNwPKGC5_NbyD5HWeW_pzNiMuW5W81FIn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای چهارمین روز پیاپی به تاسیسات برق و آب کویت حمله شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136357" target="_blank">📅 15:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136354">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzAeZkT7edqUafwVPuBZBsJY_qQ6GXA0xHNaV9dwpkJxNq3gAdeKuZ2CnGiFRysO1AbTqtdrRlWn7FpabEf5RJyZxGvZS88M1vsjtyPJh25rS6w5pQjgtZjD8LIVJ1QBwUOZLrq2pPy7OjCSLRAqKsN9bqd4XvWk_LRe0lnPSmLBy-vYQkPgZAj0DC5zpN53hluCzYf5l2hbm5ttzfLb1X4oYEMNh2jMyStPHhNb4dgLkVCmfE0usg-qYkLwBpy3bjaKYvcTIYHgLLVKj1waNOMkKxVinnO7EqbYDM_65LS2n-4A9FQjiaxUdFAlhg7SJl9J-Hgq9vXxM8FX_MiBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور با نخست‌وزیر پاکستان دیدار کرد
🔴
مومنی در اولین جلسه کاری در اسلام آباد با فیلد مارشال عاصم منیر، فرمانده ارتش و رئیس نیروهای دفاعی پاکستان، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136354" target="_blank">📅 15:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136353">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: تهدیدات امنیتی در تنگه باب‌المندب بر نگرانی بازارهای جهانی افزوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136353" target="_blank">📅 15:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136352">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqT0TpFwJ3Daw5w0A8Gdupya16tALUNV7-WUi9nehBFGOSarPT1TtRzjssxQBvhGZG2b3Dp1VMbjarBgNL1b1locKZwS-ih8SEj-RODnmIjtTl1P_JYxv9BW99HYF9mvlc3AaRHCiiThlAXC4ph3_lo49Bf0OcrVA3-kLmIoAGu2gbBOpZcNsSoTk_IiSeEIdpqy3LxMWp9td89U0Uv1Ps0MrgdrAHiEuc8R4xgdSyR0SVZtgmnsq0k2DnSVartmErnYuFS9g9ATGY8a8iDNUHuYRDCV3yu4GBjI68bQxZ07kWrZMHbtPoOyk-NedktfYLrTbSBuUxB4Ee4ouQKlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده مجری صدا و سیما:
عراقچی در زمینه مذاکره خودسری کرده است!/ عراقچی بدون هماهنگی با تهران به آمریکایی‌ها قول دالانِ جدید کشتی‌رانی در تنگه هرمز را داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136352" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jbFHSo-_vQUJSKmp1P1qOfgrt-07li6wVoAqMA3u6uuO06laVUoJkDGz7J269cJngTGObbCR2jhGWD5_9V6rgSW2yeftaKKON8eS_LToWCD2GFdhrXfHJJI5JkyJOQXeKAxg7BxqdtmvhWxLjBggLB0nEy9uuYlG448cp29MJ-MPAwPEpiNMmeFUP8AR9eF36Mci7lGHi6vlOMUQg99V3E24WQdWlAVHrI4ZAASFPBxPVlR9ewLpL0sRwEkIvIPJqSs_JfIeNS7w83wD6QsahuW1_xPNvTyjw1o3MVzLhnwCaEx_O6jxONQicW_9xTIw3-qmMhSEPhFnuG8KYGOGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته: با این مملکت درس خوندن جواب نمیده.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136351" target="_blank">📅 14:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daef934e1e.mp4?token=HcnA5-8XlBcXw81q_593P548U-JAbzVIhvRqmlzrWZ6q6fN8Uzul56w6Qlm67lJDb1P6VkM-e0_wosvyfnnwKPwPH1EKb46s7BMdK7vTju3VBdjfekTZAX5yh0Y-KqAPJeDwgen8wQjBk7_I2-l1h6TR0eaa0-kjiYC_Bu51Ix51a0BbUSACi4jlAUI4eUGMBaKeyiII3eK9x0RRwV7ebBU9mhpq9EMZ1dRE9X4V3ATkqM7qzECqhjHzf06VeurZd0tOfiria_qjB3Av6KsYdy3K6uqFL6fm_kzBYzwyeJ3WXuwTk1s_J87pj76uZwVZz8MVYmM9cnut-WaHPDBifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daef934e1e.mp4?token=HcnA5-8XlBcXw81q_593P548U-JAbzVIhvRqmlzrWZ6q6fN8Uzul56w6Qlm67lJDb1P6VkM-e0_wosvyfnnwKPwPH1EKb46s7BMdK7vTju3VBdjfekTZAX5yh0Y-KqAPJeDwgen8wQjBk7_I2-l1h6TR0eaa0-kjiYC_Bu51Ix51a0BbUSACi4jlAUI4eUGMBaKeyiII3eK9x0RRwV7ebBU9mhpq9EMZ1dRE9X4V3ATkqM7qzECqhjHzf06VeurZd0tOfiria_qjB3Av6KsYdy3K6uqFL6fm_kzBYzwyeJ3WXuwTk1s_J87pj76uZwVZz8MVYmM9cnut-WaHPDBifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی‌های دقیق ۱سال قبل مطهرنیا از وضعیت آینده، تنها یک موردش مونده!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136350" target="_blank">📅 14:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXhoCyFPIv7vH9w9nAiqDIa93hL6bkwL3LT9DZXoY08arQOMxU7sKHekeLw0AZWTBMP02B7fsajLDOR6KdaatVYAM8eVXPXhV6baORrmfTLHsGviqPQBjffM-ZosXymJLDvPCwszjsW2qsm4mffTOxlyvgnKQ-PIJHv8MmnTi-ePS1bP46shtFdCft4YZDwP-dZa4yl63rAT8biYaVK0LPx1JJ5UXZLo3Od4j3-TNlgjOYdhUCf2LJObs1LzmaZvFmOj06Q65r4-HI38kT-qZbW5sVFWzJlzKKQUSRi-sDwIa1vx5r_ZaW8FGgkW0pGTs9FjB2unjcLCwbpuuP2qVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان :
ارتباط ما با آقا مجتبی خامنه‌ای، روز به روز بیشتر میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136349" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzdc_GFM83BrwOvYl-cMbjnKWyjipZz_3mDW5Xc8KeMVAdisObs-2BKMg6NPhbEe7VURymWl4cqSalSCOwUUN896xDinnNGnE5r4yuAo0vjpa-2znLc2G0rY-MnbN92mP8PwXAxTIe9WNzRNFWnvkVDpVLvcFF9mkNaK7ewRiWyoYQpItnti7Zo6nICAmOodI5c4AMXS797v45_0LD5_vSoskaKOhpp1WtGDz5TaUm3NpYPRV5bcx0OVZ3ItmfpCV1g-Rg-j3iP2XsPeA3KlE1VwI-fA-ONGxX6hBLlk4dO75L_Efc0qdHCEvfFwRSJAlQnXU-Vj0y_cB_6Bn6jnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136348" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgP76TCPAcFAC5aMvOnDj48YN2O1hiDO-hlxU2HXVSzyW7MBRFKBs039bJcxtfrk04KJkkEvhiDuQNdaMcQymZJy9kZ_xaeAkfSogYkVif-7g9qWcuHODpIbuHOG1fGbAW-231L5p7EHyUSAv_lexRld_vbKDxP5u5QXd2W3f3RqLWhfhVWB8fHYe8jxwUANE6GGqogei_RI25jnHo_UL7M24OHsLzyDEoWSzcuNt67UyBJsHaaG4yIfaQTmt1o5Fxrhq0p2tvYQYbyVX4SGWr7WxuJU93tXhNJxXKTb42eE5pVjr4tcskORVm1IuFRdcJRQvOgl0eIHeNMQC-KMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی از اسلام آباد داره میاد سمت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136347" target="_blank">📅 14:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNQ-QVKlbT-lOyWVKwfBxuAqHqA9SF389ugGGQyQUDDwo1bwPsvywodwT4VPehhpvEq3n60t2vP8rJT70CbF9nAOzMXMMfkLDNR5x1shPQunVbctBjaPUHxZT7LkkljHy1pxREnvAqNlnqVvgLN_KUKqt4NFbx2klX83sqBP6nXPmJBSS6u-iVgZCUzyurhLfzKg_Mrzf68x-A5fYFwlkJKvLNjVvJY7vwH2Itnj5aQRDWBATTkgZkpst0ghUfI2IzbhPjR8W4qEALyvil2-4qdqKzRd44PIPNVyPBo7tjtNrSTX-aOE6rwB01SVRoX7nSg1pz42J-U9bUQafGHLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مراد ویسی، عباس عراقچی رو فالو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136346" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLeUxi9ZW3iDbSyjxorWxFPc_ZArygz6a15wew1NVnOi1rgtlOmHXUD8fjlAqxqnlTt0fQHdkl8FRV642dWPu8sgTxkt8hwKz-mb9G6bHNiHQvkaGZTXNsPS38nKUxSGre6kbSeR9A21SCLxmimd9PmGrZjjdwGXC_6KVYotuVBuzKYmL_o7PBD_cnatgsukc5vTzawk9LTNhtHJ6U8YniKnfxd-JQ7FQwrr-XqSAVaHU4BY36Kuzf7sTAG09tU9VkxWq8QBkDHpp_q0yURWj7O8P7_xRB5zAcmRs3dAi1XqeKMkeZgpnP6rdQUZcH0c9uVRusOMRHidxd3FVXecFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
این افتخار آفرینی فقط بخاطر من نیست، یه گروه آنالیزور و نخبه داشتیم و این یه افتخار تیمیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136345" target="_blank">📅 14:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjqgF5SE0i1RVGj7dU0HpwtmOfpj-U6U2zOA8cUGyWUFY6Z1yrBIOptdh0yXX4Gn1xUrq8-GA4qUvY-qpHBMSJ5PC8flaqMCvzLA1due9KyrL0F3rYn1uY0K5D0bPIGPtxeNU45cP_vozXabvzRGgW_MWbelsJHCJwyrKug8fqKYq67Qr6JyNm6N8EkCSo-oaKBcyIev3Qo6Q1j6UWWY0V4ss8RXX4HrFF6nJxBnvP_gpMiovPq2BZa6skqBgCT00U_hPv6Ta-20NARLaEiAGA0jn6v3Lot2HT0I3J0p7jvE-NQs0fcfmIwbOS6VFiUxX8N4d5olhb5jPLfZA8EmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLI9Nb1-CownyJPLjS1fhfn80IQ9xwXekD7nV6Gq5RppXZWqBBFBsOrK0N_D0KMU5ocqfVeOPOrn1bFazzLu-CeckWG0UKzCy0yrOc32no6FURPmXlpgw_C_Uka30Dl8gFT7dpjMQgX8xHdVQ46kr0iDHF27KT9b_r81o1ZtkMf7MgsVuHIWvJ9u3YHXL8tsjWRFOzys_oI6F6f6zIH75hfWvv3A9XvFqGubrvshTW2djMvH1cY9rqWYlAVGVvva0of_u2p4RGBnDVfgD8seDe3DQww5hzUxAUp4aJG1wibmJ0xBuPC3wu4qi93iKG6c0FGJ76hEvZ2ue2kdfWlNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWs7bDWVyr4zb7hvsvKh1-w57S2SUT2OKiF-HJ6V4dxs1nO6hfEGfZbQO4ZCMEHT_TgrcPyZ45ChT2AvObKNA1DWYYeiYmAWlxBnB1vYbavETbIDr_JuDwWS6HZE8_QwFDpIzwE3GjYdJjZj_M7csU1offkcINkP6Un_nFcdGMGhVl63PHPnkujv7-HZL3P1q8xtNbv5k2VoXs7GLjIf-L6pX8aMp9Qz8hKd8SCUJcZsILPPfU8nBGXeR2v2ROPM9h9YQRD5lxIUt4MbN3LAefa69EEW34ZKtrKrwjWJEIrhwm3rlasg2VjT-WQkwFUW-PCkO24lXqvB8JC_SJ4txA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید سنتینل، آثار اصابت حداقل یک موشک به مرکز عملیات ویژۀ سنتکام در اردن را نشان می‌دهند (تصویر سوم نمای با کیفیت این مرکز قبل از اصابت است)
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136342" target="_blank">📅 14:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فایننشال تایمز: ترامپ ممکن است آخر این هفته تعرفه های جدیدی بر ده ها کشور اعمال کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136341" target="_blank">📅 14:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d4790891.mp4?token=MjF1QrE9tusGbDjOhzf2khcJbfwoarrFP-efUxBMI-rbsYVpc8A9TCk6ohkx7sMetMGD1T4UsIUuUZ8j8CCltiBJKBerLji-zxBYXLzJkiwjlGUp4etko1Wviyr62KsWiQVUAznfpHMdL8R4RkpRC5VxzJt6kZM2cra1QT5Re66xUOcfHyiNrSwRKDj7qN4yZea-5KSQloJOaXom3Q02fnyx_1QYVbd6ZmhZkp5sG_CfrlGXPNaqhTnXHBD0cVprCchQas-nn3Zhq6_ZCQkJM5NYZpw022BKS88C3zFPlvUrXf4Yesd01NBO4x-mCL1DlAAd8etP-I9JvG-UWzzWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d4790891.mp4?token=MjF1QrE9tusGbDjOhzf2khcJbfwoarrFP-efUxBMI-rbsYVpc8A9TCk6ohkx7sMetMGD1T4UsIUuUZ8j8CCltiBJKBerLji-zxBYXLzJkiwjlGUp4etko1Wviyr62KsWiQVUAznfpHMdL8R4RkpRC5VxzJt6kZM2cra1QT5Re66xUOcfHyiNrSwRKDj7qN4yZea-5KSQloJOaXom3Q02fnyx_1QYVbd6ZmhZkp5sG_CfrlGXPNaqhTnXHBD0cVprCchQas-nn3Zhq6_ZCQkJM5NYZpw022BKS88C3zFPlvUrXf4Yesd01NBO4x-mCL1DlAAd8etP-I9JvG-UWzzWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بمال بمال در تنگه دار، شمال
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136340" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9CQ4cmDaBYoLXZfXU7pP0zP14kSVTwjoDlOHvbQnROU08OUQg7Sd0X_ULj-P1UYvCqoOZBp0k7zvYocNUzbxTlw-ZQxnPl4RzktnPJN2GTg8kC7nL_AnHGav19CPFPM6CO4nqRL5qZZLPu5yHvvtzKURTzuIRTN5ml2c4Miv7RUCNwJfkaMJ9WxZAutRXfPSiLMk5dUBlWLYuxbSEzf2qTLaYt5y4oQOImKJY4-ayBLt8PQDxrPt5ZfWiHebIUslWZdIlJgStvOS_P6O5UAUKf8rXp9PWgNIGrmYr6Q6FzQJC8XjPKY9HwKp8pihQLTLRabfRjuIIAnvmdcxb5afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای دیگر متعلق به بخش انتقال پزشکی، انتقال سربازان مجروح آمریکایی را از اردن به آلمان تکمیل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136339" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136338" target="_blank">📅 14:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230d24ae4d.mp4?token=T2-cgFFIWMkIH-h2U-sVxyMp9bYxIQUkyNHUiQSVezDDZKPPuq26C-pb2AEzENleUztNoksnKrhVZkMoGoRNXCfoJAfDvL3X640iR1ajmPeRZ--th--tjZYJi3zPQzwSFg_ZvIIhpdX5RrGiUIHgOdTQWIq1LErcKrVJTyhnM7k4n68PJctBpj-HapexLbboxqgqGwpE5Zd8LihDCStb7LsPR9yq71K1j0lMRCJnoyDw20og4MXN1vlkTIUjykFVKMK8Uf7Z3QmkR7GjdNVEpCO7Rkmh9M0M7dhpLXRhwV1QF4qgMu3lU0LkJBUSn8WiEoUshb0fOn2VsQ0by1Ih3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230d24ae4d.mp4?token=T2-cgFFIWMkIH-h2U-sVxyMp9bYxIQUkyNHUiQSVezDDZKPPuq26C-pb2AEzENleUztNoksnKrhVZkMoGoRNXCfoJAfDvL3X640iR1ajmPeRZ--th--tjZYJi3zPQzwSFg_ZvIIhpdX5RrGiUIHgOdTQWIq1LErcKrVJTyhnM7k4n68PJctBpj-HapexLbboxqgqGwpE5Zd8LihDCStb7LsPR9yq71K1j0lMRCJnoyDw20og4MXN1vlkTIUjykFVKMK8Uf7Z3QmkR7GjdNVEpCO7Rkmh9M0M7dhpLXRhwV1QF4qgMu3lU0LkJBUSn8WiEoUshb0fOn2VsQ0by1Ih3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمزه صفوی از توهمات مسئولان کصخول و جنگ طلب
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136337" target="_blank">📅 13:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a820c8571.mp4?token=h1ZV-7C-5S64USaMYZvDGSqr28NZQcBVnoGXdlrDqSsAX0_7g-S2_AYnHqO5OE7JHxVgNzymRJLKsKWAhjxCngnT8vil0sG7wA2bILAeK_0RCcT_q5jm3wWPs-8gafP622SGxx4xhqpISmKjYALdnSzXtbOQeVGabzZWnfWtenXxFvpDSL1P95_ICh-LRXlVtjqjl0RHakbT81fTF8Oh3Gd8gBNsZUH42Zf1QOd0mYemp50K0Gqu-wjLVkiMrjY-4Lck2Cns8amnNhFiGAx8FVSeVGijWDxZWyPuzlrZSeP2QsaW9PfLpl8rEd9bJ7bg2Zkku2aFYQad8t4hd7loWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a820c8571.mp4?token=h1ZV-7C-5S64USaMYZvDGSqr28NZQcBVnoGXdlrDqSsAX0_7g-S2_AYnHqO5OE7JHxVgNzymRJLKsKWAhjxCngnT8vil0sG7wA2bILAeK_0RCcT_q5jm3wWPs-8gafP622SGxx4xhqpISmKjYALdnSzXtbOQeVGabzZWnfWtenXxFvpDSL1P95_ICh-LRXlVtjqjl0RHakbT81fTF8Oh3Gd8gBNsZUH42Zf1QOd0mYemp50K0Gqu-wjLVkiMrjY-4Lck2Cns8amnNhFiGAx8FVSeVGijWDxZWyPuzlrZSeP2QsaW9PfLpl8rEd9bJ7bg2Zkku2aFYQad8t4hd7loWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد اوکراینی مدل FP-2 با برد متوسط، به کامیون‌هایی که در ایستگاه بازرسی چونخار در کریمه صف کشیده بودند، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136336" target="_blank">📅 13:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ آمریکا و ایران در حال ورود به مرحله پیچیده‌تری است
🔴
روزنامه فایننشال تایمز نوشت: جنگ میان ایران و آمریکا وارد مرحله‌ای پیچیده شده است و ترامپ در یک بن‌بست راهبردی گیر کرده است.
🔴
محافل امنیتی آمریکا در تعیین اهداف جنگ متواضع‌تر شده‌اند؛ یعنی به جای صحبت از دستیابی به پیروزی قاطع، بر بازگشایی تنگه هرمز و بازگرداندن محدودیت‌های هسته‌ای به سطح دوران اوباما تمرکز کرده‌اند، ولی حتی در مورد امکان دستیابی به این دو هدف نیز تردید وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136335" target="_blank">📅 13:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پولیتیکو: دموکرات‌ها به دنبال توقف حملات آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136334" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پزشکیان: برخی اظهارات در داخل، دستاوردهای ما در مذاکرات را کم‌اهمیت جلوه می‌دهد و نباید با اظهارنظرهای نسنجیده، زحمات ما نادیده گرفته شود.
🔴
در یادداشت تفاهم، ما بر باز شدن تنگه هرمز به روی صادرات نفت تمرکز کردیم، اما طرف مقابل این موضوع را نقض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136333" target="_blank">📅 13:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / حمله به ارتفاعات خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136332" target="_blank">📅 13:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته
VS.
دانش آموزی که ۰/۷۵ گرفته
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136331" target="_blank">📅 13:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0_4zQofpDfbKKDtVluutA9vXHy1Bwq2OzEligkn1mHU3XHst9Uw82nbqgwUgsVAu6N3PK2k0YMYDWpNSEiY2natRzmzx9W6cqADmhZ0qj1yR7s8SapMQfMV20GYYUa_GOZCOPu69dQxN39uTGeFOJO0K8JDzvNTdQRHaQiikHcwKG4RyR7HIGL0fDtNChJWsILAHr-yLaBbv2ExFH6VTQzE7FIZBLxZkhN_uWJKM5cRxkL3mpdKnEDjAQEBPIbGayC8ez9kdJG_bAc-sraq8jKvNxwMt3UUvjeAlARnRl5_4l06DP2lWAV8Kd2Lq5VlW98vqDThM4KlYkKCWwl3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنین مشاهده شده است که یک عملیات نظارتی و جاسوسی مستمر توسط آمریکا، که از عربستان سعودی آغاز شده، به سمت قطر در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136330" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkG6apNAVkgLfFIk25W50Sfy-8_IvVgA3p4WwppAm0I_2qWefKlNGRjmUG-i5O-CNLnQshU-oM4f0uo9bhHx2m-IQHVZCrFk1XU2PE8VpTLeTkMPfdQmZXl4akqiai02P9imH51lbH5hfcednMSBTEUUq6FIszihRrWsy7L9Vbg2RcSHftZsrEFJl7ueFozYOd_9WWTQyoI76THnAdQ3hzoReccLtaTTKeSrTxr3Z_g04IUgBHCmvyvD3jfOli9qnZA5pCosIlY5qM6t3nZP1y2M7AOQZq8neHjzyn7tNP9uiaSLCV1aGCs2SJWCta2vbXZ5E5qllRn_1vwrEWqD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد یک پهباد جاسوسی آمریکایی در آسمان قطر، در نزدیکی سواحل ایران، مورد هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136329" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
