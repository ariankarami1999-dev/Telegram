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
<img src="https://cdn4.telesco.pe/file/AstfgjoVRdBNcp2eyoDxFkiqslyTkqayzZzjQON3y6UzTxV4krkmMDfSC90DwHi2QnuymwPQUB0gwfLU8ze04ZGGy1VMs7MVo7f9NaGLVufi4A4KLnvTuRfPV_RtRD3rD5MOE4orp-i1tp16mXI4W-UkudZeGvgZ_xqzZtR_qde2KTljTXZJKdAkRxSLsmvvfvGlZXSUOZ4LwDvNnlFKEbUnjnWDPL432GTUMytuDHEvNgicb30ZVn_CkgGpqCO_o6VZykna1TEFJvfrpwAi3WiFf-0USUq_RV9uyWgovvm9AmA0i35kvrt3ZtOkt2RAdZNCYI0eP4Qv57BTAU0PjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 04:19:23</div>
<hr>

<div class="tg-post" id="msg-89615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇦
إنفجار عنيف يهز خميس مشيط جنوبي السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/naya_foriraq/89615" target="_blank">📅 04:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني:
الرد على عدوان وجرائم السعودية مستمر حتى اللحظة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/naya_foriraq/89614" target="_blank">📅 03:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1FgiHCHvAV2KKOf7DbRRTWusz6NgxaLs-a0gSzeYqzrDPfP27TfEMafDlFK6K2MLAbw4D4QmWP1IdAzVtIGSTvXTr8NkG6jUaPWWq8N95xdvb_qbPLwfV3sbuLG0wuZT8xkFl-B_MtkqIatu3GN2EcA7aVtc7WEQlhT06Awbmi5kKI43NLNSbi6E7CX7JlhXqrbYjh8T_Ink50MnaQN2FI-egDIu8QrN_GnvYCiDq87jYUTvXHwoyn9UdR4kXl1MQMf4FFaakLyxbyvk3uAkJZXcsYP-YaqxH0jkmb9luCV1h-m5DuL02Ql5gjY8ycCs0gh7MCwx4SlKSNnsXgq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JD-FFDZ6bT10IThuVZPDcUYkMlM16oboDejW59o7Rj6fSuIuAA9WVAqOPgsbq0H1O2AOMMUHAgnN1gENcunSshOBXx8Dcoo0rn4gu5e2Efnl8im0LM8HrUQe2E7gQDZzPM2PLsHta7Eqwdf3PZ5rPeTzQOcmPuXSA_9ibbA91UOA7N0nXg2TxunP6FlZJRioz8Sf-sATJ2_rGmItRBX8UdypvThIOWHw7wWv-ZYhTV0A5sr7lfetfo8nCitcGLYLVhg4R91o0q_JmAMrAXVn1_LeioipBrcI0VVVOmWY_ePN7BpdUaSmpIktAw9WIMKXbTX6b5V6JqrFO6RsHWztvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف منشأة نفطية ثانية تابعة لشركة أرامكو في مدينة أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/naya_foriraq/89612" target="_blank">📅 03:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي في هذه الأثناء على محافظة صعدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/naya_foriraq/89611" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حبا بالعررررراء
عمي احنه وطنچيه
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/naya_foriraq/89610" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/naya_foriraq/89609" target="_blank">📅 03:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
تصاعد أعمدة الدخان من مصفاة جيزان النفطي في السعودية نتيجة ضربة صاروخية يمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/89608" target="_blank">📅 03:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSbapMUQnwmYZbigSMcQfsiHx1Q5CHUDRADoZeIYpWZwJXIciRMOu34QoO4QrYPwWLHs-KtOd11_EnnXg_WrwxDtgkoQcKb9AZBHycndr42bHiA3QMHaQauiAPn0HwnHjEKYaYdGXyL5vIUIJlukWnwPH76Jit07AzAXpmGXCcmznvThWXwbbRiE6ULYNXAfqQqu7LOr_6N2KoHXkuuZXhDPNyh7pdxyLuGTKrVrGIu341bn_OdzlimEbX3L5-F-zLxk3bjJGk5CcBJcF3h4I-PzIIMMWJhcP9ANR-b1LSgl_DziaWw-U7ZDFnUs6hCtGi_RQzj46ML3t1UVBD1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
ستنخفض أسعار النفط بشكل حاد عندما ننتصر في الحرب مع إيران ، ستصل إلى ثلاثة دولارات للجالون وكل هذا سيحدث بسرعة ، ولن تمتلك إيران أبدًا سلاحًا نوويًا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/89606" target="_blank">📅 02:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89605" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/89605" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
🇸🇦
سرب جديد من المسيرات الإنقضاضية اليمنية يستهدف مدن جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/89604" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇸🇦
إصابات مباشرة في قاعدة الملك خالد الجوية بخميس مشيط جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/89603" target="_blank">📅 02:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
🇸🇦
صاروخ يمني أثناء مروره بسماء المدن السعودية متوجها نحو هدفه.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/89602" target="_blank">📅 02:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة صاروخية جديدة تنطلق من اليمن نحو أبها ومدن سعودية أخرى.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/89601" target="_blank">📅 02:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
🇸🇦
الصواريخ والمسيرات اليمنية تطرب في أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/89600" target="_blank">📅 02:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N36im1lcQP4qZxHHWQhvyM2ZXa5Z36DApYGUIaBZ4h_r86KKV-2Lz1uQJ3kuzzrmqmYbA8e8s-P7rFD0TFl4ydp_tBAanFWEizqsMlx9OtDpMEjkOFykK6Xote7jnl4RcmtBY_oYNpoO-lGSY7D6n5vRQlT48PH46p-a5hFUElu4P-1qB3gf5D83kKNGQPgfyeRv06_jY-SXaFjJGJzrLgGnlZSNiOAW6jumpwH3MuPXjup6wSEFYD3EmP2p6pr3Z760UOGPTH6g_pm-8QSSl4qgHpVPg5zunN6lNzyYYeDVW8-N8dQNTEUZjYfffPGHDnIp3MEam9c7JR5Bh3vIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرب من المسيرات الإنقضاضية اليمنية يدك السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/89599" target="_blank">📅 02:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/89598" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">السعودية تفعل منظومة " لا تصور تكفى " بعد فشل منظومة الباترويت   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/89597" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط بالسعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89596" target="_blank">📅 01:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/naya_foriraq/89595" target="_blank">📅 01:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط بالسعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89594" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89593" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
محسن
رضائي
: ‏في الأيام الأخيرة، تلقت واشنطن تحذيراً واضحاً من الصواريخ الإيرانية الجديدة. سيتم الرد على الحرب الاقتصادية بفرض منطقة حظر بحري عبر الخليج الفارسي وصولاً إلى محيط الحصار. وقد أُعيد تقييم الوضع العملياتي تجاه السفن الحربية والقواعد الأمريكية بشكل جذري.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89592" target="_blank">📅 01:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇷
🇮🇶
ماذا حدث في سمنان بايران   تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89591" target="_blank">📅 00:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇮🇶
ماذا حدث في سمنان بايران
تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور الأمر إلى اعتداء على السكن الجامعي الذي يضم طلبة عراقيين . وبعد ذلك تجمع نحو 200 شخص أمام السكن لعدة ساعات، وقام بعضهم برشق النوافذ بالحجارة وترديد شعارات مناهضة للنظام في ايران . ويضم السكن نحو 100 طالب عراقي، وهم ضيوف في إيران، ولم يرتكبوا أي ذنب أو مخالفة. ومع وصول الشرطة ورئيس الجامعة، تم تفريق التجمع، وتبين أن الحادثة لا علاقة لها بالشرف أو بأي قضية أخلاقية حسب ما اعتقد بعض الجمهور الإيراني ، وأن الطلاب العراقيين لم يكونوا طرفًا في المشكلة، فيما ألقت الشرطة القبض على عدد من المعتدين. ومن المؤسف أن البعض حاول استغلال الحادثة لإثارة الفتنة والتوتر بين الشعبين العراقي والإيراني، رغم أن الحقيقة واضحة: الطلاب العراقيون لم يرتكبوا أي ذنب. وان العلاقات العراقية الإيرانية مبنية على أساس الدين والمذهب ووحدة العقيدة والدم حتى اختلطت دمائنا في ساحات القتال وكان يوم المطار بمطار بغداد خير شاهد على ذلك
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/89590" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
بعد عدوانها الآثم على مقارّ الحشد الشعبي في العراق، تواصل العائلة الحاكمة لأرض الحجاز جرائمها بحق الشعب اليمني، استكمالا لسلسلة الجرائم الصهيوأمريكية ضد الشعوب المناوئة للهيمنة الأمريكية في المنطقة.
إن هذه الأعمال الوحشية لا تزيد الشعبَ اليمني إلا إصراراً على المضي في درب المقاومة، وعزيمة على استعادة حقوقه، وإرادة صلبة لكسر الحصار السعودي الجائر.
إنَّ العدو السعودي المعروف بديدنه الإجرامي، قد ارتكب مجزرة تضاف إلى رصيده الأسود من الجرائم، حين استهدف بقصفه الوحشي الأعيان المدنية في مديرية الحزم بمحافظة الجوف، وهو ما يزال يواصل عدوانه على المستشفيات، والطرقات، وصالات العزاء، وسائر مرافق الحياة الحيوية في يمن العزة والصمود.
وإننا، إذ نجدد تضامننا المطلق مع الشعب اليمني الشقيق في دفاعه المشروع عن أرضه، نشد على سواعد أبنائه المرابطين في جبهات المواجهة والكرامة ضد الكيان السعودي ومرتزقته، الذين أثبتوا للعالم أن إرادة الشعوب أقوى من الطائرات والصواريخ، وأن الحق وإن طال انتظاره آت لا محالة بعونه تعالى.
كتائب حزب الله</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89589" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇦
انفجارات قوية في كييف.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89588" target="_blank">📅 00:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
رئيس اللجنة الوطنية لشؤون الاسرى في اليمن
: طلائع جيش مرتزقة النظام السعودي الذين شنوا هجوم على أطراف محافظة الجوف تصل إلى صنعاء وقدهم في ضيافتنا ( أسرى).
منتظرين وصول البقية خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89587" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
البعثة الإيرانية إلى مجلس محافظي الوكالة الدولية للطاقة الذرية:
إن تطبيع الأعمال غير القانونية التي تقوم بها الولايات المتحدة وإسرائيل ضد المنشآت النووية السلمية الإيرانية وتلك الخاضعة للضمانات سيكون أقل العواقب السلبية لهذه الهجمات.
‏ اليوم، يتم استهداف إيران؛ غدًا، قد يتم استهداف دولة أخرى.
‏ كن متيقظاً ومستعداً. أهلاً بكم في نظام عالمي جديد يسوده الفوضى العالمية.
‏ فيما يتعلق بالمخاوف التي أثيرت في أحد البيانات حول سلامة محطة بوشهر للطاقة النووية، نؤكد لكم أن هذه المحطة تستوفي جميع معايير السلامة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89586" target="_blank">📅 23:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي:
إيران تحذر من أن أصول الطاقة الأمريكية في الخليج ضعيفة بعد الاشتباكات الاخيرة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89585" target="_blank">📅 23:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇱
🔻
انتحار جندي إسرائيلي في كريات جات بسبب الازمات النفسية التي واجهته مع حزب الله.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89584" target="_blank">📅 22:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
الجيش اليمني يستمر باطلاقة عدة صواريخ باليستية نحو تحشيدات لمليشيات الموالية للسعودية في المخا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89583" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
اطلاق صاروخي من سيريك نحو مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89582" target="_blank">📅 21:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
🚀
🔵
إعلام غربي : رصد طائرة مسيرة أخرى في مطار لايبزيغ هاله في المانيا ؛ ويأتي هذا الحادث بعد أسابيع من اكتشاف طائرة مسيرة محملة بالمتفجرات بالقرب من طائرة شحن أوكرانية في المطار نفسه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89581" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
🇺🇦
أنباء اولية عن سقوط طائرتين روسية من طراز Su35 في سماء مدينة كورسك الحدودية مع أوكرانيا
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89580" target="_blank">📅 21:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f031a921c.mp4?token=sMHbkMet9NOMLQgODaDS5PxGoDogaPegFZMdCvmyOjJ4c3bh6a4Ljn4gn2RcSulXKn5fHtAsdenDCQKHZGEqw5nWtjc0T9IjTderATVc3WrUc4s-8kiwgiSk6ue2X3SbGuG6pxYbdIe02RZJBjw6XF62rOLH_VmVyqlvPsm-MjJ3b9p3FlmxhE55e6Uhkn9E0GJ5dCtBriZVPj3atbZ1eOAujCwM-Dd9xotPkLym74LjyJJuzia-XA6viwXy4PqQS9O-tZkoqOtWnwqG6XSZ6myNTFaELJkM8kCIM5Q1xBeMWNPCyvpr2iT8X6OX9nUEXSsJnkKhZAbdlEleQSMoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f031a921c.mp4?token=sMHbkMet9NOMLQgODaDS5PxGoDogaPegFZMdCvmyOjJ4c3bh6a4Ljn4gn2RcSulXKn5fHtAsdenDCQKHZGEqw5nWtjc0T9IjTderATVc3WrUc4s-8kiwgiSk6ue2X3SbGuG6pxYbdIe02RZJBjw6XF62rOLH_VmVyqlvPsm-MjJ3b9p3FlmxhE55e6Uhkn9E0GJ5dCtBriZVPj3atbZ1eOAujCwM-Dd9xotPkLym74LjyJJuzia-XA6viwXy4PqQS9O-tZkoqOtWnwqG6XSZ6myNTFaELJkM8kCIM5Q1xBeMWNPCyvpr2iT8X6OX9nUEXSsJnkKhZAbdlEleQSMoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مدير الإصلاحية في الجوف: انتشال طفل شهيد وجريحين نتيجة العدوان السعودي ولا يزال 35 نزيلا تحت الأنقاض بالإضافة إلى امرأة كانت زائرة لزوجها.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89579" target="_blank">📅 20:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgJlQtY4Camq2CSdsyAbZcfe_9GO7WBz171lNFEsXAVj-BNaHc5G4rH16sfL_h0BeQudVKu2svBv-DRXGZ8hsZhd6QzPB4-xNjkRBNMwoq5yaoszbJQcmas-rfYUYreLvyzJ59QG-aQozitpQTIblsHKz7JZrOtoOip0MHelyBISxUz_UkGPV0upv0tQoAUPTxCUSCGox9KF73XuV_6jIrqmwzxO14EaYVjeUvEJZq4DdqUyrvCk555r2kJvUFaY29kfFgCCBVKQ80vz_yI2fNXST4WPER5lGfn3ERM-GsfHSxbnIGb4laAJ4VLNJIGnQbMGQoTkhvzFGmVM2C5hKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاينانشيال تايمز: اضرار في ارامكو  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89578" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ee613451.mp4?token=nqRi47XtKKUfCen8mzJ9_CIwqXmdaast6RpeOzoH78pcgZHeqXzO97kMSdAqDedDU-DtJjQfSVi47K1LKjUkXMpTGX2IIBjIhiAOvK6KQGbaDOhiESLpoeivjIlhev5B87q78MSn1BhIIYPYQZePWSxB1oW4RETu6vNxp6HDMTv7ZKjS3fvkhRBgpNJ0SawMKn6M-pdNSfZRFXYNqzYMkTA3eh0B3NQAxjQKJ1IZxDSVZ6EmgTJCxdQlek7h2KkLXHvk5Q7TX3xgQtDRXsmrGgvNXFjyPi9ga337DmHJmLmeX719FUXkZHuDVtyOehwmrjLsq8lEmL3ReOJpO2HAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ee613451.mp4?token=nqRi47XtKKUfCen8mzJ9_CIwqXmdaast6RpeOzoH78pcgZHeqXzO97kMSdAqDedDU-DtJjQfSVi47K1LKjUkXMpTGX2IIBjIhiAOvK6KQGbaDOhiESLpoeivjIlhev5B87q78MSn1BhIIYPYQZePWSxB1oW4RETu6vNxp6HDMTv7ZKjS3fvkhRBgpNJ0SawMKn6M-pdNSfZRFXYNqzYMkTA3eh0B3NQAxjQKJ1IZxDSVZ6EmgTJCxdQlek7h2KkLXHvk5Q7TX3xgQtDRXsmrGgvNXFjyPi9ga337DmHJmLmeX719FUXkZHuDVtyOehwmrjLsq8lEmL3ReOJpO2HAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي: يؤسفني انه تم القبض على قصي شفيق بالجرم المشهود. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89577" target="_blank">📅 20:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89576">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_imbDXDFr2zJcAihNXoJYcgi3HTltDZf_idDvWcJu5nmD7AqKrQgjI0Pjf8M6daW5JwFk_zMEbnFCwZPj8BBSEMt04XEiFsnik-13mpAd897BVm1Xk3Q6LhFbfqUdAsuPTC4FzU4DbmHAQoaRVpoV2zZcIkPKYiuRNKVirqb2Dkv1JC8Ao8ZXOGxkCNYkxqpO--3lKfRYDGorEUzhDCIRDVlhIFo5p7ZXS2_xFqI5gDlPcCXidKo4P6_MfiC9NB5ysSpgUDP0D_8gL66bsj3E6KxJjlC7bCTu2MVefOOJfr97ak06jnwiZd0dZ9hbxrfiWIxb6K7p1jmkvz1naFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي:
يؤسفني انه تم القبض على قصي شفيق بالجرم المشهود.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89576" target="_blank">📅 19:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89575">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
الجيش اليمني:
تمكنت القوات المسلحة اليمنية بفضل من إسقاط طائرة استطلاع مسلح نوع CH4 تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية قبل قليل في أجواء محافظة الجوف، وتعد هذه الطائرة هي الثانية من هذا النوع التي تم إسقاطها خلال ال12 ساعة الماضية، والرابعة خلال ال24 ساعة الماضية، وتم إسقاطها بسلاح مناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89575" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89574">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89574" target="_blank">📅 19:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89573">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89573" target="_blank">📅 19:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89572">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في مشهد مثير للغضب..
رجل مسن يتعرض للضرب والإهانة لغرض الطشة وجمع اللايكات وسط دعوات لوزارة الداخلية العراقية بمحاسبته قانونيا
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89572" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89571">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
مدير الإصلاحية في الجوف: لا يزال تحت الأنقاض 35 نزيلا بالإضافة إلى امرأة كانت زائرة لزوجها إثر العدوان السعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89571" target="_blank">📅 18:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89570">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مشاهد من العدوان السعودي على الإصلاحية المركزية في محافظة الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89570" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89569">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني: لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89569" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89568">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
مصدر أمني مقرب من المقاومة الإسلامية حركة النجباء بالعراق
-النجباء تتابع عن كثب تطور الأحداث بالجبهة اليمنية و الدور الخبيث الذي تمارسه قرن الشيطآن السعودية بحق الشعب المسلم في اليمن .
- المصدر ابلغ نايا بأن النجباء قد يصدر منها موقف ميداني بالتشاور مع باقي فصائل المقاومة بالمنطقة حول الأحداث باليمن .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89568" target="_blank">📅 18:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89567">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89567" target="_blank">📅 18:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89566">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/89566" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89566" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89565">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇾🇪
المتحدث باسم القوات المسلحة اليمنية يحيى سريع:
بموازاة حصاره المستمر على اليمن أقدم العدو السعودي على خطوات تصعيدية بشن غارات جوية وارتكاب مجازر والتي كان آخرها مجزرة الجوف وتحليق بطيران التجسس وإمداد مرتزقته بمختلف أنواع الأسلحة.
إن العدوان السعودي المستمر على اليمن لن يبقى دون رد وعقاب، وعلى العدو السعودي أن يتحمل عواقب إجرامه بحق الشعب اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89565" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
🇮🇷
القضاء الإيراني:
صدور الأوامر القضائية من المدعي العام لمركز المحافظة بحق شخصين من المتورطين بالاعتداء على الطلبة العراقيين واستدعاؤهما إلى الجهة الأمنية المختصة، فيما تتواصل التحريات لتحديد باقي الأشخاص المؤثرين في وقوع الاشتباك.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89564" target="_blank">📅 18:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
معارك واسعة بين القوات المسلحة اليمنية ومرتزقة السعودية في محافظة الجوف.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89563" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89560">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvPYsXm-FeudJxbZAfE4pm-_9k1t4h_OWkPZ9RFkdiG1soHWNN0bzCy2uBUFBfyWqseYqQmLwltAh_NWSD1S4eHSsYiFDQZZN9WdXG5hG50HHYjHs-oQnGLg9HdGpsQrbZioKJSPepU131BzM7TlaCZhUmWov4FYTSXLM7qEJOumsvVcrWNTBz-U7hyQfYcuIZsAKP8Z8t5NzkhUvKMFS1MwNsQzplK-exH_3-FDt-h5RP7YEUoU9EcjW8xCXSGcs-3-WwGp80ELkkCQ35r2A1BUYTmAilAb7xmtSBncSMun6KEab82PlKoLea_245wxBrEc4c67z7fbR0Im0y-x_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0L4gTJm5sJqkhdW86XypqiZVVjoCSaqNarMFs_iTrORFaTW34GhyFonySqkTKZK--eJKuMOFiapa3Ez_uhnP_x5Rzd4fXJVxGqr34KTcFIBI0HXK51KdAE4iysaBgrz4zRnb91-bdoQr-Zbi9_49-6RYAsqVQAiiV_cpCTaGJwrax53dsVKNOwVONMmTQdIQij_602VXJT-_09qKhFkmklpLRA2bsGGUA2YpFHMLKRc-wUBao5iR0UuXSokqvGlUHE3NvV6c4GHGQ3t5FJ2HgnKpiiCk7y1DFjBV-dfrStGEgsUY_4xxeqIe15hPjergNslz06FymSmk2niN-9nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t24vfYufjOcuZfo9dN1chQROScR29W_3pJQ6m0x39UIdTD_gkheHgFoicDPfU-LRzZvUecI7sXorrv_9A_259GAG1pNBQT-XppzcR23kNuo1C90CWndjEDVXY6iUWVyHtAJyklzliFkeOuT2zUH8OPqLmv5BQyKG9NKLf2_idm9w-KaKo8JtqWQDtIij_GbGRHRukEZ9yUeBM-pvBQyPmxXAER0jWQzyzSlxnF6PIAw34-g2P5hSRZyCenRbi8bZF4T_j2UyXMq4g-KfQY43tLPJbxQ__0qzZJAzuu0QGcUJGAYMP9Qf2XYWfKGJnxyJS7OoqPUPl2BYbQYDnLCYSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان سعودي يطال سجن الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89560" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89559">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj2bchhFjOlJlO1boM1DSd7RnPVoF7BTb-X3EPvmoVGjgGDFaN4Tx9GoHn4qRr0jKxcBMmY_LFzUFVXhvFa6wKYYiCSM3Dh8ON5vz04N3ERxcD4UtfM2bx-iTIG2PR2zNz5Scm36l8nR06qn7_gX8ydYJK6jd8r9dzx1csF0C0b9d32AooBYO5p74ERHX4MLVxFCFKU477sCUFPJv5UWk-ffcYZIBFzvF75qf4HUrj9SVSR9IQXdEy5qYAPcAwFvxAVKUFcEHYLvVtiLS3CPyKLrhBpyMNfIM8ikBkW3NYLKSdDu41v7IfcYeBmnJsAwr2br0_TjKRQFsEY3l_q3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89559" target="_blank">📅 17:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89558">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89558" target="_blank">📅 17:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89557">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇸🇦
🇾🇪
قصف مدفعي سعودي يستهدف منطقة آل الشيخ في مديرية منبه اليمنية الحدودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89557" target="_blank">📅 17:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89556">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇰🇵
‏
وزير دفاع كوريا الشمالية:
إذا سعت الولايات المتحدة وحلفاؤها إلى مواجهة عسكرية جديدة، فسنتخذ إجراءات مضادة قوية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89556" target="_blank">📅 17:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇷🇺
وزارة الخارجية الروسية تغلق القنصلية الألمانية في سانت بطرسبرغ.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89555" target="_blank">📅 17:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89553">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء يطال النساء أمام وزارة المالية العراقية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89553" target="_blank">📅 17:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89552">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من استهداف القوات المسلحة اليمنية لشاحنات محملة بالعتاد العسكري قادمة من الأراضي السعودية
في معسكر
الوديعة بصواريخ باليستية مناسبة محلية الصنع.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89552" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89551">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇸🇦
العدو السعودي يستهدف بغارة محيط مدرسة عثمان بالروض الربيعي في مديرية التعزية اليمنية أثناء تشييع بالمنطقة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89551" target="_blank">📅 16:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89550">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
بلومبرغ:
العراق يواجه صعوبات في بيع النفط من البصرة بعد رفع أسعاره.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89550" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPiZdQ5wVzeRStT18N5P9DF-HzBf9meQ6bVkdRyfkcczWwR9UOSKlopqR9NDmvJW6Q-RYTxO6K7naNYH0Mb-a3Hob4LtoM9pXy6dnmPw347pPI9wdhEqoHplT0Fs245W52iwboWrkltfw4SMuleQ5xWf0NQ0R88_Z_-ZqlYh1sNH-jOH8idY9y2Y4VCf0XlJR6WslC2cCB0XBUstpK4ghAs6bKw--NL-3ygyzvxbw-nvJx2NFUhrwQWCDEjHL-D4ST5UyTtCPJpIUH8j6x_dtuCLwyF9yNSzMQIyXWqik1iK1M5s5AyJb4vTcOLWOvCs9XLfjAlbVjKS-4sgo5L1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتال مرتزقة السعودية في الوازعية بتعز</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89549" target="_blank">📅 16:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgGDoTS6CErLdmmv8MZnJf5W9ke3qrTC427rvivp66txNjQP1W_w6uMZjfQO4kGMwGHvdjdrju3ea29kZCxXEPF-Z7-DeoJP4wCVSEgp4VeBBSIx4Yuj40LjW5-oixCK67qIClR_op5daxCGaKj4doqHNjCXjloXb5ujO-WE2E1UhsCVkcTIAV1qSvf4VQ_seKgpkcoBXjP4YmSVSQF5tAbGdDzYjgJj65isw7D-w1vURykgovnhUxLmUQXFcsot7bC7Jqi_tk3g2q3-D5gdvA0cmyvGBSqUVMeC2uCrBu58U0IixHrVHrsGiINf9yNvBEHz_eQDQx-RTos3rNc1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابادة رتل لمرتزقة السعودية في الوازعية بتعز على يد بواسل انصار الله.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89548" target="_blank">📅 16:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89547">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89547" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89546">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89546" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89545">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
وزارة الخارجية العراقية تثمن الإجراءات التي اتخذتها السلطات الإيرانية لتوفير الحماية للطلبة العراقيين في محافظة سمنان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89545" target="_blank">📅 16:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89544">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
‏
بلومبيرغ:
أميركا تعتزم تحويل الملف النووي الإيراني لمجلس الأمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89544" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89543">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89543" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89542">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89542" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89541">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205a87d0b.mp4?token=YG0gaIplCc8Esr4plRgMXxtaMI2v4VJlO83VDu2zhF5MxNFWa8SCtW1uR0eDLy1PJLxhu_0DGdhFdkDLdNTVqfRgurkn8IrUkt6ymijKO0PIrhgZBnnYNkS9qvwWCsKPp0bA0Sp_flS1C_tauEDO2XHxIF9I0BL0sSNjnbHiFBXLi1PSU0zXrp7zP2Hc6Z8Qtp7gergvfvRH7Ifqh_2A1-vTDDO_uFACOfB705IqqItkOX9CzumJQXYs7LNKC8B0pipfBsKO8RSjvIJaHAcRHakHgLnUx6uB8NpmU0FIVrzVmdTtnAiQGBB9xmtCmEzgTyrsHhxngU3Usfk_zoZAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205a87d0b.mp4?token=YG0gaIplCc8Esr4plRgMXxtaMI2v4VJlO83VDu2zhF5MxNFWa8SCtW1uR0eDLy1PJLxhu_0DGdhFdkDLdNTVqfRgurkn8IrUkt6ymijKO0PIrhgZBnnYNkS9qvwWCsKPp0bA0Sp_flS1C_tauEDO2XHxIF9I0BL0sSNjnbHiFBXLi1PSU0zXrp7zP2Hc6Z8Qtp7gergvfvRH7Ifqh_2A1-vTDDO_uFACOfB705IqqItkOX9CzumJQXYs7LNKC8B0pipfBsKO8RSjvIJaHAcRHakHgLnUx6uB8NpmU0FIVrzVmdTtnAiQGBB9xmtCmEzgTyrsHhxngU3Usfk_zoZAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
🇾🇪
مواطن يمني يرد على عصابات الجولاني التي تنشر قريبا ستتعانق دمشق وصنعاء: "اخرجوا نتنياهو من ريف دمشق ودرعا، اقل شيء اخرجوا نتنياهو لنتعانق على انفراد".
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89541" target="_blank">📅 15:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89540">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الرابعة والنصف عصرا مشاهد نوعية توثق لحظة استهداف واحتراق شاحنات أسلحة قادمة من السعودية في معسكر الوديعة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89540" target="_blank">📅 15:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
العدو السعودي يجدد استهداف محافظات الجوف والبيضاء ومأرب وتعز بعدد من الغارات الجوية وصواريخ الكروز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89538" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اعتداء يطال الخريجين القدامى أمام وزارة المالية العراقية في العاصمة بغداد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89537" target="_blank">📅 15:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e737d33906.mp4?token=T4Wh-1wsd-_0q8PcbvAPkss-Hbmu9EP7UKk_ZTj9jbF2F2dpQEhNMQZd3RRKHeiaJyWh6LvZsIkl5ZQkEgwVQwhxCwWhrD4iscDqGg6ImBq2bbEueH8JW5MnVDlv6V3ObCXlNkIGyev_LsAgkM4u3DHt9kSOkS4WybIzBMoQ31hWkDxNnwQTlGIUc3sZR42PWgtVbNDChnIY6ktuVHbf8l_SKfZHiFb0h9jz7lIB0r7yZhTTnP162-VEg5oL7h5XAFLGq5YzwBs5_udEc6f55w-TPH7OfsugoPCUJwIpZXjPJNkHQN21FqsDqi2t6r52c3voQxjUN_6qRqdIJlUcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e737d33906.mp4?token=T4Wh-1wsd-_0q8PcbvAPkss-Hbmu9EP7UKk_ZTj9jbF2F2dpQEhNMQZd3RRKHeiaJyWh6LvZsIkl5ZQkEgwVQwhxCwWhrD4iscDqGg6ImBq2bbEueH8JW5MnVDlv6V3ObCXlNkIGyev_LsAgkM4u3DHt9kSOkS4WybIzBMoQ31hWkDxNnwQTlGIUc3sZR42PWgtVbNDChnIY6ktuVHbf8l_SKfZHiFb0h9jz7lIB0r7yZhTTnP162-VEg5oL7h5XAFLGq5YzwBs5_udEc6f55w-TPH7OfsugoPCUJwIpZXjPJNkHQN21FqsDqi2t6r52c3voQxjUN_6qRqdIJlUcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء يطال الخريجين القدامى أمام وزارة المالية العراقية في العاصمة بغداد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89536" target="_blank">📅 15:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89535" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف التحشيدات التابعة للعدو السعودي وتدمر مدرعاته وآلياته وتكبده خسائر فادحة شرق محافظة الجوف
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89534" target="_blank">📅 14:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات تهز ارامكو السعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89533" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89532" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89531" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان: إجراءات الحكومة لتنفيذ برنامج حصر السلاح بيد الدولة يتم بموجب خطة مدروسة تبناها الإطار التنسيقي عبر لجنة منبثقة عنه تتولى اعدادها وسيتم الإعلان عنها حال اكتمالها وفي توقيتها المناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89530" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
من المبكر جدا الحديث عن استئناف الحوار مع أوكرانيا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89529" target="_blank">📅 13:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس: أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89528" target="_blank">📅 13:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جيش العدو يعلن استشهاد المنفذ  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89527" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم اعتقال المنفذ بعد العثور على سيارته بالقرب منها حيث جرى إطلاق النار عليه بعد محاولته طعن قائد القوة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89526" target="_blank">📅 12:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني
كاتس:
أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89525" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني   أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89524" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89522">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇸🇦
🇾🇪
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء محافظة البيضاء، وقد تم استهدافها بسلاح مناسب.
وتعد هذه الطائرة هي الثالثة التي تم إسقاطها خلال ال24 ساعة الماضية بفضل الله وتأييده.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89522" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89521">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89521" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89520">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني
أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89520" target="_blank">📅 11:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur9T2dcgmrKlFZM7DNskt5DiNpNf7uazUVXz6mNlHnDNKMCeeCgt_05jcHeckbF6mtVggQxSdqNPu2xQF8wMj0JesJtVBerwwGem9-5DgcelsiuYOmQ2eKFHV67ahZOeMmZifR59i5DhFfcjfk6ttIOL2JygT19csbpXoRqPDclSDWXmfxzkcFgn-DUarYqMqaQRR7p3wdx02rOZmdalELI2MdVM_baGq4meQdu1i6v8tVB_f4-XMqDdC3cXQEaYoCEDxwvfG1ct_P8Tqky-nJDznVMn47uzX1OM7wNKZn164EZOMGnknKXKACOEEDKUaW2jGCkkiZzONy_XqnDi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوربا تنهار ببطىء   ‏يتصدر حزب البديل من أجل ألمانيا اليميني النتائج الأولية في انتخابات ولاية ساكسونيا-أنهالت ؛ الحزب يعتبر نازي وعنصري متطرف ويرفض الحرب ضد روسيا وحرب امريكا في ايران</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89519" target="_blank">📅 11:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🇮🇷
🔻
المستشار الرئاسي الإماراتي قرقاش : التعامل مع إيران لا يزال قضية محورية بالنسبة للإمارات العربية المتحدة ودول الخليج الأخرى.
- من غير المقبول أن تتعرض ناقلات النفط والسفن للتهديد المستمر في مضيق هرمز
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89518" target="_blank">📅 10:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89517">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89517" target="_blank">📅 10:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89516">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇱
إعلام العدو
: بعد أسبوع من إعادة فتح الشواطئ في حيفا: وزارة الصحة تحذر الجمهور من السباحة في شاطئ كريات حاييم حتى إشعار آخر، وذلك بعد تلقي نتائج ميكروبيولوجية غير طبيعية في فحوصات جودة مياه البحر، والظروف التي أدت إلى ذلك غير معروفة في الوقت الحالي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89516" target="_blank">📅 10:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89515" target="_blank">📅 10:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تصاعد أعمدة الدخان من مقرات الإنفصاليين في محافظة السليمانية شمالي العراق، نتيجة هجوم بطائرات مسيرة انتحارية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89514" target="_blank">📅 09:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏وقع انفجار للألعاب النارية بالقرب من كنيسة مكسيكية خلال احتفال ديني، مما أسفر عن مقتل ما لا يقل عن 10 أشخاص وإصابة 64 آخرين
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89513" target="_blank">📅 09:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89512" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruZE49Zv0u3jAyktXWIl_iXgM3uTXGhMe8q4gv5_coXtDBx8gXvgsroC3SPpsf8o63uJmDTXQowBjrMxYY_4xoiQZ6dACz4xXAZ28WGcOoyZdv78LvWg1F1KLWO2314mzWLkefFs0M3Bc26Tsq5ha1SQExm0xUKyxfpfLrxilzjMKhwCfDhwAfNutq4aLSV6jEro6oMr3l_CfHMxSaCzMy3ol28yfe2d6jNPIrCOXW2xKWjFvsR8MxBU2fEW3vfDJNdpfWQ8zCaSlrfqEDsAZcykXXjmjLpn491hoVGZ4URRb1BHNkpZwS03QjsRwbBSDeWC9twM_H2sJzoIRmYbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة
النفط يلامس ٩٨ دولار للبرميل الواحد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89511" target="_blank">📅 08:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89510" target="_blank">📅 08:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89509" target="_blank">📅 08:00 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
