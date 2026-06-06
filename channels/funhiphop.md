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
<img src="https://cdn4.telesco.pe/file/uIm0T3pqXlX0hc23FIrGPxlJLeKuXvfe0ignZCdQokZy-GW2J21jvP_-YP7Vmlj4KX_iHGG1AtCyx3a0qc78GVEraDJ-DVxCYSWquFSn-LBfXfiTdjrSulepeghzHEB5SYSXOHxQukzQLpZzMoBlursnDpxAzpbHiVicUnc2yvuJ0JHJcQ6FSQfrwrJvz8hT77LdyAt4Qx0Lq8aVdwXp2dXPIFDo5XY3Bn6N94meXlYDHlOHzIgFS2IleA5F8YkD7aa17E82rt-WUk__1gpyS7ANVMMt_jG_W2y_6jqGS2l5DjmITIDuMOfm2pTvPiHwog3eoUGWk6CVLc9ZAYFK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 20:31:30</div>
<hr>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خواستم این رو برسونم که اتفاقات خوبی قرار نیست بیوفته
هرچی جک و جنده که تو خارج بودن دارن برمیگردن ایران و طرفدار حکومت میشن
جدای اینا بعضی افراد هم که حکم های سنگینی هم داشتن دارن به بهونه برگشت به آغوش باز ج.ا دارن برمیگردن به ایران
بنظر من همه این داستانا یه تله هست برای کشوندن افراد بزرگتری به ایران برای محاکمشون
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/funhiphop/77006" target="_blank">📅 20:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxZA7Mrhyva4v5ei_kPnAVuehIo75FRheCB2xddhnpsaU_Ae_277iELAIwwx-Ml5O3JKAfSCCynHu-Kvc6Sj-JjWXkCrgP4kJiSGtWUUgJtHd_9asvm8a4mUK3VQC3PGvfKhwMm_pgtXa-asNsLbVJQhGzn9ZuQJlZUHF8pw-Q_MpurkJ0PqbN_eIl4K-2T8NwieZ_645N9OHSCH1PkI9Z5HYWtr72B8KHuefMt63J9WmQ2hjO2HcA1lU_7aeGB31sSRQmzxl-cie7YgZGp5iWjza_4HzKhAOLgQMrvQO1357JiBLz3PtNyNve5NU1jrh489THAsLXXASGkZUP0uFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیکا فلاحی</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/77005" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باور میکنید comatozze سالم تر از نیکا فلاحیه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/funhiphop/77004" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHE3AM</strong></div>
<div class="tg-text">مرسلی حرکت کن مادر جنده</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/funhiphop/77003" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IquPkXqnxeThmd387WwOZ7Unnl3jTh8LT6-Xcr56F1u0KX7licK4onftAfe_mC7nr2ol0j9w93FBPNZ0x14OGmhGT0y-P2I8gm7fxv6KGwGcQyHEte9r4u1CBBSGVA8G4tYDOh3JqS2Zye26EEN6mCPy9gNdUJ_jZR1gSEWegxNKscVA8EZrFgsOc9JOrE_ponltqR_68v7Cf7Kh6k_jXp-wSIUJOv-bd-sJQ3vls6oYJpfO6-bL-UpiQzYDBw9K93yIf-2QaHYE8995QfRNt3astJnWr2YaOcQIVH8hSB1x4hgg_OLxM4843V8sVI3sSYA5v1jBNmNzq2AML1bC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فرداست دنیا جهانبخت هم برگرده ایران
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/funhiphop/77002" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">من بین ویلسون و خلسه "و" رو انتخاب میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/funhiphop/77001" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی، حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249 تومن
🔥
❤️
لینک ربات
👈
…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/77000" target="_blank">📅 20:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZzZtb8NEzvFnZvYGE-YVOX7QUp5KNbTMJtS2puFxK0sOUD7G8lGh1QAHdS_U9Xr0hx9ShN1u4LgInc95L1THJudhPF6b5vVonfj9c88hYzqXYdtZehOKndPkK3MurHGeEBZGIAK17wAMtgcHyUAz6DUZxPpsFMLEXXRaJ_eJxv8JRdcYp28z3wXvHvm1dgyUkYtN2U5KD2R5__YyQpB4jvGFqdnycRQsAklss202Nggt4q8KEQBwc30XqZUbcX3froj7pPCRlDs0HT1ba1TinR9_xZT6ThmhU_yi1s9n6TuhKf1wHtaJdGrUoCPTLRrWycibkEpy3jqdWmqg61h6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی،
حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه
سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249
تومن
🔥
❤️
لینک ربات
👈
@Window_VPN_bot
💻
به همرا پشتیبانی قدرتمند WINDOW VPN  تا یک لحظه هم قطع نشی
😉
@window_community
:کانال تلگرام
🛫
پشتیبانی:
@WINDOW_SUPPORT</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/76999" target="_blank">📅 20:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کامنتا بنویسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/76998" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بانو آنا د آرماس ببینید.  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/76997" target="_blank">📅 18:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpLyBrt3gpXhUd-XfKQBjRwthIax1XfDIG3iV3cfDfCZDCXIg7qOJH3Dz2HIdT8XbTcrb8hiejY46Ye398NpfkoMy0tK1WPYN8Gh4ZRVbwvSXtvusglhB67i2w0Uqp1MhMxuBk5khUbhqlBhM7vUcgnKecB2-0HQquyFhy02K4u6I6Irq8OBbY9Y2diSROyFCc9GK3sib2UWvqJq8YQM_KmAHewUjsxtrnhPtVwozEFLfhUrNrQK6WHaOyVZiEQRUHnCikzK99tbj3HH6HV_vsvtjkNm-UY6UC6y7jdpMBi-L8xDdWvn9QpSTYsJxtxCC1MDk4U515xGAoNsXCNjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txl2FoaZUfHcYfuZh8SIYALVLgn1TnO1i_cIw6_oY3j5wf6l5fUgSt7ogNqluaRq7e-fRrJ63AMK3SWjXQRAzFGzrAVE8cf5rKWSuDQIBySPe599_LnZypCiX3sjzLFttEsJKg2FbVAzt1F1hqKtv2HW-9wIfBkc2Sds0geq3Hi1z5mgljWP1fsB9YwTr1QpglW0bh029wLrg0VRPB81Beusz1FpkJyjjeDoNecDJnhTiiEG9zzs_Ehl02eVMNdbZpQsZSho9WhJr05pNIqphpxpn_L4Y0WDa9xjLWu6bssf0TF4F1FUtW-1lUzy84_yWQXIFcKI2OITGSdLQvl-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjRQBdPKjSt3PrfUPO0VPgC2W1xQdlmnBYiXDVrktO4E34qVhxCq9l5fWZcBOBhGgF37P5xLyfoA2YxvUq6SM1nt9su9bZEyj4qCRGLKc5RdL0FKuXx5rCHe4fAshBDxy52Ydwdgh6jYxAbjK_HTdQWQyjPU4CwJy0rJpQhby1wQpStAva6zKoNDPkDKQgA_SB0bivq-SlcNMWOp9fsGu7n358Viw1GrtTsnyvpcfcqITbQA5JPqQgK1zTcmmulE0VVBTv3GLDTZKqkz684NWuL93V9OVdx_fadRwGNDLD5Val4OJjrbE2foxjMq_8Ra49-BJeq1k5h0A4kVtK4vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNhhVsQ_x3HfV_QJFJHZoJuQjzF4V_B5gEQ-Ge-xac3IpUOCvNTD9VQxqlV0lr4rt3KtEyR5vr2GUWfKxplP4IoDMTW8Asgtkcx7TDGGPFvBESQEVOSLO7NVzpALc4n4e49-0X6B58y6VL_TiWlP7uzWEPM9BM1B-pVAJ5orOF4kKEGKuQ3P3hhUkKOrlFEDsFjXlev-g5sHG2OizPv5thlr3mW7J_Ys3KmTc5QwgX05RDwl4fUkWKmIe-BT_F4TZeJCMlVLg260UB7LUroRW7fRS8OLN41T9emcPxWNSlos2c5GQncCewe7HZTRuGamQbbIVr4LDVZd-4PZlwIzBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو آنا د آرماس ببینید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/76993" target="_blank">📅 17:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OctgiX7yFvH6uGokFZFA3ZwdKfMSWo0QPTviGLTkzHjagUfH7OGxiktwKtP22Gx2xrqQr33CrChNKCFj1ByKIIBMFgFOBWZGgNDFlMF34E8HCUGHaBs7ZGeONo5xnTR5aA7jijRckFhzKpC-MhacvhgNeN2XUMYPFYOQaq1LsfPcrnc-cfSwmXh0kIMpD2hFb8EqC7kvgyeS0swSTiamicHbXSx49MpjTcFLnS8hfHRK1kN93jh21Mcq5xF-0CqQlYUjNqcf3BuL7hxWe_BRUoe_b2fkojuWq_4QBU7uXRm_LBoVowqIaaiByAP1JTLoN6r_W6ChT9Z6bbO0eDUX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای ممبرای ۱۵ سالمون؛ اسکین وینیسیوس جونیور به بازی فورتنایت اضافه شد، برید عشق کنید
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/76992" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/funhiphop/76991" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex7ZTRIEDMTVcVZHoDi5f6FAUf8XHk9UD3dFrV7RPXxtcCs6dJWVrcsqyJROcVHSsWoYGiGo4gqOETzDoaJ_MsBSVrsQswoD8zGABvG3WMsI5aA_w4hMlcI6WUnqJBYPnR_LRSUsW2EuiDt4Wrt0qV851acWI1QQJqieVMv807931zVESpaQxKDfdgCeFHelUuW2QkKDUl9PLo3azCaC66GUguoj7Z63zrixzMZ5ex12pg8HX3wJJWSt7VSsOiCpHZnymrLWqmt6yhEAHJckuBgaFX1Wfo-O2vPNCPsZmF74f2PTKefSC0zqqZ91SBz7JGWuB3C7KwyE6jY9sH0ioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g16
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/76990" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ داخلی پارت 2
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/funhiphop/76989" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خلسه هم آدم جالبیه، به ویلسون میرینه میگه وصلی، بعد همزمان با جی‌جی هنوز رفیقه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/76988" target="_blank">📅 17:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جمهوری اسلامی پاکستان ۲۰ هزار نیروی سرکوبگر به مناطق آزاد جامو و کشمیر جهت سرکوب معترضین ارسال کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/76987" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJIdSHZUeU9ab6zm2c0hLKpLq6XU35o3R3CvdMQhQgZta4g0WH_s6Cv0JBcEbn5n3tUk-NmH_wVaJq9QAqqjXOh2BQp-WxkZQzDIaaqyMnbQfb0O7X4iSjObe4R3NimuNwrocYaiWiGhQ9cYs5PaImlD_TEF_ORKb9WJRfua2TqMwFsYM21iYbh0yp6ONQyzk1NOP42WWuw5bJEQTdmXpQ_0IViv5QcGU1FuDLKox_A8wHND4AFuf-74tfz1UM48RYJNKqT16gXsGXsT7QPs0dnvO5KD7gFSOykjcFu6TaO3VYVQKUtLbbdHdsgiCMRhVHpL-QrzhlNiJp3C61_XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز سلام و عرض ادب میخوام یه ذره بی ادب شم تو این ویدیو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/76986" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">او اینقدر بزرگ و قهرمان بود که حتی دشمن خونی او یعنی دونالد ترامپ
اورا "سان آف اِ بیچ" یعنی خورشید ساحل به معنی بینهایت و قدرتمند خطاب میکرد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/76985" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iR96A7GLvDDg3KgvHwDbdGELlRb35AvGc-09ptlpMkxZg9VEdXfa4M8GP5tclz40Z1zNJeNBqcguCPl9TkYmsyByq3_wS1zU4ZR0mQwGjIu02XvznH3BsJNcmDWuLuNZ42ZADDO5fSaA8kaSZzjz9_zij8Q1kfq3TGfwDzgUJdPJK74TSwlGrcaQsFpFPGLzZaDbAvZNHu--F3mpCEd5aUKheRqhGtkosmiePsBE3Sl-YOAcFGZnXfTRVdJzbuSVX2uGZ3dCxCIIwQDpcFu_f4GZZPpwWyvEp-P4AFLA2mc-Cgs47RoAP6ips005AHay_Si0fjxOy6c9sJi3YVShsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX3sQ-nnCA-v9c65q2FJ66HPC8gsWDnIqKR3EB75KJCcFcApYsxB-ORbkVu2_3BN-hrjQRuVF-HQ9HpguAB14939NJlrJudvlCxDyumEr3iZJvapUsLns8py7yXsWOUL6YTwNSXHo7FIiRyWEpzp012zmA5a2ceUdX2KN0t_JnwFpRb4OlHJAXFudmciYjfYKKcfI2Jy3gQSYoCxOgArgwHzDD2XPCiz7IWab1YyCgVFFzKH_Beh-F8GBNAYmYkaDk66GSd2co9BzUTQ2ITCRkhuG9za9nV7qakNwQv4tW16J1YcXz4lhfH3oQs8gW5UCffY9zHwbjXNg4X_sHhPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان این وسط بازی نبودا، خیلی واضح اونوری بود</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76978" target="_blank">📅 14:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">استوری جدید امیرحسین قیاسی  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76977" target="_blank">📅 14:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIuNraQ73HRa0MMt3SPXG-7YQG_Orfmd3MOROtadgpKq8j5zKx15_A4yHGVyDDre0WImmMVb7v7-Nb8TrrYL9G7A5uz6_rxqDEOIlE6otjVOnS8okmUtbHrfVoPcgBQrAUMVDlNxk8-TA8q0eVt74jUzEKoXd-HWxZWstxNq3kpzFQQGNBlnfu6ODwHKUArY9he_fHm3wDD62Tg7SYCW3N1KbFeaNCRqrzL2wmRmluAAONRpwTo_vkLHNFYGCexKJ9AaTCyU-R2R9rim5JKAtf2QVT8lm72M0AryRVsgAo5FyUhznri_5dqty3s0RgPBjuD3yj2XYdOoe_X198WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAbxlFmyi3kMk_LqGw7DapCxQ_5w37J4KI6C1wes307BubjZNiqxT732-OK5umVWP1x3pUs8X8sxAwba1hwLoloxMRNDe8wTFBoRDfx453BHaltIlp8egvCIyj7ZbK_WOySFPtrnAqbjEHBE-ssZV8XOKdCxq2cKtvNXbaWhKp1PFB2p3xufvZXWHZynmQmckrHe_oYWKmX9miBktjr0diMg4K3AHeiVk3NSbrRJsTwF_lzm1aYVw5iNrT9o44EzltJKr9x4BsvsZvFmHxvwj0gRs1-O0Js_mUYKksXocFhNmF1UyGYmKRZlnoQ0gLQhZM5JW3m8pIXuQZbxtjs4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcSb3EfnZWVTT12e2PtZZ3sPesecjC7XJwCCQlKsOY2T5ttGNXfWlX4L-8yupUfhDo_Oz_zt8eDbz1nu8zPaRC-L758HBKuVfYe1Z6Xj5_ot_-aDHrM0iFEZhMAutnEw_3pTEucWNoqVcx2EMy1A85X7BpbDvtBsufaIoMPHnZWHeia4iXrHmNnkmut2c0k9CXzno47io81w7J031neTmGVA1Dx5GGACb6qty7qKgcSnq5kOhXESOFmvjlJlZuvIS-UCocmwHJKMDSQ9W7M59yG6AoV-jt2VlJ26O0F78H8fNXVebC2XVguq3C6igcMJOk5GX07MIdhbTE-pX7FTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncg57xqyRinV5QNwYA0cedu92e0ZD2ZBPEdExLOyHB5pRSLBHfFOFdPtvTWS2MW87PKDm2SvW7TLlPnwN5lGQFyLJMhY1huaxx-Y4vHw7Qdm2yswR2NKtgylzwwrbux-vR2OTFBFTYiEj7sq--eLRAdSCk4e5zO0pYk6pGLw9--bRhpWK_WLqUVdm_wudj5XcPeqZZKldcU0y05Qy27o0yB0CF-M9U6IWKZNN9widQzOErz5Zs9D3XXbYSqPHM0i0om1bbKPFAHWA_QSglcKqleYve5p2eLLB4fRFedV2Kvp6f6jkQwS9H9eLRLoJXToBVJrz731ZR5ISeUMjusFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iON55MiHP0KTlMLJMtuYGlVyX0tXhsLxDvXbJ5enG3ZC6nsQQuodyXCfWwoAvQykcWFu_is4aZ2pLJ4ew3PXhq2hVwZZRU0DcBcz11H2H-aGApDl3jR7pt2fFwvv_YrL-tWbm51ZRsPoo-S2dqjMFE5nP1rkJZhqBNrIcDYWTgiPtuXIhKrsHuQmGPrjf8aNffxDrdJ5VncSvczjkTGs_nDzzwpPJEStvD78--SGqzKPdWsT68ITSwFwP__VE0_qI2XLHzFEjW7O2Hm_ddyO-CjJnZZgPF6mSmxQX57SUILhVnYhNfigb_SeXxTWUTkREEc_hX1Qy0F6RNbsC6BPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwhnzduc8t4e2zmU-Wq2DdpdtqilwiOwMnpnVJLAV7YKIowSAwbUTFA1dp2kUyZkSpBJAXUizH1Ge1EM_ZyGhjEjUXHuVrCGBW1bLfzqVKA-CeWKOh-2-3MrbG4zh9Uehwm7GjixsqB6hl04U2PXdnVrAvuadnFEN6A_K1-rm1W4cnoqbj5yRU_Tw96fXZkM81rIPp5wVe9IDd-klLjIaUrdfM6gDXqHZ3TNPPnZGahjMUwa4HpWkiVBM8BEXRxZxl2cQRt6Bacb2jvQGXlo4hQokee6t5IuwCAwFZHy5HMz3Qrdhkrsmvw-prEdhU2cyK4GffLFcQF7LhfmF1wQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpK8isyomUSf9HDtqeLF-YESUsSjOJ5Sf5u6PqMoO2X-NAw4FKmjdrQhM7sf-UHneZOBFsG-oJAk1UQslMrrpcctnZa-AtqaGJsXJB1eTipH94XeoybQvVjH8RzMCOeMb9rttt4e3lz8uuuad-nChmHodCjE31N9CBn6G9qWQQjTxe4Myr_I07RZk7HKIfVcpN5XtPmBqK6YvINETeI75UJNtWWEkMY2fVJZt1q29n_2bvSXzt1OwLO90HK6Gz8lgacDT8Fnqf8eKhdlBCXf50W16jKHmwbkjf-sziPRRi666mzpYhjItgaALEsiSmy60SBCkaR1cloPt1OYTxVRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RTogO0CIabb9nOzRrlrubxcJ7B72oy3TyPEmNCLhMaJjZsjmGyEORz7-aqMaoGns40z70tSGuRZKStR0j86aI870cCF4rmvjejY1ulcCwYtSdECEFIHTpnP88LnhZID5k9Znoz2Noz6q6wWc6E3Kc7pdBIl1YPwVGHvsN7Uj3_h_MNxc3p5n5pl7CvQu-ivhQI6GJ9sxEAL5bZdjFJsKzfOnGttYimaCMAuvU1GCjYikrACbVkXT2J6xjmxtyrTJcL5LwjubkHuCV_qjAb0b-K3RsQFDHbvNj_ro6s8zfsrytyprusxDHs68eEsUzWSLE2Ez9g4pgnp3-UNYGflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فنای اسپرز بیایید بالا میخوام بخندم بهتون</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76954" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76953" target="_blank">📅 11:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0fllZ3RCduHURYfk_OOcQvD49kXG4DQwhM1pTOewbdrmn4GbMDMw7gWcLQIbXgrDpZ9xLtHXIM8sRzE_Fxq6u-M3dc807x82bRTXsgy22i2OVuY8HPKQzavLBAoD4WvxFaHZ3SGMP_qt6pRRgauA7fY0O6Yqs1brr7VB2zAF3zEY1UPJOcAYsnyDPvDQVh9bUGO2g-_nf7R9foNNClN6DXBfhkr500EqTi9WibJ03y2pfrAOj8PfNb3Q_nVQjkGIbWInmIoi0qriRHKdR4YGvXeq-2_UraNtEHn4qVqdgv0SY93pD6beC7f0E91GLCQkF4ENj3k3UcRAEaBBvVJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم سریال جدید اسپایدر نوآر با بازی نیکولاس کیج رو حتما ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76952" target="_blank">📅 10:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شایعه شده که خولیان آلوارز رباط داده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76951" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9mqgIpdPXEit9T7VP4wY183Vw0w18U0DN1tc_7uDQqvLQ_66kigH0oXrD9IExr9IpEGmYCtWJU1rqKLFeUnFq_W7xKt4kdsrHqJNjATh8olat13atCx2lmeRRB4YL1-y-tTv4kY6jbwVEhDWXompwFMkRz3OSXRphsvjGCBFxkJ1G0NkpBMSfV4RM0wt4cdrAd2QxLvp94FnqiQISRrgHG0vO8LooFcN-mIAkIvzT-n-xLDf2AEdvVK4wswuQH2fiCEFCzurEUOfhNHrwawyWIOMlNPeBHX6DV0QJv_4pZIR8BVL8_kdeSX8Evgfw7kQg4hn3P07hnFeHJIEaZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو : رک و پوست کنده بهتون بگم، ناصر کیرشم دست پرز نمیده چه برسه به ویتینیا و نوس، پرز رفته دنبال جذب اولیسه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76950" target="_blank">📅 09:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbS4mauxdHn8mp0hQoANhDPRo6gXt9C21CZ59lLaM2w75zLRb2bRthvPhebAydLKYADbQ28NttUQqeLm9ZnE8t1m1Dy2moU2TE5u2y7mipgloe26MfuPIjzaollPUW2HnLFvAt1SJAGsG_0eRag1gRjnsJvBDHM5kjnkIuuTY9fqWyQns4zY4YB_Ph2zSA3Rfl8hrqMmp-TJOi9wzJ9eOpEOrSZM4f7QmvNwcb_WFjATmxuU8ZLexBGj9_cPKuXcu60TmasYDPCSp7vlqsvGYEosemSnQnZgkD0YJagA43ZF2n7LxAwh6JCWRH-P3S_ZsFCNkbMbj_AOatA9AONZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI82lzNuME284R2oLHsSUEeo76BoSxUhazGvlhZdFVEOLzzIGeiq1-X02lmG22yniZ7fkZOphgiFkh7YYUs_eUlClEgo07HoJqcgKkytBLRY7EOxo5IPQy2skQG9MMH6y_fV1gkNA50m4m-e7W_tQ5mdJJtYn_da3S9cFvnA0PaP2HhN8UIWSz5UyQM3qD0gY0l_FpTb55_tvvigCW26aHKAl0fqiXkIyPKZE4osVhJewqdfLhAxv2jEASDh2Xa9MR_fqBfRNM4rfKPJT0SfKIgT-uHBfubE-rQD7v4ApzpFM9lQj25nxtkGWiLrs-8rBgQ1RdngwZvk8Nq9AH1Lpg.jpg" alt="photo" loading="lazy"/></div>
</div>
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
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76948" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6cwuq6q2ifRBedJk2QRvE_kowZPzlTc6C-3poEGUI8C9HO6ie-rJaRrBe1ywkMbhjJUNdxUB7GMgqFtiVhllhKU33Zg-CGyATYiRDsGK5-V8UIlppM-D7PbyaNulCMKXY5OYgyeiCDezV0TcgnMn4BUODh5G_AvV5ersV5Nbozd6kuv4zZrE-AUB5-69FzCLbhv7Iu3UWvVkJgEWX32jR1NkllUrrek0JSUq7PTFepF988cukiRT2VsPeovccOJdJHbrnVOd6hANAkowaevqxiInf0iENLB48HSVHNXvP79D9A79L4_CqpnPKDY7xV96UczTfTMqTwsSqPKgR14Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
R16
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76947" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روابط عمومی کل سپاه :
بسم الله القاصم الجبارین
فمن اعتدا علیکم فاعتدوا علیه بمثل معتدی علیکم
ساعت ۰۱.۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مقرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت دو، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76946" target="_blank">📅 07:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76945" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76944" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMZaNXullTHzjyt6xBfNpzj4cFvUZdQRl2pegyFoBU85SLT64WvUGFq0YtTU_NCdxgSDJZQerQ6agAS4iW-RY8muclGKwVb_NB-oOmRvrW3ph6Z7yBKjtBQAEeP2TpzVYqQ0qTNlC3jBuyZczXcetz88c7Ci6cUVYPt17CwJxe9TJrK5ULWPNGjgEa5PncWAc8vBijiIea8QAl8mGRns5YKabhkcMOE7UFrATNrDe4Ejs6HUxl066OtFovjlpmYgoSONYnIe_MbqOPSWdqmYjVXuVzJw3DyK-xp0WrOuVrv2tpCS6eOmQ0vPHKTW3zUJdV-3njfgzLT-g9W1XPfLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsllOPh9ChruR63ASDrgr7bDs8FHOS4msPaAY9xKdnqsXQqS37uOqTTOw5K0SEItJlyAKs8ouPshKp6G2RD84bX7Cs2Dw925KRpIkDNrt8wHVKV7BJM74RezQMN5dQF9YUrkH1c0tCkXocaK2uSoPBkvpVa6_xkmdVbYfnPpYSlfQwQzzoQd9F8e0XTtkEIgQsIws4n54lEyPuUy55ru8bATsifzDW6_4dG_VXMMb4gVYNCFzOGXW2kCFXvp2EMEqe5JHbwQ-N-KpQc4lWHWW1TSe_oUIdGl8N6GLlKNsc7N8so6eC92dg1oSu8kwDaLsElRUZibIcbkbDk4d9UTRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=cLhe7gQnqfN3pzB6oiRlRpcSnPh0u5a8eavYiAMlXpVv8mPlnp5BIcFgDSAPN-gUZLGHHBQlkYfBuRvEF-ulQEMw48W1wMXow-9BA8xvdDivSDaPIU5h0POmG6sLM66Mht9qyn0ikEJnWqpw_R7zB6FMp-JgklAOcAmf8YLUJsNlKv263n28Nz5aNOhgmS9FTRTR-QrfiW6CVLu55Zwpf2AC7w4mgVY7RjXKzNvWbxTWvWrXZz8jyY5dAKuiYY20fE0fRBEXTSipqSafFjaX7LsNCLpMqT47HYVl5W3KOiCXFs2JF03YjTwhcOedQDLssBgdPshKs0QV2gRfKHhJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=cLhe7gQnqfN3pzB6oiRlRpcSnPh0u5a8eavYiAMlXpVv8mPlnp5BIcFgDSAPN-gUZLGHHBQlkYfBuRvEF-ulQEMw48W1wMXow-9BA8xvdDivSDaPIU5h0POmG6sLM66Mht9qyn0ikEJnWqpw_R7zB6FMp-JgklAOcAmf8YLUJsNlKv263n28Nz5aNOhgmS9FTRTR-QrfiW6CVLu55Zwpf2AC7w4mgVY7RjXKzNvWbxTWvWrXZz8jyY5dAKuiYY20fE0fRBEXTSipqSafFjaX7LsNCLpMqT47HYVl5W3KOiCXFs2JF03YjTwhcOedQDLssBgdPshKs0QV2gRfKHhJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=WlN9fUxETNsJlyqTQixkY3ImvxervJRu_p5irEB8AONyK0WY6U9_6ot9n9OsG7MWPbwS1luD1-F4RDHI34ReSIM7tyxv6EAHzjjjfLwyvxhVrvwCgmsPa60w_NDJUYv72VMkKQe6R-nqUUi6-gyTDTE6cI-5wSe5W6O6z63FTJmJtDKRIpOkgRwDSb1M-59suXMh0_xQmZlxFhbLW0nzGuxDc6HQrW-mB7gX45dSZ9O120KaSdc4QdVKy9rbPEaMbeNldYASHTA_pm5Mam3qQlCPYJPvAuDPky6xN0wBIlY36dTSrcxIuerYOHYPGDyyMwXy4tZQ1HeenF8AQ_9giw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=WlN9fUxETNsJlyqTQixkY3ImvxervJRu_p5irEB8AONyK0WY6U9_6ot9n9OsG7MWPbwS1luD1-F4RDHI34ReSIM7tyxv6EAHzjjjfLwyvxhVrvwCgmsPa60w_NDJUYv72VMkKQe6R-nqUUi6-gyTDTE6cI-5wSe5W6O6z63FTJmJtDKRIpOkgRwDSb1M-59suXMh0_xQmZlxFhbLW0nzGuxDc6HQrW-mB7gX45dSZ9O120KaSdc4QdVKy9rbPEaMbeNldYASHTA_pm5Mam3qQlCPYJPvAuDPky6xN0wBIlY36dTSrcxIuerYOHYPGDyyMwXy4tZQ1HeenF8AQ_9giw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkDmIMKTXZ5c5q_qaV843G1XuH2HqFtJ9ySkixza8BCibfSFz4xJ-xRkBdvtUOBqXS1D7ryHsC-oo4tf61a2Fl4nXTmfCANeA2puhxRb_X7u3CHt8SOTngPn9Ltqhr89WyahS52rbZhEBnlXt544QcCwU9X6ZhUjzuiC2CE5x8N7QlMYXeMULr4du3VwzEF-TISmbz_Gxv4FPgqjhrsL_oY6A3sS945Vz0L-4n64SnvOR66vNTBBuJoYshzu8_4EkfJrwKKs5ju8DlLspFpENs_y6IKM4gdDLSMobH1NH2vzWyhpCB1P0BacczvgjrbgaPrCmXJJdPe-zUlae9TsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=NYrNxoh7qzOP_Pz0ukm9qnX6EcWgaf6s_IYpkjcovKKZs5veCh4OJweJk0ViSPNEJDWoQCWrJKBFNgcgL_M9go5xQK9Zn7zXgnlVVpmeFK5QWDv2gvOPWPG4L-fH-J9og-ZX5v5BkBIyyJ9E57ZjD-l54UykrEfugrOG32treF9P3iRXBHlm2NyUSVDaZ69SP3nINZpJ8TcWf4QWuA5OWjm93VYQZIAgC2Xvo7of9r-KN-q0EOsaW_0SeA47jgF1S7FDWHZuOWAjA80pLzbd7NYWXXz2SZqhIjlzsFNga78ZYpeyopuIAzAOgomtEqwhAHCwPr-U9F0tAZ2M_2d1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=NYrNxoh7qzOP_Pz0ukm9qnX6EcWgaf6s_IYpkjcovKKZs5veCh4OJweJk0ViSPNEJDWoQCWrJKBFNgcgL_M9go5xQK9Zn7zXgnlVVpmeFK5QWDv2gvOPWPG4L-fH-J9og-ZX5v5BkBIyyJ9E57ZjD-l54UykrEfugrOG32treF9P3iRXBHlm2NyUSVDaZ69SP3nINZpJ8TcWf4QWuA5OWjm93VYQZIAgC2Xvo7of9r-KN-q0EOsaW_0SeA47jgF1S7FDWHZuOWAjA80pLzbd7NYWXXz2SZqhIjlzsFNga78ZYpeyopuIAzAOgomtEqwhAHCwPr-U9F0tAZ2M_2d1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAmQOOdcVoxe3WbMgQE-vxLLXR8k3wzmzlsGWulMpuIW5jxsYG9ata9fE7tI16ouHOpZA2W4upKjIcbj3ugWPYEyNndkjthX4FRyEKREktxd-E-4PQsb7yCP6idOYJ4Bs8_MjGv-4oQb65_yu4dfMPWYsY7hS8fD3Nm5_jYsdk-7CKixs_K8WNP4UTIkInVBmiIsx55yHuj7mCseL0kDEbpLMdgZSnRIAgiOxyssmd0RxBEbAPorbxwpo7WxodpacvRaxNBGXnFbPk5xTI36i2aDtTxLgVp48y5zxTINREKfUgm0zoxLewXlIByBpb_G25KUXC5RC_51pUC7xHqniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja40cQ1UrtjDqZS0d5wI4YoKEBgVU24bcvPh-n-XEzbAs9PWgr3wKTIMIOgnYV5yl67CSkArZij-KtTJa5RSUFXUOfnw2yVX43tRocXZuT0vo1FOxHTujxJr7tqoONoI_X1vgfD94OeDHuH_KbGv98lFVjh_goBaeEHXWug6JwTg5w4WwUL5QcJAj23J4tdEhUvDLR4Flpynjw43MLaJZHRBhMGZna88SOCWNi6lUNNj5qHsSTX0jtNZfugCgogUyc6XKePhgEfIDk6-yFQeEnUAQGDXvCCTY9l6TWW4iAv61unYfNSN-4cPP6QLeT53gPIBgikbYhg7nx5se5H7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=aXDcu6ua2xvagmQAhPuIrl4rKj5DSezJUQWJV3HU9IbEnb7hpVIAhDbzS5xYQGRe94UxlrrNWz4INiLZb9J9FbUE22HZjHXAUG-olIwuK8EnKUxK9-UupWiNDHcfgoW4jGQgT-JaVAycObrAYOGrKdnYp1aB6cM7cLvh8qjOmCJ0dhwdcu-9c-TT54bbxFZUYAoYPnB8lcliCBJPlMbzibaNHhfre4P9IyceRncOZcn4degXi_MxnaQcMBAJ8c8faDNsID18iVzqVCPBOI8jExBjRXHRcX85iQwBxbZyKnhHoMyTWPxmsuDgS79wMUsM5GonmRXXWcUPqoxgNm6-Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=aXDcu6ua2xvagmQAhPuIrl4rKj5DSezJUQWJV3HU9IbEnb7hpVIAhDbzS5xYQGRe94UxlrrNWz4INiLZb9J9FbUE22HZjHXAUG-olIwuK8EnKUxK9-UupWiNDHcfgoW4jGQgT-JaVAycObrAYOGrKdnYp1aB6cM7cLvh8qjOmCJ0dhwdcu-9c-TT54bbxFZUYAoYPnB8lcliCBJPlMbzibaNHhfre4P9IyceRncOZcn4degXi_MxnaQcMBAJ8c8faDNsID18iVzqVCPBOI8jExBjRXHRcX85iQwBxbZyKnhHoMyTWPxmsuDgS79wMUsM5GonmRXXWcUPqoxgNm6-Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRiL0_4a-gip-SaB21KrBbhPLsmSUSw8kqGDVX-GKORst9eaJKvrDMZfTyZgX2PsmHpIYVQOW7vLM_qYINZQObmzgMIih5SR-YQx6zDxYaI_aZcn0tg3M3Na-0SOCSw0i9wc358aeK1nHqEHUI6IBgHCf6SBGfyJv5nrAhjYO9zWYvvSBFOODn6SYWoUDFfhZIUgU3Uvegb6CVu0XMwk7erxFWqEZmDKdcgNsToKIpEBLqt8M6jjCHon4TcB03eoTo6HO1whde4Nfa4APkTzxr-pe-MhO8h9mHYbNMnmVLQE3CZq-rLsNgB5mjzxK74w-1U4w0q-0v8l2PFGpbwBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtOQ5vFg8Ebes2zXlMOr97w7Yq3YNf5z2setXSte8pCwAlj9-ueYb0R_6ocNffv6aSzaAlfRl-k0IjE8Rcs4i6VZfVj5i_HNVCBvwzN-TKENF7Twnl2UK3ddoTolxijkWbZMNS9yz8TPeXVyjqWWqjEJOYIN5GYeMOw-GeVA2RYIafkknugy-4H5iEmKiDKI5qlJCABKKQoaRsW8IlFxAs-mHC-sW7X8N7V6vV-MsZPOcxOSDCi1z-uT-RUJTupsYAhZoKfWs_2S4eZJrWSxMxYVT6Ki-YXwDxKp2mSFMRuddpp8YJsieJW3ET5I9scwJiBWADHLGnlbJcBhiR-E3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmAIuERVucH1z7yxA0BJP6M8d4oKGUbGtI4FmBNp_Lp9Pjdua7k7vIJru2v13yfHjm8laf5unfl0wOfgkZUaYPPWiEg4iPCkVbxkabR0YuJWGfjBk_wkXWp8-YWQ5xl27Hq64IWFibbLKE6yN-bNeVTm2x_bYqQPmRAc1qaNc49UIOOnOexcDjmNSMz9S-bp2ZFJ5_F-tjDRnZWxDHwJxRB9OGOXbcWxeYAxH26_E3jYMQgNB6FdYjpTyWPgfRfKIyCnH_hBc0PU0kUf0n8t2o2vEDA_6dhN5-bPAyl9Evlulxtk4RJLihAHBaNI8e9_nYqAR8gob6BNTzt6M4b9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g15
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGIKznHjgUCO0ANpjBPXHO7Qko4KeRZCSSmHeorDrMmL9v7n5tNJbWIp14-1HyA2sr_cei4gH4Ia2jC2j9_2UnFNe1OJKCbH5jQN5pAy6qNv4z-GhTIgwu4HZg0gDq5mxJflmIAc0dq-0ACi3xbumB6av5pcnaBKiObLdpqxxIcoyyBNylHlhm46L6b_MmvloR9Fsc8RkSjzN3AqJ1xfAcG6r28N8KlSETI8rj5GNlWyl1ewUxW3DTpz_s6rf55-vCMw4x24eWkEREOV_98NWi9Bn0gck6F3hBDXtuobF-KHP9DyB7FVhPJtvCT4E0457efCtgVfNJObE4-y0GbCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsJ1D819WJIJPInZ29Q-jruDs1MHefqP4_kTN4XSgPLNa3PHkh--huNIssaCZOFC5K6ZHSq5NdFiO2SUQegRthkOYJSIcbhLvaaPxe02WO8Ri2XuNwBkCxi8qjp0u6KtO9XSg_HoSA4tYKK-FmNKVLZbz5m1YRZvM8dUB1sBjCcudZMkKP-_YgzNNhBVMp5B3UfQ5Tbkmul4KD0CuWGDN8HWOxbh0geZ5AccfH_eHRAkmKfUf50bguU2rsJzfUUXObakkw1L_JSu1pbwxN_0g5kuaupN44_URxzkUneM57zMCy9n7dqocvWH6_Jz-a6SJZF0lj59hUzmRQs70wwxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miPKaVsz06WcnrlRbgNJr6Xu81rnRz26epWumGbf64lSmSoWjjqH26vmD6kGDmqxWq1XeUihu5loyInLuFNlmzPyI-9rzJDuDCQtXCV7hxPydYjtqcImGr1a_5_6Z-05wBhNwtcWXInn1P9sI4vWMBRz16byCSUlyDD74rzOmLRc-S0ai5iYIKNb7cnJZmu0DCLDu73jD2hjB8dnAphn9PGB_dItxkobANlHHHA64Jk_cW3SNpTjhSttH4v9Dw-11xMXarNMfpiZ2IXX5U9YAR7ysbnXWLCHxFp33XNtkZfCM-sDtqpHO8E8OLOXvZzxdvoVic3d9O1lNdF2m6odWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=LZ5wfGe-OL6w2u2141ph37jSdS_DF5UaQaMHjuuzGneqgdQUOz4ZDxIx3mo7svEjYZMzwW-tW68MVCsdkMgA_IJJuYYpj82sTtAeo50Ll3gmjJcRQKx_wlcjYhlrjlr8KMt9z8loTkv0rfNYzBsTyQx2NGenADTirYU5ACFFr6-U6PnUI2Qf3y8SxtMxX-CTaP1-uQ9egx-Fdnn0P5mgd8EfYyFwK_fDLtIithPAPs0Pf9Yuw5JGJ0vRxgQkpESDSwfZiZuBB3TYG1a2KUC7wiM1MBwRFX_aMoyXOReTAikeX8SkJ54cbHMkk8JqL5hMnYLHT0HhtqPDizYYFlpxKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=LZ5wfGe-OL6w2u2141ph37jSdS_DF5UaQaMHjuuzGneqgdQUOz4ZDxIx3mo7svEjYZMzwW-tW68MVCsdkMgA_IJJuYYpj82sTtAeo50Ll3gmjJcRQKx_wlcjYhlrjlr8KMt9z8loTkv0rfNYzBsTyQx2NGenADTirYU5ACFFr6-U6PnUI2Qf3y8SxtMxX-CTaP1-uQ9egx-Fdnn0P5mgd8EfYyFwK_fDLtIithPAPs0Pf9Yuw5JGJ0vRxgQkpESDSwfZiZuBB3TYG1a2KUC7wiM1MBwRFX_aMoyXOReTAikeX8SkJ54cbHMkk8JqL5hMnYLHT0HhtqPDizYYFlpxKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1CZuOthPTIqd-tW-18k0LPNm_bND9OmfLcppwJ8HFtMhHCYfre7109cZHW43OpDWmFI2AT2xAn4OBzoBamc9Own2HwpTlQJEo4g8YOThI7H3mbqHSVuFEKkuoRps2f6vzCfRQjsjDM5ejIFNjanc7cxiMuf3c0RpQiAKxt7I0oxRXWe-DF5X_Sn-e_Nxv_TI-rc71GzS0sx20lNDHXyXg8LX4xnSqLpuNkdgRLhJY5XBfiq0xJ9fLbMj_mbqivkw_Gno6I5lyTrKgMEcoh8nUdkj-IIt86W3WN2oo6Cn3ixsEWMKo0FX6W_oAiEoI3F2VTFNDIhYcF-TzTcw1O6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn5anJi_ae3QqwFbFo5Vk6YOE1F2noxQGWG7nc6RIVBB_OjLLybN21qZsEx7H7xity2T-m8eIRKhEdu6HDYmNNNdDx1vJoG6y92cylK2y-F_UMBxStjwDjsPPSs4tF_nyq0RRAJNVTSkR2kk2FPYqgWNssVcL-3NxoyxGVQIQBM7aHycz77DTmasUxU5eTpOtfugXah04d6VK8HmnNrT3n2XMi4qthM3Gg0y_F8FIlCShNewAsLJb93vMEUvgIh9Xp-VqlKG0PBN_C9-kIiC4B0iOZolGC5juBmUbOebQIhGC5oxyFHUlfN63DtVuakq64MeTvd5MX4Y_91wbKtyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDRZwMfwLMIbEy72OYpLKCdyCtgTx1TI7uaL20oC9FI5X40vm7a3pHyS31ukh2wvUBZn2bsBWlbwGBElfTb7lAYfNBL5w6Ua6c6lrC27kGfiW-NVI8kh35joaoex990ZJaMaNpQdWbk3BMzjaKEd37zE2yrafp7biGQxMftvLIRH6CV6jtoBwxR-og6XskPzfTAwr_EgIHitKk6_4xgZSSkW05WM-zvM-Dfv4UeezL6cW6r5QeYuyW6orOQL71xdXCR1mkrKc8d0WeSge33VzQj1rfffPGaUpEo9wq8KPpWSp3XSlOjGWM2iZBem0EHhnUKg_eLDzaevIUEZZvZQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBWPS5fkHu1OfdySHsBo7uiDj9kMU3QNLnxRukZU-KCE1B7mxLXeE4Ba5Fr2qYAIiOJ1iMAroW3O8GOCX90Y52-ggVO_kFBUWJPPBgU1px0ck_ojlxRYp5A19pg-X9kOI4k4qoU9BaLRb7A6NLytH7sdmMTKSXwOf-lw1eo2VmNaCIJeyhwazyUtv3GC1MwhPSaZGGLN_VT66KJQscMAKr0hJK0_nfzKCRkjlQK_-0ntA0VnbTopcz6VKyod4p3Jo2Q9tRVRyUFVUPZa--2VsEGlF5Kv1g3aDuL44boOySzVtIHyC_vsK8AbpWcxUIE-We10e653nQxGMBUb6B4CeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ5QT7OdRIJDDXNavFc-2UoWw9RJFYk3P7LihwCqPPg2gi5aKfAaR3kPqz9rar3scnb2WwlcXdNPsBIyqlvY9Ya2qoc8oFIV5VHF_69slz1pDsI78NYi-B_1qdz8gNwxcogzeptihAJi1xx5V0-EO_9qeqssSyLTglyIvEAqYKQJ-LR6N45dTCCufeEQwDmL-wfsfrCX16Pj3ceF6VM1Mr5ZqWc9mSpX6axY4oKiN6bbGwsGOswgLJpnxzeYal8W1hRMJPp-qelC9BsoTM1HzEBvC6bssVpLniwiAfsPZ8lwMNDKsXmO09YBXk-TNIeQkNebWMUdoeUtDJvv0bit9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMTqq6d2SElD9E9J29xSBNFpJnfJVMCUYMM-93_ekYB1fbhu4PxtJxUW1-I4BkWZILuWYAC5ectEeZ9qeoeYb7u4jsUeTOFlFos_kjyOrl_zklIf-ZmVMEesn4COy7bvhhOSXaXT7VarYUEmv3ChgspkclAOJOzEtkR6zLyi8TBrSrEktQ9PfXsgYiFc5Y9wLoZ1g5qJEN4A6J8_ITiI_4v1-9GL1KcaQ_Jont0ncKm1NiSLRj31fY4AUCpsCWsP7bYmal0zYEoElbf-kzZ9n46GgudufuiSVwn-wBHBjcbWHxdB--F12SpFIBpx0EJ98HviAaztG-Vnz6tt9xiNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWUBs4PZZLhMLW9CqtgZ7SoMnvrr8pzmPhkfukgZe_AqYk4Zo7jmOQjH4nQUCUPsj5CaVQI7X1hWDOOR0pm4pNV-8wDlft_gS0ifb29Ocst4n_5EILZkqku6jbe-rHhbPAy_FUxCwlnUpXLrn-QgqkZaRps415mzssk1cUxuF97TMQurgoOLAJ8ic4DH-CE-O4wH3ERkXp6j2ZzETSfWgI4nknSuQnFNdBcTuYV-Ww8GtPbX0WKwExwu7SKhX7eUCc82-opulDQ_uIXFj0_50wzJ8MUFNbDwn9igZgC1vRmERKxFlj6iq7sfrEEPr1h8jS2o3KIIw_SvJeAUcBZRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
