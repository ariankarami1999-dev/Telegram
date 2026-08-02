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
<img src="https://cdn4.telesco.pe/file/AfcILezzwYHZNbc0Dx8ZI4rh_G7jP7EZhqh2YyOliUjfgbcxjyJMKypq7wSKu4pSd-wrF4rtE_deyZJ6ctpkShhv0gmna9R2gJ0VAC7_qJgHwC08KcIhl8-8J3cMb8q2XhR3I8SXzVA90HaDHfRrGL-tEaD3PmjttuiPF7AWGsr8P3FadUyhsfo2VcCje4MmdnsPuw2mBcMPx7Ppm7Hy7OOBZZ4nJgj1i0u3D72tABB2DLJgnHbnnBbqcjjXNZYiagMlhg1Jpf1tv_0BEdG1FaUcvr1gdsURiJ-HbUojLzcCBBFmcPSKERcshazC4hgVaxMrpMDDnGHtxd74vBHF8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 02:56:10</div>
<hr>

<div class="tg-post" id="msg-677917">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from📚مجتمع آموزشي غيردولتي كيان مشهد📚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK5Ng3BN-W2j4vFFyhDcGz_3A23zEB3wFhIYGmovnQbQqRSje2hiwOonzTpIPbmgjTfgcvWso3IAeGo3lTZY_OcmwuKTzFOklwiPXnExB0kVzZST-KFmShVfVszY9sm2JzGJRMbkq7VHSLIoWQ9CIOJE0L0s8zTnacLobH_7O6xBSvQNkZGkixAoDHLZE-LUF90cwJqu8qKLEJvKnlozxQQ1Gcn7izOLaOUzdI2clk8TzrmheRE_VuzO9UNehkX9i-OFmoJgOdr73O2VkPaZLPvVE__rG6nqC5uM_DXAAL7orfeH03y2u9O1HpF_fMaIFKDXizBo3ivxu1WYusm1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
مشهد
💎
خانواده بزرگ آموزشی کیان
💎
📚
ثبت نام مدارس غیردولتی کیان ویژه پایه‌های
اول تا چهارم
،
چهارم تا ششم
،
هفتم‌ تا
نهم
،
دهم تا دوازدهم
آغاز شد:
🔹
(بر روی پایه و مقطع مورد نظر کلیک فرمایید)
🥇
غیردولتی اول استان خراسان رضوی در کنکور و دوره اول‌متوسطه
⏳
لطفا بر روی مرکز مورد نظر جهت کسب اطلاعات بیشتر
#کلیک
فرمایید:
👇🏼
مدارس کیان (پایه های اول تا دوازدهم
)
کلاس های کنکور و تیزهوشان
سالن مطالعه و مشاوره
ثبت نام نهایی مدارس
💡
اینستاگرام
💡
اطلاعات بیشتر
📲
📍
دفتر مرکزی: فلسطین ۳
05138414444
📞
09155100510
📱
موسس:خدادادی
09154440510
📱</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/akhbarefori/677917" target="_blank">📅 02:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677916">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حمله مجدد رژیم صهیونیستی به ارتفاعات «علی الطاهر» در نزدیکی نبطیه در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/677916" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677915">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام دریایی بریتانیا: گزارشی از وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت کردیم
🔹
این حادثه پس از آن رخ داد که ناخدای یک نفت‌کش اعلام کرد صدای انفجاری را نزدیک به کشتی شنیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/677915" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677914">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
طفره رفتن ترامپ از پاسخ درباره جابه‌جایی نیروهای آمریکایی از کویت و بحرین
🔹
خبرنگار: گزارشی وجود دارد که حاکی از آن است شما در حال انتقال نیروهای آمریکایی از کویت و بحرین هستید.
🔹
ترامپ: من نمی‌خواهم در این مورد اظهار نظر کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/677914" target="_blank">📅 01:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677913">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
خوک کثیف درباره ایران: از ما خواستند که این کار را نکنیم. گفتند: لطفاً این کار را نکنید
🔹
حتی همسایه هایشان هم همین را می گفتند. ما فقط می بینیم که آیا می توانیم به توافق برسیم یا خیر. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/677913" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677912">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خوک زرد درباره ایران: گروهی از مردم هستند که آرزو می کنند من این کار را انجام دهم - به سادگی بمباران کنم - و گروه دیگری از مردم هستند که نمی خواهند من این کار را انجام دهم
🔹
خبرنگار: آیا ایران مهلتی برای دستیابی به توافق دارد؟
🔹
سگ زرد: خواهیم دید. من سعی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/677912" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677911">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سگ زرد درباره ایران: عربستان سعودی، امارات و قطر همگی از من خواسته اند که حملات را به تعویق بیندازم
🔹
این یک حمله بزرگ بود.
🔹
وقتی متفقین درخواست تعویق کردند، باید بگویید: باشه، ببینیم
🔹
خبرنگار: در مورد ایران، الان چه اتفاقی خواهد افتاد؟
🔹
خوک کثیف: ما با…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/677911" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677910">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سگ زرد درباره ایران: توافق در مورد هرمز وجود دارد و توافق بر سر خلع سلاح هسته ای وجود خواهد داشت #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/677910" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d1e60a8f.mp4?token=sRpkAGhf01RS9kraqeqSf_YnqsTiN8jrsDs5g7C5vsk6dqQBiJFqrvsTMiIRBau4CIF7kU2Qta1KX-i3q6QJ4GRtuo_61bHm2eUNHaI8J4XARqlPS6lCSl_7OO-60yaTgukbUsPU6xTQFzGUYDd_worWZBKPrShmpeyAG4oxq1Q90xeRiHVw8qAMf2DqaSMQK-o4xW7BNueHrgOQKLpm4hmuG7gCdch6LAKEkDJd9AlFpBPgIkCzc5OgkPL6yla8LlLOeFC9B4LcVM5zicbWxaSHxG2uk2cfec2hg5Xy5E22fnLkxnAI-YQdw3Pw49YU_CP6GMj_2vc-FeYn3wr9lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d1e60a8f.mp4?token=sRpkAGhf01RS9kraqeqSf_YnqsTiN8jrsDs5g7C5vsk6dqQBiJFqrvsTMiIRBau4CIF7kU2Qta1KX-i3q6QJ4GRtuo_61bHm2eUNHaI8J4XARqlPS6lCSl_7OO-60yaTgukbUsPU6xTQFzGUYDd_worWZBKPrShmpeyAG4oxq1Q90xeRiHVw8qAMf2DqaSMQK-o4xW7BNueHrgOQKLpm4hmuG7gCdch6LAKEkDJd9AlFpBPgIkCzc5OgkPL6yla8LlLOeFC9B4LcVM5zicbWxaSHxG2uk2cfec2hg5Xy5E22fnLkxnAI-YQdw3Pw49YU_CP6GMj_2vc-FeYn3wr9lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اربعین، به یاد شهدای میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/677909" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سگ زرد درباره ایران: توافق در مورد هرمز وجود دارد و توافق بر سر خلع سلاح هسته ای وجود خواهد داشت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/677908" target="_blank">📅 01:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198c9fbfab.mp4?token=t06CknhaJ33Z3IMnSHtp_kfNU4Vl98lpacvAWhiYSZMAL1_zSgUsFJxnjuRvFXy8EEGGpbyHl52qWnTvCk73XXE-m6ImcmeR6ey9s8PXezsL5x7l2nsnL3EqDkd-krKHCZzhfr0MiTJJ2AEyNHj1w23uS1-JN9L4bzjmiCpGsmpLdETu_8SeukgcdOMeJpiq-QIE8B1_I8vYo4M5Bqgy82Bibuffbx9MR_me0cAI2Tv62QRYyz2iUg1pLIlwtZmvEBIy64VIh5vbRdV_iY0n8NtqYuRIAHwqCu-fSRzT2_7chzDmxSzRIut0HlDhMDSbP67T9_tleZPP5zF6PFGaXqCB4JxcWKLc8k5bnl4uTPwaVCD0Rubdb4FwSbpD5VrRoaa0JqnqTF4_nvtiQo1CKfwVKehv9QI1VkcFq9q_hsvIq0MQBBxODQozOBO6O4Uwco_6i1wq-zilEC9IxrcXp94W2XwC6vTRu23RC7SwHfUMugaZ_EWFzia8_YcRkEAzRDdjyFzHJ7179pU-_UQZvFy1jfW9YlMkOzwVJ5B45w2RqRIVEggrgq4KLBW1sFiaLHN9i49vRd0IfiiKKKVf6R98VypVQvzpzuyRJp0fHnkvT8k7cayECxrU_dJKc6VXtgz1Em6N2O6S7YRUZjf92XhzuID9olPW1pdvs5V3B8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198c9fbfab.mp4?token=t06CknhaJ33Z3IMnSHtp_kfNU4Vl98lpacvAWhiYSZMAL1_zSgUsFJxnjuRvFXy8EEGGpbyHl52qWnTvCk73XXE-m6ImcmeR6ey9s8PXezsL5x7l2nsnL3EqDkd-krKHCZzhfr0MiTJJ2AEyNHj1w23uS1-JN9L4bzjmiCpGsmpLdETu_8SeukgcdOMeJpiq-QIE8B1_I8vYo4M5Bqgy82Bibuffbx9MR_me0cAI2Tv62QRYyz2iUg1pLIlwtZmvEBIy64VIh5vbRdV_iY0n8NtqYuRIAHwqCu-fSRzT2_7chzDmxSzRIut0HlDhMDSbP67T9_tleZPP5zF6PFGaXqCB4JxcWKLc8k5bnl4uTPwaVCD0Rubdb4FwSbpD5VrRoaa0JqnqTF4_nvtiQo1CKfwVKehv9QI1VkcFq9q_hsvIq0MQBBxODQozOBO6O4Uwco_6i1wq-zilEC9IxrcXp94W2XwC6vTRu23RC7SwHfUMugaZ_EWFzia8_YcRkEAzRDdjyFzHJ7179pU-_UQZvFy1jfW9YlMkOzwVJ5B45w2RqRIVEggrgq4KLBW1sFiaLHN9i49vRd0IfiiKKKVf6R98VypVQvzpzuyRJp0fHnkvT8k7cayECxrU_dJKc6VXtgz1Em6N2O6S7YRUZjf92XhzuID9olPW1pdvs5V3B8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعاتی پیش، ازدحام جمعیت در حرم مطهر امام حسین علیه السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677907" target="_blank">📅 01:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POMtaX-uf0CXTWcAJ_Z8n5iz9vQ_AQ0z1d3pkxyS_i8G7nnZvoo5KhsBTEV5-ibW5E0ztdUR6J1bey9wywd5QobzQ_g1j4cIqnhyxiDrDydcHTAYkznr-vyD-6UhZp7nnutaezXRXtDP6Erd3isbrQO-CnbokdhRNtFGC8KVvd-PP2W_beKKXaAt9RtlrAtG-u82y-47TNHgND286HTDCaO5qRviLfsLzxZpN3isPtzodlx0TKyWsMzoXgymwF2Yh5d7eUnhJgK7JMTk6xNxkfG0XRt-4cFHMkD3_4Bgeg_wCGl_wuxcottceeaIi2iydnTJ1ZTcGhztJ040z8QJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین صدها پهپاد به سمت روسیه و کریمه پرتاب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677906" target="_blank">📅 01:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWI3eWKjzd5n8Mrjxzrxb01wV2bMrcVlJLVjZLsYusOPIr0pTQOoQ5DMtElDxl3DPMN8eMvbD2LoHJfTFt6iLQ6CZy-VErDLvlQF8Bgt1D3_Hz8UVx3-p0Ghs5raYfy0jhasiS1mkGrop15_vowtavzzK7ACtp9ElwtoxvwSDga4x1q5KFvGlrRhYB9YLDm3Rlc0H8E9UXyL8hvW_lcxQjfg2xMDUUGt6Ljmt-QRA4stogz2JOAyNHo4RavMulmwwFpK1k0Zv-e_GIOgDGq_7dCnGLqSRRrzzKB_AFPTkIKfcj_f-I1EzxWjDSXDr2unlakrrlrqQNMfY5QwBsJi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع خبر از عبور یک نفتکش از کریدور فرماندهی مرکزی آمریکا داد و همزمان با ادامه «مذاکرات»، سامانه شناسایی خودکار ساعتی پیش خاموش شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/677905" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
این اپلیکیشن‌های برنامه‌ریزی زندگی‌ات را متحول می‌کنند؛ قدم اول برای تبدیل شدن به بهترین نسخه خودت
🔹
Todoist:
اپلیکیشنی برای مدیریت وظایف با امکان تنظیم اولویت‌ها و ایجاد پروژه‌های مختلف.
🔹
Trello:
ابزاری برای مدیریت پروژه‌ها با استفاده از بردهای بصری و کارت‌ها که برای تیم‌ها و افراد بسیار کاربردی است.
🔹
Notion:
اپلیکیشنی چندکاره که می‌تواند به عنوان ابزار برنامه‌ریزی، یادداشت‌برداری و مدیریت پروژه‌ها استفاده شود.
🔹
Google Calendar:
یکی از معروف‌ترین ابزارهای تقویم برای مدیریت جلسات، رویدادها و یادآوری‌ها.
🔹
Microsoft To Do:
اپلیکیشنی ساده و کارآمد برای مدیریت لیست وظایف روزانه با هماهنگی بین دستگاه‌ها.
🔹
Habitica:
یک اپلیکیشن گیمی‌فای‌ شده که به شما کمک می‌کند تا عادت‌های خوب را به شکل بازی‌وارانه تقویت کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/677904" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f7279d42.mp4?token=CWtG6A8VIjns8i2WGgkXUfFKUeAV8Xy-oREXtVoojPlvC7foYCUdCDIuoqi_2F7JFqHQWTjWCH3LD06vQ1jHbfzyUiGQn4FQj49axgVVchM9jD-AGfqSVS-VGrADDqSrJcjWvyqlexrLjMkyvmjyFLq27M19v5aAdDVJmupovCrNuXwJEWZyPPF4o2g4YcgI3WxuAPR8n_7MrS-e3AdyG1kr6o3cL9W4wls82BKde5IC6OMTdCZo5cWfQXFLn4pLBqknN9uenR5VVRYkAE5pNMvPXpK4FOsc59PUIR5V6RuQhNvhs3hkTw9RQqRWf4o9fNIw66T8ZT2H3_ngbcs8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f7279d42.mp4?token=CWtG6A8VIjns8i2WGgkXUfFKUeAV8Xy-oREXtVoojPlvC7foYCUdCDIuoqi_2F7JFqHQWTjWCH3LD06vQ1jHbfzyUiGQn4FQj49axgVVchM9jD-AGfqSVS-VGrADDqSrJcjWvyqlexrLjMkyvmjyFLq27M19v5aAdDVJmupovCrNuXwJEWZyPPF4o2g4YcgI3WxuAPR8n_7MrS-e3AdyG1kr6o3cL9W4wls82BKde5IC6OMTdCZo5cWfQXFLn4pLBqknN9uenR5VVRYkAE5pNMvPXpK4FOsc59PUIR5V6RuQhNvhs3hkTw9RQqRWf4o9fNIw66T8ZT2H3_ngbcs8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه ممدانی و ترامپ از زبان سناتور مطرح آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/677903" target="_blank">📅 00:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be19caed81.mp4?token=vlYqK_cHMSfl5zl-DzDFgeGD8wm3juWScJlNPi5FzGYdzWZyVBzYL_8SKR7Ekrl8a1LZneUWUomx_lLaL3BHVHyJUggHjp8JG4LzjFKM9AqDKurzEBBXtxooO1oZ_YLopy-txnaHkh6tocjlu0Pxeicd5tPqA5DXyRSB3r8tThr60jWLC5ZBjVIySw4d9ZbTGQ5DHtDmNeyePBTqUskyMSvNczAR5Q8sWcg1mmDonzU5aBglZqAkB-e2u8Iqok072FryPWfUJh9nyMnO2TcEq4BI8pXLvHQ37-hQV5TldUcRDPIah4lqItNGD7rLf2JBMWvppYxyxGaI5YAmVwxavg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be19caed81.mp4?token=vlYqK_cHMSfl5zl-DzDFgeGD8wm3juWScJlNPi5FzGYdzWZyVBzYL_8SKR7Ekrl8a1LZneUWUomx_lLaL3BHVHyJUggHjp8JG4LzjFKM9AqDKurzEBBXtxooO1oZ_YLopy-txnaHkh6tocjlu0Pxeicd5tPqA5DXyRSB3r8tThr60jWLC5ZBjVIySw4d9ZbTGQ5DHtDmNeyePBTqUskyMSvNczAR5Q8sWcg1mmDonzU5aBglZqAkB-e2u8Iqok072FryPWfUJh9nyMnO2TcEq4BI8pXLvHQ37-hQV5TldUcRDPIah4lqItNGD7rLf2JBMWvppYxyxGaI5YAmVwxavg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان: من یک مشکلی برایم پیش آمد که گفتم نمی‌توانم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و سردار غلامرضا رضائیان، رئیس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و به شهادت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/677902" target="_blank">📅 00:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61555f46d8.mp4?token=PVjtgCmdXZbONcFXvtF3P9UtT8RoDN12Q0x2jqJY8TH2k0Goer7ZRz-DpAqdJOGve8ChE6hYTv1EdiIH9Yr4jvTQVWOG159XU7QmOG-BL2Y5d-f2lKzWure9z6gdoE8fzu6Dt9y9h5CDKcBgeB94jz-iOQaXLivbGh5YfEK3LSYDXBREw6iqItQnMyEyuAS7dp6wB-HZJqLVyrDJEJNeG8Ku5x6Sg9y42WMUxeG6_KyF51s9Xm1tgC0MSMkHWCSDlGerKByVxGCc6jvcj4in0fERiye4W43up2Y1ZtkBrzu4PlL-zZxecClTppTN58XXPCbQ0EHU_zPNYv-F0zO9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61555f46d8.mp4?token=PVjtgCmdXZbONcFXvtF3P9UtT8RoDN12Q0x2jqJY8TH2k0Goer7ZRz-DpAqdJOGve8ChE6hYTv1EdiIH9Yr4jvTQVWOG159XU7QmOG-BL2Y5d-f2lKzWure9z6gdoE8fzu6Dt9y9h5CDKcBgeB94jz-iOQaXLivbGh5YfEK3LSYDXBREw6iqItQnMyEyuAS7dp6wB-HZJqLVyrDJEJNeG8Ku5x6Sg9y42WMUxeG6_KyF51s9Xm1tgC0MSMkHWCSDlGerKByVxGCc6jvcj4in0fERiye4W43up2Y1ZtkBrzu4PlL-zZxecClTppTN58XXPCbQ0EHU_zPNYv-F0zO9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاتز وزیر جنگ یرزمین های اشغالی: ما ۲۴ روستای لبنان را ویران کردیم. هر خانه ای را ویران کردیم
🔹
آنها برنخواهند گشت میدونی چرا؟ چون جایی برای بازگشت نیست. همه چیز نابود شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/677901" target="_blank">📅 00:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=gV7MKrLuMQOpVfoaHiVWFq8GqmzavwGKcBbdgUqB6JQ0ElKKdPqfc78XT2C2hMmOpT--81jDzZBMdSiLyj8YksowMbyJoky44OvyLpmH5HbWrTPjckwXMjBm6rzIUCGztpYHxPFskbDngRisFlXd422qPPnUfaUq4dw-ZJw2gDXS3LG0CtWhUhESR0GftE5upxgzKZHiD75MeW_Fho07Fd9sSPdRBS6I8RaPn_ABYIiIYtMkdRg9JK_iJXTctT44VGYAR7OHCOBOmxRoZARKRUMwFwiys4WLNb3z5oreLPYXEHdqAbcXO9kYSXzG-y5qm3-ZEbmW_5iRab6rOhxKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3c943d32.mp4?token=gV7MKrLuMQOpVfoaHiVWFq8GqmzavwGKcBbdgUqB6JQ0ElKKdPqfc78XT2C2hMmOpT--81jDzZBMdSiLyj8YksowMbyJoky44OvyLpmH5HbWrTPjckwXMjBm6rzIUCGztpYHxPFskbDngRisFlXd422qPPnUfaUq4dw-ZJw2gDXS3LG0CtWhUhESR0GftE5upxgzKZHiD75MeW_Fho07Fd9sSPdRBS6I8RaPn_ABYIiIYtMkdRg9JK_iJXTctT44VGYAR7OHCOBOmxRoZARKRUMwFwiys4WLNb3z5oreLPYXEHdqAbcXO9kYSXzG-y5qm3-ZEbmW_5iRab6rOhxKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی عراقی‌ها با زائران در مرز مهران: اگر کوتاهی کردیم ببخشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677900" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ebc555731.mp4?token=ZYLZJ2Uz8fcigMcWlzCm179AOb_NnSehE7Mb6cHkYpR4iA5yG50XPmlW7tx6Lhj-Cpm4W2ofcrQtfvgGtGoSiSabCzsw6_wh7eptS40PdWybZS2EB0lFiaoN1pUId0Uo1tiyzIgpUFfSGMc9H3llv9PRK-V4Xhm_wwVSSzvAtaJdf4vTNbyf-82xV9FGTqWTDZ1y1c1iOET0jqy-QkfXB2Gih1MCGY_TZUhRsvF8qN6lpUvFlQtqE8fEdfyvzclu9DajNJ-NIAMgghq7r6Sl1mdccTAQXukb2gKw6Up71E7csG0yb01bD49IlI-WVEIcDFPq2TPItDR0THq5hv1hK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ebc555731.mp4?token=ZYLZJ2Uz8fcigMcWlzCm179AOb_NnSehE7Mb6cHkYpR4iA5yG50XPmlW7tx6Lhj-Cpm4W2ofcrQtfvgGtGoSiSabCzsw6_wh7eptS40PdWybZS2EB0lFiaoN1pUId0Uo1tiyzIgpUFfSGMc9H3llv9PRK-V4Xhm_wwVSSzvAtaJdf4vTNbyf-82xV9FGTqWTDZ1y1c1iOET0jqy-QkfXB2Gih1MCGY_TZUhRsvF8qN6lpUvFlQtqE8fEdfyvzclu9DajNJ-NIAMgghq7r6Sl1mdccTAQXukb2gKw6Up71E7csG0yb01bD49IlI-WVEIcDFPq2TPItDR0THq5hv1hK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد راهی کاخ سفید شد
🔹
دونالد ترامپ پس از شرکت در مسابقات گلف، راهی کاخ سفید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/677899" target="_blank">📅 00:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حملات توپخانه‌ای رژیم صهیونیستی به شهر خان یونس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677898" target="_blank">📅 00:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تعداد مجروحین ارتش آمریکا در جنگ ایران ۶۵۳ نفر اعلام شد
🔹
بر اساس گزارش شبکه ABC آمریکایی، تعداد مجروحین در ارتش ایالات متحده در طول جنگ ایران به ۶۵۳ نفر رسیده است.
🔹
از این تعداد، ۶۴ مورد مربوط به افسران با رتبه بالا بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677897" target="_blank">📅 00:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd733b7b6d.mp4?token=H47RCQ853rwXnlxspr7vnBh7ICZ7ZVaQHSiVhqHhnUEGpNkw-OYy9bHvjlkYMYwzz4ow1mbso75SPbkN7v89mdUOxBcGUlyLeMO1MLn9vAh_nncDLBcjEKcjj1T_MGa8soiQ9yLtDxB-LON3atHh59u_1OEXOHhEmljZOGOnQ2QS71z8w6FBoRnQ0_qWQJTKi5svsE3ODFlz3wwJIEnGYUXk_NxQf3s-hk4uiCLA9tVu-_JdPlfzo2CyZl59JMjN5iS034z35Lj969ndmJDi_Vn60oElv3H-XrRedD-3YtPqQPzVejeq0Xck-KjBcFFCcfgO-Sif5rzqy3q99ExV1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd733b7b6d.mp4?token=H47RCQ853rwXnlxspr7vnBh7ICZ7ZVaQHSiVhqHhnUEGpNkw-OYy9bHvjlkYMYwzz4ow1mbso75SPbkN7v89mdUOxBcGUlyLeMO1MLn9vAh_nncDLBcjEKcjj1T_MGa8soiQ9yLtDxB-LON3atHh59u_1OEXOHhEmljZOGOnQ2QS71z8w6FBoRnQ0_qWQJTKi5svsE3ODFlz3wwJIEnGYUXk_NxQf3s-hk4uiCLA9tVu-_JdPlfzo2CyZl59JMjN5iS034z35Lj969ndmJDi_Vn60oElv3H-XrRedD-3YtPqQPzVejeq0Xck-KjBcFFCcfgO-Sif5rzqy3q99ExV1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت جنیفر کینگز، فعال رسانه‌ای آمریکایی از اقیانوس انسانی اربعین: اینجا هیچ دولتی هزینه نمی‌دهد، همه‌چیز خودجوش و مردمی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677896" target="_blank">📅 00:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نیویورک تایمز: جهان به سمت یک جنگ جهانی پیش می‌رود و به نظر می‌رسد هیچکس، از جمله رئیس جمهور آمریکا، کنترل روند حوادث را در دست ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/677895" target="_blank">📅 00:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واردات موبایل از ۹ اسفند متوقف شده
مهدی اسدی، عضو هیئت نمایندگان اتاق بازرگانی و انجمن موبایل، تبلت و لوازم جانبی، در
#گفتگو
با خبرفوری:
🔹
با گذشت پنج ماه از سال، آخرین ثبت سفارش واردات موبایل به ۹ اسفند برمی‌گردد و توقف واردات، باعث افزایش قیمت گوشی شده است.
🔹
افزایش جهانی قیمت قطعات، رشد هزینه‌های حمل‌ونقل پس از جنگ و جهش نرخ ارز مبنای واردات از حدود ۷۰ هزار تومان به ۱۳۰ تا ۱۴۰ هزار تومان، از مهم‌ترین دلایل گرانی بازار موبایل عنوان شده است.
🔹
در نتیجه این شرایط تقاضا برای تعمیرات موبایل، خرید گوشی‌های دست‌دوم و استفاده از لوازم جانبی افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/677894" target="_blank">📅 00:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e4715e7b.mp4?token=OMC0rrj96tPo4pkdsi0b1u9ncHhSIVVyufrhilmTlBThGdU4ldD-uuv4DTkk0jtsj2aL2GeXltytqQfMWjYk_gUD0-IGugg7LyDLJAd3g9rqh6lMdsIlJ6G2jLTZm8Z9tqhTAGikz2-1_1Ydy_DEmSxJmUKvnEfca0gXnZeqqMLQo0TM1KgPQ0AkitMC962VUjuR3ZAgYdI5HlzKIawocjomozpdPUOFSrWrx-daCP8dw8PdWAHBuAE2uwHSFJJc5FhhjeG3GQJ62UcSJYFcgj0em9BKn8QMvKcHFWBSoj_GmsLegBWtZZTYNtEMnSKrHVRQcTzUPNpaWbaaxA19gGt-5oVjcjzmwSUUibXQxPLAFIsRlXe5QkGZsyrpWhSQdNlguPHM_Zx7oxEXbNsvuwdUmOIfRVKOI_qgTEz2X4dXHT3BujXkKDRJb1_Kyins8zG2ZgWvN26nWEYOqHmGD94soVO_ZawBu-bV6LecuF6pCyweNGOwlxNP2V4TpIh4qjuppeg-ob7dYJN7FLhrE2aX6wKWBrKBgYE-E3yJlmO_YOfZQpXnsXMr9HQbe8ek4Mdll1baRFZp_lyoztbjzMRXuat6llA59PfpA6s0kCst5-1o4KsdjkG7_daIJkWpJOUkPSMPFvbqKaNbo3ol-hDo67eXK8lPyZIic1PBzE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e4715e7b.mp4?token=OMC0rrj96tPo4pkdsi0b1u9ncHhSIVVyufrhilmTlBThGdU4ldD-uuv4DTkk0jtsj2aL2GeXltytqQfMWjYk_gUD0-IGugg7LyDLJAd3g9rqh6lMdsIlJ6G2jLTZm8Z9tqhTAGikz2-1_1Ydy_DEmSxJmUKvnEfca0gXnZeqqMLQo0TM1KgPQ0AkitMC962VUjuR3ZAgYdI5HlzKIawocjomozpdPUOFSrWrx-daCP8dw8PdWAHBuAE2uwHSFJJc5FhhjeG3GQJ62UcSJYFcgj0em9BKn8QMvKcHFWBSoj_GmsLegBWtZZTYNtEMnSKrHVRQcTzUPNpaWbaaxA19gGt-5oVjcjzmwSUUibXQxPLAFIsRlXe5QkGZsyrpWhSQdNlguPHM_Zx7oxEXbNsvuwdUmOIfRVKOI_qgTEz2X4dXHT3BujXkKDRJb1_Kyins8zG2ZgWvN26nWEYOqHmGD94soVO_ZawBu-bV6LecuF6pCyweNGOwlxNP2V4TpIh4qjuppeg-ob7dYJN7FLhrE2aX6wKWBrKBgYE-E3yJlmO_YOfZQpXnsXMr9HQbe8ek4Mdll1baRFZp_lyoztbjzMRXuat6llA59PfpA6s0kCst5-1o4KsdjkG7_daIJkWpJOUkPSMPFvbqKaNbo3ol-hDo67eXK8lPyZIic1PBzE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/677893" target="_blank">📅 00:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d77fe50a.mp4?token=S_SS2Zy-RHbNO63OHAaunHqpRWNYzDVfU2sDatWCnxmIEhRdoMSYeUtQaKxCGGVvvts4Jm7ARTHC1SFTpcnU6tzok8gzN5B0heL-Wi9KrH6GHeWDjxx7Isd3YoC4kH7KXNVSnsGipkIrMonAXtjyI6db4gJuNW0KfdaYTlbylJIqlCLCq-bWYJoBPtF-8_RQZpSOWFAKjx6E15-Bc7S_Oz9D620WajkImRWMP0U5hmnosm9h-3yrsEyX2zuEvc9xAl03y9bK4SDyokVRcxZtm7HZ-3yEUbgRekdvGCfEztNMDy2MuCQmPlOskS150SpfhqSAfQ4U8H67FS6aXPD1xBsZ0wo1K-ScbXL_rkh78qU2npamRc5sUcwlEW8Nwdvn02fRGRSM2KOOQ9kahpavvrrT6bUpdHCihD8UwYdbqRj1ATk1jPi9IrR0aDo94klZbGmlMlbUPYSXub-_NxZvhks_wlUR2gwfysa6l9YqKGZFFCO_ps2eX583m7RXpZybb3TlyylT5HMeHTQ-cvKsv7kFI-qQdnWpBkQHonEBDiX5Gfxn2BMAz2DreAFANKSdx6dqX1Hc-_u43rvsYUToHSrBA1MPDTZW7GjUO-IvU9OET-o6cncxECbQduJFfdvApUIAR0rRL4I927GaDMuQ8JnJtk17w9Yo_qHue-WlYc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d77fe50a.mp4?token=S_SS2Zy-RHbNO63OHAaunHqpRWNYzDVfU2sDatWCnxmIEhRdoMSYeUtQaKxCGGVvvts4Jm7ARTHC1SFTpcnU6tzok8gzN5B0heL-Wi9KrH6GHeWDjxx7Isd3YoC4kH7KXNVSnsGipkIrMonAXtjyI6db4gJuNW0KfdaYTlbylJIqlCLCq-bWYJoBPtF-8_RQZpSOWFAKjx6E15-Bc7S_Oz9D620WajkImRWMP0U5hmnosm9h-3yrsEyX2zuEvc9xAl03y9bK4SDyokVRcxZtm7HZ-3yEUbgRekdvGCfEztNMDy2MuCQmPlOskS150SpfhqSAfQ4U8H67FS6aXPD1xBsZ0wo1K-ScbXL_rkh78qU2npamRc5sUcwlEW8Nwdvn02fRGRSM2KOOQ9kahpavvrrT6bUpdHCihD8UwYdbqRj1ATk1jPi9IrR0aDo94klZbGmlMlbUPYSXub-_NxZvhks_wlUR2gwfysa6l9YqKGZFFCO_ps2eX583m7RXpZybb3TlyylT5HMeHTQ-cvKsv7kFI-qQdnWpBkQHonEBDiX5Gfxn2BMAz2DreAFANKSdx6dqX1Hc-_u43rvsYUToHSrBA1MPDTZW7GjUO-IvU9OET-o6cncxECbQduJFfdvApUIAR0rRL4I927GaDMuQ8JnJtk17w9Yo_qHue-WlYc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیبی معجزه آسا که استفاده کردنش بشدت توصیه می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/677892" target="_blank">📅 00:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: ایران در آتش‌بس برنامه جدیدی را برای جنگ طرح‌ریزی کرد
ادعای نیویورک‌تایمز:
🔹
در طول یک آتش‌بس زودگذر، ایرانی‌ها مخفیانه طرحی را برای افزایش هزینه‌های جنگ برای ترامپ در صورت حمله مجدد نیروهای آمریکایی طراحی کردند.
🔹
در طول آتش‌بس کوتاه‌مدت، ژنرال‌های ایرانی مخفیانه با فرماندهان شبه‌نظامیان نیابتی در مورد چگونگی گسترش جنگ و افزایش هزینه‌های آن برای واشنگتن، استراتژی تدوین کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/677891" target="_blank">📅 00:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دومین تماس عراقچی با عاصم منیر و وزیر خارجه سعودی در ۲۴ ساعت اخیر
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران، در ادامه رایزنی های مستمر و طی دومین تماس تلفنی در بیست‌وچهار ساعت گذشته با فیصل بن فرحان وزیر امور خارجه عربستان سعودی و عاصم منیر فرمانده ارتش پاکستان، آخرین روند تلاش‌ها و ابتکارات دیپلماتیک با هدف حفظ و تقویت امنیت و ثبات در منطقه غرب آسیا را مورد بررسی و تبادل نظر قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/677890" target="_blank">📅 00:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677888">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdNg6iV6RYNp_Wft1Zq3i9f7A2EJsc9epkO8ot6emM8IQuL_Dbs_Cjz1bFxcGeAztHg1zqxcrEYT2S_Gju6SQBeloPBFf34O_PYi5dNUQStm3Q_Zf1wY3xvkralGLz9xPHOQrxyYRHWUfhER6-wCAGdKyvSH1_X4aCZAONbtRX6WB5GQmuGjhxiADqxIToIy1k3qHHqLT22UYdKIP3PyAOTA7sZgHhALWV9a22rD1RKEYvBElbBjXPnFtcnX6-p5TcfnSOAccXJ1xWKAfBzQ2QFrjYfQJ-xtwgzCgYss6lFlPokXqs-dNsiZKmrQ5Cno6IFIYi75uM9aeUP3ls84aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/677888" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677887">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azm1wUeCPxJdbUJROE_wUitOAbzhnhCB1No6wZK7pEvt7lnwaDpw8veDHHKK6cQhM_hSPSuYLZy9sXuxQ1nnZh2cqZzYXOa7t-OQJ31BMAQ-nl_xTJ5nxMhsj-ZjHzB28LXWFqz6gg057wvLR34HduooHWtANzjw83tM70kzzk1cZH5gB6RzYZqaJ2b0T9kXIplE76Ql-LQj7wm0XF82Ub0jHFxD5DC03UfKqRKeD0qhwuTX9fG8aRGJCYZlEA7W7Jjn0gtcSvQChoyUwpT5BJQEIKmcsexMPyuW7iwiWuA186M6XapWmA-8dnYyLK_OtvuMgH6gC4SPU9E8yzN80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت لاف
🔹
دونالد ترامپ برای هفتمین بار از مواضع پیشین خود درباره حمله گسترده به ایران عقب‌نشینی کرد؛ موضوعی که برخی رسانه‌های غربی آن را به نمایش توان بازدارندگی و آمادگی نظامی ایران نسبت داده‌اند. همزمان، شماری از تحلیلگران معتقدند تکرار این عقب‌نشینی‌ها می‌تواند بخشی از یک تاکتیک رسانه‌ای برای کاهش حساسیت افکار عمومی و بازارهای مالی نسبت به احتمال وقوع درگیری باشد؛ به‌گونه‌ای که در صورت هرگونه اقدام نظامی، شوک کمتری به بازار نفت و بورس آمریکا وارد شود. در همین حال، نیروهای مسلح ایران بر حفظ آمادگی کامل تأکید و اعلام کرده‌اند به هرگونه اقدام علیه تمامیت ارضی کشور، پاسخی قاطع خواهند داد.
🔹
هشتصدوبیست‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/677887" target="_blank">📅 23:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677886">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJGlt212PEeYfIgQ7UywVtwOnEktBu3vHpuSTBnb3ODB0qtpjD3mZb0QMJ9p0GDq0QBBC4frpd2eMBXj6Uq4lTVKBGJyeHWbP6HFJf7Wtn5d13VElyycvJ86_NhfwtjJ3zezlN41UIlMhOR_4KvBVLWwTd-YN2lobA1ODn5FEmp74Wp-TY5c28qbhBrbcjPwvVPgxkNOCB93UDIf-feoHT09pmNqrf9NIql7Zb29TKOpXGcxzieASmEoDgI7bWFA_5rir8Jmh0MJ2OmQmGahARd5IInrlPkAbQSqR-ALHdtYjDfa2lt10eRUYdcoYvaS-XYbJ-IoFJnGoCb6HLf6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سال‌هاست عراقی‌ها پای کار میزبانی زائران حسینی‌اند؛ این روزها ما هم می‌توانیم با قدم‌های کوچک، همراهشان باشیم
#میزبان_باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677886" target="_blank">📅 23:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677885">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufax_izp7Tz3hlEoTM_ClckZ7Jk4Zud7QS7zaEtik324w8S8w7mefkAtCvNWuDkGcHIQaJ8pLqu3oc89QRq2g0OIAoxAJix7_6PywYv56qTcwPjQo95iA2kql51v7Xsp5FCWYiIvmREuIIhuZyRv5iUjGlWi0JX7n0EKLrjpsIWAX5ZuiKMDaYuLzbyTMpfSPW2o4SxA08UvJsh4VIIK3A5LGC-qVw_s0-Bt_0DjaW033jVrt2v4Z6p2ZU6kkoe8hS_1uEedZ3W6BWP67qgoXN9_GU7lZJx7tIJ3N5GS4eXb9Y4DjyK1unj_BDwhSDvipzrqu1RHxNxTMUbx6LdY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گفته برخی منابع خبری؛ پرواز ۵ هواپیمای سوخت رسان بر فراز خاورمیانه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/677885" target="_blank">📅 23:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677884">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQbaefl8ZLY-HdnZKQQLuJFkVO6pyVEBa6u_i39PmyE8f1B1Ol3Bk6No8emYMiAyEzKivmIlVsGRmHNDbrKOoircQJIADjomHmzqdifPZrehu2kSqxpoJT8FlhF-k3uXM_H43njLvV8s68k2hoeQc0tmfUzqYrnY3tDOMjc-qSq3uk-L9SXxqdXDsySuFnkkqDNrEXHW1zTRH1epwPQScuaIyRQbpIxREs6mhIXQaZ1sSDVtBZD24uxtZsTGRJq0Zpum22so6-1NIUP9bEzxzcmCB8rpxskfYmqIi0ZJSobMRlrTmiKZeX7dQ4K-XWpWbbGexKKLNyuP_XhJmOiLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عباس جمشیدی‌فر با انتشار استوری برای وطن:
من غیر این رویا کیو دارم
دیوار امنش عین آغوشه
یه قطعه مروارید مادرزاد
قلب منه! اسم وطن روشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677884" target="_blank">📅 23:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677875">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQo95sgeVCh-6LV8GWDKoHjVf0HLLZl161kC5nVRdxzIvK44H03jFPx60WZNk-4nkAcUC9r2Gn2RC4fn6fwJ_JijmTO-n6JWiHXPckYMsruLBaoqg08lEjRosi2qBU0fLh6jSvf_FU7RR7MFPJJ80fMbwhb-k5-pFlHKgcbtV2xO7cRUsDBFwxsDU_nXDybP9rGslLBMzzrjmJ6iXgqN-2PlxN_p3vFp1zHxts878o9k7HlJQ6snn9l8jG7zweEMfXPrqpP8JY2MJoJz05hjhRGtnHF_xYqaeQ9ws3Qb5UXXz5PUGZiw9701qZef9jMM5Qwztxbq3YwfntWfh4L-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE3E-wZjmcNTlAaMpCh-QjAyEFHo77Qisz1rX7ABaeshcNHNQmMF-o6oWkLfA4zpq68Uln5plBInkRAUQZRq1CeUCE0Qp_f9_Eocg7yjc9pD2TrR6zM-8lWJ8W2Tivda2iDKxF8ed-NPtS_XkZ-eR5qHvjr-wTMk46djZBwomRGXICdFiwR8AoaDmHo7WAhFnJAM-PjnvHXM9MjL3tz0u-Y7_IgO1ohFr18NaqIFAWSPWLByBzgaJe_WY2YlT37Fuzk-zysTidLqbaiDMW1WfuW3nGYJrMdA8L5Ovu3zJ7tNxMxdNBIKVx3oqSR6HMGb1iU9UJhk8GQgFqGJUNN8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPoYgpCZeTovBfi7qNZVaF0Hl2dshLrnE0OixL9m1Q9Qr1oHDZ9xclcsyH8j5J1HQSHX9MnbTXo6oWO5CsMalIGxxwtYHlBNvYhKwEpT06vQlWI8e39HEm0bKjn44bR8P01DSPrfhKvtpjBq4tgBkLm0hhFX2TGGqAAHCWzoOKuAZdTVFbLDpeYpn8OXvM08yxrn_3VEaheLb7muk-Q3ZZoYq9KRszWx-dMwaBoppMfH-VixNXdH7R5DG8-jcam_4bKeVmv8I9_jEwIKrlMgYjhyGJ0Zf0UnfBS8jKXwXgFIH-NCAeArNburJug3tdPF73clat1NHnVWfy9WCcCZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGg22cX5P93vTsIcuSL2KsC7duSPN6888PdxNI-FlDC6YbGmCa0ccEi0k2G6ZU--sFNUwegZIhcV3wHDodEQ0je4bgatrjRvFjXE239nPdrkXMDWKa03CaKOhbH7C3m4Y57jzboJ_fdenrgQf3wPWouhszYbDub2StIuO2U4mxfZPzybb2bJxWrW8FMiC4GpH3NxWTqrSnHWfelDce9w_8Cn4RuKd4pLtCSzniEz5Awu3FXJe79iman1FWJ8T0Morixjj7gnnx-UNuXueLyqAn4brKEJ4LPrCazfA3pLgfGOGUrI63ZCVKRW0BtrHbZfcxBckFawtM-KwTkFBHYTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAVzIuJg-3uJk-RC8HE3opC-IQsPBSshNinRqnQGJr-qKboqM2_D3zHPtidZlMFdPBKUREWDD8Hr4xdxV8yQwF8q5IR2zmDVICfBPbo_2voQ6vgtJm-za8xpwTob1X6ov1bem3oaiQkL_EyNhWSabDkzYtatJ_D4QoTgqOYv0p8acqFn_RnjBSiLJOLiGn0HPNG5CB5aZ7fWEAxoO6Pm8f-WEXECRynRIsMabjI7Yauhkc3phYZ8E-6IGKh1kVKyVSIvGD5DM3eJg02NbsMW9oCCHPAZgRnqw9X0ACu9WRjNy5X3buBXgojN-nxN9EM4S832TBq-S7GWDKzliNwTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knlMLIORSpSPC_Sm-uvmoAaCmqPSlK1qmpEwQbZF29IJKrgUwXKd0sweTYnUgakBB1y5DuoO0y89UBJdNgjAdTpk-bTuSWNBr3vpFaV1H0A7h-y0LUY2q0vSrYvzEV1fKE5X4hDt3iSaVluhpVZisdJcO90cQaamYuU0Dj8n2rsA5Qs_fDvj38OrUTqYtArYuSkpZeKMHqJwOKuMUmZp_sGg7KjjgKlyf7ZCCrlvMqzMcq0LjeH37zohIvfPf5MF__0d2qFzO3PMfKvjzTz6ics1o-QCJ_0a2B-VKyENjIaz68JO6k909fjo-JGuZavQ16dRWmsfAfkzpFllgnDfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwCXRESaMmFsmnXuVMnSS0KYwoY5unFGj2S-gYF2HAyOMMR9CALv9xc4YFYYfvtoU7jmgdQLPuU-sYCoidf5RdsYbCFi1QoBXQ5gCpVl6FLdhuXalqK6i69XZzJPumaPB1hJswfsH_KOwY3zpj7jGvIhwumgz5rLMGm77ODyrXCPKF5yAoBcfOMzSKjJiMRbGzDf2ssq_kPzIpQ4rw55NMReawoSMpi265MN4fQVEYTgAi3fVG4iZ0CSBLvqC_EnbmNnIa_pp2Oo4oI0QYS_4aAY0URURDvTQQK62PK5NWIY-qe-0aGlnriKd-umSwQU8amlE-5l8apNnwD7DB_cdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUpdb2OACW2c3OoRjTt7VlTZgP421Jlj2_gI5zXCvAA721Op8MmWrg9uI4kQewsqzH9LueA1hR8D7V--qDK2Y9cHQOc1u4IqDF9ELx0ub0fUs3JrczCt10GlLsm1HkKxoGG7hjPhcOm28q68GAAWHUaK8kF81FweZvdHHzS9q6I_aeHdVFFxvY4vV3rVbwgdhr_3O8bXP5ivqTcBmCCYr1Fl-GlBVJLc3jBTOM2NqJ9S4qoo078SJD1h1MaTzzTC40dQyddhmuogOlGHE_pVguBfh2sDe-jCiRtV5IN7tMx-pGPwZn6TsocH9AA41JY_Nz8zlcSp2jZ37-V29CkXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S77P92FtOrafSdZoXlFnqrluA4twjkox4JUJxohKmbX5U9jLrDQ6jOOio5I9Uey1Q0wFgTJ0JY1C62KLbXA4JreFhBNuDEFQRx6ge43nNUYi0cnk9v3fbLj9kWRcwsAouioPs9SDivoCGOF7ZiodVx_1zBLXpzpRz66dovU9vUR7jSSfeqUyRy-xPJc4KEWu_nLD8pGTV3smgOsd6uMlQ6bvLKIz2ptJdb-Hf7Cnu5ygIcSOJDLRp9vdQfm9hVIUQH8i8jhkGwtVMl-cGOqS8h44UoKENApK_fMXnRMqwFDJIjCbjAkS2jxEUZZ6rnXlzD6GYGgf8IZcE26CJHC-4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دستگیری
💫
✨
از مکتب امام حسین علیه‌السلام آموخته‌ایم که دستگیری از مردم، یکی از زیباترین جلوه‌های ارادت به اهل‌بیت علیهم‌السلام است.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، در کنار خانواده‌های ایرانی ایستاده است.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/677875" target="_blank">📅 23:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677874">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4069a62fd9.mp4?token=vLCpu4BtwfsPY8i0OYIy5K65mP74L3PD-tTLfo9Q6SxZAPCyLjiShuAaZ6T7OWDVDGGJu68z83Zgj_k1TbLFxMDTCgMzMj0CHpDFDHcY6rQPXi46uBVCOzuAPIov1tMnZulc1GE9ML0ktbDO60YXxG3rfGQNdH_IcWpSx9dfz6OKS7shfVuwpiNLyje5bIr8Q8eUMaUxa_yCQzmV0QKxdwrP6c03gpqbSiAMvHlPEez7BIfi85mX-1T41ViAqtSkWA5ddPBi-qSg_I1JLXP0jUWLh5pCXQjRc1l6p3bcwNxSSNV3yH_hkoYMUhf83ZTZQ1s9RCo-2P7hwgGWUPiLF2oY_ATrizSN8RJeky_KyikBeZ8cYimEHb2YXH1vQVGJNEKTDxlEhr2NvCuc8k2f24tCUUbahpziwZImHNLQKPypWKkpks_Ku3Tzw3qJh4ea0x9iwnB4ScTEA5mqHtjLJTmoL5ByFDGfq0XvJ7v9cv3EuLyFNhNf7qwW-Nh8Sb4CiRBNZTasMuKf6xyoYB-7Z2_Eu2rzsroWZ9Cd1D-ZtjjmimReQCm4N0qf2_q-VEBUcCh8O8GHLcPA4dsV-rGj29HdAf8uCt2Ks0E9_NjwkrSkZtX6VlpRgaWewEZVIzuw1tcsjnMzBhjGMRIMjzevf4RkDEYy3abUnkRnzON-vmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4069a62fd9.mp4?token=vLCpu4BtwfsPY8i0OYIy5K65mP74L3PD-tTLfo9Q6SxZAPCyLjiShuAaZ6T7OWDVDGGJu68z83Zgj_k1TbLFxMDTCgMzMj0CHpDFDHcY6rQPXi46uBVCOzuAPIov1tMnZulc1GE9ML0ktbDO60YXxG3rfGQNdH_IcWpSx9dfz6OKS7shfVuwpiNLyje5bIr8Q8eUMaUxa_yCQzmV0QKxdwrP6c03gpqbSiAMvHlPEez7BIfi85mX-1T41ViAqtSkWA5ddPBi-qSg_I1JLXP0jUWLh5pCXQjRc1l6p3bcwNxSSNV3yH_hkoYMUhf83ZTZQ1s9RCo-2P7hwgGWUPiLF2oY_ATrizSN8RJeky_KyikBeZ8cYimEHb2YXH1vQVGJNEKTDxlEhr2NvCuc8k2f24tCUUbahpziwZImHNLQKPypWKkpks_Ku3Tzw3qJh4ea0x9iwnB4ScTEA5mqHtjLJTmoL5ByFDGfq0XvJ7v9cv3EuLyFNhNf7qwW-Nh8Sb4CiRBNZTasMuKf6xyoYB-7Z2_Eu2rzsroWZ9Cd1D-ZtjjmimReQCm4N0qf2_q-VEBUcCh8O8GHLcPA4dsV-rGj29HdAf8uCt2Ks0E9_NjwkrSkZtX6VlpRgaWewEZVIzuw1tcsjnMzBhjGMRIMjzevf4RkDEYy3abUnkRnzON-vmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌های ترومازده از عشق فرار می‌کنند؛ درست از همان چیزی که نجاتشان می‌دهد
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/677874" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677873">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwlbCAt91kvYZ_h1U0AQTLwW4TRANwU7fQjo3-AndfxsRziAys8-M6eCaQs9yKfTCLm35K1mPv-y2aGfZAEl1rLsahys1o92ha-L6mGBV48VpL5SeF_PAagV4OvY7Aut7-pP_zfS1gboujWcJE90msYlSheVSQqfrojLuJnPzsieKMGnyBWPRkSh63gxu4UDKWV97UBtxE1FYuuhbyT3_4zTB07t3TeKcDMd9W9o7XkuO9ePBQXEpODVgafpllKAKeE4yv2lt32zbS58I1KeIAub0fIXwhnP6psKA68CSmtXhh8Q2_olU2q4IW0SfYtw1PYICmfkH8QF47sBhRohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«پرنسس تاریکی»؛ زن مرموزی که صندوق مالی ترامپ را پُر می‌کند | مردیث اورورک، شَرخر کاخ سفید کیست؟
🔹
در دنیای پرهیاهوی سیاست آمریکا، جایی که دونالد ترامپ با سخنرانی‌های آتشین و حضورهای رسانه‌ای، تمام توجه‌ها را به خود جلب می‌کند، قدرت واقعی گاهی در سکوت و در اتاق‌های دربسته جریان دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3234989</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/677873" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون بودجه: ۱۰ تا ۱۲ میلیارد دلار از پول ملت دزدیده شده ‌است
عباس قدرتی، عضو کمیسیون برنامه و بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
نمی‌شود در شرایط تحریمی مردم در سختی باشند و تراستی‌ها با پول ملت ستم‌دیده ایران در خارج در ویلاهای خودشان تفریح کنند. براساس شنیده‌های من حدود ۱۰ تا ۱۲ میلیارد دلار از پول ملت ایران دزدیده شده‌است، ولی هنوز آمارها قطعی نیست.
🔹
از طریق پلیس اینترپل پیگیر استرداد مجرمان هستیم و نمی‌گذاریم پول ملت ایران صرف خوش‌گذرانی تراستی‌ها در اروپا شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/677872" target="_blank">📅 23:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677871">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/576e15e56f.mp4?token=IEkU7J3i_Cu-fxAPQkakZOzI1E66qeVSqRHlcCdiC3JCqRDByNF_9HGZQDHgPfsF7xaabUEvj9VAvKqW4Y_7gVqWWVKRKUPCva6dJFXIExJgxhEEEb-WBvksdCwuPIbLNHXi3bkUtlkF8FJNFwWjLMkTG1JVYk4Zw6MbsJHfTCOhH_rz5cTKK2IvDCXNEGXaXkBPbL4pThB5ae088nX8Pwpcjwd-CAs7fJPi2WqVlIrw4YVz6TaGKat-WvT1ylqWKd46f0rKLjUcBBVwSAqE1eDhruLOyWKXQZNNJelTAk93DaqnYP8intN1QtQku-3RvVCPoRRUT7q4lIGZLreT76BKueB2gu_XtiGAqFsyHq1zzCa4NNxeRK0cEd_e7YJnoD8KXdzsXof7mfrb0RSjzLIDKJkln1L5_QfiyWodh_sgGyg8p8foIumM6eAo1YldJ1ZfdvqBJ3Qe3ROPiWakaZqCa5ke3E1LA3eoy2G0cfQPCUppngPGSH6bzMUBiCcx4hKhCbRQpVB6XVQbMbFpdXPPCklNhtbo4khh3QieRLf4CGTi5ZxZngmQFomeTBBgmhNmmYRcMp0pjIEj94mRxVHcosVq8-drO4IRJ_Y5ShE1dRlhBtyJ6pOqaRLJH3toN55qS_vtZsjz8ndm_KkpPShgmShdTrwsaPAetSKPTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/576e15e56f.mp4?token=IEkU7J3i_Cu-fxAPQkakZOzI1E66qeVSqRHlcCdiC3JCqRDByNF_9HGZQDHgPfsF7xaabUEvj9VAvKqW4Y_7gVqWWVKRKUPCva6dJFXIExJgxhEEEb-WBvksdCwuPIbLNHXi3bkUtlkF8FJNFwWjLMkTG1JVYk4Zw6MbsJHfTCOhH_rz5cTKK2IvDCXNEGXaXkBPbL4pThB5ae088nX8Pwpcjwd-CAs7fJPi2WqVlIrw4YVz6TaGKat-WvT1ylqWKd46f0rKLjUcBBVwSAqE1eDhruLOyWKXQZNNJelTAk93DaqnYP8intN1QtQku-3RvVCPoRRUT7q4lIGZLreT76BKueB2gu_XtiGAqFsyHq1zzCa4NNxeRK0cEd_e7YJnoD8KXdzsXof7mfrb0RSjzLIDKJkln1L5_QfiyWodh_sgGyg8p8foIumM6eAo1YldJ1ZfdvqBJ3Qe3ROPiWakaZqCa5ke3E1LA3eoy2G0cfQPCUppngPGSH6bzMUBiCcx4hKhCbRQpVB6XVQbMbFpdXPPCklNhtbo4khh3QieRLf4CGTi5ZxZngmQFomeTBBgmhNmmYRcMp0pjIEj94mRxVHcosVq8-drO4IRJ_Y5ShE1dRlhBtyJ6pOqaRLJH3toN55qS_vtZsjz8ndm_KkpPShgmShdTrwsaPAetSKPTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابداع جالب یک کودک ایرانی برای این روزهای گرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/677871" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677870">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
چین، موتور رشد قیمت طلا را روشن کرد
🔹
طلای جهانی پس از چهار ماه افت متوالی، سرانجام در ماه جولای با رشد ۱.۳ درصدی به روند نزولی خود پایان داد. تحلیلگران، افزایش خرید در قیمت‌های پایین به‌ ویژه از سوی بانک مرکزی چین و کاهش انتظارات از افزایش شدید نرخ بهره آمریکا را دو عامل اصلی این بازگشت می‌دانند. همزمان، نقره با افت حدود یک درصدی همچنان تحت فشار نوسانات بازار باقی ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/677870" target="_blank">📅 23:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677869">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کشتی روسیه توقیف شد
🔹
نیروی دریایی بریتانیا اعلام کرد ساعاتی پیش یک کشتی روسیه‌ای را در آب‌های نزدیک پانتلریا (جزیره‌ای میان تونس و سیسیل) توقیف کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/677869" target="_blank">📅 23:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677868">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2380fa4bfd.mp4?token=u_r3isJ1vOyLPHseaNmYA1PoTa-_NhaHU3vbLhNz1f8WL73mLAoYA9dKkkE1rUWs_xXzgEahYbFteJpBX5EQNe-i7BGBj1DWZL2pIWiHv2-I8RBcUI1OaqOnwUV4WPt7wMDezgJ2JcBKjx9dBa-_CpqWam21ZSurc-u3OKx21tvhUXWSEBFghrYVve3QxJcDGukfpGL5v2MDT_r4JBPUNGMPeBgjt4sy9o_vMXyLgXqb9yalMOcj6F_6yeQKk5qEUy2AAKhPJlMeGEnERGV7EFX2HKLZ_f_Jy1zRz7Kpll2nCWy0-oy5xsnrenxefIGJfIpmHefnxAUyHyzvp3NEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2380fa4bfd.mp4?token=u_r3isJ1vOyLPHseaNmYA1PoTa-_NhaHU3vbLhNz1f8WL73mLAoYA9dKkkE1rUWs_xXzgEahYbFteJpBX5EQNe-i7BGBj1DWZL2pIWiHv2-I8RBcUI1OaqOnwUV4WPt7wMDezgJ2JcBKjx9dBa-_CpqWam21ZSurc-u3OKx21tvhUXWSEBFghrYVve3QxJcDGukfpGL5v2MDT_r4JBPUNGMPeBgjt4sy9o_vMXyLgXqb9yalMOcj6F_6yeQKk5qEUy2AAKhPJlMeGEnERGV7EFX2HKLZ_f_Jy1zRz7Kpll2nCWy0-oy5xsnrenxefIGJfIpmHefnxAUyHyzvp3NEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موسوی، کارشناس مسائل سیاسی: اگر احساس تهدید کردیم و اگر احساس کردیم که دشمن قصد حمله قریب‌الوقوع را دارد، حتما باید از حقوق منشور ملل متحد بعنوان عمل پیش‌دستانه و یا دفاع پیشگیرانه استفاده کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677868" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677867">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
توقف 2 هفته‌ای حملات و خوشبینی نسبت به شروع مذاکرات ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3235009
🔹
شاه انگلیس دامن پوشید و بین مردم قدم زد | عکس
👇
khabarfoori.com/fa/tiny/news-3235041
🔹
توضیحات خبرنگاری که ویدئوی جنجالی دست دادن عادل فردوسی پور و وزیر ارشاد را منتشر کرد، درباره واقعیت ماجرا
👇
khabarfoori.com/fa/tiny/news-3234848
🔹
جنجال پیامک پدرشوهر ۱۵ دقیقه پیش از عقد برای عروس
👇
khabarfoori.com/fa/tiny/news-3234767
🔹
چرا از رهبر سوم انقلاب هیچ صدایی منتشر نمی‌شود؟
👇
khabarfoori.com/fa/tiny/news-3234931
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/677867" target="_blank">📅 23:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تصاویر هولناک از پاکستان
🔹
حمله انتحاری در شمال این کشور دست‌کم ۷ کشته برجا گذاشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677866" target="_blank">📅 23:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763e412b91.mp4?token=Weo0UklZmhr8D0XY4R1_AfPSZZPBhbAvUojfg-K2BxevzO37qyGsw0YMqwCfAZfeOKIRk9WZvQ6Y5kObEEjaABSVudTTFC4BY8wT7a1Rfk24VLu_XELpeP5v7wFEWJOcBl4fwQBFycWo9-DAvoQxaJzjgd4tpr9CDZUmqL7wXUuhbm1rD0vMG0aiRjmqWvBYOg7gU6_fvudCDPHDVic_DwEZ1J5D43RiK2LeWCZKaQ28aMzgVAE5K823nKxlAW7kxofqpIGNef6Br-Wt3POuVv2CYEyahqN8_g6L_EilQzJzaOYkXYZIzylAjRV_xI_4Gr7VuiFjmUkVB3p9GXSahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763e412b91.mp4?token=Weo0UklZmhr8D0XY4R1_AfPSZZPBhbAvUojfg-K2BxevzO37qyGsw0YMqwCfAZfeOKIRk9WZvQ6Y5kObEEjaABSVudTTFC4BY8wT7a1Rfk24VLu_XELpeP5v7wFEWJOcBl4fwQBFycWo9-DAvoQxaJzjgd4tpr9CDZUmqL7wXUuhbm1rD0vMG0aiRjmqWvBYOg7gU6_fvudCDPHDVic_DwEZ1J5D43RiK2LeWCZKaQ28aMzgVAE5K823nKxlAW7kxofqpIGNef6Br-Wt3POuVv2CYEyahqN8_g6L_EilQzJzaOYkXYZIzylAjRV_xI_4Gr7VuiFjmUkVB3p9GXSahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ماجرای خانم فرانسوی که در مسیر زائران اربعین دفن شد
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677865" target="_blank">📅 23:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677864">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7adbcc0a55.mp4?token=AqmXUiMaJA1kWoNfvjw4ZmXqm4AXK7twBPgRYoSoRHPmslPG3Y58fbg02o-yTN8d_kbuEIlrfq3RLWoq62Jip1O2osh8MaY7L_LJeE2EAkThrFtDfngG7hUUO8ykfCdTaSQzqD18FU0bl7bt94dL6KonOJnwdtlxUhtlR_d1vFsORrcBf2gb4FkhBdAk4gBLdFPe-2EV4QWoNTWyiyniRGpGNsCLLNbHBQHsCZ1T5EPmYYYcW3MuHRa4fTLWoJo7zhS8-keMdDxENTvORoQNwhu-V9wkDFsSWGBboZ_REMZEvG2YP0LpOullQChWCnWwdMc-7DSFp3YpSDFPlj1g_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7adbcc0a55.mp4?token=AqmXUiMaJA1kWoNfvjw4ZmXqm4AXK7twBPgRYoSoRHPmslPG3Y58fbg02o-yTN8d_kbuEIlrfq3RLWoq62Jip1O2osh8MaY7L_LJeE2EAkThrFtDfngG7hUUO8ykfCdTaSQzqD18FU0bl7bt94dL6KonOJnwdtlxUhtlR_d1vFsORrcBf2gb4FkhBdAk4gBLdFPe-2EV4QWoNTWyiyniRGpGNsCLLNbHBQHsCZ1T5EPmYYYcW3MuHRa4fTLWoJo7zhS8-keMdDxENTvORoQNwhu-V9wkDFsSWGBboZ_REMZEvG2YP0LpOullQChWCnWwdMc-7DSFp3YpSDFPlj1g_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواب عجیب سربازان آمریکایی به سوالی که پرسیده میشه ازشون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677864" target="_blank">📅 22:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a716599120.mp4?token=usYSXNy90fVwJ-Lty-lzwHvzy2MIYjOBQffCW9nGIKJz7siVUQnAjDts8wjwUcezHc5rgb0ot1VsLS_aVRBKuZo5SJAIiHFgKZMGJmL_ictCO95Nzbck6Nj6v0iORW_wA-M9R1eHFMHEW_SEA2_EZvp1R9PtQmzSfjSDuKNsGNCcz1Xbh8-nmfIWMrPmHeNvTxyNB78uuqu7JlBnUoQiJlMLdHSfA9uK5Iz521NSK4jq7Ek3AcP7GcbLC4OPPhydKJlV_GSKV-pb2MtdVHaY5udutWMuIS2hIWEHHvEP1pbpbD3vfpHDCMy2oXMuxYGVSZlKEgJl-dRhs4Kxd6S-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a716599120.mp4?token=usYSXNy90fVwJ-Lty-lzwHvzy2MIYjOBQffCW9nGIKJz7siVUQnAjDts8wjwUcezHc5rgb0ot1VsLS_aVRBKuZo5SJAIiHFgKZMGJmL_ictCO95Nzbck6Nj6v0iORW_wA-M9R1eHFMHEW_SEA2_EZvp1R9PtQmzSfjSDuKNsGNCcz1Xbh8-nmfIWMrPmHeNvTxyNB78uuqu7JlBnUoQiJlMLdHSfA9uK5Iz521NSK4jq7Ek3AcP7GcbLC4OPPhydKJlV_GSKV-pb2MtdVHaY5udutWMuIS2hIWEHHvEP1pbpbD3vfpHDCMy2oXMuxYGVSZlKEgJl-dRhs4Kxd6S-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ به ازدواج زد؟!
🔹
فکر می‌کنید در ایام جنگ ۱۲ روزه و جنگ رمضان چند نفر ازدواج کرده‌اند؟
🔹
این آمار چه تفاوتی به دوره مشابه سال قبل داشته است. در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677863" target="_blank">📅 22:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تصاویر دیدنی از داخل حرم مطهر امام حسین (علیه‌السلام
)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677862" target="_blank">📅 22:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آمارسازی نهاد تروریستی سنتکام علیه ایران
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا (سنتکام) مدعی تغییر مسیر ۳۵ کشتی تجاری در چارچوب طرح موسوم به «محاصره دریایی» شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677861" target="_blank">📅 22:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677860">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smJuBhRvtKS36sNZZJxiVlidpO2FPNm4uZPYASsu7FiR4atAIbiqO5n6nd3e_2_dCNeAPX3gEFx7u00ac3oGv2giPZYWVlWx8PDeGEqiQMKeiw-sKRQJM8zzs-tlkN2K2pAcBg6SVDwZXxn64Ux59LjK97oO9lhn-uIAioYXwJ65XWGgV1b4mGcJAex07dVWRkbr2_JCLV4PcLKYNSHrky5ESOLiQi4kY3-EtdndvXIW7rIzLXP_umIfPMDvQzUvlNQ0I3HUiNOsIozunh0qcl-mpyI8LXdG5xyVq6JNhAs9_6Em10Y50_NXffpis3skOZvZjPG_vFBhgUeLuTYVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پولیتیکو: ترامپ در ایران گیر افتاده است
پولیتیکو:
🔹
ترامپ در قبال ایران با گزینه‌های دشواری روبه‌روست؛ توافق دیپلماتیک احتمالاً مستلزم پذیرش نوعی کنترل ایران بر تنگه هرمز است؛ موضوعی که در واشنگتن با مخالفت روبه‌رو خواهد شد.
🔹
از سوی دیگر، تشدید تنش‌های نظامی می‌تواند قیمت نفت را افزایش دهد، بدون آنکه تضمینی برای عقب‌نشینی یا تغییر راهبرد ایران وجود داشته باشد. ایران نیز پایان خصومت‌ها را منوط به پذیرش کنترل تنگه هرمز می‌داند؛ شرطی که برای کاخ سفید از نظر سیاسی ناخوشایند است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677860" target="_blank">📅 22:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9508a07ef3.mp4?token=jerOwsGaV-K5HG2HS4K3AEDhZ_hCK7h_D7yRRCSff8rcakvTWrrZUWYuPjXrc_pTS_bOaqNxf0YiNGsxxZQ3RnkJuNNDfFesi7tPYKobFAtbDEUMCbA8zbWI15aiRwvUFR-utU6eM6iEd_Xtlsd_iAlFPNbNV7LAScbFjgVvdNZtHnrwFUS3NxA9e46SrwiblEiIe9rhidzdvl_LBiboGkeXc-DtYBLbFyt3tMnozwhe8jrd6N_O6hzr4nja7P15wxyHvH2g1O5pHe9nJXeU-PheYywaugy1lxRVjSdITLKhdOMmxsfICBNVeXiKedXgTbY_QoU4WalpPXDwwWfVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9508a07ef3.mp4?token=jerOwsGaV-K5HG2HS4K3AEDhZ_hCK7h_D7yRRCSff8rcakvTWrrZUWYuPjXrc_pTS_bOaqNxf0YiNGsxxZQ3RnkJuNNDfFesi7tPYKobFAtbDEUMCbA8zbWI15aiRwvUFR-utU6eM6iEd_Xtlsd_iAlFPNbNV7LAScbFjgVvdNZtHnrwFUS3NxA9e46SrwiblEiIe9rhidzdvl_LBiboGkeXc-DtYBLbFyt3tMnozwhe8jrd6N_O6hzr4nja7P15wxyHvH2g1O5pHe9nJXeU-PheYywaugy1lxRVjSdITLKhdOMmxsfICBNVeXiKedXgTbY_QoU4WalpPXDwwWfVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد قهرمان مسابقات گلف در باشگاه خودش شد
🔹
رئیس‌جمهور آمریکا دونالد ترامپ روز یکشنبه با انتشار پیامی در شبکه تروث سوشال اعلام کرد که قهرمان مسابقات باشگاه گلف بدمینستر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/677856" target="_blank">📅 22:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
الجزیره: طرح روبینو برای دور زدن تنگه هرمز فعلا شدنی نیست
الجزیره:
🔹
روبینو، وزیر خارجه آمریکا، از ایده ایجاد یک تغییر ژئوپلیتیکی دائمی برای کاهش وابستگی به تنگه هرمز سخن گفته است. کارشناسان این طرح را یک چشم‌انداز بلندمدت می‌دانند.
🔹
جایگزینی نقش تنگه هرمز، که یکی از مهم‌ترین شاهراه‌های انتقال نفت جهان است، به دهه‌ها زمان و میلیاردها دلار سرمایه‌گذاری نیاز خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677855" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ماجرای فردوسی‌پور و دستور ویژه رئیس‌جمهور به روایت سخنگوی دولت
سخنگوی دولت:
🔹
در جریان اتفاقی که برای آقای دکتر فردوسی‌پور افتاد، من در سفر جنوب بودم و آنتن تلفنم هم رفته بود، به محض اینکه از سفر بازگشتم، به ایشان زنگ زدم و گفتم که من خبر را شنیدم و پیگیری می‌کنم.
🔹
بر اساس ابلاغیه پنجم مرداد ماه، هرگونه مسدودسازی یا محدودسازی سکوها و سایت‌ها، منوط به تأیید ستاد راهبری فضای مجازی و دستور نهایی رئیس‌جمهو به عنوان رئیس شورای عالی امنیت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/677854" target="_blank">📅 22:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvNnmC6IG9KBmoQArTacDGRR_fC0d8OkGJ5ut9KSc_pJrLra3dT65NZBJxQNDECm-buoJ5d5UHAISlrGlzaBXw-TgbOtWu0EuhRc55_CxV-TeaullfpKrmctGAXP2fBKBZWTxtqId9cP5lf5JpUjf4BbR_VYrSmieWggnXN8vBD8vfEdOTZpN3HL1bz5xb-hk7Azo8H89FVAA379QfTQjA5eMftX1RHlTnEHF9zE6GcHN8CasbcvlgxNSKgmkFnsQtPuB5pQ2QjuBxRgn-At5vlOFfH_f-obrElRmdholCpBgOCwUIUzHXHyLNIYL891fVUPuF8EjkhYXfQXtUOvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت پیکر دریانورد جان‌باخته و خدمه کشتی تجاری «آنا» به کشور
🔹
پس از گذشت یک هفته از حمله اوکراین به کشتی تجاری «آنا» در آب‌های فدراسیون روسیه، پیکر دریانورد جوان جان‌باخته این حادثه به همراه ۸ نفر از خدمه کشتی و با همراهی مالک کشتی، امروز به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677853" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافت
محمد جمالیان، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
هزینه‌های درمان به‌ویژه در بخش خصوصی به دغدغه اول بیماران تبدیل شده است. مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافته که نشان از ناتوانی مردم در پرداخت هزینه‌های بخش خصوصی دارد.
🔹
بیمه‌ها با کمبود بودجه مواجه هستند و ماه‌ها است که بدهی‌های خود را به داروخانه‌ها، بیمارستان‌ها و فیزیوتراپی‌ها پرداخت نکرده‌اند. پیشنهاد تزریق ۱۸۰ همت به بیمه‌ها برای کاهش فشار بر مردم به مجلس ارائه شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677852" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به شوخی‌هایی که با او در فضای مجازی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677851" target="_blank">📅 22:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه‌‌ای که دختر شهید مدرسۀ میناب برای پدرش نوشته بود: تو همۀ چیزی هستی که من دارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/677850" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWqTYwKv532hnweOwG0eflMi_TsYLghFIcKIYORIQ4-N1HXW5STKlgGGDsTxXpoBEW4HITQk2MGihEJBAOVkqVEYRet4qGzHV9T2ZyuqZkR9GxRMIlPtOG6Sl_fQ5AvBUJs3ugb75__U1ymZpnNGTy8iH8rPoxTG-Odccq7hwAliKeCV6T5ZflI-NLP9BM0Zfxdqc5bH_gEGZPXTIobTR4-BEyHualnFqmNi2qVml86O9vHb1jo2l98OzR_WUuLkSftXwDoKddK5L05IyckfJfQkyw3UdFWVUZ9LgewzHG8ufXTlQNZWxzRketD0bOUPPVk9_jeLoByWZWEQ3OsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه ژاپنی: پاکستان میانجی شد تا ۱۰ میلیارد دلار وام از آمریکا بگیرد
روزنامه نیکی آسیا ژاپن:
🔹
پاکستان برای تقویت ذخایر ارزی خود، درخواست دریافت تسهیلاتی تا سقف ۱۰ میلیارد دلار از آمریکا را مطرح کرده و در این مسیر از میانجیگری در موضوع ایران بهره برده است.
🔹
با این حال، کارشناسان هشدار می‌دهند موافقت واشنگتن با این درخواست می‌تواند به افزایش نظارت آمریکا بر بدهی‌های پاکستان به چین منجر شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/677848" target="_blank">📅 22:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veglpo4S2--qrdGUkR_8vdcoS5IO0rvnLOiXB0dBhBy0XZDQ-Y_fqaYLNmWAn3-n_R1e5jKnn9nMMmFXR9pR5H_85-aarQGf7RwTllWEztN447DklOEqecGHrSHrmJIO0nCF7_YodZor4m-VoUJ3Cc5sNR4juTALC0CJvgoM-3w76UNCy5mk_eX4bUYyWCLFeI6EufY12oTZfR2k3UZQQL-CpUxtj5UPb8rY7t_F1-Q-3nZgJHCqHfIVrfTV1S8WFyKvVGsTV1k8wXfwIxmbkPBPDuIKiOKdScukChdP8UeND-4ot59ifWDHAxvsKi3Kho-OyLOLterprPbC6W9PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش آدم‌ها فقط به حرف نیست، به کاری‌ست که درست انجامش می‌دهند
🔹
در نگاه امام علی(ع)، انسان با توانایی، مهارت، دانایی و کیفیت عملش شناخته می‌شود. هرچه انسان در کار خود پخته‌تر، مفیدتر و دقیق‌تر باشد، جایگاهش بالاتر است. این حکمت یادمان می‌دهد که برای ارزشمند…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677847" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
قاتل را بکشید
🔹
پرچم بزرگ دانشجویان ایرانی در پیاده روی اربعین و فریاد خونخواهی رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/677846" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Fg2K4OpQ_x_KLZur2sQxk7ChX_JhhLZySPeLE5CQRsXHO2gM-24QPUu-hdKD1kka_nqa3Dow_RalIy3x4f5aP1DWE8x_LekPvdnsIYuLeJGHQgBEbUU1qvZdcKudmhdAl4xZO2TiM6kP-Jg9CuCnEX5duKM97RdjE43ovQ3vkW7K3U5MTqU14P_Pod7sPpKAht98LaMVcatXjmq4kEowHyKURi2mjw4UJ08RPSifxkO4YM-60BXT-WW4nGfdqRkIyFoCyF-NIsAJx3gSJlrya1dv08ky_TPVE3Vbmnyg1OPoStqpn6xZkD53xHXY3xmdBfnDUeztzkyUeibT-JXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/677845" target="_blank">📅 22:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوابیدن روی زمین؛ درمان کمردرد یا یک باور اشتباه؟
🔹
واقعیت این است که بدن هر فرد متفاوت است. بعضی افراد روی سطح سفت احساس راحتی بیشتری دارند، اما برای برخی دیگر، به‌ویژه کسانی که مشکلات ستون فقرات، دیسک کمر یا درد مفاصل دارند، این کار می‌تواند باعث تشدید درد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/677844" target="_blank">📅 21:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/himWF_yAqspP3pZCyFR3Ch7s8BttPYmppw0Ltx63Oli01fS0Y7AuPYgGrGoKTX07xGbfwzEeEvjasiX-r-Y7t9F04okuI8dOyb1k99DyjO2bjALlyL4cVEbfRSjOW-zbxJxKNDtc8fciZpR4w_xbP-mxfPkYRTTm78aMQnT6gxd5ij5utXOtWq1SF-3p7qLbZ2mm2FZZPInFFFXgDDp_o9-EcRX8X0mH3ktwd9aWIkGfBXGDLhZ7ynn6rFCRPCVYJC5REKBdmuMKS0KPU36aeN492UIO4X51GEJLD-Ixg061NgNzb99XOpoBahS8fHTgC1PjVi6n0PiILRcAj786eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا می‌گویند «اشک تمساح»؟ حقیقتی که کمتر کسی می‌داند
🔹
وقتی تمساح غذا می‌خوره، به‌خاطر فشار و هوایی که داخل سینوس‌هاش جمع میشه، از چشم‌هاش اشک خارج میشه و این هیچ ربطی به احساس پشیمونی یا ناراحتی نداره.
🔹
به همین خاطر، به کسی که الکی خودش رو ناراحت نشون میده یا تظاهر به غم می‌کنه، میگن: «اشک تمساح نریز!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/677843" target="_blank">📅 21:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f53b22d86.mp4?token=PXAZFFsVSXRPr0AjNp8KCA0-Ras-Ffehq8XTOEZKdJ1eE0RwrdxPeI5hn4pLEpNshmrBHon2E_GgGdiMGS9Wc-pYouLQBzrUbxjEdXGwFE6oojgHaLkbCLYM5NI9whFoULy6aMdbQuiKAvYA4Vqjxk17_tZBJzBF7NuabnA-wGynCflKAE37faUIwacOWe44mLN6zC26BoAz2HRmQxvbCRXM81RjxtCcrC_7dNBvHEqIvz9vk6OcfpuUz1IzpXE9cBrWw1uqqJ1-8UYKq_hckSULyIn8JabqdKwwxsXPFMp24A_FJmb9b8a687ZkrBOvse1P-Tb0SEHf1bs12VfxGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f53b22d86.mp4?token=PXAZFFsVSXRPr0AjNp8KCA0-Ras-Ffehq8XTOEZKdJ1eE0RwrdxPeI5hn4pLEpNshmrBHon2E_GgGdiMGS9Wc-pYouLQBzrUbxjEdXGwFE6oojgHaLkbCLYM5NI9whFoULy6aMdbQuiKAvYA4Vqjxk17_tZBJzBF7NuabnA-wGynCflKAE37faUIwacOWe44mLN6zC26BoAz2HRmQxvbCRXM81RjxtCcrC_7dNBvHEqIvz9vk6OcfpuUz1IzpXE9cBrWw1uqqJ1-8UYKq_hckSULyIn8JabqdKwwxsXPFMp24A_FJmb9b8a687ZkrBOvse1P-Tb0SEHf1bs12VfxGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از رهبر شهید در مسیر اربعین
🔹
منتخبی از پیام‌های صوتی مخاطبان «خبرفوری» که در مسیر پیاده‌روی اربعین، قدم‌هایشان را به نیت «رهبر شهید» برداشتند.
🔸
صدای ارادت خود را به ما برسانید
👇
#زیارت_به_نیابت
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/677842" target="_blank">📅 21:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083e4068c2.mp4?token=JhKMcqc5BI3gjo1bzD1FeOjIKIJywIZ6WIjC5Q1o5ZHKhw4g6UhISmgSGWVME3mIKGpT_zMl0j5dmSt9wS2WWQKlbL8doKAr8ZDikrRWg4-iYMDDRGWVGLdZf4jWSFxCsqoSekub4YNcUFA1jF43nIpdoav_VwW4NINzmMHMIX4hfNQPwH9xAij0bSz2sccuSNPfhUUoWQ5XB66t8aVAfcC1TT5leDq0VFMGxi_07sXX3uWGMfm17w91hDZya6XFEj_YN6gnwCqfeiqJZ8BPpUv6yXcSRMruOLdg7adttMDhFTspr1THtAte62HWkl511aKGrVmr4OWeZxwZIcINnFEaTZpkNsrKi1bQ3UYVYynvrbTSXcI4mLW9hATNkyWUoh2AdhvxvUQi2xd6ulvvxZabZz5YFMwNFyb5seHd-7plu8HhSkRxU0rGmvxOH7SLc1M0AoYhTcTgYXolidKrFA9FuAhRxyC8HBq9DZ2YzC-3WfH0lc0URuWW_lIEHHSHvd4OLwKu4NmlUzPV31EIcrAFGpzStxYu-BpzVGvucuhAIeg8QQAhEgvZRz6uz9G6A4e20i-nIcUPRaVN8yN0TJh6qYr2Hz2NM_13yWipWDhTjS6oCdteGItcvMDArouT4gqUMwU9kMbVkNJa-R-Vgp4Ow3XsR7oX6WneLHZqpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083e4068c2.mp4?token=JhKMcqc5BI3gjo1bzD1FeOjIKIJywIZ6WIjC5Q1o5ZHKhw4g6UhISmgSGWVME3mIKGpT_zMl0j5dmSt9wS2WWQKlbL8doKAr8ZDikrRWg4-iYMDDRGWVGLdZf4jWSFxCsqoSekub4YNcUFA1jF43nIpdoav_VwW4NINzmMHMIX4hfNQPwH9xAij0bSz2sccuSNPfhUUoWQ5XB66t8aVAfcC1TT5leDq0VFMGxi_07sXX3uWGMfm17w91hDZya6XFEj_YN6gnwCqfeiqJZ8BPpUv6yXcSRMruOLdg7adttMDhFTspr1THtAte62HWkl511aKGrVmr4OWeZxwZIcINnFEaTZpkNsrKi1bQ3UYVYynvrbTSXcI4mLW9hATNkyWUoh2AdhvxvUQi2xd6ulvvxZabZz5YFMwNFyb5seHd-7plu8HhSkRxU0rGmvxOH7SLc1M0AoYhTcTgYXolidKrFA9FuAhRxyC8HBq9DZ2YzC-3WfH0lc0URuWW_lIEHHSHvd4OLwKu4NmlUzPV31EIcrAFGpzStxYu-BpzVGvucuhAIeg8QQAhEgvZRz6uz9G6A4e20i-nIcUPRaVN8yN0TJh6qYr2Hz2NM_13yWipWDhTjS6oCdteGItcvMDArouT4gqUMwU9kMbVkNJa-R-Vgp4Ow3XsR7oX6WneLHZqpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف بی‌سابقه فرمانده سابق واحد ۸۲۰۰ اطلاعات اسرائیل: تاکنون موشک‌های بالستیک ایران عامل تعیین‌کننده این جنگ بوده؛ حالا ایران معادلات منطقه را تعیین می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/677841" target="_blank">📅 21:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کانال ۱۲ به نقل از منابع امنیتی اسرائیل: رئیس‌جمهور ترامپ ما را در وضعیت ابهام و بلاتکلیفی رها کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/677840" target="_blank">📅 21:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
یک شهید در حملۀ تروریستی به یکی از مقرهای ارتش در مریوان
تیپ ۳۲۸ مریوان:
🔹
در ساعت ۳ بامداد امروز، عوامل گروهک تروریستی پژاک با استفاده از دو فروند ریز پرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای این تیپ در مرز حمله کردند.
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/677838" target="_blank">📅 21:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۵۰ حزبِ ویترینی؛ باهنر پرده از «نمایشِ حزبی» در ایران برداشت/ خاتمی در مجلس به اصلاح‌طلبان گفت دو ملیون رای خود را بردارید و بگذارید من با ۱۸ میلیون رای خودم اداره کنم؛ احمدی‌نژاد هم با اصولگرایان همین کار را کرد
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
تمام نمایندگان، ائمه جمعه، وزرا و مجمع تشخیص مصلحت نظام عموما به دنبال مطالبات غیرممکن هستند.
🔹
امروز یک نفر در کشور ما رییس‌جمهور می‌شود بعد می‌گوید حالا از کجا وزیر بیاورم. آقای رییسی یک سری را از آستان قدس و یک سری را از دانشگاه امام صادق آورد و همه آن‌ها وزیر شدند.
🔹
آن بیچاره‌هایی که در مجلس نماینده ندارند مردم بیچاره هستند. حوزه انتخابیه سراغ دارم که در ظرف ۱۲ دوره مجلس ، ۱۲ نماینده به مجلس فرستاده‌اند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/677836" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74471ab558.mp4?token=s7NTc-TxI443QN42KpcYHFk7Fj1NO3Hag8XWpb12t7cC-i-I6qqlWo5v8F508nfwJo0SV5q-xSlKgFSf9MZ2StA2E45MnNno-Q1Gd2qtyPJbyCnXwhzxsCDf4iyofdkmlZFtpmo89NIZAziXXYMbowGxKRTQnVSgyUEckNQVQaGnJMUIIhxg48X-DwyV1AWg8K0fBfcI3hPohzVRFgPgyxPtrXAKmRGSMPXcRTbOXiZO4XeJHUiq7qUY8fnFDJpBlsWw0RjXNk3kdh086v4yL01v_X2HDDbYUxo-ypScwqun5wBbbX4pPXVIRa9aqDHFp7U0Gq7aKc7X61Ax_Fzdrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74471ab558.mp4?token=s7NTc-TxI443QN42KpcYHFk7Fj1NO3Hag8XWpb12t7cC-i-I6qqlWo5v8F508nfwJo0SV5q-xSlKgFSf9MZ2StA2E45MnNno-Q1Gd2qtyPJbyCnXwhzxsCDf4iyofdkmlZFtpmo89NIZAziXXYMbowGxKRTQnVSgyUEckNQVQaGnJMUIIhxg48X-DwyV1AWg8K0fBfcI3hPohzVRFgPgyxPtrXAKmRGSMPXcRTbOXiZO4XeJHUiq7qUY8fnFDJpBlsWw0RjXNk3kdh086v4yL01v_X2HDDbYUxo-ypScwqun5wBbbX4pPXVIRa9aqDHFp7U0Gq7aKc7X61Ax_Fzdrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگ بو فقط یک ادویه نیست؛ از خواص باورنکردنی آن خبر دارید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/677835" target="_blank">📅 21:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b51a0ad3.mp4?token=hJxIwUYimOaKe_JWd8jBx5tcav9Y_UFFy7GMF-4LXOVOXYaJHGpUM2vpvYnB50tZqgRPH4XJjPAzPLWStkdlu4Mn2ObPUo31KsXxsudOgriTRvgImvdf6TQY654hFC1tpqG6GWLoN023jKBs13o-luSMjX-Qe9O-QrmW4mmFqR8dUK7ZWABVjZnmRH_GhY26YUKoswQIUUYBFfymMpmdXTpzMpM0Dzy-3UzVJevpRzq4qyBGibStR-n-dIQ7za0fF-r2-P_8AdB1CimfYq7C0TvA_0Hrgr3GF-4lvTIi4alCN5WH9JMVvWQg-q1DuYpaJBUgajATeiHVYGiaN4EhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b51a0ad3.mp4?token=hJxIwUYimOaKe_JWd8jBx5tcav9Y_UFFy7GMF-4LXOVOXYaJHGpUM2vpvYnB50tZqgRPH4XJjPAzPLWStkdlu4Mn2ObPUo31KsXxsudOgriTRvgImvdf6TQY654hFC1tpqG6GWLoN023jKBs13o-luSMjX-Qe9O-QrmW4mmFqR8dUK7ZWABVjZnmRH_GhY26YUKoswQIUUYBFfymMpmdXTpzMpM0Dzy-3UzVJevpRzq4qyBGibStR-n-dIQ7za0fF-r2-P_8AdB1CimfYq7C0TvA_0Hrgr3GF-4lvTIi4alCN5WH9JMVvWQg-q1DuYpaJBUgajATeiHVYGiaN4EhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور حجت‌الاسلام محمدجواد محمدی گلپایگانی داماد رهبر شهید انقلاب در مشایه نجف - کربلای اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/677834" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677833">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyTPSAER4K_vj7UkS3MJ0GO7h547LGAPwVAybW9wH7r3mLyhRZuoy7amrYK0Nufgjf8Ozl4v9heoi9jc42Hs0fOk5brTbzDVJMF2Ci7rnL6_7ZLrmCycRSXHlYcGwZPuw-rpHlWPbawPnkgDaQjTw1_pH5dXjWD-CfHaP8HJNHU4EBfvr7muxScEy_VHJ72Ge1yufGA2etzFy8Wz9RXEtDDKSniFiXWbdxMxk_ROmZYnCOJVc9yOr1p0Pp1eQxhcroPV9MXtuzuX-VW9-9uFh1s530JOgQGwZhYAzI1gX1joYMAq7mwSmz8koU0Oov6c6PJou52Jb3y92anF1qrf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مرموز نتانیاهو و ترامپ/ همه‌چیز درباره احتمال محاصره زمینی ایران
🔹
به نظر می رسد آمریکا توانسته رضایت کشورهای عربی را برای محاصره زمینی ایران جلب کند اما این مساله (در صورت صحت) کافی نیست. برای محاصره زمینی ایران باید دول مهمی مانند دولت ترکیه نیز راضی بوده و با ترامپ و اسرائیل همراهی کنند اما اردوغان نشان داده که با ایده محاصره ایران موافق نیست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3234830</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/677833" target="_blank">📅 21:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677832">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxJGp52zEahdHh7xYrPWVUTegrFSFasRcWEKn-w3TMhTFAeLI-UJRhdNm1WBEraIYmaiwb9EO2rOQFLtMtzUNOMYPm-O5lDfGesCDNR4T9R515DwWDk2KKzcGZ2XAIucwl8-aTHt7LNyELlwJj0lz68xswmHpIgxirdZ0dfElaP0bCL-Vhdm51ON4sNlsd4EO8ArEAhmO7JGREcryVT4eM3uJCfL_LV9qSgWY3Ei-02FQU8970mTSt30dH19kAGWtgqdTq71OnbwjRGt9Hsy2WTPHT70XSWbvg_Kl73tROOX8HeDd4aUKkXV3jyNuvBD6z4QEMJ96Kvusqh3rnOuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعضی آدما مجرم نیستن؛ فقط در جای اشتباهی به دنیا اومدن
🔹
ژانر: اجتماعی | درام | جنایی
🔹
خلاصه:«مغزهای کوچک زنگ‌زده» تصویری بی‌پرده از زندگی در حاشیه شهر است؛ جایی که فقر، قدرت و خشونت سرنوشت آدم‌ها را می‌سازند. فیلمی تلخ، پرتعلیق و از ماندگارترین آثار اجتماعی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/677832" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677831">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owQgHcKcoMYZyceRF_i3Dl73L7KlzcSqfg2AkTt_mOM_w2rEuTl6CkQFapz2RGSeAlDvjebKxIVnzjNea5gdKq97XMLCYZjZMutuOvT0b9gFo2FT2FGDRyssKmjo4BonYV0n346rIMXUQUaejbG7gG_KWE-kaC3tTNyCEMqfgmrt5dJalwrVybnEn_ozWWJsdkj1r6Qhi7_8i8RXFwrQxR401o34tq_WGk13Gpv2F5aFQxEa1qk9rMy5OLuO0bcNq8PLFO9t786dxHcGj-ZvOTGql973-ICuVBvDu9gYQk8Bh6kQdgf9e7qq8X9dltpykUy1EI5uz0ILopQATqbN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش ها حاکی از ادامه خروج نیروهای آمریکایی از اقلیم کردستان عراق است
🔹
باتری پدافند هوایی MIM-104 پاتریوت که در فرودگاه بین المللی اربیل مستقر بود نیز به کشور دیگری در منطقه منتقل شد و مورد اصابت موشک ها و پهپادها قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/677831" target="_blank">📅 21:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677830">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf5BHpjZZGi7WjD79C2SkGsu1sYpTn1HobBMAwLFtwfdBWLMc_S6WDq7Wpap9eN7BHkGdNCJfQM2tVg0zxpHdv6cnT6bsn5T5y4pLJDpAhA7fYv8j78Ij-_NAYYSOMjjZyZchv4Nm5NNuf6JK27BeCS06QPiTBxRt2F4ReX0DQY-V7z7TQRpZX9WOqgMe7tgkeyIGK66Dj4W4VslI9Mnl8x601s73JvwbE31YIhMMvv1SY_vjf5fAlqbgj1AH-s30PFEjCY9E8tUP1wJH1x56x7REO335A9-tpLSQ59wdMCJqUT76k9Jf7fNznolZXt8mK7eVClTFKunOzwBfV6JxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مدیریت راحت‌تر هزینه‌های درمان با بیمه تکمیلی انفرادی
بیمه تکمیلی درمان انفرادی می‌تونه خیال‌‌تون رو بابت بخش قابل توجهی از هزینه‌های درمانی راحت‌تر کنه.
خدمات قابل پوشش:
• هزینه‌های بستری و جراحی
• خدمات پاراکلینیکی مثل آزمایش، MRI و سی‌تی‌اسکن
• ویزیت پزشک و خدمات تخصصی
• بخشی از خدمات دندان‌پزشکی
✅
با توجه به تنوع طرح‌ها، می‌تونید گزینه‌ای متناسب با نیاز و بودجه‌تون انتخاب کنید و با درنظر گرفتن فرانشیز، سقف تعهدات و دوره انتظار، انتخاب آگاهانه‌تری داشته باشید.
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677830" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqWMMTjB8ec9fG_46VUIwukoHBQH-laDWTuF5csdcYQXJ1I2CbVxxNrGdjOqo1GjLhF4cekxPsDgdUGy8Vo2YjoyDsA1ALqP3qkg_WPdAuq8SVj8em_CCPD7epNNVmTTcLJDcxdDqVp0Y3YfF2YT2ZN_BZF72H2jfdlpEDC7C6f8Fb1-lst5JmLKadEbypTlg8ZH55Mjw5HXomE9n5Tsf8ju8hnrldJS6I51Ij5VhNF8NW6k5N37xvbZBNi_-3ZECHzI_BJfUwSYONgabBswYurde6FyaBaUuoUFMa5ptIz5DWCCXBiiK9c9Nf50OHd6uJmXuB4kay605zS6e9jB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad9X1CP2_QvimpAhR_y9K2PrXyQdjRVStDSWiYEeovrSPVJxIsuqheYSHtAGp3616i5G8mlZZBrATipnhOHEVrjlwi9CbMJUztfSdhdn_FGRVWor_AmjXwenUJAAHupC8dadOjYTsuByieXDIvo63fk8K8_klLAWDDmOnwI8CJ9iVlyRtP2HD_tEoY-OWfz-nCT40AZyWO8Gjb-DjXX-DLISEl3jmxPVXa9Rbze86ft0DZrEOqLPx5743F4TZZ9U7RphBNuxlLJG5Cie5c-hD-yXJyG4qJETRxbVozt8_zTltwlIufi84K91hu_7jEG4CWce8Kb3-kanhpMujgKgIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران ۱۰ درصد گچ جهان را تولید می‌کند
🔸
بر اساس آمار سال ۲۰۲۴، آمریکا با تولید ۲۲ میلیون تن در رتبه نخست تولید گچ جهان قرار دارد. پس از آن ایران با تولید ۱۶ میلیون تن در جایگاه دوم جهان ایستاده است.
🔸
در مجموع، تولید گچ جهان در سال ۲۰۲۴ به حدود ۱۶۰ میلیون تن رسیده و ایران با تولید ۱۶ میلیون تن، حدود ۱۰ درصد از تولید جهانی گچ را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/677826" target="_blank">📅 20:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677825">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
انتقاد پزشکیان از برخی روایت‌های نادرست درباره جایگاه رهبری
🔹
پزشکیان با اشاره به منش و رویکرد رهبری معظم انقلاب و تمجید از اخلاق، منطق و تواضع ایشان تصریح کرد: یقین دارم با حمایت‌ها و پشتیبانی‌های ایشان خواهیم توانست بسیاری از مشکلات را از سر راه برداریم. همانگونه که با حمایت‌های رهبری شهید و والا مقام توانستیم در دو سال گذشته به توفیقات زیادی دست یابیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677825" target="_blank">📅 20:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6UlAairqqvlnfUgaB8kBnjxkN_h8rcmD6puuA4tAb13LN3mnLAU-z2RrclBWI-Uykt2_04ZScwsekDTuWIN_bU-s2WEuim1ZOkMWbvWxNN4qEXHnttTCd89xABawo23hh9Nh5NyFl-AF2jOwOqP1tC1ivbnk2LaEsAkMwrDRHYi3GEY1tV6YSfbs3iCDOn5IndsvaRTCOaHzO5f8prwVe7y9WsQy4uFsL3m9QL7siQF18DumNdpZ8KQMycKsdYA8nFTPNRIFDdnYGsHb5LXoFzKw1Lja9wtHNJLo_z6C3I-aGOUbXCN6n0N7DBx8GwDzZHJtIq9SClpH7PFhbkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهتزاز پرچم ایران همراه با پرچم های عزای حسینی در بین‌الحرمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677824" target="_blank">📅 20:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در ۲۴ ساعت اخیر انگلیس، بلغارستان و اوکراین تماس گرفتند و گفتند ما در حملات احتمالی آمریکا به ایران نقشی نخواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/677823" target="_blank">📅 20:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677821">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۰۵/۰۵/۰۵ چند ازدواج ثبت شد؟
اعظم قویدل، سخنگوی سازمان ثبت اسناد و املاک کشور در
#گفتگو
با خبرفوری:
🔹
بر اساس آمار در روز پنجم مردادماه ۱۴۰۵، تعداد ۲ هزار و ۸۷۱ ازدواج ثبت شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/677821" target="_blank">📅 20:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677820">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=jYGwoTqbblYyWhNrKjffDQ6MsUg-JDre0iZ9je8xr3ZaVZK1VkrmfIELbLZiTzs4O5iJ0YvgGoM5Xw4GFjEEvbHuBJ8dOrSXXC7unuCzVb0jGZOpnRSDcMXUwO6SLc90cbdvaPerpb69q5-gqK_SVyYeyXc0eKtjm0YXILr24y_F_UXvorQzVIWf2BV-eXmzmuRFoK3D3b3Kl0SNz_dWbG3zUonwNniJhL-OZojqjO-Phxu8LTVpdwR38VLmGYf_L9oVjte-8fbIL9iGRH4LGJnZJqj-mgkUerMLx6-NcwmZ3-t6o0TURDQpRpeaum5j2lAARzKmlZ_wpKFQcYefEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=jYGwoTqbblYyWhNrKjffDQ6MsUg-JDre0iZ9je8xr3ZaVZK1VkrmfIELbLZiTzs4O5iJ0YvgGoM5Xw4GFjEEvbHuBJ8dOrSXXC7unuCzVb0jGZOpnRSDcMXUwO6SLc90cbdvaPerpb69q5-gqK_SVyYeyXc0eKtjm0YXILr24y_F_UXvorQzVIWf2BV-eXmzmuRFoK3D3b3Kl0SNz_dWbG3zUonwNniJhL-OZojqjO-Phxu8LTVpdwR38VLmGYf_L9oVjte-8fbIL9iGRH4LGJnZJqj-mgkUerMLx6-NcwmZ3-t6o0TURDQpRpeaum5j2lAARzKmlZ_wpKFQcYefEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه امام جمعه طبس بر چادر داور مسابقات والیبال کارگری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/677820" target="_blank">📅 20:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677819">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
روایت مردی که پس از بی‌حرمتی به پدر، عذاب برزخ را تجربه کرد
🔹
00:08:45 لگد زدن به سینه پدر، چند روز قبل از حادثه
🔹
00:17:20 اولین بازخواست بلافاصله بعد از جدایی روح
🔹
00:26:40 ناامید شدن از الطاف الهی در رؤیت لحظه ظلم به پدر
🔹
00:37:00 حضور حضرت ابالفضل با هیبتی وصف نشدنی
🔹
00:42:50 بازگشت دوباره پزشک به اتاق عمل و نجات پسر بخاطر حرف پدرش
🔹
00:53:20 رعایت حق‌الناس در شرایط مادی و کلامی
🔹
00:56:40 لطف خداوند در هنگام طلب حلالیت از مردم
🔹
01:10:00 باور به معاد مهم‌ترین عامل در عملکرد دنیایی انسان
🔹
قسمت نوزدهم (امشب پدر را میزنند)، فصل پنجم
🔹
#تجربه‌گر
: بهنام راعی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/677819" target="_blank">📅 20:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677817">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان منطقه آزاد کیش</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWZxq_0RM-B4Iug5yHxkXxrQ9Vxx6NjJbZMAC96RWAC4M022STUglDkD5-IEwGYWqhoN22HBZRToimHPYCvkjQMAfRjitXmP3HvRg3KI9FJpq-N28nnTBBG6-F0PjeV1bzSRHPZcjMJaihFzh5N-uwwHtsvP-1Xr_wpOe41M5UWLM9O5UlcPEP8-83u62_muCmuJB9zx3iBZSUKbjlLkIDjmkhqvzHRAjVuWiC147VzQRet3XHNZHXozWLJyoCmfatnyITUXKvJ5mQT6IJ7wvcIWtwwWW8E3ZHCuC5iSdMyZXNnm1FySzklxkD3aJvrKmhH3LUkn0jSnHuhgIXIpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*اطلاعیه عمومی: فراخوان تخصیص اراضی مسکونی فاز ۷ شهرک صدف کیش*
سازمان منطقه آزاد کیش در راستای توسعه زیرساخت‌های پایدار، از متقاضیان واجد شرایط (حقیقی و حقوقی) جهت مشارکت در طرح‌های سرمایه‌گذاری در قطعات مسکونی فاز ۷ شهرک صدف دعوت به عمل می‌آورد.
🔹
نکات کلیدی برای متقاضیان:
🗓️
مهلت ارائه: تا پایان وقت اداری ۱۴۰۵/۰۵/۱۸
🌐
ثبت‌نام صرفاً از طریق سامانه سرمایه‌گذاری سازمان به نشانی:
Invest.kish.ir
متقاضیان گرامی ملزم هستند پیش از هرگونه اقدام، ضمن مطالعه دقیق ضوابط و شرایط مندرج در سامانه، نسبت به آماده‌سازی مستندات قانونی و مالی اقدام نمایند. مسئولیت صحت اطلاعات بارگذاری‌شده تماماً بر عهده متقاضی است.
https://t.me/+Z7XNY2cgHjVjMDZk</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/677817" target="_blank">📅 20:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677816">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYR-SBqfa23e96gIcIKhEOUEsWYh11MTbNWY3HNk2aNJ1kOR46bKmrpPsG4cnGCfa_45CF6UnRk0UInxy1132lXBgHip5bEt1mwzEH9bwq6i2_as3_nDvLzIkQFJLVhdFlpmvHsyJN9Aludevb-GZS_kYzq2pFagwaWJ-TZ-WJ_TKs8gKi7xIH5WGfJYNnpK81bC7ZWyOnfMJOhvGH8Z44cgNLKZ6F2SDjel_SW5UcTnIqUygo661NJKDa7I601O-Z7V7vKuwAuUJRQ6xCT1e5Idey5avtqM9IZZ4hTdM12PNi8Aima-qxh6dLc2ErqMHQgJrfxX_1H3vu6O9mEwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه به مناسبت دومین سالگرد شهادت اسماعیل هنیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677816" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677815">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مسیر مورد توافق در تنگه هرمز، نه مسیر شمالی و نه مسیر جنوبی فعلی، بلکه مسیری جدید خواهد بود که دو طرف درباره آن تفاهم کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677815" target="_blank">📅 20:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مدیریت آینده تنگه هرمز با ایران و مشورت عمان انجام می‌شود
🔹
بر اساس بند پنجم یادداشت تفاهم پایان جنگ، مدیریت آینده تنگه هرمز باید توسط ایران و با مشورت عمان و گفت‌وگو با کشورهای منطقه انجام می‌شد.
🔹
در ۲۲ یا ۲۳ روز نخست اجرای تفاهم، مسیر شمالی تنگه کاملاً امن بود و کشتی‌ها در آن تردد می‌کردند
🔹
پیش از پایان مهلت ۳۰روزه پیش‌بینی‌شده برای بازگشت ترافیک دریایی به شرایط پیش از جنگ، «مرتکب تجاوز علیه ایران» شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677812" target="_blank">📅 20:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
عراقچی: مذاکرات بین ایران و عمان درباره تنگه هرمز در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند
🔹
عراقچی: بسته‌شدن تنگه هرمز به‌ دلیل کارشکنی‌های آمریکا و محاصرۀ دریایی ایران بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/677809" target="_blank">📅 20:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF5o47x7NVoaUj4PXQkzpJbARy16HsUvoMTw4Y3h4VJHjd71U6GFUJq3VQCMTze-F6nZvkvSiujWUmOvi9dCkSDJdJnDzKz3ei89UcE0nuENjarsr-zcXXmPw8SGIPO677i397GCVKdE7qBuFLczZQ_I-tUUBJpRwf0Tm9aY7bgVW0gB8YXI-nKwPg8MMsQcooSeDr1-9kvT18HwaFTohFN3DamI9FbVnsuVW3ZNxH8cOYhA69snKEAdxggy3Yt1X9qzXyITA_51oKji6p88npJtza5zKDdaUSf2maX25iTZn0Q_7SNVWcd2mfKVuNix45B2hl3JzA87o7Ps0gneqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/677806" target="_blank">📅 20:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRa5JOjSG-c2uiJq46rEJXUqpuOiSi9x8hcynNehwYcU5mRKz4xofqLgJrEAn8GCAn8UlKNVaE2VAY-WP4E9kpvhPmr53oz1XmORS3RjVMXaqSTRhv_ObJmad0iEYk6ToJtHdiCmsp5A9RCqPwx2KWq95pyBKV03Y1FuhOYozxYE5gBFnmzLmzwN-4vXWU3GoOya27g_SQFq9KKGcvqUrs1VLtUBAAXpjX7rOLVvEBnlMvbYlXN5bY5saHX8gh_bFo7HrIDXQzZIjliYB_Uq_9fBMWejrBSx2-Ik2bXspNt3cSm61-bPA8Hl_Nv9Xd6YmScjqCfGttZhFokd_ttCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمپول لاغری زیکورپا؛ بیش از ۳۰٪ کاهش وزن علمی
زیکورپا با ماده مؤثره تیرزپاتاید (Tirzepatide)، با کاهش اشتها و کنترل ولع غذایی به کاهش وزن کمک می‌کند. اگر اضافه‌وزن دارید، زیکورپا با تشخیص پزشک می‌تواند به کاهش وزن
ماهانه ۸ تا ۱۰ کیلوگرم
کمک کند.
👨‍⚕️
تحت نظر پزشک
در
کلینیک آئورا
، پزشکان پس از بررسی شرایط شما، مسیر کاهش وزن با
زیکورپا (تولید داروسازی دکتر عبیدی)
را آغاز می‌کنند.
✅
برای دریافت مشاوره رایگان با پزشکان کلینیک، «
کلیک کنید
».
کلینیک آئورا</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/677803" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72ef27a54.mp4?token=GG9onbeUJwjoy7bQV6lMtLtGW7lJMDnLk7-cQ5nCfCJ7waXJ6FRZop5VEHzahYWPyf-LN-B-lgYCPvLc9JnePs1O8Ck6QJM8CssOlMrGFiZBZVr_4_b4zwCD3x8npwmGzGGMdcf23yZiqn5VoNYXrd3Qa_MQPAiIsctqmvLWsBn67YejiDeYSgm-PXq8sWHsYL7aSpa1F8klVjB6aiO418bgXe06vGWZDndfcQTgnRd3hqPGsYg7vp-MUSktozYii2gHpFZ19NA7qMjU15xKiWOrUD9OcW8VHtqE5jq1KW6xHE4mRhs-Z9GCJwCOBokFRQuWI49Hs3DTKqCkFiB4HGKFTFVpYWIqeIMFqGiXEBa5huNaxSijHVvUzC7rg3Q7jK2nW6jLUavyVn7ZmPhczPVa1a9knlVaYAOU8nLyRGfM5K6gsyZx4keAr56riW3qLhGGsF4HTTue-NDT_Z6upepV1chLosM1MPftgqqmxqY2oaVpAjBhJkyKrJUn_GmluAu1TgfDU2aweRwpoJn-_Y4xxh0cP0f4EhQfVBvsB1FdVL09Y1RlGmR9rCYqSyKLAossqD6dvX4X8Nh_o01lt3qAILFy-eEqqkS78m5mPDIICLpZ1eEA7tvTip388ySpvkPv3C9NJFqBH3plcopsxkS15o5-PhG2-AhaExFWN3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72ef27a54.mp4?token=GG9onbeUJwjoy7bQV6lMtLtGW7lJMDnLk7-cQ5nCfCJ7waXJ6FRZop5VEHzahYWPyf-LN-B-lgYCPvLc9JnePs1O8Ck6QJM8CssOlMrGFiZBZVr_4_b4zwCD3x8npwmGzGGMdcf23yZiqn5VoNYXrd3Qa_MQPAiIsctqmvLWsBn67YejiDeYSgm-PXq8sWHsYL7aSpa1F8klVjB6aiO418bgXe06vGWZDndfcQTgnRd3hqPGsYg7vp-MUSktozYii2gHpFZ19NA7qMjU15xKiWOrUD9OcW8VHtqE5jq1KW6xHE4mRhs-Z9GCJwCOBokFRQuWI49Hs3DTKqCkFiB4HGKFTFVpYWIqeIMFqGiXEBa5huNaxSijHVvUzC7rg3Q7jK2nW6jLUavyVn7ZmPhczPVa1a9knlVaYAOU8nLyRGfM5K6gsyZx4keAr56riW3qLhGGsF4HTTue-NDT_Z6upepV1chLosM1MPftgqqmxqY2oaVpAjBhJkyKrJUn_GmluAu1TgfDU2aweRwpoJn-_Y4xxh0cP0f4EhQfVBvsB1FdVL09Y1RlGmR9rCYqSyKLAossqD6dvX4X8Nh_o01lt3qAILFy-eEqqkS78m5mPDIICLpZ1eEA7tvTip388ySpvkPv3C9NJFqBH3plcopsxkS15o5-PhG2-AhaExFWN3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه این روزا درگیر پنیک شدی و حالت خوب نیست، حتما این کلیپ از دکتر ابوالفضل احیایی، متخصص اعصاب و روان رو ببین..
.
https://t.me/dr_ehyai
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/677799" target="_blank">📅 19:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWs_kK53Gr74Rn9sOyjrcUgx4-M1mzZ-cRK-NKJ4X_JpLtHTtm7EcF2S-Mz4Wrk1sYQoqvpj60wrh1sxWi0C6_kpi1Zh0LQVaYLjr7U6ufGvW45nLbEHp88r7O9alZeZPOKWUrqSZ_vNdvY16Qm-t69HjzvX_u7M0ywppKYZ68UAnVBWyKmr881TkPzHENifopBvjE5_kr1KGLk592bGmnYWWHOn6r8ve7pYGsKYLYN3xyx2rh_YY-h6w2iU8SzLKBN9Hwk0BfKlhzCS1BIOuzVnTNIhDt_E-qlKm_VDLjR4Xr3UCjoH6W1kEi1lGA6yE3MYM2-6fyhBbhDR297Z3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mubKiYtE9O6Mz89DViZKrylRv4lzYNNIPdQsF_ycMpYCW0xbPri7aN3qSrCzp7R0p6Kn5lApGuPzKXRqeiLMCWZUdUo524ynmthR32-3Yb8R0TicDzmhndGEUeBVk4mfaVAJuIW95zw8yvN_x919UgwV8tF3Sc1uwi7kCoZmNJaGsloLLajCLviMHb7zLvH3Vq4jFDv2LSto7bayLZLYnElUKfxcVxtVn-hZDbbdSu4aNE36xX4B9L_ILnVnnn9mXUfbZyxvg95u8CkCtYgHAgeSO-X4_g6yWJzofTFzoSgfzJwW2OcXldVGjOcxAzmA3v4jSMI5-pjoHS2zpKrHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XswOtduc8X-t2ewaCTNniVR_vL1St9SqJ3zweH2UVahwoBhiD6j3kBCxhQHNhRnvRHKgmhg10877Um-dsTSKgXAKtJtwpVafKGfOa__8UFc0HXRJ5veCmz_h_X6aAbwmTZuqgprBdqTwBMFhIVNH3odZ_wuDX-qk8CvMttGZX6rawNOb5QshsMVIvjCpS1r8z_ouReCnON0zyiv0eS_x6uiH88D3JSj0sz-h9Tz5ebGMZ8qgsIvYFLMvaYv_0JLAL_7Febww9Uz8q5xoP6FGdbbMTQ1vlQ5h_0ZJzM5JNDbrXQyNClOxeCh888RKilPcv2QZY1mwMHOe5ExLoVJZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_QH3EUZELPLtZpv6qQJJNTzgH2cvYX8nyjYMnMcLtjtj8WBGndPzI8LkCsMa7PABgeB5fQDLB4n0N7VvFoGCEijhC4CKv2VsjDMIv-_21M7i_4R22IwnTysAkwUHJ9JblD5OGh5m7QNoP2CNd_nGkm358n1eFEpr27VhKIZy-aBbSRbgPjCH5tjSHBO9Vn4UVzH5dz62x7GFyXbGa9qNffukuxCG-K8P-1TxYuZl5kn1pSUN_c_vB3_Mr_azv53Sh8w9-IHmlu1pWzEzsOkckS4ug3CEbAAixGLIvcrbjCe5577-FC55pJKVE60xxCeB-IVIT57NLKSqKhS6T1mXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbxyAN12lQ3k2ihuK9NMxpXXHcJF-92xVGsAoF4bhZyN_pr_8mXP2QzCCNtRakwtD6VL8LWWwgo8THUQA093o_DhVoRtKpr4T5P_FF3qvCxZbZCtskC8ZKIQMYoUDEYmRX_A940QMGJB1mLnakAgm-dx7OFnmRgw5VDO9rnpJijUifsN4oH-KN5XWPiGDWNE8E-7M2rdo5wgy3D1k_q9uB3sm45sOcifN9adsG3i9wj2ATCGSy6rPLywTfK0ACAJtwNRmOzMhB35LXM5ilruneAw7ubCDYWD_ljFgGmsI9iBIMw65T6Ch0KUh8UCxMuUxlkwPq5nnvgvca6_EkEOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quH8mbMa_7MBIfYv6Xfvn8sYRd7GBVr4zbsXMVafEzrMpa4B7N-1YLLcbLJequys348Mr-wVeE2JTpOehIjYA8dxe5PzxjI1xNZUD-J18EP36F17FWPthM7Fe0Ldbj_5L9IbC-WdO0ICFw_uam_E_s6NcOuVtfty4xJwGdKBi1sr4Md_GU-GP_1ZLl9LXQzH1JXolJoQ79c_IAeWNhVHc79m8kgpOmcuuzW7tXttaAQtYqetid7W4eHColP46lkP9yhm4c1Z2hwKHBlUrDzZjOiDsUcMa-OKNKs_BQdqiEpXMiiX1aibngcXpr8KXcUX4SWwcvtD60w4KMyCzZN4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up2BRHMSTOmjNCa46c4PZTB0lL08V2kXQo-yHsFdX5vDWDZtCb52cw1HFDyfSLg_F8QVpKddXyYl-mX6FyPFoFwu5I74O-1IuyxRDRIicBsIBXWeHvOF2S2-wKNJEu5vuTHM7ecIUP-X14ACzcI6-xKLj_5_r7Hp30l_lsHNY3zl43ZZn_o1439iLD66Xb8T3yrwIYSO-gAy0KiPtC9K5QWFCd_cAGRSENJUl_AAxKtkDQUbCqrOXk2E2-xj2ywQPa8MADpym8losSTDqWQDnRG34MQczgVIE9BPWz2ixPfbwKYJZLPf21HGV4IfA2TkaR3Vu5PMHqz1Bc9lDexERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_J78O1XfyUlXKMd1H8Nkeat-g0ObfliWOlPT84OcwtkO5nEqSKM2_sonVzK719kT1fjTTXGN2p_G5YRYZ-eYYd0sMisXTKHDtsgDaJnlypAp6jrii9n5ESw-0c5s-7J3Cuf5Q06X_NNCMoRKXg-6-e1FhMNmHJOZk393uqN2ajotX0IC-h5nq4RrI2bRztdi4agas07PoGoijYweHEmUP7OGpGgNAjfpO7MDrLw5rgp7WXfk_P1B52HHQWMLSQNL3MxfrHSELxcvA-2glSjQT6D52sFQUDwbeczM8QuiUPB9eEvxvVT6ynVxrSvYuUAeriGyKcK1xE8DT5JT5aGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw70iV0qt5g5OeU3dZBP3QdSaU3OKV-tJzBcWH1xcVq0BPDS-NBcsB59dkr0i4ngHCJyeevsCdfcrOZ19GX0e6YFPB5LAeryGFRQgDKsoLyoIZDLItCLa0jMYffWIbuX0twJ4dCk8M8dxB8ei8qPjb1Tu-ZllfSceiUzZ_sJz4Jd9rawH97-x7IGKnDdY1ZrfDYV0IgvZ7cIXyM7Bf4on4-qwnHcbLOGpwiymY27PRPsly-eyv8gNFdcp_m10y2S06cXjHcRdxyRzGNeG3jeCFmqs43HCZnrbt-9j4zdJxDxhH-ffrpLEEsVRKlweAH3bujeVkUNGFTGZ1DkKbEPJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ترکیب‌های ساده آب را از دست ندهید؛ هر کدوم یک خاصیت شگفت‌انگیز
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/677790" target="_blank">📅 19:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677789">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAaoGPvvOCwqoN3Es1cZSMd8bOIFDuNEzmci3rV28OMPk8KzJAJoc_9Zh2EWZ5_A4IvAqP8UATPsK4XuIevjnJo0PrC8UwByw9FIFRpox_MnBXKE8I8FrEsXeCXtTcFJ1UHKtCNY4_jgTcoM6DXq5z0qBbdyS61P4twWqrXvpYAfGeUwIW3B5umUDs7DwOZvN-WYn7IDvXZkbCRR7YDCa7uWgxOx3UygL3u5ZkKqglGgVKXpsgdVpd4MLwtqIX_EpOKrLjcpskDQ-E7wzvHNgyqQQPrHNaLUNZ5BWRfbphYsq1kms8-qC1dm1leCj40FsqISioibAQyQpZskW__4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
قبل از شروع سفر اربعین، یادمان باشد که ما فقط مهمان نیستیم؛ باید در کنار برادران عراقیمان، مراقب این مسیر هم باشیم
▫️
یکی از همین کارهای ساده، برداشتن آب به اندازه نیاز است تا چیزی هدر نرود و سهم دیگران هم حفظ شود.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/677789" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677787">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxGfYKWRTBCl-LOoG-Lsqfzw8GCUj-spUb-FzlqRdKGCS_efKJfQ5tzJPCM_0zaG8RC_00LJk-b2_0Pdgxl_drIwsHBvHOu0gl_DjBV5qU6CNLD77l9TF-aQpIR_AEys5rtkZvoUTbExa0iYoN_Lnhz7LAyChGYRJQfjlPQJhzs5UEzHC58XnZdWoAFiS7r3mPRq7t9jZmKyrPtmgcrFH-XwDq2SfwVYlE5x07Cq-owgWxIcrUwI3Rq8fI3UwpkcJfj0x-9vnQz2WFIIYqI_87DUO6CQbnszi8gUZmbnmgG7Lp4-8j_uQ7KJPgRCORxdocMT-aS2AyAUXRxn46JAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواسته
امارات از ترامپ: به ایران سخت بگیر
ادعای وال استریت‌ژورنال:
🔹
رئیس جمهور ترامپ، حمله برنامه‌ریزی شده به ایران را لغو کرد، پس از آنکه نمایندگان مذاکره‌کننده ایرانی (عراقچی) به پیشنهاد جدیدی از سوی قطر مبنی بر باز شدن تنگه هرمز پاسخ مثبت دادند. مشخص نیست که آیا توافق نهایی بر سر این پیشنهاد حاصل خواهد شد یا خیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/677787" target="_blank">📅 19:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677785">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjcaECL7uBOxMC_HwLCERdIdg-swZL1NRodGHgBcf2Fq55T3Xc5ZqwiOsD3WVxLQTXYWG9sNJLMcQIsCXfpvLOPQxceu7SnOj8pf45AqhI5100fxm2nMenK4SN-3txXXjt2KZWVg8mD7a-EFuAEO-AXbsY7LJEpJZ30H1JncUV3h05kTxkmCAgcgCsVRjdT0b8-JYoh9Q1YUP6Y5j4HCIMtZIXb6bt1eChOTBLAQ6txoFTMPHXIakuNhGGom3OpVZse0bvHRRIculKOT1dnFDuAccxIulOk0Zj02AzEChbA3RxzfBLUcFc2OJY2KnXO5pep3VfW-lWzhvvtjlhEG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال درباره یک دیپلمات ایرانی: مقامات ایرانی از ضعف سیاسی ترامپ آگاه هستند و در صورت لزوم به دنبال سوء استفاده از او هستند
🔹
اگر تلاش‌های دیپلماتیک با شکست مواجه شود، سپاه پاسداران ایران در نظر دارد حتی اگر ایالات متحده حمله ای را انجام ندهد، حملات پیشگیرانه را انجام دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/677785" target="_blank">📅 19:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677784">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e0f1758b.mp4?token=Ckpy5cf_iI7TFId4vxGHt_RaFhEonA3l2P2Fb0kIan6A6j5JMpVHP6sbQ7JUc4Y-qlGxtEIemOYO9VhTfdQhJR4gl46EojV_At3J0gT_Mw2TW3_xdGHN4RDg6vqIknv7DhoWoJSIJhw-X971FjLNsPvfIlMSz55nKxOQVL5Dnps4qcKik9CuGOU_HF276A-Ly7G4o-zBhKbJnR6hxJy4UHaA7AYDXsflnZe-p_TgQAHkmmeZWd6EjiQxucx8R7mNeBr3aGmAtI_U-NL1SnqDLm2NPL6pUKcV1RKA7fqWaOvmElkNG9QAcDW77fxzcp2HtWjH1xXxtM4W-NQG_tR3-yJkKtrRJRuxK0pQX9pc1bGQuqxiwdlutf90s6rfkT1_cc-h1s3hXKoFrp1FB1U8uEoCFUDXfHMzOGBbL2h7jbg3fNME88Anz3IEERMzbaPV56tBWMC0G11LqJmJyJf8qI3Nb1O-_9-Y1zb9gk-4hSrN67xEHPbNg190F5WubJl_-BI_iTpX1XjaiIM-u0acHebxSzdLVM2zR6Fq3sL-DKK_UClILngjONWa6AezPKFYJ3lhF7d6rcTAp-A_kClsOxphjNzHKFlQzspy_oqG-3KmJAur6aW6O0x0LtPsQjXQBtDJsIb1D9ZjF-sAgPEi86jO_BpF_pTPIaIehi5Q6Is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e0f1758b.mp4?token=Ckpy5cf_iI7TFId4vxGHt_RaFhEonA3l2P2Fb0kIan6A6j5JMpVHP6sbQ7JUc4Y-qlGxtEIemOYO9VhTfdQhJR4gl46EojV_At3J0gT_Mw2TW3_xdGHN4RDg6vqIknv7DhoWoJSIJhw-X971FjLNsPvfIlMSz55nKxOQVL5Dnps4qcKik9CuGOU_HF276A-Ly7G4o-zBhKbJnR6hxJy4UHaA7AYDXsflnZe-p_TgQAHkmmeZWd6EjiQxucx8R7mNeBr3aGmAtI_U-NL1SnqDLm2NPL6pUKcV1RKA7fqWaOvmElkNG9QAcDW77fxzcp2HtWjH1xXxtM4W-NQG_tR3-yJkKtrRJRuxK0pQX9pc1bGQuqxiwdlutf90s6rfkT1_cc-h1s3hXKoFrp1FB1U8uEoCFUDXfHMzOGBbL2h7jbg3fNME88Anz3IEERMzbaPV56tBWMC0G11LqJmJyJf8qI3Nb1O-_9-Y1zb9gk-4hSrN67xEHPbNg190F5WubJl_-BI_iTpX1XjaiIM-u0acHebxSzdLVM2zR6Fq3sL-DKK_UClILngjONWa6AezPKFYJ3lhF7d6rcTAp-A_kClsOxphjNzHKFlQzspy_oqG-3KmJAur6aW6O0x0LtPsQjXQBtDJsIb1D9ZjF-sAgPEi86jO_BpF_pTPIaIehi5Q6Is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: برخی نمایندگان بعد از دوره نمایندگی نیاز به کمک مالی داشتند و برای آن‌ها زکات جمع می‌کردم/ ۱۰ درصد از نمایندگان پس از دوران مجلس، بار و بنه خود را می‌بندند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
یک زمانی در مجلس می‌گفتند اساتید دانشگاه دو تابعیتی نیایند که این ظلم عظیمی است. هفت دوره مجلس بودم و حدود ۱۲۰۰ نماینده را دیده‌ام.
🔹
۱۵ تا ۲۰ درصد از این ۱۲۰۰ نماینده از نظر معیشت خانوادگی وضعشان بدتر از زمانی شد که نماینده بودند. نماینده مجلس روز هفتم خرداد که رای نیاورد، همه امکانات برایش قطع می‌شود. ۶۰ تا ۷۰ درصد نمایندگان همان‌گونه که آمده بودند، همان‌گونه هم بیرون رفتند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/677784" target="_blank">📅 19:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-pSS-aCdegKtdYa_BuyAr8UchWxMGfo0jiULz_WE_bttzbi9dMCpi_vykYg7b7-5Tw2rcxu3m3Ub7ccC6RDxxgBNr4Y9CiuSMjJGByHyX1RTwP2j1fJcKfN5nmxEcp9xMn7fyvQDTlnf1SnQmeSeI2xndSILwNQe1mVRFZu_0BQMZyJfWRnXb0ZxwQj-ZFH19X1qzM1e325oUk0UkEy4ihZVO3H1EBhXHX80Jy_ah3czoAftiU4pbxJeXrIXMDMs2_EoaTPtgSF91Gf19l8DjXBxew_fAZPAYV9Xx8OSuoqDlSqeOrkTYhcblr78vjknwHQjYFk_WnqqQ1ZqyK_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با کمترین تولد ۷۰ سال اخیر؛ ۸۹۲ هزار تولد در سال ۱۴۰۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/677781" target="_blank">📅 19:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677780">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند
🔹
سهمیه ۶۰ لیتری بنزین ۱۵۰۰ تومانی برقرار است و سهمیه بنزین ۳۰۰۰ تومانی نیز ۵۰ لیتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/677780" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZi7-0r28v8mPO_JErL01R80STkwTRC4_Srg0-RUkVicBRUuWWrpxG3awr2CB69EbispI-QB-KKPZS1D7LRgqu-fu-iujT9YlKI1CZuCfTUAU21oFEDM3FIO5pY5X5elF2AF9DPznGwoyhAAU0qiL0wNsP079MqL9tey_Ka2U-rkgDNV_3OhF1fEpaVHAZ7dvIlHsrxygPX6Q6EDhRvpe80q4Q5N2j7EDL8UBWkbz_annPPv_DuQawVhcrusQK8Cb2Tvjjx2S8GPblYqQEQ0wQNPWy0Zeg7pzbILDNmWfBulVGCZnMI4WXFuzcw2VVyjh0f1Wi2ARqaXzXcFjdYg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تکذیب خبر نادرست درباره حساب‌های مشتریان بانک صادرات ایران/ تمامی خدمات حضوری و غیرحضوری پایدار است
🔹
بانک صادرات ایران خبر نادرست منتشرشده در برخی رسانه‌ها درباره حساب‌های مشتریان را تکذیب کرد و نسبت به تداوم خدمت‌رسانی در همه بسترهای حضوری و غیرحضوری اطمینان خاطر داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/677775" target="_blank">📅 18:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپانیا خواستار نشست فوری اتحادیه اروپا شد
🔹
پدرو سانچز پس از ورود ده‌ها هزار مهاجر از مراکش به منطقه خودمختار سئوتا، از برخی کشورهای عضو اتحادیه اروپا به دلیل درخواست برای تعلیق اسپانیا از حوزه شنگن به‌شدت انتقاد کرد و خواستار برگزاری فوری نشست وزیران کشور…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/677774" target="_blank">📅 18:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هولناک از پاکستان
🔹
حمله انتحاری در شمال این کشور دست‌کم ۷ کشته برجا گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/677773" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_YipcA89-9ZCFlVn2JfdxL2RbJH-p5tpsgGggYu4kHEUk0l7pXRCYCMbZaIwHRxtE0PjCLTCbacrjMMOxPar-7TrO4EbAcqjBMKhzLpiStoKnDSoqj98RuHkRMQKQURSby5sycMYcIPJNeeB25Ua_KfLxWT2Lcot5j7gYsU_JMOs5GJVWaSkVPDieWEs2pzS7Y6Wv0bS4OO45MMQ1z80MM2D126hfuu-V_9jxWWXAd4A7XseQCPwQUhlHWVdeNVXzgQ0y5AtGAyijZdSF_qm4eUsk4NLar04myqws0S2qAEUaQIDM2-FJrBvM03aLPmvy5D0Ne_9Fxl8dmfyvMjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناسب ترین نوشیدنی برای لاغری کدوم نوشیدنیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/677771" target="_blank">📅 18:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gijEyoFLDGHeX-_u6lyliNK0KxtKOL9ktbGuF9_vQCyzj6HogD38GyvmcRdRA2lZGzFVfxgS7JenMI_OXnsaxm3p6rMDVENdKttO5WSR93gBJZcxfgCo0hYGp1DlsZlFA2JXv-gh5g2yYLtiahUdjeFeL5I3PYqYA3oMUWCvuH1n8Rz3Qyc5HTgWV4vQlG0w_q1ueDZx67yjk8QHJbdCIClJeU3HL_1AtySAC51iOFO9T1hOzeOxn0l4huGzMReRYQeqUJtDKxYw8OS3C62fx3ANoXR3ZKoNQ0QHSGsPs_d-B4iFdtOmXB18Gejre7--nDn35YPnqylZkK1F8neDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚪
🦟
پرده توری آهن‌ربایی با قیمت اقتصادی
❗️
پرداخت درب منزل
❗️
✅
جلوگیری از ورود حشرات مزاحم
✅
عبور جریان هوا و خنک‌تر شدن منزل
✅
نصب آسان، بدون نیاز به جدا کردن در
✅
مناسب درب منزل، باغ، تالار و…
🔄
گارانتی تعویض و برگشت
🚀
عجله کن! لینک خرید اینجاست
👇
http://khabarfouritel.affdn.com/lead/45272
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
http://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/677770" target="_blank">📅 18:15 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
