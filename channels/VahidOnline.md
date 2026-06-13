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
<img src="https://cdn1.telesco.pe/file/E7N8iuOqWGNJtTn6I59n-K7GrUM11JqSNjvV8Yti4YI0iGJdGY8OoxWS1s3WUlC_F_j8xDy4MTodyPnjLLYFrBgo3o649vCouY8es6PAWYtBq05K7T0y_lA8A6rZUyWVZAZiztOIluwzLSTCmFKzbUs1CMKiGq2LT9Svcn13GS5GDNLiuOYaDDp8AAPG5dCILuQhbyWWt9PWcvFGZVmIgOa7avZ06y1c-nV6Wpa7iZIhWstFtLINQ_UxxNNdxDQ6UlxzDmqjIz4TP4iKqZSBu6Fgd36_S297oyviydZNWbGG2KaRtcUDEKxy03cDjq8XvyFMB0ty45N3fpEZsRca9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loM5VVjC894aqLbBnw35VywgiZQ_-yiNa_XLFoi5xyDmZOSb7hYK_9RpJdvXtj_XPD6QrsfukfTrcYf175zstjPU4ZOlD7aCqd38s5WVptG6G6FEAzEvhivnbiD6UlsLaBre8Vgl842KH84mIyNqReKQb2iPpgQmUrIaira1COEKuaAC-r_fENs2glSrxpVedao2OrJo7ueeMYKLIprdRpPfZ7RqKm59P13HVx7Q1IwGYOLIqdRdCDu2Hk1ANcLGzKjwP-RcJNH6clDfLD-Zyw8efIh_GRCFPn-K2PrMITle5Ho7kFD1YJi2G6JGfb6VgtJpn6HOyreRNgwruG69Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگوی با «فاکس‌نیوز» اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته یا روز دوشنبه نهایی شود».
بسنت با اشاره به اینکه تصمیمات دونالد ترامپ برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، هزینه‌ها و فشارهای کوتاه‌مدتی را به بازار سوخت و اقتصاد خانواده‌های آمریکایی وارد کرد، افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
وزیر خزانه‌داری آمریکا با تاکید بر اینکه زیرساخت‌های اقتصادی کشور در حال حاضر بسیار قدرتمند عمل می‌کنند و بازار انرژی به خوبی تامین شده است، خاطرنشان کرد که با حل‌وفصل این مناقشه و مهار تورم، بهای جهانی نفت حدود ۲۵ تا ۳۰ درصد و قیمت بنزین در بازار داخلی بیش از ۱۰ درصد از اوج خود کاهش یافته و روند نزولی قیمت‌ها و کاهش هزینه‌های زندگی مردم با قدرت ادامه خواهد یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/76289" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEPoQtyBSfkAn3apXD4uEQvvCCq6HCZFjnBgLZIgadlEBAtmH16fCcqZfrPAIPSWXvIHeEDfAjGhUodKPTEA-P9VQG_SPyCdTLvgqICZGxBiVwWP1GcBPZc4jPM2OWoHi2K0G8C8CewIQkCnUZ20aMSZyFLNJVDqpLLtCFHZzvWBNn9xezP8YZElaAOwcf-MATX7O2vS1v28ln9jGoxD3OxG6OxGrFZo_tUJrDqeonoEUzslf4kj_B2itK9AD9JL9CpcERXJU4VhNNvmO_0d7AQTOt7aHhcDlCbQlXFzmBYObmdxYv3QP8ZCyNhrmUluAZuwv9neInkkgb7WRso03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
فرماندهی مرکزی ارتش آمریکا (سنتکام) اعلام کرد که ایران چند پهپاد انتحاری را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورده است.
سنتکام در شبکه ایکس نوشت که نیروهای آمریکایی در ساعات اخیر همه این پهپادها را سرنگون کرده‌اند و تردد کشتی‌ها در تنگه هرمز بدون اختلال ادامه دارد.
در این پیام آمده است: «ایران چند پهپاد انتحاری را در تلاش برای هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند و جریان تردد در تنگه بدون مانع ادامه دارد. این گذرگاه مهم تجارت بین‌المللی همچنان برای عبور و مرور باز است.»
پیش‌تر نیز یک منبع آگاه به رویترز گفته بود نیروهای آمریکایی چند پهپاد ایرانی را که به سمت تنگه هرمز در حرکت بودند سرنگون کرده‌اند. این منبع گفته بود پهپادها تهدیدی برای کشتیرانی تجاری به شمار می‌رفتند.
این رویداد در حالی است که تهران و واشنگتن همزمان از پیشرفت در مذاکرات برای دستیابی به توافقی جهت پایان دادن به درگیری‌ها سخن می‌گویند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/VahidOnline/76288" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQPhbvXylbhuM7pOUVJ1Yc_5XgXznNaNQ4qYmif17eGhF35eomrqTS6W7JbDzb0A19KD41nJOEao8dLEaSlY7TeYeOY3JejRRZTO1Hvk143vXzOprphs9y4N0QhjQmUcGTHcLjQNZwdOWIto09I-ghv9183kkJ1pc4Xc1tt7ZL8BCSkxvnW3IjpaepUhc-jXWET35tU0biEXBnP9jgM_q0NcHiHPzuIEVjtuPtsSJ1ve2YN48aLY_FgSHA0eRNlcRpzxQPBjMvfREWjYBlWHRYYJMfqGREgA2xUIf8SZ9PFQdoZaxNDXRFscKi61BPJVIQxAyri2n60MTLTZrp8peA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی گزارش‌های منتشرشده در برخی رسانه‌های بین‌المللی درباره انتقال یا آزادسازی منابع مالی برای ایران را قاطعانه تکذیب کرد.
این وزارتخانه در بیانیه‌ای در شبکه اجتماعی ایکس اعلام کرد که ادعاهای مطرح‌شده درباره انتقال مبالغ مالی از امارات به جمهوری اسلامی ایران، از جمله گزارش‌هایی درباره انتقال ۳ میلیارد دلار، «نادرست» است و هیچ مبنای واقعی ندارد.
پیشتر
رویترز به نقل از چهار منبع آگاه گزارش داد که امارات متحده عربی با آزادسازی میلیاردها دلار برای ایران موافقت کرده و بخشی از این منابع مالی نیز در اختیار تهران قرار گرفته است.
اما وزارت خارجه امارات تاکید کرد که هیچ‌گونه دارایی یا منابع مالی ایران از طریق این کشور آزاد یا منتقل نشده است.
@
VahidOnline
بیانیه امارات، ترجمه ماشین:
امارات متحده عربی گزارش‌هایی را که از سوی برخی رسانه‌های بین‌المللی منتشر شده و مدعی انتقال پول از امارات به جمهوری اسلامی ایران هستند، از جمله ادعاهایی درباره مبلغ ۳ میلیارد دلار، قاطعانه تکذیب کرده است.
وزارت امور خارجه در بیانیه‌ای تأکید کرد که این ادعاها کاملاً نادرست و بی‌اساس هستند و تصریح کرد که هیچ‌گونه دارایی مسدودشده ایران از طریق امارات آزاد، منتقل یا تسهیل نشده است.
این وزارتخانه همچنین از رسانه‌ها خواست دقت را رعایت کنند، به منابع رسمی اتکا کنند و از انتشار یا بازنشر اطلاعات تأییدنشده و ادعاهای بی‌اساس خودداری کنند.
mofauae
درباره این خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76287" target="_blank">📅 01:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bw5FZ6DUUpaxemsWhUJHOoSnP4K8vSSopYL3xhyeFz0D35ZCcG2leFNInfV1utoRg_tQOAQzYn6gw-CcE457PWdmWk__FZP-1aDgNjDadhIE6ocFJjtW4h_fhMPShHFxXiajmLx2WBe2ppq2cLgNcy9cUxnjszcJaP_1RvyX4LuRD_cT8EoOrP9DyrImLLkd-FT4iFk69SC15PRSEFxcMHk887sI_8dzoNcWHuATRYx6sT7wIfKhftqU_3jv1mb_Ga35GMi2Hg69KvZnRSUkPUash7fCupZQ6m8e1kMl8wSCZgOS_YI24WLqpRLq-yXuWdrO3gWt0JzfA0x-FOBKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UGZa3jn13GtyMpQxQaOsKQ8_lAryssasK5arXG3-7HohVOMkHL8cyH_3_a4MKfAxUCd_gm21uNkC-RvJIJRReyqFD81cq5MIwJbQTspKG4ze8P-Izh_jb-nnfhxxzAtCDM0ZoyG8InIrGeR45t5BL4qLGsK-EkR59GALVaWbILWWyVkc3ke5Sq82HFUpUctTgMmZvF_Psc2I4vmCZevubthDIRP9QMW_jhiBApsLk3j_cWDW3NPZ6lJUwS558u5lkfgaA0JWldfrNYrVG0CXY87HyyMjQPkmxOIw1iydFo5uwq4ovp04JWMMXowRNKqmT_SSv780DFuT1V47l1cnaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مالک شریعتی نیاسر، دیگر عضو مجلس شورای اسلامی نوشته:
خب وقتی در باز بشه و ببینن که می‌فهمن مویوم...
malekshariati
این طور برداشت شده که داره میگه قالیباف پشت همه تصمیماتی است که به اسم مجتبی اعلام میشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76285" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClGxLxZJyjoMZaeTXEBwXuKeCx9J9vS4I7jKUKApCTkiHKdu2_OO5-tlFcI0R69P7m3Xjx5uGbzN9JWqNO48npcl7r30MeSv0RUc8qoB80XrzkfrslyeA5ABdjHD98sBLCzWdU8cn9Strps-53QDMH0luNxirPql-NLr-FJpgQ0x8uzS5N3v5CRu3t8FdjDAerBUgIpe9tCWWARAk8kAKKPpn_VgnAmsheEM81EUVbCoe1RAVXfOUGoJC1OJpOCNjw7YC_GeiNYxpnEZt-oaACQpxiFsbBrOCdZ_98Vz-wPm7Z6TN5O2A-uBhhHfUpc17a_aNPts3b39XIbLqkW4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم:
استانداری هرمزگان: صدای انفجار در حوالی بندر سیریک ناشی از شلیک هشدار در تنگه هرمز است
خبرگزاری فارس:
شلیک هشدار به کشتی‌های متخلف در تنگۀ هرمز
دقایقی پیش مردم در قشم، جاسک و سیریک در استان هرمزگان شنیدن صدایی شبیه انفجار گزارش کردند؛ گزارشی از اصابت در این نقاط مخابره نشده است.
به گزارش خبرگزاری فارس از بندرعباس، منابع محلی از شنیده شدن صدای انفجار در سه نقطه از هرمزگان خبر می‌دهند.
دقایقی پیش اهالی مسن قشم، مناطقی از سیریک و همینطور جاسک از شنیده شدن صدای انفجارهایی خبر می‌دهند.
بررسی‌های خبرنگار فارس از منابع آگاه حاکی است صداهای شنیده شده مربوط به انجام شلیک هشدار به کشتی‌های متخلف در محدوده تنگه هرمز است.
منابع استانی نیز وقوع انفجار بر اثر اصابت در این ۳ نقطه را رد می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76284" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0mUVcv9wKkHFrHBKJ9fQwzrPkXFHg-YWASRWnn4Esj24xX2T43WTeknIv1ufgXtHc2vLG5TfiUQ-1VBPZxZ7IE6Jmcj9md0AccUBXqrsWvFEZBjDeyhKfYpsRixTkDXmh3BL_dBKYAIbp-7eXm4_hODR--nHsejjcjXVJJTRckWNXqsEMrQsij6vK9z5X52s7N6piWhXf3ZWFw8Cv6YGF1ItShntHjZ3-Wm4OdeVPvXwPfZpnI_ZiMGA3Dh0kU3JhQKKWie-rX5Agnd-6PbhDbE2a5QqFq-_Ip4XXRt_qvW4TE9flrn7RZBMVYPjE3V_p1cXJsJxZo-ibx5Lh0Nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره تفاهم با آمریکا به صداوسیما گفت: «احتمالا در چند روز آینده تفاهم‌نامه میان ما و آمریکا امضا خواهد شد.»
او افزود: «امضای یادداشت تفاهم بعد از گذشتن از آخرین مراحل مذاکرات به صورت دیجیتالی و از راه دور انجام می‌شود که اعلام خواهد شد.»
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، شامگاه جمعه در یک برنامه زنده تلویزیونی اعلام کرد هنوز توافقی با آمریکا امضا نشده و مدعی شد که پرونده هسته‌ای ایران به مرحله دوم و نهایی این توافق موکول شده است.
او در گفت‌وگو با تلویزیون حکومتی ایران گفت توافق احتمالی با ایالات متحده شامل دو مرحله است و «موضوع هسته‌ای را به مرحله دوم انتقال دادیم».
این در حالی است که ساعتی قبل یک مقام ارشد آمریکایی به خبرنگاران گفت بر اساس توافق، قرار است اورانیوم غنی‌شده ایران در خاک این کشور نابود شود و سپس به خارج از ایران منتقل شود.
با این حال وزیر خارجه جمهوری اسلامی با اشاره به اینکه نتیجه مذاکرات یک «یادداشت ۱۴ ماده‌ای» است اعلام کرد مفاد آن بعد از نهایی شدن اعلام می‌شود.
وزیر خارجه ایران در گفت‌وگوی خود خبر داد که طبق تصمیم جمهوری اسلامی، «آینده تنگه هرمز و اداره آن مثل گذشته نخواهد بود‌» و ادعا کرد که ایران و عمان بیانیه مشترکی در مورد اداره این آبراه منتشر خواهند کرد.
او در ادامه اذعان کرد که طبق قوانین بین‌الملل گرفتن عوارض از کشتی‌ها در تنگه هرمز امکان‌پذیر نیست و افزود: «اما هزینه خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد.»
عراقچی اعلام کرد طبق توافق، محاصره دریایی ایالات متحده علیه بنادر ایرانی به‌طور کامل رفع خواهد شد و دارایی‌های بلوکه‌شدهٔ ایران آزاد خواهد شد.
مقام‌های آمریکایی آزاد شدن این دارایی‌ها را به دفعات رد کرده‌اند. جی‌دی ونس، معاون رئیس‌جمهور آمریکا ساعاتی پیش تصریح کرد بعد از امضای توافق، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76283" target="_blank">📅 23:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVBauF_uk6JJIaoXPMLOr_4OCabBjahBs1nvp3WwdXfVOC3aqTG0ZELkNW3tr5cnjgkuSguAuO2p5VM3tAlfkjSR6yfEeGZFBCtFxZ3ZXSiDyHsLPADtY5AUNuGCGqfpgdTslxUv1LLgErm20ElTIpGpITZdqxmXEyNxplm26JKYomDgNS3TrUfowyewefB2UcrIVv0eVgpzCOFodjSYBRmFuFt9fbukwnAcesgE-xjcG8PZkbq5llraj_-qvbdycLFrVCw_wDaAig-lZtjOe_yl46wzRbvcNvRvLnLC9nZMDEErnKMnp2jwWdu1RwM_0HzqZYkuxIGtyBat8pvRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
تعهداتی که داده می‌شوند باید عملی شوند؛ نه اما و اگری، نه عذر و بهانه‌ای. برای توافق نهاییِ پیشِ رو، راه دیگری وجود ندارد.
هرچه بکاری، همان را درو می‌کنی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76282" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCCHACnQx4k2B8wN6VyaUdPGaBhy969vkOKda_8keLMnZnOl0GOLEs6aNmORPo5jlhNioXEbszniAdV0QaD1lgTi2rs5GSgNCsI9SIUabAypXSXPnS_U8rWQxYhXGxPSYw4Y0GjbxcPVZmNBQI1WdrK1het0MBibK0yOYo8f3wScsJb7elAEagCObpUk90unR9joo9YVZls-1nV10tLzmtTsdW6fJ4GWj9HIuyZQvq1fsl6S_6s6OYQGw3D6rw_dU_j1zRR9lzRnaScRDnKMM9l3tZSojHotZOufbvULpSCjEH-RZSM349hayEk-3xl5v6y6jIvvMFSaLqkBYS4_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار منبع آگاه به رویترز اعلام کردند که امارات متحده عربی با آزادسازی میلیاردها دلار برای حکومت ایران موافقت کرده است.
رویترز نوشت که این اقدام نشان‌دهنده تغییر تاکتیکی ابوظبی پس از هفته‌ها حملات حکومت ایران به این کشور ثروتمند عربی خلیج فارس در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی است.
دو منبع منطقه‌ای به رویترز گفتند که امارات با آزادسازی مجموعا ۱۰ میلیارد دلار موافقت کرده است که
بیش از ۳ میلیارد دلار آن تاکنون پرداخت شده است.
دو منبع دیگر که از این توافق آگاهی دارند، مجموع مبالغ مورد نظر را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات حکومت ایران به امارات متحده عربی مورد توافق قرار گرفته است.
یکی از این منابع نیز گفت که نخستین بخش به ارزش ۳ میلیارد دلار تاکنون در اختیار حکومت ایران قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76281" target="_blank">📅 22:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sI585Om7DBVbZdihlFA2EXlCYE-tRTMarUAdufgRjDRBivMetye2lJj_5lsoGyupXvur4vwUb110xYICI_3U_MB7IRXmM5qnDgNWbj1zhCdzC0Gt0wPVcnrOJZOW0cJr68zDSYoMPIjJMlKBrXJUDAqYvMGcSKOaOv2kZ1cNioIsHrGaMW3nkaTRFYqJJWDYZ8CWBC_Gpaz3d5BtM5tf3KdsGwU51u4Ny26zrfvOznYwEiBid71XeNicCjZb9C5p2Uf_fKZ6wyTnJ0CqU4NZkLFC_Xz1wWNnvkMwZywoNy-6OT5KgwvvrKLYQvPxKSBYA7U3SlCId0ufnQICmfFiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در انتقاد از
توییت عراقچی
نوشته:
عراقچی نه‌تنها مستقیماً ادعای ترامپ درباره «جعلی بودن» مفاد منتشرشده را رد نکرد، بلکه با درخواست از رسانه‌ها برای پرهیز از گمانه‌زنی، عملاً فضایی ایجاد کرد که می‌توان آن را تأیید غیرمستقیم نادرست بودن برخی اخبار تلقی کرد.
آیا موضع‌گیری او نوعی عقب‌نشینی یا هماهنگی با روایت ترامپ است؟ در شرایطی که ترامپ مدعی عذرخواهی خصوصی ایران شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76280" target="_blank">📅 21:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9zrheW7FQ4ZbtyNSEvxm-KDZXIAPYlN3S3AbUptz0h-Fs7ljZJIsKQKDtBDj_I7amSpKsM82kvFvnQRDbfkx11IkBcG-b08mxnCaPoubgyQ4DZpv0X0-LzCWL7wyjl9uLx3Yn6XPSMNDnDgVzuISAEXmu8PJ38lN7aLEP5gkMTBEAxkSA647dGKj4_3eu24ttd5nmNAfpREg8kgYlk18hkOmds-47ESVJLXAt8vX61otrNWS_u9fS9BE54iBmcu_NQJCax579OmarHvSphfHUomRygBjeye6KGF3cJ0x4i2TnaJNU0I3ND8_0xKU-k3okLUQ8a9nDhks1NKA9phcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز جمعه در گفت‌وگو با خبرنگاران با اشاره به این که واشنگتن انتظار دارد توافق با ایران در روزهای آینده امضا شود، گفت یکی از مفاد آن نابودی و خروج ذخایر اورانیوم غنی‌شده ایران است.
این مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، اظهار داشت: «تیم مذاکره‌کننده ما را در موقعیت بسیار خوبی قرار داده است، اما باید ببینیم چه پیش می‌آید. هنوز کاملاً به خط پایان نرسیده‌ایم، ولی بسیار به آن نزدیک هستیم.»
او گفت که مفاد مورد توافق، اهداف اصلی دونالد ترامپ، رئیس‌جمهور آمریکا، را محقق می‌کند و «در پایان، وضعیت را در جایگاهی بسیار بسیار مطلوب قرار می‌دهد.»
این مقام افزود که مفاد آنچه «یادداشت تفاهم» نامیده می‌شود، شامل بازگشایی تنگه هرمز و لغو محاصره آمریکا علیه بنادر ایران است.
به گفته او، ذخایر اورانیوم با غنای بالای ایران نیز در محل نابود شده و سپس از ایران خارج خواهد شد.
این مقام افزود که مفاد توافق همچنین شامل یک رژیم بازرسی است تا اطمینان حاصل شود که اجرای آن در بلندمدت قابل راستی‌آزمایی و الزام‌آور خواهد بود.
@
VahidHeadline
پست‌های خبرنگار نیوزنیشن در کاخ سفید،
ترجمه ماشین:
🚨
اکنون یک مقام ارشد دولت ترامپ جزئیات بیشتری درباره توافق پیشنهادی با ایران ارائه می‌کند.
آن‌ها انتظار دارند این توافق طی «چند روز آینده» امضا شود.
صددرصد قطعی نیست، اما احتمالاً ۸۰ تا ۸۵ درصد احتمال دارد که طی چند روز آینده امضا شود.
این توافق «اهداف اصلی»‌ای را که رئیس‌جمهور برای این مأموریت تعیین کرده بود محقق می‌کند.
نخست، تنگه را بازگشایی می‌کند و محاصره را برمی‌دارد.
🔻
برچیدن برنامه هسته‌ای ایران.
دریافت مواد غنی‌شده توسط آمریکا: هم در محل نابود می‌شود و هم از کشور خارج می‌شود.
ایرانی‌ها دیگر خشونت در منطقه را تأمین مالی نخواهند کرد.
یک نظام بازرسی که اطمینان دهد این یک تعهد بلندمدت و قابل اجرای بلندمدت است.
🔻
پرسش درباره «حجم دارایی‌هایی که در صورت پایبندی ایران آزاد خواهد شد».
به گفته مقام ارشد دولت: وقتی ایرانی‌ها «به تعهدات خود عمل کنند، می‌توانند در ازای این عملکرد، امتیازاتی دریافت کنند.»
🔻
پرسش دوم: چه چیزی تغییر کرده؟ چه چیزی باعث شده این توافق نسبت به قبل ملموس‌تر باشد؟
-«ما به مرحله‌ای رسیده‌ایم که متن را به جایی رسانده‌ایم که از آن احساس خوبی داریم.»
-«ما متن یک یادداشت تفاهم را داریم که فکر می‌کنیم هر دو طرف نسبت به آن احساس خوبی دارند.»
-«ما احساس می‌کنیم کنترل ایرانی‌ها بر تنگه هرمز تضعیف شده است.»
🔻
مقام ارشد دولت: «چه تضمینی داریم که ایرانی‌ها به سهم خود از توافق پایبند بمانند؟ ما هیچ امتیازی نمی‌دهیم مگر اینکه آن‌ها به سهم خود از توافق پایبند بمانند.»
این مقام ارشد دولت درباره یادداشت تفاهم با ایران می‌گوید: «متن را به نقطه‌ای رسانده‌ایم که هر دو طرف آن را می‌پسندیم.»
به گفته مقام ارشد دولت، اگر آن‌ها بتوانند به آن پایبند بمانند، می‌توانند ظرف «چند روز آینده» به توافق برسند.
مذاکرات فنی ۶۰ روز طول خواهد کشید.
آیا رهبر عالی ایران این توافق را، به شکلی که شما شرح دادید، تأیید کرده است؟
مقام ارشد دولت می‌گوید: «افراد در طرف غیرنظامی و نظامی... شهادت داده‌اند/اطمینان داده‌اند که رهبر عالی از جایگاه فعلی آن‌ها در مذاکرات رضایت دارد.»
KellieMeyerNews
مقام ارشد دولت به من می‌گوید که در ۲۴ ساعت گذشته، همه از ونس گرفته تا ویتکاف و کوشنر و ترامپ، به‌همراه هگست، روبیو، وایلز و رتکلیف، در مذاکرات مربوط به ایران دخیل بوده‌اند.
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76279" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nRnOi0LjWvKgqVKuIoniOGcst16lwC8jU7sCMfIfbRjONt2JqulmBAEb8A6OLrvl63mb4w7UNDJ8dCQg7Xr35VbWB1dBBS4R5FrZiAVtYKII6RLxQuRaEgSfvJJZ1Lxd6JzL44W_hhJuN0nOiW63hhQoecC9yAbMC4x0bq_RcZKCDjemDS-cDT3ksTt22zZQMvV2OlvihpdjvFrHmilhF4DEE1gR7wNPKgS81Asy0QYe537nPimxixl60RHRBN4Nw3C19kDAZheDbE0Mhaza9MMviVFY-RTxmNQVQgH5J8BfFmMEhbEE-Nycu5PEAAj7AnpHHMEagZSLP2fIacCwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QN04i1mP5bRSWpImYiQY_3eCCkzTozOvhS4Gv04lxPt7s86T0yuKYFI9KCTLxgOkd0xxUEYYuhjr2yJjxz4vG41OY5icoCEnPhFc82ycDyOFxjHV9p9jAJ03LBdFSzlZx4Fpq6_Lgxgu13qY5wDUB344xCdPkd0eWjmCF-M7X_Hm1TpfYrN4IG_gfvDTsxU0IUqRnf6erccPg54wrJirW815fMrWjflfRBAAq5_kOUrrCV1YLUsp28AhHFVyFOvalR4vaRDAFuuYYfOPqlBnjyVe5DAfcxIyUtUTuk95pJCN_O1nlAeWW04rPN_4ElcZeiSzgRMaRmj5ix7tYMts9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسرائیل کاتز، وزیر امور خارجه اسرائیل، روز جمعه ۲۲ خرداد، با انتشار پیامی در شبکه اجتماعی ایکس اعلام کرد که هرچند رئیس‌جمهوری آمریکا بر اساس منافع واشنگتن و هدف مشترک با تل‌آویو، یعنی جلوگیری از دستیابی ایران به سلاح هسته‌ای، به سمت یک توافق حرکت می‌کند، اما اسرائیل انتظارات فراتری دارد. کاتز تاکید کرد: «از رئیس‌جمهوری آمریکا انتظار داریم این اصل و شروط دیگر در حوزه موشکی و گروه‌های نیابتی را حفظ کند».
او با اشاره به اینکه ضربات سنگین مشترک، توانمندی‌های ایران را سال‌ها به عقب رانده است، افزود: «اسرائیل باید تضمین کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از هسته‌ای شدن ایران را دارد؛ به همین منظور، من و بنیامین نتانیاهو به ارتش دستور آمادگی لازم را داده‌ایم.»
وزیر خارجه اسرائیل همچنین به عنوان درس اصلی از وقایع ۷ اکتبر تصریح کرد که این کشور به هیچ وجه از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نخواهد کرد و ارتش به دفاع از مرزها در برابر تهدیدات جهادی از بلندی‌های حرمون تا عمق غزه ادامه می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76277" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OxatahxcP2oxvEYdI5Dfilq-1bF3YUzQx2Hv3dqUdPFgBl-9LFb8-g-UGIUeiDEMNoxrpRSgkg6qXBPvy2Fl-aGWXtLziIxUEMBH89zHVyOv5Nr2TznSjFeumRs9bK1yn_rP_IDxosndA51C6g892bIl19IoHQOdepS5EWWjXn4gWYDHs3j-CU08SeuD81Av5og2eAIKf1Yj1rmL_bRDkCvyUGntPn3j5_PcCk_KW1bW6G8sXrsK9RrnhpyaNQ7NiPMEExeWklyYQiNtM6me1anQ3Vtutp_K-k7WJnjpNRSSpMqCwZOrj1nMIbvqkpllmGYmG1RKdw3zEAhjfgWi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/soWwnRc9qvt_Qizg5f2qSvYZfeeYGTEPr9VsDiHmPOReSSe3mQnA7Q-1Ehe1TPJaCCjQeD9HrEdlLORIttfyU5-4Aqe-F6M_FKbL50P50G8xObMrpe0leWstEN6atgWdFqZaCh6-NjxXL7M8dhIJq-yGOMP4FtF6GSoGi-T30bF3-wiRbDiaWQUykuqIqiIdQNalMvE2_zejHE-p7MwVdppFfScbRlNUydP2so_ZADbPy8iicmKZksZNkwK4RRJ5fSSRSkJgPoran6jL8QGuOvTLjRDE6OiSHXD8AOOtFnlZ63YUMuS5ZyEkAp-GpcRuZ4Lz54bQAUtvpkuFyPcEiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس شورای اسلامی، در ایکس نوشت: با مشاهده‌ی متن توافق باید اعلام کنم، نسبت به دو نسخه‌ی قبلی، خسارت بارتر و عقب‌نشینی‌های ایران نیز بیشتر شده است.
@
VahidOOnLine
نبویان سپس در توییت دیگری با اسکرین‌شات پست ترامپ درباره توییت عراقچی نوشت:
توافقی که با پخت و پز بانیان توافق ننگین برجام باشد، حتما
#خسارت_محض
است
nabaviantwt
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76275" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPBPFBI4Oaw247qqoJuIHRZVcI9ehKoRN9vKHBNBGK2cF1gpVTL4nEokvcDyCc1uruvu4kHdYfGVKrHuIjE2Sn1grwpvKodFRCLzYKZr1oprBNgbijwH-kJrs7vi5Z7gS24PUAq5pjHXYbrAyjz95hGCKk4u2M5GANwOz7TM63a4G6S6rIytTwbFttBEIolDa2H1xQ3zdcic_gGN6cqs3grxZLIcANCNuHrANns_5Yb2KlEnuug356aNckjHKdtJgBG9fpyoyW3jTJB4euU5eJjeiLUqefB_SNfR1c1Kc0ryBeFcXKY3EY_crmHXpurCxgSx9V3oBZsRlVPSSbDIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.
سی‌ان‌ان به نقل از مقام ارشد دولت ترامپ افزود که جمهوری اسلامی با «برچیدن برنامه هسته‌ای، نابودی و خروج مواد هسته‌ای، آزاد نشدن دارایی‌ها تا زمان اجرای تعهدات، باز ماندن تنگه هرمز و توقف حمایت مالی از گروه‌های تروریستی» موافقت کرده است.
مقام ارشد دولت ترامپ گفت مقام‌های جمهوری اسلامی پیش‌تر گفته بودند بدون آزادسازی دارایی‌ها توافقی را امضا نخواهند کرد و بارها از گفت‌وگو درباره حمایت مالی از گروه‌های تروریستی خودداری کرده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76274" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/II_H72jltUoNKUZYcFw6YRRhLzOCnEZ1WAEU0G5ol91GyuH6GorYLq6wxP4KZSp7JOB0lhQjCUJu_vM6It-K-vPK8j1cyXaUlccYh_3LN_jIYkDKLktu9JElKaakks_HtDgSVely_oPDWKkHASn8U4BBpNP7RXQcL4trTHOOfhwaYnYqSDBj_JTvS0O0Sm7OhXTWcyrAIs7ra4vsEdHT1sgbIsqP1YnU_qDC28g5VgxcI5v6IDOad7d_47DwJr1hKNQT5tRMl8kRc8QqsBQ1krAkvYjM6tGOq0uAFsBbp0U0EpTiQD56odIJuMPp-NRNmDNC4ocqNpCTOJc13JZqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس گزارش داد دونالد ترامپ،
پیام عباس عراقچی در شبکه ایکس
را «بسیار مثبت» ارزیابی کرد و گفت معتقد است توافق با جمهوری اسلامی می‌تواند در آخر هفته یا روز دوشنبه امضا شود.
اکسیوس همچنین به نقل از ترامپ نوشت که جمهوری اسلامی به صورت خصوصی بابت انتشار «اطلاعات نادرست» عذرخواهی کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76273" target="_blank">📅 20:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PW2WtP3yRCfvWR6cXpqhtjsdk1GyMM2sTZXmzBC__AFhjrQH9wR3pkJ2AkTWw0CmO38U6LkZFfuez56lya5fFuQRhDZrQTR7ai2uJyyFF3hqyCYZULEIkzwmvJwJY7XLkrOhcOJokQeh79_pz2_boPC346aqV7tCzEtDQiJsXPmdTl5qjuE-v1B_3sbQ7ZQGEVDrmUWduF9DT7cEQdp5xYlQBvgIVKkM2ssw6CwyQLDZ-5zpMvbEgrnT99UNGkJgYj2Cyc-IKGzSffTnHJR9MlZaCZ_tQXtpDIljn1qTWTiY595NvwobM9qUhIBQq50q4PFttEJdKWfbDoVMHUjwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرحسین ثابتی، عضو مجلس شورای اسلامی، نوشته:
طبق اطلاعات به دست آمده متن توافق احتمالی بدتر از برجام است/ چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد
دوشنبه شب در تجمع مردم در میدان مجتهدی طرشت حاضر شدم و توضیح دادم که دشمن به دنبال نابودی ایران است، چه از طریق جنگ و چه از طریق مذاکره و کسانی که هنوز هدف دشمن را نفهمیده و فکر میکنند با توافق با امریکا میشود دشمن را سرجایش نشاند، بدیهیات اتفاقات اخیر را هم نفهمیده‌اند.
سپس گفتم طبق اطلاعاتی که تا این لحظه از متن توافق احتمالی به دست آورده‌ایم توافقی ضعیف‌تر از برجام در راه است که خطوط قرمز رهبری در آن رعایت نشده و نه باعث گشایش اقتصادی میشود و نه امنیت کشور را تامین میکند.
در پایان نیز تبیین کردم که اگر بخواهیم امنیت مان را حفظ کنیم باید بیشتر از همیشه آماده جنگ باشیم وگرنه با ژست مذاکره و گفتگو و تن دادن به توافق به هر قیمت امنیت کشور نیز در دراز مدت مخدوش خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76272" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_GZXoHzQGK3MQQmPql2uH3V07oHoDY9sbBHjb0lDOXWoUBLEpxQAjxZ5LnT2mwfLZeIufM2a3i6aC3kgU8LkRbsEP7SwPh-rdU5kpnugtP-ggQ7njJklYKWBAtcTF6Olp6X236jo_I1nm26ZsBr6l22mnCzqDcjP0oGmvQNJhLDAt5AkhvxcHMto9LyYml28c3EJo_PbuPKC7rpvPinHZ8RdqY92UYFbwQ2F7qRu6HwSTNJt0vSvnnOHrDNa2qaSqNBCz13z7QLl6bXP20IwwL47WlB1s1JneBpLiexqqjkKgZIw7QCxNpKSyrhiGEDElozDC5V4RKkruvqTtPBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان در پستی در ایکس نوشته است «در میانه تلاش‌های فشرده میانجی‌گرانه پاکستان، ما کاملاً از کارزار بی‌وقفه انتشار اطلاعات نادرست که از سوی طرف‌هایی که با هدف خراب کردن توافق صلح انجام می‌شود، آگاهیم. با کنار گذاشتن این حاشیه‌ها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق حاصل شده است و پاکستان اکنون به‌طور نزدیک با هر دو طرف برای نهایی‌سازی مراحل بعدی همکاری می‌کند.»
او نوشته است:«صلح هرگز تا این حد نزدیک نبوده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76271" target="_blank">📅 20:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dwyOCuKEtL186EgrfeOTu2HKAxmMtHmuMvxSd2AcAAS8sspfz5b-YnMU4rFbiHZkE0irXI53DE6uCcgIKSwWLx0sxEv5jGu4DiKWmR3A1tB6Z-D2-BvQ93AZQqA57Eo69QMtATTC7x80935njdh__jwGT2sYGWoMUHBy7QbuXsXougDHOtfjrVOB7DYaaZXxQx_ctuzYwNoZCo1R9-nQtQ9K75MHUealBqYna2mtNvFTce4TLuqHQJhG6B_MTNZZOqQf3jv977ed6z0NCI0ezjJQISA6v5N0RukVCv-0y_mO9E2PUHpltQHJ3wQbKHxQmrkt23PCVQByWvJlrxw68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اسکرین‌شاتی از
این توییت عراقچی
رو پست کرد:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76270" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KS4MdsPm-XJEnOR_RTT0SmJzx0ACUlnOHYBUwoEEU6N6F-4ZjlEES6fI_M6GptUQFbKjM5V9SXbDD5BInIF9ej4EqfOi3OmxGFUBMMkLAhPLZ4Yp-UegtBM5pKwFZvQTfDg6bU3GpayrbLH8K-6wRdFOlxHlmwqnRmFlIROc4d3Bixxlsti4RqzdSCJcHEbvUB5pThE7nha1cU-EaSP8GQYNRHNWaUEXyK0acRJo2CkFQMVyPqV7DKm8CoQ80kB2dRvC0cX7vsTKxj69F9itZhcXNT52pLo_KijWpZZ6XNEBRL03tBaSTel6V23PSMlYbMQ7PW9PqvJiaQchUzHFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه واشینگتن‌پست در گزارشی خبر داد که قطر در جریان جنگ ایران مذاکراتی پنهانی با جمهوری اسلامی انجام داده تا تاسیسات گازی خود را از حملات تهران در امان نگه دارد.
قطر در واکنش، این گزارش را تکذیب و واشینگتن‌پست را به تلاش برای آسیب زدن به نقش میانجی‌گرانه دوحه متهم کرد.
واشینگتن‌پست در گزارش خود تاکید کرده که اقدامات پشت‌پرده قطر، تصویری از شیوه‌های پنهانی کشورهای خلیج فارس برای دور نگه داشتن خود از خسارات بزرگ‌ترین جنگ منطقه در ۲۰ سال گذشته به دست می‌دهد.
در این گزارش با اشاره به حمله موشکی جمهوری اسلامی به تاسیسات گازی راس لفان در قطر در اسفندماه سال گذشته، نوشته شده است این حمله بخش‌هایی از بزرگ‌ترین مجتمع تولید گاز طبیعی جهان را نابود کرد که نزدیک به یک پنجم گاز جهان را تامید می‌کند.
این حمله همچنین قراردادهای چندمیلیارد دلاری با چین و دیگر مشتریان را به خطر انداخت و چشم‌انداز پایان زودهنگام جنگ را با کشاندن قطر، یکی از میانجی‌های کلیدی میان آمریکا و جمهوری اسلامی، به درون درگیری تیره‌تر کرد.
به‌نوشته واشینگتن‌پست این حمله اما یک پیامد پنهان دیگر نیز داشت. به‌گفته مقام‌های امنیتی خاورمیانه و مقام‌های غربی مطلع از اطلاعات محرمانه، این حمله همچنین تلاش‌های مخفیانه قطر برای خارج نگه داشتن مجتمع گازی خود، موسوم به «راس لفان»، از فهرست اهداف جمهوری اسلامی را ناکام گذاشت.
یکی از مقام‌های ارشد امنیتی منطقه به این روزنامه گفت قطر چیزی در حد یک «توافق محرمانه» پیشنهاد کرد؛ توافقی که بر اساس آن دوحه متعهد می‌شد از نفوذ خود بر عرضه گاز برای تسریع پایان جنگ استفاده کند و در مقابل از جمهوری اسلامی تنها یک تعهد می‌خواست: «به ما حمله نخواهید کرد.»
یک مقام دیگر که به همان اطلاعات دسترسی داشته نیز به واشینگتن‌پست گفت پیام قطر به تهران این بود که: «شما بدون حمله به ما نیز به اهداف خود خواهید رسید.»
به گفته این مقام‌ها، قطر نتوانست تعهدی از جمهوری اسلامی دریافت کند. با این حال، روندی که پس از آن رخ داد نشان می‌داد که احتمال وجود یک تفاهم ضمنی دست‌کم به‌طور موقت همچنان برقرار بوده است.
قطر در سومین روز جنگ، زمانی که جمهوری اسلامی صدها موشک و پهپاد مسلح را به سوی اهدافی در سراسر خلیج فارس شلیک کرد، مجتمع راس لفان را تعطیل کرد. در آن زمان، قطر دلیل این اقدام را «حملات نظامی علیه تاسیسات عملیاتی» اعلام کرد.
تصاویر ماهواره‌ای که بعدا از سوی واشینگتن پست بررسی شد، هیچ نشانه آشکاری از خسارت در راس لفان نشان نمی‌داد.
اظهارات مقام‌های قطری نیز نگرانی‌ها را در بازارهای جهانی انرژی تشدید کرد؛ از جمله هشدار وزیر انرژی قطر که گفته بود این جنگ «اقتصادهای جهان را به زانو در خواهد آورد.»
قطر در پاسخ به پرسش‌های واشینگتن پست، هرگونه توافق محرمانه با جمهوری اسلامی را رد کرد و گفت تصمیم برای توقف تولید در راس لفان صرفا به‌دلیل تهدید حملات و نگرانی برای کارکنان و زیرساخت‌هایی اتخاذ شده بود که شریان حیاتی اقتصاد این کشور محسوب می‌شود.
...
iranintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76269" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0E4RoXqWBYQHLgFnOpnAfA-MtT86te4Ic1RrJkccrU1Nhu3iihptS5VFhDdAnri7XtYqjSHSm_gk8Bsg8-jnJVUtupQKzWjwGi4kbJHdX27u86MFHnX0UNEsoAxpmdDjOIOahuESxKK-czZLjitYfRChgBBUs1qHBWR7cU4uYrAWeteWVZeocDINmGQtOptMa2ufZCSPH8ve1Tx3fPEhlz37Vj5jfVN2tiyO8059QMptNrWCUv4qGjPkIrOcsf2sbwPczgG6ChC1jvAzWK1kSz2kPmw7D2Xi5HDQhK1PiYN8GCfYnqGgkw6IQHjANWIuaBQoxSJpDBISot0rAb_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز جمعه گفت که در ازای امضای توافق با ایالات متحده یا حضور در یک نشست، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت و تهران «هیچ پولی دریافت نمی‌کند».
او در شبکه ایکس نوشت توافق آمریکا و ایران «به گونه‌ای طراحی شده است که اطمینان حاصل شود نگرانی‌های ایالات متحده و متحدانش در اولویت قرار دارند و در صورتی که جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به ایران و همچنین به کل منطقه خواهد رسید».
معاون دونالد ترامپ همچنین وعده داد: «این توافق این ظرفیت را دارد که منطقه را دگرگون کند و به صلحی پایدار منجر شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76268" target="_blank">📅 18:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XIL98dqGeF7GiAqVrpkjRI59HnqpaijdZwLj5timIvTIBldo_xcgen2w0aqSA8ApmDVaPZ-9Y6oIeepdJAHAaZvGYcLoDVmHx-CznHdNiw9uaaWhnyznnzS-tq2SmgnDz_YEOU6aWQQCrZx6bIkkkeTcPYDLDEHNRP75rOh_GqG7FLRIJ-4WGMsWNXoFXDvxbrFheB5xWfaWg8pkxAw8AYSIsPX19gDVEEW9C--gZWEZspdwNbnXauH6Vka-L4N8ag8jeuC9QybwNrNGtYd8SSKGImCgRSOIy5IB4KE0b0gXlRSfZ5C6whR0kyLnVJ_vFjOhIAhKFh-mNvYZ-e0Mlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
یادداشت تفاهم اسلام‌آباد هیچ‌گاه تا این اندازه نزدیک به نهایی‌شدن نبوده است. تا زمان نهایی‌شدن آن، رسانه‌ها باید از ورود به گمانه‌زنی درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، همه جزئیات در زمان مقتضی با افکار عمومی در میان گذاشته خواهد شد.
araghchi
ساعتی پیش، دونالد ترامپ،‌ رئیس‌جمهور آمریکا، از آنچه درز دادن مواردی از توافق به رسانه‌ها توسط ایران خواند انتقاد کرد و اعلام کرد موضع جمهوری اسلامی درباره توافق «هیچ نسبتی با واقعیت ندارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76267" target="_blank">📅 18:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/012364ed90.mp4?token=RAFt-ICNfDLoOz-rkynufMIXOGl30-VQoDOh4ZW17VIEMpW0jOabHRmYXqUKR5qMCbamxRHf7QtSez6qols3I9uAkqtTuxjf4bUD_aE4lTxjgXXLoHhMp2frAXgVgxH7wA5wtzXOPeyw52n1MAy7tNZmwGc7X0dcKetkiRq60XKnAuxX5L-nS2JVeETn9KR2aeaLJVOwdQPxTjFOHSyeo7MEcO0LYa557NrJ5scQDchYNOAAhtJI_GuFcS2hWrQ1er73zNsJSsl6Ln1x9LZU_p-2fYdW54LwK4cWzGanXRfx9PF4PH5858V2wUvzrWgAvnN6livolQ6UspRGLNl5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/012364ed90.mp4?token=RAFt-ICNfDLoOz-rkynufMIXOGl30-VQoDOh4ZW17VIEMpW0jOabHRmYXqUKR5qMCbamxRHf7QtSez6qols3I9uAkqtTuxjf4bUD_aE4lTxjgXXLoHhMp2frAXgVgxH7wA5wtzXOPeyw52n1MAy7tNZmwGc7X0dcKetkiRq60XKnAuxX5L-nS2JVeETn9KR2aeaLJVOwdQPxTjFOHSyeo7MEcO0LYa557NrJ5scQDchYNOAAhtJI_GuFcS2hWrQ1er73zNsJSsl6Ln1x9LZU_p-2fYdW54LwK4cWzGanXRfx9PF4PH5858V2wUvzrWgAvnN6livolQ6UspRGLNl5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: خطرناک‌تر از ناو، سلاحی است که می‌تواند این ناو را به قعر دریا فرو ببرد  رهبر جمهوری اسلامی تعیین نتیجه از قبل برای مذاکرات بین ایران و آمریکا را «کار غلط و ابلهانه» خواند و گفت اگر هدف گفت‌وگوها برچیدن برنامهٔ هسته‌ای باشد، چنین موضوعی اساساً جای…</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76266" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Trm-EZtXAViiwvza8O7DEdlFaP2pBSwGWvJFX5KmDD0lVl0qAzNh3wE9sP9bZQzWupfOjfc5lW2TqT-EO0Ilr4qNleragbTnrKeI-4aAU2O7zWyyyDIhejW-Y_ejbwpHclFnNPDHY0qS0i4h3Zkq27s7sq8WoCXPyT6EYBfJL6lGOMSpWxN_CSCBv_kTaMXuUWEMriK0M0-8eJ1WXxR1MKIOi8fuTrtplQErBOtaKV5m2RCalOr8g7Q4tPKQ8vqr_qesvSlBEPrCWUlqFJKZwCwEXXmFERzImjNchFOby3e7UGD1Ty-w_CM2NQpqxJ6Tr3isujmzTwZ1sdC5-MkEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
شرایطی که ایران به رسانه‌های اخبار جعلی درز داده، هیچ ربطی به شرایطی ندارد که به‌صورت مکتوب بر سر آن توافق شده بود. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و رقت‌انگیزشان درباره داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. طرف‌های بسیار بی‌شرافتی برای معامله هستند. با آن‌ها چیزی به نام معامله با حسن‌نیت وجود ندارد. شگفت‌انگیز است!
همچنین حمله پهپادی کاملاً دفع‌شده آن‌ها در شب گذشته علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است. بهتر است هرچه زودتر خودشان را جمع‌وجور کنند، آن هم سریع!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76264" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QTtCRv7fGgQrThJrc_7WF9oinyofqWjIWQrixuD9-skFkO9ySlAIizankcTwbgIE3_7tiRuxmjZlWzq0dUtTlNd4agRlklRy1zXVa7iAOyt1fp9-Lw6o9bw2jEdGVg3_OhqxLP4TF8Ulci6MKBPWkYSOllphzoclU7kzYv-so75mMWHqgBIlFqkSNyNP6tHl6jkth85tYsi_q7mxW83SBuhBKJk0UKiqTgJQ-oEzhTOa9CKKauCSKvQ0ggcjudUfx019z5xzjZZigvCWvGRD5PehjFG99fQ8-eG0c3helEGyxCPNhmxxfscvE3EIgxXo1XcdZfFrMyXTAI99p6EcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حبیب‌الله سیاری»، معاون هماهنگ‌کننده ارتش، در گفتگویی با تلویزیون حکومتی جمهوری اسلامی تایید کرده است که از سرنوشت خلبانانی که در جنگ اخیر به قطر حمله کردند اطلاعی در دست نیست.
در این گفتگو که شامگاه پنجشنبه ۲۱خرداد۱۴۰۵ از تلویزیون جمهوری اسلامی پخش شد، سیاری درباره خلبانان یک یا چند فروند جنگنده سوخو ۲۴ متعلق به ارتش ایران سخن می‌گوید که به پایگاه العدید در قطر حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76263" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQa3iHIoqzVnFElgqATxCV3phPpW1_-tingTo1QUD-z4uyfSBAi0vusqAd7ZpT9x5d4-rcI3rsONhzE-L8eljdCHDC3djCsRi4XY39km-Xh3Mp2Q2rPXpVHcH3DrIS6PMQX4tfOsZyq1c0peyigMjqiWkVLpovn7WJH6jKutmOR_2msoaM3yzuCb0v7k81EhwwGtCNZPnMiay8RJqYsQfqg3U7YCAGSjPSFcIZf9QdiEjTY53_PJabo2a3lIgdFQEOpnylhceAos7wT0NDjxsx3ROrD0xfenT-juA98kx6u_cr-lggnfo2nIrVigUluXcwEKnDAHw0QC1ik9BnNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، نماینده مجلس جمهوری اسلامی، با انتقاد از پیش‌نویس توافق احتمالی میان آمریکا و جمهوری اسلامی، آن را مشابه برجام و «خسارت محض» توصیف کرد. او گفت: «حرف از پیروزی با این متن مبهم و خسارت‌بار کاملا غلط است.»
نبویان با انتقاد از مفاد مطرح‌شده در پیش‌نویس توافق، گفت در این توافق جمهوری اسلامی حق تولید سلاح هسته‌ای را نخواهد داشت. او همچنین افزود سرنوشت مواد غنی‌شده به رضایت آمریکا وابسته شده و همه موضوعات مرتبط با برنامه هسته‌ای باید مورد مذاکره قرار گیرد.
این نماینده مجلس تاکید کرد: «این توافق مانند برجام خسارت محض است و بخاطر تغییر محاسبات مسئولان است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76262" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc-jCFAfTdi0vqlD4Lz_aTL7mil6U4zpv387gSb1lPHcTcD5PtMRuPaZhEyc6yusnh0vCTW2j5f4x--4JWc4o7gDvjgazx4vVgJDi4Fw40ioJ2b91DUKc9St67Sk8Kl3Pqk3cee20HEaBfdXB3BUqeyaN3E8rhpmusfisraXdkZTfcffWir2z8Y6nBZpiNUwnDOs0rvMm73LHwJaNhS6Q3-ROjZvi9dLpYcPo1O8rV2KnkxRDaUXqUXXjCBRID8O4I3-4c8LG8UAk-p1a-FYf2wF67IT83Bn-XwWQiHiK9QLIWKWgqSOW-wZMIPXqb98jzMS-Nuvk2rUaHcd9VUpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اعتماد در داخل ایران به نقل از یک عضو رسانه‌ای هیئت مذاکره‌کننده جمهوری اسلامی و وب‌سایت اکسیوس در خارج به نقل از یک دیپلمات از یک کشور میانجی و یک مقام آمریکایی روز جمعه، ۲۲ خردادماه، گزارش‌هایی از محتوای احتمالی تفاهم‌نامه میان ایران و آمریکا منتشر کردند.
این دو گزارش تا اندازه‌ای به یکدیگر نزدیک هستند، اما گزارش اعتماد با وجود جزئیات بیشتر به نقطه نظر حکومت ایران نزدیک است، در حالی که متن اکسیوس برخی از موارد را منوط به آینده مذاکرات گزارش کرده است، مانند تعلیق تحریم‌ها که اکسیوس می‌گوید مشروط به پایبندی تهران به تفاهم‌نامه است.
روزنامه اعتماد به نقل از «عضو کمیته رسانه هیئت مذاکراتی ایران» از تفاهم‌نامه‌ای ۱۴ ماده‌ای می‌گوید که در آن بر «بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی» و «تعلیق تحریم‌های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن» تأکید شده است.
این در حالی است که در گزارش اکسیوس آمده است که تنگه هرمز «بلافاصله بدون دریافت عوارض بازگشایی می‌شود» و «ظرف ۳۰ روز» تعداد کشتی‌های عبوری از این تنگه به زمان پیش از جنگ بازمی‌گردد.
در مقابل این اقدام، آمریکا هم محاصره دریایی بنادر ایران را که بر صادرات نفت ایران اثر قابل توجه دارد حذف می‌کند.
اکسیوس به نقل از منبع دیپلماتیک خود می‌نویسد: «هیچ تاریخی برای تعلیق تحریم‌ها تعیین نشده و تعلیق منوط است به اجرای توافق [از طرف ایران].»
به نوشته اکسیوس، تعلیق تحریم زمانی افزایش می‌یابد که ایران «تفاهم‌نامه را اجرا کند و در مذاکرات بعدی از خود حسن نیت نشان دهد».
تفاوت دیگر بین دو گزارش از محتوای احتمالی به آزاد شدن یا نشدن اموال بلوکه‌شده ایران مربوط است. اعتماد به نقل از منبع خود می‌گوید: «آزادسازی ۲۴ میلیارد دلار پول‌های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.»
این در حالی است که دونالد ترامپ پیشتر به طور مشخص با آزاد کردن پول‌های ایران پیش از مذاکره یا رسیدن به توافق مخالفت کرده و به طور کلی به این کار به دلیل سابقه‌اش با باراک اوباما در توافق برجام حساسیت ویژه دارد.
گزارش اکسیوس در این زمینه سکوت می‌کند و می‌نویسد که «مشخص نیست» که متن تفاهم‌نامه حاوی اطلاعاتی درباره پول‌های ایران هست یا خیر.
درباره برنامه هسته‌ای ایران، اکسیوس نوشته است که تفاهم‌نامه شامل «تعهداتی»‌از طرف ایران خواهد بود، مهم‌تر از همه این که ایران هرگز به دنبال سلاح اتمی نخواهد رفت و بن‌بست در مورد اورانیوم غنی‌شده را حل خواهد کرد، دو موضوعی که ترامپ بر آن تمرکز دارد.
به نوشته اکسیوس، ترامپ موافقت کرده است که یکی از گزینه‌ها برای حل این مسئله رقیق کردن اورانیوم در داخل ایران «زیر نظر کارشناسان سازمان ملل» است، نکته‌ای که پیشتر روزنامه نیویورک تایمز هم خبر داده بود.
منبع اعتماد تنها به این شکل به این موضوعات اشاره کرده است: «۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی» و «تکرار تعهد ایران در پیمان ان‌پی‌تی مبنی بر عدم تولید سلاح هسته‌ای».
در این بخش از گزارش روزنامه اعتماد به موضوع سرنوشت مواد غنی‌شده اشاره نشده است.
به طور کلی، بر اساس گزارش اکسیوس، تفاهم‌نامه در صورت امضا شدن آتش‌بس جنگ را، از جمله در لبنان، تا ۶۰ روز تمدید می‌کند، دو ماهی که قرار است تهران و واشینگتن مذاکرات هسته‌ای را برگزار کنند.
آن طور که اکسیوس نوشته است، ایران و آمریکا بر سر متن تفاهم‌نامه توافق کرده‌اند، و این متن توسط مقامات عالی‌رتبه در جمهوری اسلامی نیز تأیید شده، اما «احتمالا هنوز تأیید مجتبی خامنه‌ای را ندارد». بنابراین در حال حاضر گفته سخنگوی وزارت خارجه ایران که تفاهم‌نامه هنوز نهایی نشده به واقعیت نزدیک‌تر است.
در حالی که ترامپ از امضای تفاهم‌نامه احتمالا در روزهای شنبه و یک‌شنبه حرف زده بود، به نوشته اکسیوس، چهار هواپیمای نیروی هوایی آمریکا روز پنج‌شنبه برای انتقال تجهیزات سفر جی‌دی ونس، معاون ترامپ، به ژنو در سوئیس برای شرکت در مراسم امضا «در روزهای آینده» پرواز کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76261" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeXB9WU4zTJXmf6KpUFrP5uizTzd9MGcnp970tqc0Rw6iIJJWLdkLTen-DBDkSi4BLVKXNAN3-Z4RUfqS7RSAtv8h8IZXERXnKO6m0xnwHsHM6wFKn0xeRJckhx087Ocg7Y9_tOL-AcWIWazVxQ7BMKY51bkH2rWZM3rB0gYVD_ND5KWbVbGK009mkAjhQmx3aJaBqOjQVD5SgtH2PWSn6YkSdnO-McmcC3Lv-iJ6ZO4z8Xr_CC6qv6Yod8S98nc1jEC0-5FEmb4HGVDWANuPtdVKw8HCJ1y3lpiAKPP11XNS2e6sHVEYkNe4JHiN-xt8i_QNa5OVgAIbEEBrSSuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از مقامات ارشد آمریکایی و ایرانی نوشته احتمال دارد توافق میان دو کشور از روز یکشنبه و در شهر ژنو سوئیس نهایی شود.
این خبرگزاری بدون اشاره به نام این مقام‌ها افزوده که طرفین «در آستانه» دستیابی به توافقی برای بازگشایی تنگه هرمز قرار دارند.
بر اساس این گزارش، طرف‌های ایرانی و آمریکایی قرار است در حاشیه اجلاس گروه هفت که از دوشنبه در فرانسه برگزار می‌شود، «دیدار کنند».
اجلاس امسال گروه هفت از ۲۵ تا ۲۷ خرداد در دامنه‌های آلپ فرانسه برگزار می‌شود. به گفته افرادی که در جریان برنامه‌ریزی‌ها قرار دارند، شهر ژنو در سوئیس که در نزدیکی محل برگزاری اجلاس قرار دارد، به عنوان یکی از گزینه‌های احتمالی برای امضای این توافق مطرح شده و ممکن است این مراسم از روز یکشنبه ۲۴ خرداد انجام شود.
یک مقام ارشد ایرانی و یکی از اعضای گروه هفت به بلومبرگ گفته‌اند که «احتمال دستیابی به توافق زیاد است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76260" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STkaalMGl2JwinFrVJoXL8_nOGfyNrKs3AU5m9JdsH_Qr2Bx8nl9VQYFrKSQggA6GAnCY4UHSQprvCIT4DWWbAF_KFX6_WmWIeEAOxY4Xcgcr0xGaIr4gBOn5hOv_oAm16naY2ji_iPB2dLopXCQF4VZHGRVgntHAYmHsAeaD1G37larGdrFyZZSixUYT7ngjvblwpMRi0A7RVIKa1CVY1wFAVzcJ3u6qUrnCvyDHMowWeli1eownUvRlcTHjkiu4t1CH-fgivZlxtrlISSIx3dhWvQJ9hA0MtbA-dRzWqh_IgsfJISzDGsk8l0-hkVE4-3-jCOmlz0uVv0P_-9jAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، جمعه ۲۲ خرداد به نقل از «منبع نزدیک به تیم مذاکره کننده ایرانی» جزئیات جدیدی از پیش‌نویس تفاهمنامه ۱۴ ماده‌ای ایران و آمریکا را منتشر کرد.
بر اساس این گزارش تهران متعهد می‌شود به دنبال ساخت سلاح هسته‌ای نرود و در مقابل، برخی امتیازهای اقتصادی از جمله تسهیل صادرات نفت و بررسی آزادسازی بخشی از دارایی‌های مسدودشده را به دست می‌آورد.
مهر به نقل از این مقام گزارش داد که پس از امضای احتمالی این تفاهم‌نامه، مذاکرات جامع‌تری به‌مدت ۶۰ روز آغاز خواهد شد و موضوعات پیچیده‌تر از جمله سطح غنی‌سازی اورانیوم، ذخایر اورانیوم غنی‌شده و جزئیات رفع تحریم‌ها مورد بررسی قرار می‌گیرد.
براساس این گزارش ۱۴ محور تفاهمنامه احتمالی تهران و واشنگتن شامل موارد زیر است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به مداخله نکردن در امور داخلی ایران
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز به وسیله ایران
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته‌ای و لغو کامل تحریم‌های اولیه، ثانویه، آمریکا و قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تعهد ایران برای تداوم عضویت در پیمان «ان پی تی» مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار اموال مسدود شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق احتمالی
۱۳- تایید توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل
مهر به نقل از این «مقام آگاه» گزارش کرد که در بند آخر توافقنامه احتمالی، دوطرف تفاهم می‌کنند، مذاکره نهایی قبل از آزادسازی نیمی از اموال مسدود شده ایران، تعلیق تحریم‌های نفتی و رفع محاصره دریایی آغاز نشود.
دونالد ترامپ، رئیس جمهوری آمریکا شامگاه پنجشنبه گفته بود که به محض امضای توافق، محاصره دریایی پایان می‌یابد و تنگه هرمز باز می‌شود.
به گزارش مهر، توافق نهایی صرفا در موضوع سرنوشت اورانیوم‌های غنی شده و غنی سازی، رفع تحریم‌ها و «برنامه بازسازی اقتصاد ایران انجام می‌شود» و بحث درباره برنامه موشکی و حمایت از گروه‌های نیابتی «به صورت قطعی از دستور کار خارج شده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76259" target="_blank">📅 17:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coOtx7-N7x8kd3dqKP2qJ7mLgRZPsgzF0JHqvMx1qV7ztbu5I6Z04bgGbv9kFhUO4zyvoocXs5iw2HuFK0bHAghbEjG8W1c8VYQY0P_7B9_NSJjjFn7BqbtBdWGZLEUQ7rkYsAUokN-6cDqktnaGlVmt54FyafPN5MRRDxFeIYjSaF0wfc03NItKOI4MkMJPJjucnkw71oOOY6dgG8X7b-je9uzqWF7NOY_GWJR6vuPX_UqbcTdtA97iOXrM4FUpl8yP0RVRdUsj00rKaGQlhUEgauRqkAiELFERy4w1Ych5CK3OsPAJqalbTbBcf-q-bPOYNTFRpFcDMZAUQ9YvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیر احمدوند» ۳۹ ساله، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در نزدیکی کلانتری رشید در تهران هدف شلیک گلوله قرار گرفت و جان خود را از دست داد. او متأهل بود و همسرش در زمان کشته‌شدن او سه ماهه باردار و در شرایط استراحت مطلق قرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76258" target="_blank">📅 17:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X45LMNHqngmg_8hgWDcyvzmlYl1LYnjave2iEYWCxn2Yqh991DwYP8-4TO8GpHV56KOlURyQMG53QD54y3aAa8kOMQOdoqYCgzA1YUtiTg0Ou5dEFiauIero7SwPxB4MAjTKxLuzNYq9vAg6MQCzRbJd72pskygEjgzElXh_sybZbUPZitX7GNfGcFDbUMKpJdIUwm8faqDe3OORKACJ2BpSSbhZCOw439AS1PcMsIA_U5ntwCN-LJ18dpiXiJjIh6LBXbuX5HzVfMwWCo4ghPaxRUbfUmGtQqI2R2ABh6-Fr8Ewzb2jPrJYD3g260l6bXyvGsN7nkIN-IjOvlh80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولتیکو، اندکی پس از آنکه دونالد ترامپ، رئیس‌جمهوری آمریکا، صبح پنجشنبه در پیامی اعلام کرد که قصد دارد ایران را «امشب به‌طور بسیار سختی هدف قرار دهد»، رهبران کشورهای حوزه خلیج فارس و جنوب آسیا در تلاشی آخرین‌دقیقه‌ای با او تماس گرفتند تا نظرش را تغییر دهند.
آنها به او اطمینان دادند که یک توافق اولیه که مسیر را برای مذاکرات جزئی‌تر هموار می‌کند، در واقع در دسترس است.
به نوشته پولتیکو، این تماس‌ها که پیش‌تر گزارش نشده بودند، به گفته دو مقام دولت آمریکا و یک دیپلمات مطلع از این تماس‌ها، از سوی تمیم بن حمد آل ثانی، امیر قطر، محمد بن زاید آل نهیان، رئیس امارات متحده عربی و عاصم منیر، رئیس دفاع پاکستان انجام شد.
هر سه منبع به دلیل حساسیت موضوع دیپلماتیک با شرط ناشناس ماندن با پولتیکو  صحبت کردند.
ترامپ سپس در تروث سوشال اعلام کرد که ممکن است یک توافق در چند روز آینده امضا شود.
@
VahidOOnLine
این رسانه نوشت گفت‌وگوها شامل بازگشایی تنگه هرمز و دسترسی ایران به بیش از ۱۶ میلیارد دلار منابع مالی بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76257" target="_blank">📅 06:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZEiCB3EbNmxAR34ewIQAX1ru0V0wzvbwrGaWtckPCHJnfH0qG11A31BvsyXPSooKMN35Z39ttCNViCob0kBljzLgk-XNMIbwPJE3sclNqIt4AwN6yAHEfDYKoOQGD7Avq49w8WBQhHuGs5JPrmc6nGOMPkN0PzkcH0jnTRwo814O9sNgrYZdy3onTRb362d6E4NPpQhrfjRFpREmGVgrkzZR7JTdaBs6_gXOuH4MEbKI4s1b8nkk9t5XXSB7_mhR0yXm99sFB_TQhKee2IkbWknPRI68cskEyIXzNj_nWfLQCcRXGq9GKfAarP5cSOFyF0HIxq-LXeUXWEwoPWtdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته یک مقام ارشد دفاعی ایالات متحده، ترافیک کشتی‌های تجاری در تنگه هرمز پنجشنبه شب پس از آنکه جمهوری اسلامی ایران پهپادهایی را به سمت کشتی‌هایی که از این آبراه استراتژیک عبور می‌کردند، شلیک کرد، آشکارا مورد تهدید قرار گرفت.
به گزارش فاکس‌نیوز این مقام گفت: «به نظر می‌رسد جمهوری اسلامی امشب تلاش کرده است به کشتی‌های تجاری که از تنگه هرمز عبور می‌کردند، حمله کند. نیروهای آمریکایی دو پهپاد تهاجمی یک‌طرفه ایرانی را سرنگون کردند.»
این مقام گفت که علیرغم این حملات، ترافیک دریایی از طریق تنگه ادامه دارد.
این تحول ساعاتی پس از آن رخ داد که دونالد ترامپ گفت توافقی با جمهوری اسلامی ممکن است ظرف چند روز امضا شود و تنگه هرمز به عنوان بخشی از این توافق بازگشایی خواهد شد.
در پی شنیده شدن صدای چندین انفجار در سواحل جنوب ایران، پیشتر خبرگزاری فارس وابسته به سپاه پاسداران به نقل از «منابع محلی» در بندرعباس گفت که نیروهای جمهوری اسلامی به یک نفتکش که «بدون هماهنگی» وارد محدود تنگه هرمز شده بود اجازه عبور ندادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76256" target="_blank">📅 05:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezdRpDKotS83fL93KeGn1lS6Y73Pt9pZ9uqWTgTe8uiRbYUw9qQUup8bqV74JdV_minKbu5pYOGy7r32lQvBak4yTTItLrvzSzL2dJfZhD8fuBNqS-iDAQOkvZDlVA8IHu17Q7i0wzYPBj0F-K_pWEC0lsFL8AFMKY3Y9fG15PGUl6CYB645p4hyJAPlir7Rs7uGmlWGWCSXaE7TmeXXhzpnzLb-DWbnAWEzkFuxfbkl7ACYbNt3bILc5_hehPuyjrsUusXBplh5lVGp7ReIObvCJTBgC6_bmeSXkP3O-vlOfweu_ix96g3PfrJOIysU0uUdPLhLyQ0TMFYlZ8LIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه به بزرگی ۳/۱ در پردیس
شرق استان تهران
عمق: ۱۰ کیلومتر
پیام‌های دریافتی:
سلام من فاز یازده پردیس هستم همین الان زلزله وحشتناکی اومد اینجا، کل خونه شد گهواره
سلام آقا وحید
یه زلزله عجیب اومد همین الان دماوند سقف میلرزید نه زمین
سلام پردیس تهران زلزله
۳
ریشتر
میشد شایدم بیشتر
سلام  زلزله آمد لواسان
ساعت 3 و ربع خونمون لرزید . رودهن
بی صدا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76255" target="_blank">📅 03:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=jHVwZQaL5a154JIN2EW2JNwEmGQS_NfUClkwjWoMeGiOSMyXObUufdWE9XaziduCpKoEPn9u2h-bewi80hNY515xEDQQs8Gny7k2rRDNwW8fgbJmkPOj1QTtTfaoTFoFLqNYCVOtiVyr3wZSTUGfcpynOUbdIzyTsGwmMilg24S1gsLrPxUBDZ6YGxiy5Rwo0uLZArwG3TBrhtlbUTAvPwdV7A4i_6CVDU9CIma8ffeTKXTQkIN28lyHRYkRAB_mU9Lm185_kXfQ2uLH8vGYubZZRSPn3K7CPEMyMmsmLApR-8mlwhWjd9ZVBXodwy8gAT6-vOoeredcRzfeUHU61w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=jHVwZQaL5a154JIN2EW2JNwEmGQS_NfUClkwjWoMeGiOSMyXObUufdWE9XaziduCpKoEPn9u2h-bewi80hNY515xEDQQs8Gny7k2rRDNwW8fgbJmkPOj1QTtTfaoTFoFLqNYCVOtiVyr3wZSTUGfcpynOUbdIzyTsGwmMilg24S1gsLrPxUBDZ6YGxiy5Rwo0uLZArwG3TBrhtlbUTAvPwdV7A4i_6CVDU9CIma8ffeTKXTQkIN28lyHRYkRAB_mU9Lm185_kXfQ2uLH8vGYubZZRSPn3K7CPEMyMmsmLApR-8mlwhWjd9ZVBXodwy8gAT6-vOoeredcRzfeUHU61w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امروز جنگ با ایران را پایان دادیم.
و آن‌ها موافقت کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند.
چیزی که ما روی آن اصرار داشتیم.
این کل هدف بود. این ۹۵٪ ماجرا بود.
در جریان گفتگوی تلفنی برای حمایت از نامزد انتخابات سنا در ایالت آلاباما
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76254" target="_blank">📅 03:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/prAYd29KeipCBwajMDM5qF3nfwUaBESbqmPVLZX-HPhzJJAfnlwBnwFGuIRfFqxM3p7FQdz6HcpJCrzZ-CbwV860D8im1X3A-1yu6_grpUDNc2zwwLSHGO0c6WEhcSN7XM9vFddPoJYGqQcWZm5oyDvfnXgWnr1p2o4EJBefxjgM1UAauXSjxi0BhCEoYfvTly9m0XBwtApGvtnfkErPbIoTiw70V3ICZ3870ZzjkmZNKkNbHDgAiuYTbMsf9KLY-oFEM-NBqBou3iTBqAUoss9BDHHiNFha7L3WP52ZhOPtKtog-1BIbmD6-Qwq79jimAsgNCakf2FuSDG77xGr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه بامداد جمعه ۲۲ خردادماه به نقل از منابع خود گزارش داد پیش‌نویس مفاد نهایی توافق میان آمریکا و جمهوری اسلامی شامل تمدید آتش‌بس به مدت ۶۰ روز و بازگشایی تنگه هرمز است.
به گفته منابع العربیه، مذاکره‌کنندگان در طول این دو ماه برای دستیابی به یک راه‌حل سیاسی دائمی تلاش خواهند کرد. این منابع افزودند مذاکرات هسته‌ای بر سازوکارهای راستی‌آزمایی، روندهای بازرسی و محدودیت‌های آینده متمرکز خواهد بود و در همین دوره درباره اورانیوم غنی‌شده با غلظت بالا نیز گفتگو خواهد شد.
به گفته منابع العربیه، آمریکا دسترسی به بخشی از دارایی‌های مسدودشده حکومت ایران را تسهیل خواهد کرد و در چارچوب توافق، کاهش و لغو بخشی از تحریم‌ها را دنبال خواهد کرد. این منابع همچنین گفتند آزادی کشتیرانی بر پایه توافق میان آمریکا و جمهوری اسلامی احیا خواهد شد و گفتگوها درباره لبنان و امنیت منطقه‌ای نیز پس از توافق ادامه می‌یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76253" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادعای خبرگزاری فارس:
ایران اجازۀ عبور نفتکش متخلف از تنگۀ هرمز را نداد
🔹
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازۀ عبور یک نفتکش متخلف که بدون هماهنگی وارد محدودۀ تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
صدا و سیما:
یک منبع آگاه نظامی تایید کرد صداهای انفجار شنیده شده در شهرستان سیریک مربوط به مقابله با یک فروند شناور متخلفی است که قصد عبور از تنگه هرمز را داشت
براساس اعلام این مقام نظامی؛  شناوری که دقایقی پیش مخل نظم دریانوردی اعلام شده بود یک فروند نفت کش است که با اخطار نیروی دریایی سپاه ناچار به رعایت قانون منع تردد در تنگه هرمز شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76252" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ادعای تسنیم: آمریکا از اصلاحیه‌های اخیر خود کوتاه آمده!
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است
▪️
پیگیری‌های خبرنگار تسنیم از منابع مطلع حاکیست: آخرین تحول رخ داده این است که فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
▪️
به گفته این منابع، ترامپ طی روزهای اخیر با شروع به فشار و تهدید و اقدام نظامی و از طریق دیگر با فشار میانجی قطری تلاش کرد تا از دو سو مواضع ایران را تغییر دهد که در نهایت ایران تغییرات جدید را نپذیرفت.
▪️
با این حال این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76251" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">"خبرگزاری مهر" وابسته به سازمان تبلیغات اسلامی، در پستی نوشته:
♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
منابع محلی در منطقه سیریک (استان هرمزگان) می‌گویند صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل، به گوش رسیده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است و‌ خبرنگار مهر در تلاش است تا جزئیات بیشتری را از مقامات محلی و رسمی پیگیری کند. /مهر
"خبرگزاری  صدا و سیما" هم بعدش در سه پست نوشت:
خبرنگار صداو سیما در سیریک:
دقایقی پیش صدای انجار در سیریک شنیده شد.
🔹
منشا و‌ مکان آن هنوز مشخص نیست.
🔺
منابع خبری از شنیده‌شدن مجدد صدا در محدوده دریایی سیریک خبر دادند
🔺
ماهیت و علت انفجارها در سیریک  هنوز بطور دقیق مشخص نشده اما برخی منابع آگاه آنرا مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند.
آپدیت ۱:۱۰
پست تازه خبرگزاری مهر:
♦️
تکرار صدای انفجار در محدوده دریایی سیریک؛ علت هنوز نامشخص
🔹
منابع خبری مهر تأیید کرده‌اند که بار دیگر صدای انفجار در محدوده دریایی سیریک، در استان هرمزگان، به گوش رسیده است.
🔹
هنوز ماهیت و علت دقیق این انفجارها مشخص نشده، با این حال براساس اخبار رسیده به خبرنگار مهر احتمال می‌رود که این رویدادها با سیاست‌های مربوط به بسته نگه داشتن تنگه هرمز در ارتباط باشد.
🔹
پیش از این نیز منابع محلی از شنیده شدن صدای انفجاری در دریا، در فاصله حدود دو کیلومتری ساحل سیریک، خبر داده بودند.
🔹
با این حال، هیچ‌یک از این فرضیه‌ها تاکنون به طور رسمی تأیید نشده است.
آپدیت ۱:۱۵
تسنیم: سیریک نیست. سمت دریا است.
یک منبع در استانداری هرمزگان به تسنیم کفت:
🔹
تا این لحظه هیچ اصابت پرتابه و درگیری در سیریک وجود نداشته است.
🔹
صداهای شنیده شده از سمت دریا و مرتبط با تنگه هرمز است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76250" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPBtUzVvAlFHNuDqJlwfz7AIlmeohvyo4FVLQkprWgnXAMCzIcEwBX35Ean9JeoZvfBEWEaBQ9Js-hJEtcYvf7PGOJswT-LABsM3xX8Mki9Kdw-B1Jei7NNH5k2VtRgjCetSqodGY33yxlUqnFtr5S0fJzNckdzj0_4qNt__GC4OP9PDoE9uxU0885jmuTOraxkn93_f2T1DszAPvJ2ZOc1qq_r4PIUbpR1io4rOUz91WPtXzFItUDZN2KGheBIis5QdyEZqVwrcMTU3JXCRQ9GHyVZkq89q-CMI3RVGGr69vfeYkxu_bWH6O08azOn5Hi2QOxPXn5s8LjqBJQBpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابعی در جمهوری اسلامی نوشته‌اند که: با میانجی‌گری قطر، آمریکا به شبکه beIN Sports معافیت داده تا مسابقات جام جهانی را در ایران پخش کند.
تاکید هم کردند که: این امتیاز توسط دولت ایران و کاملاً جدا از هرگونه یادداشت تفاهم (MoU) به دست آمده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76249" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=vWHoB_uvMG_SIgwkWfMsziGe0RYwj2rFCdqAx6Q3pbi710_VW1z27XOlOOlPHhvaa4atuoLEe4rHpDppBti3zorJxe8ovNhWs1VyYnnJeF2GXJvs5Fa-9vOucdOUpKd4RRC6qxE_md9XK1yR5Hzq2tdrGTtHn6EHhTCl4RXrqnaR57KjgwO6sFgvgQgyDYzK2uo2DPyA_3bccnrXmrgDaR3VUrXXX5DrFwwVsrVhyuyIN45Q3nXlwyIY-VvHEnt2tMuq4nCIRgU2ZC-LevkN_o8OqB1HbPNicluKej6DJXjnRmfYkVa-XPMSgb3eUcRDLqlGKp3f88bH3DfqNe0ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efef15c7c2.mp4?token=vWHoB_uvMG_SIgwkWfMsziGe0RYwj2rFCdqAx6Q3pbi710_VW1z27XOlOOlPHhvaa4atuoLEe4rHpDppBti3zorJxe8ovNhWs1VyYnnJeF2GXJvs5Fa-9vOucdOUpKd4RRC6qxE_md9XK1yR5Hzq2tdrGTtHn6EHhTCl4RXrqnaR57KjgwO6sFgvgQgyDYzK2uo2DPyA_3bccnrXmrgDaR3VUrXXX5DrFwwVsrVhyuyIN45Q3nXlwyIY-VvHEnt2tMuq4nCIRgU2ZC-LevkN_o8OqB1HbPNicluKej6DJXjnRmfYkVa-XPMSgb3eUcRDLqlGKp3f88bH3DfqNe0ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات جمهوری اسلامی:
من این افراد را بسیار منطقی‌تر از افرادی می‌دانم که دیگر با ما نیستند. این یک گروه متفاوت است و من فکر می‌کنم گروهی باهوش‌تر است که منطق دارد. همه آنها توافق را تأیید کرده‌اند.
آپدیت:
بعدا ویدیوی طولانی‌تری رو جایگزین کردم که اکانت فارسی وزارت خارجه آمریکا زیرنویس کرده و شامل حرف‌های دیگری هم هست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76248" target="_blank">📅 00:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8xUuSyWJ4LdMcAwRybvfEd7X0lVAevPHlQR0dKMIONICuiMGB_oG9Gfx3fcAQFFtby01uCwkbGMOYmiibnym4cUHO6m4ofL1PnFFr7w7BSoIV8ZHaG5-Dpq40wDOFikhJGnLSvgSFhy6HiZHVQJXtQ_kCcaQZo-aFFh6Hk9h3I1IU86xb-1gIMuS4gnoRtmZrs4FOVmuGRwTZWeYqe_3LzcfTErnGgNZsHD2nM2yO7LjMCfW7r0qYPYl3X2GTKkp8IpO0CY8W1GYfbj7U7yfmqjSl0ZcYlbECYG8AvU6N0q-CTLxES9alzuKN4auMeTs8WXuZFbtYCVye53IaaFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی در یک مصاحبه تلفنی گفت علیرغم فعالیت قطر و پاکستان به عنوان میانجی، روند دیپلماتیک مذاکرات به دلیل اقدامات آمریکا تحت تاثیر قرار گرفته است.
اسماعیل بقایی تاکید کرد که بخش عمده متن توافق نهایی شده اما به خاطر مواضع ضدونقیض آمریکا باعث تلاطم و اخلال در دست یافتن به توافق شده است.
سخنگوی وزارت خارجه در این مصاحبه گفت: «ادعاها درباره زمان و مکان توافق صرفا گمانه‌زنی رسانه‌ای است و تا مراجع ذی‌ربط نظام درباره تک‌تک اجزای متن توافق به جمع‌بندی نهایی نرسند صحبت درباره شکل امضا و مکان آن فایده ندارد.»
آقای بقایی اشاره کرد که متن توافق از پیش برای ما روشن بود اما طرف آمریکایی هربار مطالبه غیرمعقولی مطرح می‌کرد و بار دیگر تاکید کرده که ایران تحت فشار و تهدید از مواضع اصولی و خطوط قرمز خود کوتاه نخواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76247" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OAPQSzvzsgUCe3U4flQ1bs7JomkomZdZcA7fdKioT3nZr4XigJ_u29xi7Di9OYZ-Qk005qj1N0mrFP4cSItNbkG-9TxFR9PtGBoDbDdmKq7e8gEnx1xfmAWTU_DokuDi2-_gMh4EV9tL4CK-Gc5V1dRSP0ZXEBpu5Zdlc6Cyzbe2WAkPsc9bfO-_LlKdVPZoWqFHx49m5a4h9aER7d7OOmXem91gv_TJmSO3qiLXn0_w0Rc4VzFiar_1UlAj__rzE1SAII7x0NLv7_1hVtvx9UC-34IRUSCcMEDH0G29N3npcHD3vE655XfJHC-i8GVuJRRjbhf3B12FVDn2iMk9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل طرف تفاهم‌نامه با جمهوری اسلامی نیست
دفتر نخست‌وزیری اسرائیل، اعلام کرد که دونالد ترامپ، رییس‌جمهوری آمریکا، درباره یک یادداشت تفاهم در حال شکل‌گیری با حکومت ایران برای ورود به مذاکرات، با بنیامین نتانیاهو گفت‌وگو کرده است.
این دفتر افزود نتانیاهو از تعهد ترامپ درباره شرایط هر توافق نهایی با ایران ابراز قدردانی کرده، هرچند اسرائیل طرف این تفاهم‌نامه نیست.
دفتر نتانیاهو نوشت تعهد ترامپ شامل این موارد است:
-حذف مواد غنی‌شده
-برچیدن زیرساخت‌های غنی‌سازی
-محدودیت‌های تولید موشک
- توقف حمایت جمهوری اسلامی از گروه‌های نیابتی خود در منطقه
@
VahidOOnLine
به نوشته تایمز اسرائیل دفتر آقای نتانیاهو در بیانیه‌ای که «سعی در کم‌اهمیت جلوه دادن توافق احتمالی» داشت، می‌گوید که آنها درباره «یادداشت تفاهم قریب‌الوقوع با ایران در مورد ورود به مذاکرات» صحبت کردند.
به گفته دفتر آقای نتانیاهو، در این مکالمه، نخست‌وزیر اسرائیل دیدگاه نسبتا خوش‌بینانه‌ای نسبت به توافق ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76246" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=uWrEpD6FhDzGOoZeQ4jlzo9BluCHeieBaY7TBkaS-1d8m55Kf9rDAzGea3OGNRYDs3wNFf8ZKxUypdrgHXE2cc9mVo6_adnGXl8kfZdSct-xch_cOCKkcoFBbcBzFZbYPxo2hCRVQgeMR3-RgzIA-ItqagQL9l8jPaY_fKitxozVah3JLYFjdwHkg0waU1cxi4Kmsg3OD1aFhSZz42wSIXlPYx5Cu14CyE2FCDQp25XKFIgk83V2le6mwbJurz-CwhWjhN-YcfQ-WA4dI3QiBJWd-8Kw1J7nzU9d8FrWOvMNI6AVxF0Ug_SbS6VHAkDjdHlya5w180yrnCJCX8mWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d148f37d4.mp4?token=uWrEpD6FhDzGOoZeQ4jlzo9BluCHeieBaY7TBkaS-1d8m55Kf9rDAzGea3OGNRYDs3wNFf8ZKxUypdrgHXE2cc9mVo6_adnGXl8kfZdSct-xch_cOCKkcoFBbcBzFZbYPxo2hCRVQgeMR3-RgzIA-ItqagQL9l8jPaY_fKitxozVah3JLYFjdwHkg0waU1cxi4Kmsg3OD1aFhSZz42wSIXlPYx5Cu14CyE2FCDQp25XKFIgk83V2le6mwbJurz-CwhWjhN-YcfQ-WA4dI3QiBJWd-8Kw1J7nzU9d8FrWOvMNI6AVxF0Ug_SbS6VHAkDjdHlya5w180yrnCJCX8mWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ضرب‌الاجل شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
ترامپ: نمی‌خواهم ضرب‌الاجل بگویم چون بعدش می‌گویید من ضرب‌الاجل را رعایت نکردم.
خیلی مهم نخواهد بود چون قرار است امضا شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76245" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=ff2fV-1ZDzKBZ3Jly7HaaYhF3j2ERX3avdmUyU18_h2pwnGNiGO_VLlWlNOPjsgX10laDn4Gn_1v3wmu44PsBcnfYzLXCFM1l2bdD9_bj6xQ371cngCEvNnVJxnj47EzLIx6wTZOsK3S4X2dZOKg2AofG4P5VxxPO8HB-PigB_hFD9dFkmx36D1DJAytkJViulZ17mfGtC9T5caTL1U5BRx8Evrwf_58auP_KJ9ApFN2b_5PPOqmQtAWAJmjjxVei3tCvA1XE8K9yGGZ6LrUn6vtDdWrcj5z2_e8jSyyBJzaDUe9HVffcBZKmXCEyB1qJpcUJWPyiJhCJiXmhuKyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75104b39d.mp4?token=ff2fV-1ZDzKBZ3Jly7HaaYhF3j2ERX3avdmUyU18_h2pwnGNiGO_VLlWlNOPjsgX10laDn4Gn_1v3wmu44PsBcnfYzLXCFM1l2bdD9_bj6xQ371cngCEvNnVJxnj47EzLIx6wTZOsK3S4X2dZOKg2AofG4P5VxxPO8HB-PigB_hFD9dFkmx36D1DJAytkJViulZ17mfGtC9T5caTL1U5BRx8Evrwf_58auP_KJ9ApFN2b_5PPOqmQtAWAJmjjxVei3tCvA1XE8K9yGGZ6LrUn6vtDdWrcj5z2_e8jSyyBJzaDUe9HVffcBZKmXCEyB1qJpcUJWPyiJhCJiXmhuKyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه باز است. تنگه برای چندین ماه است که باز بوده، اما شما فقط از آن خبر نداشتید.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76244" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=u1YaJeKMMwrUSlDS5FxZK79YrrYK2KHkkseL2MeinlKHWgmak4OBxucv1O4WcLoqitUPBXnFIwfWTd4EHcXKeS9x8bvsOyRE62OepewIAvSz9GE-MaDZjKZ7IOil-_RTlvWnSDwOY-EURl3Qu7tGiQr0FipxOeDz1dLt_Kg1zRt31JQ-Y5m3c-JbiQzTYjX9F_hDmxzRP_4CAYIRAlGFvRM3HxtJiUu2Vp7b58IieaXZi2UbPQYb5rGD9jnGMg9syRHS7PMITV3-Me3GTp02seQE0zcudY1FAWbi0PK9gB1oPuYsThYNf0wzF92R4D_HU1jhc28J_ygnzH5Y705BtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38fa98505b.mp4?token=u1YaJeKMMwrUSlDS5FxZK79YrrYK2KHkkseL2MeinlKHWgmak4OBxucv1O4WcLoqitUPBXnFIwfWTd4EHcXKeS9x8bvsOyRE62OepewIAvSz9GE-MaDZjKZ7IOil-_RTlvWnSDwOY-EURl3Qu7tGiQr0FipxOeDz1dLt_Kg1zRt31JQ-Y5m3c-JbiQzTYjX9F_hDmxzRP_4CAYIRAlGFvRM3HxtJiUu2Vp7b58IieaXZi2UbPQYb5rGD9jnGMg9syRHS7PMITV3-Me3GTp02seQE0zcudY1FAWbi0PK9gB1oPuYsThYNf0wzF92R4D_HU1jhc28J_ygnzH5Y705BtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما قبلاً گفته‌اید که ایران و آمریکا به توافق نزدیک بوده‌اند. هنوز این اتفاق نیفتاده است. چرا اینقدر مطمئن هستید که این بار متفاوت است؟
ترامپ: چون آنها ضربه سختی را تحمل کرده‌اند. ضربه‌ای که کمتر کسی می‌تواند تحمل کند. و آنها خیلی بیشتر از من می‌خواهند به توافق برسند.
===
خبرنگار نیوزنیشن در کاخ سفید:
از رئیس‌جمهور ترامپ پرسیده شد که آیا می‌تواند این توافق را به سرانجام برساند یا نه، چون پیش‌تر هم به آن نزدیک شده بود. او گفت: «من بسیار مطمئنم.»
او درباره اینکه آیا واقعاً این توافق تا پایان این هفته نهایی می‌شود یا نه، با احتیاط پاسخ داد: «به‌زودی خواهد بود، شاید همین آخر هفته.»
ترامپ در پاسخ به این پرسش که آیا رهبر عالی این توافق را تأیید کرده است، گفت: «برداشت من این است که پاسخ مثبت است.»
KellieMeyerNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76243" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=OZVJQ15jKX1jhZnREsJ1lmkRP42RMNlTHz2CWNKMTD0_7Zgq54zi-JpTX2TgL2dtsrXbxoPrPMNHXMINm_-SfCndf0lgIeXPCIw2SBRMxRE_CIftby8rzH2E5Z3zUvFzFkCVNR4bUIO68R4Cy10n1zPrER5D76dxCOxxNaRWr22WFtiq4xp_9bJ4XIy8_L6vY06N-qZZnHREkOC-diPX_plPWNiEvTbKkH42zjUjXTkTFq-c8EoBbzJI0ITpg75yp7r1Xlu45eQ--PXu-_UiPMDBKwj7jpPGLZLD7YUoQAB71URaW5j0tWnp3ws629X0bUZqT7qhDmrU69zkyDDv6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30b9b51ccd.mp4?token=OZVJQ15jKX1jhZnREsJ1lmkRP42RMNlTHz2CWNKMTD0_7Zgq54zi-JpTX2TgL2dtsrXbxoPrPMNHXMINm_-SfCndf0lgIeXPCIw2SBRMxRE_CIftby8rzH2E5Z3zUvFzFkCVNR4bUIO68R4Cy10n1zPrER5D76dxCOxxNaRWr22WFtiq4xp_9bJ4XIy8_L6vY06N-qZZnHREkOC-diPX_plPWNiEvTbKkH42zjUjXTkTFq-c8EoBbzJI0ITpg75yp7r1Xlu45eQ--PXu-_UiPMDBKwj7jpPGLZLD7YUoQAB71URaW5j0tWnp3ws629X0bUZqT7qhDmrU69zkyDDv6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ممکن است آخر هفته در اروپا قراردادی امضا شود. من نمی‌توانم آنجا باشم، اما جی دی ونس آنجا خواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76242" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=UrWWjSXYpE2id6kdCsG5c_SpbLkC3r9TRPz09edUZp7wkPLtQGxMQfbOtQXGa3rMp1SDeyXlNfrWn3U4-dbnj_bU8GZuvQ351F9sy7KGQyJVDSoDgcjjwX-CkEwWIfhlb96hZUKI7Zkj5MA1lqeB7MU4FGUFEC50YcqwQ1dERPWytisflRBUC1rofDidFGZ4qGYjbt1sI_O4m2ubOhUvgbM0p6eCV0G2pJxxflQjbwx5yY-ZtxlA5eOcVJ8kFN8hiLj1j2h4NGdtHcxzZ_v01UB6lsyjShCEeskV8XNuzXL4DBD9Zqx-wFtHE6h3HTTgqm-g1Yapkl6uQlGzhvhMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f82f63f23.mp4?token=UrWWjSXYpE2id6kdCsG5c_SpbLkC3r9TRPz09edUZp7wkPLtQGxMQfbOtQXGa3rMp1SDeyXlNfrWn3U4-dbnj_bU8GZuvQ351F9sy7KGQyJVDSoDgcjjwX-CkEwWIfhlb96hZUKI7Zkj5MA1lqeB7MU4FGUFEC50YcqwQ1dERPWytisflRBUC1rofDidFGZ4qGYjbt1sI_O4m2ubOhUvgbM0p6eCV0G2pJxxflQjbwx5yY-ZtxlA5eOcVJ8kFN8hiLj1j2h4NGdtHcxzZ_v01UB6lsyjShCEeskV8XNuzXL4DBD9Zqx-wFtHE6h3HTTgqm-g1Yapkl6uQlGzhvhMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به زودی توافق را امضا خواهیم کرد و اسناد تقریباً در مراحل نهایی هستند.
دونالد ترامپ، رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر در خصوص توافق با ایران گفته است که ایالات متحده «به‌تازگی به یک توافق بزرگ در مورد جنگ با ایران رسیده است.»
او گفته است که «ما در حال نهایی کردن اسناد هستیم. این کار باید طی چند روز آینده انجام شود.»
آقای ترامپ می‌گوید که پس از نهایی شدن اسناد، «احتمالا امضا آن شاید در اروپا» انجام خواهد شد و این کار باید «خیلی سریع» انجام شود.
به گفته او «ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که هدف اصلی از آنچه که ما برای رسیدن به این هدف طی کردیم، همین بود. بنابراین، این یک چیز بسیار بزرگ است.»
رئیس جمهور ایالات متحده تأکید کرد که توافق «به زودی امضا» انجام خواهد شد و اسناد «تقریبا به شکل نهایی هستند، بنابراین خواهیم دید».
آقای ترامپ همچنین گفت تنگه هرمز نیز «به محض اینکه آن را امضا کنیم» باز خواهد شد.
او همچنین می‌گوید که با رهبران منطقه، از جمله متحدان خلیج فارس و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده است و افزود: «تمام خاورمیانه بسیار خوشحال است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76241" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سی‌بی‌اس:
احتمالاً اوایل هفته آینده یادداشت تفاهمی بین ایالات متحده و ایران امضا خواهد شد که راه را برای مذاکرات بیشتر در مورد یک توافق بلندمدت هموار می‌کند.
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76240" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smyesFXkuUH3IylsFxwTNWaIFpgqDTLBusA13gqYxCKYqGTGW_WZLzDrxc_kqRrJJYhI3gXjrDQuYZuF2CZP0hrBPQ_sALA1bKzwVJkrqSsQH-OTR8P_v6BDvSn8o87TLfj-Qup14Px3iQ91Kx3CfUqXSMzlbkHIn-aeeeRtsQ4I0H31J2wwlQLIFjPVL_LvtaJ6QmdDn_UGd1OScgoFbG6r4_3NCMQq1N9uB3hDuwgwdgnturTaDBnWhYOkbpDrgGS3dRrgIdFAQpDJ4BKqkrEO3EniPKjpfDGQ6o3zrR4EIxK07r5errs6nCSVyfP5evlRMcvgAI3TCBEXYtz63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس در پستی جدید نوشته:
"بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال تایید این متن در مراجع اصلی‌نظام بالا است‌."
🔄
آپدیت:
خبرگزاری فارس جملات بالا که در انتهای پست نوشته بود رو تغییر داد به:
"البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76239" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kjIZVyWCXveKLriDuZaV9i4H-3RVi4gChPNkUd6bV-E8ktQLLcpGozqCXW8-a7rSFImcMLMkOXSdvvxcXN0WNXIrfg1J4xTTwmlxBNfVZtzMqHhMpTbqWglgRiCVXbX58Pr_dAK8BG0VdtGemD5YkkXp_BAr3UY7Y9XHAgcU4-shmGxfsFyQmWo49350g4FYxY0r7Nd0tovGCbTOoASuySWppAhOAhCHcqzXIqPuaG8uRnBEwN5GPBhz9lB4K6njbo7CBjMOT_LuSNadyp6XTT6vohnMnWBduGdt3zNUxuMADcFb6p3KJlwwPgC79aWj2BG1z9MYqFxnMqBiTGh30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث به نقل از یک مقام ارشد گزارش داد هیات قطری که از تهران بازگشت، موافقت جمهوری اسلامی با پیش‌نویس نهایی توافق را اعلام کرد.
همچنین دفتر امیر قطر اعلام کرد که تمیم بن حمد آل ثانی، امیر این کشور، و دونالد ترامپ، رییس‌جمهوری ایالات متحده، پنج‌شنبه در یک تماس تلفنی نتایج رایزنی‌های آمریکا و ایران را که به پیشرفت در تفاهم‌نامه پیشنهادی در چارچوب یک مسیر مذاکراتی منجر شده بود، بررسی کردند.
دفتر امیر قطر در بیانیه‌ای افزود که ترامپ به امیر قطر گفته است تلاش‌ها برای تکمیل مراحل نهایی پیش از اعلام ترتیبات مربوط به امضای یک توافق ادامه دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76238" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیویورک‌تایمز: ‌قبل از لغو حملات برنامه‌ریزی‌شده به ایران در روز پنج‌شنبه، ترامپ با میانجی‌گران پاکستانی صحبت کرد که به او گفتند با ایران «توافقی» دارند.
clashreport
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76237" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/feT_WwB6CsIGTWkuHAzlF5BYBxlqCRpkwOD5UpDwp2gVMOs7iatlWm8NQocog0fjqKCumw5uqWTYbzCLb70HuvK2qBqnbpL-RTBJ_uNmifdGLoZV72nBsLCIoVqWp-flipSL7RoIrA7BvXOqJWj6bp2ee_CI-i4pqPEdn7bqGnUk5EHxZk4iO1wur1ZrO8wbfNduGUpm37SD-iqgancMk1WRiyddg6wed2JoBtU0HAZ_ZgHCqRNjTQecfEy3p6f-J3NCwxxzhf5lcP8zAbM9xlImqTcC1rF7aVFDkDlh_54A4B3uQZWoyv0wCD8TFnkbqPE1s28R-JddmOmm8vwzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی گزارش داد پست دونالد ترامپ در تروث سوشال درباره نزدیک بودن توافق با تهران، بنیامین نتانیاهو را غافلگیر کرد؛ در حالی که او در میانه یک نشست امنیتی درباره ایران حضور داشت.
سی‌ان‌ان افزود که این کشور از وجود هرگونه توافق قریب‌الوقوع با جمهوری اسلامی یا تایید آن بی‌اطلاع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76236" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiYyb5Zwd10wtOpLSyIqyeSUE2n0sQlorm02AMqzjrJfdSEH98c8WE_WO6z6pwmaDuB4d_d6aEudI0luaN8LuUrxMj9TqnfCngEetk_sRWUMJRcctXY6ClziF8ogWCbOrsAGwdULtYO45O-pMt4LdaKvWYC0kCxGYLAy63rVHtFrKM4qplQY3WT_u84s9gYfl-nT5QopjiumuO1Zxn_d0ghIw3P1p-OmK4dwrffRqDXxOwiC75P4qYCE0YmF23BuDQo5kX87MjjR5QrY9-bHmY7Sn_G0Dm1AWUb2MJ6JazAjgkb8TuJXpeiPAd4GJEMCRsDmYNnddwdcxUtUzS2b0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، ساعتی پس از پیام دونالد ترامپ دربارهٔ مذاکرات با ایران، مدعی شد که «هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تأیید نشده است».
فارس ادعای خود را با استناد به اظهارات «یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران» بیان کرده است.
رئیس‌جمهور آمریکا گفت: «زمان و مکان امضای این توافق به‌زودی اعلام خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76235" target="_blank">📅 22:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6m44mjqWxeKNBiZM-E6gTP9_vfmdDmqp9YxiYuzbxT24NTnCjLL3pR44VnFLHYvW9ZVPBTqaEjgyEU4hQ8a3j0hJg0Sv_6LSvQSWKKOeXsYNJRYPasDHuH-TjmCkOZ-G0fasz4-8tTRPKMmZ0b12GBRNOCFi-X7q7P9YuiodrEBSQLk1Nv9eQKQ2RmOWd9FBjTVK_DFY5ZA9LrllIRrZBy_ZKIl6MJwBOXBrGU11Z5qzHKOs_Bk4WTktFYk31VKVeGxWGxgcWTq0rHMK5BA438EfLcqBGXhWq2KOOSZZ8oZO0gqCVLDQJYvzvf_FJka7tnGbrHNqWxUk-W69qcUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه منبع آگاه گزارش داد اختلافات اصلی تهران و واشینگتن برای رسیدن به یک تفاهم‌نامه، چهارشنبه در جریان گفت‌وگو میان مقام‌های جمهوری اسلامی و میانجی‌های قطری برطرف شده است.
بر اساس این گزارش، مقام‌های ایرانی پنج‌شنبه به چند کشور اعلام کرده‌اند مذاکرات تهران به توافقی اصولی منجر شده، اما مجتبی خامنه‌ای باید تایید نهایی را صادر کند.
این منابع خاطرنشان کردند که هم ایرانی‌ها و هم قطری‌ها تاکید کرده‌اند که حملات آمریکا در طول شامگاه چهارشنبه، تردیدهای ایران نسبت به نیت واقعی ترامپ را به شکل قابل توجهی افزایش داده است.
@
VahidOOnLine
ترامپ: توافق تقریبا نهایی شده
ترجمه ماشین:
... نیویورک‌پست نخستین‌بار گزارش داد ایران چهارشنبه‌شب پیش‌نویس نهایی یک توافق را به میانجی‌های قطری ارائه کرده است.
رئیس‌جمهور ترامپ روز پنجشنبه، پس از اعلام اینکه حملات برنامه‌ریزی‌شده علیه ایران را متوقف کرده، به نیویورک‌پست گفت توافقی که مدت‌ها انتظارش می‌رفت برای آغاز مذاکرات هسته‌ای با تهران «تقریباً نهایی شده است».
او در یک تماس تلفنی کوتاه با نیویورک‌پست گفت: «تقریباً همه‌چیز نهایی شده است.»
nypost
سی‌ان‌ان به نقل از یک منبع آگاه گزارش داد مقامات آمریکایی بر این باورند که نشست‌های این هفته میان مقامات ایران و قطر در تهران، به حل برخی از نقاط مبهم و کلیدی باقی‌مانده در توافق با ایالات متحده کمک کرده است. این اختلافات عمدتا شامل جزئیات نحوه پیشبرد مذاکرات آینده در قبال برنامه هسته‌ای ایران و ترتیب زمان‌بندی لغو تحریم‌ها و گشایش‌های مالی برای تهران بوده است.
بر اساس این گزارش، ایران اواسط این هفته جدیدترین پیش‌نویس توافق پیشنهادی خود با آمریکا را از طریق میانجی‌های قطری ارسال کرد. این در حالی است که حدود دو هفته پیش، دونالد ترامپ با اعمال تغییراتی در متن، خواستار سخت‌گیرانه‌تر شدن لحن توافق در بخش هسته‌ای شده بود و از طولانی شدن پاسخ ایران ابراز نارضایتی می‌کرد.
با این وجود، رایزنی‌های این هفته از طریق قطر باعث کاهش شکاف‌ها شد. مقامات آمریکایی در تمام این مدت در تماس مداوم با میانجی‌ها بودند؛ حتی در روزهایی که واشنگتن و تهران به طور پی‌درپی در حال تبادل آتش و حملات نظامی به یکدیگر بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76234" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzBcgXyEufUrjFvQbIT2s9uUHZHegrUqJVbDODEkFTxJTjpAfbmuA6uLvoacE9Fsy-veguX7XEuwBlYJbx6oX4TOVUfMjN7cHMuzdp5HCd6pbahgb08mJP5uIvmLxqXWDLc8URDr133Mp8i1mlybNpMUWguE6AXkl0eJo-Auxp2u1HfUW7u_v0v2vQSOxX1sy5RrYqc-DgFI56nhQN4fM2Kfwn92QanbM9x8_oGi_tChVdnn1FlNUVgV7PO3px878byIWGZdJLDyqWa5b6nEsssTQDHuT6L3TlAJH3cv-ZElU2ZO0YKXz1Eno6YswCeJPUoYn3nsQXNWiQVJDBhCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله امشب را  لغو کردم چون بالاترین سطح رهبری در جمهوری اسلامی توافق را تایید کرد
پست ترامپ، ترجمه ماشین:
با توجه به این واقعیت که گفت‌وگوها با جمهوری اسلامی ایران به عالی‌ترین سطح رهبری ایران رسانده شده و مورد تأیید قرار گرفته است، من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران در شامگاه امروز را لغو کرده‌ام.
گفت‌وگوها و نکات نهایی، هم در کلیات و هم با جزئیات فراوان، به تأیید همه طرف‌های دخیل رسیده است؛ از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران.
محاصره دریایی تا زمانی که این توافق نهایی شود، با تمام قدرت و به‌طور کامل برقرار خواهد ماند — زمان و مکان امضا به‌زودی اعلام خواهد شد.
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76233" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzoP7BorSTFvm2AyOd_l5UPitkrIUCJf3oqFtTvExG_iWgre9ppLMRMV0HwoEF4zaRUKRDbiE-pgDuUErnbzebKeUSWbu7w-D7jwIF314yelXIuE1ElR2R2Pwr4VNK9kFC8UeVcMgp1NBUb-OK_hIx8whxH18XG_icIuXLBHNCgri9EOChzERpGP4D6nnPUnb_NLuFk3xg6e6LBpSSqZg77pL-rhXzxIhFnBPOKq9aJFQ5g1anSS63Xob6LdA4GYFdiyuLFjX1DG5olrQAVRzgB4SvQZBHFeRZoDGYcMXI8XLJdhwe-MTUiPz5tdPIWBVcVsJ46DXp5a5S1cIRgbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، در گزارشی اعلام کرد ایستگاه‌های زمینی استارلینک در اسرائیل، قطر، اردن، امارات و عمان به همراه سهامداران شرکت اسپیس‌ایکس و زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» به فهرست اهداف نظامی جمهوری اسلامی ایران اضافه شده‌اند.
فارس مدعی شد این تصمیم پس از به دست آمدن شواهدی مبنی بر استفاده ارتش‌های آمریکا و اسرائیل از زیرساخت‌های تحت مدیریت ایلان ماسک، از جمله شبکه اینترنت ماهواره‌ای استارلینک، اتخاذ شده است.
بر اساس این گزارش، «ایستگاه‌های زمینی استارلینک» در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران شرکت اسپیس‌ایکس و همچنین زیرساخت‌های شرکت‌های «الفیظابی» و «مبادله» در فهرست جدید اهداف ایران قرار گرفته‌اند.
فارس نوشت: «ایستگاه‌های زمینی استارلینک واقع در اسرائیل، قطر، اردن، امارات و عمان، به همراه سهامداران اسپیس‌ایکس و همچنین زیرساخت‌های دو شرکت الفیظابی و مبادله، از جمله مکان‌های جدید در فهرست اهداف ایران هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76232" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vD_KnDVvEs2L8f_ctihGHzpiltBKpgAM7lSBvxtNhlySxGJhfah9OCj4tBWXAGvm-_2GqPwtLEcAWbQ6Qsthy5gIVm6d4kv3KwZePfSJB_EBiOHjH8pFAksfhn6tjwfRjIpaG2UXXbWvIR04Xtl8Ln0CYP3B8Lp89fSGjiRlp3zWjTLP51y9ftIvqdgY7pHChd4w0JUBMkLVgZ7moVg8MXDZKv31BoTQfuNTNpm6wKd-brbXjAdiqutMWu4_11OMCld5_1QeYYM3VLP8-6caSRjtFYYrEcAsnEiwFXl47UawJh4N4L_3YpOhOht9KPXmlTiXXAuTFTp-_aJOkL-7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع جمهوری اسلامی در بیانیه‌ای اعلام کرد «هرگونه خطای محاسباتی یا تعرض به امنیت و تمامیت ارضی کشور با پاسخی قاطع، پشیمان‌کننده و فراتر از تصور غلط دشمنان مواجه خواهد شد.»
در بخشی از این بیانیه آمده است: «بی‌تردید نیروهای مسلح جمهوری اسلامی امروز از آمادگی، توانمندی و قدرت دفاعی قوی‌تر از گذشته برخوردارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76231" target="_blank">📅 20:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwIf7HLjYLeN2fHDBtZz23pxIZFE9Una_vKx6hFQ9lPbqQkk36BAyr1_GfZuYfLRoB_x57n8EM9KSOVB-bB7V_F_uNlyzXfoFrm1Ml9H3o1d_QuMzpHubmKm-bAbW7CPYeALPkJZuvaMbK-51wHVEy4PSymfZTl3fsXvshNOPmNhXul5qH6P-LTZ2aDul_YZxCesz0V7xVTutL4Q1OGsyu4M9USjzVVNziYBdIefdDBfFW6Elb3tU5a7E9AS74goE3fZrjVJJ6BGdA5uG1k0FRtCkQi5Wfdba7xA0W-ZUn2V9xORgXOeDiZE--gJVmU0wvOm_JtrlTaUSqcFHBVang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، در خصوص تهدید زیرساخت‌های نفتی ایران از سوی دونالد ترامپ گفت: «یا صادرات نفت و گاز برای همه برقرار خواهد بود یا برای هیچ‌کس امکان‌پذیر نخواهد بود.»
او ادامه داد: «در صورت تکرار حملات آمریکا، پاسخی شدیدتر خواهیم داد و آتش جنگ می‌تواند گسترده‌تر شود.»
فرمانده قرارگاه مرکزی خاتم‌الانبیا اضافه کرد: «تناقض در گفتار و رفتار آمریکا عامل اصلی ناامنی در منطقه است و امنیت تجارت بین‌المللی، به‌ویژه در تنگه هرمز، را به خطر انداخته است.»
او گفت سران آمریکا با «عدم شناخت ملت ایران و نیروهای مسلح» در دور باطل قرار دارند و با جنگ رسانه‌ای نمی‌توانند «شکست‌های پی‌درپی» خود را پنهان کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76230" target="_blank">📅 20:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2QwwtkF5vW2Hud6q7iPTSeWveo4wDDK3ZJiidtSa5LCHEi-_7XoU6dm0UKcQckXa2S2rUaUg2WV07rpL8yINuZt2cGJaJ71gj5Cw_oxo4dm7kze-uHAB1IiexCwDs72tmNSsliWNnAcGPqY7fw5XNy_AB2mrgy1dNnCiUtoSLB27-Xbjeozx3-Dw0itCnCTCDxGgyq9yAqJP4F2XQfisHBKmmG59KftYIL1Zj5JJ5SwOcMP_hiFgNuk-DbYq0V86kSHoQtjUF80cQOjIxNXyDpLbo0_98LO1iepiE5aCb1nLDjAoTh_rRfNN4Y6wVX8DVZICew7nBtf77YMAsxjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
"تنگه هرمز برای عبور و مرور باز است
مسیرهای امنی برای کشتی‌های تجاری که از تنگه هرمز عبور می‌کنند ایجاد شده است.
این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.
صدها کشتی در دو ماه گذشته از این مسیر عبور کرده‌اند.
نیروهای آمریکا برای دفاع در برابر تجاوز ایران در موضع آمادگی قرار دارند.
ایران کنترل تنگه هرمز را در اختیار ندارد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76229" target="_blank">📅 20:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=sI5bpJWvHnc_Fs-c1a2jX33XrVSU97V3gJADUe80RfOmVMz_bqwedzDQQj-hfR4AA9ilzafNfXqYi7nnoZNbxlgpNJ8J7gmKc4BLIm-g2G4bBUQM4uGYEsp8p9N_3XkTl55YZUrLEUtZHyndlUsK_NUitVpBH4P6ZdtJgb7NzFG4BXqM81SKemuVvaza3tco4dyx_ko0614Nx2aLocazdDS7D5mEOee4Cd_VrIZgWwppDkf6igZr6aQHclnf-obSPcAcJJxyzPnXRffQShg6A8nU_qLZpe7eLniHQ68vNUsIWHvuMtG3EpQAtcldxql5FlhElGVLIGccGsJESyQGK3eXzG90LCB0oK51NldXhlj6LURhRpfQH05oKz0GDkUdNw8QU3A-Uh7BYrDCSyI_zilHmOKKyvNRhvS6Y8nq-TOesc06pkfZ03B_bpOv2gI7quWxNnfpWM24q_aw8uILCaVKw_2f5JSiqfQPe8BVkTaY8sOoE9v5vnTUo9pOliQ9wio6mzNT47XGN48lc6P1FJjIk6xL-huOpVAuiFlHj4EE5ah6QUT-4TnmXaeN8jhuDLEYpSkm6lCO8C8dxVmZdSbb_CgTjSekrRirQvf4JqV9A3cCkZKh27Lef3mdU2aEjtufsxcfLKYUky3jMkyUT2h4W4JAsotXreK047CMfwY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8d3934df9.mp4?token=sI5bpJWvHnc_Fs-c1a2jX33XrVSU97V3gJADUe80RfOmVMz_bqwedzDQQj-hfR4AA9ilzafNfXqYi7nnoZNbxlgpNJ8J7gmKc4BLIm-g2G4bBUQM4uGYEsp8p9N_3XkTl55YZUrLEUtZHyndlUsK_NUitVpBH4P6ZdtJgb7NzFG4BXqM81SKemuVvaza3tco4dyx_ko0614Nx2aLocazdDS7D5mEOee4Cd_VrIZgWwppDkf6igZr6aQHclnf-obSPcAcJJxyzPnXRffQShg6A8nU_qLZpe7eLniHQ68vNUsIWHvuMtG3EpQAtcldxql5FlhElGVLIGccGsJESyQGK3eXzG90LCB0oK51NldXhlj6LURhRpfQH05oKz0GDkUdNw8QU3A-Uh7BYrDCSyI_zilHmOKKyvNRhvS6Y8nq-TOesc06pkfZ03B_bpOv2gI7quWxNnfpWM24q_aw8uILCaVKw_2f5JSiqfQPe8BVkTaY8sOoE9v5vnTUo9pOliQ9wio6mzNT47XGN48lc6P1FJjIk6xL-huOpVAuiFlHj4EE5ah6QUT-4TnmXaeN8jhuDLEYpSkm6lCO8C8dxVmZdSbb_CgTjSekrRirQvf4JqV9A3cCkZKh27Lef3mdU2aEjtufsxcfLKYUky3jMkyUT2h4W4JAsotXreK047CMfwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما هواپیماها را وسط تهران به پرواز درمی‌آوریم و آن‌ها حتی خبر ندارند. تمام رادارها و پدافندهایشان نابوده شده. آنها تمام شده‌اند... برایشان سخت است چون مغرور هستند. ۴۷ سال قلدر خاورمیانه بوده‌اند...
ویدیوهایی است از
این مصاحبه فاکس‌نیوز
با ترجمه و زیرنویس هوش مصنوعی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76228" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy01zYwzCj9le3yMnGZShuj0CLcn7I67DOJRWnGse8Ng8G0OeZas5428vvUFVZ3jcvaDJXu7ywUdd0GsPHwey4oaUrJQG1CyQK4wFZ2whJUJlAxzb8-xPYIQPUSi8Vk8giJ5vhq0QEksY4cCIQqKLLKBYkNnBy9W30EEjKpWRiGx-iVUDsJNyEs9TsCrrhPshjWMGsBoz5U4EWfEoPEqd49NicHGnWC5121TVCkmNOjrtyK81pLKUFJeg3G5Ex72AUsuTlmUOBrbGfCUi9B1f6M6N_8y8j8jzwb2tfLOKuhk6GbwZdXczmL4_0Ta57ZxiGr6Oty63S6YTfZqqIaOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ به نقل از «منابع آگاه» گزارش داد که مقام‌های ارشد امنیت ملی امارات متحده عربی و ایران برای نخستین بار از زمان آغاز جنگ آمریکا و اسرائیل علیه تهران، حضوری با یکدیگر دیدار کردند.
این دیدار که در هفته جاری انجام شد، به نوشتهٔ بلومبرگ، نشان‌دهندهٔ چرخشی قابل توجه در رویکرد دو طرف است و در شرایطی صورت می‌گیرد که هر دو کشور بیش از پیش به اهمیت روابط دوجانبه آرام‌تر پی برده‌اند.
این خبرگزاری می‌گوید که منابع آن به‌دلیل حساسیت موضوع نخواستند نامشان فاش شود.
بر اساس این گزارش، رهبران امارات می‌خواهند برنامه‌های بلندپروازانهٔ اقتصادی خود، از جمله سرمایه‌گذاری میلیاردی در افزایش تولید نفت و ایجاد مراکز دادهٔ هوش مصنوعی، بدون اختلال ادامه یابد. این رابطه برای تهران نیز اهمیت دارد، زیرا امارات پیش از آغاز جنگ یکی از بزرگ‌ترین شرکای تجاری تهران و مسیر مهمی برای انتقال نفت تحریم‌شده ایران بود.
به گفتهٔ منابع بلومبرگ، تماس اخیر ابوظبی با ایران عمدتاً با هدف دستیابی به نوعی تنش‌زدایی با حکومتی انجام شده که آن را دشمن می‌داند.
از زمان آغاز جنگ خاورمیانه در ۹ اسفند پارسال، ایران بیش از هر کشور دیگری امارات را هدف حملات خود قرار داده است.
ابوظبی نیز در چندین نوبت پاسخ داده و در میان همسایگان عرب خود تهاجمی‌ترین موضع را در قبال ایران اتخاذ کرده است.
با این حال، به نظر می‌رسد امارات اکنون مسیری مشابه قطر و عربستان سعودی را در پیش گرفته که با وجود هدف قرار گرفتن توسط ایران و نیروهای وابسته آن، در پی کاهش تنش از طریق دیپلماسی هستند.
به نوشتهٔ بلومبرگ، عربستان که تأسیسات انرژی و پایگاه‌های نظامی‌اش هدف قرار گرفته، از اوایل ماه آوریل تماس‌ها با تهران را در سطح وزیران خارجه از سر گرفته است.
قطر که تأسیسات بزرگ گاز طبیعی راس لفان آن هدف حمله قرار گرفت، بیش از همه در پی آشتی بوده و اواخر ماه گذشته میزبان هیأتی از ایران شد و به‌طور فزاینده‌ای به‌عنوان میانجی میان واشینگتن و تهران نقش‌آفرینی می‌کند.
بلومبرگ تأکید کرده که هر سه کشور عربی به ضرورت همزیستی با همسایه‌ای در آن سوی خلیج فارس، با جمعیتی ۹۰ میلیونی و توان نظامی قابل توجه، واقف هستند؛ حتی با وجود خسارات گسترده‌ای که از بمباران آمریکا و اسرائیل متحمل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76227" target="_blank">📅 19:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0U2XyWEvWpkNwnP7UL3TXBmV4lMcOMYmvozGTShqW3YiBncWaVtSNx6qdpDKd0TpL1p2qgh14XOSXALeaCBbt49kTgI8Qw2cG9SnUvhoz8N_Vkgp0hmnmCtK4jDG211l-94X1JJqSO7e3s7h1daRa9rpZSE5ySDez4aBEMYOUgdRK0xIFya6wYfWioDzqQjLho7nQb0i_DcxJUuTzdludYXiwuzoJr-d_ZfvCitYOUwjIT-FaWXvYOeE1s6v3bUMcBSZZafJy4bZvchbNDGAiER60hBMOJN1tYHwQd7Mpbw6GBogUGrAh-Z2DKEKSTtSTenm0-yef9FbWXGysmsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان روز پنجشنبه به نقل از یک مقام ارشد پنتاگون و دو مقام دولت آمریکا اعلام کرد که طرح‌های ارتش ایالات متحده برای تصرف جزیره خارگ در جنوب ایران از «ماه‌ها پیش» تهیه شده، اما به دلیل «بیش از حد پرخطر بودن» کنار گذاشته شده‌اند.
دونالد ترامپ، رئیس‌جمهور آمریکا، ساعتی پیش از تمایل خود برای در اختیار گرفتن این جزیره به عنوان یکی از مهم‌ترین زیرساخت‌های صادرات نفت ایران خبر داد.
سی‌ان‌ان به نقل از مقام‌های آمریکایی نوشت: «دیدگاه غالب در کاخ سفید و پنتاگون این است که تصرف جزیره خارگ یا نابود کردن زیرساخت‌های انرژی این جزیره، عملاً ایران را ورشکسته خواهد کرد و توانایی‌های آن را تا حدی کاهش می‌دهد که دیگر قادر به ادامه جنگ نباشد.»
در عین حال مقام‌های دولتی به رئیس‌جمهور آمریکا گفته‌اند که چنین عملیاتی نیاز به نیروهای زمینی پرشمار خواهد داشت و «ممکن است به تلفات سنگین نیروهای آمریکایی منجر شود».
سی‌ان‌ان ادعا کرده که پنتاگون و کاخ سفید هرگونه اقدام برای تصرف جزیره خارگ را به عنوان یک «گزینه نهایی» در نظر گرفته‌اند؛ اقدامی که به گفته مقام‌های آمریکایی «می‌تواند موازنه جنگ را تغییر دهد، اما هزینه بسیار بالایی خواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76226" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDbGiMLd8yESiX44Wz_tQdi1keYvhg7ScsrZucvOV3cEWJQ9DUBEGPVAF6sCO_xyOcq0uXFg7Vrrt-2MxvYB_kh7BbEWJpPtFo6KOvBBX2S8c5vIlv_MuHvNNcsf9U_FneQyshLiMLjWaaniToKRzE1uBLWZC8JBPOK2wAIRlmI2oU0lMjr5TqGRpW13BFgFKZ20XnD2JjDMX-JYJEIlYeN5SjNICPxm7SzwxayHE90A0SjunMlTQ3vNNn8kG-5gjUy14OE-lvt5umRa-471_w69-s_C_uPgCODAeE3JiK8JIaPsaNvgxnMXaF6qQA7jyta8lKbSKi7mep0uJFKaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
راهبردهای نادرست و تصمیم‌های شتاب‌زده، کل صحنه را به شکلی بدتر از نو تنظیم خواهد کرد، زیرساخت‌ها و بازارهای انرژی را منفجر خواهد کرد و باتلاقی بی‌پایان خواهد ساخت که سال‌ها در آن گرفتار خواهید ماند.
شما با ایرانی متفاوت روبه‌رو خواهید شد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76225" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYGCFSPeCijWph1Rfpz8PAVXG4utb1Z-ELw1f5VeFJ69LJfL4Cpo9k3emHqARDtXaooCsNa207vsx_5fT_CXaXer_oV-ybOdF_h7vjyGgCtLYm06WyMUsIgnvstBn45rlfFHU2ldOtZ93ZPBYykMTpNOkSIm1yWpRbRxArs6fOEN7ezlEPN8bs3OsQwjlKXJvjTuYgzDahQniexmoaMYjnnlTZxUANsqkoJyrsI4Iqgr4dLBzdP_1kvzjmBNQh5EO3CyfuM3XjLxKPNa-8UU-wpyEibKrjtNzTpmVYgoWPaSIeCWji41ln5EqzvWS0e_wxXLhUT2zDDj-TOsSazJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آتش‌نشانی و امداد و نجات شهرستان آرلینگتون در شبکه اجتماعی ایکس اعلام کردند که ماموران آتش‌نشانی در حال بررسی حادثه‌ای مربوط به مواد خطرناک (Hazardous Materials) در ساختمان پنتاگون هستند.
شبکه خبری سی‌ان‌ان نیز به نقل از منابع ناشناس گزارش داد که این ساختمان تحت قرنطینه و تدابیر شدید امنیتی قرار گرفته و کارکنان چندین طبقه از آن تخلیه شده‌اند.
در همین حال، سخنگوی پنتاگون در این باره اعلام کرد: «پنتاگون متوجه مشکلی در کیفیت هوای ساختمان شده است که تا زمان تعیین میزان اهمیت و خطر آن، اتخاذ اقدامات پیشگیرانه را ضروری ساخته است.»
او در ادامه افزود: «وزارت دفاع در حال اجرای پروتکل‌های حفاظتی استاندارد است؛ این اقدامات شامل صدور دستور پناه‌گیری در محل (Shelter-in-place) برای بخش‌های آسیب‌دیده ساختمان می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76223" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک صداهایی شنیده شده. گویا بیشتر در غرب تهران
پیام‌های دریافتی:
سلام وحید پونک سردار جنگل همین الان انفجار وحشتناک
۱۸:۲۹ یه صدای وحشتناک سمت پونک اومد
داداش صدا اومد الان، هوا هم ابری نیست، شمال تهران
سلام غرب تهران (صادقیه) ۳تا صدا اومد
توی پونک اشرفی اصفهانی صدای انفجار اومد
صدا میاد شدید ولی هوا صافه
سلام وحید جان
تهران ساعت ۱۸:۲۹
صدای چندین انفجار پشت سر هم
من از محدوده تجریش شنیدم
سلام‌ وحید جان
خیابان جلفا ۲ تا صدای انفجار اومد از دورتر
ساعت ۱۸:۳۰، ۲۱ خرداد
اندرزگو یه صدا خیلی دور اومد
شبیه رعد وبرق ولی ابری نیست
سلام آقا وحید تهران انفجار شد یا توهم زدیم؟
میرداماد همین الان صدای انفجار اومد
سلام وحید جان ساعت ۱۸:۱۷ ما سمت مختاری هستیم اول خیابان ولیعصر صدای انفجار اومد ولی خیلی نزدیک نبود خیلی هم دور نبود
صدای موشک و‌انفجار بود انگار
نمیدونممااا من از صداش خواب بودم خوابش رو دیدم بعدش بیدارشدم صدای انفجار شندیدم
من غرب تهرانم بقیه رو چک کن
سلام وحید جان اگر گزارش صدا از  تهران شنیدی ۹۹٪ رعد و برق هست ابر خیلی کمه مردم فکر میکنند انفجار هستش
آپدیت:
گویا صدای رعد و برق بود.
بلافاصله بعد از انتشار پیام‌های بالا یهو ده‌ها پیام اومد که صدای رعد و برق بود.
آپدیت: حالا بعد از این آپدیت هم شهروندانی دارند عکس می‌فرستند که هوا به این صافی رعد و برق کجا بود.
ولی برداشت نهایی من از اون همه پیام‌هایی که نقل نکردم همون رعد و برقه. آسمون هم همه جا صاف نیست.
آپدیت: بعدش هم برای خیلی‌ها که شک داشتند واضح شد که رعد و برق بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76222" target="_blank">📅 18:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=usUHSXlVsqBEc0QRf-3JbjOex7fykMcZIAKttTmKHYLl-7R6cSTbgN2qERUL67UGGkfI-H1OIcrOjCjW9JHbn_8Rb21YJxDDxcocyqGqu1OdkeU4XfQahfH9jCcpt3pdNq91FP0DFF7n7auOgI3NaFzio8AfZWTrO2pgteab-NNumaGe03edR6J7_fDd3JEDMNtwLVtP5T3hx8WNzYP3pXy62RGvBnwabRlit0oJ4GQwRnJ09Lm77U5xBt2WK_DYMV9QiAcIjiW31XP3EvJkCW0D0js8PoH3OGsE46OHKw4OOXUgZ6hOSlaWpKtamBM0rMh8ir4dlTDQo1H0Frg3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a23ead45.mp4?token=usUHSXlVsqBEc0QRf-3JbjOex7fykMcZIAKttTmKHYLl-7R6cSTbgN2qERUL67UGGkfI-H1OIcrOjCjW9JHbn_8Rb21YJxDDxcocyqGqu1OdkeU4XfQahfH9jCcpt3pdNq91FP0DFF7n7auOgI3NaFzio8AfZWTrO2pgteab-NNumaGe03edR6J7_fDd3JEDMNtwLVtP5T3hx8WNzYP3pXy62RGvBnwabRlit0oJ4GQwRnJ09Lm77U5xBt2WK_DYMV9QiAcIjiW31XP3EvJkCW0D0js8PoH3OGsE46OHKw4OOXUgZ6hOSlaWpKtamBM0rMh8ir4dlTDQo1H0Frg3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'لحظه انفجار حمله حدود ۴ صبح به پیشوا در استان تهران'
ویدیوی دریافتی، پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76221" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZN4iX1mej5fTJKZ3rvLc7lBl0kcB6z8vAj9-PZ4fSWgaAsxMn_csADqatnF71sKMgDaLHDKnSBL2TTR7hZWjOSRSKiDCcoo1j5m74IEHXpSCwhuai_y2b1Ioq4Edh1MML2B85J7G_gwP87X4G5djuwm6d-JfzRfPPNExUfU1bvCK1qATo_UkEKffl31QCUv9FLKSX0njRyC9SIqN_jlaXjKe4UEV_JGUWDLOZDTYeHjBNCGLCH_cwGhgPg80Z9INtFPAokJnY4NcQAm-yzARbCOxCRvdM9T07iDOvKBkQr8tEgsyUg1tWsTuXFAnLnsp-e5OWKaWyoCXAsxIaBoFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RDDya00e-Z1rxCUvfPdGQytX4NzYikNsmgmizLePcvVfYwX0VeqXrnvW3q0BdBPrdBtosVfwTsHkq9dC2pXX2JahzBURbGEHEULDTeBnbnft3gVFthUGAqlhUTwkXfi6GDtKClQ7ZxdTXqYFpU3NmoM8SG4Dp8NcvRyFTAmVa-QIXEzbZDWElOYcZoZeCYNkjT4WACrw3oN5z4Dh1U0s_0FLR4CCA400_rzbcbr6MsWEW6_2OiOqsKU608BqM2oj6UgqIHfwPVjfdRRSQxwKeD1DBRD24TVgjbHlUB9SO8LY8h_oFgT2JRaDKUlNeSn7sAbijmbVEErJEOxSQ5Mqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tge2OIYVpzv_J15vV7PTQKEvvpM353SFWyUc8w0Dj0XsgCX0qD4_lNQ4dUtzGH79mvOD98JMxei1hZ3BBt52qkxTNoKA6JaRcIFVCnWPkYKK9o2X9oITxSiVUhi9U__6O4aBZOHRkx8CppRBDM2x_f7c0llCMf8pSXVgB8L66zbuYHNT9T4FNf3ZQe3Wd3uMmQes9PvqHRFGTZbZjw98vwB26IyYvjxgpGbbM4ibA4DbOSzjW51mQrjG2pWtHQYQ7UqeQ-eUesGUFmHTYLSukeoZS0COy0SQWKOpPB5o9ZL19uhBq5te4eT3o1ufASs6Kk1WR2b_EwCrboB6yeCxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/caQkeTn1hEu7HSetnl_ppNJP51naWvj1evEAwhE_C5b1_0LbcPwHwoDvEd0ZgAZg4eXwlVuwIj_lZHh7iiS6N9bJPTlR1WR1cShzB0XgAHwnNXDRjianoSWU5ctiz9isOTLXaRVvj6Ccb5M4G497XvhOawUvQqdxx5ouwvSCV7F6Yx_HIKaQ1YYrlbI3rKP6rHa0aqrOJtj2eVQGECZ0VSj8skFErsPYRm0BOBSBMO1yOhM8daerHEEx4ztmpvvANL40sBRK3cw37qWq8TWk0wRAtuYb8ePypIvMCuvOTESn-Q1DEjArfM9R3X7o_tSBNEyh4kQ3OFan523ow1AjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CV7VlqV2ZcbkFA8rKywK0eqvoNdkbkJRMm1bTTlVkGTRiemjX20TT14i2gLcgTR6HoWCl72brAw9N87-gMzGLn-ZnkTDeS98_99J64J3IilssEKYGmQv_WY-_M7wZjXNXOOoNei-UUBG8ln86YrbD60K-6YYDTJ5InFm9MGLfGxtK0xkIOnMDEE4uMV2EKWNapKEmmoQLlp7Ts2vnpuQNHBjyV4R4vzITiMwL5UvA8dRJO2zWXTku7l_L1I0hY8c0bfxdyjHvskYrh0qnzEhsa0PW-tXP0rBQbW8Ac-ck-EyWWRPqIDaH9JVcwRO54Hxbj_Xd5W6J_IK7gd7G6xO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pVf6Ie-rsBV9SJSakUR-8NtNV7IZJOcUCDE7afTXdO1kh1GwBUQ_W2Z_w2TvMiU0UGkzgDN-Q9vvGLbEHhRmWY_bWhtwqWrF3tIp9HH4s-eVaA27tVznzuPeCQwLHMEitV25utTfs9bNYQkBIeUhrz5I_hR2sYS0rtGaPu10079NXV8BbHrEaILd6K6dxiJW9qwWxbvdBOt_bU0cwbc8efriULLJh9vBQCnkUKtbBBKoz4eFSpVFanZoCT9FFo9vAY6X9PqKMZ7UXlmhAHtJkbnjAYPRDHY6RWGLgOOtMIpbunAGXwLrtYPoeoZw6_YHYBIpvYPez54GZIRwAv1fzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=eeI5Xh7NLR4gRcfDHBx--a3PTC0_6jNZww0Zic9aMeqq-rzAvbZe00Z0kLZtfBRN2qIAeuc7zLqZKgu9799Yo-Ytv9av2jlYEqXSaGLIRhGYfuPAXbWY-4dP8xyBr6u6u99Oid6mWCnYrWVu_FAZAORXIwmH-PUWb8dkV7mWaEbyjsiNCqwBL36oIHLOfQ7tKVBHtnFjFCPeiVuDdsPFiOTiQhN7ri1idRkm6lopi0ZmuUpY2xzrrqAnpySe5qWw7vQ7yKmzYl6-63c4tPCxTtVB9_nnbDMKC5msv4Wo-qd2q_tph8gGiRFIrUG_M1ynSlP5SF1AACPAvvwBKhEv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4acc6e36de.mp4?token=eeI5Xh7NLR4gRcfDHBx--a3PTC0_6jNZww0Zic9aMeqq-rzAvbZe00Z0kLZtfBRN2qIAeuc7zLqZKgu9799Yo-Ytv9av2jlYEqXSaGLIRhGYfuPAXbWY-4dP8xyBr6u6u99Oid6mWCnYrWVu_FAZAORXIwmH-PUWb8dkV7mWaEbyjsiNCqwBL36oIHLOfQ7tKVBHtnFjFCPeiVuDdsPFiOTiQhN7ri1idRkm6lopi0ZmuUpY2xzrrqAnpySe5qWw7vQ7yKmzYl6-63c4tPCxTtVB9_nnbDMKC5msv4Wo-qd2q_tph8gGiRFIrUG_M1ynSlP5SF1AACPAvvwBKhEv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری آمریکا دقایقی بعد از انتشار
این پست
در برنامه صبحگاهی شبکه خبری فاکس حاضر شد و درباره این پست و تنش‌های جاری و فزاینده میان ایالات متحده و جمهوری اسلامی توضیح داد.
🔻
«ترجیح من تصرف خارک است»
او در این گفت‌وگو تاکید کرد که شامگاه پنج‌شنبه حملاتی شدیدتر از شامگاه چهارشنبه، ۲۰ خرداد در انتظار حکومت ایران خواهد بود.
او با اعلام اینکه در حملات چهارشنبه «۲۵۰ میلیون دلار» بمب بر ایران ریخته شد، افزود: «آنها [حکومت ایران] واقعا در حال تسلیم شدن‌اند، فقط هنوز خودشان این را نمی‌دانند.»
او هم‌زمان گفت واشینگتن همچنان با تهران در حال گفت‌وگو است.
ترامپ در پاسخ به پرسش مجری برنامه درباره تصرف بخش‌هایی از ایران گفت ترجیح او «تصرف جزیره خارک» است، اما تردید دارد که افکار عمومی آمریکا آمادگی پذیرش چنین اقدامی را داشته باشد.
او افزود: «با این کار ثروت هنگفتی به دست خواهیم آورد، اما فکر می‌کنم مردم آمریکا دوست دارند ببینند ما به خانه برمی‌گردیم.»
ترامپ در ادامه تصرف خارک و تاسیسات نفتی ایران را با تجربه ونزوئلا مقایسه کرد و گفت آمریکا «میلیون‌ها و میلیون‌ها بشکه نفت» از آن کشور خارج و به پالایشگاه‌هایی در هیوستون، لوئیزیانا و دیگر نقاط منتقل کرده است؛ پالایشگاه‌هایی که به گفته او «شبانه‌روزی کار می‌کنند و ثروت هنگفتی به دست می‌آورند».
ترامپ گفت از اجرای همین الگو در مورد ایران نیز استقبال می‌کند، اما مطمئن نیست «کشور آمادگی آن را داشته باشد».
🔻
«اکنون تمایل کمتری به توافق دارم»
ترامپ همچنین گفت اکنون نسبت به سه یا چهار هفته پیش، تمایل کمتری به دستیابی به توافق با جمهوری اسلامی دارد.
او افزود: «نمی‌دانم آمریکا آمادگی انجام کاری را که من واقعا ترجیح می‌دهم انجام دهم، داشته باشد.»
در بخش دیگری از گفت‌وگو، مجری فاکس‌نیوز از ترامپ پرسید آیا از جمهوری اسلامی عصبانی است؟ او پاسخ داد: «من عصبانی نیستم. من عصبانی نمی‌شوم.»
او درباره توافق هسته‌ای مورد نظر خود گفت: «توافق من راهی به سوی نداشتن سلاح هسته‌ای است.»
ترامپ افزود که ایران نباید اجازه داشته باشد سلاح هسته‌ای «توسعه دهد یا خریداری کند» و گفت در متن توافق پیشنهادی او، هر دو مورد گنجانده شده و حکومت ایران نیز با آن موافقت کرده است.
ترامپ همچنین مدعی شد «کار حکومت ایران تمام است» و افزود: «آنها دیگر نیروی دریایی، نیروی هوایی و پدافند هوایی ندارند.»
او همچنین اشاره کرد که هواپیماهای آمریکایی بر فراز مرکز تهران پرواز می‌کنند و مقام‌های جمهوری اسلامی «اصلا نمی‌دانند ما آنجا هستیم».
به‌گفته ترامپ، آمریکا همه رادارها و سامانه‌های پدافند هوایی جمهوری اسلامی، بخش زیادی از موشک‌ها و بیشتر پرتابگرهای موشکی حکومت را از کار انداخته و توان پهپادی آنها نیز «به‌شدت کاهش یافته است».
🔻
«نمی‌خواهم نیروگاه‌های برق آسیب ببینند»
در ادامه، وقتی مجری برنامه از احتمال هدف قرار دادن یک نیروگاه برق پرسید، ترامپ گفت: «بله احتمال دارد، اما ترجیح می‌دهم این کار را نکنم، چون وقتی چنین کاری می‌کنید، مردم رنج می‌برند.»
او همچنین درباره تاسیسات آب گفت قطع آب «ضربه‌ای ویرانگر» برای مردم ایران خواهد بود و افزود: «می‌توانم در یک دقیقه بگویم آن را از کار بیندازند، اما مشکل این است که مردم دیگر نمی‌توانند آب بنوشند.»
ترامپ در بخش پایانی این مصاحبه کوتاه گفت مردم ایران از اعتراض می‌ترسند، زیرا به گفته او «سلاح ندارند» و طرف مقابل مسلح است. او بار دیگر طی ماه‌های گذشته به کشتار گسترده مردم در اعتراض‌های دی‌ماه اشاره کرد و گفت نیروهای حکومت ایران به معترضان شلیک می‌کنند و وقتی مردم با مسلسل یا تک‌تیرانداز مواجه باشند، برگزاری تجمع دشوار است.
او اظهار کرد جمهوری اسلامی دست‌کم «۴۰ تا ۵۰ هزار نفر» را کشته است و افزود نمی‌توان مردم ایران را به دلیل ترس از اعتراض سرزنش کرد.
🔻
«از کردها ناامید شدم»
رییس‌جمهوری ایالات متحده در ادامه گفت آمریکا برای مردم ایران سلاح فرستاده بود، اما از کردها «بسیار ناامید» شده است.
او افزود با تحویل سلاح به کردها مخالف بوده و باور داشته است کردها این سلاح‌ها را تحویل نخواهند داد.
ترامپ گفت: «فکر می‌کنم آنها سلاح‌ها را برای خودشان نگه داشتند. این مایه ننگ است و من این را به یاد خواهم داشت.»
گروه‌های کرد مخالف جمهوری اسلامی، از جمله حزب دموکرات کردستان، حزب کومله کردستان ایران، حزب کومله زحمتکشان و حزب آزادی کردستان (پاک) در هفته‌های گذشته دریافت سلاح از آمریکا را تکذیب کرده‌اند
.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76214" target="_blank">📅 17:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apQVv5VMxcj18ohz9sCV32Y4uF02g3xj_WDsWM8XA2qN8I0LVHTXINwWbgiVb3KfwgzUVsN0AejjCTb5ryKDXBd6mjjbwj70ausHh2R_fKIo31iGrl6b8IFd86N96P-usPJ46kN9cAuF-C7JhJ66Qq_Kx7UH9EY7Ur4rFiZx__UxuycJir0bsKECb4rKsfVyFhWZLHwhoUwWDeqGXrkSpFxzIA_BOgeSgroS_u1wblxOZPb3epw_9hnNLA6Ybx3LAn5pGAkfJ2dxYNlZ2sv1YHS6bVafQP078hQ9RGvYAEk5w_ndyKVhTajgP33bBXoyTXetiIsOzvc8OJuoPPOaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکات بسنت»، وزیر دارایی ایالات متحده، در شبکه ایکس نوشت که جمهوری اسلامی ایران در «بازی با حاصل جمع صفر» شکست خواهد خورد.
بسنت در این پست توضیح دادکه خساراتی که حملات موشکی و پهپادی جمهوری اسلامی به کشورهای عربی به‌عنوان «متحدان آمریکا در خلیج فارس» وارد می‌کند از محل دارایی‌های بلوکه شده در آمریکا برداشت خواهد شد.
وزیر دارایی آمریکا همچنین نوشت که هرگونه عوارضی که از کشتی‌ها برای عبور از تنگه هرمز دریافت شود، با برداشت از حساب‌های ایران جبران خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76213" target="_blank">📅 17:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmrFXpgYBVtuRlDcBQ1DlYypoL_P3OgJScjULyKijPoOIXZXeTYcq9ukpDjbb_59eFi0ZvusMPaVivlOfcG58Ms9-GSddS8sZbXSeOVWEe4RY8_0m7UFRvTxu88aW7BnuxyjP9pW7CFIGSxickbCmS0DjX6gR5_NhsRKg_XKJRhQVsaNIOfn9ixYbPERWIg7ttO4ma1_VU6kyi1O1Uy4AGlIR--AG-z95JiTZzP5uRqjQkt--oun5jGQUrafyIs7V8lP8pzoVo_nYKt47dUx-UCmBOyyoCAlnBsobj-RrBemk7TqPnleMUE8g3jbrkZ2H1awYZ3l0VDfUKCm18TjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز پنجشنبه اعلام کرد که ارتش این کشور امشب بار دیگر ایران را به سختی مورد حمله قرار خواهد داد و از برنامه ایالات متحده برای به دست آوردن کنترل جزیره خارگ ایران خبر داد.
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروث سوشال نوشت: «ایالات متحده امشب ضربات بسیار سختی به ایران وارد خواهد کرد؛ کشوری که نیروی دریایی، نیروی هوایی، سامانه‌های راداری، پدافند ضدهوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش عمده توان تهاجمی‌اش، از بین رفته‌اند!»
آقای ترامپ در ادامه پیام خود نوشت: «در مقطعی در آینده‌ای نه‌چندان دور، ما جزیره خارگ و دیگر زیرساخت‌های نفتی را در اختیار خواهیم گرفت و کنترل کامل بازارهای نفت و گاز ایران را به دست خواهیم آورد؛ همان‌گونه که در مورد ونزوئلا انجام داده‌ایم، اقدامی که نتایج فوق‌العاده‌ای هم برای ونزوئلا و هم برای ایالات متحده آمریکا داشته است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76212" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj4LoyFPJb5x0WHSvuoTnUiyNQxDtsScY_kGD5h36q0OwiBIWXdcQ7gI9yVANbl81l4T_HRR0jBsq4gQyTvMy4D9rpSjtzQcTxOaRMtZIplWNLcx5nhr8oR3yx6-AL1nK5zWm3R61Q28LGOLK5Cs_UpR1TFYw0O1JlyyTkiv7CK3iu2s5t7RsCooXdHsI96hcz6KVEzrK0WkYeXA5pywSpJIorxwiorTTekI4FY5W_GSPQ7ZtJTPZwWgBw1VHcxTeNeFLvBv5qAqyuRRYjTvjkeTE5qXRqXpo4IwI0eARO5e_0Ey8uPyjblSyS2Ff3nBvjdLaP2t3eGrTDGCaBAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل متحد، آنتونیو گوترش، در پیامی تازه درباره وضعیت خاورمیانه هشدار داد که این منطقه «هر روز بیشتر به سمت بحران عمیق‌تر کشیده می‌شود» و تأکید کرد پیامدهای آن فراتر از مرزهای منطقه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76211" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFgZo-s4VNbCxbESWifPdCUUdiDLRcRJPPnvqSzHSFE49fj2bQf-yewBxSqHwkXULTKSsayxR2g-vTn4DRY8q2XettvVi-Vnab7MxfD3veo-SXuBAoDT2Rm_7enMujdnwnq5CTNV-7ff74-GAfQEDDPny4DvRgk-U4Tge1uqIB0c9W72t-A82aT28xN0K0Qo4wMZj4HZqHc1vVBwI1-QrUBoIM_QIzzwUSjAIi-D5m1DYrtdge4LFkM88ydC0qOnhOgQIjhRrY43cVB1O7pQNJytOC2iDVM4JYHwmvM1l_HBAfLc8_xNQ-hjWxOleJ1eOw6xXY9Dqgh6uj00hxdRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی با صدور بیانیه‌ای در واکنش به حملات ارتش آمریکا به اهدافی در ایران، این اقدام را نقض قوانین بین‌المللی خوانده و گفته است این حملات آتش‌بس ۱۹ فروردین را عملا بی‌معنی کرده است.
در بیانیه وزارت خارجه ایران بار دیگر به کشورهای حاشیه خلیج‌فارس درباره استفاده ارتش آمریکا از قلمرو، امکانات و منابع آنها هشدار داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76210" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d46260783d.mp4?token=I-k8GMfSiLsyDmYCQ94h2i-8pT4iTDWSUo3s1u8Kt6DlD8SkUXLIau_hLhsLjUpkSjmR1aE9UQNReYI2XdHxFFy-eURqy2B4oz6gKZIUzizBnyD0XPxrpTovuFcm5nwxypF6emL8URkzl5EiJMInZg3wLrKI97Rp-Mxjoga4fk26yLkaHQsd2Tb-I7c3tj2vigrMjKjnWvjhPXOJMvroZQ99rpsfv0zNNyLiIb4tg8-NeSFlYUFgCOT2epJPMHhdcnQaQ_DXw_cik73vPLa3XFSdyIZp4u9yVAKrgxPjASjM2UG0_SleCDGMRBJXCbyRxm85MkFrhEUxSi4Gj_p1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d46260783d.mp4?token=I-k8GMfSiLsyDmYCQ94h2i-8pT4iTDWSUo3s1u8Kt6DlD8SkUXLIau_hLhsLjUpkSjmR1aE9UQNReYI2XdHxFFy-eURqy2B4oz6gKZIUzizBnyD0XPxrpTovuFcm5nwxypF6emL8URkzl5EiJMInZg3wLrKI97Rp-Mxjoga4fk26yLkaHQsd2Tb-I7c3tj2vigrMjKjnWvjhPXOJMvroZQ99rpsfv0zNNyLiIb4tg8-NeSFlYUFgCOT2epJPMHhdcnQaQ_DXw_cik73vPLa3XFSdyIZp4u9yVAKrgxPjASjM2UG0_SleCDGMRBJXCbyRxm85MkFrhEUxSi4Gj_p1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا سومین نفتکش ناقض محاصره را در خلیج عمان از کار انداختند
تامپا، فلوریدا — نیروهای آمریکا ساعت ۱۱:۲۰ شب به وقت شرق آمریکا در ۱۰ ژوئن، پس از آنکه یک نفتکش با تلاش برای انتقال نفت ایران محاصره علیه ایران را نقض کرد، این شناور را در خلیج عمان از کار انداختند. این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی از کار انداخته می‌شود.
فرماندهی مرکزی آمریکا، سنتکام، علیه نفتکش
M/T Jalveer
با پرچم گینه بیسائو اقدام کرد؛ این کشتی در تلاش بود نفت را از ایران از مسیر خلیج عمان منتقل کند. یک هواپیمای آمریکایی پس از آنکه خدمه کشتی بارها از اجرای دستورهای نیروهای آمریکایی سر باز زدند، دو موشک هلفایر به اتاق موتور کشتی شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی به‌ترتیب در روزهای دوشنبه و سه‌شنبه دو کشتی با پرچم پالائو، یعنی
M/T Marivex
و
M/T Settebello
، را از کار انداختند. مارویکس با تلاش برای حرکت به‌سوی یک بندر ایرانی محاصره را نقض کرد و ستبِلو نیز تلاش داشت نفت ایران را منتقل کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام ۹ شناور نافرمان را از کار انداخته‌اند، ۱۳۵ کشتی را که از دستورها پیروی کردند تغییر مسیر داده‌اند و اجازه عبور به ۴۲ شناور حامل کمک‌های بشردوستانه داده‌اند.
این محاصره به‌طور بی‌طرفانه علیه شناورهای همه کشورها که وارد بنادر و مناطق ساحلی ایران می‌شوند یا از آن‌ها خارج می‌شوند، اجرا می‌شود؛ از جمله همه بنادر ایران در «خلیج [فارس]» و خلیج عمان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76209" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQc6fvuye4yNXI3zQKc0xigjloj6ttBruxd9v2qqq3g79vfEY9KlGt3k59CMXLEaLJekgvLPH8tIimy05Utw6131GAoF2THVYvhXrZwgWqbv8eI2Ellewv_wVVHXiA_X2ALNhnU4l71tHGS3LYCRRIf6-rZ5D7bKnqHcgC_7KL4aTDqOQvJV2KbaFS_V6s-qjX9UgxgQjWZI6OYQatGxpUT54cTvEkp2z7V7eKtGbIoh525KpLXNpk_PUMOQLSKEkrDcD1ccJ9yMyz7c16aTwqTP-td2P7ehMJhJKY92_vrq_y40tfXpDO5oHx7WuhkfF-R3GvVp71NdB8jkL_6_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرحیم سلیمانی اردستانی، عضو مجمع مدرسین و محققین حوزه علمیه قم، توسط دادگاه ویژه روحانیت به شش سال حبس، خلع لباس روحانیت و پرداخت جزای نقدی محکوم شد.
نزدیکان آقای سلیمانی اردستانی اعلام کردند که وی تنها به شرط برگزاری دادگاه علنی حاضر به اعتراض به این حکم است و در غیر اینصورت، حکم را بدون اعتراض می‌پذیرد.
او به اتهاماتی چون توهین به مقدسات، توهین به علی و مجتبی خامنه‌ای، توهین به مقدسات تشیع، توهین به مراجع دینی و هتک حیثیت روحانیت شیعه متهم شده است.
سلیمانی اردستانی در فروردین ماه توسط نیروهای امنیتی بازداشت و به زندان ساحلی قم منتقل شد.
او پیش از بازداشت و در تحلیل نخستین پیام مجتبی خامنه‌ای که به تجلیل از علی خامنه‌ای پرداخته بود، نوشت: «مهم‌ترین هنر والد شما این بود که مخالفان و منتقدان خود را بی‌بصیرت یا مزدور بیگانگان می‌خواند و هر برخوردی را با آنان روا می‌دانست! از صفات اخلاقی ایشان دو صفت لجبازی و کینه‌توزی را بسیار برجسته یافتم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76208" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lem28L1XEr0ojtvrSDaw35s-luUeeWv9KJwb_ei0Tm54-H0Pom10OUWK8liEXmnl3oFh-fAWcJ7KhdwoOg3-jPnRXiU_IOlt3_dNoEZe1Rvsr94-rE0XKAHZJOpCMX_cyKCDt-363n2iFcVus06uXiW9f7rokY2Qw9ammFptw1vTuE-jaaor01cWpjQKybDAQBu09BO4SFrpfUNOFz0ctcz5Jag5OP7Mkke6122mz2kjPLsM3T7npFykAIR56h7LvPVRmk556iu8hXOQHI75dVysLbCFqZanSbKWo8v2PmLK4c8xmZyYnrusMczUT9h29S_Sde48FVMvNmS-a8x5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی از پیشوا در جنوب شرق استان تهران
'دود انفجار حمله حدود ساعت ۴ صبح که در ورامین و پاکدشت هم احساس شد.'
پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 503K · <a href="https://t.me/VahidOnline/76207" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/769901b74f.mp4?token=nE8bPRampguIjzAOWIf9cst_JmlR28fUHzs-ON7WBBVab2J0A1t6Gjes0_y0zw53euYH6Sf9sIj0G1lAAdskVkOxTbv8oEENpimkFUxhHyVfocC9CNXcVGaR6m1rYCS3huLBrRHLxdAn3PphFQJktd0HC42hZVaD2ndKXX6vwZEv6jpMlyzUIwSnw8Svnof051mzVOQzglK_pnUuwdlrs3TEt31lSW7ImUvcrnP1zbq0AGGHW4ssEHJDgrrVhYhLCIvK4Xzp0mvmfbRAiM6ECXiZ-ugOALjyIGmQF_nbfPdU8hQ5uVlzVq4b1EZclz0yiHdO_3cIy4EGR2v8hQCq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/769901b74f.mp4?token=nE8bPRampguIjzAOWIf9cst_JmlR28fUHzs-ON7WBBVab2J0A1t6Gjes0_y0zw53euYH6Sf9sIj0G1lAAdskVkOxTbv8oEENpimkFUxhHyVfocC9CNXcVGaR6m1rYCS3huLBrRHLxdAn3PphFQJktd0HC42hZVaD2ndKXX6vwZEv6jpMlyzUIwSnw8Svnof051mzVOQzglK_pnUuwdlrs3TEt31lSW7ImUvcrnP1zbq0AGGHW4ssEHJDgrrVhYhLCIvK4Xzp0mvmfbRAiM6ECXiZ-ugOALjyIGmQF_nbfPdU8hQ5uVlzVq4b1EZclz0yiHdO_3cIy4EGR2v8hQCq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'نور یکی از انفجارهای حملات بامداد پنج‌شنبه به استان البرز'
ویدیوی دریافتی: 'فردیس کرج، ساعت حدود ۴' پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/76206" target="_blank">📅 06:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vimlOmGlmPhpL-aR9rCnndHnaqQ5VufhC9dymYapWNhZWVf_DM9zsa3-lc8GUqzd0QwN2Y2xFaEE54yNNmypUgnMJfru6x3aVEAywmggtS83e93KTirJ0eRPQX9u7IE3yESoCoRZRf-MkustwjoBtlq8CHj7aEMHc3JehzmqSixBOS9yPYcKFXnQxqbRiO_al_OCC11WYL8O7_CsYSc1kQ8NAtqdqNK21evOa-DNVNrqtQbwXSmgapXDJTl0w2iZQgU4COhscsgbLiYCkrCpsUcMVq1Wf6BIqG7V_FVlx9RiTY4cCFCFRHnsKHnvMIhSmNC5Snpz3RZvJuisKC0TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TLT0QZoE2wl8qne8cM0rXh_B1PwhSUU_RFiYyN9IFEufa3wPh3dmWxKiDD3E42XrZbxzJChaFUOQzJllA35X_xbBj7bjNH8M6XRwg-U72KBucQkMQ3X0YCb445aqjCIyKEn0zQmzuX4ZRyh75fSrEk4BgIp4WxFrizpoXG5WDTlcDXMDRt0SSig-H7qZnvO9laPFwFeTNN1oA8y1mPt_uL9XV8iLWFvKAJoBcG7MsfKvVRvx2kH6mmwiXBy2hh8xj3qxlNHOa6lnVp5J2FoqcIxZKmzwq_cGyFXT_vN_vLmqGt2mrTX43_qMTq80EIvBAReb8f8LeO2fFX0vybH45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qRf2U7_MoceTgpXmYnndkyfZGH4gk0vdFwZK9Ybjb-iqIENWL0S2cOGqbZvO-AVFycOABSJkfXN1gpVg1yEUGa1i81Ce3xfksRHddsieeDv0cyFYSFJd-qGTMY5S7PGCSVNUuSE1wA_u0ckUkgdskYUYedknIhUe3uzth6NjbTDwXvRiirOU9WpDk_ylAoo08I4gK_Zb13H0H2qvh86UyCX_-S6jl-_HTDVQGUqfY5CXMHGBvAFsmHV8mDnh1tbeYJH5cK5MR3h1CPJZ9kc8R2dWX9Zb_RgdS4nRDrzanzGo5bn2-plx7_-4F9n-bFZH0EPJHHQwB8suHjvrBIOPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d-xgrOcI_T-0OtI0YNPeb2C3o8H91Ub0O4wZ1Ud2UjYWm3fEpiYChSMyeQ7eL5s6hC8oNJBO1n7ZrvL1E5wYEybIWPARGxvDP6vccS1W50LlOqrmSTmk0juQdLgLqscLeEfvUPe4cy3KaqTzYsLElxJ7u1NQe1w4C6FnYT06V8kJeKHNQzAJxYjFF7L4OWNzy6HqM8XVw3hpJdZUu-uK4jQIURPoBCUG_-_ErGuDEW9T5zcWLOCFXSatoWiw3jXkmPOrV4tqeJmMnvTP5bCsunmFqys3FvRQeIdK7sY8iTa19gITPSgoziWnpFowMR0qel-IwXLd5GJdn7Gmb91T8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e891de921.mp4?token=JiL4aInAO7nsDsVYHNybtkw8iGAjy7L2adf9EEr_1tV5QedTRZx6e0e_3OZkY2FQ_pxasA2444vTzQ-KlKHLEJzT7qL-SKuz_LFfZZUHYB5XTIvkko3XMS-ku5iHweh6_0tj-Pud994-k-65qpCAyTN2fUJdVhn8Xgu0q12QwzyV-Unenjv6Z-z_ew807aMtAFRwK1g74vFCZHZWN_wOGfdLv79IsiEydx0cGWumWdHiWc3_2_JVEHIb2b9lNDKsh-ODA04UuRe5sWwC6FsJ3RudoN47Walz8Z7CUVLbIh2qmWnWokczKxr8_rV5OU5riMWYHG0rYGnhpNRJRBm3ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e891de921.mp4?token=JiL4aInAO7nsDsVYHNybtkw8iGAjy7L2adf9EEr_1tV5QedTRZx6e0e_3OZkY2FQ_pxasA2444vTzQ-KlKHLEJzT7qL-SKuz_LFfZZUHYB5XTIvkko3XMS-ku5iHweh6_0tj-Pud994-k-65qpCAyTN2fUJdVhn8Xgu0q12QwzyV-Unenjv6Z-z_ew807aMtAFRwK1g74vFCZHZWN_wOGfdLv79IsiEydx0cGWumWdHiWc3_2_JVEHIb2b9lNDKsh-ODA04UuRe5sWwC6FsJ3RudoN47Walz8Z7CUVLbIh2qmWnWokczKxr8_rV5OU5riMWYHG0rYGnhpNRJRBm3ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دود انفجارهای حملات آمریکا به غرب استان البرز و
#کرج
تصاویر دریافتی از  حوالی "حصارک"، "کمال‌شهر"، "مسیر کرج به قزوین" و...
بامداد پنج‌شنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/76198" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9jStG8Oax-aWoj9r_iM5fRpPKKFs6NTaRCWY7jZm2QlIKtLXKzWmC4bFT2yrRe8UQhxDwvhChkHwIAPfAcksPtKQn75XKw4H7xyQ8VgIvSmMj0eSxGtZmQ09XGxv0sCk8krOn4k3bWmVozp1Ue2_g7VJW5A0IzaVlhbEjlNC-v2Fh7I_55jKLNe3SjNjnvQkvem4pX5OizehYyPkm76ZIcq22AXvUlzXEwmvti8tuFw_tyrqLKUjfvpfWNeOsn3yUPVDcva2Ey-n4ZITieox-uvM4-hNO9K7ZbpygeqleyDjOxoJ09_q08T0qkCmVKr-qyB1x9_HTPPD4TrUcwITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح : شلیک موشک از استان اصفهان ۶:۰۳ پنج‌شنبه ۲۱ خرداد
آژیر هشدار حمله هوایی در بحرین صبح پنج شنبه برای بار دوم به صدا در آمد. ویدیوهای منتشر شده در شبکه‌های اجتماعی شلیک موشک از چند استان در ایران را نشان می‌دهد.
@
VahidHeadline
ارتش کویت بامداد پنجشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور در حال رهگیری اهداف «متخاصم» هستند.
پیش‌تر روابط عمومی سپاه از حمله به اهداف مرتبط با آمریکا در کویت خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76197" target="_blank">📅 06:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863187a248.mp4?token=I3-C1V2zlzimZ4Hs-H1L7PLeadGcP6JSCZ8Sy8_vjhbuIn1Xo0igooYEIYPBlC7biD8ryYk84xxANDieBfYWSgWydA0iBkwsZ8DfiIIg6M8CX2d4CDsnEC6gY4tW0f8zCUbCY6oLLRbOMiweedrPfQkx7dBjdz_Zg-o5z1L1EjS4XKa1Ajgp9BmP0CD_ZrlIrZDYR0No5pZqoB6L1snkRdAfujL34zRmj7TUebompY5uM5x2yDX3_MJU3i0CC1ftv-7t2YmfeCSnDhgGDIx047o1wkHfgh_Y_aLGVTQQpZv5dlLg62s3vjCOu55AxAnT40vBtu1MoRzhmXIRqvWZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863187a248.mp4?token=I3-C1V2zlzimZ4Hs-H1L7PLeadGcP6JSCZ8Sy8_vjhbuIn1Xo0igooYEIYPBlC7biD8ryYk84xxANDieBfYWSgWydA0iBkwsZ8DfiIIg6M8CX2d4CDsnEC6gY4tW0f8zCUbCY6oLLRbOMiweedrPfQkx7dBjdz_Zg-o5z1L1EjS4XKa1Ajgp9BmP0CD_ZrlIrZDYR0No5pZqoB6L1snkRdAfujL34zRmj7TUebompY5uM5x2yDX3_MJU3i0CC1ftv-7t2YmfeCSnDhgGDIx047o1wkHfgh_Y_aLGVTQQpZv5dlLg62s3vjCOu55AxAnT40vBtu1MoRzhmXIRqvWZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'موشک‌های شلیک شده از استان
#زنجان
'
ویدیوی دریافتی، پنجشنبه ۲۱ خراد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76196" target="_blank">📅 05:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=rfVB-ZO5S4kNBFMKB4WbvTLoXN9aE8uJVsp4B5YricV6bMr7MNhhamMpi50gF9Rm3b2ZhWYBdhdb8GtgHf3z5-Ki4Gvr4W_Grf30rQwayUIaEDbzwH-tNwK2JTxkze8lumQVQ0FWoCIhbZsJdzvVGH5YobpwQbVlDlrUIS5YUlc6bXDsfiJRczRz8U4ytWWxXh_6PkAOAcEe7foDL-Un8rWJhbaM62B75yt-321phqa8zKyHKkE5ETv4DPdOb3S7cA23aoN5sjoZ98GJ6H1j_dOXQfX3fbx0Bu90ixjeYBGwyDtr5PaeYREgBuBWyG0leMqnJiRNFdLGSeZ7muKaig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ce876bdc1.mp4?token=rfVB-ZO5S4kNBFMKB4WbvTLoXN9aE8uJVsp4B5YricV6bMr7MNhhamMpi50gF9Rm3b2ZhWYBdhdb8GtgHf3z5-Ki4Gvr4W_Grf30rQwayUIaEDbzwH-tNwK2JTxkze8lumQVQ0FWoCIhbZsJdzvVGH5YobpwQbVlDlrUIS5YUlc6bXDsfiJRczRz8U4ytWWxXh_6PkAOAcEe7foDL-Un8rWJhbaM62B75yt-321phqa8zKyHKkE5ETv4DPdOb3S7cA23aoN5sjoZ98GJ6H1j_dOXQfX3fbx0Bu90ixjeYBGwyDtr5PaeYREgBuBWyG0leMqnJiRNFdLGSeZ7muKaig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان تبریز
ویدیوی دریافتی: عبور یک موشک از میان رد موشک‌های قبلی
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76195" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/056cecd324.mp4?token=YzWM5YhUUadAjgcUa4k_yzG7E5cF-fyv3IoORRAEU0xBpIze6d-BLn5GQRPItj4kYPOzbIp0fCgDYBTjfGQlz3kdlh48PxknFMssY5Utmxr_M1R0Lyx7Bmu9pTYYGRwJ4ekPHqc2EA1x59W_Ub-scNyV-HRgDTW5tauO7IQz4SuhFYKmx_Fkofjw30WCXv-OKF45EvpvsM75QN-Fuwzg7wAgcz4oNgSff-FLnEn4zt7XJFP0bf8wcrd6o0jxHczRUOuzvn7mLefjfUPmwXYbd-VijYvUVSRkirQJVMuH_o59w7x4FbhPgX8dljfXRbpS-0m6HGtq0qnsEmRVQoaXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/056cecd324.mp4?token=YzWM5YhUUadAjgcUa4k_yzG7E5cF-fyv3IoORRAEU0xBpIze6d-BLn5GQRPItj4kYPOzbIp0fCgDYBTjfGQlz3kdlh48PxknFMssY5Utmxr_M1R0Lyx7Bmu9pTYYGRwJ4ekPHqc2EA1x59W_Ub-scNyV-HRgDTW5tauO7IQz4SuhFYKmx_Fkofjw30WCXv-OKF45EvpvsM75QN-Fuwzg7wAgcz4oNgSff-FLnEn4zt7XJFP0bf8wcrd6o0jxHczRUOuzvn7mLefjfUPmwXYbd-VijYvUVSRkirQJVMuH_o59w7x4FbhPgX8dljfXRbpS-0m6HGtq0qnsEmRVQoaXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: رد موشک شلیک‌شده در آسمان ارومیه
پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76194" target="_blank">📅 05:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=SGdcZ2Su33hXTrhL4ggb8asch5My6nwhyDg7D2NfSkiUc9k--UjXu7A5PgJL0ND980F6Eh4bkSAZ6qJHYRnOPyw_N_Dk0hcwgKavVl__0Qb2EKQ2hTeWgfPOynQdC_sEu3G_Q3ppFaZDbyFwfSfd_YpA2hLOEIzez9aRDQUfHSdSoScTYsM8LOsIjVqWIz_a48DNGwDiN8Zrnyc7LNc6bRdHq_CtUauyL52SeIGGwovbq2AUjUAN9TYcl2YMjChIHi6jr189xK5yHEFYZrRONqMcoqD85RjRxw1Y7jA07qXFKj1IEwhZlmpWseFFzpBs0Y_53MK5P498yeERXveeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62d2ba90a6.mp4?token=SGdcZ2Su33hXTrhL4ggb8asch5My6nwhyDg7D2NfSkiUc9k--UjXu7A5PgJL0ND980F6Eh4bkSAZ6qJHYRnOPyw_N_Dk0hcwgKavVl__0Qb2EKQ2hTeWgfPOynQdC_sEu3G_Q3ppFaZDbyFwfSfd_YpA2hLOEIzez9aRDQUfHSdSoScTYsM8LOsIjVqWIz_a48DNGwDiN8Zrnyc7LNc6bRdHq_CtUauyL52SeIGGwovbq2AUjUAN9TYcl2YMjChIHi6jr189xK5yHEFYZrRONqMcoqD85RjRxw1Y7jA07qXFKj1IEwhZlmpWseFFzpBs0Y_53MK5P498yeERXveeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک از استان زنجان
ویدیوی دریافتی پنجشنبه ۲۱ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76193" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sUP300EUS9mgrQa3m-aQHTGrvGLNAc-kxuFwkwqQ60F1ID7v0XUswygjxSAT8P1pwfEMjk6XgDajTvSYz0OJURXogEw8MEdBiNkVHlZEWsOqGw3tJ3OmrL1CNv8pktZktdyYUtY8FRZsEsWmsYl1Ruhw70ztNqSRVS4gBKtQjhlCZIYU5Zumk0oo9XEoSlau_waOJ1ATFKq2HfQ0VUsHcoVpjtDviL52r3xQfompY5nW4WXUUF3NL_KbyPLaQrHcg5SazpAW4Tw24FlqHWIIIizQmJ9ghLOJiDHeOCVcsXGpuEzF30yC6MG2AQbUlmQl-RH35m2laO3vpWdHYn2K_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XT-ji_lB5EXoubgXeZTYFCNq6xjUl8_RZ7zkV9BsAlY4ptxQ-XwmOlPM3UrY5u_UlaZzPmmDp8WaVn3M4iFP-2thx4MM8uL2lOYjcemGZP8Imd1rZNqISbMPuTv2o5oRAvuGUx9ksZZjs9p_uFhtPmyhwLWVGAZjufjKAY0MR3DW7iUo4Smyg8OvmaemYvgVuwykkq8pN_LxU7Cj0mohD00J0ngpJWZ1_HRVfV1BYXiDY0dIYPruc-T0NsIarU0sHDiGWP8HWjwecL5najzhuvOg6RccFB3ucbx-o27AGUdTXn6UcIzo3D4ehQNS9R95H138nOzTqFnpwxKMSOVTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KmvaEXBc4XwprzhHyDmD-4jxXyZ2lYZFncaf603VSKtl4KJntHGktVV3I8m8rA6Bg8mGMOHqmLI1zbGiD0hN_fzaADrqzKjDjWNxMpWwHj5mqdt3fvME9ij2hQ8Kl0k2YdJUXsVwFsfmU3eu6U3lyFCPzGdZ7zn9_6pFS5bnaPfBwtqi8bbbDPveE-NFDXJt-AuEtSu8EfdgODd-sOdIWH2fZdlhRSbLIXUUM3l7V8LN9_i-ceVnZWyMM58EE2faZ9VnzhTvVXamvCQEcxdhtqPM57Ne3xV5Jdk4Ox6QJLO-NFbBp-WDuXkNRhHIHbylD74NbQvChBkGEgX3HVtBpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک موشک از زنجان، تبریز و ارومیه
الان از شبستر تبریز سه تا موشک زدن نمیدونم به کجا
صداش خیلی زیاد بود
الان یدونه دیگه زد
سلام 5:16
همین الان تبریز صدای انفجار قوی اومد
از ارومیه موشک بلند کردن
5.18 ارومیه  صدای 4 - 5 انفجار
سلام وحید جان تو ارومیه ساعت ۵.۱۷ چهار بار صدای انفجار شدید اومد
هنوزم ادامه داره
3 تا دیگه زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76190" target="_blank">📅 05:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw16ZqMAM9PjnDQztNIjFi7eRPZgLH8Uar7X3PtDboF9QTKjmvLgcgnaeZ-yFCAMSjeLzPjwVj2e4cLMap3CIXrsso3vw4pLCbULuYP6Ub8kEaXz_Qa4e3cETA-tpR99AmSsjRFnKe8uVqphGLFuveqSNZUJ_5EFTcel5VQ9fzngcsbUky-mf2zf6n6JnarFpLCjC6Mwyag8b4oiqC7R_W0f00aIBLWi9kmKd_cDpZyXJvwpBso4SMsGhM-1l1L-WQsIpzhqIWobKfaHE2tW6CumG116ZdYilYRkKIk7Yxwra8SV4BMRdtubMJYvwDjV-BW3FG-sZk3q_mejGFt5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
ساعتی بعد از حملات بامداد پنجشنبه آمریکا، خبرگزاری‌های رسمی به نقل از ارتش جمهوری اسلامی ایران نوشتند: «ناوگان پنجم آمریکا در بحرین، آماج حملات پهپادی ارتش، قرار گرفت. در این موج از حملات پهپادی ارتش، آنتن‌های ارتباطی و تاسیسات راداری سامانه پاتریوت ناوگان پنجم مورد هدف قرار گرفت.»یییی
همزمان وزارت کشور بحرین در پیامی در شبکه اجتماعی ایکس از ساکنان خواست تا با حفظ آرامش به نزدیک‌ترین مکان امن بروند.
سپاه پاسداران از حمله به« ۱۸ موضع نیروهای آمریکا» در منطقه خبر داده است.
کانال تلگرامی سپاه نیوز نوشت که طی «دو موج عملیاتی ۱۸ هدف مهم» متعلق به ارتش امریکا در پایگاه‌های هوایی «علی السالم» و «احمدالجابر» و همچنین پایگاه‌های هوایی «شیخ عیسی» را هدف قرار داده و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76189" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PsYenDWBpTHs37xYCfqid0Qh6dGQu21jst-WDl7N3XHuY7zc5X1dbVDE_LxeW0X3aNiSd-PuT3EMZW77sv7l4Oees1GuHZhEOOWAtIOBupoIPCqNKH-oMTuXiurvMjDY-7TWvNvTwSWPv5DZ6YEm2-mdlrNjojqSFd0uUFKpW66Cw2-6mKDrZssng_nCy_O-cSe4N7NsAZXLVZw1OpXVjki0DHiaFCO1ltpXEj-oKrgjhsh34Vp-EdGPTR8i0_dZznquXu9NfEhjykMdRlL_0gTi_LFV3s7-tWOvhEMffbcwD5KEcISjolsiMvDe0sZCvBnjyti9mSty7zEFjJFCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ گزارش داد که اسرائیل در حمله نخستین ساعات بامداد پنجشنبه به اهدافی در جنوب ایران مشارکت نداشت اما به‌طور حتم ارتش اسرائیل در سطح آمادگی بالا قرار دارد. او در عین حال گفت که آمریکا بیش از ۵۰ هزار نیرو در منطقه دارد که بسیاری از آنها در عملیات مشارکت داشتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76188" target="_blank">📅 05:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=vkIf4cCfIeVbDdjbYDnGYTfSnUiJVzicpLgCsV3qZefD20cGtqe1Mi4Rb4tPA7gNTU6RPEG4LibKf8PZoJ5HmnAGbbFePtFtO00DINvg_rNpl6Yx0jvnwsvu1lD_bDRgVxp6Lwx3B6zluZiRDvhr-CHodW27YM-sJlP1KBFObL7M6r9Qceg9s_lz9WzqdUB9bfuDlQxIGgelvxHNA8vZVTCTIZv4Bb4EHnTIFcuRhbK3hpY4_QKOHq33dieqaZFiEhQ70y2zaK0Ym9objerWTeFWao7lFJxJkmgisUisYNZfD_qSQ3t_bxfHX0RsQSIQzpPFhuCcgbUu6iFd67zrQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c67229aee8.mp4?token=vkIf4cCfIeVbDdjbYDnGYTfSnUiJVzicpLgCsV3qZefD20cGtqe1Mi4Rb4tPA7gNTU6RPEG4LibKf8PZoJ5HmnAGbbFePtFtO00DINvg_rNpl6Yx0jvnwsvu1lD_bDRgVxp6Lwx3B6zluZiRDvhr-CHodW27YM-sJlP1KBFObL7M6r9Qceg9s_lz9WzqdUB9bfuDlQxIGgelvxHNA8vZVTCTIZv4Bb4EHnTIFcuRhbK3hpY4_QKOHq33dieqaZFiEhQ70y2zaK0Ym9objerWTeFWao7lFJxJkmgisUisYNZfD_qSQ3t_bxfHX0RsQSIQzpPFhuCcgbUu6iFd67zrQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکا تازه‌ترین حملات در ایران را تکمیل کردند
ترجمه ماشین:
"تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا، سنتکام، روز ۱۰ ژوئن، به دستور فرمانده کل قوا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران تکمیل کردند.
نیروهای سنتکام حملاتی را علیه توانایی‌های نظارت نظامی ایران، سامانه‌های ارتباطی و سایت‌های پدافند هوایی در سراسر ایران انجام دادند. تجهیزات و نیروهای سپاه تفنگداران دریایی، نیروی هوایی و نیروی دریایی آمریکا مهمات هدایت‌شونده دقیق را به سوی اهداف ایرانی شلیک کردند؛ اهدافی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند.
این حملات در پاسخ به تجاوز بی‌دلیل و ادامه‌دار ایران انجام شده است. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده هستند."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76187" target="_blank">📅 04:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی:
درود صدای انفجار در شهر کنگان ۴:۱۷
شهر کنگان صدای انفجار
کنگانو زدن ۴:۱۸
سلام شهر کنگان در جنوب کشور صدای انفجار
کنگان رو زدن
سلام.
کنگانوووو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76186" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یک صدای دیگه از کرج همین الان ساعت ۴:۱۰
سلام وحید
یکی دیگه الان
همین الان دوباره کرج
ساعت ۴:۱۰، انفجار دوباره
۴ده دیقه کرج کمالشهر
وحید صدا های جدید ساعت ۴ و ۱۰
ساعت ۴:۱۰ یه تک انفجار دیگه گلشهر کرج
صدای انفجار خیلی بلند و طولانی بود
ساعت ٤:١٠ دقيقه باز صداي انفجار هشتگرد شنيده شد
مهرشهر کرج ساعت ۴:۱۰ صدای انفجار
همین الان ۴:۱۰ گلشهر مهرشهر
دوباره صدای انفجار خیلی شدید به همرذه لرزش زمین
سلام وحید جان کرج دوباره صدای انفجار همین الان ۴:۱۱ دقیقه
و کلی پیام مشابه دیگر که نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76185" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام از پیشوا صدای دوتا انفجار شدید
ساعت 4:۰۶ ورامین
۲ تا صدای انفجار
سلام آقا وحید، ساعت ۴:۰۶ صبح پیشوا ورامین صدای دو تا انفجار اومد و مثل اینکه سپاه پیشوا رو زدن
الان ساعت ۴:۰۵ دقیقه نزدیک پاکدشت دوتا صدای انفجار اومد
ساعت 4.5سپاه پیشوا
وحید جان ورامین همین الان صدای دو تا انفجار اومد
سلام وحید جان ورامین دوتا انفجار پشت هم ساعت ۰۴:۰۶ دقیقه
ورامین 2 تا انفجار خونه لرزید همین الان ساعت 4.8
همین الان دوتا صدای انفجار شدید داشتیم ولی مشخص نیست کجا رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76184" target="_blank">📅 04:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام وحید
بندرعباس رو الان زد
صدای انفجار شدید
صدای انفجار بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
سلام مجدد ٠٤:٠٥ دقيقه بندر دو صداي انفجار اومد
٠٤:٠٧ دو صداي ديگه مجددد بندرعباس
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
بندرعباس همین الان ساعت 4:06 صدای انفجار نسبتا شدیدی اومدی
سلام خوب هستین من بندرعباس زندگی میکنم ساعت 4:6 دقیقه صبح دوتا انفجار مهیب پشت سر همدیگه صداهاش به گوشمون میرسه
داداش وحید بندرعباس همین الان زدن
دوتا انفجار به فاصله یک دقیقه سمت دریا
۴:۰۶ یه انفجار دیگه قشم احساس شد
همین الان بندرعباس چند تا انفجار پشت سر هم شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76183" target="_blank">📅 04:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای انفجار در کرج
آپدیت: میگن شد ۶ تا انفجار
کرج صدای انفجار 3:53
ساعت ۳:۵۳ کرج انفجار
الان باز صدای موشک اومد
۳:۵۳ وحشتناک بود خیلی بد بود و هنوز صدا میاد
درود کرج ساعت ۳:۵۳ صدای انفجار شدید
کرج شاهین ویلا همین الان یه صدای مهیب انفجار اومد
سلام، همین الان ۳:۵۲ انفجار شدید، کرج، ما باغستانیم خیلی واضح بود
سلام وحید ساعت سه و ۵۳ یه انفجار خیلی شدید ( گلشهر کرج )
۱ موشک دیگه ترکید
وحشتناک لرزیدیم
بازم داره میزنه
وحید سمت ساوجبلاغ ۲تا صدا خفن دوباره اومد
خیلی شدید بود نمیدونم کجاست ولی  نظرآباد میلرزه دوتا انفجار شدید فکر کنم آبیک بوده
بازم داره میزنه سمت هشتگردو ساعت۳:۵۵
علاوه بر اون اون پنج تا انفجار قبلی الان صدای دو تا انفجار دیگه اومد ساعت 3:53 آیبلاق
انفجار در کرج سمت فرودگاه پیام
وحید جان من مهرشهر کرجم الان یه صدای انفجار مهیب اومد
سلام نظرابادم
دوتا صدا انفجار وحشتناک اومد از سمت کرج
بازم زدن همین الان۳:۵۵
کرج ۳.۵۴ انفجار شدید
کرج جهانشهر صدای انفجار ۰۳:۵۵
تک انفجار شدید اطراف شهر کرج همین الان ساعت ۳:۵۴ شنیده شد
فردیس کرج هم صدای خیلی بلند اومد و شیشه ها تکون خورد
همین الان فردیس کرج صدای دو انفجار شنیده شد
۳.۵۳ هشتگرد بازم ۴ انفجار دیگه اینبار نزدیک تر بود درای خونه لرزید
سومین انفجار ۳:۵۶
سومین انفجار تو کرج
سه انفجار وحشتناک توی کرج همین الان!
گوهردشت ۳ تا انفجار خیلی بلند شنیدیم
شلیک موشک اینا نبود
انفجار بود
ما مهرشهر هستیم صدا خیلی بلند بود در حدی که خونه لرزید
چهار انفجار به فاصله یک دقیقه از هم فوق‌العاده مهیب ساعت ۳:۵۵ اطراف جنوب کرج. همه پریدن از خواب. لرزش عجیب و غریب. امتداد صدای انفجار شاید ۱۰ ثانیه طول کشید. مثل پژواک صدای رعد. تا به حال چنین تجربه‌ای نداشتیم
وحید نظراباد صدا از دور پشت هم میاد ولی شدید خونه میلرزه
سلام آقا وحید سمت باغستان کرج سه تا صدای انفجار آمده و ساختمون لرزیده
۳ تا صدای انفجار خیلی نزدیک اومد
کرج باغستان
شیشه های ما لرزید
ساعت ۳:۵۶اطراف هشتگرد نظراباد بدجوری دارن میکوبن
سلام از فردیس پیام میدم اینجا الان یه صدای وحشتناک اومد
دوباره هم یه صدا اومد ولی اینبار دورتر بود ۳:۵۷
سلام آقا وحید. من شهرک بنفشه زندگی میکنم و ۵ دقیقه پیش صدای چندتا انفجار شدید اومد
صدای سه تا انفجار با فاصله یکی دو دقیقه در کرج، ساعت ۳:۵۲ بامداد
وحید جان چند صدای مهیب در مهرشهر کرج الان.
۴ صبح . مهرشهر کرج . صدای انفجار میاد
سلام وحید جان ساعت ۳:۵۴ و ۳:۵۶ صدای انفجار و لرزش محدوده ساوجبلاغ البرز، مشخص بود از طرف کرج عه
یه جوری فرودگاه پیام رو زدن سه متر از خواب پریدم هوا
وحید شهرک بعثت کرجم ۴ تا صدای انفجار خیلی زیاد اومد
ولی صدای جنگنده نیومد اصلا
خیلی موجش شدید بود
3/59دقیقه فرودگاه پیام و زدن
همین الان صدای انفجار شدید اومد
بعدش ده‌ها پیام مشابه دیگر اومد که دیگه نقل نمی‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76182" target="_blank">📅 03:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیام دریافتی از شهروندی با سابقه اخبار درست:
"دو انفجار. نیروی دریایی سپاه سیریک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76181" target="_blank">📅 03:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پست خبرگزاری سپاهی تسنیم:
۱۸ هدف مهم متعلق به ارتش شرور امریکا طی دو موج عملیاتی مورد هدف قرار گرفتند
روابط عمومی سپاه:
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
رزمندگان شجاع نیروی هوافضا و قهرمانان نیروی دریایی سپاه سحرگاه امروز در تنبیه متجاوز و پاسخ به تعرض ارتش کودک کش آمریکا به بعضی از واحدهای خدماتی و پاسگاه های ساحلی سپاه و فرماندهی انتظامی و محوط فرودگاه بندرعباس طی دو موج عملیاتی
هجده هدف مهم متعلق به ارتش شرور امریکا در پایگاه های هوایی علی السالم و احمدالجابر و همچنین پایگاه های هوایی شیخ عیسی
را مورد اصابت قرار داده و منهدم کردند
وَمَا النَّصرُ إِلّا مِن عِندِ اللَّهِ العَزيزِ الحَكيمِ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76180" target="_blank">📅 03:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی از حوالی غرب استان البرز و شرق استان قزوین
من سمت ساوجبلاغ کرجم
ده دقیقه صدای موشک اومد
الان صدای پنج انفجار اومد ۳:۳۲
سلام همین الان ساعت ۳:۳۳صبح اطراف هشتگرد صدای اتفجار و موج میاد
سلام ۶ بار سمت نظرآباد البرز رو زدن
ساعت ۳.۳۴
۲۱ خرداد
ساعت۳:۳۰
شهر جدید هشتگرد
۶/۷ تا انفجار پشت هم
اما خیلی دوره
نمیدونم کرجه یا تهران
ابیک قزوین ساعت ۳:۳۴
بامداد ۲۱ خرداد
صدای و موج انفجار اومد، به نظر میاد از سمت کرج یا هشتگرد باشه
۵-۶ تا بود حداقل
۳:۳۰ صدای ۵ تا انفجاد اومد از اطراف هشتگرد بود فکر کنم قشنگ شنیدم
سلام وحید نظراباد از دور صدا ۷.۸ تا موشک پشت هم اومد در های خونه لرزید
هشتگرد ۵ صدای انفجار از طرف اشتهارد
سلام وحید جان ساعت ۳.۳۳ صدای ۱۰ تا انفجار شدید اومد من نظرآبادم ولی صدا از دور بود
پشت هم موشک داره میاد با نور انفجار و صدای مهیب
محدوده نظر اباد هشتگرد
از پشت بوم کاملا مشخصه
سلاممم کرج هشتگرد 4تا صدای انفجار شدید اومد
دوتاش خیلی بزرگ بود بطوری ک کل خانواده از خواب پریدن
قشنگ کل خونه لرزید
۵ ۶ تا صدای انفجار هشتگرد جدید ساعت ۳:۲۰
سلام وحید جان
۶ بار صدای انفجار مهیب اطراف اشتهارد شنیدیم‌ از حدود ساعت ۳:۲۰ تا ۳:۳۵
نزدیک چهار یا پنج تا انفجار اومد از سمت آبیک اطراف ساعت ۳:۴۵ خیلی مهیب بودن
سلام وحید جان ما سهیلیه کرج هستیم بد جور لرزیدیم
۷ تا ۸ تا صدا انفجار بود سمت سهیلیه کرج‌کامل لرزید،
سلام ماهم اطراف آبیک قزوین هستیم ساعت ۳:۳۵ حدود پنج تا انفجار شنیدیم اما دور بود ازمون
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76179" target="_blank">📅 03:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aeILbKLJrwVsrDvzlZeQFoXIPQyebeJwInZ8ENM0d0Nxi35cF7gEwa8YactQeHfLG0icX78gbip4oDBBaDUH9kOXMJ3LtwJbJcShcpCLktrDHll1lfmuuYavF2WgiOlaBnWzf8tYPqEO1aU7asOBZp3d9ImPphDwFbttNUFuG3GcA9JmkrMf4EYDdTD9CLWW90U5UQ5IySn3RUZ4dgtdEm7AKSSJuOUJHlPbulW_q4aLdOq45iEKf6dfI14PsnOVOefuhWChI6LXlcNYFLM3pIwZCcZAJ4k6s4m3L8oCpR5P3uJGiYFORXqohjzamv_NAsTFLYWJZyo9N7USFRVNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما به نقل از یک مقام ارشد جمهوری اسلامی اعلام کرد اظهارات ترامپ درباره تماس او با مقامات ایرانی دروغ است.
این مقام افزود: این اظهارات پوششی برای فرار از جنگ علیه جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76178" target="_blank">📅 03:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jeOWamZm66fqjTgsvsyAe8otwFj-cD7mbX15lf4e90E4rzd5UYmEDRqyZcfVS62PlKQiHRhj6eV0kNH9ve9_7GR8Pim43xRBvl3H-ZJnVZYIcgi1vU37249EM5X2k3DUD9ar7_lVmKyWe2vtB33icA10cO5yPZ3d7Qm4ob2aHWKVv86ubk5c-oVFszsE6nAAYXfrBqqa6EunseGnqYVnRmn-j41GzT3P9sQreraLCa_PNZg04npE6EIkqi2EHwlYdbw5YjjgxVx1-4xlEaC2P_SSuUOwlWdOMOgBpVcwlDdxfuiiHJws17h9WWsQtNmNgwbLFZZCVub_fFHxZODVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌‌‌های اکانت فرماندهی مرکزی ایالات متحده، سنتکام
ترجمه ماشین:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
✅
واقعیت:
کشتی‌های تجاری امشب همچنان در حال عبور و مرور به داخل و خارج از تنگه هرمز هستند.
CENTCOM
🚫
ادعا: منابع رسانه‌ای ایران مدعی‌اند که ایران به یک ناو جنگی آمریکا در تنگه هرمز حمله کرده است. نادرست است.
✅
واقعیت: هیچ ناو جنگی آمریکایی هدف قرار نگرفته است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76177" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORfwPeRPLrThy1SfoGJoWeFsSfeHYi2AfzaGn_eJzCeAuv4TRs_Bd37n_px7-qSYC2dBKt08Lf2W6WyYBZzQFZgKAInvmu22P70W4RVqSENMO98ret9vAdGd3b7lDEWVagZokw0ZtycLqZdvG6AlJe8U0VMUH2ZurYb4KGo2dA_kl008L5wR7QJR8J17grIvReO02L5Dp1Xp5XdG8IXyd0N8kOviZ8J2V2mX446ug8iT-Dfr_AttfqV2pHWO6jeM9rSXLzD_hCvWfGb30Pi48mB6FRDyN4GC4BLWZTAL06g6XzA_Xk9gs78lx4pM3yBixFpxm-5ieRQ6svqM7UGAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: مقامات ایرانی در تماس مستقیم خواستند بمباران متوقف شود
پست خبرنگار فاکس‌نیوز، ترجمه ماشین:
امشب با پرزیدنت ترامپ صحبت کردم؛ در حالی که او از اتاق وضعیت، حملات نظامی آمریکا علیه ایران را زیر نظر داشت.
رئیس‌جمهور به من گفت که امشب مستقیماً با مقام‌های ایرانی صحبت کرده است؛ مقام‌هایی که از او خواسته‌اند بمباران را متوقف کند.
در زمان گفت‌وگوی ما،
ایالات متحده ۴۹ موشک تاماهاوک شلیک کرده بود و جنگنده‌ها نیز در حال بمباران بودند.
نزدیک‌ترین هدف به تهران حدود ۴۰ مایل [۶۴ کیلومتر] بیرون از شهر بود.
ترامپ افزود که
بمباران به‌زودی متوقف خواهد شد، اما اگر آن‌ها توافق را امضا نکنند، «تا سر حد نابودی بمبارانشان می‌کنیم.»
پرزیدنت ترامپ این را
نقض‌شده‌ترین آتش‌بس در تاریخ جهان
خواند.
جی‌دی ونس، معاون رئیس‌جمهور، به من گفت که ایالات متحده در روند مذاکرات، هم با صداهای میانه‌رو و هم با صداهای تندروتر در ایران سروکار دارد.
به‌روزرسانی‌های بیشتر در فاکس‌نیوز منتشر خواهد شد.
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76176" target="_blank">📅 03:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTwEmn4lDExgzK1s4V5B5cGfFg4W4LdS6ZJdrXaitciqR7A2GaoycO8wFEMSQkxXoQWTmkY-HsrV1Em0QAvoHpEGCh_Y-kV5P9zVNXkajbwyRMi0EtVbEi8dlynpbJz8kfJb0YUc84JB9oDFnIPxIqZcKGdSiAU9khxJ-67PaQ3e5T8hpB1x5GQ-ftxf7vspV4o-7ACbjtOoSMDVmDzADIaSGu6lhUMi8XMxusRorL1xfaXJo9s_lDCF33fWPjoNpIyhET394AlHORJynTM8Exu0zLO_9Z2aDdYJOIyMulh3Eft1Zd_l91X_XyEOcfbkpOqRXRbHv-9Vw_Jqh5a1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی پس از بیانیه قرارگاه خاتم که در آن تنگه هرمز کاملا بسته اعلام شده و هشدار داده شده بود که به هر شناوری که قصد عبور داشته باشد شلیک می‌شود، تسنیم از مورد اصابت قرار گرفتن دو کشتی در تنگه هرمز خبر داد. در گزارش این رسانه وابسته به سپاه آمده است که کشتی‌های «متخلف» قصد داشتند «به‌طور غیرقانونی» از تنگه هرمز عبور کنند. هنوز مقامات رسمی و سنتکام در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76174" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Di1GPJYXTBKBuEla9Wrk0Ah8zKM10Nv2NMM5Lh3cfz0M0MTj9mXgZ7MrRfC2ZEcVfKz5q5eT528R-enFPl2fcjfAlro8v_HP8IEE1WJ-DPIh_IeNwkNfQTJP5dJkUcok6kQYGGkRh3BBFIgqlJ24-aB8r8F7MtURdesc4b54dhQB1vk_xivnXqXiJ2Kif03z87_vi0Y2E6sUrzdYjsMGZCzbGODAFWT4tD6jk9YkVxVgXulb5YAu7cDT9ekozyuChhFCbzzgAiDs3eV0lf6bloFggnmctDIhTVNTqKBzhNlWR4pXTsnE5PNRvTHRkOqZ2cyWEHAF9EM0m1g3BqIDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
روزنامه وال‌استریت ژورنال پنج‌شنبه شب به وقت واشنگتن به نقل از یک مقام ارشد آمریکایی گزارش داد که هیچ سایت زیرساختی در ایران مورد اصابت قرار نگرفته است و نیروهای نظامی ایالات متحده در حال حمله به پدافند هوایی و سایت‌های راداری در نزدیکی تنگه هرمز بودند. انفجارهایی در امتداد تنگه هرمز، از جمله بندرعباس، جزیره قشم و سیریک گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76173" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
قشم ۲:۳۵ صدا و لرزشش حس شد
۲:۳۵ دقیقه بندرعباس دوباره صدای انفجار اومد
سلام  بندرعباس دوباره زدن ۲:۳۷
[احتمالا منظورشون اینه که صدا شنیدند!]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76172" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7_gXx3bUKzrqMBgUlzrAMlAQI-q-mT47sYejqq_uNN6YXq8Sgww7l2Vmy80YVvJS9ZhcwPQg34LgM11AISplG9pYZ80vlLuIgt0mHiA7vipxWPEvyPJuUzBQmwDZS6zihhGlnPuupPzBB8WA84rlOspDn6ruunCg8S9yjuxvY4VdlAkZhX9h1aqG8n_4SNIEaHMWntEg4GoC9o8R7vl7blgm8RR_higuPT_V7ZyWCe8DkneBg3cT6h92MMmkCN-R0iu7jDoW6ImfIdNvbP2aKKgnv8AZtNyg-Tw5z37T9ciBradvyw-gd9TeZprAeZjsTDjdSVh8gMy-l_O3hcVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: هرگونه تردد شناورها از تنگه هرمز مورد اصابت قرار خواهد گرفت
منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76171" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpR0uQDnE_NnpU0k6WR26jgm4m64FU70eFopCDU0tHGpO4CzS-ciWlqvOkkFIUx-kscY_jCShr7NEnClj3Np99MUDal6J_Nqe_p3AY4HCTafV3QdZ_pmySz-GdLXGEG4H2qq5YcFbL7XthHnMT2jf0BIIEnBafkmkfVm8qXpbys_otmEPVX2fGjpz-adIKnWJgCzvBTdEpcEYH2eUBoj0JC7h08_b2Fua3CFqKAz7tHEbEMp9B2EXsv33AxFESxDgnk-EO4iN_Hp3wqdEI7xBn0bDpqnskKpOtblbcZVnU3YU3fKfQloq-elzmU1weeWi4-ZieJrCA50mQe4RCIMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس بامداد پنجشنبه ۲۱ خردادماه به نقل از یک مقام آمریکایی گزارش داد تمامی اهدافی که در حملات اخیر مورد هدف قرار گرفته‌اند، در جنوب ایران واقع شده‌اند.
این مقام آمریکایی گفت سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها از جمله اهداف این حملات بوده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76170" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بعضی کانال‌های خبری به نقل از تسنیم نوشته بودند:
‌
منابع خبری از هدف قرار گرفتن یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه خبر دادند
خبرگزاری تسنیم وابسته به سپاه در پستی نوشت:
انتشار خبر جعلی در کانالهای فیک‌نیوز به نقل از تسنیم
برخی فیک‌نیوزها از دقایقی پیش به صورت هماهنگ خبری با عنوان "هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد" به نقل از تسنیم نقل می‌کنند.
این در حالی است که امشب چنین خبری تا این لحظه بر روی هیچکدام از خروجی‌های تسنیم قرار نگرفته است و چنین خبری تاکنون صحت ندارد.
به هرحال اون خبر رو خبرگزاری دانشجو وابسته به بسیج هم منتشر کرده و الان به نقل از اون داره پخش میشه.
🔄
آپدیت:
ایرنا، خبرگزاری رسمی دولت در جمهوری اسلامی:
فرمانداران عسلویه و کنگان که هر دو شهرستان میزبان تاسیسات پارس جنوبی هستند هرگونه حمله و انفجاری را تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76169" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
