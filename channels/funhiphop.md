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
<img src="https://cdn4.telesco.pe/file/nbbBaaOK-_Xcv8Fwpww0mLzgRB8IVc7fE-SLb-TwzHtdOh-G_vxkmb0Gqe5A2UEzUXc7dKONVJ_WpudzduCChle0oMQXEIYlmUr2Zzu8Qh8Tr9AzD8bJwfkLBnnWaNh45goOb_sQS1JWhY1LMs8-cONHZD1objzBvr95vz4drhLifCZrw9SDsH3R5zx0LbfeNt2WdBNB4u7ct0U6RWQNLBQDm2joimOS3nkK87CSW0oeCpddZd9F8ItsztI7qzvn37EHp6pLsKC73Vc1N0bigSa6mezxVIilic4N7pZm_m7CMeaT94GvFhhyAmdA36ENUlvminILR7SnltU7vs212w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH5_eC7uXy-tsuYl76F-ugn3H3bB4dnqs4EkRIFkMkpyMVDCcuNgbgZuVWj3csPJftgcy0ZY3IuiSlQYlxr8he_moRCy_hHfYLOHhH1m0zOApaTFc-Ot5lnwwFnaDIml7S8Ps9SMeqPTJSiH8GN1BMZoEhWhzVVhg22Uwe0N3w_ZNCDYzxGhpXBpJ06O_tF_5S3g4s9ulYwFFqaJ8KiVVfUAoixdaq19x_d51tbC9HBX4s84LiniiXqORq_QohL7xJKqgAOmXAvO8LCMWW3Z0tSc9bIOOWg9Ju7aIkDbssyC8U23Ve_wPMMDZxsutPE7MYkywde6hBdh7JiZhQF50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=BQkaETSmyx8gJwAExFXQlpQNIbBF_sLzqGsuQL9AJZk6iIIa9YceyiOinoGqD0clfe5yi1LdtEY6sTC5f-5bjEWMEscrsvZAHbc8a13c6SkNHeHMmoGqGz_OvA_aHm0u4xKEEH-OykTERPoAWnfKPn7MFE58QbvczWvj3ElYTI-AciTNcYlneLMrAkozW-X05mN1o9VPQJzxnJQuuaBVfBprRTGh0P3aWiZrM2XPPfYQE0OvHYT6cSbSq3o8iKoLFyXHmbwhd7T2DMGPFt4MR7VN1ydiTXhDD4XKa6fFFt-Y5eTZQBj8M06QYQcnHYogvAMjqGApxaxVI3vysAONgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=BQkaETSmyx8gJwAExFXQlpQNIbBF_sLzqGsuQL9AJZk6iIIa9YceyiOinoGqD0clfe5yi1LdtEY6sTC5f-5bjEWMEscrsvZAHbc8a13c6SkNHeHMmoGqGz_OvA_aHm0u4xKEEH-OykTERPoAWnfKPn7MFE58QbvczWvj3ElYTI-AciTNcYlneLMrAkozW-X05mN1o9VPQJzxnJQuuaBVfBprRTGh0P3aWiZrM2XPPfYQE0OvHYT6cSbSq3o8iKoLFyXHmbwhd7T2DMGPFt4MR7VN1ydiTXhDD4XKa6fFFt-Y5eTZQBj8M06QYQcnHYogvAMjqGApxaxVI3vysAONgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W62onPAL0JU4UnPlNaz1uDlE-BxPxxDsXkFYiuu_eDzInc2AlKvHOP8o8QqJrqYDXjxTg9EZlHKKjzJjFUMQZFRdXCArNmyBsIZCH9BAUsWlTI-3QHKAC7fhoIFuB1jaKSwZBB3yAY9flXoJz7mNfotCG1Q-Xgj_7a8EicPJSV2zIRQRtY2lHllGUKshjeiQEIQLaRo91TolqWocPAcrnCV8y_iTzUR4R276-yuahwALM1kL5Nh_i6_buA38IqCoFxihW5FjrsWOftr5n-zA9g_cx5JW_rCBrRjLFHNukLmPLcDan9HRQuSJK5n3ic18pfuTQSIbb8wUdVIlL5Nf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2Cc-zJ2Ph16MmdICqhQE60h_sjTVadbj2N7YsZjnfKur9qxbj0eBWu4zMqhh4_UNLDsU5IHaJ-lI8ocJn212lk8NVc2eCJEGrc8Y9YLp0G07aB5qyZWxLwu-seupM3cQ2DXkSYBlBfzfH0xqa1Gp7Is8spnctVdKqwecrEmZUA22siAvoXd7Mp2rShwnjCi9gyJSBVJcj7o2Qw-JXwgYLeZu_P-jOzjvOuF5VepTT1t4PRMRifHusxy9oocOzk-S41eiDpPljyRJjaoZTqwThTml0tuXM7yFLduGv_g54pD5pGYu_jIxkIRFzkwetMEHx5DNQPrbEmFfhHXfqSw-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=NSf75J1TvHD_DyOmqzuSzkv0iLEP6VCBcsX2bkeI1Swqa6FpBPhQB4NzUvg6ShWKRzEqQwpvOmsbEQkbZAjP7xqwCrP0Dyx4yDpSsegSac55Ty3p8jAeVxCoWwYM0tluJ6xFKxa6LiX52rJS-4VMvzrvdwjBkfaG-j05qGjhRUojRhWCDurXEzZlGQ8OCA_pDpfiXxSU53prOPaFzpIHJKQOEyQZcrQbA5sv3uUt1XOM9mgciWbK_hKHSIgmaHI_b75VJaXSxQkKzN4QQoP8F_A9VfWVh9RjlRvUCu0Aarwev-Sf3GqcwdoB7LX6XfeSxbx4NZ80bUsoD2UMQOPk0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=NSf75J1TvHD_DyOmqzuSzkv0iLEP6VCBcsX2bkeI1Swqa6FpBPhQB4NzUvg6ShWKRzEqQwpvOmsbEQkbZAjP7xqwCrP0Dyx4yDpSsegSac55Ty3p8jAeVxCoWwYM0tluJ6xFKxa6LiX52rJS-4VMvzrvdwjBkfaG-j05qGjhRUojRhWCDurXEzZlGQ8OCA_pDpfiXxSU53prOPaFzpIHJKQOEyQZcrQbA5sv3uUt1XOM9mgciWbK_hKHSIgmaHI_b75VJaXSxQkKzN4QQoP8F_A9VfWVh9RjlRvUCu0Aarwev-Sf3GqcwdoB7LX6XfeSxbx4NZ80bUsoD2UMQOPk0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAo6dBuR26LzYtVao7vZ58w8yzPFVNOZ-Kdk7OfeuUd5R9KrZXgZnTB2hjJQiX1S95BjH44g4-fbbj8ZxAWZdeV5jvZRkiOTnfcFSX3MopbcM_Bqe0t5Uav6aYsFsaMPEJPYyKynGgsBURS0WOttkntC9Md_h1d62-PmURuwv_SCgpwPF9IctKuF-Xoq183sJvlc-nfVxC4Tc9HAcompRc6F5lH3g3hdppPDRiqz4qa9X43VpVhxNANMWQBmFDJUuFsSfIkD6_PsJZcFGskCfoyfYCNWpfRQnU4aKpqX4TWbQZkEbYsAH3TTNhxS9lJiPaeVmXll8WigwaBBLD0avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry1XI0YKVHrfysBFTiGMCIbd1vIULvVvNRhUPXN4LfaD5MZFoTk1xp5VsBZ-Zt60mlZwqJyQP1NdHZkit7tTi5s3tUTZpU8AIEN3NCpVbFB_AW757wXYeZ7_jjuNSKMNa-jc4fxlzgcikxZQr2OS0S8ArShGiTNwnDKiZeIig2hk7C3v46K7whPYgQsf8pzgFTMHaLMvrJqumvlkkMN1WgmLc4c2rQGlEbXEqMy1HFn3ZoqSBaG7A8xPaKCeCbXV1fmASKNr5ye3XRPIpyXbr8miH-z062exYioUv9-5SJesD9KDGMRvFa-AP8y0D--FB_bvLf6buNm8mKLFnNTU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGv2dg5t81dVk4MeeTc6sSO5VqQs0gb0GNVqk_lMx0g28j8GFfxNjq98Iv__E3XDdeoDaF-8FJ10ec0sb9VwpJm8zWYb8knersR8cRHy2B6c7ONimpZptjN5GuUaF8vjmv_n-Rx8zKbr5Nv0aXtlgpih_dl7y_osG2MS1Kbff7CuGdsgk6aVZlVvprSDkFTrRnmGdmhda_fHOeqR2Ydul340Ap61T1xVxfdj1SklqK6ZGSqf7UnuzaPL2ublW4vK1Qsl5cMSDQa0jDOURF0cli2Fd61-b4w8lwUiM635aLixpGa4UcT03CcKoAmOyPskBw0hn3hUoDKg6m-cZDk-6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5lO7jQq_iO9Q4ZpJ6KTTL9upOsF-NAu_rZRWpFWjjoD5NXtTQ2y5XMSkuQpeeGnfroMegkKXzReaQVJRptwBQ-ejN47XtKFOhxylyXe9QiKckCz-mxs25lFkr0ipirP7M_duSzrfpNpP-dyU7Mf7E01hzKgJgxZ_A8Th5nDY9PayA5qzo6VE9SV_hsO564E0QdBO7GY98IsSz2S0EqMbN0HfX2dfPfyyV_2kFVOVOahXKDGtU68j-ZUw0KJUz8jSNLC9NRcibdORsDkV7UqfkHOuYOizB7KOh_vc4KcR96bpLzVu_5Wmf1y49JcvyHdyUa1yZRFiitvYP_LGOnAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUmPXyAk7XI5Vmfo1q9I7VfIJ6l3IlQG_Xqw8xWVlReCzJGj8hQhKkOsJ26Yz7pc0uXTp9ZPdWNbIhRK5TRtZ_UVrg4r3MBN7bVHzKxaawvZB1zIRniKN9v2R7pZ6wo-pSApzB8xd44mhClIy5ZA6gOz8CSVJy4tK6Y5t95rXjBmH2MrPP5793GoErhuBeHkcTp04xxIeQLy-SU-SAo86TMrPtkRMEHVpTswsbSX5WfWV_XdJMkMtkmfJhzlFZ0BRH7ULk0HmwVPZ1-wDotdHleOS3_CF2SHaMyeoYv6gFGL_vISrlkW7-lTHvdokzzUzg6xSNSqtRxEkVfgmvYTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-U4ZfRm68pC6ZdN7Hazm45ypBvJAHXyPkl3xggf_rw0GbrHIfkkXrl-cIbVI7dTB5akcT0mtnewdZCxhnYunHbh-gYaVcfEfCtXC8Rrq-jlI_HR_6iqPzvIgAYmf-LXKJJbqvooVlvma5_vS_wdDnIQ7uAV1Br-Zvn8zWPQlrxMF_4TqQcAYu83DptKvPePaLip3_bd9XG9LK0pwW0BR9cPcuEHYG7xNenXKEqdQe_X7zZxzu7cMNLSl4KIa22U9yWcRxI8JcXqYP62U7bgb37ZGrEVwAdPFiB1GuMs8sXKAtBbGmiPQoK89sPmx1_8ztOid-7iO6z1cmmoHwF9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhFlm_V-JzAmdYGZD_rMwF4ojPDhgaBHeV27J_U9gJ5JMW3iZh-C60vGFpkbsWD2ryU86p5ams6uPEchwrJJ3qkIk905-5VMCvbetjvGwo3HoZ73c5ykcpoINUXW-6hXBD9WnyeQVRI6R-RMoenpgn22Om4YQsKs7xBbew8bLkeQgjh1hcNEYtpCFcS7fc0Rpjlsk2cVW8QM2RLC6BZ-Fo-Mhmvr14RsaLuIah23LMlHnDsB9AOOQlrYR9CBuMQACASG7AIH4AI-y-K-amI-ucIMBE_AuIQLeaVS3xzaQbxGEOMXoq03YIA6pt5wHI4pDbIGq3pI7ogaYF_1JwU_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3rjGyimQlhK0fNNs9NmcHaSITvYMrfcd34U1C-7mq_g_VZTetlRRjVBuKj6eIbqlSVhoiDYunCCScSgGyJFsUfOtX2_noIbhjRawvItrtBGtwcKZVS3fw859v95NOlKYvb30hthpy9ACKKAWic6GBypWX_n5z4V2eGlEgSHym2r6EediqyztaJ7kM42E2X5LTMPUAeUGyPt9L-G6jxXVcj4ITWlxtFEsanwfTroM1Y6QR3xLkxU68ijnvQyTbW4hKxvwjSNaS1OISMr8lTGGo2OzjV5ZKt_zpC3cTz7WJGkmq0qPlA9BreTKDnajFJ4cD-DsmWyHqHleLWrnuSCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hn-vOQ0FNPAHeW6h-kou6FqzbVPbWIQn21T9k3UdBiIeSFdbDtm50AL_irnjsu2mxBilcQPDpTl5Nu-IBLyELD81Jdmiruw2yx0kNK8M9K5KxcXRNoPY6IXbvy3JpnE-9A32fAjN2FuFRrHiRVxIHjP2Xem0sJppt17JkTKhbnl-UP-cH16SvyppMO_0Xs6KfgsLiufCsDQtuH_IwsYAO--XPcWFS_gggvAp-Akx-ntlwZDuG2_gqgF67gdA6IpwjcDC_8cj4ttpFMqfBvWqDq6rMGz9Biy6R-YON94KeBhfg-YUYtNrgr9mw3YKdp2V1AhD0-I0OHgw82rXtAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDW1WTpYmk_1HAO5rG93cCxE2ZBpRtzcrQEQlWuDZQkiftJ0aiZxP2e-dP0colBzezLE-vgrKJHF0IFtFtA33WbDqy_NGJQzA0I92gQ7OtLt_Lu12x8nm7F9RTWSeuFuQIwgQUg82boabl_nvjwZz9Eg66nxCFuDazEx26p9gzqKwvVZyzpcaQ9665JvUehfG9YqbMQWR8EcTejdh4m6J8n82zmgenCh4aTfLBq7xf9U_zHcd6bk-8QsvXTxMdOlfAdobqZtZ-jBq4YqZA6gfHKGRSrT5NBQeWrEuJP8rvO3C2-IhnmfF7eatro8otVV6pgsw_Io5e9prZYiIGjAFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXOcZn4rkXmRdmkUoP1XnVvEGAMyc4e6w9WiObPDQlz9XnBAiUpkv9YcZn_H3Mug4XLkrUVW9f-WIo3s2Dd7YAa1GmD9Nb9EJGuBZdFAjnSlHdKZm7pLQuLSzK93Ej6yRiRU6nBBEHkJ94b3HJMSjiGOCN3KckVw5K26knqUY6AAnjKznxvarWVohH473-J_ymo1PAIsNaX-wjhVfOAsDw1F3jPJCCcxW6OxSed07QU9z344kPDoaPdigPlgtc5nAKi7YC08PYS6jtGPB_ZiPGJgow9gUysapK8I0jP3i8gURpmmvyqMOSpGdleXhx_xw3r3jVpEcsjWyOy0e7SJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4rVkGLIIwh7yphtqSLZp-j4hzgBVyZpQ0YyOuNcem1VPZ7DG9tEVrYVAzo7Gph3qFFUEsB7n8tiWbNuQdzCyA7czh7PChDjMHqk-HeUN_j-XZhbd7N3NNZk0QSqzKNm5DpcC6c2f-ArqPGOzTOxW4BROdQageMQ8MKCaaJGolbdLcY2y4jBpH7swFUtm3eC0yLC5fm10U1sYs3t4x16vAo5Chqyt2bzL7nIkSniUaVU51jOekLs1M7xhn02Pdfyr9F9W7lxJL4ZxNW3spFuvY-hny0wHxEMQhxoBzi-crNfxUraw5CHqlu-aqB7HjiwWBWhqTfU3yeVPqz5dP9rMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HedsQBAn7G5zs-z1zxiqvs-Pxsim7slPEV2DM5W7neJGrcBfUBqpZa64bpwq67VwBEsj5hZCA-VfScUqoG4xLE_NY2cg5BcD1ELON_SpFkmTxpEw5egpZqAJfsnxq9DjZwCcWiv_gevgaXhPF-TQPEn0OmIgrUcyz6Q6-IY6651CQCSuFo1bZW92ZxTaGxU9Z0zmHKAQj0efrDCj72a8l17JuXFD1izDuK3SY0cK2SU7-0pfKb4uwzPmuqP5WGK9qc6lTBnxPW-f_TKhWzJc1pk8Ahks5gRAA2TKKw1X6dJRuquEry4MnkGrm_6zUpEuhxqD9OhbaKOvSjLK4LqDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUiOEzr0qejaDDi0y1npfm3IX3QEbOSeUErdOTlXY1aUFtwE1Nb1DK_jj2SHwNQgevTLVOGXFPAUAwT2SGIZkEQjzJfa2P6mwtDp7MlgswdnNd_h0mRDsHIf5qAm3ofeIjnURDtvM86iGm6PE3d8u4fqkX44rv79osgEH8lJAsiezxmTtk-o7gcQRaQT9qhqyi_442MfqRkwrgEtfqXoY0SolVOQ7-wudLylXr53xYyTrEtL2hRXYfw-Dq0sntHLSEha7lpdLj9CoKTOgdOS7LOi-ntA-F_d24K25LFiNf6p4PqjJQrL9wIBV3Dca0F5fWYoeeRraZSY_KD9ZcmZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNHNXmb4J83r-2IG21mSCnd6DJVUb4KWy5hvQExKSutA8b6EPNyI0CiRg_6gE503KCqbi81uv-hLP2ep6_yQgfOfyvBuIGR_Ac5A3ZUSzdQSfHNmGEv-UDaE9q1PKoLUFO4I8uQx-E2ErSLPAFrWS_uFWJLl8IA6oiqVvXXf33r8gabV01FWWFMv8fJ0SoQXxiArE5-osN_usfp8LM_QAjH9kSvd21DaGnm0Ypj-db1pYhe8SlHbXUEipvgE-X9G3GE2f5GGXO7xFZnO0vMxi4U-VNPo3OZNTRW6LF9-ByM0pjfa-71zZbojbEt5BWnGKI5IVSaLj7vXuAm1_aLHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76865">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUAHGlTJI7bOoZTe_rO5G55rE3qQChfDNCZHkaSdIEYwzShp8ZR8KbJiLi-EdClhzxQL4xk7RmuAfGyowhhdo6u7vzORk5PDfFbBSvxkG1I51qUNALBOxXfNvO90Ggb1jO_pCCbHB6keYMvjt95LOuS8K5XXp18S-WFgTSyVkjDzzpN01GBVv3EKMDjSIqs4bmcV9AMr8Xz4AilKgtuS0hWRmG-U_A-oKsh3C1328R1AjI1OekjpRr5IggWN4NsR7gExW6zaYyhxScki7hiyVhGL8WVlH-iIXX2f6WOAP4aZRIBQXpOwWvEpaqbI1wcTvyzJ5wp33JXaVmrWjGBt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن نامحدود فروش باز شد به شدت محدود
🥚
هم براى ايفون هم براى اندرويد
🍏
🤖
600
تا اکانت شارژ شد
📣
قیمت آف شدید خورد
🏧
فقط و فقط تا پایان ظهر قیمت 397/000  هزارتومان
( )
➡️
حداقل خرید به علت محدودیت درگاه (
٣٩٧
/
000
) میباشد
💓
جهت خرید ریالی از ربات زیر
❤️
@V2boxinobot
اينم تخفيف امروز
💓
تضمين بازگشت وجه
➡️
➡️
➡️
بدون يكـ ثانيه قطعى
👍
اپليكيشن تخصصى
🤖
🍏
💻
اكانت  ٣١ روزه تكـ كاربر
✅
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76865" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7IZeLPq9SacW5C1eE2QU-jdZREZFy6RADHynPBvV_jWXShOh7Q4mJGn34aV1JK0olYtdoWLbMz6H0rgftfywlZArvcBtqDBxk_QX4EKCshPVRxnGuvHR5cSbif29T2TNCcIQQ23N0gXSLMDbbKdx2rLjYs-IvnAatjtZejy08yAgishcuPIkePyUAMrGyjUBy5IDTcfslb_yW5537nreVB1mbGa3MibMzf7Y7gVv82Yz3Zl74touKPiVwPi9eOPWXzY8qQFDriWRYJHcqJ7gHIl5lVMUMhdx6BQwdHd_w7qD3T-uqM6ldO9e1zEOhUMywNprQohlx9NfOgMR0_7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-dsV6QHAhzjRhKyQTjdtgBTUnWjpMJrnHWGQRFlMZmlfiet25utaxK89fJeGlMfLb0aWkLU6e134fMgu_P74fKk7R3rWS4LQsIjPeZr5hwbTg7zySxArR4X-mkV64BL6to4Gbtcs7XBy9fa3CVAIUk8jhjOFj_178_r0EervNcrI0GbBWPtfY_TyINwyQ3klTeOzrBVfi9iSiUlJebHAekDz_NtNZKLsah5L--zCL2gwD2p3ODJDrO0Q3p0IbNbkZeXZpQj43eQJSTL2NJt-vfQazvu_vE46s8hVVrJ4IssIc1qK525q383xAMkqoAeeJaTvrwTXbIB4p7vCHzd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N13ZiyM29JQx92VZR8U4q7-LfD-GY4BwCoEuHdT8b2jxa6_TsgNAKw3UQystnFja56rX4zfSRKgPh1YzYrq5n2ABMogTOcdEOxRLmYiwtaVEaK-KUQpj1HAsH1BNtOm7M4lgep-S4BjhReLhSMzeAktFKPugNQpTpF8NdN2okYO1vHCZW_F3Kl7Ap_diiu93AU-wrw17xtIObm6LdQhhEoH-UB5h0RobdONawK30h4945gdcKGkdAD68e4qbQ2KmBsFDHImqYIkK3w3_jLJMXUbGisdBh9lrK6qPeyOY4AHgt9E4HYMn_M11-C1S1Yhnqh2COOa0kOeGwP46l2DavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e570681.mp4?token=rpN5mEzuvc_vZ7n27Oqy7L0SySPtAj73nXmznEmtNTMEw7o5hw9K9be6Gy-ZpBQeF5w3rGLD41Y_VKLq-H1rb30VVFciTritP11LsxZbi1DRA-GSuVbv-IuzMUr3vkXimkHTjGPk1to6BryA-KOKvsQAdBc1eour9vBJOJjidkAcVnH70A5yLaKOI9x3fJj9rZ6FLEDSXjxrcrHsWou0_iBPLZH9FVNhiCui54dAzy9x9z6agH71qhg9pHyj4sEIRjnq0xHjtrtumyLPF6WaAs1TG7hvxPun0Rfm-E2Z8qgLYJ1_OkWAwBAnCgP_yfqPWkSMzMry0zzo-1ijFGdlsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e570681.mp4?token=rpN5mEzuvc_vZ7n27Oqy7L0SySPtAj73nXmznEmtNTMEw7o5hw9K9be6Gy-ZpBQeF5w3rGLD41Y_VKLq-H1rb30VVFciTritP11LsxZbi1DRA-GSuVbv-IuzMUr3vkXimkHTjGPk1to6BryA-KOKvsQAdBc1eour9vBJOJjidkAcVnH70A5yLaKOI9x3fJj9rZ6FLEDSXjxrcrHsWou0_iBPLZH9FVNhiCui54dAzy9x9z6agH71qhg9pHyj4sEIRjnq0xHjtrtumyLPF6WaAs1TG7hvxPun0Rfm-E2Z8qgLYJ1_OkWAwBAnCgP_yfqPWkSMzMry0zzo-1ijFGdlsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر جدید عصر یخبندان ۶
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76851" target="_blank">📅 21:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🛍
قیمت به گیگی 8 هزار تومان کاهش پیدا کرد
🛍
حراج ویژه تا پایان امشب
⭐️
💎
30G-295
💎
50G-470
💎
70G-590
💎
100G-800
🤩
لود بالانس شده و مولتی آیپی
🤩
🤩
بدون ضریب و محدودیت کاربر
🤩
🔴
ظرفیت به شدت محدود هست
💬
خرید
🚀
کانال مشتریان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76850" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شهر صور در جنوب لبنان بمباران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76849" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMFcEB77-9wtemrMApyjhN0dMz4uYTi8C1z66R_43gKGF5roAsDCjuyr0I6XyFQdUiBADf8KFncC73ELUBezUjpfVQUh3G-c5hCIEUXsPfLgZzK1zAb_5jkmIHQrlR24SZ6qq-NBQfupnw_iW2oGIrkAHtpLKPOx5gKTCkPL8wpBLJlmoqgHTswSTI-1RB6zXeAnnLbNvMz_bWRJDcEhXfdSuQccRdXRIoOUoWLv0cMClukDXrPBGmfA2ey2HKkmkdk7OT6gJnlB5J9SeRhjnwuIXb9SFlo3JuL5P679ecEOCJTvM0QxpBFWZzE0FscHwjT0p8LMr1NXMI5Rn2komw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArZgJdmqyJhj0RAFOp1YKtGYDmafCBRmWHPMa2v21GDijpVL5Be3IaE2ly0Wk_DOqYG8BCiVoONo_DnY8YPUxJNygEYUS4xFpI6H5fe9updNP_tgDl-jdAFRZxijuAdTXiB937swAAKSQnQWxVQsjHPWdc84mzC-Cp_XDmOKXs0q4asVeLBzRcxWTjMT-fD2rc8OAJ8-gfQcfd9VIhaxyZcvA_NC0G0mqGn7QFzKTlZy3hl5pJ7eTKXnHe2FJXwicSwuKb9umGu46z8umOLkGNr76CLTfwdLhzScUAuIlDnYkbsrhwrnaBDRoTi1TWwAmlToxdbRWnfuZrSrgsCOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=V7TjzfxwXVDloXpzKsuYT-kChVFKSrHS3TwfsITDsU0xAG8r3se2Ug62MYf9xPYJQADCVFFqpRuy8xt-IoemKzFuOv76KOC0oBeyS2l5DwcaEpENSR7GKZyFXYGtBZBTkK4uZpCHqlyROHXo28PL2XbaOTOw8gnCy2j2AQnNQCFJy4z4SOuGoHjJVKRtUf5WnYqHCiXDkVdoJZj4ouInJ4C1x1VSWd6PZlLwn3Jbv-PEQuQG3eibTlaEsW1qqurw0oFe0Uwg-GLHXcT9IFPlYd_Lh_Yk1gJ-aHde9gNZYzCG15JB47HtqUMYoNGZ9F7v9vK5cqIKZ_MV1QsKZ-YbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=V7TjzfxwXVDloXpzKsuYT-kChVFKSrHS3TwfsITDsU0xAG8r3se2Ug62MYf9xPYJQADCVFFqpRuy8xt-IoemKzFuOv76KOC0oBeyS2l5DwcaEpENSR7GKZyFXYGtBZBTkK4uZpCHqlyROHXo28PL2XbaOTOw8gnCy2j2AQnNQCFJy4z4SOuGoHjJVKRtUf5WnYqHCiXDkVdoJZj4ouInJ4C1x1VSWd6PZlLwn3Jbv-PEQuQG3eibTlaEsW1qqurw0oFe0Uwg-GLHXcT9IFPlYd_Lh_Yk1gJ-aHde9gNZYzCG15JB47HtqUMYoNGZ9F7v9vK5cqIKZ_MV1QsKZ-YbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=EnT-e7K_MomzK0WYJvU9UvqKBGKVW-ym2Z_jv4eTIuNdCnBkJMEX9zAgBZgmQgIerkazJ2v6nh_3fpSBqDkLhHIrKOT8bzHURbM7nRsaTDQtoATHNU5sUe1eGcQiyzohJzBLjbjk9du5a7qlawn3pAgXGrYbF1BVXCSEfW6oh3sKypVk-Oe1i2PPk2VW7qiUVapEXr2n5SGXZWUmG3fr9UfzBe4X1Km4G-8qkBx9w2lUXPsz_9FIhSIXgau7P_hcoT5rkbPDaJH9K__U0Ho2Us4XanvXVxtDC9zneT3QBiYPEIWLyjvPVSz630PFJowycfzN4RNBGVgpZEX-TyiGow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=EnT-e7K_MomzK0WYJvU9UvqKBGKVW-ym2Z_jv4eTIuNdCnBkJMEX9zAgBZgmQgIerkazJ2v6nh_3fpSBqDkLhHIrKOT8bzHURbM7nRsaTDQtoATHNU5sUe1eGcQiyzohJzBLjbjk9du5a7qlawn3pAgXGrYbF1BVXCSEfW6oh3sKypVk-Oe1i2PPk2VW7qiUVapEXr2n5SGXZWUmG3fr9UfzBe4X1Km4G-8qkBx9w2lUXPsz_9FIhSIXgau7P_hcoT5rkbPDaJH9K__U0Ho2Us4XanvXVxtDC9zneT3QBiYPEIWLyjvPVSz630PFJowycfzN4RNBGVgpZEX-TyiGow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=LO7AJLmPl5Eqqa1dwpnrvVl7aglgXW48wq2iNUF5wGQ4GVswHlbJAt4mKiNSUT8f8nhx9IlRo786I6GYMN6lsAc9DQBxWnOw3LltnkO2hA5MpsYCQBzJpFVgujq1J99zjZ_c-7SBnSEYHDB_5XTIwENrGJz_-xobgRcTWhfX--SY5Xe2KafidN66sJH5Q0tZrq1fgB2W9LBMDF2yS0il0nK9nB5dYT9qYJJqBVGVC0mTEGsyEOEP-4FSPd_APJwJqaj04zHZlDGE9r8NHx_0KUBn2aWjagaSepi4dy285HsHUgazwr_FcoPyE0FeF4P2u1ldrx4Q-NsuS7O-H6kf0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=LO7AJLmPl5Eqqa1dwpnrvVl7aglgXW48wq2iNUF5wGQ4GVswHlbJAt4mKiNSUT8f8nhx9IlRo786I6GYMN6lsAc9DQBxWnOw3LltnkO2hA5MpsYCQBzJpFVgujq1J99zjZ_c-7SBnSEYHDB_5XTIwENrGJz_-xobgRcTWhfX--SY5Xe2KafidN66sJH5Q0tZrq1fgB2W9LBMDF2yS0il0nK9nB5dYT9qYJJqBVGVC0mTEGsyEOEP-4FSPd_APJwJqaj04zHZlDGE9r8NHx_0KUBn2aWjagaSepi4dy285HsHUgazwr_FcoPyE0FeF4P2u1ldrx4Q-NsuS7O-H6kf0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPTMt1KDhqcgu_JxvjiXxGjDkyLsE-_J08v3_1beW7QVbtnYmu4om1eXSzNupxrV_hOYQJ4U8kHimjEquQAgSlZqLEWQPv2bIGd4sWOBEEuEIdxsBc86jdEZcAg0t-XyfFAzio3GT1ITKCIVW6nG8h06r5Vlr3-zRZPGWPrFFHYoK5AkE58EAv0jvRt1c1IoOc6bpr6r6JCBdpgZ4M9mc-fSetenvuurq9m4zKIv25VSJwrMFvEJoWCWITrpVNZb-1GEQl4BC3gPP_E2gy4IUYOgozpaEjKf4zvYNdVh-dh6c08hrgwIOosQhDwsRq2A0sLpSxzwmTb7xDTMG7hp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4xyCUzsKliwHKJRaoPwFNPSrcDYCVLlVB4t59zGaPM3DPgRU5suHjQhfHI8aDF0n-FAo-J1URmVuF0BFKdrgXAx_L4ECBMMp_9vqs9osEI_fAguwLPc8LdUY3yhjDJcjzjjxSoxC1YvvjNR9cxM4c_elrta-XT2U5iuKx_85WFa145SBZcgNQZJBVn1LuF8PPVrlYMGueCmsxNe78l7USUOBAN3qcX5tdSANSieaIAaNMbqLqwqGCRW3inoFTD-bamcwP6gvcgcN7zqGS4-AuJ6CWL9si86o9GoTBOdMqdItklx8EGeeLU8YucUN-Jb3RtIVOMAg7z2cpD-2UtIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6r5MjBdNdp6IP1dNfsPOp5G9wibxo7bSBSxzj3BDJFkaxBXn9CRV486Uzn_p6bzjsDnVxJfUSD3rltlCwViH5MaLXAgG_3HZ9R4ntlQSduXgXIdVU7yzPIpIL8nWxnm26h51receKGM3Nlu1_x_BUjZt5fbCWXcIs5ODPhSumR00SiMzBkXMxMcgCyevjEMp_J75o3NbnZa-PHGJU2cSrfm0Jd5VokAdGYxir9AO88p4ue_76J2T_F-i6I7uHw7gUDZL7yGcMjdpbOXrmQw1tlWw2DkeL7rWZKF39RYvRa34Vz3uBYGmOn5Jc4wGUD9PcRHqSLjsSwMWu_XgiDOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIenX6kcZ-VqEx22JbEin2mm9m86vq2Lhgq8726yofKgt6JxShsWBQPHlYecxVDZE1RIamFom-L4t4dZ8qdwKhF7I8drCe5--MNwNVEH3YUhO42zfA8ejGjKmCeGPf7sKuJEXweDQyxM2QghFFegWRCk5Il7MojCkDRGG_GlHNj2McFGS4vqcN3kFzqUwsrQc6Wuv1vnkriBHrJI0CXmDBQp2p7SK8xPfY2YIV8xqRFQ9mfyFQX_i2SsE1N3qkqM4TiIJXkJqeTh2NY--mQ_aFV2N2wptHUrHPgOIIUu-kdiHUJVEVAr_KYqwsyJzgBLcriqXl1QFFjCMvjnJKqqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD79tx9Iw2m8hVIgDbg0hS0kc7-pUkNw3YUcgopqPr-j_5NCJ8-eU2VVq8sCBuM6LGwuiHKN-UHAkI_eTBT2PM5G6vLtXCwTfmdC5BaFb34SkRODGRQ_8eFoF9fSL4OxBHrdNCp4dcYzDhmjTTxnFWIuW-Kzoc3d_1otmYUziitKEiLoWZ-ZkWMJdcVLe8KxHiSzl7D2ogAzygW0rl6qYcJClZjw5NGqIANzRM0MdXlEyvzLsVE1fR-bhKnQrH_mwfYt8FctmCMq21vGQvHXwTnOB5ME8MdT-qyHX6SHdN_1rLscUjq4Jnf7w17W9N0tLyI3xbxqo1NQ_y_2CCaSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=uj0O0WWUrIyTo6VPdSGQjfq79BGiTgZYsgE_JEyfn3CKYY5gk1zgdaop6abub0_WR30MxGH_brLaI4rdwY5ZnVRJ4dm_9221HSsf10U2I7ZvOqrgpEbt_DogmYWd3gD9qrniWo0tDj_Z7kzFk2AxNdUNPstdYTL_n44HiEfaYeWTvmqvi_zHzpYig5VFlGoExD1lwRGb5R-mJGe4DstLUIbhsvI7f1cVi4jLRDIdKxr3wn7zs2xj7YXIbbPAO5xcpYgGp0yOjPwmHH-svJf1MPbRVn4NEGdNV6v6eBdOQuA0Xe3hIdWdbilDGoMDmUuqh598jOnQc3vfCATQ-k1e2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=uj0O0WWUrIyTo6VPdSGQjfq79BGiTgZYsgE_JEyfn3CKYY5gk1zgdaop6abub0_WR30MxGH_brLaI4rdwY5ZnVRJ4dm_9221HSsf10U2I7ZvOqrgpEbt_DogmYWd3gD9qrniWo0tDj_Z7kzFk2AxNdUNPstdYTL_n44HiEfaYeWTvmqvi_zHzpYig5VFlGoExD1lwRGb5R-mJGe4DstLUIbhsvI7f1cVi4jLRDIdKxr3wn7zs2xj7YXIbbPAO5xcpYgGp0yOjPwmHH-svJf1MPbRVn4NEGdNV6v6eBdOQuA0Xe3hIdWdbilDGoMDmUuqh598jOnQc3vfCATQ-k1e2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANy8hqeNTBgSVNM_pUPSSJ_-lyfYHF6H6fAlpT-n7oJOPOFa6lq7NKeNrpaKaejZVD7fZZRUBtOpDd6t7SW_bhtjuZo4LmapefpHPF3YK5AmhG-2lnyyPBu1QbCG8uzbT7gG2rLUB08mDKuAzDZhHtHzA8gEB5rDeQntZ7gnTkOvoX3xNcD88EWnjqmeibA7MZWfKdE7_hOAtYY9y6zJw_iiSStchcq9aRt5_zJRAW_t7ev11M_yX5prCOPzeatgHzKckR-p1xwjXoIdTg1jkuQHbqJOSz2xtCuZiVhHD-6DOm63nEdFCBvQl0FUHfbmzxZX29jIpCw4fGrXNFI1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=ijJw12CEgw5eq4rVd5l9ihQfzKF3DMxHuxvx9qqjV1NqDwc4Gf3uN0YzZUI1Q9Tza1I4U9DFSw6XdwrvXsT8_nQ0GbQ84QNAtTFJrn_ztqD5Eg_AiYtzZ_hb3HCmUb2d-srebiRIGT9TjuMhYzj3VshKhZd7jLz9rTSUahKcaLs1tyhK78OFasu87NlcWRV68udLpBYLZuXNwmWdw3oR9NRoZtgIlnpxhKGn9bGti5tgEHpDsf3R3uaPahBTXxZGrlwaAhF0cJ1yWNJxC8WeuO-ij1lGbfeWi9ABam7-W0FWCh5k7SZ7J34Pyn12fbOcFxYFDL6jjzKMhyS5RtxrWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=ijJw12CEgw5eq4rVd5l9ihQfzKF3DMxHuxvx9qqjV1NqDwc4Gf3uN0YzZUI1Q9Tza1I4U9DFSw6XdwrvXsT8_nQ0GbQ84QNAtTFJrn_ztqD5Eg_AiYtzZ_hb3HCmUb2d-srebiRIGT9TjuMhYzj3VshKhZd7jLz9rTSUahKcaLs1tyhK78OFasu87NlcWRV68udLpBYLZuXNwmWdw3oR9NRoZtgIlnpxhKGn9bGti5tgEHpDsf3R3uaPahBTXxZGrlwaAhF0cJ1yWNJxC8WeuO-ij1lGbfeWi9ABam7-W0FWCh5k7SZ7J34Pyn12fbOcFxYFDL6jjzKMhyS5RtxrWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
