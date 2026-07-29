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
<img src="https://cdn4.telesco.pe/file/ByBnrWlPIdFYs2I-n_8FFJMR9xe_x9krdBhK0WPv9X3YWt2RThVfjkwTMX5KPZg3gu-gFyH3mnRJxWSM0_kgDvAa7ydMiKrfFC0O0SQJXDCd4oySLlAR_YdsvZCY3Zd0gonI57STzowYgfs_k2-w14PFaSqycRVjQC39ZFlfr7XQuFwKZGv-53V7p119d_igJ6TheyF19oskJ16bqpMN-4-Ht9bueqwCPieSFcwFbUCt871umO9qeUZUxb5TyH57k4M75_sMrrp2-RjT3S6e83xrNAoa5ePzoSjoom4D5GCIolBvFgoV7RcflZuwc8ftcR133dskJ9yae5aR1nz8Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 218K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 08:42:55</div>
<hr>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orsd9WHhucG3uH2dR6yyilDnVkxL1UDR7U922C4N5hHqmqhvmY_a0ZsPnefSQwWzkyD7cjXjGCbT0zexJDYKoJKyN8nJYURlvXlTQ5-Jxyl05zxddsSIVIGGI2mv2TKbMEOFBX8G-EPvvqcFmdhmU0_Q9gK1al13tnh0M0mmui-kHgYdzrx4JPWZ_yT2SHOGcVh_wiuMRhQMxejB2qT1Ed0GVqrEV6S6wT_ZVRU0ZMXSTNh5Xs_LbEHgQ2AnArcnrgKK4Uel6gxsMytjwDNI9B7BZrM2xnUYlWSFkK028Ik5PwsXbFgLd0_nZp0xSU60jVGrFEaYrksp0iRCfMZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdfDv4SEstWKVn4oQCim5YZX8ZU8Zm8gpaq0M1uh7d2x1vW6zPfmvghbChes-5iR5uub-QGV2PnYSaXh3SMHRM84Z7dJihwOekBz48a0UkyTtYE8VtdPc3SMC-qDuTGuU16G0WRaROSGQXNJsd_2Q9GqEaVwvo_n_17pOezmApX-QVN0oSqgVNwQ3fh3dRVwIZWsN8Jdz_l6gyO2zP_iJ6CR2Cno2KGbWJr6f-utSSohb-srNZE1cbcbXgTYNmA-5ZtMc0u8XW36iObHQnH8LcjyB5GSWB222r61lipv3lQXb4HnWXmqHDVJ1TX6Jzb202-7IaTHo0U9K8mCQp2a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvetXyuaYJBn2LR8cmxvn8Zolxm63BEt7sgn8cG6DDQ23hlxZEwQsPkmPTgdtHtVtLXqeMoFwyIYVbg_fd5SE7B_VvC_-FY06y2j8FFH6EcwzNp5bbF4crn6ECApqItfhO3el1teUsk9Zv5RbJQn5iI1Aq7CevDHPTXzQ7q4qT4EVkNc-gtZ2HCSvm4frFHv15Ea4gdmwciT50S8cZ7vH5HmaSh4_Jt4kEX7_IsEuv94ciGqYyT5F9zKh670u8u-4_f8oyjg4voYSoswhPLCMRPxUtuAyIGIgq6qbNVYuZiU4-w1Ngm7H5dPjb0ApADweukEF7wWfK5L1pBBMgaTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz8lONVKIPB8szW8wugzURwf-HzFe2z-32Izj4-bSEUTIblhMzNjAL2tqUqMqmDrenNW8rWBkKyEaj6kcK1Vj1tuHeozozv_rC1SMRzObeNPCwY99YZDVb2hTprFkWoxyfFELHVb5Fehu_D9GIxz6qtspEh5xeDO8euNa1zvuDY6DXcF0JHly_02BVHNtDaN420P10rJfSk29OHSVzq-bqAmyu6TN-_5e69ndETmk25kMgg_5AXDmLp95FtFQU80GjMxrUW2Fn_Yy8xGwV16Wl27C8WN5Kys6n3jjBeqytrVy7BrfY2BbJLnntiCnrS9naOFKlYYj8hZvagn4XT0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb62683sueE3BuwpNZ0-uofFmigb0KWyYVWC4D-35QYXeQhljaJkTSQ0xHETkhEd8uyI11K5yVRwbVl0QdRc2WHxYEkhgFZ2rV7WQMdFjapfANjC1JSW8qfhau8OPy0KFICdebzGcmlrZs79HLV8mKIzxi68ldvyMR3E-1rELadHugldSzUXTJSJIYCruuoCkZ7U7rVxwH1y41W0nN1DPDLgjVFMj9QRvcJTnQt8jniuXpBC-CCLWHkrllEzjhPuIeLkQz_wGjNPWi7R5khQ3p5xCFzRFvHBt5mOPRED9aZDxDTza7PdBRMJuNZx0XyVYFQlDD4AeKpd7z5oBnNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMX2digeWQgUyzhA0-IX0l0t9sOIKFeRpCi_l0jcM1yxGKBtQ_7EopPaD3kdYi4CuEUwQE03KZUTzuzqDIr3nQLdXA0Knb5LQG5Xu6hzC8uRXdlzHeNgISkk1uxfeIMii1b30elDtxqPbYl75b91w_-gaTp1FKuJf8PoqqNk7DjIlu3fVzdH7VCkcxmkoqtYLQflwYERlLCYObL-FQRUlDYbB-lwpaXpEfEKv5NdAniZUkfXTVK0HFWWZgUFalmscK27qYCI_RMf30PVO31SZbar-0XUVlje_TcJMUpgDijwFuntvaxn47TVfVcSwh2OjQPfq5gv4kcbFEIM5G7S8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmcJpQ_rrEF4DQjhtvnNlwkUGitBweQluctv4fhxqVOP7oZAR3iMLbI2o9Zkz_rButoql25tEuqHPU4l8bxGOVZOOCZSUF456hErwLVfJsFxpSMp66uwACHq9wZhhMkol2z2_rk0KG5PdNrtIxu8K-odZOzYmrUQQBCmEedi7LgHiGI7nLKLcq0eMFdcI5ZVa3z2Pg3hnAxlZeECzLHhaqr3G3e49GiuDyiAnVHOk_XaxGNEMl9q8KIdaWi-Q3H8t9FO9MZDUUVc-RCudAbxgtmw28jx26nI6PMBN2rDxkkjHU9NYaDYsoJldnogqiIbUDOaJpUlKbCL_xmd5T0SLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=ro4ilP_rk6MiBOgm5XVHSoIVIdg6jJsG7V9CVrWK1k8sMV47sGQ6JyX2g82KCH_G8exSYg6DsUQCpFpwcB1smEapI0Cm2NuiHnXqD4-bn4pbHDX9U2tTnoETFQiG7Sk8APKe4eija9fjpyXT2D-kpIi2Ae21yaxdjw-CnbLFmSWF-Q4iXgXIbqWueUbGXMGnnMcEUnZ_Jablmzxy8dBUki288VPpzCXbesKgVmJOR7jy1AjKC591LQv68LIDA8VuInNrr93gcq02TWEuBXEXH69-UtmAjVnSksxcJcv0XrJseMjh2F27WDAO1X-_OwVdGMpg4HqzJmf5Rnin-jJLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=ro4ilP_rk6MiBOgm5XVHSoIVIdg6jJsG7V9CVrWK1k8sMV47sGQ6JyX2g82KCH_G8exSYg6DsUQCpFpwcB1smEapI0Cm2NuiHnXqD4-bn4pbHDX9U2tTnoETFQiG7Sk8APKe4eija9fjpyXT2D-kpIi2Ae21yaxdjw-CnbLFmSWF-Q4iXgXIbqWueUbGXMGnnMcEUnZ_Jablmzxy8dBUki288VPpzCXbesKgVmJOR7jy1AjKC591LQv68LIDA8VuInNrr93gcq02TWEuBXEXH69-UtmAjVnSksxcJcv0XrJseMjh2F27WDAO1X-_OwVdGMpg4HqzJmf5Rnin-jJLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJwpwxyDu3oQ2TTyyaUOb8_f0ohVWUwLHbdzNZOTLGv0yH7V64libAyEvFtuRkebnx6MKewiJtetWOPJYn7l6IkKs7x8HQZTDAC8PF7YsBRi8VTXwdBrtEJlQr_asem-bkJftzwNzL6hNHL6MnKFNVikp3Fuh0qSKAaSA0BdmFmr9JOPgz72-LZpZDJ5ay-4nOjyGo7cThkg86XB0W8BUK9js9t9fFoycxnieyVbgnQJQ-IQD9tEtZBw27SpwBy5pwr9lF8vRoLT7yYhycqvXX5-pqUvzqGM6pGbn2v6YsTItIcWOku-ckdbnRz5A34qRfwuWSV6u2nDdEGBptttwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQdXWVsGqRyRU_4MeXuEsNIMCPIsq0uyWSXRTIj2KNFTwM-88mGG6CIqyM4cGqByoXRWa2WT7A0ZhsOEEoYVgu5plyJ1UiONGydhFnCgv0fw3xlL4H9Owa3aIzXT4BGvO17Xi86-y9GkDq59UkpvHC6Wn_eigPhzz1ieABiOm9F7ayeixY6bGYfvSVghiNEf0sXNMpx_2gM4SifZez_pWiE1ugL4NY2Tx4YwG4Tm-4s_do2oeGbjlZsE5O6nNHAIPmVnkuhdQWCJf9iAi1wgKPU9OoKPpmyjP1Mb0g1IW05mLtp3EnpjWgedp11Cw52NDjGL-SwFWJCIJVSAPYLOOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg91LmHLx-cccJnTON43IiQRt1K-Sus-FFNDbAZsBAIL7vDBqiNou4GpA05cukj_Q4mrEvcceFzISoMeL_W6D_R4hfoDXY-X_i144g7ZJ1e4V2UqeIPNKCM6oLW0qldULagRYQtV0Kzc-Zw61KBH0-G9DAXfGQZOY-Mq34VhH_4uSJ6ATJ-rT-e_hYM9ZqdulrsoEcGYm-bH4k4eUpVetlsWVcLzttw3dWuRDWUFxQXNoTh7kQ0599ALAwvYx3LsFek8v6VkNPwzdHrGrJzFI8BDnnceeJ6Iprh-UY4UlVsiVF-o76m00tWN7IgdXLK_KJ9DeSTaeBFsc8Khd8rM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmJJzgmoshZGRGca9noNBA6q9gaWLR1rxra_ZyxxUB5cpuYjnzQs7EhPPkBaphAMp8vxgDsQFYE5iwDhHnFBOJQlUDhJjtlf_GFmfNF8nfAdL5zCfLu1ZWk3MueDg3lZojvTsc_NdTnrggKax8j4gi5IhvattDh3c4lku5YiGh7Jt50m0np-XKrSJqw1wdLOCaUE1eNgeFrXpGrqeet4u7af-eO7L10jHKQqLRRJKaeRMkMctixkv5FezOpUILiBZRYUSOVqqUzza3ga2mJJf5Scn3KS5kgBpGyK_mWNjZMqS7BBo0bHpdnrmmjwoRjsm5h6BXqkYvGFzQtNa9u2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfh1zna2gwwRRbD9oLYST_WczA1krHWzHL9_j7CkMOHGUBOQE74aZUPmhNjgWMjJLQF5_25mbYHNnhg5BjsbS0lp8LdSB-0IBKCb83srXdIf5AHaa1TSLzr8xTyxKMXalvM1fgnaEeEzK5k6bzH1km17Z8vfQHpzzmwq-yDPjw46_u60J44-67rRaJFI4XKezNAKAWnBhs_J0eQUFGcYTiyY-MgelMNUAH4ntq4OgLZDNcOZshyQqqdlunxGq2-S8qUBab8qDlCvXyT2-5VIYasqGbf9PPMy1O7dgLkr3v2pXvNY0ixlKxVLqFEGHP_KhcnCagJZy6sHiYH3ubEOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_o9SkIXPcmbZ2ZXM8X6beNoIT6LPH8L9YLID1Urw33SFwnxQ9nR5xrwdRDbsFL3oINzx0Dwhw-9A0oVvco6sfD5uxmJuCrxxFvve4CF_bDKO4-mHs4l8WU-mZtEf1cxtBxPCc68ATMVua02RAAN7zFTUik9ViMk_xmuCMUTGuJ7a0jQKuAABMe1SsYDpRuQeWXwPYxn8tplrsXNVwqlU4PWwTYXOoDUt39zQkGK9M__pqdOitKWMglB1SQ_3gXGvHUas8gr8Q9QKbTuIf0U0TVP-1PLuv1rQ7j2s4o586TDK_EeFMiO16zXLM65QCjy01gfP1Mcz86ybh1fPBoJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcKj1cwU_aCY4hIZiqzx7fcOpCA8EPhThER4RlgUPjHIuVEIi6QlPe8dtlRIfDUyDgljf9f236JJ0YW3Ql6cbLQSzv8KkXio8Qk2SGSU2lwW_RitvmaT4EfbCuqL_Vew4eoH1JRFq1SbMTv_31c6MkWXoZzQ_vclISw-qsAIk9CzpYt3fCuVikBaNUdV18CLlsfsXUSHZK4FFcYFo_SGy4uip6PFN5OOSd3bcZD_pJnXwHjdAt_l3cc0G6RnInmfzf4L4ksDwQzhjgcC16vrH8SdHJ0bk33T1d1isUxDQ60t-2ALD9PXqnjSftWIZQfuAzOSWdmUxIDtMjlq7E4y0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKlqR3uvAy9VvwMVUAP6_5t_73CTWDFpUQ7BmmiTvF55xcQ_s2RuNUv759yj-3_s84H3ytIpw1x9__FDuJMqq7EP1zkUuP2hw-F59GxTv8656ff2BSrCkOoiw_elD7o6UfNCGZAd4dNTOFfJVIcfuP18eX0ynNnQJfUNbcbG3-SEu3G98wjkavDyC7sTF4DiKlcfaNiKFUGS_fmvkGPOiE8ic0PPjVv7mU7geB7zCWbESxMw48WxjeTlcUHqx9boOIoAUQwRDVUMkYUo-ZXPnJxJvZDALtJEZHrRV0uJf2BaUavCBgGS0q4nEJF_Bc5njz8-eGGkWhMarURO9Le3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ede7_ScxA5gfiss7ngxxySIuPL_rf8xjK147VUjhysxxg9pcJtFgUjJiENul5h9sWkIH41GRQFAMR3O0wNQbda6LLKzHPW-kftbo3gc6-7oN27JE275g-XaU_0AaefcEZMMViHyOkuMNuY92YGpZzkIx7aaBIc5Wcc830Rhx2n62AF7MTVAfjhgw-yM5ZeM713B9NFtBYyg09mCWtjTBdy73XRfpXyyEl5Bk7bHGzOqFOAurneO2Oua_EGmkJ5bdeIIc6DE5N2GfO8-1BsgyHDPnw4taFFrqMHIjsFsOE0ipttFc8GBP6aO7NR9o4y3H5881s1-qXEb7k7V1W07-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPQMEMkiVlyvO-SO2NGkZBqNIXvafK7fZf1HsDWDcd8FPNXrxqplNJuyDHToezDcOXQXyEtkd4ilfLaRP2TR5LGwRWCSGJb1sHrT1K5tkmUV9yDQLHaJqtJfdBe2FeKy-hl1YtRH2bWR6TZEf-uHJ6_JotsNpKYj6GHbE5A50dn39du7H4wGLpUphidPVZKMZ0sWcOYACQkuo4tBW_3FewNp3tjPnmo4FQwtyytFWKmOhLwIjqVTN-y-6R8P1L8V5nwfrpXrwH7zIojjsc5QyypUEEL23rtXOpiyto8YNiDMRiC6gWCIhJq7WnI7MGsM5Kjik3WpXkDSlgfur89Mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-LJRWwGMsalhPE5bXPrhhWqwIL6ITvyu9Mwg1bddSNH-rvUO1_O5R3YhkFwkjt8cJOtcwUlpssD5Y_NO4EksndjmI11wPbi63mHywa9FJ85p3D7NtqqcjYzqxJtB3i5JuPkH8sjPoctPyGcStNeLUK0LKxX4R-mkPmr2mGVf3Sc5gZinclWzJwx9VMwukVrixobcogeOqbPaC1Gl2zbkarEJzhdCCSxhIXUdVDX_cze0OLTm36p8FHz-Tet5RpjZsiecy4KovaZMFKYgdeMMI4xyhKhnfDHQlwvGSq5068m_o-FElM592UbgAn6Lt-kbVjsus1f2Ry7TqkeMbHAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVYrDhrCCdmSILEjEu7H4lCs7jyM1BncH5nqILB3xTm2lVs5YeIPj_oqmR0UQnB3nHlWqyFZprFgeXlfqUzFzT_0BooHGThWU_-vq-a8XFLYK_qcBTJOqbG3jS_9qpAC37ueG43LoDXztUTwUj229XRi9dW30sGCL1pcXd0ANypyt9KByKIfk6xNhqAfKhcBvzCZJBX_Ykzs5XHr8x08J0KeDZYalwsqEhD2SSniUwOT_C_oWRWoUIDlH-kM7UeZzxC2zfrO_B01scOrOZLX4Af9w1j8ybr9qsgYg939h1YZKWQCRkYW-Ua53bq3ssJsjMHbxjzmP5idCNAeNirX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KL4kmO7Uf-pSc8BwuSH8xkrfeO6jL2S4XSLBaBdfkIO_ljUSrd4AyzzzbgZCWJeRuup9jS09j3qlEpqqdOOwT4_L6aP52BOLeu7oY07DKyXpTjAUWEWEthRoyiNCS2HHnRokKVVY8ok33TOld0f42BsFk5zSogHhtuyaRMgrPXb8CGsir84bLsAgrOWto1zgWiEqqC7QKmAMZu6Z4Q3XZupYjVPeTC7pKjmY3xSpiMkzprxThHv77zdqzyWm39UHwtjeAkF4gDf3rEvztqg64YnIYuvgnF5bVh8ZRUO9HlkkWTZvppmFVwSvrufla_SiUK_M_mxZzeaEgH6SGzyXNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3IX4DxErGJ9wlvpnEgF6gQM7WhfzgCI0Mo-9rAI7e31rcrGkjiG8aNxpFNWxmthld5RKX1gMWYZanO46U04E7Q61NXG3DJcGAHNC8ivdFmlS7wa7QVaqcg284sY7RHr-sY3LiSIQmwPPpMuidmYUEOGHUp323JuFclnrCbWSs6BHq2geYpX-bG879wrdkXLHabzHIRtXyJYtvFRvNL9q4EY9_4ruD1VxFOP-zM-GqOPVsJG263JP5klWb095OPfhwHjcGtLnDDPHE3gVb3EZ2UZFPjC1iEoWmW1RXu2BmFQqdpYLGcLxVflKTwo88d53S37qn5Ts7CfXYc13TOFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=kr6r5EVuTpDqvm170m5eJUvVVDbj3ygpe7nfqvfvngZumhl1qhfG4h8ligwFCd95v11yiAOGOyVNQVADFn6E_ZdvvBKkW4LAcgj3UtyJDXQHa3Sh_mFqBpIm5ODY_9AV1Kd0BE4nLm7_2kIZNnXJVPGtMuNSTnjmeRt7G2aDLu-jHTryu8awd-vtHdAF60rC3vadSPpoqrlyM4Ukb9kWE21Z30SRppoYMubJ7GIatSsnpBGwE6lkO2fLkC9AbsOnnf3dWJS6iezjzvxLF7jPTFmq5rLjxvU89Gx0Y0WA4vaT8tZuStzjJOuSgs7_xv9xr7S9tDSJqJHZKG_Ukx_SIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=kr6r5EVuTpDqvm170m5eJUvVVDbj3ygpe7nfqvfvngZumhl1qhfG4h8ligwFCd95v11yiAOGOyVNQVADFn6E_ZdvvBKkW4LAcgj3UtyJDXQHa3Sh_mFqBpIm5ODY_9AV1Kd0BE4nLm7_2kIZNnXJVPGtMuNSTnjmeRt7G2aDLu-jHTryu8awd-vtHdAF60rC3vadSPpoqrlyM4Ukb9kWE21Z30SRppoYMubJ7GIatSsnpBGwE6lkO2fLkC9AbsOnnf3dWJS6iezjzvxLF7jPTFmq5rLjxvU89Gx0Y0WA4vaT8tZuStzjJOuSgs7_xv9xr7S9tDSJqJHZKG_Ukx_SIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8zy2pqeFCMgklfAl44NT0RYy2Ar-V1Ko70p7In5s3U-ZXdeQDCY2S_i4hIRDk_V2HRtht-OFJsDpH7ygX__dC1ujVDNZ7XpOH4E1FXc5jxYYoHTQmNXaCsfDcUkMoOtSsontRlERG7UOXlGCSEG0sHB3ZURrXBSTDdvvXYDn64nfVhJMQoOov7McJ6vB7jf0mfIkXdN8vChTHraolTm4qsPWRK4G4JheX7AOxsNkQtd-AIteqUC7T2zaFKbp9lfvP9emmE2Eyn7lWANp7foG50c5fyHdIi6RRrpBGW9u7GfFl_LurCrdz_bDV8bas84JlYKAhhUHJCIfz3xkZrI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=IbZdHD3nSvGef5TSrGwd-nJJoGINwDKHH-vuW03c_oJqZAg4RIdohpx0brnKNHzQu68l1v_jNeoyrssZN9PV0DAiLAiMdfXNFZ-8yv0jF2jUaA8XVQfI73TLtelCFcyGe4frjpYduAcWzNIkXcO7G17x78U9sqik4Bs6cMq8hH4_JRz9Acvppmi4cwF27ckRnN7duBABW33S3rplYtlsFRMTBMgxm7DcHCaY5T6ahKGAK57J37VSjn7v1UjbJFryG6DVz46H4AtTcb236QgCMHSCNnpfzwbxVneVLK3HOtsASjuUoMP8dpdkFcO9EvP0RZXYQO2NhtPyCMXggRYZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=IbZdHD3nSvGef5TSrGwd-nJJoGINwDKHH-vuW03c_oJqZAg4RIdohpx0brnKNHzQu68l1v_jNeoyrssZN9PV0DAiLAiMdfXNFZ-8yv0jF2jUaA8XVQfI73TLtelCFcyGe4frjpYduAcWzNIkXcO7G17x78U9sqik4Bs6cMq8hH4_JRz9Acvppmi4cwF27ckRnN7duBABW33S3rplYtlsFRMTBMgxm7DcHCaY5T6ahKGAK57J37VSjn7v1UjbJFryG6DVz46H4AtTcb236QgCMHSCNnpfzwbxVneVLK3HOtsASjuUoMP8dpdkFcO9EvP0RZXYQO2NhtPyCMXggRYZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6dMThSZSCdoKMk3TRKROrnMk8HzikDQOq9PkK19RcV-QP-WsNfW07bFqBcDu0dAHR45ImSQXOso4WroVtXwDmgoZA58PTOP-EJ519d7YmoqjtMjKi0TGQHxNUapGoiZaKzktmBqlQFyavkuMOnMzjjKtB5nZxl3_tykIZj4e18LHWVdNOpAx8cignseJmJjnOhFjk3UIuQOv2Z1Iex2mW3CnQ29xsKhyWWXrs-eZs3KVsDWE-MlBLSkidRrLHkg5IXIr1g4VxoYXnTWH4hatsosImc5mSZApFD4DgWspb2mYywMCOqBtffn3VjKnXSlXRptiByuN7J0CPmQKUOT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl1H999wePQ0vw_yyr8c9b0au8IVmdSp3MHL-wB6FFO3x2f5JYVhx10sMTmC9mMf8K-Uyeow_Q8dTBBWXMxfuNSQgi_194CYXScZytImJylHm627L0MPUoQVtawYgoe82p8Y9YI0cPiCTm0xbokmVKs2NajRyRhB4H1gQd7j0YPZkMbECD-hzzeNW2_fFus_LNtdoKKLStIM_uj6C1l_itXnrQlApUDVZkrJAwPkrJyHu1T-ZxMjpbK5LSWHUOurDIYrslTVy1Bjz_AbAVBF_vZG4T7qr4BSTbRhfJIMX2aBo5piyO_vDpQYGitRw-UpCRhGFucnNu2wHcmGJk7Rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IftTaoVkIg2Cd2XBESQV1paEjWhEflLQ8-KKutSEsYeq2YlV15sg43ZXKw0Cb4onnTfYJ2uK7Qnf3Q9vefaNdURoHwVVszvF3xnAD2fDb37JIvU1KBHxtNVMwf8M2dTRyDNcN0LQAFoJy0WKVS4IRFmP5DKCc5mtMefSQnmOwIxPLMpDkDmRYepOGypAHpCwD7UxFIS8ApGfsPR2UFS38i8RhKmkUTyI62KTOXLS2EGoX_aklwN_hSkjEbWjqDu4sm8WkxlXU8OTR9q87ivy-36E-lrlyyXP9MGucpUYNnBKA9lJ2mwfUBzoWtaX_b82DksDQ91vKrJQbhVfwe5vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=V1IbJp3atXMEfPV6VL-zG90drvMZexaRzV6LtNULxJ6oV2NMs9WAsVCcy5UjFGqdxKpxVAkhIvR6v8r9nHgrwN3Pn6zaaQoONP0rBPqu-S53HXkEXG5j8T2Y1nZXm3p0CoaZJQbRKUZvgs3DN13fUyOWKY_WwGkbw32LYt03sBJENyxkXdhcV64HqGEoRunGrLR9c7oKz2xXO1EJOPasp-tnWPDtffWpX7T7QDfr9HVbUl-gw7o1nuisfeZuC8f1ZoE-3bpXetGmgFlpRJ-4rpNtWv5wB1JkUOzwHcoviMb3dUjCTllL0uc3x66shg3Fy_HkOMELCWujjNibUl_TlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=V1IbJp3atXMEfPV6VL-zG90drvMZexaRzV6LtNULxJ6oV2NMs9WAsVCcy5UjFGqdxKpxVAkhIvR6v8r9nHgrwN3Pn6zaaQoONP0rBPqu-S53HXkEXG5j8T2Y1nZXm3p0CoaZJQbRKUZvgs3DN13fUyOWKY_WwGkbw32LYt03sBJENyxkXdhcV64HqGEoRunGrLR9c7oKz2xXO1EJOPasp-tnWPDtffWpX7T7QDfr9HVbUl-gw7o1nuisfeZuC8f1ZoE-3bpXetGmgFlpRJ-4rpNtWv5wB1JkUOzwHcoviMb3dUjCTllL0uc3x66shg3Fy_HkOMELCWujjNibUl_TlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=S62N9cvLgyuEVxhtH8NLuFSWAFIleCduM_KFspIRaLdeIgXetC2LLZNcouovDJaGiNw2oAdi_bFGNS1lWDb_1ptcyHd-J4P2M1OXXE__F3A7Jaj9OyK-HnzAps-RfzdepvFDeDGOo9U5CsXoTuyUvCszOqiugTEpwi4GVF5t4RKoPYRAMwqzkavM7jtSqOO8zjnyDIX_lwzQ0VeSi0N5nN8aytFWr38FM0JMCOmsXp7mxXpnOYP56tpcBPCgLmU0aIOZRdlNg5ZxyB1hFTr5vWeVSgVS-Xx5LibxkKNVFtol1hvpay1wB2C1fmkgXo2N7QsgSlmKVov4y6Oc7761Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=S62N9cvLgyuEVxhtH8NLuFSWAFIleCduM_KFspIRaLdeIgXetC2LLZNcouovDJaGiNw2oAdi_bFGNS1lWDb_1ptcyHd-J4P2M1OXXE__F3A7Jaj9OyK-HnzAps-RfzdepvFDeDGOo9U5CsXoTuyUvCszOqiugTEpwi4GVF5t4RKoPYRAMwqzkavM7jtSqOO8zjnyDIX_lwzQ0VeSi0N5nN8aytFWr38FM0JMCOmsXp7mxXpnOYP56tpcBPCgLmU0aIOZRdlNg5ZxyB1hFTr5vWeVSgVS-Xx5LibxkKNVFtol1hvpay1wB2C1fmkgXo2N7QsgSlmKVov4y6Oc7761Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB-L5icrXLSnJn9G8yoJV_k0hZ9zOaRXO2BXGcJaK9tNmu9SWVc8qiCp70Q4pR0xfFepl73a0Uhbd1ReO1aExpXkXJs8eIg426QgCWgB8lkKOooL9CNiBzKP9PSvhxxzO63OCrkZexbNEdEGuCJfIustOM3efah8eiXNc92eMYw3HtDdBen7NI8mWZ_vod01OGetS5sfVA6AdgD2fgp8qZDzdd5RqMk8eEt0TvgWONxLOQrkGvbNrOEscvE1tWA2rP-cmgYW9Mf5QEwWLCtTId04g9NF08RqdN0jXUL1RljUNq3aKt5VJxQMh7EdsvY2ap7I8oTNcUz3IG3rvkS2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb2c2ZgWUJOllnnoyzXnfH5pkGJ6YgvyM3njBq4aS0DBziqxWpzDGisa0e7_RsxbvN5Sw00YMqQul3yhMDvkpBy6HoCVhhiTMw83yfcEZpTKeY0XcD7q6tRjMpBie_jdOsI2MN_v5s3H22VkNhafbG6fDif9CAJ5CSop_TrkNgHiXjYU1MZE11v5etXE6dBWczJNk70usysTn-Ye1axmZchf5jb9Bkhi95hIeMZcpasRX-wAqAZqMkNdLshJKDQx_p-ZsbqOg3ohFqV7SqcC-R1gnNXDunh-3j9xN-Sl-bGwuNwHHtE-3D5JNjZKZHYcea22r_2xhV2ea4BDIxBdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr92Xn4JKMnb33HPQ5iX0Mc5k1KtBqsmug-FOXqkGlkkvyDdRvoe6B1JDDfT7PXqDxzdBXXUdquccatAXWGQZN96Dwlcqvj4ycN4to8sSrlcBsPtqzaQjq1iUx_yThRtJGgTZ_xx9_Nha8ua4OAmJYgmmkxYADNqxlGiOa2K26MhYkGhgMins_B-CFsMP_axuMfV9NR00Y-meFfA2KLCU7w5C9TivUiL_AI6-iWOTTrn9KD7Q7WAwBNiqOVSA6iT5Ri203Yf7mTlegcd3YXlSZROdaiQzC5LP4Py9NUEk9laZIiQA73Rzv_kAy-EN-v38S_dL85cQDsDdMME4bVYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwP-0A1trtCn-Gobbp2owbdUI9q95sbHmwpjXYuesrBcnEerjfVmL_qqz5azPuoQ4dOnjpzFNK0_QVQTyCuY0v7DTlp6ZQTDpZUfkTg5Tlz7eRfeTom-E-1R02RowluCXgdLdeBUMj94Bwpsg7wo6p80mkCygSSOADupeqKuDP_Qe3MqscLAAhPKU8VLIlsLVat9LF5dIRN1mRKsp9fb9t7QkF1OTWM-66BeIm9QaACuY2nQIzFgwLozkx1PuY9-EqAN2dyS_tmhL8mX9U2Uxut4b38GNnjxVyasWWmkj6dQzFiSqQUDB9X2N1ykXR7fQtn46gf-vnx7EHO4_3TwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3sDt8f2I6r5dGom5oxfKhOBTExyWH_VtK0CEBfrwB1zZq7mLldJjs_CT2WMYTBgLcCAzn3NYrzVYovdMo1PTf4jz8LGJFrCWzJkKLAF0TlC34GQ2BKZTOxqkd_Fb_ZhSDE7Vujoonq8xCsV6u9Th4gR-EDoRPyoTxD83N8rL78hfDz41JHpIpwFXat2AYKMjUYshpMqvhKPpKOKw4bWKmiyyM7RikyEZAWL4fa16PutE9nck4lbF4Y0Bia1phPyBpJCLkgfrtAMrvxGtSZJppjkLRqkMzh-_Wu0D4b_AdOq2STI2XIwt3duHT-1kdrzJ7-SGtTeXDtDg3vE2X1E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7rgZeO6_PZhunZ6Aobfu_sOKe4zvkD6yF3SDW_BlPEBkE-dvcNnE_IjoRVRRrCWPykhQvNjFD702uWsTy4NT6CawfbiYOFZjBHSYd0QXMmE3q8Tjz4VwYECQy9n7YCvtSRguGRhKylwhS4qdVvsoJsRAlFxr8KrEHwCsIuXvvDgYjQFfjo_qvqOoASRgFpczA158qMAIRnFg8TDhOt6I5x5Ok6fIHD8beFg1eT0e_wae3aDpL1NCuEgPCDhdmTYIqkT3NWIwarp_yxkd8fcjhKtTQXBDart7tSUfudgVxWncKUTlJNtvVVrxPVA5uhrxEIhE8eK0zG8w6LKu1ppaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2EWkL10qpf7rLt9PJXCT5pl-wgADou4pD9P7woUa67S0oXJjNI5wFQhXnhZBJj-tNiRSf1JKTgJafBIbDC-mn_yt2xU12VGchQgIBLUvN6mJLlnd_fbOEGa9UL--C-NSQBKLs7_d1-Lxj4PcynCDNckpHAStrqjD4h_YqoT2xNk5DszetAXNHCig2w--8J7EKbFNYkgDNWv0Xr45oW7fcD_Wi4QNYPc3AqOKRIDcNxtufDkd1JOd0jeKPMgTgW5wvI1o5D9Y92xWGgreqc-v338UnpC474U_rM6yv5pAO0WwMrZM5OKgIJqoMNjXAf3syjRbDkUf57LOdX-YICgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD5D4BObM5XAavcvw_K0Rz9iTDAm8I6bq0ttmbSt7cWqv5_B0axJ7qn6SM64QTMaK2-qWgsZHcKz6qMGJdmjI_GfzsmSCV4Ef5r84UbSokryMh5BZKrQG6VvEP4wbiHBdlwV5gf7vcVvS_RTAF2TCWkFE7wUQ1pKhjDUKi5mXqt5g13D6T3LqFnUZslC6l3RknlpxcR6kS5WpQAW3Cx37IWAaEr7fwrKE4zVX1dv1Wj2xRu0hPfhtNlzG35r-ydwHMOCy-8aCt8OI2pCE_zL5EHAXOukVGoRVBHUGKNse6zPoFwVKFgFZjLxAbRkRc_YbZlV3a1luPD9VzIHKIN6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1IZSDW_OdAvftadcrf1t8I06e_kxjtTOKIRLhcNugVEGiqTfHjdSyyJxiL8h7v2XKjGy4GN7O238HXbwmwpWLvQz8smve5328bb1IybSNlurg6IuWQ_oJfPmpG0kfVoW-9aEpEnNkqSFJ6ObeQOpfkz-o4MabqQjjvqRyGFYBQIpDxap1unAS8P3PsOo3AIKqx6lanN7BkhlxXvJtR_BoNk557EIZQWGDwIGjGdmnZunGOwQrOxM6I-5hUe0QTejQ1OPSZhXcv2akzzF3jbRPVTPYSa4G26IwxXBWvYLQlvZ-dYLT46Qmy87JkLQFYbUdjEkhTgP53XvPrARALHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTXmCusodUjFenYj9xy651q0NLPI8y3gX59KmLJpyH_yxjmAJkCjT_QXlhRGCWqULhDBeNjsCeaLAcg0hClBNJ2dtGrERD3nC6bjztRA4GejacOFtyYg8nJDoQ-rqeM6VdnvHSY0XzfWtZsJjPlDS9XQ1fvQ0GOqOX3OQlcRTufdVIKub9N_8R9vny7Vmg_eUXPYABxBsXGooUt2Pr_HG3uRVUiDsQEnOiIW7JZLvW9wseiV_UYEdxcnA_MUthSIIOqTTOioKxaC1IgwB-K0c9aFVmYF84FC_PB1FglN6ZhH23Aev9AT1Al914bobO6c6JMvZebQUQVswiHS6A4Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpqY0DpHMijOLTPr6cZjnKYgJ4SAaVpJoD5WbWX_pB3YGRMOpZT33-YOP5cocbDvb9zu2gPtfy6l7OrYFT5N2Q4LQnY5RgH_7seIXM8GJ3RCi69kZZnKMC-GK741mXmaxhsQHLemvK_CLWs6hh2rn-aNO797SukrXhmW6QeiqSHbLC6DO86OVrxIuNs3gnaMno9TF1zNGhFnqvR-lsFb0OA4x25L7s0nF09JIXGYSc_xue7cQIDNv1uSDedOmQOfbw_aZW0MUcM6B-lXpLYEDpGDH6EqR6qJ6i1xhjUUeKn6pE5tCTvnnNi12PzTvsaZu4efXCO6XJzaxf8QzPZg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCemFmEUwy6W-d7mqxcMwpLP_ut6eDzaFs2QECitT1PGZ2UyjL11Cuv7K-UvXRS_sn0Yjv9OL0wQix_iIINOKKK4K4t48fF4XruVPDO9ZGRLdCU4XV8L6RXUuNAqqAZqpYX2V2UIUVBBgHDv2LbRF7w5NbuDXVCvvGUkaQ3RWhM2BvdgOXsezkM08xrbx_m11rF0dcefmJYqfHrc01gOKi2sW1b5muL8s2pHxz-DNPTfQSm06i9A4wenrFu8OqtpbJHQWxzbSv1k5_CSTsGSl6e_S_-8auJ2x0U0qpC0eGstNJvoG_Bp4YQnLd-FgU4jlHsQVAmJ386gjeIVBrjlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDuk5t5wTl8PNYmuSNVwk8_AHfT7ULgo4oGekjjXNeMKomeeGqER2ozlmKvokajoSnxv_xHQXj-AqrpTKzYPGPiUBUISDPDq_GNbxQc_JXMCRuHNTVyX5GD_yDNBqzhXNoCJj0scHxN4rtAhXXt6oCdA7qHIsNjGue2DAncJuRsCVELvJWC6N8NB_29pVDugpizRm5qkdFHiDMpDgVeMSNklcM5kzJ1tvBR9gFCzOCCoBJ6fFEtROCpU25fV74N3E5Sgc6sQ8w2IGsLAtznDZLLB2wiJkGl5_pqQpLWoRG262MvCoFCkHB12MdvpbMtyS67aHtTTPA3R3ptv43fEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuxOb6sZIn-qO2aC159qt4h5xpQ8UIbjaIju103y00qw7RRlLfCgNsyf_92idNXMNty7_aEnHI4h53z0yAxlNvV7YG_JGYL1Dr44Wv0_FhVI8UsWk6IYXowMSoeMy6uBU83pBHfpLy83KrBzDYDj4fCgex1zy_BqJcA0TCjgAgJYqXCLA3e_0DjbyyBJMfTXWjhO1iBETyXNEhBbJq7UZp3lZlfjEU3ZAJGRVlqqbiXvjI6WVoj2THA2_C7APHPNxueZPoVQE94iAlHl97l7eZmugAOSSeHZrQf01-_gpJmQOPiCMa5UkZtq36JUlZGy9RvM2OnzbCUA18-Yncyb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9_tK1jAETXAQvu90oXciwWO2tfV7YCq9RL6QjQcmWu1ko6fAv5wKSBlSuOZ9txpcNfMGl-SuU6s0zHi43crrmSaFsCd6GRd3evi3tzfN9dyXx-pVHHScDgvjCseJH2hcxFexGSnNI7AGCgbCiPK-IbuwJlwl8Dy8toKW87JLQuyMCckT719IhTkiaiccRHQQ2fFLgq9RNursnstvSrtSvV1Vrgbkpeo2RF_7AxbSbZLIC4574d5jUMHetbw25NjbW2iWh-seTkgZBE3WxSD_gzNf-O3YUeUboGIwMPbu7IBVProiyToA6-VbPfV9rgaroEHqNvtw77wYWCGm_ex5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP_Ay3JVkeGm2XghhfoFGteFiLBOH6jtyPDCXHOui_kaL1V9yW5cDGUuYS9Q-kdAX0y05iFMu28HMKMDW1ar-yzlXYBWVsYOTgNbttFvr0jb1A1AADZEnjfcnu-20-NIBFtO_WsCrpveLoZ-y4_1F_knKBhFGFDAFRw9ss4Ryid2E-c4DoW9m7UWbQlrp4YXXHxk2qBHwhiB2y4-iqmiPikK2wyCcu67p_tUZVXpEE76_zJYv2vsyFuhdCHMN5nmJu2klKMfwmnSh8Lj_Fv03-YU3Mxf5Hl-GZZ_UJR1RISzsM8Ibc6o7T-XehEsyUg1cY62pnQjy-OIJIgYSVrGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFQSERncVo6ZK59rJdXlVkXX-xH_3Zv0zUQSPKMR0DxzRJIf0eRKpWYDgMhiV1uPXsIKjRpE1wFbNPN9n8PmHRi1sbNTYz8sI_dVeeJIxkqxgN-TbTkiA-mZ7N3nRe8sdSx_MLIlGi253zDc0U71yrKVdcXkuZdga-RaBSt15M2GR4-g6VWrY6NipBB-SdeR-8CwSYdTaTfbZjfRByX0bsNa94mUpMpR-uwlUv7l8gYzqLN1nz0cro_3xBI1kCTUcSwnzh5mDIka9vN2S82CeJ8xgad-t3wpYjI7xpQ7EkegOtsOHkaJ0iDiyonCVSorjXgphAdX3anl4A9K82QuhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymc0fIdOGy0LPEFIo5JzSfa2rkoYiL8BlQGGTr8MyyOMClhl6cLu7B9ytLP4yAEuERvTUdYaAu-K3C8p7y2eK0qlFRnVf-G87Qd0bIaWDdAKrkETbskdoDQgAQ9KOF2e_qSNnLfVPlHj6SpYrOiYo6ATFtB-Qhu1bxDn655tVt_OYPTNJ7NTB_ciH5qXmikCICrSADUSVE1uLUP42LUei3mh0_L9wKV1N9jHm5HHB5FukKx542f5QGZLtT_Wl7YaKeiPBJmUuOFejCKnIrk7Dl7BkD0XUxv_6EUsEHPDePrwTZRhHmAs417hTwc73EcwGR5AMzjfVWJZo8hXteLniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=Qa7NuMMGvf7UqRXYE5Be3yiBVcu8KQZ1vl9e94HcWjLvaKuwiO7bfuVZSmoZstuhlaoOpcGNLkSUe3INqH9tD2peC6aS2C0n3ojBgKDSYiG-VJuFNQZgYiZPGkSWPFOatc8LJjVesyB6rFSt_VKm1QZLI_PQPSw-H77erSpsmABRhNYyaYRa5_a8tK4hXRbIhXzXs2FaHRP6tXkFnNPOVavivDeAZsmIFgKG3qs94migq18NQ_Q9Vf5VH2YGbsLFRceHmmD2r6NpLRn2jsnKJx5Hyzk5nMLlEjjahlQQn5KKpMbY3SAyvONUYJsxtEJk4gFaLya-J_eiS28F7WbIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=Qa7NuMMGvf7UqRXYE5Be3yiBVcu8KQZ1vl9e94HcWjLvaKuwiO7bfuVZSmoZstuhlaoOpcGNLkSUe3INqH9tD2peC6aS2C0n3ojBgKDSYiG-VJuFNQZgYiZPGkSWPFOatc8LJjVesyB6rFSt_VKm1QZLI_PQPSw-H77erSpsmABRhNYyaYRa5_a8tK4hXRbIhXzXs2FaHRP6tXkFnNPOVavivDeAZsmIFgKG3qs94migq18NQ_Q9Vf5VH2YGbsLFRceHmmD2r6NpLRn2jsnKJx5Hyzk5nMLlEjjahlQQn5KKpMbY3SAyvONUYJsxtEJk4gFaLya-J_eiS28F7WbIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMbQdIzTwumTUAkRYdJWUERz8YdIRtLI7UvRV5Q-iM34EUMv0b6-rTowV-tolJ1dXt669K846BaQF1yYk5P4eTfxJ2ZPG4olEKbxDslBv_wDdKUr1dz7JG-FnWei5SEl8WRqe6VLa1FJVio-7RIqrccrSfQFi-bQAB9y_q0pX-OOdoSXnwJq6I-uJh04g1QjQGYdLc1I9s5j62r8gJXDfToU7sntt0WdPkPzYoHNKdM863pabdUsAa-Fy2WbvYlUt3DT-kFsPZQ1m6RQhSyDA_sUjvLR9wRtP2HsfYEqMpi0LmyVhqm4qG5mcio2M5XrFnos_Bz9PXnYuVsQZJrd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYzmB62cxE-ZZ6YdohN1NmGiaViZPJoL7_uHCq77Ys-fm655Ga4BCSFy-8IQN5rAvVPmE3LjPy_EHo4i5sITLfOMn7rLE9vt5lUWQYJo4eCZNPTnhgLHVxlbQxMRpwmwm88SjFBhD5pCA2I30QYEoikI21hTKT25_UZP1H85Om3XdArL2Wx0kpDM4ww3Bn6c6RkCA8Dmv4vpLhGg5elULUJcS_sHEZ6CTuSipPJ9HysRR1nnnnxrZ7rQI8hTl-kY8M0mj3LBfj2Hwe6o8wiMxzzPdntZjeTN5aIama9b8tWLpqKykc6jbv5Eurj8C4GlpArwDP7U7e5dnjflymdJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj_Sp0E8hMHhFhCPFuEaTOSQy6cVDG4cvRtAuZrtN48p5mOeCXTOKsBEHYAeDdM5IHk_c0AnvK-C6ncQ6bEukFayHjYEpZ8yzBmYmyKZl4KNUlsdmEK4kiE7cxJcSvhrFYxTsUcUZuV7F04yjFEFGPPEVlmUZLg52uE31vgYVwKTEcs4KrOro3nDaWplku99jEJt_a1wYuR_nnjM9PYhCH1vGjVXtI3XyZGDdmxPqNSi9q_uO00Zn14U-e8aaltb2l5y2Flv5wCXCeL3JfnYVae6sbk4QmnxL9rV0fPNHQ4C7fMERJ_O9KovE8OYuC4rUKmkh0WqTO2HdW4STGMzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwgiYKuRtE569SuWXMvhG4IgzYz1CTO4GJumElIJO7Lb30sdEitqZG4PQRToh63avO1ZkpJTEVRKp9QD8gyGqgQWNJeHAtExLNQuASuziSOYxMn0MihevgjCGF9Y4zflzF73p93qyaCDN1stxgkz5IpDc6s8RWmg4DSpmio3YoPLsraIK-fILs3cBUzafEwJyvYaP3MubHMJBx1tMW9scfdAAwZpcrujhSpi_oPYfKM7zdm7d70I-2jrVLB55-sxTUJ73gXhF3R4jz-8dekWeiMRx3B68O1Qnytzc4DEPfqbe-eiswhK_lv0mkLXDudFqpKwFrummbtd6mQKFkYeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKVIr3hEfhPSEjZYsftwss_ZIMhvqrC2rjfLeNiSScggdYs0qm3kCUA73b3cWU62y1-Viq_C1BbPjaUh_HleB3QAG87RTrvS2CPsU5w3lGI5VRvglYfL9iJPodqi--90WqCD-VI8PEpsPDNPZoT8DESz5DmArG48kv1p4HbPNLdTwotC6wB4QyGwTxvMtDNNuxCVzB-qnl5J5dluL-MnYlRmV2youc1NjujtTIiXTZoQSDtOE4a5a4ZFNkxbwK1OreWwVpfD02cmh4ZbYrAaYpRhRGdpPgtZZATNq-Rf5s-QSuz2utwZcNhSTSJUGazMBo7bb7NjuvOFwWM1a3rXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaZee9fONM7h5WUa6rjo2PU9E6WA2M6phrnUvJPT4jbLf9BhXDB8gbx6A3YNQbPmx8AgQXBgqeFRPqx6e-prTCH4jzg0aMKn_wDur7Uwzb3qnUXae8AHb9bDWgNIVgAp_1AQjZJJDlUZ832GTJCrVaZFPIIxlnohpq6YUL5zPbtvdc8rqyBKsQT0WoV0FdL-PsbQAqJ63ShbP4JUxyo-YN7sbJ6LW_rWYpNOK0FadHKgBlDLMaVAUdQlGG6r9l3z2z0jCnCQcYxc3SjmsdumunkVHbBqxevIsCfLPeGhUQ0benh-tcQWBLanDw1al6Mwk7WcNxRumiqPv-sjSOqlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERIlKQiT6r6S5Bsuh1CGK-ekLa9xs-DThmSxo4rqhCCfmRY4hpNKhODhHqjqmvUO2zgP59cHlIhoc_AC_Lmdl7GDmpGckzPTrwviqtDGAVR5Q1E4SzvIHvZWIp7-z6pijZzT6P1yqawrgfpt8rJQt82ErClfqljy3aNPTARLlae4F0b2mkh5pE5CLVpV87C49X7JFqsroSL315I8lPelsONgL5cDms8XBo-i8HFNLodHKkwRymknnsFp5pppiKgGWipbd7qcvnVzJPJmLcY-MO_biZ1p-6cNnrNvJ4EkrEogtSCBxzQHnhmvxlH7yrFe-RfLkGejQBKcPvDD-aadRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKBvZGXCIxpBkddgQS_dZUOtX9ONUesoRCKcyiBmh4CarTc_FM2B2qPJFwH-wCZM9NBLcXcKzrvcwOhgd-u5oY5vOucitNuydTx4NWlQWwg8NFDKrSlaCRgE8P_gLFEPYBaP40Ukmg-zJd-5NZw65sTZlURQVyAzMSrTxOoyuCoaWXAUNaNkjRlpncI5_Smdkk7Be0jlnUOuir_dmcEiM12oz97aGCFaGNc5zs2S_3jTcBYggql0k6k_xahfSltJrE6DWCkipRdPi-WBACVBa3veXC0e8Kb_DFq-dCrgDr0yWONk4VYjJpHbKPTXLOw1pM3RV5RN_eBInkm1CMu4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoua01f71-MyIwhkzsW6u4tX77jcBncayQBo9rvv8Kg3amV2fg9MtpMqg6LUuFt8DVzxBEGNUqn0xHXfx0U8X_CSp5gt7Nf_tgj3kT0NiYWoCz67ILmGTXwwD5IPwFue5Bm7XkQPUuTe4lVRWNiy7sB1HwZCVdKRl6x_fhPBpoTyncGZYpMedQZoix8029pMtoH5IXYJz27LUhdbejQr_WdA0AUQrFvMiHZzT0_MF93FeiLavTIykzK2Y4k8URGo4cEBrClsadxcb8VvgbkHpaJg9jW4QYLrYh58wDwHg2bH4DAEUiVFltHRa4vgEEXimobLqEtKy4eY-aifL_gA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5IgzPD50Y-wrWFeLeaDdBMe6JuWtZ3Hdxi_lLR6hP7JJpTjR4G0W9xFDSde3egnMmH0tYZXUb_ClkC2HVqi6YsVWKzGci7mSbDPdard-laoEpwX720okeAvc3BPPyempmlJ-1DTJb7k1kVTkCEJISn55FlCGyZ8AtzT5wJMa0q_riE-MOCe4KtMS-8scrdIjCn7b15wa_DHlXbI92jJJe_Z81mdf72lu3op4zNF5R3O_sLrmUQNi0ubvp-3sHUak2ol5u9BzkDEVTFl9ZvbZyW1mbXQswjk-5s3wWIIamT5J1CDrT1xKY9Cp2eVDZafoczVl9LzDS-GW84aZkQFlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt5swrvdVBYSeR3pWvs7iHn7Xl81EMEDuc0wCen7HhcNVgNxz5C09xCZsFWtrnv5TbQG-HcTFfwr7GJrbFdRVjcvpNuxU7WkDkF9HXoG1IodWO0A8iH9le87GfKcybdNZQ4NgAL3muq68Jj3phNa17VD78KED6uYESbiN2oKEjMDO2xPqNHJf2-cCytqCskgKFKztAmY2Wf24UhtQxyolZ1-oKAjJGPV0uYGzUUGNak2CsqNfOaevzG1XnAc_nBZUk4d3USbxkJ9aT2QLeE8UJPTHcVkmTzfaucSkIbvZZAbUzvjcZs_RFNNUPWe4S6wcxGHbu-enBCu1hb33zc0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvHfrXJXzradDqAsY3rZWw7UmvGNjz_qva-1hOfbOLTTwGG-TcNbM64qrlBAgPwUzmL904gUn-AoxxdxjBYghC3aLLMDGdyZyZEhg3sDiwhPI0ykBQTdLBN6pDl-2KcPFzZzPFTwL3OGHzVTKmUd8VbIIzf8ZgAqtgvvueZCWEBm5nvPgZv-zRDUYJ9bmK_GgzO24YgIDzmldbc5mje-vubF3wxnSpL1Z2GRfTESJ_0yBmuF7Y-zfGNsYrAg3RMjBtsmgV95PH30YQcG2ADHExqLQjsC9Yic7YmC2O8tL2oDDdeF806J4rr4p5FmCUuKgjj6htKVx4hc6YwNuI1NPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5anjiciO_QohRZaj9ulidrByEGTzn2m6y1XU-4prd0y4dbUTTTXzMtyZRmMvcJazP-PWOxaJzv8cwQeueG35XwwWXklpV2HXO8u941H9tyiAY2Ob9kGXjcKkhnUsxirCBP8egOdkgz1oU8Y6yG0_sAV5yRQJNRp2acB0dLcnTWWroT6UJnsjhMTggoZAiDZg3JfbMJAAzov22Ex8pK_igQyycN_7dxh1MljUF5XqojRN4WtM0E5UJydYhv2CMIE405HCpPx23LCatqR8oQduEER770XcZ9DF1jm5easfyo8R5oXjqchRtoccQYQdYuMmEdR3nXgGwpi7X_HC70H8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=nf66oddNBfk5npqUa3_wIX5fQaYR9Zh-Ghd_5_BzWCADrzx1J0hfIWUzToYA6oO5yQxDDTJEwtklv_DBeU6xNvTMd4TQM8dzEg-8tcfVxjQN4N2ClDthoIQorsh_VjVvfwLc6jH6rdrUyJhM4QW0o4qIuxmJmUTlZ-LEwSIxvLK9MMD_6cCfRCi1tzbA89H9hyNCUd60_YjazjKync8or137XVGtkhjtJ8widL0EvKQVWE7vzHIweGWCFGmaPMONbjMVjrFNOHCqz5y-9ZLQhQX8VANmEgHKF-x6ij7iJTDeFm0PfVlNHMe_-YH7a8cqq0r3OexkpgDdXPmgEFMIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=nf66oddNBfk5npqUa3_wIX5fQaYR9Zh-Ghd_5_BzWCADrzx1J0hfIWUzToYA6oO5yQxDDTJEwtklv_DBeU6xNvTMd4TQM8dzEg-8tcfVxjQN4N2ClDthoIQorsh_VjVvfwLc6jH6rdrUyJhM4QW0o4qIuxmJmUTlZ-LEwSIxvLK9MMD_6cCfRCi1tzbA89H9hyNCUd60_YjazjKync8or137XVGtkhjtJ8widL0EvKQVWE7vzHIweGWCFGmaPMONbjMVjrFNOHCqz5y-9ZLQhQX8VANmEgHKF-x6ij7iJTDeFm0PfVlNHMe_-YH7a8cqq0r3OexkpgDdXPmgEFMIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
