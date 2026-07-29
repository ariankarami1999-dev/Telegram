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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 05:18:31</div>
<hr>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orsd9WHhucG3uH2dR6yyilDnVkxL1UDR7U922C4N5hHqmqhvmY_a0ZsPnefSQwWzkyD7cjXjGCbT0zexJDYKoJKyN8nJYURlvXlTQ5-Jxyl05zxddsSIVIGGI2mv2TKbMEOFBX8G-EPvvqcFmdhmU0_Q9gK1al13tnh0M0mmui-kHgYdzrx4JPWZ_yT2SHOGcVh_wiuMRhQMxejB2qT1Ed0GVqrEV6S6wT_ZVRU0ZMXSTNh5Xs_LbEHgQ2AnArcnrgKK4Uel6gxsMytjwDNI9B7BZrM2xnUYlWSFkK028Ik5PwsXbFgLd0_nZp0xSU60jVGrFEaYrksp0iRCfMZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdfDv4SEstWKVn4oQCim5YZX8ZU8Zm8gpaq0M1uh7d2x1vW6zPfmvghbChes-5iR5uub-QGV2PnYSaXh3SMHRM84Z7dJihwOekBz48a0UkyTtYE8VtdPc3SMC-qDuTGuU16G0WRaROSGQXNJsd_2Q9GqEaVwvo_n_17pOezmApX-QVN0oSqgVNwQ3fh3dRVwIZWsN8Jdz_l6gyO2zP_iJ6CR2Cno2KGbWJr6f-utSSohb-srNZE1cbcbXgTYNmA-5ZtMc0u8XW36iObHQnH8LcjyB5GSWB222r61lipv3lQXb4HnWXmqHDVJ1TX6Jzb202-7IaTHo0U9K8mCQp2a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvetXyuaYJBn2LR8cmxvn8Zolxm63BEt7sgn8cG6DDQ23hlxZEwQsPkmPTgdtHtVtLXqeMoFwyIYVbg_fd5SE7B_VvC_-FY06y2j8FFH6EcwzNp5bbF4crn6ECApqItfhO3el1teUsk9Zv5RbJQn5iI1Aq7CevDHPTXzQ7q4qT4EVkNc-gtZ2HCSvm4frFHv15Ea4gdmwciT50S8cZ7vH5HmaSh4_Jt4kEX7_IsEuv94ciGqYyT5F9zKh670u8u-4_f8oyjg4voYSoswhPLCMRPxUtuAyIGIgq6qbNVYuZiU4-w1Ngm7H5dPjb0ApADweukEF7wWfK5L1pBBMgaTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz8lONVKIPB8szW8wugzURwf-HzFe2z-32Izj4-bSEUTIblhMzNjAL2tqUqMqmDrenNW8rWBkKyEaj6kcK1Vj1tuHeozozv_rC1SMRzObeNPCwY99YZDVb2hTprFkWoxyfFELHVb5Fehu_D9GIxz6qtspEh5xeDO8euNa1zvuDY6DXcF0JHly_02BVHNtDaN420P10rJfSk29OHSVzq-bqAmyu6TN-_5e69ndETmk25kMgg_5AXDmLp95FtFQU80GjMxrUW2Fn_Yy8xGwV16Wl27C8WN5Kys6n3jjBeqytrVy7BrfY2BbJLnntiCnrS9naOFKlYYj8hZvagn4XT0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb62683sueE3BuwpNZ0-uofFmigb0KWyYVWC4D-35QYXeQhljaJkTSQ0xHETkhEd8uyI11K5yVRwbVl0QdRc2WHxYEkhgFZ2rV7WQMdFjapfANjC1JSW8qfhau8OPy0KFICdebzGcmlrZs79HLV8mKIzxi68ldvyMR3E-1rELadHugldSzUXTJSJIYCruuoCkZ7U7rVxwH1y41W0nN1DPDLgjVFMj9QRvcJTnQt8jniuXpBC-CCLWHkrllEzjhPuIeLkQz_wGjNPWi7R5khQ3p5xCFzRFvHBt5mOPRED9aZDxDTza7PdBRMJuNZx0XyVYFQlDD4AeKpd7z5oBnNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmJJzgmoshZGRGca9noNBA6q9gaWLR1rxra_ZyxxUB5cpuYjnzQs7EhPPkBaphAMp8vxgDsQFYE5iwDhHnFBOJQlUDhJjtlf_GFmfNF8nfAdL5zCfLu1ZWk3MueDg3lZojvTsc_NdTnrggKax8j4gi5IhvattDh3c4lku5YiGh7Jt50m0np-XKrSJqw1wdLOCaUE1eNgeFrXpGrqeet4u7af-eO7L10jHKQqLRRJKaeRMkMctixkv5FezOpUILiBZRYUSOVqqUzza3ga2mJJf5Scn3KS5kgBpGyK_mWNjZMqS7BBo0bHpdnrmmjwoRjsm5h6BXqkYvGFzQtNa9u2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfh1zna2gwwRRbD9oLYST_WczA1krHWzHL9_j7CkMOHGUBOQE74aZUPmhNjgWMjJLQF5_25mbYHNnhg5BjsbS0lp8LdSB-0IBKCb83srXdIf5AHaa1TSLzr8xTyxKMXalvM1fgnaEeEzK5k6bzH1km17Z8vfQHpzzmwq-yDPjw46_u60J44-67rRaJFI4XKezNAKAWnBhs_J0eQUFGcYTiyY-MgelMNUAH4ntq4OgLZDNcOZshyQqqdlunxGq2-S8qUBab8qDlCvXyT2-5VIYasqGbf9PPMy1O7dgLkr3v2pXvNY0ixlKxVLqFEGHP_KhcnCagJZy6sHiYH3ubEOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_o9SkIXPcmbZ2ZXM8X6beNoIT6LPH8L9YLID1Urw33SFwnxQ9nR5xrwdRDbsFL3oINzx0Dwhw-9A0oVvco6sfD5uxmJuCrxxFvve4CF_bDKO4-mHs4l8WU-mZtEf1cxtBxPCc68ATMVua02RAAN7zFTUik9ViMk_xmuCMUTGuJ7a0jQKuAABMe1SsYDpRuQeWXwPYxn8tplrsXNVwqlU4PWwTYXOoDUt39zQkGK9M__pqdOitKWMglB1SQ_3gXGvHUas8gr8Q9QKbTuIf0U0TVP-1PLuv1rQ7j2s4o586TDK_EeFMiO16zXLM65QCjy01gfP1Mcz86ybh1fPBoJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcKj1cwU_aCY4hIZiqzx7fcOpCA8EPhThER4RlgUPjHIuVEIi6QlPe8dtlRIfDUyDgljf9f236JJ0YW3Ql6cbLQSzv8KkXio8Qk2SGSU2lwW_RitvmaT4EfbCuqL_Vew4eoH1JRFq1SbMTv_31c6MkWXoZzQ_vclISw-qsAIk9CzpYt3fCuVikBaNUdV18CLlsfsXUSHZK4FFcYFo_SGy4uip6PFN5OOSd3bcZD_pJnXwHjdAt_l3cc0G6RnInmfzf4L4ksDwQzhjgcC16vrH8SdHJ0bk33T1d1isUxDQ60t-2ALD9PXqnjSftWIZQfuAzOSWdmUxIDtMjlq7E4y0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKlqR3uvAy9VvwMVUAP6_5t_73CTWDFpUQ7BmmiTvF55xcQ_s2RuNUv759yj-3_s84H3ytIpw1x9__FDuJMqq7EP1zkUuP2hw-F59GxTv8656ff2BSrCkOoiw_elD7o6UfNCGZAd4dNTOFfJVIcfuP18eX0ynNnQJfUNbcbG3-SEu3G98wjkavDyC7sTF4DiKlcfaNiKFUGS_fmvkGPOiE8ic0PPjVv7mU7geB7zCWbESxMw48WxjeTlcUHqx9boOIoAUQwRDVUMkYUo-ZXPnJxJvZDALtJEZHrRV0uJf2BaUavCBgGS0q4nEJF_Bc5njz8-eGGkWhMarURO9Le3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ede7_ScxA5gfiss7ngxxySIuPL_rf8xjK147VUjhysxxg9pcJtFgUjJiENul5h9sWkIH41GRQFAMR3O0wNQbda6LLKzHPW-kftbo3gc6-7oN27JE275g-XaU_0AaefcEZMMViHyOkuMNuY92YGpZzkIx7aaBIc5Wcc830Rhx2n62AF7MTVAfjhgw-yM5ZeM713B9NFtBYyg09mCWtjTBdy73XRfpXyyEl5Bk7bHGzOqFOAurneO2Oua_EGmkJ5bdeIIc6DE5N2GfO8-1BsgyHDPnw4taFFrqMHIjsFsOE0ipttFc8GBP6aO7NR9o4y3H5881s1-qXEb7k7V1W07-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-LJRWwGMsalhPE5bXPrhhWqwIL6ITvyu9Mwg1bddSNH-rvUO1_O5R3YhkFwkjt8cJOtcwUlpssD5Y_NO4EksndjmI11wPbi63mHywa9FJ85p3D7NtqqcjYzqxJtB3i5JuPkH8sjPoctPyGcStNeLUK0LKxX4R-mkPmr2mGVf3Sc5gZinclWzJwx9VMwukVrixobcogeOqbPaC1Gl2zbkarEJzhdCCSxhIXUdVDX_cze0OLTm36p8FHz-Tet5RpjZsiecy4KovaZMFKYgdeMMI4xyhKhnfDHQlwvGSq5068m_o-FElM592UbgAn6Lt-kbVjsus1f2Ry7TqkeMbHAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLdIKogLBlDfgPd3KV5lKT4SvJxxf3-zuxLRGUpj47C4nOoSrOuebOE3nMryeiI6D8Ng1eMOcUbHsb_ER1MZBdqes6U50v816CWsDi6y0Kzzz_zWBJUZkmMq8oXicMdXtlL-bW4jqjqWFIXZY1ws1bd8OiiNXKTuWjAKZGlnN-RO9acZu5IlqQFiO3KDlXDohFAQeGU3I_g2wdRHUzmMZGsqoZqoNtmwvdp0CKrTMyHM8dwDjBl5g6G2N8LBUZO2FdlNsHm5e8YcqmFubwA4RwABK6Uq1ZmaROYXvLbXTXnlPw51-9gIurjMI-JT_cwdVfMKho20GmIYBMNVjSADDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6dMThSZSCdoKMk3TRKROrnMk8HzikDQOq9PkK19RcV-QP-WsNfW07bFqBcDu0dAHR45ImSQXOso4WroVtXwDmgoZA58PTOP-EJ519d7YmoqjtMjKi0TGQHxNUapGoiZaKzktmBqlQFyavkuMOnMzjjKtB5nZxl3_tykIZj4e18LHWVdNOpAx8cignseJmJjnOhFjk3UIuQOv2Z1Iex2mW3CnQ29xsKhyWWXrs-eZs3KVsDWE-MlBLSkidRrLHkg5IXIr1g4VxoYXnTWH4hatsosImc5mSZApFD4DgWspb2mYywMCOqBtffn3VjKnXSlXRptiByuN7J0CPmQKUOT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_QoLehFqAYI8DWdCQq3emfwa4O53yHby1g-Lg7kqGhTf0501ArWEQM6ERfSp-wkiqbZQgfLB63kdHpHC5BNz3YPhz4txeZfnfcoAWd8ym_x_n93-uZ2rV9YOrRpimxecvyD78yYNWwyp-Uszok088jO4D-NpV7-mwRm_JT9N8paqLOEQvu5Ip_KQEtFDU_4fALT04VHxghCQjMR4JTsHPtBGdOJNXuk33HqUocNSY57rLw7rBeqjBVVpfLlQQwvGo5nUkiVwQi6junesrggxgZTlez4n8z1FNuHvdcjq7Vccc8NJgJ_XgYwRJNcqSdR1yd_fxCuHIP_SG_5WcANPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVHbiiPwF3AWtJ4us7fQpsG7BFYVNcUTSvWFzlJud7B1LxOKRJl2WQKPIO2_V2RG_EnIfURlk-gGCW0WqpbB_-vYLurcWs8e2KLPkIrTwP_y4yYw2EjKxKojdTfNcPpfcel3hR6cctH6YYCE77-Pnd0ZhwRPAGJvTSooHgxvS41EMOTsLXtZoZre3YtZ46ZtlwgomtTrr_yp8S_thSbpkhNIlzEbRNzV90mZUFr9a313ZRX9LgubEczf3wxoFeDMI_Qqo7tjsmH40KM4npBp8XxIj4XhZgE6zP2eo8yB4TBSiZxWplAr3hHDFhxZP0nXoh_RXAXypOuYb5qFHe77g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9PUjyqQuH0KsmVH8OPLj_L6UzW1rkyTHbEDKt5E5g0wRAshKSjKbzW8XFPtqNMFo9AZuT_3X-xYPpy6VSTA9wowu06Ht24xWxO9AzGFxjGKhc4PSe804vhrXfZOy601pUyyABOehtz4KoGI-i-MLNGfIjOPokyaKDseeSOZByhurqaOTFPsIEtF6c3LAPNVrgEiy0iws0aUNxx-3kCRGKOfqr5cs4YwneLQOM-kX7V6sh-yR-X31HL4RDL0Ghgf1LDcs4bZhfuebafU4o0Ax2YYP9R62UcA1FUEPk10arGhAcwPNCGlayJLHwN41_YsUywvWFE7hD_QxDMySOOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPizIAVoAnzw2t79xZkiz9vvP0n42rK7kVXbvrXYM-mEcQjtrlZQoAKGUyATPWVvPYpVUePJDq8BkcjR3DE4DvhhLCelp5jDtd8JhLUKgRCKbLhPyIkiDPlGWeFfxzt098CaDNsZEQgfW_aJGXb9xWPbpRBppfBwh1mAeJA1eLT5MVe6wsS4lLkt8TDH7wbmSrbq8Ajuha7p-t5qSlqG2VpzbPpjRzDMDkeCBLaDqjVtmZF41NnRJE9dIz4YRDPiGlIc-f11fyX3RDuYNJrAb0Li54fwDpSfDpMl6DXRsjm2eIandCBjAOoCm8nSOGxsB8cz1-m5VqUDbhRHe-fB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h42vh_nxaURd9abyrtzqBIwNlF4tpsAuasVFhc3otwGFAq8VAodp78RCFkSQBkXqaXl9LIWvcn1464viYE_JJKksWyMMWQUlNYFkuSQa6IlA3On7-Drm1FGi1D3nSQBRzrMIDpgXduv9f5JIOPAtaw-UIdWfVQRtN0rNmvtAGwKtC3yWpT1Ep4lQxK3oBXx1ihToUuGVr60Zk1VxumMWq22ZBW8aGGQdfji1dToYYDzuOmKBAOqkdPhL0pRM6rM_vToFoH-O0pzgQEcwuF9WCI_vM61g7h-vj9CxZj9Yyq96-LIESn47jobP8Kg6_ShY3rErbYLCbVYiRIHdbZMrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ENTDkBay4E6JNNLGMyiJI1w1MyIydgA0akWdgvwBIZyErQPUAEOv1J6AVqIMyo2uiDGNm27f7Zr7zerbMncU_MNWDDl0XK2ZVD3h_PoBgvxCMqvpE9gdATL3_niF1aa9778Dl3FYQXvfIJ8zDqn1o1dcg6C4OiW9sNFJC5rPWLD6hK0BeQLm--aT6o7MRWlabVVwtxIPHyr2Gcqpy8LwugzZepCYMn834cHbbZXW5P5uvUsqS6eQAD4rq-TwBwc4Coe9LkMJXAyKotiwJ5VaVWaxgWh5buzEGaaVd8kbOgiwpBWrI9lBM60p6XMrix3L6LKlxfNWbuRc7Zdl0jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2V5EkxuYfMZZ-bz7rAuy2CJwV2N6xGASwmXE8cs3D6FhwdaEb7kzAuHEnGqBkp0NIL7dYXUp99yP4rjLP_1DMEftT811fQumKEJ2alUjEHytBlLhlCkBMIhe03r7V4zfpuIt4Ei8ojh3Q953pcW9r9mkiCcDSiv3bKfvdth3wQPKNa2Wv3r6jMfQ7m2hpiAUNnikXmBmhxXQmOq5GT04taF5q0qr_GCyWjU5NeBcXJAbt72GBokB0t_I8ATEVFmsgojnpHBExlvnbpQpRkPdUAFY15Qx_x5oSwXjFT0XAgJ8wICp7FTdEyW1WKqfNFdisuHtyV8PN6dIE16oLhxlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE1h01MtEAqF8Cfrh_8vODPwmmiBLcC8I_8Q7RFwE49xSY59-5X8loJroZumqGTKOJ1B3-UOs2seXmUOUlYdew0OX6SxhSefNFlAGRG8ff1CHMU0pCIxZDeNWE09kL6XyisTYG62BdZfyHoK4nLgOl0hTcMO_KSd4641P0wJzUnmyGOqHF3Dj3EYVfiaCds_5heLkT8Gha42Suagn9yJ2cOm68p00EKIETJgQSxtciHpHoctbfBgmCGCsKsPnRHX23NuoPrrmNgeXhInETviw-kzrsmbmiHQxmJYd6aqtlS-skxcJ4EyIpL_AHBT_bIbryXxOOI_xApIqdO-Eh8iuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC6pkVLNRzFLmFkUEcJzWQYuiqMW932Jb3ccitha3tupKBBXX2-afBd6voZ3IPQEYELMSSHKrwZkNdUjBYuisCXKa4wnxgJtgb2h-DqsAwZbeUnkNOGeu8QO1i_wdFrZIIligKrmF1kCNyHo_bXV_e3D4_RFATG35UryBFagPyr4Lwra2D74dNoqqy99t0o3Ki5aFnxIZpz5UNyIpztNPad--fKzZq6GjyfggfZEkKfKCgBnCCkrrUZZGOnLtwT9Y4n1QsHYlQV-O8hEDZmP2x13Y5JD5B9ij7VqwVy6pj-l-aw2tGEeZYc70ZPt1jKMlo9GpfBmaUjT069cOGkN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sls-q9NIXvHgcNmgNK8TYjU65UW-2rxNw6FtVINCtVElFy2LPNvFdcDfXXLeA_Vr5kvIInLMhRm9e070_CyBq3qW1PavDrjHB4osct0dnr_VN2KfKFnO_WhZl1pwMTF5RMlF2ZQOige6TeCzsFK96dms15e2y0WVLZZCICAs3a1OMnkktnfSmd2bO-IlwS76QftxFcAOpd2ADrBoDrIIbY3FIrB3c3QqkWKN7_1XBnxP_Mxp4bKAs1JIRCJGAEMhAKOS6se93bQzOpxVZSkpWjwC628YTehM9WDCPGrEKIlsQ4a9lfFm5UAVdusZuxY72Ok3qEW675qK4Wi5zx6Wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUyqYD4yLBwBGufiUSyNDPjBa0ibfHji0UGxSYRKIDgdLpqXhLIYJCWC4WD5TFyqKq-KzdvE_-9SdS8GGqNaBSMxFPpE5G9zzrsx_j3JnTcEDtd7isfOqV5qyuVqmmTq5dQTl15tcd8MO1kakMwU-adGazWa0j6b3kjgPAWiAcpBFixxSpxs7l7OIKQyhXi_lVmQ1LM9lf-l02ap_lEEhIdAVZAok0SmlPBFbCJqbMQ48AlK7Dtqeil0477LZliVC-EDcsdjvhQzyweYlzAPkNM8s0jKcMFOWXzAzxyAaejtctf66s_K01rlob0AWdRH87-u4KGGnzjIBkZY3RKUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk_YXzmRflcZJKphEf0bg3eHf8v2OCJi2oPMFx9GF4H4lPKsso0LFy3qCb5S7zc-xF32UQpiLGDhbWhphvrn9weWtt4-MwTxaocpbx-C3BVYnRw9U7wq4f0qbdpcUPyJ2XEQQJTpUp6OcpjXR3Zn2zCeqiRiF_34RW12Q02-gGN_pCbxVWvngzpoyu-AEbGQrFdM6iW4P-BgDaiUPcP0v3KnlrKh3qZ1a_DMRDFQAVAjPu4WLt08k_LYGZNfcktvRvOmuV0WIDfEL97DpryOpqHydDPejiVB7qFj6YnvhMPuikpsy18euI_tJtW4umQfQHolHEOELlWrT5CcFH4rOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfNV2GC5vSRMPii2PFltsbB7iDD59OSI56LtK5k1D0cr3PtG-WtLUw_Cshx8ij2rXlGtAbKmhOgeoWkF7OOSHYs0wtkSh4Lb0-FaZSSXvUQZbul_mXYqF0UpaKDMo8FxGZEe4_Difot-2f16l_achJq9t5bg0ECnIQMXxeXvnmEXcaI1H6Kih83YndbqwynuiZ7JwkHNwk6dohTxkM9Kw11RoYBPQ1gCDooIkEFLNSgApKZ4clpF0Kq-inW-u6Y8VwlOuxpwVkYMXbNyV9N8-xM0NOTBpr_CqqnE4gm_lLIUPEkSvf6POOCWhsLXu5n4GvptvV1aCFlDuDnnrB8K3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTLLSXpcJgadkGpJWNZ8Bo_uFgxyE-dR_2nSQEQa6pra44OMg50jMoG2N_qHXmmiOPO4k-m0rrWKvhjMU4mkY8g1WisUCmE9IOef4s3J2seG7r6gbA7z9KbIcQUyPHuX0xO0hXPO_zHOEOUmRD01tYQ1DQGXGt_O4hRfWL_ddrO0Oou4wmDg6c-rxU1H5cEIdGDOONS2r_gkUscqRxF4pKOdvD07GF3H-IsDNsF1LHh7LE6eUGgbywym_Jbqmtfp-10Q6a0y6i3WqdwDrCsFO7-BZkxUgY8DlEZ8qaGh_LRY0XKsag_crUNUSSXGW1rYXiVX70BsNjn4hAAAxVsSkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZiAjbr13SutGSATn33oN_NGFYnZSyAnGICp9sCJTiWggdebIz5_AXaavINksY-NoPwUoYHY-XcVANXNIWhgUMZMgcEbmSkgQ4wOGazsw3VJd6fhkXMWBjlqwDpNrFBm3i1pJsujV1FfDl7aahvfreE239SWwHws-q9Cnp4apOI-WE0fsdjNdV0UxhU2wp5w5XZLGaisMZ9h02dVKYD9ExNmg1t1ebpwJMQvdDYH85lU9Z1_hlrbZWvzzSWZ-3nVoYLH8L8VRyarkmdnvWqxX3KXuqM1MyHpRi7xG9eMrjwS1hTOnBUhdXskYX4STPjz4ssDEbdomOhYzoF9146VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peK5TeDewONp0O3szFIQDvm7URRW6IGXQRkpMEEUkMhae8_YZe-Ak0gpO9NztlYH7Yz07lUbrj-N67juV0PZCpZyRRTlayEeSDgw1a1IdIX9QlnFgu0D5n3sxo03nZJZ-I3PZd92e6ZFONZ-oiEBh2Ds0TSyo347M6hfbi1t3XF3Mf6AWJhbXnZkz6ArBhwpVO7SEkotTorI8E9-3HfqASbCJ8V1rxfMmfKSxi8AQRnKy_cmAeDhTwP1iA8qGqsrks71gB977Y0OIR0AWELY5VWUaE6jjtbndqnaRBIwUowQSFDrb6YME6uYjciyQNoQem0B1KZxy9LdQSbBbo8kTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGho0k08YIx8II-_7bQxc1eFJ0Q7fQ_UC7K1ECzJCzxbgmRn5TfYLrq500swZU-MXG_cBgQDs476LAnDTyhPS7p7v-0Ss8lvzKeVL1Bc4eZsDX6RUZMXMSc81VvX2v-OEIfOC4XymHDMWcmGiFS1q6_7HxYU3f4dDBM-dWnUc5DCb_LZksvPSZA1rHdQUYe8EoAdBk0D0Fh6morypMll7JjNAgTtz0d_j65trRAhFTa3uONaD9uhOq0k2tW3xy7bD2U-S6hNQrODKl26FA8-kd9bnnfzQSrWNQtdIa66ljY9dYMhSdwZn4CCWNDm47jpbkWAPUJyw3TtrLbqAzo6tA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=ki6FkeJMCyBGmdz_5id3MIiOPGNaaDS0dVY8rrwEWFfLjUZg-g-8Gj2P8__JG7ov8Z9o_yEdWqikYiiLMN28m_k9Gu2Wk7dyUS14C72P_40mpyPPWOWDvXZe00jYCiSk7IT_vf97jOG4bK0nJMfxPAzscG5kCc6bVsTJR83TSdr6kqiSPKgmC6N0962ceST6Sc28y_rGdsEijKCPh7oFCCyY087AYow1_YbKUDCJOu4BRdhqMpWIILmjhxJcHAq4U9ANJKGOHKUMB9588-z4zXoRKt7AJMM1VFC1hqFqRXIv1OlPkNX9EoPkzocnM7W2dXZ73s2KtDVV1wD0YBnzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=ki6FkeJMCyBGmdz_5id3MIiOPGNaaDS0dVY8rrwEWFfLjUZg-g-8Gj2P8__JG7ov8Z9o_yEdWqikYiiLMN28m_k9Gu2Wk7dyUS14C72P_40mpyPPWOWDvXZe00jYCiSk7IT_vf97jOG4bK0nJMfxPAzscG5kCc6bVsTJR83TSdr6kqiSPKgmC6N0962ceST6Sc28y_rGdsEijKCPh7oFCCyY087AYow1_YbKUDCJOu4BRdhqMpWIILmjhxJcHAq4U9ANJKGOHKUMB9588-z4zXoRKt7AJMM1VFC1hqFqRXIv1OlPkNX9EoPkzocnM7W2dXZ73s2KtDVV1wD0YBnzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiR749Jd2qNaY4PFJyk4bQUO2EJTbeq4-CEdMrGG570wvb8FqEp9gveusEas8yIVO4w2YFqtKyglQzyrz5jzLNpaZx3WRnHkf6kSZLdNxW3N4peYULE7kUSb5nmyI3avHhAxoKq89BRx23Ct6DyMed6cyL3uLve563Ae3xpiMuQIYVQexRRYZjxQr3oHFOc-q7kOs3BbCbxRXSV_pfHJ0iXZW6_H6RdL-JGn-agL2BdvOBnuVE090P_6AiWZajztfXjzaR6tEHs8_Rl_J8KH_KQwbtARvSyJ0JxxsdeWNhD4AX5oGnivcaTXrhYmKE_X9yjyON6Bx2L1S4ECeun2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WklLd8Sgnu0YyVSydSGCg1dJ4nKUDNeAoqth_3xHHixEBaLA01-PER5SnN_0nuYkG8nYyDsWnhR6djIx0nvz15DcBQDGqx9p8GvQPNibTB8nVx7-MTIF8HFRPuByspSaSyXvyng4fQemQtf5X9npy0b3qmTWr2q218dADeevFrfiky9stW-wXQW_hLh_wSh2979c9JVtNnbuajTnv9eC2u9xjF4tMT3SMpfdU_C0FZeglK8LImqLVVUDHah9k_iZHczym8p2yUohriebM1tBkA17vvCJOLjQJvTO13wN270-10OidRYLOZ_vXH8sHkmGuLo5EPKwyiELqBolQwvl-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPK1TJSwX7D8uGX9CvxIrlr17z1q_jWKk6uawCQQOXGfABrU4bAd93i-11o_VugpYRUn6U6kdJxZFtEDhUGwkrS-yt3zH4dnwF0YN8cPWtKmx5eM9Z3nLGPvbCr79pybXx3_DHHzoWxdumOiUHYgGHywRe7MPe_lFVXHe7vl1kUyvwd5e2LNkX9YDB5wMmt3a1HQDKAHSLDy_H56sgHmsyWoRkZwk-LX1yX7NRTlo2FeHg0XcC48i-jQPv12-TLaJLZKpS9Xs3RRRSijQHwKEG03syBirrG2u16INxAjcwAAoyctOqIWL3EGQ9uUDtj7idEvZ69IQrEMUGqcvcl3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsZrFYHftYGUOD-Cd9XZ3oVIE3tphowmTKFFlmUkRVZsGpjZMtQjkFNSCoiQQRdKMHInaONAAWcn33d7JAtCUe8sDuxDhnTWfjN98QnLIZBKRius5rVqlwwlwTKux1hluPnmyKc9_f1ecjQvXVxMjz1RhbCmHjRWjKv7yPTYiCItitGiJvallu8PdNkIEW1-VrQsIw8lTHM7GyZ71ir_I1X0rSoV9xwmMRqzVaxFAFlEaeWoQFBlFNND05QQSMEZ-AcIamSd6cf-n-LDWCo1AJ9M1eKYKjlapp4KpUS6bCMYwKOmMhQGTWQEACZBIOhUjwH8iYcZbsiSUbr_iRXKLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayX54S4vLEaTyyTJat4nTvD58ZumD3C3MqkBXfWOxeJ9ezPPrG0oOfw98eWAjjPiEUxp4dt68GJjA3wFmEq34k8wBCkzYkQXHEFJpPP4MB7_gyav1q2P7FIVfmUFjkKSbeQAcRL0Fkhrg47cw7l4Ih6PWMvwBgBNwztTX3wYCorrrcfkpgFQyVw9G1NqvFXY_D1_75zQSI6vqscWJnWb564kSMaVNpSSlKugaODX-fzPGVn3VZaHM4fnbn19kJ4ZD-aT34f55A789uECR1caDOEznrq-CJtpvCoZr8z_5OE4pckELmXuSGmQNBnrkTTQPQes654EC8m1l-yuw6Ep3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA4jWIcGg-BtGOmR1giGX-jbnNDmh-Den8rdizXgJhCFptYGGrMGr3NM-t3SOmR_MI4CqaiOqHTuTy2-UQ3hqzRTRtZOHxfZnchgiwUjmBgA4L7dr02ve8hXc5PkVfXDiagX-P9xnkVFYh_kqAx_2YlK4jJKFGnVozm2tlkwlWCJZp_QE3mNdWKZseCenOxaK9ObmyB7-d1CfJ7EQhVG4oqQ7TC03D8vlnrjtf8AS2SxGWlOhLxgpF00jPXEtBWP7GNOmRcmETKUKVxsK5kg_QTanIVR0SJHcEcXRNZ7ZIgsvknpILCh0BGL2v8ToDxEiS5VxMJbagJWVTQmXqIcEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC63iq4mmuS5_m6JOuftNTB2aLEa_DVbWtYvLCphO9BdhTPVCL2DxHAgPPcNm7y8sZjalWJ7wtKXhJkRvdc6NwJTjshYEJIOURL2KQq-RnJJJoz4WIuVJz3CHsjUegRc1cxZUGcgBJ_Igni0_OnGNrDv8qUfaJ9ch8yFMXoJtllJyCB-aLNIgfaHo0520LJX6TLS8SIFrgBTF6ukY5ySwpZs9ToJXy2lB-Oct8pRkpZXCRKpi8-O1GzN4Q1DZdMfcBMuepXfyD4uk2tUIdYgGl1icOS2lOa2HBM5JpCQWe2_6Ct0_gW4Aa7PwaycLgWlwCzpSrY3gQtmlhloss9RJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYOs3qtGiWU2JUn-YWZWdqT2gYLBCSRYE8s0tqn1QMjncdnPQDn8GDe-fGl_xVYZAZr7QjIpxZIBHq1G8m9rLhEBkRQA4OV9enLBKI6g7yhREM-2dnabjOPLQKzHjm4nP70XA8rUCHDRysBYSwWFMg-iBdNQi1Dywv72eU6D-NgAZJhu1CYvWiYDk7y82yZ7-3RWGq24Zc7amLEsTY0VNZK92itkJMFz-BmyJZgVBCh0qWZTldcq94DK6S8lTSy-JNdAh8iT_rQfSUSKwTcEdYWBnE8AZ6_O3pBiOFEOjqVHQxS8-wLu28pLkUE-sT6IglFSQ8Aw_0GXF9ETxLywWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDPrgy_knQtIbsBRmTcbtbufgRhkpBvRKc0-MfQ5io58VQRI0Yz-NgHN92jnT2mDxFAOLEz02ncYfujiTirn0hGjB9fzrfPoSzAUVWWzvJScci_CayvBNuz3rXvDe6J8RHF6yQAkcQNmP5M91ay6FJv1Eam6A6EdjN8b8Sklm4rshIkvPFjo69tDZtYLQVSjqfXMYoBtO8SM3oJDrkcEYqdTMHX-VUCUboJocOAolTc_XaDB6j7rqCPIUyUB0cNz1fckN5946dQg39iP2TZIdmzm2KIhG4uqdGvuBzrXXd0Qc0MHFkuzoAHAABShvK7DychMrOBID1rvgXUBUz0BnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCzeRAXqK50YRBaZPDxjgREgfNhM2ZKj47hFW7PnT22bMrY9i4n6WOmu9ZqMZjhz1RR7QcpACAVPQsNhOCzBgCcIqU0jnyFXnalxg42sDo2UJvMHVPJvQdcXMUIvCVLg-ewgDI71_yZQamGj0wHyPp3yH--Km-b0BB3OdJc6Y3KAPxg0h3-0vM-y2gStyebteugtAyDmGb6rXcUziyz-KKB48QVzLaGHYN7SYa-M34Fv2CPMOL9RaIrNf5F0lZwPrRet8b0f6FJgP4mG_AWIvES56CDrGp6BSmNVpSx3SvAGBPmWvv57idEGoJZa3MWqX_ZmjR2hQZkZJdGPb_LYiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMvw6-cWVkPJSmuGnQG66U-ksNKb71rZg05PTlFc1FTvmYzoR9liQLxcKz9T0WO9u8m_VlFwtSrA0zLSf3QEpGDATog2yLLm7QL1r0rL0WDq8ap479bxj-Xb0LvHBzPmTEgPNNHUF_eaxebUJl6R0owBZMsTpQCqBa31-B85rQWrvG-DLgRIPRA84738zdfCmZNLuJ-6LvdnOZsQn9c2d3KFpgD-XqE9f_w6J4r5C-9ZgbBjqhw4UVZu7QCRCEF0jJKJ5vzvuZBwMZ68OAxc2i9-gO1HjqDAqGTyf5D5Z7pbZ-8NCOTZUDslE-zmmH-gCoYeRgp2KaAQM3S0ycIsSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA2vNVkWddAtLAbQCAsEqwy0lky2SsOertrtKzc2ZH2iPU4XCx5U7pYGPnVgUbl4JMSJAY5V0_reKHh3ZBCC4b4m1g8V9c03bBggmBTs0dw5AKFa79ML4CARwdNseIyvlL9kpCODwb3K5v7u7CW9rHUWxbV2HuOUo5hAHIXD5M5PoTVeqwc_M4fbOal0WW36qAVli3804OHS-eH7_LPM3oBayPrGXA6Y09CBcKp_B4_xQfEqm_c6R2x1G1aQtvKpVTgl_Ahww_D6mLuQ4Ojh4Njjbp8tiiM83TPMIUUr-3EAtET31W3gZUDSLxF0Xyp7ucaEZ-FSnuPat4Q-WAst6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUzkD6QusQ9gXwJ7Ls_RK15u49ExxNaMhq16rauBxyMcWzCagLbKy2Am6vTe5cNCU3rRakCBCi2INMV2dIqHh_gqIHPmeb9jXIGlRQBwypDLixbKkbz7m5SfmWseRgMZWJ5ijhZFHnKCiXDj_BTQ7RkFG-vmi_0-DX02LlMt4qi_Fn1ire4Lsiytv4NbhYRkhLesvrObLKTkIeklTsbcmk9v3uo3ozzGR5eWTiXVgFCpfGkGg_ckMX6sSRZV5j38GE7lfCU-N95VEnBV7Sr2crbXom8ueqmTNuttSik4kMdRdjA7Sh2LWoW9sNCW1FbYeVcT92c5aU2Jhg7zBTV9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=W5AWL1hSMjaJDrsEQG07z733Ys_8fCPNtNFCDdrnUEt6Tite2LPohuab9QbPNiKPsXg5JwLulJRGBNAqSqrv4_IqCW3ILC3FUDDYQCD8BmJKiIsRyMHwAFaTvUC_ZZ64xX7JzWBXuV8eYZLKuYGkpqhdvF6Tt4UiUA-euRzEWOSp1HJe0WQXEghhZDZVnksjEdDXG63ryQmQjZWpTo7DzxTT5waCxjM5hHo1vcMzh8UfQhqJk3nNbIYHqVC7iOiWTkbwLwZ830GHMNNEOAhZA0BvFH56vHePSMg73KfXtw-EkCF8od55bcoD-1w2fTDP57-hkRmZECjiGSTC1QA2kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=W5AWL1hSMjaJDrsEQG07z733Ys_8fCPNtNFCDdrnUEt6Tite2LPohuab9QbPNiKPsXg5JwLulJRGBNAqSqrv4_IqCW3ILC3FUDDYQCD8BmJKiIsRyMHwAFaTvUC_ZZ64xX7JzWBXuV8eYZLKuYGkpqhdvF6Tt4UiUA-euRzEWOSp1HJe0WQXEghhZDZVnksjEdDXG63ryQmQjZWpTo7DzxTT5waCxjM5hHo1vcMzh8UfQhqJk3nNbIYHqVC7iOiWTkbwLwZ830GHMNNEOAhZA0BvFH56vHePSMg73KfXtw-EkCF8od55bcoD-1w2fTDP57-hkRmZECjiGSTC1QA2kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
