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
<img src="https://cdn4.telesco.pe/file/R4iz227nIC58QkdJbhGGjs66IoEyc0b7yd6mUI1FktF10AQfueS6EX-IW3MOuvYdFqITqH38hEWGUVDXx869JV3TKyXxWn4qB2mLEOO6B0um-pCFj0sojrDyRNmZo19OSUPQAOXxMp4Z1njWXQU32afHyj6J74B_edeHfFioAPcgu6YBear02B6pce3pDtMPKC96B2374ZJS3a2hf75EGjh2p-sMUaxUDx2LZ1pEer3aj539F9ASpIKp4kwVnQyBamM3kSMQJe-LqP_ZNf4S1WPdMLcStD4P9-Yy4OF8OM0tmfwJvw_e2RYl0aDON73VMYPNg2vW_mGsCEJOWzb5PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 261K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-82652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  مجاهدي قوة الجوفضاء التابعة للحرس الثوري، في المرحلة الثالثة من عملية "المعاملة بالمثل" وردًا على انتهاكات النظام الأمريكي المستكبر والمتجاوز، قاموا بتدمير مخازن الوقود وأنظمة الدفاع الجوي "باتريوت" في القاعدة الأمريكية في علي سالم بالكويت،…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/naya_foriraq/82652" target="_blank">📅 07:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسؤول عسكري اردني:
أي محاولة للمساس بسيادة البلاد ستواجه بكل حزم.</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/naya_foriraq/82651" target="_blank">📅 07:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/naya_foriraq/82650" target="_blank">📅 07:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/naya_foriraq/82649" target="_blank">📅 07:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703c922c.mp4?token=ng_53-njBr2CdfQYyKUHZShwyaATOg9oPJO6lvrMpiI0EFXCfVO4RorYzgDxOjuX0zOxu5W-PaL7I9iiJLPntOGs9XVWwA5C5kexK0pZhGfxm9_T0aLKD4DOi2ADw7_9gynMiLN0A-edMdYuAqxLMD1DKguikt81h4RyPh3QvhkYGn2eUNSdL_VsHwJozfj7jNINKnkg1SZly0TB-K85tLQeLV0k6dAb3TxnCXoJ1Clv2UUTjyaHhTSpp1oT4CIOYcHtAvDdUntjsqoWEiyaWRMiY4o3-S7XAbet8B4uFv1MVDheDoP-Ss7PBYj7kNbyzBivAJu4Iiz5fh9hbths1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703c922c.mp4?token=ng_53-njBr2CdfQYyKUHZShwyaATOg9oPJO6lvrMpiI0EFXCfVO4RorYzgDxOjuX0zOxu5W-PaL7I9iiJLPntOGs9XVWwA5C5kexK0pZhGfxm9_T0aLKD4DOi2ADw7_9gynMiLN0A-edMdYuAqxLMD1DKguikt81h4RyPh3QvhkYGn2eUNSdL_VsHwJozfj7jNINKnkg1SZly0TB-K85tLQeLV0k6dAb3TxnCXoJ1Clv2UUTjyaHhTSpp1oT4CIOYcHtAvDdUntjsqoWEiyaWRMiY4o3-S7XAbet8B4uFv1MVDheDoP-Ss7PBYj7kNbyzBivAJu4Iiz5fh9hbths1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/82648" target="_blank">📅 07:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/82647" target="_blank">📅 07:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/naya_foriraq/82646" target="_blank">📅 07:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwawJqZWZ9fJRyENTQpgiRbBloWGeQOqRq71FHVRrxFrEAnB0jIYftv4QV16HcR__rzVosKChLXozIggZeQGJHkS7inaznsZWdTBYSh9Z8qbcSNvjzKCQeGyfNbSH8azY9cGRP9S4k86nXTjmoIwVKp2nbV86b02ydA2jRgme99p2GCBCLe_01MJHUixU3luNFpJ-KMNSv9Jsx19p4TGi9vQiwqLhFCydr2u9utgEnv_5ZP8N-Lbjt_M96ipOIXlmlAWGit_8Zxf0e97cKj500QA5VwEE3MwgmTIewEoDQKe0fJ-1pYPRns8yjyis9lBwuEliQrQPEy1EUoYodE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
We will stop any ship not following our order,
Hurmoz from 0 to 30 km under our control</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/82645" target="_blank">📅 07:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4f4be296.mp4?token=u7oBUURR6fSQGX3OzyB_K2BOOp6lpGAGIhp6zy60cpI5Dcs0i5xdJFXzH0PqtYHLw8XJmX6jr-DzI47a2qNOQ63tMbKsydNt9WR66kTTmA97Qz0ppKwxmdPn0WZqvGC97w7ippC_g1jXffzf08bsP-HnIpB9yOlCXod5oFp1L_bljjmD0v4H9DvPAszlETvu-X4RGnm3hF7zFWkmdnw2-Jj3H_BwWKs6juYeATg-Q2x0HsxXdS9a6hDIDr0AfMRrB_S9mR4PAQFciQkdz7g2qBbfmGLO9fC80wx35beLtoe2GJwWN2NhjB2EGHtpucvs041s7hEoF4areVOwdKQfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4f4be296.mp4?token=u7oBUURR6fSQGX3OzyB_K2BOOp6lpGAGIhp6zy60cpI5Dcs0i5xdJFXzH0PqtYHLw8XJmX6jr-DzI47a2qNOQ63tMbKsydNt9WR66kTTmA97Qz0ppKwxmdPn0WZqvGC97w7ippC_g1jXffzf08bsP-HnIpB9yOlCXod5oFp1L_bljjmD0v4H9DvPAszlETvu-X4RGnm3hF7zFWkmdnw2-Jj3H_BwWKs6juYeATg-Q2x0HsxXdS9a6hDIDr0AfMRrB_S9mR4PAQFciQkdz7g2qBbfmGLO9fC80wx35beLtoe2GJwWN2NhjB2EGHtpucvs041s7hEoF4areVOwdKQfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سحب الدخان تملأ سماء القواعد والأصول الأمريكية في البحرين بعد إستهدافها وإحراقها من قبل القوة الصاروخية الإيرانية</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/82644" target="_blank">📅 06:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c1059f20.mp4?token=CfUq4B8ouFiXiOUuainXHsvtcy8xvaitzD22LgtfvZANz-ZSQWaZnr1Nfvum12v8NR3WBD0x0bIZ6g5OiycoLqNpZM-liGF8pBlNeFB3ajfUruUISkXikpRlb3CLaFe2s6Y269MmIztP1qddKRsgDGmfCzlglBm4XK_cz9UEht55I49ldsHf6jG8vshAP1R8i9-yXqN_3F16N1h6pB59IJW9t2i3htg2MP2anjIQ85CcMhGNhBDcGg1VL-EJCNdrLOLJCo5ztPwVRxkVFdvtQLQwknlOeA4gR7rf64JFVFfKGHj_zRIVUN9gZxgEWL2qZ8zxRnaKNGSQmgeYCpHQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c1059f20.mp4?token=CfUq4B8ouFiXiOUuainXHsvtcy8xvaitzD22LgtfvZANz-ZSQWaZnr1Nfvum12v8NR3WBD0x0bIZ6g5OiycoLqNpZM-liGF8pBlNeFB3ajfUruUISkXikpRlb3CLaFe2s6Y269MmIztP1qddKRsgDGmfCzlglBm4XK_cz9UEht55I49ldsHf6jG8vshAP1R8i9-yXqN_3F16N1h6pB59IJW9t2i3htg2MP2anjIQ85CcMhGNhBDcGg1VL-EJCNdrLOLJCo5ztPwVRxkVFdvtQLQwknlOeA4gR7rf64JFVFfKGHj_zRIVUN9gZxgEWL2qZ8zxRnaKNGSQmgeYCpHQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد في سماء البحرين عقب الضربة الصاروخية الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/82643" target="_blank">📅 06:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2dde51952.mp4?token=sdxxNRo_xywiBSF0wIeXmoQncz_QAOzUJz1Qf2dFED2EDAR0ytI515HPrSCZC7UgSKOrvoFpOJxpv46l-XE_JIYDWiWt1vrqnMTR9oMERprAnQJfgM3AMVtmutwUliPc8Y6RFSW4z43xQC0HgaSHH-MpHpi_NO0oLRRcwX_T8DWxYNk1L4-b5rmHG76roXb6onXMNmUE6irhR9tBBeC33tdLhNfBfUtOkqdUyaUlZchMg2-lHn-T_8tqU63BdCCXDLGRE6YOJKXNDkOAH9Op-0hgvfgXg5VY2fgkzRbKgJsdYmmk6_yPelCi03eWJVkZrsaURhXi92rdrGPYYbtzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2dde51952.mp4?token=sdxxNRo_xywiBSF0wIeXmoQncz_QAOzUJz1Qf2dFED2EDAR0ytI515HPrSCZC7UgSKOrvoFpOJxpv46l-XE_JIYDWiWt1vrqnMTR9oMERprAnQJfgM3AMVtmutwUliPc8Y6RFSW4z43xQC0HgaSHH-MpHpi_NO0oLRRcwX_T8DWxYNk1L4-b5rmHG76roXb6onXMNmUE6irhR9tBBeC33tdLhNfBfUtOkqdUyaUlZchMg2-lHn-T_8tqU63BdCCXDLGRE6YOJKXNDkOAH9Op-0hgvfgXg5VY2fgkzRbKgJsdYmmk6_yPelCi03eWJVkZrsaURhXi92rdrGPYYbtzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  استهداف مقر إحدى الشركات التجارية الأمريكية في البحرين والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/82642" target="_blank">📅 06:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b44a7e1802.mp4?token=cgxE4T7p0dXBQO6nzDJoC1Qh7txOv4eu2TppCKxLcYwrIc5onBYYMO7WkeAKk6o-HirX35PxHTTR1uRSFKzTjGpVFssY2HZjPpuylF2bN1WhqceSpV48ZHj6LWke_C9qZkWYIBabqsMJUlBaHh-z4PZMbzWAWNxvuTFkQbmsuRNs0yaM2BFrQkRKUS4aswdazTKt78TKRFg1CeC9KpFELlfDDJEwbkizdYrCfFvT0_KPI79BF0VttHhIMGl-kuHn2MEfl6wKVzsuTVea3hZ5QuFZhbC-j-c2zdba-x6EJGurft35m3lrTmB91V8OQPn914SKwrWUJKHCLPU8nVf5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b44a7e1802.mp4?token=cgxE4T7p0dXBQO6nzDJoC1Qh7txOv4eu2TppCKxLcYwrIc5onBYYMO7WkeAKk6o-HirX35PxHTTR1uRSFKzTjGpVFssY2HZjPpuylF2bN1WhqceSpV48ZHj6LWke_C9qZkWYIBabqsMJUlBaHh-z4PZMbzWAWNxvuTFkQbmsuRNs0yaM2BFrQkRKUS4aswdazTKt78TKRFg1CeC9KpFELlfDDJEwbkizdYrCfFvT0_KPI79BF0VttHhIMGl-kuHn2MEfl6wKVzsuTVea3hZ5QuFZhbC-j-c2zdba-x6EJGurft35m3lrTmB91V8OQPn914SKwrWUJKHCLPU8nVf5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/82641" target="_blank">📅 06:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وصلت الصواريخ وانفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/82640" target="_blank">📅 06:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/82639" target="_blank">📅 06:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/82638" target="_blank">📅 06:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على هذه الاعتداءات، قام مجاهدو  الجوفضاء التابعون للحرس الثوري بتدمير مراكز مهمة لإصلاح وصيانة المروحيات، ومنصة طائرات الاستطلاع الإلكترونية من طراز P-8، ومركز قيادة وتحكم الطائرات بدون طيار التابع للجيش الأمريكي القاتل للأطفال، في قاعدة…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/82637" target="_blank">📅 06:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
الجيش الأمريكي:
فلوريدا - أكملت القيادة المركزية الأمريكية (سنتكوم) موجة جديدة من الضربات الهجومية ضد إيران في 12 يوليو/تموز، حيث استهدفت عشرات المواقع في مناطق متعددة بذخائر دقيقة بهدف تقويض قدرة إيران على مواصلة مهاجمة الملاحة الدولية العابرة لمضيق هرمز.
وضربت قوات سنتكوم، ولأول مرة، أنظمة الدفاع الجوي العسكرية الإيرانية، ومواقع الرادار الساحلية، وقدرات الصواريخ والطائرات المسيّرة، والزوارق الصغيرة، مستخدمةً طائرات مقاتلة أمريكية، وسفنًا حربية، وطائرات مسيّرة هجومية جوية وبحرية أحادية الاتجاه.
ويُعدّ مضيق هرمز ممرًا بحريًا حيويًا للتجارة العالمية، وإيران لا تسيطر عليه.
وتتمتع القوات الأمريكية باستعداد تام لضمان استمرار حرية الملاحة أمام السفن التجارية، على الرغم من استمرار العدوان الإيراني غير المبرر، والمضايقات، والتهديدات، والتصريحات التعسفية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/82636" target="_blank">📅 06:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5-xotnFzop4VLOWj8O1fljJCqVO7ei3outlPjAcom2NJmCu_lpZUxV4GiaPbrMtSLOKqYr6WYFzvXa0d5E-IxshtCsufYxXilksALWGqfC3JY9z2_5Ck1d83cCHOWvVa5c23ln8bdi60_RJCaCUOG-HfpRAlF4WNslnVBIFxeAvphQEq4VgI67xS-_g3B27NKjr0Yyd0mu4iFVc35FTyiSAnRUu6CKbSVrk205mxgS8fxOaAES3uT-RiWIquiB61yWQvG6Czwv4nEUzyj7SPJzcLKcWb7h4wDA5tRLp2Hgf2LphwmonT_Kt9j4fq4YC6hIgbm4CqNqDyJG8Jc5IWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
عقب تبادل الهجمات بين إيران والولايات المتحدة..
أسعار النفط العالمية تلامس 80 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/82635" target="_blank">📅 06:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  بسم الله قاصم الجبارين وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ کله
🔺
في الليلة الماضية، وبعد عملية قامت بها القوة البحرية لحرس الثورة الإسلامية لإيقاف سفينتين متورطتين، اللتين أطفأتا أنظمتهما وتحركتا في مسار غير قانوني،…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/82634" target="_blank">📅 06:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوي انفجار في بندر عباس جنوبي إيران</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82633" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
بسم الله قاصم الجبارين
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ کله
🔺
في الليلة الماضية، وبعد عملية قامت بها القوة البحرية لحرس الثورة الإسلامية لإيقاف سفينتين متورطتين، اللتين أطفأتا أنظمتهما وتحركتا في مسار غير قانوني، مما عرّض الملاحة في مضيق هرمز للخطر، كشفت القوات الأمريكية "التي تقتل الأطفال" مرة أخرى عن طبيعتها الوحشية من خلال التعدي على القواعد الساحلية التابعة للقوات المسلحة في الجمهورية الإسلامية الإيرانية.
🔺
في المرحلة الأولى من الرد على هذه التعديات، أضرم مقاتلو الإسلام الشجعان النيران في عدة مخازن كبيرة للصواريخ ومخازن الوقود في القاعدة الجوية "الأمير حسن" في الأردن، وذلك عن طريق إطلاق الصواريخ والطائرات المسيرة.
🔺
تستمر عمليات الرد بالمثل التي يقوم بها مقاتلو الإسلام، وسيتم إطلاعكم على نتائجها في البيانات اللاحقة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82632" target="_blank">📅 05:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e8cbafb1a.mp4?token=OEbPzI8cR8ZjXof7_kTB39dXTNn3yW3fqUN90VwMLRb1RKeYEY9f-sD6FGPZs2Ato11zWos6I2zq638_dYFon_qAmuaJoAiXVHrFJtZAdlDsEHulRPgkEDLBRmh4NXPH3USBVylANsnnmG_4iAJO8RKvP-vN4Cn8prQLaJkpzbb1VEQAcoz4rzyjPaiTL9ipiqc8UNZcdtaOpm96CFHBcavq5XHbQuZDoVluMHGaOyBBPjN6Gu7NMViuIkBBqJuoYYHoe1uS3sauDNzBsllrOvVYtnGNejPrRNxtW9fSKYbyrMhgWEiELgCilZd8_nvoKKkuvcsQpRfyHOKkEB4rGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e8cbafb1a.mp4?token=OEbPzI8cR8ZjXof7_kTB39dXTNn3yW3fqUN90VwMLRb1RKeYEY9f-sD6FGPZs2Ato11zWos6I2zq638_dYFon_qAmuaJoAiXVHrFJtZAdlDsEHulRPgkEDLBRmh4NXPH3USBVylANsnnmG_4iAJO8RKvP-vN4Cn8prQLaJkpzbb1VEQAcoz4rzyjPaiTL9ipiqc8UNZcdtaOpm96CFHBcavq5XHbQuZDoVluMHGaOyBBPjN6Gu7NMViuIkBBqJuoYYHoe1uS3sauDNzBsllrOvVYtnGNejPrRNxtW9fSKYbyrMhgWEiELgCilZd8_nvoKKkuvcsQpRfyHOKkEB4rGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران تشتعل داخل مقر الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/82631" target="_blank">📅 05:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">النيران تشتعل داخل مقر الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/82630" target="_blank">📅 05:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl4_cx_TDh5RcJ7hC2WbQOoLfZfA7BVvJ9-EBiZh8jcxbc0RFbJlXWKANAFnScekCNlzYQ-UhGJTxuMPOgnw0diajekqwYwx9GloU_lGpiZNI0_jiuwMSFxo9GhvzwzOWiO4pIYKKwnbeJuthM4qpuP3l1Z53etlmDzJRrXwiJnpA-r0-H8PRiRNqDjn89oVrK1PGl-ZNrtmG-l7ctHxSdNzXxdNTn6Y7UBQCxC2q16bOm4UshreW_KFcLen_T4AZxoS4S78BcNCBCH5sS-4xlNBT1fyYb2ffMmoULLZNJ-4gxNjVvNEK2jFJECVtSoc1mDlEPB2B5v_5haboVE53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82629" target="_blank">📅 05:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b1b68cef9.mp4?token=X7jjnK07vZWghCHZMIRdoQ8CbautGdgtCYa3d-2ZtDw-2He3OXeAMCEtbxkWV328nr144xDeCWAYfblxk1PjB24c3pqvh6NTJ7XUy8qnLwZBsMBcpCg6f9hgsV8Hz0ZTQsOD1WjcLl50FgR0KrTrClgLIGPd9Egci1q4CMPNnTACz9Zc0_r7X-5oi96HlPlYlwadWNJ8_Tm_f3Fg1FfL4Qo52qPYGNQB9v6tKM6ZQ3PYG60BGRvSU_xY42BCIh3eapTdzGu0aFatc85xSt2Zlg-5qn8_dCp4qkfd3N8e8_1v5wqRa-WS84VyWphx15D6WMuphD9NxZ9FFtnNKawsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b1b68cef9.mp4?token=X7jjnK07vZWghCHZMIRdoQ8CbautGdgtCYa3d-2ZtDw-2He3OXeAMCEtbxkWV328nr144xDeCWAYfblxk1PjB24c3pqvh6NTJ7XUy8qnLwZBsMBcpCg6f9hgsV8Hz0ZTQsOD1WjcLl50FgR0KrTrClgLIGPd9Egci1q4CMPNnTACz9Zc0_r7X-5oi96HlPlYlwadWNJ8_Tm_f3Fg1FfL4Qo52qPYGNQB9v6tKM6ZQ3PYG60BGRvSU_xY42BCIh3eapTdzGu0aFatc85xSt2Zlg-5qn8_dCp4qkfd3N8e8_1v5wqRa-WS84VyWphx15D6WMuphD9NxZ9FFtnNKawsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية كبيرة تنطلق من إيران</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/82628" target="_blank">📅 05:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umHlKzfzqrcOkxdosNKqT7YH_L1_3H-0mKA2aXPC-0MUCXJ_kTjWTYHl5x07pZQX7eyGXlWcPzy-9ldFdfCC55SYfds4OXW0KiN6N33n5e3CQglQooSrSH5pFCjMc5oHSsCOQIMgKC7gEMuSPhfPUqoqkbm7GoLz6uBtkEWwW3Fjxgz640CAIQGxXzbmdpvlFvgi7POYO5wPy0Y5g_wmA5yUuwRXv3H2oWRBEugSMMY2CtYa37sWPlJLcMpHR0du5e_QEtZdPqY0_BmwgFAWwc0aLWUJUvkcvgeWjY2IDSLgtkTQyOAFjWfP_CnLxx8XETcyV3kfSP4WWl-JT_aqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozW7TiTYrGFdnR3dmdR0hmyNwRE-D4wSPCXxPqmdtzZH0PwqGlDs72mQI-2GvZZb0z8VhJlRQEuuBaeilm7b395mU-v15D8LC3F_z4nGriHK7g5ttHtn2R_Pw3uqsK6b119Mp7nTQtoIW_QrIm_GQ6M8ES6sJ3SuR75-gFvva9CSCSoKhshEHnwuuv5EV0iIyhDXsLR8aDTJ1uYd_rz-XMFZNni0U7BoepoPpgAy0oAsdqcisBCuSCDRbWimsWshvvhZVrOLmYzbUSlkPo_SztEc6OyeXFLcDZRxUiGUgjbSa7olbpBeY10zo79k0hzp6K0yTIyn9SeaDssqVRTFvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f265dd887.mp4?token=YCsFYyjGXAmLarXBDQJBtJhKsBr4fu4ArCgljG0fnyTbEbU2clgOWpBgYswLlHML0qXZT-HPOlZtPmILPzt6c8i3sTUtEMuTH9eWwzoRLLUhNmWqfQrUFxl100WGZdBNdnOzuNn6U-h8sd0PcT8ntG6HfZZBI5L5ClWfRKXebf6wpuUAI27y811czMwKoEVrNCcmNa-b_ke5mRvhlOUI3pjqXoCTgaijoBaqxGKAy6d0VdXLnTVkNCRnuZJR-JcXa-gGgcMcHBvOazu7zzeM2brIUl4lXDCwIJ6QzLCjx9YdruFPt5rIEVRuR3Q88MM4iylnW3WXbQMLnrpcsvt6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f265dd887.mp4?token=YCsFYyjGXAmLarXBDQJBtJhKsBr4fu4ArCgljG0fnyTbEbU2clgOWpBgYswLlHML0qXZT-HPOlZtPmILPzt6c8i3sTUtEMuTH9eWwzoRLLUhNmWqfQrUFxl100WGZdBNdnOzuNn6U-h8sd0PcT8ntG6HfZZBI5L5ClWfRKXebf6wpuUAI27y811czMwKoEVrNCcmNa-b_ke5mRvhlOUI3pjqXoCTgaijoBaqxGKAy6d0VdXLnTVkNCRnuZJR-JcXa-gGgcMcHBvOazu7zzeM2brIUl4lXDCwIJ6QzLCjx9YdruFPt5rIEVRuR3Q88MM4iylnW3WXbQMLnrpcsvt6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات جديدة تنطلق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/82625" target="_blank">📅 05:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">موجات جديدة تنطلق</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/82624" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/82623" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نفس نیروهای آمریکایی در منطقه را خواهیم برید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82622" target="_blank">📅 05:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/82621" target="_blank">📅 05:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/82620" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات عنيفة تهز الأردن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82619" target="_blank">📅 04:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pmy_zqMOqsUKZB4bYpDoocBC08wy3ld08EboUEsfSJlPcZDJguqgl92SDzxCVJfRnBMxXYmchEnvkTeWnaVZ3ivYYXCQToCjfL7xnYiYkVgTPFczpC1GcolXgvoowJRk2mypigwOOxNI2CH_683fq1fxHGponw_7k-kAaa5t6E7Lz4Mk6bLaJDqJUFiU9IXHWVrxvouXI9p4nsDU7cobrJj3VW8fO82tsMsXYMOYADWFkv8-xKe48OCE0L0xdLmp-491uaFQ2LPs-QGqI3m3prEL6cZpOMwZ3bi9VnqRkzzENQB3lW4p1X7uS5kdg_RIQSu8I8u1SY_B7rRmwnSuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApN5W7J8LiwPMlOkcb7m9TJ_LqnBx16IkIPL2lw-W6B-B6Jr8zDl2JZ4_EbnCrQMTd7iFnMEIbReamIs2jZ4Gam3LJJP5ABhZimWBH6erRIxV4Ahu5ZPJnDux4AtrxnVL-7fdjK060kN6g1lB2FmAhjgfGC014027G4rBVu10SyeJ9VDTXMq5HZ5_i4SkH34ySAadDdDUZETmj0L27DihRG949plAaOc_ti0yE-ldO2a7kAd9XaHIrCJgZMw2TWNad3EpjvEH170koHFZgphOao74OgYnjZSP756GmcPuo3o3yox9HCQ5QiwIcObbav0xbLsI5nDbMxI6QA1AhtIrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رشقة صاروخية كبيرة تنطلق نحو الاهداف المعادية في المنطقة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/82617" target="_blank">📅 04:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfkguwaur_u9hKz6isdx0W3DNzwZoUmoR4kZdjlkQM881v5WQzXa9JLfua0yaeY7J6E1AjLzbcxPO62mF3QNcGGfLHyMyzkNiSupgfDOQLDh5PSYRM9XwnhzNQbx5NPG_KEmPRGMHO5AHWQe_hicsSxd4eMY5zZQeLBOQiPgS9lXbST-YE_W6uvEuSnpzBzT-rneyRygJcnCqBLpE8uuxzdqI7S8vHfGXPaha2nvabKhvBMbxTXFaP8yROEIkBoAYkWmZ4r9k_wimpB-nDC2fWc1EOTHUw58wYfAsckgElrlnlWYAtIQhP7XVKmf5EXEY5LJ03vT-R3ye5n_cdG2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر  موجة صاروخية جديدة تنطلق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82616" target="_blank">📅 04:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJE3m0-gZjJUongrB9sIw08rPaddLUJdWlbvcNiV2mt1xqx0lpdcl9h5mR1Jh52t5WtI7w6xIKGKA9XeqgcXyexzmGZQrE6Tsqg7U2e6s2MdPQNVFzhlHBwjz1dEbAPewlzM3nFNGZkSBNTLn3gKy10CaGZeqiyw5h6Xh5gVhFRuI-Ah-lq3algFN-THPnb_KobQ3YPjVoV1JkMYrjPlSFrYp2hMU9DljU6djXpTtODNdMkD84RufJklrHnJ3qxnKRLF0NfKhDzV4xf1600JAjoRBFLtqNWl9s5-5lxz29X_xkMKJt0sHSU_ixRBAiTCHJ4j5uVx9Ooq8jKMnu4meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
موجة صاروخية جديدة تنطلق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82615" target="_blank">📅 04:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">إطلاق موجة صاروخية من إيران نحو الأهداف المعادية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82614" target="_blank">📅 04:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2I-Q9BN_AU9W-aGKvtUikBa6wNhj_O5xl4pQBpC2bKPvlnbx6HkKQE-NVWul9gExvnzvbOx6QBt0wVHO9Swj5hKLSww1v-EdJVjRXATT0Dgn9u-HACotjYOatVk-KFLbqpwathS2f_5PIR6IiLS1eBFQrk-cGVV3MpRxsF9v02GQsKlkRisrcJIktMmL8klC6vpJRdpRRG_q7O8wW3qHuN0HjEoKCAHqotq8kJGWrZum0TIBarhUptT14beM1NyAN10CD4Kr_lRyI_fgOvINMWmvKHtvx9i2bMzt9XJZbp5hM-FReACkgRuQFLc_J_IYq2gGmXWEzrsHYEQkBKMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يَا ذَا اَلْبَطْشِ اَلشَّدِيدِ...</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82613" target="_blank">📅 04:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">يَا ذَا اَلْبَطْشِ اَلشَّدِيدِ...</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82612" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول أمريكي:
الضربات الأمريكية ضد إيران لم تنته بعد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/82611" target="_blank">📅 04:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82610" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
مصدر إيراني:
عودة الهدوء إلى محافظة خوزستان في جنوب إيران بعد عدة هجمات أمريكية طالت عدد من المدن.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82609" target="_blank">📅 03:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
مصدر إيراني لنايا:
الأنباء التي تتحدث عن انقطاع التيار الكهربائي في جميع أنحاء الأهواز غير صحيحة وكاذبة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82608" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة تنفيذ العدوان على مدينة الأهواز الإيرانية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82607" target="_blank">📅 02:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عدوان على مدينة انديمشك بمحافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82606" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد إطلاق صواريخ من الأراضي الكويتية نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82603" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82602">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات في مدينة اميدية ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82602" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb3b90797.mp4?token=uzRif_xFYrTq0YLP4JKF4p48N93upAIeDuAY4RlGXDQ2qzwcqwQSYpqIEYXdvS5ydZIgXzcRxz5EdREX2rKEGPTxyGK8KuQMY7kl4-csLzIPdT3TgZS6xnukYutBen11IArwhzzBbcIYkJ2KGLzpCUdQ5tGyQPTf8WX0x3iixAjPYJ69s2xINQdyIG6tqQK2GM_ZvjmAwocS9CBBOYuz-r7B_QWfur3_vim3pPGwPWGAWbm36l0EnldLrxxZEvXQOmCAYv58WWOGudPKDFiUKvy7QgEBjrpeC7Y2bGZdCeSJeD7XJjw4O7ZBreB3MltG3sZ4XzCeyP1NVQPX69YqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb3b90797.mp4?token=uzRif_xFYrTq0YLP4JKF4p48N93upAIeDuAY4RlGXDQ2qzwcqwQSYpqIEYXdvS5ydZIgXzcRxz5EdREX2rKEGPTxyGK8KuQMY7kl4-csLzIPdT3TgZS6xnukYutBen11IArwhzzBbcIYkJ2KGLzpCUdQ5tGyQPTf8WX0x3iixAjPYJ69s2xINQdyIG6tqQK2GM_ZvjmAwocS9CBBOYuz-r7B_QWfur3_vim3pPGwPWGAWbm36l0EnldLrxxZEvXQOmCAYv58WWOGudPKDFiUKvy7QgEBjrpeC7Y2bGZdCeSJeD7XJjw4O7ZBreB3MltG3sZ4XzCeyP1NVQPX69YqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية في مناطق جنوب غربي البلاد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82601" target="_blank">📅 02:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82600">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات في بهبهان ودزفول بمحافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82600" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82599" target="_blank">📅 01:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات في بهبهان ودزفول بمحافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82598" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9f5eacac.mp4?token=HNf_UL2fysB79CV2Ryw-FhOnw16cvzHuCnGSnJhyZmUp6-wn9jRDXyUFL5b0HCf2UuACovVI9q2O7mMVr9yGb4NRmaq_vVkLGsy6-BkKMpi7Hya_w7pgpQ7QS2BzY43zvZzJ4KSp5Hs-w_zx-yONhBfEIgw8Kgt8VunU61euY9S045REGJaGiBiyhD1oCBkIVKkYyHkuQoTVIBieHpENJtfxdZPiSUbjCxsHGcIUbIi5fOSub9Rvs8ovZfKLhWX9E4GJfxd-Z12lfy2I9h0ZL4W7wYINYh4_e4DO2244aXqu46z-80OBKAS2FNecH4zRZWKbqIv27PIQgr10fKcCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9f5eacac.mp4?token=HNf_UL2fysB79CV2Ryw-FhOnw16cvzHuCnGSnJhyZmUp6-wn9jRDXyUFL5b0HCf2UuACovVI9q2O7mMVr9yGb4NRmaq_vVkLGsy6-BkKMpi7Hya_w7pgpQ7QS2BzY43zvZzJ4KSp5Hs-w_zx-yONhBfEIgw8Kgt8VunU61euY9S045REGJaGiBiyhD1oCBkIVKkYyHkuQoTVIBieHpENJtfxdZPiSUbjCxsHGcIUbIi5fOSub9Rvs8ovZfKLhWX9E4GJfxd-Z12lfy2I9h0ZL4W7wYINYh4_e4DO2244aXqu46z-80OBKAS2FNecH4zRZWKbqIv27PIQgr10fKcCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة ماهشهر</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82597" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82596" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JoQzg47215oJR6jBuQIbWxKucWeQzeSewh0xo7KyZ4odcfHlSCRSmum8NN5dXFlLxtvfIWOjMsADAGnKcoD0ePgNzrg4lD48kTrx4ok0nloo19Qw0ClhCMXN8SUzzH9gDzwYJDLJWN75lLcABgdJIy1o1SAkVVBw3IE6a-_Ws0Kv0cdgVVXLnGhFZ6SGSPjUf4JE52fmy2zBx0sWOLjSk0tqF1ZGA9E19Iw_Wy2iFfym0ss0Yaz_ccPiesAQKx8ICwp2qPIRuzoWEbwWO2WJnNbIBcoBQ-gS6WR5gjEYpBWggEHac9uhbCujQ_Ka-djvL15hw2uSw7egcovLsgPyow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JoQzg47215oJR6jBuQIbWxKucWeQzeSewh0xo7KyZ4odcfHlSCRSmum8NN5dXFlLxtvfIWOjMsADAGnKcoD0ePgNzrg4lD48kTrx4ok0nloo19Qw0ClhCMXN8SUzzH9gDzwYJDLJWN75lLcABgdJIy1o1SAkVVBw3IE6a-_Ws0Kv0cdgVVXLnGhFZ6SGSPjUf4JE52fmy2zBx0sWOLjSk0tqF1ZGA9E19Iw_Wy2iFfym0ss0Yaz_ccPiesAQKx8ICwp2qPIRuzoWEbwWO2WJnNbIBcoBQ-gS6WR5gjEYpBWggEHac9uhbCujQ_Ka-djvL15hw2uSw7egcovLsgPyow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82595" target="_blank">📅 01:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82594" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات في محيط مدينة خنداب بمحافظة مركزي الإيرانية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82593" target="_blank">📅 01:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjdnfoF5dwrKZh8uxrMxxWP1yIJW8ninrzFMhqzxyqyldNKbdkoYM1a8YKleI-Ic5xplSlAY-C1pm7ZaT2SwRt7wpNBtaT2XIugOc6PV_gMJKRNJAFs1li7AynYvQRUw9bE6qHgS0Yx389URjNNPp7Yhm4D63KbsCXqUVp8gbSaCEIMxCG1jzvFXMhH8JRR4Evm_pTLtPvijQQSw4GmMyiS4waQqxfMBbXz_5YNTpKRRT8nuHT4BM9rNyNsQIYQBecGb2tRZ07JSqIbPaYxpIT12645xUlKwP7EGvhQVjXFCPHrAQ_yXRo4ZyOB8Ocym-RTgz7SQVsOGW7l8i_dEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد إطلاق صواريخ من الأراضي الكويتية نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82592" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82591" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82590" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات في جابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82589" target="_blank">📅 01:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyJmJj5nQTTy5wRUa04fqyzG0nOVfAraUiX_SzKP8_KFNJt2h1JRAcFDLFFMAng5JmBJE2EIuPZSxVQuLpYps1r3WAnXgDF1hFSAAPtvmpEgYYzOL2wBkI91-rrRZN64U4aQ6dilYUn2xOMXw9IpFw-ytunCnN5Q7bGtI-5F3-ohK5s8QATTT5bBDTscaWHFsey5CFC-UZnXVLD7yu7ldjaZddBaPkLUyaMBNLubFseFk22aALUeG_W7US5mlXi0eAEeG-geR9UdKvvVPeBh3XW7nLIqEdDDwGgN5ez5uk019uRHgoGe_fLY-zbQELcEgxYnrlnmlwl_wxoRUm0kug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=MPIT-xjA9fIDz2ugLuHwusBrV17zwlQT_sAAqhCxxktNmmyhR-ZP4ZCpIhQ9OS3dbXOsSB04CvZiMzzWSmJh1GTZGLacdcNVW2eeJAhtr_PSjHrVgIOJunek3FN1zYLE5sZuCPqqczfD4WzEw0NuF9V9sqzerGXi7H3CIPdiLAvHoOzMSIMVtEtHTugVsqPg4x3UphksYGCdTf-wyeYeBV2lk7G0Wz1kRkkRWoih8e_ZMJ7hNtFvl6QgqJ2vVCvxEHbu85egs02JezT2lOB7yhPjvphnCYd48XqJxHIWNJZQOxd0IyZrUkG1Qmri-78cm82cm2T-Edm-0jP-BIZE9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=MPIT-xjA9fIDz2ugLuHwusBrV17zwlQT_sAAqhCxxktNmmyhR-ZP4ZCpIhQ9OS3dbXOsSB04CvZiMzzWSmJh1GTZGLacdcNVW2eeJAhtr_PSjHrVgIOJunek3FN1zYLE5sZuCPqqczfD4WzEw0NuF9V9sqzerGXi7H3CIPdiLAvHoOzMSIMVtEtHTugVsqPg4x3UphksYGCdTf-wyeYeBV2lk7G0Wz1kRkkRWoih8e_ZMJ7hNtFvl6QgqJ2vVCvxEHbu85egs02JezT2lOB7yhPjvphnCYd48XqJxHIWNJZQOxd0IyZrUkG1Qmri-78cm82cm2T-Edm-0jP-BIZE9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سيريك وجاسك وکنگان وبندرعباس</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82587" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF2GwE9LixRjslG-fTqqmE0bzG7WaTdVhh3b2Yfh06SeXXWNqFmju1KSmZN9PvDTctOwBPnBvt4uHWZOfXM6x9-oPBURtSi_nLMDV7mQd_bwASXQrnsze-nKOZ95W2JrFkZzJk2QANpQyHwyEdvYIrLVFb0-64PJS_zUh3bfPldmTXLSBdSZFxzzabCOakdN_hcQVfGZY7b3VCRpK-1Dc69kMJoJLOVRmI9mn4vwfBHB2XIsG6tDv-5WEy8aTRPSQSHJdVQwTuT0hBawJgfUuWFJLpx4rQRG5vXmnio3kIOok4XuA3IAQz9ubydw2iQ1Fpu4SWd59l-F9zthx0KF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ طائرات التزود بالوقود الأمريكية تنشط الآن بشكل مكثف فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/82585" target="_blank">📅 01:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1d9hjQcgrI3pzoFaIpkykw_dqxFV103BOSy0-BdHBlbZu6NUjqnMPhX6ASWaQBYl6TSJ8pxQcOaayKj3hZazcjCU6XM8Pwo5R1QYgMMuoUEdt2cllS4NKOv_7FMkrD6zLD5X4TnRfuDJMPx2UFqBv4ArlhrRRM9JcDeOurTJbFVCTxo_TlwfyCnMxguVPZnfZT4CH4tMU_orhZaCX7d4UJhwLuPb72vEXIOUwNVDgwQrq5Wv1RDvfPs1N47CAxf2hGiiJUiGpgB-40P97tAyKWEm8CjD1gziH3OlRHABw5_2Ek-qf7lNJ4nZzN9RoNusTh8hHmi8aGzU8nY6EgMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
المواقع التي سمع دوي انفجارات بها في جنوب إيران إثر العدوان الامريكي والاشتباكات الجوية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82584" target="_blank">📅 01:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
ما تسمى بالقيادة المركزية الأمريكية: ‏
في تمام الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية شنّ المزيد من الضربات ضد إيران لمواصلة تقويض قدرتها على مهاجمة البحارة المدنيين والسفن التجارية التي تعبر مضيق هرمز بحرية. وقد وجّه القائد الأعلى للقوات المسلحة هذه الضربات لمحاسبة القوات الإيرانية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82583" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/82582" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82581" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e93d3a70.mp4?token=l-qc6NpfBZF4qRQqlyGhARYNICMgQg_n9ye01Yr52bXH4LtlB9HC_PAq2WDZW6m2Y8XfYKPB9doU2AhGYM_YgmP9QL_8dxVJWeve0n22w7clUdKerjxRZSR8IKfR77igr-V4XCuQSNc4B22VkERB9yojFyrcOSXHGw1hk0u5Ly2eWgdMwLHfA2i-TFnR6kVb6xE7MnYChJ3EMS2ir5AIAnVW4Vq7eapHsO8zlIRzrWhR1UhtWyeBAOpLmXZ3VhkX_jDFG4q-urVOje8_mzP1MXX76ViTNV-jPb8rY6BmWK1cDI0eTnLaursGM_e7gteFO_WB6qpS0oha-yR52oY5-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e93d3a70.mp4?token=l-qc6NpfBZF4qRQqlyGhARYNICMgQg_n9ye01Yr52bXH4LtlB9HC_PAq2WDZW6m2Y8XfYKPB9doU2AhGYM_YgmP9QL_8dxVJWeve0n22w7clUdKerjxRZSR8IKfR77igr-V4XCuQSNc4B22VkERB9yojFyrcOSXHGw1hk0u5Ly2eWgdMwLHfA2i-TFnR6kVb6xE7MnYChJ3EMS2ir5AIAnVW4Vq7eapHsO8zlIRzrWhR1UhtWyeBAOpLmXZ3VhkX_jDFG4q-urVOje8_mzP1MXX76ViTNV-jPb8rY6BmWK1cDI0eTnLaursGM_e7gteFO_WB6qpS0oha-yR52oY5-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انباء متداولة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82580" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00811a2e17.mp4?token=G8LevjGEymrLbCS-d3dUhWisYyrj8j4MMFD06UCmgzNL--d3ojY7nJGnKSITbiUJw9NcjXstzQc8hZ1GZRCTsI9LX9ZNY8CjtRxHsVfCHme9xGSRB3LKyq5wasHM6EYW_UjUNgQzMpueckVohm3LQ_luGBg3q38lP6U_zvAQI4KpAOjlC2xLgdPNgWSSlP4eivOGZAQSQ0epsM3nTOrCxRGmWOhod6C8UFjZuuYa4IdQzo8eR-Ej1AIXoFrmpkWIyAkzyoN6ZunhIYRWtNIlt6Mm23lDGB1ADjlDZ2h4Pz_hmp6OMY2oZ7QdZbR2wC2RHp-r1s2Wlditufzi7wSU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00811a2e17.mp4?token=G8LevjGEymrLbCS-d3dUhWisYyrj8j4MMFD06UCmgzNL--d3ojY7nJGnKSITbiUJw9NcjXstzQc8hZ1GZRCTsI9LX9ZNY8CjtRxHsVfCHme9xGSRB3LKyq5wasHM6EYW_UjUNgQzMpueckVohm3LQ_luGBg3q38lP6U_zvAQI4KpAOjlC2xLgdPNgWSSlP4eivOGZAQSQ0epsM3nTOrCxRGmWOhod6C8UFjZuuYa4IdQzo8eR-Ej1AIXoFrmpkWIyAkzyoN6ZunhIYRWtNIlt6Mm23lDGB1ADjlDZ2h4Pz_hmp6OMY2oZ7QdZbR2wC2RHp-r1s2Wlditufzi7wSU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
مشاهد متداولة لسفن روسية تحمل النفط تعرضتا لهجوم من طائرات مسيرة أوكرانية في بحر آزوف.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82578" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
ما تسمى بالقيادة المركزية الأمريكية: ‏يتم تزويد طائرة مقاتلة من طراز إف-35 إيه الشبحية التابعة لسلاح الجو الأمريكي بالوقود فوق الشرق الأوسط. القوات الأمريكية متواجدة باستمرار وجاهزة عند الحاجة.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82577" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex1ujWY-ZerM9F1AC1alMGK51KR9QrFL7O6lpZNsvAB9d-wRToi8ycOHk4w8lOyUsOzhrw3ZqpTuQ6DBp5Utd-R19RCCM_rFT2ycQRcvxyx5eAwl_RqxhdQH5ATFpZYF8CgAKZL0uVhc3WFhiTHlznqqqujVeAquaIzsnfEf5P5iKgP24vJ3wUq-R63bXul9Pz0YBOXzLoIYOyl-owjXaEG7K2fXoqJrhGIac9IjN_FSMUMm8AR5inPY_Ji5upwu_yPwp9z3Fv2KdxDVzqL5BO-b6aG021nufQpGiKCeetG65rwCOHitmEbk0sjgBQ2_FGD6A547j2w84RRqi-Di7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة إنذار مبكر أمريكية أقلعت من قاعدة الأمير سلطان الجوية جنوب الرياض في السعودية وقامت بمهام مراقبة مطولة فوق مياه الخليج الفارسي قبل عودتها.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/82576" target="_blank">📅 23:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مراسل نايا في إقليم كردستان: مشاهدة أجسام مضيئة في سماء محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82575" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
اسماعيل بقائي: ‏ينبغي عليك حث الدول المعنية على التوقف فوراً عن السماح للولايات المتحدة باستخدام أراضيها كمنصات انطلاق للعدوان على إيران.
▫️
‏ليس من المسؤولية إطلاقاً إلقاء اللوم على إيران لدفاعها عن سيادتها مع عدم محاسبة المعتدين على انتهاكهم الصارخ للقانون</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/82574" target="_blank">📅 23:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/82573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82573" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTlyi9c5E8zdcR0HA-Wl4tO5zKbxeNmdt0XVrLNv_0Y-M0P2SIcbQPNa7mR8q5QcqKUzlKgwNQkDc9uJhJ35lS7FpEO4tt4dNtGlxHNzBjfx2t7vdMZs1JQUqiUvJWVaE_fbO3gFtfxHKqpDH7veOeU2ka4K2KjmmcxSmH46uf98Tlzsow68JVCMiaVYWP6KNS20pI5GBiZDTWruGRW_MPzqMO4HPSjqTGELIdBLJnyseA_gq9BYpCnj-NZscTN0ZUHFf2dfiblwKUIrMEUFBvBUU-_Z61T5lmafVgh9GpZ2HeGYbGpKzgp-gSBNm-k8IjDTdh0ROd_p-krMoC2EgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَمَن يَتَوَلَّهُم مِّنكُمْ فَإِنَّهُ مِنْهُمْ ۗ إِنَّ اللَّهَ لَا يَهْدِي الْقَوْمَ الظَّالِمِينَ)
​في الوقت الذي تواصل فيه آلة الحرب الصهيونية الأمريكية ارتكاب المجازر الوحشية وسفك دماء آلاف المؤمنين والأبرياء في العراق وإيران ولبنان واليمن وفلسطين، يخرج وفدٌ حكوميٌّ عراقي إلى واشنطن للقاء الإدارة الأمريكية. وإذ نعلن في المقاومة الإسلامية رفضنا المبدئي لهذه الزيارة التي تتزامن مع غليان قلوب المؤمنين والأحرار في العالم حزناً وكمداً إزاء استمرار تلك الجرائم البشعة، فإننا نؤكد الآتي:
​١- إننا نتعامل مع المواقف بحسبها؛ فدعمنا للحكومة في ملاحقة الفاسدين لا يعني منحها تفويضاً مفتوحاً في سائر سياساتها، ولا يبرر تمرير مشاريع ترهن مستقبل الأجيال لشركات ترتبط، بصورة مباشرة أو غير مباشرة، بمصالح الاحتلال، وقد ثبت أن عدداً منها يمتلك شراكات أصيلة مع العدو الصهيوني، وهو أمر يتنافى مع مقتضيات الكرامة الوطنية ويخالف الوفاء لتضحيات الشهداء.
​٢- نجدد التأكيد على أن استمرار وجود القوات الأمريكية على أرض العراق يمثل احتلالاً، وأن من أولويات الحكومة العمل، بمختلف السبل، على إنهائه وفق الجدول الزمني المُعلن.
​٣- نعارض التبادل التجاري وإبرام العقود مع أي دولة تكمن العداء لشعبنا المقاوم أو تعمل على مصادرة القرار السياسي وهتك السيادة، ونرفض في الوقت ذاته أي احتكار أو هيمنة اقتصادية على مقدرات العراق، ونحذر من استبدال الاحتلال العسكري باحتلال اقتصادي أشد خطراً، بعد كل ما بذله شعبنا من دماء وتضحيات في سبيل تحرير الأرض وصون القرار الوطني.
​٤- إن تحرير الاقتصاد العراقي من الهيمنة الأمريكية، التي تفرض سيطرتها على مقدرات العراق وأمواله، فتقيدها تارةً أو تفرج عن النزر اليسير منها تارةً أخرى، يُعد من صدارة المسؤوليات الوطنية لأي حكومة عراقية.
​٥- إن لا يتحول مراد القبول الدولي إلى التنازل أو الانبطاح لدول الاستكبار ويوصف فيما بعد أنه نجاح حكومي.
​٦- إن التطبيع مع الكيان الصهيوني خيانة عظمى، سواء جاء تحت مظلة الاتفاقيات الإبراهيمية أو بأي مسمى آخر.
​٧- إن تمثيل العراق في أي لقاء أو محفل دولي يجب أن يستحضر عظمة هذا الشعب، وتضحياته، وبطولات أبنائه، من دون ضعف أو رضوخ أو قبول بالذل، فنحن أبناء مدرسة «هيهات منا الذلة».
​٨- يجب عرض أي معاهدة أو اتفاقية يعتزم أي وفد حكومي إبرامها على مجلس النواب العراقي لاستحصال مصادقته، بعيداً عن الالتفاف القانوني بتغيير المسميات، كإطلاق وصف «مذكرة تفاهم» أو «إطار تعاون»، بقصد الإفلات من خضوعها للرقابة البرلمانية.
​٩- نحذر أي شركة احتكارية تسعى إلى استغلال ثروات العراق أو الاعتداء على حقوق شعبه، ونؤكد أن خيار الدفاع عن الوطن ومصالحه المشروعة سيبقى قائماً، وأن شعبنا يدرك أن قوة الموقف الوطني أسمى من كل عقود الإذعان، وأن سيادة العراق ليست سلعةً للتفاوض، وأن إرادة الأحرار لا تشترى ولا ترهن، وأن حقوق الشعب لا تصان إلا بالمواقف الثابتة والعزائم الراسخة.
المقاومة الإسلامية في العراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82572" target="_blank">📅 22:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88ad999a7.mp4?token=OWxqF-ItuTfZPeR7DhDK53tnf5_DV0wzLlL-Q-ndcB10zDvXr4tsNePfDnpvEFsM0vp5T4PGwsh7RRuVIBkCFjalyr_uQkLPfTc6V6k5tBGDXAn1fbmG7WQ9zmG9-9ODL_ES6-s_SOxbqvz342W-tU_YaOvEA8pcUYYJphvGvozfDaM4-WyR_NuetypcsUMFuomEu7nPT91P9KO50PIIofCOnSThbah6B_XzD8d0l1ysouWO2DRQaZH306yaHEXdirCks5lxVGU6mBRQG7Zqba8xGubBXApkadpai3SxSzPhnE-GdC1XDyV8mVLarZiQepPgX1vzhyFo9zSVNpiEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88ad999a7.mp4?token=OWxqF-ItuTfZPeR7DhDK53tnf5_DV0wzLlL-Q-ndcB10zDvXr4tsNePfDnpvEFsM0vp5T4PGwsh7RRuVIBkCFjalyr_uQkLPfTc6V6k5tBGDXAn1fbmG7WQ9zmG9-9ODL_ES6-s_SOxbqvz342W-tU_YaOvEA8pcUYYJphvGvozfDaM4-WyR_NuetypcsUMFuomEu7nPT91P9KO50PIIofCOnSThbah6B_XzD8d0l1ysouWO2DRQaZH306yaHEXdirCks5lxVGU6mBRQG7Zqba8xGubBXApkadpai3SxSzPhnE-GdC1XDyV8mVLarZiQepPgX1vzhyFo9zSVNpiEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
البحرين:
في ختام مراسم وداع الإمام الشهيد علي الخامنئي(رضوان الله عليه) حشود من المعزين في قرية السنابس ترفع نعشا رمزيا للسيد الشهيد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82571" target="_blank">📅 22:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHZxPzW2NkTHoMw3NV1MvgoeCV6Iu_uGD_l-vhPLTN-2Sxia5lbNiqdwv5SSr8Su5e2zjyU-HhhEBVW9Qtebmieeq-bl6n5rVP2fCL3NB7Jnvm0-rsWc_x74o-IQYyn7_w3Nn4mfJk42vUFdXIfJzL9LneIKgB31Jem19ArYpT9hnFS5IAZVtzVySff_5RefTcxDySyLtrWuhqTPyv2W3UFJrswOxyGuD5Fn4v0-5Gwef7o8GcFu4tF44GTGGxFBv0vR9-yORgQt7oFeb-RIm_jBJCDkcpZhpv5o6AKp2M5Zntiql04eVP5UREmR4As6y3DjHqy2wXFhARAL4lwKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
Nato bases in west Asia be careful this night, have a nice night baby with love from IRGC</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82570" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDLxvFaVXA-EZX0BhrTR-trmPnLKZJgrtPOSWeysWxeQpTZZ8zo2iejOsC-FabuR6grSa0ftbUD0qCreIumruZ91q2A4dEMi-n_aYbheF3_nOkojWFGMgqXLkiHjhvTq1l_mdTt0knqmmJ_n-LpF1WtvU_ZsuhMz7W_gcuHd7L6t8yi7hSr163DHGcRyi8tzSKC5ZGhsv1dEIZrpre3v8EgYvfqI3pbVY_GYtWrEdLZlTK2T5TYG-i_2SwxoVfX6hZL29uBad1jrwEcEGyusuEgSNXQsfuhDet8eEk1kL26OCtkcz3QCDzFdIt33euD3r0zLObuacAO-uulM6haKyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تحذير عاجل  إلى جميع المواطنين والمقيمين في الكويت والبحرين والإمارات العربية المتحدة: نظرًا إلى ارتهان حكّامكم، واستخدام بعض المناطق السكنية في الدول المذكورة لإطلاق صواريخ أرض–أرض باتجاه إيران، ندعوكم إلى توخّي أقصى درجات الحذر.  وفي حال رصد أي منظومات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/82569" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShGWPbk3E_QrPTY7F9_emUJ_UxV2Z3KxkLi7tAdfZIMtEPM7IpCVn9RHAjhN22VaFS63KdBWbb77A79pM5WpKdNNsFg-wekTvnQO2dlI8BiNi4gDKA0qZmKkYKIaBGwBnQtZGpfuf8AWaTsUPVhohX7VJ_Bya8TjvwPHgCOiudPfCpU2koDMD-gRplcqz11rvuCbH_9eZRzvw941T7A-HfBR2dhowA3j6nM51XFKGAZbpSIRP8e26Zjl4vfdLD1cQE5X8gL-KV_y_OoD1HXyiflKNAflx5rq2Q2wYP4_ryxnXpojDeqRF0Jvh4o4a9Rh_XfBfHoP6SlUiUxd--BbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:  سيصدر إنذار عاجل قريبًا، ترقّبوا.  يتبع</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82568" target="_blank">📅 22:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طيرهن مالته عمارة
Our friends it's Iraqi Poetry mean we will fly our birds soon</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82566" target="_blank">📅 21:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/82565" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:  سيصدر إنذار عاجل قريبًا، ترقّبوا.  يتبع</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82564" target="_blank">📅 21:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسالة هامة لشعوب بلدان خليج فارس  يتبع</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82563" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسالة هامة لشعوب بلدان خليج فارس
يتبع</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82562" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDDWMDEeeR-Xeic3D-YsWce5PZH09jt4NOEapfBauNbh1lsYde9MWQ3wZy3f6yBnETaKv4ecG0LQmWsECjQRIwP3LCpjKlLST31PebBNGIxxcJQWhnuTwDnRgc1hGNO0TMUGU6CkQ-bVXNdSm92OFFyNzF8NJYm4821bU86UQdZy8Xm3CKtMay1d3d8xQ17rz0lD9ZMZqZgbzzLddA8-6Ii3NuUOn74rIz-Gui13DiWO_vDOH9CsPkM2W_1pQZ840mGhtKn1NjkYmteiNe7sr_6t2ZHrAHZGOOJfnkfaesGvRQd0tt7JP-WF_gzkxXH7YI2GmM8Dknb6SYSdVGKRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82561" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82560" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:
سيصدر إنذار عاجل قريبًا، ترقّبوا.
يتبع</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82559" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
مصدر ايراني ينفي هجوم على محطة بوشهر النووية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82558" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/82557" target="_blank">📅 21:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5019ff156.mp4?token=Uk3mXk8Om0Xjh95hs2RQmJk_x_y9N1zQW5E7_DRNnoZW98pgimYQeg5lWyCc0Mkf-MYgshKU_idJwCgzrgPqcrvH-mBpdCf6otXInY4yEqoFtXb1M-cueaiMNMSeC35-pbJKDGAdK58NAOtrxZnkMHu-3pIEWsHYg6DwzWTYt3lfxi-fJHvziSNWraFEChu5skD2LXW4QAsH7ptxxfnIwphjHOASblyvXE9z1Xy8013YgM6_HAXMgPPMXOiEJTaISkb079ph-f45TTtXC1lpHMq_TsHk29CulYo7nC33ARAo49e6s94pjdISVJ08gYc0C04gSDvw9-0vQzlGBbbOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5019ff156.mp4?token=Uk3mXk8Om0Xjh95hs2RQmJk_x_y9N1zQW5E7_DRNnoZW98pgimYQeg5lWyCc0Mkf-MYgshKU_idJwCgzrgPqcrvH-mBpdCf6otXInY4yEqoFtXb1M-cueaiMNMSeC35-pbJKDGAdK58NAOtrxZnkMHu-3pIEWsHYg6DwzWTYt3lfxi-fJHvziSNWraFEChu5skD2LXW4QAsH7ptxxfnIwphjHOASblyvXE9z1Xy8013YgM6_HAXMgPPMXOiEJTaISkb079ph-f45TTtXC1lpHMq_TsHk29CulYo7nC33ARAo49e6s94pjdISVJ08gYc0C04gSDvw9-0vQzlGBbbOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران حربي كثيف مجهول فوق سماء الأردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/82556" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/82555" target="_blank">📅 21:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
‏
اعلام العبري:
الجيش الإسرائيلي في حالة تأهب دفاعية استعدادا لعدة سيناريوهات.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/82554" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فشل جديد للمنظومات الدفاعية الأمريكية في اعتراض الهجوم على الكويت.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/82553" target="_blank">📅 20:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚩
SUDDEN ILLNESS  Lindsey Graham is Dead! Iran Lego is ready :) Who's next?  #KT
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/82551" target="_blank">📅 19:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/82550" target="_blank">📅 19:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
مصادر أمنية لنايا..   الجيش الأمريكي نقل إصابات خطرة  لمستشفى قاعدة رامشتاين في أوربا نتيجة الضربة الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/82549" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/82548" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82547" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
مصادر أمنية لنايا.
.
الجيش الأمريكي نقل إصابات خطرة  لمستشفى قاعدة رامشتاين في أوربا نتيجة الضربة الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/82546" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الحرس الثوري يستهدف بوارج وسفن أمريكية مخالفة بمنطقة الكيلو ٢٠ بمضيق هرمز الإيراني</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/82545" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82544" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/82543" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
