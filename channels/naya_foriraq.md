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
<img src="https://cdn4.telesco.pe/file/PKIxG6ZM3HudFY182CK-sG05fmF2EnsNv-12DWwwi3CWr6F9EajkSo7ou64ycKjfQ89TURVlkn_2adoyimoZZ_04TtXUNQvl4kp2CbPiW6TvsDQInbzHRu4aJAd6JGDOquK6cUdOQxJPswBKaA_41cMVhheekAoJJGtsQN787l6O3-ItqjyAemEF-PYM_FH9BidStDs13d1MVq7iJuWKTgBjs9I7xSWCgTIXQZ6hRGPvgmZXF1LdXE-F4YzT_LvUeR6QMr6IJBsc-Lrh09jScd-XDNvvr8NqD3moti6aqDO3nL-g5GW2L6nPPn4d5VYT6rqD4J9lively7k5fqd47Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=in_vX3-OCD_mAcN6LyGI58TuZre0i19ESKAqJQN2iwNqQvv_l6pZOPkHeAiNExbsKucYKeDVVhj5Ax-yVfkTQqPUb-9UM3H-GoxT4Oxq2oH8nNf-OzZlpq6Z9ZHHa5WwgDKaMG2ZpWN_2TWbiU3KaUf289k9-Wp3hVi0Q5lchcukpTSAlFGyHJkysDiH4iCLAGWpGcFL7hLBCrt5PssDE5vyIzQvwuOwKdzfO1pILgjZp4AJxZL0iP28EEuwB85NokyRyMqI5XpVC2dqWl886sz6kINau7DEPheTmWyaDBSv8fYGy8FapSSpP2RQiXiSQjKZHzaSN0xBm8Ya-PbzLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=in_vX3-OCD_mAcN6LyGI58TuZre0i19ESKAqJQN2iwNqQvv_l6pZOPkHeAiNExbsKucYKeDVVhj5Ax-yVfkTQqPUb-9UM3H-GoxT4Oxq2oH8nNf-OzZlpq6Z9ZHHa5WwgDKaMG2ZpWN_2TWbiU3KaUf289k9-Wp3hVi0Q5lchcukpTSAlFGyHJkysDiH4iCLAGWpGcFL7hLBCrt5PssDE5vyIzQvwuOwKdzfO1pILgjZp4AJxZL0iP28EEuwB85NokyRyMqI5XpVC2dqWl886sz6kINau7DEPheTmWyaDBSv8fYGy8FapSSpP2RQiXiSQjKZHzaSN0xBm8Ya-PbzLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا طهران حيث رايات كتائب حزب الله تشارك في الوداع الاخير
مشاركة واهتمام واسع من قبل الحكومة الإيرانية بوفد التشكيل العراقي الأكثر ايلاما على الاحتلال الأمريكي في حرب رمضان</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/naya_foriraq/81123" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=H7KbnrIsptv86LEMJeP4LgbRXvL-phdSDBqnXOLMSXyLaDHH8kuDkROklpZ2C7FPw8-BpRm8SLFA7q0WxntpYE3cChl_FClaNuUyr2MtpYb9eZfMjF-af-sVSAzNRgph9YguciPQP1oVHIuxxFlxlc6grjzDrSQ24FZzlJnBYWnln-13mVswpcnqUGbYMkqEHY85vZSGFQ6nLMXKcdP83rKHEhrh1hwLVktLj31Fl9mGNfYXVEivHkKMZHhQ9twtX49W0DZrKJuIvyZJhfqMYhWJG1U241bUH72irEid3JDzcZWAPvkV7TsA0XNxxv9VvyATgAY0Gn29n_VSWzIPJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=H7KbnrIsptv86LEMJeP4LgbRXvL-phdSDBqnXOLMSXyLaDHH8kuDkROklpZ2C7FPw8-BpRm8SLFA7q0WxntpYE3cChl_FClaNuUyr2MtpYb9eZfMjF-af-sVSAzNRgph9YguciPQP1oVHIuxxFlxlc6grjzDrSQ24FZzlJnBYWnln-13mVswpcnqUGbYMkqEHY85vZSGFQ6nLMXKcdP83rKHEhrh1hwLVktLj31Fl9mGNfYXVEivHkKMZHhQ9twtX49W0DZrKJuIvyZJhfqMYhWJG1U241bUH72irEid3JDzcZWAPvkV7TsA0XNxxv9VvyATgAY0Gn29n_VSWzIPJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إجلاء 11 عاملاً كانوا محاصرين داخل المجمع التجاري الذي التهمته النيران في شارع الظلال وسط العاصمة بغداد ولا تزال النيران مشتعلة وممتدة إلى الأبنية المجاورة.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/81122" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=D77kkTNuaPyPNoIhCyOyO3rRuGckS6wZH7m_yOVrlXlRqNP9xPO_xJjNGnCqCRKMkuecQljofNrBcdTKVO5vs7mw2mWWQq8C3EF0iWOeytIgpAa9BCXUYzAV2Ec-LchJuys5aaAXmmFI2_KpqHC0_MA2ha2m1G7VmEaSBzCkhHDch9LS3IMObnusaLpN-NwWcgUNvXoT-X-Kb_MVp7kSHLHftWnY-NZyLP5MQBVTiWxzr0JhyxF9ikoiclxAxXSxeBZ29Rz1kLXv5xa8J1ndJ0jfeFZUcF25V0boBJiAbvoZRnjz19R2MXVSF---dk-2J6unSvMX6QWgfE4okZ9SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=D77kkTNuaPyPNoIhCyOyO3rRuGckS6wZH7m_yOVrlXlRqNP9xPO_xJjNGnCqCRKMkuecQljofNrBcdTKVO5vs7mw2mWWQq8C3EF0iWOeytIgpAa9BCXUYzAV2Ec-LchJuys5aaAXmmFI2_KpqHC0_MA2ha2m1G7VmEaSBzCkhHDch9LS3IMObnusaLpN-NwWcgUNvXoT-X-Kb_MVp7kSHLHftWnY-NZyLP5MQBVTiWxzr0JhyxF9ikoiclxAxXSxeBZ29Rz1kLXv5xa8J1ndJ0jfeFZUcF25V0boBJiAbvoZRnjz19R2MXVSF---dk-2J6unSvMX6QWgfE4okZ9SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلم ابو حسين
الرايات الصفراء الراية الأقرب لقلب الحاج سليماني والسيد الولي تشارك بالتشيع الرسمي في الوداع الاخير</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/81121" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-text">كلمة الامين العام لكتائب سيد الشهداء الحاج ابو الاء الولائي (دام عزه) في رسالة الى الشعب العراقي العظيم.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/naya_foriraq/81120" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKfhlMWiLjLLhPy3luU_-EYGq50vsbkrg8888tidQxrGaJaqaHMpIXYy2Uzm2WNuB3KTKEdhWIseLpwdg2j4ywQPkrtRX8_yyuO5vWjNyQFtVOJcZzqdowkPOV_6TZ3ykkVZdon6IMkguguep3k1kOVojflK4MHett8WPcW-sesRvZYxAEOFROnYzztReQrz7ZOLu52X5C-mauqgh76h3gn2vHXEDu0ErbX2PXhaHB897O1nIJ07b161brOezH2_G8kbj9AUpP4eu2-gtgBD6S2n5P_x3bN-sifyJJvDnj_t3_ULZhMJsPUq_YTzNZa2xQQbq9q80YQdkGTP9opczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: شكرًا لك FIFA على فعل ما هو صحيح، وإلغاء ظلم كبير!
علماً أن الـ FIFA قد ألغت البطاقة الحمراء لمهاجم المنتخب الأمريكي ورفعت الإيقاف عنه قبل مباراته المقبلة في المونديال!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/naya_foriraq/81119" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruBCwpykcR6WHNZUybivQkRm5Iv-XErr9dorB8w3XE-sL5XZKbElN09RZAL4X8zXgA7jawQEhhdmsPusvCTcKpC4n7OCRqpxZsBvKXqe9djGcpiJIN-5ArPP4puhZXu62yjdZ4eemg36idLHGWQgXTEqfPUuMYM5BZykxBokTUw5mIeHJpBn2Tf_gx_fVXFiy23yimMzAYejctKyMyS4iUOIdaAFWX5HI3dmaZmipu0qLNoZvrsdkjCiJWRg62SRw-le9HKDUZ8xam2z3PtzcVVi6O6M-TP2SH8ixN7NfcPdhxYXyZ8uU-GWoWgIwvU4UWCfSKUOJWc2EOIfDFBr0XDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruBCwpykcR6WHNZUybivQkRm5Iv-XErr9dorB8w3XE-sL5XZKbElN09RZAL4X8zXgA7jawQEhhdmsPusvCTcKpC4n7OCRqpxZsBvKXqe9djGcpiJIN-5ArPP4puhZXu62yjdZ4eemg36idLHGWQgXTEqfPUuMYM5BZykxBokTUw5mIeHJpBn2Tf_gx_fVXFiy23yimMzAYejctKyMyS4iUOIdaAFWX5HI3dmaZmipu0qLNoZvrsdkjCiJWRg62SRw-le9HKDUZ8xam2z3PtzcVVi6O6M-TP2SH8ixN7NfcPdhxYXyZ8uU-GWoWgIwvU4UWCfSKUOJWc2EOIfDFBr0XDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أنباء عن محاصرة عدد من العمال داخل المبنى المحترق وسط محاولات كبيرة للدفاع المدني لإخراجهم.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/81118" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏البيت الأبيض: ترمب سيلتقي الجولاني على هامش قمة الناتو</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/81117" target="_blank">📅 20:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=gxOMPUPNzBMjSPXU4Qh8Vw3eJpVRe-ReYT7Mo_rFdXnXMVmB08G__np6kllPeWyaqHvmVXvEK11kJOtjSFB40c1b7HTkpbksvfUHUHIRQwx5qCVsv0DNKid6b9P5fenQTdM6_SvaBBKDIN43ihPa-1QirmJDmARr8F05wtUejgivvxJAOn9V-e0_hZhYnbjL9RBzfWNkrZG204Q41cqhqAZtrMfrCfV7Qdd2cknNH3O5u_MB0R9KYDJDLcjwGQRxdZM-0OP9XwhQsK8mjNtJNyvXHmK6_dF3UczMrCYubwAeiMqI0VCjrahBpHbv7ySuMxuUCOwq82KAWBxN6h-DAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=gxOMPUPNzBMjSPXU4Qh8Vw3eJpVRe-ReYT7Mo_rFdXnXMVmB08G__np6kllPeWyaqHvmVXvEK11kJOtjSFB40c1b7HTkpbksvfUHUHIRQwx5qCVsv0DNKid6b9P5fenQTdM6_SvaBBKDIN43ihPa-1QirmJDmARr8F05wtUejgivvxJAOn9V-e0_hZhYnbjL9RBzfWNkrZG204Q41cqhqAZtrMfrCfV7Qdd2cknNH3O5u_MB0R9KYDJDLcjwGQRxdZM-0OP9XwhQsK8mjNtJNyvXHmK6_dF3UczMrCYubwAeiMqI0VCjrahBpHbv7ySuMxuUCOwq82KAWBxN6h-DAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحريق يمتد ليشمل الأبنية المجاورة للمجمع التجاري في العاصمة بغداد والبدء بإجلاء السكان من منازلهم.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/81116" target="_blank">📅 20:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=P9Cz6YG7JPCE4TNH_zidXYneqeStoXEzirB_UEq3E7PXXQ1hNxfniHCzmEBn3O21rWmJmoqimTnSwuAHkdgsB4g7F_NNFbRIPTV0gOTUUdjKsTsiSHF4q4WWqVuY6agSZ8GKRgDDvzVYwVf0LrIy-BuHauEKDZu7LWCJxyFvLDhQFZqWZYcq2sT3kL8YUhNheKvGRkfn-FMfpkJaKBdmmpa88EKabvT5Jg06wJ0E6m_6Uy4LVKYP9EgJGyxn7XWu31cONuRaePsXaGtBn-PFji1FrOpjZ7pvrvvxljnbmd_u1oMqboyYOPD6avInATSoMT4ThXinioUcjpRtB_D0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=P9Cz6YG7JPCE4TNH_zidXYneqeStoXEzirB_UEq3E7PXXQ1hNxfniHCzmEBn3O21rWmJmoqimTnSwuAHkdgsB4g7F_NNFbRIPTV0gOTUUdjKsTsiSHF4q4WWqVuY6agSZ8GKRgDDvzVYwVf0LrIy-BuHauEKDZu7LWCJxyFvLDhQFZqWZYcq2sT3kL8YUhNheKvGRkfn-FMfpkJaKBdmmpa88EKabvT5Jg06wJ0E6m_6Uy4LVKYP9EgJGyxn7XWu31cONuRaePsXaGtBn-PFji1FrOpjZ7pvrvvxljnbmd_u1oMqboyYOPD6avInATSoMT4ThXinioUcjpRtB_D0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق شارع الظلال في العاصمة بغداد يخرج عن سيطرة الدفاع المدني ومخاوف كبيرة من انتشار الحريق إلى المنازل المجاورة.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/naya_foriraq/81115" target="_blank">📅 20:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95438bf709.mp4?token=VWU6Zh6N1FcDx8AzzlC8Y0husLJ0epRR3-9lhn_P9I7P1_uzc311dK_fI71ZNAebD2g00vq5z0vzvH0xPe41rrNcevdXiJ4F2sZbrUqgmkxL47VAwZteTiUFXUvwLuvJLwspbm27OBNMY9eADDjYQ6W3NEL4I0zWKQUEiliwbg_b7aa1QiFoeDHsOOa2IfSfHbGDLyPU67qgSvnwQF22yh06ZQwbUKzTh_QUWLBMCF6PTR2RGlGedO8EhWUrmfgkMLqooRHbY49EYMeskSVyhBy_cN8js_lfLbC-3IRgfQ5qgMD38NICQ-pFL5QniyAcu84f4iYB5md-0hBsgECfFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95438bf709.mp4?token=VWU6Zh6N1FcDx8AzzlC8Y0husLJ0epRR3-9lhn_P9I7P1_uzc311dK_fI71ZNAebD2g00vq5z0vzvH0xPe41rrNcevdXiJ4F2sZbrUqgmkxL47VAwZteTiUFXUvwLuvJLwspbm27OBNMY9eADDjYQ6W3NEL4I0zWKQUEiliwbg_b7aa1QiFoeDHsOOa2IfSfHbGDLyPU67qgSvnwQF22yh06ZQwbUKzTh_QUWLBMCF6PTR2RGlGedO8EhWUrmfgkMLqooRHbY49EYMeskSVyhBy_cN8js_lfLbC-3IRgfQ5qgMD38NICQ-pFL5QniyAcu84f4iYB5md-0hBsgECfFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار محاولات إخماد الحريق الضخم الذي التهم المجمع التجاري في شارع الظلال بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/naya_foriraq/81113" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇸🇾
انفجارات شديدة تهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/81112" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c020bdc8b.mp4?token=b1lAlKuXV6G36ZduMufOUmGXb6lDpMdAQs_RE7n59Sey8pKr7bbqI7V1SZUHkY5ooBCTYPOa2MTGqjoZarrh54cU6vlvx6JA59vCTnsG8uSZ8HoBXve3rI9Dwd_Jh_7ylItFeH9Wv4llEZNqzELH7VfT_Pp789hIQN44piz4tEhHl9tGR9juWNYZ13KAWs5Z_i8uzZktc2k66UtK6xAZ9yi2HQpJyaI_GSsfnmow4TA5E2rgVRGtvn4Kq3WVi9yy343fnpb58RGfB7bWQtuEu9odieHjj1fv3MPfz_2ed6r6zVWl6ZE1eqbM33kENssKshcHNN84d9dvNhoeQnnGigFadiDzyrffuM5cWltldPYFxXHdmqAFFi3j3ysVWiXi81F8L3pWIZOScIPKTkIGKI2fPMRzOPhSMTRTri5gE_woNdTqJqVCoVlxmeD5zV58BWporEipVjPXuIgbZJStjgAKHUf4e2Ck9AFSLTYed2PBtUzn0pmNA9xI9P-liz6INoinHych5beLWFmgD2LpuNydhOlqMrpwWQ7SOJ9XOCGgwhmWre1BldDqfsFo1hE-nFz2J3pF2ec_fZUFED6JmBXZ76Xl7wh6FRbF7HNFs3FI_19q9VCqbgVBX9d0KMq95GPqippfZrhBQx-Zj9guQTTQk3WUWVTI_HfZK1GBXEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c020bdc8b.mp4?token=b1lAlKuXV6G36ZduMufOUmGXb6lDpMdAQs_RE7n59Sey8pKr7bbqI7V1SZUHkY5ooBCTYPOa2MTGqjoZarrh54cU6vlvx6JA59vCTnsG8uSZ8HoBXve3rI9Dwd_Jh_7ylItFeH9Wv4llEZNqzELH7VfT_Pp789hIQN44piz4tEhHl9tGR9juWNYZ13KAWs5Z_i8uzZktc2k66UtK6xAZ9yi2HQpJyaI_GSsfnmow4TA5E2rgVRGtvn4Kq3WVi9yy343fnpb58RGfB7bWQtuEu9odieHjj1fv3MPfz_2ed6r6zVWl6ZE1eqbM33kENssKshcHNN84d9dvNhoeQnnGigFadiDzyrffuM5cWltldPYFxXHdmqAFFi3j3ysVWiXi81F8L3pWIZOScIPKTkIGKI2fPMRzOPhSMTRTri5gE_woNdTqJqVCoVlxmeD5zV58BWporEipVjPXuIgbZJStjgAKHUf4e2Ck9AFSLTYed2PBtUzn0pmNA9xI9P-liz6INoinHych5beLWFmgD2LpuNydhOlqMrpwWQ7SOJ9XOCGgwhmWre1BldDqfsFo1hE-nFz2J3pF2ec_fZUFED6JmBXZ76Xl7wh6FRbF7HNFs3FI_19q9VCqbgVBX9d0KMq95GPqippfZrhBQx-Zj9guQTTQk3WUWVTI_HfZK1GBXEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من استقبال الأمانة العامة للعتبة الحسينية المقدسة لوفداً كبيراً من عوائل الشهداء في الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/81111" target="_blank">📅 20:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
مطار النجف الأشرف الدولي: تعليق جميع الرحلات التجارية لأسباب تشغيلية حتى صباح يوم الخميس المقبل</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/81110" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68bd6daac.mp4?token=VZjvSVS3lPBzYdx2lE33N3Nb1tAgmqOp87X3Zw2_Y3huEdP_vW5opAGkB9f6GYKT8Jfu63nuKnmJfdoe8vhply14_QN1ZVYL4Gjhkp_lLHLnLBf_ITSdT8jqwuwa8jxqdR95fOZ11xiS2g0FeRJoG7WocF3PUof4kKCtBA45nmyvTBXf94MZzlwDBCO_QEoqYfogpBaXzCyfjV90AHs3-n1sH1ks-RTy6JlHwkGLzg-M1BetvqROZF32O5M-dgxT1Di9cygV09jd0cKVsPU0ohjGkgTwBShBvF-N3GwrrwRfukk8ubYLAgYT4sUbFWgFQ2j4svVDmu1IUlTyZR8NBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68bd6daac.mp4?token=VZjvSVS3lPBzYdx2lE33N3Nb1tAgmqOp87X3Zw2_Y3huEdP_vW5opAGkB9f6GYKT8Jfu63nuKnmJfdoe8vhply14_QN1ZVYL4Gjhkp_lLHLnLBf_ITSdT8jqwuwa8jxqdR95fOZ11xiS2g0FeRJoG7WocF3PUof4kKCtBA45nmyvTBXf94MZzlwDBCO_QEoqYfogpBaXzCyfjV90AHs3-n1sH1ks-RTy6JlHwkGLzg-M1BetvqROZF32O5M-dgxT1Di9cygV09jd0cKVsPU0ohjGkgTwBShBvF-N3GwrrwRfukk8ubYLAgYT4sUbFWgFQ2j4svVDmu1IUlTyZR8NBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم يلتهم مجمع تجاري في شارع الظلال بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/81109" target="_blank">📅 19:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81108">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09643659f3.mp4?token=TXuqWSABDYnALJQEg1GC86LPKp7B7cYx_D2BwiaKlTHlCspocBaEewf1Kc_RH-udoWt-l2H0Un6FAU4pm-1YHIUdysk5SZzIQnHxyRvZ5rkebGHqBtY3jFNxi_RR3TvY7SqvUsBS11JJBHiuFFQ7H8Dl0j8o50kqhlekOGrTPcFypa9otlYErJqfdBdNSOplLF6_bpKhx0sV6ttx7jTqOezm7pdH9b-Vl6Za-wUVB9T9S7bu9HEkUqwU_FEuTii06ExwzLibCxma2EtJC3GUI4MEe2w9OzIYxMxSm4cpKViUNrLt51HfxLoyoP1dhLBR1iKsLW0lgRHM-DGtuGtwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09643659f3.mp4?token=TXuqWSABDYnALJQEg1GC86LPKp7B7cYx_D2BwiaKlTHlCspocBaEewf1Kc_RH-udoWt-l2H0Un6FAU4pm-1YHIUdysk5SZzIQnHxyRvZ5rkebGHqBtY3jFNxi_RR3TvY7SqvUsBS11JJBHiuFFQ7H8Dl0j8o50kqhlekOGrTPcFypa9otlYErJqfdBdNSOplLF6_bpKhx0sV6ttx7jTqOezm7pdH9b-Vl6Za-wUVB9T9S7bu9HEkUqwU_FEuTii06ExwzLibCxma2EtJC3GUI4MEe2w9OzIYxMxSm4cpKViUNrLt51HfxLoyoP1dhLBR1iKsLW0lgRHM-DGtuGtwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الساعات الأخيرة من مراسم توديع السيد الشهيد علي الخامنئي قبل صلاة المغرب مسجد طهران</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/81108" target="_blank">📅 19:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f791916ef.mp4?token=hKQ129HGiM7a2y4ckN68VVKaZdOEnN5lF9t2wHTlMMoUDbRbmJ_teldbDcjNVfAfoHJfq7fJL2M7lh50VOImHRiDwaaphLgwRLyEybRyfN0JfecIAm0rkn3D1I-nsxW8hjvU6o1gVtT1GdxeXW7uJnyXXLyCzxzocq9zoBRbeSyG11J-tNk46kcASUXX2F-nHj6w_M9G3vXclc0-X5qmLOkCaguiJPOUdI9v8zSQ8TFlLPuxFqv27CG3CLkJgs-nQ-rSnaKRC9vSfoW8YsppaNEamHoW60KW5amf5YA9viAIPHC5TLYfL_gWTwglBR0Y7zPpPyDwU5iKSHl2KrG4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f791916ef.mp4?token=hKQ129HGiM7a2y4ckN68VVKaZdOEnN5lF9t2wHTlMMoUDbRbmJ_teldbDcjNVfAfoHJfq7fJL2M7lh50VOImHRiDwaaphLgwRLyEybRyfN0JfecIAm0rkn3D1I-nsxW8hjvU6o1gVtT1GdxeXW7uJnyXXLyCzxzocq9zoBRbeSyG11J-tNk46kcASUXX2F-nHj6w_M9G3vXclc0-X5qmLOkCaguiJPOUdI9v8zSQ8TFlLPuxFqv27CG3CLkJgs-nQ-rSnaKRC9vSfoW8YsppaNEamHoW60KW5amf5YA9viAIPHC5TLYfL_gWTwglBR0Y7zPpPyDwU5iKSHl2KrG4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طائرات مروحية تحلق فوق منزل خورشيد هركي ومدرعات منتشرة حوله خشية اندلاع حرب بين قبيلة الهركي وقوات البرزاني.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/naya_foriraq/81107" target="_blank">📅 19:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107ad2da99.mp4?token=XEUdl1iIch8d8tmfQR2q_WMVq8CpNDveSKGs7DMVm3tMyyEGtRrhcVlYXnHhGpTDFU6dhAEKd_j5cmDJ9TG1nh-aLmWuPlvCpxw8Uv7mKnM1kRNi1DbmTnjfuiuL_T0tDrvGn3pmqRSSR4NcSkLqKwfTdAwhUqOenvAn3t9fskHSWn2E9AWyCQYWLHzDfeEjAqpkBSrc__AyFtcfkGfx4-X4L-2qgsn3aEmG-8IG7CNw7ItaGCcGPLbWDR1eFBuD02QcIPE7XVGPXx8mwN4KxZjWxCUEclD6t7oEb-wzS9KHjKl0FPbGKDbvk8SBjTSSJsjzuaZd-DpMvpZVIZNELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107ad2da99.mp4?token=XEUdl1iIch8d8tmfQR2q_WMVq8CpNDveSKGs7DMVm3tMyyEGtRrhcVlYXnHhGpTDFU6dhAEKd_j5cmDJ9TG1nh-aLmWuPlvCpxw8Uv7mKnM1kRNi1DbmTnjfuiuL_T0tDrvGn3pmqRSSR4NcSkLqKwfTdAwhUqOenvAn3t9fskHSWn2E9AWyCQYWLHzDfeEjAqpkBSrc__AyFtcfkGfx4-X4L-2qgsn3aEmG-8IG7CNw7ItaGCcGPLbWDR1eFBuD02QcIPE7XVGPXx8mwN4KxZjWxCUEclD6t7oEb-wzS9KHjKl0FPbGKDbvk8SBjTSSJsjzuaZd-DpMvpZVIZNELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم يلتهم مجمع تجاري في شارع الظلال بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/81106" target="_blank">📅 19:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3abe6f8f5f.mp4?token=jprgy92kepkZm5OFqTaMuHawdWm_FUdFl0NQm0B95Di5BgGXTqBoxFJIT9TPFRgIehdN0s2niQtOTdsy2Z6mdpk8ejrBU0yof4_jRy1WEPJo-lntMtzu7e51o9xDcs4iHV2Vay1iYNMKD-INtqRVwvkp3bR56JiKnL5-FoC_vEovuGIUQ7zRIcMWGYLxkhXybhgjvLCi5U_gvHBucHecLGArXXRzyjeJ136Gv6ntDviEtpUcFCUW20LQ1m6AgJY_37q9E7CMl7g-DjVINisTGdkZAq4AdGbaRtg3Mq0mjqMdWqsz9VkMgwjJuD6-ahIynzvK0SnZKWxeZnw1ma2Scg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3abe6f8f5f.mp4?token=jprgy92kepkZm5OFqTaMuHawdWm_FUdFl0NQm0B95Di5BgGXTqBoxFJIT9TPFRgIehdN0s2niQtOTdsy2Z6mdpk8ejrBU0yof4_jRy1WEPJo-lntMtzu7e51o9xDcs4iHV2Vay1iYNMKD-INtqRVwvkp3bR56JiKnL5-FoC_vEovuGIUQ7zRIcMWGYLxkhXybhgjvLCi5U_gvHBucHecLGArXXRzyjeJ136Gv6ntDviEtpUcFCUW20LQ1m6AgJY_37q9E7CMl7g-DjVINisTGdkZAq4AdGbaRtg3Mq0mjqMdWqsz9VkMgwjJuD6-ahIynzvK0SnZKWxeZnw1ma2Scg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقابلة حصرية مع الأمين العام لكتائب سيد الشهداء في العراق..
⭐️
في هذه المقابلة، يتناول الأمين العام لكتائب سيد الشهداء أهم التحولات السياسية في العراق، والأحداث الهامة في المنطقة، وخاصة الحرب التي استمرت 40 يومًا، ودور هذه الكتائب في استهداف القواعد العسكرية الأمريكية في المنطقة، وإلحاق الضرر بالمجموعات الانفصالية الكردية خلال أيام الحرب المفروضة على إيران من قبل الولايات المتحدة وإسرائيل، وتفاصيل حول قاعدة سرية للجيش الإسرائيلي في عمق الأراضي العراقية خلال معركة رمضان، بالإضافة إلى بعض الذكريات الشيقة عن شخصيات سياسية إيرانية بارزة وقادة محور المقاومة، مثل الشهيد سيد حسن نصر الله، والشهيد الحاج قاسم سليماني، والشهيد علي لاريجاني.
⭐️
"سيتم نشر النسخة الكاملة من هذه المقابلة المرئية قريبًا".</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/81105" target="_blank">📅 19:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
محافظة ذي قار تعلن عن توفير سيارات نقل مجانية للراغبين بالمشاركة في مراسم تشييع السيد علي الخامنئي"رضوان الله عليه" حيث سيكون موعد الانطلاق يوم الثلاثاء الساعة الثانية عشرة بعد منتصف الليل، من أمام مبنى ديوان محافظة ذي قار في شارع الإمام علي (ع)، باتجاه محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/81104" target="_blank">📅 19:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58ab0b0ae.mp4?token=NLJ3dHfNWBq_jR5oqoimBkgd2dpfL0_GrkrUHRfBcMKrO-UcGHdebBPqiXFenTplSjEyGgw69kdtlN_BAZ78OvRWB_4hHAY5851ZElGi8mixMAPi9pmbczVG075-WWeJKygUuyL54L0L576s-xYyveXD1n1iEM_57II4UCh6MFQr2qsHXjcfj9W6AF2eJVMD8CwoqedmRKTLvTREKeh3Wpwvct-gnv8UiFSHfFT0iWzyYMgJYnJgPq80AmozgUjVok1Ale-OBYb_bXihe4jun9a7W-kHX3jK22VkPq6R5cGoVjZJ1GYNmH79eCsoBjHk7olQGpulvJbOtHs9VoucUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58ab0b0ae.mp4?token=NLJ3dHfNWBq_jR5oqoimBkgd2dpfL0_GrkrUHRfBcMKrO-UcGHdebBPqiXFenTplSjEyGgw69kdtlN_BAZ78OvRWB_4hHAY5851ZElGi8mixMAPi9pmbczVG075-WWeJKygUuyL54L0L576s-xYyveXD1n1iEM_57II4UCh6MFQr2qsHXjcfj9W6AF2eJVMD8CwoqedmRKTLvTREKeh3Wpwvct-gnv8UiFSHfFT0iWzyYMgJYnJgPq80AmozgUjVok1Ale-OBYb_bXihe4jun9a7W-kHX3jK22VkPq6R5cGoVjZJ1GYNmH79eCsoBjHk7olQGpulvJbOtHs9VoucUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحزب الديمقراطي الكردستاني يبدأ البحث عن جماعة الهركي لاعتقالهم قبل بدء الحرب بين الطرفين في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/81103" target="_blank">📅 19:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2955c79e.mp4?token=GUKPJqhc3t-rCForsXSLywy-56e8KIE_WZ8Qv0KG6Va5-Z_nC8PFYx51nCd8djyZv_vXB_aSkOFskSLEd7MCI4rpCnjskgFTJECqJHTRr6x-dGeMYu-k52NAPoIcyA7p7ge9GCsLZnS-AIKUXWw6iuPM9PLebYhQETMZaTeyBbbdzUZ-2lMD-5K8-e3V1NMtZnjGzKpSnBWgs56nJwMnu1aUPFPpNnvLAFFIjgNJUpibiIcd9_P98yzPC_gQvWdoEZ6zQrA6XGdpLOCFYibqBpsWcLlhDW7kJQawT9CVqpI9F9TahPhcwCstJ_FdayWBfG5dMaE0brYtkJIKZAIuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2955c79e.mp4?token=GUKPJqhc3t-rCForsXSLywy-56e8KIE_WZ8Qv0KG6Va5-Z_nC8PFYx51nCd8djyZv_vXB_aSkOFskSLEd7MCI4rpCnjskgFTJECqJHTRr6x-dGeMYu-k52NAPoIcyA7p7ge9GCsLZnS-AIKUXWw6iuPM9PLebYhQETMZaTeyBbbdzUZ-2lMD-5K8-e3V1NMtZnjGzKpSnBWgs56nJwMnu1aUPFPpNnvLAFFIjgNJUpibiIcd9_P98yzPC_gQvWdoEZ6zQrA6XGdpLOCFYibqBpsWcLlhDW7kJQawT9CVqpI9F9TahPhcwCstJ_FdayWBfG5dMaE0brYtkJIKZAIuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مقاتلي قبيلة الهركي يتجمعون مدججين بالأسلحة الثقيلة ويقطعون طريق أربيل_الموصل الرئيسي</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/81102" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72be292d0b.mp4?token=vpX2gDtp_aG2dfeVrk3wA1eA_8yvTWMxrJf6tmMyr3r4rOxNNYVwxfrWWXhyfCRd6iXAhhXTIHomgC5BLC_bhbuRdDoh7zI5zWArQJx2pMSL6yugtCwrtv0hNAOEqiJxRtH-7Yq8hJPk_ElbFmP4-Nvt-fTjxpvw7TQLDl8Sx_QNsa6l1-lpQ8_UEsI7TT7K-Rlkf_OkoAGZO3nk5vIaMb7NeMcVgq0CSbT3nbf9S8GrHUpRrVdt61QdSBRfk3-zE9eAu6nlSNcYiLUuW8N56SKJIcqEP7SW3dToohIL95l-zjV6wQjdVaWs4X0gBYJGgnp24e6H2Ysx_yZ0qNxE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72be292d0b.mp4?token=vpX2gDtp_aG2dfeVrk3wA1eA_8yvTWMxrJf6tmMyr3r4rOxNNYVwxfrWWXhyfCRd6iXAhhXTIHomgC5BLC_bhbuRdDoh7zI5zWArQJx2pMSL6yugtCwrtv0hNAOEqiJxRtH-7Yq8hJPk_ElbFmP4-Nvt-fTjxpvw7TQLDl8Sx_QNsa6l1-lpQ8_UEsI7TT7K-Rlkf_OkoAGZO3nk5vIaMb7NeMcVgq0CSbT3nbf9S8GrHUpRrVdt61QdSBRfk3-zE9eAu6nlSNcYiLUuW8N56SKJIcqEP7SW3dToohIL95l-zjV6wQjdVaWs4X0gBYJGgnp24e6H2Ysx_yZ0qNxE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تجمع المئات من مقاتلي قبيلة الحركي أمام منزل شقيق خورشيد حركي في محافظة أربيل شمال العراق مستعدين لمهاجمة مصفاة لاناز ومحطة خباط لتوليد الطاقة.</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/naya_foriraq/81101" target="_blank">📅 19:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv1oAe1-FWXF3NU77Rul9VXCz5ErX7M1ujPB0XDcR9KoCOU082av1EaygDZYknPfbxT54_BM2cELWhpL2KCznVTDUQQE5g2ipC05FWSfbsICaVpVnXQSI7WGGzUEV7pyN2_p2hpEoyaJhbSxoRVmfMQPTiN5aksOb8qxqM9nSdpLF_fVEOdF1tSU_00zUkcLO0Pdi6TTznUaI7bqENPxqgmWjHK9D2kHkTw48ineZ80JRnq55rmGnVmCAINUleBsP9Io9inDnd9MQ99NnSvI25X5GmZXBki1XhEjY67GLaZsnhpwjw6bX9CV7VlzfkQlSpAbrNbs21ZmT2ihIpE9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعيين محسني إيجئي رئيساً للسلطة القضائية بالجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/81100" target="_blank">📅 19:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7984718766.mp4?token=dxaYOM-fySTPnpPEXoPddxI_wx81-gsA0XahQvihibWhJANiwWWvIeNUM2Q0LLp664koT_fpQfzSiLD_VRyL8cBRUs7YP9O9-PWcA5pJLOTPzOnH0iuivdUKSj4eGrd_a-Wx2nWGKmMqhWbg15fv9r2EXu1y6UhcSvrBt6uKV1zOhSnzIOPpf1OygcF0jMJym-jR_O1r1aWwFy1y1Oseorx17upvJ8XAANnOxRQk6q2wHkRmWQS_UWz1WAIjL7YVCCE4l5RVk8v1bCNgiZhWIpEkGXKAGx7Pt3IEexKj6YaY8f0JzWRgnl6gh3BDfz1GQP6J8u7E_YHPdC8cTvbJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7984718766.mp4?token=dxaYOM-fySTPnpPEXoPddxI_wx81-gsA0XahQvihibWhJANiwWWvIeNUM2Q0LLp664koT_fpQfzSiLD_VRyL8cBRUs7YP9O9-PWcA5pJLOTPzOnH0iuivdUKSj4eGrd_a-Wx2nWGKmMqhWbg15fv9r2EXu1y6UhcSvrBt6uKV1zOhSnzIOPpf1OygcF0jMJym-jR_O1r1aWwFy1y1Oseorx17upvJ8XAANnOxRQk6q2wHkRmWQS_UWz1WAIjL7YVCCE4l5RVk8v1bCNgiZhWIpEkGXKAGx7Pt3IEexKj6YaY8f0JzWRgnl6gh3BDfz1GQP6J8u7E_YHPdC8cTvbJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبيلة الهركي تمهل سلطات البرزاني حتى الساعة الثامنة مساء لاطلاق سراح خورشيد الهركي وتهدد بمهاجمة جميع المؤسسات الحكومية وخاصة مصفاتي لانز وكار</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/81099" target="_blank">📅 18:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81098">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
معاريف العبرية: تحذيرات من أن مدينة إيلات في جنوب البلاد قد تكون هدفاً لهجوم بري.</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/81098" target="_blank">📅 18:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
قيادات الحشد الشعبي تجري جولة استطلاعية ميدانية للاطلاع على واقع الطرق والمحاور الرئيسة استعداداً لتشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره) في العراق.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/81097" target="_blank">📅 18:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇵🇸
رئيس مجلس قيادة حركة حماس محمد درويش: كل بند في اتفاقية إسلام آباد هو انتصار لإيران وهزيمة لأمريكا. إيران تمكنت أيضًا، في ساحة الدبلوماسية، من تغيير الموازين لصالح الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/81096" target="_blank">📅 17:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇵🇸
رئيس مجلس قيادة حركة حماس محمد درويش:
كل بند في اتفاقية إسلام آباد هو انتصار لإيران وهزيمة لأمريكا. إيران تمكنت أيضًا، في ساحة الدبلوماسية، من تغيير الموازين لصالح الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/81095" target="_blank">📅 17:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
‏مقتل ما لا يقل عن 14 جندياً مدعوماً من السعودية وأصيب 23 آخرون في هجوم شنته حركة أنصار الله على مواقع في حيس، جنوب الحديدة، تضمن الهجوم نيران القناصة والطائرات المسيرة وقذائف الهاون كما سيطرت الحركة لفترة وجيزة على المواقع.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/81094" target="_blank">📅 17:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/81093" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">البحرية الامريكية تعلن مقتل عناصرها المفقود</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/81092" target="_blank">📅 17:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">البحرية الامريكية تعلن مقتل عناصرها المفقود</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/81091" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/81089" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
لجنة مراسم التشييع:
ستبدأ مراسم تشييع جثمان القائد الشهيد يوم غد في طهران عند الساعة 6:00 صباحًا. يشمل مسار الجنازة شارع دماوند، وساحة الإمام الحسين (عليه السلام)، وشارع انقلاب، وساحة انقلاب، وشارع آزادي، وساحة آزادي، وطريق لشكري السريع.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/81088" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4l6oKRH0N_qCZHXS5LAnO61kMR6Tf5fp8roWLun4pPR647goR-1eFgsKsm6SkGR43EGUEz-Hk8BkOu4M8jeSOOxp4XPIy-h_ozKZczOSzDjI6Q0s2-FDs2uYzPEryzEXx9Tf3CX-GBc0oPipvABviIXdxJA7w-MZDUho8I17wboXtXL4HJSqtfxms8DWg20UJdBjCTvD8YY0NDXcOmaISnBa4Ier-K9tpZVL7xvli2XQeL6RsypPQzB3c-WK-yLpnSGuVOPn0M68LkBd2aDgNpBKAEfvQlD0rhar8nhYZJKkQzqu6xAKrBSqJSfU_XrWBxmSgoQDHB0YyOLnpgr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحن، الشيعة، نعاقب قتلة زعيمنا.
من مصلى الامام الخميني في العاصمة طهران</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81087" target="_blank">📅 17:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">متداول:
قوة من النزاهة تدخل مصفى بيجي وتعتقل ثلاث اشخاص (مهندس منهل ، احمد النامس ، زياد الراوي)</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/81086" target="_blank">📅 17:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
اشتباكات مسلحة في ابي الخصيب ضمن محافظة البصرة جنوبي العراق بين قوة من جهاز الامن الوطني وتاجر مخدرات تسفر عن إصابة 3 منتسبين من الأمن الوطني.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/81085" target="_blank">📅 17:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
رئيس المحكمة العراقية الجنائية:
- نحو 3300 أمر قبض غير منفذ بحق أزلام النظام السابق من المتهمين بجرائم ضد الإنسانية داخل العراق وخارجه
- عدد المحكومين من أزلام النظام السابق بلغ 160 محكوماً بينهم 26 نُفذ بهم حكم الإعدام ونحو 270 مفرجاً عنهم
- حكم الإعدام بحق صدام حسين كان عن قضية الدجيل فقط في حين أن هناك جرائم كثيرة مُرتكبة توقفت الإجراءات بشأنها بعد تنفيذ الحكم
- المتهم سعدون صبري أُدين بقتل الشهيد السيد محمد باقر الصدر
- بعض الاعترافات الواردة ذكرت مسؤولية طاهر جليل الحبوش عن جريمة اغتيال الشهيد السيد محمد محمد صادق الصدر
- صدور حكم الإعدام بحق المتهمين بقتل مقلدي المرجع الشهيد السيد محمد صادق الصدر والمصلين في صلاة الجمعة بمدينة الصدر
- ثبتنا باعترافات المدان عجاج بارتكاب عمليات اغتصاب لنساء ومقابر جماعية
- رئاسة الجمهورية لا تملك صلاحية تعديل أو تخفيف أو إلغاء أحكام الإعدام الصادرة عن المحكمة الجنائية العراقية العليا
- جميع أحكام المحكمة الجنائية العراقية العليا غير مشمولة بقوانين العفو العام
- إجراءات الحجز على أموال المتهمين تتوقف عند وفاة المتهم</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81084" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">متداول
اطلاق سراح معاون مدير مصافي الجنوب منتصر حالوب بعد أيام من اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81083" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يومي الاربعاء والخميس لإتاحة الفرصة أمام الجموع المشاركة في مراسم تشييع جثمان الشهيد القائد سماحة آية الله العظمى السيد علي خامنئي (قدّس الله سرّه)</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81082" target="_blank">📅 16:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=cG7VFLzbS6PrxvIyMJvlsmEOkNiGyOv-mNo-lzq3XX1blF7M2w1C2kcNo-nPr5scWy-UIJLwt__oewOQicPMOCLMlSWeBB-1cGAlu1WoGPxaxwu5nwa2TExLfXdEHqgxwVEIsyLU9s8DrV1uv75q6zbs2KAItS0MClnqh_PXhMbcxFfc-uz97EUTIE4mCAYHhkrWNKT7gBQ-_SIO8UifyOBuB3v0Wt1-wHIw_1Pg8VckRrEjHbP4jNZLa4mKNTk9PsRTy_yFaSK64IokRoTGTHmAsjX9C38BvPRdYh-Ve9PDxhYNeEvkaRhnabQSu3xs6blyTzndYy0LWlAEHk8FFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=cG7VFLzbS6PrxvIyMJvlsmEOkNiGyOv-mNo-lzq3XX1blF7M2w1C2kcNo-nPr5scWy-UIJLwt__oewOQicPMOCLMlSWeBB-1cGAlu1WoGPxaxwu5nwa2TExLfXdEHqgxwVEIsyLU9s8DrV1uv75q6zbs2KAItS0MClnqh_PXhMbcxFfc-uz97EUTIE4mCAYHhkrWNKT7gBQ-_SIO8UifyOBuB3v0Wt1-wHIw_1Pg8VckRrEjHbP4jNZLa4mKNTk9PsRTy_yFaSK64IokRoTGTHmAsjX9C38BvPRdYh-Ve9PDxhYNeEvkaRhnabQSu3xs6blyTzndYy0LWlAEHk8FFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81081" target="_blank">📅 16:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=D9T_ANknpMvf4cbWCZKgeHopNvE6QTDcpfSRD8PlhjGP7J98BgdzQ4OHilroPnZSEjyXyTVt7uZc0D1NLnCSrZKHesFaZyt_aCZ9Vt32tDcH2tIZjsmT6TWNnz6VZcdXSRnhl1sNFfDjzsPT92K55zfBXNR0ffHVpn60yuFu4i52YqvgG55VXm7lduzv4yX1vS-7Qf62OcECwbxKmDTj0A-Bcs_dnW2B-Egz2c3mk6F5-R-j6v2KfkU8XPKu-sLsHlajypA4DbZ3zAryO3arntGOmIX4UVccMNw4l7-osR4-eV2W-ef0EPwpENjlHIQxta49sIScSnOjyl5g-HHkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=D9T_ANknpMvf4cbWCZKgeHopNvE6QTDcpfSRD8PlhjGP7J98BgdzQ4OHilroPnZSEjyXyTVt7uZc0D1NLnCSrZKHesFaZyt_aCZ9Vt32tDcH2tIZjsmT6TWNnz6VZcdXSRnhl1sNFfDjzsPT92K55zfBXNR0ffHVpn60yuFu4i52YqvgG55VXm7lduzv4yX1vS-7Qf62OcECwbxKmDTj0A-Bcs_dnW2B-Egz2c3mk6F5-R-j6v2KfkU8XPKu-sLsHlajypA4DbZ3zAryO3arntGOmIX4UVccMNw4l7-osR4-eV2W-ef0EPwpENjlHIQxta49sIScSnOjyl5g-HHkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81080" target="_blank">📅 16:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🫡
قيادة العمليات المشتركة العراقية: طائرات F-16 العراقية تنفذ ثلاث ضربات جوية ناجحة ودقيقة استهدفت ما تبقى من أوكار ومخابئ العصابات الإرهابية في الحدود الفاصلة بين المركز والإقليم من جهة قضاء الدبس</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/81079" target="_blank">📅 15:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81078" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Tus6fAAo9lgkM1yNMdmqaoO4ycWOQsWgCewsqmgZV8dPDePK2CyZL-wp6PqbUqgkmW4kbPnXEkEb5tw04zN0koNb6aXDI8Pr34pVkrXosI8W3Bd4yX4J0fxcmBtkvHzUVxHS34Zx4RUUWggu58_lIa3NAS9pe7KRoYfoB1AhbMYtxoOsa7_V8y_TzveD0veX4bfNrbNgA9H9IXwkPTpDxtz2yfUeGoTBBN_WIrqu_RfDm5FKMykKQaaVdjO6vNqSEI6ZkY8AbKmua1CHGqbJ3c5mtcjK2JHXKTMr1dCM4bckgGq6oA6uBkD_ElGPu4BLLMzY7Bbir_Z3yBx3Y8Q3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Tus6fAAo9lgkM1yNMdmqaoO4ycWOQsWgCewsqmgZV8dPDePK2CyZL-wp6PqbUqgkmW4kbPnXEkEb5tw04zN0koNb6aXDI8Pr34pVkrXosI8W3Bd4yX4J0fxcmBtkvHzUVxHS34Zx4RUUWggu58_lIa3NAS9pe7KRoYfoB1AhbMYtxoOsa7_V8y_TzveD0veX4bfNrbNgA9H9IXwkPTpDxtz2yfUeGoTBBN_WIrqu_RfDm5FKMykKQaaVdjO6vNqSEI6ZkY8AbKmua1CHGqbJ3c5mtcjK2JHXKTMr1dCM4bckgGq6oA6uBkD_ElGPu4BLLMzY7Bbir_Z3yBx3Y8Q3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اطلاق النار على المتظاهرين ضد تردي الكهرباء في قضاء قلعة صالح ضمن محافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81077" target="_blank">📅 15:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
رئيس اركان جيش العدو:
منطقة البوفور هي منطقة استراتيجية حيوية مليئة ببنية تحتية لحزب الله بتمويل وتوجيه إيرانيين، قامت على مدى عقود ببناء شبكات أنفاق تحت الأرض في هذه المنطقة لتهديد مستوطنات الشمال. يجب على الجيش اللبناني الوفاء بالتزاماته بموجب الاتفاق والعمل على تطهير المنطقة من مسلحي حزب الله.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81075" target="_blank">📅 15:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇾
في اول جلسة له..
ما يسمى بـ"مجلس الشعب السوري" يعلن تأجيل جلسته يوم غد بسبب زيارة ماكرون وعدم قدرة نظام الجولاني على تنظيم الزيارة واقامة الجلسة.
بارعين بس بالتفخيخ
هيج سوالف صعبة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81074" target="_blank">📅 15:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي:
من حق الشعب ان يتساءل: أين كانت النزاهة الحكومية والرقابة المالية والمتابعة البرلمانية من جرائم نفط الشمال التي تجلت اليوم؟ فهناك تقصير واضح.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81073" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81072">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-rK2baRKzXlZpzjZ5_SLbfE4oHm0DE1RxpHLExDncyRFut5SlYMKDcV4zt3hgC8P8SM-2Hq0t7gIK8Cy7fx4HuPlRnEa7_hugJdpUwIzUNmkcr4Yf7x5m_Z_ceozRb8uz6XHUnwvyeXfM3J7RvhgfE5_qQjkxD2W79-KXyoXooC1HUpw7kdf1em3a8smpf0BebHVrMM4AMOKwkoUZwhmHpSI_dOF-aZk0XJ1XwcxP3XUkjO8g4iL8f1g43Fh6ogmEIg75hTO-IUWPQWUmGVuwaeqfqBPJWxJehV2eUnSP_oTZQPOyQ9mZW5jNpO2luSMXOUymwu17jK9wi0rKvz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تقول ان العراق يمتلك امكانيات هائلة وشركاتنا هي من ستطلق عنان هذه الامكانيات.
وبمعنى اخر العب لو اخرب الملعب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81072" target="_blank">📅 14:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
وزارة التعليم العالي والبحث العلمي العراقية توجه بوضع الإمكانات اللوجستية المتاحة لدى الوزارة وتشكيلاتها في خدمة جهود اللجنة العليا المشرفة على مراسم تشييع جثمان قائد الثورة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81071" target="_blank">📅 14:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لحظة وصول جثمان قائد الثورة الشهيد لإقامة صلاة الجنازة.
#قوموا_لله</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81070" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=XN1_DENLQwK2SanUVlqB_JaCK6ZF20adrysDS_Vh-AlvwzqbRVKREjnEOj73opiJmrCJZgiCAheonTs5HBW8NA4cTggeyBaWQ7V27pkBEQxeLLcOI7mw7Yy9f58FpGVUaY6sYRWHxKgxLGOW-2EWf1aKt2jt4t_WxLshk_Cbx6XEqpMNvsi8LI9IT625tPeGqi7fMlA5n9xY8oNh8-eQZYRfYA5YF_adF32_vN7vG3XWu_DruOXETYisP5AiwQeOuPRWZrifmQeVQS5-UyKOKZ6QVsdQMnWKklW2uHMzYfwysdcZMmidIwa6Z1OyYFVz_ROaGCahUTQcwcXm-cGf0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=XN1_DENLQwK2SanUVlqB_JaCK6ZF20adrysDS_Vh-AlvwzqbRVKREjnEOj73opiJmrCJZgiCAheonTs5HBW8NA4cTggeyBaWQ7V27pkBEQxeLLcOI7mw7Yy9f58FpGVUaY6sYRWHxKgxLGOW-2EWf1aKt2jt4t_WxLshk_Cbx6XEqpMNvsi8LI9IT625tPeGqi7fMlA5n9xY8oNh8-eQZYRfYA5YF_adF32_vN7vG3XWu_DruOXETYisP5AiwQeOuPRWZrifmQeVQS5-UyKOKZ6QVsdQMnWKklW2uHMzYfwysdcZMmidIwa6Z1OyYFVz_ROaGCahUTQcwcXm-cGf0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81069" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
مقتل عدد من عناصر عصابات داعsh الإرهابية خلال الضربات الجوية للطيران العراقي في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81068" target="_blank">📅 14:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQssJSbWlyTfEoL1Znzswq1FhUhlBjTIzYKApr2JLlkJoXZ8EW2_muRv3GTBDmizyi1ISDW0LQHFGg4jDtiqYEMKnLvIl8YqJJNmN_9Wvceb8vlvXX6XhAB07bkRhK28eMeHHX8TCkFHFIUgQrOmluHNaYm3Oh3e9NfyNxJ9XU_7RxArUIhEqRTegErok2hLBlhjEh1kjV_VY7NAKnyD13ku9di2p-bK03beMabREYRv5t89GE9FUkbZ7X6V2g3TvL08uArT2ly3pgZblVEMjE8CY9Q4qveB39a3FWQHquzpIxgwgtnZ_arEaI6m73o0R9OmRoQUcUa79c0wEYRAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
اليوم، شهد الشعب الإيراني الإسلامي الأبيّ الذي لا يُقهر، بصوت واحد، لإمامه المجاهد الشهيد قائلاً:
«اللهم إنا لا نعلم منه إلا خيرًا».
ثم نهض الجميع صفًا واحدًا، وهتفوا من أعماق قلوبهم:
«يا لثارات الحسين (عليه السلام)».</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81067" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
‏الدول الـ7 في أوبك+ تقرر زيادة إنتاج النفط 188 ألف برميل يوميا في أغسطس.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81066" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUb5uq3VKpfld7bdOA8gyfSYVYsslHRBF9oFrTTy2y_EQyUIv8J6-LqFzSiHbU2dZ3KVMQIA6bUj3IsHzhS56750oTlaRl2lnTEqY3HJAe-8vxjFlc8jxO3xU1jO23YdkIWt1PpS28MjhLwlbelOAEMB3ghjl1MEWTFuGwhnFTH5unN4SUbE7VKHui6FZ_3ZwDfr0eERzw2qzxfDL1rciUfUtPBUWd9RuxP3J1S41obyUnAE3cIZwAjvxllOH4-ttfQVIGicKr244N0bHr3X_VTwy8KbhI8edjrlxWPkvfDNtfGj4cAm4PFwyLK8nD6Rfw_AkRPbEEMgCLNyeXbYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المجلس الأعلى للأمن القومي الإيراني:
راقبوا إيران خلال هذه الأيام القليلة.
هذه هي إيران التي ظننتُم أنكم تستطيعون إضعافها في غضون أيام قليلة!
هذا البحر المتدفق من الجموع، يرفع الآن شعارين خلال مراسم الوداع والتشييع لقائدهم: المقاومة في وجه الأعداء والانتقام لدم القائد الشهيد لإيران.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81065" target="_blank">📅 13:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالقناة الاعلامية المركزية لتشييع الإمام الخامنئي في العراق</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨روابط_المنصّات_الرسميّة_للجنة_الإعلاميّة⁩_2.pdf</div>
  <div class="tg-doc-extra">172 KB</div>
</div>
<a href="https://t.me/naya_foriraq/81064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">جمهورنا الكريم..
نضع بين أيديكم روابط المنصات الإعلامية الرسمية المعتمدة من قبل اللجنة الإعلامية العليا لمراسم التشييع لمتابعة التغطية والبيانات والمستجدات أولًا بأول</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81064" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a75ce7c26.mp4?token=B0sNF29GlGcFLH8ThwxBZbdQVAUKaTYklu23ky-QTT2SehIF2yEV87qraUVgQAtns0sYEBNUqZ77jsN6ZCaQxvBij_ifAz9v45JDCED_6znF9XTcHbo0OR44k6tvoUkpM1dK9berwRLvBgdlME3mGuUeiqbo-ZNga0KnTomRpxbpeLZUU4TekN_ATIGtstOFwEdw8Z2pAU1Nx15uugBPbUhjHO4vFytBUSONidCReIPe5JtNo9jOgZncOSObZgjOisptdBwY9OowGyzECRZdWnv1we07ZuAIvn3WndsxmJeu-jpmXYaLnzHj7BbDZAbxwHNCZZqnqGA_5Cn2m7B87g10z_wYLkQBw8qx2pWCClAkKvd-dEFkK2xlzLZLfbNQV2OVdBvHaPQWBJ0ovGBo3JYbBH8oDDZyPzfU7vtkGsni5jozKaYKOkeEitipISvEPydeH14BJLw9JubaGgEsKfaWJkJvuRMzz93cGD4k7nr8uBLNo4gso3d4hSskCmiwaxEJNJvWbiBnbobKRYGkFLS2rKAtyQjKv05DKrtybhgj2QS3c6dXE6yI56LxwriN7RBhkQoyzC91dH19SB8U-pS2tQXfVb6cQ_DacTkVMklR5OhlgtU0v_nE1z2uftf19SZN7vDrhNxQzmuOT115GhEnDzquUzZif-KZMEofPNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a75ce7c26.mp4?token=B0sNF29GlGcFLH8ThwxBZbdQVAUKaTYklu23ky-QTT2SehIF2yEV87qraUVgQAtns0sYEBNUqZ77jsN6ZCaQxvBij_ifAz9v45JDCED_6znF9XTcHbo0OR44k6tvoUkpM1dK9berwRLvBgdlME3mGuUeiqbo-ZNga0KnTomRpxbpeLZUU4TekN_ATIGtstOFwEdw8Z2pAU1Nx15uugBPbUhjHO4vFytBUSONidCReIPe5JtNo9jOgZncOSObZgjOisptdBwY9OowGyzECRZdWnv1we07ZuAIvn3WndsxmJeu-jpmXYaLnzHj7BbDZAbxwHNCZZqnqGA_5Cn2m7B87g10z_wYLkQBw8qx2pWCClAkKvd-dEFkK2xlzLZLfbNQV2OVdBvHaPQWBJ0ovGBo3JYbBH8oDDZyPzfU7vtkGsni5jozKaYKOkeEitipISvEPydeH14BJLw9JubaGgEsKfaWJkJvuRMzz93cGD4k7nr8uBLNo4gso3d4hSskCmiwaxEJNJvWbiBnbobKRYGkFLS2rKAtyQjKv05DKrtybhgj2QS3c6dXE6yI56LxwriN7RBhkQoyzC91dH19SB8U-pS2tQXfVb6cQ_DacTkVMklR5OhlgtU0v_nE1z2uftf19SZN7vDrhNxQzmuOT115GhEnDzquUzZif-KZMEofPNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات مسلحة إضافية تنتشر عند مداخل قضاء خبات وبالقرب من منزل خورشيد الهركي بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81063" target="_blank">📅 12:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
الإعلام الأمريكي:
حادث إطلاق نار في نيويورك خلال احتفالات عيد الاستقلال الأمريكي، أسفر عن إصابة ما لا يقل عن 8 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81062" target="_blank">📅 12:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bq8KsDhL5CJ9SeHr9Lo1YhkZTw29JGOLdnyTV8Tcvj-xSktjyEO80t2GO-DRZ0gAMM1E3TCkLrl2HHzCWOyrwVSLjSmPld0yqPBhVzNIuI6OKpH8wxX3nLgbEUSJGa-FmQdtsSElhOQamKnWgPIdt05oy1Ap_TAAvnvc8ZUkcdOCGP7rcR0oTdBmiQ_XvyJjqAVn7erLE46K74DRs5SLpvWwVL8sKee2W6kZJ5monEDEwVxNdntBVtz7MaaODDWbJ0XBOTKbxttvHyEr2L6c3yUoeNh3IBYMV7Fw4AZH6wVAZne5j5WuOaWd1LWZ86W2Yiypl3vJDpV3WNPcY7kELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvUDubqCL0U-9zpWyy296fTn7zyJ3m5YW1T6dXja0dDEed3_Fa88gKcCIPCGwC3pwp6EVxgS2UCi7p7jnJKcn7fiKM5vs7_zfI8ps-ybxdSg6CTl0nP5tHJq6TMqNH5cL2dpp5-h7gDQJHlphoy_4qYVM131t9oOP3bEtmqt9D4lDC6pvj8TQu-fRZkbYVmWlO0UdWtbDFQcoCviN0hziN_xPNrCFhGqPZY5fkLpTw-nb-6C6CMFVzce0-CpXEGNrDWEe79z7ZYg4-cBSeSmjUbeo9o-BFQbGwFB9PFehTrnrIHNeR9syxsaBc2gkZz0taHEHkjACXIrwxoVWq43yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cawCP44W73VZxQ1V2wLM1OX15b5DZsClRbcypWduEO7SXKvgSwYcc94FKKGF4b7IRoWAOO1nztd7T-rJPGyV6HbuKpVgjDq51kfUZvOQc3pWSQyrMNveiCS8h20blVZd6je-C17dpdWrChb4qcqawY1SHSBI_dyoa-8I7z1b0Zaxu8SCYFCNSb-VtW1YtB0meGrkHav6rSAUCxha3feFtAIG808LaPE0xv__69OV2Cm8uOjhfNAjh7KQaybaT48CfjYRQwONMkpYPNbKcLYfW3fGljT3YuDVL-3J33mkRf1oEIfroo1wj_lA97FgtR61os8CghWnMBbDHqaQrSZuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kticemf4C1YOfloNTwxWt0A3O47kTHlLRInm3jbos_M6vvKYwa-PhOolpn_PmrSABd7vjNr6_1EOUUmT7qyDzxonThDKxcCvOBIDsgLXWQhSr21exUmUVVr_GpXyAryNCoKysmne722SnVyEP02yohnCFg2oMw277WYZwdTBDf8NvgI2ureK3Dy92pfdGUJdtAo1oyircIltADGxQkuIdeDiQ9vADybUdS1Jze1W0u_e-OFEyzHKSGtMQtRxkJL_qbQCyzMj-SEMiuUN3D4LWGsvtKeemNPlVvKdmiaEvyJmaMroPCEXY389LH175YDCv4AoQqCTNWJ4M3DxE5ex6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
أضرار كبيرة في منزل "خورشيد هركي" بعد إقتحامه من قبل مسلحين تابعين لحزب الديمقراطي الكردستاني خلال عملية إقتاله وعدد من أبناء عشيرته بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81058" target="_blank">📅 12:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVpfxCzXw1_YLV8sxoPioVdXyLnm8_uR76eSISaAusXtrl0VRslBk7vq9CQwW0esZBUG5anUWKuLVfDmn0UfR5pBF6a3a8ZnHuC43w5PiLZoITaz_PLgYg82u71TgBEUMgrJNXLfdvZirnr2UNmGdKvueEOvXI-aTNPH6dkL7KNr2yH9MztzH8dByYvvpAmE9W4YdUvPeXpu89J0DeOqhYL3UGjG0MMlDmSkR-LBmnQUaAB8aNXnDOLl99_DzF7gyGN2BN2MDBmIkugpsc1Hlgt_YNDv4oYm-OUg-uM4zu9RbWSdKUzSGGQLyB8SsMa2PbYZq5Whm7WNgHQL7vWyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم على سفينة قبالة سواحل الحديدة في اليمن</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81057" target="_blank">📅 12:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوي انفجار قبالة سواحل ميناء الحديدة في اليمن</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81056" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوي انفجار قبالة سواحل ميناء الحديدة في اليمن</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81055" target="_blank">📅 12:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
جهاز مكافحة الإرهاب: استشهاد المقاتل الشهيد الملازم اول (حسن خضير زغير) الذي نال شرف الشهادة دفاعا عن وطننا الغالي اثناء الاشتباكات مع عصابات داعsh الارهابي في محافظة كركوك.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81054" target="_blank">📅 12:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
عقب إستشهاد منتسب في القوات الأمنية.. الطيران الحربي العراقي يقصف مضافات لعصابات داعsh الإرهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81053" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82316eee4.mp4?token=medfkbI_MmtewGbvxt_4rGpz2kfkoxj7uEoOqlmGcKjsjDs9mop79yUyPo3f2HkKY-dFD1lRX9bTYx2Vit1rvBeyJmTMkhMR4eiCjIMLjxxyL_c6bxqMA-rtx_a03JOzGx_KvaQTUJs8IbVk63MVizuZOT1gHA_Uw4IeG2gViGbzIQOVFZ7BQ1ghUPzyivM9qFrJw3DPWZ1doiVY-s-NR5bwU_QikuyTXmDnBSpEiIuujlC1jhNdSlvzOZT3BTk_czvFcyWlZtHE7hkjlYYbipAPNQGcXPI0GjJWUorAN-A9-ZxvBGxB_DvHrxQFKsGE9A6HBBRpI5g52R9Vy37R9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82316eee4.mp4?token=medfkbI_MmtewGbvxt_4rGpz2kfkoxj7uEoOqlmGcKjsjDs9mop79yUyPo3f2HkKY-dFD1lRX9bTYx2Vit1rvBeyJmTMkhMR4eiCjIMLjxxyL_c6bxqMA-rtx_a03JOzGx_KvaQTUJs8IbVk63MVizuZOT1gHA_Uw4IeG2gViGbzIQOVFZ7BQ1ghUPzyivM9qFrJw3DPWZ1doiVY-s-NR5bwU_QikuyTXmDnBSpEiIuujlC1jhNdSlvzOZT3BTk_czvFcyWlZtHE7hkjlYYbipAPNQGcXPI0GjJWUorAN-A9-ZxvBGxB_DvHrxQFKsGE9A6HBBRpI5g52R9Vy37R9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عقب إستشهاد منتسب في القوات الأمنية..
الطيران الحربي العراقي يقصف مضافات لعصابات داعsh الإرهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81052" target="_blank">📅 12:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
زلزال قوي يضرب مقاطعة بستك في غرب محافظة هرمزكان جنوبي إيران.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81051" target="_blank">📅 11:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
أماكن وتفاصيل وسائل النقل المجانية لنقل مُشيعي الإمام الخامنئي من جميع المحافظات إلى النجف الأشرف وكربلاء المقدسة:
محافظة بغداد:
- النهروان
الحجز والاستفسار: 07813838567
- الشعلة – الرحمانية
للتواصل: 07709248650
-الشعب – الحسينية – بوب الشام
الحجز والاستفسار: 07727114505
- بغداد الجديدة – الأمين – المشتل – العبيدي – النهروان – الكرغولية
التسجيل والاستفسار: 07737264563
- الزعفرانية
مكان الانطلاق: قرب جامع الصدرين، مقابل حلويات الحمداني.
موعد الانطلاق: الأربعاء الساعة 10:00 صباحًا.
الوجهة: كربلاء المقدسة.
المتكفل: محمد العسكري.
---
محافظة البصرة:
- قطارات سكك حديد العراق
مكان الانطلاق: محطة قطارات البصرة.
الوجهة: كربلاء المقدسة.
موعد الانطلاق: الثلاثاء 7/7/2026 الساعة 8:30 مساءً.
المتكفل: رضا محمد الهاشمي – مدير سكك المنطقة الجنوبية.
- مكتب النائب أبو تراب التميمي
نقل مجاني من البصرة إلى النجف الأشرف وكربلاء المقدسة.
للاستفسار:
07705500886
07832775556
- تجمع تقاطع المعارض – قرب سنتر مهدي
موعد التجمع: الثلاثاء الساعة 7:00 مساءً.
المتكفل: أبو كيان.
للتسجيل والاستفسار:
07725800010
07801401020
---
محافظة نينوى:
- مدينة الموصل
الحاج أبو رقية: 07740926267
- قضاء تلعفر
السيد بهاء الموسوي: 07718255424
- سهل نينوى
الحاج أبو فاضل: 07704863222
- الموصل – تلعفر
الحجز والاستفسار:
07502906786
07503253470
---
محافظة الديوانية:
- قضاء الحمزة الشرقي: 07853995550
- مدينة الديوانية
الحجز والاستفسار: 07830966317
- الديوانية – الشنافية – السدير – الحمزة
سيد علي: 07828989246
سيد علاء: 07811194705
---
محافظة ديالى:
- خانقين
الحاج أبو رضا: 07701909645
كاك كاروان: 07700921834
- مناطق مختلفة في ديالى
الحجز والاستفسار: 07737400051
---
محافظة المثنى:
منتظر/ 07825516717
كمال / 07822527997
جعفر / 07831445477
امير /  07815574897</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81050" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
محافظة بابل تقرر تعطيل الدوام الرسمي يومي الأربعاء والخميس المقبلين بمناسبة تشييع السيد الشهيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81049" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
سنرد بحزم وقوة على أي خطأ يرتكبه العدو.
نستفيد من فرصة وقف إطلاق النار لتعزيز قدراتنا القتالية ولا نضيع لحظة في سبيل ذلك.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81048" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3893914609.mp4?token=kP5CKOz1C9nvlNsmMwRVRbVSsHBIkRU6TLBk8rgeSNGwz27lJ4Zn6F7F3oBtLjfvg-TjJqwq9Wm4mVADf3H7898jgMQg_3EwK9hpa6uziCxghlWFFkm3sLvHSYEwaohoIdqurLlM-ZYsQvtI7rUW2Cr4wE9miiDMCdzfaEkbH1xlTlW_GeFgmO-GeFJz-drfTrAEhDQaEmpIlf-FMWn63oi3iRmiaQbzKX2gMxotWyGBTggtOJVFhO56H_UQXYrDLkbKt3nXkijy9mFSqm19rtPsO4_ciVbx6hEkVdrTIF56-nQgZ-1kikEsg6jds6JIrAkcT-Q00liKrWCMuwvmM5uM_lyZwSFN9ooJwtsw5-OcEieTRyGiB7-vvtixevGbZqptyCprqHpfAFs80MHj8bZUYVGbYN9gDFZXe-PQSEbUi-ydmZ_clNYm1gsTzne_i8YX_3HfxEPryy8Mn0inMrwBFWXmHhYlrMIZmYfJ_HbwDUCrVuQkLiKZfdYUnQbzRry-vWhGIW7V1kQdcBVU1DT2AruNis-wu_C7zkbpaSfAJNCzmXtxs9Z0ycJTxyzhTVgI9LUy-kn-OFp3l2BAC9MIJe2lvrO_0DSNQSvUg_k5kQ5dSiPBioqaDhup7C0w5E1jg5g_HUFCvvhEx70TZmF3-qgDakOoEEPBBwDO0Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3893914609.mp4?token=kP5CKOz1C9nvlNsmMwRVRbVSsHBIkRU6TLBk8rgeSNGwz27lJ4Zn6F7F3oBtLjfvg-TjJqwq9Wm4mVADf3H7898jgMQg_3EwK9hpa6uziCxghlWFFkm3sLvHSYEwaohoIdqurLlM-ZYsQvtI7rUW2Cr4wE9miiDMCdzfaEkbH1xlTlW_GeFgmO-GeFJz-drfTrAEhDQaEmpIlf-FMWn63oi3iRmiaQbzKX2gMxotWyGBTggtOJVFhO56H_UQXYrDLkbKt3nXkijy9mFSqm19rtPsO4_ciVbx6hEkVdrTIF56-nQgZ-1kikEsg6jds6JIrAkcT-Q00liKrWCMuwvmM5uM_lyZwSFN9ooJwtsw5-OcEieTRyGiB7-vvtixevGbZqptyCprqHpfAFs80MHj8bZUYVGbYN9gDFZXe-PQSEbUi-ydmZ_clNYm1gsTzne_i8YX_3HfxEPryy8Mn0inMrwBFWXmHhYlrMIZmYfJ_HbwDUCrVuQkLiKZfdYUnQbzRry-vWhGIW7V1kQdcBVU1DT2AruNis-wu_C7zkbpaSfAJNCzmXtxs9Z0ycJTxyzhTVgI9LUy-kn-OFp3l2BAC9MIJe2lvrO_0DSNQSvUg_k5kQ5dSiPBioqaDhup7C0w5E1jg5g_HUFCvvhEx70TZmF3-qgDakOoEEPBBwDO0Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لحظة وصول القوات التابعة لحزب الديمقراطي الكردستاني والتي اعتقلت خورشيد هركي وشقيقه وعدد أخر من أبناء عشيرته في قضاء خبات بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81047" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d0ed1436.mp4?token=pNo-3_MmNeIGhl5_bILoH3Y0gSFEDeWpP6eSWfl1Dutg9P_YPYhELh5JouExzBuYBKGQDlMzaqz9cpHJyjPXXKCkFBuD8PQ4u-Y2_uiDTQYECgyH4dWsTZevOZJEL4ouax1QGbYZPcl1698XAcW0ds_1J9QjrMvA7RfJbFfoJejb0V78Wsj5hnOAlPnVWPrmt2pFAHD6tj07dcMXkbmDMfEp-oOjgL9aXeyWHcpBW7PPvd1RXRv-SnZMZXwB0K5YrmHzj6Uv0OBAs_fE2KSkSf2O8_oMc95TDazOBfGbvNfre7tevwzJU_vfRFCeUDIi8UZmkW-dmPvs4Jk3KbyFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d0ed1436.mp4?token=pNo-3_MmNeIGhl5_bILoH3Y0gSFEDeWpP6eSWfl1Dutg9P_YPYhELh5JouExzBuYBKGQDlMzaqz9cpHJyjPXXKCkFBuD8PQ4u-Y2_uiDTQYECgyH4dWsTZevOZJEL4ouax1QGbYZPcl1698XAcW0ds_1J9QjrMvA7RfJbFfoJejb0V78Wsj5hnOAlPnVWPrmt2pFAHD6tj07dcMXkbmDMfEp-oOjgL9aXeyWHcpBW7PPvd1RXRv-SnZMZXwB0K5YrmHzj6Uv0OBAs_fE2KSkSf2O8_oMc95TDazOBfGbvNfre7tevwzJU_vfRFCeUDIi8UZmkW-dmPvs4Jk3KbyFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ساعات من انتهاء صلاة الجنازة على جثمان الإمام الشهيد، لا تزال الحشود الغفيرة تتوافد إلى مصلى الإمام الخميني لتوديع قائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81046" target="_blank">📅 10:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dcfb8b54c.mp4?token=uOT3tHpM8MxAHtivaYSoyB8rNAnMR9Y1rtuQr4trVYkjNTj0l1McLIohEM61ybGAEt1eHEDEt9R6S82nOXhknA1QgozoO1KeW-Xfx3GqVT4cuqDfh6enWSIxxII_LQZAMDNIYjHP4WWLlAQAURzj5j_4fWNxv4f1-jhZjR21sCiSjxKvVsEd4E1eeSYJ_moOqMlWDBkmU-o3d99yJo73ftkOUrgLZz_0ZiFdKXFApE15o-Q_J-Var5Us-nuLPFc_nZdyoqZDjpwqdNgrZ-wuuXw8oSqKZGl1fgxP7URLHXNkoAkv1I-vvhwKPQ3x0PYWtUhKlJ141Xqn5K6yJotugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dcfb8b54c.mp4?token=uOT3tHpM8MxAHtivaYSoyB8rNAnMR9Y1rtuQr4trVYkjNTj0l1McLIohEM61ybGAEt1eHEDEt9R6S82nOXhknA1QgozoO1KeW-Xfx3GqVT4cuqDfh6enWSIxxII_LQZAMDNIYjHP4WWLlAQAURzj5j_4fWNxv4f1-jhZjR21sCiSjxKvVsEd4E1eeSYJ_moOqMlWDBkmU-o3d99yJo73ftkOUrgLZz_0ZiFdKXFApE15o-Q_J-Var5Us-nuLPFc_nZdyoqZDjpwqdNgrZ-wuuXw8oSqKZGl1fgxP7URLHXNkoAkv1I-vvhwKPQ3x0PYWtUhKlJ141Xqn5K6yJotugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هكذا استُقبِل القائد العام للحرس الثوري اللواء "أحمد وحيدي" من قبل الحشود الحاضرة في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81045" target="_blank">📅 10:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ce08a411.mp4?token=KOYjTxjc2SojGDmVVGeGaSF9yn5TMSMGgwf8mulM6wktOvOctP6ItTBXPQLVonVbZ-oiXrdsLsaqPK3RnnjUu50RDYy1fI_CxvsRGWNVsJQOHrfuBJhJD9WfW4pT225eVxcFAxeB6MRYZFn1iHYYBOecgyRQ3C2ddkh6X3nsixMyeRV4l9V527fK5-ngtsdshWBmI_JL9oFEt6ngdJp-sTpLj6O4T8lhmT_SLEBcezF2inUcYj0StYG9uMwOYxK0StPgltxyetPOFOejN2YUOZN_JOc5cjCdgp7h7ec8YeXtWwyqBl4PDIgn_9oBbBuzbahO8n0Oi30PWCLsE-riSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ce08a411.mp4?token=KOYjTxjc2SojGDmVVGeGaSF9yn5TMSMGgwf8mulM6wktOvOctP6ItTBXPQLVonVbZ-oiXrdsLsaqPK3RnnjUu50RDYy1fI_CxvsRGWNVsJQOHrfuBJhJD9WfW4pT225eVxcFAxeB6MRYZFn1iHYYBOecgyRQ3C2ddkh6X3nsixMyeRV4l9V527fK5-ngtsdshWBmI_JL9oFEt6ngdJp-sTpLj6O4T8lhmT_SLEBcezF2inUcYj0StYG9uMwOYxK0StPgltxyetPOFOejN2YUOZN_JOc5cjCdgp7h7ec8YeXtWwyqBl4PDIgn_9oBbBuzbahO8n0Oi30PWCLsE-riSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عشيرة الهركي تعلن الإستنفار والتوجه نحو منزل خورشيد الهركي في قضاء خبات بمحافظة أربيل، عقب إعتقاله من قبل قوات تابعة لحزب الديمقراطي الكردستاني.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81044" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اللواء وحيدي في صفوف المصلين على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81043" target="_blank">📅 10:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197834fec.mp4?token=NQHkcIt_PUbcF-R2bZsen9rv3wwVhmPimY12GSQ0cNMcWweJoDD9ziZr4s7SDWjmmkxwWAiPzp8Dk1brYFDcpO-bXMuNB_-LPvOeGTB61C04VLIurdYw1fY1UYPHGNfDLcCoHH6qGIwoGFTQ1KBlSWH2CLS8k0XLVeCGOkOzpAH0Odhuu_LFu_JanPh2gwHeu2Kka3qFCAIRnbehvf30eCASzXHDlDyjysxC8IKy0GjXYpwTKuyWLIqWyb8m-WUQ74hQ--4OieeM_WZ0wXLNH5TRthQrplqHKcRU69yHbceOTHXebgfmlZ_493jsSX2GKzclv6fiZDtTSVUxJlLdAiJsODk5HfUw-8Prov9fe1NnmTZpijkaU-6PWAxU4-lsdLUdZWPDic7HpjcX7kwMRAo07VeCYCRGWxIhURU70THuXk7gBoV43B5dmCBJY377UBYFLOj8PPgUR9qaCmdsg2yCKkm6pOYK7Agu5mSBoirv9qCS6Bh0jAVQkcOKhYTIp2z3oxzePTj-bnEWpjzP579J5kyAIPy_l0-7UCuMWOmJpVNwcIEm_RfH4H2Haf-T3W_qsgFS65xBlxnw9Z3bA7aq-Al5Jtl_yrG6s1u-8qSVjAAZGWgsCWjRjmYiaJhN_ijHNssHFrPflJ4fMcq0q-axS08KhJlG22astb1pu0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197834fec.mp4?token=NQHkcIt_PUbcF-R2bZsen9rv3wwVhmPimY12GSQ0cNMcWweJoDD9ziZr4s7SDWjmmkxwWAiPzp8Dk1brYFDcpO-bXMuNB_-LPvOeGTB61C04VLIurdYw1fY1UYPHGNfDLcCoHH6qGIwoGFTQ1KBlSWH2CLS8k0XLVeCGOkOzpAH0Odhuu_LFu_JanPh2gwHeu2Kka3qFCAIRnbehvf30eCASzXHDlDyjysxC8IKy0GjXYpwTKuyWLIqWyb8m-WUQ74hQ--4OieeM_WZ0wXLNH5TRthQrplqHKcRU69yHbceOTHXebgfmlZ_493jsSX2GKzclv6fiZDtTSVUxJlLdAiJsODk5HfUw-8Prov9fe1NnmTZpijkaU-6PWAxU4-lsdLUdZWPDic7HpjcX7kwMRAo07VeCYCRGWxIhURU70THuXk7gBoV43B5dmCBJY377UBYFLOj8PPgUR9qaCmdsg2yCKkm6pOYK7Agu5mSBoirv9qCS6Bh0jAVQkcOKhYTIp2z3oxzePTj-bnEWpjzP579J5kyAIPy_l0-7UCuMWOmJpVNwcIEm_RfH4H2Haf-T3W_qsgFS65xBlxnw9Z3bA7aq-Al5Jtl_yrG6s1u-8qSVjAAZGWgsCWjRjmYiaJhN_ijHNssHFrPflJ4fMcq0q-axS08KhJlG22astb1pu0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصلى الإمام الخميني بعد إقامة صلاة الجنازة على الجثمان الطاهر لقائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81042" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قوات مسلحة تابعة لحزب الديمقراطي الكردستاني التابع بمسعود بارزاني تحيط بمنازل عشيرة الهركي في محافظة أربيل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81041" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81040">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انتشار كبير لمكافحة إرهاب إقليم كردستان في محيط منزل خورشيد الهركي بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81040" target="_blank">📅 09:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81039">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قوات تابعة مكافحة إرهاب كردستان العراق تعتقل عدد من أبناء عشيرة الهركي في محافظة أربيل.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81039" target="_blank">📅 08:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81038" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81037" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصلى الإمام الخميني بعد إقامة صلاة الجنازة على الجثمان الطاهر لقائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81036" target="_blank">📅 08:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای پسر فاطمه، تسلیت تسلیت.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81035" target="_blank">📅 08:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf4gYCIHda8ArRu3bGHfPS_o72RRVEj3g4cwt-HJhQvhHYAvMmEYHFK97zgcTRXpI693ZFNS65eyzvGF8vrTja5R2HzN3ddtKmLjSduM_2HmtI29zgEMg07wbtBCsFecdGdB2dn_yFErr10JNNN8DtP_uxQylfZwryn_WGu0jXs0X7J9AVoUrOP_gA_YCEiOz7aQNF83-GXRgZbizecCytJBKoBwhIhrrNma8f8oxFuQBhOeiVxSTRCblkgNjnEvm_gzIdp8XLqUJP3Rup-jcz22LTGUT1Y_4sEMzdQTXnw2somOatuRU10xJw0FnBhmbPwsAJ6DnnO_vZ2AD4KaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يالثارات الحسين</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81034" target="_blank">📅 08:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81033">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللواء وحيدي في صفوف المصلين على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81033" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/81032" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/81031" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=s30CaSFSGj--5WgmTUOK4v0mJWkGaRF3T1eia3aS3hDbxWGO3sSCUY8n-rYQRjAONUoSLQEq7_lG4kyDgNobcNrRF_vxIxvptm03uAMGJ5BZU_dNe0fnrBsqu82ysOST0B1SEyEDhwJafy7J4JmdDwWw41yocfp8ebx_TBHeOPhxVfWoyeBys7XS3XdWiebjvAiEt8MrDar_R0ozrHhhcPUYwYzzuLPbra9-fzRoDcbCwUl3FfmllH3GeKJhI5GQmOM0Q_4iIYXxMga-O587WzfsW5Axn-1e-R1V28BDKBFBXhQIuQ9g-TdXUPXoK_12r_lxv5jmXBiwjvhpnJi2fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=s30CaSFSGj--5WgmTUOK4v0mJWkGaRF3T1eia3aS3hDbxWGO3sSCUY8n-rYQRjAONUoSLQEq7_lG4kyDgNobcNrRF_vxIxvptm03uAMGJ5BZU_dNe0fnrBsqu82ysOST0B1SEyEDhwJafy7J4JmdDwWw41yocfp8ebx_TBHeOPhxVfWoyeBys7XS3XdWiebjvAiEt8MrDar_R0ozrHhhcPUYwYzzuLPbra9-fzRoDcbCwUl3FfmllH3GeKJhI5GQmOM0Q_4iIYXxMga-O587WzfsW5Axn-1e-R1V28BDKBFBXhQIuQ9g-TdXUPXoK_12r_lxv5jmXBiwjvhpnJi2fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/naya_foriraq/81030" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/81029" target="_blank">📅 08:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/81028" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=hLn5LlKSBuk3z2tYSEphp0HNfAaqC__9XMub5-0wHj4c89bTnwMchJOgD5nG-NvYmWuBmZX-QnJCZojmsgdba5LKIUQ3pRzA3ikOu95FLNoCaJVCumu-ilyPa6TTpgdpdhhB_wQeHd_LoSoLThpkEE4uRJ_pI4aSPiOCMeAxh0jcWhAhHPX7jJiw2WJ0hXemTo61kofFtKgkghYOhPIt-WdXsX7X5BTIQqOJOCp2jOTHyJY45rurRL4ae4Neg6hMMhpm7MtkVJEoNVHoCsIw-AUmQB6txgsLiUSQxWgktxI7y6M_kBsaH9d9_k2duLrzhttB5Bkw4oIlnykwYoC_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=hLn5LlKSBuk3z2tYSEphp0HNfAaqC__9XMub5-0wHj4c89bTnwMchJOgD5nG-NvYmWuBmZX-QnJCZojmsgdba5LKIUQ3pRzA3ikOu95FLNoCaJVCumu-ilyPa6TTpgdpdhhB_wQeHd_LoSoLThpkEE4uRJ_pI4aSPiOCMeAxh0jcWhAhHPX7jJiw2WJ0hXemTo61kofFtKgkghYOhPIt-WdXsX7X5BTIQqOJOCp2jOTHyJY45rurRL4ae4Neg6hMMhpm7MtkVJEoNVHoCsIw-AUmQB6txgsLiUSQxWgktxI7y6M_kBsaH9d9_k2duLrzhttB5Bkw4oIlnykwYoC_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/81027" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أداء صلاة الجنازة على جثامين عائلة القائد الشهيد</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/81026" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=SCQzz-imLKO3lB7q_1pqEWTaoNB-mvyeXJiGUvS6hYlE6dlWxd8HdVJBlzvKr0DxZ_tV0_WCEOPdb2SFzfYIFCsqxZC-pDLR3YIhH33TMwODUDLM6FV8YZsi2iz9_3TV1pf8JnwlrmJumJ2chvgvaYDJgimzBabTJX9Li5PPJsyt14_X8GZ_oLgiZYbRXfQQRVKgSU_WarR1kiEteSYH5fEW1RNl1UxY0XAqDbwfOjH5pba_4a8QubeZ11L6kX1YGUvUEqUxvRJ1EpGfJ8DuxQbXG86OmF05Augp5kWh3R880yx7CDQd0oNcdAc89FcDmVpdTN7qNoQ70AMrLxM29Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=SCQzz-imLKO3lB7q_1pqEWTaoNB-mvyeXJiGUvS6hYlE6dlWxd8HdVJBlzvKr0DxZ_tV0_WCEOPdb2SFzfYIFCsqxZC-pDLR3YIhH33TMwODUDLM6FV8YZsi2iz9_3TV1pf8JnwlrmJumJ2chvgvaYDJgimzBabTJX9Li5PPJsyt14_X8GZ_oLgiZYbRXfQQRVKgSU_WarR1kiEteSYH5fEW1RNl1UxY0XAqDbwfOjH5pba_4a8QubeZ11L6kX1YGUvUEqUxvRJ1EpGfJ8DuxQbXG86OmF05Augp5kWh3R880yx7CDQd0oNcdAc89FcDmVpdTN7qNoQ70AMrLxM29Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الآلاف يقيمون الصلاة على الجثامين الطاهرة في مصلى طهران</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/81025" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy_bcOOOK-VqO5snz2nz-afQvZ3_UansfewrfQ_zBiM9O1vtGGMGIaTe88G9dGPgBQ5DorDzQK9y3vVnxZkMx3yBpAOIKuPYjBJGJamrkG70OrQL8ImfK-b44jo9cJhjdT5wo6pIhAv0i0BIDZUyi3wIUIE3a5tHt0shQznIolPi92w0RSg7P1qdC24H-N9tF6vgYslKYdtzTK-qEG4iom7srQX6Ly-aoIlGuBroUPhwLU5yaqBJkchDHmxNQi96Xe1OStGAELUveDDwktI7LMDu1uFRq_Kq-2YrgyzX6s4FWuyTQyI6125Dmvg1oIZxjJAV0ttDm2wx5NKqTBDe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصلاة على جثامين شهداء عائلة الإمام الشهيد</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/81024" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81023" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=GRU5Qpm2U9pZJgN7cgfv2G69iuxg1f12GETcIZ9roWqcx30CTLZAVJDH-dkEJn_5zo1MCWU4tqK9HIElQpIf7345aTSTNRp-4jZfgyuqrJxEhS9Jp4590hDx7DIpAXLGkP5pbdwx4fXOyvhwkFCzacOnvbXaQHtp6CsB4jGWkM_lsPQCKsR2yV70p7c2lHiUUtiaT1WJzkcFGIFchjL1oFJEYiPUnGRPeb3DShHwElVNNE9nIC8bDtrsvl4TDoxiA_1ahe7a4ca5lUXvO93YwgYH6JExbQhxWD54FbekZzLCJbnPjeMBxlGHIXh_rrjiRNEvkqWrjuI-kjOg5wUi8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=GRU5Qpm2U9pZJgN7cgfv2G69iuxg1f12GETcIZ9roWqcx30CTLZAVJDH-dkEJn_5zo1MCWU4tqK9HIElQpIf7345aTSTNRp-4jZfgyuqrJxEhS9Jp4590hDx7DIpAXLGkP5pbdwx4fXOyvhwkFCzacOnvbXaQHtp6CsB4jGWkM_lsPQCKsR2yV70p7c2lHiUUtiaT1WJzkcFGIFchjL1oFJEYiPUnGRPeb3DShHwElVNNE9nIC8bDtrsvl4TDoxiA_1ahe7a4ca5lUXvO93YwgYH6JExbQhxWD54FbekZzLCJbnPjeMBxlGHIXh_rrjiRNEvkqWrjuI-kjOg5wUi8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/81022" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=IT3mOPojxbrK9f4d6kvydL6jQyxSfvcTPW12rbZYaZWkCQePtiO_4FIgwnFIjR-V18HuRvfXOfq6J8utOhVNoJfZRyNLRsbW1ijtrTry8R8-NM0UIcgACebDGmCTu5MYzRXkiXUI7pvAU0poWfgUosG8DGDTLG4TW28t6s39nOGF_5kgqDKRYJTXhooCWxtQkDgA0vokG-ISDbZIZHNjr4NIIqQBrLTkksdcwU3Hm1qKajftO4zr7hH1BEIRk7fzSNz45bN1wtncx7LkUCRDs-RRAL1PTNEeUht8WIdFhjLrySZyJP9bFCXs3HvLCbsu41qUKYBDBaoyR6qrvlusEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=IT3mOPojxbrK9f4d6kvydL6jQyxSfvcTPW12rbZYaZWkCQePtiO_4FIgwnFIjR-V18HuRvfXOfq6J8utOhVNoJfZRyNLRsbW1ijtrTry8R8-NM0UIcgACebDGmCTu5MYzRXkiXUI7pvAU0poWfgUosG8DGDTLG4TW28t6s39nOGF_5kgqDKRYJTXhooCWxtQkDgA0vokG-ISDbZIZHNjr4NIIqQBrLTkksdcwU3Hm1qKajftO4zr7hH1BEIRk7fzSNz45bN1wtncx7LkUCRDs-RRAL1PTNEeUht8WIdFhjLrySZyJP9bFCXs3HvLCbsu41qUKYBDBaoyR6qrvlusEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الصلاة على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/81021" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNleMPpZPbr0SyOf5LhyIP_qWvfC2lw9I4XNcMILNZJ59WN90OmWYhOgJZHJCl4of0DPwu_AngNfkRq67vsx6iPzG-rIYsShwkwLlrVryOuRn9WBkscKmBMFrD1VYVe8Atpfr-2Mz7SVDbc7jjtvQyS1p0QYgX75ByYrEYiq8P8JAidoKXQds1le7fHUv01cLXlwmoeTpbixmKaD95sNRKt7Zw7-alUX1XGdovBcEhCblh1iWOPdx1fEQS3WGyc_x30e93nQozzL110CYDu679hLXv_kW6NmnESee1fkDXa0eX9A0m7OQlEvVa-mL6yXRAUt9KU1QVoLfX38iv6o1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء الصلاة على جثمان الإمام الشهيد</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/81020" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رفع نداء "الصلاة الصلاة" على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/81019" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=PEUIMD9PwW0SxN8BTP_OTFef6iupN3bdSKeLKTB1jIg7GEJYA9TIBt4sKbgqbSQ4Sn9JXkQWBI9bIpQyxpk81O8vKjoEs9XKBB5XsOErMd_efKl114iskd4aUmgfh_zcsNHEBg9XpyglzFI-BKEcREM9ZY8CdJ4zdrdDdORa8LSbDrmZhZYNtyzvAsI8O8Pi_biBjYyksEvicpm8dtXV0G6jOMLgs4Xu40rLvkZXUTW0ucecNiqszKvpHTp6Oyi_xcAB_eWinA7CxCQa-81WKIWwdA5VqWdXFfOcZiFqxtluBeAgDe6glKMzhpNGvbHgTp6wMWIhhZQXJGztmtTArg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=PEUIMD9PwW0SxN8BTP_OTFef6iupN3bdSKeLKTB1jIg7GEJYA9TIBt4sKbgqbSQ4Sn9JXkQWBI9bIpQyxpk81O8vKjoEs9XKBB5XsOErMd_efKl114iskd4aUmgfh_zcsNHEBg9XpyglzFI-BKEcREM9ZY8CdJ4zdrdDdORa8LSbDrmZhZYNtyzvAsI8O8Pi_biBjYyksEvicpm8dtXV0G6jOMLgs4Xu40rLvkZXUTW0ucecNiqszKvpHTp6Oyi_xcAB_eWinA7CxCQa-81WKIWwdA5VqWdXFfOcZiFqxtluBeAgDe6glKMzhpNGvbHgTp6wMWIhhZQXJGztmtTArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بأي ذنب قتلت</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/81018" target="_blank">📅 08:00 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
