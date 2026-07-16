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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 170K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 09:44:46</div>
<hr>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYp0b4gh2gqoRfL4EZJ4w83Wo6HR2FSR6N_CWh93-_x0xmKCjvCLGNkRRbCNPGp9l4_-RBU8v654nIZbKtg3Wj8khi_HbEIJTVNyO7D6Gujjl7ob3jAhXZTVuCCK7QXTBRyYJydz-VftSUzp-vWEO5la7FhlTFHDYYOFVUQPKW0mhvO-cL_PLxbuNDpHnSZMg_nePjojVXYhLLeZ2Gdu1Li7Hos9VQgcgYmEwmPsQWfX9uGz_pxsXh3kNx22gQlEclPrOtYaVbnD8BUEbzwk8XRR_bO-YQDAobLcTlWCN-H6aeCxMvZEvy6NFFPvYLHnO9Yfx_3MuQiv30ylMQZl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh2c7CiExExDZH_6VF5C6tdVG9rMUcQGnyFGy0YG7fkVv3rn24zEBONEuOkVky__U2AwTVIl1V61XIi8mVoThO6LluGLhJ1_4gJmhR3v_I5fxTpXnEpIPNLcP9cOOjNzPoQyGVWIp7eU-3_x8m0hUUMY-H4QgroNE9B4eCmaYDS0EZw8QJI68S7Fad7iCMpkYM0MtQrAk-ekT4BQbhKGipAWZL8jx4YhG9ts85QvYURc-ny17Yig0amG5SznsBvdh1IoObbxCkjpseh2ytTZiQ9eXJV7pPMRNvE6YvpXC2lGT38tjBPnb7Aj-5LITqBLdIy8YkKIKXtM7dHMGB9LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aci8UzDiFtULbTKoiiPmNABF4E7oT1bYeFeHu5xYqiVw4LJPP2wLWEigl66C5kd_5qTCQfRIqF1uz3UR3wDlU0vtm9J7_bABcbMYqQF9l01oCvBtodrTD95asWZTpwJQq6ZrbSGfmWSzOtfW9kFgiFKZLg3-JVtN_AuqURNh8T5WAz-EbL0knrnwuCeErC4DQiByKAMh7vVBdGWr_wgKdq2aj3wJTIa3lKWtmfodE87p2-2GRc5OIhn3KG_LOFftsgzsgLGySd_cbQMlkfbjS0eNKHyteMOaqgAytJ479LsYQOmfJ0fxR5N0AYfi0z9hhOaXe7xRY3eYvnm7gqSWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiZrourKo8VTzQNd10XtY2wz1mVW1tuTmzH8YP9PiLABLBJ-ap_5H9F6WwAQgVL4Y___uPq57exGqIw3dzUZh6CsblSNrqJPOV09VIHDgns9l3CtGq7-7Fx9eDV9NDmXtL1Fa0mDlI9h6MnUhnc4YGnkQFxwL7SZGL9j7VcfnfMKjSDjgg1CGMLIcehLdc6VmkMGXhxlHzpOBH-73M7tp8_trj8ti3q6HlTfXziBkGYVQy7Eo-D0Yq3069M278MxZKDUo3L48CbFQNaJCMKkgCkZiWjX5sYy1_d-1yCvikpDU0GYZqKLRqyITq_IGYvWt-dTz12NbmrycoVsBMsNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEQYYWgOAdUAGDHWSJyG01ge7Ol6bl7MfCiPCiPtdm9IRq1x4uMQKXyhOHX8-H_gqyXI-2HUfQ7d2yvPhHO8Okx1WA-_hquLua6zyzlF7Iu1dFRKDQjcj8yFURBp9P05JgQvPPOk-FRpMz8Kw675ExoBDcbPodma0N_rGg_ELnFbX1MTfWm5dR35BHRe4N1G3trohBFhNHT6zLkEaoQ-c2i6rJpKpuZ-j7ZIaBTsSMl_QWmN_RybHlKPp5uW3z6Mr3xSvpP27gSjVLhpmtH9CtbHy3SUodullvtYbprnrONP2WF6PiVsCuL8aVW9aZoSnx_P9Pq4X251B4p43JGuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=NQb5nXcYcdHo7BwXCl8Go8t4FzaYiaiyT-rmuX2YTXsxvW2zW8TZBT5yw-YGAoH7nSIuoLpRqX_vcXs_aky7i2Hz1fCgtpAvKLvv_WeTQt4yAbJ8EBqPT9577cGPStyZjHAkI9xyEM0rrtTTJv0-Hw_awbk7giHa_ipasADeTed27i-bpg77IdKX7sK5LYoNSaa7JeE5FFyiNSrXrCqe9a5nogz8Nww1VkA5RAVHLwabw7hWB38OeYSfhDjvN2E97lwrt1z-YB9uyjgiFxqOjH3rYwwxy5t6SCzPPIYoH3fO-FRe94yFP82uKXqNEXfjF6XsH8mKj_FQSy6JXhT_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=BXYefYgXFBdFDIZqjlYtTx-7tTU1rKgQktPF2Jh4XL6errEDECK2LgR60Ju3uNZFp53gk0dgoQXICGc2aaF7enSVEe8ZdB-r4sAwsBSB6vTbgm7Cvq1EQyAK5creTCaLmuyX4VmI7jiM0jtdJkZ23RIn8zlwI_sO32JumG6VrbnBN7eSr03QN3GMKoXVTHGDUrH_XfPh3ZzAsnMWJfFjqmP6f6w48tOQM0-FI6qW4-IgE7GfAlmFVP3g749nlAxoUtaLGOOe-nOzmI1XzTVb-ZDnREqnVfd2ijfNVauA_sW0GsHmsnPr_7fz_JAXzTh1Tdmq3pHXG4Exn0KZzWiiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuNlz9JoFGV16ojlrUBLMih6UUYa-igFsf2CLOyEB_0vmAxxyxrDzfCGpaUIyEhRc98Z_V2TXUWlGqHvyAteLTbrxG7Ue5RwCoXF8vwq_K9O-uooRcjoyfZw7Str2jr7RMUz_W8VTSRGJ1bGcBvbIC1_5R0Yb01y9IbYp5vTkqN5c1rWiWI6qZqrAgaNy6CSuDN7JA8TdzLnJ0urR78s3wVwsagLZlsjjgod3eSYeXb2jG1iWsRqaIlta-ABGjsz9oEQPzlUpbKpjk8FaHACKCeNusiChjp2slPdNSgdW1gVPcHaWtAfREmCBf7SNPoFwA8jVPyPkWbY3ODFo23LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=rCJKkm2wbCx4A1_dS0hPZVqUU1u5ae5vdJTaC7abFQW6pL8vu0Kcl-Iv8VYQ9zupYfHcc8oRsaVMstNiUzt2h2OaQ_4B6IiOvx4lYzJzeu1IwmTikNSov-_qCmOL0-cVEA4KKi5GZ99TSrh8HGdgZMq-_WptOETtDRhMPwJndw9dyz9VEEvYtJDA_Q8uOG56-1fVVUu6eZEzLPt3v5v3ZQrE4VQ46AC2XlDBoDTDce4eeN3HCo7hqXxLLa0Z8IicO_wsVOcX1lOQlZqLYJLhXZ5CpgWwtiU0FO8vPCZx8yjsA5HVGdhwEU1QBapmI5kYqTPlGeJ5vY1EnBLp_7GTBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksqSjg8n6CLwx8xkpnWZjJCmU5GubEPqEj1Ko3iL3Beu8RYmte7Ll_5GrNsqT7peMC9hPqqUV6QGw1Z5Ld1sn0MARHfqoxIlKXWvMYf3NwwqoKbn6rHHTlTYqXgnaHM9DXDbe6cYXG_vpSOnArZZvTacXaW7wIcCkkBz4O_3e95KiKaT1vqOSZBiMklSDXfKZGoidPmyZ-jLuED6UNK55tD-5Sbe93eYGur7JdD_3oYlcxQMOlygwA_Ixj6g0xah3MGjt7QdsuO-rEG0A7X970ydgQMEdFwmGr5D9OEUne0vHWqvoPE2nzbDS_k1FU-_3Ot86Zak4nnpeZxBEhhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuqjLK28YVYM6vM0RB4Djuca9WFuWPiGND66o_k4ZmmdEz8K_5lAeudahkdKpHJiVKhuUMFwAJPc3N3ZjmPhhLrtaJpJUvf6OIfF47aGvhL-GcxF-o05oc-2Wg8jYWYMD8wSGS5UK4IuWARNQGJNL8Fy2JKfF21Wu2oKI5gw8SF35t2_Oy1iKayidqAi8rbOaiPInJYZAoP4cDIml6npmOg-RMtRkSCLu5EAcTlFEgN2B2SEuL2HODDCx5QW5cqaNis9TJqGTfmdNpGc6_8a_Uv0TxxpNNy6alCoAc7oDLarjMkCe4zR8aiD8o2KnCpHRWM3ozW4jQPInQ6vwMSQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPZSYaTN-Rh-BT-W3syor8mQL6dF9yZxmQu4uxzBt-6cqBuP0dLqz6gD_7FXcrlK9tehmqrEDviTDWuW890NKJpuY1Srn1UmFPuuCyjt8bxvpMSzJSi9bz6N0rjavtvtCEcvuidfJhLb9HSCGInRIApSYTHgDibVZ8oUMwCbuSxxQjDaRdgm0v9ZwCsCljqiYl0oyXPKg5KXeULQGWB3JZgqrweXaScRibVPtB_BmTS4j5Ix7VfDO7a_t5oWIS6qsaNkMoY3Mjc0R2qvWEdcPRlilwfN_VaDUOOpHEmspwSlvtbPOq2CzDyhn4SWsKpsdHi_EA47A8om4xX5rFwjfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsHPwBB_kuDSkjlJd_p66xhbw7CMyG0stg97canvOWGpx8c0TT6vxS7-nct6OHcy0q-A_3mhx5nRvZoYzRhYrB3zXOY7tE9j6nDnLDxUIx79Lcl49aV4okU4YohzV0d56ECCasM6EOOBRwZ3TQR18TfpNCrtARdnxHMX_nKw31MLpdznyBid08fpZNu07fvb_Die-u3_c8KVy1XU1sJepFPEjToCTugPUiyEFPEQhnKe5vrSu4L3N_OCOFpEf87jSqFpkgYiODOF6zdQWtCTRdFV9I-sxk5Szi_YV_yr2Mxif2zLCTIQx2ahVWeQ03RSW4Zqew6LmbKttMetkURigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKSPKEC6mZjbHdmghtj2F9263_Ng0Kc4REMPHto7kM0dherxA3ts_FjjWN0oewdfMQ4DftVpSUcLB29i24OjjBjn0vRwX7VjM1GW5UDQEhfUgHESJCrFMMqq_wIMjFZoKR3P1CNDM4iojQPac0J9TVuI3woUDojSfVXObeeEdT4L1C8tTLmxmH2pULiVlQRES3ysxDZuREpZX4OQg3jwPwl_W1McEMANEWO6gOTeiFU_Lwwo70aPS2ydPQTuZSMOSlyrebZPJmSTSdtsB1NI_Kg9TEUscO0ZlS9UxEDKpzjDuRnyF2nJsiPFfcFC6njqDQa78-o0TMcJCPwnG632NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DI9lqE4sA3BBcqZRWqexaweO4dvG_cz4uz1Q4AP9Q60osj_pBr05qOOKhy1ZTvV3oMIGKgXNvd6PH4NM64PlozWEphc6w7JS1mB9KgG8AxWhFY6lML7Zu8P1c5BMV_R9w_Zkpfi5tfP4J_YAlVoDx010R3MpV8N4Pq8fDzjz-H2tSeMuNQs2x6qQkiI2uAXqzWZJqjqee2DK3q2VqZ2ZcVaHLNT1XTj3DHk3Oo2k3T1_4AtT3-sWrtdeBvU6bKQaPmmVxuWiUJdDQ45wbA3nEzXklTruIN0kqZjA488eB6TWE9kYxpF4ziBvs-8SnfSuic4Kf6l8CfEnE7Yi1Hqp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z00EnNVGpO8_ixSR6Lb_Z4kv3lExtuCe56LCku0wRTiYMHNcLsVsQcAhOg9bSux9I2984oiRAs0FJ_e35pR9N6hfyIkfd-JJy1hkUfcI76a00I5pwlGcq21hAOehN5WDOCprwQ4TRQzCvklufR9y72bmets0bl8fyu_6RqwKRulEWfNHsMRwS-64AX_BY6yPd0XySkcaHy3PX9oSao2dulbZmyaKMPMH3VE8Un073FMVqrjy5mJblTmKb7WhySJGx9WP5TBd4cQYldyiENpTIH9ZysLC-w0fnfEjxugA-0yfpoFXzE0SOSwZmapnotz516yp57uvqM_eVql7081fYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=E62JRyOQEjmvsL5EzVRcmqlAmY76v3oiZ3CAOUCprVNJeWCDCVrdHDfEBuKNbiZVEVTdA5oNBNMfhCZUd6cSvGMgPaxfyG1ib93ll5TZTABd0qEIxR0rpciFuT-8Z-Aqjc1yvJmJWNOsJC-yyC5J3Wmd7YWtRWFnJhyo_BNE6Qvusm71emJdVJbSI3MB73hki0OcbZSZ9BsePu9fyva9VIHE5MkxNc6PmW27PTSPYvfQ4X4LTCekJ9HJ5fvmOCOAdEQW83LQ2fo44FuQXwzTM1POrV5XqS5CzZDlUFzSNmWinh-v3eRwVmB-0GjMfrR21vg7qW208wCX795CmYtu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzXVSI8rV2an8u2p_e0nxQD3mm5SZA3gv3gGvJ50C46K-w-ti2wkBq4AphtjAGSkUnDV5iX2pUEAOfkhSaItWLJ_tSq881Q4W6GAriEPxEPDzfNRyfZQRsF6zlFh5xt5KlmhnH4mJrezIkJtb_1AEIHXe4L-B7dwsVQuSf4mYS4C-6r0B8jhjBRrPvdO9CGhChbT_2SKTdYYWCziLzPwS5aPWAFNydCz1wGdVBuc-lFyeCXMS6V4lcnvSyreBPX1ATUILSWv2S52QeKMBItRPNl1eFgMf6YmXpdKy3jpGmishSJl1FWg1pqfVwaw-f3Q-ql4qt5vXmz04oiGpbiUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYCrAmTkgUZyGi5Df8cLRnwQgHnZiVXeFV7ADVfACje1fwlNjDXyp6RhbAdUnuqeCuVOR3G5PG4W5nfBtoWCdE6rtJqGaDdf9_68ci_HOCoFF_IpzclofBIcXAhEzWgxHBAjEwiUgRCgG5O_R2DCq-WxYlyK2MrTT2naGteQ7t_ZF8yqwtDly3dL0YnbzJz9LA3N6MbbxkAQ46Xm46E6y9a0Dn76srgnPcLIUhVAKQGZD_JTHdPvV0caXRC67Ag21UjPy72VGOAEUMptW9eDYUP3tiuMKfIKA6qxu3XNBPLcPYXgxC0KVNdnn5epAIzDqyIZ0iQxHnFqXWEVdXD4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=n5Z6jBbNa94sOqM_Bw2kPhVnHqEs1U2EP_qlIf6Jt7wNC9_vcoVJg2WP-N_W83p_lYLtxIu-G-yxvquV4ZZChraPtVJsikvVm-oZUHFwOzlH7MzZUm8S3vtJ8h9mX_bePdeuLZbqcxy_cwfqo2FpJpxT8JME7sMvQfJYgfU4Wt-snS__OFOZbTv2W60WO_0fzWImY4uJK2VtHFGUF7AEa7aN-NOFhyCwSRvJW0NK89kBGhj1Fys3QOpI83rgVooAx44POgM1QmZXowIhM9cM8C6DrQHCorBN4rW1OZnI67hoBCO5nI7EHbvvfRZ_iGKc3eQ2ky8jkyEVSKR8zp7Aig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=n5Z6jBbNa94sOqM_Bw2kPhVnHqEs1U2EP_qlIf6Jt7wNC9_vcoVJg2WP-N_W83p_lYLtxIu-G-yxvquV4ZZChraPtVJsikvVm-oZUHFwOzlH7MzZUm8S3vtJ8h9mX_bePdeuLZbqcxy_cwfqo2FpJpxT8JME7sMvQfJYgfU4Wt-snS__OFOZbTv2W60WO_0fzWImY4uJK2VtHFGUF7AEa7aN-NOFhyCwSRvJW0NK89kBGhj1Fys3QOpI83rgVooAx44POgM1QmZXowIhM9cM8C6DrQHCorBN4rW1OZnI67hoBCO5nI7EHbvvfRZ_iGKc3eQ2ky8jkyEVSKR8zp7Aig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBmHdT1mWNXgnrzQ9-BcGDcp6-sfFIARtYAmnkGKJ0r_qojDoS73y7F3Ws_iQ1KucCrkfr4OZX82QLYj6rN0H8OB7YORfFl1c6QY1PyymHbWSC_0ToN2RYahKUJBGbo3lYpJFEcUEaqbtePkiJwDDBqaiL4wU7sd6mBLjNBVbWXIMtXvQDuoV1izSWIS_pKOE6JeFfDWv7NbWU9NK__dLCAu-fy_hdcei6j9clRWUpblh4QRcG7O33vFNB11w8fLbDGFod13UbvBtITqwBtAKt-K0D0_gEICAGD91REazMH_8JX_0jNMNDHnoND3h_dusjG-eUa0BcejHOIczTzkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhgguWrWIrzR8su9UOBMAIH_snCmPxoUQgm0e7SsbNkWWtQLWHpRY4NvJZ3NLyJXln5Xrr_PbLxVcJE0ugb5i39mDlCX3bmJ4SQfdKWX-mSucHvVjUV3x-FDC51mj4w3Coy1xll1VacX0qz-TGROuePE44vGh70IrJuHYH9qYcD7E_aW1BnjUvOXiEB5bVzuqFBYndMeC_-r_tHdgJmEICp3ZG9LcpIANkd1e_WqQvVCjy9Tk5bu-6HPtBFHjkdkzr6-hpQZcLbiXmVo0JzvbWetjLSbsd5BCtgKdY34KLCAyUUrN0FcC-65hNmvk5GTLstc0m-i9nBwS0pAkpwXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isdTcsDuqpGDLh2BQLN931PwtY8B-xqAMZO-S9WbnpCrptip4p5IUVptXtkEFVX_bFQatHYSABYBZrfaZVOylpicgQnnBTJj5PxPqX52F21BbBGM-kmxpKGhD9DewY2oMFBYuMJXRTtYGkSbtxA1_dx4Iwbcf2KtCxAUhZXjdKHAQX0MZT1DnscKliM5RFK5WPsBMHA-NZy3CNYVcVtKYApoSxaB9Xo0oby9Tezw6XnUG6GNNH2bkPC4kHhHW6XlUyBEmkGrOF8t73kC4OFjtINV3-bds605qcWkjPAjrlEbqa7lwiZ1U3AaJ7nNxH1bBUkKaoJoOI5-4MA8gu7pwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAHCQcKxYsCa2hLPFY2C9MtDdamynSw7gGZSiNMtest6agTvjtAdZsTsFTqslqKG2NRflIWSZIa6o16DkJRimFA-wXVI9sNM5pJAAckK8HD1V41Yi3p6epIA7l3lorLT_sZilIKDKjXp78zC94QY2NtgMVr0305NAyM37WFJR_P6UqpjTV2My6Ik6pw3WIaX2IUNcSg6VeWOuhxnCbSsOwfnt2FhOuKAjerY0Zw6SwE3sH-Q9jVuyYWfKblER89rkL7TILYpsgD1BAk4-oaenxLxWpLdOdR6OeM7QtiCvo-CFwb2Jg-CxwE-Ds5JE0LgpuWO7eqIlX9Awr4otn1pcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VZccJcbQzEvRvPo-RnVood_zouryF6_QOkFfUZgI79yrY5P9Cp87GmjawQXzKlNV-L9NbbC1bWeFnh914phTqCkR-BPLFUOVFHeQ-mX--8x24tjc_QJXqYmwQ23K9ateibaKyDTrMM2m6qJYXONh1TysuyhwJnFXjKsQuPdE39kb0QQHqpiKixvi4AHs8Vp46WwgjqQ-8-2QuR0Ked74yOUpxvqJNenOpTvsgR6dt95Q-po3hZ-2a_6N8i0hGvU4h7KJUFNSd796_zS-tumQ6h3athxtgLDYArX0uMza7ie-pmEqiq6AYTBOZCxI6oi2sVLaZY6adaphT3G0tgAeIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=VZccJcbQzEvRvPo-RnVood_zouryF6_QOkFfUZgI79yrY5P9Cp87GmjawQXzKlNV-L9NbbC1bWeFnh914phTqCkR-BPLFUOVFHeQ-mX--8x24tjc_QJXqYmwQ23K9ateibaKyDTrMM2m6qJYXONh1TysuyhwJnFXjKsQuPdE39kb0QQHqpiKixvi4AHs8Vp46WwgjqQ-8-2QuR0Ked74yOUpxvqJNenOpTvsgR6dt95Q-po3hZ-2a_6N8i0hGvU4h7KJUFNSd796_zS-tumQ6h3athxtgLDYArX0uMza7ie-pmEqiq6AYTBOZCxI6oi2sVLaZY6adaphT3G0tgAeIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=DpzXG9fSPHjbKMarewUmD2_wURkqiJOo_gxZxNriGB3KtWUGtrz3uXtiF6E42AEqaZatdEF_-uW4wy9E4Fna6qH6R7r-2GM6M_7bJ4tfY1cZ4szLgu0RdpwieA3jE8khJoxp1CP2FhogMI0mrPaSLSMS8rwV7fOkiXzCcf-FyXIgvsTWgm2NXogwHFNRqcPA21RT87A5pY28QdjTzkA4a3T6Ee8IhwF0qKjF7nDhppZZUCYezlf57TLQ8kqsOKV0gjTkZiIL7Dhf11xn8zA5ozbkw5lPT2MikeBkYH_5Z9rogUhItYohmwJL_lv669lIeVildXWH9mwAlyMBcajBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=FHV4uHPyb9hyQUy8lxI_e28ux2KF4BgC8v7j24Gm-GoQYYjg91ZukTddbl4FVionr_L-bDTsYy15W6Hz2xMTD45jt-d_ntotZR--m7sws_Ysa28DUovbQ5C-31nU5BNA9gvxen6Qttm6J_A6ySo0Npfsh44Rbhhk98vXoGQO_CQWm6x5UTzB1_43Ue35zLO08CgJqoLlS9CGFUp7yQQqWz1KKzom3_rN-h5YN1pXVqnh1MM8qYql1HpNRSE10QJgCBj6tlUB-5HwgekHERbz-aO4-SzM4l0FRQoNZl6jGRlmWuImxzhTCm7bnUghm5R1HdkErGuVi5mB4uSFAoCSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=FHV4uHPyb9hyQUy8lxI_e28ux2KF4BgC8v7j24Gm-GoQYYjg91ZukTddbl4FVionr_L-bDTsYy15W6Hz2xMTD45jt-d_ntotZR--m7sws_Ysa28DUovbQ5C-31nU5BNA9gvxen6Qttm6J_A6ySo0Npfsh44Rbhhk98vXoGQO_CQWm6x5UTzB1_43Ue35zLO08CgJqoLlS9CGFUp7yQQqWz1KKzom3_rN-h5YN1pXVqnh1MM8qYql1HpNRSE10QJgCBj6tlUB-5HwgekHERbz-aO4-SzM4l0FRQoNZl6jGRlmWuImxzhTCm7bnUghm5R1HdkErGuVi5mB4uSFAoCSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRUPNB3ujGIEdsX8QlK8kycO__d1TD7Vu4eeZjrr5HL78wc3bjJvMjmNYOUP8-5St-ieF3McBQqjSK_I55OCTThfH-L5VihQZU4-70RiRN43H-o80UsitU9Ct4KtRBTvxOVxWTqMZaCK5oDzwXBjhdlXX1cBo96DfPZ9cU2hQG3dLk7Li_HKwMwYCmbrYgPbzJbdaddWYqtkZ_fgb1ZYpweAIwQ7GUdvZKTLNxpNCYGGGAcyYmFIdAwoBPC2JrtXgepb5ziSX1MbF-ArAWoYqoXzpWx_v5pRWMFzZYuq3c9Adhzk36GOp_L_GtU7Y0L3W0pF1hql75C5fwdWprPmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=IsWyvkPZ7HFi3A0QOqmMna2jvczoN2Oso9rNX001upHcgIvnj0dumrRTjDNBf0UqqeDCb9nHGJ-V27FaxMWXa2R8YxrVpbdjdvzRHTCRyKASb-_bkvwW9mrVm4xj1KMRVldTcIr3WCCcL494KURUrqoF_W4N4jzraKrXxGwKHq6X2gSTQuqS_rmWBbnhVc38SgUmQAQcDo4mFbDxuDJYs0F_WmK4zA7J-1AKlxAEaIhfooM79JkRlQA4ZQlQR1-ioqjW7n0PJINtOr8ZoIgc1LwRhwAlu100K1EebxQx6AwoyMfFEwoSLRt-CuS7KZnEQMArL5XN81r8Wxap7C_XVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=IsWyvkPZ7HFi3A0QOqmMna2jvczoN2Oso9rNX001upHcgIvnj0dumrRTjDNBf0UqqeDCb9nHGJ-V27FaxMWXa2R8YxrVpbdjdvzRHTCRyKASb-_bkvwW9mrVm4xj1KMRVldTcIr3WCCcL494KURUrqoF_W4N4jzraKrXxGwKHq6X2gSTQuqS_rmWBbnhVc38SgUmQAQcDo4mFbDxuDJYs0F_WmK4zA7J-1AKlxAEaIhfooM79JkRlQA4ZQlQR1-ioqjW7n0PJINtOr8ZoIgc1LwRhwAlu100K1EebxQx6AwoyMfFEwoSLRt-CuS7KZnEQMArL5XN81r8Wxap7C_XVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=W3fwyUV1m38JjQGuRN8Sdu6cIz4PmBNLm5JgOOOV06-4bHypoDf1pgIAjx60wS3AXpA5Lfc_7LLTV2dWqwOHuAMhdm_FgTMMRB_hoel1ijpsIRoK189vpl2KdWHE3Fn3m_w_5bG6Gut6f_rp-fAb1bBg3s02HoG6T6gAWiX5HzQ3EInaFyCzvTOAv7nJ0PAzpEF-xsLXO5sA3tKwUTbMYJM6CdXfE9OXGr8nHSrdKnhbLD2MgMZVUwwRXEPl97g96E7rFuv0jT3fZx7DdYyuPHQGqQwXFHSCip6MfHcJv7UiNpWVzCoDh637_gNzaEMqNNsbcN7OvXqHEHrzb92TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=W3fwyUV1m38JjQGuRN8Sdu6cIz4PmBNLm5JgOOOV06-4bHypoDf1pgIAjx60wS3AXpA5Lfc_7LLTV2dWqwOHuAMhdm_FgTMMRB_hoel1ijpsIRoK189vpl2KdWHE3Fn3m_w_5bG6Gut6f_rp-fAb1bBg3s02HoG6T6gAWiX5HzQ3EInaFyCzvTOAv7nJ0PAzpEF-xsLXO5sA3tKwUTbMYJM6CdXfE9OXGr8nHSrdKnhbLD2MgMZVUwwRXEPl97g96E7rFuv0jT3fZx7DdYyuPHQGqQwXFHSCip6MfHcJv7UiNpWVzCoDh637_gNzaEMqNNsbcN7OvXqHEHrzb92TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=KHWhQHr9baqyJdQf-64moa7UsewaCW79YNKaCyiJkDlaxv-PygDVzt0D5wfw12DyvUQOBDKkwp6gjjywIXJOMA8CrhFehsWaZ3oooU2EPTpfJ_LplqxQPSH36KKr3SYQVjzDYGUVSvy9_IyoxLqM7QnKNnLTsMzqLOhgTRD0drStJKN0k8hKN4Ruj9ex08X7fPMuIX-x2eIbc41P2gote38AyUq_RNzhU7-v-6f1jk4tTRbaSGep0Q2yacuVAggt_OIPwAmoa5z4uU1JDy5NyXECC_WkSWOp5oMUlVjv_fMeazeaahZ3YA7kjdNsT_xx_j47lXa-HokD6yofENWewQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=KHWhQHr9baqyJdQf-64moa7UsewaCW79YNKaCyiJkDlaxv-PygDVzt0D5wfw12DyvUQOBDKkwp6gjjywIXJOMA8CrhFehsWaZ3oooU2EPTpfJ_LplqxQPSH36KKr3SYQVjzDYGUVSvy9_IyoxLqM7QnKNnLTsMzqLOhgTRD0drStJKN0k8hKN4Ruj9ex08X7fPMuIX-x2eIbc41P2gote38AyUq_RNzhU7-v-6f1jk4tTRbaSGep0Q2yacuVAggt_OIPwAmoa5z4uU1JDy5NyXECC_WkSWOp5oMUlVjv_fMeazeaahZ3YA7kjdNsT_xx_j47lXa-HokD6yofENWewQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9U_oAPDcSDV1FjtcxBURg4-oJAr3ovbDFjNvqSy2tTOLR4m8OX3QtU4hpKFvpo-pdtce7i5nj5X9dUa53K6rMpNIsVJV8ra2Kne_sedwT-NIvBeipgncOsgzNFcsIV9BG6yzlfEJpr_C22s7h2Bjbll8f8SmzhKReiHBU2hHwewQlB_xXr-kEGSG1JDNrKfxpFAWn1R0P7t4aZ8Yc2d2dl7Ui71ZPgzWO0LDtnaoXN8rLapxE1mtoc9JSvpcig2OA4NfOdb-hP9osrYFj9wTK1gOsESaHO7btqKb2WWLXc-4IMPgsEcQwnW-Z239uXEsoczqNqbtzbLT9WfrfQeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCXTV_dHeWO3p8VztzBBqQ90B7WtItljN87smxtHtDH6mRFepDxx95r0LkQgdjECys3lpH9b3JgJSYFGOS4mO5Mw5ao269Chot7XhW69_TQJdSXyTwJOU-0rvH344nVXr1SorNVMsoUeyKnRK8exUdNuzNBI6WHy10oVMsfozBmTSVDCVyoC7i9LU1YE0Gxix5-2H5IqPhn3baW56HcJAWGX4uZ7w_9yVZOUBsisMcIiclP7OU5-8pJqNi2E1kIJnzu3WDMM81So9q5mZDY_hY0M_eb4AZYC0_SC0MXxFl5WZm5zHYibhT66QM3UxLCzCWcIrhJ3C-mNfXB7tI73EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZaACSUzUPRYjRPFCs0eGm6Prc6i6ZYgxVWbaszEGsu10jwGNz4JQ8MSJ7PIIsLKZSEQBP39hjDQVRLSoWJ9zFkbLheGBYE-0h7BMl6KFlPFxVhv8DmaA0yTPNQTcG-cB5XUJ4eajt5ErX7JuLiIjj1vctbqiSswoIPEaDC_Xof9hhcPqm24H-SM8UPUbjmC7LWsZhp4WMRjhprkuK8no9OoUyohbCxVkrVY2LWDWTEkx7JYMurQUPbxlI8Tn26OGXe5jrXH6CFVKMMbEKuSFJaX7_5a1px9y2LkeatNIeSY67K21xGC4v8qoT_RNgYOtMkeDe7aILT49oC-0lBeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=maPeV42QdGzAJgpTwE0nW36Yekeec2vgPtXvWLenRTtqjkrQew_G4UR5kir0-ldnrqnW5pbx_x21mNhLjGw91jl8UBYrd0VmmCZuilZVmm1sWMMx4unGK0m37080BxW-Gx5JRTpAqnb0L24UIykqEGD9WGa_WoLOhEjQv1yM4fq2oludMerP1WWMzLHd1t2gt3nxA0gmnF7tKVCZyr0zpVhTEiHsCJfePevju3jWLwGiCje5WgU8xJreqJJpK2-6L_XAXiafSSnnAu0KpyB7pn4nbvxEPbmwSl7Swcnw55txlwjmhnTu39WuFA0v-IqTYml1Qcm3o3D8fvbonQ3fHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=maPeV42QdGzAJgpTwE0nW36Yekeec2vgPtXvWLenRTtqjkrQew_G4UR5kir0-ldnrqnW5pbx_x21mNhLjGw91jl8UBYrd0VmmCZuilZVmm1sWMMx4unGK0m37080BxW-Gx5JRTpAqnb0L24UIykqEGD9WGa_WoLOhEjQv1yM4fq2oludMerP1WWMzLHd1t2gt3nxA0gmnF7tKVCZyr0zpVhTEiHsCJfePevju3jWLwGiCje5WgU8xJreqJJpK2-6L_XAXiafSSnnAu0KpyB7pn4nbvxEPbmwSl7Swcnw55txlwjmhnTu39WuFA0v-IqTYml1Qcm3o3D8fvbonQ3fHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLB15NNW-P78ePKUMx6ORKVWCLM6vM7NsgevswLYtCbdDL9rLWxLDmxjqGNdp2RjgEXQktPctA-O410K38Hvfxw0hL4ICiIUNuuqy39zOB4QmQcOvfV3m5opdC_-sD4gzmsJXdisyF0v_6Hgais1bDPZxHaNRTUUW1LmTz1y-KbdQ_SqPLXoHWamS36GUTN8SCX5Nxk0DYSv9E55bSpTYI9Oipn0GZ2S9weDE-QFKNlADZwOijKae6DZcdvJwmtfQsuh2ywwD5CqDSLFCLmRyBwj4J5qZFzwQ9m_M3GbzRkIgLWXqiODnmj6ZxqN3D77Vuk-cr1CMbGp70GfiaOnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuZW1bZvVDHoL59ROmaUzPI9kEB5jCvptFcggoyN9r8kQN7gb7L1N7B_TL49yBDGNR1H5MpIVvWmT95IaxlthqwQDbnSjWtdsDiSTYVecwqxbOnug04EFZdSIAbN3twKsVQyvG7fbmjt_HEWkRuV4bOwj7sH-97F36ghikQiTJCMn3AAaJaFZvE9Ko8nWdAiKErTdQJZgXv53aXkqx3EvCJ5tdwtvNSHyVwMRuQiDhpmN-9vk1_14gGoHEd6k44WrKPuJ-gud9HKEQf3201-lAtSj6N8gIIeEdz6Ey9D5P_SP6zxbFy88yHn9gwlzGCxZAvVfVzC7_NWzsHxC3kf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-5IP4lFqVPVpazXGn9SQZApmHobUpd8IpgDajE7cHZ6M3ZfxGPHQgVwQ-hepGojESChfXwH9TngGQRRZMJ5OffTQEWDwh1PuWNyeNLa2bOx-oBT_jIuNndsHOSSFCDwGcuCRADh9G0-wBbCd608xrrT0zKmmOgJn5I9w2IgHBOa-Wqi7t56iD8T_M5Wjw6S6LH3ECGrWBZLk4DQySkPB4IFX9gty9qlp0H1rGjoNDhZA3eY5eg_pxcYaECh6VjNBmhgBKiYE9naq8-AcdAuECwOrv6PmN82KAfEjqTjf4LjK3Jfa_sfd8FDqYtflXoAEUgl9ne7bCxRYfAQ3VbM1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=aeVGz586FabvajfHjmkh-TrjNmnQPoIv5wJ91fdjBWiUQoFHyXZ_CoIxsb2DrokDAhHr8I29cEOuVo1O6EBTx_XwmNVsbqgVe2ZWnoolM39VLATjzZjPZcPL8m-799u6ArjBX3nZRxVcOSoGIYOLcxp7Uaxri0KhS8-V0A1kp87B9PRuwh8ry_HqHz7KyXcUOA50p2WisCYWWS9twIuCe0rtB9WHoyrwunTEdA7eqNVpnGmsOBTf9pXawcqxOe86AvIxXV7YdNiQyjl_9KBSd2sbgx9AA9JCHNKDl7QiPD-dTes3MTPM2-G5VP9FcKET4if1APYZOJtf2IIyuWciCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=aeVGz586FabvajfHjmkh-TrjNmnQPoIv5wJ91fdjBWiUQoFHyXZ_CoIxsb2DrokDAhHr8I29cEOuVo1O6EBTx_XwmNVsbqgVe2ZWnoolM39VLATjzZjPZcPL8m-799u6ArjBX3nZRxVcOSoGIYOLcxp7Uaxri0KhS8-V0A1kp87B9PRuwh8ry_HqHz7KyXcUOA50p2WisCYWWS9twIuCe0rtB9WHoyrwunTEdA7eqNVpnGmsOBTf9pXawcqxOe86AvIxXV7YdNiQyjl_9KBSd2sbgx9AA9JCHNKDl7QiPD-dTes3MTPM2-G5VP9FcKET4if1APYZOJtf2IIyuWciCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEphPbXkOSu-HdK2VybnRFrUKLEimbO-Ehq3vA71jBir1-VBYAY28EPuB5NxS8KQPJqOcLPK4KZvmTXM9AE7YSLrbpe-yqraMRFZuchqYAyfzLAnmF-ZU60evqDM89VOxEPagjptNF6c93TK3E1RGj5jxie-BeEU_KO_4TwstSQZGxaZzz15HtNLjDw1m2mjK5pc4GSB7GjdOPUpD8u0xx-nX4V2MXm0NBeC2jAG8QnTataGBbpoaTCoMPnlpxDmUTJIJWM_dn4JM6GS0S8eUh0v402kf83S-KO1E1N5UY_HPJ7T_SGXxo1GZCoqGBP009_YniA0KL84hfdF5Wo_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8on9Iznv1uUbBADy7nU48ryLT_nxqA7y2lWqU0356Va_4sPScG_rE5LteKqFF_mSfoCWY_zMblehi9wOUfWbzbZPeXkY2mNGNlsmItKm8eWWqVXzheDpkfnYnT3nZkx7e1_AjiVbTt5_j6fT7QebzhNcfJv0wZX7uHVA3SxcjUl7MrYj4OzmG70tEfAgZnKoUEifH6tErYK4ZV1ChMEz06J1gVlnhd7J4vpDnKH1y8rDusclg-NzbVcWJbEyq1x9GKLzauOwQhBMxh3mUkVQ4Nx_LlbFtyAz-qZ8y-eJR-KHo5JUR6jwMTb7iAH7YDeVFuQ7gu9UTrp6aS8hLG_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT08uuZi6rfdSrbuVkG0v_s2GP_rzQOlIGMBu5FBY__S0A6WJKPrZwEPk-c65YTO1N6y9MFkcwnbcgEnki5UrxcFyUltfIl3Bvs6N6j8qTPtOwmG1JXdut2cc9po7Z6VPA1bXD0wgJzzm8652TKvS9iqsLP7vvIA5Ws1xpFzyj6HRKp9Drz9afYmdsc19CFCF5bCz1ia1XvI4mlrz6llCl4T5y937Wme3fa5InM0mtZj-IOEL2le9Nygezf6ZELR4rfSY3iE4Ze388w85cubfhhyCRd2ymOTfpclAmGQkaLgHtp2uACWY_bO_IF3ESinyA_Uhz9RlEEEIJ0uEzP9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=U1tt9etEvcfIWMiGs6Xu4AGZcntyEjhVmw4Bk7rI_c_VzRcECmKLXsU7z7dY6j2JWlRKn-ZMTeimekYYgrPjXwZmIeGppqariXFHs8eTCSbjISHmzkbqhiK_Dt6JhFyqH3a8gHkCQtDJtzts7LzGhSiXfn7UFj5Jrqduyhq-IQUVR4EX-0QvrC3qhy4oO5u6b-sdnQWyw1nMmp8INR1RrkTd0773MdbK8KZZEeQaiiJDn2OQ7-77nYt9LEdbZJtlcetru7UGeBOc6JX1x0LLX09Udl7FJbGnHfZGg0RTlQQPKHszgFDcd5ZOLCyEcpng3fWrxvHiar1NphZ2qxFFBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=U1tt9etEvcfIWMiGs6Xu4AGZcntyEjhVmw4Bk7rI_c_VzRcECmKLXsU7z7dY6j2JWlRKn-ZMTeimekYYgrPjXwZmIeGppqariXFHs8eTCSbjISHmzkbqhiK_Dt6JhFyqH3a8gHkCQtDJtzts7LzGhSiXfn7UFj5Jrqduyhq-IQUVR4EX-0QvrC3qhy4oO5u6b-sdnQWyw1nMmp8INR1RrkTd0773MdbK8KZZEeQaiiJDn2OQ7-77nYt9LEdbZJtlcetru7UGeBOc6JX1x0LLX09Udl7FJbGnHfZGg0RTlQQPKHszgFDcd5ZOLCyEcpng3fWrxvHiar1NphZ2qxFFBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAdm2LuoUZdYRLNVx9CshjUbHypKk5eehHJGp_TSRwbz-PYPe4fsAe1ZXuYu-JKWgSPviHx4f_ZoyZHMdnI5__QVmwuwwooyRyCRt8he4omU4p7A_rZ28t4IyLtJo3Ey8IWRA_tbmAx5reRSS4krbeHxNXv9CDh_sfJ3c4-ZyAUseANTFfbDCyh-l7F56bX8NU1DjM5fsj7TyrF7MxUFZBSKcUb2OEyweVzKcKw9pZMIdvvKCwmpaCeqjge6gGZNvtohHGQgIDkq_ogY9dyYfRNGfD4AqiJuJQgZuk3nURFMX2aECxOlXaOPf-r2dyU8CEplUUkvMY2UYMNQlE3Ljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=NivjYGPEulcZb7M9nEIh2WzAy4BiW7slJUxb2ZHVkjei2dBTTgDwZ04YsYjsrvH__NID_ipubJpDexAVI6mWzdQCdPbPBjuCzgSY199P4GfdXkbCpK5MD2JWVPb9K_TVkNXbZfe0EgyWg4Rd3KSE39E1Q4ODnhnU8XdfSsbwtPLpMzf0vVYb35fRv8QD4aQp242w3We_2Z6LYRUXLL5KzzRwOgRCMV-byLIU65GsvWfm79GfWPqJpeHmJLbyGdafDZFatJq-qVv27dnIZQaiIzgfsmUiYSwJ4wZHkmPB2ZbJqWKY4bAJD1jU4WU8jnCuBkuyrIon3EhZb29THou1Zww-U5HWAl9SkSB62IyXc7HpLEt5PPNNch1B3tjI6IFfcOW99R3wYdD9gQr8whj4Au97a1AhwmyT1Xfe7rnM5s4XPPP3fFhaxoBBky1IyPwck0UflXh4cNoBdIIIpR1XmZ4MTaqfBLZqbN6H1HNtAm-XEJaHFJ96pwq6a_4IjArScJsVtNpLcFVnHSBmS4-rMePJithyQfXmhrRH1eDlIrmOnRmVTs43afB-azPL1sgkaWn4bn2Y7EqVNgSHEJ7kKzpCBIFnDwmw8wNwt3Z4b6seaiWq9ahI9kTY10YYRnn11BTbDW_uQ4gwbnybipEggsBEPb_I9Y33eFpzn7jPAl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=NivjYGPEulcZb7M9nEIh2WzAy4BiW7slJUxb2ZHVkjei2dBTTgDwZ04YsYjsrvH__NID_ipubJpDexAVI6mWzdQCdPbPBjuCzgSY199P4GfdXkbCpK5MD2JWVPb9K_TVkNXbZfe0EgyWg4Rd3KSE39E1Q4ODnhnU8XdfSsbwtPLpMzf0vVYb35fRv8QD4aQp242w3We_2Z6LYRUXLL5KzzRwOgRCMV-byLIU65GsvWfm79GfWPqJpeHmJLbyGdafDZFatJq-qVv27dnIZQaiIzgfsmUiYSwJ4wZHkmPB2ZbJqWKY4bAJD1jU4WU8jnCuBkuyrIon3EhZb29THou1Zww-U5HWAl9SkSB62IyXc7HpLEt5PPNNch1B3tjI6IFfcOW99R3wYdD9gQr8whj4Au97a1AhwmyT1Xfe7rnM5s4XPPP3fFhaxoBBky1IyPwck0UflXh4cNoBdIIIpR1XmZ4MTaqfBLZqbN6H1HNtAm-XEJaHFJ96pwq6a_4IjArScJsVtNpLcFVnHSBmS4-rMePJithyQfXmhrRH1eDlIrmOnRmVTs43afB-azPL1sgkaWn4bn2Y7EqVNgSHEJ7kKzpCBIFnDwmw8wNwt3Z4b6seaiWq9ahI9kTY10YYRnn11BTbDW_uQ4gwbnybipEggsBEPb_I9Y33eFpzn7jPAl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=eIiQaMsZz9uzzDFLX8jJkvmwQCuogDZ8gq0hEqSaLvIJBuYT4rysL6MdApbJTn38UxpSvmCD8xrI4_8SWt2tUtv3gm9C7B7q5mQ08teGa7nllA7Jggu4P56U630dyracAdbxWvygEpldbPZMAlcRaUJ5vSy9t8o7YhlUuKT3TLo8CxDj5nyyMfaIdEKEtpmUjLVZ3ocQuA40btQVTb_HPm-HR0BTGYhBmWqiqRlGd0nk58YeFkW0PFrcaCM374BLgLm8lCeusq-vOLQLyIb-3743xHfYq9r-va_CeK2QqVBVkzC_pAcgy0diSZPa4vucjM5V6sRBA_OGlzFoDz-0IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=eIiQaMsZz9uzzDFLX8jJkvmwQCuogDZ8gq0hEqSaLvIJBuYT4rysL6MdApbJTn38UxpSvmCD8xrI4_8SWt2tUtv3gm9C7B7q5mQ08teGa7nllA7Jggu4P56U630dyracAdbxWvygEpldbPZMAlcRaUJ5vSy9t8o7YhlUuKT3TLo8CxDj5nyyMfaIdEKEtpmUjLVZ3ocQuA40btQVTb_HPm-HR0BTGYhBmWqiqRlGd0nk58YeFkW0PFrcaCM374BLgLm8lCeusq-vOLQLyIb-3743xHfYq9r-va_CeK2QqVBVkzC_pAcgy0diSZPa4vucjM5V6sRBA_OGlzFoDz-0IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIZDH8JqamWM4xkJi0b6xgBsOmTiqJkTLnkq-E-2k36eUAe9ILjpEffoadM5yAsaky_QAe8ASeSmnOoGhifItlMUXwA4TfXPb43y8tsnTzsTvV60bz42HN2xZUynNfMQuoBnokfn9swY3Svzn3DssUvTY2VWfLPj78MNRDAN1U7dDxB2cKorX12I1Xl-ZT0UQCy2i3EEAKS5Xasmxh-PQreTAWB15_MRCKPpQaG6eu_WrQ-bgh13wndshWtmmAhaoiSygAH5Zt4-5re7WWE8cCFurhXVT0y_iqDOACvGnkYgio9Ex0UL5h6IzSvc5QhdIAH45Ss0u-MsLJjGe061Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=p606xp8mcubSwWeWYC99IXtxGBQ_1y0mrFbzbCHMTwVfyWqndgnYJ56B-Zf2fDXMs8G25-qXDBILWTjZP8BA8v8LWwh085g9Psrt2RsHbjF7F8Cvwhsvmjm7DtybCeZbbWFxoAYvGIVfYMVpJ9ExBa1w73gy-bIIkniWmpOAz2eEqTS46pdZd2gw6fbTQa6kz6P5mWOr4mzPHtClgYERYT6VVp1JcSZ_eEvUXo0YrRTRfYJ8b9hKrbLoDAQ0mtqCQhIHInZtjI8pDZlOLDAL-UUX-uYF0dFqfGaNd1QkWKG4jWXB52EhypiNt8B-RkhLZFcxGUg3fbSUv_iYe2Gwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=p606xp8mcubSwWeWYC99IXtxGBQ_1y0mrFbzbCHMTwVfyWqndgnYJ56B-Zf2fDXMs8G25-qXDBILWTjZP8BA8v8LWwh085g9Psrt2RsHbjF7F8Cvwhsvmjm7DtybCeZbbWFxoAYvGIVfYMVpJ9ExBa1w73gy-bIIkniWmpOAz2eEqTS46pdZd2gw6fbTQa6kz6P5mWOr4mzPHtClgYERYT6VVp1JcSZ_eEvUXo0YrRTRfYJ8b9hKrbLoDAQ0mtqCQhIHInZtjI8pDZlOLDAL-UUX-uYF0dFqfGaNd1QkWKG4jWXB52EhypiNt8B-RkhLZFcxGUg3fbSUv_iYe2Gwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=sB_sqSkvJRqDaosi7CueCHYTG7tjLqO_SfUNu7u4Bf82Fp1BC04EfKvHYk5dbruWrbrvo8rSjDld_hivBzsbcqHI4tn1stesXPSHMLqAIX6OmDrV8Vk0GsJUEXxHJfHe-KO-dxXJ8qHOE_jwzTIefEvjaoSL9UUlS_F_xbjBot8cjQLNPcNb8_eKhG33n4cQVTJYV1Nh5OlAQhn0TA1d20iBSbkD4eHcvZ-w2UJXOAoeQbt9Jd0k3n-yWZzlvQjLLDB3HHhJJC_px4Xq8p7QkVl9uSCZzhRXnk7YLTwBTJStu87-xxQ60oS_GJIZQUMWRzazuMshLubhc6NijHPN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=sB_sqSkvJRqDaosi7CueCHYTG7tjLqO_SfUNu7u4Bf82Fp1BC04EfKvHYk5dbruWrbrvo8rSjDld_hivBzsbcqHI4tn1stesXPSHMLqAIX6OmDrV8Vk0GsJUEXxHJfHe-KO-dxXJ8qHOE_jwzTIefEvjaoSL9UUlS_F_xbjBot8cjQLNPcNb8_eKhG33n4cQVTJYV1Nh5OlAQhn0TA1d20iBSbkD4eHcvZ-w2UJXOAoeQbt9Jd0k3n-yWZzlvQjLLDB3HHhJJC_px4Xq8p7QkVl9uSCZzhRXnk7YLTwBTJStu87-xxQ60oS_GJIZQUMWRzazuMshLubhc6NijHPN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=i4mXGxKHO9JTzQCHLQBCygiEBPQ5XFV3igzkDuqFxtmbokIvBzq6sdQgNosCxdAiofYQIL96929_Mj1RHAaxPAysmUzLBwC5jx9rAPbloHfsKmWz_4tMf4XAMO0RSR4CHBd9eJbyKwBURPJ1EVgK_vLOpJggaHRPNMJxOddG4RLkhIDiPMlCFzbsKUSPfVM46l_JCS6m0iweyqCQEECCv53RSiLIAxkRgkOSfcvOA-rc_OTB2WpaFlUMCOdnDCq5sTRW_czH2Hk2QwjQskcYj3Tv8pQ9AUYxdl2IbJg9hNp7n-zCMLHh7bbOr5mYSGi0CqPTtgasdlwukqXJikrNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=i4mXGxKHO9JTzQCHLQBCygiEBPQ5XFV3igzkDuqFxtmbokIvBzq6sdQgNosCxdAiofYQIL96929_Mj1RHAaxPAysmUzLBwC5jx9rAPbloHfsKmWz_4tMf4XAMO0RSR4CHBd9eJbyKwBURPJ1EVgK_vLOpJggaHRPNMJxOddG4RLkhIDiPMlCFzbsKUSPfVM46l_JCS6m0iweyqCQEECCv53RSiLIAxkRgkOSfcvOA-rc_OTB2WpaFlUMCOdnDCq5sTRW_czH2Hk2QwjQskcYj3Tv8pQ9AUYxdl2IbJg9hNp7n-zCMLHh7bbOr5mYSGi0CqPTtgasdlwukqXJikrNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=oq05zri1BavxyrzpuA_IbHdZSLrui_qoQy-WjXWuvCs-MSFt9GzLHXfzoK59aBKC86xnZm0pj8p9e6JeVOWVyy8xFZ_z9B5Xt5kZqyHZ83yeZIHln5qHwbrJc4I-ctWYa8UXwEumLT82GYOaLpePD_Zu0ftzRWTMh1sy6ZoBmy0Q3z8g1xAtQWyXWdxUEDPIbpJKPIIH1Ca0DLDcjZ6B3iHyJdtM5xvY5CdIwY2XYtXqJWXSm_gVbfVHqmgJtncIScvWPy63mlpMFTkpLiNYcEpedeAnnF0lmmn8keGPVGiNafJrwyVuQ_OTCBlLXDhIU4bum8mDPJpYwnEyEo1OgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=oq05zri1BavxyrzpuA_IbHdZSLrui_qoQy-WjXWuvCs-MSFt9GzLHXfzoK59aBKC86xnZm0pj8p9e6JeVOWVyy8xFZ_z9B5Xt5kZqyHZ83yeZIHln5qHwbrJc4I-ctWYa8UXwEumLT82GYOaLpePD_Zu0ftzRWTMh1sy6ZoBmy0Q3z8g1xAtQWyXWdxUEDPIbpJKPIIH1Ca0DLDcjZ6B3iHyJdtM5xvY5CdIwY2XYtXqJWXSm_gVbfVHqmgJtncIScvWPy63mlpMFTkpLiNYcEpedeAnnF0lmmn8keGPVGiNafJrwyVuQ_OTCBlLXDhIU4bum8mDPJpYwnEyEo1OgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=NkK8cMolH57ljSSxl22NqaNbMUJuuxMsbSmJJ-cjrUld3yl0p1TY3Oivkp_BavPjZ-oAUFp0p0byVpe2VKuj8u0QgUbTBgcqVlL5MMSGHngjcxhAoRoGDS3amO6Z9SryHfnMFb_CmLqsilBBOz5I1SPcUwYEFIczC-74unrL3DaoPqq7LejGuZzXMUKRgLshywWDDhNvIOZkwnAoWOhSMkdXtMbg_JcUBN5v4SJF1aRho2w95p3tIMR6vL624TA19tL-wRt6T153WE_PlHbKhPVnVP1s7ch8DkCiTppFSbDIXvxS_gLe1gFKhEWFfLhrSBw-UyitQ8EVBF2aEg4wyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=NkK8cMolH57ljSSxl22NqaNbMUJuuxMsbSmJJ-cjrUld3yl0p1TY3Oivkp_BavPjZ-oAUFp0p0byVpe2VKuj8u0QgUbTBgcqVlL5MMSGHngjcxhAoRoGDS3amO6Z9SryHfnMFb_CmLqsilBBOz5I1SPcUwYEFIczC-74unrL3DaoPqq7LejGuZzXMUKRgLshywWDDhNvIOZkwnAoWOhSMkdXtMbg_JcUBN5v4SJF1aRho2w95p3tIMR6vL624TA19tL-wRt6T153WE_PlHbKhPVnVP1s7ch8DkCiTppFSbDIXvxS_gLe1gFKhEWFfLhrSBw-UyitQ8EVBF2aEg4wyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
