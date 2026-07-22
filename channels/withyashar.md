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
<img src="https://cdn4.telesco.pe/file/Ag9bJ44kEhHJJKQTg5GoERrbNhyjLUWH58OjCMtICRpGu_8sN3B6P1KqQXXEfTdPLnxt0xtFVhWWgzkEbu2bl--c54MtttYwvAIaROR1jjLejLeF6WZl20pEydiHJw0-x3fSyr3OzMqMi6byNB5lU4iyFcp2GWUB2iJKwCbaRz4dns-M4VgzG6a2TPFM4Pcomkq0OnElZ9f9dwuc2ryRmMoys3sBMWPO2Zd_GTVyjcrPVDZ2UYfBuqtXyKHWxiIIOLBxQ7XH1kdB7ByGz0FYWN4zF4ohHz7QgMKzJ2sxrRMZlgClf8KEeXi4oNIr4QCXH2PSnLyLSCF944QNVPYC1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 419K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 08:41:34</div>
<hr>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسپانیا ممنوعیت پرواز بر فراز حریم هوایی خود برای نیروی هوایی آمریکا را که در جنگ علیه ایران شرکت دارد، تداوم بخشید.
@WarRoom</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/withyashar/19288" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/19287" target="_blank">📅 08:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=t5jc1uPmLrIes_nnr4SBHwoW9fgu8i_vnQ1gP630UFmttucF10hX-6tTYOtSdidyDJzucEpW6bqm5PnjGqBtan0R07iU265ZNxopisbCrhG732SX60_lFpQ_q2CTwI-tT6rRiKEV4YBHg8x5haeCKmjfv4_6i8-hAg_9PE0x3SuvJiACn83T_J7S4jhHzLuqCWhytSKmLxyEnl6k89JboRkyTlrM9aPDrY3f0PrOvdnjf7wwWL9KGshDeRS1HjPW-WGkeLJm-xHGFFgN3n_FStQJkNf-RSkzwFRuADty3Xx3Te3kmUZkez4TCE51RGgGIA2V9R8taScMlnN2xBb69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630b6aa1be.mp4?token=t5jc1uPmLrIes_nnr4SBHwoW9fgu8i_vnQ1gP630UFmttucF10hX-6tTYOtSdidyDJzucEpW6bqm5PnjGqBtan0R07iU265ZNxopisbCrhG732SX60_lFpQ_q2CTwI-tT6rRiKEV4YBHg8x5haeCKmjfv4_6i8-hAg_9PE0x3SuvJiACn83T_J7S4jhHzLuqCWhytSKmLxyEnl6k89JboRkyTlrM9aPDrY3f0PrOvdnjf7wwWL9KGshDeRS1HjPW-WGkeLJm-xHGFFgN3n_FStQJkNf-RSkzwFRuADty3Xx3Te3kmUZkez4TCE51RGgGIA2V9R8taScMlnN2xBb69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو های حمله به پادگان بخردیان بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/withyashar/19284" target="_blank">📅 08:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avJGVKfPuMADOP2h2fc2anR7I5RNc0wfnGLs9gtU_Rb2X-zx27i7kfsNIJ_4rah-P3IRBvZic7UtAVHpD1nmuOmBQtNyQUNQEMrIRwD54eUuMmmgavwOeuvHLFRcO6oxhnhwDeXTVYrSxVzTZY7j6DT3yycOALkn4npNSJwwUhBXedBE1QbluvP0N699wAKRyvVmSQmv28cgRVMlQG7Fp3QSqec9Q2Zsk0jeZQSDgtD5PVQAsfkxaEIn-ZxMe1tM8lxjo-cQn0PB_5OIA25xud4AgKJldViQuobNSYDTBOhuk0rvgZpyM6HwZuWAcay_2jc1YvNy5eDRnIAhUptFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-XF7p9vkSNu5QxvZBfEsFhd4be1Z5b5j7q5Rbz5XGdkG5d-CwN4OqUgyieP8aJwwI4XAbGif3fpmrNgUgvmQN09P8IJLGW1v7cEe2bH8zF6YHyg8bDHgqXxcrvDqHYmSg8CVMf1aAtrWgIYEaiN6kIbNsaQ4CSOZM3m3Sv-w9nRfAd0B7iw_M1zXKzs0z_dgtGHK4BERb3ftxKfM6gbWMVUG3YBr1CENOOXQEWsKGV-0Ta5bMXQnk67pdXm-nT4SglWUtdpJfGEWaAH7MTdyfOm_evs0bY59uQKe01cxWkmfiIfNLj82iD6w_UKsfKPdAf3UKZcuGkGiek39jj6xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند @WarRoom</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/19282" target="_blank">📅 08:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kacCWa5JtlXlNYsNmPwvDqqkoaTOGGQvpNZmiHBj7XKvGSc9p6xOz6chdez_VMHfshwfPRgsDKOPFtg-VJrjl-FT_Y_LavBti7h_aPU76KQBMhe3mLT2dqeTwzDChB-B64Jl7J2oHfvhrr7B3GRhkqcHv0e-fpD2zxu7NikeJ2GT-8OTgLxZWm9a16aKKR_JSPgqvoA5p81n5Te8SDsiv8mLjNgHOSji5bh-BFdizGNODDzbVVVy6saB2xzkXp3XJwZ9aGEW-th5sY0lB_8yLMaeieShgfsjuuM7XDohnlj1Kx_eNi3Yzo5aWjQQuNB18XC1OMLZGj-HCkrLmtCeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ارتباطات هوایی آمریکایی مدل E-11A BACN (روتر وای‌فای در آسمان )از آمریکا به پایگاه هوایی رامشتاین آلمان رسید و احتمالاً در ادامه به پایگاه الامیر سلطان در عربستان سعودی منتقل خواهد شد، جایی که در حال حاضر بین ۴ تا ۵ فروند از همین نوع هواپیما مستقر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/19281" target="_blank">📅 08:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت. @WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/19280" target="_blank">📅 08:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار بامداد امروز در نارمک تهران
یک انفجار نامشخص باعث شد میله‌ها و ورق‌های پلاستیکی به اطراف پرتاب شده و سه تا از شیشه‌های خانه های مجاور شکسته و به خودروی ام وی ام پارک شده هم خسارت جزئی وارد شود، اما حادثه مصدومی نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/withyashar/19279" target="_blank">📅 08:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فهرست حملات آمریکا در بامداد چهارشنبه
💥
سیریک (هرمزگان)
💥
بوشهر
💥
بهبهان (خوزستان)
💥
امیدیه (خوزستان)
💥
تبریز
💥
چابهار(سیستان و بلوچستان)
💥
کنارک (سیستان و بلوچستان)
💥
چوار (ایلام)
💥
آبدانان (ایلام)
💥
بانه (کردستان)
🚨
تهران: صدای شلیک پدافند
@WarRoom</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/19278" target="_blank">📅 08:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cb529807.mp4?token=ObyTX6I-HohtwlEuQ6-aMwJZg7M8hqGRjIplo5zlhjKmm2SHbUH8BF8qyirCJyuB36L6Ux7ouMVkdYtnOGcOv898zTlRzrwkNHxK4Qb7yRPSkG8EhYI1FAnq0IFy-NyiD0GlAeXRW33zQV-kgKM-ns-bn5327XRfSw97GTsSGxGy6tsglVedhp0uWzynMUWftU892fZP0UtxmxB2VOlGGEWR6A7qIeOEM1GQF-GntAIiTat7_a3929NsudtuFfXc8daCS4vzSVALilvHjYFUqTyzddHbr0Dk4ccaFnW1ERCTj9odyRVilN3PlXV2LBvwxTlMkcX5iQXQlXMX3eQjzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cb529807.mp4?token=ObyTX6I-HohtwlEuQ6-aMwJZg7M8hqGRjIplo5zlhjKmm2SHbUH8BF8qyirCJyuB36L6Ux7ouMVkdYtnOGcOv898zTlRzrwkNHxK4Qb7yRPSkG8EhYI1FAnq0IFy-NyiD0GlAeXRW33zQV-kgKM-ns-bn5327XRfSw97GTsSGxGy6tsglVedhp0uWzynMUWftU892fZP0UtxmxB2VOlGGEWR6A7qIeOEM1GQF-GntAIiTat7_a3929NsudtuFfXc8daCS4vzSVALilvHjYFUqTyzddHbr0Dk4ccaFnW1ERCTj9odyRVilN3PlXV2LBvwxTlMkcX5iQXQlXMX3eQjzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :
امروز ۰۲:۳۰ بامداد
۳۱ تیر به وقت تهران حملات خود را آغاز و ۰۳:۴۵ بامداد (در ۷۵ دقیقه)
با موفقیت
یازدهمین شب متوالی حملات
علیه ایران را به پایان رساندیم.
نیروهای سنتکام
مراکز عملیات نظامی، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی ایران
را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در
تنگه هرمز
بیش از پیش تضعیف شود
@WarRoom</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/19277" target="_blank">📅 07:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19276" target="_blank">📅 02:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میرم بخوابم بعضی ها لیاقت ندارد انگار خرج منو میدن نمیفهمن این گزارشات بر پایه پیغام های زیاده حالا حمله نبوده باشه یه عنی صدا داده که پیغام دادن این همه آدم ، شب خوش
🙌🏾</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19275" target="_blank">📅 02:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش صدای انفجار تهران نارمک
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19274" target="_blank">📅 02:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش انفجار ‌بوشهر
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19273" target="_blank">📅 01:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uE7wr9PwAGt8EB-4h44u1bsZUq7ivoSjORxlG3uo-0zjEdbIo1KVnV0Kqjg2uCerPjgp5PTm_3lPcRrXdjHSnmA-RpyNzaPTCO2TP8ZwXr7T_VVcBY_E4-_7D7U9k6M7AESZCcWzIY6uuzRETClcY7yS6GPb2W4nNGzJ-_HE78nbljgWuGp6rE7hqyOdg8QGk-hEUWAekMZ2oCppzWZyC9k3ZfMzGyio5---44-zveKL4E45HNCwh5GvCGpRnrdYHh-61YuxlfyZ93hm6iKKmVpWLqIpaSKhR_jNohrq7-bgsZx4qw-v6gHBUCX8gmZ5-1H3xhBAF6oqgzVkhCoP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲-۶‏ فروند وارتاگ A10 با کیت جدید سوخترسانی هوایی بر فراز مدیترانه و در حالی که به سمت اردن در پرواز بودن از صفحه رادار محو شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19272" target="_blank">📅 01:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش کویت: پدافند هوایی در حال مقابله با حملات پهپادی از سوی ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19271" target="_blank">📅 01:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش صدای انفجار / درگیری پدافند در بحرین
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19270" target="_blank">📅 01:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جمهوری اسلامی دید امریکا نمیزنه خودش شروع کرد ، از ملارد موشک الان پرتاب کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19269" target="_blank">📅 01:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvw_q3ulcq5y8DxcXBGiF0mvhiVW_h78xpO0YW4nbGe9CpDeI668V2apgAMS9h01v8uxqOvS4_C7St86bAVadqKtr70t7IGpGEeQp1AukTKVIsR0jeCCGnLUoyO5hdRIhJ0FY3l0Ao2A5C5czRC7eO7S27O_t3YuWYtb_oYr2ic78mXxmk7N5XV6vlImvomYZ2F5DxMLf6RmsnM45E95Y3tXBDwscE3dnYcCvXvQRZ2AygUv41Kd-sbg6lbP2a-1Bi7dyHks_OZdCdEiATow0ba8wpq3fkyxekciAT0DQpv5mky-EOHHcTRQ62fjhajEE1-lM01EUMcmJ2gDfvFDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوأل امتحان تاریخ سال ۲۶۰۰ شاهنشاهی (۱۵ سال دیگه) امشب اینجا دود میشه
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19268" target="_blank">📅 01:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هم اکنون ۶ سوخترسان از اسرائیل بلند شدند و چند سوخترسان به همراه هواپیمای  آواکس از سعودی @WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19267" target="_blank">📅 00:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکا مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است اعلام می‌گردد چنانچه آمریکا وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم‌پیمانان و حامیان آن ، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19266" target="_blank">📅 00:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19264" target="_blank">📅 00:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19263" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیشترین کمکی که شما به من می‌کنید انتشار این پست است. حتما مطمئن باشید چهار پلتفرم را فالو داشته باشید
🌐
instagram.com/yashar
🌐
t.me/WarRoom
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19262" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/19261" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19261" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هگست وزیر جنگ آمریکا در سنا:
آیا شما می‌خواهید که اسلام‌گرایان افراطی یک بمب هسته‌ای داشته باشند که بتواند کل جهان را تهدید کند؟
@WarRoom
یاشار : عمو هگست داره سنا میجنگه پول جنگ رو بگیره امشب</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19260" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p83K8kCa2mJAgNdf3mzoKsM_uOUvWeBFCGVO7mcBHkhAFmtT6M4y06zgVIOFyFuIXZ6Qd99SBliKbG-qfPWtbTTAjwV5HxfazVkxIevQLgLdVOiEKxdib74sF8PbIgTkqep_3aHZ3y1idMX5_mSF9kghc4181uso7UZJ4P1bVisp98My974PuFPkyMWetIeMciQn5JFB0-AAPq6t1SeVwPPVKDaGS9ZM7QOUkepLfpjGZSUWogSUxZAJrHmf4_T-LPAYSTm_zn9fgdZcT25piAYQPInkY6yMsmYuAeIgUw8R-hjfutyJ6TTMNbqzBDlNQ4luYqrKDT-mbp-uFKeMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۶ سوخترسان از اسرائیل بلند شدند و چند سوخترسان به همراه هواپیمای  آواکس از سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19259" target="_blank">📅 23:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
کمر بند ها رو ببندید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19258" target="_blank">📅 23:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTMyIFBovUroL5B1mikrkHiiqNpM-5ubCJjce14NU5KO5q4ELIJ-bcXedf8L-hAJ55FYDI2CLqw2PrWOEYnnYt-RA1gPd_mwvdr7DonPotDxXgdu5p42xIeo2jBi1HUusiC5hkg5JT7Uc50AGKV_mh0YDXgf2zS1J88iJ6hr1RZ1tg9Tn4kIJanNg2xNz_PZmrjTgtKrCSyOS2olCMEalvEzkU55sOPfIvhR3kw1ANMubNdUYoyEe1C9SutPIhQWAO8VaSTPvPg7ryu-M3xz0HyNO2nFPCLTMo8WA3oWzWtFuFpzdOYShPMTKlss0N56Mf7ogmdFebuPAeFNLCs4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث:
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
جنگ در ونزوئلا: ۱ روز، صفر کشته.
درگیری در ایران: ۴ ماه، ۱۸ کشته.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19257" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیت هگست، وزیر جنگ ایالات متحده، در جلسه سنای آمریکا به سوالات پاسخ داد و گفت که جنگ با ایران تاکنون ۳۷.۵ میلیارد دلار هزینه داشته است. وی افزود که بدون افزایش فوری بودجه، کاهش آموزش نظامی ضروری خواهد بود.
@WarRoom
یاشار : فاکتورمون داره میره بالا
🥴</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19256" target="_blank">📅 23:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19255" target="_blank">📅 23:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
@WarRoom
روز ۳۱ تیر</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19254" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7699bf9bb.mp4?token=sytmry4LC1KrvNLWVUlq1hnsgybVpOyyu_fA8WEiMtmuJU2Upl1j2vyrrxvPHZ_GbaZ1mzmdvlfpvAwH6VyiUAKOJFXNoR1LA9-CSmbF5hV25I98D1BaXSgxncmsLcooeUTvT2maBU2jOYElrEsxsdylgBY0t5Cl1kH2eSmX6QL2gBHMYX8CwBaWsfWB8iTZ71ejP7vVSaIjrE5ald5qw2W5ZeAJ6cPw01GgO87AQ70L-IcwGKx7pPRQvdr5_4451qEdOdhmxDWUn4q_bby673VIf-CSBctGJtIFODar3U_SbCvZNEd_Rx4XG9i0uagK1qIMKWAzP7wXXrntAfm1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7699bf9bb.mp4?token=sytmry4LC1KrvNLWVUlq1hnsgybVpOyyu_fA8WEiMtmuJU2Upl1j2vyrrxvPHZ_GbaZ1mzmdvlfpvAwH6VyiUAKOJFXNoR1LA9-CSmbF5hV25I98D1BaXSgxncmsLcooeUTvT2maBU2jOYElrEsxsdylgBY0t5Cl1kH2eSmX6QL2gBHMYX8CwBaWsfWB8iTZ71ejP7vVSaIjrE5ald5qw2W5ZeAJ6cPw01GgO87AQ70L-IcwGKx7pPRQvdr5_4451qEdOdhmxDWUn4q_bby673VIf-CSBctGJtIFODar3U_SbCvZNEd_Rx4XG9i0uagK1qIMKWAzP7wXXrntAfm1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : هر موفقیت عملیاتی در خاورمیانه با تمرکز اعضای ارتش بر مأموریت‌هایشان بدست می آید، از جمله محاصره ایران توسط ایالات متحده، آغاز و پایان می‌یابد. تا ۲۱ ژوئیه، نیروهای آمریکایی ۸ کشتی تجاری را تغییر مسیر داده(۱ کشتی‌امروز) و ۱ کشتی را غیرفعال کرده‌اند تا محاصره را به طور کامل اجرا کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19253" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بمب اتم بزنه به کمر کسی که این خبر فیک رو پخش‌کرد !!! نترسید الان زمان جنگ جهانی دوم نیست ، جمهوری اسلامی هم امپراتوری ژاپن نیست !</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19252" target="_blank">📅 23:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19251" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من چت جی پی تی‌نیستم دایرکت ندید !</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19250" target="_blank">📅 23:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏بلومبرگ گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده آمریکا از شماری از پایگاه‌های نظامی این کشور برای انجام حملات علیه رژیم جمهوری اسلامی موافقت کرده است.
@WarRoom
عمو عندی
🤣</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19249" target="_blank">📅 22:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19248" target="_blank">📅 22:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏گزارش‌ها از پروازهای مکرر هواپیماها از فرودگاه مهرآباد تهران
@WarRoom
🚨
🚨
🚨
تخلیه ؟</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19247" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0298192d9.mp4?token=IyLTPerlabU9sbOPMnhNbiT_kXFws5rnPcL1qMdaRoiKyCXMZ-EgsXl-lnc_n7uCQhtXnxI1ldRhwRoKvLQaIGpPTIeJR0GaduwNQgyWnx9ljv2e4JEBp7axSHGBens7PhWGKM32HkQTOOAdG-tlw_FLPw55QaSMzquEg6mhP0rzzuG7ujWDod3q-nMv6bcXnnClF0KeHuesVcLpKhEGF_oL2AHbdBWX8m0rmn7PF9NoIy_6DJngwjyb7MqHk7N2w_cY1kR-NaZb-XlcGq5nJ_GGD6Ps4c24hkevcQlsK988PcpD5E6QqwU6XwWvTMzA28_UPxkDhlPT0OBiARhk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0298192d9.mp4?token=IyLTPerlabU9sbOPMnhNbiT_kXFws5rnPcL1qMdaRoiKyCXMZ-EgsXl-lnc_n7uCQhtXnxI1ldRhwRoKvLQaIGpPTIeJR0GaduwNQgyWnx9ljv2e4JEBp7axSHGBens7PhWGKM32HkQTOOAdG-tlw_FLPw55QaSMzquEg6mhP0rzzuG7ujWDod3q-nMv6bcXnnClF0KeHuesVcLpKhEGF_oL2AHbdBWX8m0rmn7PF9NoIy_6DJngwjyb7MqHk7N2w_cY1kR-NaZb-XlcGq5nJ_GGD6Ps4c24hkevcQlsK988PcpD5E6QqwU6XwWvTMzA28_UPxkDhlPT0OBiARhk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم منتسب به حمله به سفارت یا نزدیکی سفارت اسرائیل در بحرین. خبرگزاری رژیم فارس هم این را تأیید کرده.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19246" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">BiBi joined the
@warroom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19245" target="_blank">📅 22:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گروه‌های کرد اعلام کرده‌اند که به مقرهای آن‌ها در منطقه دارشکران در اربیل حمله شده
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19243" target="_blank">📅 21:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر جنگ اسرائیل: ایران تمام فرصت‌ها را برای مذاکره داشت، اما این فرصت‌ها به پایان رسید
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19242" target="_blank">📅 21:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:ایران هنوز چیزی ندیده است،
به زودی اقدامات بسیار بزرگی انجام خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19241" target="_blank">📅 21:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام ارشد امنیتی اسرائیل به شبکه 14 گفت:
«ما با روزهای سرنوشت‌ساز روبرو هستیم. هم ایران و هم ایالات متحده در حال بررسی گام‌های بعدی خود هستند.
نظام امنیتی در بالاترین سطح آمادگی برای هرگونه تحولی قرار دارد. ما تخمین می‌زنیم که احتمال وقوع جنگ در آینده نزدیک حدود 50 درصد است.»
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19240" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">موج جدید حمله موشکی ۳ پا ، گزارش صدای انفجار در اربیل عراق و بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19239" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efsHj6JeFBQPG4RvPsR77JmfIJo6jbnSyU-ji6pEmUdxuBaHU9m_D5SJX59cQ8eouxte9VmCk0L_IqthmmNJvueNxNpuxyOB4Ja5AOZ2OTaOBDzSA7hX3PJSnwyjMNFI8vd-OVmymvpp97-SXYY3f3yrDKj18g6TvR8PDsF-MW1OiOYZvQZiaDcuNr0e7J5nCcliu4gABwEfQmECa__FcplYnMWO0IbqOE6ibJLgH83iL6rXoVD8PjMEPzdC1DKyEpNRwdvFPH2SpOzIQGOwFoLDzQTu9DNc_Nb8nSgHF8suQ3W1ap1wpaRdi5TC4r_Zj3Zql1zWAyPkIM-llx6mLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6473d165.mp4?token=OUPM-dgnXIDzUvChcyw0PuskTqRCVXbzvwjawd1743Q0u9Gx-EveSYs_SUXxnxWzIiizna5YEds3rLuEUJVcANwkK4dm6SvxawDUiDPg943YgzBLgvuo_i4fVaCL_44T4AysCUKAolqLssUUSDHsF8GTVCprrYCrh0be2-aTDIm55p7MwEkrxUHk6e1aM_SxeEixs3sfTQWDes13XiwIjIw1tgxXLkjS5L7XlxOFVLukoXOBse1Mb5QqI2szzFhBYxpQDKnXxvAX59czjRpTL9zgQhRVTUua-HSyPmrSLXbme3f_tQEavSgEfcpRgXkwoUxkHUiRDXkZQvphrSXI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6473d165.mp4?token=OUPM-dgnXIDzUvChcyw0PuskTqRCVXbzvwjawd1743Q0u9Gx-EveSYs_SUXxnxWzIiizna5YEds3rLuEUJVcANwkK4dm6SvxawDUiDPg943YgzBLgvuo_i4fVaCL_44T4AysCUKAolqLssUUSDHsF8GTVCprrYCrh0be2-aTDIm55p7MwEkrxUHk6e1aM_SxeEixs3sfTQWDes13XiwIjIw1tgxXLkjS5L7XlxOFVLukoXOBse1Mb5QqI2szzFhBYxpQDKnXxvAX59czjRpTL9zgQhRVTUua-HSyPmrSLXbme3f_tQEavSgEfcpRgXkwoUxkHUiRDXkZQvphrSXI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر لحظه آتش سوزی داره بیشتر میشه آمبولانس و آتش نشانی به اون سمت میرن
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19236" target="_blank">📅 20:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/traycp9tAzTWUdzSA_JAkBuBMv3wvzznLl8cvn2muRwPx5ErQnWt7s-nCYvVv9zQ5yosAxx-XJZu0hbigwd5h9NVe1RbHXhdjGwkUMLvfeczG8KYc8hmq6_nc0hYhFCgQq425H1Gxkf4HLRzqjvSI3TYmE9lRVPp_q9_hutU6gszJn4pG8RjadkAFWV0g5g-PweWINdODs3K30Xa8AbmZQHNR7GC2c-6Fnp0VDUUZZsoGMZuRipARkPZm5wh-sEUgk2wJ5BJFHVParau3f9IgRgKmFqtXoyewCAsPJ9rMyc6TXaAkMQW-IDP2_5xyAZxABp9YG6JWperUxPG_8Crxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/212322f58b.mp4?token=ksuYsTBjXhy1pRGWA4jrLTERLbqzxS2Cb41ewbxtpk2uhGo9cdEQilVOaed8ZbGY-U33ULZuD0lk6wncfeAJvU-JfLoQZy8P2omjYKpJuA5pndYnShcZVpz1CPfRFLW-wMem0R2Ep1VfxIQg3GRRq2gjipVDjlByZeqzEUFAcGN81_xRvYRVSY79OufKDWzmxD9SA2goiysUA_7n-jSqZrvWAtfXsCAqHiwTsZK0-NN_brASrpklwsYaWOdwcSG2KgE9gQyRAwYgWe3O-N3fP1IoGLQ0RylN0caOdbjEEzIPf9Sea2bYzxVd3lTCXaScS5V6AAt1ymuKe4qYQMRVVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/212322f58b.mp4?token=ksuYsTBjXhy1pRGWA4jrLTERLbqzxS2Cb41ewbxtpk2uhGo9cdEQilVOaed8ZbGY-U33ULZuD0lk6wncfeAJvU-JfLoQZy8P2omjYKpJuA5pndYnShcZVpz1CPfRFLW-wMem0R2Ep1VfxIQg3GRRq2gjipVDjlByZeqzEUFAcGN81_xRvYRVSY79OufKDWzmxD9SA2goiysUA_7n-jSqZrvWAtfXsCAqHiwTsZK0-NN_brASrpklwsYaWOdwcSG2KgE9gQyRAwYgWe3O-N3fP1IoGLQ0RylN0caOdbjEEzIPf9Sea2bYzxVd3lTCXaScS5V6AAt1ymuKe4qYQMRVVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی کوه دراک شیراز ( دیشب حمله شده بود به این کوه)
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19234" target="_blank">📅 20:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هم اکنون تعدادی از بمب‌افکن‌های مخوف آمریکایی مدل B-1 از بریتانیا خارج شدند، همزمان با اظهارات ترامپ مبنی بر هدف قرار دادن کوه "کلنگ" در ایران. @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19233" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هم اکنون تعدادی از بمب‌افکن‌های مخوف آمریکایی مدل B-1 از بریتانیا خارج شدند، همزمان با اظهارات ترامپ مبنی بر هدف قرار دادن کوه "کلنگ" در ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19230" target="_blank">📅 20:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19229" target="_blank">📅 19:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ : ما اصلاً کارمان با ایران تمام نشده است،ما در حال حاضر قصد ترک خاورمیانه را نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19228" target="_blank">📅 19:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19227" target="_blank">📅 19:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سه فروند هلیکوپتر آمریکایی در خاک عراق توقف کردند و سپس به سمت اردن حرکت کردند. این عملیات که شامل فرود نیروها بود، حدود یک ساعت در نزدیکی مرز الولید به طول انجامید.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19226" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ارتش لبنان را در منطقه امن مشاهده کردیم که با عبور از موانع در منطقه زوتر شرقی، توافقات را نقض کرده‌اند و به آنها شلیک هوایی هشدار دادیم آنجا منطقه آزمایشی نیست !
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19225" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا: اگر ایران به حملات علیه نیروهای ما ادامه دهد با قدرتی ده برابری به آن حمله خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19224" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: محاصره دریایی اعمال شده علیه ایران ادامه می‌یابد. اشخاصی شرور بر ایران حکومت می‌کنند. اگر به ایران حمله نمی‌کردم و از توافق هسته‌ای خارج می‌شدم به سلاح هسته‌ای دست می‌یافت. ایران به 20 الی 25 سال زمان نیاز دارد تا آنچه ویران شده است را بازسازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19223" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:بدون شک، ما تأسیسات هسته ای در "کوه کلنگ" را در ایران بمباران خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19222" target="_blank">📅 19:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19221" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6046e4dc14.mp4?token=VRhaEhfLznHvoADWrr7BrNo07TokLxlsEKpVel3SYTu6_eA-SnqrQLZOYX7y51_ekhrac2VVfoKcpoS0fpbY8s-ySxNc1ZLZe0sC20egfHbxYraCJ0NdJKe57ggxPxmkOm3MaMMhIjpRdB-rwC9_y_6fSm9MhOG6DQvkxOik3U33_kEX9E_C_-ko93YOTKmQOHH-BDkc0q7svWK90xWCqMeS5RtIkRwswkPXrCns9fb71zfWH5qMRBKFh-g6oII9zsiB7uAsoLAuJ3WmuNYNe3YHvJb6jha7cXNpmTT9M25Nys4gJXF14X2tnQi-ZNJqqKMCoW22T-WqOiTLUCef6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6046e4dc14.mp4?token=VRhaEhfLznHvoADWrr7BrNo07TokLxlsEKpVel3SYTu6_eA-SnqrQLZOYX7y51_ekhrac2VVfoKcpoS0fpbY8s-ySxNc1ZLZe0sC20egfHbxYraCJ0NdJKe57ggxPxmkOm3MaMMhIjpRdB-rwC9_y_6fSm9MhOG6DQvkxOik3U33_kEX9E_C_-ko93YOTKmQOHH-BDkc0q7svWK90xWCqMeS5RtIkRwswkPXrCns9fb71zfWH5qMRBKFh-g6oII9zsiB7uAsoLAuJ3WmuNYNe3YHvJb6jha7cXNpmTT9M25Nys4gJXF14X2tnQi-ZNJqqKMCoW22T-WqOiTLUCef6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏پرزیدنت ترامپ خطاب به جوزف عون درباره جنایات رژیم اشغالگر جمهوری اسلامی گفت: «آنها کودکان کوچک را طوری می‌کشند که انگار هیچ هستند، انگار آبنبات هستند. کاری که انجام می‌دهند دیوانه‌کننده است.»
‏او افزود: «آنها مردم را کاملاً تصادفی می‌کشند، بیش از ۵۲۰۰۰ نفر را کشته‌اند و هیچ‌کس درباره آن صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19220" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ درباره ایران : «ما آن‌ها را در سطحی تضعیف می‌کنیم که هیچ‌کس فکرش را هم نمی‌کرد ممکن باشد. آن‌ها واقعاً به‌شدت در حال تضعیف شدن هستند.
البته آن‌ها توانستند یک مورد را از اردن عبور بدهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19219" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:آنها به‌شدت می‌خواهند با ما دیدار کنند. تا زمانی که برای یک دیدار معنادار آماده نباشند، ما هیچ علاقه‌ای به دیدار نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19218" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار: هیچ نشانه‌ای وجود ندارد که ایران آماده‌ی توقف جنگ باشد. پس برنامه چیست؟
ترامپ: شما از کجا می‌دانید؟ از کجا می‌دانید که هیچ نشانه‌ای وجود ندارد؟ چرا؟ چرا شما چیزی را می‌دانید که من نمی‌دانم؟
شما نمی‌دانید پشت صحنه چه گفت‌وگوهایی در جریان است. آنها به‌شدت می‌خواهند دیدار کنند تا تلاش کنند به این جنگ پایان دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19217" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامپ: «هیچ مسدودی در تنگه باب‌المندب وجود ندارد.»
@WarRoom
یاشار : پس اینم بستن
🤒</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19216" target="_blank">📅 18:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری های رژیم: دلیل قطع برنامه فوتبال 360 عادل فردوسی پور دعوت کردن از علیرضا فغانی به برنامش بوده سر همین قوه قضائیه تصمیم به توقف برنامشون‌ گرفته  و نباید اینکارو میکرد چون فغانی ضد رژیمه و با ترامپ هم‌ دست داده.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19215" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال 14 اسرائیل: جمهوری اسلامی فردا برای مذاکره با میانجی‌ها و تلاش برای احیای توافق موقت با آمریکا، هیأتی رو به پاکستان اعزام میکنه.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19214" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/674fc57c31.mp4?token=vjpH7XhyQGtcZPDplQjsw89dWPdqyiqILRuEH6pKS01TF_7JfJ7UiP5bhu2sRvKM7Fz8oJx6YAhBNMTgFzW6zQ16FqYE84kyU1N0M6kk7tPP-DqKZjvjmT7wkuxdstIkoU9lhHmYZgwhAOWtWg4ULQ2k-Q7XxmSMNlIWTq0IvHr2toQSwcZR5AsQYcewr_JAocU7Ol3HUopK7jEG59_4jegQb3alRfBqldRj2Bkgk63wFpTdDqjDEIwls9gC1fyiDeEDuXaqDhXZWuyGO_hWF6Lus8y12L_OdoJz_-m3n0zUJyIpAK_oVsfbyC3WIs2N-17KnQjy4ronYttPpmsI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/674fc57c31.mp4?token=vjpH7XhyQGtcZPDplQjsw89dWPdqyiqILRuEH6pKS01TF_7JfJ7UiP5bhu2sRvKM7Fz8oJx6YAhBNMTgFzW6zQ16FqYE84kyU1N0M6kk7tPP-DqKZjvjmT7wkuxdstIkoU9lhHmYZgwhAOWtWg4ULQ2k-Q7XxmSMNlIWTq0IvHr2toQSwcZR5AsQYcewr_JAocU7Ol3HUopK7jEG59_4jegQb3alRfBqldRj2Bkgk63wFpTdDqjDEIwls9gC1fyiDeEDuXaqDhXZWuyGO_hWF6Lus8y12L_OdoJz_-m3n0zUJyIpAK_oVsfbyC3WIs2N-17KnQjy4ronYttPpmsI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دارلین گراهام، خواهر سناتور فقید لیندسی گراهام، بطور رسمی اعلام کرد برای کسب کرسی دائمی سنای ایالت کارولینای جنوبی نامزد خواهد شد و قصد دارد جایگزین برادرش شود.
WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19213" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19212" target="_blank">📅 18:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19211" target="_blank">📅 17:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19210" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19209" target="_blank">📅 17:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با موجی از موشک‌ها و پهپادهای تهاجمی رژیم اشغالگر جمهوری اسلامی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19208" target="_blank">📅 17:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19207" target="_blank">📅 17:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19206" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19205" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آلارم حمله موشکی/پهپادی به کویت به صدا در آمد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19204" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBdcKNrjmk0QVqHs3VvsW2TQwrrlQC6ygRBMfnMgKCkEtsyiWeu0gc2gMPeZ4yvDKJKk_AaukyMsy4xC4Av6cQSoV_sCoQrafSC0gPaD_HUbMMhYzJ7cqNqeKZawU85yQi0slBIZW22KOIGeD1D9S3eq9vncObz8mSjTtZ3PUGVBMrMW0cwQOrjSI9AkoS_0Qtiho2Mu3vy06d0kJw3CA3FQjQuwFGx7MTe2W9RkV1KRLEi0OnHK2YVDVHK4NlqoL1HUQx5EawbjhP43j5lhAnr_Svtog7yOGKjg2uWACSujEw1b72TqkMMOgHHgYKZ9mSESvfxT5zHKI0q3iLmPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وزارت جنگ آمریکا تصویر مایکل سوینتون، سرباز ۲۶ ساله آمریکایی را منتشر کرد که دو روز پیش هنگام خنثی‌سازی یک پهپاد عمل‌نکرده متعلق به رژیم اشغالگر جمهوری اسلامی جان خود را از دست داد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19203" target="_blank">📅 17:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19202">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک حادثه امنیتی جدید در دریای سرخ نزدیک تنگه باب المندب رخ داد
تعداد کشتی‌هایی که مسیر خود را در دریای سرخ تغییر می‌دهند، به ۴ فروند افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19202" target="_blank">📅 16:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19201">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تشدید درگیری میان آمریکا و ایران می‌تواند باعث لغو ۳۰ پرواز مسافری اسرائیل در روز شود؛ حتی بدون آنکه ایران مستقیماً اسرائیل را هدف حمله قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19201" target="_blank">📅 16:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19200">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سی‌ان‌ان: هگست قرار است امروز بعدازظهر در برابر یکی از کمیته‌های مهم سنای این کشور حاضر شود  و درباره درخواست میلیاردها دلار برای جنگ با ایران پاسخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19200" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2LEQUvU10rhPVsADJSFXCkEx02dg96M-Hjs919A075GlkMIzDttQsNxyHT-AMv1nPvE8iVt2o4TrTm1BRsJ2yH2VWDZLz15DdJMLAOUObnP5WyCFRnh32nJAmrNgQGSgvu4ujVETlkl8Ps2nOhLtXSrgJrAAV3fpYRM-aQErg4qiEX__mtEkGL9qVDzOXT-IABR49LUhxAOjdAO6LRQajGGatOMGTLw540fdBeb-XXljpug_iJGHwtfeRSXDjAfVAQV6sowh6GnadD1hvWJZOM9hbeanKownS7aZEpe6-ATr6IMCmh97Fl9ONvnkl32GFZ0B825kn9X8GvaLezPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکس معترض گریان ایرانی را بازنشر کرد،نوشته روی عکس : کشتار را متوقف کنید
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19199" target="_blank">📅 16:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoUgdnEhL_8tst1wlUXFvG6vpQLJtJZ8oPGGRZ2prt8zQmtQ0072jJvxv9giHhbPriUs19S_IJN4n8pM0eR6JKy0OM1wc2pxPtwDY2t3OPgSdPtyGRy8gMD-9kRXOUeBeQawlp_PUEAxJCaaIGFcZigIdeLYBdBlYUNkPFjcIcN85qzf6PeWt6RrumtvLLC7jil4p8XZvkHyZeuqJF5CsqWgG3_RXpd58tcrHaEJELZ-Vg40OXKIZbwOpvmofOoPsnp2pNzrvJJUfbXrvYZ8MbLqY7XR3L6EwUTHJh-oNc2LekeEjxwU7FX27I1hfoRp_YtD1891FXoKBI6Y5--0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث:
آخرین مورد از بین ۵۲۰۰۰ نفر، به علاوه معترضین بی‌گناه... ای وحشی‌ها!!! دموکرات‌ها کی بیدار می‌شوند؟؟؟
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19198" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال 14 اسرائیل: در حال حاضر، آمریکا نمیتونه پایگاه‌های خودش رو در منطقه در برابر حملات ایران محافظت کنه، به همین دلیل در حال تخلیه این پایگاه‌ها و انتقال هواپیماهای تانکردار و اسکادران‌های جنگنده‌های خود به اسرائیل است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19197" target="_blank">📅 15:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پزشکیان: روز به روز ارتباطم با مجتبی بیشتر میشه و مارو هدایت میکنه
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19196" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5tjJlk0uRb6nCpw-yg9lzrhNzWqRqsVPFKMWCDoF_0Unw-E1-yGRnzP0299-1C12Rm83Lw6FMbzwooWUtXEe83DH0lsU79_B0N7E2dHYgDPEqwegGZiT-rNImHuTfbVPzJL0NJKPWAbaxVAA34-lMNjHndjlSMep2ik2BM9RLR_kOAxiKDOtgdOc4etS1IxElfa9cqTTKbShmBz0ZT7DB_g5aMoVzRADFqtmlOMNiR3kVBn-C_kh7wVpjngyJy5wYpNGzi7JmxlYFsU7HHN9eZzPN9lWl-5_6EC8forj97AT-yFjXqR3ERFtrrn0O_szDwlhQz9JTbZVck5RrZo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای کاربران رسانه های خارجی هم بسیار سوال بوده که چرا اینقدر به صنایع شیراز، صاایران حمله میشود. آنها با این عکس گفتند که پیجر و تجهیزات ارتباطی میسازد.
@WarRoom
اگه همین پیجرم درست میساخت چرا نداد به حزب الله که اونجوری لت و پار نشن؟
😁</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19195" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏جروزالم پست: جمهوری اسلامی از طریق میانجی‌ها پیشنهاد آتش‌بس ۱۰ روزه را به آمریکا داده است اما
ترامپ با آن مخالفت کرده و گفته که جمهوری اسلامی باید بهای اقداماتش رو بپردازد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19194" target="_blank">📅 14:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">@WarRoom
انتقاد محترمانه</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19193" target="_blank">📅 14:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دولت قطر با ارسال نامه‌هایی به رئیس شورای امنیت و دبیرکل سازمان ملل، رژیم جمهوری اسلامی را مسئول حمله به یک نفتکش قطری در ۱۶ تیر و شلیک موشک به خاک قطر در ۲۱ و ۲۶ تیر دانست و خواستار پرداخت غرامت شد. در حمله ۲۱ تیر، سه نفر از جمله یک کودک بر اثر سقوط ترکش‌های رهگیری موشک‌ها زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19192" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی لحظاتی پیش از حمله به مکانی در ارتفاعات کوه بالای خرم آباد لرستان خبر داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19191" target="_blank">📅 14:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : فیلمی با عنوان «بمب افکن شبح» که در حالت دید در شب به چند خودرو حمله می‌کند، وایرال شده. این یک بازی شبیه‌سازی جنگ است ، لطفا دقت بیشتر بفرمایید.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19190" target="_blank">📅 13:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3212047c5f.mp4?token=d1GXwtLX3yazle5kAP1I4TGZ9JMqGasSLE-uX7ubQ9cTm0zUtim2CUQpXEoYbjiAHzrTmssGKcg2XxOpsE-eT7WwkrPzSzViQFLH7-UztTlBBItooqDalPV0Fca9thheKEFdBl8GbNbqg5uL5CL87D4V-DpOxWn-KLw0eqd5tiKTisfpyiJ95PdeWarleTDrqCLx5mVB1ZEOxHe0K18F_fJufW0uKv1C_tSsiFeafYGM-R1JkB1LVEYRtMrmfzy9-45nXHYsWJ1MTAdy-ILMRtM67NTZ2WEl16EVyKGDDfia5QLnq9yz0Sod0hSXj8mICWim95cK_sD57mL6KujiQA2_1n7I7rUDZAN7N7YcjlvCAZoIoBLrqklvk4x75mFAF3LXmWlUPSb_Q7djo1Oovp5WiYXqNVci63h2OcVcKIbU6cRk3KwNr_j_KQMmWd3SQY7B5fhiYjcLuBmDGais79vj7PsqBcKPyDbdZGPruYb2vOsZkVqloQ75EuslvVEQUHVeb311S5GTyw7IrTGjQGmylBESw7EosxxbTkSx7lmaupYbYRP-T4K2wBKSXYHiWwYsUVx_TSDKWpXEhV_ax6aAjrJxDh7lB725XPQeo9Anf6CekPMK39YHD2xXWPIKBWjO9OZEYgrq8_xH6naKunAIgOmPEikUjBEvPzHR2-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3212047c5f.mp4?token=d1GXwtLX3yazle5kAP1I4TGZ9JMqGasSLE-uX7ubQ9cTm0zUtim2CUQpXEoYbjiAHzrTmssGKcg2XxOpsE-eT7WwkrPzSzViQFLH7-UztTlBBItooqDalPV0Fca9thheKEFdBl8GbNbqg5uL5CL87D4V-DpOxWn-KLw0eqd5tiKTisfpyiJ95PdeWarleTDrqCLx5mVB1ZEOxHe0K18F_fJufW0uKv1C_tSsiFeafYGM-R1JkB1LVEYRtMrmfzy9-45nXHYsWJ1MTAdy-ILMRtM67NTZ2WEl16EVyKGDDfia5QLnq9yz0Sod0hSXj8mICWim95cK_sD57mL6KujiQA2_1n7I7rUDZAN7N7YcjlvCAZoIoBLrqklvk4x75mFAF3LXmWlUPSb_Q7djo1Oovp5WiYXqNVci63h2OcVcKIbU6cRk3KwNr_j_KQMmWd3SQY7B5fhiYjcLuBmDGais79vj7PsqBcKPyDbdZGPruYb2vOsZkVqloQ75EuslvVEQUHVeb311S5GTyw7IrTGjQGmylBESw7EosxxbTkSx7lmaupYbYRP-T4K2wBKSXYHiWwYsUVx_TSDKWpXEhV_ax6aAjrJxDh7lB725XPQeo9Anf6CekPMK39YHD2xXWPIKBWjO9OZEYgrq8_xH6naKunAIgOmPEikUjBEvPzHR2-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای نشان می‌دهند حملات آمریکا بر ورودی تونل‌های زیرزمینی پایگاه دریایی گروه تروریستی سپاه پاسداران در نزدیکی کنارک متمرکز بوده است. به نظر می‌رسد این مجموعه برای نگهداری تجهیزات و زیرساخت‌های نظامی حفاظت‌شده نیروی دریایی این گروه تروریستی استفاده می‌شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19189" target="_blank">📅 13:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7RZgjTaOOMnlyrQSiGP0JBtCYgjRyZ6zV-DEQqK1OxvPdaNdTiOZFglXtjqJ7DdISe8cFiTCevavRe9gTtjugMsldxT48vhy4sM7V_v4QOPlHoaEYWDRHlgJZtxl74OOOLrzWICnuMo1gdgnvWGHSflG2TzMi2eaRQMhkHsxu6rOoKeIlRI0njYcc79hTMgzXQdh2ATR63crTCfrqCOfxnvq6lw8n23QTwEb-HLYDsYkaLTnqyIYOtFYJAj6oqR8Xm976qN5y2SPfOIl2g71G1hwFsFl_D5DO9Q_ppbYWgkocFzE1HtmQd0ttBpBb9_XkpxUXUYjuUpRav0vhOVMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۵ فروند دیگر از هواپیماهای سوخت‌رسان نیروی هوایی آمریکا احتمالا با یک اسکادران جنگنده وارد منطقه شدند و در پایگاه سیگونلا ایتالیا به زمین نشستند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19188" target="_blank">📅 13:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏وای‌نت گزارش داد مقامات ارشد اسرائیلی مدعی‌اند تیم جی‌دی ونس مانع دیدار نتانیاهو و پرزیدنت ترامپ می‌شود تا از اتخاذ مواضع تندتر علیه رژیم اشغالگر جمهوری اسلامی جلوگیری کند. عالیجناب نتانیاهو قصد دارد سفر خود را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تنها در صورت قطعی شدن دیدار با پرزیدنت ترامپ راهی آمریکا خواهد شد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19187" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرتاب موشک جدید از شیراز/لار @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19186" target="_blank">📅 13:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرتاب موشک جدید از شیراز/لار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19185" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پرتاب موشک از زنجان @WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19184" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ6Qaox7pG230l7OX-fnA3D2xS6l82jbNF9hVv1m1fVbPzJjETvMgkFV2pj-ub6eJYWYcfpQylp0LULbOOaor99as2n-H41upNv1PlDMhvh463NTvloWdnZoWKPJD0pO5MqVsgyVUut3tpKoR2j8N5IPPMawFV3_FRL7X5a2vZF1MBfBcDIGsPXX_f7VJrsozRWri7dDzbt1NzclvGzemgDAZeCBvEdfB2iFLQPZ_7DfU7TkkQvI5y5MgeJPrjgmYSXgpnS08izKLUK--axMJnu6JUEYIhP8joWGm_zJdrXc1ndUgsvIVLMBviGmo_YmXmF2m8EfWeSIQsUVhSkDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از زنجان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19183" target="_blank">📅 12:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارشات رسانه های عبری :
امریکا برای برخی حملاتش در خاک ایران از بمب افکن b52 استفاده کرده و همچنان استفاده خواهد کرد .
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19182" target="_blank">📅 12:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a274348cae.mp4?token=BBq8fNw15VTUO4J8V7uej6VZPmRWhPaUQTW3p1VmKTbyofskbateF121oglvGvjcaVCPlIETcfCwvisdPRYy9VGut92fa3n-ZTIOUqOuWhdtMfeP_69vqfOA4eXvbLqakR1Gbzfl2q3NLSkcw0ghLLSTfE1aj8ImptRD6G1qKLq2_9NSdZY3oNLQW3Te5l5tIrG3jnkmO9Cn5QlsVmI_oHrWxoCh_oQG0McWSHFTK15p_IXlbZ3f2ZgfZX7GLfvUKC4-InTUgQRWqU6xSoonq8oIODqdDLUEGNI31abxbvZApv8Hgn9GaVlxYHFaWi4pyg0eCo6qgbVJVDkXjkBgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a274348cae.mp4?token=BBq8fNw15VTUO4J8V7uej6VZPmRWhPaUQTW3p1VmKTbyofskbateF121oglvGvjcaVCPlIETcfCwvisdPRYy9VGut92fa3n-ZTIOUqOuWhdtMfeP_69vqfOA4eXvbLqakR1Gbzfl2q3NLSkcw0ghLLSTfE1aj8ImptRD6G1qKLq2_9NSdZY3oNLQW3Te5l5tIrG3jnkmO9Cn5QlsVmI_oHrWxoCh_oQG0McWSHFTK15p_IXlbZ3f2ZgfZX7GLfvUKC4-InTUgQRWqU6xSoonq8oIODqdDLUEGNI31abxbvZApv8Hgn9GaVlxYHFaWi4pyg0eCo6qgbVJVDkXjkBgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : نزدیک رصد خانه لار ، لانچر زدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19181" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19180" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19179" target="_blank">📅 11:51 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
