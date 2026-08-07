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
<img src="https://cdn4.telesco.pe/file/tm6My5s2HZ1IxTHUZipp4A1sBcSuiXyP4ade9rCaw-7a4K0p-mIFu3i2THHzsGiZqaLc042kRbES2t2z9OUZg38FH2crsgeTgKssl9WryujJB7jUmd5fiHBZFGm1VJSGYEd7AQGF2DXiHecPCiI7DH9EMyBc6kn1FmzdA1H3rH7JD9XWDTGJ9fsng0TSgkw_zSFoBD86CeBanbzVIfdYNnO1bbIqJnZ1E4aljFNlrfkg4_gfOu65v0q0vyfaM4YdQi25vc-T02Psp2RrHfeZ5QIq1496GKMalj1BCoZMF3vdHkQiAryX2uwlBCPZwMkY4LOB0i3kG--2vY7wIiQttg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 11:37:30</div>
<hr>

<div class="tg-post" id="msg-137506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند این فصل سرباز هست./ ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/137506" target="_blank">📅 11:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSC-xhBbbHRAeYhJLY84ZuBRBmbuKdcNpZav-NdxLwg0JH68dItGhYL9ukjtXXqHbVxOjyEcUVsA7bBwL-DeYHzWYSlrlwrvyJCAVLt1wFAowmzVcGdIcLq8GqKA75s-RYeaq4P6Vd4bBxF0HzArKKMGqHUjCnSDfvay6H92IoK_vKQzyE4vARKFXOZaudhm0bkBZvpwZO6iG6uHN2mliq_EB8rhiPKawRkZsLrZntcLxOkEiizu-AmES9ygUze5N93NOkE7G9iXXvEkhyV4x-i8ZCRek9l85ceH9Xdx6fiwvrMQk078tIgD93bajkXC8Q3rrIe5vEqTs_Fy1JQWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
فرهیختگان: ماجرای محمد قربانی داره شبیه پرونده محبی می‌شه، تراکتور منتظره قربانی بازیکن آزاد بشه و رایگان جذبش کنه، اما پرسپولیس می‌خواد با پرداخت رضایت‌نامه به الوحده، این انتقال رو نهایی و دوباره هایجک کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/137505" target="_blank">📅 10:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRGc4myyj9Xt-3aSsael-vmERtsY5DR567Nc_TrgICmAqHHv0o6ADvgHO_w8PfxCA6Iip5zU5fo9UYmCROrsAj-iFZKRZAwnYtWjvmEXIJSyGRV6C-Q2j9Kia6vDz9SZgnuInUHjbHiuuL5epQzDzf_eDxGh0rB0J3sQh6HJx_LaOUBoNk0VF9OJ1BJe-mnzT1OoVUU8DfKqVshDJlzoCxsD4T9ONxz0xygEnNgO8Orv2oU56YYwPfokxY2Hq2MsK1jUCPNHfaStZErykybseOEyu0xwiOZt0XghtLlt-SM_BiKbJNSjCf2-fUtdJ66i3_JuUp_qXr6ea4RVGllSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔹
🔹
🔻
هزینه رضایت‌نامه ۴ خرید پرسپولیس روی همدیگه تازه میرسه به رضایت‌نامه سعید سحرخیزان، بعد رسانه‌ها تیتر میزنن ریخت و پاش پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/137504" target="_blank">📅 10:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/137503" target="_blank">📅 10:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
اضافه شدن بازیکنان امید پرسپولیس به تمرینات بزرگسالان
🔻
🔻
با اعلام باشگاه پرسپولیس، در ادامه سیاست‌های باشگاه پرسپولیس در مسیر جوان‌گرایی و توجه ویژه به استعدادهای تیم‌های پایه، با درخواست پیمان حدادی، بازیکنان تیم‌های پایه که دارای قرارداد حرفه‌ای با باشگاه…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/137502" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/137501" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
شایعات: رامین با مبلغ باشگاه کم و بیش موافقت کرده و تارتار باید تصمیم بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/137500" target="_blank">📅 09:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwefL0N3SMGCE3-1VHOkWEcKlNs_aj_YvnDSjGGG6_R6B7zFET0fbtqGYYIZ9-AhXAVPCHo-d7jExp1C2gf0KwG0qkpzynWeKB78iBGtnNb6NXByUnmyqmxM3xb0ozeIuS2ROzK-LqMEINeVX1h9CSC-adzo3E47BGlwy1k7ZWug1MGALd7Do0aDVakEZTgVlHuQ09RVTKdBp4bLUEkpCsu4CnJu-y999p6tFVevroOecIg6jwO81sLVv8kuXYeTaS6TwaYbBVEZr6Z6JUys6l3J8rRBjYoa60k1rmZGC-EDUGoSJcWoipfvw9vURQvU5iPB16XHck8GYHgTxJmuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/137499" target="_blank">📅 09:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137498">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=Kwj9G--FRaTKewUz-ryNRdK_gsUsLdGbr3i_WPQKdZ5Pj89BXvEdNO4KPyUkbcJGUYScq8Gk-7ubElz9Dm3QNO64PMWp_o0gaJMMsGZf2ttuFJ6M6SbVVEU6Sb-yIKKWz25EtwCgNlIuY_ac2qxnKZUdghiRoJxfhss65YAtAFhPsdQ3eII2vAab0_d9OZ9CsXOP0v_T3CPphG6J789PRfpfPqH8YcD8X4kMKNseSdk-ikOD3RG8BtG0CCFbP3Je3srnrOwooLTHY1qfYR5_k-g6pcYljP-OdRbH1jQ9ALGqZeyIFfZcqiC2fPd5qiX5eiyMiIukb2Bgmd70A8Zgw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0995cd13e9.mp4?token=Kwj9G--FRaTKewUz-ryNRdK_gsUsLdGbr3i_WPQKdZ5Pj89BXvEdNO4KPyUkbcJGUYScq8Gk-7ubElz9Dm3QNO64PMWp_o0gaJMMsGZf2ttuFJ6M6SbVVEU6Sb-yIKKWz25EtwCgNlIuY_ac2qxnKZUdghiRoJxfhss65YAtAFhPsdQ3eII2vAab0_d9OZ9CsXOP0v_T3CPphG6J789PRfpfPqH8YcD8X4kMKNseSdk-ikOD3RG8BtG0CCFbP3Je3srnrOwooLTHY1qfYR5_k-g6pcYljP-OdRbH1jQ9ALGqZeyIFfZcqiC2fPd5qiX5eiyMiIukb2Bgmd70A8Zgw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ حساب کاربری، ۱۵ فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/137498" target="_blank">📅 02:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137497">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQ-LoUqeiNeDW8rh2pDOZ5-K-vuBjKhnWHuOqmLHjdHHqmPrkwAzubbNYfmr2mxkWD_nwrduzL44udasBZfoJYIgxPXoGY6agVX2kkjP1LBrOltnmkTXSNndA4MDebtXoKTPxfgM3C_s-cYbATGOmo0ejqSY86-ThoVUjK1D0__0kpDUX1Xosm_c5EoHow02q2od0-K-unsGowO9I05kSI2rPklRb0Qc8Yd90bfgVudy0DychROt5eNB-Km0RXxHPq3Dmid0EYGkCUNfeA3kIHaHIyGgUrURWbPkRCYpJc8FGNvmkidVDE65lmxXP9mL3czL7c7X0GRVVyaSnW3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شبتون بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/137497" target="_blank">📅 01:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
🔹
🔹
برای محمد قربانی فردا جمعه میتونیم بگیم تمام و مبارکه
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/137496" target="_blank">📅 01:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
قرارداد گرا ۷۰۰ هزار دلاره که ۶۰-۷۰ درصدشو میخواد
⬇
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137495" target="_blank">📅 01:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137494">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
🔹
🔹
🔹
پرسپولیس و الوحده برای قربانی فردا تفاهمنامه امضاء میکنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137494" target="_blank">📅 01:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tne38HrAGRp4kl06rPEjtFcG9qSXnghSSYsULcLo9IXIrLblgqd79kks9fBrjxopn3OfF53IYaRwP8Rm7N2eViOuvqYFUaYJ3t7PjdqH1hSPgtD3ywMFR1Lg_LSc9b5KMfLNZsLzF2j3P3HEsRzltIRDENHmOf5gfbn6ZYZhpqQY6UHT2Sho-8DD59E_kcx2IVm8YlkQwHuBZaoWIAcEBZQuPsy4hyNbBWq8plWMjOXhX7zPRt6SUtcLTfWArGAk4EzkkJMU9ftBxapfaMvjszP_euHLwGJW0bLlqafgbsdNPrpLY3PQwG6H5OCXgGeSn6Cf99YAp-4786AhzHO6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه پرسپولیس در حال تواقق نهایی با هواپیمایی وارش متعلق به مالک نساجی تا این ایرلاین یکی از اسپانسرهای تیم در فصل آینده باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/137493" target="_blank">📅 00:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
#تکمیلی | ترامپ:
🔻
من در مذاکرات با ایران مشارکت دارم. اوضاع به خوبی پیش می‌رود.
🔻
احتمالاً به زودی به توافقی دست خواهیم یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/137492" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ : من دیگر ترجیحم این است با ایران به توافق برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137491" target="_blank">📅 00:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
فوووووووووووری
🚨
طبق گزارشات رسیده، پرسپولیس به جذب محمد قربانی خیلی نزدیک شده و امکان عقد قرارداد‌ طبق مذاکرات انجام شده بسیار زیاد گفته میشه
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137490" target="_blank">📅 00:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔔
🔔
🔔
تراکتور با قربانی توافق کرده بود که بعد مازاد شدنش رایگان جذبش کنه که حدادی به الوحده نامه میزنه و حالا تیم اماراتی میخواد او رو به پرسپولیس بفروشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137489" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: من اسمی به جز حسین نژاد ؛ قربانی و رامین رضاییان نشنیدم و سوپرایز خط هافبکی که ورزش سه گفته احتمالا بین دوتا اولیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137488" target="_blank">📅 00:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✖️
✖️
✖️
قدوسی: رامین دیده مشتری نداره و گفته با ۱۵۰ تا میام پرسپولیس میبندم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137487" target="_blank">📅 00:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚪️
⚪️
⚪️
پرسپولیس برای تکمیل لیست نفرات خود در پست‌های دفاع وسط، دفاع چپ و هافبک، به دنبال جذب سه بازیکن جدید است. با توجه به محدودیت‌های سهمیه لیگ برتری، سرخپوشان برای دور زدن این چالش قانونی، استراتژی جذب بازیکنان آزاد را در دستور کار دارند؛ بازیکنانی که تا…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137486" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووری
❌
❌
باشگاه الوحده امارات در آستانه توافق با باشگاه پرسپولیس برای انتقال محمد قربانی به پرسپولیس /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137485" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137484">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137484" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137483">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
دنیل گرا از پرسپولیس کنار گذاشته شد، اما برای فسخ قرارداد بر سر مبلغ جدایی با باشگاه به توافق نرسیده است.
❌
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137483" target="_blank">📅 23:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137482">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5wLL6Bc5xsbOFxsuTeNPvPE4XxPJAWqRGT8zdBJGGXBr1pX9Qx6YPYYostqc2b_MQA8BPnOfwBmdX1YTmPWJIuUTgzXd0N78JbMzh84OqQIexscBrDq947YJ7eeUBJWRspxV4A1TBAjRLwP7m9M11_Xj9o6xyBfyeU-nrEhQpFg10YedPK5yPTGh_2CnlMK2eQdkRiYb6hrYx5oYfijJDRH3m4EBM10hs8yXgf1di4FZbW-X4K7PzOwerMQijfWsNHGu-UhChHbm__n5C54OCvGUT2pG538N8D-fes4-ctFYEP-GG9myS_MFI2vPf-RZxYVqYR-uboq-rKY66kQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
میلاد محمدی تو اولین بازی تیم جدیدش امشب تیمش تو پلی‌آف لیگ کنفرانس تو عرض کمتر از ۱۵ دقیقه ۲ تا کارت زرد گرفت و اخراج شد :)))
😄
😄
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137482" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137481">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
قدوسی: من اسمی به جز حسین نژاد ؛ قربانی و رامین رضاییان نشنیدم و سوپرایز خط هافبکی که ورزش سه گفته احتمالا بین دوتا اولیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137481" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137480">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz5NT_pxBtmpNqwOCfgfXeqKtPNH2QXM587uWrejk0Bh7IgYpaahy1WfNjIJ9PiPg9VAbzsjI911lpv8c0tUeaVkdUebvbN5EBvX7yVp3XyT4MyoNLtMo2O164tP3cirhsZr6UuvHXT9EnJ1nwF-J4DtmGOKGZcjKe5cnTMCWljqC1cAQ0j72YOkJWzCDfkHxOVX_xiqVgCsvrplbL-G12OYdonhw4mG2RbCQDw9uHhqNswMrYrdzg2ODnlQKP84zvjqcnXLCCeT0NP6xSQ1v9lhQLCV5lUvHQ1ctwau4TNnO0dWQ6EAqvsnnbOvNfC32DoneLyRgfAF6t3QagZ44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
علیرضا اشرف پیش از تمرین امروز بعنوان مدیر رسانه‌ای جدید پرسپولیس، معارفه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137480" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭕️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137479" target="_blank">📅 22:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
العربیه: تماس‌های غیرمستقیم میان واشنگتن و تهران که از طریق میانجی‌ها در جریان است، وارد مرحله نهایی شده و در حال حاضر، میانجیگران در حال تدوین سند نهایی مرتبط با بازگشایی تنگه هرمز هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137478" target="_blank">📅 22:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYAtvlNuDr1dI1M2l914bq6Xd8jWtLYDENdu6MjDPO85GJ9oXFjwAHWnJyZ0dU-L-dGLW2j8KjJ2ekvXK-0cBoCpk6NNVLCaol6bO3CTBSzwVRfGPzlQjWTSdpZqW5a3esm3DXzlhxt11IMjypywgP_3JCHB86EHlko6c3PcAJm2lVXnXu4-8mKxIC7TXgQ_clc209qZ9HLbX-oIzXsC2PxsoTPhpbzni8Ciay9cK3Aa_ym_9dAU5uTKGbCoz5MQoH3bPLI6hQBci7zSDfYq2xrIMKLj5_o7aVr9R5IVCzIr2H4BNJoHxbu_ONr8HAIbWFYVsWvGOj6OjpuHe6z2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137477" target="_blank">📅 22:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKHwgthw5TukqSftBP-GLTQviXPbpywxOlgwuuy_UshS_IxC6NJzVGFLVGNM0UUbLmFAn-7SmjU8-VwxcBTUfdHBI9A7XXICwQJNILJ7ghrTN0D1KH1Mks7ATc0zf5Fd3ZnuFP5VeLANaGhL-s0dXL2FhXakWLT0OxSWfN6oSGS3KIE-9Zqhlq79ofKhza1pTfhJ9zqfLYyj0uLQ2lJ195kSgNuU_iJ7jdn9CbW5D63PgjW3_jgNykBndO-cNHY6o64zgTKQkI6HBPvmKez-hmKuW1KD5XblQAX3QMTh89GaS132cHIPmNWS5xMhFstaXxTwKt8oLOSxN4vc_udd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
تنها ۲ روز تا بونوس ویژه ۱۵ چرخش رایگان بازی Egypt Power x1000 باقی مانده!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ حساب کاربری، ۱۵ فری اسپین رایگان
Egypt Power x1000
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137476" target="_blank">📅 21:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxmYMFvk7sIZW0YcNsQuVnqmtbTXSGtWvEUV4Z0vr0N-mwqjNBoJ9zZesPxoPfgAJ386is8oU_bLl6bZA3cqcWP3Ym-KwXbwHsJXSu1dhN4LWWSZsA7-HcH62WB10u_rjlFntWVy1ivm0SJEDkzXVCjQ_3_-KpqKsm8dVk2oCF-QKzAbXbvpwP9a5wb84w-FZmnpVUy4Vfyzgtb3ee6j6BbUebfx87vbM2NipDne9E9sIZdOVY5A9VDOD8uNhAnUw2nBLB7S9oy7R33x-pvGjFwi7F8NkO1ZK3oacgX95aBm2EIG0HXSIW3ON_qN2lGAnSm0GU4iQVq8KbIZ1aDpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اضافه شدن بازیکنان امید پرسپولیس به تمرینات بزرگسالان
🔻
🔻
با اعلام باشگاه پرسپولیس، در ادامه سیاست‌های باشگاه پرسپولیس در مسیر جوان‌گرایی و توجه ویژه به استعدادهای تیم‌های پایه، با درخواست پیمان حدادی، بازیکنان تیم‌های پایه که دارای قرارداد حرفه‌ای با باشگاه هستند، به تمرینات تیم بزرگسالان اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137475" target="_blank">📅 21:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
قدوسی: با فروش علیرضا ملکی از نساجی به خیبر، پرونده فروش طاهری تا نیم‌فصل حداقل بسته موند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137474" target="_blank">📅 21:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
‌قدوسی: کسرا طاهری موندنی شده و بعیده این پنجره از نساجی جدا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137473" target="_blank">📅 21:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✖️
✖️
✖️
قدوسی: رامین دیده مشتری نداره و گفته با ۱۵۰ تا میام پرسپولیس میبندم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137472" target="_blank">📅 19:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⚡
پایان همکاری استقلال و رامین رضاییان
⏺
به گزارش سایت رسمی باشگاه استقلال، با توجه به مفاد قرارداد یک‌ساله رامین رضاییان و عدم پذیرش شرایط پیشنهادی باشگاه از سوی این بازیکن برای ادامه همکاری، همچنین با پایان یافتن مهلت تفاهم‌نامه فی‌مابین، باشگاه استقلال…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137471" target="_blank">📅 19:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137470" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137469" target="_blank">📅 19:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
آسوشیتدپرس: پیش‌نویس توافق درمورد تنگه هرمز نهایی شده و در انتظار تایید مجتبی خامنه‌ایه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137468" target="_blank">📅 19:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137467" target="_blank">📅 19:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
❌
ترجیح مهدی تارتار از بین محمدجواد حسین نژاد و محمد قربانی جذب محمدجواد حسین نژاد است و مذاکرات مدیران باشگاه پرسپولیس برای جذب این بازیکن آغاز شده است / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137466" target="_blank">📅 19:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
حسین‌نژاد اولویت اصلی پرسپولیسه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137465" target="_blank">📅 19:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXjcGhC-255mK_0HKydwefUnlRUFWt8L20cLaR7tRm9JSaLRlr8z_BFSQTXTc6fAr7Hhz4_kocGY30g_0hKRqEUnlt5fAox7om9PS8HGdA79jQ3PucO58g_VwdQv3hn7RuiwFVVgcgeyj09l9xuhRvfhBROQx3BW3xbr5S5olQ5bu37GGG6TDHtSrakHHCH66mb0Z9tpTtba5hyUBxv-ICVB-voP5vsbNVz1v6NgeNi6fBrOaScRmPD_GTRkkSChU5cLNLQuLUZRrKTouh-91PTbtyC-un_-fUe8SYTiYFLs_1jOYDvajQu7Y3H-cgl0XiSH3kM-q8HBTCCEGZH-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین‌نژاد اولویت اصلی پرسپولیسه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137464" target="_blank">📅 19:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es7mh8u84cQvTyw-VqwH_flmKxAnNLQTOFUewcVNlVxXJ5t6nG60KDQSMHqm8lG8ODc_HH_Fc_1SbCkoT4yuihPhvuQoOTzJTggHbjtAqyl9cSETU0AZSIbV3bwumWhxxttf_CoYTkhQ0HbXfLmjOF6jxsd95_6YTKglTZiDLw5-_X5uecbbNWabJWIXQGWeSqa73ok7HtpA9mE18CADAGiYTlTJBCWFDowYxiYSwSBzqbPyMiemN0-xajdDkrE5K9dmYLmorEnAskmzHis0BpwFcOGWQZUVIWcEcpTBMvG-L3sHYA4jZlwDcKxawLhhuWkbvBJhaC2Z5sypeOfzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انتقال دانیال ایری به پرسپولیس به دلیل اینکه این بازیکن بیش از 16 هفته پیش با نساجی قرارداد بسته پل‌ محسوب نمیشود و این بازیکن در آستانه عقد قرارداد با پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137463" target="_blank">📅 19:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
پرسپولیس در مذاکره با دنیل گرا به این بازیکن پیشنهاد داده که با نصف قرارداد فصل آینده اش بیاید فسخ کند که این بازیکن این پیشنهاد را رد کرده است و خواهان تمام قرارداد فصل آینده اش شده است..
✍️
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137462" target="_blank">📅 18:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
محمد امین کاظمیان: آقای تارتار به من لطف و تمایل داشت بمانم و باشگاه پرسپولیس هم موافق جدایی من نبود، اما در نهایت تصمیم گرفتم جدا شوم، چون دوست داشتم در تیمی بازی کنم که شانس بیشتری برای حضور در ترکیب ثابت داشته باشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137461" target="_blank">📅 17:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
فرزین معامله گری سرباز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137460" target="_blank">📅 16:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137459" target="_blank">📅 16:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
اعتراف تکان‌دهنده رامین رضاییان بزرگ‌ترین اشتباه زندگی‌ام را کردم!
🔴
طبق شنیده‌های کاملاً موثق، رامین در محافل خصوصی صراحتاً اعلام کرده که پیوستنش به استقلال، بزرگ‌ترین اشتباه زندگی فوتبالی‌اش بوده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137458" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137457" target="_blank">📅 16:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔔
🔔
گفته میشود مبلغ قرارداد تیوی بیفوما در فصل آینده 850 هزار دلار معادل 140 میلیارد تومن است و احتمالا در پرسپولیس خواهد ماند. باشگاه فولاد خوزستان حاضر به پرداخت چنین مبالغی به او نشده و پیشنهاد معاوضه با رزاق پور را رد کرده است
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137456" target="_blank">📅 16:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137455" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
از اونجایی که پنجره کیسه بسته میمونه راه پرسپولیس برا جذب بازیکنانی مثل ایری و حسین نژاد هموار تر شده و فقط باید بانک شهر سر کیسه رو شل کنه و یه تیم جوون و درست حسابی ببنده برا امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137454" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upi1Lp5l2bzbVRJjRsAnL1RrLoMR8Rn4vKzm2hszC3Xfq3cTu3zj4xz7nN7t5opbn3Z9ZlClbxyjYMxyVg9jc16FbhakM8N0FezvrzGQQ-UINVY4yVovLiAA586G1dnC5k-LwW9CUT-MDRzZ7AIOXASGtLThZFVOu3nQhOD7DQKWlRkVJtN4sZIn6ke7r0qI-M8-lb9To527ZU4Tmfyzp8IF1U3rTgqZUY36WBBjUK1hvRu0SFmSgF7sF-B1UmqUgDiFKnBDcWiuMY3SSchcmf3KmQsEbJ4kTQGNgDCf5D006OkGdHNqk3JIS-KgXkzdaPOiF7uXA-cqLRXViST3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حسین‌نژاد و قربانی
کدومشون پرسپولیسی میشن
تکلیف ایری مشخص شد
همین الان در سرخ توییت بخوانید
❤️</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137453" target="_blank">📅 16:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🔴
👀
ورزش سه: پرسپولیس در آستانه جذب یک هافبک قرار داره که گفته می‌شه یک سوپرایز بزرگ برای هواداراست!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137452" target="_blank">📅 15:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
❌
خبر ورزشی : پوریا لطیفی فر خرید جدید پرسپولیس سهمیه لیگ برتری حساب نمی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137451" target="_blank">📅 15:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyHcVpNbKVx2fX7tUCy-Y2sXridF-KDlMLQvbJv2mjzKUF8InxFcsjTDfYrAEhkoE1dHwLkf3oTu-pa8Aj8vDvlamom9KkQEdbgg-o1oZqv-S2r_aslA7T-_UTuqfHx41GCo_-iVtWAm_sVi3JnWEiSg2ygMQZR5Cp65QEzsWBBA_fGmihwd9GKtUKuKHykJZUq_9G6fgzkoLCUmawgpdjhqAZu8pbO2s9GG50wZgMveHYqodFTsaFn_QHWv7goqndjnB-2q4bIuflAdren1jvqAwYo0A0g3orsQy3EnLHXSUYxMs7Vx7JXAeIQaMD0gREeeC8xOz4Rjqwf-3ZFHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
پیمان حدادی سفیر افتخاری چوگان شد
😀
✔️
دیدار مدیرعامل پرسپولیس و رئیس فدراسیون چوگان؛ تأکید بر همکاری‌های مشترک در توسعه و ترویج ورزش ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137450" target="_blank">📅 15:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
آسوشیتدپرس: پیش‌نویس توافق درمورد تنگه هرمز نهایی شده و در انتظار تایید مجتبی خامنه‌ایه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137449" target="_blank">📅 15:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owPDtxU_oxZW-RFjEiz-ozKZ_Rif5wp7k12ZZ7qnBgo-RT5mDMz6HJagAXPOmzlod_Zfnq4-gptWLWbiSC-FIntsrMrGp41FNkaBhq8_8SVBHlZDbc0pHlF3XJSfbjTHS7ytWCZgjzSBi3RO8NpCrteoo1e6wtfqkaH9gHCj1LekdDKwPLqqWMgaBB0yw8tg2Jl5_RDbbpaogM4ZEfr-NQ4KDt7Ldd6erVkoobiEz4mct4CNyOCvDgpLGTFhO8UN5Od1JPzi0AAwVvwRTk-YMs5DT3-bbTE1qb2fNib2JvYEXNnnuaF-KyhrjLwkUrs6bcFeiFN2XkyaFuaFtIk5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137448" target="_blank">📅 15:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
باشگاه پرسپولیس هنوز در حال مذاکره برای جذب دانیال ایری است. اگر مبلغ انتقال شفاف و مطابق قوانین باشد، احتمال نهایی شدن این انتقال وجود دارد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137447" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137446" target="_blank">📅 15:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137445">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_xjTddqSnXFgqOj1KLSYbsbEgHdOj6ljm9uBq7f1VEy-2JA_tY69e2Ik0t_pn_gy9YASTtG8q4d16hc7QzoZfLGFKBSlTc1mapeq0kawP_T2Sxa-lq9_UujVikV-laMo84Zl_zAUUbr36exMEUakvJUGJIKcGuAFja8M4j6dmz2ox-vgo1v06RpBZQ7IA3Kv5yzQ79p6RYLi8u9KQaWUMwkeopFoYfef7_vkaoYffBXUntPIEbVgEpTrQlBabumzD_gGZ3vREachpNiaaUFVdOSSzqco5ELvsYQjPWuXUV2xYQrghTPRf9FgVMeZOMcZ5Y37JUf-P1y8usNwDFPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
نبردهای حساس لیگ اروپا؛ آغاز مسیر صعود در شبی پرهیجان
⚽️
دیدارهای امشب دور سوم مقدماتی لیگ اروپا، تقابل تیم‌های باتجربه با مدعیان جاه‌طلب را رقم می‌زند و نتیجه بازی‌های رفت می‌تواند نقش مهمی در تعیین سرنوشت صعود داشته باشد. رنجرز برابر یاگیلونیا، بنفیکا مقابل هارتس و سالزبورگ برابر پافوس از مهم‌ترین مسابقات شب هستند؛ دیدارهایی که انتظار می‌رود با فوتبال هجومی، فشار بالا و رقابتی نزدیک همراه باشند.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137445" target="_blank">📅 14:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137444">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137444" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137443">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
آخرین مرحله مذاکرات پرسپولیس با نساجی برای جذب دانیال ایری با در نظر گرفتن تمام جوانب حقوقی در حال انجامه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137443" target="_blank">📅 13:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137442">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137442" target="_blank">📅 13:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137441">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه نساجی برای امضای تفاهم نامه قرارداد ایری امروز و فردا می‌کنه/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137441" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137440">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx_hFI0XqN9KHQc9nwXyBuE_DGmJxJDP1n75DjnRHGQLo2FDRTXxPhOuSVHgJP7LMQvOZ5K3OTLGrsSsKWCgkvzpHvp4OE9RH08Ud26uXGQj3V4Ls5miHEegIg2jxUuxiWZKHnwSF9tWxDYMQGy02obs0TDRdHpxJ02LEf62NO7iQsJ9s-YOJ24ueo8r0oL4sDNns0AP9cN8PiRiOoCfgEssd5fUXpnUv0vGXW0tDXDYjah0fn5cCAJ5zb9Ya2Zai27uIY6JDZObTfXmCHnNRhOV-5a7rkDYJ4b7sDLUkEb_j233ft6Oo02oltv5PupYchgX1mXD_s4rCwBCOwejmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس در مذاکره با دنیل گرا به این بازیکن پیشنهاد داده که با نصف قرارداد فصل آینده اش بیاید فسخ کند که این بازیکن این پیشنهاد را رد کرده است و خواهان تمام قرارداد فصل آینده اش شده است..
✍️
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137440" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137439">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
تارتار گفته جذب دفاع چپ خیلی مهمه و درصورت مصدومیت جلالی تیم دچار مشکل میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137439" target="_blank">📅 12:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💠
💠
💠
پرسپولیس با وجود ۸ خرید، هنوز در خط دفاع، به‌خصوص دفاع وسط و دفاع چپ، کمبود بازیکن دارد. اگر این ضعف‌ها برطرف نشود، ممکن است از همان هفته اول لیگ برای تیم دردسرساز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137438" target="_blank">📅 11:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137437" target="_blank">📅 11:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5EP4uoxFlB_uCRRwrrsqXQC1SSgvhFwJB5jSdog81bepuG1Bj56yw5taDvVSFLkDllKJ7kV_KWb4KBwQQcputBafcJq_IiuAVZ1OIUyR3wfiLdRK1OkgPz2ji4ZZ9za6W1H5o8ncXoTQS_GfKfwbTPG2Tyn1IjR8SsDvljFR7yDPcqjbWAq41XgmtWq26cJW2u8RMoKw2jgDcFMKB6OzVXeUK2IE65DfqplT4Te1qOuqkKT2qU07So9Bs8KobZxv9-YED_a4H8XWhTQugC-WSXv4cpXx1gjS3VD7VsACY1jvr-Og863aBb_GbGf6gMZhSNRMsN-ME9QkRlfpBmmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
💙
رامین رضاییان میشه گفت تنها بازیکن جهانه که از نظر فنی فوق‌العادس اما از نظر اخلاقی و رفتاری میشه گفت بدترین بازیکن ممکن و با تمام مربی های کریرش لج افتاده ؛ بنظر شما حق با مربیان بوده یا رامین رضاییان؟
⚪️
رامین رضاییان
👍
⚪️
مربیان
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137436" target="_blank">📅 11:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
🔹
کشوری‌فرد: مسابقات لیگ برتر با حضور تماشاگران برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137435" target="_blank">📅 11:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137434">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
ایری فقط یکقدم تا پرسپولیسی شدن
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137434" target="_blank">📅 11:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137433">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
؛ به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137433" target="_blank">📅 11:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137432">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137432" target="_blank">📅 09:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⏳
⏳
مهلت ۴۸ ساعته ادعایی ترامپ که برای تعویق حمله به ایران گذاشته شده بود ساعت ۳ بامداد امشب به وقت تهران به پایان می‌رسه و فعلا نه خبری از توافق قطعی منتشر شده و نه خبری از تمدید مهلت تعیین شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137431" target="_blank">📅 09:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137430">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏺
منهای ورزش
⚡️
⚡️
طبق گزارش‌های منتشرشده، اپراتورهای تلفن همراه برای اینترنت بین‌الملل ضریب 2.7 در نظر گرفتن؛ یعنی اگه کاربر 1 گیگ اینترنت بین‌الملل مصرف کنه، 2.7 گیگ از حجم بسته‌ش کم میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137430" target="_blank">📅 09:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137429">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
ایری فقط یکقدم تا پرسپولیسی شدن
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137429" target="_blank">📅 09:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137428">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
الوحده تا 600هزار تا حاضره پایین بیاد و رضایتنامه رو بده.الان باشگاه باید سر دستمزد قربانی با خودش چک و چونه ها رو بزنه/قرمز آنلاین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137428" target="_blank">📅 09:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137426" target="_blank">📅 09:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137425" target="_blank">📅 09:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137424" target="_blank">📅 09:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Vz-LZEfPG332yjB3vR0O3LL9gvdBkGeUyeO943h_-ZOa9Gptv2sLjRQxn4J-e4Q_ytLZ_d1gJ0f7KuGeaPlf7RKHba1AwrYobx_WsYDQQiXR9byOfN2cR15nP2dHeUGFM3musdMWx16ehbyu5l97rxKYXoK10SSB8Wd9lgj3wgroEAN3jJQV94sCVjBRU07QOQVHv7asnYv5X6h6U-w65bRr6bv-3Qlp5jGRltmE3CzcdTQTnEi6E0Q7qmiUHjb__ah_VbeVM6lz7rITJaEpw2g06UWsNi1seWKHhUNe6nVPFOZA5v08-Wi84URbJWGPlg6scZoHppLsW9hzufknVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=Vz-LZEfPG332yjB3vR0O3LL9gvdBkGeUyeO943h_-ZOa9Gptv2sLjRQxn4J-e4Q_ytLZ_d1gJ0f7KuGeaPlf7RKHba1AwrYobx_WsYDQQiXR9byOfN2cR15nP2dHeUGFM3musdMWx16ehbyu5l97rxKYXoK10SSB8Wd9lgj3wgroEAN3jJQV94sCVjBRU07QOQVHv7asnYv5X6h6U-w65bRr6bv-3Qlp5jGRltmE3CzcdTQTnEi6E0Q7qmiUHjb__ah_VbeVM6lz7rITJaEpw2g06UWsNi1seWKHhUNe6nVPFOZA5v08-Wi84URbJWGPlg6scZoHppLsW9hzufknVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
بونوس ویژه ۱۵ چرخش رایگان بازی Egypt Power x1000 با شانس جوایز میلیونی فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان ۱۰۰ هزار تومانی دریافت کنید.
📌
نکات مهم این بونوس:
👇
▪
︎ ۱۵ اسپین رایگان ۱۰۰ هزار تومانی
▪
︎ ارزش اسمی بونوس: ۱,۵۰۰,۰۰۰ تومان
▪
︎ مبلغ فوق تضمین‌شده نیست و میزان برد به نتیجه چرخش اسپین‌ها بستگی دارد.
▪
︎ پس از پایان اسپین‌ها، برد نهایی بی‌قید و شرط به موجودی حساب شما اضافه می‌شود.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔵
sportn5b2.com
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137423" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137422" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxadNb4o-0_s0tfOmPihxTgtfDl3NJGKoQVvGTIg2NnGqRNUJL7eeKNJW_rPVNaOe9mKi291J4_1HtAFDfxX6BHAiLczt66ro8f3IAEr0XYoSCpfHMTJ0XrsjoNj99FO_c6CguGy1NJIvQRZfH24PVM-kXIoKpfotnIqXx7Rpu1tKU2gkXqL0ipPnunw7XxaNo4zXu5QTfORJteoSg8YP_JqislNczsTUBlIbHOH0vG_zvhXlCSCzfpwCXdNcMPYe1ttPV3dxT6mS6Qq04hoMNwE8J6oWuFMmlxcgaQ3-10QSqH7oMfIIajDNwc7ptBx_jaBO9jPoj_J0VfQ292Shg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیتر سوپر حق فرهیختگان چاپ فردا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/137421" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137420" target="_blank">📅 00:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzSP1CtnXSL4HEkjsDlgSHpJL2QullLSWwjGl427Dv1oRaDeXTO8voQrtsGx2n6ReY6lvab3rU6DX52f7mptyFXhm7wfEu0Xydb1vaXS8B9JV2WGBrHLgUN3_7YLa0-xnf4DNySBvkvdfoTyXjZ5iHhUNIeabiBgQw8P69o37Uaa_HwwJI_2tIt-NKw2bCnl6bKqe2XYlc3P8IozVyYP1IZDQO7UDT0UEeTfAvC4ji3_0C6yA4VY2RgoKi8_hv-s9wI4HyB3Y6JTpv3_FPtpD8rZgEQBPDp_ekZXLwb7VkZx2rNmf2dk1m7xbv7dBoiYOMDj7x_B4uMcMeChDCUoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137419" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
❌
پرسپولیسی‌ها ریختن زیر کانال تلگرامی باشگاه ماخاچ قلعه روسیه و ۱۳ هزارتا کامنت گذاشتن که آقا این محمدجواد حسین نژاد رو بدید ما ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137418" target="_blank">📅 00:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137417" target="_blank">📅 23:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137416" target="_blank">📅 23:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚡️
⚡️
⚡️
استقلال طی یک بیانیه اعلام کرد که با وجود تلاش‌های گسترده و مستمر مدیران در هفته‌ها و ماه‌های گذشته، متأسفانه سومین تلاش رسمی باشگاه برای گرفتن دستور موقت جهت باز شدن پنجره نقل‌وانتقالات نیز به نتیجه نرسید و در مقطع کنونی امکان ثبت قرارداد بازیکنان جدید…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137415" target="_blank">📅 23:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
رقابت پرسپولیس و تراکتور بر سر جذب هافبک الوحده ادامه دارد.
❌
❌
به گزارش قرمزآنلاین، در خبرها آمده، باشگاه الوحده رضایت‌نامه محمد قربانی را ۸۰۰ دلار تعیین کرده اما تراکتورسازی حاضر است  ۶۰۰ هزار دلار بپردازد و اگر پرسپولیس با این رقم موافقت کند الوحده مجوز…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137414" target="_blank">📅 23:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
🔹
🔹
با اعلام رسمی باشگاه استقلال، پنجره این تیم بسته باقی ماند
😀
‼️
پ.ن این همه هزینه کردن وکیل گرفتن
🙃
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137413" target="_blank">📅 23:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137412">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🗣
🗣
🗣
‏  پنجره استقلال همچنان بسته است/ خریدهای جدید در خطر از دست دادن فصل  ‏
✅
در حالی که طی روزهای اخیر در فضای مجازی عنوان شده بود پنجره نقل‌وانتقالاتی باشگاه استقلال روز سه‌شنبه ۱۳ مرداد باز خواهد شد، این اتفاق رخ نداد و آبی‌پوشان پایتخت همچنان با مشکل بسته…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137412" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137411">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
فوری؛ معاونت ورزشی منحل شد!
🔴
باشگاه پرسپولیس در بیانیه‌ای رسمی اعلام کرد معاونت ورزشی منحل شد و ۳ مدیریت جدید جایگزین آن شد:
مدیریت آکادمی
مدیریت تیم بزرگسالان
مدیریت تیم‌های بانوان
🔴
پ. ن؛ البته در بیانیه باشگاه قید شده این تصمیم هیئت مدیره با قید «تا اطلاع ثانوی» هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137411" target="_blank">📅 23:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137410">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nurd47vBdrsAe5A06YTEsEkylbtwfw88sCS3xBsifKGWopgP3D-wP20yGR86MfPwSc_j1ZlO1NscL1sS033M3MA8XOrYZaCteWK3sqQDmVwI_BvgRCF5AeUAC9wtkK62R72X6fc3bMkbTgHTpTZtEO8Ml-E-M9U_UGjelVBs9eBIRcFcLBCb27FtlYLfHBoGt7qUcE8Tg4QhjOS3suNVi5tP4zkZ5SdFF105mz0pnQIqkBK7gfZ8yAU88vdK1SMiiRzKNTw6V7-vrgApOmhsfUQhbTJJ_wpQIJDo-BZX_vJYQq0L0eNBbPhNK4sbKhT8le_iD8X2HMeyFM8Z-Qq-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
خط حمله فصل بعد گلگهر
.
👀
👀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137410" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137409">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnwroukcdavEO6grZw8SouNwCq-ExYlmKyDGk8iHoJ8Hu17fbuIBuMJijDuHHthVSP8O9zqaPpjcUUyCj-QAcgkqJW49cUoZnUVfJd3Na_Gijpevy4ul-6NcB3IABv4UkYMm005Vdog_9ysDcVg-1h7owDMMA1OzQRs0GiSHyqL-1ATGGm5UGw9IV4jPmqnLOoMd7YoylxM20kkeotputPY1J4Spr3Cwvi6DvsJdxbacaf1f6Ag_gH4nwagi4bbnCl-mapNPaSRZp0aqcY_dVdFT3RQ8z97b0u6dXIcUDyFstyr8l0XToLTI-T8wlbcG_ZIdlrTZNo8sRvGgN0W86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عضو هیئت‌رئیسه فدراسیون در پرسپولیس پست گرفت
🗣
با اعلام باشگاه پرسپولیس، محمدرحمان سالاری، عضو هیئت‌رئیسه فدراسیون به‌عنوان مشاور حدادی، مدیرعامل سرخپوشان منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137409" target="_blank">📅 23:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137408">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
قدوسی: رامین تمایل داره به پرسپولیس برگرده و از قطر هم پیشنهاد داره و تکلیفش تا روز های آینده مشخص میشه.
❌
❌
اول نیاز به تأیید تارتار هستش ؛ بعد از اون بحث مبلغ قرارداد و پرسپولیس بیشتر از سقف خودش به هیچ کسی پول نمیده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137408" target="_blank">📅 22:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری از ورزش سه
🚨
جدایی دنیل گرا از پرسپولیس قطعی شد و مدافع مجارستانی از پرسپولیس جدا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137407" target="_blank">📅 22:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
تعداد کامنت های پست آخر پیج پرسپولیس به بیش از 130 هزار رسیده است
✈️
✈️
هشتگ های هواداران به جذب بازیکنانی مانند قربانی، ایری و حسین نژاد اختصاص یافته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137406" target="_blank">📅 21:48 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
