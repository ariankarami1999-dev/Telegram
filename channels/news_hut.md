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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 157K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 02:18:51</div>
<hr>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZltrDHXVt6guSPd7QYKmGg56E2dhqGI6cW8lQ6gyiIxBHLWhhGYOGOIvQYGCGN7Pzj0Zt_o9H1oSJGoCnWeizOk0hI44f6XdHGFn81TDSS3OTy3LV56GHLATf18h7dMDhaU9sUSmi4Q3j7uFH6wq3OUkrQ-lrWFkd18CMG87gqDC5ETT3PRhUutkqUd_Gn5dUpsBeuapAKsr4I1BC6DpupEbmoA4qQSjBOlqO2UwNOVeeiD2doW-ujLJNNs_o-rd-jVUyiG1FPDJnCm66igbgZtEdmKL9Ujg9laTBxotpRDR7fg5dzbYTjdZhhUVrexmIvPQLTX52-7LBdXr1zoBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiPRp7ryaqGWrhpRK7fDLVkh_9r7GDq0kv1tew2kdYDtpo87cLp5rlRjvZcB7jlLx2UBUeEVY0VovNVOButo_sV4xxeMfrY02SQb6ExmTr7lLjqtbnxDIDvzwq7lXf5eAnbUtGr9DuI_inUyRA5fFk3-zIpY4NakORTbIG1twGIGM5lvytl29Go7O-A8Kb7wpDTEvz7HdLea4XPu0kduMfcOUKK-YUqPAy1I6io4H2rEsfRe31UnIxgp1YTUs38sg2P1FgoBLEPLUDAMVSwcdhIBS82P0fwZJOnRubbP1hjNmetjjPZi8zGsFjGfHLZKx8XWlX-lBGG0-2ST9Klp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpojz-MASnh_LSO_MCb9k2ZsW1loBjVAnrps9r0bwdVZO7jbBzsKTdhcGxxYy_TLGJ3E9tjzRQ2JlMHm4Kv6t6OFWlovmnkZ1_Hcs0mIptektMuSQji2_Fhy8j4Xj4KfUYUBRuW_Yy41DYjetV1WtOWfbx_hpbP5roLDmVL8AJQNMq5DG7BIle8nh_Jv2Np3mTH0tt9EzfOHBzs727CjwBYBPIdLiECk_HU7Ga2bbfTfpUyq_JwqENkZ2hfVSdQU7k97rJ28CtdDqApE12o9oIDo_vTI5XKUuik7ZeQCh7UCTpHDR2O7oyrL7AIRU8gynNPwK-lFuuJ1GmLOkY6TwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAcfFOU97TzYGdOJ_uAYDYX9CohQ_iy7nZ9h66WRxNgsj3wGfBS3osvhprjFYoblEL4TE348_Ly7AtFcYx6Zts4LB68jcyXU6fThLwmalAA6iF7vkAF1QZw-1eeMYTV4tMxUM8wUD3j78N7GXsQEoxumx3UNAIJiVroal8tp-pRrxGDboCG-gEpShGm6K2OgdrrHETAWCZFUH1DRt_e0DZQ10vwXlxCEe-9arYKjroNFiKM3juiwuElRkiNqZMHUNfgrzymtH3Q4K4WG-Qf21iKyz6g6ENBqdnSAud-rwIDWng1mQVEzjQIIJBNEAL84NI4QFNfyGpHeKa0Fn-rg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWByc09QF3GAhxnQSSzdHGoQXEjyGZADwO875qIu-m_G4sCNqZAG9Eev2D_QKB4vsP2QvZfCu97m13-vrh7PB6oGXX2bjNbFjFFn2mFhkoxVsqe1XGHYvYaJtjeg_ils7KdmNUCmA_A19UUajgEOBInI8U6a-imWXKOG7iUlayjsjGuUQQ2pZJ2pYOYNOSThILzDILzNqjkgCkveqkH1FmQHyxXYQT_6-0HdQzIXlf7XcQ7yg2nneQLAxgWUGmOXWB1Lb5-wiiXUVLrmmvuLNop1tR4tPCIm1ATQLRbB_jaQyoWTHu_-Cv8dUEoktJt_7E6wXX_5bPXgmSy2XLLlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YjgDb3wGBCKVwVhhOxE2cPZVmBTWnQP5cDdUvgV3BbHRy3cFHagUsIN0ZJneLi4n4prSph8jrU26xdTyrUqNKussMh15h_5EQTgojJCYPI4XJ9Ns1NfwCbR2jiIAo-yAUbwwJWtkv4FsoFsSdLnoudGwZO610BKxdCBREOohCsDvnaruzSUnlLfhw2mm67kQiLcUHA5F_z8c4-WGfOzRHZ1jdkyV_o8Zt3BDyZfV2Tf4PSYhZIneQh-FQthaO4EukH_eT5c-n-eDMRa14pBk_Sw4_E-nVBLlkIPTMYB24bD1x3Vlii2CRxx4lBhpakmB4SQxR1ro2p5rlBLgc195IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oX2CgFrGOYcaxe5F8XuQmD8WctuPa1yY9fSsTluw7NzyWRyy4EbWQUKlB4RmI2TVxdCw9rgHfhwvDxPcAw4EjOJddY5QznYisMlbPfsy7ZKYCIpRqYaORVbNiXYNIbwZjl4MrCA3u0Xk_Wbk8hQDRtvSoGhr_ZBPg22uv4F-JJwT5-119QLdF2rw-Xenzpgf73_lGrdQ6TpXvLsE23iOEDdBt-L7KHGBh9662CjARzl1DYIw1UXiRr7fblfQHUjYhd1u2tOWvuzQZvrCfWRnntfa8bvLqfIm1HmBSoSJS9GxUOhp_lbyrrrO562g2h8NApgu8fUDhJZ-jp54uiHmjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=rMNsPqceT7KTKAY8FOqCiqH5dKPiIV9j8XcjacerJbdbrVRAp84h59o5pLsJw7kQNdxH1vyy6B638EoiXlJf8wgyJkauVZ3jg8zYVdcsX6gZYtcaKrtEHDI7fl6ihNufl8HLbQ2Se1m7hOLqoLhJyrirHFAzRGPqzD-N1Z3pnpfbW1t0nx7ryrXftB20xqLO59qgxjbko_OPuY5gT5jVfRfcI5tP6LLZNi2oKvy_C-yrj9dSM8va5BNktobSbTBB6Tk45LizwD82tZUoHHVTMzyVwHHHF6hM-YDbdTFg1dws1lYrfl24A7CbhO0uEotCcgqqcE5L5lVMRYXii3jbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=rMNsPqceT7KTKAY8FOqCiqH5dKPiIV9j8XcjacerJbdbrVRAp84h59o5pLsJw7kQNdxH1vyy6B638EoiXlJf8wgyJkauVZ3jg8zYVdcsX6gZYtcaKrtEHDI7fl6ihNufl8HLbQ2Se1m7hOLqoLhJyrirHFAzRGPqzD-N1Z3pnpfbW1t0nx7ryrXftB20xqLO59qgxjbko_OPuY5gT5jVfRfcI5tP6LLZNi2oKvy_C-yrj9dSM8va5BNktobSbTBB6Tk45LizwD82tZUoHHVTMzyVwHHHF6hM-YDbdTFg1dws1lYrfl24A7CbhO0uEotCcgqqcE5L5lVMRYXii3jbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGRf1z3-YZgQ3AhWWx_ygbzvmgoquoM36Vw5xr3PgQmhAxHCqj779wgooZF23jwL8K9l9Yt2TxByoD_RWaLOoGPKaHeePbU3aGUHVCYpDoWHqmxmKa7SrWptY2xCZWtONryhetacG0urSS2Yke7HymYcDDi47kPRtUqpSmmtmuO9keQEvkeqsKhF_ZS2cdeIkzRpTzwRMUu4zIhbpKcZBPf2vavB3k4AuTT8zCbVygvQgMVFuLmOKOYxugoQ2s4LxqEsGP5zChFaAsD6onoKBw_3JWhxagU_hUGTKKDalf9ya8_9j-EYQM8KcPH1hjxeZyBDswYfedx48Sz-N0csug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=aq50obxMCSoSiZK2i_V-iZvezqGnadINaqwVOJhGbpWrFAYPnyD9erjH5SCLeaR17OAKquIPsu2KDKwoxDozo65tlzuqaxpBJ3YtMMrmAxz-eysD0MVS9pYNY31bQfNhfslii3l44jD8yMP6nfR-wZmdwgZP4A3p94Q7ukMmflpRoupuf_EDcHmNHcj7R_K_umn83-IoTjZMfF5F7jyyfHdXlwd5M8PVHuPis6krvWTapVSly4majvLPDo4S0JN4Xke5GgoyPMpirFQouoyL0cLNOHsnrX8eObk1R4bheTzqhXU8nsx1D6tZgopwgz65GZuzwh5X3u1ODWE5UUgclw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=aq50obxMCSoSiZK2i_V-iZvezqGnadINaqwVOJhGbpWrFAYPnyD9erjH5SCLeaR17OAKquIPsu2KDKwoxDozo65tlzuqaxpBJ3YtMMrmAxz-eysD0MVS9pYNY31bQfNhfslii3l44jD8yMP6nfR-wZmdwgZP4A3p94Q7ukMmflpRoupuf_EDcHmNHcj7R_K_umn83-IoTjZMfF5F7jyyfHdXlwd5M8PVHuPis6krvWTapVSly4majvLPDo4S0JN4Xke5GgoyPMpirFQouoyL0cLNOHsnrX8eObk1R4bheTzqhXU8nsx1D6tZgopwgz65GZuzwh5X3u1ODWE5UUgclw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=dMZdMG4ggMCL0gw31jTn2uKlAF8cAbH0krqTSR_uKH-oZ82my8814lz8gLFMwUO1-2KuB-mnLBvL0y2YNH53XQlVJxqnT3NeNGVMhWcdud7vA5J40U4yc2dsTe-pKW_YSFqa6m60uLuj6YQbXr4wjrOr7DNWDAHG4B6nD1D-va1-_1mnyw7SkDmHBIAvRs-p4G9t54oGijGiwenNrNbSg3oFcJYDbGbs5206x-Q42HRxuomRfdPl3xiJBweYPwZCVcxqchxyi5qcpE30xXV5RRdnM_2bUI7uNCJnutmazIRPBYWbgzX6FyOz22UKuCmOfEyeRjkZ280bJ-UBZK8TzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=dMZdMG4ggMCL0gw31jTn2uKlAF8cAbH0krqTSR_uKH-oZ82my8814lz8gLFMwUO1-2KuB-mnLBvL0y2YNH53XQlVJxqnT3NeNGVMhWcdud7vA5J40U4yc2dsTe-pKW_YSFqa6m60uLuj6YQbXr4wjrOr7DNWDAHG4B6nD1D-va1-_1mnyw7SkDmHBIAvRs-p4G9t54oGijGiwenNrNbSg3oFcJYDbGbs5206x-Q42HRxuomRfdPl3xiJBweYPwZCVcxqchxyi5qcpE30xXV5RRdnM_2bUI7uNCJnutmazIRPBYWbgzX6FyOz22UKuCmOfEyeRjkZ280bJ-UBZK8TzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiNI4YFCykBHw-83EzG4UwvEgsW6NIrDWLoBdv6BJCE98PUjIbV0jmeG_hjpEBFcPVfzGdtWj_GxxUqrM-jTXGXGqNdS-zzphoeiNVKZlWh1v4p4963auSc_-33fDh4cG0FQMQRMI_buHCmn0nFyaGZ7RN5PWQ6ewG6R41Z7y_qUXujScRJJ8ai5sD7AalhBuonzLL3_h1RHy-BSalUNGbNJfdmbMFVyaa57kVyNxmoMQVDU5CtoOmTkdKiK8S7bgToLuTwcEncEvWwcxHoXn5GzGBOGLYkXXRhnkY6LKlPkqBkoDRoyQXenyAS04Ag0ud-4urQjK3zADA47n9pQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRzXfrlMIVcLyVaLeNZZBMgaYQdSxEzP7IY8R_JPMd-DoBE-3IgVxIXEchfho_sHIyUGTkJICdCHHyzGIxYoWM8Bv9SeztD9eA8F2zlQbUplL7XGDwv1h-aPyTULDkAmMCAOpGLH8mh9FxNV6aS-wEnCa8OJsVJDRb-X6x5MuOP6v49BGRCyjLC5WAvVzYDbMJsa80JArwONSf-MwfPE0rwYqQjb0YxK3yoKxAi_VENNEFJEm2SUaHY1Rg6TL3uEXCedwHmpPAvFq111v6Yzo1ex6YDAJ3CCKCn1xyRZhqFM1_T5RU13vNpiYAoaIW10DwTBhUrjHkTr04DgRoi1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO0Rj7_WIQUWvQ4Z7DyNnQktYJMiZNQGOsXdUCCkK5jlgL3PrsoWOKkvwCF9-BBFFUxM3EaTgC40CpwuRNTTpbUh9NXdFUmnOUYWtKMPXJj92Px08liq54v6DAhKhAJu7dUSqptiyu3HdgcRRXca2siLqnGxFTd1lApjEiBgsvS14uk-B_6SZm4UAjWNimdWcaFE10Rg1GcPYmMsCKtY9ArJvyz6EXZ7f4R9-ZvbtgcsFO7sI48jpbSEyZiAHYLsQgCFtNLB5NIdpFHribJiboPSPJ7Nh3fTVHHZoz6nI_Widj0RYzstc0JAo5WwZf67wQKP-9ifFfIVB-lLxR0n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=TLyoEU_BhbbLfy8I7DLePuMsljgYaP_qXdXSrzd6NeLgni7XuAODWFYDJ2ZYLBmjtr0eunYSMMiRirwkOufsAB1NAwixd_1TyLFRuLgdNhMvlMW1tjn5bdQ3YtdX8-PolLMhBjIKPYq4Cst5Z6kHequiA5Ol2ubsm4ceDCIhUPAld_T4ousqegHTZefsqQh3vTm9xxN9LtHu76DINIX2wA7r7XxWPLH62suUgvoL_y2bwnZu5asNdvQF4tJ2_Ft4hPYnjxN4UUJ77E1_8idyqn31QJQwqNqs5wne-n59qKEhBIZMEoNzzvJ5N9OswILEPG7gBLu5vn0ago7iVEC_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=TLyoEU_BhbbLfy8I7DLePuMsljgYaP_qXdXSrzd6NeLgni7XuAODWFYDJ2ZYLBmjtr0eunYSMMiRirwkOufsAB1NAwixd_1TyLFRuLgdNhMvlMW1tjn5bdQ3YtdX8-PolLMhBjIKPYq4Cst5Z6kHequiA5Ol2ubsm4ceDCIhUPAld_T4ousqegHTZefsqQh3vTm9xxN9LtHu76DINIX2wA7r7XxWPLH62suUgvoL_y2bwnZu5asNdvQF4tJ2_Ft4hPYnjxN4UUJ77E1_8idyqn31QJQwqNqs5wne-n59qKEhBIZMEoNzzvJ5N9OswILEPG7gBLu5vn0ago7iVEC_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5swn4zV4jderke27EADSc0hnIWduujhKSJct5Prcs0wnUt0O8Ahg53GRB70oSia_YoMeuczI_adntj5LTZbrFSPDohGX2Rla7Y9HGnaStqJm9froCChLv7-xL3qHO6QeLGwIkq6FYTfN8P5FQkEMq46nrdCR7bOXKW6PFkqlcQHw5DqALAI0t1gneBS1MgcuNB0f_MXKYGh-emTUp-DQNm-iP-gg7WkGT6dffzMZjVOUM-rz_CoekjIYReL5fSnK0VgXF2xRWOddr69CY-RzB6UgNkUdBZ_obrOxvAsZBiWYZwQLorzV1g443xfMcgqmnXj9uil9zPZ4OqSkTZsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=opzBpD3TkHJWYZ4n6jTxrjaHW39mz0fXBVXKQug24ui6IgESyRW1wWwESp42xBbxnqbONTl__zAziYSlPU84frX9Yci8QVvBy1Q3iMW-1YUUD4lJ69oZ6YqHMNlTJJbyA4Blg1t8camqXdJWnnH0NqqP7B1h-dKMcfjgDjfWES9-a7WijJLpgHaduwxKiokMmVTx0CSMHf19r-hPdTxKZqUeEZ9DwI9Wfzyrcmk3YuRaMC1ldGf_r8BKEyx0hfP-8KLDuzElOv6ttGN3bzBMuFMV2cAJEazCTtbGqRuYHh0IlHSDr-x62NzrM5jAr_ZsQPHMK72N7AjQqRzUIjWzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=opzBpD3TkHJWYZ4n6jTxrjaHW39mz0fXBVXKQug24ui6IgESyRW1wWwESp42xBbxnqbONTl__zAziYSlPU84frX9Yci8QVvBy1Q3iMW-1YUUD4lJ69oZ6YqHMNlTJJbyA4Blg1t8camqXdJWnnH0NqqP7B1h-dKMcfjgDjfWES9-a7WijJLpgHaduwxKiokMmVTx0CSMHf19r-hPdTxKZqUeEZ9DwI9Wfzyrcmk3YuRaMC1ldGf_r8BKEyx0hfP-8KLDuzElOv6ttGN3bzBMuFMV2cAJEazCTtbGqRuYHh0IlHSDr-x62NzrM5jAr_ZsQPHMK72N7AjQqRzUIjWzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONiJVpW-GW-LOYLnyUAdtz7VAJiHf81TnLLQSEBlhFl43xu_2wLdC3GbjvDRW-t0H8fMptNzD9-RGWimhXxGryCkAgCiZJ2nsgy2tVswBznQ4UjlqXXEUKA7q7y33-L4IbjhhA9agrTOnjORw1bY5c3AUkt9uRhmRe_BHAS1J0CumRyl9IydAW2XDZRTN8jAIVOwTmimXMbNjm4j4cSX2McLGNywHlB2fvFq0g9lx4JeYGn09qiJhj74Pwo8BUlRlriZ-QzJbugTa5d1TASRgwQ5O_nrPa8jyw584k3GkMYWaRwiuCZuJECUHAlbz2E_Doh13t6Fw65-SgGESXSu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVi_QND2zsADdHFfpLB-EA4BCB-7n3-Q5JH78cGjS2iCEmCNARf9xqWF7ewOhEYOdEKQ3wb1iJuHgmQre0-1sMewXvQYD5FXgIRxz_cQAUM51w6oHyblsx0_qDLTPVyD7CKvH8p-jSx6DN_MMcE0INC2Sm3wRJpO4I6RKbAasGkeuezq69cKM80rX-JRbmiXF4tNyc_8p2Nj9ixbWm5MpVohjt1zy9WTvsacc0c8UrAlHNl13K8a0Fc7K9qA-FsVEt23OPl57MIkKHU8P2Yott7QOlGuTbJtPj_NU62HepQD6GwdFw2opLtTc-ztKAGu_xnTaW2TA86t4haJUGjWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW21tcHFtgeqUb2qG_I03OdDueM_v0d0eDooSC4NG4ztT8gDliz118sYB-5srf0CRw5JOpJCBWkzxg-Yyo7kv3HeLVC180H9W1B9O0Hp1w8cLovLb4tj-YsPp2t0pVgy3X9GvPnPFA1ca1t_ZkwXlXOCIrm0WQ8zH7TXq7MUIU2Ss_Rwh7QqdOA3aXwuDdHFekSjmVL2gfLVZT0Ef-bmm7JA7ct0g1Mhquo9sFT51q-vG5Y7wefY6FBfl4on2fFair5c8XlNHQC8-hSFKcwY33ZFbGrhw3CGVIig5os6tuIjY-bvSAfc3EUsJ4G7dsIkHY1jeoNmYHbg-QknGL8YNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rptRd1jPA8ewvP4zeCtqAfWcPN0f0KUDHa0r8FEJv1wSW6IHCXGXbYKNaRLm3hatqzucz6Fevp4YSeYhRvhHywSvaZ5MXfGV32ZUll9qICN5L9EL5_8OfhO6bBL3E-ciyZiMKc2HXE8QTPRX_6RIICiAhrhZ-rsnPrOtR681BtNtgm_y5cHwpY4dPAPDAgg0knibc6XKyczSr1pHOZ-CFkUdGGs-4sIw1fDEXci3oKm7q_nt4rXpWS-9wMxYY1wrQe8C0-MlOg8sIx9q_js8G196elL-C_mYN7kkRVz06odftHLgaESAsMrpfYbXACYNyg55F5g1zLkCz2kvhI_U9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXBOe9HoUl7S9iD6-2VLrRag1-KebBsstXlZz_FZ_vcY4pZEEai-mN9z3N_CQGwqHmxeMzF3omfbKSUXmcLH3ifYN5rnChDSYCXGX-kOkgSBHbW5NOy3ZK6wiDzBb8xPuSyeFxmkvQRDVpdqElF_D5uyiCH2UcYjUm_fO9IUWZfj4u-GvKjmJyyJnQQWAjVrwvAQNHALqMNf2wzfjgTu-2AVATs4VkNxyxsIiNL2w1g9QvhF6H9EUeJHbtYuLep7CedyNOwamvX1k6OhBHFxN6oB_M6AC0Z9xcMtcO_TzfpXaX4DtmH9LMWCFlHk9GtDxE9N7_yjw7pgQAeQxVQDQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MssiY5x3raeKrydzdth-mpgHILvkSzX1T5gtqedCFteQcwilwiqpKJC28SrNfgMcKuH7-t31K8kEvr6S_Ni109aLMpP_6J4qomYni6d5JwOTu34HotJfAYqW23EGXGIClMyROL7EjmQ50f4LPdQxC9NEB0IAFsdm1_4VA8HsQu5K5mif9bbe_YoYi-Az9q19-fysnavJWx9mXujv7cYSdb96fWzePavI8Fm3iw9jBDlwJmB2vHm33CcomL5veElEPibx30ynIJ6FWvKmI10NT3CFyPgHZTE9OgiXgjMWFYh-jQy5L7WLL1p8g_RSqvGVmDDWLpx9lBJvyWDbNpps8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4-bH0-KXXHTt95nweTCJYnA7avKwHPnoD9bjxK6LOWFmFKLi7vqL1CmiglHZvaMww4N3qlkGABa3vXIl1YK-EFyEUqpPe7R_FycU2dkheE6ZC6x5Z2AGFS6bAibP2WkvmVto047CuqwhwKYY7Rnb0uLFkRbyvxxKasO3YuydnD11w4UOhTS0CXR9A5avuP_sAMj-Fey6HIx-kkrFfBeCoDp8ILuDoLNQ9vsTsRLH7ZkYAl2nnrOp0v4Lxx6UVsiTxymT3Xrggz1FyeoQ0NNcvVnNcvkrlIWVQlDOVF2K-zngiTt2oteHiKU_nE4OpADi_f2aZPMfwsepj1QjsBaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aX4aZeI8IKd8xzXN77TNrj-QVQ9V8T_EjwXldF8YPmUm8VJ0o1ZdT2PbElDDjvoCWgn56FPYK7-Hmmxu5xSWXtJgOdvgs6aKbeffrug4gi-AoqpBLdIwc4sCCrAQKGphZN52YcRrQl17fWVq109xBZd-h9DEWwo3zoEN4gblDPckD_ufcEnbjG3zqlgk8ueBuG_bcOheij_v5LX_Uk55LiH0Cw_2j7XrMCtPi31b17cSmORbiBy8_taN0nq7ZhstK1LheyivlGy2xqciQ5RiuHsTR1yCuReUEmCKDXbu6rjAkeP3QV4L2qDc7oVlZLPnUO8RQCmgbLYIMh503HqYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aX4aZeI8IKd8xzXN77TNrj-QVQ9V8T_EjwXldF8YPmUm8VJ0o1ZdT2PbElDDjvoCWgn56FPYK7-Hmmxu5xSWXtJgOdvgs6aKbeffrug4gi-AoqpBLdIwc4sCCrAQKGphZN52YcRrQl17fWVq109xBZd-h9DEWwo3zoEN4gblDPckD_ufcEnbjG3zqlgk8ueBuG_bcOheij_v5LX_Uk55LiH0Cw_2j7XrMCtPi31b17cSmORbiBy8_taN0nq7ZhstK1LheyivlGy2xqciQ5RiuHsTR1yCuReUEmCKDXbu6rjAkeP3QV4L2qDc7oVlZLPnUO8RQCmgbLYIMh503HqYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHfasZ7Fer_cFWwKBY3IRepd_ePE3btlGeScFjWCc8Zqh3SVzRVnrZ2p5lsVl6bqsGf4-maSq_kB4MysXe90nvCuv8rjQeJzdXi9p9_LUWIbn9vCkNK6IEbcUP4hCNTlmwwvZ24c9Jiqu5PVbsptyAPtrWAwGDOVLKcw8Eti2A4T4YBHat8UAYfQkd-SPhl4sYWkrPdXqrCHy0VEs7nUntEqbtOng-ELosgSvTrNiFNQQnFX_Cyz4Abg0BhxeSRITB_nvX1skYJ2xvvWg3FmBLzYFTDKAET6gjxXG-OHBm_LroQdoFsbNOv-m-4BTiZpGAirckX-krrXRfpHV2U-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYnrxBJe8Bpl_PtJR03JKAIQwy-4lBrA_8SyXtRdVRvMhZyfrf_UPFIxyA6-YCzG7eQiIoFyGxBVnnEJ0yWeLNjIOpU_Np8icqhNt5PPBClYruENBxc38uLdNjhflMtYVFjPXqWneXjMbsPuZz8EvWJh6wwfQllDxOn5fqqzjVj0Gs3iMtAv_y-kZvgSu2zRIe6phLnWJNQh5MqBHU-hP1cP5UZzyTxGWelPt7RxcLm_vNyjVSZe0K2ht5MjO4efSSpKJAwqBKUo1wZWsw5Reebk5mtspbxM7E4BIRez4k3dSvAcq95lffPS30rrU2DZe36A2zPesM4FCYfrgSIsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZISkm0uuy8k-V2HyaL38QPa0AJRIOhjWM1csejPKciCjcRvakHYHdZBJSHSh-yX6FH3NY2HzazJgSD6C1YybWJgX98VKI-5fNMPtOSXj-66XzROi5Js_Bn6QH3J49UvCOOtmREbUMIll5czmsTzVwbHAP-sqwqxzr_OKCunoJ5cj2G8Gf0ghejQxN-KsrLVSd_-0S4R_hm__Iidu7zxLbj8ep8x199_IBdLndVWzs7d_uD2EVXShHGwRh70ktzmFEJYbLyUCyf8wwrUUX5fhCGGBcLGCcU3fmKvdZVCMfZXBc_NKuFct7AOMYrkkUE12WzPlhv7KesnK-LNxnBrm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OprYbmBQ-cLQqHWJLnEfq31h7a68CG9DMDaHP7qbSzJgFhAMd4XwR4IP5itxtfMx_5ONlafHRoB4UWdJWG0uQ8zcWH11Oao2oFCBZ4nxmT9-k2nJARB1i8Cr7ossL18KqF-M99AW1_mQUV0OcUGFWq3f1uiqCPlsFilBfolFgExx7-Zz5gyLkHxf4x9xH2lrQSQHXsF7B6ARPAjlC-oVWBaIHbF_4tjL4DJXaujFt5Xrqw40SLxzp65tVoFHD7C1CEKpfJy9OGXSL1oDImxRU-wrmTLMN8tdIHIuBb3m7qXltTwvwCf1ZpZByS3TGevhA9ILfBj8Lcsr82I0pqhqhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu-CSegMEF6RU30E6v21_fhPtedUJz1i6Zuu_1soCmUwKvBcrR5leXjD1cl-n_zj3MEVGyf_LWu1tqdTv7PRSwxMotbxJIwN1ZE3RvkwSgWmjvcRQQF2bu_pnmdy5TLzkqqWCEem-sWAyI6RVSn1EMM_2Y4d9VfwjNq8DOoMjzZoPRSnfwXTiy_bvPDwzPhxWpyR7zRmcbY2Wx6cXB2kXBEIY4kLSasWSwrMbui6xg7F1B0SL7ScNx8nw9N2gF55J1d6Bqr7f5Vgpr__AijY9VA0JY8mlZe1sOcy-ygu_LfPBpr01JgREj5loAGZHg-JizU41TvdUNJK7466piV95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=oDhRXp5sBSBdJcbAdsKr35RPwP_w9vjJzv7kgx0R6vzm6D4-zvgUvu0KTHoINeL30p1gv8uBygS4x56rcsaNFed43M8AG9hxf4gRG3geQovHMQtUD7xiRvdLoP2ydAJG1pVpRaWOrTrvL2qyJCdxVnbJvxgThKQdyuiZSMfD6XfdBksYIE44LJzFDCMewNJ8cMshtBeoNUcXRv8W-Hq6es8n9MfI0yjLEJvLwk_TXdK1rkKxgz49Llg3kadcJ01zN3GuqofK5PEH_GYSPoff8_-_HdvEKmVRQkAlbaVdb9FtIwB3OVWfOY6vsnkLftGX7qDdiEFL-MJCSBZi3xS9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=oDhRXp5sBSBdJcbAdsKr35RPwP_w9vjJzv7kgx0R6vzm6D4-zvgUvu0KTHoINeL30p1gv8uBygS4x56rcsaNFed43M8AG9hxf4gRG3geQovHMQtUD7xiRvdLoP2ydAJG1pVpRaWOrTrvL2qyJCdxVnbJvxgThKQdyuiZSMfD6XfdBksYIE44LJzFDCMewNJ8cMshtBeoNUcXRv8W-Hq6es8n9MfI0yjLEJvLwk_TXdK1rkKxgz49Llg3kadcJ01zN3GuqofK5PEH_GYSPoff8_-_HdvEKmVRQkAlbaVdb9FtIwB3OVWfOY6vsnkLftGX7qDdiEFL-MJCSBZi3xS9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuGHe-D8O22cnkzbkeEFiLVCty06iYl4MgO2ATEIBsnutxIBCgmj4KvMglYgc8eAsnnF9UOX8HTAOGSc1SY7NMZOVyoMURjE8-g6nU2BeTlNJ8zuzoxo1fzyUIe3gHyAB_roPRJ6YJ6bEdX92zONRDewgPVXUGjI2YxdQm0CX--dIhYfCXhmtzrhZRg5T72ENs3ETUuZHDebEBI5RKozTXpqTGtiSykWjkIbocpzwky8fQ0s0bJBGuy9oWSeKLArsAw5tLKp0NZ4PvwJOqt4o11iPI_pj-0ZfKXubMmSpBIWWDk84Ota9NcDe8RHdNVcR07bqUPBJ79oAL2g5poePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpXuRQdyq0ovmZH_EQvzJSinY-2WQHKcXZ7NL-xqaUQbXRyERvJiNv7LzgFLXKZyMndhBIixzB_nJcOsvS8XTjGQoenTsymevehfG9iS-h4Y3nV5CmBvLU2XbiS5jb3QYt2Y5W1YLYX1hXy-qnPxnruJPdPbZyFCm4-FbUguxFZPkZyuMhLddoNvfvLiYFjt4rpEDUyiX7iVK6rXQ3x4p785EFoGZn2G7OQ13ozt9BD99EIqW8TMZrb_l1FsPyC6AnyO9xmCYVBiRiYthSvsQWIOnAzVLo6qB6pEcvrSYUNib9u-oEhQWPOklKvCvp545faC_Ccm8JNuUy-XsqVZEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-AURUV6xez7vArynKC-d9Ta4BUE5gMcTJ1s3x8OMXC0Xsh3oMD3NGXIajLd2B06sieNF6ZzHQ2pd2dCXJAr6U6Wz1rD9FJTGckwJ7COPiYExgpz_jdyOSW1-i_scbE8S1S1hj59BqSq0p5uPtDAm910YyLVFpFSxO4z_Cw_dfcDKaIDf_kaxKw50S0S-Fpz13dUpgkX3c0xD3NXhflPyfS0v2iOoOSQML8qeZ0mECk6hZqpxPAdiICI6FKkbckyN3sY90sbphHvbI88gGbwzRuXNG_mIAPrhAvFvxEimUj8VvyP8DtcCSFKoyqFRv1CIQ4H_OWkpUJelbkbJQcG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFlw1cCaVwRb-qScJVBedxVnYEpk9-IR5W3sEMMnBGljY0q_rn-RL9RLEuJPu1PxflkVjP8YvleRvQS0E_Nn1Heaznjdn4vz2qYNdZeI4B4pS3QB81yxOcTn3Qv8CkwV9BbqijTgWQfk8gV3deDh0WJw9MDg9sDoPpVp244BHYIz8sqQFM7Cy65gGmzYxXkG2TGh5mv0bt08vcnkxUeeRAScQb6hm45NYn9Eem3LXSpNGPZxIbeSWXm3wooQu2jATRdjD6HUQWJhSuGyrzJG_Istr4aPc5xJuhGiNy5AMGHViyQhANWyc5cGsVIZrJg-U6nh2HNqdRiOi3iH3txzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0DbeybaBeaG1Ubdg4I41cW73pJ8Yzt2ll5mo3easHNBYpkt5CtqEbMA6wVZjEuM-b0jvlXafEXn4hTU2aM3zlX8KAUoH4emQcny2vUtxFBPSW_SvtNSo770Mt2UUl9vjfO4f2W_CjyBghk0HQBs2bmnGvAWRhB0A21lM_nLcdAOK2pZRKAAbqgLxatt2WPb8kfpMZp2A0kMzPA-rqu5LpVeOyh1nrcq3nVuJdGQ9nJ-iDSxiDi_EM1F_GnA7rxsE6AGIMuhk9cQX31M0yepaHnYEicw7EVH52Dnvq_EeOHXW0GJHulQM14h-OuIF8sJNLKSsqg6aivh-EUPRzYeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=K5zrbVDj8U9-L2HXrbqQASEIT3GuTs3S5dzFx8aCVlSpc113vojH-IqIDOha-C0D0SV5SgGE5KA9ewZEF94weTgpjpMm_3WsblXzsxwPhvE6yvsh3mJWjZfvU98ACCTOYjreoDgT-ekCZNWDB1sneNL2bM_i1UOgpNPxQVEywylgqDSnU-VpaT6ZDc5MfEOrMGOqAR5f-Kavo9sGp6aDhQyGmVm2Hz_oXhStp2ZhaVVH3Y38NDBtCSwOX3mN0CbdZxEXc8puS_6MP_tQtVAD6g7SfXGOXpEqFPy-Q2K4zgTIdkeoE9OZk5mpogMtwsaRhuSQibfQDKQX60hdstbVJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=K5zrbVDj8U9-L2HXrbqQASEIT3GuTs3S5dzFx8aCVlSpc113vojH-IqIDOha-C0D0SV5SgGE5KA9ewZEF94weTgpjpMm_3WsblXzsxwPhvE6yvsh3mJWjZfvU98ACCTOYjreoDgT-ekCZNWDB1sneNL2bM_i1UOgpNPxQVEywylgqDSnU-VpaT6ZDc5MfEOrMGOqAR5f-Kavo9sGp6aDhQyGmVm2Hz_oXhStp2ZhaVVH3Y38NDBtCSwOX3mN0CbdZxEXc8puS_6MP_tQtVAD6g7SfXGOXpEqFPy-Q2K4zgTIdkeoE9OZk5mpogMtwsaRhuSQibfQDKQX60hdstbVJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7dOQH9xvilXg3RbdplAy-ULrUzAeLStLDus1Yq_9x8osBoO1uXa79xg3U6atjXM64Eq_5DR7X0GdTKoZ6dtGXnPGo9Lx4twLl_7ZtGJQjd-ZEzTYKL2adOvV7F-yXnH3Ms7qyEp72UvT2sYBoWjYXxHgG-WW1tC6nHATrNmT3m0UL1JFJCnqpWqM0LS4seIELZX9PiSZ_Tip1Vo1WSEOwj_Jzq4gAD9T9X8H0xcbZuCsNKhZDx1P_PJ507LKRcP-Yo9yqlTczZdYSG9Xp_Z59WGwXXbGPXR0hAQ6BIzXTolCCQgKTr_qgc3O4kj86S8_qQrogVEJeAEa25zf3cBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqR12p1XCvkUg49SyWyLwWcd5cYm7IybjI6GIy2x0o8V54fYVxzwkm9wg-k0qg06RZNedyR4jQ7rzs-JgawaH4Q86XgNJTru3Ob8CL-LiMbNYJYVkQhdmmab7JZ3tdlN76LMqgGypUORHxL9cliBLbRbEztXKdqOva5ZXJb5WnBMpN6jmY0mAFoy2Ugdl4_aKMLDGGxgXfnQqB-nHIZkMJH5eD0-D7U6fCxyFvBkyL2DakG11XmxbXbI_UxT1M6pJTMAb4Ec_74zBIIgKfCmPxlMnD6xNPD5nU9uvhZzaHgHj5GkM39_Ars3kryaaBhpQqIEDlr2C0n83InZiqMtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=vJQ_Swxzert7Dz9QOYPDTpKKvLVLlulvVryJK1vvrzjOlxWRitS2cTRcOS9qS8eATuStZ28SwVR6y1QpL_yJASVZ2C__5mQR7f-THqSczRmYhvVyW9qH3t3qJLD3cF6Mc6L46_Y1R4Ezzggynrl8celBY9cQwPp__xDybNdVcBZzq2c2bRjRhVeU7tYfeqYw81ke9L-XfJAU95S-sZ4j8hy8sdA2FrXXsL_eEeBkSGoXSTdzacIqg01Kx350gW4NyJPQzZ7rz9ERraNI-u3RHyp8DbbrWd8zyLrpmcWGatXjzFe5fhGMzrQFq5EeqwJRVewnsJT8uglQqoDf84pagA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=vJQ_Swxzert7Dz9QOYPDTpKKvLVLlulvVryJK1vvrzjOlxWRitS2cTRcOS9qS8eATuStZ28SwVR6y1QpL_yJASVZ2C__5mQR7f-THqSczRmYhvVyW9qH3t3qJLD3cF6Mc6L46_Y1R4Ezzggynrl8celBY9cQwPp__xDybNdVcBZzq2c2bRjRhVeU7tYfeqYw81ke9L-XfJAU95S-sZ4j8hy8sdA2FrXXsL_eEeBkSGoXSTdzacIqg01Kx350gW4NyJPQzZ7rz9ERraNI-u3RHyp8DbbrWd8zyLrpmcWGatXjzFe5fhGMzrQFq5EeqwJRVewnsJT8uglQqoDf84pagA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=LhIGqedj0e60IJvwVWJCWgxiD_DvB0RqyQe8fTm8KkN5RRdW9eA7KZ0NhoB4Cv52pXabcuaIuYDCYQeURVUsswgLnWPq_4UdawC65EEv3wbN7a3k7dyXw_xsd3XXa4IxK3ipxDsTfIOBfWtj9AZ-v84PrbWUgoztM1YP6XR0oYI9v6jxxA-v_zhASO35CQXA-FcR14CpKMhHq__0DI409Xl6aKmA8XwswjOnIa8KVNvm1LPau-xMyCG_51Sr6oOb1C6pENxDLFXaUaoH3dNMjzF3R2y61OEDr6LTEsc5WhsshSl8vMDklauFxF_buN4oGZxEr_GTYQ3QfTyP1Cvv8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=LhIGqedj0e60IJvwVWJCWgxiD_DvB0RqyQe8fTm8KkN5RRdW9eA7KZ0NhoB4Cv52pXabcuaIuYDCYQeURVUsswgLnWPq_4UdawC65EEv3wbN7a3k7dyXw_xsd3XXa4IxK3ipxDsTfIOBfWtj9AZ-v84PrbWUgoztM1YP6XR0oYI9v6jxxA-v_zhASO35CQXA-FcR14CpKMhHq__0DI409Xl6aKmA8XwswjOnIa8KVNvm1LPau-xMyCG_51Sr6oOb1C6pENxDLFXaUaoH3dNMjzF3R2y61OEDr6LTEsc5WhsshSl8vMDklauFxF_buN4oGZxEr_GTYQ3QfTyP1Cvv8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=LnFSH917FkWNo9OnS_dr3YK31IW0MmnK2r2AU1_8GJvR-fBucKNTyCuygnUaNq1d57kO5Hswudizv0Dh2BH7K3safarppFuUbdArDdJpWQXWQjL5M_h_PYHsTPQjIYLvDGi5_b3YQYE4iskRsprCC-iafANnoh_aSbkrfzvV4p3lPoYXbaoPr3eTeitkDoQ_HdEgp_M2SG568_mT3lI5q4ATUDjn6ovvzK2H4tSawXRotQSu_o-xGOcesnxHEaOncuWOXb0PBd0KtYXgKLcHuWI4VFQBzuq6yRGJr2f5kT8zk8RGd6svVYGtvRIDKDjhOSPV7k0G7UKggkfsanJGJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=LnFSH917FkWNo9OnS_dr3YK31IW0MmnK2r2AU1_8GJvR-fBucKNTyCuygnUaNq1d57kO5Hswudizv0Dh2BH7K3safarppFuUbdArDdJpWQXWQjL5M_h_PYHsTPQjIYLvDGi5_b3YQYE4iskRsprCC-iafANnoh_aSbkrfzvV4p3lPoYXbaoPr3eTeitkDoQ_HdEgp_M2SG568_mT3lI5q4ATUDjn6ovvzK2H4tSawXRotQSu_o-xGOcesnxHEaOncuWOXb0PBd0KtYXgKLcHuWI4VFQBzuq6yRGJr2f5kT8zk8RGd6svVYGtvRIDKDjhOSPV7k0G7UKggkfsanJGJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGYDxEnjK3s8OU-OxrWWV_F1cvENf_OuARk-gPGq_pDVAZlD_I8Y02UnJhm2K89Ypr2yMNPtOFrtCVsYWotbY4Q44QLUHoUEoKqlxzX-HLGhZbobDUh7rzNyL8uBSxNDtoGzOWY8iuBLIEh8sdK_xLn-ty2cZ3l0IMKWqaWMh1Iw0_Ah936k27_QdaEzC9IeZr8ge6dfSSJsKxDZUeTPgcqhBihU5TncJCpwYNwrv2X-m69pFrSd-tyQtK_aon3GMlnkoKAnHLC5lByDtn96wG5e26doJPUhNhsVNIn9Q54jmB43ywDXyfXmPNh5F1onHkkUqQ5jOy0t0mJvLAAX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bVvpFFU65aoXY50FJmgZbTuHhRd3gMLquvk2cgMGNJi5Ed-iLqtizuZEyXw6ZKFYI-rrI6KW1qGdhUqdbpB81GtTECRRn3Kq6K1AU2vr-k6ZHndnxgX_b9s_W-W3O2oEgENDcB2Wc86bS4zjqsI14AdiIYaUIH3R2NqCo7fzmxT_Dk6j0yBNYoxukD_CgRIOV0IRLXByohY6Xf2Pfd6BwDETd5KNZLwuOKHAuY4MdxV2W_xGipMg-YQgQR-2WiKLXyVejstZg87diYfWvryDPRthUfpguGR-11PBIyPrzyD0whzpQyY__fm4qmxHHNPpmUxqhjboHrZqxH3W0dvPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bVvpFFU65aoXY50FJmgZbTuHhRd3gMLquvk2cgMGNJi5Ed-iLqtizuZEyXw6ZKFYI-rrI6KW1qGdhUqdbpB81GtTECRRn3Kq6K1AU2vr-k6ZHndnxgX_b9s_W-W3O2oEgENDcB2Wc86bS4zjqsI14AdiIYaUIH3R2NqCo7fzmxT_Dk6j0yBNYoxukD_CgRIOV0IRLXByohY6Xf2Pfd6BwDETd5KNZLwuOKHAuY4MdxV2W_xGipMg-YQgQR-2WiKLXyVejstZg87diYfWvryDPRthUfpguGR-11PBIyPrzyD0whzpQyY__fm4qmxHHNPpmUxqhjboHrZqxH3W0dvPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=raWTEUtwXGja09OAB_UYN2mW7z8l6lPShytKfDvHc1NxPdvJVy-adAoz6SQH4fXW213UvZKgRcl52SQK8mjbj7gLF85NN_pTO4unQ3QJcLMEjGy-IEQfqZ6ztNnqA3yxblPK0hfwef_rhXrRdZ3M_URoHNUaEIdy8cnjeZsLRSak-fyNfLco11C6JlETkoES9H__u2tYTcNzd0txPdvHS4MpzvcBzkI4eAsHOx_eqLsYXdWpo0Pefwn7hcIK-kBSMXL5YEi1IkZ742ZxjWlT_3YsPJaPzz0dJMAeH9mQvO0DG7VUgWidfpxB63GUdggpbqptiuQ2VD71Q-IdMnGjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=raWTEUtwXGja09OAB_UYN2mW7z8l6lPShytKfDvHc1NxPdvJVy-adAoz6SQH4fXW213UvZKgRcl52SQK8mjbj7gLF85NN_pTO4unQ3QJcLMEjGy-IEQfqZ6ztNnqA3yxblPK0hfwef_rhXrRdZ3M_URoHNUaEIdy8cnjeZsLRSak-fyNfLco11C6JlETkoES9H__u2tYTcNzd0txPdvHS4MpzvcBzkI4eAsHOx_eqLsYXdWpo0Pefwn7hcIK-kBSMXL5YEi1IkZ742ZxjWlT_3YsPJaPzz0dJMAeH9mQvO0DG7VUgWidfpxB63GUdggpbqptiuQ2VD71Q-IdMnGjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jblJ4tSxCrdqjXVq-7GlkoPFt0CboD5ySQB3FkMYMLAZEOALV7d4Km3kjZSX1Cv1SjAXWo_-khl-SJ1HVAfJpMc_kmwFoB6TvQ0Dzknu_oxOTIxcNskLYZMn5JkPNTE7gHOeTykzojsbG0TPt6MEownYbJDMpui6Z6dUcoOwF3XGAN_rYcvpl0msLevYXyYn9Z3Hu-YGY6V2I6RDpTGXa14qZ0PIR8O6dtsAuQzB5wjLtt9ZPMUusR38K0tc4RnE6i5DK_DDh0P3EkloIbP6zxbqHCl74iJv2knLmouIaBm_8vNBIYVuJwPZtBwAj0lzzG-UrLY8osTTktbdp7NIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=hcXhjysfYb5_en-0_CdaeK2csN25sbBvwwuI3yY87D_LUnJMGx0wpkuZsxL7nqUkdudAOSqPU44H_vdNEoymRESjOoPQ-cFGHwAKVCvvbbVMxQGu__kFs63LaZx44Uty65xtBZjp0xsy2W-8SV2K_dWEbR091ZYEQg-rpp9PRubx2yz8BqGwL3_p6z8LgIJKV3bHTC22zUxvPatSvRQ4OTv2ytcRsDFg9yyb45iZfUavjk6sduf9ClxBATqbVmM2OmvCKX8FzJjrHGwKj8MNqcRomo02u9SL5XzatpTi9XSr8fTt6Mrpua4GL7Zn1RxGXqwcc3pxI9AHm64Yj5xd5iRLljJBtlUDsdC-Gy9SOzL5fWuCf3CzjOJyDJ716Fron0uzoW7445uvA483B0djwZqwU5zRfGbgubCt9XIHMgsHZOHDd4L6vX-k_99BdxKok3judUvQNG2734L2Onkf8y2avEoBUuBsXGAfJQ2ZR82H3xKD0C3WJ6raD8l82gVv93YEHee0XJDROHhuXmD4DX2P7KTjS8AojvuGi5JHgM0wF8w54EDi1X4Uxm5OO97O9KC_hOAwf0lrCamcv-GZ9OeBfGYfj5JS9LL4l3p7C74ORAWIA6825RA8wtcXVnm1q9S-hBoaMjTZ3iEISGrPbKfTZfEP7fMXWCgw0MzSvUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=hcXhjysfYb5_en-0_CdaeK2csN25sbBvwwuI3yY87D_LUnJMGx0wpkuZsxL7nqUkdudAOSqPU44H_vdNEoymRESjOoPQ-cFGHwAKVCvvbbVMxQGu__kFs63LaZx44Uty65xtBZjp0xsy2W-8SV2K_dWEbR091ZYEQg-rpp9PRubx2yz8BqGwL3_p6z8LgIJKV3bHTC22zUxvPatSvRQ4OTv2ytcRsDFg9yyb45iZfUavjk6sduf9ClxBATqbVmM2OmvCKX8FzJjrHGwKj8MNqcRomo02u9SL5XzatpTi9XSr8fTt6Mrpua4GL7Zn1RxGXqwcc3pxI9AHm64Yj5xd5iRLljJBtlUDsdC-Gy9SOzL5fWuCf3CzjOJyDJ716Fron0uzoW7445uvA483B0djwZqwU5zRfGbgubCt9XIHMgsHZOHDd4L6vX-k_99BdxKok3judUvQNG2734L2Onkf8y2avEoBUuBsXGAfJQ2ZR82H3xKD0C3WJ6raD8l82gVv93YEHee0XJDROHhuXmD4DX2P7KTjS8AojvuGi5JHgM0wF8w54EDi1X4Uxm5OO97O9KC_hOAwf0lrCamcv-GZ9OeBfGYfj5JS9LL4l3p7C74ORAWIA6825RA8wtcXVnm1q9S-hBoaMjTZ3iEISGrPbKfTZfEP7fMXWCgw0MzSvUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjI7fwoOuZkQf5bgthdhHXCdYV0MKIFfUSbc0G5ctOo2zvPQ0VVMYVvS51lRdzSGUTZyI0zN79iyoFbiePNOdX9c3x6nUSaSLTPVabEqEXC5QKFkOPwS8ZFGiJIGVbZ5qaWKo1klbZEPiTE60K6n4SmdE1KUMB2kas2JDJmLJ3QQxorQ17ISrvZAF_1KSQAla19czrVlnFPsdYru530Wfi_vq-KgSV_n6VS7b5f6I70D9sSi9KGG2OStVLEOLAccwtsDyXeq5ZPcHRoxzRvs-zs7T61HYvWKlrSpm3-g-l1_BTgtrkcbfp6oylAPIVMCGIEPSRgIs0UUGBtF56kSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgrGjVuUyOYwacYmZs8u2JaP4_xBydpAFK6IazJN61YZSbjlYzU4twKiEZNCu2VbBNtS9ur8vnIElMIoIZZUerB7BreTmvlSMiMSRC_AIi30lfNCdKSjRkkfvNu9u-i4-y9WE8M_cbc5g3WbvyU-PSWqDUy0RKZOmLkqFClZkgIUV4CC8fYGuDSN9oWaCGRYjQWLO-MOnQl2nJBmmlWoF9ixo00Ez345HrEyGbWHUTiIK4eFYIZqqBbr1AUKmV-bwrPZ6WJsDClMQ5CLNrB2-dxHB99nP4ZSrq0f_csLpIFULzSx2kesaYQOsnM9-5TRlICFeLHEhW9-sBR8GvD21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Ck9t8TrPDMw4es6ZOoVZYLErdu_G9BhzXlEpQ_-0iPSP-fA5tlRfGkQgABHkAfZgDVAby7MTFSOQMqjBFxLA91EXMf3-vUCXlPGR4MWJ1oc-8HIWYo7Z-6A12-3VJYBufYL5CyfoT7T4nh8FM2iTCm5YLdclq8aJhbUN72o1jFsHR8h5qiiSsvaMKeGdPi9UzwEHnNO6uJxoAvvBeVsge4zYWbLyWmoMWg71QW_v0k_TjxUF58rqKRVoOktGrU5ODUC93GW_OjS5YShXuE7v5IleFSeIbaZYP43shyma9VyIDJfJ91G_FD5qCuLiJyssvSnPzJh4Qs8Cg5hTJFKBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Ck9t8TrPDMw4es6ZOoVZYLErdu_G9BhzXlEpQ_-0iPSP-fA5tlRfGkQgABHkAfZgDVAby7MTFSOQMqjBFxLA91EXMf3-vUCXlPGR4MWJ1oc-8HIWYo7Z-6A12-3VJYBufYL5CyfoT7T4nh8FM2iTCm5YLdclq8aJhbUN72o1jFsHR8h5qiiSsvaMKeGdPi9UzwEHnNO6uJxoAvvBeVsge4zYWbLyWmoMWg71QW_v0k_TjxUF58rqKRVoOktGrU5ODUC93GW_OjS5YShXuE7v5IleFSeIbaZYP43shyma9VyIDJfJ91G_FD5qCuLiJyssvSnPzJh4Qs8Cg5hTJFKBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foaQwmrrvLlVoInYZX0lF3XaYQJCn9G6IxnYH_VkQfkwQi_TwAvVIqfBnh-qWxzcpkg-Mn4gjLs-oS4J63fuFec-8TSisOANH2j7ZtDOvUXA1LnrUsfqD8sp65Xch1dRubop3j-yiGBEszajweEwm2wNDd-54t7-_8Ob69Y5eCH7FKq2geqOdEP8hiJg3-pZVbt0IUFQw5jC9M-DBTVxhmT7AhymasxRjIQjZt2y9weHZ9RDWaDCJEEQ9Xj2JnP-pxk-jLXKTUXORC9pYXDG7vfFJ-B7CCjfSN2sHBQy5RIqB4IxcMSpEaZ-czzX_8fhnr75NijWq_RserDKa5ln8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=JOlCkmJKlbQKDGIvJ0TL-4Brp6ufxuF36SO2HhFPF_hHpQWAsUXeMOV0T01Ws8OR9itZ5T8f-MdgWPzbjz3wsfRY1gbD-mNN7W6wBgZa7jhbQqkuzAVyHMrpZ1LXcJ_zG09EPumjiAnymRgAxJ6NH9HDUiC3fMiGTCeosBCtM4bqGnkI5dPMhHS5xvjmk29mC6qvU9cf4DYwLymToNCPq-WjfULjAKZXrK_TtPYH_sRhnkbATKCWnv4XnhmV4_M-j3yr13QlXaFrO1y56x_MeJYfEqoGEc1ERqbfBcL-mKiitlLr5CNVR7KKRvqGwfwScOhmPIEIEatkk6bxE3fglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=JOlCkmJKlbQKDGIvJ0TL-4Brp6ufxuF36SO2HhFPF_hHpQWAsUXeMOV0T01Ws8OR9itZ5T8f-MdgWPzbjz3wsfRY1gbD-mNN7W6wBgZa7jhbQqkuzAVyHMrpZ1LXcJ_zG09EPumjiAnymRgAxJ6NH9HDUiC3fMiGTCeosBCtM4bqGnkI5dPMhHS5xvjmk29mC6qvU9cf4DYwLymToNCPq-WjfULjAKZXrK_TtPYH_sRhnkbATKCWnv4XnhmV4_M-j3yr13QlXaFrO1y56x_MeJYfEqoGEc1ERqbfBcL-mKiitlLr5CNVR7KKRvqGwfwScOhmPIEIEatkk6bxE3fglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=TTTreoi2iuOsFtfhvYBZE8BmJI60D-wDkjm2Q_h2tfWxnxD7nOCbMWSKasrBpyRlA-p1aqbXJr09-kozQQvNtbex_vRj-PZJMza7-XtsR9HUlRDPA_TR7VHTC-TzC-3vlBlNQqkc_Qwk5lRnoYPIuY0jzvYHvUZDvQoPeirl9UMEBiLFcmLzJT4r05390oJC4C2ePslHwMnKstCDauCcqV5sQ_SolzgAO9OHCvXJNcOfJibaJh9qYPzIuAIfbaSfImzSxLLepqyf8bVgq0mhvzxmS5t00yPNN6F1Z_BfQf7PqQ3LxzcWR9g9hhqvIOE7lxyCI_36cIGUN3AxRNvK7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=TTTreoi2iuOsFtfhvYBZE8BmJI60D-wDkjm2Q_h2tfWxnxD7nOCbMWSKasrBpyRlA-p1aqbXJr09-kozQQvNtbex_vRj-PZJMza7-XtsR9HUlRDPA_TR7VHTC-TzC-3vlBlNQqkc_Qwk5lRnoYPIuY0jzvYHvUZDvQoPeirl9UMEBiLFcmLzJT4r05390oJC4C2ePslHwMnKstCDauCcqV5sQ_SolzgAO9OHCvXJNcOfJibaJh9qYPzIuAIfbaSfImzSxLLepqyf8bVgq0mhvzxmS5t00yPNN6F1Z_BfQf7PqQ3LxzcWR9g9hhqvIOE7lxyCI_36cIGUN3AxRNvK7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=T7-jLPC_5uwi01lVBD8PTku-lnGtxEGKAibbI8Kxl7d-uG4Uakjbu6Pw30puVWO5pwrLqtEWtVw0rvjlslQkwXvkf3-QnmzBZ-oyAz_HX34qOt9Yz5xF090K0fku4hngDHSEB4uCuJX9R3P4lUD6YPPFO6xTY-qMffnvD-rAt78gr3IC450mqH3w1zOuCUQ5Zc828iL_BbDQ4g35M6fV2A_qoYr7KfjyeitnOsvk5HflqNWuue2l3gouUSEEeOiHvvABoRISkjuD0_trpHE5l7VhOuEsIhIf0lxSACxDsKS8_5Fv4CXDuwJVEFapkSrXeyrgx92H6MbuKm0JI5ekkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=T7-jLPC_5uwi01lVBD8PTku-lnGtxEGKAibbI8Kxl7d-uG4Uakjbu6Pw30puVWO5pwrLqtEWtVw0rvjlslQkwXvkf3-QnmzBZ-oyAz_HX34qOt9Yz5xF090K0fku4hngDHSEB4uCuJX9R3P4lUD6YPPFO6xTY-qMffnvD-rAt78gr3IC450mqH3w1zOuCUQ5Zc828iL_BbDQ4g35M6fV2A_qoYr7KfjyeitnOsvk5HflqNWuue2l3gouUSEEeOiHvvABoRISkjuD0_trpHE5l7VhOuEsIhIf0lxSACxDsKS8_5Fv4CXDuwJVEFapkSrXeyrgx92H6MbuKm0JI5ekkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=LU7174t7ddSScX5blw1Vx6OeY8eNfxiqYVUZ7uSkEcXBTUmYPYsuv7FznxUEgAvm6D9jXxbtxOsXK4lP-Iw6L34v9TCPVdpTH4_3dXCxQEPi3NBZkjhvkjAR2Tz2eg9IZqjWE2BbFhLomnr4wIJMcKeJCHgC19-vEAnathwm56alPEJHh6FiLJPUMZvdwZx3SGREWad83oaT1mziJy5XVhqP60ZrZtEZAIhd7SQdHt8h72cSkqLcdbfsGr_acUUsova4Msbt2Vu4DA_V_rOugy5WC_iX_my3do8UfCW7gB2VwZXEKn6dIBjL54FMAUIipMjwKhVm3-Zq6YlEzV_VdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=LU7174t7ddSScX5blw1Vx6OeY8eNfxiqYVUZ7uSkEcXBTUmYPYsuv7FznxUEgAvm6D9jXxbtxOsXK4lP-Iw6L34v9TCPVdpTH4_3dXCxQEPi3NBZkjhvkjAR2Tz2eg9IZqjWE2BbFhLomnr4wIJMcKeJCHgC19-vEAnathwm56alPEJHh6FiLJPUMZvdwZx3SGREWad83oaT1mziJy5XVhqP60ZrZtEZAIhd7SQdHt8h72cSkqLcdbfsGr_acUUsova4Msbt2Vu4DA_V_rOugy5WC_iX_my3do8UfCW7gB2VwZXEKn6dIBjL54FMAUIipMjwKhVm3-Zq6YlEzV_VdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaOZ--U9ACgI_8PC6LvBOm7ZJpBKHTNNhrMYAbCRTjmkvfQbV2xDfiunEDgaYpX8d7Pre-_4BrbV59mt9y1cKgjoO5Ansoswpx6VJb8hWr66qMT4sN8hsgI3z7IW4HbnEHZmISYtEHjsMx4grl92tM5udGYWWAIop7CzmKbsgcdAG7F0OY2NfTu4yD16bmbDBQFRMvtz9ubPLxPh6NDRPclvtVV9LydVwX0tWKp95ovYP9Xx9vXTZjD9rf3MrC1gOF9FBHOLDnpgI5qt1d6lOZ1nu8EbmVAkNmKIYdgosPvFjeACisDx3qeit1xqAzY-NP-6edlMSgaqmoCx7Riepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=UoLv41QSyGf2sHHB_7ItzMnRQAHACyWa6Lo3OnxBKA0sPyzetYL99F0nbOLk_Dr10R4wNinZB08P4LQprLl0bDcZCYmA-navVyUuG2EkitYmCK0M5xt_PxeAMLe7l6n5CA3anBJBNyKyv-L4HNIHi4x2FmVizXvm5ActQh30CghsnhDDIGUkr8ZeTWuY2ByhJrgEuTCycXEqbozFya-z2UophERIpNa7JgJx6lNgrooYbEZOVG7kCO9_6EodHr5Hbt7sxc7HFXahVQmGbZP4jDK4TVJRqAcDjHGobv1IqpJshatYkTFzcutTXXQvKqPgOF0mx4L8Ikp_l8hMwNFLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=UoLv41QSyGf2sHHB_7ItzMnRQAHACyWa6Lo3OnxBKA0sPyzetYL99F0nbOLk_Dr10R4wNinZB08P4LQprLl0bDcZCYmA-navVyUuG2EkitYmCK0M5xt_PxeAMLe7l6n5CA3anBJBNyKyv-L4HNIHi4x2FmVizXvm5ActQh30CghsnhDDIGUkr8ZeTWuY2ByhJrgEuTCycXEqbozFya-z2UophERIpNa7JgJx6lNgrooYbEZOVG7kCO9_6EodHr5Hbt7sxc7HFXahVQmGbZP4jDK4TVJRqAcDjHGobv1IqpJshatYkTFzcutTXXQvKqPgOF0mx4L8Ikp_l8hMwNFLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8a55kH9nB853TFSU8OSbdHEUq-61Py6I-oVsUZtHbnWrwnxciAZsdVR7rvCe05ARKXxkFVD1yBK0C_vmJJN0jtCYUNS3TUZVD6VbM0NPA8Bt-QHfeZekd4ehdExzhoIoO7q7yoX6YoUli-KJr0vMzlSSz7yfsRVe141NMWXDidzuvvD1RyzsGS0Y0mJpM6JKzClUf6SRMNjpq8UVoLVAJLbLDb9FpBn9kfUGx6cFIdS2H__nChiDKtJwTHj01eBrLfSCOU-gfkVoIgQTgNVZOTDiffMEf5ZwF2e81NCCKVWZvO3jsptjXWBtaORGTYCVYNdH_NVsSsIkAMfDO0sqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=MKJIv-7vUZzuKwCkBE7w3jJLSGH6AQmmWGyI6nfvKFA2042V-H7s8XB3Plr8yo1M2PxpBY4af6QbSHsI0EuyZFa2gpMjt76rIN2q0K94KbO_eq076IzcT2-PwwiBQMBFIULhCL1VDq_V5HNP3b9EGR_8zRcnNMU4FTFTTO0KXu6YVi-p2HU6240P8z17N2xKxX5_8fft0A8pLdtonflXRPYb2yKxLnrRtajBbnRnEaM4wPMdJJuzHgmZyDfO_UEENo_BUxs1rMs3ep0WkORqHanzFY5Hh4uSku_69sK7Z3LTvrsy4NR9UvjDZ4En4JCJIHontGxujzfxwIhFts_0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=MKJIv-7vUZzuKwCkBE7w3jJLSGH6AQmmWGyI6nfvKFA2042V-H7s8XB3Plr8yo1M2PxpBY4af6QbSHsI0EuyZFa2gpMjt76rIN2q0K94KbO_eq076IzcT2-PwwiBQMBFIULhCL1VDq_V5HNP3b9EGR_8zRcnNMU4FTFTTO0KXu6YVi-p2HU6240P8z17N2xKxX5_8fft0A8pLdtonflXRPYb2yKxLnrRtajBbnRnEaM4wPMdJJuzHgmZyDfO_UEENo_BUxs1rMs3ep0WkORqHanzFY5Hh4uSku_69sK7Z3LTvrsy4NR9UvjDZ4En4JCJIHontGxujzfxwIhFts_0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=MuGN5WxLBmhB1KcRCPZxeH61OB9hGPk-EoaI9NDeBLDviJdS4wvN20hvilpdxSDyPJe2pocWEaS_UyL-inyKHcCFO2a5swpLruVj-saguLWXX6X9L5ULKsDbkKUepokr8NQyFplByEkPFZNSQGkQVLDtBZSUkJpGyxHZe_YfxhiJkVAKrasRGd11QIz8U6jVGIoa1LNQA11fat6swDSHqbMznEXne6F1DGjRmpKlZi3b9KUcgTfQW6j9PqC4F3SDia4YPA9RYxlkRlKju0R7YWHFKM6lq5S_dCjmeX1GSPTa-QHHp2d2An0vOee3F9UsFXnMNyvMW0trZf9Em9_hFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=MuGN5WxLBmhB1KcRCPZxeH61OB9hGPk-EoaI9NDeBLDviJdS4wvN20hvilpdxSDyPJe2pocWEaS_UyL-inyKHcCFO2a5swpLruVj-saguLWXX6X9L5ULKsDbkKUepokr8NQyFplByEkPFZNSQGkQVLDtBZSUkJpGyxHZe_YfxhiJkVAKrasRGd11QIz8U6jVGIoa1LNQA11fat6swDSHqbMznEXne6F1DGjRmpKlZi3b9KUcgTfQW6j9PqC4F3SDia4YPA9RYxlkRlKju0R7YWHFKM6lq5S_dCjmeX1GSPTa-QHHp2d2An0vOee3F9UsFXnMNyvMW0trZf9Em9_hFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=S8ihVB__TUy5QU6UxqBk8STKC8P0x_ji23BMY_9xDDL3eEj2y4GqD6idNEL8x1qySAqagEummiYJhkqDXQB6bnoErB16-OXAFPZ7psf9nr_EgtJHnv2HXkLy5FhEwSCK6trW_ichN0Lz8O89loq9X2VSIgsePVGq0cWvIpQknvVpaqxxAh8pCerV_WUSm2hpDtnYENBYGBPQIfLe3TV2UFZgvZaO7n5IZDOkZnwvw37R28YxUGmJ6nnP64b4aaXkXnHMqhbki3HHMsjpcleMKMwnRY4eYVMJdYwBGj87KWKmkjAE2rFYAsdxdSdXH1vCirkjqwzFo1D8haYP-UpKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=S8ihVB__TUy5QU6UxqBk8STKC8P0x_ji23BMY_9xDDL3eEj2y4GqD6idNEL8x1qySAqagEummiYJhkqDXQB6bnoErB16-OXAFPZ7psf9nr_EgtJHnv2HXkLy5FhEwSCK6trW_ichN0Lz8O89loq9X2VSIgsePVGq0cWvIpQknvVpaqxxAh8pCerV_WUSm2hpDtnYENBYGBPQIfLe3TV2UFZgvZaO7n5IZDOkZnwvw37R28YxUGmJ6nnP64b4aaXkXnHMqhbki3HHMsjpcleMKMwnRY4eYVMJdYwBGj87KWKmkjAE2rFYAsdxdSdXH1vCirkjqwzFo1D8haYP-UpKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaTzFaIYOWOAejYJssOLk5f5u-Iut5rbq8ffLu1_oQMCeZN7bV0hW1_I-j9Uw61-QG-xbI8yjnsfbwn5-TAX-1VZ1yWPp82-CM69ml0q_gDJkmcWp_DvZM5joP93t8GKacPfPpiIEKxwbs9LCHPinFFjDEaEHYPotHhownL3yYlJ6CGPIBq3MK2WbF8_PkPIccqQhCwiXi8X9j7s0buM0IhRcksxsT4IfiAeJ3ReOSDt04S2CW6LukBkeRphJN4gDLNY3P_xO5Z8dfiKiPxucZum6mkrMZKA1Id0ehGykEt_9m6eX5-tZ1jyVWPcEEUWQLVCRJHAoc41PBOXmpO3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-j_OSdxAxbD1XME3EPtMezum14JKQpgvTGo_A6wFvJzOD7kChmgmEU4yroCz8LgudkSDXo5_l8egscO7QZQeZyltxMPAJfaDL5NIrZn8m5KpPzaVyLUkbh9S7hmfoQM2tDGzodnfLI1fjJh-MJjCUDyfV-4vlLKaojlktyZ44hkw8Ng_QSSZ-DPo0h5Pu6hwOqx_4i38QRNiMLhbs0tioy7krsipwKhjsijrw80Z3Hdpc3iIVuH4rHtIeHewksej0bFIaiB6b5HYr8QomJ8swlLSa_LCVNyvW_xYWW82HqclgyIFIlkiBf_hTYpeWtTJ_5ZtBRM1XpjGC70MRnXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOG-46FR81PwhT0W-Rv010w9VUJZlnxbzLyF9158qSXMc3DTD8-to-tieVoFBT-D1Xc_i1gsLGI5iLLV2SqnwC7AKnpUGRA9Pt8eSn_7-KnWKsAxXTPPSdD7TdjoohZraTwG2Qy6nE8TINKkCDoqCfow-lPH_QlFROts35BG045c7pOzdBJ9gJtVHNURZ53k3EtOC1KwoatCeJ04aJU7QYhem-4lpQT9SfH-inAWFtH-zE96mXWEU3LB1qUJdCaCymDkh0kg2SJYL7u0UZOmJVQpBk_VCnnCjULTgjm5HRDX4lILSVZljxdaiqowkxJeb4WRbMjbsyXduVQTYT1gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlJNS531xAXiZn4qxAH_gzmWvR7dg2Pim3GK9AcYycATqVPb9s_pwPzQL6wUMrPwpoP_Si_NPdQaaDSriqVlk4vVTtCzUg8GZLOvvATW9jhsSlGpy3Lwgib3cW4Z0TivYIuFZYKMcJ56J_j3HLRQsqALHXgTSVgyi5-mWNO1TgmMtjlxwoGyCc2rQx7SGF0embThL35B39H8YbbxVUg2vfV8kLqbfbPWoDT8lHEPGChKPJ2f2H_uOPCg7h_ekz3a9B5FGnjzb_i5L-cFm01siZ3gnaYojozJRcBMZ4rMpWbBRbMCZ1Y6TllleqxzB89zZNrOnXQtZsrgw7-MBvw6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfZJiUJx3t7dk6p6l1faNjfl65pHnn87SetrpykopLRuRNu_XU78LgmVBwraDmg0EnAtgSyz69qfLUKdAxBeo6Bjt8iBgPVUpndXKYvi_-hMBj4v897o7gwTNAQEC3KZxIZUxyCMDe6wHy5YMqA18qmbKEYnRAXItafcB1g3w_FsxL9mcc-n0Ktq7XTGigqLphdPONbQYLTAUbWneauhBvpAkk3AxNvo83katYoil_YXJOft-xvlSux_ukrZN3qeXaFchV8TrAYHeM9ftNJ8U36vJ2SI0cDPWbDptISI5sGVzXZ2cEcpW9MvMOJUdor10dC8A4GrNil1iv9fvEBdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
