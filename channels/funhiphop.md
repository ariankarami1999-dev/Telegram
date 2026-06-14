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
<img src="https://cdn4.telesco.pe/file/fiUtkfufKVOKcdNwJMsdSaiB0cUDSvUdrM8aoWmrB03xOR3HJXFTHCOQfR570KL518j_ZiB6T7GtfHZuv_3aAwgkhIFvYqgyvsFHtYBFv3fvTwUWzfaUZUrxFwXWWeSsB4AQX0lUSTzrlX-e3D8_itnokSjTa4rRvzBSMoaySVbNS7A3bwMw_VsR7PrEuKT9rCoi1A-4p3pbf40I3ws_0kKlkA4As4vZLJckj_uHus7ws09HKu1yzS8SSSwlSxg8scS6CH_sE-g7yJ4g8oynmHZzDDaQadj6_H1sfXGdRNPxEHc_5MArJP1Byojiuw-K_P6b_GF0eYzPXS1ixz61zw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: توافق ظرف دو تا سه ساعت نهایی می‌شود. حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد. به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟  @FuunHipHop |…</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/funhiphop/77874" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
توافق ظرف دو تا سه ساعت نهایی می‌شود.
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/funhiphop/77873" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسمی:
توافق نامه بین ایران و آمریکا توسط ترامپ و علی لاریجانی امضا شد!
پایان جنگ ۲۵ ساله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/77872" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqwbBf4jPsOEoWupK7Ir-AuCqi3XF0ioFHeL-ZczxcCdHUa3e1yQd9DagBAMFmrmTdB7NkaRS96uTFURBo1mJL7AkEFTHzQvPMuGdHAPeDjgd7pXQPp77fA3TDvhmcD94BwZ0ehUPvSb5IyciDVocbYXUnUnjjxy_dkTDTqd14mO82wLfqwISohCbAnNOLO_u7Ur919SoFNPzQL3H8kNgKUX3u0t1GnZ_X2TGAT45c85gWsMmKKxN88wZmmPFdwMHWRfL_V7pB3uTekCi4pnY1eABY6uutHbsaPT5wVTdVRTzN8k7dSZmZNprYvosU3cPSu9RwZnIPokf2yS-ZKwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهش گفتم 90 درصد زیبایی دنیا مال توئه
خندید شد 100 درصد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/77871" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/By3rxijtjqppdyRbH6scEC4Xi0xPntR85zNR-3OEIDPuAK66G33WeVODxTkg3hf7QU9I019vZBq3twfqrsX2t1-cSNxA5g7bDYUSuCsg2RWqPt4o5fzJpiFSW2D3ENeReIxugix_hsXHqps7aJiGUq6sNNfxK3WDQR8kF73ZvWrTYCXQRn7IiW1-3X3tubQso2VtGtzeC_yaa6EX4dZ6uX72uDSyN4qv7q1YKRgQGVU_OZ0y6kWLEIk05zA3xN665zc-OlYdcf5YK0d5YMp56HPKsmnsI3PU5QIF4vPZCGkPhWpy7uwRZw2BzNT0P5uvJ79aYboCAd-dB52cZ9ju2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S99x49IIAvOLYakXu4Jr7_ql6HPovl3XbyOVPkgDxoNj5EaXzZlgMyGjgaRh47sfkJDQO8oiN4hBJo7Qxgp0E0KHMO_70SWhDpeYNkePb0T0z1veS7WZ72eiSuJPgVkK50Ohl-adqz7aAhL-tZLWenU3oLL0NiDVHvSiHQfqH0FpI0T0iAjJBPK-jTCngleAfyOB_UMfXDv-T4V2Ch6qWJWPH4fZGv5T5S4QE4JZkOBkJN9BROIE5zpFMGUJCCpnbqHn_CYZboKt8Ax4vBy5k7Qs_8Ee3JJrpdDRgHt74Q2vD8E3pX5v52vP1tP9-7IGDZtRPyQ6RYb4oOap7SoZGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادار ترکیه تو بازی صبح امروز با استرالیا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/77869" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/77868" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioanSFgGNKnSVwPE4fbeWQz-1asZHE5s2oXCTEceb2i3D_JQ0R2XsmV3urUnRF_BFUQpcLvYxygZend0_gZiXCzVH2lIcUpyW3Z9e5GCWFs8tLwlEtsn3mswH4756UVQrvbbOrfz3rhhLlF4mgUBoWRVzfOrGNUMU041UCV_Q6QQFkZ_fNFPvOm1dBaI5vW7KtMcyIdz_9b0e25MfeAcZOIq3GI2IVJaQEZpV-M50q_vd26X9NwLiOGPOvQmV7Zl5463fSjagvRjW36JKh0qWqoDAICFNWZAtuuDgPY55_toT08Q7J_QXre0LM1KtdExcx1nvTyR9WuR4FMjFZu5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g24
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/77867" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ZHnLjLYYfGn64GqzSYuEFS8NpXADC0l_jtYa98ZacyZZZq97pyUDAtfemMh0faNU0s1k8az8xO_Zx2hQFzj6-t3zAm-dNoaZ6yqAD2iUdm7gKxxzGn7B3chGiHcTEusy7ih5cHD8RL5rcpP5efESCs4_JBLRl7FX3Z967_hb0CCfb5Xkb85U_qey-1LmysQYspiZ690BS31Vr1Xvf5IyxK1IuXTo-bDDQS0gHeHWM_O3RuI-JkNC7sziRwZ99UQ6VKIRmLF4MKHXwoEG1aAmvDiHurW_TIi87vaOEQvWsElW-5JDNLVIWlYiySuSCl8Kr-aT360_v-Sspkpf8uWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید آن را خراب نکنیم!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/77866" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V25bvotkGQ5V9fxFs24sagaOQMxZjtxG4CAwueWHsz7V_-ScaAHk7DxzaI1YDZ3tCTxueibBBSA1cdPrYtVkYqQKBRmZbA1D01VDntkb7dr_FcpNK7LHdQRsIenTzRYmdEHsRVrYR4LM32KcjaGG7PvgePs6KPRAV--anQ4zVjJzzjbqOHLmLb2RLtijYNUHmMiWVaulbWz3A3136aXmt6TUFO6inqfsqIZ4fl826EC24suEVXQ_PndpAWx7P3YQbg6MThY2UqpXmjEpukCP_T5Sd7PFslb1AA7agISczlaQQiACgpVmxzOoBa2loDUv7ZTdyJthreI3LFVBkxHiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید رضا پیشرو
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/77865" target="_blank">📅 18:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXwyrn-AUJk17LQq6YBCQq2ruKu3uZ9rnoBt8Dh9Hl5ycNkiF_F15dTh1l1m2Q1TKV5lcuiYG56NfT1Oh88PiV29o43hYLmlN26hKAPErUVt-nwxmFv4WQCu0K4OdNWmWhPiMMLU-vY8kG4Kr0L1uxG3vqCytiIYnDW_yuCHP0x2I-IeI2cR6XA3ZaXki6e-btT-mdFbTex4IwG6xTKL4_neLFioL8pG4C0RacAQi947CEhwnSASJsKQsBM1Xy-F_iFfe-TPjA5s_DUWDqym9gToGDM3vR1f6ociFjQlJJhzPZTY1QIKe2S-zyqxujWtM30b-TVat9Db74M2NH1MFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSu3vycLg3c0o8X2OVBFT34x7a7125nRgBXEcKfRB9Jtxkg_WtFshnUIuzseZ_D_TOjthO4ldOiaN_FmzQa7Rjrw3H7Qppkz9uxcXc-zw5nt3VkVNZui-R-5rNrZUCkWCYeYRNjjz1n09VOES0AeuiGN-RPkNDSn-fTd1S6oRQyGHsNRVh62hFArkbxufG9QMug4H_p9rAWv5Zd40NEtOcc5wioQPTevYBpnxpVW_Aav1AA3a4o8ao6LgJwBtNqDTNvsW7mlNyZzeqezdfrKUsFCSPPQAKkFUWE6BhFmn85_IMDe1mfgd47FmXtjXesiClqpvK0DQxw9ys7ZKJsW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muEb5WNQMEUCLdOW7Pq6uPnA2JV50wsmGQ7USqGHr8Nemr0qDxkOHFR_UR17YmYEv92UmgumbeOIkjTnxZsvZ4WNjqIbyMYRc_57ZFws_Msp3zKoE0WmTvLp1up2IWhAEZtODchzLBbxIsh7bq3AilVeDcgWUHfsh_cAaPnDQjfI9d7Tkkl_kr5ApgcSds8749mbfeUTO6D9I5zOdYpnOogjtWNsPRKUwEdZOUFAT7-n3mArim9hisbuSJXG2Mp_gPUNnzlkCS-IAcJ_dkSN6GCJnKPrOg_yojYOMBQ4wCfRtCN9U5NSQ75_-NRk5JkfIVOpWWrmoUxdCYBHbujpbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OjnTjKCPNr_ZDFlEaAzAcoHXuarndP-Uk5hU1hdJ94szFF4jSecqczRwKlQVxsYZjVC51vxpKBdiSVhzFzARV_Odpg9N9IHGzxOsLN2alDzeli_aUIc7hsgaHpIVq6IK66Poy8LqNGp0Sg-G_z6JtFGFTLnXMvOQfdR4nXtaAAsjrA3UkQ_MAztwgaLiU5Qz5I6UIOsie3UQ3N6LljjVhzPXzh4S99UDmFTVIYvaXQWp77Do5i7DaLdo1w6lzSw3AHOSuMsfJ6jRbmfN3KCGOZgeXmHhhN9y_HTw6hk_HQVf2IGG_jwWWkFp29ogJ8rPl9CF-PIjJsLEhlQOXqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZKC20AqQrs4QEOcU0HmDtJfCQLnxsT7WmBQuCRjJM68t6TAHiGnR_obi-VqtDtsRyXfrrOT_ELQxKtBBCcSOvUiEam2YOvGQjcQTBKTk6Phi3qkN047mjmq-7z0JKZkeOeUktatdvWEAMNTE-aVXVcy_wytd92SXtGI2jIF3JDApH-SjAC21TpmxkEzc_m_jyKTTmI4aJVpM4EzbcC41FBJ744J4u5AJ4FrVie_QHLt6Ka54ZqYxXIA5DIEQIDsWALYGXlPwwCA5botPPPKQnF9Xe-eM-Wkzb6J3-YTQyR79YNLeJIVFhEXKMMCPKcPp_d6NbxJ1mJA12gdO4TxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-DWhHBMynzlMn5RF2jkTu_VPlGyVFxnwsf8elUaahpUXVpna7gXfVQb74QjjxxYNLDCJ5bIgb_tHAkBNkaHN4csIX1zqf7neVVGd8aMe_BaDlHMLkU_F-QcMUggaLQqciEcD8kzoy-cHgJx5h-JvvgqXtDLTG5gMIhk4qU_AS6wU--toWeGed2IEGjRr5vAsNukZkeO-1HbkgvidEpkJZshBa_eDj0Iu2ipIkbqttVA1RwZ0rVu1ntq1L4i1nQbiFWR_t_tLdnMYZu4K67Q1TH6iGzqprDeNsCmzfTnR4-Pg2_3av2SecjKLCPKY6nuXz6z6j9UUXxoSikzzedVpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgnXO6OsGCFs5Drff9C7j1HiT4zfXWfHLs1tI68-X5oQP1fbH8Yvfe3jpM1aU9vUg8ItDAlaNsNATuUL0pCOWQMtrVPYf7j0eD3QOZWjJZ5mlmLYH6DcImcPgjkStudWBJz9JXvzT8prEDDXlGW6ZBJ6_XOIe01nZxpGnXfYeoWlZF77s8qYaZNdemhEitw17r0MNi0MRI_db7sHLsUv28GMqHn4zyBUVsFoamsAp7JAHEWWXaUWwMsoLIwmxWYWz9RiaWPvc6ZcVcOAu9w4CaQpQBScQKk03C7y2tm69QcxJFLOiSiUvNBt3OWDhadBdV4DGewD4tiRgRsAQNLkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLter0WhYTfXleVUSZOwPQ43Gw3VhjqSREWmPltkIDKlWCoWLa5ZOBEKg1M3g6yHneQpyHfW3hIHVvBCNgKS1CDobZnTjEa7j4rOoXjiMfw580wVMv6FmydtwNAXMkmHXKaPsnHMCfX8ULOz3VkTL64RKLTrEmLlZy8Dl9riQKe42vnc7xvfAUhgvm3yrxoWEewTKD9j8r5VcIZ_DQB6o8FQMle9pY6RgiLbmWBnmT0KgpuNZsily8VemWsnlf-dY3apPJutsyY4H8gq26CvsvWvDDmoiPAnq-xy-riAoAJLXScnozwray8Bm8lSQvu5M88_nFhcqtErHSEotz4hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NotR-lTGkzS0ocFcp-7VjwyQ-Q_ToVSnnruQBNN64_zbZnkPQasMy_yONBF-tQQVj1Ge52kOlnMxXDeAgffQC6E8fb3qTGkHeO8XBtgfRUDRmGl6FDV8hKx6S_Oa0MyPkiUhPq9Y5aU8HKfexJi8mbCeb-p8dOTAIVE-eq4wys5kpGyJt3HPiULJqIFNJuAm_N38m0NnKFlk-OZQP6vVYHEYE7B3T1CME1W8xfE2oX6kUWoCyMRpyBDARQjE6i3i8obtkZzoqRLVJcyvPzZIE7GMeMlT-wjVZVo8w0fJ6hNGh6146OfGOr7g5LDrmUsf4wWtAA7En5dmoeGzdsYEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJeSGPoOpGpiiyvamsfMXtoPwKm9_idHFdo9l2hreMTl6rjZZZvoJFQcRv9901ckc5TVvDtz40J8khA96fjk5DbfHnu5FxDwpOSB5Ahvr12rdTNSj4kGD07mcZ3ghJTnQHdNErnqHfnTcDuDhVBjqal4ZNQdywnvLn0A41rMjlv-MtD4b_gj6xGpQX58v-yxHXfO6dfsaffPMe_htsjsChc2y1CMp4uopdmAlEnThXBx77_D-3Ndj7ZgtUgPBnuZzSs2F5OKrw1PetDpcSltX1q6iKC62Qu6UXKLMzR9ujijKain5v7i5xtWvf4bim7jwsOkrr1dmHJxcw1lPI3oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-uxS5gaFj-IHIyZCA6PRTpliDMMFpfuRtSaR-UJt3DqD2D1TopTUWrx-mBGZz10nXE7au9Inw0ugcTMHj_x319MqwePBmwER0GLEkuIi5TdWARRRmSfIqAb6lgMWMG9knxURC3L14_mFsLP3imrwu2OM6hdtn_dumyTYizmtZRPnvnn50r-xwarELkFLwx-0LNHvSZ32O8LImjb3LVEw_tnxfFndLdh3N9aHfieCYKgFNijPahzvPOGJTL8Mbhdc0xRpmy7TzVtK1XFGqjIFzBGRKf6g7wChebP5jB-SnPTQrtf3aaGsvCFpMsbckJJxVkYLORi7HehTYzFNp9TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDWjIBE9GD4NxBI6-kIwdGQmnBZAoarMlOGTK9g4QZkGq6izVHyZrvZ4T17IlcaHzhp3nMVhSU4MfhkgA0SP-CWSSTDpAquo83zKnCg0SOtiEPj6QHGLHT250DlmsN74zpnqP8kt2LtvpkvOdtyFfKfohzv62cxmhkJAqWK36RkD0_EmOdmuqvZIyAFJzS58Z0-rrSCqd_SKpwYvAI9DdzFFx8VJcyHhe2U7dCm4AIxfyUsZ_4LqPLJOPn7ZnOdx2m5SONjAapKRM0YLJscycnmCJKfeY--3s73DIL1xnTDJKMhcsolRGizDhLalgDxBz1qS532JpxudffcyfL4u1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQHddPnKAWYMQ2GaLrvmcof7Q6yyjnpJsmU-cDd2aM7rYxK1SHOyvUJEAjLHqKW1BTNW86NSzO3m7ey96dXz_KzaUpmyUeNfY9gpM5vJBWysyQRlkUgyaC_vZrYu-yzjRoZ2d2IaqBOJEz6UXaGGs3PUGg6zd8MV82sYtnNB8yxMcT1vi8vtnCmPPNOyYJylEattKnX5jTYnE4FBLV0qJKvWptMqmxVpN9_2WnCqZjQvC3iDbRTIHgDweq6qIzUra2sWWuZNwf6d5plt3lPQio2-U1eNVqY38GhqRBghO6CVtIe58r9o8Vcb7-Lsw6hCL_RSudlrFgU92V_DdYnhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzoKIipfGh8QFpWO2UhO5g20maqHyssL_95tpWJXLMmVobLpSdPY4k2TwrJy3eskri_R81V9i5embfHoUVAs45qRvzS_AtXyBjHZudUXGdIC_Dd1pu7uzazID8ZlnI18B1vFZ6fycnLFJ0THASGqnpz_4x_0VkJfxFTiZBWwi8w47g-3rJL9KnnyZXIgsIKiFEg5W89V-ODF6xNiZ8O7ksK5HTyC2LGQhmrkAgHCPXA9Ww07LOLMwjH2urqKQzcdYX55ctO_ZMQYOvul7eZU2sH08kpRyMtFQjTOKAAvq5HkVTI5CVi0nXJpRteiN0D_vxgnfI0t3bae860WP1adEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=UD0GR2W2eTWh2hLvI3R0U_QiE03z29yPqHVrpFoMC5TL177uKT4P9viNWQpk3RyrkzP8PdPfgBwG-IpUO-mL_hLTr2OIvQK1H-E33IiENsHgYdLIiN_l7suxnunSfJmjJI_AK_8P31DTAJUVSSgA9xAC53D8dKKHpYL_3_AFP9V0MIPo28lwYyYv4H_tW3tmy0mIejEgDk1Dt_2LKmCP1L4qy528lw0Oqm661KJsSjAtLlnLFINnljP0tCQ7m4cMGIPxvvLNRitX9-hV1YKE4xbgY3JyrzsPhjkpOWb_XnLMz2izGcdccOMg8rnNUc7Za02zgpVRIpmpMClqaJ8jlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=UD0GR2W2eTWh2hLvI3R0U_QiE03z29yPqHVrpFoMC5TL177uKT4P9viNWQpk3RyrkzP8PdPfgBwG-IpUO-mL_hLTr2OIvQK1H-E33IiENsHgYdLIiN_l7suxnunSfJmjJI_AK_8P31DTAJUVSSgA9xAC53D8dKKHpYL_3_AFP9V0MIPo28lwYyYv4H_tW3tmy0mIejEgDk1Dt_2LKmCP1L4qy528lw0Oqm661KJsSjAtLlnLFINnljP0tCQ7m4cMGIPxvvLNRitX9-hV1YKE4xbgY3JyrzsPhjkpOWb_XnLMz2izGcdccOMg8rnNUc7Za02zgpVRIpmpMClqaJ8jlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Imlzg5S5VfNaU7tl5NIsSv1sihz1mn_c4sBcd_vZTGq3vLQxID021baVEKa9DX9YklvB3TC7FoxDO_QnGJhMP8YH_tFtI1FiTW94SzImzEPQJWPXKwUh22wN50YbdKfmKLL5iTSzBrUaaUSgj_2SehLi5E5MOtOTu7Sm-fEaoorY9zbkOfU3qluuNZpUtQVI79Cv3UmfeE2vYo6U9Vq_P8xgofzJRGhHX_1VDttk3MVDxLUC7o1UOrp_7DkW7dbsRmyklFH_fvlwgtS_M_fZKO3Ncm-B1zm46lsg18-B4CsGhyJqVULOvegglzGbdOXxxPhqLMXjCK0Pb5Prq5cwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Imlzg5S5VfNaU7tl5NIsSv1sihz1mn_c4sBcd_vZTGq3vLQxID021baVEKa9DX9YklvB3TC7FoxDO_QnGJhMP8YH_tFtI1FiTW94SzImzEPQJWPXKwUh22wN50YbdKfmKLL5iTSzBrUaaUSgj_2SehLi5E5MOtOTu7Sm-fEaoorY9zbkOfU3qluuNZpUtQVI79Cv3UmfeE2vYo6U9Vq_P8xgofzJRGhHX_1VDttk3MVDxLUC7o1UOrp_7DkW7dbsRmyklFH_fvlwgtS_M_fZKO3Ncm-B1zm46lsg18-B4CsGhyJqVULOvegglzGbdOXxxPhqLMXjCK0Pb5Prq5cwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=ow_j1R2mFBDwBXbHXpM7a6aMYhsnVv3WQ4Ed20p4LW_bk46emvVtFAzw3aUJIpJYI6NF46ova5CUr5qEbYh_Rc8WxsctZknjrnWnUQ_xWXBWoiBA7pysguTBOObrNDFYvSoOlWmjoxIu2lsFeIvPbcM8cmkrBUU5gVKwPepZ7J_zE6BkKUnBO3pClGCYk6Ii1cdTxQxLvSHjmMukYsvsG952UOLQIBSYXUqJissLj5Lz0pCDPcaB_ORW9mYS96ZihlwepYv4WkQNzdZxmBXddq2hauJiMvZrB0TmVhF1EegoKsD2jxPtpOT3cukBdZpd4Ve9CvdncvslntwJ-Lgnbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=ow_j1R2mFBDwBXbHXpM7a6aMYhsnVv3WQ4Ed20p4LW_bk46emvVtFAzw3aUJIpJYI6NF46ova5CUr5qEbYh_Rc8WxsctZknjrnWnUQ_xWXBWoiBA7pysguTBOObrNDFYvSoOlWmjoxIu2lsFeIvPbcM8cmkrBUU5gVKwPepZ7J_zE6BkKUnBO3pClGCYk6Ii1cdTxQxLvSHjmMukYsvsG952UOLQIBSYXUqJissLj5Lz0pCDPcaB_ORW9mYS96ZihlwepYv4WkQNzdZxmBXddq2hauJiMvZrB0TmVhF1EegoKsD2jxPtpOT3cukBdZpd4Ve9CvdncvslntwJ-Lgnbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxq309aMuOLWMD95A9TOIz1rRkao1NjVekudV-KoxWnrxgU1EaVofrLZEarmuEbLXjodVeTi1EHQ9e5JUP4a8UkLBrFevz4Lnf-MgnhpmgZqlelt34z2zBiEmGIeZyEQscz73ymzifcOKfe1WNv7FNFcTEADawUd3CLFdNvL0pPbAOQggnbbOaZgJXJnQE9Pjn3WGoNiS3ylIkteEIJQqzy4iBxzJouBFSoJmnIEPm3Hh71CGQkX6y5Vlj8Deg8G66eaurCR8pgvGP6DQvfOA4H1DEGOD_jBjbaVDGX5kaswNvqxOGCVgV3AiSG0Z94I8ryzVvqAOgyVabXJVN8TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJs2ry16czj4C1eY8EWPWgVqV8_bNjhDlMRWBbxyWSQ7h_qC9QPvj-jgpcdULO4B2h_OQpjmnx4NFj_O3VZtGX2OjEW7f_6t6YV9eXHuCBmVRH4NsL9PMSnVfTLhuOOLnxFZuzgQ9zJqdF6M36hAAkdRzSbgL6GUDR-F2sMAy-LxsvFCaHHYNqY2g9DqoqHx7Bimd1jpnScmTrbvSVSoPkEr7nlg0vx2GEFgobcYv0B8ekHpujpx1aUZEQ9WR75t5kYfBXFSAbHF1kC6kheTU7efrvdsoKrzCYHu7oVq6tQn8zJhuZ5TJ0qOYO5DrDr2-pYioKOyIiLD9zXet16L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFzRToBVDJkG_qkzmDFzcOUr6KkDCo4NsvCLUhLuNdQ2cVN47N8YhbdksHhz-5ipNQOZijIZ2Ghlt5d9-9xVXfV3cMWM-VytyTpaneiE1-L1KBVV3RXZ2IGX3wkqiNg1ds-eNgNf9x2mucyIe9axqCg-4jn9JlESII3b-5n6fHFZqAU6K0ZdwEzsth-mCYuUgaWEcI_VzftfCYBCHbaA4NgfCVgZ74Z4SujEJG5P6EnMHt38miIRtQXI0dAKKWbGb0PNUIxwfpIQdqCUaxOvHpbdpR3QUrS-BJxq2VlrgGXlotayk0Ij7rgqgaqMZOZ0RDQqLRynYcan6LTIykyoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZnSUQmTUjhprAPCDKsMKXYpbNwiM-kXRqpsCctDpzlrZv45gQ678fOUQuZQsT3w2xdsgRQ-hE7UU79Dmoa2oPb9LYeaZ9VWed67gi9H0q4PANEcGqP3D8I7VNDPultbuEz9LCR__38m0HpMJpmdemxwAHlVDMP_QRQBoRZl_80sFxh2Wcj-4MTvmSGqMc8mkoaWuhrVG1-E5TMr2rzHfwLGC4mI9sgIlsflRcv5IObtORyi5K3WttIlzCdcROx_n1chLaJqTk06RZXWBZjRWnhBN6dD3CuZqz6kVzPQrPbZvYoSlfOy-P1ZASWze6bLpKg8O8_uPbvxwyyEJmDkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDPqPnQVUonfbKdjuQxuF4Q4gU8ArsECbzzx0Lc6s70cpLEk8nO5v2tdCog5NYw4ECwtui8Y_FofaetQ351E9EaS_5e9Rj6tS9vNzzf5VgU6kh8gRv-Zwz7DycP12thSOXk0j6YlHJKm239mNoncCF_BUhPV663kkRYfHOwNqsKuPxSENP-pdWha-D2rUHkyzel3-gcHEUPsHTKxV1t7b1sTbVMbrBpnsB_6IUcmA7SV20GKGf-Q_Muk3fz3d5iY0CYEAGUwXPSvm4rTvXXIvDK6ZNpYbzqd3D7o37Eko4Fc5JunsrTkAyoHpt8wqPkrDV1AYpZ7LVWRS847UeXeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0t0yhsWDeuMeW9g9oG690ps7DSdIFOXmXtLZFt8129S9u7crGnqqLl6BDvMk4M6PiAG--aiN-JE_I6rolvp2MePHyCUfvPsEA1ApxUqUZzLNmVP9ybJW_aTfxymdUQN4QfPeSWdikodA7gTNtDsxV0LgRGAeYTLQaYRm5q6UJxjEe1aJG9oGRNlzR0K68981hjlD--xPwSEp76p8xfmAvnjijZDMqZXfNbO96sg7jHb0iaU0I75nR9GlhSXVwTQ7MRYojr3OPxZHVUDNves7wZu0NFbO4pLF1vArYY5ghKSzc04XSBUK-3XunfYWqMc6YncB4jgpDaCBY_dX8hXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuXOKdMJhVMJF0eZo-MtOx0Bw0BMnh562EFJBfAjnWe9nJcH9mwu2z4BOTXLfCZzQiaKrxnxsD3RLKvs1MRZ1Hyo2OvK5dGrut2b-jsXsTyazg_eaj8iBzQTqYNzzShCv-rok9EXULRIEy2QxOhzPmFEpAZDNnw4lfdD8x-3Ya4Uh9a5ol9kjHLKrV4YC-cbR_S7WBh9Jd2ca04BI3FczFmkeQPxFyffWf-IfyPcL86IX7M9mWJNc63AOh9KTE8RG9O3CsQhQ3UcgxgOo44wx8Hz6tj8X2wwGHzPMAerSxCiZuBKoxbwRcxxlfUE21jV48pKZUGnrEzLzBO9spZyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY1o0RUziu7IjvckP5JwL7yw8B0e_DRj5ymRRyg22ntaplFztA8fYUOhAgx9yH9mZgUONHoo9iCrGFrfYq3dt5JxeM2IRjdsY0WStSy9L0XpBkU3tdZm5glYsiXjrR_QkWmg4_PF5ANGtaz2zbsCihCiiWOXYhNbp5rX4G1Ins-nsjfiId78IZUNZx8fvp5OtfHIlsWtKSUEM9go-oR4R1j7oxjEGAotvOJ9z8voXl03vXexWR3ZbF7_Jxei2b-WH5IQd0UsWoELJL5R4nbWlg2V9Gokm-uMhZN4Fa8m6W3geJFCxDDablovkdB-ZT2LK1my8dBnKfZyMr7ESpRLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5TIO9CmDwmDIqvti2dJfBXNOm4YwQstPR7DghlGp76W-SZ_-vcbnp66avWPcP9dkze8thmLEtE5EulTeSBKVmtCGewb-VqaK6rToG8EaXfew8XooY7cdjbDTQvn2HYlW61RejTTCIkMnwjCIHJZYkyU99rpBLsovBQowU8ul-iQQo5jBxstuegSBB2Ii_4Gby0nsKSQ1ru-Ty1bKoCj_c5CLEbiAIAipTCdmCLXGBdubHapgHEkenNKwGhrKGJ2eu164ybwevXpL5nUb_wwdgUuF1TERXtQjedm8wjPdRUuK3tZUnFiO34AZD41S7kgo7USCb2ecfUkOrmJE9GSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs6v2AgQrZ0cbq1QmYOaNWFETnfkHCQk7NZbankSN3mKR2eQ6wSrusDctNIJZMhWiOOjZ2UDrZ3tPCnd6b0JWOFSsoAjKiZgpLFxRxC6SiAuS_aKzmYURkCmDFi_EmTrVEjCtn7VJ6zlxAMIlixz8NUJtm63YXDEVOg1ScHNHYkWWA3c4eYkkdE_1ha9hVJ3j84t5-TiU_NiqeuT1v3znQRpCtga5uit_0Qy9u47I8xDU1RJq6BkBTo5paPLQmwabcxjwC4aE2p3RClQcbvlxwCOULZTzBz9t8hHtDOFb7woeVOu71lKYpLaRHwOrnY97j8llMfOm8vzyYW_b1vhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Drake
📌
Ice Man
📌
Habibti
📌
Made Of Honour
📌
$
ome $exy $ongs 4 U
📌
For All The Dogs Scary Hours Edition
📌
For All The Dogs
📌
Her Loss
📌
Honestly Nevermind
📌
Certified Lover Boy
📌
Dark Lane Demo Tapes
📌
Care Package
📌
Scorpion
📌
More Life
📌
Views
📌
What A Time To Be Alive
📌
If You’re Reading This It’s Too Late
📌
Nothing Was The Same
📌
Nothing Was The Same (Deluxe)
📌
Take Care (Deluxe)
📌
Thank Me Later
📌
So Far Gone
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd1vvajNAXVSgcLsNpj-tSc79Ie0VXpY50Vk7a6N3EDrWnOtzxN_kZVyCJtqIaS16r_X3nEU5Hvn5GqgpYEheVftds-_qQQhrAlaNycn2W4xuv4t_OVNNbl2pnYhHZG8HOr9b5xWPFayQgtFbhx-AKdlsOQqDFy-psqzfzNBeBJpJouI_rRJA7tp2Fc1kZHowXYlu1lMSakMqv2ubUHNf0l8gzszZiF5a1X87MtRiMsMX7LksvLtnJCGx_jwhyqt3r-FBz5uMapM4rGyAszoSST-AXFh3g2NEb1WuSr9w69pl9M81QqV2C5cVnYOMnfKqD71SXIAFbctFs1XL1KvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBYL0ckqKDZ7jF_gjMgQ2cW3ok9CO7ldEEdp4WrNJzRWDE01zeiSMUoCN_J08GXv68UL_7tMCBI-WljIKLIyQ1XlSIHjPES5Sg4h3zX_ns0A5ORnyCPBFRrKrdQhMjQgtl611tgsC_Ud4hdPPbM53IN1TzrSaE4l_0ER3mXAUc7-Qtj3bB1uNUGrHP6Epp1VrNXpTNv28oIMXJdzLHXUWdbUyw1dBmXV1sIk1uDmLxbkrv1FPfnDiJrBJ7jKrEJWGr__ylF0cCSTI3HBjY7ACWQk11QHxJ__xrZvQAIPGFmhgvz9untAjahBm8nn-iHIwOvNmdktv3u4695nn6iyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJRYGmIQk3rjU-Yevr3fIgKyavbxDACro8c4YPUUvRv6k5WzeYLzf1L1zkEDVb1n4Zo-BO0dfLwhcIJmfCJvdINNH43A0Zc0kxlsSS79ojFWKzS0JJLUVGNeXxZrd4PSVzHMHXFHDtUKzAs7wRO8ORE4SvuW-Wk_jA15MwqxJXBcraBlVAOgqtma9EFrr0_JDxiMZj0TPLmnyrNcxdYbWSLCl4Y8GaiEsDo55e_POOeOPzj9TRZX9e8DZ9ojzUgsQKhZp1X7uaVEIp_e1w-RjGZcp8LjGaMT8Trj1qYQVuw_pW-d8GlPWHVEtx6uwxo_VI6F82pspKVZyTwCY4H96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q80kb9aZ_cOP91zBrvnlA5A77Oa8lZyUoidXydAL5Fn2laV8oBjZe-Iur3NeBlnHozIH9YQzvEcoseRc9ocXjSYiIh20zpR9M5kas8FVezUYyT7S-fNDb5Sc_-b81QVfpgAZl15nEjVBSOASW9Y1U6bJUxecmiekXH9twLPToWZLwE9OktyH4vCbJHAdVJrQyhp3RKnMJxoz8XQnycL9VINcoNfqnfWIjt9nB_fuDZP26gGkxEO-SwE9Ukr_5rMBI9pzAIXyCYq3PJYk3t83lgX3JehdMnc3m0eYJ3DoFZb0uICpmhzGIiMh1_-icSzNqbPVWXYBSxU0uxJe6Xf1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=n8Avq9iJtXeOxKUWE_r89umNLtC2H8LqZrHTG3kEyF3zAaC4wqmT2i6XApBAwIjKge3Z8NkbWkET7yf_KFSIUumml_O5DLJRrHESmYuCwBuqBTosd4pRPyOwi6i4CYBGsgCJs-FT_uZ-HhYRVUNTlN0nDu8JTg34bSCZOUQYvBtMahoDN1FeeO01X3pF2LTTOuEd-5oAa9xhkxKCEV8UaLl5P2J2SUHEheUyEh1zqb-ZajwHVbI8aFxhYcod53wBWRyVdcQI6BupBOv_zKlOA-LksGu6g4F_YGQgPOOoz7WWrmgSVYagy4gNRFrHdr59kb6-3JlLNnUso35IMBmKcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=n8Avq9iJtXeOxKUWE_r89umNLtC2H8LqZrHTG3kEyF3zAaC4wqmT2i6XApBAwIjKge3Z8NkbWkET7yf_KFSIUumml_O5DLJRrHESmYuCwBuqBTosd4pRPyOwi6i4CYBGsgCJs-FT_uZ-HhYRVUNTlN0nDu8JTg34bSCZOUQYvBtMahoDN1FeeO01X3pF2LTTOuEd-5oAa9xhkxKCEV8UaLl5P2J2SUHEheUyEh1zqb-ZajwHVbI8aFxhYcod53wBWRyVdcQI6BupBOv_zKlOA-LksGu6g4F_YGQgPOOoz7WWrmgSVYagy4gNRFrHdr59kb6-3JlLNnUso35IMBmKcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtoxejeIcqzo3BAY-RWK9GT8moNb6jPVLD_L6ggmnlJ_t2P_Qx6-RCYsg8Wi1zTI-1JdroGhaBBMc7rcpV5j3kkzL7hF4gp0PoqaXX8AULWMAOofUkBDRCIRpjlIeMGJfenvIdj8HnCVhKMhpKC06BfOGGTdfzSXpUcU3EhocKowEJvkxm7GTS3ZLmU8A4eA-RUzMbuJJQxSzFcebkQQTVh6mlQ7V-_uXtX739X0tTEtT-NrOCJrFrUfTf-dYRKhuOQhidkD1EcdHMge9AS-8J11YFNP5LBrpzwtbb8x2lT69xPZ7xsNorzIGaA7LS2IUIH_OIigU68BoPJHjxlplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATCLAu9QMFQTksQd1ixgvU-5Ndp_QeZw6N6h_yUZQLdNpQpgZTx6k5RDQTbF3H-ZZu0aQpKtQpeZDideSNPpVIZFA1Mlg7aJaQ3iCgcHs5OIQDhJ62bEj_C_SBPbaGEi8lmPgipRYKOQLBMEG4FxW6IagSMmh8A3-KVKfQnZ-jiNLy8jt4Xtld0i6wKE2Rf9UqdmkFv7Az2SgHUKfdz8v0lemLzHap_3DskVTbcvKcaKNCJNuvXdXti-NbY3q3auulORa0qLj9D3OoeQb8brUBlEOktKZD89ipmUPQjQ3kaPIZ638z9D_uD6bc2EGVDBqS0d1SbmA8QAeJD3TiUCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO5dapp5UON_FtSJ5MzIsAN1XCOBTsxTuM4k5zELvo7lWIK1mDhgNb_o7EaCRgFnu26jzPat1CkKxjYZl0gMPQxH7ns_inHIh_JoGpyZF612n9_p_WQaoF6QsY0fz-X4bfgzFIVD9IrsSDjXzRm8Fwd1mHIoSIbrlkLONHKeCCWQ70zpOs7g1UrktfgQyfprZKB6avA1qcpAmjEQOKriozwpbmls38Pu0mj6jqaWpTcEXuu6pcjQh4aoZQcslRGso8Eyjg-s4UHq4R9dsEZLeoo2RVh9JhhMrkYdy2OpJBrHraPycVXxKe7HEXUVUoLMEPiGNODYQ0O9xxMUpL02mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8lOI19jNoHqqtuJjFphrYfgUiy05W3_6rla48ACvjfO_JeM27Nrw0lT8IblqZlAqHFEG09mhfDuQ4zGhapVJ2KNVi2ONSozWdepC5qjMLfuq2E9YwZL-hfmOo0Zyy8Lw_Fc7Ehe_RY8iY4MK98bQ-9QwWjxMgy-G8aUuEx8T2scV1f-fr29hpShHg2wmiEq2gQ4vrAFVL1wefBKxDZCz0lxPxJZA3j5Xu82bktigNY62rvZkROJBFH6aazW0hoRPMNIe40JfWOIIZ6cJy-v2IFbwqVZdnRP8itcmkaMkkX8x_tK5K6Errm3lb035xGR44cziA_9zPTQ4XMxX1zVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
