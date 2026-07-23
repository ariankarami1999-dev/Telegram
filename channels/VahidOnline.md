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
<img src="https://cdn1.telesco.pe/file/n5SIPvrAuTLHLbEOX3daN4WdVene5ygQ2kyBDEo07SUmo4aI9krslKxZtE_N0zESmZnMLpYw8aWnYht0nRn2kGEp3QmNICJTMyolFyDYdWQrnejPvXStEREdGyuGf6gNfjxmpKJ9f0KrJPPAzVIhk1PvZQuL110En2AUgkLXk12jvzCjDg-KX56jpEjqQQqoJPEJqY9WW-MAaMQJx9NYhQCAINvP0Eo6TOYCA_U8lALK1T2D-HG-CEGyKiL9HxcvK7GD4kwlxuqZnyNLhL-IyH5C1cG-TxyYnFksjyM1KgJBlaMiCrQvGaaelZky2LLTj0NmhgsPhVAibpQTkiU-3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COehEZ_lWYvchUo8da8mzvWElgFMM7cwGIgLvPi3ZWJB_9qnCn9UYLPF4bwVkSjSWKiglgr_uvCmq7RjGnnFKga_uy-9ujpbedUlbd08u2VqgUnYJ7ooHDOy87h2lN9ulhyW7SY5-yUxy2LwvrSTyfQ4VPzDOcV3bv3cpu2TdqpdZJe4-wGPJNMm5Fg6-u6soQ5tAgA6Zx5-nheSjK2MnKnk4pIPaoNXgULLBmb1MbK_WK4sGRXaKZCoTcfWBkdc4MzgzvUwNP8T_irR0PL6HEXXGB6u87MlNyrpAfN_Pfh6BGOGrMSNkxd-NOLz18KvEczTJKo9oQhH30scknMsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTGS-FtD9qb9PdGtyGXgXZH-k6gtCCZxqrzrKrvSElxkb7t9XlsYB0ohEIEfHCQVQiSsT2Yi_CZygAbELG9BY0LINTb_C524z4RhweghDvGPiXUEmsXX6zEooH_soekyNQ_cisYD68VRM3Tjcjz7MAVNFA7zoP7LkmY8iktWWMdBNM1qhu5_3UjrVvq-l7qRKVHocu7aOPae0Rqi0xAscVJcZds7WhW00ULboMv-BZM-pT-86m5jgmTUfb1uX9_2SP2MZyj_eLCxW7GxDPnlb_S6hAAamNb1Ni19ItQ6TO47LEQw5sTC56KE7-6xPI-wLH68mQJhNQ1hGH7p11PqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lf7c732FASWPw9r3whDJVfcB9pZCn58XKL9YSpwPOo5XUmIvlVC6071U3gb_7yAFR--l8nHs2LMrB8pkKp_x8ghoJ8rLio5s1yQ3EnzlF_RFuVWsd5S-7yqS6_tt4pao2PBLqQhCmU-AbA41CTKZytoRcgqIRhrUgbV5WIzNPR6OeDXx8908wKAy3oRenZ46Ebvt-AxV6tc7kXNYmb7jctnPY7OMw-MSEh3nd5af1k569sFn2I6sG3chdlYGQlLsUzlrw2OB8r_f5c447d56hkDyRWJaiDQzmIkl_z0HhDtjHL_G88TV_hl0zJs64HP26sOu4XseS9EmLNmrK8F6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ioKHXi2PzGtxbMWB_PARLS2PhDRMFU-WN1RIijNVyi5ywDS0A8HvtZUCkkuWr8rRcuuUoSJH2imkUi4p6TCPjzudJ1pAO9Y-Z2Y3EmWxu9nK0bR05KKXM8I7oQa7jjUS9NipjHBdISHGtW_G67m7mKhKtr38UAPQriP_ZeyPpm1T5q050SGGPzGF97x_gdeI7cL4yxDtr46DfPdhgzC23yjwRS0v0x_1WAQya6kFKLS-mcpj8IQ2nHTxG0BrInzkZzjRr8cQROmJdBV-B3lERVnl2sXAcTwAoh__7mB5Jcxm72NV3LyX6FEQp1E8FttYCMZLAOD0bFWRRlu3iMLusg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVPG4D3wQNgFQdK85ZzV4d1FulfdhbmhGA56eLONmlXSsK3D8ag__9isXvUvbt1QWcGMY9mrmQHHiGxpwpb-yGW8iY489zZVyE-LdxGqIhSyoV82U3gDVJM-vrRV38PFktpn06h6WxeBKktbEOu6Rz7W_z-JYqA4OvFJV7gqyelrYx5_Lwf7ti1cKgJhEh_aSmEN_v1VHE1oajYn6_t8A0Tg3uaQhgZM5q389_GnMQFF6K_q-agbNsekKMQlkqr-byK43CIvGNjlupsIBBXUv9ctdwWiJwNbpO7WtyP7-eFaaztG1we7Yg2yu6d5AaBk7A1dmeHYvGR8nGAnXBJitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzX3zz_sOgRCyy6QEy15Wsg_evlKy3jWLaRnJZVDMnizK5fnvEgI2sdOhoCEHW3Q4fVF9tKNjLXeoDI3Dt_Cd-g2oOdpbZJar6tk4iinWP_ZgVauFplzs6Fd_cwRFd04-7RVNC8Pha-7aKmgrpVSJ4V2PlSiPySRM5TjIbYyYYl75YI9-VOqILPF5gfQ9wBhd8hz7WJPklul7KQIDfvyee5v1RbHyTX4UaQ2OPCmPKQJeu58qPVV6tGEEXkT5E0nkkoNCSPakON8TlSIQSFsMzoje2qUe6q__vSLstA3v_hF-_d3yDBGbpn4W869qQfA9JLW5beLrVj9OpFTgzMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما و خبرگزاری تسنیم، روز پنجشنبه یکم مرداد ماه از شنیده شدن صدای چند انفجار در شهرستان کنارک در استان سیستان و بلوچستان خبر داده‌اند.
خبرنگار صدا و سیما در گزارش زنده اعلام کرد، صدای پرواز جنگنده‌ها نیز در این منطقه شنیده شده است. به گفته این منبع خبری،َ انفجارهای روز پنجشنبه، اولین حملات آمریکا در طی ۲۴ ساعت گذشته به این شهرستان بوده است.
@
VahidOOnLine
من هم حدود ساعت ۱۰ صبح پیام‌ها و عکس‌های مختلفی درباره کنارک دریافت کره بودم + کلی پیام از چند شهر دیگر درباره پرتاب موشک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/VahidOnline/77427" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNBAMRdw6Llf749It_GI0iAkPePPiSzzvIar4IiJEq7ESG64gdp-if4UZ7nfAasu0nNIpf-Vf8WxiV-uG3k4Vwy4QQh6d7S1e-ScEa0CUSt8sDx7Sowu4DdRJaq7dq2gXggW520fFDJAPwoTSF_na_46gPPeo9vsjxgCFZRAZAAGweyEFyH-a6W00NesLbbSAnaYpUTdxbwwC11GxtiEPotMvWVsBKpz7VIQ0gLrgbc3afY3c9cQkH15_MjBMeqrHvTc_2M7ltJIVFcDw3CR7L4ewOhitIpGiEKKpAEYV0NlM2bZr7IBWTS8nCi1vVj8qIsCQoDfJQ55S6fQmG1yZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری
از داوطلبان آزمون کارشناسی ارشد در شهرستان‌های بستک و بندر خمیر استان هرمزگان به‌دلیل تخریب پل‌ها و بسته شدن مسیرهای ارتباطی پس از حملات آمریکا، از حضور در جلسه آزمون بازمانده‌اند. به گفته آن‌ها، با وجود اطلاع مسئولان از وضعیت منطقه، هیچ راهکار جایگزینی برای برگزاری آزمون یا انتقال داوطلبان ارائه نشد.
کانال تلگرامی «
دانشجویان متحد
» خبر داده است که شامگاه ۲۶ تیرماه ۱۴۰۵ و هم‌‌زمان‌‌‌ با برگزاری آزمون کارشناسی ارشد، پل‌های محور بستک–بندر خمیر–بندرعباس در حملات پهپادی سنتکام هدف قرار گرفت و مسیر ارتباطی این دو شهرستان با بندرعباس به‌طور کامل مسدود شد.
در حالی که حوزه امتحانی داوطلبان این مناطق در بندرعباس تعیین شده بود، بسته شدن جاده‌ها باعث شد هیچ‌یک از آن‌ها نتوانند خود را به محل برگزاری آزمون برسانند.
به گفته این داوطلبان، آن‌ها تا آخرین ساعات پیش از آزمون بارها با اداره راهداری و دیگر نهادهای مسئول تماس گرفتند، اما هیچ راه‌حلی برای انتقال یا تغییر حوزه امتحانی در نظر گرفته نشد.
این دانشجویان می‌گویند ماه‌ها برای شرکت در آزمون آماده شده بودند، اما در نهایت به‌دلیل شرایط جنگی و نبود تدبیر مسئولان، فرصت حضور در کنکور را از دست دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/VahidOnline/77426" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItSsRsTRtmCu1syfPrWatm8QN6NNaPVdAGWv9-2bHPgRcSj40-COOIX0aEAJWkC0N4GqFRhDSqP46P7td-9hkVtZTHRzRp9lRgVyKD4NIoJnVvBu7BT2fpIyOl2oICAMZRulbBL4mY7AQEY6TjvvWgZlltJW8bVeoY0f-ZIZ3tU1ToQCNZT4XYeu-01tV2uJwNljsMvGCx3iE3wCdbyPzQD3dTd4F7uF_qkg_4oza83ewoU1NNgRabj5T7WkBtDinlX3QOpCoDs-Xuoc6CJSa1ID0nH93DvmxkZchONzUNDwF8N_yp0bPjqjWFX_2kws76aDi6OZZx7SJTRNv4xLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا، در حاشیهٔ نشست آسه‌آن در مانیل، با تکرار اظهارات پیشین خود مبنی بر «آماده نبودن ایران برای توافق» گفت: «آن‌ها هزینهٔ این موضوع را خواهند پرداخت.»
مارکو روبیو روز پنج‌شنبه یکم مرداد گفت «هزینهٔ ایران هر شب بیشتر می‌شود تا زمانی که به خود بیایند» و افزود: «با وجود جسارت ایران، آن‌ها به‌شدت در عذاب‌اند و این رنج همچنان ادامه خواهد یافت.»
وزیر خارجه آمریکا در عین حال ابراز امیدواری کرد که حکومت ایران «احتمالاً به‌زودی» آمادهٔ توافق شود، اما تأکید کرد در حال حاضر به‌وضوح آمادهٔ توافق نیستند، «حداقل نه توافقی که حاضر باشند با آن کنار بیایند».
روبیو در پاسخ به سؤالی دربارهٔ اظهارات اخیر دونالد ترامپ دربارهٔ پرداخت هزینه از سوی ایران در ازای کشته شدن سربازان آمریکایی و حمله به کشتی‌ها در تنگهٔ هرمز نیز گفت سیاست ترامپ «سر در برابر چشم است و ایران هزینهٔ سنگینی خواهد پرداخت.»
وزیر خارجهٔ آمریکا همچنین با ابراز امیدواری نسبت به توقف حملات حوثی‌های یمن گفت: «امیدوارم آن‌ها تنش‌زدایی کنند، ایران آن‌ها را فریب داده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/VahidOnline/77425" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA7izafkC9qOf-cRyrO1GLxBsC6ZgB43uYTrYU69EC-XN43_kTighkgiac5-8zKRBcqcGysZGyESeM0mBab7vvBdBI2Dz8omvZLfJ_U-P47nxX5SjCuQfIVYCHsA0aQIFY-CPf8VBn6lQn1CrcusFlZwLyI3aVZT74YhTIQo4NnDhb_CWhsd65E1o46B8y5TNFZmwNfOAXFGsRQGVmfT9jRVQTAvZsvKzBEyxp1GZebKOQxeJU_GjiWrTf--Hudfbl5uUzVYlSaWsLW156rnRDMwAD8_eKlA1ISMvDfCA4DzeSGBLZ_hHVtH-e9diY8-6zGv3pccddaKaZauV-2u8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی برای دو نفر از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ احکام سنگینی صادر کرد؛ مهنام نواب‌صفوی به اعدام محکوم و حکم ۱۰ سال زندان علی صانعی نیز در دادگاه تجدیدنظر تایید شده است.
مهنام نواب‌صفوی، محبوس در زندان دستگرد اصفهان، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد با اتهام «محاربه» به اعدام محکوم شده است.
در پرونده او اتهام‌هایی از جمله «محاربه از طریق مشارکت در تخریب اموال عمومی»، «تبلیغ علیه نظام»، «اجتماع و تبانی علیه امنیت کشور» و «تشویق مردم به کشتار یکدیگر» مطرح شده است.
هم‌زمان، حکم ۱۰ سال حبس علی صانعی، دانشجوی ۲۲ ساله رشته کامپیوتر، در دادگاه تجدیدنظر تایید شد.
صانعی اسفندماه ۱۴۰۴ در ملارد بازداشت و به زندان تهران بزرگ منتقل شد. شعبه ۲۸ دادگاه انقلاب تهران به ریاست قاضی عموزاد او را با اتهام‌هایی از جمله «توهین به رهبری»، «اجتماع و تبانی علیه امنیت کشور»، «تبلیغ علیه نظام» و «همکاری با اسرائیل» به ۱۰ سال حبس محکوم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/VahidOnline/77424" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bn2kc6qWmC9M1loKI2zKAKhJfNVrAZSVhmNL5wqy6FSKWKmcA_-7FrpojQfEPHesFkvt43PJ5wHAH3ZzC2nIijS0MlPBT4SZ2Dx0QI1ThAv0h-6DJAe7JXu_fpTpYuxVYad0LX6WjwSb5VpBNRLTD9DexVsh5jxHBsFGIGa-GkQSkFysrbMrVOYer52HT7SfQMqI8OMheI07nPa6-LUmRmCAtRJoip4CQry_CREho_HHoFh7szjnSKA5OyCt1oaWge0jnsZj0ciuYOmqKXps_N0sas8laz9R98U2Z9_iItk6cQ0lmpBedskdAGKlyGkhsT1ZBFMD_HHLpcxphEhkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: آمریکا هم‌زمان با تشدید حملات به ایران، بمب‌افکن B-1 را به‌کار گرفت
ترجمه ماشین:
مقام‌های آمریکایی گفتند ارتش ایالات متحده روز سه‌شنبه برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران از یک بمب‌افکن دوربرد B-1 استفاده کرد.
چرا مهم است: این نخستین بار از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش بود که آمریکا مأموریتی با بمب‌افکن B-1 انجام داد.
استفاده از بمب‌افکن‌های B-1 که می‌توانند ۲۴ بمب ۲٬۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل‌توجه کارزار نظامی آمریکا بود.
‏B-1 می‌تواند در ارتفاع پایین با سرعتی بیشتر از سرعت صوت پرواز کند و در میان همه انواع بمب‌افکن‌ها، بیشترین محموله بمب را حمل کند.
هم‌زمان با ادامه افزایش حضور نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان در حال بررسی بازگشت به عملیات رزمی گسترده علیه ایران است. مقام‌های آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
اصل خبر: بمب‌افکن B-1 مأموریت خود را از یک پایگاه هوایی در بریتانیا آغاز کرد و در وب‌سایت‌های آنلاین رهگیری هواپیما مشاهده شد.
فرماندهی مرکزی ایالات متحده (سنتکام) در بیانیه روز سه‌شنبه خود درباره حملات آن روز، به مأموریت B-1 اشاره نکرد.
در این بیانیه آمده بود: «دارایی‌های سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.»
مشخص نیست B-1 چه هدفی را مورد حمله قرار داده و آیا این مأموریت عظیم از دیگر حملات چند روز گذشته مؤثرتر بوده است یا نه.
آمریکا در جریان عملیات «خشم حماسی» چندین مأموریت با B-1 انجام داد و پایگاه‌های موشکی، مراکز فرماندهی، تأسیسات نگهداری سلاح و سامانه‌های پدافند هوایی را هدف قرار داد.
وضعیت کنونی: با وجود گسترش حملات آمریکا، به نظر نمی‌رسد حکومت ایران موضع خود درباره تنگه هرمز را تغییر داده باشد. ایران همچنان به حملات علیه پایگاه‌های آمریکا در منطقه ادامه می‌دهد.
برخی مقام‌های دفاعی آمریکا می‌گویند توانایی نظامی ایران در اطراف تنگه هرمز «تقریباً از بین رفته است»، اما برخی دیگر می‌گویند ایران همچنان قادر به حمله به کشتی‌ها در این منطقه است.
رئیس‌جمهور ترامپ روز چهارشنبه تهدید کرد که اگر ایران به حملات بیشتر علیه کشتی‌ها در تنگه هرمز دست بزند، پل‌ها و نیروگاه‌ها، از جمله تأسیساتی در تهران، را بمباران خواهد کرد. ایران نیز در پاسخ، زیرساخت‌های کشورهای حاشیه خلیج فارس متحد آمریکا را تهدید کرد.
نمای گسترده‌تر: همچنین روز چهارشنبه، شورشیان حوثی برای نخستین بار از زمان اعلام محاصره بنادر عربستان سعودی، به کشتی‌های سعودی حمله کردند.
یک مقام دفاعی آمریکا گفت حملات حوثی‌ها، پس از چند ماه که تقریباً به‌طور کامل از جنگ دور مانده بودند، ممکن است با تحریک ایران انجام شده باشد.
این مقام گفت ایران می‌خواهد با استفاده از حوثی‌ها، علاوه بر خلیج فارس جبهه جدیدی در دریای سرخ ایجاد کند و بر یکی دیگر از مسیرهای حیاتی بین‌المللی حمل‌ونقل نفت فشار وارد کند.
روز چهارشنبه چندین کشتی تجاری در حال عبور از دریای سرخ دیده شدند که از بیم حملات حوثی‌ها، مسیر خود را تغییر دادند تا از تنگه باب‌المندب عبور نکنند.
آنچه باید زیر نظر داشت: مقام‌های آمریکایی گفتند میانجی‌های قطری همچنان با مقام‌های آمریکایی، ایرانی و عمانی گفت‌وگو می‌کنند تا به توافق جدیدی برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند؛ این موضوع را منابع مطلع اعلام کردند.
یک منبع منطقه‌ای گفت رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده از سوی میانجی‌ها را نپذیرفته است.
مشخص نیست ترامپ چه مدت به تلاش‌های دیپلماتیک فرصت خواهد داد. ترامپ چهارشنبه‌شب در سخنرانی‌ای در جورجیا گفت: «آن‌ها به‌شدت زیر ضربه هستند و می‌خواهند توافق کنند.»
«اما من می‌گویم آن‌ها آماده توافق نیستند، چون هر بار توافق می‌کنند می‌خواهند آن را عوض کنند و همه‌چیز را تغییر دهند. آن‌ها آماده نیستند. خیلی زود آماده خواهند شد.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77423" target="_blank">📅 07:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRyjIdwm7702coHGXo2bBtjAuS7iyP7IDDCggR_saiISRn0pEyZqlnI7CszHSxItuRj-dnIDm-hAfBaYw5Upbe6IUO1lGC7OgKpDAbrdtXZtNCxN8Z8brlLAjGcXP5QOO4DKlzuhzH3mLzmPCrlgEAM-oKamri0r1jeMnczWBiS3udQ5Mk3lP3cTfqtUn_3j7qm-EvLe0nztDzjbRJ8l9wJtxez2n6jY_Z2S5JSaOsai07shBWQVWpwE61iQ8iC2KBd3iEvuF3Qu8Va1Lr0D6EKsb__zCakw-OLP8CGdvpGh7ci4w6pg2pu3Eei_4me_-O0hnq7ffwYVLEO4WBT2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان (واس) تایید کرد که کشتی «انسیلیا» متعلق به یکی از شرکت‌های سعودی در دریای سرخ هدف قرار گرفته است.
به گزارش واس، در پی این حمله، آتش‌سوزی در بخش جلویی کشتی رخ داد، اما همه اعضای خدمه سالم هستند.
یک منبع در سازمان حمل‌ونقل عربستان نیز اعلام کرد نهادهای مسئول اقدامات لازم را برای تامین امنیت کشتی «انسیلیا» انجام داده‌اند.
پیش از این، حوثی‌های مورد حمایت جمهوری اسلامی اعلام کرده بودند که دو نفتکش عربستان سعودی را هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77422" target="_blank">📅 07:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/111a8149da.mp4?token=W3TeJI5TdvoqOjBmzuKrqf_U3lpuZAs5MgpFQxWxvu6LIqEIVEHLIargxye9jFlnIIMRJXk20DM7oyMb5jhh_O5JYVuZeDvomGoKcLpCBDSab4TmFJOodxJgXHSIQQ7QwXdx-KVh17Mc5dn-2wgZKfWzIzwzdJQSgK03ArHJ7oENHcjSDu1vdzZGlIeVj4etlcp_q8wPy6pqDUwc9dRADeX-AO5w9UIX2_PgNdArvUrHszAxVg15BNUZM2V8QOI6zOh41g49c4wMPJAj96rOuHycv4zMELhQsbjKZYKhxh5xvgUZ5IQaihBosH_g7U_JVSoCYi9nHZml5sdWCsbtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/111a8149da.mp4?token=W3TeJI5TdvoqOjBmzuKrqf_U3lpuZAs5MgpFQxWxvu6LIqEIVEHLIargxye9jFlnIIMRJXk20DM7oyMb5jhh_O5JYVuZeDvomGoKcLpCBDSab4TmFJOodxJgXHSIQQ7QwXdx-KVh17Mc5dn-2wgZKfWzIzwzdJQSgK03ArHJ7oENHcjSDu1vdzZGlIeVj4etlcp_q8wPy6pqDUwc9dRADeX-AO5w9UIX2_PgNdArvUrHszAxVg15BNUZM2V8QOI6zOh41g49c4wMPJAj96rOuHycv4zMELhQsbjKZYKhxh5xvgUZ5IQaihBosH_g7U_JVSoCYi9nHZml5sdWCsbtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا [۶ صبح به وقت تهران] در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
نیروهای آمریکایی اهداف نظامی ایران، از جمله توانمندی‌های دریایی، تأسیسات نگهداری موشک و پهپاد، مراکز نظارت ساحلی و تجهیزات پدافند هوایی را هدف قرار دادند. این حملات توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری را بیش از پیش تضعیف می‌کند.
در ماه جاری، نیروهای آمریکایی ده‌ها مرکز نظامی ایران در خشکی را هدف قرار داده‌اند و هم‌زمان محاصره دریایی علیه ایران را از سر گرفته‌اند. تا امروز، سنتکام برای جلوگیری از ورود کشتی‌ها به بنادر ایران یا خروج آن‌ها از این بنادر، مسیر ۹ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته است.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت هستند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77421" target="_blank">📅 06:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwUCZH1f-Ebw70ZyMEowSB_f1NZyutAUflkb1NBps4WF1aC0hTZ3dPQAu223AVR7hsdvEyWrwVKoA528WQ41NZsUIXJo-cy6RW_upC70dIJT2Up2gNqOADK61cuxG8zzFotVV5r4RoN6eFTiW7kJLHz6ZgdHdKq5MMgBCLsagX4sG7iV5hs1v5orFRxxDAxhAlkATURhEQ2AnCSG43Zfzgeek5dIy8jwFIS7-2n2QaQinwon3GnJ2MCja6eXPuAp7UbYc0PB_UxZW2j3yFMINFmjgVPuCNwDH1ZU384qbmnU-n-Sa7wKc_ca-Zs6vKCq4quQIV-ESnE5Iujjd2EKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه پیام دریافتی از ساعت ۵:۱۳:
دوتا انفجار سنگین پایگاه دریایی ارتش جاسک
جاسک ۲ بار زد
جاسک چند دقیقه پیش دوبار زدن . سلام
🔄
دوباره زدن
صدایی شبیه به جنگنده هم میاد
یک صدای وحشتناک انفجار جاسک 5:30
همین ۱ دیقه پیش دوباره جاسک زدن، نمیدونم دقیقا کجا ولی صدای خیلی شدیدی داشت
باز انفجار مهیب در بندرجاسک ۵:۳۱
جنگنده بالای سر شهر در حال چرخیدنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77420" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrlzmKGPGyQ-U_vtT_5FTagHM4clKSf4CC2UW94dY31WlK1AdQbvcxHPdhPwbUW4MZuwYfRGcDWHbjm-bp9cFpjuwdTmEaxCQUJq6F0NmyfQNLaZ0bZhwrRSjM_h1G7uDb6v51lH8gbpvaLCymWWKmQ_4r9SDguMZF1YbQg96pgCsA4OjoUUHO_OXrq4aAhtJ6HBzZ-uGY-5sqLd8mmB0n22skBqaD-ecLg9qHwwTgL9MqAIR-PTf8AIBgoSacOmrUIOBFkts9dE-Ow-A9PosvooZerHKXhgiP9UKE6l3HpdmxAEk6mets_pWHSp4fjDMuPzKLHvUiG_ZKplp55rgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mtBV24lZacQf5Rpq_G55RmFUwayWGgcx8hEerJ2g_IE3adTrSlsaN1r3Dxfc6cMychxhprvT6LGPqPReVkJn6H0e3896whGxTGmtQcp92kHi0d0fFwAC370UxXogEqpB__ZEB3AvbiLM5rfyw6uw3mouubg_DxrlPVt93vdo7HHdUEBP_0HepxrZPTDWc8jp5odwwvq4Opn3w0ffafbbajxMUDCD9Rr7JWjlJovuCF7Q8SdbWQTvTtsbiJ6MBml4X7s7NQPPqw8fhtQ-Pw7FLrfh3ahU14fYo08wIXnSoXNkc7DF5MlxKvIzZxKC-aurIlsC3tGjqUcy8-qmX04MTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PLfpYvcFcWRoRtx5XY0mzMsJ9WE0g-bO5p0corT1YBMSce8hU02Ss_Hc-6mP22cHiEg7micAS92jAxfyWOO5tWP0ek8b-vtLyoh_cGLXOVP1Yvyq_bvAsJKypXsN4UxN1X6QC4Y13aQKCrJGPsqYVUAW9Ivsh7laXny4ROZ6EG7Aep9WioHJDPCyO_7xS0FX-l3_sV4VehV4LZtAPinUzynmV5a7ySzBQdKT95sFNhcNl3jF5w-9c9uNpcKkYmWn4mqq0HLM2j02XOg8KWFbcQglrgaUJj7nfjTkkEzVAsZo_s6LPGUKvdXCQpUn9zVOpdd0jxzXh6YjzR88eWx2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kEemvNew_rNkWTdoDuPoqR3DM1jJSGB2_NWM95CfvR8G9koJR1gWGFSYWDKcqT2lH-7iZ_063wb8_8g5PBTSaUGFHfGabVoslGtszouBrE8AR52u2eEC8uIaT7yV67Zp0wI-G5VyYqlYiJoGhclStwABm2iSrNGm4kP7HCBziqR8lysgu3Jn64rJQKocEVcyXW0U2WBvMBfLUbolbg40b8Yk3Rgqc7Wm5kRMR3-ZnynDfYzkd2TU7HZGdkk6tho41grbcn3SkZPf94pNTb5sGsZNRoHmg5Wjq_eV4qi6gU4uBEV2eNV5MY9npr0Cq13WJc0PtjbXdE0p5Ex8oacXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر پخش شده با شرح: انفجارهای حمله به  اسلام‌آباد غرب در استان کرمانشاه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77416" target="_blank">📅 04:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBOYLX4PwoGXdX51k2Z-jI6Cc9t5PZZDLckwGK0cYSiDZqhD3YnZ9ggL_FOnQwW0M6xjpWmkhZYLpsPfnF_0cIwol79riMVejbQ57YRKriEiyi5j2WLJ7duV1Ul5VSCHIHKtru0ehLmS7JbLpZRdDj9nbwBhMVdfamC5hFkGQXm75p6XAUAGKinorIuQpKtMt20rC1hb8qou1SFcWRKF01Aqof49Ic8jaI-tePFiqFnn8YLJas09jbxuSnll8Ig-wfMI007ZIVgWNFiDo2mK-SDWRQeQ7nXZ1Cu1Oanec6n9aQmeoYQCyCwyfqd2dCkbIZU6t-4IBDbnn8aF2Tt3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، معاون استاندار خوزستان اعلام کرد یک نقطه در اطراف شهر اندیمشک هدف حمله موشکی قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77415" target="_blank">📅 04:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=hGhOau4Q0Mc_nS8HudAGtBiRPvevTQk6MaZs9veLc8se3mL1REzJlqakaETYfYG2H20uZEh6mNHCVSU8a33vUs9yO_o20t4HuINHgH8z2qJGAQSOw7JmVhIZIEZPXoyEjTuDGw47ycvUT_4eFauu7lpBjRAHrGNu2xsJPGgFRH98sQdirMZuF_Et27sIjIGlvBiSn2RRbPTQlnFmOTcjOX6uZligjbjdccCVcCnGP_Z5xM5WF-2yt-FrLbxiZh6EtZYb6cqFhjq8Fyu-YU69lUbfyRR5OjXQpgkZBomL0nt_w01QbP3rbOpfApz4xp6tunz1skSEMuu56sNBudMU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=hGhOau4Q0Mc_nS8HudAGtBiRPvevTQk6MaZs9veLc8se3mL1REzJlqakaETYfYG2H20uZEh6mNHCVSU8a33vUs9yO_o20t4HuINHgH8z2qJGAQSOw7JmVhIZIEZPXoyEjTuDGw47ycvUT_4eFauu7lpBjRAHrGNu2xsJPGgFRH98sQdirMZuF_Et27sIjIGlvBiSn2RRbPTQlnFmOTcjOX6uZligjbjdccCVcCnGP_Z5xM5WF-2yt-FrLbxiZh6EtZYb6cqFhjq8Fyu-YU69lUbfyRR5OjXQpgkZBomL0nt_w01QbP3rbOpfApz4xp6tunz1skSEMuu56sNBudMU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید بوشهر زدن بدددد
بوشهر انفجار خیلی شدید
😐
دستم میلرزه بزرگترین انفجار
سلام وحید همین الان انفجار خیلی شدیدی بوشهر از قبلیا خیلی بدتر بود
وحید بوشهر زد ساعت ۳:۵۹
بوشهر چند انفجار وحشتناک همزمان ساعت ۰۴:۰۰
بوشهر زدن ساعت ۳:۵۹
سلام وحید الان بوشهر رو زدن و خونه لرزید یه صدا خیلی زیاد هم اومد
انفجار سنگین شهر بوشهر ۴:۰۰
سلام وحید جان
ساعت 3:59 بوشهر رو زدن صداش متوسط بود
بوشهر صداش خیلیی بلند بود
همین الان وحشتناک بوشهر زد
همین الان بوشهر زدن ۴:۵۸
وحید جان بوشهر پایگاه هوایی باز زد الان
درود، همین الان
3:59
بوشهر رو زدن صدای مهیبی داشت
وحید جان بوشهر
همین الان زدن دقیق ۳ و ۵۹
یک انفجار نسبتاً شدید ساعت ۳:۵۹
۰۳:۵۹ بوشهر صدای انفجار خیلی شدید و خیلی نزدیک اومد
سلام بوشهر رو الان زد
همین الان یک دقیقه پیش انفجار وحشتناک بوشهر خونه لرزید
از بوشهر همین الان یه صدای خیلی بلند انفجار دقیقا نمی‌دونم چی بود اما خیلی بلند بود همه از خواب پریدیم
ساعت ۴ صبح انفجار مهیب در بوشهر
چندین انفجار بوشهر
یکیش خیلی بلند بود و لرزش داشت
داش بوشهر بغل خونمون انگار بمب اتم زدن
بوشهر صدای وحشتناک انفجار، گمانم پایگاه هوایی بود... ساعت ۴ صبح
همین الان خیلی شدید
از خواب بیدار شدیم
بوشهر
صدای انفجار خیلی شدید از پایگاه هوایی بوشهر
سلام همین الان بوشهررر صدای بدی اومد که همه بیدار شدن
تک انفجار ساعت ۴ ولی جوندار زدن
آپدیت:
پیام‌های ساعت ۴:۴۱:
صدای پدافند بوشهر
وحید بوشهر انفجار
ضدهوایی هم کار می‌کنه
بوشهر پایگاه هوایی صدای پدافند
بوشهر ۴و ۴۰ پدافند پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77414" target="_blank">📅 03:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">استان کرمانشاه
فقط سه پیام دریافتی در ده دقیقه:
انفجار کرمانشاه ۳:۳۶
اسلام آباد کرمانشاه رو زدن
سلام ۵دقیقه پیش اسلام آبادغرب در کرمانشاه را زد ۲تاانفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77413" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVkrlqG3WNvOfaXInpMz0-AcHz0AOoNzV7xhUh3LViV3bxpW2KhOOzpwAZt2LtJKVj-SetDF2FH2--Pk7YN0Hd1bn860rXtExkDrN_GDGEHn6eymOFjFwIJBOWNOVQjbIY-vDxF72MrmazMdu7EwhD_8kxfbuijRoPQN9oai-m5xL1YUp5XflqtIpwTAbVvyvgqIx5QMhrEDJEF0Q8WXc-J0NvsUSJGiwuiODtAjKfMsH6M6DFscm0Et0DfdjZZceauSbCrgX54AbSqNGMGpFGJ9n5OoHH4LFm6XkI6CI7gLb_n49GbcWAZpd7Z1l7nGmx9651B0AgHRCbgWy-bCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران صبح پنجشنبه در اطلاعیه‌ای گفت که سه کشتی قصد عبور از تنگه هرمز را داشتند که یکی از آنها آتش گرفت. سپاه دلیل آتش گرفتن این کشتی را برخورد با مین عنوان کرده است.
سپاه در این بیانیه تاکید کرده که کنترل تنگه هرمز را در اختیار دارد و هیچ کشتی از این تنگه عبور نمی‌کند. در عین حال ارتش آمریکا می‌گوید تنگه هرمز باز است و هفته‌های اخیر ۹۰۰ کشتی از آن عبور کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77412" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=K8iQF7TZuu2rOwt-Mfs5DP1APUdufM2169N3yEJEwwU1wNuX5Xb7YgZ-uh0wWAQ2jkP7cxQohFKPgKwJ_Cc15154PH02ccsXHzpmVd2OtxgBvwGPSg1mDq0aune2Ax4-MwZeq6Js3yRgmx5m2zvPayDDVAWP0AYdTg2qVDydDO1k06kZtUE8W0_BJ5Ejf6eTUWJIhopQqlE-HQZacTTaaoSG_984uGxFTFX7yR0Fc-l_1yJGpnS6PY0keKlVLb_RL2AbowxzX7wPYkPNUhRvB1qH-bj1SQOIVQqrAXXXPqsk5UDBNyPlNjndFNnux7DWldj0Pk17BchzVRlIHvDWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=K8iQF7TZuu2rOwt-Mfs5DP1APUdufM2169N3yEJEwwU1wNuX5Xb7YgZ-uh0wWAQ2jkP7cxQohFKPgKwJ_Cc15154PH02ccsXHzpmVd2OtxgBvwGPSg1mDq0aune2Ax4-MwZeq6Js3yRgmx5m2zvPayDDVAWP0AYdTg2qVDydDO1k06kZtUE8W0_BJ5Ejf6eTUWJIhopQqlE-HQZacTTaaoSG_984uGxFTFX7yR0Fc-l_1yJGpnS6PY0keKlVLb_RL2AbowxzX7wPYkPNUhRvB1qH-bj1SQOIVQqrAXXXPqsk5UDBNyPlNjndFNnux7DWldj0Pk17BchzVRlIHvDWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای منابع حکومتی: حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
به گفته وی، تردد زائرین بدون مشکل در حال انجام است.
منابع حکومتی: کشته شدن دو نفر
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77411" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KVbJ9xYW6AEbHrgza71Pt0LcKun1rkk6z-NSiuhR7F2Fr6rSj29XEIEnfFc3d6C8zDfWHGLFzpO6zpM3lhbfw7tcHgzHBqdR9OKAzdx93Q8HwOjgm2pkZ6Jb61l3-o2ISmv6ll4mPDWKVI7fmGVK9suoKDZSmJihe9QAuJbBQh0JHymlRD6jVGjeQhc-j3a73nQArfG_Nptlhr11XL8kprrthZl9Z2QpJ5eoreCWvvEf0wAt1M38Hk0puGxJ7Hs7kQSQKNGxnFpxD1QbFBmeNJbS2nFlWqT8pY1cMMnVNw4b6k2_S_Wz-8mMB17nXQzIwfNfEaOPjcSL1WY6pD-_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا گفت تفاهم‌نامه با جمهوری اسلامی بر پایه پایبندی به تعهدات بود، اما تهران آن را نقض کرد و در نتیجه این توافق دیگر معتبر نیست.
او افزود تفاهم‌نامه شامل بازگشایی تنگه هرمز و تضمین آزادی کشتیرانی بود و جمهوری اسلامی باید حدود یک هفته و نیم پیش بیانیه‌ای در این باره منتشر می‌کرد، اما در همان روز به یک کشتی حمله شد.
وزیر خارجه آمریکا همچنین گفت واشینگتن همچنان از دیپلماسی و راه‌حل مذاکره حمایت می‌کند، اما به نظر می‌رسد جمهوری اسلامی در حال حاضر در این زمینه جدی نیست.
روبیو افزود، چین نیز با اقدام‌های جمهوری اسلامی در تنگه هرمز و اعمال عوارض بر عبور کشتی‌ها مخالف است.
به گفته مارکو روبیو وزیر خارجه آمریکا، جمهوری اسلامی با مشکلات اقتصادی جدی روبه‌رو است و شهروندان ایران با تورم بالا و افزایش شدید قیمت مواد غذایی مواجه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77410" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنرانی ترامپ در ایالت جورجیا، بخش‌هایی مرتبط با ایران، ترجمه ماشین:
...
اما میلیون‌ها و میلیون‌ها بشکه نفت در راه است و ونزوئلا هم اکنون بهتر از هر زمان دیگری عمل می‌کند. شرکت‌های بزرگ نفتی وارد می‌شوند و قرارداد می‌بندند. کریس رایت روی آن کار می‌کند، داگ برگم هم روی آن کار می‌کند، اسکات هم با آن‌ها کار می‌کند و واقعاً فوق‌العاده بوده است. آنجا ذخایر عظیم نفت دارد.
در واقع، اگر آمریکا و ونزوئلا را با هم حساب کنید، حدود ۶۲ درصد بازار نفت جهان را در اختیار داریم. بنابراین ما به تنگه‌ها نیازی نداریم؛ به هیچ‌چیز نیاز نداریم. به تنگه هرمز نیازی نداریم، اما وارد عمل می‌شویم، چون مجبوریم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
در قبال جمهوری اسلامی ایران نیز در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز، هرگز نتوانند همان کاری را که با بسیاری کرده‌اند با ما انجام دهند. می‌دانید، آن‌ها بیش از ۵۲ هزار معترض را کشته‌اند. افرادی که اعتراض می‌کردند کشته شده‌اند؛ ۵۲ هزار نفر در چهار ماه گذشته. هیچ‌کس نمی‌خواهد درباره‌اش حرف بزند. رسانه‌های جعلی آن عقب هرگز به آن اشاره نمی‌کنند.
[ + جملاتی مربوط به مراسم سربازان کشته‌شده آمریکایی که در ویدیو هست ولی در پست جا نمیشه.]
---
بازار سهام رکورد زده است؛ آن هم در حالی که این درگیری کوچک در جریان است. من آن را یک «درگیری کوچک» می‌نامم. این درگیری کوچک ما با جمهوری اسلامی ایران است.
دلیل اینکه آن را این‌طور می‌نامم این است که، بگذارید بگویم، آن‌ها چنان سخت هدف قرار می‌گیرند و می‌خواهند توافق کنند. اما من می‌گویم هنوز برای توافق آماده نیستند، چون هر بار توافقی می‌کنند، می‌خواهند آن را تغییر دهند و چیزهای دیگر.
هنوز آماده نیستند. خیلی زود آماده خواهند شد. با وجود اینکه این وضعیت همچنان ادامه دارد، بازار سهام رکورد زده است.
---
نفت نیز پایین خواهد آمد؛ قیمتش سقوط خواهد کرد.
سه هفته پیش فکر می‌کردند توافق کرده‌ایم. گفتم: «فکر نمی‌کنم با این‌ها توافقی داشته باشیم. آن‌ها هر توافقی را که می‌بندند، نقض می‌کنند.»
اما مردم و نابغه‌های وال‌استریت فکر دیگری می‌کردند. قیمت نفت خیلی پایین آمد، بعد کمی بالا رفت، اما دوباره پایین خواهد آمد؛ شاید حتی پایین‌تر از زمانی که شروع کردیم. فقط کمی به من فرصت بدهید.
من همیشه می‌گویم: «کمی به من فرصت بدهید.» به کشاورزان هم گفتم: «کمی به من فرصت بدهید و ببینید اوضاع کشاورزان و مزارع چطور پیش می‌رود. این کشور با قدرت در حال پیشروی است.»
---
فقط در ۱۸ ماه، این کشور را به شکلی متحول کرده‌ایم که هیچ‌کس پیش‌تر ندیده است. فکرش را بکنید: مرز ما امن است، اشتغال افزایش یافته، تورم به‌شدت پایین آمده و کارخانه‌ها در حال افتتاح هستند.
سرمایه‌گذاری به کشورمان سرازیر می‌شود. گفتم: ۱۹٫۲ تریلیون دلار. ارتش ما با فاصله‌ای بسیار زیاد از همیشه قدرتمندتر است. می‌بینید؟ ونزوئلا، ایران.
آمریکا بازگشته است. از همیشه قدرتمندتر است و به شما می‌گویم که فقط در یک جهت حرکت می‌کند: رو به بالا.
تا زمانی که همین طرز فکر و همین نظام کنونی را حفظ کنیم، رو به بالا می‌رویم. اگر راه دیگری را بروید، هیچ‌چیز موفق نمی‌شود.
یک بار گفتم: «در کمونیسم، همه‌چیز به گُه تبدیل می‌شود.»
بسیار خب؟ حقیقت دارد. چیز وحشتناکی است.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77409" target="_blank">📅 03:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzhDVgmcc6mctYbkBpKLV6YJX2kFHpRLICXGlZCPqi7ETl2L1XHyvXKpenBLUbUAxi5AyipN2L9JMBkr__1-KY4zEwClfnSKjZF2oQRLWZCkEsRLNlvuOVjG4ayErXUIzpqClwSyeV2SOZpOTs7FOVt4Bl-2b8Dla_j3A5FNtuiJnFRdAo2Dci7Vs7T9P42cU9EYnWKa1F_7HmgzLIEDn1SbZqLyCs4-RLfSoVsXYT298mn9UncDS4kMopxt0GcUZSNja9C0YHzigxbM7CaNQIBz38YOoGuQJYCj_lQvQaGYpBPL1H482PsAZpgYf1ftq3fN9SuJyka7sGxK3Q9HTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستاد کل ارتش کویت، بامداد پنجشنبه اول مردادماه، با صدور بیانیه‌ای اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» هستند.
در این بیانیه، این حملات تاکید شده است که صداهای انفجار احتمالی، ناشی از رهگیری و انهدام این اهداف توسط سامانه‌های دفاعی کویت در پی حملات «تجاوزکارانه ایران» است.
ارتش کویت همچنین از شهروندان خواست ضمن حفظ آرامش، دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77408" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJEguQ-Z2UjmOgCf5bhsAMFeZtBzGBye63fEh52r8I-LvFkq1Q3CsOczE6Y1lcOmmGQ8e7TnrX81IfpHuzNu-5u18FDCnE8hSjDpW8F3OEZZ8T2RXJHAdYUrhkaWuiJfxGezS29MNuB1QJON9BFQ8BFkY4YeNVrJIKo13p0xrA1FUaO6e-7uBre5Zq0tedrdLJqcerLzLUumS7R3XL_RUxgwu5dzuy0LR9S3y9CjVv3g9tiHC-rP9sZHKmON1hzzHxUwqjvJEmnwcvzKNsbhTPtvV7PEiNXKJfRIqagmhoikhhYswAPw3tHNisxRdQxlm8czOevB6TF2UcCo1idVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۳۰ بعدازظهر به وقت شرق آمریکا [ساعت ۱:۰۰ بامداد پنج‌شنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات علیه اهداف نظامی ایران را آغاز کردند. این عملیات ادامه خواهد یافت تا توانایی ایران برای تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال تردد در آب‌های منطقه بیش از پیش تضعیف شود.
CENTCOM
نکته قابل توجه این که همه گزارش‌های امشب درباره صدای انفجارها مربوط به پیش از ساعت یک بامداد بودند!
حالا یا ساعت رو درست ننوشتند یا اون حملات کار آمریکا نبوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77407" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qDNVySzz2EZ2qpr4N13dar6zeKgM9AOHZnRk3IhnIOYq2k4GY3mcvhNY7-J1OULTjwx8B6eqwdr47-CFGKhAtY-KGz_h8w_9jKU9J7ZcS6pfxLLlNM_dbR7yubbpQb_6YDnW3d5NehTZaBhwM0kkciNE4lzFiFJk_WY4lmbEnl6BeQe8kiQwRmnqB1RA3fmfSzPh9UULzB205SJViZRxm2jJmDpb9k8MpTZwlpl5JzA0HnXedXu-GNjcN4be-j8JJlJa5vq_MntjCtSDziCPmugC_8CQCtJztZRWFdgwzKkXnWEoV5x2RGuFCoGZdWIYOe-air0sCjyuqmNh4lTQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت گزارش در تصویر: ۲۳:۳۰ چهارشنبه به وقت ایران
یعنی قبل از گزارش‌ها درباره شنیده شدن صدای انفجارهای خوزستان و هرمزگان در بامداد پنج‌شنبه
ترجمه ماشین:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در ۷۰ مایل دریایی جنوب‌غربی الشقیق، عربستان سعودی، دریافت کرده است.
ناخدای یک نفتکش گزارش داده است که یک پرتابه ناشناس به کشتی برخورد کرده و باعث آتش‌سوزی در عرشه شده است؛ خدمه در حال حاضر مشغول مهار آتش هستند.
هیچ تلفاتی یا پیامد زیست‌محیطی گزارش نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77406" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
سلام بوشهر دو صدای انفجار ساعت 12 و 49
صدای دو انفجار بوشهر 0.49
بوشهر و زد همین الان
سلام وحید بوشهر همین الان دوتا پشت سر هم بد زدن
وحید بوشهر زد دوبار ۰۰:۴۹
خود بوشهر زدن ساعت۱۲:۴۹ دوتا پشت هم
دوتا انفجار خیلی شدیدبوشهر
پایگاه هوایی الان
همین الان بوشهر ساعت ۱۲.۴۹ سمت بهمنی رو زدند.
وحید بوشهر پایگاه هوایی زد
سلام،۱۲:۴۹ دقیقه دوبار بوشهر رو زدن
بوشهر ساعت ۱۲:۴۹
سه صدای انفجار
۰۰:۴۹ صدای دو انفجار شهر بوشهر
بوشهر دو سه انفجار بود خیلی صدا داشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77405" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنیم:
شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
دوباره، تسنیم:
بر اساس گزارش منابع محلی، ۵۰ دقیقه بامداد صدای انفجار در سیریک شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77404" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در اهواز صدایی شنیده شده.
آپدیت: چند پیام هم از رامشیر، ماهشهر و سربندر داشتم.
پیام‌های دریافتی درباره اهواز:
وححححيييد
زدن
بعد از روزها..
اهواز ساعت ١٢:٠٩
اهوازو زدن
اهواز انفجار ۱۲:۹
وحید جان اهواز ۰۰:۰۸ صدای انفجار شدید
آقا اهواز زد دو بار
اهواز انفجار ۱۲:۹
سلام ساعت ۰۰:۰۹ اهواز صدای انفجار اومد
سلام وحید اهواز همین الان صدا برخورد اومد
۰۰:۰۸ دقیقا
سلام وحید اهواز یه صدایی اومد ۱۲:۰۹
اهواز ۱۲:۱۰ صدای انفجار
وحید همین الان ۱ ۱۰دقیقه بامداد انفجار شدید اهواز
وحید داداش ۲ تا انفجار ۰۰:۹ اهواز
اهواز به نظر میاد ساعت 00.10 یه انفجار مهیب بود. فقط لرزش رو حس کردیم.
سلام وحید جان اهوازو زدن
00:08  اهواز انفجار
وحید اهواز ساعت ۱۲:۰۹ دقیقه ۲ بار صدا انفجار اومد
سلام اهواز صدای یک انفجار شنیدیم
اهواز دو تا صدا اومد
وحید الان اهواز ۲بار پشت سرهم صدا اومد
تو اهواز دوبار صدای انفجار اومد
🔄
منابع حکومتی:
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: یک نقطه در اطراف شهر اهواز توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت.
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77403" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HabxSSSz17rywZtQvlLn5xZFfvvu36IBJrRUkGAjT344DzmeYyPOg2cQndXyQMTJcbtNKNdnmCk5ZqMvpAcbV41HvXn42Le7J6GEuAaZaV8Uyat2BBay9oF4MM-Dv-DvnnSiYA9Xz_C_uuptcwMs9qUqmr4K8rQHq_zubepccku6yAjeOPRZmkC2zvHugax7tC48pz633MRIwfUGs_-j_OfqCbSPT1Poloa-_IpU8fZlgjC9MoDzFoUxGEGNJh_BXS5PB776fMgHUboQ1UUWBNcqJly_MGWqowkm3q2dPkeUSLIxQvaAe1SN-0IuSpGY9d0xejOgSRL9389iHaAfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: امروز نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران مدعی شد که ورود و خروج از تنگه هرمز را کنترل می‌کند؛ ادعایی که نشان می‌دهد دریانوردان بین‌المللی فقط می‌توانند از مسیرهای مورد نظر سپاه استفاده کنند. این ادعا نادرست است.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این آبراه بین‌المللی، صرف‌نظر از تهدیدها و حملات سپاه، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77402" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
دکترین دفاعی ما روشن است: چشم در برابر چشم.
هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قدرتمند و قاطع روبه‌رو خواهد شد.
کسانی که به هر شکلی در چنین تجاوزی مشارکت داشته باشند، آن‌ها نیز اهداف مشروع تلقی خواهند شد.
Our defense doctrine is clear: eye for an eye.
Any aggression against Iran, including our infrastructure, will compel a powerful and decisive response.
Those who contribute to such aggression, whatever the kind of support, will also be considered as legitimate targets.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77401" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اکسیوس:‌ رئیس جدید موساد با رئیس سیا درباره ایران دیدار کرد
ترجمه ماشین:
به گفته دو منبع مطلع، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
چرا مهم است: گوفمن یکی از نزدیک‌ترین مشاوران بنیامین نتانیاهو، نخست‌وزیر اسرائیل، است. این نخستین سفر او به واشنگتن از زمان تصدی این مقام در ماه ژوئن بود.
خبر اصلی: سفر رئیس موساد درست پیش از تشدید تنش‌ها در تنگه هرمز و ازسرگیری درگیری‌ها انجام شد.
یک منبع اسرائیلی گفت یکی از اهداف سفر گوفمن، هماهنگی با کاخ سفید درباره مذاکرات با ایران برای دستیابی به یک توافق هسته‌ای بود.
پشت پرده: منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد.
سیا و موساد از اظهارنظر خودداری کردند.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77400" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پست قالیباف:
معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت. اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است. بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77399" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=MFov2Lc4Lpe_66w6SE1BNvUnak3MSJRGqi8ayY5lGFA2Q6-H1U6UxBDi2Z4oAmhW18abR7XDcsyG-fMBw7mYgmenIjgKGJNsyzoURT531G1MWHbqRPsERhkdDGgt1f_XjS0MoRYdlFpt48BjyzA7MMcyI58Uh7Azae7Dc6edPqgVqpht5E9e-jBZjpJmQWpC8Dl77c8zpWW9VZMD5DEzMO-CpztEr8CPfakOaYPYD296_FR_Wn_MO1k-53PLBKlQMrezcDuYfiMBoWGhzPGrkmmxPNiRrmbWaA5Hp_Q7opymp5zAzTILSik2G2Ysxvba7tGA8kfPu84Atja_whBLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=MFov2Lc4Lpe_66w6SE1BNvUnak3MSJRGqi8ayY5lGFA2Q6-H1U6UxBDi2Z4oAmhW18abR7XDcsyG-fMBw7mYgmenIjgKGJNsyzoURT531G1MWHbqRPsERhkdDGgt1f_XjS0MoRYdlFpt48BjyzA7MMcyI58Uh7Azae7Dc6edPqgVqpht5E9e-jBZjpJmQWpC8Dl77c8zpWW9VZMD5DEzMO-CpztEr8CPfakOaYPYD296_FR_Wn_MO1k-53PLBKlQMrezcDuYfiMBoWGhzPGrkmmxPNiRrmbWaA5Hp_Q7opymp5zAzTILSik2G2Ysxvba7tGA8kfPu84Atja_whBLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ کاخ سفید را به مقصد پایگاه نیروی هوایی «دوور» ترک کرد تا در مراسم رسمی مربوط به سربازان آمریکایی کشته‌شده شرکت کند.
تشخیص و ترجمه ماشین:
ترامپ:
برای ادای احترام به قهرمانان‌مان می‌رویم؛ و آنها واقعاً قهرمانان بزرگی هستند. واقعاً. آنها گفتند، و همه‌شان با قاطعیت گفتند: «نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد.» آنها سلاح هسته‌ای نخواهند داشت.
بنابراین می‌خواهیم به آنها ادای احترام کنیم. این برای من یکی از سخت‌ترین کارهایی است که یک رئیس‌جمهور باید انجام بدهد، اما باید انجام شود. فکر می‌کنم، همان‌طور که برای ادای احترام به این سربازان می‌رویم...
خبرنگار:
آیا درباره تحقیقات، اطلاعات تازه‌ای دارید که مشخص کند [چگونه آن‌ها در اردن کشته شده‌اند]؟
ترامپ:
نه، دارند روی آن کار می‌کنند. نتایج منتشر خواهد شد. می‌دانید چیست؟ ایران...
خبرنگار: [گفته می‌شود ایران پادگان‌ها را هدف قرار داده].
ترامپ: نمی‌دانم. خب، آنها بهای سنگینی خواهند پرداخت. دارند... در حال نابود شدن هستند.
خبرنگار:
قطعاً در میان خانواده‌های این سربازان، کسانی هستند که با این جنگ مخالف‌اند. به آنها چه می‌گویید؟
ترامپ:
خب، آمریکایی‌ها مخالف جنگ نیستند. یک نظرسنجی... یک نظرسنجی همین حالا منتشر شده. آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند. این موضوع در آن نظرسنجی کاملاً روشن بود.
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد. شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید خوب است؟ بفرمایید.
خبرنگار:
[نامفهوم]؛ به آن چه پاسخی می‌دهید؟
ترامپ:
تنها چیزی که خواهم گفت این است: «دوستتان داریم. فرزندتان را دوست داریم.» و آنها برای خانواده‌هایشان همین هستند؛ آنها فرزندان‌شان هستند. هیچ بازی‌ای در کار نیست، هیچ‌چیز. او فرزندشان است. و تنها کاری که می‌توانید بکنید این است که هرچه در دل دارید نثارشان کنید.
متشکرم. بسیار متشکرم.
خبرنگار:
پس مذاکره با آنها در بحبوحه جنگ چه فایده‌ای دارد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77398" target="_blank">📅 18:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/huAn-Q6uSdY8HeGVgNuQuyWBxPJXJkzrIbAhAx939mb1GjwUOFPO22ElhDbd_ynMn_49l2VqsnGaAD6a3canJvGc0L66CkDGzPo4BbnHwhwT5AJqzPsdYqCk5yo1UPaeIdctLyoKH3UZTJS14SkMsdU6DnixU8Ravs8Fi9Quxl4P-WAuLl9GeDxV1h9cFfW9i32aG96Q0m7pvjZ1fv36m4RW0MtTJc3F4ocHZdRDnmIY-EOqpt4z2RtR7fjl74JwshJGfqW-viORQDQ7OhKzbcxL64SKKkI567dsS6tKh10Vpis6ppf4g70ZCEhndFjLJx8X1PSiOPnf9YYTcG13lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز چهارشنبه ۳۱ تیر، گزارش داد جزیره لارک در تنگه هرمز ساعت ۱۴:۴۸ هدف حمله موشکی آمریکا قرار گرفته و به گفته ساکنان منطقه، صدای انفجار شدیدی در حوالی این جزیره شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77397" target="_blank">📅 17:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJ0xlID4CCuHkW2-m-bAhpg7sA6hZ4NjeuBJr-FCMlALa6Z0EnS6bV-g4Fl-BTcwLHgN2ZlUw0zGBjIEeJ6HXjToQ0JNF9N1VO3WCZ4nbqdYxUUE2Tfh7DRWMHUTWX-d_ysnHxeRqQnZFQoJe4kIq_JLvd4KvZ7LGYtI5Sjq6RYBlZzx1K9dN52Zf_y8X82h5e2ravfB3mWo0K6jJhDuNkkBgwfSfLEuEJ8jRcnaQ7V3nYv2-CguIKX8OvSOt4mkMxnyVaDqfchXZ4HBYmd3wv1SuDKfm8g86ucUFJW7smm41N2sOTmn0aIdzUVmuxXkm5QclCfEXssg83alx9wWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
از این لحظه به بعد،
هر بار که جمهوری اسلامی ایران به یک کشتی در تنگه هرمز شلیک کند
ــ چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری ــ
ایالات متحده
یک پل یا نیروگاه برق
را بمباران و نابود خواهد کرد؛
از جمله پل‌ها یا نیروگاه‌هایی که در نزدیکی یا داخل پایتخت، شهر تهران، قرار دارند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
From this point forward, any time the Islamic Republic of Iran shoots at a ship in the Strait of Hormuz, whether it be by Missile, Rocket, Drone, or any other device or weapon, the United States will bomb and destroy ONE BRIDGE OR POWER PLANT, including those located next to, or in, the Capital City of Tehran. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
پل و نیروگاه برق رو با حروف بزرگ تایپ کرده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77396" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fym5-jPPesWIhFR6mMC7Dd7fcZ3H5-ReUOjABL4pkZsZo6iBOy61zGM-iltMhXhr6S_FcbUCzIbK09k1lrlpKPWlyXB9o8wGSV-MNaoPDVXhzWkOZGiHn8a2VRQwJ-s17R6Na9TKMCpZZGuB8rMQ1KvtxcpPupAogeZQoarhaLmoVsb-zUVmwxVD2IbsE48lbR8eJWAmJ73_2f_35-UFqTKQr8UnR5tY1-gt19BBQ1mUEUPY7UA5wxdJH1T4Xm57NVTKVxPfe7JeOImGM7SJZV5f-lyVKDeKk6iZ9VXFV42MSmGGSItNIlJeHzLU1B5TlJFS_y4dCenWhScKBr_x1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز چهارشنبه ۳۱ تیرماه با انتشار پیامی در اکس نوشت که ایران هیچ فعالیت هسته‌ای در «کوه‌گلنگ» ندارد.
این نخستین واکنش رسمی یک مقام جمهوری اسلامی به گزارش‌ها از انتقال هزاران سانتریفیوژ به کوه‌کلنگ در پاییز سال گذشته به شمار می‌رود.
بقایی در این پیام نوشت:‌ «حملات و تهدیدات مکرر ایالات متحده علیه تاسیسات هسته‌ای صلح‌آمیز ایران نه تنها نقض آشکار اصول اساسی منشور سازمان ملل متحد، حقوق بین‌الملل و قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، کنفرانس عمومی و شورای امنیت سازمان ملل متحد است، بلکه دشمنی ریشه‌دار ایالات متحده با پیشرفت علمی و توسعه فناوری ایران را نیز آشکار می‌کند.»
دونالد ترامپ، رئیس جمهوری آمریکا روز گذشته و در جریان دیدار با رئیس جمهوری لبنان گفته بود فکر می‌کند به‌زودی ضربه سختی به این تاسیسات هسته‌ای ایران خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77395" target="_blank">📅 17:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6910775c10.mp4?token=Co46xaerFZGO5KmxCrzOPdp-KYDYNH6v6uOD2Ro0mXDhl32XPcwZWjxAIzlyyNdZoiGHCeH6i0MB8aWe3gpB0B5etnX8_AKJ04ldn2-dBTbogNAHg73Rfr6NC1H_Jb6uq0mAKcPgwRcf_b5RUGwB3DxMf2jYGaCAvT7ZPjYX0ZmkqKD6rWQxGd-2N7ilLa1VrB9inwctFIgnUkdjhv5_FAmzbsJcmSE5GYLc0wIyswwllcAep6byl_H29AMMqEPGvBdRVEDufL755JX8aRz2nwjn3hEtORNxcrOxiRb--fHpmyNkflMXUIfsOhcW65z05jBk065NppD9JqRkbywvvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6910775c10.mp4?token=Co46xaerFZGO5KmxCrzOPdp-KYDYNH6v6uOD2Ro0mXDhl32XPcwZWjxAIzlyyNdZoiGHCeH6i0MB8aWe3gpB0B5etnX8_AKJ04ldn2-dBTbogNAHg73Rfr6NC1H_Jb6uq0mAKcPgwRcf_b5RUGwB3DxMf2jYGaCAvT7ZPjYX0ZmkqKD6rWQxGd-2N7ilLa1VrB9inwctFIgnUkdjhv5_FAmzbsJcmSE5GYLc0wIyswwllcAep6byl_H29AMMqEPGvBdRVEDufL755JX8aRz2nwjn3hEtORNxcrOxiRb--fHpmyNkflMXUIfsOhcW65z05jBk065NppD9JqRkbywvvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید واشینگتن برای تعامل و گفت‌وگو با ایران با هدف حل‌وفصل اختلافات آمادگی دارد.
مارکو روبیو که در مانیل پایتخت فیلیپین به‌سر می‌برد، گفت مشکل این است که «تهران در مورد گفت‌وگو جدی نیست».
وزیر خارجۀ آمریکا در دیدار با همتایانش از کشورهای جنوب شرقی آسیا عضو آسه‌آن، که نسبت به دور جدید درگیری‌ها بین آمریکا و ایران ابراز نگرانی جدی می‌کنند، گفت: «اگر ایرانی‌ها جدی باشند، ما هم جدی هستیم. اگر آنها جدی نباشند، آنوقت برای حفاظت از منافع‌ حود و متحدانمان به هر اقدامی که لازم باشد، دست می‌زنیم».
مارکو روبیو در این نشست همچنین گفت باز گذاشتن دست ایران برای کنترل تنگۀ هرمز، «سابقه‌ای خطرناک» را بوجود خواهد آورد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77394" target="_blank">📅 17:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77393">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDrfPXVfPyA37o-BV6QU3nTIFOGm1yd3JXMgfFzyhcDRnaYgpdd1M9aakohxQ0ramG-zgMYpuPyf73h-5cAoTuk7Wn31yUcy_S6uOlrbpY1dqUi-aTzAKmEy7rmBLnh3vb9vi5GCPO9iH-MwT4TQvWV14QplO46XGChkoeW8X9iW-gd7Ind1pue62s3ul7RqLd28YyRvZ72etfFIVCpFTOaXvJRuUATGQbUzcP9Nn4V4h8SgQ07Zr7MppdBdQRHv5bevfL-w_PreyzdaEM9L_q2lW-35gcfKOVvS-WyznbFc60_7EkgEzWu-3lrMvwzkxwsaEXuAb_xEoYHwc-ZeTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعدام آقای مهدی خانکی؛ از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴
🔸
مرکز رسانه قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام آقای مهدی خانکی، از بازداشت‌شدگان مرتبط با اعتراضات سراسری دی‌ماه ۱۴۰۴، خبر داد. این نهاد اعلام کرده است که وی پس از تأیید حکم در دیوان عالی کشور اعدام شده، اما زمان و محل اجرای حکم را اعلام نکرده است.
🔸
قوه قضاییه مدعی است که آقای مهدی خانکی به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» و همچنین «ساخت، تهیه و نگهداری اسلحه، مهمات جنگی و استفاده از آنها» از سوی دادگاه انقلاب کرج به اعدام و مصادره اموال محکوم شده بود. این نهاد همچنین ادعا کرده که وی در ۲۱ بهمن ۱۴۰۴ در کرج بازداشت شده و در بازرسی از منزلش سلاح، مهمات و مواد منفجره کشف شده است.
🔸
با این حال، جزئیات مستقلی درباره روند دادرسی، مستندات پرونده، نحوه اخذ این اعترافات و دسترسی وی به وکیل مستقل منتشر نشده است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77393" target="_blank">📅 17:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77392">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معاون استاندار همدان اعلام کرد در ادامه حملات آمریکا، ساعتی پیش نقاطی در شهرستان کبودرآهنگ هدف حمله هوایی قرار گرفت.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
پیام ساعت ۳:۵۹
آقا پادگان نوژه همدان شخم زدن
پیام ساعت ۴:۰۸
سلام پایگاه نوژه همدان صدا انفجار پی در پی اومد
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد آمریکا ساعت ۰۲:۵۵ بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه در استان کردستان را هدف حمله قرار داد.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
وحید بانه رو زدن
صدای انفجار همین الان اومد
بیرون شهره نمیدونم کجاست
بانه صدای جنگنده اومد
بعد صدای انفجار ازدور  میاد
همین الان‌۲:۵۸ دقیقه
برای سومین شب متوالی
گردنه خان بانه رو زدن
همون تایم
پیام قبلی ایشون (شب قبلش):
رادار گردنه خان بانه رو زدن
ساعت 2.20 نصف شب
چوار، آبدانان، انارک و دینارکوه در استان ایلام نیز هدف حمله قرار گرفتند.
فرماندار آبدانان گفت این حمله‌ها هیچ تلفات جانی نداشته است، اما حمله هوایی به منطقه انارک در چوار باعث آتش‌سوزی در زمین‌های منابع طبیعی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 505K · <a href="https://t.me/VahidOnline/77392" target="_blank">📅 05:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی:
من تهرانم دوباره صدای پدافند داره میاد
پدافند مشیریه
دوباره پدافند داره کار میکند شرق تهران
صدای پدافند شدید افسریه
فعال شدن مجدد پدافند همین الان خ پیروزی
فعالیت پدافند شرق تهران. ۴:۵۱.
ساعت 4:52 دقیقه فعالیت پدافند شرق تهران
جنوب تهران پدافند 4:51
وحید من منطقه ۱۵ ناحیه ۴ تهران هستم محله مشیریه ۶ انفجار اومد پدافند به شدت فعاله ساعت ۴ و ۵۰ دقیقه
[صدای انفجار لزوما به معنای برخورد نیست. توپ‌های ضدهوایی هم با صدای انفجار شلیک می‌کنند.]
🔄
سلام وحید جان منطقه ۱۵ تهران همین الان ساعت ۰۵/۱۵ پدافند مشغوله
ساعت 5:15 دوباره صدای پدافند در مشیریه
سلام باز مشیریه همین الان صدا اومد
😂
😐
سلام الان ساعت ۵:۱۴ دقیقه صدای توپ های ضد هوایی و پدافند از جنوب شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77391" target="_blank">📅 04:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=lGPisvZwDAyEYu9kS9Ke2amF2HjzyynMRBjV6RJAeZeC_RRV-KTJVZY3PNRHK3OcXYCRkTptDV4T_TSht066etu1EHHqX9Tly_2O3UZuQOj6092cnxEA2-TgFDqifjIlvKAPYYFYFC20cCXgdAPkqDgNGl-LptxEf7kd0q6Bh9nIchkwQt-JiEY0yu7QQ0l2oO5kE5zvq9o7jnCX4N8N3eELYHth6PNtH9XbiO5Ln9Xvb-isxstT6ChzhcsL1to0fTERqSbg_ytS9DQw_wzu26mc6imAeKao6T4GEaGpdtDx9V-suIRRdm6G2TkfgZkNcNhwdmcR3zAH9uIQSASAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=lGPisvZwDAyEYu9kS9Ke2amF2HjzyynMRBjV6RJAeZeC_RRV-KTJVZY3PNRHK3OcXYCRkTptDV4T_TSht066etu1EHHqX9Tly_2O3UZuQOj6092cnxEA2-TgFDqifjIlvKAPYYFYFC20cCXgdAPkqDgNGl-LptxEf7kd0q6Bh9nIchkwQt-JiEY0yu7QQ0l2oO5kE5zvq9o7jnCX4N8N3eELYHth6PNtH9XbiO5Ln9Xvb-isxstT6ChzhcsL1to0fTERqSbg_ytS9DQw_wzu26mc6imAeKao6T4GEaGpdtDx9V-suIRRdm6G2TkfgZkNcNhwdmcR3zAH9uIQSASAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا یازدهمین شب حملات علیه ایران را به پایان رساندند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۸:۱۵ شب ۲۱ ژوئیه به وقت شرق آمریکا [۳:۴۵ به وقت تهران]، یازدهمین شب متوالی حملات علیه ایران را با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.
ایران طی سه ماه گذشته به بیش از ۳۰ کشتی تجاری در حال عبور از این آبراه بین‌المللی که برای تجارت منطقه‌ای و جهانی حیاتی است، حمله کرده است. این حملات بی‌دلیل، صدها دریانورد بی‌گناه را به خطر انداخته و آزادی کشتیرانی را تضعیف کرده‌اند.
با وجود اقدامات تجاوزکارانه ایران، تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77390" target="_blank">📅 04:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=jPcUGx3x9L_MTSgk8WlOLC_Yfn3SzrnAVnaixaR8AJIH4_Wl36FZ4Kr2ArDAD01ROlAGOLE410QM6TYsgK9tdaq_W5nP1vE1aOn5WJXIxfy-HjtnCAv37BYiZcadeq5rg5-6TWIMSVwsdNk3-ULhXxecgwjO102BUPDByTllfVZA7folmt158d8KzO1fSZpvmAofWxP0e-fe08QWHi6MNhzfrmUojJMXVOevmjKnb1UFLElTqVgNlzE51NFCzF1GByursxpVYGHoDU_pVoJWuxuXHGemug5sHkJjQbcP5xHSr-sDYpU-SJf6Mq3AeC3TZytbj2gIHpKcopNS24RPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=jPcUGx3x9L_MTSgk8WlOLC_Yfn3SzrnAVnaixaR8AJIH4_Wl36FZ4Kr2ArDAD01ROlAGOLE410QM6TYsgK9tdaq_W5nP1vE1aOn5WJXIxfy-HjtnCAv37BYiZcadeq5rg5-6TWIMSVwsdNk3-ULhXxecgwjO102BUPDByTllfVZA7folmt158d8KzO1fSZpvmAofWxP0e-fe08QWHi6MNhzfrmUojJMXVOevmjKnb1UFLElTqVgNlzE51NFCzF1GByursxpVYGHoDU_pVoJWuxuXHGemug5sHkJjQbcP5xHSr-sDYpU-SJf6Mq3AeC3TZytbj2gIHpKcopNS24RPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح شعله‌های انفجارهای حمله به 'پادگان بخردیان در بهبهان خوزستان'
چهارشنبه ۳۱ تیر، حدود ساعت ۲:۳۰، هم‌زمان با آغاز اعلام حملات از سوی آمریکا
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77386" target="_blank">📅 04:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌های دریافتی:
سلام اصفهان صدای پدافند اومد
پدافند اصفهان فعال شد . سمت بهارستان و صفه
اصفهان صدای انفجار اومد الان چندتا پشت هم ولی از خیلی دور
ساعت ۴ صبح صدای پدافند جنوب شهر اصفهان
جنوب اصفهان شهر موشکی رو به روی بهارستان پدافند فعال شد ساعت 4:5
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77385" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=LhNuwNDzuQ6mdle6eQXZeNEs0xTxKG7u57GLspYCwmh_t9e9lQuocpt9lf9plgZqz--zvY6OuaL9PEo7cBgioE9O8gY1Y7S40BZjps0eymuNF4420vwhZ5219x7HDCSKByvm75dlxoAd1Stga492nS47Ro2RUt8Nt23UdDa7rpAyFTJXaShVApUyaeZSZCu_gUxdl2HIAG4IXbUq18fzC-a_5pl-rJ0wjcYP9aRTIpMYbKpJ5Cq_-5ehjQoUMtpCFLd1SPQhjPLKvoM5daKCGgsYA2MjPhPdpanQMrUH-173AsuUUq_yOKogjwkJ6VdMBQq3bGOkYZL1_iGbPpboXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=LhNuwNDzuQ6mdle6eQXZeNEs0xTxKG7u57GLspYCwmh_t9e9lQuocpt9lf9plgZqz--zvY6OuaL9PEo7cBgioE9O8gY1Y7S40BZjps0eymuNF4420vwhZ5219x7HDCSKByvm75dlxoAd1Stga492nS47Ro2RUt8Nt23UdDa7rpAyFTJXaShVApUyaeZSZCu_gUxdl2HIAG4IXbUq18fzC-a_5pl-rJ0wjcYP9aRTIpMYbKpJ5Cq_-5ehjQoUMtpCFLd1SPQhjPLKvoM5daKCGgsYA2MjPhPdpanQMrUH-173AsuUUq_yOKogjwkJ6VdMBQq3bGOkYZL1_iGbPpboXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ۳:۱۰
دوباره پدافند شمال شرق تهران فعال شد. شدیدتر از دفعه قبل
شرق تهران صدا پدافند
+ ده‌ها پیام مشابه از شهروندانی که همین صداها رو در محله‌های مختلف شرق و شمال شرق تهران شنیده‌اند.
🔄
ساعت ۳:۲۶:
ده‌ها پیام رگباری دیگر درباره صدای فعالیت پدافند
من حتی نمی‌رسم بازشون کنم فقط از پیش‌نمایش دارم آخرین پیام هر کسی رو می‌بینم باز هم کلی عقبم.
پیام‌ها رسیده به مرکز شهر و حتی مناطقی در غرب تهران
گرچه همیشه هستند کسانی که هر صدایی رو به برخورد تعبیر کنند ولی از حجم پیام‌ها واضحه که صدای پدافند شنیده میشه در مناطق مختلف تهران
آپدیت ساعت ۳:۴۰:
تا الان به طور پیوسته در هر ثانیه کلی پیام میومد. الان داره به حدود یک پیام در ثانیه کاهش پیدا می‌کنه.
همچنان درباره صدای پدافند در همه مناطق تهران
آپدیت ۳:۵۰:
سکوت نسبی برقرار شد. میزان نوتیفیکیشن‌ها هم به حالت معمول برگشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77384" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا [۲:۳۰ به وقت تهران]، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند. این حملات با هدف ادامه تضعیف توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77383" target="_blank">📅 03:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فعالیت پدافند در شرق شهر و استان تهران:
پردیس صدای انفجار و پدافند
همین الان شرق تهران
پدافندداره روی شهرک خمینی اتوبان بابایی کار میکنه، فعلا انفجار بزرگی نشنیدم، ممکنه هدف خجیر یا پارچین باشه
صدا پدافند زیاد میاد
ما سمت پردیس هستیم
سلام پردیس صدای انفجار از راه دور اومد
ساعت ۲:۵۰
سلام وحید جان از پردیس چندین انفجار شنیدیم الان
وحید صدای انفجار و پدافند شرق تهران همین الان
سلام تهران حکیمیه ۲:۵۳ دقیقه صدای پدافند میاد
سلام وحید جان همین الان  ساعت ۲:۵۰پدافند پارچین فعاله از پردیس مشخصه
صدای هواپیما میاد
همین دو سه دقه پیش
بشدت پدافندا فعالیت داشتن
پنج شیشتا صدای انفجار اومد
چندبار صدای پدافند سمت شرق ته
ران ۰۲:۵۰
پردیس صدای پدافند و انفجار اومد
شهرستان پردیس فاز ۱۱ از استان تهران صدای مکرر پدافند.  ساعت ۲:۵۵ صبح
شرق تهران(لواسان) صدای پافند ۲:۵۲
پردیس شرق تهران، چهار پنج تا صدا شبیه انفجار واضح ، ولی با فاصله شنیدیم ، حدود ساعت ۲:۵۳ صبح
سلام وحید جان  ساعت ۲.۵۰ دقیقه صدای حداقل ۱۰ انفجار از خجیر  که از حکیمیه شنیدیم
درود وحید جان ساعت ۲:۲۰ دقیقه ما پردیسیم
یه صدایی اومد گفتن سایت هسته ای پارچین زدن
پدافند شرق تهران فعاله
ما پردیسیم
اطراف (احتمالا پارچین)صدای انفجار و پدافند
[+ ده‌ها پیام مشابه دیگر از مناطق مختلف شرق و شمال شرق تهران که دیگه نقل نمی‌کنم و ازشون عبور می‌کنم چون تازه رسیدم به پیام‌های ۱۰ دقیقه پیش و از پیام‌های تازه‌تر بی‌خبرم.
هم‌زمان دارم همه پست‌های قبلی مربوط به شهرهای دیگر رو هم آپدیت می‌کنم با پیام‌های تازه‌تر]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77382" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
همین الان بوشهر صدای انفجار
بوشهر یکی سنگین
۰۲:۴۸ بوشهر صدای انفجار اومد
سلام خسته نباشید بندر گناوم چند بار موج انفجار اومد ولی نمیدونیم کجاست
بوشهر صدا و انفجار خیلی مهیب اومد
بوشهر صدا اومد ۲:۴۸ ریشهر
بوشهر صدای دو انفجار ساعت 2:48
بوشهر  انفجار فوق فوق سنگین ۲:۴۸
وحید الان ۲:۴۷ بوشهر زد زمین لرزید
وحید جان همین الان بوشهر عاشوری صدای وحشتناک بمب اومد تمام خونه لرزید
همین الان بوشهر دو انفجار بزرگ
بوشهر الآن صدای انفجار اومد، ساعت ۲:۴۷
ساعت ۲:۴۸ بوشهر صدای انفجار اومد!
انفجار وحشتناک بوشهر ۰۲:۴۸
خود شهر بوشهر صدای انفجار
۲:۴۷ بوشهر، یه انفجار خیلی وحشتناک و مهیب
سلام وحید جان همین الان بوشهر صدای انفجار ناحیه پایگاه هوایی و دریایی
سلام بوشهر ساعت دو و چهل و هشت دقیقه تک انفجار
بوشهر 2:48 یک انفجار مهیب محدوده بهمنی
ساعت ۲:۴۸ دقیقه بوشهر رو زدن صداش خیلی بلند بود
سلام آقا وحید، بوشهر ۲:۴۹ یه صدایی اومد و در های خونه کمی لرزید
بوشهرو الان ۲:۴۸‌‌بد زدن پایگاه هوایی
سلام بوشهر ساعت ۲:۴۸ دقیقه انفجار شدید
من یه سر شهرم.. دوستم یه سر دیگه شهر
جفت خونه هامون لرزید
بوشهر - چهارمین انفجار «مهیب» در ۲:۵۳
برازجان (استان بوشهر) تک صدای بلند و لرزش زمین. 2:54
وحید صدای انفجار شبیه شلیک موشک برازجان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77381" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=XF7PybN_YYawh5v1R5YL8yU4FqgnbyyfpRGctdTXjQYZ0xmOP7plEqQmi3ciBhqh0idytLKMRt0Gue7nLRHRRetIjhOEmT9Y1FWMNEDSoALsVO8R17Kt9mpzCWJYiDIvz4rtNGzQ1gpTQ_gAMuZyKii-uQap8k8GT7WGNGhPKzSON1yCQ7ykqdiOzN-jw6C-azJfSkgzbzXD0E9NgafF2U3mOAAsAsk8wEK0q-q_Bf7xj7KhoHy3RNIpy_2so5jbsqsV9eS8Ixpg7yX8ajo65R6YuPs72CQHCQCsemZXhvFhKCdxJVS20WyjsZCmp1OAET-jcD_VsqNQaWi_memhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=XF7PybN_YYawh5v1R5YL8yU4FqgnbyyfpRGctdTXjQYZ0xmOP7plEqQmi3ciBhqh0idytLKMRt0Gue7nLRHRRetIjhOEmT9Y1FWMNEDSoALsVO8R17Kt9mpzCWJYiDIvz4rtNGzQ1gpTQ_gAMuZyKii-uQap8k8GT7WGNGhPKzSON1yCQ7ykqdiOzN-jw6C-azJfSkgzbzXD0E9NgafF2U3mOAAsAsk8wEK0q-q_Bf7xj7KhoHy3RNIpy_2so5jbsqsV9eS8Ixpg7yX8ajo65R6YuPs72CQHCQCsemZXhvFhKCdxJVS20WyjsZCmp1OAET-jcD_VsqNQaWi_memhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
تبریز ۶/۷ تا همین الان  زدن شدید
همین الان شیش تا صدای انفجار تبریز اومد
پشت سر هم
۲:۴۲ از تبریز ۴تا صدای بلند انفجار یا پرتاب موشک اومد
سلام همین الان ۸ تا انفجار تبریز
سلام 5 انفجار شدید تبریز
سلام ساعت ۲:۴۲ بمب باران تبریز بیشتر از ۱۰ تا
۷ انفجار تبریز ۲:۴۰
از تبریز فک کنم موشک زدن
صدای انفجار از تبریز ۲:۴۲
وحید جان انفجارهای خیلی شدید اطراف تبریز ۲:۴۲ دقیقه
همین الان تبریز ۶ ۷ انفجار شدید
ساعت ۰۲:۴۲
ساعت ۲.۴۰ دقیقه تبریز رو زدن،حداقل چهار پنج تا صدای انفجار اومد
تبریز صدای ۵ انفجار توسط جنگنده بود
سلام تبریز ۴.۵ تا زدن
سلام همین الان صدای ۶انفجار سهند تبریز
ساعت ۲.۴۲
۷ تا انفجار شدید تبریز
همین الان2:43 دقیقه
پنج تا بیشتر زد تبریز رو و مشخصه سنگین بود و عجیب به مرکز شهر نزدیک
صدای انفجار از تبریز
۳ یا ۴ تا با فاصله خیلی کم
سلام وحید جان تبریز 2.43 شش هفت تا انجار وحشتناک بلند خونه لرزید و از خواب بلندم کرد
وحید تبریز ۸ تا صدای انفجار اومده
شدید و مهیب
تبریز موشک نبود. رادار رو زدن
سلام همین الان ۲:۴۲ بامداد ۶ بار سنگین زدن تبریز رو احتمالا سایت موشکی باشه
🔄
وحید دوباره تبریزو زدن
تبریز دوباره دو تا شنیدم اما دور بود صداش ضعیف میومد
دوتا انفجار دیگه تبریز ولی دورتر بود
تبریز دو تا صدا اومد
ادامه انفجارها در
#تبریز
سلام. الان تبریز پدافند کار کرد.
بازم تبریز رو زد، ۵ انفجار، شدتش کمتر از قبل بود ولی؛ ساعت ۰۳:۰۴
۵ انفجار یا بیشتر تبریز ۳:۰۴، یا شاید فعالیت پدافند ،(غرب تبریز)
تبریز بازم داره می‌زنه ساعت ۳:۰۴
۵ تا انفجار پشت سر هم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77380" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
چند تا صدای انفجار چابهار شنیده شد بنظر کنارک بود
چابهار صدا اومد.
سلام وحید جان چابهار صدا جنگنده و بمب اومد چند تا هم اومد از 2/5 شروع کرده
صدای انفجار در چابهار
چابهار همین الان چهارتا زد ساعت ۲:۳۸
چندددیقه قبلشم یکی زد
چابهار وحشتناک. داره میزنه
۷ انفجار رگباری پشت سر هم
ساعت 2:30 چهارشنبه چابهار یه صدای انفجار سنگین شنیده شد
الان دو سری 4، 5 تایی پشت هم زد
چابهار همین الآن صدای چند انفجار پشت سر هم
خود چابهار نبود
صداها دور بود
ولی تعدادش زیاد بود</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77379" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بندرعباس الان سه تا پشت هم زیادد زدن
بندرعباس پشت سر هم داره میزنه
بندرعباس سلام صدای چندتا انفجار ساعت ۲:۲۷.
سلام وحید جان بندرعباس صدای 3 انفجار
سلام وحید جان همین الان  بندرعباس صدایی وحشتناک از سمت اسکله باهنر اومد ۲تا صدای وحشتناک
وحید جان دوتا انفجار پشت سرهم بندرعباس 2:38 دقیقه، دور بود
بندرعباس ۲:۳۸ چند صدای انفجار شنیدم
سلام صدای انفجار بندرعباس سه تا پشت سرهم همین الان
بندرعباس ۲:۳۷
سه انفجار
بندرعباس ۳ تا انفجار پشت هم الان
سلام آقا وحید ساعت ۲:۳۷ دقیقه بندرعباس صدای ۳ تا انفجار اومد که اولی از همه بلندتر بود
سلام بندرعباس الان صدای ۳تا انفجار شدید ۲:۳۷
سلام بندرعباس 2:37 حدودا ۴ تا صدای انفجار اومد
بندر عباس صدای ۳ انفجار ۲:۳۹
بندرعباس صدای انفجار اومد الان
میگن سمت اسکله باهنر زدن</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77378" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام صدای انفجار یا پرتاب موشک از کنگاور
سلام ۲ و ۳۵ صدای انفجار و لرزش کنگاور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77377" target="_blank">📅 02:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ماهشهر دو صدای انفجار از دور
همین الان یک انفجار دیگه
سه چهارتا انفجار ماهشهر همین الاننن
ماهشهر ۴تا موج از دور ولی حس شد
بندر ماهشهر ۴ انفجار
سه چهارتا انفجار ماهشهر همین الاننن
سلام ماهشهر الان ۳ انفجار
وحید خسته نباشی بندرماهشهر الان چند انفجار اومد
سلام صداها مثل ویبره هستن انگاردورازماهشهره به فاصله 2ذقیفه
ماهشهر صدای انفجار ساعت ۲:۳۱
🔄
اقا وحید ماهشهر دوتا دیگه زد همین الان 2.48 دقه
باز ماهشهر دوتا زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77376" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
سلام خسته نباشید همین الان بهبهان رو زدن
چهار بار زدن
خیلی بد زدن
خونه ها خیلی لرزیدن
وحید
بهبهان رو زدن
۴ انفجار محکم
بهبهانو چنان داره میزنه که هبچ وقت اینجوری نزده بودددد
انفجارها انقدر قوین که تا حالا همچین چیزی ندیده بودمممم
بهبهان ۳ یا ۴ تا صدا انفجار خیلی شدید
پشت سر هم
۲:۳۲ دقیقه
خیلی شدیده
🔄
سلام بهبهان همین الان ۲ و ۳۰ بامداد ۴ انفجار بسیار سنگین
شد چهار بار دوباره اومد
بازم زد
بهبهان 4 موج انفجار 2:30
4موج انفجار نزدیک تر 2:34
۷ بار زدن بهبهان رو
سلام منصوریه بهبهان هستیم
همینجور صدای انفجار میاد پشت هم
سلام توی همین ۴ دقیقه ۸ انفجار داشتیم
همینطوری داره صدا میاد
درود وحید جان ۷ تا انفجار پیاپی و سنگین بهبهان احتمالا سمت پادگان بخردیان
دود از سمت پالایشگاه بیدبلند میاد نمیدونم کجا رو زدن
حاجی ۱۰بار زدن در خدی که زمین لرزید
بهبهان وحشتناک دارن میزنن
سلام ، تا اینجا حدود ۹ صدای انفجار اومده بهبهان
از ۲:۳۲ تا ۲:۳۵
بهبهان ۲:۳۵
صدای ۶ انفجار
همین الان بههبهان زدن صداش خیلی بلند از استرس تو کوچه ایم
سلام سپاه روبروی بیدبلند بهبهان رو حدود هفت بار زد
سلام صدای های مهیب موشک در آسمان بهبهان
شایدم انفجار
بهبهان درب خونه ها از موج انفجار چند بار لرزی از خواب بیدار شدیم وحشتناک
🔄
پیام‌های حدود ساعت ۲:۵۰
بهبهان بازم صدا انفجار
قطع نمیشه
خیلی شدیده
حاجی هنوز صدای انفجار میاد
بهبهان بازم صدای انفجار میاد
۴ تا پشت هم
بهبهان دوباره داره صدا مياد، 4 بار
دوباره دارن میزنن
بهبهان دوباره زد
۴ تا انفجار
۴ بار دیگه الان بهبهان رو زدن آقا وحید
۳ انفجار بزرگ دیگه همین الان
داداش وحید سه موج بخردیان بهبهان رو زدن
۲:۳۰
۲:۳۵
۲:۵۰
همین الان بهبهان،جدای از اون ۸ تا الان ۳ تا دیگه شدیییید زد
ساعت ۲:۵۰
بهبهان دوباره دوتا انفجار شدید
ساعت ۰۲:۴۹..دوباره ۳ انفجار شدید دیگه بهبهان.
سلام رگباری دارن بهبهان رو میزنن
بهبهان تا الان 11 تا انفجار شده وحید
وحید جان از ساعت ۲:۳۲ تا ۲:۴۷ دقیقه صدای ۱۰ انفجار داخل بهبهان اومد
سلام وحید 2و50دیقه دوباره 2انفجار  بهبهان زدن انفجار خیلی مهیبه
باز هم همونجا رو حدود چهار بار دیگه زد بیست کیلومتری شهر هستش
بهبهان پونزده بار تا حالا زدن همین الان صدا ۵ انفجار دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77375" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">در بخشی از نارمک تهران صدایی شنیده شده که معلوم نیست مربوط به چی بوده.
پیام‌های دریافتی خیلی کم:
سلام شرق نارمک صدای خیلی بلند مثل انفجار
من سمت نارمکم الان یه صدایی شبیه به انفجار پهپاد شنیدم
شرق تهران نارمک شیشه ها لرزید و صدای انفجار
تهران الان صدا اومد فکر کنم زدن
ساعت 02:01
سمت نارمک ساعت ۲بامداد صدای انفجار اومد
سمت نارمک صدایی شبیه به انفجار  بود ساعت ۲:۰۰
ما هم شنیدیم ولی انفجار نبود یه صدایی مثل زمانی که پدافند می زدن
🔄
پیام‌های تازه:
انفجار گاز بوده
سلام انفجار گاز بوده میدان ۹۵
انفجار نشنیدم اما ده دقیقه پیش صدای آتش‌نشانی اومد تعداد زیاد
نزدیک نارمکیم، گلبرگ
نارمک میدان ۹۵ کوچه مهدی
ظاهرا ترکیدگی گازه
کسی صدمه ندیده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77374" target="_blank">📅 02:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSxProJ3XHAPoIN7Xouu5U8IRioLlwxEWn4FtD_KvkQmJhYhVNibJbJMBB7rQycSky7ebBpNaWinXM1GoNldKeLY5YPdarN3QZcwFBVaK10u49o8AjQOBKsxbQL3qmJ39apCCRObUPlEhPUdl-vWVFhpKwC34QVg5RWKrr4--qug-U8uC6x-X7ukjZOQEMnE_yojrnC29eUtomMfiQxeLgWkPcFrr630XGMxnG-Y9lzYLl5565eNlyeeoe3YLgM99cAfSisNbvdDF6t6L2N4u3l8alQX1B3Xt_7bF9BSeoPPFBL5OdAMrUhCUE_g-haGDtun5g2pYpYdOyHOCMpHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل ارتش کویت، بامداد چهارشنبه، با صدور بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال حاضر در حال مقابله با حملات پهپادهای متخاصم در پی «تجاوز گستاخانه ایران» است و تصریح کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری این اهداف توسط سامانه‌های دفاع جوی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77373" target="_blank">📅 01:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): تعرض به مراکز هسته‌ای ایران، پاسخ گسترده نیروهای مسلح را درپی دارد
🔹
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است. اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به‌عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77372" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgtALmKXgMy_-WpHpS0tIXxBHhLOpx6SKm7AD2La9Ch0lHgyvvnvRxS9eHs_x596mO7IKxQnpUVe7qyykFMAAkBPAJBwwz33fjUUwsoxc9oZcngi8I2exsHFESi0KLxw55_ScFhjIJmhqdNW1E6a8Fod_P5tugb4hx-YtxF18kGkiX2Gy07N9Xsi3Yriegaq6_3FqgjGaGSV5S76qEG-9ImGtEs8jHxisPC2PFrTpziqbiwf2xlmebyK0ZrdTtr34ZhyJnXys6NSLPperyliNMrB5Ci4wGyIq3OfRxv9eY3J0OhdeBf0li99dqcPUpvA-_9BbeXEDTq9Zh5a3pItMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع ایالات متحده می‌گوید جنگ با ایران تاکنون ۳۷ میلیارد و پانصد میلیون دلار هزینه داشته است.
پیت هگست این موضوع را خطاب به اعضای کنگره اعلام کرد؛ آماری که از افزایش نزدیک به ۸ میلیارد دلاری هزینۀ جنگ، نسبت به ارقام قبلی که دو ماه پیش اعلام شده بود، حکایت دارد.
وزیر دفاع آمریکا البته تأکید کرد که این رقم تازه، هزینه‌های پیش‌بینی‌شده تا پایان سال مالی جاری، یعنی ۳۰ سپتامبر مطابق با ۸ مهرماه ۱۴۰۵ را هم شامل می‌شود.
از زمان آغاز مجدد درگیری‌ها بین ایران و آمریکا، این نخستین بار است که پیت هگست وزیر دفاع ایالات متحده به همراه ژنرال دن کِین رئیس ستاد مشترک نیروهای مسلح این کشور، با حضور در کمیتۀ تخصصی کنگره، ویژۀ تخصیص بودجه، به سوالات اعضا پاسخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77371" target="_blank">📅 00:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jI9L1a0_Cjygyl2s1nKyucPYtFm7g4UOBE0wnYnrumxFnE0KmPDOc2Sh6RVNBt_baSp2Qygx4J3MGPTvDf2W3rKf8TM4umfrhn5HiJZD7VR0gKzKh08LWIpYv6u7UK8fM4_FhUcMJrOZCgMjG_YgCVTvar9OO1EcCW8Zh03mxxhEGbtWLxu5u_mLhiU6NxyeMEVh5ZzJd_JlEL4Uw2qaHfel3tjp-7C_ES9JPMbQXDEaeIaTzlIeyrJ2K1WeO0FGHjv_OxHxq7WqGoMyw9yFyDoCjtTUsLlremKFE3nhLda21eWaXYBnQJnFTa9U1vrJqt0_pb6TClHMU14oSd8FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
جنگ افغانستان: 20 سال، 2,000 کشته.
جنگ عراق: 9 سال، 4,600 کشته.
جنگ ویتنام: 19 سال و 5 ماه، 58,220 کشته.
جنگ کره: 3 سال و 1 ماه، 36,574 کشته.
جنگ ونزوئلا: 1 روز، بدون کشته.
درگیری نظامی با ایران: 4 ماه، 18 کشته.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77370" target="_blank">📅 23:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hWnnywMG3QFQqAxVbQu1kL-YmMG3FubSTwj4dJY6gnP9PW5rILNDB_Mh-HfFqMyb-O_u--SW5RLFDALLWlrvSUz_kO-gZnPoIRn0g63uCjY-7bLSSvwUGMtSb1HmpGIgoaaGKRiNjNtOMv9GFuMQFDv9Cs_BnkLi4xiFI0yyXI5m2ObjaBBnLPRvc0FmdqZfRL3ONtDcFa4q4DLNTm8eGHANbK3PYi8nyU8PT70bsq2MbKfuIJNYXZ8Ft8BCXt0rH_WN9iMX7a1LawHrTPaNNdSD1Pg3kxQmb_DrDWDyg4TDtDAzbAx7uD9WHfswWpA2cKyoin63wox9SwY5vAjTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hWnnywMG3QFQqAxVbQu1kL-YmMG3FubSTwj4dJY6gnP9PW5rILNDB_Mh-HfFqMyb-O_u--SW5RLFDALLWlrvSUz_kO-gZnPoIRn0g63uCjY-7bLSSvwUGMtSb1HmpGIgoaaGKRiNjNtOMv9GFuMQFDv9Cs_BnkLi4xiFI0yyXI5m2ObjaBBnLPRvc0FmdqZfRL3ONtDcFa4q4DLNTm8eGHANbK3PYi8nyU8PT70bsq2MbKfuIJNYXZ8Ft8BCXt0rH_WN9iMX7a1LawHrTPaNNdSD1Pg3kxQmb_DrDWDyg4TDtDAzbAx7uD9WHfswWpA2cKyoin63wox9SwY5vAjTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: معترضان چندین بار جلسه ادای شهادت پیت هگست، وزیر جنگ، در برابر مجلس سنا را مختل کردند و پلاکاردهایی با نوشته «نه به جنگ با ایران» در دست گرفتند.
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77369" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL50g0D7KpvTdgvKFKRoZJCVkoEdl8v-_QoBViqCVdV--GRfXZRasPla_Ec3UJs1ppjztJJ487EVPPk1Cehelvb5IgHwmrraPDxLV2ZDbvKlWKQR3tcZe5YrQ_K_KCuU7uzx_v-940TxMR_Z1JonUDLc5Dy9YYcykI8bZdYqoRRUMKvzVolZIct-6qRQL0P1La6icMsoj-tHc6XIhxpfLgV2x1l49G-ucVD7iBfgTIQsej6-N2MN5koCjpPvQixWZvw4knyHX6uTA6nOkh-uIvSKqERZ_4iCATMH69EHyx3fBZep7SEWgv_jVu0KWEJTG3cxCX8Bhx_1z5xqr2Inqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز سه‌شنبه ۳۰ تیرماه گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده ایالات متحده از پایگاه‌های نظامی بریتانیا برای آنچه لندن «حملات دفاعی» علیه ایران می‌نامد موافقت کرده و بدین ترتیب سیاست سلف خود، کی‌یر استارمر، را ادامه داده است.
این خبرگزاری به نقل از منابع آگاه نوشته که استارمر روز ۲۶ تیرماه نشستی با وزرا و مقام‌های ارشد برگزار کرد تا سیاست بریتانیا پس از ازسرگیری عملیات آمریکا در اوایل این ماه بررسی شود.
این منابع افزودند که در آن نشست، وزرا تصمیم گرفتند سیاست موجود ادامه یابد.
بر اساس این سیاست، پایگاه دیه‌گو گارسیا در اقیانوس هند و پایگاه هوایی «آراف فیرفورد» در گلاسترشر انگلستان می‌توانند در اختیار هواپیماهای آمریکایی قرار گیرند که مأموریت‌هایی برای مقابله با تهدید موشکی ایران و نیز اهداف مرتبط با تنگه هرمز انجام می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77368" target="_blank">📅 22:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzxZF9e-nk_cTG9345khozmGm02Zi8-2Lw_NnFbIMejHrYhZly9qEitV2Fc576H5HW5stLSpUMPz-yA3FcQnAkup2DeM1hnRzJXSSCzA7qySGQPtFhgSAXPC3bqK6dad_7t-aaITg0VKbk3bLK_e70V5_73uxKybWFCzML0iJO7ddyUaMprwq6hSc53bkHjl1quXh2o_WCGGW7X7Cyw3d5aqXuui4vtNr8aTbhwQRBqa286BnE91uynNHbAbEyWtjh62sOzJ9tywO6TfyoUmrADuq9Yx3Ebu-lbNbd8O58SY65-9bvhNEhs_df5L0CnaSuwIrU5Xm9USd-wtz4m90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته دفاع پارلمان بلغارستان روز سه‌شنبه ۳۰ تیر با طرح دولت برای استقرار موقت هواپیماهای سوخت‌رسان و نیروهای نظامی آمریکا در پایگاه هوایی بزمِر موافقت کرد؛ اقدامی که با هشدار جمهوری اسلامی به صوفیه همراه شد.
بر اساس گزارش خبرگزاری رسمی بلغارستان، کمیته دفاع پارلمان از پیش‌نویس مصوبه شورای وزیران حمایت کرد که بر اساس آن، حداکثر هشت فروند هواپیمای سوخت‌رسان آمریکایی و ۲۵۰ نیروی نظامی این کشور می‌توانند به طور موقت در پایگاه هوایی بزمِر در جنوب شرقی بلغارستان مستقر شوند تا از عملیات آمریکا در خاورمیانه پشتیبانی کنند.
بر اساس این گزارش، آمریکا درخواست کرده است این استقرار از ۲۴ ژوییه تا اول اکتبر ادامه داشته باشد.
فرماندهی مرکزی آمریکا، سنتکام، در پاسخ به پرسش شبکه سی‌ان‌ان درباره این استقرار اعلام کرد: «به دلایل امنیت عملیاتی، درباره جابه‌جایی نیروها یا آرایش احتمالی نیروها در آینده اظهار نظر نمی‌کنیم.»
ساعاتی پیش، جمهوری اسلامی به دولت بلغارستان هشدار داد از خاک یا تاسیسات خود برای حمایت از عملیات نظامی آمریکا علیه ایران استفاده نکند.
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، گفت هرگونه مشارکت در برنامه‌ریزی یا اجرای چنین عملیاتی به منزله همدستی در «جنایت تجاوز و جنایت‌های جنگی» خواهد بود. او همچنین از پارلمان بلغارستان خواست با این طرح مخالفت کند.
بلغارستان که از اعضای ناتو است، بر اساس توافق‌نامه همکاری دفاعی دوجانبه با آمریکا که در سال ۲۰۰۶ امضا شد، پایگاه هوایی بزمِر را به عنوان یک تاسیسات مشترک در اختیار نیروهای مسلح دو کشور قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77367" target="_blank">📅 21:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXraqJ_xV0eYFBIi3a5Xvt1w6OiqFFYcblzHSEgURCRdf5ENN1vaxEyIdLwh2tJfwRF6RFwhPY8Z7CajW0Wq51qTY20miGy6TOVqWPFCo74DZTiH7wKuaIACBnLkeF5s5Ih8nknDS9-Apzw-ZBrShZafRC5gV9nminlY1xdqFrsHzTGfHlLsnxy3vBrZMCUs9jiE0jas7bBEvSlv-aN1DgkS-J5CdKj3C-vE2sjwuKIAs-aQ2WpeWqiDQSdJ1bWCpdIu3yw68YLz4-k7hHCKUDDNfiYma17gmRSsaGuj-mvLOzt3ETnzs8RBEL_njgV7ihzEmRN8L9fJYOC5NHmVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KRVNZ7UtPL6Ee91o7iIPlQ5SgQfORnJ9YprEoUKilg8jGSw7fBN6nmanBvNMD_iDXUpTYp9S9MrlQtyZVNejD2Fqm6gl4tjQvUYvSQwr372njhA26hgdyLFxVq1D7O4OieRT1Y2oca5UoL1yMerGon7cQzafRzvV9ff4qKjypJ0BtFKeicv6g31voHGBmCiyTBOJ3i2q-UDuK1AMh5BW8NesJJtKySFtr7jhhC1sj8i1IHOD1B94ti_Zp8ThYNxdsaCXbrwUvnlrS7o1-Zsn2ULitFUgTN5-GhgBh7kgd5yVfwb2It6CJGCiRnqkF8RW5yUaS1iec4zBO693Ek9IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sg528jWgcg7Y56fgKqgSPw7qM78ADtr4KYlObzLFIGJX4TNGlRttHDOONO-JxdFDgNDgkWn2QRzfwjEGhWYMBww-JDl92oscFiF3GH5YpA8DAjysUZtv0Z2PTvXEUhkZhIhNxh6pHuRLKpZMXgtcOArszQvaBDpuTTKj0hoprc1gCmQ8dsS4TKZzc45htc1puK3EA92go36mcLptEftTzfk0x7Z35fCuOnL9sGkuUBAw-u3vaxnz7FxHGgRqaAeIERLfz16Cyp-sWlBgIb6Ru30akVGFWQFB7dWeLQDIQx1gRRZcpHKLR-2UbRJYeFmUco6myqM9q6TPvFNV_Hae6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRy3A3yeXBEXUGPbHsW3ej8NlHEnKIYiVuJUJSQnJ55uwpoTb-Qg4yJvFNO0D_jJ3QWNA2iMVEvHy7FL5jYbcvmmMhv2iMxjwoVHo55hnkNT9dnSMSoh1sMGCrL3zya7UpXQ2gOW4oLOJQjQds0D48AOmLGttDEnUfviVv9GbzSOVYb9vC3fJRxI9HTTv0L-kbk4kAU5dKHdus-TJhG95amRUVVnsZxvkBADdqS1Jd1gf6AHMdsNopJCBmZyyfSH-gstKVQ9-vtLOnTiyBNR2-mA9pLayv1wRtw7PzQIs5wKkp9oYjj3ceKIgZHiix3FTrJ7YPIGsYSUGOtjP2ZD0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4477673f76.mp4?token=kT1t-WTTGqRDhJjThuoEpUO1gejsxrIU01Ve7ytt_-5Oy_4KymjjR8XVJaZwYwyAVAfjJ4IP9Jvl13vIDUcT4_SiIeUdOOE8bbSMrMY4r_hc9bNb4IPhBxmq3QN9N7xHzU06hsVuw76I3i2YR4bi2VaKXyWo2Fu7_Tl_EhAq2NajthFjaUkeQX2b4pT7sHpqHxXIouiIFqi-DOWYutF7OdO4j38e5S8jwTLSCCGefrvd8yb2plXOlX9toysOEHq-Ur8kRNRmIn7haJlGtotO-6Lhkv-6eoTQNG808_i0rMJAEznGDT947RW4miudAlIWKZ-1HP3mAaUi5tSQwYmwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4477673f76.mp4?token=kT1t-WTTGqRDhJjThuoEpUO1gejsxrIU01Ve7ytt_-5Oy_4KymjjR8XVJaZwYwyAVAfjJ4IP9Jvl13vIDUcT4_SiIeUdOOE8bbSMrMY4r_hc9bNb4IPhBxmq3QN9N7xHzU06hsVuw76I3i2YR4bi2VaKXyWo2Fu7_Tl_EhAq2NajthFjaUkeQX2b4pT7sHpqHxXIouiIFqi-DOWYutF7OdO4j38e5S8jwTLSCCGefrvd8yb2plXOlX9toysOEHq-Ur8kRNRmIn7haJlGtotO-6Lhkv-6eoTQNG808_i0rMJAEznGDT947RW4miudAlIWKZ-1HP3mAaUi5tSQwYmwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی  در شیراز
دو تصویر اول منتشر شده در سایر منابع
سایر تصاویر دریافتی از شهروندان،
سه‌شنبه ۳۰ تیر
گویا تصاویر بالا دو نقطه مختلف شیراز رو نشون میدن: کوه دراک و کوه نزدیک دروازه قرآن
آپدیت:
به گزارش رسانه‌های ایران عصر امروز سه‌شنبه(۳۰ تیرماه) آتش‌سوزی گسترده در ارتفاعات دراک شیراز رخ داده است که همچنان ادامه دارد.
خبرگزاری ایرنا گزارش داده است که شعله‌های آتش، مراتع ارتفاعات دراک در شمال‌غرب شیراز و کوه‌های نزدیک به دروازه‌ قرآن را در بر گرفته است و «زبانه‌های این آتش‌ از نقاط مختلف شهر به وضوح قابل مشاهده است.»
رئیس سازمان آتش‌نشانی شیراز گفته است: «۵۰ آتش‌نشان به همراه دو تیم تخصصی کوهستان در حال تلاش برای مهار حریق هستند.»
هادی عیدی‌پور به خبرگزاری مهر گفته است: «به دلیل صعب‌العبور بودن منطقه کوهستانی، وزش باد و وجود پوشش گیاهی خشک که موجب گسترش و شعله‌ور شدن آتش می‌شود، عملیات مهار حریق با دشواری همراه است.»
دلیل این آتش‌سوزی هنور اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77361" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQBKrphWxjTUX7jF_vQa8Dj25w04XJNxHZSv-1NFFNpQS98mgQJaFFz_nb1O_3Gb0Ri6NBuRqV8NvXuoEdb3pPWT_8Enl8L1vwlW0NkFQ_jzquQcUBzrx8plSIRtDDupbLZkRPpLARjxHJkos3o1LZ1lErliC5xDurzrPY-eksGO8d3WNJHCqtXEhmaGDMpTlzFRaIpCjNbiCVQWpmww6-4RdvsJ3pfrxyz7LMOYmrw0rixS08SbrAR4Z_klVMR7oK8tnMaiBUa8NWw_3_26N_GW_BBq4FM-XtQIWlnMj2yviWLsicK9WBE9EOWTUm7kIf39yPyqwGc-ds579v1XoVQE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQBKrphWxjTUX7jF_vQa8Dj25w04XJNxHZSv-1NFFNpQS98mgQJaFFz_nb1O_3Gb0Ri6NBuRqV8NvXuoEdb3pPWT_8Enl8L1vwlW0NkFQ_jzquQcUBzrx8plSIRtDDupbLZkRPpLARjxHJkos3o1LZ1lErliC5xDurzrPY-eksGO8d3WNJHCqtXEhmaGDMpTlzFRaIpCjNbiCVQWpmww6-4RdvsJ3pfrxyz7LMOYmrw0rixS08SbrAR4Z_klVMR7oK8tnMaiBUa8NWw_3_26N_GW_BBq4FM-XtQIWlnMj2yviWLsicK9WBE9EOWTUm7kIf39yPyqwGc-ds579v1XoVQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد
06:33
دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۰ تیر در دیدار با جوزف عون، رییس‌جمهوری لبنان، گفت جمهوری اسلامی با «درماندگی» به دنبال مذاکره برای پایان دادن به جنگ است و هشدار داد آمریکا به‌زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد.
@
VahidHeadline
رئیس جمهور آمریکا در پاسخ به این سوال که آیا ممکن است ایران سانتریفوژهای خود را به داخل تاسیسات کوه کلنگ منتقل کرده باشد، گفت:
«ممکن است کرده باشند ... ما اطلاعات مستندی نداریم ما فقط در اخبار جعلی این چیزها را می شنویم. اما سانتریفوژ بدون مواد هسته‌ای اهمیتی ندارد. ما مواد هسته‌ای را دنبال می‌کنیم که اصل قضیه است. آنجا را می‌زنیم، احتمالا خیلی زود. معمولا این چیزها را اعلام نمی‌کنم. اگر فکر می‌کردم می‌توانند جلویمان را بگیرند نمی‌گفتم.»
@
VahidHeadline
ویدیوی بالا: قطعات مربوط به ایران به تشخیص ماشین
متن زیرنویس ویدیوی بالا (ترجمه ماشین
)
تیترهای پیشنهادی چت جی‌پی‌تی درباره متن زیرنویس ویدیوی بالا:
▪️
ترامپ: ایران عاجزانه خواهان مذاکره است؛ هر تأسیسات هسته‌ای تازه را به‌شدت هدف قرار می‌دهیم
▪️
ترامپ: اگر امروز هم خارج شویم، بازسازی توان ایران ۲۰ تا ۲۵ سال طول می‌کشد
▪️
ترامپ: ایران هنوز چیزی ندیده؛ به هر محل فعالیت هسته‌ای حمله خواهیم کرد
▪️
ترامپ: محاصره ایران مانند دیوار فولادی است؛ هیچ‌کس عبور نمی‌کند
▪️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ برای حملات سنگین‌تر آماده‌ایم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77360" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=S3W1ZdvnKEg9CpKIRz-1RQfVquqf6zbO20kVhqqBgbvRr5tLQDj7B71mzh4DdTA6gq0WDZk-WjyBhHe4dWBmLzHcYjiD-EsZ69cL9SSjgFxXWBjNJahZpbY6qrvPPFyXER_I0hG4F_xcIfuszZLWgkwy58wzz1b9VlVCG-61I_aFPXKQRb-H2_78tvczz_Q6RLYucn_gZdNbeCLyjIspee-L6XPSier3cBptb2kh4-ULtNlZ7bye05LPpBg-yGAtKjerQ6YbbK2vNzgG5Fk578eihWc6Euq3HiKNL35RelHNrdJFxBtyrgW_0NgcNYxBe5ES8SKeCJ-jFEfZ5fo9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=S3W1ZdvnKEg9CpKIRz-1RQfVquqf6zbO20kVhqqBgbvRr5tLQDj7B71mzh4DdTA6gq0WDZk-WjyBhHe4dWBmLzHcYjiD-EsZ69cL9SSjgFxXWBjNJahZpbY6qrvPPFyXER_I0hG4F_xcIfuszZLWgkwy58wzz1b9VlVCG-61I_aFPXKQRb-H2_78tvczz_Q6RLYucn_gZdNbeCLyjIspee-L6XPSier3cBptb2kh4-ULtNlZ7bye05LPpBg-yGAtKjerQ6YbbK2vNzgG5Fk578eihWc6Euq3HiKNL35RelHNrdJFxBtyrgW_0NgcNYxBe5ES8SKeCJ-jFEfZ5fo9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، روز سه‌شنبه ۳۰ تیرماه در یک مراسم عمومی با بیان این‌که «سطح دسترسی» به مجتبی خامنه‌ای افزایش یافته، گفت تمام اقدامات مربوط به مذاکره «بر اساس رهنمودهای» رهبر جمهوری اسلامی انجام شده و از «اظهارنظرهای نادرست و بی‌توجه به ابعاد مختلف» در این باره انتقاد کرد.
مجتبی خامنه‌ای حدود ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر جمهوری اسلامی معرفی شد، اما از آن زمان نه تنها هیچ فایل تصویری که هیچ فایل صوتی هم از او منتشر نشده است.
عباس عراقچی، وزیر خارجه ایران، به‌تازگی اعلام کرده که «هیچ‌وقت» مجتبی خامنه‌ای را از نزدیک ندیده و در دورهٔ رهبری او نیز جز معدودی او را ندیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77359" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggIHTCGLVjdrQalYISA94Y9_5pLn5K1E_pX6j0-28JPlaC7MNbW_JdeWYrGjgLUEwkOJ8Gn0eFqsiUhsS2GY-VfUkEEyExIJeJwcwTHykkfc1FhTMPcz5ntTL4P05S7A7OPqZlD1OMSwhG_6--xeis8ea2Sh4YvIxl4gVbaGJfg37UfnKp93XVs7XHc6FkmtxRJtBYwz77L8Cp5PDA7EMBWWHZLqANCHBl45bATS9MPqhIKRyvfsydBryVHYKBkV7JI7zfSQGna7HSDtEivtXzEej3Bj2Yb4My5iW-u9Tu6ZqvNlYUuuhIUxn8eS31Up6GnzIOmi7inN2yiE0KTt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، «شیده توکلی»، شهروند بهایی ساکن تهران، را به ۱۱ سال حبس تعزیری، جریمه نقدی، محرومیت دائم از اشتغال در خدمات عمومی و دولتی و مصادره بخشی از اموالش محکوم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77358" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=F_u1CvMbrJKBZsG2MEBkKH7EcKd5zZfEFadLGXYbnbaQaPPr8XzmEdLrIOzz8c5V1EKTE5D4pUBjnD5hCJuQLPiwX-wxoJqnRKfHpmPTY37Blchx40rM_BmpW00foWDD3e6dY668kuHRkWFc1LmrqoGA6Cr0hn72c5_j4xRJrf3Oiw5JjOKwflYuTpO34RPf97M5VJvCTqx_CmQfniX8dUSYGWQvE_vLfQqSumlY9v_IDNL7jj2oVp9nmaSGUCnMYnaMzwVVigjRVFIOJ9E41bljLVms4-SxL2tMddEIitC6v947IBbeqxVy-6PAjPa_ntTTtCv2QTQMEitxM95wUTg9PPsbd8Oo41xIDwxn1dOs2FV1DyQmYeQSCYHVVARTRpx9BvzsIEmtjEpHQQjWo8mDjU7c8mFepS1L4ehDDbFWDJrAj-_djQ4BX69fPPMmAHZIvjNLjRroilDsGbTREolI-cWgxLnLgoGDcvo0xfXFVKcPGfS72f3JUNx_ySpM5MYJuW_FTl57GfdTM8Ba3a1PjnzLmGTvAAEUiCBmNzrR2-gy9AicYLk1-_mwIdYtrsQDlriUE7UDKtiC5x8O6IrR5hC7hiQ-57OZwFftL2Bif5w10hhH50cQxQ1m8aitvl8XWbonooPiMkr4ml9UH_wmkxLOkBIudUZhFicidrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=F_u1CvMbrJKBZsG2MEBkKH7EcKd5zZfEFadLGXYbnbaQaPPr8XzmEdLrIOzz8c5V1EKTE5D4pUBjnD5hCJuQLPiwX-wxoJqnRKfHpmPTY37Blchx40rM_BmpW00foWDD3e6dY668kuHRkWFc1LmrqoGA6Cr0hn72c5_j4xRJrf3Oiw5JjOKwflYuTpO34RPf97M5VJvCTqx_CmQfniX8dUSYGWQvE_vLfQqSumlY9v_IDNL7jj2oVp9nmaSGUCnMYnaMzwVVigjRVFIOJ9E41bljLVms4-SxL2tMddEIitC6v947IBbeqxVy-6PAjPa_ntTTtCv2QTQMEitxM95wUTg9PPsbd8Oo41xIDwxn1dOs2FV1DyQmYeQSCYHVVARTRpx9BvzsIEmtjEpHQQjWo8mDjU7c8mFepS1L4ehDDbFWDJrAj-_djQ4BX69fPPMmAHZIvjNLjRroilDsGbTREolI-cWgxLnLgoGDcvo0xfXFVKcPGfS72f3JUNx_ySpM5MYJuW_FTl57GfdTM8Ba3a1PjnzLmGTvAAEUiCBmNzrR2-gy9AicYLk1-_mwIdYtrsQDlriUE7UDKtiC5x8O6IrR5hC7hiQ-57OZwFftL2Bif5w10hhH50cQxQ1m8aitvl8XWbonooPiMkr4ml9UH_wmkxLOkBIudUZhFicidrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند  از ابتدای سال ۲۰۲۶ تاکنون اعدام دست‌کم ۸۵۱ نفر در ایران مستند کرده است که ۳۲ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
بر اساس قوانین بین‌المللی، مجازات اعدام تنها به «شدیدترین جرایم» — که به معنای قتل عمد تفسیر می‌شود — محدود شده است؛ با این حال در ایران، جرایم غیر خشن مرتبط با مواد مخدر، بیشترین سهم را در آمارهای اعدام با این‌گونه اتهامات دارند.
🔸
طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مربوط به اتهامات منتسب به مواد مخدر بوده است.
🔸
سوءاستفاده حکومت ایران از مجازات اعدام به حدی وخیم شده که زندانیان واحد دو زندان قزل‌حصار ، بزرگ‌ترین زندان دولتی ایران برای دومین بار در سال جاری دست به اعتصاب غذا زده‌اند و حتی برخی از آن‌ها لب‌های خود را دوخته‌اند. با گذشت هشت روز از آغاز این اعتصاب، هیچ‌یک از مسئولان پاسخگوی وضعیت آنان نبوده و به خواسته‌های اعتصاب آنها توجه نکرده‌اند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77357" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UQz-eTlLyWZq4TCM2epV2rrAYfkjjjpuDOuZU72knMdMuUQ4DAG5_nQ8R0Qh_xQoGSlwPdAthiI8MjvkOveGo0SP9Z1pUNWz0zs_qnxI3JynLv4f2-6kG7S8YEDV6NmtAgegtXSMDNq4f5yR09gaPhTviUqztIYYKX255oYSXrLN2LNBH9ebgQ6BMNNeZsz6xrOEUdyAcZgRVrsOReHtsvGFsoS1R-Ve4Lq2ZC9fdAM3u7fFXPwkTYAZJIIw-gFjjI0L8g5Xu2PzWwxWyyszDhejtVMbxCWOhXZ3M2bUxhqRXxFTptJVT_V-uUd0FLUB1U6gz6aanYomkTWe7iFHhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XV_VDKP3Q5fGH8spftBKgz5NVskQK4NhI3-_m9jkHcyHXA0xnWHsdlrtKePHiQj2qNXFeu2y40jxdTOLsHjhkBeu7NLZ02615w5avGn_2mwfzaOK47jkmpC117gkqxtx--haBFCsNJTIGlBA9sNvKuTgJarH7pY4bZyZMCeXhd5hqKrVZ-yPPtob11fU30T6rHMwIQPJjPDaHYtCs3G5BQpZR_c9XCNvaiCRZpa5belp5NGlZm8_0g1zqC9YqbRD-gd4VCtfNmgrB0fKKEG_9Nu_Re_7u0zpHBU2rOsfvh9QDH1twVDt6qrij936oV5smJgTndFqD2lyiXZO__bCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bCVsPS5mObGNi2hDqumBEwXxjy8JlddXyQ2V57YSJGFkvrN5HJxW4N0-LP_GLTcxzPdeQ9D-hRpq8T9T3GvTovpi_cUBjsCmVcL7_02CpXeMml7j7Fd_faUFYapcjwU32OANS1Ff2eCrWHjrdXATbfsPx3nP1ip1PNafo8-QW1fAnH7xV3y9V4ZV8GKmLj69JE5bafvdKxq5GbnZBlGx7Qu3F5qgDiN2AlqBsII6LzozCFg9DMNj5f8ATJj4_Qi4WdXwMbEWiDqfNfBeNmRvhj0Mb5cXe8cU3pGVXwW278gdjwEduPYbh-4O5Q3lvafla4EZDa1fleXMnpHgVNnhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BHikbZQ-S4Dxt05A4iC-hCz7V2sx60eeYa6TGAnLSCz8G-lwrXBH-9-705_6FyW5f8NvA1ZV08Ye4_bsgZ1ZB9WHpmyzPwQKI7MpU5lIbl0Xj36_j8bPrBISX7ln_B7gF1XU_Laz6StW3_iXUN3haSUMseo6GaCTnWrjndjRETmOlQo5PR1ygXoHwYPdPJueZPsIYMSYRjA29FyUBICAyb_yEYcD8JgTtnGq2aKvk6WlJH4YC9fBz6_BD3gZJrAVfgTCizGSTE4sVCnu29GpCrHGIT3r9MmdC8KUh7j9gnHPeYJlM6eig0biZbaiLsCUauTQlNHqkPnBk3x3wpASGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز سه‌شنبه ۳۰ تیر با انتشار چند پست مختلف در شبکه اجتماعی تروث‌سوشال با بازنشر تصاویر و نوشته‌هایی از دو معترض به تازگی اعدام‌شده در ایران، مقام‌های جمهوری اسلامی را «وحشی‌» خطاب کرد.
دونالد ترامپ در یکی از پیام‌هایش با انتشار تصویری از یک پیام منتشرشده در شبکهٔ اجتماعی ایکس که به اعدام گل‌محمد محمدی، یکی از معترضان پروندهٔ موسوم به «میدان علیخانی اصفهان» اشاره کرده، نوشت: «آخرین مورد از ۵۲ هزار معترض بی‌گناه، و حتی بیشتر. وحشی‌ها!!! دموکرات‌ها کی از خواب بیدار می‌شوند؟؟؟»
رئیس‌جمهور آمریکا در پیام دیگری تصویری از یک پیام منتشرشده کاربری در شبکهٔ اجتماعی ایکس را منتشر کرد که در آن در کنار تصویری از عرفان اسفندیاری، معترض ۱۹ ساله اعدام‌شده در پرونده علیخانی اصفهان، نوشته شده که «لطفاً کمک کنید. لطفا صدایشان باشید».
آقای ترامپ در پیام دیگری، تصویری از یک زن گریان را بر حاشیه‌ای از پرچم در حال سوختن جمهوری اسلامی منتشر کرد که پلاکاری با این جمله را در دست دارد: «ما را نکشید».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77353" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های زیادی از اصفهان دریافت می‌کنم درباره شنیدن شدن صدای انفجار و لرزش شیشه‌ها
پیش‌تر اعلام شده که:
صدا وسیما: صدای انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده از ساعت ۹تا ۱۶ بعدازظهر امروز در جنوب و غرب شهر اصفهان، بهارستان و محدوده‌های صفه و شهر ابریشم شنیده می شود
مردم نگران نباشند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77352" target="_blank">📅 09:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfKlIDTUjMSA5J40e98x9MvIH2ZXb9HDW8dpaROW0x0v9fvEWGIUyPATCh3hg4pDH-FZfqXdVh1K3KuTasaKoRzovmMKUIB4c5tbgJUdam-6yhAdT2awppWqoVDhNFr9gNjpNVDKX_H6KJGdVORzU82jLvu95XI1gUcKvqME668v3hEl6IwwOmImopjbmjFE_1jH0uieDI9g0OQapWqwBvj4DKTalvl7ab_SlFpDYS9-HmKkhz4bZV4AeHWRc_C2Cp1L_9vsEEQVRy29qz8N7NSTFPq6in2pTI0w5Ja-M3x-5H-cH1hmze7fZnqticTIZvt1z9rhCLy47p3tkW763A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
خبرگزاری فارس:
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
ادعای سپاه: زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
خبرگزاری فارس:
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77351" target="_blank">📅 09:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرماندار آبدانان: آمریکا با موشک به نقطه‌ای در کوه‌های اطراف آبدانان حمله کرد
خبرگزاری جمهوری اسلامی، ایرنا:
🔹
به گفته فرماندار آبدانان، ساعتی پیش دشمن متجاوز آمریکایی با چند پرتابه مناطقی در بیرون از این شهر استان ایلام را هدف گرفت.
🔹
بهزاد نورمحمدی صبح سه‌شنبه در گفت‌وگو با خبرنگار ایرنا اظهار کرد: دشمن آمریکایی با پرتاب موشک، به نقطه‌ای غیرنظامی در کوه‌های اطراف آبدانان حمله کرد.
🔹
وی افزود: خوشبختانه این حادثه هیچ‌گونه تلفات جانی در پی نداشته و دستگاه‌های مسئول در حال بررسی ابعاد موضوع هستند.
🔹
نورمحمدی یادآور شد: دستگاه‌های امدادی به محل حادثه اعزام شده و مشغول بررسی دقیق ابعاد تجاوز دشمن هستند.
پیام‌هایی که من از یک شهروند دریافت کرده بودم از ساعت ۲:۴۱:
سلام وحید جان صدای دو انفجار اومد چند دقیقه پیش
ما آبدانان هستیم ولی صدا خیلی دور بود بیرون شهر بود.
ظهر هم رد موشک تو آسمون دیده میشد
الآنم یکی دیگه
2:49 دوباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/77350" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=Buek9VziD2WuA4hkiiwSQ_USBuqmFAoO-_a3o-xKQDo7roFKFTtP5WRN-RFV5NcgMzonP7ggZhB82AqK2dJj7WNfI8ozvNazU1FXVXrGfJl0RCf9D1kugYCHXkSbxPhVKPJ7ZS6E1_t4Y_joVgdGGKeWc6GwPzp86vq-tlM9Ow7CU-tZI3HgeJMP1ZxoyE20ow58ra33MVlu6mNdmu0HkKzUZ4CaKQ8cY2b-EklWjbUqvHNZg9tqsHSDn7rk_BILRYwU5Jlk-YO9r5FxFVK0mRw_p2Ftj5urD4BNG8gLQf9txcJfbzEuQd6MTSqtVftyYIKOF83jfESpmqH9tkvvWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=Buek9VziD2WuA4hkiiwSQ_USBuqmFAoO-_a3o-xKQDo7roFKFTtP5WRN-RFV5NcgMzonP7ggZhB82AqK2dJj7WNfI8ozvNazU1FXVXrGfJl0RCf9D1kugYCHXkSbxPhVKPJ7ZS6E1_t4Y_joVgdGGKeWc6GwPzp86vq-tlM9Ow7CU-tZI3HgeJMP1ZxoyE20ow58ra33MVlu6mNdmu0HkKzUZ4CaKQ8cY2b-EklWjbUqvHNZg9tqsHSDn7rk_BILRYwU5Jlk-YO9r5FxFVK0mRw_p2Ftj5urD4BNG8gLQf9txcJfbzEuQd6MTSqtVftyYIKOF83jfESpmqH9tkvvWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی با انتشار ویدیوی بالا: سه پایگاه مهم آمریکا در کویت، هدف حملات پهپادهای انهدامی ارتش قرار گرفت
مرحله نوزدهم عملیات صاعقه ارتش
روابط عمومی ارتش:
🔹
در پاسخ به شرارت‌ها و نقض عهدهای مکرر شیطان بزرگ، بامداد امروز و در مرحله نوزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، ساختمان‌های اداری  و آنتن‌های جهت‌یاب در پایگاه عریفجان، پارکینگ گروهی بالگردها در اردوگاه العدیری و ساختمان اسقرار نیروهای ارتش تروریستی در پایگاه احمدالجابر کویت را هدف حملات پهپادهای انهدامی خود قرار داد.
🔹
پایگاه عریفجان از بزرگ‌ترین مراکز استقرار نیروها و ستاد فرماندهی نیروی زمینی آمریکا در جنوب غرب آسیا و پایگاه العدیری محل استقرار بالگردهای آپاچی، شنوک و بلک هاوک نیروهای دریایی و هوایی  آمریکا است.
🔹
پایگاه احمدالجابر نیز نقش محوری در آماد و پشتیبانی ارتش متجاوز آمریکا در غرب آسیا دارد و تاثیر عمده‌ای در عملیات‌های هوایی و نظارتی این کشور ایفا کرده است.
🔹
ارتش جمهوری اسلامی ایران اعلام کرد، امنیت منطقه در پی شرارت های نیروهای تروریستی آمریکا مختل شده و  نیروهای مسلح جمهوری اسلامی تلاش می‌کنند در نبرد با آمریکا، امنیت و آرامش را به منطقه بازگردانند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77349" target="_blank">📅 06:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/841c527612.mp4?token=O4tEDWl8XWNMfzj9SWM1DMMw_B6keRMB4g5XacJYec6QJNYKVeGvataPyQ4JSTQwdSHh_-2BGJQ1R-Y577Olf0AeOYncJnsWUbtZpWPw_VrNIWLpK_gFBQTl9zinbyy6UNMoaAoIt0ZYhVhNpjWA1BL5YAfo9cGoHFeNgr9--ILaS3xlEyGhFOpyx9vL6wcoNRR7Jj2xJdLOnj2VFhN429OOwZzCC-ZnLc4oxjvZCpXDSFNSTMNFO3Eka7CHG9jpo0Y21hnmJXlZfG-SEihobX4HHhKp9ynn6nvoR1Yz2UwZKZssRUu24Uez5HbAeNV5qwT2hJ0BcSsMB1Q1tSgxig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/841c527612.mp4?token=O4tEDWl8XWNMfzj9SWM1DMMw_B6keRMB4g5XacJYec6QJNYKVeGvataPyQ4JSTQwdSHh_-2BGJQ1R-Y577Olf0AeOYncJnsWUbtZpWPw_VrNIWLpK_gFBQTl9zinbyy6UNMoaAoIt0ZYhVhNpjWA1BL5YAfo9cGoHFeNgr9--ILaS3xlEyGhFOpyx9vL6wcoNRR7Jj2xJdLOnj2VFhN429OOwZzCC-ZnLc4oxjvZCpXDSFNSTMNFO3Eka7CHG9jpo0Y21hnmJXlZfG-SEihobX4HHhKp9ynn6nvoR1Yz2UwZKZssRUu24Uez5HbAeNV5qwT2hJ0BcSsMB1Q1tSgxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند.
ترجمه ماشین:
پایان تازه‌ترین حملات آمریکا علیه ایران
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دور دیگری از حملات علیه ایران را در ساعت ۹ شب ۲۰ ژوئیه به وقت شرق آمریکا به پایان رساند.
نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز را کاهش دهند.
عبور کشتی‌های تجاری از این گذرگاه حیاتی دریایی بین‌المللی همچنان ادامه دارد. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
نیروهای آمریکایی همچنان در موقعیت و آمادگی لازم برای پاسخگو کردن ایران به‌دلیل تجاوز بی‌دلیل علیه دریانوردان غیرنظامی که در پی عبور آزادانه و بدون مانع از این تنگه هستند، قرار دارند.
CENTCOM
اطلاعیه شماره ۳۵ سپاه:
شب سیاه رادارها و سامانه های پدافند هوایی آمریکا در منطقه
روابط عمومی سپاه:
🔹
ملت عظیم الشان و مجاهد ایران اسلامی؛ حماسه حضور در میدان و ۱۴۰ شبانه روز ایستادگی بی‌نظیر و پرشور شما چنان روحیه ای به رزمندگان اسلام و مدافعان از جان گذشته وطن بخشیده است که با لطف و امداد الهی هر روز حماسه‌ای نو خلق می کنند.
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🔹
تنبیه متجاوز ادامه دارد و گزارش آن به استحضار شما ملت عزیز و قهرمان خواهد رسید
و ماالنصر اِلا من عند الله العزیز الحکیم
اطلاعیه شماره ۳۶ سپاه:
یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی و یک سوله آشیانه پهپادهای MQ9 منهدم شدند
روابط عمومی سپاه:
🔹
ملت عظیم الشان و قهرمان ایران اسلامی؛ در ادامه عملیات تنبیهی رزمندگان هوافضای سپاه و در راستای هموارسازی مسیر، برای دفع موانع عملیات هوایی و موشکی گسترده در مرحله دوم موج ۲۴ عملیات نصر۲،  امشب یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی ارتش کودک کش آمریکا مستقر در کویت مورد اصابت موشکی و پهپادی قرار گرفت و منهدم شد.
🔹
همچنین یک سوله آشیانه پهپادهای MQ9 نیز در پایگاه علی السالم مورد اصابت واقع و تعدادی پهپاد منهدم شده یا آسیب کلی دیدند.
🔹
عملیات تنبیهی فرزندان شما ادامه دارد. التماس دعا.
و ما النصر الا من عند الله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77348" target="_blank">📅 04:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RxbYZT6B-lJIO6piSpu3ORCUOCz4EkBJtvkOiPKMMSnEQ-e5ToMZkOLMjxacBXw9gSYpXN9S_Kl6l4lGwHiv_1C_CTPpyzKdFSG2k2TdexUroewGIoZCuVW6_ZqMrK5Ndkri8zb5Cln4uzcaexy2u1gemXEl_hQ9eDZ-6vnlhSQCrr6sYIruuTbsbZqbUUlzNKU1qLBRtLETyt3krUlAjdJx8Daj4DHfgvsHCV95kp8-2-dAxcC1zDodjTLwqfMC0JUrf5Fdm8ivVK6BMSssZqyNioNq9BD0QW4bUo8iLBAk3evCVURweBEv1j9VlxANy9453tM7FpTKJZ19pTjJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
خبرنگار صداوسیما: حوالی ساعت یک بامداد در برخی نقاط شیراز صدای انفجار شنیده شد که بر اساس گزارش‌ها یک نقطه در شرق و دیگری در غرب شیراز مورد هجوم دشمن قرار گرفته است.
چند پیامی که من دریافت کرده بودم:
شیراز رو باز زدن
یجوری شیراز رو زدن که شیشه ما بدجور لرزید
سلام صدای دوباره انفجار در شیراز
شیراز دوباره زدن
خیلی بد زد
شیراز 1:21 صدای دوتا انفجار خفیف دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77347" target="_blank">📅 03:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koYB8ka9LLacCrjC_hmPq202zKFjN3NxmUTmho_bEiCxYz4RuaMp5VWOF3UhlyNmz_U7hW8MlOZP6GmDPZ0V8NAM8b9ib_BFPj5u_u1gDtMjaapqN9XG2N7UK_9Om6xHZ6x0NJj5GgzpCZqJrAkNVg9KnO_p4_gIwgseq6YF5eNv-84kppE4wlFfFcESMZ0gLk3D5xfCAucCND55IWTyuf6EUwOFcQJ5p3gUXBiQzKNt9wYzzIjDMDvRPJ38K18J6g6GMdrGx-iv7HwHDo9XcYoIIq-0ae0OKsrxcH51pSkPH_BfjX7HSqm6Gru8nnVKZhQV6KE2xfCDEtsfOmkagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره تماس با نخست‌وزیر تازه بریتانیا: درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
ترجمه ماشین:
گفت‌وگوی بسیار خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام، داشتم. درباره موضوعات بسیاری گفت‌وگو کردیم، از جمله روابط فوق‌العاده‌ای که با بریتانیا داشته‌ایم.
در آینده‌ای نه‌چندان دور برای گفت‌وگو درباره موضوعات مورد علاقه مشترک دیدار خواهیم کرد. نخست‌وزیر کار بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا نیز برای کمک در کنار او خواهد بود!
درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
این تماس جالب بود و بسیار خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت کردم: موفق باشید و خدا به همراهتان!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77346" target="_blank">📅 02:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WikryssCUjw1kKyrNtgbIf_uv7kc-mIPTqCDiLu3qxcLbl8nLELZ-YHj9CFuztWO07SHNFc31AG8Zo0Z7FmgzzoKlyeKwS0Nx6gjDiJprG7uKwlt0ga9xUlbrv81O1r9bliG7d15FwRfwrCNuLkMLqGQRbJvLKB07BYQjDf0XmF9rSO6w8kM_LYjQdYbsREjc8yhLRD79Sf9uP3iiXJVxIewCTt8KZkvZ2CWqhR5Xo8ritXadYb2vwzZo6Da4J1B5M_7HaGJlO9S2e9LI_UyMevhKPMqeafjTqpKg0nV9fFaT4rSyGRoWNLHT0PYb6__joh3iR4fzCDxtDrLh6duiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از یک حادثه در فاصله ۸ مایل دریایی شمال شرقی لیما در عمان دریافت کرده است.
این سازمان افزود گزارش‌های متعددی دریافت کرده که بر اساس آنها، یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77345" target="_blank">📅 02:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس پایگاه هوایی ۲ انفجار ۰۱:۴۷
بندر ٢ تا شنيدم ٣٠ ثانيه پيش
1:47 دو انفجار به شدت قوی در پایگاه هوایی خیلی شدتش زیاد بود بندرعباس
بندرعباس ۱:۴۷ دو صدای انفجار شنیدم
درود آقا وحید دوتا انفجار وحشتناک ساعت ۱:۴۷ دقیقه بندرعباس
همین الان ساعت ۱۱:۴۶ انفجار فوق شدید بندرعباس
۲ تا انفجار وحشتناک بندرعباس ۱:۴۷
صدای ماشین‌ها درومد
صدای دو انفجار الان بندرعباس ۱:۴۷
بندرعباس ۱:۴۷ صدای دو انفجار
تک انفجار شدید بندر
سلام الان صدای دوتا انفجار بندرعباس اومد
سلام وحید جان صدای دوتا انفجار پشت سر هم اومد بندرعباس
ساعت 1:48 بامداد
بندرعباس ۳ تا انفجار شدید
صدای ۲ تا انفجار سمت پایگاه هوایی بندرعباس
سلام صدای دو انفجار بسیار شدید بندرعباس ساعت ۱:۴۷
درود وحید جان وقتتون‌ بخیر
بندرعباس ساعت ۱:۴۸ دو صدای انفجار بلند.
بندرعباس ساعت 1:47، دو سه بار سنگین زد
سلام وحید جان الان دو تا انفجار سنگین سمت فرودگاه بندرعباس آمد که شیش ها لزیدند 1:48
سلام وحید خان بندرعباس ساعت 1:46 چندتا انفجار پشت سر هم
سلام وحید بندرعباس همین الان صدای 2 انفجار خیلی وحشتناک
اقا وحید  ۳تا انفجار شدید قشم ساعت ۱:۴۶
وحید‌ داداش
حوالی۱.۴۷ اینا دو انفجار مهیب. اومد
فک کنم پایگاه هوایی بود
ثانیه پیش هم زدن
حدودا ۴ انفجار شد
تعداشو دقیق شمردم کمی با هم فاصله داشت
در حد هر کدوم ۳۰ ثانیه
ولی همش از یه سمت بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77344" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی:
۱:۴۵ قشم صدای انفجار همراه با لرزش
قشم من چهارتا صدا شنیدم، نمیدونم توهم زدم یا واقعی یود چون خیلی خفیف صدا اومد ۱:۴۵
چهار انفجار فعلا بندرعباس
وحید جان
قشم چهار تا انفجار ۱:۴۵ دقیقه
صدای انفجار بندرعباس ۱:۴۵
سلام وحید جان ستا انفجار همین الان بندر عباس ساعت ۱:۴۵
بندرعباس الان دو تا صدا آمد ولی صدا دور بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77343" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منابع حکومتی
منابع محلی لحظاتی پیش گزارش دادند برای دومین بار طی بامداد امروز صدای انفجار در بندرلنگه شنیده شد.
چند پیامی که من دریافت کرده بودم:
سلام وحید جان بندر لنگه دو بار زدن
صدا و لرزش زیاد
ساعت ۱۲ و ۴۰ دیقه
ساعت ۰:۴۰   صدای انفجار در بندرلنگه شنیده شد
درود وحید جان
صدای انفجار در ساعت ۱۲:۴۰ بامداد از بندرلنگه اومد ۲ بار
گویا هدف، نیروی دریایی سپاه بوده
صدای انفجار ۲ بار در خونه لرزید بندر لنگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77342" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی:
۳ انفجار در کنارک همین الان
۵تا انفجار سنگین چابهار ۱.۲۷
مجدد چابهار صدای چندین انفجار میاد
چابهار ۱:۲۷ دقیقه صدای ۲ تا انفجار اومد
ساعت 1:27 چهار انفجار پشت سر هم دیگه چابهار
کنارک 1:28 دو انفجار
۱:۲۸ دیقه کنارک دو بار صدای انفجار اومد
🔄
کنارک 4 انفجار دیگه
خیلی سنگین بودن این چهار تا انگار خونه رو سرمون خراب شد
۴تا دیگه چابهار همین الان ۱.۳۰
۱:۳۰دقیقه ۴ بار چابهار زد
نمیدونم کجاست اما از سمت دریا بزرگ دورتر
۱:۲۹ چابهار ۲ تا انفجار دیگه اتفاق افتاد
دوتا پشت سر هم و باز 3تا پشت سر هم 1:30 چابهار
صداهای شنیده شده در چابهار و کنارک: ۵ انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77341" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wgd8KewQExeEWnfzOEeBD3kCqpPAnDgfSCcAz4m7oLRso84uCqRkTMZI1Xed9Fbh7nonwRYOaoZReig07ShnGUKSou15AfNZAayq9Yip27IQIj082_0erUWv-CjZaTcbl49BOd0oaAnE8JNek_I4My9g6ph7dxUeJ0BWIJEpNqEnt71EOIUmvjm1ZA0BxqcejlHQxdf-DbbdMCfXj5eQFoUHeO7M5gwUWBfSSUp1xZfFbApHCDSKEgVagWHSbj1KTINitD9IPfniwxyVjHMcKSYU2JtdipmvAWjG70DqiMD8y28rC4EwyE9p6XTzJ2O7aCE55WtvUnnoF7rM8dTJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر از شنیده شدن صدای دو انفجار در شهر اصفهان خبر داد.
دقایقی بعد، استاندار اصفهان اعلام کرد که امشب حمله‌ای به شهر اصفهان صورت نگرفته است.
@
VahidOOnLine
فارس:
استاندار اصفهان گفت: امشب حمله‌ای به اصفهان صورت نگرفته است.
وی ادامه داد: در حال بررسی علت شنیده شدن صدای انفجار اعلام شده از سوی شهروندان هستیم.
تسنیم:
معاون استانداری اصفهان: هیچ گونه تجاوز دشمن یا انفجار در سطح شهر اصفهان و سایر نقاط استان نداشته‌ایم
من هم چند پیام مردد داشتم و از این رو فکر می‌کنم صدایی شنیده شده ولی مطمئن نیستم که دلیلی نظامی داشته یا نه.
منابع زیادی هم هستند که هر روز کلی خبر دروغ تولید می‌کنند و از این رو اعتنا کردن به پیام‌هایی که بعد از چرندیات تولیدی اون کانال‌ها ارسال میشن هم خیلی سخته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77340" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NIRkA-yQXWyA36EANPdDCAh7-8D6SSG5N8OcfRVn_BYFmmLcUn3RWQlEAcr5Uo28R8HuKtscX52f-UpxQfNBEAkwDJIckL8hzs0yIvowAwpN3WtJuxqagehXM_1grepoi17ZoYmRqGJoVA07zrmp7PrNgtlT1_t9lDihodNOSfoVGuthMR6nOWNPK-ZURAJbz9MPgf1Ja07A-i_5gcX3KcEBloQxZEfKjd0x6aOvUu9-l0KlG_0TWBQjMDQNh2bA_3lVKdNlzltJVpVVZTIPxp69miF7QJngkkHKgy1idfo07ZL4FI0a_u5P_dl4gKhgz6Nl5kXa4nkQOQktNyXpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UJO4YYkAoMIa9YokZB_esc7fHeJIjeFqwi8tqb_iguXsZJ__eLCcNlEGVjVEE_OCowUJGsq8EBbwIH4nnUnLRE6HHRdkkBUJb96Z5WMLXqo0XzLZjdKjaGenxMLsk4gVOPnx7ug5i2AVQMDNBusRiBEwx9svGiFEN0PLG4zxzscKoHoHP0iBSHTHsI86BlNbPK2-grGiWHJGkSnr9SPf7yRR3xXQVkfotm0HJ0WKNvHftZphNxId3vXR3g28LmUlunV_UtPqTwyr9uOZoII_2adPxvgUpphjOsw96rw8TXAfr6uvi_guTjUKAwVICOdq_8I_MSwg-Jb1d0W4DOpRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kiuKIcg1QKKrqskDkvTnqB_0NTnQUh4EkIl7-eSXhr1gWdw8Oy-hgGrINxI6Hg1cq1oid50wLyo7DBwSItki6wLKoQa4xXQ4Pr4po1WQnXW-oDDOzIz8w5iGS2tfuT-6PykkZb9m4fSDjDbNNfW4kXyasL79TUQKj1DU_Yw1SPiCKMCDXyaD89sRCh6x6Sdxb7LSHlKKTiiGHdjA9gIyyhILOyzt5zzuT7o76ndoDxcwmk8avM5bmSPMEUGFiDk8o2fQnu4XVzWwfLZ_M-27y5RI5Bjx0xj2MkVxZWLKwo5XITQjjWvZHO8tWrNq09EZixcbr07HUlmRlrE09rXN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c2WAPrdtqnmbVXEm_kqJcbSM6Vi81E4Xc7A5Bu_Du1E9yug4MXRnqHC3FCN0BDjwZoZ1YL-Z5cy4aqPWRul3ZINOR-2dINUXv6r3z8LcsuuJ98wjTmlAHi9-_Rf1UsVfMUaaYDaU_G3QbBzZwL0X0h8wptKBKss3AZLNq95WUTlUL1Ldex6YL8HoXzWZoY38eE4G_fNt8I5FqJECzmkxQGw_4l2UI6HKnYinVQLy2oH5e_3IMu5BuQmhCU9hxxsRXked95DPqciPWIT5-S4CltGrm002ycNpUixmWUUaRfWzJ6oTaol3LKyUIk-caaGY9xKknQd3_C1eq0N48N5ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tOs3MEBM2hNS0udkP-mQ5a9bNHfWhdnkEFxZ34Y2ZPbk4mCvpv-SaYR7VUynbs3DI_OT0MPJdQMg86tBKHmjJx03G0Ud5L-NAajJidLm-YWZ8Usf48j9iMgZyjT6mKh5FAMQw49_5PNUWLjjaSGxh4TfxSuzNRssU77LD2lpFExN94fXDu0lb6bXNAKz4yjbRzvy2k5U95wYY5nw6Lf7dwNBBHZS3Sw3TOxncQ7igv6KLpPPR5q8eF_WTakNYd_EEovNTczTQRAJ4qL1KxHIucm3QjxacLemI6ZplaDrhhvo9w9-iEUmMYCAX7tKMcxjA4B6lXkp8R7cPW3rOdWoSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vahid
'هدف قرار گرفتن نقطه‌ای در کوه دراک شیراز'
تصاویر دریافتی از شهروندان با شرح بالا، سه‌شنبه ۳۰ تیر حدود ساعت ۰۰:۴۰ بامداد
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77335" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PTkqPXP-xtpZOA9aGKRFrxN6ZoAKBd1U5YLf_-oZu3FxDMARgBXpBL-Y3Z3qPEV_xatc8G5HcK5UpgeMB4srbRNiHinwXunXajJXVNPi9nq9gBsklhpUI158L_XpUHCwyKpOxkbPO9vXemHeoEyBZfxF9hPINNHa1RPLvo8D1tFv8F8kscrV4wIFiqUgawHvCNrENwTvlNHwY5zHJY_tzVRBlSvkMeQeDB-p4Nw8DEUsGnXfZIw_mQA8IyzV4DLLK75ka3cboOMQwtIRczv6brCXp_Bd1zyPA6qPvRxBAuFwJ8UvQZE8o_out9K8BEMQbbkwmpNOeIR17nQ2Hz5kUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TkheQUqzLbkNjwjB4DickaCESdxiUDzDMJylqhkZKDY2MMEXtjargGrqnQJgGdwsfuTWFc-U8_1mAqGKxp5AUZn4kYdzb7jsrzvjPcWo4HYibiGClL7lZsENOXnLYxIdu55VCVk2RGKe7xmN-_ZAgL613tZ5V9bex1UupVx1xiEnc7UaEytQTuDLTBNCVB8i-jJDGW5trSoV_bTV3XJgf6FEP4qpqtiraUyARUBHoQyHSI5TauKcLS2QlwMGNUwBghguz7IZLPtTKm2DvPyBSYzaQohqBiZFiaBlCkCmVZDRf9LKnVO31KzwloW_Qj3FcXcJ511VrMHyIa0pERF0oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی درباره صدور هشدار در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77329" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده ده دقیقه پیش:
سلام شیراز همین الان صدای انفجار اومد12.37
شیراز همین الان صدای انفجار اومد
شیراز همین الان صدای انفجار مهیب اومد
🔄
پیام‌های رگباری الان:
همین الان شیراز و زد کلفت
همین الان صنایع صدای انفجار اومد
سلام وحید جان
شیراز سمت صنایع رو زدن ساعت 00:45
00:45 شیراز صدای انفجار
فکنم صنایع الکترونیک رو زدن
همین الان شیراز صنایع رو زدن
شیرازو زدن همین الان
سلام وقتتون بخیر
ساعت ۱۲ و ۴۵ دقیقه بامداده
شیراز همین الان صدای انفجار اومد
شیراز صدای انفجار
همین الان شیرازو زدن رکن آباد خونه لرزید
فرهنگ شهر شیراز صدای انفجار مهیب  ۰۰:۴۵
شیراز صدا اومد
سلام یدونه تک انفجار صنایع شیراز ساعت 0:45
شیشه ها لرزید
ساعت ۰۰:۴۵ صدای انفجار از شیراز
شیراز ۱۲:۴۴
احتمالا صنایع صدای انفجار
درود وحید جان
الان صنایع الکترونیک شیراز رو زدن
این دومین انفجار امروز تو صنایع هست
شیراز الان 00.46 زدن
12:45 معالی آباد صدای بلندی شنیده شد ( انفجار یا بمب نمیدونم)
چهل و شش دقیقهٔ بامداد صدای جنگنده و انفجار در شیراز
سلام وحید. ساعت 00:46 محدوده صنایع الکترونیک، صدای انفجار شنیدیم.
شیراز صدرا همین الان صدای شدید انفجار اومد
شیراز صدای جنگنده اومد روی کوه دراکو زد انفجارشو دیدم
همه فکر میکنن صنایع رو زد ولی بالای کوه دراک بود
امروز ساعت ۵ هم از بقیه شنیدم که صنایع الکترونیک شیراز رو زده بودن
سلام شنیده شدن صدای انفجار صدرا ۱۲:۴۷
همین الان صدرای شیرازو زدن
شیراز صدای وحشتناک بلند همه جای شهر شنیدن یا صنایع بوده یا کوه دراک
وحید ساعت ۱۲:۴۵ بعد نیمه شب صنایع الکترونیک شیراز رو زدند صدای انفجار اومد
۰۰:۴۵ صدای مهیبی اومد، ما ابیوردی هستیم ولی صدای انفجار تا اینجا اومد
سلام همین الان حدود ساعت ۱۲:۴۵ شیراز صدای انفجار شدید اومد
سلام الان شیراز صدرا هستم صدای انفجار اومد
شیراز  0:45 صدای انفجار اومد
سمت فرهنگ شهریم ما
سلام ۰:۴۵ شیراز سمت شهرک گلستان صدا انفجار اومد
شیراز زدن نمیدونم کجا بود ولی من از فرهنگشهر شنیدم صداشو
سلام وحید جان  دکل مخابراتی کوه دراک شیراز رو با جنگده زدن ۰۰:۴۰
من رو پشت بام بودم دکل کوه دراک رو زدن
صدای جنگده اومد بعد زدن
خونه ما معمولا وقتی صنایع رو میزنه صداش نمیاد، این انفجار مشخص بود خیلی عمیق  و بزرگ بود که انقد واضح صداشو شنیدم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77328" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
چابهار صدای جنگنده سطح پایین میاد الان
سلام صدای انفجار شدید در چابهار ۰۰:۰۲
۰۰:۰۶ دیقه صدای انفجار اومد کنارک انگار دور بود
چابهار ساعت 12 شب دوتا سنگین زد
🔄
چابهار دوباره صدا جنگنده :۶
انفجار سنگین :۰۷
الان زدن چابهار 12:07
چابهار الان صدای انفجار شدید
درود چابهار الان زدن خونه لرزید 00:07
دوتا دیگه هم زد
چابهار همین الان دوباره زد
انفجار خعلی سنگین ۱۲:۰۸
وحید ۰۰:۰۷ انفجار شدیدتر
کنارک همین الان صدای سه انفجار
سلام چابهار الان ۳ تا صدای انفجار اومد۰۰:۰۸
چابهار همین الان دوباره زد
۳ بار شد
🔄
صدای ۲ انفجار دیگه در کنارک
همین الان یکی دیکه چابهار
صدای انفجار دوباره در چابهار
صدا جت امام علی زد یکی ۱۲:۱۱
باز یکی دیگه زد همین دقیقه
پشت هم داره میزنه
جنگنده ها در ارتفاع پایین در حال پرواز هستند
داداش امامعلی چابهار رو مثل اینکه زدن
سلام آقا وحید طرف های امام علی نه خود [پایگاه] امام علی رو زد
دو تا چیز شبیه فلر از سمت دریا اومد چابهار
نمی‌دونم چی بودن
منابع حکومتی:
فرماندار ویژه چابهار از حمله هوایی دشمن به شهرهای کنارک و چابهار در بامداد سه‌شنبه خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77327" target="_blank">📅 00:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWUlVTdihMcndKHMr7I6x-kiT8bNInGus1UihQIW9zec3Iwkijya7mcLOoP1J-4uYpsW6LoTA61JZySye64V2IJ_j4r3bs3sBBtGIHinan99wPEo6XyTlIFqM-1uQyuOeCtDz4iG4Hju3DEwii96m4xypwMfAKKm472PBKfvmyKRNek1-J7ct5oIJ8uzzqd2LNPXbumirPjDyT2h1-Lv-6dmuV0k6UmdMwlM3MeDmlmWms-hVNRn2cCz0P290wDUv2yKacSEUs0VGWvBeMx_X0Mw28bbHwnme64Q9fDtc87SLICuzaRaAwCpv0NSTGguCxf4uBq8OgEnmtMqln4_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۴ بعدازظهر به وقت شرق آمریکا [۲۳:۳۰ به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور جدیدی از حملات علیه ایران را آغاز کردند. هدف از این حملات، تضعیف بیشتر توانمندی‌های نظامی ایران است که برای حمله به کشتیرانی تجاری در تنگه هرمز به کار گرفته می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77326" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار الان بندرعباس
صدای انفجار مهیب بندرعباس ساعت 22:33
همین الان ۱۱:۳۴ بندرعباس صدای انفجار شنیدم فکر کنم
سلام وحید جان ، بندرعباس صدا اومد الان
بندرعباس انفجار همین الان
سلام ساعت یازده ۲۳:۴۳ بندرعباس موج انفجار
انفجار در بندرعباس
بندر انفجار ۱۱.۳۴
ساعت ٢٣:٣۴ صدای انفجار نسبتا شدید بندرعباس
انفجار شدید بندرعباس ۲۳:۳۴
بندرعباس الان یدونه صدای انفجار اومد
بندرعباس ساعت ۲۳:۳۴ صدای انفجار شنیده شد
۱۱:۳۴ صدای انفجار بندرعباس
وحید سلام ساعت ۱۱:۳۵ بندرعباس یه انفجار خیلی شدید امد
بندرعباس صدای شدید انفجار همین الان 11:35 الهیه جنوبی
سلام صدای انفجار بندرعباس ۲۳:۳۵
بندرعباس الان صدا اومد تقریبا شدید بود
بندرعباس صدایییی وحشتنام ۲۳:۳۴ دقیقه دو تا انفجار
بندرعباس ۲۳و۳۵صدای انفجار اومد خیلی سنگین بود
سلام آقا وحید ساعت ۲۳:۳۴ دقیقه صدای انفجار اومد بندرعباس
ساعت ۲۳:۳۷ دقیقه یه صدای انفجار دیگه از سمت دریا اومد
یک ربع پیش از پیام‌های بندرعباس خبرگزاری فارس نوشته بود:
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77325" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFyPZBf9qQUpsTsKq-yPm28VTZAWX5ZC6mz1v5GvUhZ67g8f9TCaktbSYEVQP73270RiVVvVrGjTOzLxHWmQhJb41IVtpf87NO5SC95ZBrfxk-Em7sQy6EFUG58eghfx6IGW9U2Sf7N4_MluqduaQeLxZuxz5iOF8afyMnNvttkDTyZfI1YjEcg-j7iyo7db9oNUx9dY7Xfv2AGweMYn50sJoJ2FGj_aYwKey1ZeQYHZbz_oDGoxLICOtrDlM_bxjCWf3aryOsxOadbC-wor6SQ6bb1R5-5-t0UpWFatDyWcpwqDg2WT_x1-VlqZdUAEnJxz8oDStEoB7_KeVoAFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فارسی وزارت خارجه آمریکا شامگاه دوشنبه ۲۹ تیر با انتشار یک هشدار امنیتی از شهروندان آمریکایی خواست در پی افزایش تنش‌ها در خاورمیانه، هرچه سریع‌تر ایران را ترک کنند.
در این هشدار آمده است که وضعیت امنیتی منطقه همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
@
VahidHeadline
خبرنگار اکسیوس، ترجمه ماشین:
یک مقام آمریکایی درباره گفت‌وگوهای احتمالی آتش‌بس با ایران به من می‌گوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را به‌دلیل نقض تفاهم‌نامه و ادامه اقدامات تروریستی‌اش در تنگه هرمز مجازات کند. علاوه بر این، رئیس‌جمهور ایران را به‌دلیل کشته‌شدن اخیر سربازان آمریکایی مجازات خواهد کرد. این ضربات ویرانگر تا زمانی که رئیس‌جمهور صلاح بداند ادامه خواهد یافت، اما گفت‌وگوها میان دو کشورمان همچنان در جریان است.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77324" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=h8RPIIGjcZZt1SxFiSUvo3ug6ZXL6lrD7lGdtrLDqhEZOuPQqzDT7jHmv8BHL5EAOSB0BelBdl84AQcfdxunAwURk4gVEQgygxHmvEqFk6WXJ2fG5PYAaUDCpZB9tMXV18w2z0UAs79gaAtasOQY-Z9HdY1V4IeTzzA7rKjGgHW0Zu8A3aBWFJiVqCo3BQg6O6KmBb5pbADn99OvJgYDofLIX-rO43Jnr8NE1IBc11t335Na5uyZXeJHcKqvHfmBR23girl8785YnWKd_dDTBKxBssHlMYXEfvQ9ZJVj72AvaT7jljOmTu2tSgS5mwAs3UX2yinLLubSWKHTZjwSKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=h8RPIIGjcZZt1SxFiSUvo3ug6ZXL6lrD7lGdtrLDqhEZOuPQqzDT7jHmv8BHL5EAOSB0BelBdl84AQcfdxunAwURk4gVEQgygxHmvEqFk6WXJ2fG5PYAaUDCpZB9tMXV18w2z0UAs79gaAtasOQY-Z9HdY1V4IeTzzA7rKjGgHW0Zu8A3aBWFJiVqCo3BQg6O6KmBb5pbADn99OvJgYDofLIX-rO43Jnr8NE1IBc11t335Na5uyZXeJHcKqvHfmBR23girl8785YnWKd_dDTBKxBssHlMYXEfvQ9ZJVj72AvaT7jljOmTu2tSgS5mwAs3UX2yinLLubSWKHTZjwSKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد گودرزوند چگینی‌، نماینده شهرستان رودبار در مجلس شورای اسلامی می‌گوید که در تحولات اخیر، این ایران بوده که ابتدا توافق آتش‌بس میان ایران و آمریکا را نقض کرده است.
او در پاسخ به سوالی درباره توقف مذاکرات به دلیل نقض آتش‌بس گفت: نمی‌دانم گفتنش درست است یا نه اما اول ما حمله کردیم و بعد آنها سیریک را هدف قراردادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77323" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82071ea2df.mov?token=d4HKRMYZrsB-2lPYO80qZaEYZhphz9HvNoMRNuSeejPoHIXlcz9NWPqU3tIoPi5Pi8nGwbenGm-8PsQCc5_b6Qvqtw1XBPlLrdkq_bnehR6YIaYQ4U729k35scMNcW-vF7oYZAxOvw1M37sws5iFKpY75bOCDMBADd5Mqj7JtD2SeSUlw9ArPF0UAwqiC-fFG3MSL48I_PMfb6jjbwo4wucwjbwpqYV422yH_vDw6EFCP4Sc67LDoZGYCO8wu_UIApYyUIzqvCDnWZVTYMBhcnRwm_S8qfEDHPnASu_Gzd0vtpDMpp-ESh3YEmkSpw860vDkydzFAlmc-xUM1oV9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82071ea2df.mov?token=d4HKRMYZrsB-2lPYO80qZaEYZhphz9HvNoMRNuSeejPoHIXlcz9NWPqU3tIoPi5Pi8nGwbenGm-8PsQCc5_b6Qvqtw1XBPlLrdkq_bnehR6YIaYQ4U729k35scMNcW-vF7oYZAxOvw1M37sws5iFKpY75bOCDMBADd5Mqj7JtD2SeSUlw9ArPF0UAwqiC-fFG3MSL48I_PMfb6jjbwo4wucwjbwpqYV422yH_vDw6EFCP4Sc67LDoZGYCO8wu_UIApYyUIzqvCDnWZVTYMBhcnRwm_S8qfEDHPnASu_Gzd0vtpDMpp-ESh3YEmkSpw860vDkydzFAlmc-xUM1oV9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: موشک‌هایی در آسمان ارومیه
آپدیت:
ارتش اردن شامگاه دوشنبه ۲۹ تیر حمله موشکی به این کشور را تایید و از رهگیری موشک‌های شلیک شده به سوی این کشور خبر داد و اعلام کرد که سه موشک از مبدا ایران که پادشاهی اردن را هدف قرار داده بودند، سرنگون کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77322" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=RLUxCYEN2aiPIJZZKCwGLdkYq0LOiR9oCsWJ2G9edJEHUn2AfPP3VzwdPAAz_5TMf0g8suQ1t58cYcSGxzQca-_-yPKrGh9I_ZuuX4feAxfcx-uYhfQmbCqhaSGvR2APgkd0PW0ZN6scM76-uVATjSANjX95OFzDNWn0a3BMd_vHGUBU-b-oTmm_gfDAWR1_8_yOMmTYhsZJaqCeKYQBSdGFBTnVjmgyeEcB-qnoWQj0kOgAo_B5lu-Zja4Rly-FQoN63Sq8YLOBMav1Nz5vojKUxxHjYmSugOUqnctSr7onTq-JbyCS63Lq3NvP4b5_YvYEyiihQOQ-wE1gQ1opFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=RLUxCYEN2aiPIJZZKCwGLdkYq0LOiR9oCsWJ2G9edJEHUn2AfPP3VzwdPAAz_5TMf0g8suQ1t58cYcSGxzQca-_-yPKrGh9I_ZuuX4feAxfcx-uYhfQmbCqhaSGvR2APgkd0PW0ZN6scM76-uVATjSANjX95OFzDNWn0a3BMd_vHGUBU-b-oTmm_gfDAWR1_8_yOMmTYhsZJaqCeKYQBSdGFBTnVjmgyeEcB-qnoWQj0kOgAo_B5lu-Zja4Rly-FQoN63Sq8YLOBMav1Nz5vojKUxxHjYmSugOUqnctSr7onTq-JbyCS63Lq3NvP4b5_YvYEyiihQOQ-wE1gQ1opFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از تبریز
ویدیوی بالا: شلیک موشک از [...] تبریز ساعت ۲۱:۲۴
صداشنیدم تبریز موشک زدن 9:25
میگن از [...] بلند شده
همین الان از [...] تبریز ۲ تا موشک فرستادن. ۲۱.۲۵
همین الان دوتا موشک از تبریز فرستادن  21:24
از تبریز دو تا موشک شلیک شد الان
صدای شلیک موشک ساعت ۲۱:۲۵ از تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77321" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=IZCMzQnheqkIzVtgl1Yp3JmGfYgmRx-jsc3LtDWFnh3dxkQiLQW6gOpjhGY1SAg1G6Q_sOPGYRvAqH5ZlIZCQgTK3slttysHrU4RJ_ijcupffFcxQlfxMxXLasvWF8QagxxyVysflOpEwwBtcQ7J6T-dX_fyfZtOXyAVS1Q6B8YcofaqJmQhW6Yx3jmbxDH0BQGrImiaYjCOSPB_mB8oXkSqDH5aOiaNZ0Oye1zqv8sq-G-hApq9LgjRF3TlwKdou7kIYXTqH1Aw5LoF8uDtfhRMYotbBfP4RJ8c_NJxQVesmKrpDFbUNZ-8-20UVecjN5bpUmlHBxyWFeelWjIiMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=IZCMzQnheqkIzVtgl1Yp3JmGfYgmRx-jsc3LtDWFnh3dxkQiLQW6gOpjhGY1SAg1G6Q_sOPGYRvAqH5ZlIZCQgTK3slttysHrU4RJ_ijcupffFcxQlfxMxXLasvWF8QagxxyVysflOpEwwBtcQ7J6T-dX_fyfZtOXyAVS1Q6B8YcofaqJmQhW6Yx3jmbxDH0BQGrImiaYjCOSPB_mB8oXkSqDH5aOiaNZ0Oye1zqv8sq-G-hApq9LgjRF3TlwKdou7kIYXTqH1Aw5LoF8uDtfhRMYotbBfP4RJ8c_NJxQVesmKrpDFbUNZ-8-20UVecjN5bpUmlHBxyWFeelWjIiMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل‌ها و پل‌های تخریب شده در حملات آمریکا، روی نقشه
در جریان حملات اخیر آمریکا که عمدتا بر جنوب ایران متمرکز شده، چند پل و یک تونل و یک ایستگاه انشعاب راه‌آهن در استان هرمزگان هدف قرار گرفت که خسارات جدی وارد کرد.
این پل‌ها و تونل در مسیرهای دسترسی استان هرمزگان به استان‌های فارس و کرمان قرار دارد و تخریب آنها باعث توقف تردد در مسیرهای بندرعباس به سمت شیراز و همچنین استان کرمان شد.
تونل شهید میرزایی در محدوده گلوگاه در مسیر بندرعباس به سمت حاجی آباد یک روز بعد از تخریب هر دو دهانه رفت و برگشت باز شد. در مسیرهای دیگر که پل‌ها هدف قرار گرفت، مسیرهای جانبی پل‌ها به طور موقت مورد استفاده قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77320" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omMQmBGTcm0Xs0klLW5k60HgV3jX_DFFcR0dTeVl63JTX29c0KMEe5zfKKGLr8uXAmIOI2ywVc2HFP1Bdjmbaq1vpCAoNRnqJ_mAF17H9siKr6QV9mV_brk8vBegl-aHT--yzzn8UfkJkmmnYfY7wQp4Bzubxs__v8RgDJEr2hfVSTwzYlYAIyDNXK5bs9M1UWa8dOh73Z1Pi-s5Fe1A76TNQSocn_g1gaVWgw6OWMHJWxaQ02buVjvYB_-K7pDYo74MTauykBiNL47-C5zBBK35s2qYlcyx5c6JmUlij885cCINblS0ziQYZZ9Qvtlox6dVBP0utNtSqVn-t1_z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت! این دستور به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک ارتش، و تمامی فرماندهان نظامی ابلاغ شده است.
رئیس‌جمهور دونالد جی. ترامپ
Every time Iran kills an American Soldier they will pay for that killing many times over! This directive has been passed on to Secretary of War, Pete Hegseth, Chairman of the Joint Chiefs of Staff, Daniel Caine, and every Leader in the Military. President DONALD J. TRUMP
realDonaldTrump
ترامپ در پستی دیگر نوشت:
بنیامین نتانیاهو تحت هیچ شرایطی، به هیچ شکل و طریقی، در ایالات متحده آمریکا بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را کشته و طی ۴۷ سال گذشته سربازان آمریکایی و دیگران را به قتل رسانده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که رؤسای‌جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!
رئیس‌جمهور دونالد جی. ترامپ
Benjamin Netanyahu will not be arrested, in any way, shape, or form, while in the United States of America. He is fighting against the Islamic Republic of Iran, which recently killed 52,000 innocent protestors, and has spent the last 47 years killing American Soldiers, and others. The only ones that should be arrested are the people that led Iran into this unprecedented SPIRAL OF DEATH AND DESTRUCTION, something that should have been dealt with years ago, by previous Presidents! President DONALD J. TRUMP
realDonaldTrump
پیش‌تر:
زهران ممدانی، شهردار نیویورک، اعلام کرد در حال بررسی امکان بازداشت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در صورت سفر به این شهر برای شرکت در مجمع عمومی سازمان ملل متحد در پاییز امسال است. ... @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77319" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bDQSIip_MPYH2JO4Jdb8hrS-FxZ7mg-JV28bbTEEenHREqL9PWCE3Bz5Q0nA4Z3FeUd3WHROqiHePBez5-31cXqIE5qk1UWW8F6oF5V7GBKBQ2KN1Lm2A_HU7PzKPgA0JBsKszgBra_Ux5aoAATVsVdAQe-6NfYCn48_JJsM-HmLB_evk9NOsPsbExYN_LfWpWPvzRN8I9pSigFRcwPg5iKI39noVuRMv71D9--9RIyJVmeFxszSMWGdLyc78Sd6f4K2lc6cQfTkGEDShsYgPXHGllbKGPVdLLheT_lUV8aqHyTuUxOBeANaQT0whRYEqgd2vAJliY_xrHOgjmB7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند پیام دریافتی تاییدنشده با مضمون: کارخانه نخ شهرستان خمین رو هدف قرار دادند.
هم‌زمان منابع حکومتی:
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی در گفتگو با خبرگزاری صداوسیما: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77318" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWLNh-oSajbgxIhiN0LU6OrPl2kp9NhJLqNMFBVYw4X0GtfPFDWLq1zxXGtqmqmxlfx91MEZF0j0RJEYG5jGStVUJzLMr3NeMIcBwE2eh1EMI7h5OOeD5rRe-1FTxkqCqJtD6qtbrUtexR8dHquGA5bMLjSxO98VDVDkUkGgd7mpd8MoKHr1Drjk75osJtc4m7SgX2khAvGII14VKh2wWavBPcFLU9F06poMq5eFKkrNJh-FkeUnZnMGkbtFnCsWGEWc1cDzPp-GFO_bbD6iqSxO0DzYVMLEZcxgchq2lAEovIe2ejHnYmxFeT6Kl9EXwe1pt1mLHf6ehN-YUS1vLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان نوئل بارو، وزیر خارجه فرانسه، در شبکه ایکس اعلام کرد که دو نفر از کارکنان سفارت این کشور یک‌شنبه از سوی نیروهای امنیتی جمهوری اسلامی مورد «تهدید و رفتار ارعاب‌آمیز شدید» قرار گرفتند.
بارو گفت این اقدام نقض آشکار مصونیت‌های دیپلماتیکی است که این افراد از آن برخوردارند.
وزیر خارجه فرانسه افزود: «آن‌ها بدون هیچ دلیلی برای چندین ساعت بازداشت بودند و مورد بازجویی قرار گرفتند و یکی از آن‌ها نیز مورد ضرب‌وشتم قرار گرفت.»
او گفت: «آنها سرانجام توانستند به سفارت برگردند و اکنون در آنجا در امنیت به سر می‌برند تا در ساعات آینده به فرانسه بازگردند.»
بارو تاکید کرد به عباس عراقچی، وزیر خارجه جمهوری اسلامی، اطلاع داده‌ که «این تعرض غیرقابل‌قبول به سلامت و امنیت کارکنان ما، بدون پیامد نخواهد ماند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77317" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnOhGN2SY27tl2XtXMBkmfnlqrdYEQ0nngAXzU_NLFyvVrAz1vIKxJ-mqIwHtVhiHWhK_h-GuKj183LrfptwaqEX3IrD-kR9aWbTv9hjpRsVFEVIHVjPpUgP6XVtBsh60CYaFUZ2sKoCYZpcKBP-z8cvzwbfSzi6Cw5zPT4U6UYfXWAYdBagX3JSe_RiNX4Vv6hIdxf89HVoSnL5EjrZH4R2DDstuu040hg1pvipIn-tC75x9_EaR_5_gILpFLTXslFMT3dUBOyFXOziytQkOpnsmP5RSeGotxR_97lxIiO8I4Hhm4HfDapIAjtPh0uYMM3zug0s-hVTEFERGkUioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: پنتاگون تصویری از سرباز ایزابلا گونزالس، نظامی ۱۹ ساله آمریکایی اهل کارولتونِ تگزاس، منتشر کرده است که در حملات موشک‌های بالستیک و پهپادی ایران در آخر هفته کشته شد.
گونزالس در حال پشتیبانی از مأموریت آمریکا علیه گروه «دولت اسلامی» بود که هنگام کمک به دفاع در برابر حملات ورودی ایران کشته شد.
مرگ او در حالی رخ می‌دهد که درگیری‌ها در سراسر خاورمیانه همچنان شدت می‌گیرد.
نیروهای آمریکایی نهمین شب متوالی حملات تلافی‌جویانه علیه اهداف ایرانی را آغاز کردند؛ در حالی که دو کشور همچنان برای کنترل تنگه هرمز با یکدیگر می‌جنگند.
FoxNews
آپدیت:
خبر فوری: رئیس‌جمهور ترامپ در مراسم انتقال رسمی و با احترام پیکر دو سربازی که در حملات ایران در اردن کشته شدند، شرکت خواهد کرد. این مراسم فردا شب در پایگاه نیروی هوایی دوور برگزار می‌شود.
کارولین لیویت، سخنگوی کاخ سفید، در پستی در شبکه ایکس نوشت: «رئیس‌جمهور و تمامی اعضای کاخ سفید برای خانواده‌های آنان دعا می‌کنند.»
رئیس‌جمهور نیز در پستی در تروث سوشال نوشت: «هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت»؛ در حالی که آمریکا به کارزار نظامی خود در خاورمیانه ادامه می‌دهد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77316" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6cac939191.mp4?token=uH8vL99ZSm0w6VMhPre8ZzQM43PkK9sW1AcTE-yg5Xhb5GQVciyz3pnLYz-58slS6ru_qTkS2pQqocskLg-Jxqlc_d6-ZJxF_3F_AP1H_DNzBj1mZIqR56jp-MAynTKQEAV1xrWn5NUL3HX662hUiSuPggZoIxX_6gvq4buhfIH4xr4cqLUPw8xw97lzGzFn_dfUs2eNPO_uLM6CPOwzgTwYrWX746RyNGXqKGxdy5Juu9ifVD6qs2iZyoWtMufvwaqUYJHOASfHlT97Cpp6GPPrgPaJdS1tfPrr6OPIHNgO5RpuCvsMuclr-vFE1ZNRDOkD8LODLoL9w9VZUKFAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6cac939191.mp4?token=uH8vL99ZSm0w6VMhPre8ZzQM43PkK9sW1AcTE-yg5Xhb5GQVciyz3pnLYz-58slS6ru_qTkS2pQqocskLg-Jxqlc_d6-ZJxF_3F_AP1H_DNzBj1mZIqR56jp-MAynTKQEAV1xrWn5NUL3HX662hUiSuPggZoIxX_6gvq4buhfIH4xr4cqLUPw8xw97lzGzFn_dfUs2eNPO_uLM6CPOwzgTwYrWX746RyNGXqKGxdy5Juu9ifVD6qs2iZyoWtMufvwaqUYJHOASfHlT97Cpp6GPPrgPaJdS1tfPrr6OPIHNgO5RpuCvsMuclr-vFE1ZNRDOkD8LODLoL9w9VZUKFAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پیام‌ها و تصاویر دریافتی: پرتاب موشک از حوالی لار در استان فارس، دوشنبه ۲۹ تیر حدود ساعت ۱۹'
هم‌زمان: پیام‌های دریافتی از صدور هشدار در بحرین
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77315" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه‌های داخل ایران از پلمب چند کافه و رستوران در مرکز شهر تهران خبر داده‌اند.
براساس این گزارش‌ها جو کافه، ۱۴۰۱، سام‌کافه، دو بار، نووک و تئوری در خیابان‌های سنایی و ایرانشهر پلمب‌ شده‌اند.
وبسایت امتداد نوشت که به هریک از این کافه‌ها دلیل متفاوتی ارائه شده است از جمله «حجاب، داشتن ساندویچ در منو و صندلی در پیاده‌رو».
پلمب کافه‌ها و رستوران‌ها به دلایلی مثل حجاب یا موسیقی زنده سابقه طولانی دارد.
@
VahidHeadline
پیام دریافتی به همراه تصویر یک حکم:
چهارشنبه (چندروز پیش) به ۹ تا کافه داخل اکباتان فاز یک حکم پلمب دادند بدون هیچ توجیهی (فقط گفتن حجاب رعایت نشد) و همه کافه ها رو پلمب کردن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77313" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPoX_pK2CdYVq6AIQ9d0wIEK3f1hqJjkx6Jo8NJeHNozdW4LI6GuwFFpjYPn8xz0yAs_H1nGUyV92QPnS5fvsETI0U-iF24ASepurqJRTTFgQTkvWggcher3LAWPTJyGvrav1FfZfqker-9_MJt8klpa9_zR6o4hLw3VuFZ6lnU3u6fsJgJ56qH0OCqAtYR5fwCSoOeZj-QHtdKluEv4XNn_TsUZMaw_3dGS-zNUzqGqsND2cIKF8vZtoiVi_ag4pawe56EctJp7-9lvC8FajQp6Mlf7NYtzRXKLqy_qvBS6PLE2aIHclZm4tYrsRsl6I4mFH3XHx9mVgHrJb6NacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکندر مومنی»، وزیر کشور جمهوری اسلامی، در راس هیاتی از نمایندگان دستگاه‌های اجرایی، به دعوت همتای پاکستانی خود عازم اسلام‌آباد شد.
رسانه‌های ایران روز دوشنبه ۲۹تیر۱۴۰۵ گزارش دادند که هدف از این سفر، بررسی راه‌های توسعه همکاری‌های دوجانبه میان ایران و پاکستان است. جزییات بیشتری درباره برنامه دیدارها و محورهای مذاکرات وزیر کشور جمهوری اسلامی منتشر نشده است.
سفر مومنی به اسلام‌آباد در حالی انجام می‌شود که وزارت خارجه جمهوری اسلامی ساعاتی پیش دریافت پیشنهادهایی از سوی کشورهای میانجی برای توقف درگیری‌ها را تایید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77312" target="_blank">📅 18:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsoVpL3SpYOu4vXBRwn71tOYQvYmV3vVI1UIqPXGXS1HNjThtUCUN0t-TBCQtCSuTdTXEajRw_2exnSfQBYGgB1_lM4KphgImvAETRXVJ_oFhPfhkK1ZpICoJ4HRFGDKe-peAMsHRHNDhaPTWBDBMXEY0-_CeGDZUI_AugEL9_R3N8QSl3VBTPCTXKjInVcZRFBZIinJ5E5RXI7sZ-xA-EfB_7Ic1nGZ9uPdz_dpxpQ4g37loilCdt_xqL27aihAx8G3-qX5SBMUra5zufbes9j7xLBxRcbHH8WIJDL7G96k2MQG-KvB9p1aPYK6b7Z8dLq2dJQKLHNHqfAXMUgsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، با انتقاد از سیاست‌های آمریکا در منطقه، با انتشار پستی در حساب «ایکس» خود نوشته است که واشینگتن هم‌زمان با ادعای تلاش برای توقف جنگ، به انتقال تجهیزات نظامی جدید به منطقه ادامه می‌دهد.
قالیباف در پیامی که دوشنبه ۲۹تیر۱۴۰۵ منتشر کرده، نوشته است: «آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند.»
رییس مجلس شورای اسلامی همچنین با اشاره به آنچه «آمریکایی‌بازی‌ها» خواند، نوشته است: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. جمهوری اسلامی در شناخت این رفتارها «به مرحله استاد تمامی رسیده و بر همین اساس برای مواجهه با آن آماده شده است.»
قالیباف در پایان نوشته که اقدامات باید موید ادعاها باشد، نه ناقض آن‌ها.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77311" target="_blank">📅 18:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQdPiKxDgclrceQJCOMHyoBaw52EV8w45cK14Pm9dT5og53e90kjp1-xNDl0SthDgDLHitH7wQUSVCo5ftSaxHiiKw76kX_GNKJAxGJz8lTauxwLJcScVYySjYpf2ET0HXlXqiH5GBkRbCa6bsv8vw2aEzhqcNyDF-AaLDrLFbZowIsqMG4lOvolJWHH8Jof9XRo6GpF_v6aIKpHzgMgLWoaJKpf0IbCJNLoTiYlOwM_BZbPajXbjUhdYAdDFSXGsZdsR4-pL2zxiA7QBU8DwC1EBy9WmHTmukC41sSIKPySU5no1pQSiXd4uiJftnjwIlY8PtK1D6EPzqbGHAs5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت کشتیرانی یونانی «دایناکام تنکرز» همزمان با بالا گرفتن درگیری‌ها میان ایران و آمریکا در منطقه اعلام کرد که دو نفتکش تحت مدیریت این شرکت روز دوشنبه هنگام عبور در آب‌های ساحلی عمان، هدف پرتابه‌هایی با منشأ نامشخص قرار گرفتند.
شرکت دایناکام اعلام کرد نفتکش «کاوومیلیز» با پرچم مالت هدف دو پرتابه قرار گرفت که باعث آتش‌سوزی در اتاق موتور آن شد و خدمه را ناچار به ترک کشتی کرد.
این شرکت در بیانیه‌ای گفت: «پس از فعال شدن سامانه اطفای حریق کشتی، ناخدا تصمیم گرفت کشتی را تخلیه کند.»
دایناکام افزود که تمامی خدمه توسط مقام‌های عمانی به سلامت پیدا شده و به ساحل منتقل شدند و این شرکت در تماس نزدیک با همه مقام‌های ذی‌ربط منطقه‌ای قرار دارد.
شرکت بریتانیایی مدیریت ریسک دریایی ونگارد اعلام کرد این حادثه زمانی رخ داد که کشتی در فاصله حدود هشت مایل دریایی در شمال‌غربی کُمزار عمان در حال عبور بود.
سازمان عملیات تجارت دریایی بریتانیا که پیش‌تر گزارش داده بود این کشتی دچار آتش‌سوزی شده است، اعلام کرد هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77310" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PsLf2HyKJl8FMxIjQmuVklKcZ9BT9kwS5U--Crjbunm5At2AGT1yz_pPFbkFmckiHc90MSPDt4pe9KnG-YQHow8WIzhgaYlNLBMruo-BusPGYPSy5Rop40ladYhEyXB3SrFAKcmeUL0qV3HdL-NS2DX3NdKh_AhXwfPvYtgmFWUVNubsj2gedR6SefpOlZOH10mdHhQJivgamcDQC67wnnjGhYup7QyWbLALiJ_IPC2tmJXVk6bTtSB4qZkj3zhFuwUevoGaaASeEkpfpP4DEmO6exYzKGWdSwrNF8IBxirIaUGD47hWcPFBbkgUs7fJm3Rqic3Qzjlc4WxMytkedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X1A_EXbDz4TvptrPISskRsuK62Rn67bpjt4QMU5RyfpPqFYDtgWMCPpH8b_HNMYBskykzTRb1BPm8CtuIZXrHN1g_fpjHgLuW7LAEZ_8Q1iITgC0EW0JbUZ77NahAyGs5ewt3phDlECnlNqdYHd9fsini3QsCglrXyqVdi4lRSAUYjowi1F2s8sj4W1i9wv48fbbIzrB07unRWbAjEyUdH4yoKo7RuIEHa7cXuzNhHqUV9zKXEVGPnkcN--UM0dR54QVBQ5ME3U3q9dEobzQC0KtAJm2CyNenSFUzQex9S1r9vyLZFUIBswQrG9jhEBQ6sn5LrqmKjYXcWT6yZDDtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رویترز به نقل از یک مقام ارشد جمهوری اسلامی گزارش داد که میانجی‌ها پیشنهادی را به جمهوری اسلامی ارائه کرده‌اند که هدف آن کاهش تنش در جنگ با آمریکا است.
بر اساس این گزارش، این پیشنهاد شامل یک آتش‌بس ۱۰ روزه برای یافتن راه‌هایی جهت احیای تفاهم‌نامه میان جمهوری اسلامی و آمریکاست که ماه گذشته حاصل شده بود.
پیشتر سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد که پیشنهادهایی از طریق میانجی‌ها دریافت کرده است. این اظهارات در بحبوحه تنش‌های نظامی میان آمریکا و جمهوری اسلامی مطرح شده است.
اسماعیل بقائی روز دوشنبه در یک نشست خبری بدون ارائه جزئیات افزود: «اصل موضوع که در این روزها ایده‌هایی از سوی برخی میانجی‌ها به جمهوری اسلامی واصل شده، تأیید می‌شود.»
تنش‌های اخیر پس از حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77308" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چند پست بعدی مربوط به ساعت‌های گذشته هستند.</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77307" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
