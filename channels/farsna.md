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
<img src="https://cdn4.telesco.pe/file/VWO0aYo5UMUIwy2PHfdffMSbs8YezV9vByp1BbOH-Ox3ECudvjb2TsMBQ57IqFKCW_z4b6zkQx9pSaIBwRKj83s7yEd2WzZuNfK0r6d_hZ0OnnMUlvZo5MbrfphaAPqnPj9e-bQAUSpzGDiFL-pLlg4y4zuilH87_Rw1wMohHqmD6ke0GxFlt7HYw0YtDhfRD0RhstgSMeF_GktDpSheJuHjedIuPzYQjwT4S-0UlpAxE80DTk53CT0WrsSui5wwPpDXhzuf_70V2mwllCIuI-AnilgyCG25qiYwmZtww9wcF8J4fzRIiGTAKAL5ZO_XGfKkmIWW45b-x4WoecKkhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-450452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfddfba7c.mp4?token=kKfHpm-vveuG_cqqTgKVeqwqxJiTE3qiIv6a5a3B6O6kfLeMD14ZGtBsGeLwwCx-oCXk8PMmpof06kTfZCrl2rU-vaOBIiQCl5N_0AjMFXhT3JIiJhF5_H0-VD2ys6PYGvuOdrYhe4bqW-5rQ9SNQGIH8yiunbHx3ZyxVAWKo9LuUIf3tLzzafkpUUC_jCZREmb5ch9G-R7m0uH3F1pdV9-mOaO62sLdjW6lU5ckJnUzCOS4h18DwJdUOiAmTJ5rEoI05D_pQQTvDEWTOwsGip87PD8JMgr1IsgBgwzAyT0BBXGWWNT2gEYDIzft3IXLrtVFlR-sauEtKtkExboKLhobNLGQehRz8-WyLdlk_O-pkDaj8fUiH9nez704X07pIOWpegM8EXGlNwtEC1Ujnh5KMDBs4i-liOXsttod_CFw74PMRE35ZBWB98CbOqjos3W7uYG2kgJ6YJ_3AaUDthVWHx6P6R5FsyJjOVE7nOb8qHjxYJKIHrsz82rghE3U_CJG3g2095PjfUftZfCK-40Gkkpc2ZCimOcDTFpS79J8wK98Id0YQ7PzuExzrPK3kMqMo2d7phvXb4z1K1u5dEnAfgimQhmL1JSX7m1sg-KNPOjwz8Ce-V2vLR1jNMp-MJza7t1FjhNs_23Xt-n7btuIQvQ0RNgrgK3A3jOz4HI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfddfba7c.mp4?token=kKfHpm-vveuG_cqqTgKVeqwqxJiTE3qiIv6a5a3B6O6kfLeMD14ZGtBsGeLwwCx-oCXk8PMmpof06kTfZCrl2rU-vaOBIiQCl5N_0AjMFXhT3JIiJhF5_H0-VD2ys6PYGvuOdrYhe4bqW-5rQ9SNQGIH8yiunbHx3ZyxVAWKo9LuUIf3tLzzafkpUUC_jCZREmb5ch9G-R7m0uH3F1pdV9-mOaO62sLdjW6lU5ckJnUzCOS4h18DwJdUOiAmTJ5rEoI05D_pQQTvDEWTOwsGip87PD8JMgr1IsgBgwzAyT0BBXGWWNT2gEYDIzft3IXLrtVFlR-sauEtKtkExboKLhobNLGQehRz8-WyLdlk_O-pkDaj8fUiH9nez704X07pIOWpegM8EXGlNwtEC1Ujnh5KMDBs4i-liOXsttod_CFw74PMRE35ZBWB98CbOqjos3W7uYG2kgJ6YJ_3AaUDthVWHx6P6R5FsyJjOVE7nOb8qHjxYJKIHrsz82rghE3U_CJG3g2095PjfUftZfCK-40Gkkpc2ZCimOcDTFpS79J8wK98Id0YQ7PzuExzrPK3kMqMo2d7phvXb4z1K1u5dEnAfgimQhmL1JSX7m1sg-KNPOjwz8Ce-V2vLR1jNMp-MJza7t1FjhNs_23Xt-n7btuIQvQ0RNgrgK3A3jOz4HI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز در آزمون کارشناسی ارشد چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 350 · <a href="https://t.me/farsna/450452" target="_blank">📅 21:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99153d6474.mp4?token=akVlqH6ltaFPCBsOYvcJzxqIOB8O-R8FYlG92tRYfj8dqdN3Aevl3wI8qAfLPP3f0SAGn7QgZyuEHNtvRhanHj9bvLcNZJKvD5j3JOdkbXcKSINRdIK2wNrhvMN9jk-oO3bBdmHgDKp2IOEheS33v1Euz4vtxk_jumYWFKYeYVC-thpqD_4DQEFRd6UZAC6Tjq_kT4UvVMEEQnK88g05Sjma4al_TnM99hyleO7GsE3sKqNH3SK0Nqb2mcpjLdv63PUulbLIfF-OXJDONY1WSS0jqtYb-KVPiKEVN70PzYJGXKnxzfxqb82M4zkO--Mfr4DHtkADy_MxTIBE7myXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99153d6474.mp4?token=akVlqH6ltaFPCBsOYvcJzxqIOB8O-R8FYlG92tRYfj8dqdN3Aevl3wI8qAfLPP3f0SAGn7QgZyuEHNtvRhanHj9bvLcNZJKvD5j3JOdkbXcKSINRdIK2wNrhvMN9jk-oO3bBdmHgDKp2IOEheS33v1Euz4vtxk_jumYWFKYeYVC-thpqD_4DQEFRd6UZAC6Tjq_kT4UvVMEEQnK88g05Sjma4al_TnM99hyleO7GsE3sKqNH3SK0Nqb2mcpjLdv63PUulbLIfF-OXJDONY1WSS0jqtYb-KVPiKEVN70PzYJGXKnxzfxqb82M4zkO--Mfr4DHtkADy_MxTIBE7myXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای دود سیاه در آسمان بهبهان خوزستان چه بود؟
🔹
درپی انتشار تصاویری از یک ستون دود سیاه در حومه بهبهان و گمانه‌زنی برخی کانال‌های فضای مجازی درباره وقوع انفجار یا حادثه امنیتی، پیگیری‌ها از مراجع مسئول نشان می‌دهد هیچ‌گونه حادثه امنیتی، انفجار یا اقدام خصمانه‌ای در این منطقه رخ نداده است.
🔹
فرماندار بهبهان اعلام کرد دود مشاهده‌شده ناشی از سوزاندن غیراصولی زباله و لاستیک‌های ضایعاتی در اطراف شهر بوده و هیچ ارتباطی با مسائل امنیتی یا نظامی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/450451" target="_blank">📅 21:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dde642eee.mp4?token=dSnwiq27m9rOv9jdVMRp4NsS4H6JswuGx142kBeNn8c6D4m1TDJpgMP09VKQ4-hl419tXRdEezcNri_s3F8ewW76HR9J8_T8sXazvUh7w9Kzeb6VJdPYIcLQAsf0k6t4avximYxn-ikeRL95N1oggiV5djbwEc-oeHO4630mEQ1yLb56qzasoqsQWpVzntTr-UriAzwaROTRP4W_toUf295H2_ec2v7VlcRCxOGxDcP0Cc4_wwAxUrtVpI2Rjish8ak9TCyPWThrnlIegRzjZBe4qb3IQ5ENmwGrThqSub-eYkS8ifqnEeDk02OUTh_v9TLAVM-D36f6K-ZSOf3x6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dde642eee.mp4?token=dSnwiq27m9rOv9jdVMRp4NsS4H6JswuGx142kBeNn8c6D4m1TDJpgMP09VKQ4-hl419tXRdEezcNri_s3F8ewW76HR9J8_T8sXazvUh7w9Kzeb6VJdPYIcLQAsf0k6t4avximYxn-ikeRL95N1oggiV5djbwEc-oeHO4630mEQ1yLb56qzasoqsQWpVzntTr-UriAzwaROTRP4W_toUf295H2_ec2v7VlcRCxOGxDcP0Cc4_wwAxUrtVpI2Rjish8ak9TCyPWThrnlIegRzjZBe4qb3IQ5ENmwGrThqSub-eYkS8ifqnEeDk02OUTh_v9TLAVM-D36f6K-ZSOf3x6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت آب و فاضلاب: پیش‌بینی می‌شود در تابستان مشکلی برای تأمین آب نداشته باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/450450" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e6476c6c.mp4?token=QcHDxFUMILQrngMH6Fi5IuTI_medWdV4GEu2lcYwShN14fqaOPe4HJ0xi8B56t2WxCZd1Th0mvJOhfa-Twm4WEg2xwWA0CwR3JdUb3cEuiq0IZIIRKTpnRUj8uD5sbiI6Bf6I3bU43nkllzcEHr-Gw9UO7EF7pZiMBJ6D6da0qLOjUXchwjpQQYaawhlQxcBaZdj0O13Fy9evvto9GmnDUTLIeIOfbYLTiXpM1GBSYBXooLhC89P3b45pKMGAxbVeS6u5VtagHw7nxF4BfR8rFlwZahF5f0850H2wej3MK1ZUKjia6R8lLWKjC96cERR8YjVs3qP1htyo8Lnx9pKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e6476c6c.mp4?token=QcHDxFUMILQrngMH6Fi5IuTI_medWdV4GEu2lcYwShN14fqaOPe4HJ0xi8B56t2WxCZd1Th0mvJOhfa-Twm4WEg2xwWA0CwR3JdUb3cEuiq0IZIIRKTpnRUj8uD5sbiI6Bf6I3bU43nkllzcEHr-Gw9UO7EF7pZiMBJ6D6da0qLOjUXchwjpQQYaawhlQxcBaZdj0O13Fy9evvto9GmnDUTLIeIOfbYLTiXpM1GBSYBXooLhC89P3b45pKMGAxbVeS6u5VtagHw7nxF4BfR8rFlwZahF5f0850H2wej3MK1ZUKjia6R8lLWKjC96cERR8YjVs3qP1htyo8Lnx9pKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارمند هتل محل اقامت سربازان آمریکایی در عمان، هدف‌قرارگرفته‌شدن این هتل توسط ایران را تایید کرد
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/450449" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13957b8c40.mp4?token=EZ47Kiekq8ufTtZFxwzZ6a7F82Ia2xw4NyY9tJS71KHTLQh7UjZiKCx2GZiYeD4k0NUNAkYDEdL1X8GNUNLSxrsHHk27T-6VgAo48eJPSlBEusOFl0tMMxjtHRtvdmm80WmyJhGA3c5HjTvcuymoVRCFOB2vzazaO4k12NEIRJ6cFBQCo2aVaFUH8NRjDihbFXrF6q7OL0aZhFehWxP7JsMEYPmgxvpCCUhslPw6uzGxVbFZEtDEs47J5lF3U3ZaAjDJrbVjDs6cmPxpQxn08Gzdk579MBOX5N3asZ1fWA5LKMF8JgBt7N-0Xefy3zH_p4fkO5CTTaNvW7Hw34bj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13957b8c40.mp4?token=EZ47Kiekq8ufTtZFxwzZ6a7F82Ia2xw4NyY9tJS71KHTLQh7UjZiKCx2GZiYeD4k0NUNAkYDEdL1X8GNUNLSxrsHHk27T-6VgAo48eJPSlBEusOFl0tMMxjtHRtvdmm80WmyJhGA3c5HjTvcuymoVRCFOB2vzazaO4k12NEIRJ6cFBQCo2aVaFUH8NRjDihbFXrF6q7OL0aZhFehWxP7JsMEYPmgxvpCCUhslPw6uzGxVbFZEtDEs47J5lF3U3ZaAjDJrbVjDs6cmPxpQxn08Gzdk579MBOX5N3asZ1fWA5LKMF8JgBt7N-0Xefy3zH_p4fkO5CTTaNvW7Hw34bj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی ستاد اربعین: معطلی زائران اربعین در گیت‌های مرزی کمتر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/450448" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUfe-uopsoDpaKVYqR7FFWI7deyiTARLsdIQ9Rx8zeRL_rQUy717XqntlFPTwUwrLao3W2qqfTvfaRhv1GL855-6VkmVfS5FBlHxCuDQ8CXa1OpA8id0WRA8w7BM-50uDeS28--3MSWaR3nsIKLEr8y7UvKa74RKfHZe6IzyEU32eY3c67aqrDCEDmycc7QylmROVhw8LO2AxiNn5Jm0zOd4dVCPtkgO9DYPTu-T8GBEK_GRIwPre0rSAiTxTMasxeVIShh02i9kZFHcKs-H8P2qGZEq5Q_JFAn5P0mi9Nqq3c7J8vgccglpjHA8OC2JGSlEOCFwqZFaNSCPVHiZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک اسرائیل به عربستان برای مقابله با پاسخ یمن
🔹
شبکه المیادین به نقل از منبع نظامی بلندپایه‌ای در وزارت دفاع یمن اعلام کرد که نیروی هوایی رژیم صهیونیستی در تلاش برای مقابله با پاسخ یمنی‌ها به بمباران فرودگاه صنعا، با سعودی‌ها همکاری کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/450447" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e308ddab4e.mp4?token=KutiSkyxvQYDxT22vPKtXn1Gx8p3YHGiBY8qxsiDvrCUjh5TqxHBRIS2Z-CWJakJwAhvO-FP0Jct7eB0rVJObp8bLkZ4WIEy34L5bb3BwK7sW3a1iwZpt9igOkwQanoF57FJboTrmpImUQ5UidZaOSCLU8AY-t66W332OAEHx-HHK4y17RyhiQaxEX1xH-J8fK2JjkxXx-7hFdURuxL1Lb1XHINDzDwuI6e4dY4eosqE1xRguu1Apm5yhN_7zM6yin3fEE29-UMrenQb28H5TocGQwc_S7SHsiKgFGoQgB4TZAuB4iByWCKClI2c9OOteSpABboc4fUIpgyBVwZpOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e308ddab4e.mp4?token=KutiSkyxvQYDxT22vPKtXn1Gx8p3YHGiBY8qxsiDvrCUjh5TqxHBRIS2Z-CWJakJwAhvO-FP0Jct7eB0rVJObp8bLkZ4WIEy34L5bb3BwK7sW3a1iwZpt9igOkwQanoF57FJboTrmpImUQ5UidZaOSCLU8AY-t66W332OAEHx-HHK4y17RyhiQaxEX1xH-J8fK2JjkxXx-7hFdURuxL1Lb1XHINDzDwuI6e4dY4eosqE1xRguu1Apm5yhN_7zM6yin3fEE29-UMrenQb28H5TocGQwc_S7SHsiKgFGoQgB4TZAuB4iByWCKClI2c9OOteSpABboc4fUIpgyBVwZpOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این سربازان هیچ‌گاه پست خود را ترک نمی‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/450446" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
آمریکا تاوان تجاوز را پرداخت
@Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/450445" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfb3af009.mp4?token=ZE-DVZc5BjfEA52RaN-0xG9KOpeGuu-rkZWpqS4xrujf2laaxJr-ezNDXkEWXtftPI5LNRDuvOkWyU-EnA-fYYRg5YkU0XKq0usFccp1h0XhtVHsNeF7TZzFCrBLcdusYn8hzHasDeJ572yqnxtaWhWtfTzmSJqR9OehMUDO2VGk3rIDuJA7S5ZZojZlIkggaEBKsXsbri13JaRD7mfkWyQ3Y9J1Bu_kD4I8u5OSHUDp1B3O2a2t8My49DgT6pCaEZBb0Z-byNU0i8ZDLuBe9emKIaKezK4duV9YwNINjBliWycf1NiLi-3pCfHgJ_c78DCRCzGa-0jAxkGup3M4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfb3af009.mp4?token=ZE-DVZc5BjfEA52RaN-0xG9KOpeGuu-rkZWpqS4xrujf2laaxJr-ezNDXkEWXtftPI5LNRDuvOkWyU-EnA-fYYRg5YkU0XKq0usFccp1h0XhtVHsNeF7TZzFCrBLcdusYn8hzHasDeJ572yqnxtaWhWtfTzmSJqR9OehMUDO2VGk3rIDuJA7S5ZZojZlIkggaEBKsXsbri13JaRD7mfkWyQ3Y9J1Bu_kD4I8u5OSHUDp1B3O2a2t8My49DgT6pCaEZBb0Z-byNU0i8ZDLuBe9emKIaKezK4duV9YwNINjBliWycf1NiLi-3pCfHgJ_c78DCRCzGa-0jAxkGup3M4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده می‌شود که نیروهای مستقر در محل با سلاح‌های سبک به سمت آن تیراندازی می‌کنند.
🔹
این تصاویر در حالی منتشر شده که بررسی‌ها، هویت پهپاد را تأیید کرده و نشان می‌دهد ابوظبی، برخلاف ادعاهای بی‌طرفی، در حملات علیه ایران نقش عملیاتی داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/450444" target="_blank">📅 20:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f1bb656.mp4?token=jDTcvl3_X2BRjmITizo9cewU2HVdYEt75nRh_jtx5U_Rr2nUVVRQsL2gRnOsxRtcjxSYIyGBoXn5XX1_mWRSj781HcZW_uLyltJWgef0Kvy6p6eL2FgYJw3bfgGKgmSn0F9XpCLA-wvSevOt4tadJ2b4xfwOy7HzNqKSyeOzTHoKkVQ9bEAOEqTuXaZEcEoA_bzIuT1q6BMdBLInJ4gj4T9wOu8Not9AxsrFqQrzts80xGD4gMycUWqO9K4nkqMh5YL2TXiw6xHBt6qhhugytdm_zWYkDCov3Wt54XpwbT-4iVxg83GYfq3zUu4ts29H1brYtIsxdFKEhMTeHXYTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f1bb656.mp4?token=jDTcvl3_X2BRjmITizo9cewU2HVdYEt75nRh_jtx5U_Rr2nUVVRQsL2gRnOsxRtcjxSYIyGBoXn5XX1_mWRSj781HcZW_uLyltJWgef0Kvy6p6eL2FgYJw3bfgGKgmSn0F9XpCLA-wvSevOt4tadJ2b4xfwOy7HzNqKSyeOzTHoKkVQ9bEAOEqTuXaZEcEoA_bzIuT1q6BMdBLInJ4gj4T9wOu8Not9AxsrFqQrzts80xGD4gMycUWqO9K4nkqMh5YL2TXiw6xHBt6qhhugytdm_zWYkDCov3Wt54XpwbT-4iVxg83GYfq3zUu4ts29H1brYtIsxdFKEhMTeHXYTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلمان حریف ملی‌پوشان ایران نشد
این‌بار برنده ست پنجم ما بودیم
🏐
ایران ۳ - ۲ آلمان
🇮🇷
۲۵ | ۲۶ | ۱۸ | ۲۵ | ۱۵
🇩🇪
۲۲ | ۲۸ | ۲۵ | ۲۰ | ۱۲
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/450443" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9547638aa.mp4?token=Vd8CBQl179CRNH7__5SRfeQvGtcvoFsEqatScJ304UAXcsHrFgq_mj2Ii0O5oxRd4ybNEikcaSq5uhbJvoFXNLWqgxsW0LkiEzBBnQbQE10fV2oJerW_vhYLH0XRLyMJVTEQ5rfpV8BBL9yGzDK0qHmu1rRgwx2iwYLJkJcabPQxiuABlJqz6v3cvJ1iE5wTeNctpZwXhKcxMuBU1QDKBkSYkJIcZI5CnkKnAeHBC2ci_0a3_aD4UAtFSId3O_U8OxWNBES_Ldm4_I7hpxoNgWNAhoDMDN-I75_4QsbUMFkLj1fNw8mTUU_ygJKz8MSesoNCiZ22x5F3oxTk6kgOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9547638aa.mp4?token=Vd8CBQl179CRNH7__5SRfeQvGtcvoFsEqatScJ304UAXcsHrFgq_mj2Ii0O5oxRd4ybNEikcaSq5uhbJvoFXNLWqgxsW0LkiEzBBnQbQE10fV2oJerW_vhYLH0XRLyMJVTEQ5rfpV8BBL9yGzDK0qHmu1rRgwx2iwYLJkJcabPQxiuABlJqz6v3cvJ1iE5wTeNctpZwXhKcxMuBU1QDKBkSYkJIcZI5CnkKnAeHBC2ci_0a3_aD4UAtFSId3O_U8OxWNBES_Ldm4_I7hpxoNgWNAhoDMDN-I75_4QsbUMFkLj1fNw8mTUU_ygJKz8MSesoNCiZ22x5F3oxTk6kgOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس ارشد حوزهٔ نفت: در مدت اجرای تفاهم حدود ۸۰ میلیون بشکه نفت و فرآورده‌های نفتی صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/450442" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97eb8935c8.mp4?token=va2GS__7n9gjosgBzgAi7QejbLhhcsEEgP7hbiL4VYD5ltVEv54QUk6XlMqhq79-fuEkmX3_lLoc0Ne58Ecx3FN79UteaSFwxPfWS4N8Q757Tx3jHGHJF-G-9yqHQOt-NMS-OuaPjr5AsAWA4P8gBkYMkVzeH2WCtPpezx_2IOMUzJtXnI1r-6oyj_CAyX0COkmdq9GggDrXYuMmLYIOooFqZFdbxgByrNBa74Gnw56yyah9bbC-UV1msEsSsGAO27oKAjKeNHf5ApJv2HHIhkRzVNzJaMY8Y_lw1v5vj_fLtxC2L8b05yrf3uqY7u7t60e-Z8h8wrRIPGlSfxbing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97eb8935c8.mp4?token=va2GS__7n9gjosgBzgAi7QejbLhhcsEEgP7hbiL4VYD5ltVEv54QUk6XlMqhq79-fuEkmX3_lLoc0Ne58Ecx3FN79UteaSFwxPfWS4N8Q757Tx3jHGHJF-G-9yqHQOt-NMS-OuaPjr5AsAWA4P8gBkYMkVzeH2WCtPpezx_2IOMUzJtXnI1r-6oyj_CAyX0COkmdq9GggDrXYuMmLYIOooFqZFdbxgByrNBa74Gnw56yyah9bbC-UV1msEsSsGAO27oKAjKeNHf5ApJv2HHIhkRzVNzJaMY8Y_lw1v5vj_fLtxC2L8b05yrf3uqY7u7t60e-Z8h8wrRIPGlSfxbing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ جزئیات حملۀ بامدادی آمریکا به سمنان
🔹
سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
🔹
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
🔹
خوشبختانه بخش‌های…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/450441" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c674f4f5.mp4?token=LNOTQK-k__8NartoEe9jqPhbNwdrhPS7xBpxEhj3kBtygLjkLejCDXr50ZkpksSvHcs-UM-IfqBm-4DgKHQZp8PNsFRY2r75tHB83MtO_Ap7qxJ-AbGKWF7fzSXHfkgJIvJPqNgya1JhjIUx_e_7TVMgxVqznJSK0kb2WKujIlzMeFpvgjEqsadcfPGYLr-M1MADL-rlHxxSbzXin0PlMS8r9tP62V8TYJl3hZKOMs_YHHxHwpYMVk3O6yZJlNx1y4kzN2YD1U0zpjySt9W2C_UQtcoJun374p3SJN000bpuVTUKfxAp_ZeKnssS5Re-aXbxxxBkTeCRnMQrgjq9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c674f4f5.mp4?token=LNOTQK-k__8NartoEe9jqPhbNwdrhPS7xBpxEhj3kBtygLjkLejCDXr50ZkpksSvHcs-UM-IfqBm-4DgKHQZp8PNsFRY2r75tHB83MtO_Ap7qxJ-AbGKWF7fzSXHfkgJIvJPqNgya1JhjIUx_e_7TVMgxVqznJSK0kb2WKujIlzMeFpvgjEqsadcfPGYLr-M1MADL-rlHxxSbzXin0PlMS8r9tP62V8TYJl3hZKOMs_YHHxHwpYMVk3O6yZJlNx1y4kzN2YD1U0zpjySt9W2C_UQtcoJun374p3SJN000bpuVTUKfxAp_ZeKnssS5Re-aXbxxxBkTeCRnMQrgjq9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/450440" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da6ff51f.mp4?token=oGABHZr3eNgN96jv401U1X4vp7mj2UOoYqXNIERaIVXRNhftZ3NZmuxL4wEKweKh2tNu9rLba-vXDdvqaqOj08SBa9hjNd9hXNCuze6QID_IAXi6OFwPhBTm1YDi9IcPJbkClw6HN8HVb4mgVhDMUoGzKHm-C9OU54HK6dheWWIVfHe3pvraMdVfRBxAcdlsowtehwMgw4T1AeWdai55eBKDBXlVCVzSEzxW0e6_RM2bdy9RJB9GoOXzsAG2zlaHBPeOhVUOsaAbmC9d025fm8BOTHSLh5pcN0Zc1FiQai0D1dGtyFEW3hg6gaLnfbZRXGRbl_BQu5cbFe-_Bq219A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da6ff51f.mp4?token=oGABHZr3eNgN96jv401U1X4vp7mj2UOoYqXNIERaIVXRNhftZ3NZmuxL4wEKweKh2tNu9rLba-vXDdvqaqOj08SBa9hjNd9hXNCuze6QID_IAXi6OFwPhBTm1YDi9IcPJbkClw6HN8HVb4mgVhDMUoGzKHm-C9OU54HK6dheWWIVfHe3pvraMdVfRBxAcdlsowtehwMgw4T1AeWdai55eBKDBXlVCVzSEzxW0e6_RM2bdy9RJB9GoOXzsAG2zlaHBPeOhVUOsaAbmC9d025fm8BOTHSLh5pcN0Zc1FiQai0D1dGtyFEW3hg6gaLnfbZRXGRbl_BQu5cbFe-_Bq219A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
توپی که نمی‌افتاد، به نام ایران تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/450439" target="_blank">📅 20:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
رویترز: لحظاتی پیش صدای چند انفجار در شهر دبی به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/450438" target="_blank">📅 20:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6110e06d4.mp4?token=I4fMCnWY0PmKD0nJbyWcbSHf14WwOXU_da-tEY8ogAJBAP7iqcPhMbfR2x_Lq38MvmgAY2LSLI2QHPJvwGp-YXVN0EddiDMSHMYIKu1Y3URPD17SrW0FM9EKBMmM5tx3Io_b61pHY1rhxcgmYGeHzKTbrBcgVTQfLPo1fiq2Nr2tHgfTF9yUlpsc50VNHvQjRPgyo08FIuK9W-5A0_NBE6JWKpJCBzH5zEuBb1lH-tG1W2lByJ2I-Axg-JIIZsxa0_wMbTfzwgTDU7JyPfJcNgKgNHxkAcL8EvQ7BMDylgeLzBlJVILuqW_QNnfnjXOPAGT_ugc2bfWTJPAEgqYrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6110e06d4.mp4?token=I4fMCnWY0PmKD0nJbyWcbSHf14WwOXU_da-tEY8ogAJBAP7iqcPhMbfR2x_Lq38MvmgAY2LSLI2QHPJvwGp-YXVN0EddiDMSHMYIKu1Y3URPD17SrW0FM9EKBMmM5tx3Io_b61pHY1rhxcgmYGeHzKTbrBcgVTQfLPo1fiq2Nr2tHgfTF9yUlpsc50VNHvQjRPgyo08FIuK9W-5A0_NBE6JWKpJCBzH5zEuBb1lH-tG1W2lByJ2I-Axg-JIIZsxa0_wMbTfzwgTDU7JyPfJcNgKgNHxkAcL8EvQ7BMDylgeLzBlJVILuqW_QNnfnjXOPAGT_ugc2bfWTJPAEgqYrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگرانی تازه برای فینال جام جهانی در نیویورک
🔹
در فاصلهٔ چند روز تا فینال جام جهانی، آلودگی هوای ناشی از دود آتش‌سوزی‌های کانادا نگرانی‌هایی ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/450437" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450436">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l94ZmgYDOw14wcZQVS4dg9qJWtGrMZCtThKNQSTBF7FgtrxHtueFajgd77LFbT08TD1Mqkv9vic4JMYqBqo3ZWNoRcsvZ0XEKhSe1r93uaZOgc_a9DfDOUuqx890RVd8GT8V5v1vyQk7GVK36BIWkjFKCZqBDYi9jyUwrImq9Iklp23Pqoc-1wMnSeC656xDUcfgud9tC-VKRc33u3NBdjO2n7imEQNeXKp9WD4yWjTjz3aNeZ6fL-TE37Mh5CQgK0irM53g23xkk89Zt52Gqy_P87f-TTzXxo_0AX5cGAvHq4V1Guv5M5k2wMauP8DSDKU1g9JXwT33NVoznnHQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف معاون ترامپ به ارتباط اپستین با نهادهای اطلاعاتی آمریکا و اسرائیل
🔹
معاون رئیس‌جمهور آمریکا می‌گوید اپستین «به وضوح» با عناصری از دولت پنهان اسرائیل مرتبط بوده است.
🔹
او به‌وضوح با بالاترین سطوح اطلاعاتی آمریکا ارتباط داشت. او به‌وضوح با بالاترین سطوح اطلاعاتی اسرائیل ارتباط داشت.
🔹
ونس در طول این مصاحبه پذیرفت که دولت ترامپ «کاملاً» در برخورد با اطلاع‌رسانی‌های مربوط به پرونده‌های اپستین اشتباه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/450436" target="_blank">📅 19:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450435">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQwdtlhf_UZUNGH6ir0ItE9H1N8g_vu3Oa2eLSB9FWfhcpFt3sgbkA0muWIKsi2RvpyHbLjTO15dW6xbTKmnclGVjvLj9hM90iFApEG5u3QS3TyPS-7lIwejakJuXutvN0cBLo2ESF5ZDxh4VP0xX7u01A3-1SdDdMTxIvUdcH1ML4J7ab2Eyz6tX2wisv4NGFfIZ9LwiUBtzHVSp4oixwva4co_H8NqIH6QJxOivK7zlP35Xb3DKpGjNSVFiT6d9KtaHIMLqLqhZKf4a2fbg00EG5Bd4kEOQBERNTp7L8q-sRPAO3JYcQZ2-rQG4xq5frtICdGJUUwxOEfB88XbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: دستان آمریکا به خون کودکان ایران آغشته است
🔹
وزارت خارجهٔ یمن: هدف قرار دادن محوطهٔ بیمارستان کودکان سرطانی «شهید بقایی» در اهواز توسط دشمن آمریکایی را محکوم می‌کنیم؛ حمله‌ای که مقامات ایرانی را مجبور به تخلیه آن برای حفظ جان بیماران کرد.
🔹
این جنایت نقض آشکار حقوق بین‌الملل بشردوستانه، به‌ویژه کنوانسیون چهارم ژنو در مورد حمایت از غیرنظامیان در زمان جنگ (مصوب ۱۹۴۹) است.
🔹
دستان آمریکا به خون کودکان ایران آغشته است و این جنایت، ادامه جنایات آمریکا علیه آنان به‌شمار می‌رود؛ به‌ویژه کشتار مدرسه ابتدایی دخترانه میناب که به شهادت بیش از ۱۶۵ دختر بچه انجامید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/450435" target="_blank">📅 19:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450434">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJEMImpiObEmvtbL47KVY0PkYk7_G-Tq4mIqnd3tA3MnnXXoUuH-s3q1LCZ6dmhI71KmBesKEM60qY3RX75MgZ6SGKIMeYI3r6FtKXH0V0j2wt40C-V6G70Eqy1uUcl0HuygVAQOr0IbTI5-FJjv87EYshwZjXjv-1GKZZUr2wlVwjo05K09P6JmDOMMc0Qq0lo6QyYcizzUVEoNim8jpelvl3d3mzZxvjUrklwVB7FIDmCed9wEnmpgGBTz5cAgqJA3YsxucEF_1hsU6mexQmKdPFhbrdu0rpCqesSlzr5MXF11HKQ9JozRS2Avdi8VHZp8i1hHvxKqiLB9_7XSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ترسیم نقشه راه بانک ملی برای آینده توسط سیفی؛ از توسعه زیرساخت‌های فناوری تا اصلاح مدل کسب و کار
🔹
مدیرعامل بانک ملی ایران مهم‌ترین راهبردهای بانک برای عبور از شرایط موجود را اجرای برنامه‌های گسترده در حوزه اصلاح مدل کسب‌ و کار، توسعه زیرساخت‌های فناوری، تقویت بانکداری شرکتی، افزایش اختیارات شبکه شعب، بازگشت منابع و ارتقای سطح رضایتمندی مشتریان و کارکنان دانست.
🔗
مشروح خبر…
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/450434" target="_blank">📅 19:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilG8waf5NYNAfs2c4DliQrOG3Aoudd6_vNfNQf1Nf-QGeRpeg1PaGafNGg2AmPRUtra8vjsWhu_LX3yQaiIR0b-OC2Kfw5ua6I3UIkTjp_OsNvOx8CoeDGeDUrSax90YckGHPU_mAATxrL4SaAuYQ1c3XvTe1YmIi0asESzoinpvbfQrlt7xLvMX6FW5HKk7o0wLlDlowGLOFe0jb-pbsgAkYLXRApFnUyIZk1XN2ktzQm_8MWkc1iG2Gmi8eafkbJpjN5ZsAoAT7rQ9rH-u1WpnEz3AoP6gzQnVJLYXJnKEXVvNA6dcbG7WA1ksSBgHf1Kv50wns81NGFViS7b19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/450433" target="_blank">📅 19:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450432">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/450432" target="_blank">📅 19:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYAbuRbXqVQcIc27fXSVxdr1GIedMXUno-T2Gs06AnI4pPdla863R7fAZMNupjSdWbkegrnQrdtNF06qh3M0dwCyuVK9jQOzc0ewmdC5xXdg9IiIbEePDndz5eRvbvRC20eVUJYn45Qt2wEKEwKfpiwzSZYvkgHX9660OLc3EjSYUZHOax7iv9M5jVgISHTvQR7kd38itQMWrar5hg0OgOvnH8CAprG2IwmbKeTiOvtV4wSXCkebZI2S0dZbvq1RH1dUzLY1KNVWbANOFfc4CtJBXjJ3n88VOM4qIfKO8DXrMXfB15Jj9a4fBitmVrqXZSaWJxAW7mgma_47nPWPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کمبود موشک تا رکود؛ ۴ چالش ترامپ برای تشدید درگیری‌ها با ایران
🔹
در حالی که رئیس‌جمهور آمریکا هر روز فهرست تهدیدات خود علیه ایران را تکرار می‌کند، نشریه نزدیک به کنگره آمریکا روز پنجشنبه نوشت که اگر دونالد ترامپ مسیر دیپلماسی را رها کرده و همانند گذشته تجاوز نظامی را از سر بگیرد، با خطرات جدی در داخل و خارج از آمریکا روبرو خواهد شد.
🔹
جنگ علیه ایران حجم عظیمی از مهمات آمریکا را مصرف کرد. فرمانده سنتکام برد کوپر در ماه می (اردیبهشت) به سنا گفت که تا قبل از برقراری آتش‌بس، ارتش آمریکا بیش از ۱۳۰۰۰ مهمات جنگی شلیک کرده است.
🔹
ترامپ پس از امضای یادداشت تفاهم اعتراف کرد که بخشی از انگیزه او برای امضای تفاهم‌نامه (MOU) با ایران جهت بازگشایی تنگه هرمز، خطر رکود جهانی در صورت ادامه کاهش ذخایر انرژی بود.
🔹
محبوبیت ترامپ، به ویژه در حوزه اقتصاد هم‌مسیر با اقدامات او در ایران نوسان داشته است. این موضوع باعث نگرانی جمهوری‌خواهان از این شده که درگیری در خاورمیانه چگونه می‌تواند رأی‌دهندگان را در انتخابات ماه نوامبر (آبان) از آن‌ها دور کند.
🔸
شرح کامل این گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/450431" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450430">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اصابت موشک آمریکایی در حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
📝
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/450430" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450429">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c29363757.mp4?token=NFOZJAym93Y_qo-jtVUN5e9oBOl2XBvMIcqJIve6QMbNIaJGjX5tuxCah5wMtTKtBw_OSoZdhgNC_-ghBi_C92WxiTPTUiGiJCcuCI2Lu8gVN57Vv5ZJZ4ydRHZ2tsXY5RXzwtDrJK4BvqbkyAELYloTmMDShNa3b4FrJjSoSvWNPCBYM04gKsEaXxYN6-soiLOqZcq1UdYz7pETQRHE2J3EmaQFw2eyAxZsg-v4IcB5gQ4oOoGzTab6WxAOqA_nMni9-9Sit6-ZKT7aDxXjmU1zB_5ZEFhFly8607sZNK0zXrCiZ_a9a7QGWGSa9qbjQ9bfgDQhRX6YSg3rOESM3QMT0HwO8aHpN8LMptreEtlX3gJHDTxhHObzKs18ydjYXO0yXV6vzIOrRWYr1BRXtnQZprdC5hGhwzQp1kqOyWKb356ElRyPdura1FeKGzVcGzDOmegCKlgnJREjyHzETaFvGJqb_fIxtk0IDqbtz7HBvC88wN_twOoJqrM97uIVXmWwoFL4RasuvySWR-vk5nMmZs1jv-7lQKblHAeKnLT2rVOAyS-mZZYdOtmGs5mDdpRv2ZUNzo6JCGHikTm6BTK3rDSjBsE_U7nLMy2l8pbhL5OYWFz_AUL0n067Dlj7ThXyDXFZxHkooaSssJTocKSdOjQfsSmyy2C2kNZuqkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c29363757.mp4?token=NFOZJAym93Y_qo-jtVUN5e9oBOl2XBvMIcqJIve6QMbNIaJGjX5tuxCah5wMtTKtBw_OSoZdhgNC_-ghBi_C92WxiTPTUiGiJCcuCI2Lu8gVN57Vv5ZJZ4ydRHZ2tsXY5RXzwtDrJK4BvqbkyAELYloTmMDShNa3b4FrJjSoSvWNPCBYM04gKsEaXxYN6-soiLOqZcq1UdYz7pETQRHE2J3EmaQFw2eyAxZsg-v4IcB5gQ4oOoGzTab6WxAOqA_nMni9-9Sit6-ZKT7aDxXjmU1zB_5ZEFhFly8607sZNK0zXrCiZ_a9a7QGWGSa9qbjQ9bfgDQhRX6YSg3rOESM3QMT0HwO8aHpN8LMptreEtlX3gJHDTxhHObzKs18ydjYXO0yXV6vzIOrRWYr1BRXtnQZprdC5hGhwzQp1kqOyWKb356ElRyPdura1FeKGzVcGzDOmegCKlgnJREjyHzETaFvGJqb_fIxtk0IDqbtz7HBvC88wN_twOoJqrM97uIVXmWwoFL4RasuvySWR-vk5nMmZs1jv-7lQKblHAeKnLT2rVOAyS-mZZYdOtmGs5mDdpRv2ZUNzo6JCGHikTm6BTK3rDSjBsE_U7nLMy2l8pbhL5OYWFz_AUL0n067Dlj7ThXyDXFZxHkooaSssJTocKSdOjQfsSmyy2C2kNZuqkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌های بی‌پایان عاشقان برای تجدید پیمان با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/450429" target="_blank">📅 19:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450428">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67340c5ecf.mp4?token=RjwUEou8rUmZEYqQAFnuf8p1Q76c-u-0L3Hz-Qfq4cyXkda9YAZu7w8jR16sdbLl3AwmzUSkj5U55nfzEFGmgz-OjtHThjYSXca_504wE0XdCRLTIwuzEZUe5x22AU7m077NA2V7T4LzJFJQexyACXsD-JdyZmN0vv1guBxBcaIoIQdHBJGGBrQlw4ZkMjDBS3-s1SQ76tcdeCWyJ-l4rrC3Xg6DOSPTCyVngAbnQKmTs1-LTH4kaoJeAWdBltHP3wcaj48vzV2wa-f3LsrvitURC2idX1xlL4-l8N4hYWGQeb-yaeZ_5tzFjv29WajikdeotMpa3dNd_Pf72GgI4zTyqSIWN21WxkoH-4bak96sMJ8ltKWtBTExkz1-wkHIYQxwAS-3-GNULgQd4rdjd9835PlTEFPK_I94TjAJabhNn5kHtklzDImeob0ioDSVTQ0ae-7QlI85tTpYCsXg0zLOFxTjtbXhh63AMG_imcr-P6u-9I9MHiGMHjVqbIfTy0bMb1EFAj5O7HhQfva3BQTFp-MFXdgizFw4258X6vX92VACjb1G4OVtK9bm9hG2tPsgbmOM7J7YAEahmgrCnm4ry-5Hwqj9bUQvQWeYCK6x8rDHqH0mscZzPr7YtSx0WwgM70GbUNLWhwJCyeV9BDnxQ2cdI-ybbzyVM0EpYIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67340c5ecf.mp4?token=RjwUEou8rUmZEYqQAFnuf8p1Q76c-u-0L3Hz-Qfq4cyXkda9YAZu7w8jR16sdbLl3AwmzUSkj5U55nfzEFGmgz-OjtHThjYSXca_504wE0XdCRLTIwuzEZUe5x22AU7m077NA2V7T4LzJFJQexyACXsD-JdyZmN0vv1guBxBcaIoIQdHBJGGBrQlw4ZkMjDBS3-s1SQ76tcdeCWyJ-l4rrC3Xg6DOSPTCyVngAbnQKmTs1-LTH4kaoJeAWdBltHP3wcaj48vzV2wa-f3LsrvitURC2idX1xlL4-l8N4hYWGQeb-yaeZ_5tzFjv29WajikdeotMpa3dNd_Pf72GgI4zTyqSIWN21WxkoH-4bak96sMJ8ltKWtBTExkz1-wkHIYQxwAS-3-GNULgQd4rdjd9835PlTEFPK_I94TjAJabhNn5kHtklzDImeob0ioDSVTQ0ae-7QlI85tTpYCsXg0zLOFxTjtbXhh63AMG_imcr-P6u-9I9MHiGMHjVqbIfTy0bMb1EFAj5O7HhQfva3BQTFp-MFXdgizFw4258X6vX92VACjb1G4OVtK9bm9hG2tPsgbmOM7J7YAEahmgrCnm4ry-5Hwqj9bUQvQWeYCK6x8rDHqH0mscZzPr7YtSx0WwgM70GbUNLWhwJCyeV9BDnxQ2cdI-ybbzyVM0EpYIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود اولین کاروان اربعین حسینی به سرپل ذهاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450428" target="_blank">📅 19:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_2r1StHGsGTU6v4b6E3p_JFMQInmIcLIA48VK0qRyp-ycaORQCG7Y1e6CohS2LXQ8WVYxEjTY8199tvC7OqCj74gsp9JpJwd8DbW2ZQogq5-mxUzMNfJ-oKioXDbKGhEWc4ft47p2cCdeFVceXxViH7TvP1zoZLcHnQmKqhyKZuuyY0toBWx4uV8B8s5Y2cuCi7rtuXcSUyXbOIrRmtD6THEiiKDgU2-wknR80AcOgwxtlvvcBHyHhGvDDJfhzeO3H0h0u-GrI5N2dqrl_JDr4gx7RJbOTCtH-8zKOf8S37BdupGksihr57AYPlyPVTEqFwoWArkMwUNxadFuybWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce1H4dTCxhOduerxEQyFU-9VuJr_x-A3e43jLQZGk3LHgUARxVEwFpI4OAT7jAUK6csrx20srjWPZkQf8cLvzNoukroEoMMfYoo3y32OcUKhx55_7dOCAySGQ0cSlGXKjeUhTtmEmqTHZ0riFJroPF37qkfXTNDmryauATF4bAp-4pwgOhCdShbfyp1gM10rDEQRMFf6U932ImFrsfPS4T0ac1YEMBjEUEV8Idg99GuC1m3e7rqtT3S4-5veyGBs8IuURA6JyBB-d3a9DJXJPXklnKuPC8JvVxaxRj3RH_kqpKiIkQRlglebg5-5ad6hkHog3ZJt39VrKqfa32ySJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بیانیهٔ وزارت امورخارجه دربارهٔ حملات وحشیانهٔ آمریکا علیه ایران و جنایات جنگی ارتکابی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450426" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9Zd4vg3WPo5Y3h_JS5ikmJCRCRxc4QJiCxB9-_Vio_y8M4t1E67g_oaupEiLhjUNJqvnTh1qFu7FcZhVZFIfWxIUuCyURA5sKVacfEvNAfBAZIP_A5m5B4aMKU8XvO-2IMzJ_oGB3u-EtryBpaKuT0ezUzFfJjvkPlcFExUwFBTyAAoBn29ciZvBDTPsn6LrUKsjRrhGUp4E5lHRrXSPRJlSlqXRndj81Alh2fjpsOuPlZptXgDwvlJDdPOKh0eZ-xon7neA6Si8zuos9EFCpnlUZWtHs6xqDzoD7f1rzchi13NxUY0yPeQXSSAG1nsdmHtjF4yWGvIkjHTHpLsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدهکاران بزرگ پای ثابت بانک‌ها را بشناسید
🔹
بررسی آمارهای بانک مرکزی نشان می‌دهد نام برخی شرکت‌ها و گروه‌های اقتصادی طی ۵ سال گذشته به‌طور مداوم در فهرست بزرگ‌ترین بدهکاران کلان بانک‌ها تکرار شده است.
🔹
بانک مرکزی از سال ۱۴۰۰ آمار وام‌گیرندگان کلان شبکه بانکی را منتشر می‌کند. بر اساس این آمار برخی شرکت‌ها در چند سال یا چند بانک بزرگ‌ترین بدهکار بوده‌اند و برخی دیگر نیز هرچند در همه سال‌ها رتبه نخست را نداشته‌اند، اما همچنان در فهرست ۱۰ بدهکار اول باقی مانده‌اند.
🔹
در میان این بدهکاران نام برخی شرکت‌های زیرمجموعه خود بانک‌ها نیز دیده می‌شود؛ شرکت‌هایی که از همان بانک تسهیلات گرفته‌اند اما اقساط آن را پرداخت نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450425" target="_blank">📅 18:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اصابت موشک آمریکایی در حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
📝
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450424" target="_blank">📅 18:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📷
مراسم گرامیداشت رهبر شهید ازسوی آیت‌الله سیستانی
🔹
این مراسم باحضور حجت‌الاسلام شهرستانی، نماینده تام‌الاختیار آیت‌الله سیستانی در ایران و جمعی دیگر از علمای قم برگزار شد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/450423" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450422">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حملهٔ پهپادی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار اعلام کرد که پهپاد ارتش رژیم‌صهیونیستی منطقه واقع در بین النبطیه‌ الفوقا‌ و کفرتبنیت‌ در جنوب لبنان را هدف گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/450422" target="_blank">📅 18:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450421">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaD6S01uXW7o9Ml2Sednf9KvanYExYxkM01JvPcagReMAUEpyWujdk5dHapiBYLaYkVvUIrLHlJFme3v56IilWSG24a1Ul8F9WkRobnOF20WMbDFUWJ2th4nkr4fx_mLAV5olvmeBmIupI3DCnPOY9jPO8DWsgbmN3npMCqXh-vrDxsc_bN5hha-i6cfWtPRMf2VLN6hpdcsBtMTqd_HqmSca_Zv5ZUgizB2zUqG_yo1jao-iAdlV0lbwSH1aAdc-i2JahH-_65Aqqj1r4X0yb4NBqAHFp6LQi683-FHnSsR9puj5G2-k8Fr8skW3Y5s7cigcU7z8y3lF_QjfVDmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضوابط جدید واردات و عرضهٔ خودرو در منطقهٔ آزاد انزلی ابلاغ شد
🔹
سخنگوی سازمان منطقهٔ آزاد انزلی: مطابق ابلاغیه رسمی پلیس راهور کشور، از تاریخ اول شهریورماه، ترخیص و شماره‌گذاری خودروهای وارداتی به نام اشخاص حقیقی امکان‌پذیر نخواهد بود.
🔹
همچنین پیش‌فروش خودروهای وارداتی با پلاک مناطق آزاد ممنوع اعلام شده و متقاضیان باید تمامی مراحل واردات، شماره‌گذاری و عرضهٔ خودرو را از مسیرهای قانونی و تعیین‌شده دنبال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/450421" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450420">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0JLHtM-7TCZ7P9LuSjVCTFvFs8mMPQPfG7uMQIP7NUwDDFR-Kzc3ikBQq6JMaZXkFJBIZABUFBM0KZfco0wjOb7GUsVmtP2WSja3ibSU0iZjFQRx8OxOqV4eo41abXersRSOjFX26_QE9oas4B96-nQw_9EuJ5HytLgbGWeWLI1zOGaTm-Z3MhOeg-ctiiwvlE-GG6vsVO6P-xoKFOUnyzgorF4UvSqltOObXARUdM47HM1vv6gtHMqdRtHhN4XrvHg0SV0NoPBVrqig-w13fJ8yVB7v1kgfxBeHy6lPQa6l7gArywuJb-Z1gymEsP7cQUiFHAejsR8YP5OfA_4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال امنیتی ابزار برنامه‌نویسی ایلان ماسک!
🔹
گزارش‌ها نشان می‌دهد ابزار «گراک بیلد» به‌جای ارسال فایل‌های موردنیاز، بخش بزرگی از مخزن کد کاربران را به فضای ابری منتقل می‌کرد؛ موضوعی که نگرانی‌هایی درباره افشای اطلاعات محرمانه توسعه‌دهندگان ایجاد کرد.
🔹
گراک بیلد (Grok Build) یک ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی است که توسط اسپیس‌ایکس‌ای‌آی توسعه یافته و برای کمک به برنامه‌نویسان در محیط ترمینال طراحی شده است و این ابزار با دستور گراک اجرا می‌شود.
🔹
پژوهشگران امنیتی دریافتند این ابزار در برخی شرایط، کل تاریخچهٔ پروژه و فایل‌های مخزن را به سرورهای ابری ارسال می‌کند. در میان داده‌های منتقل‌شده، کلیدهای SSH، رمزهای عبور، اسناد شخصی و تصاویر نیز مشاهده شده است.
🔹
بررسی‌ها نشان داد حجم اطلاعات ارسالی بسیار بیشتر از نیاز واقعی ابزار بوده و حتی فایل‌های حساس مانند «دات‌اِن‌وی» نیز بدون حذف اطلاعات محرمانه بارگذاری می‌شدند؛ به‌طوری که غیرفعال کردن گزینه «بهبود مدل» نیز مانع ارسال این داده‌ها نمی‌شد.
🔹
پس از رسانه‌ای شدن این موضوع، اسپیس‌ایکس‌ای‌آی قابلیت آپلود کد را غیرفعال کرد، وعده حذف داده‌های قبلی را داد و در نهایت «گراک بیلد» را به‌صورت متن‌باز در گیت‌هاب منتشر کرد تا کاربران بتوانند کد آن را بررسی و با اطمینان بیشتری از آن استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/450420" target="_blank">📅 18:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450419">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTQuy8qeE6q1ZW-GNn8lTgVBKLImJhZ2DqT60M_dKPcK22q64LGu8wCW87Ie0vfwJN2vGXhDT_2Z9N-oC-E9CLEM77lP6lvnDgyuPa4koXxkcJCk-oxMLvF5neWQ3eMKvahgGoZm43_yBCDE3mHl8yDlVB2sGEiMEo6A7-vxbw-sJI-EVETHhcfsrZ5p9vE6agtMi9iTBQnqufeXSh_5kUzpN2tAfbzY-nI6E7xvg0taL2wTZbO_zklC0FUbPjPk7aEX0T7Vtopir4xDasbXzOVMuavtrbr60oynvgEpYA-k8dhZegRfIa-ch8Dqwa3ehoUC87lFEF1P_C_UHDyO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله: حاکمیت لبنان با دیکتهٔ آمریکا به مقاومت از پشت خنجر می‌زند
🔹
نقش مقاومت در لبنان بسیار بزرگ است و موجب سربلندی امت عربی و اسلامی می‌شود، اما این مقاومت از سوی حاکمیت لبنان و با دیکته‌های آمریکا از پشت خنجر می‌خورد.
🔹
حاکمیت لبنان به جای بهره‌گیری…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450419" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450418">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGmqZj-HKbTEvJLvIfFDPQUZZk6hArh_k_hgEBtL-KEQi7rc3PgVPnWR7Q5TJJ2Kj_mScqEY6DrMurQHsO5o-MB0RjzNavOJ-FSeFxZeAV4WnGh12AMr_oKOLE1RGBGnjlVE86M_Ps94y7tli09LeO153kpCk6Qf4T6LIaBD8Lqs2ZGilD3JZ7G1EMEQ40ZT865mWeZXO8SKxL9WYhkeA3xbidbJ1vctML1cbN0yVn9RIL9K0D_vR_IKtdFzyxjXWF4HZupwuTPNKEpDsQerwXi4e5DhKHOI8cQss5mzN-KgJlZGGah22B1jHiR2LMJ7zrQGv6ReygHr9MVeHAAZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: عربستان باید مجازات شود
🔹
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
🔹
تجاوز عربستان به یمن سال‌هاست که ادامه دارد، هیچ‌گونه توجیه قانونی ندارد…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450418" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb730c5cdd.mp4?token=kflqE1U8USkWmZBap44MMfKbONNV1EDT7FVZkaYXEratpPFcx7t_pfhJrDJbEBe9etknn-4-kCsaFHOWgK-gu9HKPQP5aYvph-i0y8GUMFOm86IkJcK1VgRNRvG1GvMGia1QhtlaGg9teOl-5vqcAD5hc2dMjFiYk43hVnkfSxvEOQUKwTL4tH22FlEQiWx_X18qHuuIGzHCiCLOOI2vBolsZc_HkFyS-p5NWxdcwUpuNbopq9l0knjUsaxnkgHeRF3aM_DSuI_dajb7MseU1frftOGsj_GH4B95Yvn4W1-84K3cWGxi-rK-H8fvxaRmZHGYwJT768-aZxSUann9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb730c5cdd.mp4?token=kflqE1U8USkWmZBap44MMfKbONNV1EDT7FVZkaYXEratpPFcx7t_pfhJrDJbEBe9etknn-4-kCsaFHOWgK-gu9HKPQP5aYvph-i0y8GUMFOm86IkJcK1VgRNRvG1GvMGia1QhtlaGg9teOl-5vqcAD5hc2dMjFiYk43hVnkfSxvEOQUKwTL4tH22FlEQiWx_X18qHuuIGzHCiCLOOI2vBolsZc_HkFyS-p5NWxdcwUpuNbopq9l0knjUsaxnkgHeRF3aM_DSuI_dajb7MseU1frftOGsj_GH4B95Yvn4W1-84K3cWGxi-rK-H8fvxaRmZHGYwJT768-aZxSUann9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انصارالله: آمریکا و رژیم‌صهیونیستی در تلاش‌اند کشتار مردم غزه را عادی‌سازی کنند و آن را به امری پذیرفته‌شده تبدیل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450417" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc873432fe.mp4?token=Jo_JwLGRjBMbzTIcUb5F1wUNqyb9iRgPqg3ZmpwAamD797ingtNRIyVKpS4vvi-Ra5jC1d2bbLLJ8la3vGYPqKHv7CHKeyg8dZ22nz3C-nfYmJtNjq1EOekpooK1nnKsJO4afrLBaLdvDaF_l-0og-c38ScHQ4MTB9MKxeqAqiigbJz6KqJMVsgufZ0rt3OcUAFAC3o447aBvIHo0GTS8YIbHj1bxW6nBdtGlV3-kyX7npnjXu_InOJjn1HW20lZtM6U6zkSVkyMRZZQqFMI65fqvFmLL4i-wNf7WV5QQMXQNqjoLBcaUY_cjuUqHkePe-EJn7mA7L-hS3DiGZRA34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc873432fe.mp4?token=Jo_JwLGRjBMbzTIcUb5F1wUNqyb9iRgPqg3ZmpwAamD797ingtNRIyVKpS4vvi-Ra5jC1d2bbLLJ8la3vGYPqKHv7CHKeyg8dZ22nz3C-nfYmJtNjq1EOekpooK1nnKsJO4afrLBaLdvDaF_l-0og-c38ScHQ4MTB9MKxeqAqiigbJz6KqJMVsgufZ0rt3OcUAFAC3o447aBvIHo0GTS8YIbHj1bxW6nBdtGlV3-kyX7npnjXu_InOJjn1HW20lZtM6U6zkSVkyMRZZQqFMI65fqvFmLL4i-wNf7WV5QQMXQNqjoLBcaUY_cjuUqHkePe-EJn7mA7L-hS3DiGZRA34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار آمریکایی: امروز ۷.۵ میلیارد نفر در جهان از ایران حمایت می‌کنند
🔹
سانچز: ایران به رقیبی هم‌تراز برای آمریکا و غرب تبدیل شده و در کنار روسیه و چین، مثلثی قدرتمند را در برابر هژمونی غرب تشکیل داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450416" target="_blank">📅 17:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byPU766ub1KW7DAnZ4vW-z1oViabkXxDLbIEiGz-_y3TlsTim_1YrTytUOukR-_8EPSGRPQmfwVgThpdlDbfAHkK152DZwuSyXfSpHPWmlN9bOMo1HZuskXevps5c4uEJe-4e31DW_kBGKJt0DCb7jPj0WXy9UsyPM_VrYiqaxgoavdhQuWP_qoVH6NnOG4ncAwqF8fxKSOBbNF8kQCMm5oKJ-5Ss-UmWfNNnjJjB2bv_JE3EbwSGd4Px4m5sr2Ye15KT12fnHWvTKZl9TpkLs8YTxUdAf8CCk1CxOAGzUIqIp9S1TXFN_gNQHEGx_AKV7MeNt12sZ46iBlt9sv9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: آمریکا، اسرائیل و هم‌پیمانانش تهدید ثبات جهانی هستند
🔹
ستمگران امروز می‌کوشند از انسان‌ها به گونه‌ای بهره‌برداری کنند که در خدمت اهداف شیطانی آنان باشد و طمع‌ورزی‌ها و جاه‌طلبی‌های هولناکشان را محقق کند.
🔹
آمریکا، اسرائیل و کسانی که در…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450414" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwrlT0z_ojpyRv93ZL6iPf7kxVpeeTCDoLvt_qAgbEi0vYYxfGp7F4xJTzAYa3F2MIDClFFuM5ePBjUP0gNHZ_7TlNYCJQpoRXauD8KxCoZ9RiMXvAEx6ZvJ8NI-efAU16a2zyNIDX07wijW9Hyv0kioi_kypiHp5CXvApkpFCOgv7njJ1PB1zR-78o3owZpKOJIgPY7pHf_ts4D_0R3Hl8yLXW1ljlnvqoCxzldSPKhWH2dCHOvx-m2iqBu-IDkCFfF8yZgsp0lCqt5sWIU41T-X2WE-yYMn5ZDyE7eOo16iQLSnCDYhd7J_YODWRXwERy2aq-JkHeI6aSkXpBD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: آمریکا، اسرائیل و هم
‌
پیمانانش تهدید ثبات جهانی هستند
🔹
ستمگران امروز می‌کوشند از انسان‌ها به گونه‌ای بهره‌برداری کنند که در خدمت اهداف شیطانی آنان باشد و طمع‌ورزی‌ها و جاه‌طلبی‌های هولناکشان را محقق کند.
🔹
آمریکا، اسرائیل و کسانی که در مدار و هم‌پیمان آن‌ها هستند، منشأ شری هستند که ثبات جهانی را تهدید می‌کند
🔹
طرح‌ها و برنامه‌های آمریکا و اسرائیل برای هدف قرار دادن ثبات جهانی، از طریق غارت ثروت ملت‌ها و به راه انداختن جنگ‌ها، از فلسطین و دیگر کشورها تاکنون متوقف نشده است.
🔹
آمریکا، اسرائیل و کسانی که در مدار آن‌ها قرار دارند، به هیچ‌یک از توافق‌های بین‌المللی و قطعنامه‌های سازمان ملل احترام نمی‌گذارند و حتی به نابودی ملت‌ها و تمدن‌ها افتخار می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450413" target="_blank">📅 16:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450412">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0INOKf1CpQHn5gR5Hf4krfMbrkYVsKy5iMmKpnAQfYkez6R9MDCLOThrH8uNvlAQKJSc4yqxhIBxttDvlhfBELDAvGe-gQsT2jAZX35iYmxcxWVa0cTQM-NBXJBcpNXnDrYP1yGxxz60FrrEjl0UIfK_OxE7h9Ph61zQW0Fawt5IHvFWt38K1VemFwm_FIH4maR5jkUJ9lJZAYgij59xvCriLAKEBpqt-sZOD0GmrZ6WG1-P_JrYuuBZ4uANkJ6Zps-QVonU7zdbzBiYpd50ak3aNnRIS-c3Zx-9oBM744kGsf7OZ9jaymKxA6G0XWfZjdCQrYBkl3aB74Hb2AARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای رویترز: یمن آمادهٔ بستن باب‌المندب است
🔹
رویترز به‌نقل از منابع آگاه مدعی شد ایران از جنبش انصارالله خواسته در صورت حملهٔ آمریکا به زیرساخت‌های انرژی ایران، برای بستن تنگهٔ باب‌المندب آماده باشد و یمنی‌ها با استقرار موشک‌ و پهپاد در نزدیکی این آبراه، آمادگی خود را تکمیل کرده‌اند.
🔹
به‌تحلیل رویترز، هرگونه تهدید علیه دریای سرخ و تنگهٔ باب‌المندب می‌تواند بحران جهانی انرژی ناشی از بسته‌شدن تنگهٔ هرمز را به‌طور چشمگیری تشدید کند و جبههٔ‌ جدید بحران انرژی و درگیری گسترده‌تر بین ایران و آمریکا ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450412" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQPC-R3VYh8It4xEIPwO_K-RO76VBoKSvvl9U_AbX_5IVWqPOwHs2Eq5nND8geLnNnpJLs6ShX5-3ANzrf9IwDT1VcEL1G5LgkBM-8Rz0-RXjQi16VSvaBqBQJ99k59qF6X1goRinRe4DlyqTfKTbCHehiAs9FFM43L-7ewhgq8-hFX9tUong9WHqWwvjeBsD68NPCXDJPfUfGtr6G1OB1tytjsHUcylrG9mf_74-XM__lqKneale_8yHooWxmMiIxWHd3WKQ6xRf_DVnH6iJusy7ZOoEtRAapMXQZMcTVdzCXiRCBtV2DH10wkAD7ZyVjq5oZ8N5-E70WNAXMqLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست طرح قطع کمک ۳.۳ میلیارد دلاری به اسرائیل در کنگره
🔹
بیش از دو سوم اعضای مجلس نمایندگان آمریکا با لایحه قطع کمک نظامی حداقل ۳.۳ میلیارد دلاری به رژیم صهیونیستی مخالفت کردند و به این ترتیب، این لایحه برای بازنگری بازگردانده شد.
🔹
این طرح از سوی توماس مَسی، نماینده جمهوری‌خواه کنگره ارائه شده بود و در صحن علنی به رأی گذاشته شد. در جریان رأی‌گیری، ۱۰۴ نماینده موافق، ۳۱۴ نماینده مخالف و ۱۰ نماینده ممتنع بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450411" target="_blank">📅 16:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNouirsCohRShR3zGGxQOyGFz8dMYc_mWgeOlzHXC58bAuy_P12XV2VQQyRYjI6Y9tPyCqB6G7dL6SOkkSats4l9J2lY4VCE4KX4qsKQHQPGUGtvEqnF8fPrMdiIuMWjKndsiOzol-DDiY6E5p7wKOK3TuABuvtQRhD0LvuqglwonVR_8J3tu05HugPoXDf-OEq7W-Bd_zwoePnYI6IjAn3-pcJSqT_gohYeh11A0DQ_R2qn3tohl0SaP6hiR0R6XVhFovdtTLr9sJ2Zxlp9K0awjXReizVhaHsu62hnT5heDKgDBQlKsn_8iH-xJx-akm0rGiAcyMpU8rqvqiUZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا دوباره محصولات خود را گران می‌کند
🔹
مدیرعامل سایپا با اعلام قریب‌الوقوع‌بودن افزایش قیمت محصولات این شرکت، از مردم خواست منتظر اعلام نرخ‌های جدید باشند.
🔹
در این نامه آمده است که توقف نماد با هدف جلوگیری از ایجاد ابهام در معاملات و حفظ حقوق سهام‌داران…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450410" target="_blank">📅 16:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkRSLzvEHY7MRqYaCokchuxpm5H2qzUcIbNFXCcWs4V-_SLwQfg5r4FIajYtlh9RsN8-33_4pKoJXwGCwXHE6FlvSC52JxV9fUpUoi-trZTm8zJ9_Rs2TLdtWz1BTajWLBZhvj1ND0th1LskThcQ0yxkza9GkhHR_IKlHaZsl6KobcICmBYe-LwN8N_xLq5skYE9PjzpqJC7o7dQw4YrbHhR3KXOIWIvlBxRbYF4HudO8CGK7dyUcmxMB_sZC1UafrRyqMDKqi7BD9f5alF7SILzgt2iumkBs_Ty5IytXsUyauty4bfJn4pXmjqv7GZcgVXEI_ooiGH841oUhPluww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ توضیحات دانشگاه علامه دربارهٔ برخورد با کارمند آمر به معروف
🔹
دانشگاه علامه طباطبائی در واکنش به مطالب منتشرشده دربارهٔ برخورد با یکی از کارکنان این دانشگاه به‌دلیل تذکر حجاب: این فرد اخراج نشده و صرفاً با درخواست کتبی خود و به‌دلیل مسائل اداری و اختلاف…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450409" target="_blank">📅 16:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450408">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwIIEp9qSwYd3qNY_o4QWMR0DtjQmfJBeBYJ-qxqnag_NE-zRo7GV1hglSwlRe15uSw2C7MAIh5NBEpcFXMvMkIW74s8zyUDKC8Ei7KhtLlDzDtJ67F0Z4A-p5TSMwTuqWG8N6NHhAQG4DKAnC4hkCCSi5pGbULiu_xpDDffknN0uwVUtQ4hRv8T1Znpaj39I2mOoZUeSun8NZSUvxAcUHc_2TsrzXjM-iR6wyjG_jhM1kSDrB2xCE7hNFGnrdKzdVVLNf8wa-82sel4YLJVxEKt4p5SntRZGxkGznGZyjvY9B6fUVx6YIAmRfwFu5299L3ZmwyGGU09pkBpZXAAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای آتش‌سوزی مقابل شرکت مینو چه بود؟
🔹
سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450408" target="_blank">📅 16:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450407">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b62e7292.mp4?token=JIRQKLmPuL4NAIgjkppljU3Fk7Dh0RlLPyx1sg8mSRCuAEUSlb0VCGm2S0LEq4XvdFGTdcCmSRaVU2Stb5Oj2cjbXHhd3ds4rEscWsKoC5h0S4aoi_1c4FXhOURuccBfBDXSe_bsppUj2WtbSw-7LoIOHfCN4PU4UyfvH0miKDCi82CeJPFWE3fViwVsE9g0pujd8GvGGGaCutXPX-5V6cPugeLAfJGFK77q6s8xYhvfr1o3eLHHDHnw2DWEXkgp45v-QyabEt9bRtoYSIwK2gYljQZUAdDAzReJ2GS_LK7cEDfSVEvPN-HJMbTHEl9wCN6lxBo9diY_fSnN6kJqxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b62e7292.mp4?token=JIRQKLmPuL4NAIgjkppljU3Fk7Dh0RlLPyx1sg8mSRCuAEUSlb0VCGm2S0LEq4XvdFGTdcCmSRaVU2Stb5Oj2cjbXHhd3ds4rEscWsKoC5h0S4aoi_1c4FXhOURuccBfBDXSe_bsppUj2WtbSw-7LoIOHfCN4PU4UyfvH0miKDCi82CeJPFWE3fViwVsE9g0pujd8GvGGGaCutXPX-5V6cPugeLAfJGFK77q6s8xYhvfr1o3eLHHDHnw2DWEXkgp45v-QyabEt9bRtoYSIwK2gYljQZUAdDAzReJ2GS_LK7cEDfSVEvPN-HJMbTHEl9wCN6lxBo9diY_fSnN6kJqxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ دموکرات کنگرهٔ آمریکا: ترامپ احمق مناسبی برای نتانیاهو است
🔹
کراکت: دونالد ترامپ دنباله‌روی بنیامین نتانیاهو است؛ همین تبعیت، آمریکا را وارد یک جنگ غیرقانونی کرده است.
🔹
من هرگز طرفدار نتانیاهو نبوده‌ام. نتانیاهو مثل نسخهٔ باهوش‌تر ترامپ است. متأسفانه، او احمق مناسب را در کاخ سفید پیدا کرد تا دنباله‌رو او در این مسیر باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450407" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450401">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fas7YeZMWplGc13A_JmnWiiIQgCS-Rf25Nwo4UyA9HkFG3jjLS3TAHR8fk0bzKZZynmivAZjC1iKmdXdtV92w4-Bq8zWFu2lPZ3MndeyVK_ZbXVbmTSKIxoE2jmPdZuTBnl8DBYWDbLu_ZQX_nQBqi3mMUiyza3AYmu7V0XgI6QUn7hLKwYNxU0ZOqjsocWUDfqENb1JQWCpBYGDQRV0gYEIrogOisnMSN-26AuomOF28ziKpu2fqYCMv2bSOGwaJtV1C2zF10GuiXr5vu8V2ytrowPNkgACVSNDTtvYbUi9o2D-nCgLWjFP0h96hYJk96CfR7AgLytXksUE2glDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arCwckFlQBXGpmePfwkT2jMBxZUUbG__WGPKzIEJJBhvfprc0iSCEzWGLyeX6PKAE9-9N-NyynBoZKYMR-z1edqP1P1ddIOFhg8vP6EDnlroLEDzUJnCOdrnmiN9RpQfEDOs4rj-ZaW_DmO9LUjA4MSRiV354CSvHUM-3ApgSo-1y0gtO8i_eU76e6sO5E0yXYY5vWfU67NFSqTx-K_8GPo8zNyNLRGmj7A71369K1jObKpHGtTJ8oZNqrUQqiLvQYiaO8yhPokoCsicUNiza9oLRJbe-BYqVPKQpUsGq0sFIZe0PO5HWUNnxOC9ZpbGWmkjj_Mrsr3c-Z4PkOiMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUpfUw34cUxV5XPu8RgkoIx0K-SpJOzgHeOM3TM61idZHFj9JyapxPPstJ-AvW34RfE3aJWbYhz-iiHj-VZcIDU73837_UfPNXTwfOVVYjEMwaDehMJNdk6IHnWnJdyI5H6jF3fknkaW5r5me3IOOCpYMJFt39C72AZf-X2zgKLieLKFKi4kt0HE--mwKDBGFXeZmZ9OLeg4BR4Vp9lQJzNYElQePnnWdBPS9zAY0xePt02qo6Cbvuf6Xk2swzhjIs1wgefVUiOR6OZ2WqKBwMGRVnVGUcTABGzXdmpJQMxKMMWn7th2qRdbwka27GIuWugZ_7R1aZ7efGjwnsPfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQLyR4YKAtsMpm4EX0N3H6iuqy9VhFpb3AD0BSf8Jzi6tdv_2AICy2v-nyDjS5H46yKW1s3dyCUiorXaI3IhV9SGtkVwUUdxb9qwFBSC_1ly7qjpHwYCLmdXWzONRupVi3RoUjwEzR-Hdn_xdT43ggaCeJ8iEhYD_BwbXj_6Z-c5IZAdStCyz25kOaxgVRgW2rWYMlHch1wAgSqkVb1Ak06-tjwYv1lAT8vuDz0H9hyWWygzBZUjv2GqBu49wuURnKL2u3ezVDtCYFTqOUQ32RMDZzXsV8621Ahd2_qX1oi7ybco8y3JOQW2K1YsvQRSLDi0A5DWq9mkTo4mLnGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIKXAN8YSHU4PPlbKKd97S2tVGumJjtaLaEFWuAP_irlA9qNgA3PforXhOmuxIDS5KMp0FuJf_hllEWoqn0WNtBX-yjEVN_Uapf74BbSEQYWafB71RAV55a7G4YDzC0QG6s31cepYnvzXysCSM--UDnJh6wiiVVLMk43UA7xUPWOKJU5JnwBZM7WjPyYMw25UND_JqvdAR-QrxWzdxfUabQIx_nBlRyR5OWko0h5mUZIEkj7kl2Aogmt5rjOv1vZFDPW8lPxlTHcZwae_GdM6jxSfoyiu_aPN_Jpp-ZlBxf-8B2DaEzQPbP3MhCFxHJkQFriXgkL1AKj8HjD-dbBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBlHb6OVqKqL9uZkFIzf2PKG9PnwfZl8HupUOh8E4M01jGjK497Hoj96lSKdKAczWHEp5xniUBsVZVkdVn0LVrmayUxvzylydhAYGHeIWTWgzvZhGgAyjn2eHoHCInFZUIi9MPf3SKIRsDQbXg-yW9847ADPY5JoZRM3aE0J4Qc4rALQNEzXZeRJBX2amuLwm59VuEqbY8vIUTiSuOtrDk-fVq9vFVFTC_a0xaPskhuZ1fNMFe0KrD6VERuaMtF6uj_8UPkrutrGOkltNjJten486UwPdJn6_tahBieRpsU7HCfnn9VBXhE2oov9pahhG4MqX3lrgiJmxbQNxCNxng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاش دلتان برای جنوب ایران می‌سوخت
🔹
در روزهای اخیر موجی جدید در شبکه‌های اجتماعی به‌راه افتاده که در ظاهر حمایت از جنوب است، اما باطنش چیز دیگری است.
🔹
«مردم مظلوم جنوب ایران دل ما پیش شماست»؛ اگر در استوری‌های اینستاگرامتان چشم بگردانید احتمالاً یکی در میان محتوایی شبیه به این را در صفحۀ سلبریتی‌ها خواهید دید.
🔹
همدلی و اتحاد بین ایرانیان همواره زبانزد بوده. خصوصاً در دوره‌های سختی این «یک پیکری» بیشتر نمود پیدا می‌کند؛ اما چرا همۀ این واکنش‌ها در شبکه‌های اجتماعی لزوماً به‌معنای حمایت از «جنوب ایران» نیست؟
🔹
بخشی از این واکنش‌ها از سوی کسانی منتشر شده که در ۵ ماه اخیر در قبال بمباران نظامی و غیرنظامی، زیرساخت و مناطق مسکونی سکوت کردند؛ آن‌ها نه شهادت کودکان دانش‌آموز میناب خَم به ابرویشان آورد و نه دلشان برای کودکان ورزشکار شهید لامرد لرزید. اگر هم حرفی می‌زدند درمورد قطع اینترنت بود.
🖼
در برخورد اول، یک سؤال پیش می‌آید:
🔸
چطور وقتی «تمام ایران» بمباران شد، سکوت کردند، حالا از «جنوب ایران» می‌گویند؟ یک استدلال پشیمانی و جبران است. اما چرا این فرضیه چندان مقبول نیست؟ چون در حرف‌هایشان خبری از مهاجم نیست؛ گویی در جنوب زلزله آمده یا جنگلی آتش‌گرفته.
🔗
ادامهٔ مطلب را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450401" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450400">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb9b129d7.mp4?token=VuEsGiQofcYXh4sksUGwuBOEveSDi4MNIUkEjPfZJYm4IBbN3onrhvBbH07yquoTJJqODE2Tvua-1Wel7llXozVmh_zyFkCei_KyIeQr3X7MNEO8pxvxc8LCqw3dvMuYaI6yS-ziw0DZa36P-R57RRx4sVs-lFJ11ck6oObCqF7SoE6Ts7hGdl3tTogadzEoetnlgAoyH4_JsUZvt3EYwsb-KN3n0oVOd5ido9JauXY9wqNuzWLxjR3NV7onYFay7T87RToWI-zzKT9hrLLGHJApdBiF-x749iLm6kJBf2sbHkqAUYvrpxDTzxjzXZI1sZdcEBsGDmRvyQxUzsv0JqKljCd6v5AmlQM0Ci7O5hBU4hbxGb0PqztWAif5As4-Tf-dUCv3DOj3avmRAqjsRKzOZy6x2Po2TG9hlRhugTyh-WOhdS23lanrQIE6aUjPrlSBp9sqhAviaX35WuYKlIy26TBNpdVf-bbUGy3jrUwfIRCNLELeNEi1hEybb4h4h5i7-kYvsacOczWMGYqkXfHO87KNUSDYk47NGdObcnEakcOLRsdxbCFtomGr-A4n8gWcLLpHiD4dPoljKxNDVAn1tjuiPE3mMnVHkVWtYx-3bYbRi1ESUhWlP-1aLtu4M_UMxkq-8vOM5Mrh8lm34Jv7JxMapZwQmUxzIbRZx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb9b129d7.mp4?token=VuEsGiQofcYXh4sksUGwuBOEveSDi4MNIUkEjPfZJYm4IBbN3onrhvBbH07yquoTJJqODE2Tvua-1Wel7llXozVmh_zyFkCei_KyIeQr3X7MNEO8pxvxc8LCqw3dvMuYaI6yS-ziw0DZa36P-R57RRx4sVs-lFJ11ck6oObCqF7SoE6Ts7hGdl3tTogadzEoetnlgAoyH4_JsUZvt3EYwsb-KN3n0oVOd5ido9JauXY9wqNuzWLxjR3NV7onYFay7T87RToWI-zzKT9hrLLGHJApdBiF-x749iLm6kJBf2sbHkqAUYvrpxDTzxjzXZI1sZdcEBsGDmRvyQxUzsv0JqKljCd6v5AmlQM0Ci7O5hBU4hbxGb0PqztWAif5As4-Tf-dUCv3DOj3avmRAqjsRKzOZy6x2Po2TG9hlRhugTyh-WOhdS23lanrQIE6aUjPrlSBp9sqhAviaX35WuYKlIy26TBNpdVf-bbUGy3jrUwfIRCNLELeNEi1hEybb4h4h5i7-kYvsacOczWMGYqkXfHO87KNUSDYk47NGdObcnEakcOLRsdxbCFtomGr-A4n8gWcLLpHiD4dPoljKxNDVAn1tjuiPE3mMnVHkVWtYx-3bYbRi1ESUhWlP-1aLtu4M_UMxkq-8vOM5Mrh8lm34Jv7JxMapZwQmUxzIbRZx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایانی بر سیاه‌نمایی افراطی
اعتراف تاریخی استاد خودتحقیر: ما هم خسته شدیم از این همه سیاه‌نمایی کردن
به همراه اطلاعات و تصاویر کمتر دیده شده از ایران زیبا
@Fars_plus</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450400" target="_blank">📅 15:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450399">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlFP8usjo2LzSo8_MtSzodh-_oWKTs-mEJRwsrWmtKkcwJY55oQTTjdYUEhDsLrlfG484SnYcTGqYkysGjroc0ZtPth40IJYrQKYE7qxj2LPBb0VhHLa0n8Nn9AkwxSp1RsparOgUpybhaZaS4EMGSg2E2c_-HLT-n6hwmR4PZVP3Zl7iOFQu4lzPliO8Sm6BJEpF7UGXufpkCZWnuEdK0uySh85gpPfnLQhI4kAHKcJT5WLS_tPxG93Djf4MWxNVZdOBLWEc4o0ayKiVyqHynLD0DINVZmGsAPF72nIVK_Nu73l5OmEV5_K91C-UOD8vfEAUK8yNGMltgBEOp7ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450399" target="_blank">📅 15:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80691e93a.mp4?token=rEQzm-Fv-F7lmz2M0E6kUeTTZBpEu-HOm0Z_7X7bXu1dGxDgMZ48ZBxL4tPxsVkkyvmCwhVFZmMoB3VOVTTX7OKOgnnevIq1QyxVQQCcG1_352NltwLtTo1u5_VUORE3nLP_ocKLZwsRTSOrYdocCl_uzWxEfu0-FjXbuaj0S9oFhTGVUGBkE-wn0h5JPq3Lx_0-J79i9R38SVg5q86NDdCAhApP91pbJi83hoabVuE90RfugUPxG4udDqGCA2U34GhgAttI66zdn3bEiyKyT1M0UZT6UeESa1sAN_mt99T5rnA9r5AnNiDhllN7LNellf_wxc-VIrTrvLeVXu4IHH8lBlxc4b46d4Qga9iEQqqcUoGoGhV3itu77g7jqirqPOdNx4nDpEZN2H8-gupqdXG5mpPQXwSbuB2_BXoJOU4sNgVeeHxGYfEsiEoNw6UG9E19LxfJ7a41yJhNEFlwC2-3eIUc4KvKTQRzkr9k58Pn0xgMipTv0q0M0PrCDTlqNsVHco5pEZJslu3wjwFQvzpngjqFg1hdQ_AXQyfGgRllaf89Raj3fU6Yb5TsVo09BDzCI1l_Jj8XNHFFkzKeuD4FGSk0Va4ZFir4W2F4_XGwjZefx1qjRNRMQbDmbBo1Kg7UfYTlN-3B4ZiPYuvKfWQb_MqROuGwnrtvTv7GDqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80691e93a.mp4?token=rEQzm-Fv-F7lmz2M0E6kUeTTZBpEu-HOm0Z_7X7bXu1dGxDgMZ48ZBxL4tPxsVkkyvmCwhVFZmMoB3VOVTTX7OKOgnnevIq1QyxVQQCcG1_352NltwLtTo1u5_VUORE3nLP_ocKLZwsRTSOrYdocCl_uzWxEfu0-FjXbuaj0S9oFhTGVUGBkE-wn0h5JPq3Lx_0-J79i9R38SVg5q86NDdCAhApP91pbJi83hoabVuE90RfugUPxG4udDqGCA2U34GhgAttI66zdn3bEiyKyT1M0UZT6UeESa1sAN_mt99T5rnA9r5AnNiDhllN7LNellf_wxc-VIrTrvLeVXu4IHH8lBlxc4b46d4Qga9iEQqqcUoGoGhV3itu77g7jqirqPOdNx4nDpEZN2H8-gupqdXG5mpPQXwSbuB2_BXoJOU4sNgVeeHxGYfEsiEoNw6UG9E19LxfJ7a41yJhNEFlwC2-3eIUc4KvKTQRzkr9k58Pn0xgMipTv0q0M0PrCDTlqNsVHco5pEZJslu3wjwFQvzpngjqFg1hdQ_AXQyfGgRllaf89Raj3fU6Yb5TsVo09BDzCI1l_Jj8XNHFFkzKeuD4FGSk0Va4ZFir4W2F4_XGwjZefx1qjRNRMQbDmbBo1Kg7UfYTlN-3B4ZiPYuvKfWQb_MqROuGwnrtvTv7GDqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در موج‌های ۸، ۹ و ۱۰ عملیات نصر ۲ و در مراحل ۹ و ۱۰ عملیات صاعقه چه مواضعی از دشمن آمریکایی هدف گرفته شد؟
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450398" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqFP_K-6nE89Uuej9IaanRrMeWCYXhNDxFStxKOSS8fIgRDlQcKfwVz13ojuxfXHm-YLE0XTH1BivkfWFzd8W-h4zmgXXBgChIgNZtPq9sLx1MaqMtvX_geOz3-T63PQbX73MsiTjG5eyB6cSbNg_p94h6KeQNqEdJevSHoRRJntIpAAksSwLtpChXejx0G-VUYaXlYs3pjm10XcKPZklCGScoRpdkfPZsUpKVeSkfqBPc1QTuWA5SoIk-z4LjI8-d1si9iif_2vbRq8hQ5jzsUhRNXOjv-vg7YV9k-KoJCxX-IQgIvD6zwVKOAMf7eDVI2mgQcAX47RrE72gpfj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش کویت از درگیری پدافند این کشور با پهپادهای «متخاصم» خبر داد
🔹
حساب رسمی ستاد کل ارتش کویت در شبکه اجتماعی ایکس دقایقی پیش اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450397" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450396">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whg_uX2IGLaSFn5P3_3g4XwblLIwgBHe80e-yQueAc9ce7M4inl7GKDNqFnOr6hP6URhSp5hindUrdncs-AwspuTPi0reQGu_zgOLiWFq8jtBkX_pB06NEnUaWeZGIdzLFx7Lruj-az3JQYYVk3Vj8Ev6L5KmK1iNIDy8g_mWHG_NO_8fmd9oRI6Biyv1fms1q6Gl5H2HyC-gJ6f_cOTTVcDVZcQCRwlQ6_NqVP6mZcVchYEM0n1elBz92LTwclsaNL67Zx49H7pwYrC-arn61B5Ir7lqPPnN1loLSBdLEkVnOAwZKBk5TYfMj32FlHUqZafR7Jm-mI4Dn1hJmpytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورعلی هم پرسپولیسی شد
🔹
پویا پورعلی که در پست هافبک دفاعی به میدان می‌رود، با امضای قراردادی ۲ ساله به جمع سرخ‌پوشان پایتخت پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450396" target="_blank">📅 14:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450395">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c91f64bd4.mp4?token=bcjU1K8e1Fko3MJmBVHj0pgYIa2Kr4lPEy9MPUSriMYwZfW_3u961j3jIQWJrwO_QZqHKEFNOV37qujT9ssvtVR34NFL45365kpSNN6RnotqOeY4KsAgzWzlFTJMTTwlZAuqdX14LIIexaq4GBibhw2-IagKzdSksGarXkWQ1YMlJOWkg2oTTkI3450KzTWYRpR9RP2mKb4fL3M8SaDGjhsGNG73n4Y4V6QTTCajA3_glPHERhP1hVtR7stHbuxre1mDiAjAAZ6NvcXX3pGPpXCVAL14c65GPhckkH3f41My1Gs-rmHcpD4faOpafpq1f28Pxd9c6Mrlmg3zmfVl_DmQkOUwLnLm55w8OIjupSMpA3sypdMCrUs_tmBsAFOEb-egIGVktH_5TDAOyaSeS_QrxpuIdz0jJiGFvQhwWTOu-9NJY4_ik3A-KXXnW5aJeP5hOy6AgW-eHJLXMJXNvWlCpTP9uZaLiJCv9yNZwLRmxy3Xq30-neTMkOamZg6GOvB0kV0smY23A59vHKG-xgVSmJD8uZVsQUTUXFN1PNd0W932ahi-1vXbhiqp8wM7CkZtBB8fK4OqV2BpnXojBBCqyGmAFrvnt_Rj3v2qBaPcfKUR2e20go_bkrY4vSuNxpPJIqtvzEfhkI6Czrn3uo0BxGlkiH0XUTmw7weVYVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c91f64bd4.mp4?token=bcjU1K8e1Fko3MJmBVHj0pgYIa2Kr4lPEy9MPUSriMYwZfW_3u961j3jIQWJrwO_QZqHKEFNOV37qujT9ssvtVR34NFL45365kpSNN6RnotqOeY4KsAgzWzlFTJMTTwlZAuqdX14LIIexaq4GBibhw2-IagKzdSksGarXkWQ1YMlJOWkg2oTTkI3450KzTWYRpR9RP2mKb4fL3M8SaDGjhsGNG73n4Y4V6QTTCajA3_glPHERhP1hVtR7stHbuxre1mDiAjAAZ6NvcXX3pGPpXCVAL14c65GPhckkH3f41My1Gs-rmHcpD4faOpafpq1f28Pxd9c6Mrlmg3zmfVl_DmQkOUwLnLm55w8OIjupSMpA3sypdMCrUs_tmBsAFOEb-egIGVktH_5TDAOyaSeS_QrxpuIdz0jJiGFvQhwWTOu-9NJY4_ik3A-KXXnW5aJeP5hOy6AgW-eHJLXMJXNvWlCpTP9uZaLiJCv9yNZwLRmxy3Xq30-neTMkOamZg6GOvB0kV0smY23A59vHKG-xgVSmJD8uZVsQUTUXFN1PNd0W932ahi-1vXbhiqp8wM7CkZtBB8fK4OqV2BpnXojBBCqyGmAFrvnt_Rj3v2qBaPcfKUR2e20go_bkrY4vSuNxpPJIqtvzEfhkI6Czrn3uo0BxGlkiH0XUTmw7weVYVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از درخواست حملهٔ نظامی تا اشک تمساح برای مردم جنوب!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450395" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450394">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6sEHv3qmMeRvddZDv3kBjK-oB1_B5pIvco1J0EPoxPOzQuDDVmpYNOS-dcUna2YbqQuRvrfuc9dI9Pl4mBRlcGj7yLjDvn760wh_y5vjzYuq259PwRacxg5MA3ODHj9yCRLXA-R6UbVKdq224-MJmBNttph4CFcny75fBUmDLlyj4dCe6MTA4cSXypT7640ZUAvgx_sxURkzGseKclZbGbpvCzpELY5vaVvr-gDx-CaoEqAKWpyuM0h2_8GP8EyTc8XX0WdvvWzUpX5mbkt8yGvh4xTkIptP9ILjANN67utAsBA0Fveph9xriHEz-oxVT_LnD3WzBLmJLWaBGfvhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم گرامیداشت سردار شهید محمدسعید ایزدی فردا از ساعت ۱۷ تا ۱۹ در مسجد امام صادق(ع) واقع در میدان فلسطین تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450394" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450393">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت رفاه اجتماعی: یارانهٔ تیرماه دهک‌های اول تا سوم واریز شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450393" target="_blank">📅 14:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450392">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f343b822b4.mp4?token=l2_g46Q8c4c5z5f-RL-iemufwiM-a2AFmuq0KgjlbZYhXRjA214XbWfXSU0ZMAEbyWAO8o3HNQObAjzHWkR80yIz1hd-SXpZcRd-G5X_stIdNqQKkZEEyEG1xWbndzKrlhOrkttDX95GuHSDZcSsB2BDhV70X17astKP0K6HeQFRh5cwcJTyi-B2KB1CQuwTTBLGoZ5sMyMeHaBWFzblJvryrPpWao_pn9H_3kGYsj7Zsa2ILRVzDsDiw8Nuzf4c43wImeDODeOal1fwqgN_chmSVS__6FIk6h9iydeJo2iEckwGL2zqoAUf1Bhlk7uUCOSOMRhhdRQKdkkJr6lDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f343b822b4.mp4?token=l2_g46Q8c4c5z5f-RL-iemufwiM-a2AFmuq0KgjlbZYhXRjA214XbWfXSU0ZMAEbyWAO8o3HNQObAjzHWkR80yIz1hd-SXpZcRd-G5X_stIdNqQKkZEEyEG1xWbndzKrlhOrkttDX95GuHSDZcSsB2BDhV70X17astKP0K6HeQFRh5cwcJTyi-B2KB1CQuwTTBLGoZ5sMyMeHaBWFzblJvryrPpWao_pn9H_3kGYsj7Zsa2ILRVzDsDiw8Nuzf4c43wImeDODeOal1fwqgN_chmSVS__6FIk6h9iydeJo2iEckwGL2zqoAUf1Bhlk7uUCOSOMRhhdRQKdkkJr6lDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸ کشته و زخمی درپی حملات روسیه کی‌یف
🔹
مقامات اوکراینی می‌گویند که در حملات موشکی بامداد امروز به پایتخت اوکراین، حداقل ۲ نفر کشته و ۶ تن زخمی شدند.
🔹
رئیس اداره نظامی پایتخت اوکراین گفت که روسیه در این حمله از موشک‌های بالستیک استفاده کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450392" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450391">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9b24b51.mp4?token=KNT9OAX8NQPh23g6Gy9qggohBFwB51PpkBHNI1pm2_tQMzb97sozUXQP157Ff2UjxD_rvl1p7xjcDaPt7bLMVW-jovA4WPKT2zE4_aO4705Is37B1gqne9jsc1BlEEwbE6BH6Z8rKvXLuyncGAHPsXN3prySCxfU5QAYT8jD01tm3YhfUWiSizJ6LqDF8Iio33za_ozuq0G7DhPligOSUVrIMJdOutMnEP8HYayu_GDbuPAldXZwJoivo-9SRuy2kZhiwFw6rRWwWI5NRXrQIE5XALDXPni8UjS1HHbdAsbTrOcCendxR62o4xR9UZmsxpLyIF6ERQPtNT1NmvW29g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9b24b51.mp4?token=KNT9OAX8NQPh23g6Gy9qggohBFwB51PpkBHNI1pm2_tQMzb97sozUXQP157Ff2UjxD_rvl1p7xjcDaPt7bLMVW-jovA4WPKT2zE4_aO4705Is37B1gqne9jsc1BlEEwbE6BH6Z8rKvXLuyncGAHPsXN3prySCxfU5QAYT8jD01tm3YhfUWiSizJ6LqDF8Iio33za_ozuq0G7DhPligOSUVrIMJdOutMnEP8HYayu_GDbuPAldXZwJoivo-9SRuy2kZhiwFw6rRWwWI5NRXrQIE5XALDXPni8UjS1HHbdAsbTrOcCendxR62o4xR9UZmsxpLyIF6ERQPtNT1NmvW29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: رادار کشف و کنترل هوایی و ایستگاه پمپاژ مخازن سوخت جنگنده‌های دشمن متجاوز در پایگاه شیخ عیسی بحرین به طور کامل منهدم گردید
🔹
مردم همیشه در میدان و بصیر ایران اسلامی! در پاسخ به جنایت ارتش کودک‌کش آمریکا در تجاوز به پایگاه‌های ساحلی و بعضی…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450391" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450390">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV2-HNdIaW5k7T2C2EQZbyel7jGRJNb_2WjIyPZxORMDd2nPpxVmL4ol4IN3rZUhjLqAzo1bQHyFcawfyY0ByeiTk1b-fquP1QBdk5--m_XyCMt6xF0ezXYRxWhz63wP-FgzfifjEFKNsmUhOaXlZrf7NrHaSkm-H11VY1GUwVO4bFQDMQ6z96WqVjpZJ2fyLKwUgZ26fumIEYQn0d9WhABGO1BWFj6THeuU877Ma3Lx8TtpKG0Hsg4iqGSVAX49KTOdWQNSnZKCao3zCqLIX8q6HOpdHnjhgWHCMAmDGcFc8EyaOJKcIO93qcpUS3xyFauhYx7TRHVPv79qDeYXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع به پرسپولیس پیوست
🔹
محمدمهدی زارع، مدافع میانی ۲۳ سالهٔ احمدگروژنی روسیه، با عقد قراردادی ۴ ساله به پرسپولیس پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450390" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450389">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gaDT1rIxQxLFQjcnAd5VCHlvAO2Sqt0jnLpCVmX6GpRjfrdZPllZixSkXW9ED-IPqKYZ4KtleOkFdZsKWbQfQ_T--uzCzX48OjJkCdRZGZcX5ikuz2UVzGHvCjCczWu6__ISqmWinMPUkDAzu1B5z2dcrIat-pBuNwy8B75PZ2scuw6--NO8PbeN99otFPuCmHzXJ16IpabE3_SPNfwhhtZrhaPHX9llTy25jQf2ztzt2RowpZT5p5M0s5XTQJRl7xMkSqvWoGSvIZ0FfKwYVtPCTWdwWCWK6LUIBtvB6DGRuEfGxebdRO72QUUKLObYpeCJ1Vh-2vO3NeajpXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد ناشناس بندر نفتی بصره را تعطیل کرد
🔹
شبکه‌های الجزیره و رویترز دقایقی پیش به‌نقل از منابع امنیتی و نفتی عراق گزارش دادند که یک نفتکش در بندر البصره هدف حملهٔ پهپادی قرار گرفته است.
🔹
اگرچه این حمله تلفات جانی یا خسارت جدی درپی نداشته، اما مقامات عراقی عملیات بارگیری و صادرات نفت از این بندر را به‌حالت تعلیق درآورده‌اند.
🔹
حدود ۹۰ درصد از صادرات نفت عراق از طریق این بندر و دیگر پایانه‌های بصره انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450389" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450388">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BItrkYM2vHbEFaPx7oaxrK-E3BzlbqD26D13CxfSoQDGUl_0Zsa7vZrY24X10K4Z4sVvcnX2KjNh5YWeJhMEhBdYPFWVhOsk_VPcYojrXUqfMbwZPqbpz7SKI2CIfDbrx0ZBm20-PXXs9dX5K1eQzUA9Bb8aOHJsK_6BEMCGidhLsPEhChMpMtwD1SuFr__QHCGAQb06xUf27Ti4bjN6hl-axDxNbuIIa0Cf9X_Lrh0CrWASco5dHVy8Jtq_9kpnZHffoO7VF1i6JGze9y0OP4U2ziq7y50ImIXyG_V0dm32K-8Vxm2oRGqpidNAev_SGKG4onCMpkXHnpsT6VMoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان والیبال ایران سهمیهٔ رقبت‌های جهانی را به‌دست آوردند
🔹
تیم ملی والیبال نوجوانان پسر ایران صبح امروز در چهارمین بازی خود در رقابت‌های والیبال قهرمانی زیر ۱۸ سال پسر آسیا به مصاف کرهٔ جنوبی رفت و ۳ بر یک این تیم را شکست داد؛ با این برد تیم ملی سهمیهٔ رقابت‌های جهانی سال ۲۰۲۷ را به‌دست آورد.
🔹
مرحلهٔ دوم حذفی مسابقات والیبال قهرمانی زیر ۱۸ سال آسیا فردا برگزار می‌شود و تیم ملی ایران به مصاف برندهٔ دیدار چین و پاکستان می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450388" target="_blank">📅 13:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDzUGrCsdekkokTo91FC-4jLBD44I91lQtSOPDaEDVrwO9xN2xZkc-Y5bm-bm19--MlSa4V_7_ZcZrB1cJSvi5GgBnQW-qsBf1RcihYvpC7Kaw86jaxPojwCoo31RJ_bj_3s2bXuswpD2EUQ7jH6WJwdgVrG3nt329XvDhM7TuLEDR16vUV73zY6B-AfUiAmQvs5XMMnf6Vt1paSlTFIydvjcveq8pw-wV0dkAnwKkT8J5dfUQfHDS4dio7rdOGIwUttpoy2Enc1K0RegGoMCrPmUTg-yWx7EuVU5WWmhWh7j9-yxymYt6tHFhv_H-i7qKnqUsA_vlD_5qfA4hLdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3jbET4sMnOidY-cIi5ZY18RZ59cPv8kIlGN5QxE9NJbv__FLDaLCQgd3qti61m2l07BPJmy-6YXsu2DkE47B4ew7F_CQZlZm1sVaHgirbgl6Lu9K_YM0cPxncnzPiw0CXWQ_8h3I1SFGIwMrd_AsDK9lW2uXWxlFehO0UQpnCfrAU2bmyjfo4dWFAWyDVk7rIq5zchtqHtw5_HKdKtkqPGd6VH1UCVmYY1vJSdbYnIZpJTGJbARkeyg72c8hLmsQQgi24dVU69wtJHTFz_R5B33FL5lp_iYvBSvWDLoErrEfYhloLOSmFiR_-oRlFw6eMOeNSXYPrId9gbxEyhLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RK2-HESVy8vxndKrx6qj49Vk3le1CQi2S0JbevoU7dE64r5SpTpvdc4TulFNYZg1KjuZ_AIGG11fzNZ79tcxiDqh6rmnwqNZD9AOPxXXZZiESX3rtKUskpRYI6zV0ziKyxCIsiciEZa9JEhstHgSNslnc_nSmlZR2KuzkAYWVxhjDNAOlMHUOKsezVLyQu0UvsSRnTJ9OGSGqUjAFLMwMknpg7C-pBj4wafaXzyCVtcFZbHuV0MZB-_YC5YeqkivzdLTeZ71bDyOiT9GptQy0j_NdHpOXCtNIyx50QKFNEJcgLjkCkyvtBBbg_MjmDOBPiX0rmJkbt1l6MQNEwYEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFs71UCTc8SMqt1CvjCxPN31eWAI49vaIKV-7rJbEktO9Lqi3NUAFacB9CR_5LiJlfQDu51ty9g55bL-YvHZb7HJS09vhFjr93pb1OU0q1lTTB2Iv002jzJOnIgsY1sNOWDRiUoFkRSrUyMI29E6Od4US11zsspXqVHyxeG8E1V-O5ai2CeSGz4j0SA1Fgc4lsod5X2W9bmZjRrldAp-FMvOEM1HfuAVOXVdqYbmVYeyEHUJwHXH5A9U9y9BiL53Egtejbe-XkhEuOrVF5gLfMHmPhU31g9Uv8UGzfbWLIdDvYAUndCEHvwN3nGNedOUu9jJTs4_CYz-qnvhSMjoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzZj8yXHthSge7N4-B1crGHX2i8rbYI4ErVkTZ2DIphnybWbKrGUFXqV8C8q86BPFGKx2Ssk1SqzV3e5Bs5HPAON6Z7jcTIE5KuHU_bCDEroQ1cUddbbYfwHMJ5mt9rrH5EQ3s_PpE2r_Hp2Z-Zk3SBPd0cZO-Lzmz7rU-MqjFxV-X8nYFVEJ4Yt6w8VIXJztyCdEo6hsAgAFLjaQ8Yu38JbgJPY9GyEL-npjWddoNCGgZpJfvcQR1zHX5tisrD3WeKLZtPS6IN3POLJimqtyabkqwkN4gSBUYRkqxHNXh6mrNR8-nqQq3QZMA5cWpnDEFOvlOEym8P9JxtgSt32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvJX36bfVFkzBqvgCgIFwwTjg-tvxpCemNGWLiM5opImZ4jeuY13_90PeJtVZ7FVhrGJbzevIuq767rNrYYwACs3u9VyJa0dTfnVAjWkF087JxOXBVqbEj2AwWTD9fE6ulfpgIC7sW6sfhKKgJFC3ktGTe75NwcBLWAlosqkvcS-6OWAlh3-a7otcY0vL-kOU9ROHrejyrPGVz2F_mYiJkFFnAR72nIxHU-1EKOPaHaYwlVa7l85ZqTgyOVnqEJBW0Gp8gdXP7z-apt3qqeyukZRL2KvK2UJBJ-iXunUoosuxI8Sb3O7rdjPCKsFD96Vf3UVK1YE-LzXrMJ_-9rDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3XrI5DMmmSEVcBsN-SPhUDa6gThh4IfgWLXHxgcCD-Yla4mhGlzIGyKZV01qkZ8LrbfsGoPnjXPCQ8-8su0D_Wnw1DkQeiX2T-UJPoM1rH-G5CxFeXkiwR6lXoc5sjDoJZjrPbOm5PQ7oGP0y_WLeDn2Yp1ooJvZSuQT7M7CkQBAyjTbQeEujuLXh3NvwHelb6Pvk-B_ak60h7mEts_CbmqDdJ-f9O4Tq6svND7s-QyjqrjLpQbI2FrrmbHB6Ts433ZCORZhI0aUUS4BicOWzTr3l0-2LtwNZfB5TAUrmfGWR8yuHGpz0bDHEIl-6wUNZVcTKfOLfelKdTGPl943Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کنکور کارشناسی ارشد در مشهد
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450381" target="_blank">📅 13:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7J2_ctsh3OdQKjXfEobYoNdvvmsO4l1tNvGM_nzkykoarUVhoPH1E9pOcA7gDjgZEKZpiUMivqk560xcyrYFetTag8M2DpvAiaaDUr9BY0FXP2dnqc4LMiokIBJBk7WLovDWTnPiQNIsAmVrBgy4D0K1e-JsIcdrl16l3FEPHR2G-FVnMT_eIirKKu_7h0yuU1PeQ3H6ovfgmQ75N_npXGk9jtV_h19mHvVaUU7cBOoP9vna5PR6e6CbqNdekJD2u_kwAmr0yNkdmgCFtndxZnUfN7IzcXRznvTl2JyQKbzgaSQrWI9wD63aEOLqYzXkopY68OCJEDy7H9dAX6M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدارک یمن برای بستن باب‌المندب به ادعای رسانه غربی
🔹
روزنامه انگلیسی تلگراف به نقل از «منابعی در یمن» مدعی شد که انصارالله «در حال آماده شدن برای بستن تنگه باب المندب» است.
🔹
این روزنامه هشدار داد: «هرگونه بسته شدن تنگه باب المندب، اقتصاد جهانی را به طور جدی مختل می‌کند و کشتیرانی را مجبور می‌کند تا یک مسیر انحرافی چند هفته‌ای را در مناطق جنوبی آفریقا طی کند که هزینه‌های اقتصاد جهانی را افزایش می‌دهد. این دو تنگه (باب المندب و هرمز) هرگز به طور همزمان بسته نشده‌اند. حوثی‌ها پیش از این نشان داده‌اند که قادر به بستن این آبراه هستند.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450380" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWUCAhhhY8eZVkRTj1rIE15hOw9xvZ2faA1R4b9t0LvnLxNmRcxcCcE7N9k6cUCcbYya1vJiJYFSF8de51XItwFT5gJbEkGRBRCLYKyPeHUP6F25nYhkqzva6-n0x2gnfFsIWhlCmf9SEY4pg0YHJgn0WTbIsngO-MaEYhqj8NuUge8x1MDQHhPceYeUcRoVSnEvCTB0Tu3jP-OCR8HXwSuR42odTEfNwCXSOX3AOyjoA7TgOiuLnAFZcdNw-sUYab5va2zvnv1I2zHySfBYLTEreq-nMpl7JOwCr3RnuAC5Rj1BbXBCoob6bhHU5RL_na1aclSXxNYgwXKGpoNQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والیبال نشستهٔ ایران بلیت لس‌آنجلس را رزرو کرد
🏐
تیم ملی والیبال نشستهٔ مردان ایران در مرحلهٔ نیمه‌نهایی چهاردهمین دورهٔ رقابت‌های قهرمانی جهان در چین، امروز به مصاف قزاقستان رفت و این حریف را با ارائه یک عملکرد مقتدرانه ۳ بر ۰ مغلوب کرد و ضمن صعود به فینال، سهمیهٔ حضور در بازی‌های پارالمپیک ۲۰۲۸ لس‌آنجلس را به‌دست آورد.
🏐
ایران از ساعت ۱۰:۳۰ فردا برای کسب نهمین قهرمانی خود در این رقابت‌ها به مصاف برندهٔ جدال بوسنی و برزیل خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450379" target="_blank">📅 13:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مهار آتش‌سوزی کارگاه قیر در حرم رضوی
🔹
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم مطهر رضوی آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
🔸
گفتنی‌ست کارگاه ساختمانی واقع در صحن غدیر حرم…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450378" target="_blank">📅 12:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b23efd0e.mp4?token=kD1echTPCwxnq9huG8ZcrU3QtM2RpR7ZL7A4nZaV6MegcZCAZY_uqIIQcIxNfU2OqyRhCErzmt5AkyuGWsHHhrNmnTWVK9-YZsmOjmmmV9leGNJ4WvGQ33Lpcs6modalkDHvRhFMiyH4iEZ50LaPYONKgf1j103ZG_QnGnbe1NFZ_frWep-TYRTqrjAlun6xmfbLGXtH9iQDMdLNTWeKnYKt517tvZAJFnfSfk-TS5IEDjNjN5YQLj-DdPxxwNvJv7snuQaubo6lLBP0EUvEzwksSXg_ytb0ARVQhl9RT1jcTobeeI8ymZ9FDi4puyIZnl0qkQZW9xxStguV5sDLsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b23efd0e.mp4?token=kD1echTPCwxnq9huG8ZcrU3QtM2RpR7ZL7A4nZaV6MegcZCAZY_uqIIQcIxNfU2OqyRhCErzmt5AkyuGWsHHhrNmnTWVK9-YZsmOjmmmV9leGNJ4WvGQ33Lpcs6modalkDHvRhFMiyH4iEZ50LaPYONKgf1j103ZG_QnGnbe1NFZ_frWep-TYRTqrjAlun6xmfbLGXtH9iQDMdLNTWeKnYKt517tvZAJFnfSfk-TS5IEDjNjN5YQLj-DdPxxwNvJv7snuQaubo6lLBP0EUvEzwksSXg_ytb0ARVQhl9RT1jcTobeeI8ymZ9FDi4puyIZnl0qkQZW9xxStguV5sDLsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حبیب امنیت
🔹
مستندی از شهید غیب‌پرور به‌مناسبت سالروز شهادت ایشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450377" target="_blank">📅 12:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450376">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مهار آتش‌سوزی کارگاه قیر در حرم رضوی
🔹
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم مطهر رضوی آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
🔸
گفتنی‌ست کارگاه ساختمانی واقع در صحن غدیر حرم مطهر آتش گرفته است و این موضوع ارتباطی با خود حرم ندارد و در کارگاه ساختمانی رواق امیرالمومنین(ع) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450376" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450375">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf7PyQh53Tz_HFbsueVcfwdXx0wJjhbndLWzw-fMlO4ISUMMUb3Db_tHP1fXqPr3TH4jU5WPHG1YU1Wz0vJxB1Yhy9zg246YATnCsP6nrH4KYOK-ceAjmFBhprWlTy5NgQlF0ot20NYW5RJD7VqKmQugc-TQYnfb1m3v9BkFv2a2A2GFmA0mhD09KNEqNnxik95Ksq3bl8S16pg4p1ylrhQyXcSmfXMZ7Y37SlFfHmizi3cu71qiUda9T4VwbVb7VKu1qkauBUIFB4kQ2C6c11Zel3dwZ-f0_cFHClH_hZDXTUaiVrgl_DdvsNiafUbAZy2Tg-FXglXeI4mykKYQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضارب آمریکایی: می‌خواهم همه مسلمانان را بکشم
🔹
مرد ۴۸ ساله آمریکایی در ایالت یوتا با بیش از ۱۵ ضربه چاقو به یک فرد مسلمان حمله کرد و در بازجویی‌ها به پلیس گفت، قصد کشتن «همه مسلمانان» را دارد.
🔹
طبق گزارش برخی رسانه‌های محلی، پیتر مایکل لارسن روز دوشنبه به سید سهیل الدین نزدیک شده و نام و مذهب او را پرسیده و قبل از چاقوکشی، به او گفته که یک بطری آب می‌خواهد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450375" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450374">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">واکنش‌ها به برخورد با یک کارمند به‌دلیل امر به معروف در دانشگاه علامه
🔹
اخراج یکی از کارکنان دانشگاه علامه طباطبایی پس از تذکر به چند دانشجو دربارهٔ رعایت حجاب، واکنش‌هایی را در میان برخی فعالان دانشجویی، اساتید و چهره‌های رسانه‌ای برانگیخته است.
🔹
درپی انتشار…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450374" target="_blank">📅 12:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450373">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6eb1b5774.mp4?token=LLh6rK6Nqzyqa4cDlaNuf2gkhlGvyebxs2c7ptNeo4ZRRjVaFc67FDyaTwqb1fbhJed7F5h5yfBgliz21wnevMmQwpKn3VbnRjP92O6l-RexAJod3hfWeTtaUPz_tvBJlGoQhNPhmJwJJeOfdRiKwqK3D3JZP_itpjnxx8Ft-8Yz1JLoxLZl7td4RficHKc2EHK9MApsyZnRCFQpPfW_uEFJkS7mt5NDSO0einKH5ybsvKwQBCtuc-jwGHk9z9AEFNxt4TbQISW0vUOP_F-3HtIM_f77Wn1NVAqqE4fd6AMBD0vEFnKppSCK5X0GaBkSkEryw4ImuRykPrY7ugNnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6eb1b5774.mp4?token=LLh6rK6Nqzyqa4cDlaNuf2gkhlGvyebxs2c7ptNeo4ZRRjVaFc67FDyaTwqb1fbhJed7F5h5yfBgliz21wnevMmQwpKn3VbnRjP92O6l-RexAJod3hfWeTtaUPz_tvBJlGoQhNPhmJwJJeOfdRiKwqK3D3JZP_itpjnxx8Ft-8Yz1JLoxLZl7td4RficHKc2EHK9MApsyZnRCFQpPfW_uEFJkS7mt5NDSO0einKH5ybsvKwQBCtuc-jwGHk9z9AEFNxt4TbQISW0vUOP_F-3HtIM_f77Wn1NVAqqE4fd6AMBD0vEFnKppSCK5X0GaBkSkEryw4ImuRykPrY7ugNnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید شهیدان حاجی‌زاده و محمود باقری از شهر موشکی زیرزمینی
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450373" target="_blank">📅 12:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450372">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sfey1ZJKluXiPXPO9BtyZJViUUfjM__I9VePIJvcLjYmQeuZzJ1UjwoTI0KwzjpDNPRLbKYXaWfFqpsYkAudw0RWQY-a_DASIiJ6392mTj9fu2dJXdohNsT4YI6HtOIC3kTeVvdVqGvp4fabjK8kJF0ebr5sKrfccOdpzVGDydqoTiPvNrt5bNE5dCawQNCzeg30HWxnkMDOrbRav-Dq6bS-e49B4fLPI8wzTQEa4k23KGoM1J3DxOOU01rAoZik8pOp_uAh0dA8wYnakpOz1G96VftkJOavft3sbjgndUSdgEJY9QzIiAEfSWxvQkzNkDBjSRM2ZZ9iucF4FpxBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها: اخراج کارمند دانشگاه علامه به‌دلیل تذکر حجاب را تا برخورد با مدیر دانشگاه پیگیری می‌کنیم
🔹
کرمی، معاون فرهنگی نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها، در واکنش به اخراج یکی از کارکنان دانشگاه علامه طباطبایی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450372" target="_blank">📅 11:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450371">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Gv4mZKaViyEGjWNb747H1M5cjqN2a_MNvAqbAr0eB-xivwzqDugUI7KNNc2Yf1J1CTwyyEt6W_ZXpO8bGweHiMRsQO063T_6uGPBtrjkWBCjvVMlv4G6W0CQx1hvCsc9c2LJQ3MTwiw-8pB-NER2AxqXq8U44w-EbD2klHVVLAEeeGCmj0Yo9TPR9uyu7tNPaqA-HYRGLd6WxaddzTsNfyuXxWT5sMzEfPiMa9v364xz_oaJzCq8yRsRNb0JI9W0kJ6WmmOqatiUsAwrqVq2xYQcsetYFK3Gu-UgK8cAqMQtOBzr_vhyRxBMBt91p8gNrgY5D6v1WMXJZibU7eBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک محمولهٔ سلاح در سیستان‌و‌بلوچستان
🔹
فرمانده مرزبانی سیستان‌وبلوچستان: درپی توقیف محمولهٔ سلاح از قاچاقچیان که قصد انتقال آن به کشور را داشتند، ۱۵ کلت کمری، یک کلاش و ۱۸۶ فشنگ جنگی کشف شد.
🔹
تلاش برای دستگیری عوامل مرتبط با این پرونده ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450371" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450370">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انهدام مهمات باقی‌مانده از جنگ در شرق بندرعباس
🔹
سپاه هرمزگان: به‌دلیل انهدام کنترل‌شدهٔ مهمات باقی‌مانده از حملات دشمن در شرق بندرعباس از ساعت ۱۱:۳۰ تا ۱۴ امروز، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450370" target="_blank">📅 11:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450369">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984732b934.mp4?token=h65cDlW1dfWr9WMLt0opoXL_s7-Xv5Z9MtUyv8pSc8bVsbxq2RP41cv6Z_NEOnnqjJl5_wzIC1Mu2cS23BO6yrVK4FiDkEDnLVr7zgWObuHPcpc2ZZWYhJR3ykR4XEx0uNrgT-chigFlWyzF8PZsqDBafjF086wQFVB_2KOu5wdD_Ylw4GrZhIm-wuMGfBhGTDvDM-jHgG2tC9BnaVAK8p6SaNgh8ccPmcu6FEgUL4uytfTuAUW96z1NkJdyh0ZqLa2HxkTHh6EH9RKN9Rj3_BlCIErkz6jqZurKzlMgO6V0oaCMoqMwwQHJXtBWcN3aystLu6ylIv7k_SdH2fCzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984732b934.mp4?token=h65cDlW1dfWr9WMLt0opoXL_s7-Xv5Z9MtUyv8pSc8bVsbxq2RP41cv6Z_NEOnnqjJl5_wzIC1Mu2cS23BO6yrVK4FiDkEDnLVr7zgWObuHPcpc2ZZWYhJR3ykR4XEx0uNrgT-chigFlWyzF8PZsqDBafjF086wQFVB_2KOu5wdD_Ylw4GrZhIm-wuMGfBhGTDvDM-jHgG2tC9BnaVAK8p6SaNgh8ccPmcu6FEgUL4uytfTuAUW96z1NkJdyh0ZqLa2HxkTHh6EH9RKN9Rj3_BlCIErkz6jqZurKzlMgO6V0oaCMoqMwwQHJXtBWcN3aystLu6ylIv7k_SdH2fCzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات هوایی رژیم صهیونی به خیمهٔ آوارگان غزه
🔹
رسانه‌های فلسطینی از حملهٔ هوایی صبح امروز به خیمهٔ آوارگان در بندر غزه و شهادت یک شهروند به‌نام ریاض عروقی و زخمی‌شدن چندین کودک خبر دادند که همگی به مجمع پزشکی شفا انتقال یافتند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450369" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450368">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj4ORiMdyKTNvqApSa-OppS5m8Aj5DFw1tBngNpLb874sPp5DS47reF23XxCZlysYfnZriiQV6S5wxwm98wIKgTFZ6DSXSAWZx1QebrldVC9Bly7vs3wS_BRGJsPUcl0ldhEyFX_O0nq_0GufCvCfr2TJ8E-UHigPRz9PMiugfDI8dLMQxxo4vVQPXcXGGNKOiHzPGBa6w78lT6uRjLiNk09t15pVFkuUw6gXmvt6mDear5HsWQ0SAtnYIcgYDFz5SiYfKzrzBei-x72Usmm5qfiyxSz-FgBBg_ubpIQ8xuvGERMJQf1oUeBn_Rbjo6fEPcLIQuJxbwvETLOIAEYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم میکس مردان و زنان ایران قهرمان جهان شد
🔹
تیم ملی تکواندو میکس ایران صبح امروز با ترکیب هستی محمدی، باران نعمتی، محمدحسین یزدانی و امیرسینا بختیاری با شکست‌دادن مراکش، تایلند و روسیه قهرمان جهان شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450368" target="_blank">📅 10:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXUsYrBLE8PtdXhMPpNLZD3PW4LEt8gNrGHFUjP9OpXHWh47t-EdSh0gi-qQ3DaUAg7jE7xIUgNZ-mzQzVg5PAKpDXnad7LCQNEs7hbfBXfZ18A5817Qi25VQEm12g4Wi4JZNql57odCxHUW5o-O_kOOyOCs5kuolK35Hv7oizj4B_PhxdwXz5WSsAOAQlQiueVwwWl-81LeCmOyBKSKsqlG0ekqZB5UreqOFleptaCsrnfMGOpqf_s9F7y--aF9EGfYaFfO-z4TCeNvAc_RxS_pxfuPNrPqDYOAT_GotRdeb_z4Ei3U097zoogamdX97xdaVDRNc3X4eRVjoEVFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا حملات خود در ایران را به اسرائیل گزارش کرد
🔹
وزیر جنگ آمریکا در تماسی شبانه، اسرائیل کاتز همتای اسرائیلی خود را در جریان حملات علیه خاک ایران قرار داد.
🔹
دفتر وزارت جنگ رژیم صهیونیستی همچنین اعلام کرد که در این گفت‌وگو، کاتز بر باقی ماندن اسرائیل در لبنان، سوریه و غزه تاکید کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450367" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGAd-Dn4Pxh6GcCuZa-E6p5J9LMuaePhoQa1mkyvnS4nof2QHB0hiSM-pyQfoappYnSdtuKYG826AKkRv4by9F5ca5oZl3r0q9kbgKiQCV8RLHpJf79uRxPYKu3DqmElbQVr-ZH8L5VUcYyT088mQ4CEjEpqFGunMkU4VbM1rUH1e0oO8ZIHMVAleoPCQiIM5d20OCY15EyImojMlDZUIteaYkedvUqyn5rEbKew6AQ2IIWRyK4d9yeZ9QYTp_L0Jm730EBP0Ev4OBlHODFHeSw7o8THP854mUrefyVtjUZOeeLz4xkaWjNIRjVCoMiq0zngW6DeqyLxfyNv_Wjg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g09jTl10JfJPNbm2BUd1oo9I3Me3QKs94ZGGMEZewKngHarQqwzW7ug721x23HDPU2OVIKEC-TRp90B-Ked6hYn6Wwk2qzp6dDWTY-DJBV_LEXD8TDX_nboT5e0YO9FYDJT3-VtvciQc5eRmd8Scf0KniilCoaO1NJe_wVIBNcWnsugZjJM4qca6ImZ9-_qi9rsJvC749WqrOrMFfZyxbim-jnYVcBDX--1O2HtdqapyGurIJzhm4-zPjqyKHV2Qn6SdOfGa8-KNr7T7GQfxOEhD77ZXrWr2288RAL4wYkF9l01bDwU5JO_aKc--24N5oIkoABKbGK4d01HBGBr_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMj90t7rviGe6E93reDM0-CduV-T5UDiMmQGDpkPGZsPxIWLHKG2TgPLw1Y2_lWgZ5WAUT_-Ukwr6aE-jUW1fu3LdLNdOYx6NykGK2CDtIRyv0S47ERqnwAHQKagZGLHF9FC4J8VoMYwUeEeFE0V7xbfkj4kVtgmY4owtao7vvBj8yaGg1NzLQEq_NCKbBH1Iad-78-OZYCgaRyuHcQ8fDL4QYpKWVF5Z2FP8bvmajukWwuEby8D2UEDAkkgABIOv_FGA60jYs9mtEcTC0qZmWk3xKkiATUzI_GhqlUJ7r9B0KJ5kCsGRp1G4u2HoMBhlvw2qaZpzx6KMcKJ7DiZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F79MT0wWbsjKbK7GDTUS5YWsVUUC7FoH9EZA4iGa6MvVU_zYRa_30MJ_x9855Rq5auQ5klNYrSi8R0u5eUafbcaE50wTgykxTeY_7fpZIqIb48yUOvJ_EowNTsTfHPa5XCgeWpPIEK0uJfAht7U7ipuOk9qyAEYpSpFkIGQpTyStjnIKrSzft_qtQ_WztPqaPETaw8ICXHrbsDs-V-3c4OLAYdjhli9F3L4wpT7KZ6Jml5jZ7Ddic33lANPYpPXYjjT_7SgxnTNuyyFyfn55wbwkqK2DP80d7NcGpDgChKRfrKnq9eFap1tfC0s0LqtIwx4lE4cFdiUkIXvng__CjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZXIGPSi4r3pLwWvSDpO2qxSp0mIUhRpJq-xe_O2W9DnZvobMQqPfRdejtekSVEe7oHg1ywlFYKXWNhNEvFG0ThLuc7M_bLY6VXaZzASsu80jxsIFS-oVCOeC4f_2NO6EJ3uVL6vFA6JcUkfIlKPp_hnTiAn9ea8juM17P_NeqtyOA2iZqYeq-AmeFCDEtIFSwt3n8UmuZX73dRqAq8FANXEtjhXWYuVyfYs5yRPKTF1_c8XrKeh-mNcfnrY2C8e5Hmoo-I_0Un6tB4M2xRc0Du7-b8Hto1OgJXzqwKOAnABKWOzcBb3iYP2OnBVXboM1it5GjXbrYy6yF5D0FjFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Syyvq61diqQh21Nsrj84DVbJ08dha3eW-jLjyAIbGajro_Rpsm1ZaBzmlNnkVprcePIPfEEsqlH2n5JemNnawC6xiqiDkC3oOpJivDZ-F6cnc-Yx88g5Fjuuwl_A0SJJlT39gKdGId_uHzoWeOsLaYK8Kc0HB1U9JjJRwTdNRDVOryeQ5W-gx1AGRfJZxser-LBsh-SIBfv0LnuLzuxiheZn5njvtCLULiIAAZ5EX41u--7gK4bMq6nmOBudHXA3ooaa2g1Uo9Bp-Uc-uoB9bp5LSldgTqpq58sSRJOGpcejclGacyGaQGRYeNWdOLK7kd5qIbY1Lo4EfpZkLOhSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_IxKyrdhrzXpfI6zEX4sdcbaK43C7onAj0P_uU7nfEHII9ht3rCdbrVFhfzchnKPDMcZ-exz7K8KB77Z6hJv3ojL-O3h-BN_IY4kAWFFvyeshDHw1hJS4AwjhbzhWieh06X9LEHbNA-WqANfCCOwQutRMdDsx199EkAxRC2kLyhHZcQVXFLUnNRA8ENUB0WUhzsazIZZA9T_nL70G1X-itwl9Tra40Ai2oX1o4LH2DCoLuLMzsBcg4Cn_fPTm2TkSkdq2ssyChCWZdt9Qu9gkRv2Tgc0ifIKShctzcTn6_sj69-nr31C3YIaohOb7IYu4I7ZRXsjrr8iK2lzKlURQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت طالبی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450360" target="_blank">📅 10:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آشپزی با چشم بسته روی آنتن زنده شبکه سه!
مهارت عجیب یک سرآشپز همه را شوکه کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450359" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450358">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#دعوتید
به بزرگترین سفره نذری حضرت رقیه سلام الله علیها
🎁
همراه با پخش گل سر و جوایز ویژه دختران
🎭
اجرای تئاتر “ خرابه شام”
🔰
قرعه کشی کمک هزینه اربعین برای ۱۰ نفر
اطلاعات بیشتر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450358" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450357" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450356">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0w7fm6HfoApSgsKUwp9INacUeaLvUuUCLa0T4XEh-3TbDk21lpZH47LY7HqlgM8XhOTN_sLipkb9Se6eyBCrwRqQqLbld-0MM6If_xYNz2y7P0rNxgBqSgIlwXghfncziQptIPhwXsXCSc33D4xjh3Rs4uSxTScnOC5fSwSJbNvm1st3rRokIATM2SE8W0qPGJz1E34phN7txz4rm_0ypdPHymvsTNjnMDLH6TeGOlR60XuwJVlD06n5Ij_ENyUIfpNxxXp4oQ7XsYl1TsjwAO_jzkgGsIvf2GFyU4DRdwEY48YkxvS7zkA7TaEh0QXYfXEH9GcDLwoQbY-RjVTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات سوسیس آزاد شد
🔹
وزارت صمت در نامه‌ای به دفتر صادرات گمرک جمهوری اسلامی ایران، رفع ممنوعیت صادرات سوسیس و محصولات مشابه را اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450356" target="_blank">📅 10:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmw8gv8fttvFz6BpOfXaWsHiZRKfM90sH6fdjC1csC0YCxUZJ1AULpXf1WxL4CBC1lNVtkCXLDFEqOxP3SJ8uddBIjD6VcGCw38L82wwCMOFKxjSn_GqW67aquiV29XrXT5Hp3HaZydZIQkjQdtIR2JbtLpXK8vFcKk33WP6cl6YNP2gou9kOI0A2xnxUF1vWnodHSeSO1QN2gIk8z-oe41Al2tVTPetGbgLTNZj8B5i3XPxgxcrAfQy3FM6HslkELx5Kb8hfsVQbywE5fnulWL9IOfX9FslFdciRww8ZX8L9CV30BdYudwp_CPgW3poie6TIAGi146tdbdzUY1R7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: در صورت تداوم تجاوز آمریکا، جنگ به عرصه‌های جدید کشیده خواهد شد
🔹
کشورهای فرامنطقه‌ای باید در تعامل با ایران بر پایهٔ احترام متقابل عمل کنند و نیروهای مسلح کشور نیز برای صیانت از امنیت و منافع ملی آمادگی کامل دارند.
🔹
ایران هیچ‌گونه تقابلی با کشورهای همسایه و اسلامی منطقه ندارد و همواره بر توسعهٔ همکاری‌ها و روابط برادرانه با کشورهای منطقه تأکید کرده است.
🔹
بخش مهمی از ظرفیت‌ها و قابلیت‌های نیروهای مسلح هنوز به‌نمایش گذاشته نشده است و در صورت تداوم هرگونه اقدام خصمانه علیه کشور، پاسخ ایران متناسب با شرایط و فراتر از پیش‌بینی‌های دشمن خواهد بود و عرصه‌های جدیدی از تقابل شکل خواهد گرفت.
🔹
نیروهای مسلح ایران حفاظت از امنیت، منافع و عزت ملت ایران را مأموریت اصلی خود می‌دانند و در این مسیر از هیچ تلاشی دریغ نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450355" target="_blank">📅 10:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450354">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0JbXJ7Cxs23wnZZX7w3QU-rxTCjwChAIgEj85tqw29sD7z-HVjg56OZhRQhigoYi40zqLobDu8P-F6mRtGZDTVu6hcjImeCrFeEmihyGCYKhKkwFCPlKP-tRJGizP3k24SfMmEDAkG1s8do2oN7O4rlSGGQZ88ilc_j7XGMaN09maqJJMxilBDCudbNTdv94wd-1EzGSxm-ubH-pVsbnBqsVmFs1PgMnuG6dLMWO4IGQfVhqVE570CjiOv4BSnECtFll-ufslWyyKl5yuWkpSBd5dC4m3EukDjozahJvRCVobJVSWRJL8NdY4o35sTr37r4De6L2woOtY8hXQtxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگداشت هفتمین شب تدفین رهبر شهید در حرم رضوی
🔹
آستان قدس رضوی: مراسم بزرگداشت هفتمین شب تدفین رهبر شهید انقلاب امروز همزمان با اقامهٔ نماز جماعت مغرب و عشاء در صحن پیامبر اعظم(ص) برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450354" target="_blank">📅 10:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsrJ-2jUvSR95rp0RIHvEGebzhTMdtQLQIXVJ09oMrv0qA0PN-xCXPny7kkVPvu3RFgDE9xjy2QCU_M6Pvgm78ahPtyDAsXrZGGdt6C2lyD6ADvYJ8tgigATMcym_HuXMAiUBUM7ShNGkk7OMdUri4ybqA-GJNs_CzBlDCXKVoAFBL1AtD_f83NzJJPF8klJo4IwxppFZjNVvSWcpbcnpewoWVcjZT6vZVDRo1zYrMCT2Swh8TV95SCbfvvtN6AItdkBadcbZ3sLCm11WPPXKGtSa6cegab_jzmXoCJPqR1UhECMfGPjKgBQnoJTc9NTQGCVUZkn5IE51L4-z0WdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفهٔ ۲۵ درصدی آمریکا علیه کالاهای وارداتی برزیل
🔹
وزیر خارجهٔ آمریکا اعلام کرد که به‌دستور ترامپ، تعرفهٔ‌ ۲۵ درصدی علیه اکثر کالاهای وارداتی برزیل اعمال می‌شود.
🔹
دیپلمات ارشد آمریکایی در توجیه این جنگ تعرفه‌ای مدعی شد که دولت برزیل در مذاکرات با آمریکا، حسن نیت نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450353" target="_blank">📅 09:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd585a60f2.mp4?token=SFc2-NwUVEbEC_RDbXMfcPWaru5V2oLrNWTwUj2dWHNc9Xg0qCdB2dWs_kiac8C4U6N5PDwIcmKnVL-ppbu8OAiSqyDgC1Ghng29fcXWjEj28o0Hz7wDEKY5kXqnIg3Y72qZemLr-BfraDgpM94yZSq8hovlKTYSXhswQuW-PWv3cg5UyTiv3R7y1q3fFEUi085SIUBijlh5OxsSGglr3r4GUs8luAkdZtZzC8pq6kU-_gPnvTcOl02OR7Ar_oAiANLupV4R1EvGChnJorStecJLsFIsl57wXYN_bpf9Ed_iAjY325twF2s7vHnsmAUl0wSzG3FEOX_iMyVaUdpKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd585a60f2.mp4?token=SFc2-NwUVEbEC_RDbXMfcPWaru5V2oLrNWTwUj2dWHNc9Xg0qCdB2dWs_kiac8C4U6N5PDwIcmKnVL-ppbu8OAiSqyDgC1Ghng29fcXWjEj28o0Hz7wDEKY5kXqnIg3Y72qZemLr-BfraDgpM94yZSq8hovlKTYSXhswQuW-PWv3cg5UyTiv3R7y1q3fFEUi085SIUBijlh5OxsSGglr3r4GUs8luAkdZtZzC8pq6kU-_gPnvTcOl02OR7Ar_oAiANLupV4R1EvGChnJorStecJLsFIsl57wXYN_bpf9Ed_iAjY325twF2s7vHnsmAUl0wSzG3FEOX_iMyVaUdpKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی قرارگاه خاتم‌الانبیا: زیرساخت بزنید همهٔ زیرساخت‌های منطقه را می‌زنیم
🔹
تحت هیچ شرایطی و به‌هیچ‌وجه به آمریکا به‌عنوان یک‌کشور بیگانه و فرامنطقه‌ای، اجازهٔ دخالت در تنگه هرمز را نمی‌دهیم. این، خط قرمزِ شکست‌ناپذیر ایران است.
🔹
در صورتی که تهدیدهای اخیر رئیس‌جمهورِ از تهی سرشارِ آمریکا، مبنی‌بر هدف‌قرار‌دادن زیرساخت‌های ایران اسلامی توسط ارتش متجاوز آن کشور عملی شود، همهٔ آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی ایران در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.
🔹
دشمن نادان بداند، لحظهٔ حماسه برای ما، لحظهٔ پرهیز نیست. آنچه از سوی نیروهای مسلح ایران رخ می‌دهد، ضربهٔ هم‌تراز نیست، ضربهٔ برتر است. ضرباتی که شدیدتر، گسترده‌تر و ویران‌کننده‌تر از همیشه خواهد بود. آتش خشم ملتی که هیچگاه تسلیم نشده، دامن متجاوز را خواهد سوزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450352" target="_blank">📅 09:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: مرکز ارتباطات ماهواره‌ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
🔹
مردم شریف کویت شب گذشته ارتش کودک کش آمریکا با حمله به نقاط متعدد در خوزستان از جمله محیط یک بیمارستان درمان…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450351" target="_blank">📅 09:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450350">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: رمپ نگهداری جنگنده‌های آمریکایی و مرکز فرماندهی و کنترل جدید آمریکا در غرب آسیا در الازرق اردن هدف موشک‌های بالستیک خیبرشکن قرار گرفت
🔹
مردم شریف و نجیب اردن! شب گذشته ارتش کودک‌کش آمریکا در یک تجاوز آشکار با استفاده از پایگاه های هوایی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450350" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450349">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450349" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450348">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwVtle4GNwZkR-Lt2C8uDAjNcHXkmzZhegMbTAK2Sl6FgoXFxg2EgTLgmqdTAbm834g8WfVf2PZzoKFrmDeMZn7npCR_SCYUD5VZSMaLVH4pAe7MDbm0X_EOMKeYstYvB3m7L66XyJi6USULKS_txRKNq3xGiEBM5rgPCmzJq47LZkxRnwy7KWRKAhSCAsc3I72EsF2tOd91WQMM88dch9iaE-XnosKiYbfXTxRpLbpajd1o4gm4coCZ8sgBE3WGKvfgDHAqdml1nNj7Ec4GUzOUA5BBfFCS3cdHx1bbAxRfAWBU8_geLzfQBJBf4HJjXnhT5M8Z43phTPINmevxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام نتایج نهایی کنکور کارشناسی ارشد تا نیمهٔ اول مهر
🔹
سازمان سنجش آموزش کشور: نتایج اولیهٔ کنکور کارشناسی ارشد امسال تا پایان مرداد و نتایج نهایی تا نیمهٔ نخست مهر اعلام می‌شود و پذیرفته‌شدگان در نیمهٔ نخست مهر وارد دانشگاه‌ها خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450348" target="_blank">📅 08:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450347">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حملهٔ بامدادی دشمن به کبودرآهنگ همدان
🔹
استانداری همدان: بامداد امروز نقاطی در کبودرآهنگ مورد حمله قرار گرفت که این حمله آسیب انسانی درپی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450347" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌ جزئیات حملۀ بامدادی آمریکا به سمنان
🔹
سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
🔹
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
🔹
خوشبختانه بخش‌های…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/450346" target="_blank">📅 08:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450345" target="_blank">📅 08:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f57a8907.mp4?token=j9UnYYZCcr3T1ZkNAvf74_YKAuUAejPdjZb00vA3lzMQ8fUb7DCy_PEI6n-f-igFlav5skFkjoQdypPcELSm89IM11Jmpbh6TUg91PoS8clYPu777yYoLU1Dnh1-fhFDhw4JUeF1P3bBWyhLX0e1-wX2VEo6cJQZ_S_uo9UkvxeZnXFAn1Wpy-eZObspf09-PSOl8NRAjFC3tl93kFdt3mvuGZ441UAA8MSKufaU2KQxBqGatK8qOVIr4NsLyp2HE51ptDZ59_yUW9I_LXMrwfpi2eXdt5rweuq0u0522eW9ga87cQwFxJV0U7Nmv1u-i7ROVhCESgDPRwnJeeVncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f57a8907.mp4?token=j9UnYYZCcr3T1ZkNAvf74_YKAuUAejPdjZb00vA3lzMQ8fUb7DCy_PEI6n-f-igFlav5skFkjoQdypPcELSm89IM11Jmpbh6TUg91PoS8clYPu777yYoLU1Dnh1-fhFDhw4JUeF1P3bBWyhLX0e1-wX2VEo6cJQZ_S_uo9UkvxeZnXFAn1Wpy-eZObspf09-PSOl8NRAjFC3tl93kFdt3mvuGZ441UAA8MSKufaU2KQxBqGatK8qOVIr4NsLyp2HE51ptDZ59_yUW9I_LXMrwfpi2eXdt5rweuq0u0522eW9ga87cQwFxJV0U7Nmv1u-i7ROVhCESgDPRwnJeeVncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ پهپادی ارتش به سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن
🔹
پهپادهای انهدامی ارتش در مرحلۀ نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450344" target="_blank">📅 07:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB0XFI8zE3Jr--ri3JfP_zXLtMW5HSxapOmxZ5-313UG7d37nkcVvCiHmZcD1Hy36PgE5270AK2PiLFDLjKb8FOETRxd9lGH8t5scKa1K5UuRRV_SutliH2btilY0b_XNS1oqNxhzYIZY2Wsev0JBqq50JdJQ56A4_2qmydyjCgqi83nsEo4uTCfyzimvGsOp1NRaiYTUJG_1ccErL5wjXLm3M20k1XhPvIKD0jLGUmOnv0IMe0ymxdN6XLzom1-5EKjOGG6hzKZulrwJT6nFBrhNopSDg14TnpVfiM6ptRnHWJrAzN_GzKi8w8hNo-faDzReCfWytiGFghuGiLfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: کنکور سراسری قطعا  ۲۹ و ۳۰ مرداد برگزار می‌شود</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450343" target="_blank">📅 07:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4Zh-XhLjLsy6rO2IZRWjL9WLdGWTykce3eZ2zdvg-0w_IX3TNPMwL8NUQK5a3W5Sqzs8iD1UuE0yFmoU2P73uVdYOR3PTvgtQPIPOvYB2PIe4tA_CXwj9dyCAqUPot8oAOvnFb03klNylUIE-_QciS7jGxaaxgWKN3mJKep7Z3c2MBizX_9TOTiQ5MD8TJrPL99-OzDgEZ--WcbaxJxKlNAc-33CCf-q6KX3NMcoOHCaSmuJnPdLALTkHtvfUFzK6q9i_YxrwRqtswTLvtR6vWuTN6vnVmtl_YPyACaEjziT_R3xjud-5Cj76EXMTjuPPPwKf6VR9SOwzyHMSrbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا برای حمله به کوبا آماده می‌شود
🔹
شبکۀ سی‌بی‌اس به نقل از مقام‌های آمریکایی گزارش داد که پنتاگون در حال آماده‌سازی برای حملۀ نظامی و تجاوز زمینی به کوبا است.
🔹
در این گزارش آمده: راهبردشناس‌های نظامی در هفته‌های اخیر طیف وسیعی از اقدامات احتمالی علیه جزیره (کوبا) را بررسی کرده‌اند، از جمله حملۀ هوایی ارتش که شامل هزاران سرباز آمریکایی می‌شود و توسط لشکر ۱۰۱ هوابرد انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450341" target="_blank">📅 07:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
شنیده شدن صدای ۲ انفجار در خرم‌آباد
🔹
دقایقی پیش مردم در خرم‌آباد ۲ صدای انفجار را در این شهرستان شنیدند.
🔹
هنوز محل دقیق و منشا این انفجارها مشخص نیست و تاکنون مسئولین استان در این خصوص اظهار نظری نداشته‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450340" target="_blank">📅 07:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmQ5-8-wDSdC_B0_5Susn507Xv5DBwM6TJFU403N8qaj3HNyGeaqQUz40Kcv-klpv-ZBzaI21v00JsgSarbFGP-yFdr8xI-P4qmbwitZb-xFBHBewXbUQNGeeUp0AntVB5Z91UJQM0xyKqUyIrbwdUvIilcptA0RoKbslL_GTVVqius8Gr2_eAKL21FKYTqhqbUEPviHdYxDQB4hxNkVrYO_8Y1qqyUbPuWcsHhPE9swoGj6usvnpHPFSx9i2WUYfMHiofvwQKUm5i6twrhEat3IYUns3NVa3HYlIdFsuaDPtFMKs3zWLZGjCaJxhxcfFA_AejUFiOY7JhsUka3rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون یک تغییر در دادگاه تلویزیون
🔹
برای مدت‌ها سریال‌های ژانر حقوقی تلویزیون از یک الگوی آشنا پیروی می‌کردند؛ روایت‌هایی دنباله‌دار که در آن وجه داستانی و درام ماجرا بر موضوع حقوقی غلبه می‌کرد و بار اصلی قصه را برعهده داشت.
🔹
با ورود «آقای قاضی» به آنتن تلویزیون، این فرمول دگرگون و با فرمت متفاوت داستان‌گویی و اپیزودیک، تجربه‌ای دیگر از ژانر حقوقی برای مخاطب عیان شد.
🔹
درواقع «آقای قاضی» نه ‌تنها فرمتی جدید برای روایت درام‌های دادگاهی در تلویزیون تعریف کرد، بلکه آموزش مفاهیم حقوقی را نیز در دل یک روایت قرار داد.
🔸
فصل سوم «آقای قاضی» با عنوان قاضی بیگی درحالی روی آنتن می‌رود که بهزاد خلج، بازیگر فصل‌های پیشین کرسی قضاوت خود را به مهدی بهرام‌بیگی خواهد داد.
🔹
سازندگان تصمیم بر این گرفته‌اند تا این نقش را با بازیگری تازه ادامه دهند. انتخابی که از یک‌سو می‌تواند به ایجاد تنوع در مجموعه کمک کند اما از سویی دیگر ریسک قابل ‌توجهی نیز به‌همراه دارد.
🔹
حال با ورود مهدی بهرام‌بیگی باید ببینیم قاضی بیگی چگونه از زیر سایۀ قاضی خلج در نظر تماشاگران بیرون خواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/450339" target="_blank">📅 06:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec13e6c9e.mp4?token=cw0Ex9Uh6Egi1fJctRcpaYYmOTGhTeUx86xeA7BJMN6iEWflMc0PTx80O7hY0IQONXUdviasYg8st2gxOiFOfW8o3QFSlLfo03LksDECbxcOKhaJVeKPHiCw2hzs4ihTGvyn4QLsozCahyYXkZRqorlrJCTMNikdm5AaVc6yFLGnDefE0OGcZsQrrjAoO5eZYN7tQLWtOm_pEIrEFTUrIN8JCzMUqlASoEnJtdFJBzxf0h44mxzBVoC6ye_D4ifwKnq-pz6nLTnrxFb1yowGeKj5ZJwOrmDIQdfXY2FSuNretJkfyboOCnMvFUPsTv66P4wEQQKP_cw2l_t_N24uzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec13e6c9e.mp4?token=cw0Ex9Uh6Egi1fJctRcpaYYmOTGhTeUx86xeA7BJMN6iEWflMc0PTx80O7hY0IQONXUdviasYg8st2gxOiFOfW8o3QFSlLfo03LksDECbxcOKhaJVeKPHiCw2hzs4ihTGvyn4QLsozCahyYXkZRqorlrJCTMNikdm5AaVc6yFLGnDefE0OGcZsQrrjAoO5eZYN7tQLWtOm_pEIrEFTUrIN8JCzMUqlASoEnJtdFJBzxf0h44mxzBVoC6ye_D4ifwKnq-pz6nLTnrxFb1yowGeKj5ZJwOrmDIQdfXY2FSuNretJkfyboOCnMvFUPsTv66P4wEQQKP_cw2l_t_N24uzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام خمینی(ره): با فقط گفتن «عجِّل فرج» ظهور نزدیک نمی‌شود
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450338" target="_blank">📅 06:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1GzNBuWtIMMzCOBrWLUBDTD9MflYqcRfrMiSSM5hGPo_-H0d_X1NkuPsbbiep4h6jG-Tgs20Igv5VDLAHRCeD494NGo9LCm43EL0uQh17FwWiFCur2U8XFUucI_Zmc42BDmdMXs_PLng6MN5lo2AWmfEbjKmvhtW2ou2TgoEnxcoLarz6F217YRAqKV5g0e1PTd0qUO9R55tpqzBQIKZRzPbd9_yj3M0VNFCHa0uhehNauVNr3PBDVm2Pq_1NdEClIJGeD5j3-sl1psCKaQJzKZfWbnydFN8A0Gskq__aHdVS_z6DKc_lUcvCEY_OXfFTt92RjYbrr0NBx4O9oM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامۀ انگلیسی: یمن دریای سرخ را از دو سو محاصره می‌کند
🔹
روزنامۀ دیلی‌تلگراف مدعی شد یمنی‌ها به‌دنبال پیاده‌کردن سناریوی مشابه تسلط ایران بر تنگۀ هرمز در باب‌المندب و کنترل کرانۀ دیگر دریای سرخ هستند.
🔹
این اقدام که در راستای افزایش فشار بر اقتصاد جهانی و دولت ترامپ صورت می‌گیرد، هماهنگی نزدیکی با سومالی دارد تا کنترل هر دو سوی این آبراه استراتژیک را در دست گیرد.
🔹
گفته می‌شود حوثی‌ها، فناوری پهپادی را در اختیار افرادی در سومالی قرار می‌دهند. عملاً حوثی‌ها در حال تبدیل شدن به رهبران صحنه در منطقه هستند.
🔸
بر اساس این گزارش،‌ بسته شدن هم‌زمان دو تنگۀ هرمز و باب‌المندب که حدود ۱۰ تا ۱۲ درصد از تجارت سالانۀ دریایی جهان از آن عبور می‌کند، می‌تواند شوکی عظیم به بازار انرژی وارد کند و قیمت نفت را تا مرز ۲۰۰ دلار در هر بشکه افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/450337" target="_blank">📅 06:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450336">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d3086b69.mp4?token=J1a0lEbdv81N9ck0UEEk1aYrEhNcZvcMdn8ya1wwYr2m2PVSa9Apgb5vsCb3lw8Nn1bd2LoZT7n2iS97rgu3nD_ZhSvWa6-D7fWXfpk0T4g75iqwFIb6N64kQKQawGjqvHlH_tU87yaKICh9mMeK0UVTNFI826-cw2C-kv8-Onljb8TLzvu6dBEPThyQY7h3UFpTAavBCmf3DdIArs6XjtmkrGcAh0yCr1xDTclacIBrxzC2cRviCj4Odvax7_ekHj5kgc1RHjk9gBad-EQPJOjeOlUkrgeC9lo1qKNV5bqcDQPfEL2oD-yagrbWCoOyWvjoLQM_LrC_K8v2eLojsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d3086b69.mp4?token=J1a0lEbdv81N9ck0UEEk1aYrEhNcZvcMdn8ya1wwYr2m2PVSa9Apgb5vsCb3lw8Nn1bd2LoZT7n2iS97rgu3nD_ZhSvWa6-D7fWXfpk0T4g75iqwFIb6N64kQKQawGjqvHlH_tU87yaKICh9mMeK0UVTNFI826-cw2C-kv8-Onljb8TLzvu6dBEPThyQY7h3UFpTAavBCmf3DdIArs6XjtmkrGcAh0yCr1xDTclacIBrxzC2cRviCj4Odvax7_ekHj5kgc1RHjk9gBad-EQPJOjeOlUkrgeC9lo1qKNV5bqcDQPfEL2oD-yagrbWCoOyWvjoLQM_LrC_K8v2eLojsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ پهپادی ارتش به سامانه‌های ارتباطی و مخازن سوخت ارتش تروریستی آمریکا در اردن
🔹
پهپادهای انهدامی ارتش در مرحلۀ نهم عملیات صاعقه و در پاسخ به تجاوزات دشمن کودک‌کش به مناطقی از کشورمان و پادگان بمپور ایرانشهر که منجربه شهادت ۷ تن از درجه‌داران و سربازان نیروی زمینی ارتش شد، سایت راداری ثابت، سامانۀ ارتباط و مخازن سوخت ارتش تروریستی و کودک‌کش آمریکایی در پایگاه الازرق اردن را هدف قرار دادند.
🔹
این پایگاه محل استقرار سامانه‌های پدافند ضد موشکی و یکی از مهمترین مراکز راهبردی و فرماندهی نیروهای متجاوز آمریکایی در منطقۀ غرب آسیا محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450336" target="_blank">📅 05:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450335">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
سپاه: رادار پیش‌هشدار سامانۀ C-RAM در پایگاه علی السالم کویت، و محل تجمع سربازان ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
🔹
سپاه: مردم غیور و بپاخاسته ایران؛ در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری(س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانۀ C-RAM را در پایگاه علی‌السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/450335" target="_blank">📅 05:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450334">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
سپاه: هیچ اصابتی در پارچین و پاکدشت رخ نداده است
🔹
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/450334" target="_blank">📅 05:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450333">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/450333" target="_blank">📅 05:13 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
