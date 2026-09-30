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
<img src="https://cdn4.telesco.pe/file/KvMRwPuDtpbIO-7p1sCDSzxRBmR0cXQo5tlUFByk0WVBLCxPyft15WxNId2Hy4ZlqV7fp-IcH-9du0EfXk_ecw1e6GKIb3s2K0ICLqzz4iamRC1lWURO6SgizKpTf4vUWhhYMKkKQ20NCEQQ7kFiLxPG6exLxN4odnvlmlxg-Ob0kTW070k1b0PwpSurZWej-gT8E31UHb8ZKRyijobrC9kGcH2ZjZfbbTGpa8tD5qMnN68hhnk8Sn96maUsNiUasZk2bS0x9EDPChXTt--3yC_LEVa3s92UjlEX34r364uVojQTUPU6TxKqTRndFtMpaAbpihaFoaRkhp3sP7wh4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 06:39:04</div>
<hr>

<div class="tg-post" id="msg-92030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
اعلام اجنبي نقلاً عن مسؤول في البنتاغون:
الولايات المتحدة بصدد إنهاء عملياتها العسكرية الرسمية في العراق، عدد من عناصر مشاة البحرية سيبقون لحماية بعثاتنا الدبلوماسية ويذكر ان واشنطن ستحتفظ بقدرات استخباراتية واستطلاعية يمكن استخدامها داخل العراق
تم سحب بطارية صواريخ باتريوت للدفاع الجوي كانت متمركزة في محيط أربيل</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/naya_foriraq/92030" target="_blank">📅 04:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8859995348.mp4?token=YmeMVMA9LQF4HuJ5fuxe8WxW2cix4V0NTYRCCHtXBEPDCTL_Oea8Hkxnjk_8MWaFpLY6OcF_wCWpuMAe0a6DPB6R0XXBx8_gXgJUyBaaw3-D-Li4MwXbESZwkFK77kB3YrqkyO6QMrRVptsgzaa8r2332JY477V0818FaHQJqPRkhImvx0lJMkdMbKrsPanjt7lkGGyyE_k4Ww6PkMinyt49Yz-AsKznj3EAVZHFupu9KyjG7tcs2V20WHYLM1eQXjKXeBSRZgISIIJpVG7GhVzkF_uVQ5gut6yA_z1jUXAotVdcmCNrt4ZTNEkd9f6rv6U8PvAj_7FtKS3xmhaMq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8859995348.mp4?token=YmeMVMA9LQF4HuJ5fuxe8WxW2cix4V0NTYRCCHtXBEPDCTL_Oea8Hkxnjk_8MWaFpLY6OcF_wCWpuMAe0a6DPB6R0XXBx8_gXgJUyBaaw3-D-Li4MwXbESZwkFK77kB3YrqkyO6QMrRVptsgzaa8r2332JY477V0818FaHQJqPRkhImvx0lJMkdMbKrsPanjt7lkGGyyE_k4Ww6PkMinyt49Yz-AsKznj3EAVZHFupu9KyjG7tcs2V20WHYLM1eQXjKXeBSRZgISIIJpVG7GhVzkF_uVQ5gut6yA_z1jUXAotVdcmCNrt4ZTNEkd9f6rv6U8PvAj_7FtKS3xmhaMq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لاجئ عراقي في كندا يشكو من ارتفاع أسعار الوقود والمواد الغذائية، محمّلًا سياسات ترامب مسؤولية ارتفاع تكاليف المعيشة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/naya_foriraq/92029" target="_blank">📅 04:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
🇮🇷
اعلام اجنبي:
‏لم تحرز المحادثات التي توسطت فيها قطر بين الولايات المتحدة وإيران تقدماً يذكر، حيث رفض كلا الجانبين تقديم تنازلات وتزايدت المخاوف من تجدد القتال.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92028" target="_blank">📅 02:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1293457b8.mp4?token=KTy7OxTiHCAKcZ7KSFAyO2sNwvEPuW2OVLhsE3JF7B4ooS0SKF2SIYozelncwmdFlFEz4m0cYvD4Fn94vfGRcijeojk29A_Z9Z5tO11U2qsikOz-JtL_fxOLE072SvbIkER_voKiAz0GJIBZuch4v7PWwRbJL-G2bGsqI-LrqXgJ4AozU4iANvtS3xuuJvApcg4hXKFrKphRz0ZP1lYFB2D1qx6ueJAYDxxVDL4x3NUHGxxTDp5r33f6pxwq-gxBXCcknIyxe74jf-yoqfRx5OkXu7bhscrogHhtcoYXeRlzyDV0BozahbD1ASSsWkCJ53qcLE1VIRtgoBNcolzhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1293457b8.mp4?token=KTy7OxTiHCAKcZ7KSFAyO2sNwvEPuW2OVLhsE3JF7B4ooS0SKF2SIYozelncwmdFlFEz4m0cYvD4Fn94vfGRcijeojk29A_Z9Z5tO11U2qsikOz-JtL_fxOLE072SvbIkER_voKiAz0GJIBZuch4v7PWwRbJL-G2bGsqI-LrqXgJ4AozU4iANvtS3xuuJvApcg4hXKFrKphRz0ZP1lYFB2D1qx6ueJAYDxxVDL4x3NUHGxxTDp5r33f6pxwq-gxBXCcknIyxe74jf-yoqfRx5OkXu7bhscrogHhtcoYXeRlzyDV0BozahbD1ASSsWkCJ53qcLE1VIRtgoBNcolzhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تصعيد خطير في التون كوبري ودخول اشخاص مسلحين من اربيل شمالي العراق قامو بغلق الطريق وسط تفرج القوات الأمنية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/92027" target="_blank">📅 01:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92026">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ازدياد حدة احتجاجات حزب البارتي في محافظة كركوك وسط رشق بالحجارة من قبل المحتجين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92026" target="_blank">📅 01:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92025">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983ce94215.mp4?token=WNiv_OIXurP41d4b_2CnkqGP_kxH7CwwSaqPXXFRbzadzPifEP2N1ndV8rpBzgrdfCrcINrgY00tLJ3bBVjtLMQqg1O7yG4oGxYxHMvxti92GADVmUeecOPWpmwZ1cbObZHpSySnqY_lT3ioF0YGkwq9dZqk8YhYVeLXIq3t18i25zhypkj7GHAyrzmuGKD2UPVEERllrgh6_jhWqBZQeXbuDY0lKKZfddj2Tv_RjHNIleTy1GyKW1Olrji_AMsLupuxCDkM2TEeLu3M-wsOw19UkvjDTnnwoYJCRKWZUeX_NmfR2ClIEjhDMxPRN1i_6olYthZwFyek-LziOsw0PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983ce94215.mp4?token=WNiv_OIXurP41d4b_2CnkqGP_kxH7CwwSaqPXXFRbzadzPifEP2N1ndV8rpBzgrdfCrcINrgY00tLJ3bBVjtLMQqg1O7yG4oGxYxHMvxti92GADVmUeecOPWpmwZ1cbObZHpSySnqY_lT3ioF0YGkwq9dZqk8YhYVeLXIq3t18i25zhypkj7GHAyrzmuGKD2UPVEERllrgh6_jhWqBZQeXbuDY0lKKZfddj2Tv_RjHNIleTy1GyKW1Olrji_AMsLupuxCDkM2TEeLu3M-wsOw19UkvjDTnnwoYJCRKWZUeX_NmfR2ClIEjhDMxPRN1i_6olYthZwFyek-LziOsw0PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار غلق المحتجين للشوارع في محافظة كركوك شمالي العراق وسط تعزيزات عسكرية تتجه نحو المحافظة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92025" target="_blank">📅 00:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇸🇦
الاعلام الرسمي السعودي: تم إبلاغ منتخب عُمان بالتأهل في أرضية الملعب بشكل خاطئ، ‏منتخبا العراق وعمان متعادلين بكل شي وسيتم اللجوء لقرعة لحسم المتأهل.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92024" target="_blank">📅 00:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998af4ba9e.mp4?token=aB4RVE-2L3AR0_TXfu5MazXgO3OjsxVhsPmDyVEceWAW0C8J7-O-RwcTYHtSqTiqSPp0H4j2GqRiZ3Mc2zGjMzN5sQKmWqJrlL6Lk63q4v3znRx4eunSVNFbDQ5sjAEVOXNYDZcmhp7_ov3UwQFlzN9Vgljp3TAtEEOrAgtlK8sU1ZMyrsGyblStMDM0CORJm7m1-5X8VExQL2ic2VO34wwo88kPXZ1vAVJJ0cxmnQxKr_Llq5qtkQCQ1EpsX5Xmn8YsAU_KWK6ubjFgRJQU447MeTrK62vvVTpY_aifdCHXVslnUyh-AXuPcwgOlEu4jTYMYmuzVZ1S_4UQRKh9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998af4ba9e.mp4?token=aB4RVE-2L3AR0_TXfu5MazXgO3OjsxVhsPmDyVEceWAW0C8J7-O-RwcTYHtSqTiqSPp0H4j2GqRiZ3Mc2zGjMzN5sQKmWqJrlL6Lk63q4v3znRx4eunSVNFbDQ5sjAEVOXNYDZcmhp7_ov3UwQFlzN9Vgljp3TAtEEOrAgtlK8sU1ZMyrsGyblStMDM0CORJm7m1-5X8VExQL2ic2VO34wwo88kPXZ1vAVJJ0cxmnQxKr_Llq5qtkQCQ1EpsX5Xmn8YsAU_KWK6ubjFgRJQU447MeTrK62vvVTpY_aifdCHXVslnUyh-AXuPcwgOlEu4jTYMYmuzVZ1S_4UQRKh9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البرزاني يدفع بانصاره في محافظة كركوك لقطع الشوارع وتخريب الممتلكات العامة احتجاجا على استشهاد مدنيين اثنين اثناء عملية التون كوبري على ايدي جهاز مكافحة الارهاب حسب وصفهم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92023" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHcZ-_HrwXajS1CCmK8-LOT-JFy-XlWAVkFUFOLhKZ2RsBc70VlYCHFEdmgwweFiDTeLRWywR55yuCHqMob6I6aynp2Ge_MTdZPUc_EjnZPmT9w5h-KKmVcRbM-SrRxFoa5HXzIuIMoTZjGyTxNta2zfM6EaVVc8CrmszhAJfffnCERWyRaMTqJjf6XYvJwoT8TUzp6luoVyu6QWDQlU8R2KLQ3FWeAvMg9_lw-zHD9m-MRc6yZIEGNgnYPk_2j1MWMqV7ewLaSQ5Y_deBjUexUtSSsLGbs3ksqmTvGJdeWZOTtoMdXiGmGwcxPm7HE1S10GWJRK7yCNXlz23gI3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الشيخ حيدر الغراوي:
إنصاف الحشد وفاء للدماء، وحفظ حقوق مجاهديه مسؤولية دولة، وتشريع قانونه استحقاق لا ينبغي أن يبقى مؤجلاً.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92022" target="_blank">📅 00:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a911c60c57.mp4?token=mYbDNpduiLmFivSsR9W2CkCR2qEiTwRzJBII9cKOyH2yuPXrKrS3VSP53NdllY8IfH6QnG2bULBl1DLaZlXL9Zrscrx-f53mSJUndKWqkLVpt-H-P1vPHbYwBsGmrgM6rS7pZEt58hu2aOqWR_UZyU31T5rP1Eq-lBTRxHFOz-ecVBggfjGvIhx8hyvIJFvO8oVF9jOmkZETeNWRclIAU3YTMcbdGYuYGG8aNz8G2-hD78piR3aqX4fUtIj53EcWDE1zw7jhgervGkLvEtt13kFS67CtNqO193sXsrAjSBb8yRFpNBhSmlTnEoGEogbg7b85inaWsBIb-BBliI72Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a911c60c57.mp4?token=mYbDNpduiLmFivSsR9W2CkCR2qEiTwRzJBII9cKOyH2yuPXrKrS3VSP53NdllY8IfH6QnG2bULBl1DLaZlXL9Zrscrx-f53mSJUndKWqkLVpt-H-P1vPHbYwBsGmrgM6rS7pZEt58hu2aOqWR_UZyU31T5rP1Eq-lBTRxHFOz-ecVBggfjGvIhx8hyvIJFvO8oVF9jOmkZETeNWRclIAU3YTMcbdGYuYGG8aNz8G2-hD78piR3aqX4fUtIj53EcWDE1zw7jhgervGkLvEtt13kFS67CtNqO193sXsrAjSBb8yRFpNBhSmlTnEoGEogbg7b85inaWsBIb-BBliI72Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحزب الديمقراطي الكوردستاني يتهم جهاز مكافحة الإرهاب بقتل مدنيين اثنين في حادثة التون كوبري وتسليم جثمانيهما إلى ذويهما على أنهما من "قتلى داعش".</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92021" target="_blank">📅 23:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇸🇦
الاعلام الاميركي:
تقوم المملكة العربية السعودية بإعادة تموضع بطاريات باتريوت حول الجسور والقواعد العسكرية ومحطات تحلية المياه بعد أن هددت مصادر مرتبطة بالحوثيين بنقل الحرب إلى عمق البنية التحتية السعودية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92020" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679f679452.mp4?token=NA7uI5bYIah0FP5prZkReFAZuS7DQ4UxDLAW9mTfMtgmvD0ZN3iHKXKiaWfbCW3l1h9dfJ0xXOYbdyIFtt0-ku88Sdii9wIIdQVONR-_t2tG9LNgPjX1PgZz_kTxzKR_n1RJNnhTli4QNunWcBzPxGjFfT_K-dkdr_45iyEShCUkzOY2aTa7ugj3C_abpeMgB9qFOf2CYVp4fqs8GomzaJ_0pChoyvi55daKm2bWcBX13Z8I21BYIG1Pz2hxl_S5O4fPJnnwlRJv3R8cB3BWWEfikBChR-5TDJLR82UN0gNlBACTO-BYvvNKjufGcUncF6_zVhCnOFSpdK_EcVpQ6rgunYT8CIUQJ1QeP01NYEBoeVnbCg7Rq1ZwBlI1MF0t4HmROiXktY-FlK0Et3CjANF8yLWzXYPd1hA6JdqWIa0PZtLm_ALJEkphllYNI-9VenRmsm_OgpssNeWKaPGouguFXtx5vrkVCHe8a9Cy3yn1qJ2vyeoBvKE39fCgXAhjU9Hi3MAwopGk834MM8hudJ95fMcPk6G3WRsWoEBeZbs88tbB1CFkwsVw8Mmd-r1F9p3eI_IRoaPHwGdMDkQSRMdCDlIuyNwtRsB1FSz86PWWD1aWVzSr5C1uVKQQzItlao1VYLArAD9farLs5Pevu5iVQikVRnK5m3GSUU8-LIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679f679452.mp4?token=NA7uI5bYIah0FP5prZkReFAZuS7DQ4UxDLAW9mTfMtgmvD0ZN3iHKXKiaWfbCW3l1h9dfJ0xXOYbdyIFtt0-ku88Sdii9wIIdQVONR-_t2tG9LNgPjX1PgZz_kTxzKR_n1RJNnhTli4QNunWcBzPxGjFfT_K-dkdr_45iyEShCUkzOY2aTa7ugj3C_abpeMgB9qFOf2CYVp4fqs8GomzaJ_0pChoyvi55daKm2bWcBX13Z8I21BYIG1Pz2hxl_S5O4fPJnnwlRJv3R8cB3BWWEfikBChR-5TDJLR82UN0gNlBACTO-BYvvNKjufGcUncF6_zVhCnOFSpdK_EcVpQ6rgunYT8CIUQJ1QeP01NYEBoeVnbCg7Rq1ZwBlI1MF0t4HmROiXktY-FlK0Et3CjANF8yLWzXYPd1hA6JdqWIa0PZtLm_ALJEkphllYNI-9VenRmsm_OgpssNeWKaPGouguFXtx5vrkVCHe8a9Cy3yn1qJ2vyeoBvKE39fCgXAhjU9Hi3MAwopGk834MM8hudJ95fMcPk6G3WRsWoEBeZbs88tbB1CFkwsVw8Mmd-r1F9p3eI_IRoaPHwGdMDkQSRMdCDlIuyNwtRsB1FSz86PWWD1aWVzSr5C1uVKQQzItlao1VYLArAD9farLs5Pevu5iVQikVRnK5m3GSUU8-LIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: هل يمكنك إخبارنا المزيد عن الحادث الذي وقع في القاعدة الجوية في المملكة المتحدة؟
ترامب: أنا أشعر بخيبة أمل فقط لأنهم قبضوا على إرهابيين ثم سمحوا لهم بالخروج.
كيف يمكن منح إرهابيين الكفالة؟ لذلك، لا أعرف.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92019" target="_blank">📅 23:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
اعلام الرياضي: قرعة بين العراق وعُمان لحسم المتأهل إلى نصف نهائي كأس الخليج العربي لكرة القدم «خليجي 27»، ستُجرى بعد قليل في فندق إنتركونتننتال بجدة، وذلك عقب فوز عُمان على الكويت 3-1، وخسارة العراق أمام السعودية 0-2.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92018" target="_blank">📅 23:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOUSjvl8akbJSmAE0m2Dns4RRNN1jtDyy8KCynk_piI3V6RV9hSaFfod1YNDGvaCOaGOnsbZSYRO9cVZiHfG9axqubrXMQBJEFNL5jHyBGXu7XvMmkVKo3Rnnc8ZjNejYi5Ip1ODLfzuo-i7tEP-skRikkv_OmCqW_9dXQMB6tsGbbGi2cGCQ4Gcfy1G9_yt4szH0SF2iTbfbkS-CY4B1x4zqqMkjIyKcv5fAQUi-i_VLgy4tvakFB5YIFKmSU7aAklTzstj2T3qhWaALm3pelEu0Nt9IcEyQ7x2La7UjA5kNHw2gbtvFlXL9WbDinty-TpQXGOvLuUE_v0tFZd_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس الوزراء الاسبق السيد عادل عبد المهدي:
نشعر بالخجل بان مكتب مراقبة الاصول الاجنبية". يملي علينا أوامره المذلة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92017" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب
: إيران تمر بأوضاع صعبة للغاية، ولا أعرف ما إذا كانت ستستسلم أم لا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92016" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
العراق يودع بطولة الخليج بعد الخسارة امام السعودية بهدفين نظيفين.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92015" target="_blank">📅 23:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92014" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92013" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
🇸🇦
إنطلاق مباراة منتخبنا الوطني أمام نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92012" target="_blank">📅 22:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية تسجل الهدف الثاني في شباك العراق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92011" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية تسجل الهدف الاول في شباك العراق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92010" target="_blank">📅 22:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي في حركة النجباء الشيخ علي الأسدي: تحاورنا مع الإطار ورفضنا تسمية "حصر السلاح" وثبتنا أن المصطلح مضر وغيرناه إلى "تنظيم السلاح، نأسف لقرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في العراق، قرار السلطة العراقية منع الطائرات الإيرانية…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92009" target="_blank">📅 22:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
🇸🇦
إنطلاق مباراة منتخبنا الوطني أمام نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92008" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في غلاف غزة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92007" target="_blank">📅 22:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في غلاف غزة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92006" target="_blank">📅 22:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي في حركة النجباء الشيخ علي الأسدي:
تحاورنا مع الإطار ورفضنا تسمية "حصر السلاح" وثبتنا أن المصطلح مضر وغيرناه إلى "تنظيم السلاح، نأسف لقرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في العراق، قرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في مطارات العراق انصياع للبلطجة الأميركية، لدينا معلومات عن كل التحركات الأميركية وعن الفرقة التي أنشأوها والتي تضم عراقيين بإشرافهم، لدينا معلومات أين موقع هذه الفرقة وما هي واجباتها في المرحلة المقبلة وكل هذا مرصود، إنشاء هذه الفرقة هو لتنفيذ الاغتيالات والفتنة وهي مثل "بلاك ووتر" بعنوان آخر، البيشمركة يجب أن تكون تحت قيادة القائد العام للقوات المسلحة، علاقتنا مع الرئيس الزيدي جيدة واجتمعنا به عدة مرات بشأن السلاح ونرى أن المشكلة في مستشاريه.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92005" target="_blank">📅 21:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نايا - NAYA
pinned a GIF</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/92004" target="_blank">📅 21:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=TywXejQirQNAIyOxPXE6mhGCcgDRZNbzzsmT-LpdF1hBzWY80YoUyL5k8LrE8F9SsevWFLH20Cyzfg4tN5gQoJGQyQD3Qj5y8F1K_Sva4BLAaufwk3srV3w8Wa1-VpFrqFs58awroRkho5iNXcfXrFcu_NcllAMOv5GtiGGHjWbj634jKAUhsYApuPsvoy3xoXs_JZtj61vH4ftanm1ZEItYDPlhSIP2jL5zVNduPp2WpzRAd1F1QupcMWApibjTfmPRHyO45AM8fE8P5I6ou5ma-K0VA7sbSHUM6KjhNcXD6fZY5HtRSNT9ehO9rvGaq1Jj4Hs_44-i7utHLlNq0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=TywXejQirQNAIyOxPXE6mhGCcgDRZNbzzsmT-LpdF1hBzWY80YoUyL5k8LrE8F9SsevWFLH20Cyzfg4tN5gQoJGQyQD3Qj5y8F1K_Sva4BLAaufwk3srV3w8Wa1-VpFrqFs58awroRkho5iNXcfXrFcu_NcllAMOv5GtiGGHjWbj634jKAUhsYApuPsvoy3xoXs_JZtj61vH4ftanm1ZEItYDPlhSIP2jL5zVNduPp2WpzRAd1F1QupcMWApibjTfmPRHyO45AM8fE8P5I6ou5ma-K0VA7sbSHUM6KjhNcXD6fZY5HtRSNT9ehO9rvGaq1Jj4Hs_44-i7utHLlNq0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وَيَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِينَ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92003" target="_blank">📅 21:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
الكيان الصهيوني يهدد باستهداف قيادات حركة حماس في قطر وتركيا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92002" target="_blank">📅 21:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
تشكيلة منتخبنا الوطنيّ لمواجهة نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92001" target="_blank">📅 21:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
احترمنا رأي فصائل ربطت تسليم السلاح بانسحاب التحالف، وبعض الفصائل ستنضم للحشد الشعبي بأسماء جديدة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92000" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
منذ ساعة، تمّت محاصرة مجموعة من اللصوص المسلحين من قبل قوات الشرطة في مدينة إيرانشهر بمحافظة سيستان وبلوشستان، وأصوات إطلاق النار التي سمعت في المدينة، تعود إلى هذه العملية الأمنية لاعتقالهم.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91999" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▫️
الشرطة البريطانية:
لم يتم العثور على أي أجهزة متفجرة في قاعدة "فيرفورد" الجوية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91998" target="_blank">📅 20:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 35 غارةً جويةً من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف استهدفت الأعيان المدنية من شبكات اتصالات ومدارس وغيرها في محافظات تعز والجوف وعمران وصعدة والحديدة.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1158 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91997" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76dd2e40a0.mp4?token=ZI3142G0LSLympVbfUU9i-vXPKyjeOcNCbX4vvrbkAqVEAn5Y_zBUh4AJhJwgL8hmnp8EVit4gQPxLzO-ymqGJShkTNgo__0ooFkNDxAmnK4lEovLloHilRwl3ZW0er-yrSxobiMrH9YodauVdM3TjZrwbo8tuncZwNsMjh98Pvzg27W03Mr0ZXUhPSHBZT5cK7LCoNWbZStRhJf5-76iC3jF0T6PNYpmi9RYiU7yjBeMXsCXTo5GjaBvxq2avbl-87zIshTeL8Q4gcHG0akMCS3fwcc1lGLY5Su9aAXpkY6tQ-ccBRDrcH7isGyKb1YCPHTE_22eASrbqjJESoGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76dd2e40a0.mp4?token=ZI3142G0LSLympVbfUU9i-vXPKyjeOcNCbX4vvrbkAqVEAn5Y_zBUh4AJhJwgL8hmnp8EVit4gQPxLzO-ymqGJShkTNgo__0ooFkNDxAmnK4lEovLloHilRwl3ZW0er-yrSxobiMrH9YodauVdM3TjZrwbo8tuncZwNsMjh98Pvzg27W03Mr0ZXUhPSHBZT5cK7LCoNWbZStRhJf5-76iC3jF0T6PNYpmi9RYiU7yjBeMXsCXTo5GjaBvxq2avbl-87zIshTeL8Q4gcHG0akMCS3fwcc1lGLY5Su9aAXpkY6tQ-ccBRDrcH7isGyKb1YCPHTE_22eASrbqjJESoGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
إندلاع إشتباكات مسلحة، يرجح أنها بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة ايرانشهر جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91995" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية تعلن عن إطلاق مخزون النفط الاستراتيجي في بيان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91994" target="_blank">📅 20:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91993" target="_blank">📅 20:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91992" target="_blank">📅 19:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFEVUGBD6xyo5sTyhHEhXugU1NWMSN3r5dDhdVom4WaTQ35Fg3Q2qui3FEyEviHzjb1f4EGT8BUJdIzAHH_iZh8Cga17Y5SMpJxVYLJEDOeinbLpz4ylWPOus3aOsUFM_21WYs6xfkY44WX0T1OwFwrz8kCYEQ7XIA7lTXzeQHK-WQIsowfgVFE1x-Peg5qxmju2qEGeNI1yUB9BZaLf6kPNzrU1DytKpso3KopxoLEDZBuHL4LbOdm-XGAihn-5Og569Z8_XkcZkbuJQp2tlRnjHBCgveaxfAFDehwB-e0VG1652OyXbPhnMRVTaOxrDAWUwwSO85U6DxZZFxtXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
‏الملك المغربي يكلف فاطمة الزهراء المنصوري برئاسة الوزراء كأول امرأة تتقلد هذا المنصب.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91991" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBNlIDWJ4D-jKA47ewKDMPl2cTda0fxfKSaLhEx0IM-5ANI6cLhpilJix7vW9c5Jq_E7D--WuOBuJ8QBZZsiMfC4g9--ZSw9bSHyTRfYDfrT-SO9jTPmoW5dMnkstIwDjR_Sg2sPJl-V7dQpK_1e1h9gfFtMkmHDjVZ9umTSc3oktV8DMUcDBHrPAvpesmzYBT-k6TogudB03Z9NQK_ouvF7KkqeVRXmCrTJf42D4zyzIysCQsCSgm8iUYdhnZu2_v9rrEABDTymL_LJ3F5vf9sLuqtcV3Rl86GEixFnHpiECX2uM1GrULTIMd1TFSgaLqzEviFU5HVDbo0p8aUFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تمنع ظهور عماد المسافر في وسائل الإعلام لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91990" target="_blank">📅 19:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
استشهاد طفل مدني من اهالي التون كوبري في محافظة كركوك على ايدي عصابات داعsh الارهابية اثناء الاشتباكات التي دارت عصر اليوم.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91989" target="_blank">📅 19:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية تعلن عن إطلاق مخزون النفط الاستراتيجي في بيان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91988" target="_blank">📅 19:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oODZtXV0fBBOGmtgj-_RxkAG5jlfagst1sw1BI9Q8x_8g0X2Rs8bHsOg2I4xxSmXmwojzyHsViah972h0sMm6gu_AeJz16YZubp9lFbH3HabLvhLG4yRWkgSfWcny6sHLBhwgUxY4X8zqvcJA6ESimeuiGXXYWvpfx_SauLbaEGQFphlw24SIPYwjtPylHtyblT4HKcj09j-SC2NJUTPcUy1OkxDT2yNB4gf9moj6AV5RIGMtAcCSxf8P18oJOL6EfGe9BtQeVCHCuBdwdpr9LIPeBz1GFW_SlP1JjxHHray6WyFV85eLha8Aob8P5ZQJgAuoTuKR-ecaT15-1qC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تشكيلة منتخبنا الوطنيّ لمواجهة نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91987" target="_blank">📅 19:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
🇮🇷
اهالي محافظة نينوى شمالي العراق يستنكرون القرار الذي صدر بخصوص حضر الطيران المدني بين العراق والجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91986" target="_blank">📅 19:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPbWG9OmQlZtQYfnoVMQvbnb9CvRxq6MdAIj3GAjnSafkJE8O652C97jJa6l94EQ66As0vRoe5XfYrS571-6gWA-nnOmC2v0zLOSYqkR-Gy3p4knFbtwv0HWRHd4gA0eMf_9y16X1QUbqtXsSfaNa1iQdC51GgU2crGreC9xWowFFxlBllkqibWCfQ02Hkj7i_UByMbUIiJeNz8HjpDhcvvQd6ga62B0VTfzXDMk6hQTn2FgPpRWic-b_ejqp-8eOt6NpFbRnVonoAH5IovPvLlLhijHjTixJNp9Lkwoq_NhBFVARQipNuIC52lVL7XvNIFbnuzpwh2-Nj_P7tSzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnNozxSqtXMjJA6aet6YaXCXoP_WarJ_DyXGLpru8T86Cx4t28HcqP1MiMlYQw_dgoSXWLp2LpeIRNRrwTzhkDHwtewGD-7WO_1hbowRv9B6gXpyAU5C7dmaWNFIrgvdGH1c8I__uVXcY_GmYh0Vd-2qHjUlTAq3Whrbji0AA9bkFjSeRDY_5shhZSKRipAvrM01cI5kHcx-lK4xXUuoTEVLjKF4d35vGQmEkrduHJyvY6EnS3IezqsOPEyTDUzGzLDkJlJGAx0RqDvvOj14cWLYKfnvxV_pSG9MWb4fQ6wvOy-BjnAEV1yDBOY1CSe3f1ka_xYzKiyKGZJ6EXRooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoT4C_gzr_0v2QvYDvV2JUkzRuJjfr7PWNtDgBPDNCRgIntFhxi6K2RB5JrNdk3DoNC2j4H74EwCPRilAfxezfwzwcNY8XKsp4VvwSmQzNgc1W_lIXZFX8xHX4hNSAvrUnbd814pZiC94BNs69uPWrTfybuc3tMwALdCib81-fRyxWjZ3OSj3NnnRCvfbntpUNUKaktl1nUUmMMnKM5LDMdc1b_WwmGRZqfGLo4ymP8p0XDxYKq_x2QKZyFj6pN6C18UYrh6hp1g1Y4lWXwjA0_QR9YZ2_X7v-piOv_uFC-zomt22efYuKObIyjy5el-OFwOuqhXF62J553r7Q__hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
قطعات الحشد الشعبي تبدأ بالاحتفال بيوم السيادة الوطني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91983" target="_blank">📅 19:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
لا يوجد أي عنصر من التحالف الدولي اليوم على الأراضي العراقية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91982" target="_blank">📅 18:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af18a9ad1b.mp4?token=eh6tZBiuefr9C5YnUVNBFfVaD_RzPZhQhDAL0YMxdPn_jGatScsqkYpSKQrVcocaMfaG5vQclf8tq82rVHH6W7lTqiWz-3sqjfITPa0Rp7DQGBq17Vb0600ePPII8WtRtLONp6PAOoCFFa4hp5ubWYZeMM13vYq5UBD8DCI6lOjlAJJdkrGq3XeBT64nlyxyqBytwhwpJOOADSQUb5IfPcLuIl0n2V9M_9-gLFElK1oDovJDXAky8p0bZaDPX5i7cKBaJTLsJUSf43bOWOkmH3MZ1tKRyzCxvxuVxtBwN20zNamfHNmwv5XZkZ597h-FyZKZk2BvYmSmK6dNoSevgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af18a9ad1b.mp4?token=eh6tZBiuefr9C5YnUVNBFfVaD_RzPZhQhDAL0YMxdPn_jGatScsqkYpSKQrVcocaMfaG5vQclf8tq82rVHH6W7lTqiWz-3sqjfITPa0Rp7DQGBq17Vb0600ePPII8WtRtLONp6PAOoCFFa4hp5ubWYZeMM13vYq5UBD8DCI6lOjlAJJdkrGq3XeBT64nlyxyqBytwhwpJOOADSQUb5IfPcLuIl0n2V9M_9-gLFElK1oDovJDXAky8p0bZaDPX5i7cKBaJTLsJUSf43bOWOkmH3MZ1tKRyzCxvxuVxtBwN20zNamfHNmwv5XZkZ597h-FyZKZk2BvYmSmK6dNoSevgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهدت محافظة ميسان، اليوم، وقفة احتجاجية واسعة نظمها أهالي ووجهاء العشائر، استنكاراً للقرار الحكومي القاضي بتعليق الرحلات الجوية بين العراق والجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91981" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
‏
فانس
: الأدلة المتاحة تشير إلى أن سيد مجتبى خامنئي على قيد الحياة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91980" target="_blank">📅 18:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇨🇳
🔻
الصين تتعهد بالرد إذا ما اتخذت الاتحاد الأوروبي إجراءات تمييزية بخصوص قيود اوروبية على البضائع الصينية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91979" target="_blank">📅 18:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇶🇦
شركة قطر للبترول تبدأ مفاوضات لدخول قطاع النفط والغاز في فنزويلا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91978" target="_blank">📅 18:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbSl_nWbgri8O8drlb58MzVGweVL85irAuo_5iA4aVK8rLfjZYDPVtPPN4cDEwzeGTA1QkXdb5-BJkw4nru-nF18y_dFqNzyjylBlr2UjNZUc-LshfTf_WWNVvoXSbYvy5f7T2qpT-Bse_FduQyjK9vDyxVyV8MWhjYM7SjqhY3diwIHHoHLfwjbgNF-M2Y3Tnct-HAgYlyxzWHVpkPfzqb7J4s6ky_7VpL09fEMU1aK2-IERPWKvjhzOqNotQfF6ZFmcRGVOt1v-BWHtf39XrfLj8dLAQlFm-LbvomfumgFNJXamiKZtf6KGl0tSNyW5nvJc6q_9jaWxIccGuvvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
جيش العدو الامريكي يبدأ باعادة طائرات التزود بالوقود ووضعها في مطارات بن غوريون ومطار رامون</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91977" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇱
اعلام العدو:
نتن ياهو سيعقد بعد قليل اجتماع أمني في مكتبه مع كبار المسؤولين في المنظومة الأمنية ودعى زعيم المعارضة لابيد الليلة من اجل احاطة امنية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91976" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
الكيان الصهيوني يهدد باستهداف قيادات حركة حماس في قطر وتركيا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91975" target="_blank">📅 18:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c46a987c.mp4?token=jkDcsLpK39LvCC-1yUXYtsmjiCthuMoHfpRJ2O9a389y3kmOfp5WR_UeIxKq2zWTYXa2lHRqpxXwo2YHShrKs5ETKrIMUp2aPULhoIjFlVuzG5tK6B9kYfNd-2mmKoWUJEDVAEbP3G1PSaRKpsxhLgVSxWnh9Q3CxBA4jPnIHiWCMOXm9PwxF4SOpIf7tTs9Ji-0612QbfJfrJKE5DNvsyVFZ7WW0_VSnQm9a-GhZw2jbYuwdcigHyr0-5nFOY01-10QvoY4HTwODXOi2CBpZUT6oKr8Mlh7MsM3kd_T-T54oMHZ26HCxAgjxG-TdXDnqQz8ssBsExaY1-f6uTuzjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c46a987c.mp4?token=jkDcsLpK39LvCC-1yUXYtsmjiCthuMoHfpRJ2O9a389y3kmOfp5WR_UeIxKq2zWTYXa2lHRqpxXwo2YHShrKs5ETKrIMUp2aPULhoIjFlVuzG5tK6B9kYfNd-2mmKoWUJEDVAEbP3G1PSaRKpsxhLgVSxWnh9Q3CxBA4jPnIHiWCMOXm9PwxF4SOpIf7tTs9Ji-0612QbfJfrJKE5DNvsyVFZ7WW0_VSnQm9a-GhZw2jbYuwdcigHyr0-5nFOY01-10QvoY4HTwODXOi2CBpZUT6oKr8Mlh7MsM3kd_T-T54oMHZ26HCxAgjxG-TdXDnqQz8ssBsExaY1-f6uTuzjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جماهير محافظة البصرة جنوبي العراق يرفضون الحصار الذي يشارك فيه العراق ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91974" target="_blank">📅 17:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91973" target="_blank">📅 17:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91972" target="_blank">📅 17:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
العراق ينفذ حكم الإعدام بحق 10 مدانين بجرائم إرهاب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91971" target="_blank">📅 17:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مصرع عدة عناصر تابعين لجيش النظام السعودي على يد انصار الله</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91970" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AW-dKDdAq78cLZcvsipcDDZyRi-kT9cfyYGQ37lXhGIQCnwLMSsyy-5AcBW4IrMwshLXOa0ZrFc5gNxhE6iL1VXFYGPSs8RrxIDuWOW3w37kcHH_EWCJDq_JFTqpSCgYmi84bj3fj7VC7QkUSnPWbbPIJvUXEcax8ZKpRofY7keuD7lq_sMlIH_B2GLcc2VjDmDz1eX81tKHZlFoaYp7k_dX2N18TqzTdR8GFWI3XTQMmCSAkJn6T18Sei0zmWDed6YaN85wY9SnA_HzJweaH0cABdbvejq-kkMXxNsms37LuAm1-hQcfNqsL3ctFNVUpeFfaD9sa7SOQQVlreN23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leAtTk6X3XfqEKmOyCkIQMTIo2Oj3Y_tzQzzOehyuABFF1ra2Glfd6JaBspiEKhDUTWhzYbN4QDcBsOEPhDQ9bRe66swsloK6eW5-3pZwf4M6erqrIAqFErQOn5GPGcI_3caR5nP4BSckXAdU9TCfskO-4M-d6Z2sSmPZRDFo8KhSwhG6p3Jq-qBI95fTNFR-hrdg4xK1oUMTruXEa2CbKC2vpIYXflh1U5jaIupFX2WWwu00hrOUfJ9UDTdG3mcqtpLeN7NidFGruRdFhqBIE42HCSYcBW5JIaVD7HalIfCEEJVIcrC8F3KZvHBd7cfr2PYYhl3XW8pbKCsYu6iGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصرع عدة عناصر تابعين لجيش النظام السعودي على يد انصار الله</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91968" target="_blank">📅 17:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ce5ba33d.mp4?token=vICHvwIEFBGjfcxpSO8V9jaj8GkX36fhhOpESNzYTW4_9D_JQ6X6CjwWgjWlZZ1oVHuTZtG6O6bEl9hxC1W2uHgvLeDwhWtO47np4-XFq-hfSoQEqMe_Q-3AXGlA09X3QIPP_Mo1ZCP0DK5oUsioqCWoXt487KVTk6dKcJ1Afn8T-PSCN0pQun4LambL-d39rb136Gtfu-tcYHgDLZXiRxYgQSgw5XeoGuHo7n88zt5-AW7czwQPUtwnna2ukMcnt9FUG2KBxhJrN512lBaZTvKGjXmYt7Vpc1StiH3Mq5EpJl_MWA3mMJmCIum3bBdLyGELY5-JEHUpRGRerc29G4qAEL9rrD6mEggdz-_enwaVBQ3Bm_Ykw-9HqO7Fbu79fKlXsm4EOAdVLyujynuqxjrb9o1EFAridgiHHiw_-kMWK9z0zvVKWJsTW4nEB75t5psjBgtwLUX4VWjXNaymPsZctkYwDKEP3Qft6GDxj8jug72jem7-kMbC15d0tGlTJMzzlimseAvOdsUe083vDXLswEPungpYqZLlSoucx-nsOsNgihWgr8r8eOY9JY7-HaxshC0XQkocKJdKm1DSiUNE3HTlFeHeWic17g4iQYx-w9g0YOtZeYK-e18zkaKSLvfNLUmjhmtpbtGOg7QtaVDiZAv18WV1eEUb6kJcjsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ce5ba33d.mp4?token=vICHvwIEFBGjfcxpSO8V9jaj8GkX36fhhOpESNzYTW4_9D_JQ6X6CjwWgjWlZZ1oVHuTZtG6O6bEl9hxC1W2uHgvLeDwhWtO47np4-XFq-hfSoQEqMe_Q-3AXGlA09X3QIPP_Mo1ZCP0DK5oUsioqCWoXt487KVTk6dKcJ1Afn8T-PSCN0pQun4LambL-d39rb136Gtfu-tcYHgDLZXiRxYgQSgw5XeoGuHo7n88zt5-AW7czwQPUtwnna2ukMcnt9FUG2KBxhJrN512lBaZTvKGjXmYt7Vpc1StiH3Mq5EpJl_MWA3mMJmCIum3bBdLyGELY5-JEHUpRGRerc29G4qAEL9rrD6mEggdz-_enwaVBQ3Bm_Ykw-9HqO7Fbu79fKlXsm4EOAdVLyujynuqxjrb9o1EFAridgiHHiw_-kMWK9z0zvVKWJsTW4nEB75t5psjBgtwLUX4VWjXNaymPsZctkYwDKEP3Qft6GDxj8jug72jem7-kMbC15d0tGlTJMzzlimseAvOdsUe083vDXLswEPungpYqZLlSoucx-nsOsNgihWgr8r8eOY9JY7-HaxshC0XQkocKJdKm1DSiUNE3HTlFeHeWic17g4iQYx-w9g0YOtZeYK-e18zkaKSLvfNLUmjhmtpbtGOg7QtaVDiZAv18WV1eEUb6kJcjsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جماهير محافظة البصرة جنوبي العراق يرفضون الحصار الذي يشارك فيه العراق ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91967" target="_blank">📅 17:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
🇺🇸
بعد الترخيص الامريكي لمدة شهر مع الزامها بارسال بيانات الملابس الداخلية للمسافرين الى واشنطن.. الخطوط الجوية العراقية: تهيئة المتطلبات المتعلقة بتنظيم الرحلات تمهيداً لإطلاقها من وإلى إيران خلال شهر تشرين الأول المقبل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91966" target="_blank">📅 15:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
في مخالفة قانونية..
مجلس محافظة واسط العراقية يصوت على استحداث محافظة الصويرة.
محافظة تستحدث محافظة!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91965" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏قامت السلطات التركية باحتجاز طائرة ركاب ايرانية بسبب مزاعم ديون غير مسددة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91963" target="_blank">📅 14:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:  السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران  ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91962" target="_blank">📅 14:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:  السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران  ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91961" target="_blank">📅 14:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:
السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران
ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع احتفاظ الولايات المتحدة بحق إلغائه أو تعديله في أي وقت
الرحلات المسموح بها يجب ان تغادر من مطار النجف الدولي فقط وأن تعود إليه، وأن تقتصر على نقل ركاب إيرانيين لأغراض الزيارة الدينية
يحظر نقل الأموال النقدية بالجملة، والشحنات المخصصة للاستخبارات أو الجيش أو أجهزة إنفاذ القانون الإيرانية، وأي أشخاص محظورين، بما في ذلك الأشخاص التابعون للحكومة الإيرانية، أو الأشخاص التابعون لجماعات الميليشيات المتحالفة مع إيران
ما يمكن نقله من البضائع يقتصر على الأمتعة الشخصية والأشياء اللازمة لسلامة الطيران، ومنع تصدير أو إعادة تصدير البضائع أو التكنولوجيا أو البرمجيات إلى إيران، باستثناء ما تسمح به الأحكام المحددة في الترخيص
للولايات المتحدة صلاحية إلغاء أو تعديل الترخيص في حال عدم وفاء جمهورية العراق بالتزامها بتقييد الرحلات الجوية الإيرانية من دخول المجال الجوي العراقي أو عبوره
الزام الخطوط الجوية العراقية بالاحتفاظ بسجلات المعاملات المشمولة به لمدة 10 سنوات وتقديم تقرير إلى الولايات المتحدة خلال 10 أيام عمل من انتهاء الترخيص ويجب أن يتضمن التقرير إجمالي عدد الركاب الذين نقلتهم الرحلات المصرح بها وأسماء الركاب وأرقام جوازات سفرهم، إضافة إلى الأموال التي أنفقتها الخطوط العراقية في إيران على الوقود والصيانة والخدمات الأخرى المرتبطة بالمطارات</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91960" target="_blank">📅 14:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز الجنوب السعودي</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91959" target="_blank">📅 14:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhthFEUxNz74JcbfFThnBmZrgZh6MsqQcaRcv-nVVyIUaJPF4-RHxRyUDeUGS7FfyN3pSLLyOLgS7KVUp3XB8riHjBpSmRGMIkRUevMi15c5Jdqq3ZIizfWJTnlUla6rXnVvllmHrXGuAB5uWXnBUGwL935x1sLLspomeO4MRKqYjgExoVF8TcdpoDA7XpNCBK8orKoQvVTuPIfLqXNwCKsj4NyjUgiOXRV519OpAww2FyPp57mtMyYfACHmL0cLbO3vryoac3_-Y2pfCsdKWWyKinoZ2BA6jqsODpQtE2Dtkv4vc_2Yx7GH-Llmnz2k7Ti7lNj8uSdmuwu62XejdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91957" target="_blank">📅 14:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91956" target="_blank">📅 14:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
🔻
رسالة من حرس الثورة الاسلامية إلى الشعب الأمريكي
:
افصلوا أنفسكم عن المحتلين لفلسطين، الذين سيضطرون عاجلاً أم آجلاً إلى مغادرتها والعودة إلى بلدانهم! يمكننا أن نتعايش معاً بسلام.
تخلّصوا من الحكومة المارقة، قاتلة الأطفال، الشهوانية وعديمة العقل، وأسندوا إدارة شؤونكم إلى المفكرين بدلاً من الأوباش، وذكّروهم بأن العالم قد تغيّر.
لقد استيقظت شعوب العالم، وانتهى عصر نهب ثروات الشعوب بقوة الحراب؛ فهذا القرن هو قرن انتصار إرادة الشعوب. إن مواصلة هذا النهج اللاإنساني ستحدد مصيراً مؤلماً لأمريكا؛ لأن يوم المظلوم في مواجهة الظالم سيكون أشد بكثير من يوم الظالم في مواجهة المظلوم.
قبل 7 أشهر، بدأ الجيش الأمريكي المعتدي حرباً ضد إيران، عبر انتهاك القوانين الدولية وارتكاب جريمة حرب، وذلك من خلال مهاجمة مدرسة ميناب الابتدائية وقتل 168 طفلاً من التلاميذ، وبالتزامن مع مهاجمة مكتب عمل الإمام السيد علي خامنئي، قائد الثورة الإسلامية، واستشهاده مع أفراد عائلته، بمن فيهم حفيده البالغ من العمر 14 شهراً
وقد أسفرت هذه الحرب، حتى الآن، عن استشهاد أكثر من 3600 شخص، معظمهم من المدنيين، بينهم 400 طفل، كما تعرضت 8 جامعات و3 مستشفيات و8 مدارس للقصف.
إذا ساوركم الشك في صدقنا، فيمكنكم القيام برحلة قصيرة إلى أي مكان تختارونه في إيران، حتى إلى مضيق هرمز، والتحقق بأنفسكم من صحة تصريحاتنا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91955" target="_blank">📅 13:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🇶🇦
المتحدث باسم الجيش الإيراني:
الحكومة القطرية لا تزال تعلن أنها غير مطلعة على وضع الطيارين الإيرانيين الثلاثة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91954" target="_blank">📅 13:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
إنفجار لغم في بادية محافظة المثنى جنوبي العراق؛ إرتقاء شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91953" target="_blank">📅 12:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
🇷🇺
‏
الناتو:
روسيا تواصل حملتها العدائية ضد أعضاء الحلف.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91952" target="_blank">📅 12:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A25sbkDaQUovrtxpqxz-_SvVPBJAJq8ejUoLo6ctup_Gvqfg_WzrhADY5lMBM4GWwapJ0fh4pEmt-Oke8sMhv_7d7yMcJY5Lzd-Jwfq0RU8FQx7cPX4ncSBqALqibrNFufYP7LuOAPbzdDam0BhKf-89bkKfj8CosQrWV4Coqi-m6XBFu_1YHaNms79ap3zXw8ZvGUrik0CrdQvdLWWumWZ4DYq2M5_s43gfGcFmWeDP8OnKqxuQBjNG7zcWhBcMDea-o1MXX0-lmNvj07H5hnIvq855dvhsLkc-QmwMJlzfDCe4tBiyihvqkhsiwse5ZYLuO3vhGJzo2zk_ueGJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سلطة الطيران تفرض شروط تعجيزية على المواطنين الراغبين في السفر إلى تونس عبر الطيران العراقي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91951" target="_blank">📅 12:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي يستهدف شبكة الإتصالات في محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91950" target="_blank">📅 12:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=DZt9nK2NnlIaCVcWInCyfO4py59qmz8WKSSzQua4hgrN63ct0UxpRfRzcW1vSTnhrhsnmHs2AYXuTrWirla2opr7sPyJ-hWyvO_hcwWiOaA4myvZ20raDsRy03VflYsHOTCF_m6GFQtvOJbttiv8j-uvkK7yk7W8vofPy8YtfntDGKu0dwe9_m1wuqArzxL1zU1htt0FGnFro3nv7gBrtck900x0npTD8dwLCpJ6sCfUSfGJOqhpJ97v_8NadulgSQEvET9zYNe8vUkZeG27lBUBT45-B-vo0OnbAmzTSy9tZE6exF1r2dzhLLGXClbvHgtTfYqcN0_jDrUmi_dqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=DZt9nK2NnlIaCVcWInCyfO4py59qmz8WKSSzQua4hgrN63ct0UxpRfRzcW1vSTnhrhsnmHs2AYXuTrWirla2opr7sPyJ-hWyvO_hcwWiOaA4myvZ20raDsRy03VflYsHOTCF_m6GFQtvOJbttiv8j-uvkK7yk7W8vofPy8YtfntDGKu0dwe9_m1wuqArzxL1zU1htt0FGnFro3nv7gBrtck900x0npTD8dwLCpJ6sCfUSfGJOqhpJ97v_8NadulgSQEvET9zYNe8vUkZeG27lBUBT45-B-vo0OnbAmzTSy9tZE6exF1r2dzhLLGXClbvHgtTfYqcN0_jDrUmi_dqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أعمدة الدخان المتصاعدة في سماء العاصمة الإيرانية طهران ناتجة عن حريق طال أحد المباني ولاوجود لحدث أمني.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91949" target="_blank">📅 11:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBqPXmKiYgHXvvHI6CdqSIAV_F7qLkvTcmHiRwc2Fxi6kPXeCagiGezDBf6zDUoKP4_gIg42Xi_yQVpovfcOSxYqC4SfSkzEPsm1EtsekE7nUz-JntFIv8JEcX8iE8w1MFfxL8nintckTzZ8qs2x5hgxJwtv1X_Yb7ZTgKPPdhMzt9jEXxEK6wmmFvcnjt_UcbAUlVJIBegYZhgXGHiHFIARin8oBQmKb0yDW5ncjpOUVv6Ov6J6yKeCo3eVPqNvylOLhPILl0jliITm05apqQm9z8fS9SgNwnrVDG3o8zXgEGwoSmQifLpWI4l1jeBNYprLVqO7ztOaRARNpVnMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏توقف العمليات الجوية في مطار أبها الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91948" target="_blank">📅 11:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
المتحدث باسم الحكومة الإيرانية:
نشكر الشعب العراقي الذي يسعى إلى إلغاء قرار الحظر الجوي الاستبدادي على إيران.
منع الرحلات الجوية من وإلى إيران هو تجسيد للغطرسة الأمريكية.
نحن نؤمن أساسًا بأنه يجب حل القضايا دبلوماسيًا قدر الإمكان. لذلك، تجري مفاوضاتنا، ونعتقد أنه يجب حل القضايا المحلية والإقليمية داخل المنطقة نفسها.
قمنا برفع شكوى إلى المنظمات الدولية المعنية لرفع الحظر الجوي عن إيران ونتابع هذا الملف عبر المحادثات.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91947" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
أ.ف.ب:
قاليباف يتوعد باستهداف البنى التحتية في الشرق الأوسط إذا لم يُضمن أمن إيران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91946" target="_blank">📅 10:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي يستهدف شبكة الإتصالات في محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91945" target="_blank">📅 09:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله اكبر
🇺🇸
اصابة اكثر من ثمانية جنود من المارينز في مضيق هرمز اثر تعرض سفينة لهم بصاروخ كروز بحري اطلق من قبل بحرية الحرس الثوري التي اعلن ترامب انها دمرت.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91944" target="_blank">📅 06:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
اختراق قاعدة بيانات ضخمة وشاملة لموظفي البنتاغون تحوي معلومات حساسة طال 2.76 مليون شخص على قيد الحياة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91943" target="_blank">📅 05:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91942" target="_blank">📅 05:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMypWbuJEo9uY0gn4hZytfKQE0kQFDCaFy6b-VtlrCq_M5gE2ZUj-oXxY3LUF1ejQWka4tBrFo1WnUOuy9FMK7GejQ93dqacSm5LNg9wFHRdEyMW-G1CQE43-uK56_AjlIaZO8GoBJN8BOPjKRZm14vd7YHTQLnCmDgDL-yeVDKShzXIy29aYTrxHYKRdYkl7rsBlGGGGCsR_rQqNlXPZf0kGfWX51AUnk3F5zJQhRQ4QOXg4tpTPpdpOWMO0EBfJNvbMnGm9XHgafLRtPUY6F6wG-DD1so6f1LATEDf8gdAUzwZ4hKa7EtR-njjJaVLjZicC6xp5wdRqBl_ASk_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
مراسلنا من مطار الملك خالد في الرياض يؤكد تأجيل جميع رحلات الإقلاع والهبوط فيما لم تُفعّل صفارات الإنذار لتجنّب توثيق عمليات السقوط.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91941" target="_blank">📅 05:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روبيو: لو امتلكت إيران سلاحاً نووياً يمكنها به تهديد جيرانها والعالم، فلن يتمكن أحد من فعل أي شيء حيال المضائق؛ إذ سيكون بوسعها السيطرة عليها، وفرض رسوم عبور، وتحديد من يحصل على الطاقة ومن لا يحصل عليها</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91940" target="_blank">📅 04:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d8a438ff.mp4?token=fgoMyzJIxN0nqjLMTBuKusKwsv60ARgAAvn1modp1cf0iNG6s8ux9zcUQ3aVDLG2enUwsuitkod2wELL320kqSm4lZDE5RzHU1r2zPZOMm9FUO26urDRZ9McxNwjZ3Gv5nxzTHEJWbMhpO5esa48pM6nsmfBs7vJJtGqjZHz8uu2e2gDkBEZu_lkuGMUxqpMOLnWp2mlqQFEcKImF6G5TBSxvaksnZQb65n7xWktr3ajIlhAfP3S09hc3-xL-csMgOY8Xo32etoS74-m8m1Zrn50aDqzLKnI9GJX8vQRCog8SOOj0Xg90FxDm6XF7upzvxFrD22fWODZ20Z0aZsaHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d8a438ff.mp4?token=fgoMyzJIxN0nqjLMTBuKusKwsv60ARgAAvn1modp1cf0iNG6s8ux9zcUQ3aVDLG2enUwsuitkod2wELL320kqSm4lZDE5RzHU1r2zPZOMm9FUO26urDRZ9McxNwjZ3Gv5nxzTHEJWbMhpO5esa48pM6nsmfBs7vJJtGqjZHz8uu2e2gDkBEZu_lkuGMUxqpMOLnWp2mlqQFEcKImF6G5TBSxvaksnZQb65n7xWktr3ajIlhAfP3S09hc3-xL-csMgOY8Xo32etoS74-m8m1Zrn50aDqzLKnI9GJX8vQRCog8SOOj0Xg90FxDm6XF7upzvxFrD22fWODZ20Z0aZsaHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
روبيو: ستكون هناك تداعيات إذا تعرضت المصالح الأمريكية لأي هجوم، وإيران كانت تسعى لامتلاك أعداد ضخمة من المسيرات والصواريخ والأسلحة التقليدية،وكنا على وشك أن نرى كوريا شمالية في الشرق الأوسط والرئيس ترمب منع حدوث ذلك.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91939" target="_blank">📅 04:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70770abcc.mp4?token=QXNymeZoICOoUICjYMRba3_njaAUX-zEqWA4L-FOZ4J8yD42HePbw0jNdYWuajIvfTdtWi_TE9hFudUnGaK70Gx6iQFnpOBq1A7GMBrro6XFfuFgGtE9X4ZDJsTJef6jkME7BY-DLoAGoYUBt25TJwyS0mhOre3jeZ-xRptnBX2K6t5g3x36AhZq0NBpX_hm9fIp_vzzQjMBDHD72A87C3cDmuDdGDTTdRkqTcO0twNihXGIvbk_LQrse9wAt6jyyLaIPHq02t_sp1pSb-2lajjVcnxqCDNWRoFWHEu0gHpFF7htYotNZcDwgkLiLgKEkF6H4PiTaEwTXnNZOviXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70770abcc.mp4?token=QXNymeZoICOoUICjYMRba3_njaAUX-zEqWA4L-FOZ4J8yD42HePbw0jNdYWuajIvfTdtWi_TE9hFudUnGaK70Gx6iQFnpOBq1A7GMBrro6XFfuFgGtE9X4ZDJsTJef6jkME7BY-DLoAGoYUBt25TJwyS0mhOre3jeZ-xRptnBX2K6t5g3x36AhZq0NBpX_hm9fIp_vzzQjMBDHD72A87C3cDmuDdGDTTdRkqTcO0twNihXGIvbk_LQrse9wAt6jyyLaIPHq02t_sp1pSb-2lajjVcnxqCDNWRoFWHEu0gHpFF7htYotNZcDwgkLiLgKEkF6H4PiTaEwTXnNZOviXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
روبيو
: ستكون هناك تداعيات إذا تعرضت المصالح الأمريكية لأي هجوم، وإيران كانت تسعى لامتلاك أعداد ضخمة من المسيرات والصواريخ والأسلحة التقليدية،وكنا على وشك أن نرى كوريا شمالية في الشرق الأوسط والرئيس ترمب منع حدوث ذلك.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91938" target="_blank">📅 04:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=rQVpWFvUn-OcUsLNDZd8yZmHenyDXd4X0sbsLW-VyRz__cjEtd_1sX66bzlXkY_PanwrbAqretUdYA_MlPSfiT8N42RxBzkluaDikyyzdUhN4hTSj1-oFT6EoAj5tVnQA4nHDiNAxJ43pH7YM09WCJt7MtiPCYQnv94i-DIr_Vn7JXP_-g_akEZ3B3D7B-NW3l1o-zZY6zzHugiBmLcABjkeOhuZgyMo7E0R9NsclBZ6Y6NMLCCt-WLAGaaPC522CbyHJBRvS2P2IAJNXC6kmcrNs70XKJx5t1cdvpqwJTLxPxWCV_taxIWwBMjJmGKrCXE46yivUZreYsD06RVFJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=rQVpWFvUn-OcUsLNDZd8yZmHenyDXd4X0sbsLW-VyRz__cjEtd_1sX66bzlXkY_PanwrbAqretUdYA_MlPSfiT8N42RxBzkluaDikyyzdUhN4hTSj1-oFT6EoAj5tVnQA4nHDiNAxJ43pH7YM09WCJt7MtiPCYQnv94i-DIr_Vn7JXP_-g_akEZ3B3D7B-NW3l1o-zZY6zzHugiBmLcABjkeOhuZgyMo7E0R9NsclBZ6Y6NMLCCt-WLAGaaPC522CbyHJBRvS2P2IAJNXC6kmcrNs70XKJx5t1cdvpqwJTLxPxWCV_taxIWwBMjJmGKrCXE46yivUZreYsD06RVFJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مراسلنا من مطار الملك خالد في الرياض يؤكد تأجيل جميع رحلات الإقلاع والهبوط فيما لم تُفعّل صفارات الإنذار لتجنّب توثيق عمليات السقوط.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91937" target="_blank">📅 04:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d7be32d1.mp4?token=EEqKqzMLjJtErLyWQfXefCi2LeGiTPabHvC28_3gjGfhrtnkodDazxeqcN6D2Aayron-CmUaBwHw5a3h5vR-QuiNkZY_dZ5BMAQS0GbEuEXLL5VGjgMku1FGjZKG1zcI-TqeVEXTLY3B_xdqyOrTtbINdOt5ibjjtpT46SfTo9-3NoOYeGBz3-g8UEz_H5rTWFMUFJbqkStKCXp_qkYB6vQhYh120AqM2I7rlTilk2DP1J2fw86xe4zLuRmLEHi33OutInme8sJmkS-YYXcX4pk3HIGhZj1jJ4E8hLkumuw0rEMBXWDFXFFuvSEgpuj_g3XJPPh1LZCdsmzHsALJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d7be32d1.mp4?token=EEqKqzMLjJtErLyWQfXefCi2LeGiTPabHvC28_3gjGfhrtnkodDazxeqcN6D2Aayron-CmUaBwHw5a3h5vR-QuiNkZY_dZ5BMAQS0GbEuEXLL5VGjgMku1FGjZKG1zcI-TqeVEXTLY3B_xdqyOrTtbINdOt5ibjjtpT46SfTo9-3NoOYeGBz3-g8UEz_H5rTWFMUFJbqkStKCXp_qkYB6vQhYh120AqM2I7rlTilk2DP1J2fw86xe4zLuRmLEHi33OutInme8sJmkS-YYXcX4pk3HIGhZj1jJ4E8hLkumuw0rEMBXWDFXFFuvSEgpuj_g3XJPPh1LZCdsmzHsALJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91936" target="_blank">📅 04:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91935" target="_blank">📅 04:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91934" target="_blank">📅 04:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91933" target="_blank">📅 04:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91932" target="_blank">📅 04:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9YEp6R4lfMOAavVFCalRVv6WkpKO1iCssIZToDBUaF2yBVyI6tdFW0AR6ebIslp46_hYYn-TfeBkVDvDQ8WjQx_eMeF3w8esskKDQWbxJD2q2Ic0MaGCaCWI56Rz5lLbdTEWiBMwGNZmts_faGAYJsy0V3nUZoggHnwbdUQdGxCwEHfbo73uL89ZvwaewpYWSaB9CMLbbxnwm14HEyrBLoksHa3mBrwWBsEWYq2LxN8npyyAOc_gauRq-kYizI7SuHKoGLnLRF8CVs6WHeLP0RW3TYjDzAksCyiIyCEygGCh1ChlXYiHRa2jhar3fYrOpIchQO3i9EfY3iMQZ6xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91931" target="_blank">📅 04:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية تسلل مقاوميين.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91930" target="_blank">📅 04:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a57a9c44b.mp4?token=FX07fDEjm35mB9_xUiJ2Xi5totyUUm1mMS5fYPxJ6WNUjTDXj093z5K0NjqpIobxR_X7Gc9YmA5E_VnuKLtTIsyUR4teaqW8wVMq3c-Rpe3vYjDTGZ0m3irlH7jX_PVjAE_ulWjyqdiy0oIQWLoNVVOhCp_t2RAmOAzpYU0nhE09xU-6Imd8yPma0ePU5DfS-_pYzoQN_IS5mIIPQt9kerC2I5ylPeGj6L3-gB-BiJHEMGJ-tQgg0cQZrAjeKws_q1E6h8CDpPmOxShswnkuBl2UhghTPIpIyV5yVwQAhap8PMFfOfPulQbEqRfm2Hb200hHPnEpDCvha2dhmO9soQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a57a9c44b.mp4?token=FX07fDEjm35mB9_xUiJ2Xi5totyUUm1mMS5fYPxJ6WNUjTDXj093z5K0NjqpIobxR_X7Gc9YmA5E_VnuKLtTIsyUR4teaqW8wVMq3c-Rpe3vYjDTGZ0m3irlH7jX_PVjAE_ulWjyqdiy0oIQWLoNVVOhCp_t2RAmOAzpYU0nhE09xU-6Imd8yPma0ePU5DfS-_pYzoQN_IS5mIIPQt9kerC2I5ylPeGj6L3-gB-BiJHEMGJ-tQgg0cQZrAjeKws_q1E6h8CDpPmOxShswnkuBl2UhghTPIpIyV5yVwQAhap8PMFfOfPulQbEqRfm2Hb200hHPnEpDCvha2dhmO9soQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انسحابات مذلة مستمرة لقوات الاحتلال الامريكي من اربيل الى محافظة دهوك شمال العراق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91929" target="_blank">📅 02:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شركة أمبري البريطانية:استهداف سفينة تجارية بمقذوف أثناء عبورها في مضيق هرمز شمال مدينةخصب في عُمان.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91928" target="_blank">📅 02:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
مصدر امني عراقي لنايا
ممارسة امنية تجريها القوات المسلحة العراقية بالساعة الثانية فجرا بالتزامن مع الانسحاب المذل الأمريكي من العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91927" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سطو مسلح على شقة مسؤول في منطقة المنصور " مجمع المنصور ستي " بالعاصمة بغداد .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91926" target="_blank">📅 01:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اندلاع اشتباكات مسلحة شمال بغداد بمنطقة سبع البور</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91925" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
