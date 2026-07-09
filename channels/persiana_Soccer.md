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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAj-l2Bt2FkSorCP7NLtlgscKiK8riFh20ItJQ4GMyTbmpvNPG_av77G52qcPPSBr5da-HLG-T1wrw0dKczP95Kyk-0UM8GFq3c1GXq5bW3S-1K8koloij-3eYCOjAnF71sn3rJYA-QTN1OsVpLQjVafdE0HyV5X8eJs3Z4ImBkw9gsgmD7hcFKjqLWJKsQnfSmUp-w-_8JJ5_EeThm5J9APdIGHQcZjw2Zv2bL0bcWeM9Geda0Yeq12yQa5OOVaOJCBRXNNHI-XuK4fBp1s7nAE7-pLlkawvUpTEC920UkA2YwOWk_DG0Tdr7214h4NsrBjOKpUnTmbKtrEGU1u6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Btb80ne3590zhoMtVqwpiELq_oeSdFhrMCBiPINbAHut_KA8WAcL6trl6ZZ7ai33aVr0DwUw9NGAEzZ1v0LLeInzIw_u1DIAGWXS5CM0fqEO7X5UAjveVD4-Qpu0Uo7VfkuBDdEp3RmtWMDfmGVTVQMMzrT7tVTJptLjh9uG-z-efwLQ8aW4MEnYvfuTse5fH080jmcD3WBe2eSSVH_WmpXlrU4sSyEzhBTwzlkBpio3MbEs2uZYh5n2kIVNwxg_ceogb8YBJ8myR5gY0OiuRwL4hFPe73GmUu_h0gEeRMDa9iLu5DpsX4HwW62tXz4IpJQfayIiCAE9nx93ZvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCdkOmd_Q3Z5bKvsEUmANVAvzHQ3SbTKRZd1zAm5f9jcCyVgSW76Ohn8o1mWnPLvT98fOh_687u2pAp8-Wwz5vPZt2x633dWIvVTDf6llv-xjQsV9cmaSZmg0M6SUJsxvRfAkRChRVdc0GT7Pe071uvTGJLlozlv39H_22uDNRIXul4RyG3Kk2OeYt05umIxdbWT6_9uXVa9ewAD3ufAcqE_fSho99K9zLhOafePZWFGrp4ybTohnSS398ayTLV_vwJlLY5-mUYbT2hgq2MS_G-CbEZ2qOANSOzCePE1CG16TmNNW6WzRtoltQOg_05A5mWKk4Ag7k1Q7-uMZPE9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC00z27goK4g5gf7FI7reJlntqrY-rxGq4Mh0QzkZvDW2wKalxwFh82DpdPpG5PQY4EjR9iu1d8PTTWiCuxowG1d62iHJ2PK4mEGdQbLujhcbc-pjvdwRHGbK2wHLmzXAKWaGpwhssiEgzZWrXMAnIr1ruCNAg1URejjz62EanAramLFkON9JQwNeSAeO6_YllKqxEoPzFj3ccCxSjRZNCxV69GH9VLFjUYM9ALzsJjsXVxb_KDK7ED3VDq7Jfe7CWBpYhT5iwHriTLfF8qYBtYqjWQWiZdac0Bw-mTm8DmcBdC7548UoGLfmq85R5mDYnHrF-psMAxuAOF9oUk5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT1YkV4P330oq4-9mvtHyevIii-tObMBEn9hPoTC8ApXfgNzZkvRZDlopHZsLDIkbWtcdnOX79OzkfsTuPHZyxezHu-H3Z5H6VBCBFzb1uZZpcKTATjnMy-EmeKBhc6L_FmZxb7twwH9yaYN3yNchVhFr9pDFPUUs3_wJEuY1-I7K-rhovv-8DvDmF_MaIqh2hJ43xUgME-rVj8e7Z5oAA7wErhnAXsEbOC5t4jvgCR5qhUmpGmmik51GQG7YILDDYaO5Jn0EsRoOerJnCidxf2UQjB2D5jeQkTLhHCdg_LsV3nV_MKTDqRClJh2OLXob0z_k8gUkM4AbBVVP8puvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUNpWBKwecjFe1m4_AyHp7umMEz2eaA2RFRmPxZ3bShTh2IASqrHvYZ2zRchlM6z8AyQ6JUT2fiHz3QcKmrIfxYfBYaEsBgpHKA_fIcOx764Sx66u6i0zLhNaGHZXKoUMEzg0UOuPYGZctM7HMsPoOZzW6rAn0nybWTaJbs-0sc_L3j1t0qFNvCjni_4OdedatyzcG7D3fPP494iT5azie8zAB6ML2od-vR5WHhG_ghMx0VUib9SG6sBEWJexKOvIkoK-jkFPW86hVM_ExrT8rLGauqXBFd62uP2D1ompA6srzNyUP7HffLmya5VOHvIJ-mnIEGFAqTtfaibWGGCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7QHzCOVmH2YzFvNggK-Piyi8ZPfuqfKYErPxnbjSsKVwF0_LdFI3wYLI4NosCS7PVfSN7ar56yiRIV9IATPmPK0aI2__EVHB_ONep5BP8duiwZui3dNZTXytvUDwjjFOLRvQbE4gqwTSjqrJRu9EhaPRvpGxI9jNaVlH2MPPZjptZ4XI8tqlkMfAMLREqLshUaoHCqwPKi_YAPoNAPZ0mWT0R0-RyvbXIbkCwI8DQrVEd3ag6VHTs_VT5puOvCQ5XaUZJBTFcS-kXajBYOxbg0eFrpa448astT6fsAcXTDR0GXP5r4OkAxaKxYW9abCGm4LXgpX5sisx71yKf53bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_liKjs4iGyhWa_apgo91ofu6HR2Ru8MCz8DnT7NCGm0A6n4ZZS7AVx1FMY-Qr2KK0peciwXIuj7W1evKBpURbFUTeHR7ipM-h6faSfnCqYNdn--v0X1OlayaLHI8COsLmg9ehCFEcXxdaMlFHn9Ubx5ny33HWO6bnbR4OsxSjNO9QIJXAsqVcFADgRjJUe2vMee1jPQvUCDI0qLWCbEdEqogum3YAn8SBL53P7dz-ak6cPxOY7IGobnV99iVlnmUn2KSvJJEthbr0NjG7jHdojQuGPux1-HXDCWEADZbSRLyovq8ffMtuHKuG47lm_2m9WG8Z3JyPO-qkGZFey5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKeIrhBE9PB2YgYGlUqi49hcl1YeJcfpaduU6Xl87Hu4rX4Ho2b6cWpRgUfGJIY0jSr2OH0kdvcBwS77jm3mDaSF5jYm_t6gHBjD0XO1rjSW2DT3iydUhfyXF5ZLC_WxsTPFlFnawfB5DFb1PUSF5POMFgZqjUcXTQKxiU7sEeWNmxFtrwrvO_DiIubu7ujudcBTLnJQrtkzZrPWbCn3ypu7M5R_YRK3EAsNT3Rd6NSRKVwE4ccSL5_urNtCskMYOAvYwgfR23NMh9th5UWCTfd3I29i7SHSixl2-Edjlxh7aQ6KqU9tD6lB6JgGZWLOPGSGSEvl1Wkf2DVk9hz44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAUM7kt-oHcC3bzVi3dRFiD5gZ2_eg2Duf0hjd_NMpaFJ-K59CzvAbj7iNlg8T7SIbGKkKwEMqcQJkNsuv6UjLUopdGBxGEcEjCr5L80lKzWlWp9jCSRQ7gDx5MZXFPC5R92fpN16Uk6xPS8bo0TURKvKwT6rJequeqd2i7mZPAb7NFDzZxQSjKkzehvFM2vSWoHf9qQd30oJmdVjF_lv46pmo2OJ_D8JFrcThXXLGhYf38WKMlXsYohrl90i5PRWeRjxeb6rBEsivDO-IjTA8EoRe9Yt7wxSLhO2GcubiEIos2Vuj-q5uhvpWf3aQysXMAadxfvbl6FoZ3l6NFkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLA0WXYacawZWx3_u4HVWty577zpM2nH0JI1PYVmyGQqUvEp1q01uG58hk1ZbELZeOu9k65wQWfMzumJCziZA4ySjt6IcbKkOX2HkrF3jBPNSwBL7d2RkREWAe-miI8qBFzB_EpkvmR_IuqmCJP899WGGEqcH6kwVr047R3CHt2wMn0FrMKT5jUcPsJVs4eAPTLyt4Y86CBr0NZoVfxbJ85lZUh6lJQvUkthwDoCJO9pRBoAtPiBX3XYOe8dqUff3iEZd5LiHoX4Xr8yjw86U89kJw5-nQ47cmEahzQ5wEt4QywttGBhnYPQY1RjG3eKmo-TjVgUQ5xzt_o6CDZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JosCXh85VHRAbDbcDk3trNKCJqfhPLRdbzFIu3hQ_vtvTgWHJicx5F-AX9JLs09T7lMfL_1f2BNRTU57A74IZ2ObgHel7f8HBT2UdoKQPLT-ZG8PBWiKpPr9r4dfjzF2fhu9787rRd05pYkNHuNjMytulfndcHY1NdJ27vgzp-xxNol3Yf3Ms5Zr88oj5cBTg1ksb15L7Wig6QBD2QDznE5DcTc3R1tzEYH4_90VucOiG0VidRLBCMr_YoLL9k9p4xYdilNi1GOmymufb9Jra2ugB4tBSKNraF1BVTQw15yU4sqJbUVl_wHvLFqXs7LFge_U7QhiYerpbL6Y3PY8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGSojSNHXigIM8WCCyt2nR8U6TOX3bq22Zp5Y9JYwD2Q-TQfIGGckVJ4UlpeGsvsmrNPhJJgoR7rU76MhXFViQiC1KP0geYwgdjlXMd-EWMBD7SdVcRxnkosqFu3J4aVM1EbF_UBoYVBJhmwlJjvoq5jnGCFbuqw108mwdWbKYWzO--qDjTCXob0gfJJ_KRMg9lFWahiHPrBK2wiF3CxC-whueRyRKfadatsjzYhpTY2bIXwQKAzzLWWP_zxvhTKpX3r5GlM_EmBCg6alfOLTAHVGQa9Osc3D9qM3-7_3yC5YmXNXCLUCbc2xR3c8l8I7wnLOogmoPtc3ZoA2eWxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiVHk1CQHJj_RvcFYPNcsdxPxBNfSYgU3vcVHzmmkubLFWE9FqHn7fDin073xDta0SYYqhlno__ycjO1qyBcBsKS65dnpK0VIrv0w2Eb9gg0FJ7LH2BqzX3UTLC0yTScCsDtFM2iiZooKn1X-FOHE_lIDVuj_JCbyhpEpEU2G0AEPHhmTaEtym9Vv1CZozrYETbWkRErU7Ozq3PEiFlGh7IpGt1do8PI8JkG4SXfYJ2dx2WFq6znXmexmV4N3K80h2m-biFiUrm7sclO0H7CEYyF7fV0HdpevaIzA_RZemAt_YUd3kjIyrq8WBIpkI9MFd8GIkvczLM4BOlew8Rtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxmiN-KAgTdU7i7HJPqCG_TvE8molKMeNWPB33edVWpBhiLxEtF9n8N6MzjC79yx-opxlJld7xPFf31dRIG8PRXAkBJ8HR_A8oEiqkFQXCn8Uw9oXzjHauYAL3k9HQ1WJe6w2iJa2SpZyaXMx5E68mrbxCK5jMnEFpoKNLEXK0mofQSzASwwxPLl_Gey21bHECa1j_TlcQGtckEHsHFICg5wp-FZdyWX8ypcsBo-NgddMl9IKXlDIHoCa5eK8QUsM4E7HGt9-7sLfgAwtsiabwK0nXuCRYT2hefSt-leHijokIDMZpLrxiGFVh-g0RbCtLFlJHlbETK37LrM60Fh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5hBpvVZkufDvgzdetBMa4t7-t3ekHa7Z_gTvuaIw0WVk2JiKgl4t350O6oHY-TmU5MwzBP5PieLKiikhJq9wrKVwiggY7dh3nd5bNagMVMR2NEMPDkxB5PO9txeim1KCfpUWn5-UrT67YhWe7--uxkIAR-wDE8uh48rmy6gUrdOxvvUwcHLQ67Qbu_zXhT_kDoOuzc3BuXXL96DdLhZC2E7s1gm13MC7tNgBQo4F7GuXiLa0Cv_g89MQ6FyV_TshDuLL3MSgMW7Pn-SR1Q6jpfHMGvOb0aUS65r-v6y3lzN2l278FnXv5V4TckeMhEEBO_Wa7V7E1uDCuXqnyyWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIpDT9IRQeZX2vzd0hujlyuNTqAYwkHwiPDgS9XmMX67an0nvFYutJWvNy23bg5aGNl08CwR33wXoc-X0CPnbtQ6QOoTAY2lGCBlE72HUGVmqoErxbML1tgLANpl10frNXnQfoZztdiFineLHACsoAmRMl0sLPPksXqMj8hZLvA0NmWH2jDpgHaJszmrysYIbndTbsHG8-Fcex6q9fVnNaI75ds3yotlDl6yJt0vnjC-gyhf6vAH9mnBsrpsvJ-x1WiKvsrie6YtYYRkKGctLH2wV77yTqGhzst6iTkVApoB0OtlJxZGkgFW1-IzqNdzz7qRQa4dxLZrmycfkNr7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szF6WelATEBsSN7TeyDrwXiWO_3Y4INYxCK_7Za9l6tGIjLbCSaDQH9ZRNfVbiWLiG_Meah8fTSxcJZ02Bc9xTvSSrAr1CW6GbTfXad8ZuNajUF1UeX3TRw4MR-kNCbynmYJUUAzTYTHKst5grV1XcP_rSMne_tN3Ixv1dEQVjqyUnbrakX4jsM9I1bsL51Kq9xPTka8hcNzXhSDTymJuNNLjJ0ThS1PHqJvdU0pQevLeQ7jVssk1oXa3qLCotD9DhjMY4671OcHIIEh0VDLZuwoHg5wy2hMtmjXPnu_vAvJgJhRud77Z5OTeMevkkuUHPw3JPBY9fq5smtUPRbuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Funaps8mxy1k28sM011a7dimpvu_2ra5xWwpw8JJtBH1unqDVUxWWjRHm2AKCNGhHp9aDZyYAC0DdTdntNXvhzVY3S_bSYZFcTMiiTWXDb_qM5s8SjClgYv0DLsIjzs7mBUdiemvu-ROzpDcdCyPVRP0R4BduYcTjOLNRxxRhw0K6RYM7rudHepydDDReT50oTUviUU9vOmXdVB3AvjzA-9sUe8vy6LXXTN4LMTePdi7eCOJZ29iz1E3-QY4WPdXlPJa2Zd2ZVbMKDXBPh1m9FTaEiJJ-kAuiVpEjg-zvLzQT7at6SfETMrsjbx3RuTWQ1zKXqwiXN9-IbBRUok5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Funaps8mxy1k28sM011a7dimpvu_2ra5xWwpw8JJtBH1unqDVUxWWjRHm2AKCNGhHp9aDZyYAC0DdTdntNXvhzVY3S_bSYZFcTMiiTWXDb_qM5s8SjClgYv0DLsIjzs7mBUdiemvu-ROzpDcdCyPVRP0R4BduYcTjOLNRxxRhw0K6RYM7rudHepydDDReT50oTUviUU9vOmXdVB3AvjzA-9sUe8vy6LXXTN4LMTePdi7eCOJZ29iz1E3-QY4WPdXlPJa2Zd2ZVbMKDXBPh1m9FTaEiJJ-kAuiVpEjg-zvLzQT7at6SfETMrsjbx3RuTWQ1zKXqwiXN9-IbBRUok5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3OF2rY6rzh__c-2cLGbKmxssqphmgXoqskvv9UF9FlxhZXnkofxUZfK6PcArPfPkLpyhd414-JwZbtnf2pPeT2bKqywQ6LeGEvgh-HrVE--LUhRhSUkYKzq8PTTUHjpX2IE6L3am-2E3l92wp36kJai5mjyA8NGjgynw5vkHH9HMqw5ASjupUwiHokgnrYFRLmlYxmQc5Uq6vT8QVCNbUZH5X20zGNXQjkitxryO8I0E-o3LhpsalPsQ1nP2JVVnWF1wGIFVfhpRNF9H4Uqb_Ysql0bnU6cLKAizx805NfdU8hm3dt8ThwiDnCqqKWfQCqCbVHK_CLFoxMkU-KUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv0-GFpZeBGLxwmTqv6h-H-EluiJ61YO5sgBxGa16_yt2WmniQQg0kXV-lsdFLANJn8YU9_rHksGWTqVDy1Ud43C2yvCX7-lLJxuOsytrQ4jIw9tK7Yw3K3Ts47dFxZqJkKLyhpNlicjFMk7TaEK13DR9J4TmtN1nX96KO26a4TtTIdTn1BoEbliz3FXVw_CQ2HbXYSOQDSWnUHXl8iBVVw7TSgJm80SwEJ-9CJJPeIzuyciE6M6UgfBMK8CeW_tZVQgJO4TBS57l1P6iO65WbkGEoU9o1w5-rIytW1gK5bMunm52e4atyWDxSaQldsjGCxAoHIQkRRv2GrMAGzc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyPIUG-A4Gfebxl8JBGHygw2fzdrR1fWzhy5_cqcMBUNgspczQSLE6g6BpvOHxjxVXa-B_VBlLwKBdvQUw0CRdYps0JFIj4N3Hktrr-gUZsYnY_Zek7zb3QpFBXzJz1_Y2M0aWXKy0JRucAcx3QNQU1tE5aQ4RkclgNiv2DuPlXsLq0F7P8LqFm5qAIBcGbmy2y1qeqgiPM-Q10QJ4IVlUUzCRgy6OrBUJkuoeNA2tWZirLLHu8fUlJg2xOwdE1zW8zSR_I4KflZhcmfZmMyxQjeyEJdtAlwF7AzJdeJapyqSBajP3YfIapswwzWB88I6xVAA3iOf5H__XSYfIscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=aD6qsJGZuR1tuVTyYLwa8nPgdO9h3KA7z9ynkb6o-tlRr2iy-XyxOcPbRlZbpmNnsPCVoYK_RkwmrDIImT27MB4Ql5DuuizPura0SKXvedtas12xicP-ifyW2yhcNfflLqsdNJwLkZnytvId093NIuGlZSO2P7LEOZoIhKyfytAXE9AojYoWQKZy0J_YXMXqr8OrpUaitmDBbzv3XMZQn_Rn8ZLcMQxyDlUr2SYOg4EXM16pvkVVzSs8_dSh_5e-qQadTsw9UFHhB2y7S4V2IU9OV2e_yTu5idMvMgVkkpO4OdwrO1uc2tMJi5ZiiXQiqRd4fk1p9rIH2-IdKJK3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFce7TkPocBu01EY1K82vDsPGPP1NOb2W1tAEXqD-EFq9IXe-eeXUZ45_TbA5b6xvNDeXMZ57yeqP2Bi-lN8u7x49fU_27ucGmoXTOtt_v31EcLl5A7mgDHB7ZNMfk0_G3F_Ywc9oZ9_VpaNNLFaqqSptWrGCEEff_GttHjKL7bZJW4g6foyQqGsar4g4Hg_EUQv_xWcsBdtEg2z0aWMmt7dbQXUOeYDzoxLMbXIJ0UfBqGTycbpzPlfM4SJCvjSK9xDFe81cj24xmgYBFMt_n-7rgxgFeUWN7HnwFUqVNL1M_Ln7BJ3hAy9KTiG6CJLTwn_0yfy-KXkIbbka3Tidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFa3lGLjnInVlbhpXa406gZYU0stxPOdOW4QLlh_xzRf9mXW3MKz5HRNzpIYs6hrjUnORdEFSzrcHKzt-smGiW5tBP2lv3MxSBg8tQxbHnZizmrz0sX7bG9hc1Be7hyNJsSny-ZaKNAVL6H2Vz4aV7M4wceYeoQzzYphRNQfm1coSQnoaxsYCotglcKJPT1sBFdNsoHfi0Ui6iPhuKKf0apu7ISiM2hZjUzc1k5qSOleUiGRzgREdAp_9ViPoVPsGx6bFU7mi7qZrOA3PzlDc7VQRqTOODq99tbxfD8Xt6zmwM2LBrN-DcSwk_SN2uBkJ-9PYC_R9NnSbuAnkPqhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prfMKpWXmoEGLmXsUU-ZoRba7zPYMH7sthai8jxgw4DLBpMy2s7ob65Cd6FYXaRDfVdBcRqsPZRFDpI5BqYIxkEEVbaCNJbYz-bU7_iG1AcUfTsY_0mwvVaorytgx_IiinW6JyFsnIj-M5qyD5LvsBobbz_9nlFbjsztKuQuFyeHStw1oXdBRm-qxJC4cawZ5EVvXyGftuzEwkFhoUhwuwLsm6Z6QBGzKnRIUp6rwa1KgN6zkXppKVa00Hp8hIfYtROsmJfYy2vFQa6fs4_hLlOibeo-z0rIzOXL9NK1ATkRCjHUetDKDtgMzZnJyF67U_iLdQ_5rQF3cqJeQL5rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXpoSf3xU6JaEvyz5V0ZGZzws-g_xaOZE0lOGzOaOU-ZfAJr2G97ALRZGnrofz22OQHfQcKI68EkPRpTK84_h_IMLi5lXSHeY6L-OA6hsKZh3ZOkg86lajzDFhHJPU2KpgyvcH0FAmd2fCbTvgCijw57Cs4oz8xLvnfWvXtMrI_0RH2Fri5cD0Q0_sKdSQWWIVFqK8PHozxg8PVmdyWFJBbDw8HLUx59i9Lp9ZCfJbl0Ur46o9yTr5lpsOy3OF-LfGai1_Rztc39Atv44gGO8P3QNUCfTCaIYe1lIfzyB_hnxALC3---0RdkR1PrZ7VnVev0Wu4gnUYW6UnkBJ4Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9IzGpAivKCiSiMAO5OfHrxD_DWow-SaUesgCFHvzxzyZUdN5YwL1nOuOv7m19MTccw-5VTWamJ3eBoKiXqujnd9UMxHv7-V-4GfX2zM2Hwj6cAztW8lIcapPJhbhVK3GPTM7FPcJj_tFi5y8JwABV51XljHx3A9Mr8KV75IQA_OjwDcZiHzSRThF_FsqEbSBy06P2seFBU5Sao_ztjIESBMIrVGBvKrzIiFEawcuRyBgdKP2hgcYB2gaUU7B2J8dwQkBRcpcCA9m5LOwGEUkJvn-i3ywUe1e-CcC5ukjm849JhQpXOr-5n1snS_JTqA3tkkgXFIX7UAi_mPV0ZLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou739b6LI5PmHjCUOXoKkN2wjRxhZyk3oEy3ibzAUESvLwLzSH0-E-lajZ21IpvcgNsZtJ4m-J8m3bLSlAVogVs7wPph81hRuKrEL9eXjuHq2j4saoVPatcgDcZZznQcHieatYNnxyUcOrFaHUojhetcD2M32-WjaiUd16R2ZcwbzfPpOm81caCYruo4T3Vn6ckeC6BQxJpIx0rEUGCBtjRz0rIkXaL6dbcKgHINR7a28YOoI3D6d0L_he3lA9mYR7z5L645LTSM7daqtPWu14mdZFiaVwKzKy4FpyAYWz2USsJeyURXzK2lKbnaJ11SPaMCQQxICPvbLh46J1OmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwM7XRzKzA_8gjcixTpo9Mjz5GDj33fYFCaCiuCpJTiIe7ZVF7MSwldD0Ijlj9aEef2rtF0UsgqNwfcCvUZOTTT00jME7kj2keQMXrvx5KtM4RYE5cJQC1TIfCP_qRcPqcfAz4cMkyWwzituScECoF_XL8YmzF0azzL6QanxI_x8C6lILxPkSFbFy1hE2bVfeuG3AJFN5_khtKwuCq_OVZUl2ISOikI4WProH_xexQt7b6j0XUQHZFM4tUpR9nPTaje4pE6GMgcbWQ6eGoyEncWTj3lC6YHOJ2e-qzfWdunBZ_6sfgFeCObhcVvBG-4B9PzYD-j3gbV3RZZIrE4IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeC19FpaPaFa9N8mvwKIt7G2Ud5hZ0vZftlamnMYRpAjlq8s-apwBJkEJA1ygLqx5yG-906baqBXex6xGapY4q7opEBQlcAsbrbohq4DSOfE1OMrSXnixSyBsgF2lPu89gWZOVwRWlQfX9_AWn06_UNmkNysIzYuQU_KmwtXJkXfc6u2LK_uGkdZihvBHuf6JtCBJs188kG8W9DXKylIqtgV1EXpEYlWNpz8qN4vJtizlVlYZnPGOY7XjaCigl9zWgJM7Diza29fY3rjEtvw_5VEYwvsZOAvIQSswXhwrjgmmrWBricKYmmnda0OPf1hvvFT08jENKMgekeBDpQYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grWniWMRolxizh_bvbM-HieomIZgmTMAv-Z8N61AxftvjibIy3oRmA8Af90XbVQqlrzD8NAp2yeJUW0BGHXb9AkmwM6I4Ssdbj_m1KH5jv5bs72arhXqdHDmAe-tobobegs65Cljwh0oUqM4FcBaMdoIMSJBGAygAeYAdnZJkg0sd7Cp8-O7au40gRJnXegDR4qyrls1fVlBTvRpOLhDKOy2qthz5RhCr1KbaYbhc4Tk0m4A_rDQRlkR1Apq3bwPT0vViczeMB3Rxz4iqwQW7JOAXPUpSQok3aj0bb08etny9zsOdy-zd-J_tFMEloZCfdocSKpNFz1sobPlEISBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVHSLdEEVmLOqwq7pOiBqT4Ot4wRUOhaU1DdcsIDneA9GYS5vRfpHyfM6BthddeE2aNtCk2DyP_DRHNuu9-pN0fNZQg83f1Z_5cnnzXcB2aQPcpDIJJwo0H59foMhhKZDfxYWnxS2tYe5uO1EWGYq8GerW_DOZaK8ZD6gmhs_YVRFYH7cfiZlvwUpZ-LQl4mPkG12sE6JCdjT0GR_Lm1p50mfFvnMo2KJ_UhFEhhV8CKUz2jagVZ55_HJ0tSRpiglEO6jED1DNyqvc0DwfivDHChOpCdUlFQLBA-Y9oCdQzh_tuT3oi_GopXzmCSEix_hPiwV1hmzopLgzgp3OwlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyVoP0F7ma8dSIlI3JsAKGEbm9HavuHasBjfAApBgqmBVKLV7YUzAN5zVJHsF7T5CpoGFmEfRkiql1tnRYHSainahBryrgqlOXm8Boqb0GyOdK8x6HtwqwPcTDtPAV5qI75Ia5b_hURmob9uoY0JBgINmmcBKNt_HMrS72MYFgkX3S5NqAOpCG9twNWzpLJr5tYKZorDdf58n3Ph6aHvz3HVcew4O11xj-8jSS_vN7NhVuAewd8MKfbn2q2C0inW2NYYPNQ0sim1RDrINvlGqm7-xtxRkNe6xVMagk6-2WYW5Yv6yZ136IkHWdEsstRKsJVEaZ7sSvPGbyclUrt_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aryq-eFvYca65T336GEj8A7sh5trzJVr3NxB7PLdGG94nn8BrF6K06xQ5fjTglVcRz6c1aYK0NdjBqBM9nMiYZmB_rKtl_bX7hwNmBFOrZ5jh0vrfaVPITtzRBzLi74Xj7UJ2gP85gRt7BpBxDGQ6ON1PB6cTzKjWUzmjEpo8_4sSmeOBSBOr9S2tFnhsobpRSXgTZEPgoXYw7Ol_fa7wKrLER1RfQmcH2Af6lp5xzUA7hOmXeNQYWxM_FmJr-9I1vuyoGf_xyDle1SmbnaH-M8a3TdycuEWRyCYtLV3G_Ou7oKDlOOe2hMR1bTFwgxECqk9v018oPI9EnogJ2bprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0fBOOSEWciKGmcB_typ-OUdbTfvKiYrWXBZKPCXtN0qqpkq3T8d_dv7I0qy6zH1gCF_tho---nuef5wfnpJN26St8k9ofvrBYYYY2XcqEOBLZvqfedmSgCCvBbjaCOf6C2HuQm4NAOb6y6oZnDm9lkVmsj-UMsauSbk0y54S9N-Rr1DHLRdR0hjWi76H2Q_hOdakOudG-LWSty1r_Sj663ubQxxOYp9HPkF5Vtr6coU7NVOdeZ0Gj1eLGnWKxiwleeuebAPN2D6gRiUyPkmCYimyXOHuaFHc8RY7GrrFZDMghYVzAIdD_9cgo_t_9dzvEB4Hk_2rrOVOMkaXHJJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSACBhjpJY8srntsNgvqIUvsoXaEsDofgAT6j-UY_MCUpOwwh2XGmhG3ZHIFd5JT6LrZfmDK3Abt71pQ6HG6GAYTy85nolgo4AyXSJMGu3ob8JPxPK-Gz9duEUSV8M8kX1NKDBfGkhwJ3Xq_SDmG2IiovOsJuyBJDAcGYTjIUFHWo-GXTLu_sExDuDK2dVZoBurkDyoJv5zVIroxfVB8MhiwOODyEfD27LgqEI98nY-o8HCdyuMt2ROvDmMjpbo-alomREGJFqoDsDAF9mdm5IXbe2orB0fXpUH0EVz6OUGiF3l8bC53qN_oZxN4F8HjwBAC_ynOjVPgNcsV428ajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKqYXS6kpQ6NMqnbbR6IWF0IDt6DSJLkMd2js92TcRyR32J9Q_4L8HwfDMiPF6AQd8QmqKot7KSRvAWvsE3v9xNF2PPwag9eiNR_qCk1wxx0ZavKUYJPe9uqHMuXmJedBtvqObtJVGRWL89AfE393AW5wKwOhy-nA2-343qMyeDaSxEAoTfrAM1pohmudPpqg-oBEugGLVJAbYKR6tbA_4TO-j40_f-ea0nyWh9QqI3ReekPF6es0Wsj33fUWXMHYnNFaEECQfqGW2jjaaf8-RdXSsLxFg8gqeiIGdxUSItlfhKVCS0QC9j37kKEJclevySzD4SI3WJijHBd0V1f0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFsLjJyvBP3t7EG-78Yt0vjyptU2W_i3se5iN-zpKiWEjGoDbstTrTEuuNfe53PRlaV2HYgXue4jCmxih4wAJRgOAiTn51u6sR1xiPNl_UWwbyFG5xrQOjyxkf3jhDeJ0tKq8lzMoGsog8rBtCYaX8qmc7UNyDY-ttx_HK--SytS_99H1P5lfqIi9b7qcu4ctjIHXnVZdmtzGDj-pnu8PxWC9ityYgvPkSZjT2buULYrVVZpqBeXUt8K-j6nCkatDVI9ZilCC7Orgd8Tybc6hvo2RGq9lyqG1XaTYz6FvlnUx160i3AOorC66OxDOBQSMNg8R3zDNj6DfWFE_dnuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vdrxp0-E3JuvUEr_PZLG8kH_cHyGXEObI6AUwuKt4a0wPGoyo1C1dODYnRRlNM-FPZiyHCPurmwTFHjbeVHLYjYShchNRQFyrNfLK070PTFEx3PBjqBaT1FNJDSSfLnA7cRG7309qqVoZEO4pS5T4u6KLtoLXUnbGxMUiw-M920CUCXaJKS6WGHLTEH1bW6FxU23MqYlX9hxW1K4xBbuPGE3yvqjUMmKsJizerDwj1VILajmn2D4PsO7DLN_j1s4GB4u-jHWt2LOp7AhMh18m4grpUj24EukdupZFsDbDZa9unrkH4QBDkZrv7jLcAjviMaEYcQhiw9-m9EvL_R2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRBM9n7nHJC9D-N6IqxP6kO2ppVc6GjdqK-NZcVEmT4uUpNAnxYiFN3Zi69ClPXv_PJH4Qtlgxj_3tRVyUCIk16Vqy4z1ngnifsSzzuqrI8EOg3catTGyIKcOnVxXp9KK0zD8RvtocuoO1ufkzyShWUQwpdMA-vGnx9xpYCp6ohMdYYwW9rJAHafTUT6xQhKlUIujvlQ965ooU9kHIySp6yxtF2hvBbNr8yfItXStVHCdawx3bMzoIiWMewxJuUVjDnBTO6iHi0RtVKZfbnzJsg6ti_xZTnCtNkS5eVYh0rDghfXExcTRkWCIaYRjRUq0BgtoYvhWyRDz-bFUEmpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4dXZoGPMfDhzlTsPz6kiKSkdU4eF4ucQWHBzrvadPBMYPAef9_Blve0Mj4-F8WYTFSb-vSqlWExRXZih-dU5_8tZe57IAUGcRR32oevq6mbiNatl4z3H95r4zJ8HCpQ_4RmDHBykQj8TAn7d9OL-vy8TWtwAfMjKa858bRaOTFEW0AVu7Rf-U6CyWSVxu12xUwcko-r9R_lVLJL39AX_krOAp9MEvcg_EhRnuzM20vaxOpR0ZJYl1RKWtV9qzNDeRZgFpsONLQL0HxzptpzZj4lR2fWcIzrKeDcM_N4VVL88xEISxP_-GZd2cKwoq906UlCvahFmnhXQbIhYDfwOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=pjomXs1r0cSdc03w-Tt5SGItXAcMCpJ5IkvvnabWGGwb0qcnOm5hj7tbz-oP8pr7eAhI13b6JoAKuWOyIq38o1uJDGEeK5bGgigJMrfZmI2j-FjKFRL1vdRh03_nYFRHTX0esp946GrWh2Zp7DB4h5dGjvw_8hSL71omDxhFGYoiHzrfv8Qxo1cioI-yLslqjGtwIYkzoAz37yNYiEjDXTO6sO5ge3sT6YMw7qOyPg0C2Ju4jTqRrqzNysX89ZDrOgg-ppQkotYHvHkDO8onnLEmSGdsNg_Tiv4IOvIj25J1v4GqXCjuRH42WFt5Bz1cRkR2xenXU_apgIJT7RuFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=pjomXs1r0cSdc03w-Tt5SGItXAcMCpJ5IkvvnabWGGwb0qcnOm5hj7tbz-oP8pr7eAhI13b6JoAKuWOyIq38o1uJDGEeK5bGgigJMrfZmI2j-FjKFRL1vdRh03_nYFRHTX0esp946GrWh2Zp7DB4h5dGjvw_8hSL71omDxhFGYoiHzrfv8Qxo1cioI-yLslqjGtwIYkzoAz37yNYiEjDXTO6sO5ge3sT6YMw7qOyPg0C2Ju4jTqRrqzNysX89ZDrOgg-ppQkotYHvHkDO8onnLEmSGdsNg_Tiv4IOvIj25J1v4GqXCjuRH42WFt5Bz1cRkR2xenXU_apgIJT7RuFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4pcHeNOxL0xiNG3MY6c0nS0zVKTeqncNXxJ-jrKU11jlI6hNfueZZ5pFvrnvnUShjPi0dkpIyb3NPdmJ5wuMT4mImSAAg8dlQ8q4f3QSDkmR4py5kNmB8RizfLio4K6VQlR8M_YAqUop6UV6IyjmGgBewwyhZEUxUrH9YYHsUo3iyfJTNgxlJ3nWEM8hpJfVuLdoziK_CM0KUTA22SlvF6_AH4J3at-AZROALPOV-wfnRV0LiCJKxyMY8_cz6jlqrkTvXs1X6Nwg8Mmm-FkehvS_DvTBwKHOWXvQncK_SDIbfgr9_VIVWc5shitGWKe5G2OD9Jebz-Yfu3jvud-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=hhcxMLCZVGDaAAE3UK_XqQ-bibqETzq6Z2i2eXi04I9S-4HmpytUY2boId4Z9LiWrPh6CmEGOqwyA1vrbMsF9VlCqw1cs9EFyWpceso0CqpkWmFIWM-WXY6tEEai-xQgldAYPQdzy6rBbIu8nBqYsKpQgmXUfLWy1qyliG71Cm-mLq7jmB2TI_v9PlFO-v5kua5k6uVdFWrFa524a73_q2oeTEYdJ23zWznM3OlVJN6CZkv0L4saf6MmPXP8hMkb5CJT74VLg-Bpzlt7eCpRyKyOMziFukbVwO9zdxjGK5vJFwal_89m72wAIKT6RP9b-PI5FOi-hwkJAFCNiTceu71v2li3Erje5GfjuAhyJj7BS-TsysjlwPK4x_oiq827uW7ozCv_fzhkZDEP9FHaWWm3m9Gf-Sf_Milrn7qo71sxjozEaoONTmsJ8iJZfBf1KBsT9g9wC5P2BjSJo2KUA6oSSRjw2G5D22d18r0uiArLdTjN1rB4XO0bqXn47UOdR8FPeb09EfxuTSX_N11q2udsmBUnHJ_mY0dBlQ7mcjZMHq27YA1mwuxKDnHYvMcNHgKQ_OxHn6STSejBAa_x0ecjeFopdeCRuVH9pC0FC7L5aS_cL3SXVyw-6SnxF9F_njA9qi8eDzg1l5AIh6-qL4K9I0WfEsseBXYM3NGdYYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=hhcxMLCZVGDaAAE3UK_XqQ-bibqETzq6Z2i2eXi04I9S-4HmpytUY2boId4Z9LiWrPh6CmEGOqwyA1vrbMsF9VlCqw1cs9EFyWpceso0CqpkWmFIWM-WXY6tEEai-xQgldAYPQdzy6rBbIu8nBqYsKpQgmXUfLWy1qyliG71Cm-mLq7jmB2TI_v9PlFO-v5kua5k6uVdFWrFa524a73_q2oeTEYdJ23zWznM3OlVJN6CZkv0L4saf6MmPXP8hMkb5CJT74VLg-Bpzlt7eCpRyKyOMziFukbVwO9zdxjGK5vJFwal_89m72wAIKT6RP9b-PI5FOi-hwkJAFCNiTceu71v2li3Erje5GfjuAhyJj7BS-TsysjlwPK4x_oiq827uW7ozCv_fzhkZDEP9FHaWWm3m9Gf-Sf_Milrn7qo71sxjozEaoONTmsJ8iJZfBf1KBsT9g9wC5P2BjSJo2KUA6oSSRjw2G5D22d18r0uiArLdTjN1rB4XO0bqXn47UOdR8FPeb09EfxuTSX_N11q2udsmBUnHJ_mY0dBlQ7mcjZMHq27YA1mwuxKDnHYvMcNHgKQ_OxHn6STSejBAa_x0ecjeFopdeCRuVH9pC0FC7L5aS_cL3SXVyw-6SnxF9F_njA9qi8eDzg1l5AIh6-qL4K9I0WfEsseBXYM3NGdYYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRBT-1ac8oaAX0WpD6XcdI0DTGFQxKcaofEgYnHylOkO7mN_NDi-XKDF7dk62b7UCk7Sj0q2LXo1i0SVN32X2GrvxWEoyJr498mQ_hDWW8dJJ92nm2rqKl3Gvsk_VAFMiZxbfgEt5j3OaOtvUXZzJmorSEC0Yo7A5hoVozqcRBRSRxcU-D5K7c3cIJi174jq6VuswqVhDQ7fg1YH267L-aKtoCPGGybeT0VOT0Psg0nmVEy0HS1rTZmmn4PcVHztV7e2EZlUJ4sObaCCDqgkdmkSykOhqIuXaXQjDTDnHCh6ARIRk2AVRMFww-Zghc2t2N-ytS9S1hH1_FWlS4GUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzjAIJYFa0F9awTQiQju0aOO2H2UzZMpzfZNpfftVN_0VzmjC-WGw1CN2PVmv7KK9dN9TSwzDhP1MSUo7KgE8YEvdNRmHI8xED86jZjqfg-ayRV2-uFKe9tqEpe56UsnuUiCExumbELSi090sJLREETJpobsFi3U-gPaMWcUJSsxne00mR_4Y8ObCGSs77cq-5SleCjMtNc4naXqIOz4O7JbFo3d9HInP1ZicQBKFuG4z-McXsfWY-7U4OVHIiL9acMQlrkx-AQSZNNj3tce_P0SVkiEEQMEpxKmMUD8FPCcdfQ6wza6mSrTCU-j8NaBDzrTYIVXOjPHDVsUmQQuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7VsW8-p4diZhyHanCwz2WGcI4jIfG9DNqfZMVXqUy5a6hytMaN1tjJ-iqGigX0oOtLSU3p9jZafG4pbhtM_x4h2otaMNP8xzsXQ9BXjDkeofEvkCnyZ65WVSeOKVIKMNaFNWv2BA25OqpNcE4hGCjUWH3Q0-7vV7VO0C0Wb6vf1iMRzYejhkS9DuxHyOXDwjiSdWijX91c9GW6KbHzr55Jh-6gHMPKTLx1cxZd21MRXNy9tSxqZL-JDoLkERjrDO363n-2eeP1ul_MwYNSWyppl3LsMTV9KgoxxMB5PuDVfT8gJsJfm_cCnekVKhg0TYFDUQgmWStRRAGEgUwx9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXWSKeTlJNxngIABANZvjrTid4uTf84VZxjPKCmfbMvIslHTuKi-JaesB3U3GLXQOeAblhUaxYKgL5aK-uUPEFKbx3Yu2zBSQewcot1q8o-wjCYMB3AzJInDksfI0KpMOLK46muaNQBTBW9T5rLjQwQVR6Pa72kSx5obbLLvv8JTGGM8atsV-JWU9Z84HjCQfntkDTZzLhWxiq-0Hcq3F1mP6YX2jIF3KBgCYWbeWB4oCZiO3edvDsIeRjYs8CYRVjMt0LS-KMF2_w_qRUyoOg2OrufbyK9u1XgEWEzuDapTW1prUFDjt0pf-0cHCCvkGGYf2pRu_OH7vFK_iLMexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_6DNYQZ7Uz19nUWGbwwKTQL_-TOb_Eq3LfYRYbBSQTtCwIuE5i87iy5Ms5v-3Lh0lHRDZRBJBR5vdy6W2wFq4yIId6j16exnybbbmuyHDXQtj29rukDPPmh0p46MQ--rT9nz_tqeRvnZpD5Z-54AaAaYCiQLXxm9By_iu2jRqApiYLihCmPogwZMUfa-3bAHtqXMFKVlhSciigqssjIw_8dcHWHVEg-HQNV6RXrilWnqKNYMyoJ2AGXGraXC1CBPK6Olsc6pbgKsIA1vMOOLJew386c3YEkk9Z2mTJxRK6wx7FWLdArNtKYqp9FcGjcg0HhsFQVF2y2wVMWsZLezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7vown39AZh0KOU5qQs4o-y8gjzZDHfQ6gaPmSL-flvBmjRSChdE6KNCnNTwjOJqP5rMnXBkiWWdfQbjVRG0cQXVjJSeA9lwuHG53zUhDsyFDoUF4xjOJhlU6HzVL11qvMoNP7xa4HzEilROCtaQlGHqP8fXwuGH2cROAjuLqF5rA9liXMmvjG7z5up5-tD65m96CrO3VIqZV3rGF6lhYOr_Ghut7b0N-vwys8gtcn5mMz3y98cHsd1kujjFt4J-bIEIT-nowJS8do3cRHBdCDLKrPbPaT6woHLcvieLJ7ytgg2OBKnbZ0VSFmM71QM04KxxrfXzg5bXvWnj2zJnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNAeNiXYykgitsXp6NEM8F_hXXEGaKkcg90BjLsUYJ50ovRIGCMO2Y7L__aoM3Sx3fz4D8bzWC7xqq0rfUv-PmRgW9_jzbWIPD924j7wzU4oi5AtLMkHvVvreM87JNtCk2fKbJTZh0JcgXAHQ_u27xbzXSp46lRmrB-cVeakIGHuRa7pCTUCzhGf6cr_YQg8cL5nkA73TNwwZY06VBt0jOPB_zcuxfcyOsFMxvTNgBjnUoQmW7JCNc3biN8eWeeNAx4cI1VRVIp0ISjr_XAC0a54C8UiKsCrBoBJv-tHY_LJ3dGErzuA8Iv9TbQdGxTIYtszcOE_xKrgQP1eVPw--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6xmT8PjYvintqE381mdog_0bmrDnZU7AsZWuxigZX5TwvwFo5YJz10WFgf6V5SQdWwq7AFXiB6o6pU-U0PCD5dD46nuAkhWDlbdDtw4RHBEkhvJAjjkO1sbBl52gmSHYKX-iPXsY7m2Nn9zpmHzsxgyaPwdvrwydoRLwRvM1mEooy0QboceCj3W-y6cvefJgTOTtgUvqMGrdWVLzG-V1z0MBmBhUiDnf1a3rmV0FwsKQLqzZK3lZ7MF9Fey-igSGUy9rynzq0wgWwYlcWYbTEIRAauoN4VU7YKHdUqOUC9_FS9nXrHR24Lpse81lLtMGMaUn98sM-aAYHTlROVIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEW4PNNg-k68MGsvjUED_zXb4bWMFnSZ-TqaGeVJLb4N9fm5S48WUPhO_aFh51POM_li6k6SoxE4VS8uqY5erDg08xM-3HZkddf_PI2FZ0EjSSmnuxdVwCwqezcHynHSkmf6FsajTaYKj6rdu8m62YNOW4JWmqxXCZ16TyT6YGc_jG4n2nm4aBUYdo_zfgVoGdSQ2YFYBuvhnFC_Rpzfc7FuTVyz81XszlL0tIgBZgGbnWfGLj2uUxB1ctTWRZacqwtfJ02xW4eelNeqGCGsPZvvX5XIjbJoeJCxUcTFGvjS9pc_IinA-sLSI_rPPR9-dgPeZjqXV9m8gdc_RBrZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=jA74GCYSsrUbI7fAyNrtgjtjUhjBGSpxXTxejqHDyniD3QUUev7EeJZKJe4fjWMXmeI3QwRGEBSnbydjOFE1lJ-45oGllAD7nUorFbcZ3PGVlIRdk4VTEExGVVSlyF6wNcLebDHvFw5gB2cwVff5QKJ4Qi48VZyU6dz99UJU-1WTpor95hY3evptMXDUV1lGglyl0sLHVT4f-dg_k87e5sLrptGpeIbX1Pub5WGXlX7ZWEksyyG9dI2sCxxTldJ0_3kl1L1Du9VIKKzjhLwBdrjV-VtORjBz_pTe62G_RdMWJ0pTrYbm0fXndOEGJeTk-7tc-rwhE_PytQ09V3JodA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=jA74GCYSsrUbI7fAyNrtgjtjUhjBGSpxXTxejqHDyniD3QUUev7EeJZKJe4fjWMXmeI3QwRGEBSnbydjOFE1lJ-45oGllAD7nUorFbcZ3PGVlIRdk4VTEExGVVSlyF6wNcLebDHvFw5gB2cwVff5QKJ4Qi48VZyU6dz99UJU-1WTpor95hY3evptMXDUV1lGglyl0sLHVT4f-dg_k87e5sLrptGpeIbX1Pub5WGXlX7ZWEksyyG9dI2sCxxTldJ0_3kl1L1Du9VIKKzjhLwBdrjV-VtORjBz_pTe62G_RdMWJ0pTrYbm0fXndOEGJeTk-7tc-rwhE_PytQ09V3JodA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbqDzQGg_bxRjF5Pu-bE1rr_s-ptyyRJAbvbMIwSxQ_1eIkOcRblleoaZEgxhNmxn3xAy-SDCX5i40XHFsxTG8aoHulg3ApWCYMxqtoED07wxf3zlP2uZW6887TM12mbTg-JwVd98TufqOQa9x35kIPip7h9Y3W6_t9xUZgNolK6pxkgyhDX2vl6Hyl8_nIjCQB-nTvAxnO1S1UQiJ-4LfqJhk1hSocE6qfqgCBPB-86WWNaLIKEqU4wI_xddXlRkICTj7KYmOhcddRh92D1augoVfjvuL_6rH1UH8bgMxkK4ARM6qgqQgYAxLjLqd7frflDdEvJBW4fCn1ElmxwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqHdjQKThYilH8lPBesCAuMbmoJlZ1UlxfVkzpd6DhbdrHZn3fP-MOJVAHtVfnxuBs5LBBQNowfmVRT4QXl-an-wV42vUO40igQS-e1151mgsBKP1EKVZTLo2chrK8kpoNg1rYI48WdJ26jTc7MlNF0OJsXz1F7sK27rxXEeRwIdQpY0BqE8uoTUnxznF1BJdIn_J9EXLsT8jouVUQvew-SyJl0XM5-9FKpwjUkbUWNjA8VtGFfxPMJ7u5FmvSJwMB1ithcsr2lpGbxltVTNdlViEidpljuqmy81XsImhhEu_f36clbndo36ncBR1T9XkIK_KOlz-N65UMKBoRMHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R63m17ofRiLcdCrDPu9LAL2F8cHVLu1nL9MqDeEV-mkpxSPBLqAmCUjDl2OK_CEyzpCIGSFGGWTdR2c186Y08nEsAd1Q1CAgz3TlpGCRtRQdYBEWf5--gGWdoGCCuhYplYaoSnZDHu489YgZ44LI35Fp44Bii5pcwCwSkSkKlruOVVEFiuA8KmleIFYdazICxUXnCtc2SKvZlBGp02Ul9L7Miyis--Zc9YX_UJjepPFgkqtwm8JfsJAjwFKWJc20IgQK4pxSHdPyq_CyLOf0lZGCRKoFfqpGbiiZiVnkVJrCNgRp1LQHaU1Ibgy-IJahSAoUPF5pE0ffJctmk2_HJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrbX9pfe0nxDXlOx8QGMRjDNE6_k0-nraIcreJHgi53GyJT88F1rSZ6jdeDGIdM8DNievp35R2bo8Vzt-JS4nqm7rk3XLT8rBV2Dov4du_d25YafKCv_0R5fNALKApAAS9zDUkuV4VCQ3vUfdj2V_vcmPWf0lVArecW7as_JboxrJI4NrYV65bagG4JmOCUTEviFevzMz6orHfwPa9e3z5j38c2PGEnXlvUbBJPlg-1rfUlJEOehJq55KLT7z0oPRDyxTWYBEmD4_YenlnG4nij3iww5b5t4JEiRcMW76bJybAf54VdAiHaWEy_eKpCEfP9sWU5uvFx97lQ4psYAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKn3MrJxp7qzxDLUXaPcNEgNiQ4-MPVGCbVqhq6i8AtRFWq6zIUBB2f5T71PvERIP03SKcsFGcsExYkS7FY5G121WHbQIbmcAFkXCpFptplpZChThZ7uPJ_NEL7_lxkAoEsC7EVt9BZllrmDRFTPSuGV0sPPFadfQmWWe5989bNi8DakxAiTLWkLChXODySOkicpoA5jTReJSXugjIci4Zu7XxtesTX5JABe3tJFDT_15X9olCqqALkRZqN_YxSQQTxy2yAWhvWzXCOnZ9mLSF62UGXOBq3AXnO1JI7OhOEtriVTyO5KufpjBeGgPKTJZR4lY-J4-poPgPpHsOo0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1A6-SzJfiwWBD01n38V4syWm_WlwcKXHXq4jlwulWjK9JeE1lmfFr2T1EcVrTYzPxcqhw0d-0SHaTacLu8YVpB50SrVzHiALWa5QX2-FB4HhXku5lUKlZSiCDcJH6_bmboP78raPEyj27Ujl6B9yqzK2Ir6ae016Ns_uvWvZmfQzPloOk-mPQYpv9bbgXkTgjPM3g1QNhImMyXrmUgxHyadBdyr4TKp9Xr1iAbUuc3A45WlhzKm_zz_eXGRaUW6KTCG3L-hr4hainrInxYmieqeRLO4u7YHA-NsGHPg4G8MstSHhfjqeN87B3my-YLAENUGFUHTyFAGi_2AqDYE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjBDh6Z3CO0ly_9rFvAIMA-cAJWtbx_Ot6HTd7zEz2g6iXGq9CJLHr0_M3ofCornhut3ufRwR8H7IEk9RHr1jC05XQKD97BB3R59Gup6lA4e_QCPYGZGIq68OzwxKIbhX_rUUhKpi-RZDuS6gp-XhDWfQXWuMjnjeRN4vt3nvlx_GaHhtUymWIsyiZuCkBdw88y1nvlxLHNErI5LDgL_Ankjlhupzoq70P1ygEPgmmX3X18tPMqj4pkSFSLFBobsHZz44iHP-yAWp4Ni7DjDTiNbgxjE0PqWYdD4nimYCEuuZwaLlvUaJx-HqxDM6uWlJEHVfBDtimI1srOuB-tdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0NkbspUaHPnE36GWeCSNDqezjAPs6bHTWDWoPsexYAxjnNruULpfVgSoGRUauN8xVKby88PoOTQjYPUboHfn6cuQx93n8lOKlafqTL2xMARoLIKurEmxgFhEVtDE6z5rVtX6iK_IV-oWMOOZ0M13BHUAXbcJPrMBjr7P20jmMTFPzmtq6SO7-g9I3skRLLK1J-OgyfKek0KXnXyzHHylV96WWLLR4KgUvqk9lQG02rs4jzeQr2M9fKVJuWefrctodUgOLNediogEvB0HH-iGcO2ucH3zyf01BDxxg9t7RHyVH17Kx1K2rd-nZCSWwfbMZDkrOaJKu9MBbp1S3GpAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=e-KtXUXLK0pO9jKN0iAfQWzm4hoaE1KRDoDLneHNpnzbxw44xNBhP9S2p0_vCQ6xYvCPQYRRrSmZSXdA1Q_5zBLIlQeVqtdqrn2up6gdfYdK5Twe-fnEmIWPLYk-KiSUwSjh7c4RIOOYqd8FAmM8EXHLG_904WaN3rshOIC-vDN71gm6Ye-4rXajAyltvwJ83HRIu2lxCSOcOrF1I-Dh0zskIEpnxAQ4TynHXSUP2tSdQPzZQiRX-nA-EgEGbOxwfa7Y3_X2GQYQg1UI6L1m7kuus_j0YacFHeE-0Pu4x-T8ffJc8yAb9zBVaStRUwxoZfuu7mTfLp1KPTj6yt-Czw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=e-KtXUXLK0pO9jKN0iAfQWzm4hoaE1KRDoDLneHNpnzbxw44xNBhP9S2p0_vCQ6xYvCPQYRRrSmZSXdA1Q_5zBLIlQeVqtdqrn2up6gdfYdK5Twe-fnEmIWPLYk-KiSUwSjh7c4RIOOYqd8FAmM8EXHLG_904WaN3rshOIC-vDN71gm6Ye-4rXajAyltvwJ83HRIu2lxCSOcOrF1I-Dh0zskIEpnxAQ4TynHXSUP2tSdQPzZQiRX-nA-EgEGbOxwfa7Y3_X2GQYQg1UI6L1m7kuus_j0YacFHeE-0Pu4x-T8ffJc8yAb9zBVaStRUwxoZfuu7mTfLp1KPTj6yt-Czw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_WgXQ_nASZIoQyJWiOaRCKbesDQJ1TBqMe3DXYEdM_r0AkYpoyQlDH7S-ezagA0aNuTioMomcm0KwnfJE-50Zy8SaOU1sVu3-QJ6JXY63_6o0UbDb6KaSAjyJeRC2w7stwG772iCfgZWdUheIY0oqgScm-BgmRCJDF8u3MDPHBugDRhg6UkT5T7e9hnbNhHDU8UDtkM9U8EmPs-fahYv7-qen98940BaC8liNGQhULe1N94GvwpXeIaCPcI-EWfCOPOMOdr8lnvjeTqCD6O-B_mwkZPom3G0sGwkxIzzE396vPW4S71l4NSQUYVk_9PqNSXIGs4eKiEJ0SbThAlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOx2pd-hPk80JBO6Fqq4e0X57nPsXqpAZWnilYgeeTonAT8CPXFmjN39HDASDzrxI7BpWl9hCdcltcfS3cEnxdmLPhAzR9i8iceI5w9UlnN8jszOuAIwKbUdmw56HK-vFjOST23wGdTQTfwEjWaMdTDnJWZSCbPEHUg-gqsldAz6p9JvChUY8McLG6YSIQyxuoaJIBwcqOtnS9B4oaVKVZg9ifPl_bx7932AgSv5g1rILc6-2NZMbGrnS5Sr1MjvHCA9IKnTEe1E9TWbyXzSYatL0YJLA-I3bflwN33K6nvrCbfnwtBSBLRTjUog6mP9IsUp5r2uIBCmHYm2v18pcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDeemfC0JGEKUU0TNVgnfh7wHtY5HrxjOy95CjfmWsVlu1OEF0pMpjqjozc8DvPb9XFrLOXrmRiyu6sQWkLoQG8P18oc9zphyVU7pbGtWu8Lm5nbr8pdG1-x0e6zeJkwaUfL6tZCflHtwINhAoT_abDrB18syS7Zbmdgzuq_DxgLkmI8o_MS1oRa6w2dX_i_evF2oD9olpL-AN2zaMgT9fqiWsPoWq2pDXVWBqSXVY_QsWq1UhMGgU1O1zrCs3VXhDVb-5FVQQB7R-mPBdRQUs2ibD7TGX03qrRD_7ta1qi4yUYEb0kyQVLEL2-hbc_0KKQs2qOkqzVGzjLv6EhGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYrPjcsczhvbafccbz5ycKBteoH93gYzeYj9Xp6YtxgnDv-Tt2LzOnrGuuLnW0HnQASxd9E-JBVcZbqaxN4h3bpXpUrz_Z1vqLBfeW34pdRHOYqKWYNOpTlu2LRO6fgc7j0Qp0qwRktg3Ic-wLcWr54QAEeudxV0Ix7z3POB_GYcMFGXAZPipGfGKFkIRjcT84kLy6sfjIRTV6Lmxe010ukHgKFTcIGspYtFzMws2Y8LvdRJQ-rIMA2Pi3QqTN3stM1cO6EL26WXGCpOwPJiL2zVdfL-1qvNhl_r5sm4E12I59DR9Jl8FzNddf7S9RuwBy1SKqh9Zd7LZjEA1n0PJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=dtJTyi8w0bZCJa6Hx_jh777tiTjMubCnHBOgYDF7b_hjZEtDFaTkDqz8n_KRH1lZQXYb8VTm9uBMQjOeySRRTnSiQPumOcHeyrodaJmBci6B9uPbJVTvRy_GWoVr1mV6GK1VdOZjAaSbpuXBNClQe2DBW7NQ3dpzw_B5_N23I1Xr6sZC7dA4AIww7W1aQZeNOzgKeD8SIxTnUuR8Dt9rAnjaKN8SAk1AQlnMv08QKcym81uMggEsta7b8cJpfpznGGiigYk2kv2FN3xqN6mhbrTexdweJr76LvCgu-sbkTDqdyBBgeF9OvYuQ9PGiEodfIwJR3phrbnTg07H6a4dpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=dtJTyi8w0bZCJa6Hx_jh777tiTjMubCnHBOgYDF7b_hjZEtDFaTkDqz8n_KRH1lZQXYb8VTm9uBMQjOeySRRTnSiQPumOcHeyrodaJmBci6B9uPbJVTvRy_GWoVr1mV6GK1VdOZjAaSbpuXBNClQe2DBW7NQ3dpzw_B5_N23I1Xr6sZC7dA4AIww7W1aQZeNOzgKeD8SIxTnUuR8Dt9rAnjaKN8SAk1AQlnMv08QKcym81uMggEsta7b8cJpfpznGGiigYk2kv2FN3xqN6mhbrTexdweJr76LvCgu-sbkTDqdyBBgeF9OvYuQ9PGiEodfIwJR3phrbnTg07H6a4dpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjUJEeybiSIT3kXCb0Ov1SM7M54ZI5EgQijfjE-2-AUk6v2gojk2uBpKugUFnUmQQrpEod8P9SMl7czqC-V_zVd2yuin4MevzGgspsfE7Fn6K1xxxbPQgdD2ug_ZjnE5R0OKhew6Ua5aWgWA1Ie72I6XGcCZU3rRAwVuSxWxsDpSZtTs6i09S9DpX6hpjgtpDzgOjkOe4JiNJXG42vYTZhpesDwzX_E99eB49czuzhS0ECHVXkL1YMN4lhnO9hHdMnvRvBAd0jiYyoYj3_gz7ufxqWKaYEL8J1PUePi8NvC-Pxh65z_eQBkEQBC_yIoPq_peO8MzeE9pphvhm24-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F08bQ6Fxiz97s2xLk0jExi5JMxACDxYx4fy5hA7LStXS2DmIhRvQfnt0_rCFI3jQ3b8VQR-SzYunec77zlt3MgTEGYSx193hrI5FQ1-gma3tXOocanbly6CbapuVmI7FcHAoIkE5We-MiPwnKFJuZMsB1nj4Nm3f2cic6BAv0Qv7-6s1Ez90wzTisFFvY6MLacuVU6q46NO9n83ldyvYSLIb8ONsOOC7-UMOXPdN0AAZsCPrQRIqtikoi1fb-M0PbqqPFgskgwUWJBstg_fWqChgZVxn44iDp091SJP7wjo7qwYOSBwEOXyJWD0s9YSXJn6clyVavcNSCL-vOU0wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frsmuqyHQo7kQ3l_e9-ygSrF4ihY68ENYHRzdHJOq6msFOKhN-KeISQ2ZbzRvBg0zrxCOjYlDuaBKyDjjAqfakETkRkK94jEP_0gYb_TtRaU_vfPub3QRr7GK5Gc4a3i7BFgHtIxja0oHzrLFSqC2sV8Hl6v5p9SGdiUIUpKhJk30l7dzl3JP4OyTFOHcDK_Jh6yhUfldGhiWxjrdgVkC_utuJ2zlGF29uenFBSo1OVSvgN3qGsTy3vf0g2-KuxVS_JQQbDQFDqMbbvocdthstW99PJR34pNWTQXzehDMDraqZS6O92Tk90HepKGguDuSM4nQSutLK7iLGr4rGM4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdAUdyUo22_wiekWGbpMv6DJAOnbFn83IcMCGXen8yiQyolvV3ZhCfOSYevS7o-D7ONU7yHw8kNiGHZGskp2IOA6gJsFF1jm5Thr45kRzHAoleij4yIclfqrdw5jr1YdBbBGAdvxl0l5gsiB-_TnmrApAOnbvDgHx1vKzZa0JbKyNFnCdBBncLd39f0-GM1levfMTP8fwdsK2YgeyKC51mTyozWN9MVDZwfTNJnvsdpm_oonm3NyItHuUd5Ig0bABto40trLAyAaLh9M5XijDTy_zxKEjq6BRLy1T4iZE9Knfv6cf4qYImhLMb4J5Ja5PKP-ap0RnLN-IKZ18kdt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=fxXIXHGOi8fvAAJfXbB_aCJDx5_yr78CCT4jdPjScner36xAkeTL-NXVrWEAcwlqr4AihEAIXl6cOUjwNiHN0MEeAXq0NuiYFP4it3Supk6BP40OcdkfX3dAwSK9JCv2hRLLKAmAyY1fz9WhHHHZ1gvoLOagrs1fh6v8YJX49OrgJp-rSfgYr31-Ntv3b4TYO-RMLymfGxTF7GcXdWrGHYl3g5dv4RMqkfNhl4bqb_hSgEoOfABpVbDgPW0vSoqJvc0rUJPmpaw7KAENs22IdlaiAo1zhg5GczK7ZilOgeqkP7zOb_Krf-GLyGTqas-8OxWRY3Xjz485ZoRbjTHvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=fxXIXHGOi8fvAAJfXbB_aCJDx5_yr78CCT4jdPjScner36xAkeTL-NXVrWEAcwlqr4AihEAIXl6cOUjwNiHN0MEeAXq0NuiYFP4it3Supk6BP40OcdkfX3dAwSK9JCv2hRLLKAmAyY1fz9WhHHHZ1gvoLOagrs1fh6v8YJX49OrgJp-rSfgYr31-Ntv3b4TYO-RMLymfGxTF7GcXdWrGHYl3g5dv4RMqkfNhl4bqb_hSgEoOfABpVbDgPW0vSoqJvc0rUJPmpaw7KAENs22IdlaiAo1zhg5GczK7ZilOgeqkP7zOb_Krf-GLyGTqas-8OxWRY3Xjz485ZoRbjTHvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=ihsK0WWqdPvgyShnLisbZursyEQcR--IpBEDaM0Z4uI6N2NQF3Xq6dyRurKQ4Fq99MCt0BKbYzrKbkZc_wkxX1M0NVbV8e2YfJM_D0VtgqNZjFUF1jpIe_OdCE9vWAtMjHJjHHSv6ui0MFRWjQzbhG9ehrZh_KhFkduzrMpu32IidQ83D9EaBirlJ2KeFlCfaaksjmF1yBwm7xBPynGcIjCc6dwoRCz9vEfYa7kZXIA7jJnkrquUZ3Y51GpxCN4XWgC-DaQl86fhEoIrwgvCzOWsG7f7Kq2HDcXUZlQr9quD_QqGjmlC5TfId2PX2eLFDs6kWobAKTgq8_JbOjXeqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=ihsK0WWqdPvgyShnLisbZursyEQcR--IpBEDaM0Z4uI6N2NQF3Xq6dyRurKQ4Fq99MCt0BKbYzrKbkZc_wkxX1M0NVbV8e2YfJM_D0VtgqNZjFUF1jpIe_OdCE9vWAtMjHJjHHSv6ui0MFRWjQzbhG9ehrZh_KhFkduzrMpu32IidQ83D9EaBirlJ2KeFlCfaaksjmF1yBwm7xBPynGcIjCc6dwoRCz9vEfYa7kZXIA7jJnkrquUZ3Y51GpxCN4XWgC-DaQl86fhEoIrwgvCzOWsG7f7Kq2HDcXUZlQr9quD_QqGjmlC5TfId2PX2eLFDs6kWobAKTgq8_JbOjXeqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJSt-uKBv8WrQU9HL2INoWe6jY99jSewfGFzV2VgOOuqZ3KVHR_Hhe6rUAMYfNV_fwZSEGSsPQkhVD1KdNXF_KfR1_KGafVwqdF12eWyh2X3lJYtxVTf9AW4ITQNoOuzhhDVYpeLrqZVEze4Xjz6DruAXePKmd8pud6UzHP2nIF0RwMxRwKcfpt2xPV6uyGCcY7poZ2YfGZHHJ6kDTCKajC-nWOzoxP4yYIpaAv5dEcp2f5SyaL3pgjFYY-_F6vT29wCktQSbkQlFz50u-ITltL6SIsu2h-rv4_0G_cf_E6Z9TcpseL5x0WW-HWlBrCTmjf6mFjcKqjWRT00BtOkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq2RwvB7TdfoKYBUjcBYx2rVdVeDnphibaeaTx9f3j01lLSiATEdjVMJ60ncNuDzJH7knuuWsH8qwEseL29XZ8BU8imszoEqhuz_hcqNFtbuHLNygp5aAp-DxnoxdqWXqys-wmF8_f-bt2QcexsyL-0nroU9us0-pbqLC5ixcfSa13cUAovyTICZywdKSgBCeJWjQdDeVcpzUPHljfu1Cxpmo4mWjyqr7w9oTP5ot2ik91iw96kdfnhbWKq1hGkaH9Q7f40OGNIaeV49bH0hNP2lfbu7Pr4QaVd3168Ns2Ccxh6velDIa4ZeQbk7YDkf2fLsNZWW25JTLrrFnftteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=HmgncS4QA_N8EzZ3-5Bzb3y0GM681noGinIzsFSiswn2rKMsZhxR8ZqmQGL2lYi3svr3fgUwW4Gv2s5n8bmurg5r7QzontV3AqzQImhyem40C4ezJjLCAsH6ax1kO_HQAH2mMlTfumVq8Af8h_0jdx4c7DhBzd5OL32vhw0PORwuNANL2KVEZS92nGQob1Lb8oH7FKOFRftidV3cCsWmcN0bBenzCswh5rdC_jNcpoAE2SezOJWRutGvGVwuOOVIGK5o5mYJKcJ62Mn1rpk3-R4-ugJx12B-c3yZZFrzRg4CJVhroIsMqwS-07BNIaIKKa4W4wlPj75LkWdO5mksfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=HmgncS4QA_N8EzZ3-5Bzb3y0GM681noGinIzsFSiswn2rKMsZhxR8ZqmQGL2lYi3svr3fgUwW4Gv2s5n8bmurg5r7QzontV3AqzQImhyem40C4ezJjLCAsH6ax1kO_HQAH2mMlTfumVq8Af8h_0jdx4c7DhBzd5OL32vhw0PORwuNANL2KVEZS92nGQob1Lb8oH7FKOFRftidV3cCsWmcN0bBenzCswh5rdC_jNcpoAE2SezOJWRutGvGVwuOOVIGK5o5mYJKcJ62Mn1rpk3-R4-ugJx12B-c3yZZFrzRg4CJVhroIsMqwS-07BNIaIKKa4W4wlPj75LkWdO5mksfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=f9M7XjCyYLuhPsVSFOoBrfKjGSjw_uFwv2xC26R14FiHSlF_nOd1dS64Xxo3TLcHfBQAqQq22rq1Zdm9E3ZVcvYkHs5DZNOjQJkkr-mVhxCuIfbf5YH8qP6f6IX5VDgKG22K1wwNZHBUyuWd-yRohb1i4ABReEZhxV6vjn_P2mkLW3G-pLRLFFEgUKFqIDeit2yWFexL-o4TXlIPueKGaQs3AwjbUx4Ozi9ffedzwei-_y8Er9WlnxSR2D4ZypYe9LRPb1UCYFXRICd_Qsx0oiwNCHqS5dqIRB-9a_H_rfx0wSvvpi1ArfP5Y5HHU-x2wYmPMEoj13Qq-2EHB63_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=f9M7XjCyYLuhPsVSFOoBrfKjGSjw_uFwv2xC26R14FiHSlF_nOd1dS64Xxo3TLcHfBQAqQq22rq1Zdm9E3ZVcvYkHs5DZNOjQJkkr-mVhxCuIfbf5YH8qP6f6IX5VDgKG22K1wwNZHBUyuWd-yRohb1i4ABReEZhxV6vjn_P2mkLW3G-pLRLFFEgUKFqIDeit2yWFexL-o4TXlIPueKGaQs3AwjbUx4Ozi9ffedzwei-_y8Er9WlnxSR2D4ZypYe9LRPb1UCYFXRICd_Qsx0oiwNCHqS5dqIRB-9a_H_rfx0wSvvpi1ArfP5Y5HHU-x2wYmPMEoj13Qq-2EHB63_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY9ivKJZ9MiWo4blK4ea99spAz7lG1khw-Gibf_-Fkxks1WJSmdmNhQFnL5Bz3ofPq5xBpCn60blCygv9DzSZHQrBEkD8NYiaMr4xuzEjlkESpjFJHJaOn9gqsez8IKI0bgtN-CbXE8fSnuXtoYbK9AqhlyKhRLdjWkVar7bBkac2rumXDi7__DH96kFiXdUReAecOZ-OGm8CxKcn-4Xe8I94fcA7O0LQMouQqHi_Z394SdB-Oft6HiEEDKpFXXZaKwQkhY7LNayt4Xe4uUi13xDbYWIDR663VEbV_w-MFzphhUdhD-cKkQCKYhvoHuhs-PzS6nrr8yaLAAnsmga3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYneBvdiEz8fI9igQ6k3KDfxlZTdbw0oo41HFvcbT6eZIt0BlVk6lsYu2V16TatFq93X8VtQu-uU92GpPOodN2b9ggv89yono3FojytbSAZDNP82wzea2QnfSr_oJ272oE3AMlQ1uXSBVXi9Y07Yr1-O7OSILbIyzKAXtBdiFOZS4RS3-MFyo1gC4TQI-nf_UUL_DX9yXHjWYjhPcs4a2jl9dMeKAsyVrj8KEi56EkO7oWcgSwbhDDsU_N2mUI9kQGw78NgXcgoJs54X1iSAKcNsyYJQqI6xXSdAPLqSBY8Mtyh69PDt0SwhpeS0h0F07Dddg36htXb6eT7uUYAK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M18xQvdKQOMnOPAhvOkm4iSnj7M9NMSKoW7O8LNCer6hfY6UgM1C_X0kXor4pva4g7itgbFRgy4N3jKbbNs64vIzZo7WNBjisqOVaIqswcERArbltnhfgju1X21YzXGiwydfkT7gTONlYfT7RTddXmVjxawtqbM1r2gBYicUvAKgfs5ROMMJ6zC_-BCA9ERGVe7UtcXSkVT2YuCd6bsy5hQSr_XmTJpbdH1NhbJn1oAI24Ow9HkNGFo3ypgSjKbiGgA6JnzGKzu8cQ_Nq4XjDrm6G8ork4tDGPS0j5sNHUpLkN21jzmdkCHte0KJAFJuo-T_7XEN2QGsCWk2vmj3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=CXEn113vyIFox8E9NsyXpqqbuTp7sPO3f-nyfETxigsgFOfmPE0m9Taciz9Xalh6wuaYsPu0j9O7t9QyZlNvWoZ2sSrBmWv7DkXp76sYt-7k9BQzbjxC5B4OgR1sIFF_5Uci_9Lq2U-CzPu0FS2039q5y8yyI_RAsIyDSND0o9giKzh8ZYyutg56_6-G2L8SZOV82KRktxOaxjFlCE71arx0uQpmUVhggIEZwVkmKsy3hE-YEsh_-fqP7xKV1c-wRkZ6oMF6004RkZAnthj-GtM9hN9glBZx8-QKz5ZjHwvaELjUo8DuJN8fdu-WAUekJ9JadQ42vs6YpSIYBC8vjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=CXEn113vyIFox8E9NsyXpqqbuTp7sPO3f-nyfETxigsgFOfmPE0m9Taciz9Xalh6wuaYsPu0j9O7t9QyZlNvWoZ2sSrBmWv7DkXp76sYt-7k9BQzbjxC5B4OgR1sIFF_5Uci_9Lq2U-CzPu0FS2039q5y8yyI_RAsIyDSND0o9giKzh8ZYyutg56_6-G2L8SZOV82KRktxOaxjFlCE71arx0uQpmUVhggIEZwVkmKsy3hE-YEsh_-fqP7xKV1c-wRkZ6oMF6004RkZAnthj-GtM9hN9glBZx8-QKz5ZjHwvaELjUo8DuJN8fdu-WAUekJ9JadQ42vs6YpSIYBC8vjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=FtZINbZL_Btum4L8PEC576Hqb0VHdgsXFvVShrGqcKYx3GzikpUhgc9hT9DhUvMNIjkuhA6wYUZNFF4kDW1OGeHJSmWW8-gFJgG8RKkQu5wwL5uyzDlv-jC70q6sX_WBRQfkbcc-puSdq45wfy1rtZ-H63ih4FQ-cFU2wEY1ZUGkkB5e0ZnB1JJWpJpdS-XeZz5HEPH0XOdfKAzU8iEn3qAx60kc23-qluA9tFJPo83sozRNQ7AOA7KgET0uflQqQU2FUUPBbe014T6yFi95OFCSporSdL8l-z8oKj6n8qDv_cCNhHrXDjLuPaefY3fkFHFPYtxJ9bMS_6OxfUAMcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=FtZINbZL_Btum4L8PEC576Hqb0VHdgsXFvVShrGqcKYx3GzikpUhgc9hT9DhUvMNIjkuhA6wYUZNFF4kDW1OGeHJSmWW8-gFJgG8RKkQu5wwL5uyzDlv-jC70q6sX_WBRQfkbcc-puSdq45wfy1rtZ-H63ih4FQ-cFU2wEY1ZUGkkB5e0ZnB1JJWpJpdS-XeZz5HEPH0XOdfKAzU8iEn3qAx60kc23-qluA9tFJPo83sozRNQ7AOA7KgET0uflQqQU2FUUPBbe014T6yFi95OFCSporSdL8l-z8oKj6n8qDv_cCNhHrXDjLuPaefY3fkFHFPYtxJ9bMS_6OxfUAMcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8zpScFmKBD7aqtalyAPgt4Bje-3JzkYXPxbrNXJJBa3mtqk-AgaX3ORQo4b0-qubLzZurdzNSxqYU8apjTRdCXLjaZGqn-PTYJIvyUU3xbDXZ78WPPiU6SgUMG9Uva3UtC4sNnTgMzEJZpwNble5IjVWOW5FYCt4q2VU--wUh_hoF2NMfyuUb0Tbcq79amnN5vXZRuuIID6gvB0AvGZoSz0hw0YZWR79iEG3GDz17ZJaOy8yS-oRfjXN8AL3Rf_dptESsFx47tIC9zteM64aXUwASBNtaFUNRfvyMAyUeRF693L9tCRW4VeSR3KgYs6n2Vho1ygpXf9_hSnSPekiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTCTIcyd3JuhJvtsMAv7i8TC1-RjJS5R2csGuCO0LvrDhQ7vpgzLs6vbsSvArBdS033Teo03hdCzS2wqMGZPx_HZc55yFllZQzQjQhx03hNAY_u4KIJ8ijO1r_juUhAOayrT2jHfuyBvhu5e4ZBlbF5g8ryueoehhFbpoQcHKRREpkNKYtqYco4HLHzZuGnm98eD8uzoq_-Hxr2nA7tU1AfiVvZ7ZeG6mlhbfczOTX2cfqWyF8oEvNlTHoqM4q5eEl89OS6Tc6s5IQkb07KXHuXq6mTuMMPho1uas9dVwiwpxYdZDwi7ouxlWeFXSnQjaVxoXVpyw-yW4tff1y1Nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLoF5zCZdoQYhNBktgyllicW7wDPjwcT06Yu6rWhfEMU3R0yjkRpwUF2qPOGHD4RziX-C46tfmZe7oPSFQAm2JPA9hKbyVKGGtG9YAY4AYl7qaZKm9frHEt-OXB0ufhaXkgv1kvhnEyCiknMaO7rv8N2-dEmPXAsY1pZHe3pbxg2DHPe2pGz2R2xd9Flifxltylba5TFcf5pEMV7BLf6Bza7XzRSliiUBmDGLggt9oWGo44U_1Cbooh5ERWKigb2zr4nE52Pz3ocgeUZZo_cRFJYD2TW5SBipgMhuz77BslroD5Ru4vJrsioPyZxI5wpiaFURTv5QSe-IUEST3plvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upFP_qKC-HlsOaBmt9wp4QiMi65Cd44-LcCrro8yFw83GVkTAcKuFkmqojKuF8xBtfRHsJugEnIWf8RUQhWmspTuLxMN6VWUsKeacrD6i7ElptgPzAh13RA_GouwhiqP5ei9zHCyhYWEwh_jzypplwPD3WUA_5WRvt1oFCqrSPkVgO8gzqcZBz6CiIRYJHs3YX4PsHwhjzIz3CG4F1pbXmUUzCIy33NzZP0OhgVcfEpgpgBmqY3AsXJLI_BrD5n6hvQUPrxeG487LWODWDHtpHGH50CQyBVt3d45en8mx_UXEnC3rifVRfffPpepRSVn_QZKWImA1l7KWKk2wVN-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwzlAHNkmYUKY-GovUgCa_J5y4sw6FLEuV7WfVqAufux2iia0zIcpnOCMSJVrn_hJieQV6KhY5RzsmoLinGEb1VxpQalShB_VMVV8h1lqD1DRPe4jLEfVoJm8A3RTOprHpnd0cJmFM1WgyPtA4RcXgoCeDbVSTEa-Pjnk1KyYTRh1xHTBjr79GEuTZApqbmf9fIPucw4o0VQK7rcoenwR_pX8_uj-ZBDMWbGEqgZX2YllGZ4j0AvjazPfLm1sCU126EpdSHcNaTYtjF_Rx-JcPEsRtmjpXpUrCep4li1eB0Y3UACYnXrkIBzCiDEjMbnzd5mUD5g6LoVfWteVHD1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swr4OusqhGRzCkKYZdxKbcWCF5ND3WwnYU8u0YWDyqu-cem83oSgdX3YAqcPHuHYUEiNs3a3JcS1BPS33RohQ2Vsjrtlo9hw3lwrPytR52-srXJmKJdR731BtmOjFNnS3QOn8ZE5WE0fzeN3RAP_0ShlbSkdHmQSXfwETxTUpon3joFNJ1F6sy450iScGKubx3N4RKh4uj73_4EPXd6nzvMO5-zB6ECTVVPbRhRIwdXzC73Y8mPMLVmtFPhDdYlrIQhOyoH427pBWDHVUre05GgOK3y5CeN-0Ul2a1TKx8hRLXdbSn9yH6f4Rum_6qoJePj4wqPgkLvfLkfbjiGgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-Gj7VpAeXKbKTCpw-VnoAeQXZnY4Braju94qHT4DR_FFbcRB_K8dsfqqe1RCN3e2DfXdzf_I0mgAfq2yS4u602IB2wMGWJq4IYWwhptvDZlScY1CwmjM_780DL51b9tK0IWAl2u3g3aLKb3o2Zx81JooeJ0hlbpI_X-X7PSwyhAaHSs1mPqk6Dtxoy6qqrORgsP3Vv1HAmpVvzkxf9esTr3c4E8VUzI-Gadlx3cc_jQInJ3hCOPnS2dP8HMdONAgOm2lF2yONyT48q-RYqyn3rvoAQbTQXr-qDWxupdTW04JXaAcbeHN5tY7k8C4lc4Db8iOJYLb2dhfmavOLlA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM4Rpqh27L-Bg3pSAXUoxvuAkW4c4bxYBxJ_TPQyoHoTahtV12kTHT7V8QebzdRvmZ1uqaghn8ltJlNHp2x4_ijTca1xY4F1n7Stfbvj0tNSuy1JWMN08jYS0JsDq6zZvDC1x1AWgNKQOWIZ8kt3QmoLSdci9nxkcKSDmT7DDxE0RisSbGAz9BZfVF0eLKXRQeY02rTfvU3U5Tag6gMThmoG3t1WmwseOf-MqyPwKvIEYSDiLfm-oPwfO58si_grrxj7qNl-BGr2PQ5dPKSxbgXmd6iGzfZsCt8lEnGHu1xP3i8BQolU5MsK9kQCwDyC9smMDRdosYgo7FskUFIfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=QxCXgXII28wOiXHHTC3ZmiDQH_I3wTbUVE6k57043DU1P29XLor3Vpd52GzYa5NdSeKeGSwqHbxpu9N6MUxHvdNfK5VFYZ0mP1cNxIuOK0Wp1MdLUw3wbHHj7A3PwnWtR1yzJriy6J64J9FUGGTcN5SXZmjgkCpy_sg-0UqiTH-Dp5C0gh-Es6SH2mxYw5o0plNnXPyuqi-A2G53VF00xBrXV1uECIbLp8aLZw_p25uU2wUyU2Rozly6obqKtbkZW4EHivcNbfQqi6Xs_pzISkzfa5IrHF7bsb6g2aMh4etQCPZF6ODHwKA38maufNxURfQTM6mIrcyG3s5cBQoq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=QxCXgXII28wOiXHHTC3ZmiDQH_I3wTbUVE6k57043DU1P29XLor3Vpd52GzYa5NdSeKeGSwqHbxpu9N6MUxHvdNfK5VFYZ0mP1cNxIuOK0Wp1MdLUw3wbHHj7A3PwnWtR1yzJriy6J64J9FUGGTcN5SXZmjgkCpy_sg-0UqiTH-Dp5C0gh-Es6SH2mxYw5o0plNnXPyuqi-A2G53VF00xBrXV1uECIbLp8aLZw_p25uU2wUyU2Rozly6obqKtbkZW4EHivcNbfQqi6Xs_pzISkzfa5IrHF7bsb6g2aMh4etQCPZF6ODHwKA38maufNxURfQTM6mIrcyG3s5cBQoq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=Gjtkwp5D3PMeU9xRmi8V5EuA7Sw2iPi0M3xeBIrvDGjSWM6NEz7mPCViQI3aEf5BoMfq2ADF3LMboJelW7zFx207kZjuDPgVxqyvq3HWirbPCvn6WkA0dk_eXGmqPz928z8o6uLls6Y4plpJoCXh8bsen57mj-wy-_aTIl91SII6CLSeoD3yc_urTRc3z-M6DsozQxiHbwRhje0aG5JxjvxFZD8zACW8KHX2nFh0IqUgmhYdAUzbfpByqeZvqoleSu7aaz1lZHkkMoRniWdXf39iFTVaon6NYPuQpiWVuXK4hQXaf5ZPndUcPnx-3SYJL1nlh-cOOV1mboDngBslsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=Gjtkwp5D3PMeU9xRmi8V5EuA7Sw2iPi0M3xeBIrvDGjSWM6NEz7mPCViQI3aEf5BoMfq2ADF3LMboJelW7zFx207kZjuDPgVxqyvq3HWirbPCvn6WkA0dk_eXGmqPz928z8o6uLls6Y4plpJoCXh8bsen57mj-wy-_aTIl91SII6CLSeoD3yc_urTRc3z-M6DsozQxiHbwRhje0aG5JxjvxFZD8zACW8KHX2nFh0IqUgmhYdAUzbfpByqeZvqoleSu7aaz1lZHkkMoRniWdXf39iFTVaon6NYPuQpiWVuXK4hQXaf5ZPndUcPnx-3SYJL1nlh-cOOV1mboDngBslsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5LyYOzaE8Dj6qn3eyhJfym2bgksykSjMpnH1iZCTKPEPZFMeXyjNqHDf_MCH9Akh-Nk2obc21vCQfUoKu07H3ct0OfcmRSHbygpfDnl5LMi7r5WyyTpzJDyMWlRS6Q8dXnBdKGhNqrdJUO-hyEr5qgfV9OyPPZzlli9_Nb03UJmyKurpqSaIVAZdCRCfA0KGSQyWA4LxjmQXVAz6awsIlAecbpbl0y8EOXtwy7xeDcKLTxOuxPcJeXDGs9tt6Wy21VL7fDEJWW82VIjSONa-KMzAhUUIt5N9WqEVrRa09xzLWACsaRk3ufOqmiGkEkS8m9WPaAu8_8Vb9Mu4A-eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg2M6IiQ_AQ_HLb4OtMU4Io0xrPfKCR3wRnxRlhc6BkNaUKWKZXqWEWTDcLrlX2wKttztvs3tgMNGKbp0uKVwTqEs1Aa9OtDS6vVvXVHWLKxmK2F1GWeEDWedLHPl7LisX8oVD-Dfu9w0WXAnsys51Shtyy5J7uqlahAoD3EQFdtYJ2iXPHlO7QPE7C5QY3OMxPkbC9a74aOAGQIDIhcHXQqj6Ej79DtA4NpTZr-1Vo7NcyDSPw-5KhLOusNjPxznp54y-8uTNKMsKRPkn77nCpGka7p9ffTTxrUjYGdzpKsZMcx-MfbLVjny-eM7xxli7EnsHqaIiXIkZmM-tW-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=tJLLt7TZG687VzRBtE4ZUPFCHeVB9cYAEbL5DRjk_n5txmdOZv-G8af7DfPJ9Y05Ihc3jIjC-626gDFdrvlqqh6YjkLteSYzg-4cvaKlqkaGJxw6ARX9Rgs23at-NTAZkU-yZJ9O_mQ0Xm6odixDZKD8PuCzVpV8UG0NUEAzWacspfiZTdGhY0AkEvbuRMpdgJnW-PTEnZZ2VZTHiESG4sip0vJ6oc0jOdsdzYGtSrNIzIBe8tm751H8X0ke5teycn1s280GuOjyNWscYBBQszMXwBSFuCWvcto5iYKEUEkvI_k1mooYbHGbSsgsNRJcKxYyD0qPcYZ5nZx1s45fxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=tJLLt7TZG687VzRBtE4ZUPFCHeVB9cYAEbL5DRjk_n5txmdOZv-G8af7DfPJ9Y05Ihc3jIjC-626gDFdrvlqqh6YjkLteSYzg-4cvaKlqkaGJxw6ARX9Rgs23at-NTAZkU-yZJ9O_mQ0Xm6odixDZKD8PuCzVpV8UG0NUEAzWacspfiZTdGhY0AkEvbuRMpdgJnW-PTEnZZ2VZTHiESG4sip0vJ6oc0jOdsdzYGtSrNIzIBe8tm751H8X0ke5teycn1s280GuOjyNWscYBBQszMXwBSFuCWvcto5iYKEUEkvI_k1mooYbHGbSsgsNRJcKxYyD0qPcYZ5nZx1s45fxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSpDOdhLjZDTgaeNcOMWodMjHBXMAEkwXUNTxgUTM2GSkMb8QyHlh0_qsoTNeCpIvsL9LK7clrfE09qKkLuhEWv08H1ehV8ZilxYOKBogkfyFnURhqcWKxPIM_-Od4_AfzXbzFb4XHitLneM9HUti5xlQTn-5R4QbED4_49InSer6kTgTQfC-V8O-nicORqoSFvm7Jard07BlNLVUtzMNJBtxParogPFfM_kgrxvj0Qv82yNOs21Yn1NA0DViKk7XxrxejmbzhyCc4kJ-LgcPDUhVj3jcVsBDEDMzB-NpIzNiwOysFV9xsWNFk23J5umnCBc-y0FPOJmV_1D5QO5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
