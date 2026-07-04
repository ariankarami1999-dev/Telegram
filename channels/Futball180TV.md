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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 641K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF5zJaNFeTTo-3w_ymFWvRhm2KDCeHjhSfggGi3UIBP7my_evtgFqcO7xZHh5mBolf_I6PJztBsBva5XNxYe4u5GODdTXJ8Yy58wsnNbNHmcSJdvrDgKrCvETqidS_HK2_IJJooiEw6_4bZF4QNRSf7NhZcgXzuR3MJVqdh28b4bKKjBSHz6Mjo7ufRTXFPwHgociQNFB9avkKAi9Y1gHT2QteJhmbfY-0RNNdzy2_WJKYVbIZFNqCz40pappc5Ic_lgaFn0iFP8fJvlxQApZji7pg4N8xHaLFIGG-j3fUJpbEk15Gx1p5oBbfUBAG3Ry8nrmB-lVD-2q4abIbOcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N38WORcAe2cCP9Ta_LjUYjRzrDsu-4UwERUdadfrhqLKX0e0unkblZ3vIAhPWQen_5u6Up499Tlwiu9Iq5RQHsN0XZqLAA_H_bYqV_1CLPjo1J4TKpi96njGF3u3pn4x6xtoSDDwLMsTypLdN6phnwSHl9ukSMTwQR_K0wp5Ig8F0LQUqOTKjbzj3AfUPdTTGh2FP0vTldlazOGdMVEDlqDM4V8vHrI-0GHgKydQ49V0O8MhL9opLAKjSOxiEm-5hlCE-0lix6qJe1aRCQv01RvdNswsR2jFt9uHuljPiTzteblCamNZFkUfOBj63R3AlY53FHw6n9m2Sh0XAZV2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMTQHjDdV2nl7PRYK-qDFKkwlPqf_DuDtEpZm-aZRp2CYrWC_MNH6dPWLT6enLUtmeXrTati_7VLO-mHTNeep4Zib_cipx9FA9SG_rC1w4ScIHFGX4mx2By2iJpU0CEEQ4IZnnudQIu09Oyohm739DycB6cmpBU9kU4WVm-Ztrg368UWZ4qMUYYF23b29inwRgU9kbxUKQhVoWF-EBIys3UAvKopT9CSCZ_Ur6NSeLKGnZLvfhFJ7xqMbDaXx__d_T0m5dLAo6LXgp7_VzedirB2pB4BewDMJfjli-mt7oeWKdcOztRBlVOB803RFlUF-nf7g9wMMILIznuWXHb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL8chZRAukZ9rMygwq320cS4thPmXbSq_VIzlNZGbp1RrvLlhL8OOMC47JVZP4TLeTHd0uitZB0wgvw79JhdIQwyWcx5UnK5NHd_XouaSqn_E-Cg0weVtfJDmwEOpnYz4vRPFLoxjeAA5Dsmkr7wnigv5BNntF7H3i0NNkOAKjHIYMoVw8jo92K7IdvoEqg-qUYeyHWJEalkhRgoy8Ufgl-SQhk5zgzZG7C-Pm-J_MpSy0Ow2zYqR094PItHGZ0O-tIOq9qvmk7rshH0gJbbCwO5RLhRaheTU_FABSR5Swaqk5SpGo3UmNBEME7yA0RNZTr1jAl08oLGS_MV0TdgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2PgvHuAOgFzVgbR-4lQfSXdrpXyEKZ2WDThQUCh_T0Q526lok6rQpo-HGzaQLiTYRObnVBJqtv1ZX3I53_OzBmdsMf3vX0Wc5SiV_a1S3P2pcFeu9-LOYxJM4ajcYdOei31CsSp5CF9AMe8OUS1UucwJerVSf4udvEqkwyjK49BZ-kJeVET9DgJ4dMwkbOBk0Jcaqpenrchx1irSP1yz-qrQDDCQQePJy5Re6zWGiUmiZeCvXpuCLfWDuPjn3m3-sSFaqbx0iu-g8ZMwbZ-OoUzP5sF1X5PITKINoM1aOnSI3KJKwaYTAtEKOuYVf4ie8F8WNNuOVptdnmTm6nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKtpJ_KJGDqr5UYabpwHqDQJ1R3qTszwn7NJIyWgmHMm0Y1k8MsY2ULQcu7Fe1XEwvdnHBn2ItxxsX0NTZVqL7_NYBktVmDgIvhRi1tvmyta92a3RKOdIExiD4d2A0B-NHvux5OQLDHThBRFhi1tRADgvMQ6Jj3HZq6Vrmmi-uZMqZkIqsJrN4Wj0zVF9vD5rIbm3fL01X26dMAuVUa-9ARZtCxKxi6jdFbQMcFnHVB9TO2AB8yzcUOWDynB2FzENKymr48H-gRL_WZrttviTppHSR4IliWkZ5DNfeLCEMtZUC7Rhod8xBM7TvJo8NWf7F0mT8iNN7yAG0gsrlOBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZoLubezeLmDQ4DO54rJAahRT0fvtkvRMDTCY0WsPo96LGqtUy4nE3hQHtiYNiB31vkgpeIVaBCNTxjrPiTjZczMD2zBcBj-us8r0NUoKJJrjbynM86__Ye4fHnb2fCTSu0XxAcVmdh9fJ660wjlcyu3AasnptTjt2smMrfws4l3_G200rJ96WtaZFtCEdQnk0_67rM2sdXjUUhG4TZ0lk52roxqR2NNaYgnacqdfnD6MSMbEqrQsGvZVyO3C0y7MBkMVKS1Agg9jH6IXCiRhNpASSGBOI3eXdx0V3t0Xm5_f2yAuolI1MXnFjQG-nr_Dre-HuWEJU8II0IBgdw7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQyBLzKRdHU0OWvxXRHZ5mtj1VkeSnMpS7CtYCxM286fsVd35D7f78jVDFp7qXMIAeqb6WqhyuLOIGILoxTHfv0w825vnHwxZwR8tTupv6qiRGAMdPM_Xa2SKlVoat1zlUGNX6DNqonviDc_n9T7_B16IC4mHNEGm8R-SpT_R4kiUNiUNsPVHe1viQfWq-zPzfb9HJC2vlPsCTjgCK9ItsUq_P4Z88n2yEMtT2RH2lmzCteFYCJ3dmSRH3wswCkQoGjwum55fMZOvpWhxWbmuse2xJj9FaXfOzM-4dPlnW2z08Jf8bTclfPjeXnyXKug-vEb-3VSInmGIpxWTZItGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
طبق گزارش سایت Score 90:
✅
احتمال پیروزی تیم‌های ملی در هشت بازی مرحله یک‌هشتم نهایی جام جهانی
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98179" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهرداد صدیقیان: چون رو جورجینا کراش دارم دلم میخواد پرتغال قهرمان جهان بشه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98178" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🙂
🏆
🇪🇬
شادی سم محمد صلاح بعد بازی دیشب و صعود به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98177" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwhfWmdVpQTSLmgSz1cuFVtFxQr-x_r-lfsVKa0sPNra5_sO5EpLaucBhBRC_Y3m3SeQKINRTK7aQ725OaZUkMglZkwbS7xR_9DW0FcLwHVSaKGRHOwT7TZ1QbuLXTUjLEr-9JxRdLfTnFhXsIPh0vnn-lG69z98FYHrhwD67UseLC0XGG-6oA66pMVFVIK21gm2ZrsjAzI58UOKBfKDtq8dv75dlLd_WCNaTYUIBPhNToQOO4HhEyZwmDMyS-TiDg1MLCVfGR7aMRNgBoefscTM29KNtXU4mB6PhC1WuBlwBYK0-JUamKpC5ah0C5T9KRG0Hxbp_KV0H6TmaLpduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
میگل سرانو:
باشگاه رئال مادرید اعلام کرده که منابع مالی نامحدودی نداره و انزو فرناندز، هدف مورد نظر رئیس باشگاه نیست. فلورنتینو پِرز، قصد داره یک معامله بزرگ و مهم در سطح جهانی انجام بده و معتقده که اولیسه نامیه که باید به این تیم اضافه بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98176" target="_blank">📅 18:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
😐
مهرداد صدیقیان بازیگر سینما میگه تونستم مخ دختر مایکل اوون ستاره سابق فوتبال و برنده توپ‌طلا رو بزنم و حتی برام هدیه آورده
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/98175" target="_blank">📅 18:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gudfLJ7XJyeEgfLhUAwMtnpX8EkxjI9FMfP4NMFdMgXT3FrNiinpUadxEOq07AQISRq7xHrrUIRLo9Z9MqIkmWBmGUrYX0OMyqpVcMoXvlQsH0Lplg39ixDVLONNBP6QvxhNYfhi69vI7U33LQxetWdpCWmcr3V8FMfCCXaYaVHzBSi6rYVAAXfmW1TwoMygQ9XOito8ZLJ0PIckNFsCaOXuA71sc6KRnWcpCo4BnW_Pfke6TaSxB5Ob3f2LWcF0VMS-KRwTQsb3KIxdv2WoSoaXlDL9GtecMdsYSuWkjsAW-xpEPIp2mkD0bLj3Acz3qseU4C7EuJTK-sP49dedKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇭🇷
اظهارات فوزینیا، دروازه‌بان تیم ملی کیپ‌ورد، درباره مسی:
‏" به او نزدیک شدم و حتی فرصت نکردم زیاد حرف بزنم، اما او بلافاصله به من دست داد و گفت:
‏' عالی بودی. تو یک دروازه‌بان فوق‌العاده هستی. حتماً مردم کشورت به داشتن تو خیلی افتخار می‌کنند.'
‏ شنیدن چنین حرف‌هایی از کسی مثل لئو برای من خیلی ارزشمند بود. از او تشکر کردم و گفتم: ' ممنونم، لئو، تو بهترین هستی.'
‏ سپس از او خواستم پیراهن بازی‌اش را به من بدهد، و او لبخند زد و گفت:
‏' حتماً، آن را به شما در راهرو اتاق‌های رخت می‌رسانم.'
‏ این لحظات را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98174" target="_blank">📅 17:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZoNPfkkWFkPnksXzK9IwkYDilCZM4Jp5NZwpZ-a1stOeSpp-ugqaqZQjrRqPhrDdOk9Rfi4P0kZW99pmqkuf3zZzx1shzU3kb1_745F912rI5OmgATx9S7UYXM1JB_RURZ8RAHk7VlUdMSyQoq_blzSIP5jI_h610gAXLqFA1goamksSisEUeiRJ9lvJG9XJ1HL3tiVDD63OcUxxcFeWQSI8ZnVTN_k6vuffkf8RaxCaNPRklrBcYv37vXXe0-ZTIWJ58Sc6lCw1qGEA15RQ1CBWqxElZjfMoD632635STuqnzG-Rx4lJ8fDPbY7yIvQQ66WBChb10wzoD5DrQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=babGz-6iAIxqukzJHl458u1RSKgxe2tR7ty3Q9fqs12vUyRtsvZl8nV5HPZfhAGXxi2hcoRPzDGfxLks_e-0aVxY2HHEEJDZxpDi3XIVMMNWpGlaV9dq2TSAjPBzrkd8IsM-mKL2TRHaMRPYrKaKQ-LLio4lQKdqml9TJScIXSNEceC_bl8Qk_dBkzyK0GcOCyJm-lBiIAIdsD3ODrXp2O1Eb_aUphN4CFeiaJJ5elhsY_GZfElrcGzvGPrMC3AqV9FwGX-vuXs4NjlpeEaAc3y51X8zypPW9XfoOrsORww8Sw_J43tVVlIe89nB9nkM6D-jFV_71nHhKBpRZQuTcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=babGz-6iAIxqukzJHl458u1RSKgxe2tR7ty3Q9fqs12vUyRtsvZl8nV5HPZfhAGXxi2hcoRPzDGfxLks_e-0aVxY2HHEEJDZxpDi3XIVMMNWpGlaV9dq2TSAjPBzrkd8IsM-mKL2TRHaMRPYrKaKQ-LLio4lQKdqml9TJScIXSNEceC_bl8Qk_dBkzyK0GcOCyJm-lBiIAIdsD3ODrXp2O1Eb_aUphN4CFeiaJJ5elhsY_GZfElrcGzvGPrMC3AqV9FwGX-vuXs4NjlpeEaAc3y51X8zypPW9XfoOrsORww8Sw_J43tVVlIe89nB9nkM6D-jFV_71nHhKBpRZQuTcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
رفیقای من وقتی دختر میبینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98167" target="_blank">📅 16:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98166" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98165" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی و مهدی‌تارتار قرار دارند و چند گزینه عجیب نیز به گوش می‌رسند. از طرفی نیم‌نگاه برخی اعضا به بازگشت وحید هاشمیان نیز می‌باشد هرچند که بنظر با واکنش خوبی از سوی طرفداران پرسپولیس نخواهد بود
❌
در صورتی که با نفرات اصلی ایرانی توافقی صورت نگیرد، گزینه‌خارجی در مراحل بعدی مطرح خواهد شد که به اطلاع شما خواهیم رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98164" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇦🇷
گل‌سوم آرژانتین به کیپ‌ورد از این زاویه جالب و دیدنی تماشاگران رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98163" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7fZrcticwdUcoD-5WZJ1wtTzdL2lNowtg5TJqgYibThwdlP1Am4_syUyW_Ub9M02lI7lwBNqMEvjNobW8_fyFHdxkSPHI9SXCQTkDYAGmnK9q0ITyu5E6AIDDi9CImT5xVtLXj1QzY0Z9lFASuncJlVDEeysdHcZ2hlpSeJFO0pgPigPGHmeA6teJ3jCV6RZJTEG6rBOKpFl7nhKbMIneXhZYwel8_DJWcXdlGMtSdtgovkbuaKnz3FnXVpqJ2yU5X-_BtyAgLhdLhZG1i3zaqkyv61VgOdhkPSzF8TZQJd2fFP_Ev7pZPEmMCV5JbjnhZDljT5IGF5a4iKnPR-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک فهمیده رو هرکی ببنده میبازه، 1 دلار بسته رو صعود مراکش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98162" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98161" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98160" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=og757xYae5irOiAVurlqPsLOzPmUZ7oAMVjQS7sjN3vW1fXh6yKp3OPcDjwlwVfKr8MZaIc_-98TzZsr5qpO1SH5DoBBy3iY2x_T_Qb0KNcfLYLggiNl78TOeElbjeSp_FEAoS1QwhcQvfFFXcHudjS3HWjc7SjmICgQ7QokMC2doHzAF5eK7ECdSUmsu21My9_N5eNIdfsTGFsxDAN5jF2AfxSoX2va41EPDW2YQAuvmYsvMkma3LUER-2UddyNrxXQhGcR4gotfCu7y5ICTeaBagZmSAWTnsZW7Qq6qT6ukEr8nWpruvnn6u4fGNR904vT-9bjessLAK8gBdXeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=og757xYae5irOiAVurlqPsLOzPmUZ7oAMVjQS7sjN3vW1fXh6yKp3OPcDjwlwVfKr8MZaIc_-98TzZsr5qpO1SH5DoBBy3iY2x_T_Qb0KNcfLYLggiNl78TOeElbjeSp_FEAoS1QwhcQvfFFXcHudjS3HWjc7SjmICgQ7QokMC2doHzAF5eK7ECdSUmsu21My9_N5eNIdfsTGFsxDAN5jF2AfxSoX2va41EPDW2YQAuvmYsvMkma3LUER-2UddyNrxXQhGcR4gotfCu7y5ICTeaBagZmSAWTnsZW7Qq6qT6ukEr8nWpruvnn6u4fGNR904vT-9bjessLAK8gBdXeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عادل فردوسی‌پور: اگه همین روند ادامه داشته باشه، علیرضا فغانی نیمه‌نهایی یا فینال رو سوت میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98159" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zyk8YQn4frQYhnv9unwjDjg6dvb1OLD5JbHFcCR36QF-AF8oBgI3HiVllXouYGom6FX2zDSA4PaHPfhPDxOCodPzJfND-Up1jtvaB02XmRPIU7e8Ut34m0DmrPG0ddHd-lhxtbvyTL4i59ngqTSz8SUSkCglRxoXMQmSStnUmiEi6yFG_XH1OkSAS9rpB5o2ftKbqZix2MznCYEZWmU658Bl2PEuwqkXeZdk-QpA5fbQTjV5wedbM8-qtR2d2ekstHhyiuor3dDmfeo2NzRbpqIEMI27cjoU6Or-p_RLluyjMIgyCSVJuQTC-PsHnqo4ckKAtTJZpeAO3cudEOdO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
هوادار جذاب تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98158" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح‌الله‌زاده اومده برنامه ابوطالب جلوش یه لیوان آب گذاشتن و بقیه ماجرا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98157" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhVEa3_34w38CZbOCP3o41SYGKIi319cOImbazEy9Opb47J15VXukdA1kSugqJyY6SvgLw4_PdQ8J0S8zUm-xJ3DxVVTngKeLXC8qO1Bl68UorJNCeq57qXRhMv3eG8EXw4eHkvJgVnaXtAZrJzAFUQ9GGr4XpNycFLGBxmqC-wRL3bBLz6KYs3HcYKqWE_x5yldth6-riaxcS6q1QwZF-CtB7--PS8SQy4_sjXE8814olRVPH4xOApR0MO3-Qrn6YRT7nMp63VhTzJ2xdUpfQVA6fg8l9L6qeW41PIRA64DJEGhd5lJaTB4xVtkknyL4bAF5FmT8TPT_5DJO3n9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
حمزه عبدالکریم بازیکن مصر در پاسخ به سوالی درباره تحقق رویای دیدار با مسی :
🔹
ما با آرژانتین بازی میکنیم، نه مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98156" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
دل‌هارو ببریم به سمت بازی Pes2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98155" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💥
▶️
عملکرد لامین‌یامال مقابل اتریش که هرکاری دلش خواست انجام داد بجز گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98154" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw3KdmnNZl22WGkZ2OSBcDOnym6OsmpHghWzGZVQruyWCvUAaP0rqTpszQ14VzMlDPiKbLfOt7mBgR9foofmvTVLOLri4TlJH3L5Mao56Jen3Rm6EU68l7vn5vJAzQxnmEkgxKM6SO8cvu5uWFlYCKMzMYuHuIQLBtUeLqzGTudIU7p-K8aZ8AyVhAQQgRye_YZCDP0Qkdm3tNVkdfKn16bu1sGTPbadR2om-LjxgteEqWWe3ajFcN_kL56j-bMPbBYeWE3shhCfB_W5xZmS3-OcB1wJ4MES3mdQWgzV2DrbJSmd1BzBPtX6clADmg3WnZXbjF1FJSdsSegKEV6WsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که تا به امروز بیشترین موقعیت را در جام جهانی خلق کرده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98153" target="_blank">📅 14:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOpyv5tgXFUu2W-8f9Xs9zFxk0Dk4XBRAcrWGGWvFJLRALiB93bDbzKDlzj6_LWIsGvbje2JM-Df_who2x1eGXuYx0EfOtMAAi2-eGWI97wDqXRXN9Naw01EMJ-itNrCF3BfltN0rJTIK0XXhTJ4cqc3mPqqoIWS-reycIEsbYoiBQmn--idyBHKZDtl0FOM-bGBPMEVfrNXbBlFooaNdUX7CxWEVfvU7gU3gqlcLIowyGjXUtMRigmtEB2_grZ3-F5G4GRrEwB_xqykujktqtL8SYNsUifTQg1KapI4Z1PbdGbq0c_X5L8KFkmqlKIupfR-uX1clZr9BBPji7JJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله یک شانزدهم نهایی جام‌جهانی از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98152" target="_blank">📅 14:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=Cb2p6gIjA01T-IbxG1W2Rtwu2M-sSptdjNVfQmdmg5qEty2RlRfSAK58h7qKna5KupsfxsVrSnea5H_qChH4QPC0L6nu1faoZ6PN8ztQnNYx4dOOXy_A5_Z0wdgZIyKRbR5x6bVVALYGsx2bqnI4Jx6yyl-LUAYgmdNzpOw76_-4AH5-vxJ1TfZ0-_odzQm_FIvOg6-Q_QmmBQaPYaUGCmYnxarQl2cyxLswW2X8yfurYkY5SBcXg7WQekAMq5esUblR-a6ffJACKySmKhKNgteGUiZC4CCyOCLmLkJ_Ho70fHKbx74sR5qHSyZj9mLNT3SqiTOgmQgp6vCAq9Cy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=Cb2p6gIjA01T-IbxG1W2Rtwu2M-sSptdjNVfQmdmg5qEty2RlRfSAK58h7qKna5KupsfxsVrSnea5H_qChH4QPC0L6nu1faoZ6PN8ztQnNYx4dOOXy_A5_Z0wdgZIyKRbR5x6bVVALYGsx2bqnI4Jx6yyl-LUAYgmdNzpOw76_-4AH5-vxJ1TfZ0-_odzQm_FIvOg6-Q_QmmBQaPYaUGCmYnxarQl2cyxLswW2X8yfurYkY5SBcXg7WQekAMq5esUblR-a6ffJACKySmKhKNgteGUiZC4CCyOCLmLkJ_Ho70fHKbx74sR5qHSyZj9mLNT3SqiTOgmQgp6vCAq9Cy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد صدیقیان از فوتبال دیدن فقط زن و دختر بازیکنارو دنبال میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98151" target="_blank">📅 14:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE_wH7DNFvj44cwZd7t1j6kOmITCPEFASyXNXbFZOkIoddGduzjFCwm0doGr4WfHgrMyyyiMBetNLIDdG-hT0sIiF9NaLr_uhoB2zFUIKSSLtRA5CsiNEcJZXkjBCrfaVnTNma_ZXV6rCAsvQa0cXeEgwEBBVLcbw1h1vS8dumdqNa0zKiQKFQ3RgXk7MiOR8BFLqLNXbarHNFi4RRd8Puc-a5BC8dBrtIk9G39Uu_BEqIjtClp9QH0hWhIrFsp0dTO7ipow7OdO3S7p7LUCQx4_VMXymOj_WkJ71kvHDE_h0ViyRuiSrI3R_qG1kWlXuhFgoNEgzYcwxFa3Nvxg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جیانی اینفانتینو:
‏"در این جام جهانی، مسی با یک سبک فوق‌العاده و شگفت‌انگیز بازی می‌کند. ما او را به خوبی می‌شناسیم، او یک بازیکن نابغه است و همیشه خوشحال می‌شویم که او و سایر ستارگان را در زمین مسابقه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98150" target="_blank">📅 13:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=LqcrslnaGh7yUggc83309R4W0d2y6PoIcQm-irxmBtfn3j30L7hoVsU_d9KoYmmcrdYHUwFpGPwKDc-_sHeH3JAi0tloHuScfADMqK3GFSdGCMhNbtlktrHiPy3KFrTE56_BEFYH83Brjjk2v1cc7hYdy4qHmB-Iu4Iy8NtWSQ1qAfxYeoEwfigmttnz8CXH5KXDdmZrmf5cPDJ74CMgjBWeRuVXgK0ASqaJLmAJq1hLr59aePYGMYN3mk5OlHClDT93lGVjwbEspB-sKF5wTKGbky6UG6WIiV075SLSqpAhNwd21niPJOS7NJtg5IawgFKKAS78wDawWlGX_9VjpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=LqcrslnaGh7yUggc83309R4W0d2y6PoIcQm-irxmBtfn3j30L7hoVsU_d9KoYmmcrdYHUwFpGPwKDc-_sHeH3JAi0tloHuScfADMqK3GFSdGCMhNbtlktrHiPy3KFrTE56_BEFYH83Brjjk2v1cc7hYdy4qHmB-Iu4Iy8NtWSQ1qAfxYeoEwfigmttnz8CXH5KXDdmZrmf5cPDJ74CMgjBWeRuVXgK0ASqaJLmAJq1hLr59aePYGMYN3mk5OlHClDT93lGVjwbEspB-sKF5wTKGbky6UG6WIiV075SLSqpAhNwd21niPJOS7NJtg5IawgFKKAS78wDawWlGX_9VjpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇨🇻
ووزینیا دروازبان کیپ ورد پس از درخشش مجدد برای کشورش مقابل آرژانتین:
"تقابل تک‌به‌تک با هر بازیکنی همیشه سخته، به‌خصوص با بازیکنی مثل مسی که فوق‌العاده خونسرده و قشنگ می‌دونه چطور فضاهای خالی رو پیدا کنه. برای همین مجبور بودم خودم رو آروم نگه دارم و تا آخرین ثانیه ممکن مقاومت کنم؛ خوشبختانه موفق شدم توپش رو مهار کنم.
بازی کردن مقابل مسی یا هر کدوم از بازیکنای آرژانتین همیشه خیلی سخته چون اونا بازیکنای تراز اول جهانی هستن. اما این رو هم دلم می‌خواد بگم که هم‌تیمی‌های من هم لیاقت این رو دارن که توی بزرگ‌ترین و بهترین لیگ‌های دنیا بازی کنن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98149" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=NCnrw-SkXLa3e_asrpY4VuxWzWIvqFQKaer5mpmWoLhKKJeqnOnK05CIezJA--tys30m4BgbWiKYVaSOC4V90rD8koztNVYmr4wsnFu0QXvQBE76uvvATqpemLz51-enlDRYaK-SRQ4xCybbs43kNMSmP_v2UG-xvqhZKbDQaMiPFUJatTujkLY-etwf8eVIihNnQkDWoEXrRtk_CxviJOKQNrqyKo60cvY1R1T5AqNlkH2TJD8LhoL0GWl32f6uoExIIPWo2DXKbYnR_AWRHPCPtHoZZYmwOxZsdEvv7cz8CwKbFdVTBkQMMRcppf74dmTM6u8XE6b_Ygjm-Yg06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=NCnrw-SkXLa3e_asrpY4VuxWzWIvqFQKaer5mpmWoLhKKJeqnOnK05CIezJA--tys30m4BgbWiKYVaSOC4V90rD8koztNVYmr4wsnFu0QXvQBE76uvvATqpemLz51-enlDRYaK-SRQ4xCybbs43kNMSmP_v2UG-xvqhZKbDQaMiPFUJatTujkLY-etwf8eVIihNnQkDWoEXrRtk_CxviJOKQNrqyKo60cvY1R1T5AqNlkH2TJD8LhoL0GWl32f6uoExIIPWo2DXKbYnR_AWRHPCPtHoZZYmwOxZsdEvv7cz8CwKbFdVTBkQMMRcppf74dmTM6u8XE6b_Ygjm-Yg06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98148" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRVaIck4xSb7bwaQHM33peOTF1Caxuit9dvLEW8ULzYzTb7i95n--zy6Fg692TB46S_GlfDO11pzIEhxzuljmAQWf1Tv1k6QK97ZX-cE7hb3ORc7UC26gRXmBpTyEsr9LkogixVYYOzWWCm80fhJp8Gzqpk1tyIQGzXyCgygdETRSNWLNJU8GJq5h0WYm4gCzVQQipHO1wkFB62zt6m5uVewyrQ9uvTMUA1hxEGOlSwyBmeg41AGsmz-SoRJYKvM4px-c4yrTmci3gvXSDB5luVzeJ4Y_TG7Mh63mF3da3FfXrt43tcPC0Ip-fQZf5YaM0dO3DqIX2Ak5cJbWIXnXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98147" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=QqWc6e_hF9d0jPi0eIRv-GuVrgWPo3XAbPHf5eICMC1tD_MLaX40LB__4kOcxRcH-KuyxRkOgyP8FYloZSjjO76vRbZzV-BgrZOd3l6PutGLVE5ZVxZQcpHjiMz-SwaLHpoBTgMoawjqYSu5-bWQCSJVT3__JCZOypnN-9WDorxNfwoX5b4SVKkCgwceCrXekVGktRe6w963ZVHrsAtzh-wpZ5-XvWVVjEHbezLtwUBGF65cjIdstE3IvuJvoKNXKz2CSEGrvjx70ROFVojT2NBzSp96sJlP_KE898GRUDLKXCewmdk_0vtGsh5Nl7fF2vUde_T7raGJdFIuj6xX43-7wxBvqgyK-O-sz2jo5g1C1HCwz_wQ2kkb1x3QXqgOqKbeF86ICCokGCbpXvtG35sGw2d7SHPPAQHoRjJyso5Gvo9Dci96n85EXKL8HrHOJ53HTM07tG6Ez_jd5oZ0CEm4yIfY38WGEdx9y17qkcCe1TxBKzydozrSsS36uA6TuY0ljWfHvJYABU-AA8CBoUUYg2_iDG4TioI5JACM6x7OfROO7EyW6nJW_QLpvHSiwocENNv69Vk5TNggq4ewmT4QymylrxpGdHleQrtBERs5FnjDLi6ijJiIFeM9cNG1xxbk-XdSqbCyeLEkWCl0IGJ17g4CrAWhiUBsbVYHC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=QqWc6e_hF9d0jPi0eIRv-GuVrgWPo3XAbPHf5eICMC1tD_MLaX40LB__4kOcxRcH-KuyxRkOgyP8FYloZSjjO76vRbZzV-BgrZOd3l6PutGLVE5ZVxZQcpHjiMz-SwaLHpoBTgMoawjqYSu5-bWQCSJVT3__JCZOypnN-9WDorxNfwoX5b4SVKkCgwceCrXekVGktRe6w963ZVHrsAtzh-wpZ5-XvWVVjEHbezLtwUBGF65cjIdstE3IvuJvoKNXKz2CSEGrvjx70ROFVojT2NBzSp96sJlP_KE898GRUDLKXCewmdk_0vtGsh5Nl7fF2vUde_T7raGJdFIuj6xX43-7wxBvqgyK-O-sz2jo5g1C1HCwz_wQ2kkb1x3QXqgOqKbeF86ICCokGCbpXvtG35sGw2d7SHPPAQHoRjJyso5Gvo9Dci96n85EXKL8HrHOJ53HTM07tG6Ez_jd5oZ0CEm4yIfY38WGEdx9y17qkcCe1TxBKzydozrSsS36uA6TuY0ljWfHvJYABU-AA8CBoUUYg2_iDG4TioI5JACM6x7OfROO7EyW6nJW_QLpvHSiwocENNv69Vk5TNggq4ewmT4QymylrxpGdHleQrtBERs5FnjDLi6ijJiIFeM9cNG1xxbk-XdSqbCyeLEkWCl0IGJ17g4CrAWhiUBsbVYHC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
فرنوش جعفری گزارشگر دختر ایرانی: رونالدو قبل پنالتی گفت بسم‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98146" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH0moMEQR2WBuZOldQof6-ZX75m5aE8WvdB5ZrokJ98bctekyUCbNiFSXjXnf2Ao_dHXnB3JrtgXb3wGBxndyI9OQ2RUdqBnfiukfnoLCF21lSIHQF-5OBfYSzJrvpsHOcjSPsHvns3A918LZvSzS1dECwbt7uwaSW-iZvDc1ysLLn4mBYuIHnuhb4rKMdE5cp6kLgs7B38VuWRQCuxP1g0SxzzBg0pKgnRAAsJ35zW6-wG0iAv3sQzsr4HZ_NesbojkeDgh_6-j1iBQzlBUEpJVikYJUHA0D-x6gA63PYvOAi_uB4XQTezWjgJhh5_bu92ni2ooqOMRxj7MeFSxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#
فوووووری
؛ شوامنی بدلیل مشکلات عضلانی در بازی امشب با پاراگوئه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98145" target="_blank">📅 12:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=hzgV5lw_UwOkXHQQ6m2piARpVXFs87lCL5UF67zGUs5iyyrlzM6wRibkYuH0gIZEV-r9gMZPm-1wuwChV2yjpFxbmLAO2x6ynVZVOHINX4SvRLyKVqu3dTosavk5lbofRYrCUmrTAykeYe4ifiYsvZhSwqOKOyyL-M_yam7dsKT-cMuLZ0YmeSl__-aKwIky-prjMUIjCNmjKuQRHRGOtQZ1Hg-x6AMeTc93Ir9YQqvsNccPr-HiLQ502jZZrXDUGWKN78nqJf-uX2CS_ekknYlLRE_7530fIFqJLS_imO5h5Jv_bBgmWKJBaNtX03ZA4PYR8CfuyKEOF1eISH3EUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=hzgV5lw_UwOkXHQQ6m2piARpVXFs87lCL5UF67zGUs5iyyrlzM6wRibkYuH0gIZEV-r9gMZPm-1wuwChV2yjpFxbmLAO2x6ynVZVOHINX4SvRLyKVqu3dTosavk5lbofRYrCUmrTAykeYe4ifiYsvZhSwqOKOyyL-M_yam7dsKT-cMuLZ0YmeSl__-aKwIky-prjMUIjCNmjKuQRHRGOtQZ1Hg-x6AMeTc93Ir9YQqvsNccPr-HiLQ502jZZrXDUGWKN78nqJf-uX2CS_ekknYlLRE_7530fIFqJLS_imO5h5Jv_bBgmWKJBaNtX03ZA4PYR8CfuyKEOF1eISH3EUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👀
دیس هادی حجازی‌فر به حسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98144" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=uccQEPnB1XCy8-hGrr35G7fZPN080rpRx6EICAKfWqpZo8EoVuiF_3HvmbxdVNuyMSAGQFmgFN4wFoA6cvnPupExQvIMzVh77VI7IIpYhGcDc2nXI8eixAtsuuFcHYxS_q-2OkqGOB3cIXCojGPjHCVFbqlOCJyrJ6U7lndCu9nIwceKrIQuoCPbqK6bzuz_dAW4asdMYSUEAv1WPic5-pUsuIKL_YW2sDV0IxzbsVI49FQwX2oGWl1Pd6A6T-4Bc7ng0QRxHG4ksax4sdT7bZaYW11CTpIte8gE_dqwlf-W1pq4OcMoRk20E8o4J6-0BptEdPjPKtBQlL0knH7z6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=uccQEPnB1XCy8-hGrr35G7fZPN080rpRx6EICAKfWqpZo8EoVuiF_3HvmbxdVNuyMSAGQFmgFN4wFoA6cvnPupExQvIMzVh77VI7IIpYhGcDc2nXI8eixAtsuuFcHYxS_q-2OkqGOB3cIXCojGPjHCVFbqlOCJyrJ6U7lndCu9nIwceKrIQuoCPbqK6bzuz_dAW4asdMYSUEAv1WPic5-pUsuIKL_YW2sDV0IxzbsVI49FQwX2oGWl1Pd6A6T-4Bc7ng0QRxHG4ksax4sdT7bZaYW11CTpIte8gE_dqwlf-W1pq4OcMoRk20E8o4J6-0BptEdPjPKtBQlL0knH7z6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
رییس جمهور مکزیک: از مردم میخوام اگه جلو انگلیس بردیم، زیاد مشروبات الکلی نخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98143" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=n3Rw2kG3W0PRQ-Qjp9TNhrhkk0Xq-ys5SpPAkKm9ikqtKgvGqrGr0qfiq_fn_pp6f2PuiG5KBqATSN6-oO0SEYwNpzL3qF8VvuxqQ94RD52e2DAw6eiMT0sA_BwMY88S7Rzzy260piBYbQlJ8kYLnZUiTMDYOCqBidvmGdFfI5YFKGQ7FgEgBxSJA-83ZCjHJ3pg40fxuPIAv6eLtozBnfQBDeLdJltiVrb9PVWNGZj7Q6WGLaT8H8nu5t3d53gI2DZQRRl5IL9m-Vm0UDa39Cq8S1O_jKznF9NKKv-eDnJRD1BIdnaxRRvnA7iycUGwo5cYWYIZjy78gyuWIPSsNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=n3Rw2kG3W0PRQ-Qjp9TNhrhkk0Xq-ys5SpPAkKm9ikqtKgvGqrGr0qfiq_fn_pp6f2PuiG5KBqATSN6-oO0SEYwNpzL3qF8VvuxqQ94RD52e2DAw6eiMT0sA_BwMY88S7Rzzy260piBYbQlJ8kYLnZUiTMDYOCqBidvmGdFfI5YFKGQ7FgEgBxSJA-83ZCjHJ3pg40fxuPIAv6eLtozBnfQBDeLdJltiVrb9PVWNGZj7Q6WGLaT8H8nu5t3d53gI2DZQRRl5IL9m-Vm0UDa39Cq8S1O_jKznF9NKKv-eDnJRD1BIdnaxRRvnA7iycUGwo5cYWYIZjy78gyuWIPSsNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇵🇹
رونالدو با ارسال ویدیویی به پسر بچه‌ی ونزوئلایی که از زلزله جان سالم بدر برد ولی تمام خانوادش بعلاوه یه پاشو از دست داد، از اون دعوت کرد که یکی از بازیاشو از نزدیک ببینه اون پسر هم توی بیمارستان این کلیپ رو دید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98141" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=raFQrcOWtK9ZN4_gyx2bKLjj12P97L-cl4N7TlQsF2FTBOyUWAVWqBEKu9MqYmuR_3oNXsP9W2haZmc4YGs8wtdxnj_DCyfjY1lk0vLVxn-xRf0SeTeagwWhWXrinlhFNtE7_xXVS1EvpHrolm7x5DIexJdgPNOvg6Rj_fS4ZiQFiwGCjm3HbAaw55rCRwx8tlxELKRGPVnoXDXknBVKnMbqxKzRXwR2IZoyG0WjvqQ37EhEjUKNVzlhHwyYkE8wPRKFtOiyz5D9KZZ5qK3M4BwdKjjfkJQ2F3ENeCGg9wIj2HsfWBl3ScYTzDImGLXm-YMkuD4AkHFNJkg4jWqQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=raFQrcOWtK9ZN4_gyx2bKLjj12P97L-cl4N7TlQsF2FTBOyUWAVWqBEKu9MqYmuR_3oNXsP9W2haZmc4YGs8wtdxnj_DCyfjY1lk0vLVxn-xRf0SeTeagwWhWXrinlhFNtE7_xXVS1EvpHrolm7x5DIexJdgPNOvg6Rj_fS4ZiQFiwGCjm3HbAaw55rCRwx8tlxELKRGPVnoXDXknBVKnMbqxKzRXwR2IZoyG0WjvqQ37EhEjUKNVzlhHwyYkE8wPRKFtOiyz5D9KZZ5qK3M4BwdKjjfkJQ2F3ENeCGg9wIj2HsfWBl3ScYTzDImGLXm-YMkuD4AkHFNJkg4jWqQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تکرار ادعاهای کسشر فتح الله زاده در گفتگو گو با ابوطالب حسینی: اگر مدیرعامل بودم مسی را می‌آوردم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98140" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98138">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu97vjV7L_YLtb5jB-KB64DdP7KYlKs9GTHswjKuIGtUlVcmIqOXCpoSCXonHOTLzynHlVVZ4Vv87ptxsUYVWQp1exhPz76VZTcQhYP8A8IlukpvEcIyHg1DGducH_DE0cl0c_6doL9LvWZVqvdO3Z-Wbb7YofsKkmQhkuhqS1Ahz862rzYpLPn9cjy9lVddsUEiULC9Ve6V1s0TmGr0mgGsrysoJhD0iRIPmYmCCq6SvxFBHz9FagmggJNLIq7gZEqvHV_Mj3Q0EPZuVE01WnruddpTH3Wt_NDKKyEKiXewtQ25521Pe2k5chgRg2d_bzSPBctvgl4JzVwO4_Dg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcZzqfXnNJufW7Q2A9qRiBB_O-EIPFIUEiZo3PKcaMEULBRzTYsSVejcoFU8fQu0QcUAJ07dlFWpOcS99BzgvEot97ul2-HtT80xEcIE7rvqUWfjGq6vIetCJVTCQz_L7fOynZqjEAcH7rOsV8bBFVFnwq5R3BY8_mOJ8K6Pi3N0hhM_7WwNrWVBwArdWx2MxsIuO8VPDZFrGTR6K70-P5zAnFfJG-FBR0kj_2Zhnk6Bv6NT8xuQ8ALNlPN9CjdkMSuBJaLSKleWd4Yg5JFyhe4W9G7g58jcmuyqYnbCOMGAskA3RYH90JwKAPjAozScA0RbUBIcYqjujvfKpdrpDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هتل "انگلیس" در مکزیکو سیتی، به دلیل نگرانی از احتمال ایجاد مزاحمت و اخلال در کار تیم توسط هواداران مکزیکی قبل از بازی، با تدابیر امنیتی شدید و یک "حلقه فولادی" محافظت می‌شود. نیروهای پلیس، واحدهای ضد شورش، موانع ترافیکی و گشت‌های یگان‌های ویژه ارتش در اطراف هتل مستقر شده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98138" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98137">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=BSAmdyYAgq04vQRenQ-j9e531qlFYFB0P-TsXM8oV9xi_rAzP6YrGy1CPyLmAnb7fNqAwL1AwLNEzoWRQFYbKAEAhrIIsvAkBfdPKDNXky9GFYeNfwhYf5mhH_-MiwqFN7OsQZEbqmsSJ84mQFtQ_1-Ce5mS7VGgIFBrP6vWguvH3Rrie9O_KzkppOBlYuV15lLuNXhKlYqrEERw-kVz9QZsl9MKJoMfxFZV1iHZ7gOin01dIPErJ4Lrcf84lxC_istGflrk9kYtm0ZiWY_2ATB7LmBbY87Wczl-oxdMP-10WvLKVivyAu5koL-_Tif8VDZF2abX3qU1JTUxUYxBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=BSAmdyYAgq04vQRenQ-j9e531qlFYFB0P-TsXM8oV9xi_rAzP6YrGy1CPyLmAnb7fNqAwL1AwLNEzoWRQFYbKAEAhrIIsvAkBfdPKDNXky9GFYeNfwhYf5mhH_-MiwqFN7OsQZEbqmsSJ84mQFtQ_1-Ce5mS7VGgIFBrP6vWguvH3Rrie9O_KzkppOBlYuV15lLuNXhKlYqrEERw-kVz9QZsl9MKJoMfxFZV1iHZ7gOin01dIPErJ4Lrcf84lxC_istGflrk9kYtm0ZiWY_2ATB7LmBbY87Wczl-oxdMP-10WvLKVivyAu5koL-_Tif8VDZF2abX3qU1JTUxUYxBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😎
بهترین گل‌ فعلی جام‌جهانی از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98137" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=kpe-DY-cLkvXMW5QieQd0iJI7n2rDePZOlAGnZjhygY0Y8_ciSz5XX6RqODUasMo1KMyEEKi0A-sLmu8KJTdVrHe115X-0o_j9ddWt1vkpXxFE22gDHDQl-4ojG4iUCG4QMzTVPh8k5qVFkB-T33QnemynCCbYfmpVx7c1jIxcMQK7e2bZie8z3QrGPY3ep5bhQ-bO2bDayqb-NiiO1c698zR2KeW9cg6_jEyzgXUUIh_5SpU05jV16Efle7aOtFcexBtDuYGte8p1jTEzJqiy8cVf_E1hnKwxqaMMODFDNzcTCwLOaYZ3IbVztKH7dyaW33TaHJmfaEHYK7uwxftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=kpe-DY-cLkvXMW5QieQd0iJI7n2rDePZOlAGnZjhygY0Y8_ciSz5XX6RqODUasMo1KMyEEKi0A-sLmu8KJTdVrHe115X-0o_j9ddWt1vkpXxFE22gDHDQl-4ojG4iUCG4QMzTVPh8k5qVFkB-T33QnemynCCbYfmpVx7c1jIxcMQK7e2bZie8z3QrGPY3ep5bhQ-bO2bDayqb-NiiO1c698zR2KeW9cg6_jEyzgXUUIh_5SpU05jV16Efle7aOtFcexBtDuYGte8p1jTEzJqiy8cVf_E1hnKwxqaMMODFDNzcTCwLOaYZ3IbVztKH7dyaW33TaHJmfaEHYK7uwxftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپ ورد سرانجام تسلیم شد.
💔
آرژانتین به یک هشتم نهایی رسید.
🔥
🇦🇷
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98136" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=ff5bG1_CCzuiqxMzFTcT5JYSs_04rcI9CReUnHaowYoc-9QkaBCVgxz_6ylP7tWKgT9gnDEy51b1pBRxpVUJPx12dxkb5T6a3Tq2a7uGWsZZl43rENx_W9vHpoYIztxcBcntzdrX_jbLfZRTYZTnTZPZmH3jAPuoWWtqVeUlbIDD8OPF0c0h0ugj9ehnD8nyN-xKn731-ksHJq4UrdBEYd0CeGp5oNHehSMiogl7XStmFAeLoUYCX1GL5gNbOpo381oL0nE7njsw2lqDCRJToCA64GoJz7HFuzN-ZfqFfU1qEdO5_vRIAVoGjk8gIJKM5fYUYcih1jFYd-uN7rZvGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=ff5bG1_CCzuiqxMzFTcT5JYSs_04rcI9CReUnHaowYoc-9QkaBCVgxz_6ylP7tWKgT9gnDEy51b1pBRxpVUJPx12dxkb5T6a3Tq2a7uGWsZZl43rENx_W9vHpoYIztxcBcntzdrX_jbLfZRTYZTnTZPZmH3jAPuoWWtqVeUlbIDD8OPF0c0h0ugj9ehnD8nyN-xKn731-ksHJq4UrdBEYd0CeGp5oNHehSMiogl7XStmFAeLoUYCX1GL5gNbOpo381oL0nE7njsw2lqDCRJToCA64GoJz7HFuzN-ZfqFfU1qEdO5_vRIAVoGjk8gIJKM5fYUYcih1jFYd-uN7rZvGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇻
خلاصه‌بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98135" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=WUZz5euCz2SShfGozFNSe1dhwuoKIpb2BYftz9KEhySLPff92zcigkHqVLq4NwFE1Pzhn5K8tISTZsQ5vf4--6x0a9qhzeFfsJzCt0QPEzNd6fxXxgWo8A_XmARcXLmZDElNpi1UlkagZ6gXNT0wtX7xB8rrtylOdhdntBvDDhgnwTcL7NXhmfaGJ58gEJiB9rbrR5D3XbkQCKlNN-ttEbSqWwsm_dFKwLW0E06WPLsKX4rSHbjcj4tRg7YB2olLog_2It6RJ_u4XL_CawpQ6hafjBEV3E_UeYBZEFqmWtVrel0h1DbCVFMer4gzhNmJGBqByRggnhaYwKXEqULNmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=WUZz5euCz2SShfGozFNSe1dhwuoKIpb2BYftz9KEhySLPff92zcigkHqVLq4NwFE1Pzhn5K8tISTZsQ5vf4--6x0a9qhzeFfsJzCt0QPEzNd6fxXxgWo8A_XmARcXLmZDElNpi1UlkagZ6gXNT0wtX7xB8rrtylOdhdntBvDDhgnwTcL7NXhmfaGJ58gEJiB9rbrR5D3XbkQCKlNN-ttEbSqWwsm_dFKwLW0E06WPLsKX4rSHbjcj4tRg7YB2olLog_2It6RJ_u4XL_CawpQ6hafjBEV3E_UeYBZEFqmWtVrel0h1DbCVFMer4gzhNmJGBqByRggnhaYwKXEqULNmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
جدی‌جدی ۲۰ سال از این قاب خاطره‌انگیز گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98134" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=d-vCZ3EP6a3MVJJ7Vl9HDasJnfTW839gDV2hGdL_pZyaZ-YOql-3CMuoGVFQRAwosj6XPRqpRLqtKhGDtAyNjeraDZVxceGLpUWKa9J4yT7UKy99PkBW0UINCN0oZhaaCKNWn-zHi61ubp5bbbJify7ub5ZRgDsOONWZO-eWYrQjNPH-yFEev3nTOJ9Y75SmHBC7E6j241p30JCCevTzx6ATzvoZZ1ujvf4FnYR8eDcB0I5dnXISUjrTNehkVErCPg6LM-6nqQnJkiT-7HSo0hIU6cvr3dJ-DZaa8zf2er4rLpUzQQJU4JK8HU3A0UPtYTSBZOkvVAGQAVm1H8Ujdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=d-vCZ3EP6a3MVJJ7Vl9HDasJnfTW839gDV2hGdL_pZyaZ-YOql-3CMuoGVFQRAwosj6XPRqpRLqtKhGDtAyNjeraDZVxceGLpUWKa9J4yT7UKy99PkBW0UINCN0oZhaaCKNWn-zHi61ubp5bbbJify7ub5ZRgDsOONWZO-eWYrQjNPH-yFEev3nTOJ9Y75SmHBC7E6j241p30JCCevTzx6ATzvoZZ1ujvf4FnYR8eDcB0I5dnXISUjrTNehkVErCPg6LM-6nqQnJkiT-7HSo0hIU6cvr3dJ-DZaa8zf2er4rLpUzQQJU4JK8HU3A0UPtYTSBZOkvVAGQAVm1H8Ujdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مکزیک یه زن و شوهر دعواشون شده بعد بازی که اینجوری مرد بیچاره افتاده خایه‌مالی
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98133" target="_blank">📅 10:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=CQ_h_xmN77ju92Z83ORGbs4Ehl4PaP9gvn_Dor-XPAyF-s5laE3kHeR4orqNHXP3CyBvHIiBYXUW3qrtp4Ebr2z-mdIO6pTKTYn1XvwDD3xiXt__6qyrEvzLpL9oOamUiAX02HN6h1d_Ew20jFsVirnZxDH37A0DuCmzPOn_HIUI5kI2OcI7VPUogvfyg2222d5Z_U87YHaXZpPqclmhnsJNNUTKRubFFvf2I3-kSOKiPHXciusIGD8UQ6TnBmUjqbW3duE99yxkpdk2L5VfxQpH3KZ5LpTu7dTI3TY0sF4-WXiKq4orjm0tBqW-oJoJ0RzhJ5CG-iSh2YtLKkzsWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=CQ_h_xmN77ju92Z83ORGbs4Ehl4PaP9gvn_Dor-XPAyF-s5laE3kHeR4orqNHXP3CyBvHIiBYXUW3qrtp4Ebr2z-mdIO6pTKTYn1XvwDD3xiXt__6qyrEvzLpL9oOamUiAX02HN6h1d_Ew20jFsVirnZxDH37A0DuCmzPOn_HIUI5kI2OcI7VPUogvfyg2222d5Z_U87YHaXZpPqclmhnsJNNUTKRubFFvf2I3-kSOKiPHXciusIGD8UQ6TnBmUjqbW3duE99yxkpdk2L5VfxQpH3KZ5LpTu7dTI3TY0sF4-WXiKq4orjm0tBqW-oJoJ0RzhJ5CG-iSh2YtLKkzsWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
ورژن فارسی آهنگ جام‌جهانی
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98132" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=imfoQLfaAAFA3PoRfgimlDaaI7LPElupdPgQZUP4GfjEO-tx3RlTwCcc-Gi6UPB2hdO7mB2nc9U5zy3i-Okeb3p7kDJ4FeAWTSmS2akqJNcYZ988r8k_gtIHDtg1-vfpUCeEgqyPetoBxrH3EPxgphK_zZSUNvcq2EXD-IIeyJsF9bm36JEK27Cl4PLxVeG35dRRwXo5KxjZ_T7PpBOTPludq4-Snvc50p6lUKk55drvnTyjwDFNY7CghJ4bYUNgmqabLVPfMIXOYmhbWzd_EvTr1VzqznxsUG_DCwYw3ggTDaAMPcfpJukxcRzQdMA9M7HIIABHw0rIXM5FRQOwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=imfoQLfaAAFA3PoRfgimlDaaI7LPElupdPgQZUP4GfjEO-tx3RlTwCcc-Gi6UPB2hdO7mB2nc9U5zy3i-Okeb3p7kDJ4FeAWTSmS2akqJNcYZ988r8k_gtIHDtg1-vfpUCeEgqyPetoBxrH3EPxgphK_zZSUNvcq2EXD-IIeyJsF9bm36JEK27Cl4PLxVeG35dRRwXo5KxjZ_T7PpBOTPludq4-Snvc50p6lUKk55drvnTyjwDFNY7CghJ4bYUNgmqabLVPfMIXOYmhbWzd_EvTr1VzqznxsUG_DCwYw3ggTDaAMPcfpJukxcRzQdMA9M7HIIABHw0rIXM5FRQOwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه بازی بعدی فرانسه و پاراگوئه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98131" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3536115386.mp4?token=SPBnrPeg36KAygV0MyWbuz2o3EmY8h5Uztd4BCX2dVp_69utPbek0yghw8Z5PjpeT840mcERII123Xr8228cYjt9AXmOP1DPHPQ0wqsN6ccez4KndBE_4VDfsDCeb8nhEGLpRHBcsXrkeMP4cUqVRJ-BM8HqPQyi2SMGt9MQ7Fs4BYhfXUwNhHko3Q3cWE7eQooF_xuygoMoBHR-DB5RVqChVyKzXhstr2MWFT3DD1NeQRVpEpBs3jR_xVMSSc3oUlg5puerBfZqpchAkLkl3Mb5cgAYXZx7LY9u8oj2-1rMgAF1gZgn31T8KkkgZW08z33pKCWG8Q_WGbkmhivZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3536115386.mp4?token=SPBnrPeg36KAygV0MyWbuz2o3EmY8h5Uztd4BCX2dVp_69utPbek0yghw8Z5PjpeT840mcERII123Xr8228cYjt9AXmOP1DPHPQ0wqsN6ccez4KndBE_4VDfsDCeb8nhEGLpRHBcsXrkeMP4cUqVRJ-BM8HqPQyi2SMGt9MQ7Fs4BYhfXUwNhHko3Q3cWE7eQooF_xuygoMoBHR-DB5RVqChVyKzXhstr2MWFT3DD1NeQRVpEpBs3jR_xVMSSc3oUlg5puerBfZqpchAkLkl3Mb5cgAYXZx7LY9u8oj2-1rMgAF1gZgn31T8KkkgZW08z33pKCWG8Q_WGbkmhivZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اگه کیلیان امباپه در یک کشور دیگه به دنیا بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98130" target="_blank">📅 09:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDUnkkr73ONVZQ_W1IRTfMpzcoxZuuIwUJaZzJD2952nWjS3mDzQo-dMO6UK7u1QlxwKz7Od8JF3adGlctl2FUAhow5vfgFaDJ43PsNwMkH4rnd_eHGjpt3dvWD4_RBjvueyqpPt5i445JlXdUECx6muPQW0bQS7FdyNwrVQiGndcfcC8su71Uq8iSQ2_DLwFxR-RTH8HH2lTOose67KhXM3iREX-EoMKuycwZ31CDs7BmQS9hlxeWiAzgo0SoK_VsnRQ6kBZUUnrbLlH7E-je0msQMZxBD_DREMEc9453Gs75LbLLPrKhKr50IK3G2U8IC3jTKJOjgZc3s2gYFDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
ولی چه کیری خورد این بشر؛ تو چند ساعت هم تیم ملی کشورش از جام‌جهانی حذف شد هم جادو جنبلاش اشتباه در اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98129" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_6lwSTRB1-nhB51Xy5DOf2UtVOtPXUhoPEQuqsUQXlc4fxDHlthVXVRRIeMHKi6FBABHJB-zHkalSm59I-krKIeNV66VN4rIop2JdTZCTYHW90AYUz3EkJAhX7SL_jDU1SY4T_Ike9S6_k3iwAuC7eZqcQ5M_lmZ6DHdnGPLwX-3nkxyYYoYKM160yvMW7HSO0qLaKeAIEuxMLKEyRycQF4WHTbdVl-YxmPLtHGnhVXmt3eX26GtYhWThWCVjzBQAatafP-yUVCT233IO0fYxIm2agvhRGn44Lwd94HlRBCV0EVzhwOndLPaDlXego7QISbV9VhrpP9F3Jd-W_d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات ⅛نهایی جام‌جهانی
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
پاراگوئه
🇵🇾
🗓
يکشنبه
۱۴ تیر ساعت
00:30
🇳🇴
نروژ
🆚
برزیل
🇧🇷
🗓
يکشنبه
۱۴ تیر ساعت 23
:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22
:30
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19
:30
🇨🇴
کلمبیا
🆚
سوئیس
🇨🇭
🗓
سه‌شنبه 16 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/98127" target="_blank">📅 07:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp3-cwIetf3QaYsSqj3QnHX3uO9U77YJbz84Hz9zNDvtdrcDK_mDZhNnpT4l5rYnGPpa61nZFyWkA5g15W_9hRXzxkEMjwsSpLTW-0MgBQ68UHy0_fYAbkqcz4x7CdgE-u6nH96A_6tpt9Hxgq_nJNSTvnYT-2PUYptfzzdNMC26qUPE1_uVE_wL-0G-_KadHifDkT3pSCusCJT2M60gSMbNgrNgtDGV1uZnYFr_gAhCW2Q5Twd56BycSTm2U9YqqCT6i7xLogGzaYOFT8_a7z41yTBQYNKM4PP9WAO_Hzjs5X0NvaJ2oY35bKHcm3O1yFv_g4toNuR3xZjDdrzkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98126" target="_blank">📅 06:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کیروش کون سفید پشت هم داره از کون میاره</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98125" target="_blank">📅 06:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98124">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98124" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98123">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کلمبیا دومییییییییی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98123" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98122">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98122" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98121">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIT-iAVT_xK8btWBgnK8JfTfNKRQdHdLG2ZUxf5chxV3JrNCX2gHyvmNKkygP0ZORrm2xWfxYqDwySKQuaqPHLdHp1S40HGjscgrrBfDgSdWa_O83-QuzAijFOlsHK-1XG3Z8Kina-jDuT3e_m1ZtpsJMIHkAUjuBq-AiUbfJSrWvKTkiXz2ijJWtrn1w7pOtryfxknFmVbKWeFN7HZYuLfabqZfPo030IbKpcqeNl_JYLm80mgi2XzBtIGbntgY8BTaQs0l7E8UEtj4f-glszD61nYOCQpvDKgsxcuXf2zW7LMWSPS726t3kf7SydZt2ciriqGBbyG926fio6g51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دریبل‌های موفق این بزرگوار: 2 از 2
🔹
نیمار: 0 دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98121" target="_blank">📅 06:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98120">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx_bdiZ_TjTB9HVQd7O8WsiNx6e4K7Ou3qMTzD300fODTNaoJNixFN9lP2HjLRqOMc3Tj0CRlwT-PtkN3ZDqUcz_V190-2LnwddOEzE80w1rxnQ1hNhUQJx15GljPY9hJIpL6TsZySjQVY7q7JfTgftEZHVf8VfWehkWxuM-jeKt2CANEt-mXUV4SBgXyy73sEQuirdTAk8FzgwpxlzWPWecD2Xaf6lOSOe2i-hmqdak22CGGNPXEH-WkjaUkj-NM9Xbf-cWM8D6JhrzM8RlME085ZsWTJYJm3dRXNHXmCj6_EnN5rTJZLUn90EyGlqRX_ND2ADY8QL9-VpCZcMTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خامس مصدوم شد و بین دو نیمه تعویض شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98120" target="_blank">📅 06:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98119">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98119" target="_blank">📅 06:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98118" target="_blank">📅 05:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-w3gN0nCGM6aC7AHpesxYkGDem61I4Vhb9aijrjA9Lbn7f7FMENZ2M7R_7TLDn6NzP9hUSAdXmuM6kK61nowqlG76CArG10i3MR9qR5Zj4zVW3pu84d-zHbOtZ6pANwmj9--tyO8Jle8somGTjzyBUN3TAr3F78dDruhHt2JMN_sWRqDwvEPcAEPASV8CA2wQqU_XLbQrLglH7TyRmZcJlJUgOp5Y7FJtsolDlmV3lKdpkzPK1m7504ZUfc51Y-KHueidm-fSTfkKfY_zz9Rxo9YC6PrSP5OwQ6G0l3urZcsqmkfvca0_N2IVP-PnS9GJ3iq3l95Szw5otvJ2_PvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین بازیکن آرژانتین در جام جهانی خولیان آلوارز هستش که در کنار مرحوم لائوتارو مارتینز رسما آرژانتین رو بدون نوکِ قدر کردن.
این درحالیه که مهاجم نوک اکثر تیم‌های مدعی مثل انگلیس، فرانسه و پرتغال نقطه قوتششون هستش
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98117" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQvA5FjIS2rEM1HY4SUKKvI_Q8c8edCKAIXjGXjuv6Vy8v9P_f8KkqjHPy774e-EqHfHdF-j1Lupazp839T0j5u6tPKH2aG4niIFQ638xlSNznd-Xtv-nHP4r9qPsBHTVMuXLfFKR1z01e4fOvdfVjEdysd90TIjh_XhCXcgjP1p3JKjNzC6CUV64bHVYQdKKYZOFORL9MyeovxhvOY7vFskorJhlg9Qy2qUjmfXremLRJp_FngnrCifnL5ay1orGDoeAFFCb-3Wr6LOP21kiGYdGGMOZ3mVYF2leIfpNMWUGevzpU-T7SqPKNZojsMJ7sZ8truLMK3EqzHUrQmuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتونلا هم اومده بود ورزشگاه که شوهرشو تشویق کنه
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98116" target="_blank">📅 05:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=hYhwFQeeP0hVoPEB2UvDR9Yc1v5XDM-4hB7W1n3C9PgjICwL1mK0CV32PdhkEKwKkxRG_DGcla5OIraEfdhn2774HHYenX8FkT9so-U7OD1CTcqoZgJqlrfxT30srxkiYoxye1T_Q6pqpbXmwIPFwuzTj2OwSWb6QgsnPFk9m-EMtmbpmNhX0aJ70JwLHZzhQoHeOyecGzESIwUKnuRyOdy2pS-xg8xKy46STOFPIAMizm9JXLED11zpbxygDSaCuY15lmwNH14NMiKLtrZrp_Q9PrfvOjAAQ0ldUfzAA189rh2D_1P-lPeHuOM3jqQs8nA6EcfydbXs5h29PQQF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=hYhwFQeeP0hVoPEB2UvDR9Yc1v5XDM-4hB7W1n3C9PgjICwL1mK0CV32PdhkEKwKkxRG_DGcla5OIraEfdhn2774HHYenX8FkT9so-U7OD1CTcqoZgJqlrfxT30srxkiYoxye1T_Q6pqpbXmwIPFwuzTj2OwSWb6QgsnPFk9m-EMtmbpmNhX0aJ70JwLHZzhQoHeOyecGzESIwUKnuRyOdy2pS-xg8xKy46STOFPIAMizm9JXLED11zpbxygDSaCuY15lmwNH14NMiKLtrZrp_Q9PrfvOjAAQ0ldUfzAA189rh2D_1P-lPeHuOM3jqQs8nA6EcfydbXs5h29PQQF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98115" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کلمبیا اولیو فرو کردددددددد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98114" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شروع بازی کلمبیا - غنا
🔥</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98113" target="_blank">📅 05:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INr8SUhC6-Gk4KHb1w4d6xWn_JTArUWY7t0iKQCradPpHF_9f8yqqe44nVfUORrKJDgzzatJWhdwruDZ72Mqi3wGPBhg3gmIYQnPdI5NjWBIduAvKjtlzfvd99c1r94Y9Hu5yxXaE_mH5XIhBZjCcNGOA5kE4FUqbvR-GJfehirLZRNkxkJpUY8nFRvnfw6nmBRbUUuxaAtbaeygIdkqKIv-Zos_6AS9m-_8IuJD7wCmZXa2EKgPOZZKgvjaXWBLwNsE-DDKpiEMo0w8LrZa0vSkeUCQpm-J0npPxD28eYsJ0D_4NnZfqqvcuJNfnF7_eVQZfv7OxkVm90etJEaNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🔥
🏆
لیونل مسی، اسطوره فوتبال، اولین بازیکنی است که در تاریخ جام جهانی، مقابل 14 کشور مختلف گلزنی کرده است.
‏ـــــ کیپ ورد
🇨🇻
‏ـــــ اردن
🇯🇴
‏ـــــ اتریش
🇦🇹
‏ـــــ الجزایر
🇩🇿
‏ـــــ فرانسه
🇫🇷
‏ـــــ کرواسی
🇭🇷
‏ـــــ هلند
🇳🇱
‏ـــــ استرالیا
🇦🇺
‏ـــــ مکزیک
🇲🇽
‏ـــــ عربستان سعودی
🇸🇦
‏ـــــ نیجریه
🇳🇬
‏ـــــ ایران
🇮🇷
‏ـــــ بوسنی و هرزگوین
🇧🇦
‏ـــــ صربستان
🇷🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98112" target="_blank">📅 04:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcwFBwREXv8Z6NqFGk5sOa-2vvQhnVlXu_QhZbUllSFUxCK0K8ji3xXCKxfw5EtavFfllQPgQ_EXUA9un2fN4H49gVVhubhkM-zbhEEJl6m_YJFYKJGmkQUfPh9-fj1QB3xwidMJcuKy0Stcr7ATEBIcAbIMseRARDBBGUaAJ_03BFOAX8GsH3DEmIMCOx1gsh7YSnNAsltBpGOlWRSGYe7int0-qpFoYvvxxhNYWzNVj1wV1o7CqXEaiWTr5VicOcpgGUBk3UxJE0w9DrdpBiVxFMOrvHfgLFdGddVRRplvRCRXBmvfodon01agPnACE5B3UKxfGP1Un6Ql-Bjsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📱
مسی همین الان گل زد. فکر نمی‌کنم تو بتونی کفش طلایی رو ببری، رفیق.
هالند پاسخ داد: "درسته"
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98111" target="_blank">📅 04:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4m4Kwu5AF49csW3soM1cicMj5eYmdlanjHlERkaD0KGeUlUDbzvHFBORjy8GM9bB7qUrMWvEendwnEvTIsmSzTYk9vYIjuVlT5bRefs3cRpk9clxqAH4YIuYYFNup2s2JvNRGDqXJQQWfN4mMa_XrjwkrDW6lKMQEzKyLkUg6dnRfrQLlojJHoKETUbqcHfFOGeoux81V_XiiGGFH5l57cjipz8CyNhO2i11PLJ_4EdZU-RXseAmXn6BbHdUco0JG6SL9LO0ArXA7XnMYEnUcF9QAGlXTlG-GumlDItHRot_Kh9ipYdGu_xJUV42hweQ97VcGJnBUbOoKshyMKUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
🎙
لیونل مسی:  ‏ ما دیدیم که تیم کیپ ورد در برابر اسپانیا و اروگوئه چه عملکردی داشت.  ‏می‌دانستیم که این مسابقه سخت خواهد بود، هیچ حریفی در مراحل حذفی آسان نیست.  ‏گاهی اوقات مردم ارزش بعضی از تیم‌ها را دست‌کم می‌گیرند، اما ما مطمئن بودیم که این مسابقه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98110" target="_blank">📅 04:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXVGnrqvU48JsYYOZSch_IaZOnd7d7ZN-lGZxRxY6N9BusnKkEGYuAc-BT3vztBjtNozs5XgCMEc92QIH0NwxnmrRzU1SNKwYBltUfCMV4z39Xn1V5Ay88UyUK422xWe6JkMIFzMGiRlyf7ZxEUiIo88UeKquWgxJ8-UH2cY8rn3veY9MxVW8w0o_5Gl5iNagiE7lrNljoOTgJdLFSnp0f0X3maotlDvbLkPjwLlrZ3RB6ncsQ3NJL1MIUp5ymb4dem8bLvzM6R1W8MjvHah_BV5ygTei6PFr24eYqVICCYR7XcTAw4Tc_uaX58cMAMQLrJE9rUs7VxCp7eaWC7wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
لیونل‌مسی برای چهاردهمین بار جایزه بهترین بازیکن زمین جام‌جهانی را کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98109" target="_blank">📅 04:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9z82xt2r5mApLfr0nip_wWyf-HYMlNV9gEzYmASHXpdC-ZuU47s_q_m-cjToGl66O30ov4XFK1mm1TDwFtZWidDnXWJt9wQlDfLdHSkMbXOKKFdK_zYuqzST4REYP2xkHA0lWcqfArgb0n-uieqcF8pjdTN9vfECVPn6gYxx5zAU1gRWicBv6X4xFx5uY7-8A82vyb5ZkAbPF0ujUyZCLs5VDwhRAIVuduaiWiMd832WUQ6FJ7XJsltMu48R2h0HSOcNN_3oAN-LKRny-w482p8ECoA3Z4LdL06D8KfL1JN-iJ5r8HDZ4bELnyEoAD_YO0h0S35EWc6MAVWQ_0N6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98108" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjBmbwDRLuD6g3rOqu5IK53QTmI-dVZXiZVda3b9l44YRPnHX5hQC4dYvkDS8kR-fsJp3hitORyPPg00G8y2RRk3dGtcU6kEB6Ik8x7HEAp2919b8Ah6Kckw40AvgERM-wvxeGFwGdoC5_eTV2P0UW3F38HV69Q53T-GI1myCaAza8xPcNBiwygjhSfUGaoGUxUszVZvcQfGgPFDQUxwVRbMaVuzK2yKpynrvGsrXtLeInzY2cHZ_5DU_jh3t9KjDyrgTnDEjf3l9qsY5VvBXhGE3muLTiddwiAvwE9heZVK-VntEcDSyaICww2KD7YCzd-hVZilFACfLukwyxpLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاتوووووووووووو
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98107" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD0cl54FiaArgIO-fTWwCbDGrvTPX48T1-CP7olSjiZlkIm4qVN8gaciVbgdERaicNRhdEUi0C9Se_gKAu9t26ZYtMR-3DZrDdZF--0iNx-ZsOC_jq4tAq94XBVMs0Vh7kFV8gZw_bzASViQslJkFXjbFjFZoW6Qj-_7Cc5nCW7ZAdNY0pzhiaiCKsAFmt6IbXgQM3j5HAWY-dky0Dm3AlEFb6GHtYvJAAgYGnqv_viPeDmSMClmmsszXDF_w5fDYBCbbDEOGen74eRj0uhlD84lx1kTOtgUdS5KEa0RTez_LI3K5uN1jgAIa7B7pccVH2-PtjeyTvHS-OLVOGEjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار خلقت در ۳۹ سالگی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98106" target="_blank">📅 04:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🎙
🇦🇷
🇨🇻
لیونل اسکالونی:
«می‌خواهم به حریف خود تبریک بگویم، آن‌ها امروز ثابت کردند که یک تیم بزرگ هستند. وقتی می‌گوییم که در جام جهانی بازی‌های آسانی وجود ندارد، این واقعیت دارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98105" target="_blank">📅 04:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuaDotHDpz9j_p_kcG6oN1k4yFNaN0rsZc9fv1Jb21qD3RqG9VH_KxhVS31MDkQD3dvKqtCwMyXHMYwDX0oLW7fPzqsIHCXdy3taZswdL0ae6QrpDnCAXOqaRtB4q6QweaKwmXFrKKLjNVERAY7mizUAyeTktmAeZXfgT_pUh-_cg1DSJzrUaNhyTigpLZdYz_uzbbhpEGGsF_nmdROjZfy5x4H4BHUMCRwoAiuZCz0hBZfvpCC90UCNXa2EYh0969YAEULCPgl7WVNR8aVh7IfxKgKne-Zbpr2eqSVpZn2Hs_L2r6OtIXbX_ZXjhOXZsraMmhmykuBTj4Dy7WcXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98104" target="_blank">📅 04:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6SAEzx2eZdwbiUFtvnJUUdNuq2FkMQ2gRjd-jhzvSW6lK9usBaKzCV-zOuwGx6JNM8f3Q6R7eN5Zb4GJZfyMF3GHajwT-_OejAFnO9b0wwfHa4GKwlRJhSCWtngvqo-wJ-jsYyZaCwpMRG60JE79Zhc3OqDVBj8j35wyLxVErDIwqllVmlCF4f0ZZJTcaPyf5b7GhdTSYZ7I6JPO2UVOxpMLB8SUOYeMZQ3ErkjPHDi5FJD42kd92rZK-VMrAllKuq5WjwFk9712DBBvDgs__cqciNVXX-VsyNtrbmu_2jJ9GuCyqYNvu8mWuJjM44scteu3S_WSz_sWV2PRKb2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🇦🇷
#فکت
؛ آرژانتین (از جمله در ضربات پنالتی) در ۱۰ از ۱۲ مسابقه‌ای که در جام جهانی به وقت‌های اضافه کشیده شد، پیروز شد (۴ برد مستقیم و ۶ برد در ضربات پنالتی).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98103" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP4S_Xep6VAhJqEAYkGWNLPew806tPzRmtkbznhAABsSM_UPDK8ZfdyAac-OqtoEDN-RpUXdTWiOBfpEmm_06v-XsApMpLcikF5chNNy2j2KXplL89VsLHNiHPK5xjgKI10952sDuxilE0sghnTFEHouNZ4ZWmf5xCPwiZxJMcKb_LLP30_dYAmtuaeD4ncUozRkHXOzP3xogRHIu4hWWyPwLTYEd8n-qNO6g938IDl-nNavPqUn78M68vMIgsvJva9knQ62WY0t7jtCm2FPZt18ovvDf1xM6ZaKxVHcVYIvccSPVYQ9Ml1h88io6KQ3A-QX4XN6ZNbLwkFpPzd-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
گلر کیپ‌ورد مقابل آرژانتین
🇦🇷
|
✅
— 8 دفع توپ
✅
— 5 دفع توپ از داخل محوطه جریمه
✅
— 3 دفع توپ خارج از محوطه جریمه
✅
— 1 دریبل موفق
✅
— 8 پاس بلند موفق
✅
— امتیاز 8.4 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98102" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A10CjWTk9ydna2InWzCWXFVVoZTdZSGF46qee3HikBS8VAWRKHNTyBc7E2IjJPPua3RsHB1Sr8mp_mQSi_WOpKcL2LNkWY3UfYjBX2yWRwxXp6xQ4HVq8TTWugn_LuVG5HQBd89v-Hobw9oBbkhqEyB1TYyU_Cy6pc81sDxwImHaoldFYyRV1JNMpzcqDgjRoeYrQn4B5B1xo0TOOPK7EK3rq3IsBH9TbMU9lPRr5N8d9Pp7WxuM6-LdrktO6JAW5li3Vibxkzi7BgZ5tn4XgMZ2qcLev-ZzPeV2A9vhwgwYnskZaITd__fDh9HS3I63pw7pZ8PKfMP1p_o_IjkjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
📊
مسی در مقابل تیم کیپ ورد
✅
— 1 گل
✅
— 4 پاس منجر به موقعیت گلزنی
✅
— 1 پاس منجر به گل قطعی
✅
— 6 شوت به سمت دروازه
✅
— 2 دریبل موفق
✅
— 8 نبرد موفق
✅
— 5 بار دریافت خطا
✅
— 33 پاس موفق
✅
— امتیاز 9.5 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98099" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خوب اقای وزینای عزیز الان ما بخوابیم یا سر کار بریم
کیرم
دهنت تموم برنامه هامو بهم زدی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98098" target="_blank">📅 04:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMa-ND6SWey57Hf9vg_VavXx9yOZ-lr_IAfLDv74DfYwy68LUDxl6p5X5Uy2UdE9L08SPrCQJw3EIHHy6QIxCdA6G4M0Ft-ygklVYN0m-AFmrJOZ0xpyj5ee6b9RXiQthaVDXmma8vz_P6aMVtOHLiPtIyz_fSGtYH-Mck9qpsjcpNFAUiUtagpjLIj-CB_jGUGr43P6z7CFg3Nx6hvAKxuxGvJK1OPJN_a5rChQe1N6cwktL3WR_ZL0uLboTHryxdvtPR7pIhqoZMVje4LAxmja-XC97Tnqn3UzsgOM7t28BYPL1nut82qYGIQ5Z7EMsSJMZSFpS_Kf0OpyGbeGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک‌های لیونل مسی بعد از برد مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98097" target="_blank">📅 04:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3izWcdSDYwHTFoIU3SaYFuqOHhTNei0m4MxCyQLJjcX-2iWg-BES9T2jS_GpIZLcsYP0VuUXx6dXlXq-cI5YlAu7zse_jfGHwsT6rYQPQZBK1WINl8vspL7bKIwX3QnHRaw4u1aXTIaeJSnKIdyKi3piHA0kUbweZmYZCLtdeeAhlRwNTCB_mOutS0SVpKTBXtK13gvHEE_6jhS-a8X_tnZlB1Fo-f3woKGdkgRwPaVotYqkzTLxtnyN_3AZRVEMato3bP-yq-uPETigAqlC6XMZjzEdVC1o9FyBA2OGxZE9pVg3kI0Y8PjfaOqXdv8-TJRLrN-QhSEhyO75GFUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ‌ورد سربلند ترین بازنده جام‌جهانی...
تا لحظه آخر جلوی مدعیای قهرمانی تو 90 دقیقه باخت ندادن و تو اولین دوره حضورشون در جام‌جهانی شگفتی ساز شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98096" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98095" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98094">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDnzR-EbbAA79ChRe5_UnXONyMJKL97zqnWXs1KZ7T53E-xjWAJd19Gft9y_80W_Gb-G4E0WrDIMqNl0GbIwkoeZyOoPaxZBZfpJJlw2P4LGeP4PFGW7lNfDW3RfGGT82kbOWe3yvBkhVZVX9_Oz5w-UUlOzccpgdt6cdn0fVfd7Cn-zex7P_ZemVLKj_WBSqiRhHBCHOCicwYKpoVqgzob4dRu-E1hzkcdGCKroMnlyEy_LZ0qB-oYCvJjveYhuMhE6yQWxkX_D_f3B-iEtjPw3TosHhJ65vCmse6zlUhEVGmoZL7-UD7oHPFhtbBBOTPnpFe_l2L9DgBhTcaW8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98094" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0LclOQbdndI-qG-QpMD1UnCdNYk3btMBi4QDxqYTOeuwWSJ6yta6cXe90arrbw0-Y_X_Jopk5P0bxhYqBF2z8MdIJZ2jg7imjnmKoOAiY2KRx7PvhsRNOBkUiuwstJmoOd4BzJiqQLxemwCZadk1Nx8-tx204HCvAg3fXmrnG7bQ-4aoihJkXaTTSEs7qnDVv_Gr8yHvexud5FTJIvzhlC6tMsl5mbiDhvhjEBOnbQcf_z01gaYIgmKtqh-cdYUczilFh11koFMWUlX-HM8i3NkfKX3nqjr99Bus-HvHH_QY1629ybRuId9c6YeSGsTb4t_ebUrsz81-NAMC75zoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98093" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98092">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگار این بازی خدا میخواست مسی رو بکنه
😂</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98092" target="_blank">📅 04:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98091">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkYCD6YeWQhCSjIpWeFbZCOL8dzxhlCFGrcjy5bCCGe1oRjdaffFB5yqrrRlfyTixTlS1kZMzYfvT-OWBq91vndhX2tKIJKbYDwSi_mYXo3_-2ANFBXb0K_z7LAjN29sFonH3JGna9RAaf4rXJp9tHKdWBU2HRoWnFh_h-OVjcFYf-ywPA4jlRZTvmZA7DdBOM6VvtiLKwR5gWauYSYZ96m2uUZW7ACrrrH-Mlona5zaUl9s9xGoJHObRooCpWWS8OSx3PcCqHP0meegSQ3hhMYAyz37oGaDbNNoeacnVvBv5hoRGTaBXGheEszXWj-0BuxNzaT5b6SXygbUWQfRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98091" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98090">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با اختلاااااااااف بهترین بازی جام جهانی ۲۰۲۶ رو دیدیم و یک دقیقه سکوت برای اونایکه خوابیدن و گفتن ارژانتین به راحتی صعود میکنه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98090" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98089">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
عصام‌شوالی گزارشگر بین‌اسپورت: از مدیر شبکه میخوام هفت روز بهم استراحت بده تا این بازیو هضم کنم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98089" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=mUd1-tl7GWM5DF08yF4cDoufjZYHaG1I1e_Z6WGC6FtqVawAdEi_lexagvybw8Q1lJa8ayt7rpi-v0a9VV61NPGM-bIfJ3XdH0vBp-GxBNOPDb3cqKhvS6iF9iKWHKhxojauATFhoXNULFdhej6BjGXKLxQVszRsCM2FKj9BCTBYjSUwZkTPBuoaSZEMry5tHLQbEQoz912WGcbSMqrJIRnft0rw__hgp3l7dnxEKMPnTBZ0ISkOIrfe4nQ-jLIWgAME3lUNwNxFE6fwq3fx33OyWG-Z19Epk05fI4iZDERCsYFUWyzqJogCUJihuWsyVvu6G1U6EgnqiCxctv-lXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=mUd1-tl7GWM5DF08yF4cDoufjZYHaG1I1e_Z6WGC6FtqVawAdEi_lexagvybw8Q1lJa8ayt7rpi-v0a9VV61NPGM-bIfJ3XdH0vBp-GxBNOPDb3cqKhvS6iF9iKWHKhxojauATFhoXNULFdhej6BjGXKLxQVszRsCM2FKj9BCTBYjSUwZkTPBuoaSZEMry5tHLQbEQoz912WGcbSMqrJIRnft0rw__hgp3l7dnxEKMPnTBZ0ISkOIrfe4nQ-jLIWgAME3lUNwNxFE6fwq3fx33OyWG-Z19Epk05fI4iZDERCsYFUWyzqJogCUJihuWsyVvu6G1U6EgnqiCxctv-lXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل رومرو به کیپ‌ورد با پاس گل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98084" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98082">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کیپ‌ورد خیمه زدهههههه
😐</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98082" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98080" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqpvD0SEeb5T11WBoMCdEOfdg1oo5grMQYauSLb8YSMFJPkCfI76-Visb5AcnVzDNYba2dtONkoc4pRm3WBD1W7FHjBjctWVFFsSrHALddZTdf4_eTk7UAtow8PQQNeHg8XHqPwwTfC7lZgi3AG-bklZItgy4YLwbGIVhuUO2MFke4N2qeQ9K9hm5MZrbiWtveszZer25nC0oMuVX3o--p4GK_a_75I1OQWpsmm6nSCxi292cP_DRlhHwnacOOrXH88mSbtG9aYLkG8NqvYQrLIJAnLFiK7LSbuqzRE6mUW-d3QGCvneGZ5gAvRBf9OJJUoZlDW1HjD4FqlHk1_D1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.  • اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98079" target="_blank">📅 04:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مارتینزززززز چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98078" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
