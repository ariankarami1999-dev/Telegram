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
<img src="https://cdn1.telesco.pe/file/tFE7qoswXtxanETtbv3hvymlPewm3I8dWqjkPmSCecj-DFjTxW0O6wYLRvG1sezDMoYsJmzhicf5F9c4cpqhlI135gBHqKOnd8U6XEmrh_AGUKrHNV9TvQmynNI51jqhZAEIuoSxdS3abDByzlVF33AhyXLUiwqu20WVSRS34e7cMcnk7Ff5prV4y6JqXdp4g7-eEbX9SExzmge71HVCKVRp6oDxg1eKW29frDHkcSikVgD4F1hkqNygRIK3B_pJRHYYKJ9ZncV8ncGnlgR1tzulPr3ahEZ6T7xGIACAkS9VoMDhGtYEH4rxKWYe-1tJviFKefiBiYhmQyZ7ZjaUKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
<hr>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t0MzmtkzPL4WzaWjtC1rx9N0mE3jamMhMXDruxCPUZ-tvdzykiPA9ONl0Tj2E-0f5nVatypp5PwUJU05Vykk0g1uLYJgnKnI0rcb4hH7D4xGomQ2qGoEiOkH0F8EW3Vy6F15PzCMvI6cAzHFU3rqpf23HGL7Sr50tlybR6tdlFqhCXnQs7XURJt-uENSH0tjQ2MfGA3vJWaAhORvvFEhAJjNIALepz79x3YZjW3s9KyrESwmiFlJkoiXZ_fISb0zKHLyBi2WnhExO8UfwJgvaWI3iCxWA49j1rlaUu5VYvoIhARAr1lhObXQMVQ5vslKLeKk_U0Z5CF5KsZUYYS5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZSMfVTt_SO4xB0JBVNefFBgAd3mdN5WlyO_PrEkMHGLp6Bq5K7dWjRYr2TqzDZRvtsy27olT4K3Trpk8U_Jb-6wvzGTZGwg9PVv0z-dTnIAKp0Vebh-YlcMBYbtb-0xP4C5BdQ1cZ8dggXLWaNi9Iw-XSStlYs-4vlzyNHs_NqyHbU4i07rv36alzYkz8AML3tsdy2ROV4yeFZg6fNqKhNrLVblk0rXP0pEmjL8u_4PUY87OkTNt_fwP9uGuRJcZhJXYLcWAtpdABy_8OhXMODKUuJ6WdCfVewROoo3XoQkh1s55Ox6TMCxDvLBlW92-Pgazel_Z01b269zDGG9vuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v_i_mTpBDU7l2hXE6Oe8BRO7kb3oV-lyD5AyRkpK8CfsKzWG1KhsvTYp64L2gPw_sbfd1Lp0_B7EbwFWmB4yLCqannJDKI1nvyhXzbGoh2W2jRWSftJ1DSS8Mee_-UTR2YqTvPDThxfPHI5ScctBsKkb-zzefnj9e56QoofevkiN3a09YJymQtjlR-h9PIhT02LTQ-sL6-LW8FyECQTT_1d961z3zCwbxHXvVFzogSTnjT_0d1JMwpoGaVDWAIivyI6aW2tuMaXeFHA3uOHteI03PeNNK8hx04b-r9dZ-zpcL61GKfi5Z9aD1Q6Lh_a5ItMHicUdC0ZpZFzm12yXkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=DDfb2_meooBK-ZTZetBI-9szUBqkGEkgq5DEuydDxJWwBvG9hbEUuaZbOuHiPEQal-PgDn--ssQ5O9tbfXR2qZi2v91LpBHfe00CXXXfMti7UNzEE_J68mu2fIWvQFqp4Bo0P6u1ukNIAQPSggZOWpLo17PDSfK_M0GVjTw0Cq5HOBJe2eWeYd460c5O3WSHVa96WoCO9Wf9Vq0VBa-jnHLP7hGJak595oD2mMQg5hjTvtJ0ydxKsBaEbQf0GN2-UtK8as-hgSvkCBJgzeq9WY8NrolqWQbQXrSRXWG4b0XA3qyY0opDnE3LbjZ7SIHROxqpBk1Nf8UjDSyqw5mCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=DDfb2_meooBK-ZTZetBI-9szUBqkGEkgq5DEuydDxJWwBvG9hbEUuaZbOuHiPEQal-PgDn--ssQ5O9tbfXR2qZi2v91LpBHfe00CXXXfMti7UNzEE_J68mu2fIWvQFqp4Bo0P6u1ukNIAQPSggZOWpLo17PDSfK_M0GVjTw0Cq5HOBJe2eWeYd460c5O3WSHVa96WoCO9Wf9Vq0VBa-jnHLP7hGJak595oD2mMQg5hjTvtJ0ydxKsBaEbQf0GN2-UtK8as-hgSvkCBJgzeq9WY8NrolqWQbQXrSRXWG4b0XA3qyY0opDnE3LbjZ7SIHROxqpBk1Nf8UjDSyqw5mCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
Vahid
خبرگزاری فارس:
فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده و از پیش برنامه‌ریزی شده بود.
پس چرا اعلام نشده بود؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/76929" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODnJRrvChDlHx1MIvu1sxxdrqnaR1n_ip1Xe9J5JQtNz5xqtf9eJzXUMsSRBWJ3fK7gbXei_RayNVKJj0kpU1JZwFVdoPagVPutij7wUf1t7qnvoyU5YLHGfJAcqxrrPWz9Gyl9kQeMMTIvZPOds4nZy6v_hdVeVuGpmR9x7CLe0ypw77-c8J8YmQc18VSn4UqpRi2sV-g2aqfgMNN8J-su3qR3BttasycsgXEbmxF-u79vABB6GOtTShxZzaf7uaROO_XFEBGqg9gsLhr98e2DXeagq1Q9BBeJ8zShyhJjVxAUfKfQEahhR2uy2I_Z6DJ1cwvUkn2iKWT90mf92TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در پاکدشت پارچین
سلام وحید جان
پارچین همین الان صدای یه انفجار شدید ۹:۳۱
صدای وحشتناک قرچک. مغازه لرزید
کل قرچک صدا رو شنیدن
معلوم نیست هیچی
ساعت ۹:۳۰ صدای انفجار شدید سمت پارچین
دودش مشخصه
قیامدشت کلا لرزید
شهرک صنعتی خاوران
شیشه های مغازه لرزید ۹:۳۰
سلام ما خاور شهریم صدای انفجار شدید اومد شیشه ها لرزید
صدای انفجاری محیب از قیامدشت به گوش رسید
به حدی مهیب بود خونه لرزید
سمت شهرری هم لرزید حتی
درود ، عزیز پاکدشت صدای انفجار اومده دقیق ساعت 9:28
سلام ماهم صدای انفجار پاکدشتو حس کردیم از خواب پریدیم و ترسیدیم ولی یک انفجار بود
سلام اقا وحید ما تو قیامدشت چنان حس کردیم که انگار کارخونه خودمون منفجر شد
کل قیامدشت و چهلقز شیشه ها و خونه ها لرزید
سلام وحید جان ،پارچین انفجار شدید بود،ما قیامدشتیم،موجش تا اینجا اومد
سلام قرچک صدای انفجار اومد شیشها لرزید ولی دود دیده نمیشه
سلام ما محله ی ارکیده های پاکدشت زندگی می‌کنیم
و انقد انفجار شدید بود ساختمان ها لرزیدن
سلام پردیس  شنبه ۲۰ تیر حدود ساعت ۹،۳۰ یه صدای بلند اومد
ما پارچین هستیم همین الان صدای انفجار اومد تقریبا ده دقیقه قبل ،الان دودش هم میاد
وحید جان پارچین یه انفجار شد ستون دودش معلوم بود. پشت تپه های پارچین
تموم خونه ها شدید لرزیدن
سلام. نارمک ما صدارو شنیدیم تا قبل پیامها فکر کردیم توهم بوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76928" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YSBvk3z8T6YOjmeG6FA6Etk8wT3WlJlZZnMzYyUZLvOYEzmQru4jMCwlJlPkIJe1LUt1i6Ev5HOmwLlhv109mJPciUQ60z5ueyR88TYR-uy5hBndrgAYFrYGbcAbvw1kBqTGPg0fbHq2eF-QjoF_4WVB9N3nOM0v7o7VUt19Oot04QBijDoNL5iOu4BW7ZFd-1k63apL0AOMYQKY7X0HQZVJflG6fB8udn-0hivSrkszxTbUpbU4XxSQV8sZd63XE7rhKXbL7RLb6UGtWLx607rWniwI1kzRWLZeRF_d-8YE5hL2VQGAgKgGCKG9Ub95zJvBmmGpcFB-dfdU4ddjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر تهران برای ترور من تلاش کند، هزاران موشک دیگر شلیک خواهند شد
ترجمه ماشین:
هزار موشک در حالت آماده شلیک قرار گرفته و جمهوری اسلامی ایران را هدف گرفته‌اند و در صورتی که دولت ایران تهدید خود را ــ که در بسیاری از نقاط جهان اعلام کرده ــ برای ترور یا تلاش برای ترور رئیس‌جمهور مستقر ایالات متحده آمریکا، که در این مورد شخص من هستم، عملی کند، بلافاصله هزاران موشک دیگر نیز به دنبال آن‌ها شلیک خواهند شد!
دستورها از پیش صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است برای مدت یک سال ــ که قابل تمدید است ــ تمام مناطق ایران را به‌طور کامل درهم بکوبد و نابود کند — ستایش از آنِ الله باد!
رئیس‌جمهور دونالد جی. ترامپ
1000 Missiles are Locked and Loaded and aimed at the Islamic Republic of Iran, with thousands of more to immediately follow, should the Iranian Government act on its threat, pronounced in many corners of the Globe, to assassinate, or attempt to assassinate, the sitting President of the United States of America, in this case, ME! Orders have already been given, and the U.S. Military is ready, willing, and able, for a one year period of time, subject to extension, to completely decimate and destroy all areas of Iran - PRAISE BE TO ALLAH! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/76927" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2ZouTBdPTF1W98SGbV2ilxF7LpEK0YG_07vm92ylfLTHm8E1e-R5louvcNOyg4tyMdVZ293jR19OMsPZ-VH7F1ODuWYRcgGVJsrqIuIMbgH9RKZfr7U-jQKk1bO4iR6dFyI6nT5t4w3ZHlA_5wU2ntQqe5gl909k2Ji5DID8zUBkKqw8KsbjrfLalmFoLnUmdrNO9qsRrxp2yI0a5cJzPm6EreZTFBz_xRnWdSHkJn7J3-gb8ay4zcKISHGPH-_qW5-vFHm3bWG4YoyI-hNRUghdgOsBMKylpjme4_byW80-YYoZS7Y52mpSMKuPhvQD5fCpA4x-KUXlgGzOhlEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «سی‌بی‌اس نیوز»، مقامات ارشد آمریکایی روز جمعه فاش کردند که مقامات ایران در پیامی محرمانه به مشاوران دونالد ترامپ اعتراف کرده‌اند که شلیک به کشتی‌های تجاری در تنگه هرمز یک «اشتباه» بوده و این حملات توسط یک جریان «خودسر» از تندروها با هدف تخریب مذاکرات انجام شده است.
با این حال، کاخ سفید این اقدام را نقض صریح آتش‌بس دانسته و خواستار اعتراف علنی تهران به این اشتباه شده است.
براساس این گزارش، تیمی ارشد از سوی ترامپ، شامل جی‌دی ونس، معاون رئیس‌جمهوری، جارد کوشنر، داماد ترامپ، استیو ویتکاف، فرستاده ویژه کاخ سفید و مارکو روبیو، وزیر خارجه، مامور شده‌اند تا گفتگوها را روز شنبه در عمان ادامه دهند. در حالی که واشنگتن انتظار دارد ایران پس از این نشست تعهد خود را به باز بودن کامل تنگه اعلام کند، مقامات آمریکایی هشدار داده‌اند که اگر ایران نتواند به این ساده‌ترین بخش توافق پایبند بماند، امیدی به حل مسائل پیچیده‌تر نظیر تسلیم ذخایر اورانیوم غنی‌شده نخواهد بود و در صورت ادامه اقدامات خصمانه، با پاسخ سخت نظامی و اقتصادی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76926" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f2IMOuuzK40eV65iWNQWb5ACXK7BZQId-91BhLBRCKZaNn2-bkGFeIxp-VuO9d7rXkMHfuSi7ocnCzXKAXVKsWNLRcSv5gNDKpe_ZxjBfkWJR3FkV1DryGWtJbKC0fc9XKqkTpfkzVOQNzpuqudXD5FLjCFUnvqxFyE_PGybUTwTaYcsA58AysuyaH9prFPe-OQM6HzyOToYXNq7J5rIpTnsGXccPZVUuVxYdt1q_P2Ym0-LhoprfoMfDos1IXrL5yVYDLf_1I8p1r0EKjTR3huhLQhU1QuXrdVFSCUDARxRyBqR5DaVV5aKSC6NjAiztFYRnSknMU9znlOeE9kNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از ایران خواسته است ظرف ۲۴ ساعت علناً متعهد شود که شلیک به سوی شناورها در تنگه هرمز را متوقف خواهد کرد
اکسیوس (ترجمه ماشین):
سه مقام ارشد آمریکایی روز جمعه در جلسه‌ای توجیهی با خبرنگاران گفتند ایالات متحده، هم به‌طور مستقیم و هم از طریق میانجی‌های منطقه‌ای، از ایران خواسته است امروز، شنبه، بیانیه‌ای علنی منتشر کند که در آن روشن شود تنگه هرمز باز است و ایران متعهد شود به سوی کشتی‌های تجاری عبوری از این منطقه شلیک نکند.
چرا اهمیت دارد:
ایران با چندین بار شلیک به سوی کشتی‌های تجاری در تنگه هرمز، یادداشت تفاهمی را که سه هفته پیش با ایالات متحده امضا کرده بود، نقض کرد.
این اقدام به چند دور تبادل آتش انجامید و توافق را در معرض فروپاشی قرار داد.
مقامات آمریکایی می‌گویند اگر ایران به چنین تعهد روشن و صریحی پایبند نباشد، این موضوع تردیدهای جدی درباره اجرای یک توافق هسته‌ای ایجاد می‌کند؛ توافقی که بسیار پیچیده‌تر و حساس‌تر است.
محور خبر:
قرار است عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، روز شنبه در مسقط دیدار کنند تا درباره وضعیت تنگه هرمز گفت‌وگو کنند.
عمان در هفته‌های اخیر، حتی پیش از امضای یادداشت تفاهم، با ایالات متحده و متحدانش در خلیج فارس همسو شد و یک مسیر کشتیرانی جنوبی در نزدیکی سواحل خود گشود که کشتی‌ها می‌توانند از طریق آن از تنگه عبور کنند.
ایرانی‌ها که معتقد بودند این اقدام اهرم فشارشان در مذاکرات با ایالات متحده را تضعیف کرده است، خشمگین شدند.
مقامات آمریکایی می‌گویند اعضای تیم مذاکره‌کننده ایران به آن‌ها گفته‌اند عناصر تندرو در داخل حکومت تصمیم گرفتند برای بازگرداندن این اهرم فشار، شلیک به سوی کشتی‌ها را آغاز کنند.
در مواضع علنی، تیم مذاکره‌کننده ایران، فرماندهان سپاه پاسداران انقلاب اسلامی و دیگر مقامات ارشد، همگی موضع واحدی دارند و خواستار کنترل ایران بر تنگه در آینده هستند.
پشت پرده:
یک مقام ارشد آمریکایی مدعی شد که پس از دو روز درگیری در اطراف تنگه در اوایل این هفته، ایرانی‌ها «دوباره به سراغ ما آمدند و خواستار گفت‌وگوهای بیشتری شدند تا برای حل برخی مسائل تلاش کنند.»
این مقام آمریکایی گفت: «آن‌ها به ما گفتند: “گند زدیم. اشتباه کردیم. بیایید به گفت‌وگو ادامه دهیم.”»
به گفته او، در داخل حکومت ایران بر سر اجرای یادداشت تفاهم و مرحله بعدی مذاکرات با دولت ترامپ، جنگ قدرتی در جریان است.
یکی از مقامات ارشد آمریکایی گفت: «افرادی در داخل نظام آن‌ها هستند که می‌خواهند به توافق برسند، اما ما نمی‌توانیم به‌جای آن‌ها تصمیم بگیریم. خودشان باید اوضاع را تحت کنترل بگیرند.»
چه می‌گویند:
مقامات آمریکایی گفتند انتظار دارند ایرانی‌ها پس از نشست روز شنبه در عمان بیانیه‌ای منتشر کنند.
یکی از مقامات ارشد آمریکایی گفت: «ما می‌خواهیم آن‌ها علناً بگویند که شلیک به سوی کشتی‌ها را متوقف خواهند کرد و به‌صراحت یا دست‌کم به‌طور ضمنی بپذیرند که گند زده‌اند.
در حال حاضر روی همین موضوع کار می‌کنیم. انتظار داریم ایرانی‌ها بگویند همه مسیرهای کشتیرانی در تنگه باز خواهند بود و هیچ عوارض عبوری دریافت نخواهد شد.»
یک مقام ارشد آمریکایی دیگر گفت اگر ایرانی‌ها از انجام این کار خودداری کنند، پیامدهای سنگینی در انتظارشان خواهد بود. او گفت: «اگر فردا موضع آن‌ها این نباشد، روز خوبی برایشان نخواهد بود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76925" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UeQk49GnUgNO9jckQ3hdcDNpLdCOW1CGdTwDjnItWphu6Fz8RROaMMfvoJ1hUGtLQdJQQtJvluqKK166e1XYjjyaJRDhxZb86V4en7kxCJfmP6-qiSKcBGRwy3JlXdmchGXxYcGaibEN1VK27z7_tx763wjyangQUiEZAPMyg4glg1-_NWulO8RyYKhhVJGRo40dYafdlDeH86CbsibS5We6xIf5_vm6GW3oJHwGXtJ4o2mcm0OwblGmH4-w4zeItkRjAmqTYleXN9HcqH9FJ8iSILeuGCrzRZtQDIGf5GeMP-q8hg91xBLV9_vT62MrYokuPVtWY0GL3iIYe5xY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در اقدامی که از بی‌اثر شدن تفاهم اخیر میان تهران و واشینگتن حکایت دارد، تحریم‌های تازه‌ای علیه جمهوری اسلامی و شبکه مالی آن وضع کرد. در فهرست تحریم‌های جدید نام علی انصاری، از چهره‌های نزدیک به مجتبی خامنه‌ای و متهم به فساد اقتصادی، دیده می‌شود.
وزارت خزانه‌داری آمریکا جمعه ۱۹ تیر اعلام کرد این تحریم‌ها در واکنش به حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز اعمال شده است.
این وزارتخانه علی انصاری را «تسهیل‌گر مالی» جمهوری اسلامی معرفی کرد و نوشت او بر شبکه‌ای گسترده از دارایی‌های جهانی به سود مجتبی خامنه‌ای و دیگر مقام‌های حکومت نظارت دارد.
بر اساس بیانیه وزارت خزانه‌داری، انصاری با نهادینه کردن اختلاس در ساختار جمهوری اسلامی و انتقال ثروت‌های عمومی به مجموعه‌ای از املاک و دارایی‌های تجاری در خارج از کشور، خود، مقام‌های حکومت و مسئولان ارشد دفتر رهبر جمهوری اسلامی و سپاه پاسداران را ثروتمند کرده است.
وزارت خزانه‌داری آمریکا همچنین شماری از صرافی‌های کلیدی وابسته به حکومت ایران را تحریم کرد؛ نهادهایی که سالانه میلیاردها دلار را به نمایندگی از بانک‌های تحریم‌شده ایران جابه‌جا می‌کنند و با استفاده از شبکه‌ای از شرکت‌های پوششی، فعالیت‌های مالی حکومت را پنهان می‌سازند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از وضع تحریم‌های جدید گفت مجتبی خامنه‌ای «در حالی در انزوا پنهان شده که حکومتش در حال فروپاشی است».
او ادامه داد: «وزارت خزانه‌داری همچنان از همه ابزارهای خود برای جدا کردن او و دیگر مقام‌های ارشد حکومت از نظام مالی جهانی بهره خواهد گرفت. ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76924" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=vjADP2Yun4OdAgzLf4pz-WDOn5MA-o-MoNlUtyIUS5G2qQJP7Rx8ijxUKZPQjZBbTLycAqrSbag7kr8ftDUiV_H-4QB0eXSzLT6Qc0S7KOXGYTap3a5qvW25vkogOVL9LlbWij2jtmQLWzKqDY6a3DjONg5C89-H2JNuIEY9hy02jmO04ml4fSx047dM_MN9IUiTeoS1XzsThmzq2SEhEqmPUFz5fmb1bLzcwyhm5eBKlL30lwtsX45CEfOEganjD8u7em-idmvLH760GwXKU2Ofp23uuOpzveE3GA2aCvY-4P-kqxnGZujeFD6nC0eHKgfECBaaHVz2mrn1XqsP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=vjADP2Yun4OdAgzLf4pz-WDOn5MA-o-MoNlUtyIUS5G2qQJP7Rx8ijxUKZPQjZBbTLycAqrSbag7kr8ftDUiV_H-4QB0eXSzLT6Qc0S7KOXGYTap3a5qvW25vkogOVL9LlbWij2jtmQLWzKqDY6a3DjONg5C89-H2JNuIEY9hy02jmO04ml4fSx047dM_MN9IUiTeoS1XzsThmzq2SEhEqmPUFz5fmb1bLzcwyhm5eBKlL30lwtsX45CEfOEganjD8u7em-idmvLH760GwXKU2Ofp23uuOpzveE3GA2aCvY-4P-kqxnGZujeFD6nC0eHKgfECBaaHVz2mrn1XqsP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رسانه‌های دولتی چین، ‌این کشور برای نخستین بار با موفقیت یک موشک با قابلیت استفاده مجدد را فرود آورد که این امر پیشرفت بزرگی برای برنامه فضایی این کشور محسوب می‌شود.
پیش از این، قابلیت استفاده مجدد موشک‌ها در انحصار شرکت‌های اسپیس‌ایکس ایلان ماسک و بلو اوریجین، متعلق به جف بزوس، بنیانگذار آمازون بود. حالا چین با انجام این آزمایش موفقیت‌آمیز می‌تواند برتری آمریکا در زمینه موشک‌های قابل استفاده مجدد را به چالش بکشد.
شرکت فضایی اسپیس ایکس در دسامبر ۲۰۱۵، برای نخستین بار یک موشک فالکون ۹ قابل استفاده مجدد را فرود آورد و پس از آن در نوامبر ۲۰۲۵، موشک نیو گلن شرکت بلو اوریجین به زمین نشست.
فالکون ۹ حالا حدود ۱۵۰ بار در سال با پیشرانه‌هایی پرتاب می‌شود که قابلیت ده‌ها بار استفاده مجدد را دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76923" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bR72hgIElh89mX2ST2nFoiwagpVqLfASwCdWUR5PFQFjXtQAQj5R0zmHKRRjuky_wg0_LbByOf9hQg2Ve03Qgh996SAPk8MRS1yRIghzHh8y4WTTeXWk56rK0VRMoOO46AZB798Wowvqib7fFzN5InPGqTn2QhShYHoOfW8y1vbtlUBoA0SHXVuREeqTToiu6r6YXuQFk1VkWhyML_ib5GyNbokMmUpfYalyE0Ep9Lss6heHr35E5HpXhyDGgLW4IrCYpRaahWj50OFo1M3CaekkjjT3C7uaFgkiPfYf12tiey7zqqpOKmeqCs9tATg8hNlqZRdsgG37UmhoFymf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=VYNDOYcy9WqcFmoK8SNHbH8fUkgg-rgYfeGcNQw82XoFz20T4I141B_4DRNjhEpFdOH7BYWWw9LzpHvwTBrTkKAdFcrz7dOihslG8nUyl7XZylK6OM9V86t_eOkNNIZOVitN2d0rDiAJQLf7Qe_J_kgu3LUqvdcIl2HGg7YEuidQJIHuDqoFFRVxsE4qWEYs1zdePReny6WKqNxFts-uFg3ADy7W4Qk82IEOStIMpvPMmePwYVnY1yne6zF1GT-X00bmA1hu79AdPbb5hJX-oHDDinwgxP88-zYn3HYsu-tH1XnFpMPegWcoHugTiFcGsJnlt8eWTsgSwOhsCR1lYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=VYNDOYcy9WqcFmoK8SNHbH8fUkgg-rgYfeGcNQw82XoFz20T4I141B_4DRNjhEpFdOH7BYWWw9LzpHvwTBrTkKAdFcrz7dOihslG8nUyl7XZylK6OM9V86t_eOkNNIZOVitN2d0rDiAJQLf7Qe_J_kgu3LUqvdcIl2HGg7YEuidQJIHuDqoFFRVxsE4qWEYs1zdePReny6WKqNxFts-uFg3ADy7W4Qk82IEOStIMpvPMmePwYVnY1yne6zF1GT-X00bmA1hu79AdPbb5hJX-oHDDinwgxP88-zYn3HYsu-tH1XnFpMPegWcoHugTiFcGsJnlt8eWTsgSwOhsCR1lYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست افتخاری برای حذف صدای خود از آلبوم "بدرقه" [بدرقه خامنه‌ای]
علیرضا افتخاری با انتشار ویدئویی علت این درخواست را ضعف فنی اثر عنوان کرد.
این آلبوم با صدای هفت خواننده از جمله محمد معتمدی، پرواز همای و ... به مناسبت تشییع پیکر رهبر جمهوری اسلامی ایران، توسط شهرداری تهران منتشر شده است.
Koronmusic
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76921" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=i7OKXQi-ZG3ASa9koftrPV2-XRre6sZ7x5-KVXbKo-Z4icS9EKd1QwyMS0Cc69JkOQ_-Xn34yRnzPPNTSCPVA0lZXOhmjvqKk0M6icFip2HCZBve8FT_4LkT0sk19ere9u4-nD8qwWOnShuiQA3hCFvgJGLW2OIl7ih-ELbBCU0txbVX6K-8WS47QiUm9kpu10Nt_Ir3IOPfkTmyP8w0Z48EuPCptR60NYMt_SIAc0lvkay38wRVcXnmbhqOXqFDVRAoPGBPl_zyx4DCfPysXyQ_mWXrf_3O_0FV5WRV1dhye4uGBWFSbXFxcTDxmVW797OIybNNSKM0jmUUJRLm5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=i7OKXQi-ZG3ASa9koftrPV2-XRre6sZ7x5-KVXbKo-Z4icS9EKd1QwyMS0Cc69JkOQ_-Xn34yRnzPPNTSCPVA0lZXOhmjvqKk0M6icFip2HCZBve8FT_4LkT0sk19ere9u4-nD8qwWOnShuiQA3hCFvgJGLW2OIl7ih-ELbBCU0txbVX6K-8WS47QiUm9kpu10Nt_Ir3IOPfkTmyP8w0Z48EuPCptR60NYMt_SIAc0lvkay38wRVcXnmbhqOXqFDVRAoPGBPl_zyx4DCfPysXyQ_mWXrf_3O_0FV5WRV1dhye4uGBWFSbXFxcTDxmVW797OIybNNSKM0jmUUJRLm5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">PapiTrumpo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76920" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LswCZPNIzYavuvWkQq15XqsZ2_YLxrtLKE958JgBVrtq8dosZ7h4B6NUY58Uj-S0w8u_9N9fdjdHGhTC1jc_JikGwWX8_pph71bZD-jQqvf5FvBNFS9MiP2LLjgZCZ9rAwutfNj1fXm0nAssS37kl7EOMuyeIYAaD2kf_EqKmQ_k12zAIQ9nj55omyn4KBpxR90M4x1DpgKyCBx6J_O_nghixIoUFnvLVDIHy7HEIkeg5QJsl9ijy01FaMh0ybNg02CAmHoVal3wXDY6Blds03ChDeuMGM6W6VkM8YigAhdO7skbSm0HLVF4yqq4N5-5qYB0uRt-a9z0Onk2lSIOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع آگاه نوشت که دور جدیدی از مذاکرات میان واشینگتن و تهران، احتمالا هفته آینده و شاید در سوئیس برگزار شود.
مقام‌های جمهوری اسلامی تاکنون در این خصوص اظهار نظری نکرده‌اند.
همزمان دونالد ترامپ، رییس‌جمهوری ایالات متحده، در تروث سوشال نوشت که با درخواست تهران برای ادامه مذاکره موافقت کرده اما به آن‌ها گفته آتش‌بس پایان یافته است.
@
VahidOOnLine
خبرگزاری فارس:
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76919" target="_blank">📅 19:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc_svdB_2U3A3--f2kGZVGTMfmM6S3TNVLWVpr8tG92Lcz1nHMjsDTDuqvLZk86rsifT3_1JDS88exLo5iDpGb4dEBZcltMx5bgUQd0YcIzAT-mRN0er0oKE07gxx_PCpZWISqj1WVhHO54e6gBvcLf_2akzq7Omv2mbjrQNIaW3lcbzaqtpiJyZpPbcB-c6FU6PyVypM-a9eoOTD8k_mdRCXtS43xQZl6o_U3uuc4mSyyhFRNNmtfp7oAK127VBzJcY2JX0fkljghqf90hb6vPI1H5GC7jYBVXKf9lK6FAFTV8ODdpupku5oP2fjfOzpwlTYwTmoK2jDs5d9kkcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگویی با «نیویورک‌پست» اعلام کرد که دستورات لازم را برای واکنش به هرگونه تلاش احتمالی ایران برای ترور خود صادر کرده و در صورت وقوع چنین حادثه‌ای، ایران با پاسخی ویرانگر و بی‌سابقه مواجه خواهد شد.
ترامپ اظهار داشت که مدت‌هاست در فهرست ترور تهران قرار دارد و به همین دلیل دستور داده است که اگر اتفاقی برای او بیفتد، ایالات متحده باید ایران را «به سطحی بمباران کند که هرگز پیش از آن ندیده‌اند».
او در پاسخ به گزارش‌های اخیر مبنی بر هشدار اسرائیل درباره طرح ترور جدید، با رد وجود طرحی تازه تاکید کرد که ایران سال‌هاست به دنبال حذف او بوده است. ترامپ گفت: «من از مدت‌ها قبل در صدر فهرست ترور آن‌ها بوده‌ام؛ زندگی همین است. امیدوارم دلتان برایم تنگ شود!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76918" target="_blank">📅 19:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVc2KbkrVkcAYIx8VvjAudOVQIOPZdj-NMjrIgTbUM5vSfjt2K_7JBffispv5AesiBXbFmFI3QHH9vn2FRpKgUVJMAp1bL95uhgG6Diuj9ue-P0sMXni9yDl34Pw89gnHrcOQ-sPxMuXyPEs6PvlmuuXoYE_0WbdO00T_w2LJwEL5TZKNyhn6QmCWHT4AAHzlQMbUrmT3sgpsQJuK0-E_Ck3bSEI8j17v7lqlk0aXQUYgHjh3meRWzjhoYPhWehpRhMGQs_924NKXe69U3OXlWycuB4UKpuI0GbjXEcRcAL5YeA4-E17U-M6UVfwan6G0LpF3OVSxHjHSs92vbyUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه اهواز گفت: فریاد ملت ایران انتقام است و از هرکسی که موشک و پهپاد دارد می‌خواهیم که زمین را از لوث وجود ترامپ پاک کند.
احمدرضا حاجتی  در خطبه‌های نماز جمعه گفت: سایه حکمرانی رهبر شهید همواره هست و آن مشت گره کرده او بر سر آمریکا فرود خواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76917" target="_blank">📅 18:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTnMiIc99CkiOKlkJ5vVsW4QmiV3nztaP0p3eDfBLyDD2OHDbUYjjD6owTB2glP9i21CfYBmQ5dGFBCSVwzA1R5_a49_JrpJ-9EEyqfLUtDDpbbcExIpQfeykaxGM_nT355_oHCatr5g5cgIQMitqVrnKwKZqEOKaa-02mO2HFoJoXfGDPSUP4gbRVJmKlge-0yvjwIZdWc_IF6-DjKdvpkDMnh2s9_Kb75CulrhGqePWVQ0I6yaURCRH3GllRY-8n5MTxFkw4yCBtk3kKu5F5t1DyNDi6eU_1TmcL2NuKK83D0BF8i5_ztcUWP1LuWHIYF6JgHz7HtCUCQ9xf93IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره زیر خاک رفت</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76916" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ds5FDw1JJmqEF4-uW2YyPICAkv92eSSN5QAFtsbwJfE_cB5oXzxi90x0mUQomBiK-Qp809zvF75WLAgPOI7Q9BamtLOqjvxnDtwzD8BT8omKByY9FbCZlItpf7lwOrmrBn_X0tHda95fstTrEzDS1S3dMudkat0fGC_G1SovGG0V3jri9vLPVUrovWGHJJqc7zC3R2_idiMyogezD-ykhR0L7ydaCwZQFE9F_HDpB4zFXRg0vX5RQChlIIhtBPBspYD45LkfBNvktMvvtvE5wsxSMVglMn9kvbKmNPslgBE2lpYu2oViINmOQ3auolp7ujMwkALvOzVFOtm-ctACqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران از ما خواسته است که «مذاکرات» را ادامه دهیم.
ما با این درخواست موافقت کرده‌ایم، اما ایالات متحده به‌صراحت و بدون هیچ ابهامی به آنها اعلام کرده است که آتش‌بس تمام شده است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76915" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aveqdCBTb6vrFo7lGSQDErHHXh5qp6FxPXGlbJvuAtTltOchVwBEat04hSG8R5hwAPU6cywNdzZWzmxJeApJp3Rlks4G1Av3IgV2E_1k7g4HPvIB6HdP_SAMqtHa04s6NZS3JpVeGGBzwpwqxoYj9QC41OaylqEd961pi7W-t3U7TTpZKcydQANR0PZ_DlyP6OSR8Vvcp52wpmtKhON_D5nngJwGY3ZSrs7HPtKtkmzXiQhKeVPYzf4tIU2oi2-Lsm7RkahdhRYUGzhWm1krE9_1P2lw0qptXsU66eE8R5Vi5wH4xQLou-3ZMYr4wRgLncNPjmLa66lK7U4BuEjgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت اکسیوس می‌گوید قطر، پاکستان و چند میانجی منطقه‌ای دیگر از جمله ترکیه، مصر و عربستان سعودی در تلاشند تنش میان آمریکا و ایران را کاهش دهند و مذاکرات هسته‌ای را از فروپاشی نجات دهند.
بر اساس این گزارش، با وجود آن‌که دونالد ترامپ روز ۱۷ تیرماه تفاهم‌نامه و آتش‌بس با ایران را «پایان‌یافته» اعلام کرد و دستور حملات هوایی داد، دولت او همچنان خواهان بازگشایی تنگهٔ هرمز و پرهیز از بازگشت به جنگ تمام‌عیار است.
یک منبع منطقه‌ای گفته میانجی‌ها معتقدند حملات اخیر ایران در تنگهٔ هرمز احتمالاً از سوی عناصری در داخل حکومت ایران انجام شده که با تفاهم‌نامه مخالفند و قصد تضعیف آن را دارند.
اکسیوس می‌نویسد مقام‌های میانجی روز چهارشنبه تماس‌های متعددی با مقام‌های آمریکایی و ایرانی داشته‌اند تا ابتدا بر سر کاهش تنش توافق شود و سپس تاریخی برای دور تازه مذاکرات فنی تعیین شود.
یک مقام آمریکایی نیز پس از نشست ترامپ با تیم امنیت ملی خود گفت دولت آمریکا همچنان به یافتن راه‌حل متعهد است و گفت‌وگوهای فنی برای رسیدن به توافق هسته‌ای ادامه دارد، هرچند واشینگتن حملات ایران به کشتی‌ها را «اقدامات تروریستی» و نقض عملکرد مورد انتظار در تفاهم‌نامه می‌داند.
@
VahidHeadline
خبرگزاری رویترز روز جمعه ۱۹ تیر به نقل از یک منبع آگاه اعلام کرد مذاکره‌کنندگان قطری برای دیدار با مقام‌های جمهوری اسلامی و با هدف کاهش تنش‌ها و فراهم کردن شرایط برای ادامه مذاکرات گسترده‌تر، در ایران به سر می‌برند.
بر اساس این گزارش، گفت‌وگو بین دوحه و تهران «با هماهنگی ایالات متحده» در حال انجام است.
این منبع گفت که هدف این مذاکرات، رسیدگی به اجرای تفاهم‌نامه میان آمریکا و ایران و همچنین موضوعاتی است که موجب تشدید اخیر تنش‌ها میان واشینگتن و تهران شده‌اند؛ از جمله اختلاف‌ها بر سر کشتیرانی در تنگه هرمز.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76914" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fX-VwZCakJE3342nxRHNK3XdhNf3fKqgUiuRhMBA9U-5eJKDgOR5cXmvDcqgaWRSc3m6dC6atuCzMZPMqYJ1xrZH1f2hem65dbnTjEf3YwWFgbez6u5e2KeJR6mhrj5yLSGRpMRIwNZWXL_-shFYLQ6ATmAHg0hXxQlUz15jeQByrBfUfS1ZKbiugmtoCzrJJ5G7ELi9U2uheoFYFfaRyLByUbqS11vMRe9iNA3PYLA7DLeDWS0NiqmA8UQiCQ9v0rLFcxi4oDs5uFKAxz6PWYaa_MBSLRR2yyslC9wdmvN07pOjh35liUONYbQpSPjQCjc14uTAqHTQtsaxUsInSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IzAZ0jUZYVbl6Jw08oOvyFIr8GCBWKFiMTFa3IK5TiMsSAPOVcDahbcR1IHPARXf28xJh2EO1Htekqfr1-SIrGg7x55lw6apIQcA7luNd7Otj-yCzd_wZUyet_uaPDDsoFKLkgh2CzDJjOG8i3HG8mIyMRgnYJAHYnvyMQ2euPWFZuuuAkmXdXc-Sx3uPHtRQz6HMA_zyk7lQ1irFZG7uQ25lpWJUJPqkD7G98qOcnreZXmsLpjo3JyuUkM2_NMTvdDTH90BrqDIzPhqi64s60gnD8fEkc3rqydsk1EBbvxtcsX2Nr6Sl8a5BfxBCRE11ZkER-KsTWLxRL_CiyPY4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش منابع حقوق بشری، نیروهای مرزبانی جمهوری اسلامی ایران با شلیک مستقیم به خودروی یک خانواده در روستای درکی از توابع شهرستان سروآباد، یک کودک ۱۵ ساله را کشتند و پدر او را به شدت مجروح کردند.
به گزارش هه‌نگاو، غروب پنج‌شنبه ۱۸ تیر ۱۴۰۵ (۹ ژوئیه ۲۰۲۶)، نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
هه‌نگاو گزارش داد که در نتیجه این تیراندازی، سام حسنی، کودک ۱۵ ساله، بر اثر اصابت گلوله به سر در دم جان باخت و پدرش، احسن حسنی، از ناحیه ران به شدت مجروح شد. به گفته این نهاد، پیکر سام حسنی به سردخانه بیمارستان بوعلی مریوان منتقل شده و احسن حسنی نیز در همین بیمارستان تحت درمان است.
شبکه حقوق بشر کردستان نیز با تأیید این رویداد از تشدید فضای امنیتی در مناطق مرزی مریوان، پاوه، بانه و سردشت خبر داده و به نقل از منابع محلی نوشته است که نیروهای مرزبانی و سپاه پاسداران در برخی از این مناطق، ضمن افزایش حضور نظامی، محدودیت‌های بیشتری بر رفت‌وآمد روستاییان اعمال کرده و در مواردی از دسترسی ساکنان به باغ‌ها و مراتع شخصی‌شان جلوگیری کرده‌اند.
تیراندازی نیروهای نظامی جمهوری اسلامی به سوی غیرنظامیان، در سال‌های اخیر بارها به کشته و زخمی شدن شهروندان، از جمله کودکان، منجر شده است. کیان پیرفلک، کودک ۹ ساله اهل ایذه، در حالی که شامگاه ۲۵ آبان ۱۴۰۱ همراه با خانواده‌اش در ماشین در حال گذر از خیابانی در این شهر استان خوزستان بود، هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و کشته شد. در این واقعه پدر او میثم پیرفلک نیز به‌شدت زخمی شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76912" target="_blank">📅 17:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HJKF50z73tKSwb9SLYgpTX9Wu0Nr5EQMuaFxG10ZLosnMYLAcJaHhKCWMP_3fLQqsMN8za8yaTVQKgyhHq-xNaNAnpbmUn4xbFaPtqI0p9XEVXLBc-YnI6YSsP-yQlAVFdBZIkszHEURdk7aECISVQJNfAXhHmCk7QrmGQqs5FjTaXgt_SXjzxFMY4vmVsMzhKlWv5vOKynWNRsyRTJb5dnlBTsXSxdgclXCrBKUL5Bhoox170lsZOxmq0QlusFYB0Ecn8u7Bg0e0P13S601duItzRViUJG_RYaOL4otI0LT_mK8Wy7jGBX0KsmEQcUavn3cDI6XL0i7Vlisr3MaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMWL_miGBerqziXSyyHAuzbjTi5aQzFRRVRLXeuSJqtKeCufdD5Xcw7bNOgNIvA16CajNKvbuOrypSrjS1rBiTJ7olMrDQFM6hhtaTEBbtNqDN3rSbERU9oiePnTVPoHcryw7-BW9e69eDqjSx_QjebYZ1gHLmLDbbqUeCGvbk4ruTssOvLeVhCNMe518I-TBGmghscTNPwcIoc5DCscILAM1BrTrhAEBkhqEM61XhiLNAWlv3oiTCeGaCmGzA5vWWmD_iqPGZX_NXPePq4toKMZyEip3rDi5EZ_qK4eNjFbIGXNXsUz_IHOAxJSaGTz1_FJs53ue1zYzJxe-14lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isB01sitYlB0q2DktZ-k54H5t2ZDkc1S6y8Twg3T9NF_zqfvAoDHzy8_JsVmheab3vJF1tp6uzcdvZxfdB9PNdmNvRCODUItj9e3NU5C1B4fCQW8t5LdgBLoDOaG9N87i9OzmJ0B6jvIpUIaXUiT8T1l09vpAjukiMBEY83IylQrC7UaxtdLQrfvGcMnadoVwyoqZCDslPAXGYukN0q2XMxXXXjSkMYaZ7QJrknFtZEqiFNoQHaKVzKrsqWe0EUbo1WwhyzH027qW5EkAzAr8UdDir8u7F8kGnJqzHGeW2X0ai8oBMtu4VjvoyQZp2Pmneer9vWxa2rTZIy22LiUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XTBRbmOXFcXYMwp7XIMv-kh-3RIgsxCIuCAb0OOe7k38R1QwH2xY7gCHAD-099fMBDwF0ROosqqFCsrV9cTRIFCCedtv2l25Qk38r_qSrkjgTDPOFwi-8oZxTOFWZOzVrOqhFds0BWmXDyMCQlZ_7t4gR1K5xjisoKhirZvLGyhMwfhSjaTUSldjiT_p6Zcp9v7HP-MNeedpfR7AYR7YWzrpSBuCATVhgqinx6FTb1nrV9Zz6TQL786hyjGqWTHuWjefZR8x_YkevF2dAzZapQ9QTgqkAENNrgufWA2Vm4c8gLzBZqiXis2c_qA_V7y2fTPcu-r343JKKPLCXDunPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A2ahv1vdtZbIFmVOlUVNutOuI3IHMzFqiti97FIeuc6F89oUO9pFOr03OQGu-yFnfp76VjppfY9AlQhV5O1ufTqezM8yKq_EEbWgqj1VplHbUBmyeLRJGRkADoruWeYXf6xTWCnZiSR8AKU0ssUVzGmYND2lVgvivVxaM1xE7hJl9Ik-CtRtS8A3b-bUe_FxQ-IAZFxxa-NlbPXGpkJ3ICxryqoQPDKH4QHqTYgNUW0ikmXbyEdJYe6mRfUqqENL7aGKloo3qPpmFM7mtsq-qVf7X8UDs34yVfFpyLYmSgAdpkPylTF7mGqvsa5do6iUayvpZZ-42Rt_XJWtExUPFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 488K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvYVhf7TJy1LSX6Cpst-rXpWHCz2Mmt4E982Cq2QqsqH_1qU7lqSnQuaC_IG6iX9o_2gwwfuomOWQ37KJia5s_ETEY18yumnvWIYb46W3OuAKvLwuubCa_EAzfN2hSNknUZA9rD_5RUNOCAkCXL0N7W_zTful3Ztup-8LeXhWcagTcvPMqvHlXlR6Mum6uH-T4OnoGPJ3Mp8B7qkRkvlrhMuai2Bj9SFs-OMbbG1G_plq-JKULkv3422bdwXbNAwIeqNfJ_hMHcS6Ux3dEyGKltkYHmCw32feaasjqkuriyxzr0OHb8CF7yXlKI7Hz_kkxYOz2zqjtPPW4KJj1zZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F46lbebbSfPnGFdu2vRhL9iXsY6Ug8YDEbNsfcPkGoS3DZ_d9eF11WH7VLiouMwHrQG_5f8MqeSni4HDXP0rQfwxBNWYJn4CC463deNTu86RQuq1JCCRseGyRa-2uHTMe5MQZZhis29m-PPgtcNK55I26B0DSscV3Z4KTVcwSE_ugn_wz6hxchDXJewG4_86sMxY6crgwkN6T4YRvO1NcrGtya4seCPP-Sbp6mexDwsUehLHUvp5KtPPkAd8tgBv969Jm-KwAGJq2XHYuq5mxKXscRlcZMiF0_LXb3QdQ91Jr9eHJ23GPLs8xzt0dw6xSMK7VNHvL72bOM8_7XaDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJE2UAc59o0rNiaz-4DASUhjqiE-uVHFP3p7LH-QLTDih5VA9Fmf7OqnOBBu31fyxtmdvbq1Gle6ZWoo5J8WzE0p66ASnPnIBd7yt3QYGVnz4x2dfY9M1cPs5vbNeuhkB2yvAN6xcolpLc6seNDo5HPlcgU8d1jxjtVWaHWfkiQjXOIcxGI2t0CxZfiU8-togimIFezPQvwAZDAUC6dXB-FYpHPM5kTtX1-m27uf_aAr-L768vUeNJe0mR6C9jB5cO6T5w9JY2bLuuZRP59tINI0svEY4VOgP6b8jt897kxNewmymx353FO64kwrGb8yjGCjd327fLCPJfBbo9wpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGOQ9j-nK4bOb_O7UH50Jq26l1-xnDzx3aPDYQg_GjAKPwh7skHgdzx7MZ_T38vkz-Dk2EeRlR2Aq0VuQ-3MlFhCl1Z8KdCKISxY4DINF83UnVbInSC_FvYmDcJ9OL1TP_43cUmswDtsXAYVFwL3bggAFwxXcDn3SzNQv953Nvefl2iG2kpvvBc8rP6LVM53-4wP1CXGjy8GV_BmsQxnrGfT_92i1cFdnGCz3MXLPUFV2D1drKxQ2ySKGZfR1eWiViNjAO1EnBj-6sJqZJI52edy8odeaF4sHprnfVHN30pGfQQpu2IKuezVTZCtKM5ekIQupSMiY55gXGgnLxy7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k0eP9U95nOPwJCvZm081XLw653Lz9w-B4tqzuDzHo6Ebv4SoTl1MhGOXYSLEXP2srTJcaQcRehaJteRdcX9NyhewQf5u9N8tssmp6n0MmLZ_j2pwn62VCeWcrdT2M459BtAb_BgOAgzg-CKcrIlZZZPGcJaLNEXNbuDYQSV46bKpTmyp1l4OStYCaEZBKrpxsc2XwjEPEi5F3KlE2UVlg-Q-QdoBYqnCuKrDkkWt0z0nBNpuWWoQx6o4_tX0MRWnY4W-KxwU7Oh-yeY3TZRUb8LD1y5kXyC47s550T6LJTt1EctmmUyg1J0tdtrcM9m1RfG0mC5kajfd984Z_JrDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFPaechDuf8Z2cRAi_pqMAVLmJBRFR3uFhDjhA_Il16aYvSk8MV-cGgcKLZkg5hd71JAJq-TU3HERTwxrJo00i45H0uCRbRI1BjQ42sv8PJyYuwORGWT3GsDnCjIMikZjhAwkRQOLjY5r0Onc6ObfEySlyyzxe722LG5G40UFuLkZ5IhgNoSOqks6gWi-_GsTCVYMR-dk2N0ft03HoH0mtsw2EhuRyLvEzAykpin8UKp1UYhLczz5pb2MPJ1xyH2N_L29LLR0YXvYZ2TCC7-AaUa1I8IFF7lzvQFd72xOgNzXEMyUvNzfu6SXflW9uZ1kpxn4ligaWxioSTm2vnhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ch35xmWMfzT4IHzKuS9-n7GaJnm2feoHJp_urFeKNlk_GRMabZD5s04nUqiOs1aE2u6Mz2VqeDh0wZw2r19fOqeHhY9VM8Rs_wv_dXSIIQJfBsvXPOLFMzTp4o062MP1qTAbDSIUKMV3dXnw5wFlq5hkm04Oad2GBEnsdFsG5tnjb9xg-461aLyGAc6iB60IhEyhDXA5qQP4evHnYvyyNk5ttyzvvOAsyv4Z8gG-CATKVl0Xt-TWPtdut-4w0upJseCy67fjc46qwHIPpPUPPCOq2GbqX9fhb0yg8SIChmOrHooz65NHyk-yW14KHiLVQJgO6UlVrk-G57ZWfrd7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HlIc_OH2IFju6bGbw-ZxVfDs8amewvaU2JWZQjvEsD7OWFT7di6-Nabj5o1K6SZx5MutbtDgyU1_htiJ0M7DRVqwqk_NE5ABchIMWhTX-YooqLw3z4GP3duhAkRAZkbObN9yNQM1eD3Qf_NAOYkPzhKZjais1palMVu30kXlvwMtSFgOlL7_due8thftQZG-tzQ2TX4-1JpZT3GNZtO-tyIxCzqWrj2MQBwQqWSGjir5l3Z7I9iGxHkgVaKVJZ1PNRrPyRBWG7VB6XzCObvP8eJOVIoV4cY6pWnoSnq9bikctm2A2N8bMdQ0O6UaoUpI3zocGln3SoGgt4VxFsg3zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WLbsLEdHPlibDGGBJarrvVUknUeaXY8D3t7OiYvMMxRjiLbOGsvtS2Jcv_E7tfTNPkRCzc54mKpUQKHTo0R8Dd5O8WZyAEr-Z-g3VQsJ1LHBjZaat--8W7kkYeoYbFAv4iyqFEBZ4kegZ3eBYh52dP6dWQm8D4TMFxgJ_zjMiVfGG-IuDN0mTLO5ZvFEeRVmcMvKRpa_b-gF-yk3TkaG1slim79oAIlZQ4nEM-NYiJ-fwgojAqbaqwQ9VbWA8ZB3UGpYhSuM5RVozCQwzrBB0zyCLouVIEjoCnyh40jTPEasHCJyL-3kk2Y2q2BFOe6k3g18oihjY8bxarECvjrQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OmUmLgB2SeTvfO7sASqZui2UbCNEwxtT_3gfJhX2wfvnkIfhVE9THjNBYn1NnqHIt-SA-v6GkCOhJzogbOAluhii-kwpqPaf7CVv0SkxF46FA8G6B4lXZfyqF8mDe2TvChrie1UdOrljt_oBH6yBzNL8xAjeltPWQMAIXK_RUcPuIdIrffWtJvtB_1wV8Q9cEKkj08aLclr5EYvs9k65Wh_JbG_8WdvTrNM2RYSoI88hap2x5EzyTt1CXZJA0nZMIrj1nPevg4OuN_NdT_8vAab68k7XVTQgBRgGaq-c3-gYMx50u-65_YVyTOcOQmW-utY1HIgVrgekt5oSWvWtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oI9NRcWXijSgC8ILLy5offiUQcmOewnNMHEkLva7xUqenB0Nt8FVp9qdoDAWaqgjlp3cV1xI6BtyHAtZ4EPcr_Y-0lPl9lMdzBQnmPKW7-jehIfkg3trLkSvQ_RqlnMqIkUzkLvvlVLevVUfb3R6DsTtijaim-ZKjk5uqvDah_h5clv97r2Rm_fw46CDaMTbyeshZ4zvPe_QvhUCFenScB8mJjKa2BXg9NbQI89I70XO8xEVoC6G77PM1JWSnk-4hXY3wHgE--tW_Qb9EhLGuCiZYDJqKfvFHGx6-8rW_91XQhALnWOWLFT3l8uw-Je2jC5EuZfcpukXMUi-Yxny0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=o5EdKE1v__mPnu2kFAm1REZxKnDSZmZ0bo3RDZzQgyAuSKfjBr4EZ-mv_WGc8CDdU4ai7rD9OWHA4eSWq5lxOsEgqz16IUvdaZbFD2tWnCf9FSbMP3_Tv5utMCgJj6ESbcp-rDpFUU0ZICRyIVaIN7By6aZKFXvhiBK-VjxtXuk8OfoNvw2eXW28_X_udx9p7bKafQ1pj5ftPBIpQsLYcu1CaOOPaCKzP8O5pC9M7wE61bHygvJoVJYNWdstFZqS7h8T8H2qsji3zIAXDPaCQDSPZ6uQrbQVPOHYZLjpmRDfr5SXgJuLSyF4gWw4Mq4AYDMFeE5RovZo0-KmhSbdaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=o5EdKE1v__mPnu2kFAm1REZxKnDSZmZ0bo3RDZzQgyAuSKfjBr4EZ-mv_WGc8CDdU4ai7rD9OWHA4eSWq5lxOsEgqz16IUvdaZbFD2tWnCf9FSbMP3_Tv5utMCgJj6ESbcp-rDpFUU0ZICRyIVaIN7By6aZKFXvhiBK-VjxtXuk8OfoNvw2eXW28_X_udx9p7bKafQ1pj5ftPBIpQsLYcu1CaOOPaCKzP8O5pC9M7wE61bHygvJoVJYNWdstFZqS7h8T8H2qsji3zIAXDPaCQDSPZ6uQrbQVPOHYZLjpmRDfr5SXgJuLSyF4gWw4Mq4AYDMFeE5RovZo0-KmhSbdaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h65PWLBWhvCOiQufNW1N2M37xnkZSKazGkpMii2Wv18nyczhLQPPVwAb8jRSVBODFM2BjCZBLJ0SoBRhrksF5l-x0Xan8orUKbSweXczeBqPUCAj4eYkLgwquVdzoWBkAoQbWR9DUORrCF5HQeQJqeWCU5tl9pRW8aikAcI0yxdIC3QXbpmRx2jD-2Se_2jJQA8r_L8rnb2mLPB7xCyVoKGrBA1I9xFCsQtPDIpOq4ES6AdR7ySpBihtEQrJ4kv4_61kwvMCxMlIvdodDLH-YWnVIqVBO_ohTv9RtKp0AAdRo_XsYrViSluY5gEKhd5yw5hwYtJzWXHhZSUn25Lp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddcxAojbmstZx8JK9i_gd6zqiqaL_kraP_MIU4QAC4bIOfzeaNioSkR3sQqIC-KZKbF10eNDclcsVwsEqbY0-3m8UjGExoFkls_7bVvyprynDtmIVWUTF0T3X0UaaACYlLHP0_pMpI_iKm2Bgi7TGQAgOZFF2VZPsJi41xJIAfAKH2jwge8SkO0Lsa7JWIBEmIuHlkvhqNqe6_Ya77-ZpKq3B_4__vVlisBCjplfTqEA_g9LRs91BHvIMG56e3trExPlOr3mWIkqmDIPPY3vUM8lQw0M-A16srP8a4xLeMGkVYl4YnO6ooic6Y5951LusYjyhIGLH4CkzeX_OvkU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EP63_ZLkqgfdBx1YRljdWVFaB51v2IGn1Hou3FyXy8IU6PX_ZCBsjK9AK-wFk2NIZu-QMaI6Mtp6oJ0svsag_T7YNqhHDFgSGep8VZpXR3N8_2VzquCqS_hfPnNOIS-IxnHlWexrjxCTb13FrmdhteCwvzqctty39hpuGGGJCJeJeEy6pw3frdg5x9VhoY_Z7yreqD7JWpDLQrB1y3Ho-g6y1buZPKgbApodQhDc50XXPI_C0I996Tn1LLwqT9ujWaCe9kT0WHhTVdlzRWKJMzIP81xdXHJY2jvH8TDOYYRfKmjWxOl2_RZ49Nkfsr-eV0H8OiChV2kWcv1enJ0PTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=mPzwnd_BMPTPE_FVM5Wm5GajZGyBf2KpEqusAE-vRnJ_VO6S3uOOz7KfKM0co-snILvvdC8wYdBmzbHPr1Z745JWHDUccL14O2MKHyvHQTyKPsPizH0oAUEGvE64g3hfeYbZMX4MLiS8EbOQPIkhtMTi2dVyylQlmmLYe19XMSn8joKwV_wmjZYiSUNvqkFqUhfNlo1GIB6Achl7i9sLRwQQLEzWpYYMspEYllrgfOhp3uEgBIu-3CpMQqGZcP2peE3omplTt1XsZhUa7Ex4W8nSRhon9S9jxiOKi6grIA3oplyBerL9XzdYN3SNoD1GQrcxpp0Myzf2qg-4p7vRag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=mPzwnd_BMPTPE_FVM5Wm5GajZGyBf2KpEqusAE-vRnJ_VO6S3uOOz7KfKM0co-snILvvdC8wYdBmzbHPr1Z745JWHDUccL14O2MKHyvHQTyKPsPizH0oAUEGvE64g3hfeYbZMX4MLiS8EbOQPIkhtMTi2dVyylQlmmLYe19XMSn8joKwV_wmjZYiSUNvqkFqUhfNlo1GIB6Achl7i9sLRwQQLEzWpYYMspEYllrgfOhp3uEgBIu-3CpMQqGZcP2peE3omplTt1XsZhUa7Ex4W8nSRhon9S9jxiOKi6grIA3oplyBerL9XzdYN3SNoD1GQrcxpp0Myzf2qg-4p7vRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 505K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=KoL78M97Yv1noxYeMWcmAEnPzEUAnSExxy9MEJ_M-QCNMe--aLNmw7GmGs5QWGdWr1hFfNFm14Gdco9PqAAs4o5jmtg-9LGLKC0FVxmpp5JwiNj3cEFG09PTb5jWmAqSy69cpFasc1n9FitTX1BUdKMDomHdyqQgXLR2WGpc8qGD1VPjEEKiAxNqsULshx7oAziydu3Wz9PQoM_C4GWN4hrKIKlsIquuJlyDgrFbkWtXuyt5BJ9GKgSyrCFRwc9tbBnH5hF6tboHmYklt_Glkc4_PlcOkY56jrw8gYst4nQcLYESOK-ustZmTRD85aRkswC098nYqWBLSk52eUKYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=KoL78M97Yv1noxYeMWcmAEnPzEUAnSExxy9MEJ_M-QCNMe--aLNmw7GmGs5QWGdWr1hFfNFm14Gdco9PqAAs4o5jmtg-9LGLKC0FVxmpp5JwiNj3cEFG09PTb5jWmAqSy69cpFasc1n9FitTX1BUdKMDomHdyqQgXLR2WGpc8qGD1VPjEEKiAxNqsULshx7oAziydu3Wz9PQoM_C4GWN4hrKIKlsIquuJlyDgrFbkWtXuyt5BJ9GKgSyrCFRwc9tbBnH5hF6tboHmYklt_Glkc4_PlcOkY56jrw8gYst4nQcLYESOK-ustZmTRD85aRkswC098nYqWBLSk52eUKYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VzM8ax3yDGvJAQZ7XYci10oyHH6HIy_TkoDMKK90GHoStVGLeyAmaqxm6hKF9qHwpXYRFMMxFRj-3KlddG5ZQSkTzvEnK5bZqfzd0ZKswOKwNl__Iu5zZrqVX4KvVIa91-8ee_5DXDy1ELjNOmjOFbNooz5r3bZiO8jHVXJZLVmQz6t22J6j6Ct4uEC5eOjeOq1zo_Tctz7gQgD0vXzj3XO4If7w5KhMNYPxAHqYF2l8xOi611fk_6Uwf1qoJ6YpnQ8qyFgU_L9F-4XTpwUDNc-9UW4qtzAXDQtAymWYzObS8nIbAg1qymCGgCFNAD2pu2qZZNvDo91HwdulgOb8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hxJ5tkD_kdgtwv6eknlutUXAGjm3stKYD2LTyguObVTpVyFa5SpbnyaOU4yxL7vCuj5JxDoNei1mScyArg5LLYs6U6AkyiTW9pLm5joUzvE_hcfqPjTs_-e4hlmty6cNo6otQa5mNivpyxzij3VWYv3QA8pt27fJZ4E7DLLGq0IEtL165iqKCrVVLvmpUwKFLMa5BEQwKkj-lpfiywTSBhdV-HvyJwmrn_l5uO8QU5rYhwzClZMexGfInZPmqZdOILUYoca9dOJo4M62-ThJjgsmhgpgpTRoU2kpX2XtRw5c3yhtLBqE0HnEgFc52MUMenWCsk1ksK2Iq6V9hkHLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=cxCe_VqjFBM-leXKNcvVsOkZZDCci4DKuP-njzsHK2TRMTUhJ4G2003yHVbLmQ-lmHwMp0FF7ORAliaOeCQhREow73F9HyMYXYjrkmXQNvRkvXKnu7XfXg3mgtuJwyEu2Dg5FkgaOa7Q3W5wIWSPYURdezSMMDTKHsGUccJUxZjYlxCdeswgV1Q4vPfkknSw0OE9_8J9ItclS15j6nO7IKNYtdO_drprGNZjB3ScEkulzOxb3JRBwFxTEPbpgy0Gt4KoSdQWQhYYLlIgN-7sRTeskSktNr4vfS_pbrO1S6OWpySZeI3cW-4f6_qg8W8Kj6Nt6Mqa4IRp5S4Z6Yz-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=cxCe_VqjFBM-leXKNcvVsOkZZDCci4DKuP-njzsHK2TRMTUhJ4G2003yHVbLmQ-lmHwMp0FF7ORAliaOeCQhREow73F9HyMYXYjrkmXQNvRkvXKnu7XfXg3mgtuJwyEu2Dg5FkgaOa7Q3W5wIWSPYURdezSMMDTKHsGUccJUxZjYlxCdeswgV1Q4vPfkknSw0OE9_8J9ItclS15j6nO7IKNYtdO_drprGNZjB3ScEkulzOxb3JRBwFxTEPbpgy0Gt4KoSdQWQhYYLlIgN-7sRTeskSktNr4vfS_pbrO1S6OWpySZeI3cW-4f6_qg8W8Kj6Nt6Mqa4IRp5S4Z6Yz-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=iOwxbtzcYOEQFTgG5H4ENCAE0BwYag14DSIMVMPl3YLzibf9VNOQi-qK-anSXHsnFZuJPcMZWXu8KXTEolmIRMRoSGKL23nUxSpe-FZdnpnTJZCPHutlHSjVYZ1SPXaMHVeH8CmX1jNMOHzGPQ3oPkxm3EpAK7qTpGeONK6xVr3d1cFarkHlHmGnSN3PXXry9b2hkC7_D2bVUM6ysDefMXjyHp0JKXuRjCopPWFZW4RSmVrX0gvQ-Bzhr9g3iVeBuOnrQukC06XXahadDmGEufVEEkj3CxzjHkwHrRleclKf3HCCBIXbfpucgACwC-G3NddLVO-Qzrq5IhkcxwIhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=iOwxbtzcYOEQFTgG5H4ENCAE0BwYag14DSIMVMPl3YLzibf9VNOQi-qK-anSXHsnFZuJPcMZWXu8KXTEolmIRMRoSGKL23nUxSpe-FZdnpnTJZCPHutlHSjVYZ1SPXaMHVeH8CmX1jNMOHzGPQ3oPkxm3EpAK7qTpGeONK6xVr3d1cFarkHlHmGnSN3PXXry9b2hkC7_D2bVUM6ysDefMXjyHp0JKXuRjCopPWFZW4RSmVrX0gvQ-Bzhr9g3iVeBuOnrQukC06XXahadDmGEufVEEkj3CxzjHkwHrRleclKf3HCCBIXbfpucgACwC-G3NddLVO-Qzrq5IhkcxwIhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J0zDaTJORq3GX1imne7YzikxXW8uOGDJOlEkmZvoBhG-_FyLEE8NBzsRM4gEg7tX6To1A-njoE90YJGQzuht60Jvx-uDhAXbvHxHV4nrmmg8ZyKP4EhiVExiWyQyZK0y-osp0gxxT9CMG3PQHwX4kCePRkModVirD27UCD2WUi4eO29WD-R0hoIxknjjWps-kCZ7iFYq2NJbvYKg5v628jq1G1Q9TfrfE9EIIhWM4WLvSa8hIN-ZjQu2-CxzBCDE2JXGzBNCRrt8ShfGW194bmnRiwk8aHo_6NvWwO0LJUnPGxkXo3yjKq_0mlsF_T_FJW3vwqbyQRtIAKivQICGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=RmZf4Gsq6HARa3tpfX2MrT1Q33Zx2MKyEufPITHENDnArWYcyIzJ3NbYAJ_qpI_g5vT-ca60G_HSBtJLf_cnviYd75i73rtK8ppOX4wbX_XUrGKi7sKIRNfluayVBuyDVAIiYRwncqAQKTXnMRUkHnHUWidlTCizLyVXJiMl_UB1gODQ4HZPqe9cN391wcGorrGqFftiKvlTw4gGPhPtBP07Vyw3CmAQ4zcjJnX2WPk8YQfb2pud4Q7EXY5vCBFJ6aLfynqm85iTillQKzUo3G43lLaN3dWi8sl2pvjpmuO6e-nHR4_xDwt3mQE6ISxZvCNF7gRW_nCUce6i32w3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=RmZf4Gsq6HARa3tpfX2MrT1Q33Zx2MKyEufPITHENDnArWYcyIzJ3NbYAJ_qpI_g5vT-ca60G_HSBtJLf_cnviYd75i73rtK8ppOX4wbX_XUrGKi7sKIRNfluayVBuyDVAIiYRwncqAQKTXnMRUkHnHUWidlTCizLyVXJiMl_UB1gODQ4HZPqe9cN391wcGorrGqFftiKvlTw4gGPhPtBP07Vyw3CmAQ4zcjJnX2WPk8YQfb2pud4Q7EXY5vCBFJ6aLfynqm85iTillQKzUo3G43lLaN3dWi8sl2pvjpmuO6e-nHR4_xDwt3mQE6ISxZvCNF7gRW_nCUce6i32w3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/By1v95mhhX6PUm9LVQ5lssu8JFMM6L64sBoDgbRBshh61cryn6nnas11V0gJEw8pHGGkejjtDfwcvH3SQ4GXLWDEwvYX74X0EA8xL6_-ye46qQm6eajcIXtWPcB5fdm9V4slN5SkoxMifbvAzqUZJ5Pn7gqCNPN1ywn-499T5V4vFpMJkZBgtfg8L6iSwPEUJBO9I_8khRI5U94-5pqkw7kuocUexUl173IJC8vbbWCvDCAuHS4wV8hgGeLQc2pMfdPTtkLwOwuIH4SOP7WGBTwB_j2Hioh8GeHKko9Zg40bzLk_RUAPtiMKOGFkPPuG1i38GZmkGpefj4BSeEpKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=uO_WQYJLQkgB4mtEtGtA1RknPMnjj9uCR76sqvGMvKe5ybIWhYzPnL97uQu19cvjy4ZbKDb6jdO-sZVWP2OR29snl42onU9aHdSEwb5xKEPJuR0NJY2c3OJVY45KbvN6dPnUHO9zvrfILVpYcLEbTYZPYHqmH0peGqH3mX83RXD7alRyNJ9NUJkkPz13O_iKsf3ZFM96knAOa6VGB42BkvmHKbLd4BDcFvZqX8uBOjp873DHvA63jlJpUU-L40LjuXVgq2tiU_0vlGNnKHTOrNcbosNNurWQiwhffi1InTVDfdIxs8GZHQfDLBwAFA-l3zNH4V1dyhhUPMbvDDeQDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=uO_WQYJLQkgB4mtEtGtA1RknPMnjj9uCR76sqvGMvKe5ybIWhYzPnL97uQu19cvjy4ZbKDb6jdO-sZVWP2OR29snl42onU9aHdSEwb5xKEPJuR0NJY2c3OJVY45KbvN6dPnUHO9zvrfILVpYcLEbTYZPYHqmH0peGqH3mX83RXD7alRyNJ9NUJkkPz13O_iKsf3ZFM96knAOa6VGB42BkvmHKbLd4BDcFvZqX8uBOjp873DHvA63jlJpUU-L40LjuXVgq2tiU_0vlGNnKHTOrNcbosNNurWQiwhffi1InTVDfdIxs8GZHQfDLBwAFA-l3zNH4V1dyhhUPMbvDDeQDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=Wa1ujEWlsHIT7wumVG7Nq5RlZFB2Li2Ekm_oTzAe3SYKLiB2SZ7T5Z0m59upBR61K9mpxiPPJUvjaRnZL2b5haMrf-r5dqZM3AVQ3DeAI9Cxbf6l_LYKPvp4hDj9ar9qSQyZwB5iuXZCSg23D5gmLoIfemPzRn7Hhg8EDMz0UUtcVZ0OYx9na4A1wqsxKp286RAKuugcZu9fSnKal48bquEin83wzXTf9PltgiFTLydqSg7exXf2BWsHbffJShHvQ9JNb7cD5FjCoFhbRtgc6tzi5L99-jwXOHYE4ZoNclf-uu6PVvZi2T05F7YgG1byqt_zPyxsZd6ldGfs9z34UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=Wa1ujEWlsHIT7wumVG7Nq5RlZFB2Li2Ekm_oTzAe3SYKLiB2SZ7T5Z0m59upBR61K9mpxiPPJUvjaRnZL2b5haMrf-r5dqZM3AVQ3DeAI9Cxbf6l_LYKPvp4hDj9ar9qSQyZwB5iuXZCSg23D5gmLoIfemPzRn7Hhg8EDMz0UUtcVZ0OYx9na4A1wqsxKp286RAKuugcZu9fSnKal48bquEin83wzXTf9PltgiFTLydqSg7exXf2BWsHbffJShHvQ9JNb7cD5FjCoFhbRtgc6tzi5L99-jwXOHYE4ZoNclf-uu6PVvZi2T05F7YgG1byqt_zPyxsZd6ldGfs9z34UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC2RrVMWDlFANfllm4ZbQ-usPePk6qv4sVKRQbEhVFw4sTSle8nhfFfLfTE8oqnVMXNgzyNGr_A2qrknaqEi83Q9g3GewtLTcoVI6KsJOv6woOamXaLPw1CuYVzlGa7efjlv9g9OxL_zPEr11LXWLd4RRGGV1bEjMXUbg0sQAgRy3miQfyxSqPT_S2theGnncxXz8na24rKL3hFsy2qqKJDMmShfkzSxYTntqGDedhwmbWWRy545jnGJNQrkodObz2aOk4KSgWT9O47HDqw7sKDWruO7wS8zgbQPGq33citmuf-ymbDwPnQ-IVokoeQAXiSaI-zKVIGDW-jrADJ-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EklFfYlQNDDAxdq-RjXQ2XmmJ5hMpjreHEU_zURGhcemEGArlBgxDUwYvvH9XNj9wMzGNXjZsznOf9qSCIolT887FXFyqYggL5Ss9XlksruP-hk9UV9YyS4scTXoW2qaEv0WYcOPqsCfV9gDuyfyfLlSJkIaxER5xBp-9lb9a7JN4Aj1XGavKSlGP5sw4dZ9q45VRO7sOl0VZACb6Jfj_ZvyOinnp9GHCD8vI86Q7nyg33JZUZa64H7rVJ1hrs4xq-drDSoF6MOGYsrhMCnvtd5shtXo7GHFyktHYUcpuRSzJ2VYpNBv7Fl1fwxxgaCIvFMbAgP_KRS-qnMjuc410w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KLjy4fTMmr_-2AFMyVeu0OqzA_hfz4JxwdxZwP6AmKeGEDy5fbLl58IThNMLrp6x6D17lZqDyzWoXbhjuP8fwfr7WPtiwy-dyNWjr-ecT1TmHtXzHGyCKU4dJXpPnmqwUT4cgQBZrAQOQCIOcT8iodA7XeEZTKnBaXNIDYQPT4PFCeTbnS-1fm6ldSdfqypbao4XFFXKlAPRKG80UOj_TJVZnTEOxWAIZ56U6TAOzNxdxqTPezfYOor6KRheTll4HJwIrc3WoWJp890MdEkAgpUdQB3a6hEOp0pv3Wal8zVRSCv3yCTVujZT6NMBLIiWq-MPMaOpWX6ywQ8u0OUp-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=BN3u3-qjspvuhN3Ik8mppKGLr6NkGYt5tts3c0sivldp_oRqr3fI8YjSmHehCCRlJsoYpYVDuTK9OcBqwth8cM7wWjCQACowYjXYJmG7zgHDUHr5-fZQuLr6PDPU2c1NKO4RFcA47H2_0XpQBWfEupb0Vux0Y38QqC3g8zyVZa4aGgha9lIWXB4VXrR_raiG2J_cLpTI49WT0-HhuJq_Yte5EBhBohHmDmi55K9yvdGXTwjbhUSup2NICR2oEhP7Y9GYcHqKf9lk6UQA6AruWLMfA6-qzKayXkQwxFas_DM-QHStWkdb-7AJI0B2Xcz5IBUHKrhXf_HL2vpqoaOLyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=BN3u3-qjspvuhN3Ik8mppKGLr6NkGYt5tts3c0sivldp_oRqr3fI8YjSmHehCCRlJsoYpYVDuTK9OcBqwth8cM7wWjCQACowYjXYJmG7zgHDUHr5-fZQuLr6PDPU2c1NKO4RFcA47H2_0XpQBWfEupb0Vux0Y38QqC3g8zyVZa4aGgha9lIWXB4VXrR_raiG2J_cLpTI49WT0-HhuJq_Yte5EBhBohHmDmi55K9yvdGXTwjbhUSup2NICR2oEhP7Y9GYcHqKf9lk6UQA6AruWLMfA6-qzKayXkQwxFas_DM-QHStWkdb-7AJI0B2Xcz5IBUHKrhXf_HL2vpqoaOLyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBDb_QDB60DAYWiD_jSIP7zl95ySijlg2PDpn3jsOfhUvnMmkY1-pjZcOE6EOfrd9E5kMO2FY1Glsos8ai7D8IDFwxYNIzdrRwe3OJunhGI_4UY1xojWMNUmx5FO5U8FBedNGPa2--ND86Rs-GzqJGbgUlR_pZwILmyWB0WNVQd0r57gkmSxc1hHc20fK6cTDIbPlj55xna4hCB6b6ozVVkjKUvuIoQWJmlRubNqya-kofvVRNpqRSB9EVByeo51aW4jcJukjRptZcDyFDgd-gS5AI6EoFchwOyKF1jmk0NwPovwdCITvSGPCVEaVrTScV_CeDuT9om3C2PU-ZPMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFdG41L38i5i06hIYzR9sCAlQhb1c182FsyYSrMsO4LR6DFr3_aEcAqNtTt2seyxv-qkDaewP5r1aH-FGHi1hG2b21G-3o-sHhQJmOKqOrMpFAqG4ZWtTDUMFmd3mFw96wlJP2JRSle7ou5d_wglz__foQurUzrHSjD69ZhMRGJE1owjRM9wjMW0mk7JLjDESYWg1wPJLX3zoR_FU0jSrv2St4Hfej8r60lQOpmZUElHtOYWOmXO0ujCu9PBlfPEIy9kiT3U0nm4rYfdbLbK5uvso0gv3vxO5cLFHhwDpy739LGpMOBKTzvoIZzJUIIP0tiyOBhUAtS4g_hcrsXPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=R5s2ZTsJUjnvVEAo5dmNA3KsdgUjv9UYM_L3cldDhxevMMLgpNNg3a-KNCU0dB9syw3Nj6o2s32i2pd6Ct04Pr5C7dnkzcGoezsHgbVzszLwJm6CEaADDaVnmErZRgHmdiHP63DDidHXLKL7uTzX4D0sI4TbO9qBbDoScRd-uDi4uxAWjwRG7ggtTaD3Z9Oif1A148cXXQHW8nKx1F63PvHSRbYYZDeITVZEcLegEux8ffY4kHGaN8ZOcVDOcYThBaQHaUOTmN5UJvtbkdT3fc9wh5jgLiYUpbftqhduitUygwh3lxqFD39daKDx3JPTX9poFuQmuoTws9q2hen_mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=R5s2ZTsJUjnvVEAo5dmNA3KsdgUjv9UYM_L3cldDhxevMMLgpNNg3a-KNCU0dB9syw3Nj6o2s32i2pd6Ct04Pr5C7dnkzcGoezsHgbVzszLwJm6CEaADDaVnmErZRgHmdiHP63DDidHXLKL7uTzX4D0sI4TbO9qBbDoScRd-uDi4uxAWjwRG7ggtTaD3Z9Oif1A148cXXQHW8nKx1F63PvHSRbYYZDeITVZEcLegEux8ffY4kHGaN8ZOcVDOcYThBaQHaUOTmN5UJvtbkdT3fc9wh5jgLiYUpbftqhduitUygwh3lxqFD39daKDx3JPTX9poFuQmuoTws9q2hen_mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WnALPFf4RkMk7RbT0NNcfNxnqAHjU9CUC-5ixKogvL9cJn2iiGZ15uCUn2nQ0E4vDZlDL4gRV97aCizaN2VOGHktILYUEAaLeoGwJvMmhj-zmAMpW6ITg7Qq_CpK4IdG0tYSYxDEU4DyNaBIBgXKha-VZ2h_Ly73TlXNhws3YPKuREicNrBQZoJ5fGIlAoHEsoyXBLhThpfM7WV2RIlvfpmIKOm4Vb_UhF9_8kMC32qZp6IHRiRMaGLpgYKtu6whE8lWnjbZ_5LEp4Imxgkv6rIU1_XPqm5vcSmJvBZa81qtMR3ys2yI1Xy437oed6L-YYhcnFA_iBChiYNfz1i7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=a0CjbutWWKanGtdc3UYixjCcnwh5trGj4O4SeRSZgdrtB9NryI42s8SdmjN_HLvOGoPxJcAtDZAnftdjdnDMURZ0HQc2q1fg8CyjaJfPk0lYrKyF_CKLI-wy_wh3eGi_Oy4QLx2tKid3wF2hLeY5gEU4dFnXpgmQhikZJ0ABPgrpWfMQbSmvMG4efTo2x6b4GR7T5bv_LLfoyT8CMs4upinzXNivBktZwvfSkzp-5EmjMHjP5rqU_Yjzv05BEQVVnAgjRZ-qJMSzRsJrJsx5IhCIue9H2ISYV2XLOr8vrAWRqBDDtP0zZ3-pecd1NxZ_Ly0FGN7VSWuLinq6L64Rtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=a0CjbutWWKanGtdc3UYixjCcnwh5trGj4O4SeRSZgdrtB9NryI42s8SdmjN_HLvOGoPxJcAtDZAnftdjdnDMURZ0HQc2q1fg8CyjaJfPk0lYrKyF_CKLI-wy_wh3eGi_Oy4QLx2tKid3wF2hLeY5gEU4dFnXpgmQhikZJ0ABPgrpWfMQbSmvMG4efTo2x6b4GR7T5bv_LLfoyT8CMs4upinzXNivBktZwvfSkzp-5EmjMHjP5rqU_Yjzv05BEQVVnAgjRZ-qJMSzRsJrJsx5IhCIue9H2ISYV2XLOr8vrAWRqBDDtP0zZ3-pecd1NxZ_Ly0FGN7VSWuLinq6L64Rtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0wwoDM_ncARMtZGAExKclHcVi80qv6vzthCyfzXcMMyaCqKw_EvhgMA1p2b8iQCJhm41cckgTJ_I-XgCuyaq5xOndfDo2dL6V56d6LE0MCKk3KxgBSgmKPHeVmcxgU-yJsmUle4UhY8tqebrBeCD1YauJES70bX7-NHsIkSE69CEB6nKRQTn379X5daX4rkk8sa9wJ_boJrf16LJIupzCCLPORz_py5tbcqRNeqBMymEDA5JRISeUBZYwhzAi57O1crFSIjlVjwyIxbhYWgIlCpyoJge3lnRlYB6RwKqJL5tvizbY0niC4secSAbe2ZKlbpgphd7iltFBsZ0g5lBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gAfORN5lqqy3pAhrI8QL2DVkuszgkAFCzGQ0h2b-I3f9OvNteNpT2UV5WOfJJfyyWv0qgCtvQvO6KI37Tgansr6yusQGVjCMTYGms2u-_DZYOD48IQdQMU8HEdGuwNz-75fSPI9Ifez4xg93fmwGelofgpsRCppgu6rGdfwxNR1wFZupop3WI-xFLX4GiRgFNJyQImyrlEdQ5TXDR3-qwHZft9yGXdv_-O8RNmHgUMXLbJflIpFo7NXjbxIx9vwXblhDFADnP4wqnu4Mi2R2q9u1yRmtxBDF9GdRd4TNTtyiTrYEMglDgOtEHuF0bc9p0FcZHV8Qt_YtXdYRULhDdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DhmU4gGKOuPVEZ4EbpTE_lhL46C8PsYJYZSid4oRS9WS7XYJ_QoHcVq51GC8Dy6gCYoMqUE5XtKYbfLxxAwumhnI7cV3yt_aesxn4Kv1VZm0OtaHum2Sq6zWuSxpyzbFFWMoICPo9572yLcIuK1EoRCk3rWBnUbx3sBQj-gXZfHOmA0GaRL4AENcLOOM1GPxeJ0docIIaGNXj9OyNriID9Y5328t8xykRH50Hcg7EliJpMcS8P40wLJ8J8HH_vA_UG2GvQAMx_Y8BdW1m6Cjtox6PbeFbpGeeYx9F63bS-09KISJWg9jZ1qwee27e9ru5GszSaHj1tuh7p-pIaj7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DhmU4gGKOuPVEZ4EbpTE_lhL46C8PsYJYZSid4oRS9WS7XYJ_QoHcVq51GC8Dy6gCYoMqUE5XtKYbfLxxAwumhnI7cV3yt_aesxn4Kv1VZm0OtaHum2Sq6zWuSxpyzbFFWMoICPo9572yLcIuK1EoRCk3rWBnUbx3sBQj-gXZfHOmA0GaRL4AENcLOOM1GPxeJ0docIIaGNXj9OyNriID9Y5328t8xykRH50Hcg7EliJpMcS8P40wLJ8J8HH_vA_UG2GvQAMx_Y8BdW1m6Cjtox6PbeFbpGeeYx9F63bS-09KISJWg9jZ1qwee27e9ru5GszSaHj1tuh7p-pIaj7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=fsvDCbvEBdSl0THV8Bnd50AcQ5glvUh7gJyfPQIa7coCdW2q97Tzx6v7XnfNQdksyeKToVi8xm27LmPNadX6BUsg_HiZHFwLg3qvS9GbIZ7hE-wJRU1rJgHr2EFrQQxU1P8X6a_U3J8Em7igOwRy_iqe4UhdCc76Jgv3tY3K0n-TYxr73co1TzMO7Lgazt9P9por00iYmNAg3uX1G09-yotQxwUBvcBtKIJuQvFb6y2ZDB61vGWUc7T6cJfA_ENRYgjqSmhtjtuVUhwcoHNFYiyHYXj3D3llvaos0pkLH2uDBv3J7zoC31DCrrLMVJTOgpsT-PQaScI0zwoGhg3aMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=fsvDCbvEBdSl0THV8Bnd50AcQ5glvUh7gJyfPQIa7coCdW2q97Tzx6v7XnfNQdksyeKToVi8xm27LmPNadX6BUsg_HiZHFwLg3qvS9GbIZ7hE-wJRU1rJgHr2EFrQQxU1P8X6a_U3J8Em7igOwRy_iqe4UhdCc76Jgv3tY3K0n-TYxr73co1TzMO7Lgazt9P9por00iYmNAg3uX1G09-yotQxwUBvcBtKIJuQvFb6y2ZDB61vGWUc7T6cJfA_ENRYgjqSmhtjtuVUhwcoHNFYiyHYXj3D3llvaos0pkLH2uDBv3J7zoC31DCrrLMVJTOgpsT-PQaScI0zwoGhg3aMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TOeyCeCfr5bMSwMzkwoKMMS-CyQdkdscH0mcVy8PBAz6ASV23fLA0a81hpTE7vHox3bfUiIQ7DUpfswnfMDZr2GRHw2uGka0EtDs2RRTGAChg2Up7DjFc-r1Zs8QGgzz5I8qgages5hjckJ0FBrPKrgF8H7hjvIgAw_Tc8oCYcTHC6DThYbblpGxLqCxRvSvo30x-dsBkITtwNjO8Pv-STWlAl-edMqIomf_S4HtAlPX2NrDT5O2klkP42DkXFi6Ur6oWmDv9-uPJ1XDE-FKNrqbC5aK7QutQRnpbHo1YY4yGvPDtYGKMixUrG7SKsVJpPRpPNYtffn2YSQTrIY6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=f_ooEIi4RBeCDzpSwlb_cos0C08URZeAGoyXVA_xcIk0hYeldjoM6Uoq4ju5LhyM2F4fSV6-myLEaIgfPK38lvNfaIqmECA3biCglDKCIkAaVHcmuFkj6V8WEewo4gUujpefg5K4FvqHi4ijS-cKoAZvqM0gH3iHhXboHbPtsDYiKoOwJ7Xe9K9SWyRyZUI4aOkdMyFHv6VVPhP6vl1qjyw8aC8eS1UzHPx77jlCPPgviRGXN2mTU-KnsFBVFnGDGh3x6yMqsbOJlWuJERh7sdc4TW-KLbqufD-UHMhnIzUPgKAW1ZFpNQhmonU5JT9QDe_DUhIW5sXbJycpGt0_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=f_ooEIi4RBeCDzpSwlb_cos0C08URZeAGoyXVA_xcIk0hYeldjoM6Uoq4ju5LhyM2F4fSV6-myLEaIgfPK38lvNfaIqmECA3biCglDKCIkAaVHcmuFkj6V8WEewo4gUujpefg5K4FvqHi4ijS-cKoAZvqM0gH3iHhXboHbPtsDYiKoOwJ7Xe9K9SWyRyZUI4aOkdMyFHv6VVPhP6vl1qjyw8aC8eS1UzHPx77jlCPPgviRGXN2mTU-KnsFBVFnGDGh3x6yMqsbOJlWuJERh7sdc4TW-KLbqufD-UHMhnIzUPgKAW1ZFpNQhmonU5JT9QDe_DUhIW5sXbJycpGt0_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5_ILIAArNTmC1K-9gBJx0MGgdhVASkTn8KJ7hbTkt1761q-Gyv-PHO9mmcel6YsufdWbjW4K9epwbFT7PPq1YP5LBVVb0xAdYFBje4trbSgoin8TIQK9vWFlTtd9ZE8r_fyb42CCLkGBZS51TN53GVXIMd4MpIqaLAkugJ0w71M_c1jx_KV6yjfRplZFATVU9gy-wwYFjwR7fWR29llj1p7OojtOGUocrCREW-IBVyT8AqqU83xG3bf__aECq2FFZVlYilnW3Q4Pw3MCK5EMphP7Xt7GWkij3YGx8nFXdsc9V1-wwasiznoHJiI0WngKzrjue-6DNxN84pfcjSQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=YlXBc212YiFEfBwNCbNIW1oGemzs8gOCMYEHrKNq-EtGCF-YCSm2J_Ue8x1H7yVfwBDvJ0QoRfh0w39kGQ2GjdpL8YSerAFS2_jw3_u3ujtPjte50mf-RlMAfZg_KfvYGhqer7nGeTlkH56KS7xnYnYxFWqq82kIQzjQU8kNGtwD4TooCkwZdtCYwFAOGLl7eeeUylyVJSwB1sZTZ63-HkyZ5T4Ich_8tOqXPilCvilL-ynaHPdqcZtZTIkske8rPReok6Ptz_NRsRoX9Y6XWRdCLDDE5sKhkgUAVBGOR_t3WGHx_pguC4HTP71rXYODxou2eZQfvoom8ibzcwXlYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=YlXBc212YiFEfBwNCbNIW1oGemzs8gOCMYEHrKNq-EtGCF-YCSm2J_Ue8x1H7yVfwBDvJ0QoRfh0w39kGQ2GjdpL8YSerAFS2_jw3_u3ujtPjte50mf-RlMAfZg_KfvYGhqer7nGeTlkH56KS7xnYnYxFWqq82kIQzjQU8kNGtwD4TooCkwZdtCYwFAOGLl7eeeUylyVJSwB1sZTZ63-HkyZ5T4Ich_8tOqXPilCvilL-ynaHPdqcZtZTIkske8rPReok6Ptz_NRsRoX9Y6XWRdCLDDE5sKhkgUAVBGOR_t3WGHx_pguC4HTP71rXYODxou2eZQfvoom8ibzcwXlYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=uBCL9tBmFsyT9hwd_VCdaauUlfaAUy5lHqaVYAZEJa0pgrSjBmflLoFKM0lCpQwwD0_HaRsi92oPtjj6Q5krWjcEZuyeZyC5H8IKVws4Wb2xaMZ-PQ3OLXk4d7IpBeDyA17ej-eup47BnOnJTQ8hrUmQoUTscdobEDkA7D3TLJKc7soQcO-nyYGlYl7ZapY-DfJ47lZWJoYon0fv1GoQClcsMuPR2Qxt2KmeWQh1APdAnyDuB4IvQoHuF83Cq-8SPkZw8E3tZSU5OpWPW-miWzrcPJAGX_P09Gig4Mhav3Amz2oi0Fa8zIFOIVqdzxSTXdS7GNIEeZTO5v7t2ln_bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=uBCL9tBmFsyT9hwd_VCdaauUlfaAUy5lHqaVYAZEJa0pgrSjBmflLoFKM0lCpQwwD0_HaRsi92oPtjj6Q5krWjcEZuyeZyC5H8IKVws4Wb2xaMZ-PQ3OLXk4d7IpBeDyA17ej-eup47BnOnJTQ8hrUmQoUTscdobEDkA7D3TLJKc7soQcO-nyYGlYl7ZapY-DfJ47lZWJoYon0fv1GoQClcsMuPR2Qxt2KmeWQh1APdAnyDuB4IvQoHuF83Cq-8SPkZw8E3tZSU5OpWPW-miWzrcPJAGX_P09Gig4Mhav3Amz2oi0Fa8zIFOIVqdzxSTXdS7GNIEeZTO5v7t2ln_bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tYcw_oTkiZxY_Phgq9BESph0Mk_eSWvByZ2aay_6VxCrp3f__dk15nDCyYJrYTPavi2ox6xnoFrtg93lut6gYJ9RDzmW1KopxjytOmSwN18GqJ2PXVtDpKghZfaIaINgAjvtSSusTZoRCIebUEDck6lEE0O3Z2ZOZwoCgeXy7ljybqvEX5jBYllYP5pKNHEfnGf0MnZ67EH1oywLFfKYr4pynAP2NqunwY3ZpTVeESb7JfWTJAW3PrdbyUdMQR_XFtacBu1MXdsCT-n_Gmvg0RVz8_7TAXb1rLTVvmovdf_tqi-gaX2VjNudPx9CyiCaSA_Y4rBF7tNFqAv3fc-EEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDtwEIHb79AmcnK3fvGocevyj9doPQehlsdLZs9wEk_1kAevjqp2J4PYmjdyT6D5CWWYikqeoyi0q7ds1XypuztqAnuZnn2sFu0Ppa7HEOx2m98xZsWr53HTw7EPFDk0Zzj6OFwcaSiQaUiwRgPgnXV4Lj5gob87PQyeJQiTn2_CTS1B2cIjuQf3UjuTF19tJK1JbRBhKE8RGJNU_gxWeUwbuxySYCrDG0qtdRQaGRy5oO7i4s16pmZQ7ROvIdgynhEZoe7gwFa55H8QJ9K2yHL47h8U-2T2grmwleMhrcnA8o7knyEaQj7OErGiEzPLMXTsAmo0JmyEZXZnKC8-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">(
⚠️
۴۰ دقیقه، ۸۰ مگابایت)
کل سخنرانی ترامپ در نشست خبری اجلاس ناتو با زیرنویس فارسی ماشین
دونالد ترامپ، رییس‌جمهور آمریکا، با اشاره به رهبران جدید جمهوری اسلامی گفت «ممکن است آن‌ها هم از بین بروند». او هم‌زمان تاکید کرد که درگیری با ایران طولانی نخواهد شد، اما واشینگتن در صورت لزوم به حملات خود ادامه می‌دهد.
ترامپ روز چهارشنبه پس از پایان نشست سران ناتو در آنکارا، در کنفرانس خبری خود از نحوه مدیریت جنگ با ایران دفاع کرد و درباره رهبران جمهوری اسلامی گفت: «آن‌ها رهبرانی داشتند؛ دیگر نیستند. حالا مجموعه دیگری از رهبران را دارند. ممکن است آن‌ها هم از بین بروند.»
او افزود: «ممکن است من هم کشته شوم، چون من هدف شماره یک آن‌ها هستم.»
رییس‌جمهور آمریکا در بخش دیگری از سخنانش با اشاره به تشدید تنش‌ها میان تهران و واشنگتن گفت: «فکر نمی‌کنم جنگ دوباره آغاز شود. آن‌ها چند کشتی را هدف قرار دادند و ما خیلی شدیدتر پاسخ دادیم.»
ترامپ تاکید کرد هرگونه درگیری احتمالی «خیلی سریع» پایان خواهد یافت و افزود: «هر اتفاقی که رخ دهد، خیلی سریع تمام می‌شود و فقط اوضاع را امن‌تر خواهد کرد، از جمله برای نفت. ما به دنبال یک درگیری طولانی‌مدت نیستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqV-PX-IbhqU-d1lUVR2PvTs3QBH6U83x6FVNIJuzpmF3SkX0S-UtclrOKOUfg7oiWi04mHqiK-6cpDspE-_r0GK4gDtj1yksebTe3Uh2zwUvMmnN2QA54RJvy3MA2DBozqWtgxr-JgHTGmPJk3VmuswsgkRHMjygwF_F22Gs__ytolYJ3AEh50JSM3aIDi-RRNxr8gJwRQ9nlrS7KoTsfN0bbysTXw8wX2jFRA-NdIuw4nahhsGmCV81HinRUYmbeqO_Tt0fDP6CPdamzx7TVov1BzCpCUHRDOOVkjlWHdHQBtWnB0FtNQh0CDJLa0gCtHTQVJ2xZLOl4cYGDv6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLYE54o6aCmf_MKt_-3NrfK2a7LV6_bOcSDLQw7EqjmX_BtAHvSESm70oPR6gD_ugububm4dh-u-sYGNYiFL2u2nI8yuGsBAELAl_eUKCbmjhXoUNujdjxtGrKiFCUbz9hCmgeVg49uuvLyZ9nJA63xXfYrMkbF1HrTlDv3KE36ojNvm1WO_P0miDLOX5m1smi5zXqtvtuLuSt2UVBUPv_nm7_jnt7eJKqxW8Mqe2vuAFPST9HdnZzfb1soINXEAYrYjF1S0x5B9NsPMXNWiLMgheI7z5ckqxyLR1gXAyrVOkbSWMWQrullqrAEbAYtj7w50xOMaJnyKJFvQzEQ88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=kQP9H0VCSZBaoJYkUfnT8Q6R7lnV6PgCFfQsBNktmGt6KOUjgHoq2NToBdlTU2lUMcVu5m1AZUIPZdF-G3AaTM756t2rzv1FE7NBcgaZaMOJir4BWiWntYGAuO_KwumvsPs8wDzq4-gDFbqbDAsI3f0cxv62ErtxyiOm-pFk6feEA6QsJ3gFfg4DzDcSReZ8OGLg7AXHj5qIWjd7CObLh1SS5C9JNSAjGwO2hdurBaHt8EZfpBz4pNUT_52cMCbn8GTeI44vtOb7c4YBg694TxBI05aEpTRGH7ZqV2pdpvKG2Gnw7Ja6NEDeov1818Ff7vzQVOZbchry-gQBnlAUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=kQP9H0VCSZBaoJYkUfnT8Q6R7lnV6PgCFfQsBNktmGt6KOUjgHoq2NToBdlTU2lUMcVu5m1AZUIPZdF-G3AaTM756t2rzv1FE7NBcgaZaMOJir4BWiWntYGAuO_KwumvsPs8wDzq4-gDFbqbDAsI3f0cxv62ErtxyiOm-pFk6feEA6QsJ3gFfg4DzDcSReZ8OGLg7AXHj5qIWjd7CObLh1SS5C9JNSAjGwO2hdurBaHt8EZfpBz4pNUT_52cMCbn8GTeI44vtOb7c4YBg694TxBI05aEpTRGH7ZqV2pdpvKG2Gnw7Ja6NEDeov1818Ff7vzQVOZbchry-gQBnlAUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aDk8TbHpazNEMdGdXnPT81UuyjwIMsF4exbGn7cQRrHMH_OwbqNEqG8VS_YCzYdo8pc6cABYILicYG7OD8NwgAfbgnuBUyMMWH8V6FUArz3lrbxTLZ3U1RoI8pJlFVBN5UToTdrIQD62ke76xS7PcodZjHHuaV-ErkohNc1dgVBT9KinrRy_GFnE22FbC1A-2zfrpMxAZ0vCA3X089mLrjOrf08O-T21HWMc2KNz6c-fqBnf12z9a5tVLjwpF9-k7L8qEeAR1Wb7XF_S7r_fJADcc9ciPTTsR6UwyCGQ_XVUW3ga57UzbTmRs36QbgJcpjST1WCk6YfWGvqhb26OHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pkwab6hkDQaIpc8EoAvNOzMXRd9evL9PL028pYSj589ES9Myj6-FlmaZ4rMI4h00ziU8lTMcOTkWziK_4szfIQCTrgDMR7iQT5hJKlBjgbfd6OMdhSQZCrT9C8nHrADxJw-VlZ31WjKk-wdJFFUd1b36t32TeBeSV0hi-xGGpnVsiEHVpASeqzGzJ_puFlTlmFaK7xn0_IstcSHv4dDyIcRyTGctKLiwYCNVnq2VATkT7VyqQbprQIDgnxLNLEAYceKkn-dE7BYscwAdL_eDw8q4bX2JW8CpvwM8SFbQ69uKcQumQ_f9rKfvRh03KKc-npPX8sDpowB0nBN-o4fn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vf2M5ShQsDGYmh6R2yJR5wj4Scthuhj4MI_N6Ybf0agqkPX07Eozbopvckdr3SoFBda3lUCWfxKUzSmhJ5lzDv8S-9coiyNAGe00SASFHKbfZCl1J9plgdY-d4IzL6-oAF6YcA1Eq-Wkdt9lHJJT4uR1u_f9NNuZJiuQZve3zy64B7kLlwHraXfjILKouBfTNfTZZX4ehYy28c8O92HIvSODP0WqvKa1QTZwkIogHQDJAbw49-mWtI0Tq3FoW8e0Je8hMoEX0kUPZc5gEmUlVlxbE60_mpKVlPzvRDX06SLUfj6woE8pgXa-L98GrytSyEivOtGJgKWsq75bpfVgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lRv-EdYKgNXMHb-CT5REQGPW9bFH7CVvuMhXzQM5ebawcFIzz8VkJmaLZlfSRbEzXyAJ-eLht7MksqHSQgp-y5n_VTXY-TkxUJPSf54zdWJPvVoGWEM18bYSoCQV8kqjZ9MFJ-1RVmFjYuIjpIncVPtoN9-0i-1lUOfAxIfgw0VFX_K4aZwjnGGK1vD8OKdsDHrtCK47j6_CZFiBflOTXlrPv7Jv8xUlV6Qwam5QNu375v9TciX6iY0Owf_wp5AxqZ1my92DzCtJV5hWMqJbG7xClzrAWlEqVud1hC7-fjmyMU84hjT4bAFszr9cPrBoZ-7aR24jvEfSo7eUC1cG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YetquaCfjSm3TbNZ4nsi8GA0K29hFt_g_IgwJfEBZOksXQHccaGIlUMBpSn8MTNrj7MoRgKy_92zucr5jGA7vS2jLtV65POpZjB6GElxeJezk4w7vMqjwSxQ_2jH0lEhCaMVMtdlpGtHOL6avNDjO0EcQgWdMBLpN587wb1NPhI9bMOifl0ex4Ym5jd50yoxmJ8jHwQHfutGYj5lriUCMUgrhVSuoCyDAblgEJFzcvA6X58NkFejamwYqcdPUSr3Uaa1OlSEftbAD_T9AFbjWYojWd3PJIUm1DZnQbgMc6zZNahpCkkUYK62xBc1TcNofXi0WIUwSYxVFWK66HC0HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=Jng0KCkcZwYJ6h3SiKS55Q0mWkui0uvWOwg37xzzafbVoYfLn70daDQvgpVMKUmY0Cynfo8qoG2ZfYa0MZklotk2LnVMGY9Q2FuvgCot4FSizp4d_NcEIqbnu5fbUvK6H81A_ftGsn00pWbZ3HOn9R7DpzCWVsnYw1tRVFYAqR2DRDY8TKHYBNS22YllvHjXIPVanDX7RrsB981z3x5rpx6N1nSi31a9IW9n1eNX_VOTS1oSL8rksA6e2tCyIKNKr-pEaEl8yyvmpRb3arfPqP-X9AtVIJKiipfPG8qNtadDfdDU-t_p9EFBdbP24fQrVRWLOJlk2rz-rAOxr_LPag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=Jng0KCkcZwYJ6h3SiKS55Q0mWkui0uvWOwg37xzzafbVoYfLn70daDQvgpVMKUmY0Cynfo8qoG2ZfYa0MZklotk2LnVMGY9Q2FuvgCot4FSizp4d_NcEIqbnu5fbUvK6H81A_ftGsn00pWbZ3HOn9R7DpzCWVsnYw1tRVFYAqR2DRDY8TKHYBNS22YllvHjXIPVanDX7RrsB981z3x5rpx6N1nSi31a9IW9n1eNX_VOTS1oSL8rksA6e2tCyIKNKr-pEaEl8yyvmpRb3arfPqP-X9AtVIJKiipfPG8qNtadDfdDU-t_p9EFBdbP24fQrVRWLOJlk2rz-rAOxr_LPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mpa1P3WhXO1rZZnfKHiBruiN2Ovv4AN5v6b6-u4f6ZAwDfk9ZPkfFo9b8m4QLp3i4iYcu7jD0qsEpCKc0wni6bUcITxoflkJByQ-OefSoyYMTM_yjEXOEQ9GzykWIFhwyok28-T0VmifwrEtJSpTUh3hjx1LcvIPOBYqUF8RY4GtWYitQZlUnI1OZKUY4d9hkWBVcF5YLUA26yDgmlZ-nhbWABW7irXy3XX_eFlo8gCWkCL3TlJUvjqM6m1G4NDCdzq1wb3Awn0ozXFeB_Ky8lylwocEOEuxCZtQ_ADas2QTU2O9u78P8FZ8sxQyDr_pWz3kNTSqWNWald1Xupu5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uutRbam-Ws1pzfh2r949CarvXgxN0GYB8Zu2_KtI3z1wbznNLMWkloNMsn1JNr9plyn9rp-HecyMuhqLoMDi4IX-AuuQRiSDKSOvVB0oZbziBA4XujpIvwL4tJUUzWIL4nyMQVZUHdf5bbxnrct4_Vks_zYd-nqx8MGbWEofO0WFbUa13Fb4a39Y2TZAbOlylKB8uEUVbBx7YLXSRQBDlQ-gyGw5j2tyhDeH_QqkXCJnwjdZq2EK84CMlw73Re4tLHLSKLx63sQP5wRlcSflvSLgjF2_BSCaj4MHQD15-CKQXE9k1OQ4zpiKkGEgzQDkYE94KVc2SLUULBsMA10ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ja2vOOv_cUzyPP5XWviKnXTFCtgZnrSZI7Ckt4iw2p6gf8Zs0IICjly1Mu3urm99k6j9P8pOvlAPlb1VoY1oYZPdWgS_d3HcCUYauNLDJ9pk43TxCz9Mle8QfIx1ddOqKkX09GSxN80Zr1l-6Y-o2N-hoFJ0JlCYoKQKr0qfLM4nzUufTRxZQVwd2nW7SXA_ev_qWiCMx4-yCtQkZHFYYN7fs1rTd8jDkA8X1RZdjkcJBntgkBZWYecWrVqJ5y6Emto2OAKa89YyE9_YapGm0eUcapXArNoIsjbYoK84fUTr69FVs12kP3f-2YqfO1tG88Ukr1yZUuZX-m0HxVi9jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=q_Ay7xp3cJhQFgjMF4IExvmEr6_qNiWPRJDacjyc3z51k-NsqnVYaNzP5vEjIqhqprP2DUEh6keHwNltWV5QaxSxqtNB9T28BfGPORYt0toPP4QsnRcA600kZtpDzdSxNc5Cl27T1kqm-HbWinAvEvIYo0EP5vc6ul7OV_a1BCMiXHiiRnj75LVHpnniJYPtVvWWriDupcZ99YfX2yvVwnroLQz1JTndILNOrQ0RdOsxCMp_uzJ49F6gMz7D9eR8Hgc-8cAp7hZWTPJMzpwuf4CXLhKRdX8lkJoerVO8haWDKRZLYXkRq-JIkIFqkJOmQ42_7Uo6JqTAfZr50e_I1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=q_Ay7xp3cJhQFgjMF4IExvmEr6_qNiWPRJDacjyc3z51k-NsqnVYaNzP5vEjIqhqprP2DUEh6keHwNltWV5QaxSxqtNB9T28BfGPORYt0toPP4QsnRcA600kZtpDzdSxNc5Cl27T1kqm-HbWinAvEvIYo0EP5vc6ul7OV_a1BCMiXHiiRnj75LVHpnniJYPtVvWWriDupcZ99YfX2yvVwnroLQz1JTndILNOrQ0RdOsxCMp_uzJ49F6gMz7D9eR8Hgc-8cAp7hZWTPJMzpwuf4CXLhKRdX8lkJoerVO8haWDKRZLYXkRq-JIkIFqkJOmQ42_7Uo6JqTAfZr50e_I1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrR42HneTxHDrptstuD7qb_5_m4qSws_m4BNmT0IU8Ojb5edFMDNZShvQYgQSVTYUMhMDcBIhsIvE3Mi_k3Lz4xxsr3V1JgihmI31tNMfknbjgRoyjBGNnsmBFbgMiSVGLsCOQi6_3QizxyUbvChRhdzieWkOFIymI3EPnWyNsMnbBmZLDl22XoBN9obHsWx7fZ4nN291ZrXE1zkTOkoWacKVIZ9pIq4NtmYrcHLp9WjqJg70AHPz2BMrAeTQfe6_jKlHmqp2t8RsNxJJC5v3tJZCnZ04auKCyUYjtegPaOgv6U57b2pqky9xZ9ekMEv0O8gIFD62d6USFr78XP_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvaJTFmYh0WfG-csgEiaK_vqd3AybG4mzUnwDC90pmSajSGppSyED2T_h7TFDrX652qf5jWQokMIweR9GmywglpqaLN3YKM4TQO1IGrE9gji42qBPzE-rORzFg2nYCw5Mfg9KgHrvz1ayjoe1VWOntaZBLQWx2cZi0Vu167gPGurCi3rLlnfhwuxjVHDP5AL0kMg9ag-W7RiQe6WX05s4XCtowzzmMtuoGmPFC1Wv64Yrr217ZLG9Pxp_Qf0DC9n3SvCgVETIgntlRBoM7xuUqavmLbI4Dozl_Vc87kJD4vg2zWVrGL7t40ce0X4vpXhoqQehg_YeBo0m-usBk6a1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgKvHRe_6p0Qlq4nhU6COxlL-6ui-vADafJXKxia1y7t7oF1caB3sosr_3ZlG_ggn_rCGZP3rlFGKXUrzuBp3apSkxwnRWzQteDomIbIK8TOpRaOzX169C3iH5c3YK1hEr7fexeXiJjjqjSuzZe2Vfw7sfkWaSOdI5NDUIz2zxyG4sRm-exUCPO7KVmSvDP6L5E2eoZTSaEkqWOJm90zKP_q1HC7o-Oj4t_Wik5wOvWk4murfiOC7sYlatrgdWj5OfKq7BoDIW9tzfgVVRD6R9TbR5ZjsiIUS7K5EGKaM-j-wh8WpWyIhEJ5giAuQ9iKY8GLoFcBX2OpJfoQDCYRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arQgN6RhwisxbN5sg2lqpzLpi2HAvDsySCB7rQ2kUbER6nCLDBXsqJqmrx1ut2rfAVC5wDfIse5Ne_qpBioyaxuB3dhc3jy1sEPcEHc59tD0doN7ahgJdHeiRuvW6P0W_4YFIapbPDZFBhdt8ij-5iaeGZeGXlDd5l1jpno2dDtL01qOmKaakYGxnDKHgYiEkIiJzg__F4XcezdOqoIuwH_BHQsr9UgsaEs2USZygvF1tyNfT1uwTZhKVmvPVeCRWMCC18o5ELs_OsG_2PInWHTke_0i2b9ABa48QU627OfRf6BLxCtn-G-gAaUpA0Lv9uYhqc7jD7cJVrJ2jy4QwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت ۶:۲۷ چهار تا موشک داراب شلیک شد وحید
موشک پرانی همین الان داراب فارس
+ کلی چندی پیام مشابه دیگر از داراب و هم‌زمان پیام دریافتی درباره آژیر در بحرین:
Sirens again in Bahrain for the 2nd time just now
آپدیت:
ارتش کویت: پدافند هوایی در حال مقابله با حملات موشکی و پهپادی است
ستاد کل نیروهای مسلح کویت بامداد چهارشنبه اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
در بیانیه ستاد کل ارتش کویت آمده است: «اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است.»
ارتش کویت از شهروندان و ساکنان این کشور خواسته است دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=dA9NBlI8roTH_-Mg1AQ1eODV2i2aXBAbEW0ScZ1Vsi7mP2eUw61g6rW6A0tD3ThFAShrkQY1yBPCbXwQMjIG-stKDTr4vgvIxRvv0JdaNKCYyXuxR25vN3Nj8kxS5NPUc88SBW_YVrwYU1kXeg9hFQqsibuI9_ullv_hgxVKskmNevEZr_WAhRStgNQPOOkYAv_yyDpd5zl7-kGWYvFioPXQ7CiB8kvQAKFtY9eu_i8smBqLycJXS2i_3QeAhpnDN6aspm-F4mwU7KAZajv0DmwwkvXzqjgimeWeFa28WZmuOB12FMUQvNwfBbbVecdFr9b749NGLJn2uvS9mvQcSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=dA9NBlI8roTH_-Mg1AQ1eODV2i2aXBAbEW0ScZ1Vsi7mP2eUw61g6rW6A0tD3ThFAShrkQY1yBPCbXwQMjIG-stKDTr4vgvIxRvv0JdaNKCYyXuxR25vN3Nj8kxS5NPUc88SBW_YVrwYU1kXeg9hFQqsibuI9_ullv_hgxVKskmNevEZr_WAhRStgNQPOOkYAv_yyDpd5zl7-kGWYvFioPXQ7CiB8kvQAKFtY9eu_i8smBqLycJXS2i_3QeAhpnDN6aspm-F4mwU7KAZajv0DmwwkvXzqjgimeWeFa28WZmuOB12FMUQvNwfBbbVecdFr9b749NGLJn2uvS9mvQcSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: بیش از ۸۰ هدف نظامی را با مهمات هدایت‌شونده هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده آمریکا (CENTCOM) روز ۷ ژوئیه دور تازه‌ای از حملات تهاجمی علیه ایران را تکمیل کردند و در واکنشی فوری به تازه‌ترین حملات ایران به کشتی‌های تجاری در حال عبور از تنگه هرمز، بیش از ۸۰ هدف را با مهمات هدایت‌شونده دقیق هدف قرار دادند.
نیروهای آمریکا سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های رادار ساحلی، توانمندی‌های موشکی ضدکشتی، و بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را در تنگه و اطراف آن هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه تجاری بین‌المللی را تضعیف کنند.
ایران اخیراً به سه کشتی تجاری در حال عبور از تنگه حمله کرده است؛ از جمله M/T Al Rekayyat با پرچم جزایر مارشال، M/T Wedyan با پرچم عربستان سعودی، و M/T Cyprus Prosperity با پرچم لیبریا. این تجاوز بی‌دلیل از سوی نیروهای ایرانی نقضی آشکار و خطرناک از آتش‌بس است و آزادی کشتیرانی را تضعیف می‌کند.
نیروهای سنتکام در موضع آمادگی باقی مانده‌اند و آماده‌اند هر زمان که توافق رعایت یا اجرا نشود، ایران را پاسخگو کنند.
CENTCOM
قرارگاه خاتم‌الانبیا: پاسخ کوبنده می‌دیم
خبرگزاری رسمی جمهوری اسلامی، ایرنا:
قرارگاه خاتم‌الانبیا: نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند
🔹
تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را نخواهیم داد.
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می‌گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP2XEGBbBTb7OBYECmlPShXXlTFmJ0UdHo_g5QLqvZI3pGLPOohuA3FK9aKN3AllCKSrau_g3FIEC-8xq6gIADb7mwrRd7hQndsrBK8lpA2KOHyxBQqV3tkDyTonGcy2XVj5Iovf6-BQTTOA2V3x0ZwfQoNGDhFkv8tLr5Qp5n7VIZHIF7uPyKw3kwWq0Vh_EB5_adb4C1aXDV1tRei6BV0qUs_fYLkoeZypnvI7tjQ4AWdK7uMRTkmVK9TwiCnDDvrPAna3S_gYH0J1AIV40sxIo2AxzdxWmC5_1c4wvRprlKdcrK46BGmu7DGgZifP9PoFErMg2oa5TDr-d-9ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aoNJfsvT5NzlbkTuPEhO7YS_c0r7OTQ2evVRbI2_qfvty3UR2_ip1LUoc3W0pFAC1cYpc4-9crQm78ZMu40xmdzhXIuL37xoUzCy29gT1xuWg0w8XFsQojg3Ys5u-CZf-MTLXCHn-BVITi2lQXcDC1sGPv68aBlvr-lJju69J76K3172e02aN1nuDzv5jmNN1RS-CzAgaVoZ2MRDMSTjrlZOmn11OHl0NIs_XrH_2CMRK0YSCNgZf8ZdmrI7K-yR7NgrNR1XDEQoVURYCmbxw4edo4GNqELj5jh9JBmC-pWwMC_Ci8CmMLXty0eLvsq6k654waVC7h5M09-TTaIRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XOCmux27huKXEvF54UAgamQ8s8gDTZbT5DkmdHGQsyOrG2U8sA3NuLmBFQNB3wMxgyqkTj-TPaYpA1OX1HGzg6wR8j6LSrE0S6wUbRX4TK0sRYqrZJ_gChstR3i3peDojk4iVKS9_WOvSUV_5opy6lJvBiKCIBHFwbhuO8fb2axCW2UFT6HTAxOuVFgqjHR-MtatVyy_8fzQPLV05RrQa1CK-N65FkoknkTS6NvS6xTX7DnbeN8Cv3FPCjZevgHZejxet3yNu3fq5gJIYhV-bDUCC4MoR6AAq_Z0d3NPD9izi5J0vTyQfrEcy--eTx-uW1XC3HvdC6qL5VibzChLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eV47ODEkcUuvUCxksHF4YMHMFOMojbfLy4_YhbOINdfzo2ZssKVhWVqwjfUmoeToMJ4s4E6rNpBcPQExD9ohGS4raO3_bhi-48eBOFZ1OaJgS50XRwGQpu27Pzr5GTCd_ljJcWOgoH_4z94yG6GaVAF6RTAHd80oDOMmc4J9sHmWx-1k_DusODmGYi_edB1MMFwCB6WCUm0Su6oWNKs6UOnRpgfMmHIxEom3tA5mTq7xz4Kj6-kqdrT6sBfgyW7IcGPRYd4CSAJrZUyI9SYfHG-kKuXIUfdr1pq2oDmyq6VjtZJlqc16dYbF7Tr9b2mPZ7yPA1VuHRa5uaojIA4bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sMRNpg1eRa6AsSFZBuXGpz5Nv_97bcA5qtWhOEuGEEhwwjzy9NuBQ188jCGkZXvvUl8kdZHsHZdcnZXb_jgCs7kb-buOKJMO2W-5OnKYrOvJ0Eg5WZg488tx0J-uw-DtVLyUN325uFQGhMo0Z0Mz_ZNXGGDwG6_wwVLCk-l9R8S9R9fvGjNgTcUXTbB2wsPAR9c2iK0QFq-9b6DfHW7UMeQhxgRGkkQGQ6as1Lvy_xljGorLj3XZJi8KeJTrOL64El-s7YY91IBCdxfcRneYvBAuDbRTTYf1US9ZLQTrkDn8D-NqVGSXgK03xajpErfrRgO9LxFzwNkH24HL3J_EZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/964f541742.mp4?token=IXVO3IpmSgfvjddtS_0oBzi6y9GPmSpEN4c3RgvhSP1cTbQFJCVaeLIERbRrSvhmgX5LeUe1a3hmX5SbDPfgIEAMW23tWBAo57R8G7Q7eMUOmF8a7CDoHeGBbb1OZXPpa0q2i2MeN_FHuldA2LNSXnr5sQ3nvZGgs_IzcDbzHmeSWuz_3tGX2xRQixojpOVLwWLAzOJGxS1K_qeLOThozHjM3GpkBKoH5eYHJCbO3_mCflvT-CqduIociK7IRkkExbH_FETFPTRSv8hz1LiLJkiiR9Uux2PY2qfKQTlguc1gA_RKuixhsB7V84yMuTq-tOl0IN_NhOx68JYir4sRWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/964f541742.mp4?token=IXVO3IpmSgfvjddtS_0oBzi6y9GPmSpEN4c3RgvhSP1cTbQFJCVaeLIERbRrSvhmgX5LeUe1a3hmX5SbDPfgIEAMW23tWBAo57R8G7Q7eMUOmF8a7CDoHeGBbb1OZXPpa0q2i2MeN_FHuldA2LNSXnr5sQ3nvZGgs_IzcDbzHmeSWuz_3tGX2xRQixojpOVLwWLAzOJGxS1K_qeLOThozHjM3GpkBKoH5eYHJCbO3_mCflvT-CqduIociK7IRkkExbH_FETFPTRSv8hz1LiLJkiiR9Uux2PY2qfKQTlguc1gA_RKuixhsB7V84yMuTq-tOl0IN_NhOx68JYir4sRWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکان نیوز تصویری از یک انفجار بزرگ در بندرعباس و ویدیویی از انفجار در سیریک، در پی حمله هوایی آمریکا را منتشر کرد.
@
VahidOOnLine
+ تصاویر دیگری که با شرح امشب پخش شده‌اند و من از درستی همه‌شون مطمئن نیستم.
اسکان نیوز گزارش داد که ستون دود از سمت پایگاه هوایی بندرعباس مشاهده شده است.
منابع حکومتی:
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
🔄
آپدیت:
پرس تی‌وی، شبکه خبری انگلیسی جمهوری اسلامی، از شنیده شدن انفجارهای دوباره در جزیره قشم و نیز چندین انفجار در جزیره خارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVutFMQ_Npw3C37qag2_AUErHf-ivQY8nK-rHuukCF-XBk_ff15h6Fv6UNvTBnF0-c1MEaf4ARG8Aazik7WrbjkIZ8m8hk5RQhxbRjCNmSeF4gIp8-S0KCsLM8v01XA8TgnwK5tDrUM96_vdOSlkE6DiVl3tvdmId992FPLTVuFYsd0p0_ly8Janl8iWDOGe4DZ3QIPNvHaWrRMrLocG5MEs7PaOdCYuYhb8O92BZnWpc0U8EoQVnmLivyFwSzzmHcbVic_m9CP6A_xYMJtatdoKA2Zo4jRNHSMqJzfVVpnKXHn_CFrFNawGnaheOphu2pULA39DFTBZLBE225COvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5I5gBcFrPc9dmHA7FADyctndm6CMSqX9wDIeawvdVPj3cNC8Ru2Le8_su3HwvhP_ilAKYno9NbhEvdZauUTY16lj8bWT6YfXZsb-z6v0XsmL0C8dp0wnmYvPRmn4_0tdpOlb5o2sdDNlddze_bKfHhm7c_EIbCK0jzNLXtFOSYeNMCqnKJN2DGfYXR8XWFiUIDwuiAuRkXpLejrBfwo58egYDXvVsdAhXPkGrufICtle78infs_KMvNeZQd6zgvbCya0rb_vWQ0nYjG61_QEjBb_QerawPMnLHAlkpLVqrciSZQkotTjYannqe9403nWCpA-q_LUgAZeeHXOlSsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvO_aodpNvWW2BO7KU6wGyuveMLHsiqVeFKIMNGjVa-moWHp57pyxZvSW0YnFyi6qw8CCIYg9kyRUy7Ey48_ToSM20BBffR9xRhGFpXRfQOBADnoRq61IoZ8-ChBOtjDgiVDN-pcjb5QgWQPvM-1N68uBDx2l4IMC2bccnKtAQKR8F2uKXMOvbNGo5nyoJFxScabLsTVCfiH4W8zzyjiUkgJ0U_xHP8N3C3c9F8-gBDrM9IJNgEc_8Xuc7p7g_CDnfjdxLDVaPkvY5d6eDdfkqmlkuY0rRK8fQqqtQ8h-lHIE9MrR9Idd1eq5e2eXVqlwRIiYYFtzwUcD2eC4P7fFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/umbpWVvGWZ8Q2gAh8bSUTdcUuHcvlYofjRpC77kUnStaeFf0gaVMqCHGw71fOvnRAYMJUGmEkyRLjv3_G_FDXbuWKJwh0AS1yThg95CH2InbeW71MvdQLdVOvXoGZ6IFqb_ufkqJeThpzmY1bxjtvcbHiTZXnWfG_A8bvbYrdO52MnStgq-pJgY4PIA0RnhO2yCwhc3AwNBBe8DuQmp0v2dcVE64NYii9MbvwkRzkWhzhP7ccglkkgRLpEO_RmnUvL0wvVL5GwltOm5G3oCUv-1ZDEU1NQkiml5IxjZu6hP2SSm0WJmNo7PKAT0VTWlPa86iFukBwnneN6k8EiblMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIv1L2aSUkAtJDONBSYyPSToRdIfX1huhjNvFlkUyBUiqop2AVcKe7ZDr5pFnGCNF7L4DxAohG5Ks-y5aVQxnSUZy5spIO3R21zvcjUBY0sj6FFb5QZqclDbkwxkOwBD0dXR_KNO4Lg7EeXdtnEHUtNeYY2tlgd_o-DcRtN_xNx3trfVLKtvpv_ptNwxg6X7_OQetKclzmBQsX1r7cu8gsXSHsTHsEqN5zoL53UIXHEkNNyvPdWETX4fLggszIMLm1d3JUmExGbopDvBmjmUkiZjngGIRxASEEgL3B2T2k3K2G8gnuHDfW6VyfqKMorEZpOvaTgQ-J_BRErzw6WE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNYpSC31wwqNzYM0TiOK69sue4f-hdJ-9LPZ_7dwivW4GxxTdf8LCjGtgzneT_r6xGW2Hco4N9dSlcV66fUpnOZFMOjbo_E4qWSQ_Xgwxn_kAEXRjcr_4y4E1xBdj2GHYX1hXdPk0GF11nSNBMqPH0GDKqw4va_ik1hASykG33lLlB7Dxr7fKWw9ZV1OSDYCvyOORlAT-1OUKL-mDlLt34hiGGR9rWveJhCxLhF8ngY0sRB_NwP_YDjTKyOMFniZtWpDOXq90Uhd3xH6MPhU5NRe_d2k5A8FnN6oPncbMYedBAXDV0lkpne9Klh2Y6DHMZ2KPsZmug547xHqp-7Ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez80WwdT1E6R33_W-NQTpZWErxMUfuyx-hbIUoG0qEQGw4wPbi-9xk5jecDrGFjxWwSe8ZH8klhaFjIsAHR9cIndsIpQjxh5VckTWLqdqiW2CxP0hXrDQjdE1ro6TQ_FNXyLyYZdHDIJOCD-KJVya47OZGy5IOGkpXr_E5LNhROyr5oUCi5ayF3rkuZ6I_UEvDQkNwEkZLPkbfbPLr956pkgjrOCBvgtByOpEw-2UC4MnIod-EQKUwFfup-eBJSLhSd5mQW3rCLLC6K-4Rh-VTBtS9BZsKFk-JDV9sBED4qkXlAL9_iISSkEo5X7Gr_mgo6i68Piv5MSYfgNb_szJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2uc8lUAcA9jdp5oFUzidteRrxM6ZDgOVapaf2iMUwvkUF1gJQeN3PZUCWAvD8q0aN-Tekx8nN9pjDw5dDPLQopEDEn4ZOp_W3IHTG0hIi9Iz8mkdUbP74gDXQ20xdC2NDvaGonienwmQAmt1gMAWghN1P7Tcl2s2eKAlvZtuV4QdVlE6jlkX8KmN55RDFeiAeZmED-LwtnM1uWs3WHMcrQ0n_keyffKlbXoIdjvUEBImNi1B_ihM6SyolHfC7-MH4FRJMiXLmdCS6fCzn-swY6L3k7K2Ak8CxAuHGU77GG1JHjqanzIVL2BxOYU7irIRo1b43m3RRgpTKWCX_FRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HobfGWAhvV0mDDCvw_qD5YdcRbXiZQ7aYMeY77GgpP7ylzCj5oFQAdx1OqkVYoiLLSVikYkjPyeRKWAPRD4nVPdw6hX1dAcipP0taqXLAa_3OaNkh3b1tI7cY2u_REBRpI9w1ZcbVkMxoh3Jxd1FweUp3VMoMfHxi2t5CwYU8QIrAuePjwv5eODmGxSnYQt9ruGDRVNawV1qMXQ3sb1tSUxReMt4lGu37ODqXiHPLtqNSjP5btG_ZsKtfKXvt2wtGk0H4J_c-MCt6x4cp9JC9vGDriaP0fmqaGeZk5MgKigED8NqAtUH9SzU_PkEyZJsVwKRBwZP-YJm9Y-vXIgVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=fC412F1lMR4npOYf-LdhAshXXQPxW_r2TlZZXRJYIdDC--qVGxp2cyAQwDrazelzCmDdv3c4LzpySS6S_XrrICRefJ7GBYkFZi75iYTRsbXV3lc-46tn9fi90JZpekQEPcni3dsNkj_ngoADF0Lh6UVIWl6jVEbOAD-quM6rHBncsS8gXTZdt7cQUvqOBpUX2_v7XopSCQUFZPDaBm1AQsUUU_W6cXtNUt09JeWZ0vNmC1pt4j9xMKtbNAYDZeYldpwHM20V3VlFQuZQYO2xF3VIUCG5ryCnYVH3tK-CRUpSQf1_y076lPyvJLBP9uwwCh6joCnRBJhFxqVEqyglGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=fC412F1lMR4npOYf-LdhAshXXQPxW_r2TlZZXRJYIdDC--qVGxp2cyAQwDrazelzCmDdv3c4LzpySS6S_XrrICRefJ7GBYkFZi75iYTRsbXV3lc-46tn9fi90JZpekQEPcni3dsNkj_ngoADF0Lh6UVIWl6jVEbOAD-quM6rHBncsS8gXTZdt7cQUvqOBpUX2_v7XopSCQUFZPDaBm1AQsUUU_W6cXtNUt09JeWZ0vNmC1pt4j9xMKtbNAYDZeYldpwHM20V3VlFQuZQYO2xF3VIUCG5ryCnYVH3tK-CRUpSQf1_y076lPyvJLBP9uwwCh6joCnRBJhFxqVEqyglGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=DimCGucx5d7n-gGRGFKgENMAz8HByuBb5jF8BSRsyPHSvb7StuRGyk7HmNxd40fIflON5ovSIdvqtC3_-BX-IuC4fZaah0uyLzu6ILoJDabZi6vt2R-E7g-mMSxCTvH_B3eVI3X-debGtHWdbBwN9vdTaSvlw0E1ahn-0A1h5Iv2unpcmPyCy408quMRS1fzewCyXoVwRRUCW0mInBb3hCtBeGKl44D98lUHYEgUpPFVv7RNfVkjdNnK4D4x-Nwwxhq737-kmWQ66Q2m5JfNF-a_8pXRSOS8YdUdCzQn30WtCxIvqhayKWHklF1RiMr_wfMmsO-uLuXMVj0kPCfEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=DimCGucx5d7n-gGRGFKgENMAz8HByuBb5jF8BSRsyPHSvb7StuRGyk7HmNxd40fIflON5ovSIdvqtC3_-BX-IuC4fZaah0uyLzu6ILoJDabZi6vt2R-E7g-mMSxCTvH_B3eVI3X-debGtHWdbBwN9vdTaSvlw0E1ahn-0A1h5Iv2unpcmPyCy408quMRS1fzewCyXoVwRRUCW0mInBb3hCtBeGKl44D98lUHYEgUpPFVv7RNfVkjdNnK4D4x-Nwwxhq737-kmWQ66Q2m5JfNF-a_8pXRSOS8YdUdCzQn30WtCxIvqhayKWHklF1RiMr_wfMmsO-uLuXMVj0kPCfEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFil5JSLwodvh6bQE8mlYVTalrQTLghI41Iy9NDl3Pseg8ABNiRLBZoQIdG8hSiH7Niv6aP45NnWtg_PNuZQ7TP5RWBmkhMb6GzdfUFfzHLZn4PCL_yvBnQI0ycrNuQYYFuHWyCe0l6fFSfBZX1821jE3LaAtEAbY_IqUXEJDGHx3ZD0Jkba28JpF02J_5ESD3QzgGdHzt_IlCqNlxWYEXvGZveMKvcGGa-p5WA5ZmDjaE1dMxiULX89Wf7mqYpmSwui_Gzlzi7Phmr38Op4GIGCq-wpAhzKAg3GQmQGt7L-fAHnIHrRU2a9hKopQVT8r9pmVYetjWt_ishhkIvu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است.
خبرگزاری رویترز حمله به آن دو کشتی را تأیید کرده و وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داده بود که سپاه پاسداران دست‌کم دو موشک به سوی آن‌ها شلیک کرده است؛ ادعایی که جمهوری اسلامی تاکنون به آن واکنشی نشان نداده است.
سخنگوی وزارت خارجه قطر روز سه‌شنبه اعلام کرد هدف قرار دادن نفتکش قطری «الرکیات» در نزدیکی تنگه هرمز، حمله‌ای غیرقابل قبول به امنیت کشتیرانی بین‌المللی و تأمین جهانی انرژی است و ایران را مسئول حمله به آن دانست.
هنوز هیچ گروه یا کشوری مسئولیت حملات تازه به نفتکش‌ها در تنگه هرمز را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=PP-b1qc9UOLY_B02eyIiMbCQT4NFtZMtHH6xJ72o1J_8UkgZy_cLo8_n9Po3Q6L5LBAgwqpFYyMaVuidaN9A5rZ8EDNpihoQJIQTy0busupbQDhVEgijAzvpwJNQcM3kqA1ehsMN_tzl9b-c5xKEIK7qZUPGACW-lcEncOtuUgVVRcL8A4ohe8SS7rdoBrs1MfrL5JtHHylMai_gszLmQRrN05iBM_uP3gLtXp9jo_VeSuBIB1PP_UaeI6TverLL31hbqZlsaGR0tHLVGz5TqI-tgId1UGNVSLaq03Nv0mwPmEi4IDWhBuC7ROoEPSkZoNERPVBGrO_bnI-1x06Hng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=PP-b1qc9UOLY_B02eyIiMbCQT4NFtZMtHH6xJ72o1J_8UkgZy_cLo8_n9Po3Q6L5LBAgwqpFYyMaVuidaN9A5rZ8EDNpihoQJIQTy0busupbQDhVEgijAzvpwJNQcM3kqA1ehsMN_tzl9b-c5xKEIK7qZUPGACW-lcEncOtuUgVVRcL8A4ohe8SS7rdoBrs1MfrL5JtHHylMai_gszLmQRrN05iBM_uP3gLtXp9jo_VeSuBIB1PP_UaeI6TverLL31hbqZlsaGR0tHLVGz5TqI-tgId1UGNVSLaq03Nv0mwPmEi4IDWhBuC7ROoEPSkZoNERPVBGrO_bnI-1x06Hng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AglKVMHMlh875fKwy8Bp_UrtXKCzzJ9dNED-Ak6qDAqW2w_s799Ao_RWDME3IN4AwUK5QurUyLPo5PTiyajuboug4Qre-U9g6ui8PNGQrlgQOhAB2ILPXLXHFOsrkKDg1TWaIQyg1MaOpasHwtXwTbuRbA1u_ANmbIqC0CABgaI82dWv40yNp-AkUVASMPbYFuvpAh5y8SF5bJirKqyjxt2dM0ZcYLcQZkGsZ3QXWrKon1Bxs9BgpKhaoUcG5QHu6qYJhuG0pv7iImUuFPzDpkp5DyMgY7m_nLlD3FP4ZdmWF7LG3e8rIqWFkF8O51SLIz9SqVi0L5RvTIvXjXldMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با نزدیک شدن زمان انتقال تابوت علی خامنه‌ای به عراق برای اجرای مرحله تازه‌ای از مراسم تشییع رهبر پیشین جمهوری اسلامی، محمدرضا سیستانی، فرزند ارشد علی سیستانی، مرجع عالی‌قدر شیعیان در نجف، به دفتر علی خامنه‌ای اطلاع داده است که پدرش بر تابوت او نماز نخواهد خواند.
در همین حال، جواد شهرستانی، داماد و نماینده علی سیستانی در ایران، نیز در مراسم تشییع و نماز میت علی خامنه‌ای در تهران حضور نداشت.
پیش‌تر محمدکاظم آل‌صادق، سفیر جمهوری اسلامی در عراق، اعلام کرده بود که مراسم استقبال رسمی از پیکر علی خامنه‌ای شامگاه سه‌شنبه در شهر نجف برگزار خواهد شد و آیین تشییع عمومی نیز از ساعت ۶ صبح روز چهارشنبه در شهرهای نجف و کربلا ادامه خواهد یافت.
خودداری علی سیستانی از اقامه نماز میت بر پیکر علی خامنه‌ای در حالی صورت می‌گیرد که جمهوری اسلامی از زمان کشته شدن رهبر دوم خود، مجموعه‌ای از مراسم تشییع و وداع را در چند شهر ایران برنامه‌ریزی کرده و اکنون نیز در تلاش است این آیین را با برگزاری مراسم در شهرهای مذهبی عراق ادامه دهد.
غیبت مهم‌ترین مرجع شیعیان عراق در این بخش از مراسم، یکی از مهم‌ترین حاشیه‌های مرحله عراقی تشییع علی خامنه‌ای به شمار می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vWU5isxP7jQP2YxwntRAq70BUFFlr5JxNTbQdN7G4ns9gF5uYaLgqpBPCO-5I7YHDSsiuvm8C0u0ku9si39SBMqaCCk5wEj_2KiKXJl0lL3u1Y2t1qPSE80zB7C3fBKDf2CqhoQElNTKRNK798I_qnEeVDsAu_tc8XgBiJ9r3Clsa96X6ohmty3uNwMdxd378NiLDaNSOgHPex8LmKmdK7VKb9hC144OPPGRdUluKq8f40hNlrfzdkzlOIsUIW_B_SsKObJ1pgTouvodzPLyPxtXu49UXFrY0j2feWc_BvDeQlYwdpzZDGQYLytBS48mquuptEJ8nsudgDFUFM0otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داد که سپاه پاسداران روز دوشنبه دست‌کم دو موشک به سوی کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است.
بر اساس این گزارش، دو کشتی در پی این حمله آسیب قابل توجهی دیده‌اند، اما هیچ تلفات جانی گزارش نشده است.
حمله گزارش‌شده پس از آن رخ می‌دهد که مهلت توافق یک‌هفته‌ای میان ایالات متحده و ایران برای توقف حملات در تنگه هرمز به پایان رسید.
اکسیوس می‌نویسد که ازسرگیری حملات ایران، تفاهم‌نامه‌ای را که کمتر از سه هفته پیش امضا شده بود، در معرض فروپاشی قرار داده است.
این منبع خبری می‌افزاید که
احتمال می‌رود ایالات متحده در واکنش، اهدافی در ایران را هدف حملات نظامی قرار دهد.
@
VahidHeadline
صداوسیمای جمهوری اسلامی به نقل از «برخی منابع» گزارش داد که «نفتکش الرقایات» متعلق به قطر، قصد داشت «با حمایت نیروی دریایی آمریکا» از مسیر عمانی تنگه هرمز عبور کند، اما «پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.»
این گزارش تلویزیون حکومتی جمهوری اسلامی این‌گونه القا می‌کند که تهران این حمله را انجام داده است. با این حال، جمهوری اسلامی تاکنون به‌طور رسمی مسئولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACzi9yqKX5uLgRC-FeqHMhOp6ziJEByysdCR6k6e5fr7awIEf2N1m-8SRdzRbuh3Ff6eQt0D1JjeqhwCbvc6DyJ3COPMXiV-MStfLMOWH2e1pkSfv9VTyzOiPwHoednJsWlOeOMZpxDEF3KkZ-KUlah6jG7kX_nFnH0qw6oJyihw8XCUtbmOGyjc-846Nnp7q3t4LqTp7iOQxRR-epc7i_CJMNlN6qEi_Wv0vwcWWVcnXxy5tPwI8JYCqx3CyFFRIDZ5o92eDQ1YeWgg8YYrB-b5gVmE914SUjFiJWkAvmTv3SeybSbq9U0-JowUdAQ1bAiGJzaH7w2BKyOFPsWZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=R9lWXS7NNxehWc7R-O1x-275munLKIZWJxYKgkCO63GqPNxk11rQNMPXBFGj9HPTcra18F7vwjX3JxspsUMlvrgML-CM6jv9lJmImn2XgziVArQ2zITLflaED4P5oVEmKkINCiSuA_mRH7reT_dbMb53718jUN9uPdawAd7hOEaNq3pCllE82GOZ2lgeSeACaAjrftevmPbvfO0hyj5kzVJLD0TAunxCUEBbgm4u8e6FDanN38MBpbAUV8FeCCxwr3owuul8CHljVNV-VpGj1w9P1T9bEoune0sbSJeOzfGzr3hwxXLkRBqcXfAaMsHKZT92D8m-iVHXnYO_CZqTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=R9lWXS7NNxehWc7R-O1x-275munLKIZWJxYKgkCO63GqPNxk11rQNMPXBFGj9HPTcra18F7vwjX3JxspsUMlvrgML-CM6jv9lJmImn2XgziVArQ2zITLflaED4P5oVEmKkINCiSuA_mRH7reT_dbMb53718jUN9uPdawAd7hOEaNq3pCllE82GOZ2lgeSeACaAjrftevmPbvfO0hyj5kzVJLD0TAunxCUEBbgm4u8e6FDanN38MBpbAUV8FeCCxwr3owuul8CHljVNV-VpGj1w9P1T9bEoune0sbSJeOzfGzr3hwxXLkRBqcXfAaMsHKZT92D8m-iVHXnYO_CZqTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=l4O31hTyMRiD27hUP9wLxBnNAlkaR91xkL6NuqgHCrjvlTN6IHa4MQ4pjdJn9LOMgu8c-GrckOtrSNBt36YUvRld8E-kPu0abaJmJaMzrzDs2p1F79YOCdaxNTMdLkEhRGt2Hkj1EOvcudaV97OMbpOtsPk_yEsvr6iJvDythuPsCb5DytsZat9GWp2o7KxXCYBATSA9pA0wCXszvxtoS6X1fl-7ldSs1JUnEWenHbFl77D9A73OMxNfG4s_iMEooSEm72oMWsMo3iWXUpSWVDBYSYjI1S7p4O9OL5Qy28fHLiwedEn-LphKew3QWI6rCCPZhaQ6UPrCed9G0y8mFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=l4O31hTyMRiD27hUP9wLxBnNAlkaR91xkL6NuqgHCrjvlTN6IHa4MQ4pjdJn9LOMgu8c-GrckOtrSNBt36YUvRld8E-kPu0abaJmJaMzrzDs2p1F79YOCdaxNTMdLkEhRGt2Hkj1EOvcudaV97OMbpOtsPk_yEsvr6iJvDythuPsCb5DytsZat9GWp2o7KxXCYBATSA9pA0wCXszvxtoS6X1fl-7ldSs1JUnEWenHbFl77D9A73OMxNfG4s_iMEooSEm72oMWsMo3iWXUpSWVDBYSYjI1S7p4O9OL5Qy28fHLiwedEn-LphKew3QWI6rCCPZhaQ6UPrCed9G0y8mFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uig6NyQUfrimHU9TIwWObwgojSJhwlzJcoXfurY0punMbif3iDtcd6jngZNejIpP67cZpnBK0PaI8z-1d2w5IcYH1_kKU1J4IrM61ied6XnAszR0x8lAEtiyFKgk6NyijOGcsipSiuel88-t7qLOoa4wAOj3dlbt75Nts47R9dD2zbOQ4EO508FjqP6AKp3n-BArRHee1UWOb0asZN_ZlcSs9il2syyb1pgxwBRqwR52z3zX2bDs5PgZQBZ2c1UpzZGz_BF9pHfuNFmjY_jrizeiflJ4fhzRvuSEVSyQDCuO2BpATfjF9-nV3U47X8u1zchreZ1JD6W095tdEYprFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=BFMwiQOM7kY-ladZ34BTCEiYhopjNF-KTUQ0UXro3z4S9vv1lWHYyluw1nih6wjF0g3Z6yi_sTYbp0tupM9tQC5o_lT1tFh9UQCZZYGd8_Sz3sRKKETqvbP8cdVcoOS6RjX8uTRhmKJgvOS_8rCOL9Et_5ZpASXKRX7_M10_39-FC-dxFjlJGIe4ZDPzix0Equ6aAhhhH3um3aaz-SWXQ1FI3TGK8PvfYgnb3rrwEJuaFZlLo9G046TnrJTZir-ZuY_QtS9dlQg-jg0baImlGwsN8LboCVu2sN2tJXR2Z926OobtVWkLErE_Nh_sq_Cra73wR2nL4B-Mk9lyATYS5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=BFMwiQOM7kY-ladZ34BTCEiYhopjNF-KTUQ0UXro3z4S9vv1lWHYyluw1nih6wjF0g3Z6yi_sTYbp0tupM9tQC5o_lT1tFh9UQCZZYGd8_Sz3sRKKETqvbP8cdVcoOS6RjX8uTRhmKJgvOS_8rCOL9Et_5ZpASXKRX7_M10_39-FC-dxFjlJGIe4ZDPzix0Equ6aAhhhH3um3aaz-SWXQ1FI3TGK8PvfYgnb3rrwEJuaFZlLo9G046TnrJTZir-ZuY_QtS9dlQg-jg0baImlGwsN8LboCVu2sN2tJXR2Z926OobtVWkLErE_Nh_sq_Cra73wR2nL4B-Mk9lyATYS5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAucKbltLucnQCKRn2Jr0dfxH1Anbri5oFywPnQocUKoCkfwVEr3qi5oz9tsHG5n1hyx8uoz_lYM0JHerRmqt5m1-ogWfxyWFJOnOcXUvVlUT9mAfVoi-SmcBXGaa583FkAED9AicadAnAi0dTo0BMy5f_cnPjapTGgUQKu7nMwa89cCGnWxPbN0plwvjbIBvKJAG-lz49oHna4_ePLqFtLmU505oUPEBk5TFxoVXio-JYJJmHaZPZETn8xG25DeNc2JjeXhwA8nHroMdxmffV-yE-Wc4ask7PHKmXBqCyiHX8FWCinEL02L3nzGOw93t-rouyEHdXeItKVCwc8rKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DEpiS_aykBsfCtw8kIE2SrZ6vIDo2L6pc-U8pcCHw8b8XaRG_QcmPspO4hwWcDB8tUl7Ya3Zo8QKzrXG8uPYI0oLJ56as0Q_NjyU5w5vyN9jww2Ng-eFOF0LL9rAvc3CN7novnnuV4c90JqPLx_EbkQ32OpQSxAE5RsPZEf8PuhTdoEtMI92jDtXnqdbmxs2O4MxsXohHaiuORV6j7tm9DmgZK0wqnASPq9Cw756nGIbk0NvtskuXLF5_xfRoJTKfsR3dqd1JlFHkcHRK3B3s8SjgPLSeVP06JadhGY8SqwYtuDmyRsHNWOeEXQsT-tSNOfsS-oSemZT36tlh_0Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/As4bmXZSm40Cf9BziJlaYTGT5KHHwwQgBiYJ2RlQUP1IakA9nHplswGRcDA-VnPtto3ZCLbm3n1x1rZ5OgozsAquriZYDE53scDM-7F85fZz1Erbc1NAHxBl_xkU4kbwlpShBiATXg1cWNpZNq09deiPzbHrN8UAl5mN6VWt7CtpeRdKUXkVDwDLnN0qyPzGkZs3IGnsk4kNQhyS_Hc7n6EvcfYQ11e7HJV7HN3U4TfKx00gzuUVw18JyX-TUxCbxlXhtzskj9OLVYWICYCiMakb7BuuPPqq35p3lTbscBTHvECZ2YVexhm2jtcfG4Mgok49idadNI61K1ZPFrEDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=VayvG5wCA9tqjK9Zd9pM5WwPbi3YvIZMyr0FOHI-f23k-dge-1JpFQtKhYyMwyaqrriCILDzTWtXwO9qYQf2CJ8UJCydGqFB6MC83vswJuzQbSerz-pFoGFNSUPSzcEUpWDyr9ZgNvP9S2ia0XsC1gu40YmR0q_N1Hmfu_4dH60jJjwYCRZTG9g3wP7G3fN5pyyEZKTQCIT2noD01MnWmUZABq4xYFPqpn1TPijcpAFn2I7Rd7SfyQeeMeV4BBw1mEkIpuTyB8OCeuSrdECdqBn2SyWOKeF8O2aCjh9_APIq73Ub-X7imIcdJu5dKx0CcB2eNBpzqxlS_WBvLSqNCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=VayvG5wCA9tqjK9Zd9pM5WwPbi3YvIZMyr0FOHI-f23k-dge-1JpFQtKhYyMwyaqrriCILDzTWtXwO9qYQf2CJ8UJCydGqFB6MC83vswJuzQbSerz-pFoGFNSUPSzcEUpWDyr9ZgNvP9S2ia0XsC1gu40YmR0q_N1Hmfu_4dH60jJjwYCRZTG9g3wP7G3fN5pyyEZKTQCIT2noD01MnWmUZABq4xYFPqpn1TPijcpAFn2I7Rd7SfyQeeMeV4BBw1mEkIpuTyB8OCeuSrdECdqBn2SyWOKeF8O2aCjh9_APIq73Ub-X7imIcdJu5dKx0CcB2eNBpzqxlS_WBvLSqNCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 487K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_8OpLlafk4D9DF_pnKBm_8SgMtxDDyLu5f8UGcfKnXLq64Qtd2y-RGjweJMMfeg0An2xFHU7lHBHiQNMTwh9ZU-_QXSkc4lPyRtuehpCLCS2sqoS7fVzFBCmRN_N7ISf97xDpo7LAUfyLMufWnj9rYCQV1ZXgGcL1c1MN3vJzRpYK3fTy-fZj05AIyUEP6pEFHO25MXT9P2ZEw7oaWachP1OheANurml-UixjyCWa3rE0P9rZeu3xy-JYOZXdHFO7OvQmYEkCQEbV4Cr2Ws2eu--2ktd8mk2PkwC8-sQgWhrD-hhIHrnUh2m2GQ2-8ih0qIxaEIJPFajN44VYNQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=STnu1wU94JPYPfq0nzNfwbWaRCjsLcSu5HnvcECqRljEAa3UbFUGaxSOR4syMstTObu6o5SiyTtheKRmp5mk92R-wBPZjT1UxZerHsbqJWsMkJdv592ELJnz5I1iakk3SxKUWUWjwzOADspOlzBzXo8URf5l4y9SLc6UG9xSpvpn0bx8cREAL7fhKn_Oc45yJI_YxelLDdM5c7_aKE-t-FHhKRP0a-j1IYIJ9Yk2RNWp2YRZZQyKEsENUetv1EJdxpN3w2n53HVfXqXJXcExeMXixHAimWPDnTqgReFErTkD00UMMXecJ8UDWahbAticG7VQl-QR906VdhPjOA1dyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=STnu1wU94JPYPfq0nzNfwbWaRCjsLcSu5HnvcECqRljEAa3UbFUGaxSOR4syMstTObu6o5SiyTtheKRmp5mk92R-wBPZjT1UxZerHsbqJWsMkJdv592ELJnz5I1iakk3SxKUWUWjwzOADspOlzBzXo8URf5l4y9SLc6UG9xSpvpn0bx8cREAL7fhKn_Oc45yJI_YxelLDdM5c7_aKE-t-FHhKRP0a-j1IYIJ9Yk2RNWp2YRZZQyKEsENUetv1EJdxpN3w2n53HVfXqXJXcExeMXixHAimWPDnTqgReFErTkD00UMMXecJ8UDWahbAticG7VQl-QR906VdhPjOA1dyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbcv_rGoPLWlPiVOiLjRTLemUVeXUs-TxLTwR-MdsjL5P9CRl8Tr67H_fcnILFgoCSYvEFTPhXVhNHlGrHXk9YTioL7EnFINDXwzFwbo7X4yx2MT_UbHQFVtcqXIexqYkluS_su1dz31l59ejYhs4bK4ECYIXfMRycVSZ8Y-jAiwWXLfmDU7TLTiAR5SbFG7J4x_404319-gQWjXvaPBtsiiUGxN0YC67f_swXygzbDtFEsYQJcydTCXMyraKTSFToDgnb78sY18GI4_T2JUMNepoYv9UCcXl38gylWYhqkQ2T4t1HFP9JMQmcAPd-VXmc1X1AlIPFuTIzY76evtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkgXtrOFkM_Hd0L3niP-5zbrtktdun0uorWbHJGVzYk_Nr5SQKlPawY9lfI9RKKt4hneGBb-KAUlKD5y8YVSKDASejJFTaYEf6N1aEkmxNdGhK7igUv8uepxVr_1f8RM8Yb_5lU4YmvsAaukCudt_2ryOigh-Dg0o6yKRriSjrKV9vyG52WcDZkhnUPotkob6M_PgX364_-TPKAAZeIEBsjmuhZjxcK3k2IyVfnh2MNgV5SCZZDVq_u3c6GThPKFoR03uaLSmvBzbgrc5bk5YD2DwKJzOWiEdGd9hAnIcpji6MLgzZSz7iRnPDzZ06T1rKZNybqb5KyL2X-42QV5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
