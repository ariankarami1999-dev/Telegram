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
<img src="https://cdn4.telesco.pe/file/i7uRXO5Zm3iJRdc0qbpZ_Xhr5bCu2_9bzQrLs7-vbIAZ_If_k2lmnPp8CTrV3tZPxONPKEelCGdizfh9Myw-cSZhZg-EueUsXJg1GoWUQEZ6Y_ohLCoXiYvnCze14BYRtOx0lleR7Hx2MwQ9PPoeLAH6Li1JcUo_MG0VmvdmW_y7o8uYTQURn32pJUX3t6ylV9zoTPZlbwd61kSsWsQ9NbU_lPASlUwiKNvR6D-N77BJUn4kAFlOB-5OLSeUAY4Nk3XxbfCIcuZE32ZsgRqbgqD_ehnrnnbSMGI7NmJa7RVE94GRxvoaw-nuOTTKUgz-pbWy0JxEcilXbdlHLYAqjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 08:27:22</div>
<hr>

<div class="tg-post" id="msg-86786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار داخل مصفى بيجي وحدة الهيدروجين بمحافظة صلاح الدين نتيجة خلل فني.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/naya_foriraq/86786" target="_blank">📅 07:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/86785" target="_blank">📅 07:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/naya_foriraq/86784" target="_blank">📅 07:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇬
هزة أرضية بقوة 5.7 ريختر تضرب مصر وفلسطين المحتلة، مركزها شرق القاهرة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86783" target="_blank">📅 03:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي: ‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/86782" target="_blank">📅 03:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي:
‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86781" target="_blank">📅 03:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله أكبر
🔻
تأكيداً لمانشرته نايا.. حادث أمني شمال شرق خصب في عمان.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86780" target="_blank">📅 01:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86779">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86779" target="_blank">📅 01:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=OM510SUPs2N4LKSIqxdnD8AhDmzB8R7GYVleofM4gwXUxHPnfJVh3cTFKYKWTdAxrWxtteGOoQ0qvNtwHGb270JRFMarxjhnXwri64SfFofJfxrWmF78dZyf1JY9HlOwMD2uWP0_BgZvBX8uiRl3sj1rqClslmsMWmaEnMyMwy_-eLHz5QDaQ56BeJXWilLBSmiSUTAg2lYUdJ_1RsV_lRJ3q8iam_yedL9X9fah-8-1uCZ1C_InM1gfv5bMTJegru35y-7uJvC2s6HONDF8qy19cB7Rfjsb7aU3yHsq0HJeohs2yXVMNoDFjsTB0KUkVZL2EH0KzfPbNrpTE1IOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=OM510SUPs2N4LKSIqxdnD8AhDmzB8R7GYVleofM4gwXUxHPnfJVh3cTFKYKWTdAxrWxtteGOoQ0qvNtwHGb270JRFMarxjhnXwri64SfFofJfxrWmF78dZyf1JY9HlOwMD2uWP0_BgZvBX8uiRl3sj1rqClslmsMWmaEnMyMwy_-eLHz5QDaQ56BeJXWilLBSmiSUTAg2lYUdJ_1RsV_lRJ3q8iam_yedL9X9fah-8-1uCZ1C_InM1gfv5bMTJegru35y-7uJvC2s6HONDF8qy19cB7Rfjsb7aU3yHsq0HJeohs2yXVMNoDFjsTB0KUkVZL2EH0KzfPbNrpTE1IOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هناك تقرير يشير إلى أنكم تقومون بسحب القوات الأمريكية من الكويت والبحرين.  ترامب: لا أرغب في التعليق على ذلك.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86778" target="_blank">📅 01:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد المواكب الحسينية نحو منطقة بين الحرمين في محافظة كربلاء المقدسة لإقامة العزاء بذكرى أربعينية الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86776" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65466746cb.mp4?token=gnHhw-4O2FPUV-vvdpB2YHPSuJab48DGcVTAiKguV4zlSgyF0oxX_U46BhjYcY21fjS1H1aG03B-kh7Xr4eWDHntZxozXdd5_gwcKlb6Q0gKDigbNwxCoxxWyanzLh6Ucp6wTaoOpk4_3-Z0oqwR7B1VwaCLQL0KNCfwRK0s97Eadtb2PgA70rvLpt1SZ0ouxcH1sPGpSwPwSYfzyTENWiZkjsG8jjnOASyeadcx70zcPJorW49j_H4j0h3ayBcQhlPv13c9OGqbGbJZFsd4CZ4JcQhGH4L9mNR1CLPtIg83RJ7z2rMpFiGGnJ9YvGR44QLhsnR1VjhDIbzOjc7ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65466746cb.mp4?token=gnHhw-4O2FPUV-vvdpB2YHPSuJab48DGcVTAiKguV4zlSgyF0oxX_U46BhjYcY21fjS1H1aG03B-kh7Xr4eWDHntZxozXdd5_gwcKlb6Q0gKDigbNwxCoxxWyanzLh6Ucp6wTaoOpk4_3-Z0oqwR7B1VwaCLQL0KNCfwRK0s97Eadtb2PgA70rvLpt1SZ0ouxcH1sPGpSwPwSYfzyTENWiZkjsG8jjnOASyeadcx70zcPJorW49j_H4j0h3ayBcQhlPv13c9OGqbGbJZFsd4CZ4JcQhGH4L9mNR1CLPtIg83RJ7z2rMpFiGGnJ9YvGR44QLhsnR1VjhDIbzOjc7ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:سألت ولي العهد السعودي: "ماذا تفضلون أن نفعل؟" فأجاب: "نفضل اتفاقًا على هجوم."</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86775" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=OxjFFH5t_7UgokH-mSTMnxi7HP5wwCVKLuDFmJD7LuZ5vZzu3gbcBCdgAXchoSm0roiHYZHWboUm8IieeWr3oZsN4uWcCj5-5nivRRKdYcvgbC4dry6AnDQ3OQgbFFk1crcFkxot8RjKwPwcamUWMg13xWfE8YX2om57hhMRdxBL7Tqj-PBRB6Q92oxyx4WpWS_HMyi79lB4MKctn6vnqEJ39hk9RJ_3hjq5ts5_kF6GBNAyc_CabWKIqpEJf4XlhfGP4VEyUgMMUfXan_gnHbJDMBQBNHXckaxlPe0fO1gG5odyrYqD1PC7p0xoLVU29Cq-pr9WwlJ9TMLOz21bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=OxjFFH5t_7UgokH-mSTMnxi7HP5wwCVKLuDFmJD7LuZ5vZzu3gbcBCdgAXchoSm0roiHYZHWboUm8IieeWr3oZsN4uWcCj5-5nivRRKdYcvgbC4dry6AnDQ3OQgbFFk1crcFkxot8RjKwPwcamUWMg13xWfE8YX2om57hhMRdxBL7Tqj-PBRB6Q92oxyx4WpWS_HMyi79lB4MKctn6vnqEJ39hk9RJ_3hjq5ts5_kF6GBNAyc_CabWKIqpEJf4XlhfGP4VEyUgMMUfXan_gnHbJDMBQBNHXckaxlPe0fO1gG5odyrYqD1PC7p0xoLVU29Cq-pr9WwlJ9TMLOz21bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل لدى إيران موعد نهائي للتوصل إلى اتفاق؟  ترامب: سنرى. أنا لا أسعى إلى إيذاء الناس.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86774" target="_blank">📅 01:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86773" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86772" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏ترامب: لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.  كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.  عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."  إنهم يعتقدون أن هناك اتفاقًا. هناك…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86771" target="_blank">📅 01:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51407f800d.mp4?token=gVey0H-8LQ67wTPbvFo-xC3S4p-VJH1GJ5NimXRHESoV15cBpFhT24SPDYwWkcQ1gcmpvAJV31z_ROM0kgFTw0HI0Iut70spaUrNEyZvba_zT-E3Tkm5xVQMCosnQkJJ-sH4l9pOvmziFMrHVLMuQAs6BMU2flTf4lvyLbwj0hifGVsqliQr45X6Zo3s2hTAuJ1X4QpuitP2-g37s6S8e8gTIcvE2ZXnHYVnRyX8DJaDyPhmz1JzoALxpVBklLuzAWcvZP5wJ-nlGufKJAuXpd4Ymel5VYgA5gJ1pPJGui2NARcoZ_JiZNfKfMz-vR7AdHHnXuw5eyd6NLquPM2tlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51407f800d.mp4?token=gVey0H-8LQ67wTPbvFo-xC3S4p-VJH1GJ5NimXRHESoV15cBpFhT24SPDYwWkcQ1gcmpvAJV31z_ROM0kgFTw0HI0Iut70spaUrNEyZvba_zT-E3Tkm5xVQMCosnQkJJ-sH4l9pOvmziFMrHVLMuQAs6BMU2flTf4lvyLbwj0hifGVsqliQr45X6Zo3s2hTAuJ1X4QpuitP2-g37s6S8e8gTIcvE2ZXnHYVnRyX8DJaDyPhmz1JzoALxpVBklLuzAWcvZP5wJ-nlGufKJAuXpd4Ymel5VYgA5gJ1pPJGui2NARcoZ_JiZNfKfMz-vR7AdHHnXuw5eyd6NLquPM2tlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:
لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.
كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.
عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."
إنهم يعتقدون أن هناك اتفاقًا. هناك اتفاق بشأن هرمز، وسيكون هناك اتفاق بشأن النووي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/86770" target="_blank">📅 01:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxaPl_y1RLFyVld5OUPtDv8ZUTDPOVB97T_skLHdFZz0-ylPX3icsaCXx_smv69-9DLQlX6EX4GBZOqoM38K_5Csi6ka5DEpl5f0zFLKJNisaEFXjMjnsCJKVpx7m5QI9T_EipMJ9NU-Hxr6kCU0jEJdaPr2t2VKR_h0JrtE7beW_QwyhhhhvLE_P2KNrM7aJ7TCmoe77-1_WW8gGXg3rUhYeBIEUnZHyxBfGOQ8uDFp2ko8Rzf8tR0XZlCi-gXZHks5vXJfwXP3iUvkwNVWk4ZSd3T_IA1qUNGKQs3swsIcF0kjCHRKdTCZXarhG4nhlPtP5GFrWqABFvAS8Pe4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86769" target="_blank">📅 01:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=V1ua9mEv3ZPRLI4Rp_j0heZWzpPy9MeJkVaa_85QfUS5vUGW0k2y8wi_Zol1oF33w8qzJKtJkD4IIPbeYRxwLNpY6AqJ0roecCTLbyNxcFjDE-OEB69Z455K8LoqxR6usuZkddvcU_IeqLahEFHTqTD6JGOSureV6WyctUDtbE3OksRKLs6uRamrb9MqKUrOmK8l8sEGCJ5VJgEApNZDkmCTyncKQVRK7Kw2xOU0FyJKXyoG1fA36yWKBHgAq07iRGrRl2ZkKN8tDFhaczGzrMk18vTzfklmBfRk1-NoO9tsuOYHK3apWh5KF_mEGtP-CwD4wJ5RaOavzfZjY9n5VX3I3hWfjzIYk2jWrjvQOqggQT2QRUv9G4xolrkVtPubFuZG6aagIuBXNn3yWwhF8tl9SadhSCS-5aROaOJvwxExgjv1OU-Lnz6CPyA_hx4xAB6CS8uaWVERj1vCtfHFjGcbhGCdPHJfkQgFEm8IbKtlZ8TpISsrKHGlM29L62RZMZp6tibbxnemhm2pxFJYdJrwVQAiJb_lZzUJ7tiyDrDAwiQBfVht2_a7t0NnlRhI1BtT1a9buJAfp1XF3eGD5Cru9sQ72FJhPq9IkapFUlZ_TTN6zFKS0J6Qd2c68N0zbYoWCLHeFSQIRmzRi-TyAs68OE1GMEr-blSuujdldNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=V1ua9mEv3ZPRLI4Rp_j0heZWzpPy9MeJkVaa_85QfUS5vUGW0k2y8wi_Zol1oF33w8qzJKtJkD4IIPbeYRxwLNpY6AqJ0roecCTLbyNxcFjDE-OEB69Z455K8LoqxR6usuZkddvcU_IeqLahEFHTqTD6JGOSureV6WyctUDtbE3OksRKLs6uRamrb9MqKUrOmK8l8sEGCJ5VJgEApNZDkmCTyncKQVRK7Kw2xOU0FyJKXyoG1fA36yWKBHgAq07iRGrRl2ZkKN8tDFhaczGzrMk18vTzfklmBfRk1-NoO9tsuOYHK3apWh5KF_mEGtP-CwD4wJ5RaOavzfZjY9n5VX3I3hWfjzIYk2jWrjvQOqggQT2QRUv9G4xolrkVtPubFuZG6aagIuBXNn3yWwhF8tl9SadhSCS-5aROaOJvwxExgjv1OU-Lnz6CPyA_hx4xAB6CS8uaWVERj1vCtfHFjGcbhGCdPHJfkQgFEm8IbKtlZ8TpISsrKHGlM29L62RZMZp6tibbxnemhm2pxFJYdJrwVQAiJb_lZzUJ7tiyDrDAwiQBfVht2_a7t0NnlRhI1BtT1a9buJAfp1XF3eGD5Cru9sQ72FJhPq9IkapFUlZ_TTN6zFKS0J6Qd2c68N0zbYoWCLHeFSQIRmzRi-TyAs68OE1GMEr-blSuujdldNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
|
«دار الذكر» على طريق الحسين
▫️
مشاهد مؤثرة من بناء رمزي لـ«رواق دار الذكر» ومرقد الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكية) في طريق الحسين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86768" target="_blank">📅 00:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇷🇺
🇺🇦
مصدر لنايا : ‏ طاقم السفينة الإيرانية التي تعرضت لهجوم أوكراني غادر عاد إلى طهران  ⁦</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86766" target="_blank">📅 23:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الاعلام السعودي:
نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86765" target="_blank">📅 22:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يتوافدون إلى حضرة الإمام الحسين (عليه السلام)، في مشهد إيماني مهيب يجسد عمق الولاء وإحياء الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86764" target="_blank">📅 22:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
الاعلام العبري: غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86763" target="_blank">📅 21:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-oMn7jVMp8sLMq09DjQXET7sbk1Wu1JoMzr_62PyVRW7l0Ma3qZgHi0wJxnj8c7tUkyIJcLfVbKURoAyVAa1dhtuqpP1Hep1Chpx4RfGabbKWzlsRd4A5wFOWI8iwhEo4u6PzItSO_lpzdsUi3LFqXh84nNSOVppc4xyDrqOZc6IG_EhiLwteQ6H4Gqrepbxjb-Mt3y8yCOJj9oxgK-NeITOaY7xhOYCbFOoHeycNC1ojdCyr-IJclFG14-i6n-RI4oUmSuj12dM10Sl39T5hnWzVEiLaWmRbgk7xVbtQFMe61ZYsOPZwvMfldOGJPAT-LJiWBRnMl9OwtytCzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNW8T0A75D2wH5P7UPT9Ii0hQXFHez--iXa79pvjk_nifAHemtE6AR3qZN1BEg7LBnRwlnp_GxO5VVBEOg8Q--lj_KEbM99Iq2Qm996VKaTTlwnGaypa1zRqGo7DLUvKWANX6PQSHw2M7h4L79fA3hFuhOLAt8679pfCLahxDEgSydbPCPtTbj96yXZymy7knKFm-EnfMp6cAm_x1umRbXvhgDw7IUigQgcZdHQnfwpon8KR19iesZevFL5bEAV2ckJ4_j4VOX-fm7oSFdjDuJsRFUaJm7n-RAnuHWTWr7pnx-mNUw_wDpPL0c95g4Eom2k4uMrqG-UVM7qYcFcROQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
🇸🇾
حكومة الجولاني وبموافقة السفارة البحرينية في دمشق، تمنع الزائرين الشيعة من البحرين من دخول سوريا لغرض أداء الزيارات الدينية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86758" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86757" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
إعلام العدو:
‏حافظ آلاف من أفراد الجيش والدفاع الإسرائيليين على حالة تأهب قصوى خلال عطلة نهاية الأسبوع، عقب تحذيرات أمريكية من ضربة أمريكية وشيكة على البنية التحتية الإيرانية، قبل أن يُلغي الرئيس ترامب العملية في اللحظة الأخيرة. وانتقد مسؤولون أمنيون إسرائيليون بشدة هذا الإلغاء المفاجئ - وهو الثاني خلال أسبوع - مؤكدين أن القرارات الأمريكية غير المتوقعة تُقوّض بشدة التخطيط العملياتي والاستعداد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86756" target="_blank">📅 20:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86755">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇦
صفارات الإنذار تدوي في كييف.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86755" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
عراقجي
: المحادثات الإيرانية العمانية في طريقها إلى الانتهاء وتمر بمراحلها النهائية، وتلقينا اتصالات من بريطانيا وأوكرانيا وبلغاريا وأخبرونا أنهم لن يكونوا جزءا من الحرب علينا.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86754" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مباشر.. من حرم الإمام الحسين (عليه السلام) في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86753" target="_blank">📅 19:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86752">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل اعداد كبيرة في باكستان بعد هجوم انتحاري استهدف متظاهرين</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86752" target="_blank">📅 18:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86751">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86751" target="_blank">📅 18:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86750" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R53890AeXxxyx-z2WcluDL360Ir1cztlRPIFT3LWnhT7-syvLRU4CwNFPTpxweSuZUZJUTuVjWH6lRkA6intx7RH84plJ3Ofnj7v4cH59EmPdrQi4D2AHFtOYKJqWp32NAf7d9BT8kfYgsefrVwrR0I7BCL4Lhgtjiu2KL4icy9qJeaahNbqc_W_0UtDguUXonhiB1piYkRHn6kbfuRKe-9JgsKbExIgyDUtd0LOcQcYUFzhnbF_4BT3mCESCcuzGzgpIlYYA5-jD4KDIitsSGUIcOyk21yG8EK5RVHc36DXT6OzadvtP6-hfC91McPsax81aXhWK5pbERKMpg0K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات الحسين وأبناء الحسين
نداءٌ لا يخبو، وعهدٌ يتجدَّد مع كلّ ذكرى..
في بغداد، ارتفعت جدارية الفردوس لـتعلن أن راية الحسين (ع) باقية، وأن أبناء الحسين ماضون على درب الحق، يستلهمون من كربلاء المقدسة معاني العزة والثبات والتضحية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86749" target="_blank">📅 18:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
🇪🇬
محكمة النقض المصرية تصادق على قرار يلزم الخطوط الجوية العراقية دفع مبلغ 787 مليون دولار أمريكي مع الفوائد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86748" target="_blank">📅 18:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تجدد تحذيرها لرعاياها في أنحاء الشرق الأوسط وتدعوهم إلى توخي مزيد من الحذر.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86747" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=KWUzexYb45wlEniVW1KGvMG7FKmWoxrrPrDaIUPuUrjWK6VzZjo3KfjgnJEe49KEKWhJww-mIYGg7qXO9RFKJ3mQFd8j9GJPzPuA7hfQqAfeNQMNVXRIwKcBXhV56oyQbfb9Oc43BIfNXt_W8kE1F37InYmJGwbjhXwWOrZYWM5AX6wbKkQZRRNYF5j38IdK8aZzpX7Qe56pHypE1aosHhbqijwNn5ynmXrkVUW3epXqcwWYtNQ369RvdWANvofFW9kfYjaU9fga5N9hkge5wAQ49_raaUZ5gTPUdQXspOwNfxdFeiC8phpjzbZ9DritTOCafxwx6YIHIrlNiobRpBJ2eU7zw_KdsSdNkFf-a7oiAMfekSsX1es0zkGCFRVJgMf6qhp10b1vnmIqhRQfXB14HjpIat8_CEZb1L8pvgMxlA-eQqVyIYcAwIOXnGwMFV4ViWDl8g0jB8jMowyMbWOL1ObAXKuqrPhgw3qQ1Tj9O1s878exMovBeLJaHU-R3OQi1MA2zCPAUALqc13Lp9xwwGa9KDwo6qKj0m9SgWe26TgqGZ5jgeZ9BoqhSdnXl5RbLy8vL4hulwF4z3KMTESYXHArKnp6JXLHCJGOSfwKeQAe-dFJiwEkR05EkR0PvXirAFlg0c_hsW_veKlSr5hGSOMWeavUvJ-0SySMTRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=KWUzexYb45wlEniVW1KGvMG7FKmWoxrrPrDaIUPuUrjWK6VzZjo3KfjgnJEe49KEKWhJww-mIYGg7qXO9RFKJ3mQFd8j9GJPzPuA7hfQqAfeNQMNVXRIwKcBXhV56oyQbfb9Oc43BIfNXt_W8kE1F37InYmJGwbjhXwWOrZYWM5AX6wbKkQZRRNYF5j38IdK8aZzpX7Qe56pHypE1aosHhbqijwNn5ynmXrkVUW3epXqcwWYtNQ369RvdWANvofFW9kfYjaU9fga5N9hkge5wAQ49_raaUZ5gTPUdQXspOwNfxdFeiC8phpjzbZ9DritTOCafxwx6YIHIrlNiobRpBJ2eU7zw_KdsSdNkFf-a7oiAMfekSsX1es0zkGCFRVJgMf6qhp10b1vnmIqhRQfXB14HjpIat8_CEZb1L8pvgMxlA-eQqVyIYcAwIOXnGwMFV4ViWDl8g0jB8jMowyMbWOL1ObAXKuqrPhgw3qQ1Tj9O1s878exMovBeLJaHU-R3OQi1MA2zCPAUALqc13Lp9xwwGa9KDwo6qKj0m9SgWe26TgqGZ5jgeZ9BoqhSdnXl5RbLy8vL4hulwF4z3KMTESYXHArKnp6JXLHCJGOSfwKeQAe-dFJiwEkR05EkR0PvXirAFlg0c_hsW_veKlSr5hGSOMWeavUvJ-0SySMTRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
فيديو صوره باكستانيين يظهر بحوزتهم جواز سفر بحريني بعد تجنيسهم من قبل عصابات ال خليفة في محاولة لتغيير ديموغرافية البلاد ذو الغالبية الشيعية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86746" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=UpiUWU7bkNxmdDyPtxWLVDJd8pj98WFI00Dbt4Ihqv-2-j8jNyvP_GrdxOd-8h0XKt3DH4MmobYjtvEtVwufa51lOaJkiS1pH6XWOB7GQxABqbLAChzpA27XT5TJilQ1TREWpuuthZq7f1MqYy-ubootnm24W_5iEvN7zTtBUOtOFu_U6Qa4kkIWfCxUU4n-VsISHa-HariWg5FllXcaX66yFhjIVbvpq1O9dl3jrwk1g8OxdoNdNVO-ghU47ghUD5bT1mGZ-vQ7_8E3p460bANEfbgcNYYWCbsgSqS5pOTEdKK6OEKg2jlzql5E20OoxZAd1aS20Gt94Zf3gRlc8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=UpiUWU7bkNxmdDyPtxWLVDJd8pj98WFI00Dbt4Ihqv-2-j8jNyvP_GrdxOd-8h0XKt3DH4MmobYjtvEtVwufa51lOaJkiS1pH6XWOB7GQxABqbLAChzpA27XT5TJilQ1TREWpuuthZq7f1MqYy-ubootnm24W_5iEvN7zTtBUOtOFu_U6Qa4kkIWfCxUU4n-VsISHa-HariWg5FllXcaX66yFhjIVbvpq1O9dl3jrwk1g8OxdoNdNVO-ghU47ghUD5bT1mGZ-vQ7_8E3p460bANEfbgcNYYWCbsgSqS5pOTEdKK6OEKg2jlzql5E20OoxZAd1aS20Gt94Zf3gRlc8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
تحطم طائرتان إطفاء أثناء مكافحة حريق غابات في اليونان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86745" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات متواصلة داخل معسكر التاجي</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86744" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=fibNGX3-5NCZn3575Pp1UigGf5C3nZZCVGg1rfihW7czhuOe26xUaHr1GGwBdMKmZL8L3MdS-q02o-1AlyXOmqC_byqg51llOddtedTWisIBY3KsLh04lJPx-3krVivFbXwfqoEBQt2B8NYsMUgwa9EFPC9qZtA8DMr2EkmcaAZ9ciNN0yBeHPQc2BbbY_Z_UR8CMOxMvNGWwINOUEQvFGZ9n8w4AY_nBLPSKezoXGlGF6gtQkWRXxngBSNjAzXBmbSHx0JR8KUOMxmzFoNel5gbGhj70vosRajQ1WUqFjJ61oRXkoNRd1sUu4ewDahScadLe4xecIt9j8reahvVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=fibNGX3-5NCZn3575Pp1UigGf5C3nZZCVGg1rfihW7czhuOe26xUaHr1GGwBdMKmZL8L3MdS-q02o-1AlyXOmqC_byqg51llOddtedTWisIBY3KsLh04lJPx-3krVivFbXwfqoEBQt2B8NYsMUgwa9EFPC9qZtA8DMr2EkmcaAZ9ciNN0yBeHPQc2BbbY_Z_UR8CMOxMvNGWwINOUEQvFGZ9n8w4AY_nBLPSKezoXGlGF6gtQkWRXxngBSNjAzXBmbSHx0JR8KUOMxmzFoNel5gbGhj70vosRajQ1WUqFjJ61oRXkoNRd1sUu4ewDahScadLe4xecIt9j8reahvVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متواصلة في معسكر التاجي نتيجة حريق كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86743" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86742" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=qbif5NU16IwMFw3uMsgzXC9ERi17CiMO0mHZphpwVSTgbAvwL2jNhlsko_KmOIlyXATsnq-Vk5uRmktvcS_-k3pnopCHvKQZ_622W3EQUEstYStGGfB0T_TovirXDDoL0REoBT-YLRMdmXME5NuFJYCsPL6DSHPbMwyczspEkf6yfUFwCooaJRRKBho7ERGsGlwKygjgBI3yNsXR0rFzzRMcYTfnhWT1w9dh-7L4EmGjNPBlXJUxby51TsotNG5f5tgvmXQ-_PDbka3092cHxMOWECEyOZNP27vvwWzg6bJk2nqmrAzqPKMV_6N43cNO_cpwyu0feJ62b62alukuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=qbif5NU16IwMFw3uMsgzXC9ERi17CiMO0mHZphpwVSTgbAvwL2jNhlsko_KmOIlyXATsnq-Vk5uRmktvcS_-k3pnopCHvKQZ_622W3EQUEstYStGGfB0T_TovirXDDoL0REoBT-YLRMdmXME5NuFJYCsPL6DSHPbMwyczspEkf6yfUFwCooaJRRKBho7ERGsGlwKygjgBI3yNsXR0rFzzRMcYTfnhWT1w9dh-7L4EmGjNPBlXJUxby51TsotNG5f5tgvmXQ-_PDbka3092cHxMOWECEyOZNP27vvwWzg6bJk2nqmrAzqPKMV_6N43cNO_cpwyu0feJ62b62alukuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرق الدفاع المدني تتجه لمعسكر التاجي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86741" target="_blank">📅 17:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocfUumFQO52-857pGEaIb6ry_miHz1WRaZFjUimA8dAbTfsiJGw6_3UdkpxveTJVqsY1ZZsvZ16kPAbZ9WK6qz1wwWZSr8P48TrWO9_BgKBPBOZiH1i2UMvoPm7L0ZKWCagCGmYD0D8_UQMJHjPVOnfjanRmCFal8yW-Z5gHBDK7OhCrh5bCj6EW3IxCNLaYfhSxPIjohp3Rc7fFEs3KH23wsQOOH0Tiq5Ktp-FhFNzE88G7jyKn0xO7gNNwDiKlunClOjCcOkLvBZOHR_8CSoIxoBA-zX5-oCIxX16aYf9Cd2_NPGEbKw37FS91-DeFxP4Ge70xopMW289d3aI6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86740" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=YEWwK4Uk2VyOa9fnUDsJqvl9f9tWJcKUww6E5K5TKstBoL1uSJZo8_S9esqvMFN7zLJDbVgB5WuTaeUzhGG8Eg-Er1kYMJr5eBawQF4oSP-A4i1Pgj7ECA8xdNoEDiDnGaZtNk5iPRRnqrmt6ZD4jjwvZI9zIafhm2D0CtxO-fHIoMSvkVDnqgxXI8kZM4KtxNWJq50-3BHiFrn_O1jK8jB2SO8ctfbp8L3n_h1PKnR9oZvaCz66oXAkY5WHG66U4jafPHBG1fXz53AYP3Zcrc7Ujr9iGt7OVi_sWfrf9qPYIoqjZ_0d1gxwCx5ijEUA19_0LM7_FtA_64edzvk4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=YEWwK4Uk2VyOa9fnUDsJqvl9f9tWJcKUww6E5K5TKstBoL1uSJZo8_S9esqvMFN7zLJDbVgB5WuTaeUzhGG8Eg-Er1kYMJr5eBawQF4oSP-A4i1Pgj7ECA8xdNoEDiDnGaZtNk5iPRRnqrmt6ZD4jjwvZI9zIafhm2D0CtxO-fHIoMSvkVDnqgxXI8kZM4KtxNWJq50-3BHiFrn_O1jK8jB2SO8ctfbp8L3n_h1PKnR9oZvaCz66oXAkY5WHG66U4jafPHBG1fXz53AYP3Zcrc7Ujr9iGt7OVi_sWfrf9qPYIoqjZ_0d1gxwCx5ijEUA19_0LM7_FtA_64edzvk4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86739" target="_blank">📅 16:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
- إن الانتقام لدم الشهيد، قائد الثورة، والشهيد إسماعيل هنية، أمر حتمي، وأن الرد على هذه الجرائم الكبرى سيكون قاسيًا وحاسمًا
- مؤامرة نزع سلاح حماس لن تؤدي إلى أي نتيجة، وقد باءت بالفشل منذ الآن. إننا نوعد العالم بأن عزيمة المقاومة المناهضة للصهيونية راسخة، وبفضل الله، فإن الانتصار النهائي لفلسطين على المحتلين أقرب مما يتصور الأعداء.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86738" target="_blank">📅 16:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86737" target="_blank">📅 15:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مستشار الأمن القومي العراقي يقول انه تم الاتفاق على فتح مكتب لبعثة الناتو في بغداد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86736" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=AeN8CP16qnW4WtmX2w-BINn-lO6LeKhivhH1qW0LS-m0GI5x2EOd4wkDNbzWXgjtXFVsMpxFCrGmpUT7wVdnhXwiRI_kc3Gs99JQ9atHI-iF54qS7kI1eUqRmvfO086qU_a1U4SIuKRs3bL7GRnc2uuN_iUbQJwxJfg2lrfqX_q9Z2nj3pCbpBpQkUUAWEG4Iex5tsgJCaAHVAL-nExRSaWO0BHt2g7J9RAeXY-NASLj9oEr-e78CWQuQ5DQQ8o1stm3clcpAClx5VuxK_XWxEoNIw3RIQYzJktgf8fx5J_eLXOS6SmMkCJsgnJYc-kgo4Es_PQ-InzANs5hUA57kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=AeN8CP16qnW4WtmX2w-BINn-lO6LeKhivhH1qW0LS-m0GI5x2EOd4wkDNbzWXgjtXFVsMpxFCrGmpUT7wVdnhXwiRI_kc3Gs99JQ9atHI-iF54qS7kI1eUqRmvfO086qU_a1U4SIuKRs3bL7GRnc2uuN_iUbQJwxJfg2lrfqX_q9Z2nj3pCbpBpQkUUAWEG4Iex5tsgJCaAHVAL-nExRSaWO0BHt2g7J9RAeXY-NASLj9oEr-e78CWQuQ5DQQ8o1stm3clcpAClx5VuxK_XWxEoNIw3RIQYzJktgf8fx5J_eLXOS6SmMkCJsgnJYc-kgo4Es_PQ-InzANs5hUA57kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السفارة الأمريكية في الكويت تتعهد بالدفاع عن الكويت سابقا والان وتنشر مقولة لجورج بوش الأب</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86735" target="_blank">📅 15:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLj7fP0L_P-iJPG2eNtDCZ9GHYHqDLCvX3z2CdPX9TsjB6CYaXE7t90JThitabFferxhIi8wqzplEPTJnnEzeISSV-K7h6HlSfBCQj2Em2WizP1YEZL_dgIKpmCm675LcGOGvYb23CHeaDQGaA0bQmDEBpoe0cxbxuBStWWRelC1QjIx7JkQXZoUBWOljMKq5m7B-aAJ4I4phYtQQduExzyjLBZ6b5wYK2sg49If6z2Rtdl3NLBPZTdhg5-P27BHOW1Feep-LELdnO8QySSKLYeT9wcZuRT7L7WfSGZodP9qof9PtYgn7wOPASABrecaq8k7AZ0mE2dliE-yaPS-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا:  بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86734" target="_blank">📅 15:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوي صافرات الإنذار في الأردن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86733" target="_blank">📅 15:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avb7hM-iVzBnKDbwsCZchC6iUzTnGymbdI20ISLdgllj2fp4hz3SxWLLZcen2OJCPUungDuNdZEbckoK2J-Ulb1UN6nnLaOTi1FyLvaGD8-s7hjlQkD1UErKQ4HW1AVLHmIjluH71YwL-OAJ9Ip3xGq7dGAqMFr5nUJ6VeT-ui025W35OB5E_54JUWqBv-RAhFwF9G74d_T9t2-YiIjxTr51oGofVxP2kh5UfGzF2EdiqzPPxr9Lec6wepI4QQ3_1thuik0Vh_vGS6qsC5TvBI55OHCFtEQVwYgXjBQunpWgQySbhZsh0MoAC-6papAWEUxJYkzrDS2vV48z30rzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا
:
بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان للعراق وعدد من الحقول النفطية الكويتية ولتأخذ ايران باقي الكويت
‏ومن باب الإنسانية أيضا يقترح ان يتضمن الاتفاق مع الجانب الإيراني على عدم المساس بآل صباح في حال لم يتمكنوا من الهروب إلى السعودية بالسرعة الكافية وتسليمهم إلى العراق وإذا تقدموا بطلب لجوء سياسي للسلطات العراقية فيجب الموافقة عليه ليعودوا إلى منازلهم في البصرة معززين مكرمين .</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86732" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منظمة أوبك:
سبع دول أعضاء اتفقت على خفض إنتاجها بمقدار 188 ألف برميل يوميًا.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86731" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇩
اندلاع حريق في عبّارة ركاب قبالة سواحل إندونيسيا وقد تأكدت وفاة خمسة أشخاص على الأقل بينما لا يزال 41 آخرون في عداد المفقودين.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86730" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
مصدر لنايا:
وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86729" target="_blank">📅 14:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
نبذة عن نظام حكم عائلة البرزاني في اربيل:
- اقالة محافظة اربيل اوميد خوشناو من منصبه بسبب تعليق صور نيجيرفان بارزاني في الأماكن العامة وتعيين هيمن قادر بدلاً منه
- أوميد خوشناو قام بنشر قصائد ومدائح في حق مسرور بارزاني لكي يعيده محافظا وبالفعل تم اعادته لمنصب المحافظ
- اليوم تم اقالة اوميد خوشناو ايضا وتم تكليف زانا خالد بديلا عنه في مشهد يعكس ان الصراع لم يبقى بين السليمانية واربيل فقط بل ان الصراع السياسي اصبح بين الاطراف الحاكمة في اربيل وداخل عائلة البرزاني نفسها.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86728" target="_blank">📅 13:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=TAAAoqJU_MCKhsVZg5loh9uIjucNdahH-Ih9q6rpdNixtlhkNoPfi21iwlmTmyM47KNm9PXshYrkoilSCPL_seoCfx2eVa4KBELVnlTDUWXaNZ9If4cTrRB60nx6xil8didA_yd1KW8MJS_qKRmYj8skhfMhul6GPOBZlymBTMrXM4RWvWYIxrJeWBpseMZGu_2uYSXM6aldEC-4ycih7kOqcoOE0Oxvx6rgaOz5npQzFXbLK-MUlQLyVenDBGtT_ucJuNBnGteOyDDkpsjZdPPYEY5s4eqO1NRbpKglSqF4kYXlItv6Hnib3vOEYGDZ_xRCw07aAc6kTq0V6Y8Bng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=TAAAoqJU_MCKhsVZg5loh9uIjucNdahH-Ih9q6rpdNixtlhkNoPfi21iwlmTmyM47KNm9PXshYrkoilSCPL_seoCfx2eVa4KBELVnlTDUWXaNZ9If4cTrRB60nx6xil8didA_yd1KW8MJS_qKRmYj8skhfMhul6GPOBZlymBTMrXM4RWvWYIxrJeWBpseMZGu_2uYSXM6aldEC-4ycih7kOqcoOE0Oxvx6rgaOz5npQzFXbLK-MUlQLyVenDBGtT_ucJuNBnGteOyDDkpsjZdPPYEY5s4eqO1NRbpKglSqF4kYXlItv6Hnib3vOEYGDZ_xRCw07aAc6kTq0V6Y8Bng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مضيق هرمز لا يزال مغلقًا.. مضيق هرمز يشهد اليوم رياحًا قوية وتقلبات بحرية، لكن إرادة المقاتلين الإيرانيين راسخة وقوية، وهي المهيمنة على هذا الممر المائي.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86727" target="_blank">📅 13:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86726" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKu4CnJXdRxfkf7t3fBn4djOUH56GDNXFecuznx_idrwrr4sD9m9h1q0kFDX-HapufhRCI3JZcPzHlG38tTs3FK1n2fj7y3V1mId0MADKWrq01NMmB163sOtRq8gRLpWkjrQInkzLeHGhwQL0TwBAazPQHAbgpnSZzbbsfJaL4fldgHFxK2tRNyLBb6lPm5Zx551yPURymgTsqO7FBgWvJQo4hWD2Fee1Z6MHRnnwAbNGrltQBkgekqyMgQeE5vwDfA9rbk6bDn-K_HznW9uv28ZKLNPJs8_LzgjwFU8QTw-CMpI-YZAOysMjhOLwKfC3922kS8Cubx8WvjSgiB5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAPqhpnPe262Z_u7KAdunOeGPab_VEW-HyMgW7Qg-vjUjGdG3wt2a1jW8QNwl31qnU-sD_Q94CqJLmActF_nKjEYPYgIX2iUg9r7HCent9dUXR7zE9Am5L1Br8hRj3IN4fZTIAUO9C_9DUixvGrvwsUK9T12ut60PMA4ROa1JOybgR2XY6ho9_QkUDkvR0Dc9Rqwkyu8G0Bk4lGGOB2xnGUalbbG_Xg1w3TrLfFVDtFHjuUDAnEElg4i_tFL-jmX0PDaQhkg53vcazsNR4nj2O8VV_5EfOoA_MGpDyxboW5UFLiaNhzS1bxilC0fholdY56mX2_DrvQ7KYzB6COifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RU7iUhQvDZMcCrnyzvvN9IoyMBl0S_OsGC_5DW3q-Lvd_r35PnJKm9XYMl_TAViggBsLsNOoz5msKsUTydQ77JuUnHfZ9hjkSFgSV2_j97acZaRPTVYCnFEgRCp841-vIK--1R2YZfNtRuCUB0alHnAApxAZ2pB3KlJe-I5gUPiXXgySZ8PffSKaflmFy689DWf9WP9geJWuvXf48U3Sskd3FdYc7YUSZqeVK77QV0FpZKZgRRCmj4CibrmcgJBRs5CFt76r5G69lfDnqMOIcM3ftihAwLuyzlN2Q-4XbNMylhbIbhujvu4NpYoJFZ5q1TIyf4I_DQr8qmrvQNcT1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هبوط اضطراري لرحلة الخطوط الجوية العراقية IA248 التي كانت متجهة من مطار كركوك الدولي إلى العاصمة التركية أنقرة لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86723" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
مصدر مقرب من فريق التفاوض النووي الايراني لوكالة فارس:
لا يوجد أي اتفاق بشأن إعادة فتح مضيق هرمز، والأخبار التي تم نشرها حول هذا الموضوع كاذبة. طالما استمرت الإجراءات العدائية الأمريكية، سيظل مضيق هرمز مغلقًا، وستكون حركة السفن ممكنة فقط عبر المسار المعلن وبإذن من القوة البحرية التابعة لحرس الثورة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86722" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني سموتريش يتحدث عن "اسرائيل الكبرى":
‏وعدنا الله بأرض إسرائيل بكامل امتدادها المذكور في الكتاب المقدس. ‏أرجو وأدعو الله بصدق أن تتحقق تلك الرؤية يوماً ما.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86721" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
شركة كابيتال:
اغلقتا أكثر من 300 حساب مصرفي لمنظمة ترامب بعد مراجعة داخلية لمكافحة غسل الأموال.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86720" target="_blank">📅 12:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇱
هيئة البث الصهيونية: حماس بدأت خلال الأيام الأخيرة توزيع بنادق على عناصرها في قطاع غزة تحت غطاء أسلحة شخصية، حيث أن الحركة ترفض التخلي عن سلاحها في الوقت الذي يتمسك به "مجلس السلام" بالتزام حماس بجميع بنود الاتفاق.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86716" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn9EXSYRu_TguiO87hM_teDex5aWHnI8Xd_Ghw_ch9L_ANSE4-jWw96LF8DegCjUTJR55dGQDctCeoOMsq7LcopUVipQ7PDXQEO49laxUiEY8ZkDoB3LSuuGTR8LxaQxkUWOj_jcqh3wusz512GpNHkc9EMSIFhpk4tAjkwn3WYaB9_S8AbEwmUbmG58JfcBgH41IR3pgMGyfNYDIAi98xqgs_38Ho1aDI5QVPxIC8TeNM9Ly6ZEtajAKTycnhB9GzdCxu9hhgGKCBafjJG8sQgCYUZx7cDCrA5hvOlKRvlgw0YPX4DOqN7beDEuZMrlonuRbhAVbrwBC9RivwVU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الإعلام الحكومي والنظام الكويتي يهاجم العراق بذكرى ما وصفه الغزو العراقي الغاشم ويطلق طابع ضد العراق ؛ علما ان ما يسمى الغزو كان على يد نظام صدام ولم يكن على يد الشعب العراقي وكان نتيجة سياسات الكويت التي دفعت صدام للهجوم على ايران ريثما انقلب بعدها صدام وطالبهم بدفع مبالغ مالية نتيجة دفاعهُ عليهم حسب تعبيره انذاك</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86715" target="_blank">📅 11:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2FenJp7hoaVnYsfn_fMp39GWIsB97FERW2xzN84I5zqnf1GlxcC6urTLPL-0VMLNXdwZ4ZaMyq1FUaGvrlrMLp7badxp8GZlh5Ty1eRgNuY4OQWd8I7DyKjEwviimye5UZ6XE1beOhe5x5PBZolUjzHFsE9OLxlJkOigLgkF2sQM-9XPOOKIoDbJkbNQJ_00fWmTAjdakn7vQ-Mvy_DzPALvLB-a55D4AD6QcByaDsTuOXSPAMoOp6242vJJQYY3wkMIpTlkp3RzByeYasLtIJzo7O2Fh6L2QDWq907RBw-NnZy6VeOeLb6jV7sa-T6WGWG_7h63EtIBgHZ_7AVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amWrtcQnHoroWCE7mPor2pbMoiNExLoM6vWUVwNR12cjGKGxMElr5E2hItno1UdAlii_fpXOCcIBIU_JERcyg17N9LlnaB38Dd1kGrSDg_TrVJp10n9THgcO0KE8aiwnF3807vqVTT3KwPRYdcTdJT1SUwKLv9Aeh-60RFg7-iqRO21nG8EvneWWuec0eGi7EPuuiF1-jAlY_REmCsG7cn3H_i7NlogPHPqGVczqmWnXkqq6RA6rrnV_oslvmZ1Y52aWEm-t_0c2V9QbpPXKH7Qq82kKvZ7le7dQKhYYwzdOzWxpH8HiF65V1qk_ZSVhhSbWGDokzkkIrLpXxlRLKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصدر امني لنايا   انزال أمريكي بقاعدة عين الأسد ثم انتقلت القوة باتجاه صحراء النخيب غربي العراق</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86713" target="_blank">📅 10:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: الكشف عن مخالفة أمن ميداني خطيرة بين وحدات "الجيش" الإسرائيلي التي تعمل في لبنان</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86712" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
تقارير بريطانية: مجموعة واسعة من التحالفات الدولية تشهد حالة من عدم الاستقرار - في أوروبا وآسيا والشرق الأوسط وأمريكا اللاتينية - بسبب دونالد ترامب.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86711" target="_blank">📅 10:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujxG9gs53Rirvk_M7IMZawxJxx5a8hgJ44ShMav3Hk7IKsygRl1JJZocoLzoNTaiu8A4b6Y7tOpGdcuW6KjcYJcnw6OjsGxlR8n-s5E7qLAISsBfo1F_SLWVBRM9G0oIk970Vn1mIfHo6VJPCuONuqjFexNrT9wfQ41HY39pPymqHRivcVvohptwZWQ-52QMjU3OF86fnOMOa-YFVVzv6lcsuYUTYGhzNV0YWJ_Ol-Q3gCpXYMUZjuQxq9AXvyyWvxhVG2B4Oy82VzyFGeP6qaFgXr_B7ANi_X7bkgthcJRJYnHrlRWVrrNdErDdlIaOnxtYVU1JCCz2j4xWWlgD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇰🇼
طائرة نقل عسكرية أمريكية من طراز C-17 قادمة من البحر الأحمر وتتجه نحو قاعدة علي السالم الجوية في الكويت على مايبدو تحمل بديلاً عن الرادارات التي دمرتها الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86710" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8a6J3PNTHys42rAwJyq-MTMnZNKMh7As64jwiLjI8i8J2Ro_OphQD9V4wbskiLpngBp9ta8dgPDBwqECLEaBtReISxORLg9n2mQkuPPEZ7-Qb-MjeVdmzyMPY0XMc_sfX02jw40W6TJ6FoBLJaGceY5hEkZSjiU6M38yfzJc_jz7EQ-kkqF4cIABCiMfWKraKy8KLCaMumi0hLD9n2E0GbqZst9NDcnIELuSYZTX6cwCqXD51lpVT9Mj9BdDhX32rOL-1HltAO2LDUvsghrH97IMBW9_EwVGL9-RdLzwGUzvF3sdc_WMVxw7OYArn5EzC0wwBi23NO5O1oxYLiUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBwHM-NtmihOSUv4Lp5Ze1MU_PhsMOZ18AmpyzudlRstWWKs6K-bP0nP_l4QNquMe9BMsw6v76z3t22NLGxY_utT6bMqoix0a7yjXfGCMOTrxomimRKh5phUCWx6ZHkW_L07KLa54YWJ1KrsTXUUyeZDwe3OVSVYMI4uLO_SPpaJkQjBLBQh_kAs7wDbbKYHiSom63eXuXiPIE0_cgRUT0ap7oqLp-peJjkoZDFpYBq5gVfE4O8fmHcUnjmrHgtiFnlKSu9eFGATbO2P3cNMRVBJegKpY7hL6xyVc2np6b1xI4YEVi_0Xzv1tqJLZV6-B3ag6Atn0apo6O76KwaswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcETaONRgK7GOYsBtXHn7A4_d-Fdd_3wQXu_WcAtMSmeAnhG6-NAw6EWZHSgNncmAMSmLq7lP_KMNyy7dqEhydDNYmXOOvyt9cSuVR_rJlNimhEsa5U9jorV6pNH1BGycN1ggsrcBS5TiS2rp1EK7sbGBvQ4i0kIWu8tZQV8Yd6x988nKe9gZGLOgNUuBU1hZmoDEOR1oUckkMw27ov7Rf_UgjAwpQtyJODbuHI_wx-T5L2oBxPVSxIZkIcRZ4Kb-HmpfaByN4WzJacmnlcNlBhvtcaXXDc1eQrAyMP-tXWsUap1OLN9pIGuULd-GpAdGrZDeqkfVferBcHG6sAN5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حادث سير لحافلة تقل زائرين إيرانيين في محافظة واسط العراقية مما أدى إلى استشهاد عدد من الزوار الإيرانيين بالإضافة لاستشهاد عقيد ومنتسب في الجيش العراقي.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86707" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86705">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiUnGKrEqy6tCRPLvGgC29X7-PIyQt3dblBtzonCa6B6G3twVHyOCTbdJeiI6yoFZKPvFnm3-fSOJUqavfZLlrlwZk7uzzdMuwQabfpD0ptHumKOxSS91FAAPNEGwkH_3djgyfY6FVVih0LFta4x15iNlveekJkM1ZJaqfqXqXlupf2QpuVa_9-ENsOfJ0WUdfPbNUm5CgjcN2Iqj-5SsZeOugwDGdBv5CzumoqUDjHcRLTEx0D4CV5j6fy1vvZr6HyPNqKDaGC30ld_d7aYpmUzV5s0211j5RrXkqIhn5JmQwL2veIUMwv-J_nmsbG7Ko3KfvyjCO4iTW53Eutw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2UUFwbvTkXkNfl1lawCCh8sQAKWuy2Ij4teH51UK5OYg0oF2zc3j9DH8eoLgr4-0H-U5SbVJvtDdR2rTT8iycoYdtP2SuJa4FUgMvwpmcHcl6oYVeFhueu0cTNmfh6aFynaUg-6n0nJks9As_P4kczYt_kcvIApKHbmDbD12wqX4Yx6IKM5Mb4-txJQvstBnU457ReD5PwA4xncKfo0Ggid7Nc0OI2x8dd6GhIHbO6FrTUc-GAURuxOIoDV709gl6NBJMb9O5A9eGBBZOGf3In_GHx9NRMo7kGlXmxdfqJ4yburNStAQUJ4rMCemk0X7WyhbupGvgArjq_cS5tbxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
ناقلة الغاز الطبيعي المسال GasLog Shanghai تقوم بتغيير حالتها الملاحية إثر تعرضها لحادث استهداف بمقذوف في غرفة المحركات أدى إلى نشوب حريق وفقدان كامل للطاقة والدفع أثناء محاولتها الخروج من مضيق هرمز قبالة السواحل العمانية.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86705" target="_blank">📅 08:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية تفشل لالتزام بالموعد النهائي المحدد في 31 يوليو/تموز 2026، لتسليم الملفات غير المنقحة المتعلقة بمزرعة «زورو رانش» التابعة لجيفري إبستين.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86704" target="_blank">📅 08:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlbwBrZEGhdAgzb70-KexsR4PG9BFGoDS7Fme7OJtNaNVF25qovoCQKAkR1yKWS8Yj8uN-tXtzS58MgDf97PSeMBIgrnClbEIVQAPJ18vzobWZc7z9q5AO_mEQwNMuFwh0mq1kPY3bo9pWSLImcWgmZ1mtpDmZ8geuQFqHfewlDZWztPvz2n-NMbl1YuE4aIuc9NB3MTMRHv-KW6ohTgHBg1eteu8gKqJWiAtZ7PePpaSKjMMaTD0NCA5gTtdlWKC14i1qQJdx0LBfgPXHjgl1vu7aciB6NxlcDCPLXbCtpnsLL4ZRvAgfVeM8F7miB5zVeD2O87Lt8snJdbbzX7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
خوفاً من الرد الإيراني.. ترامب:
‏"الولايات المتحدة الأمريكية على أهبة الاستعداد لمواجهة الجمهورية الإسلامية الإيرانية، بمستويات من الإرهاب العسكري والقوة لم نشهدها منذ الحرب العالمية الثانية. ومع ذلك، فقد طُلب منا مؤخرًا من قبل إيران ودول أخرى في الشرق الأوسط، تأجيل أي هجوم، وذلك بعد الاتفاق على بنود اتفاق. ويشمل هذا الاتفاق الفتح الفوري والكامل لمضيق هرمز، وإنهاء التهديد النووي الإيراني. وبناءً على هذا الطلب، وافقتُ، من أجل مصلحة العالم في المستقبل، وكذلك من أجل بقاء إيران مزدهرة وناجحة، على إلغاء الهجوم، شريطة التوصل إلى اتفاق سريع. وتشاركني دولة إسرائيل في هذا الالتزام. فلنبدأ العمل جميعًا، ولننجز هذا الأمر. شكرًا لاهتمامكم بهذا الموضوع!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/naya_foriraq/86703" target="_blank">📅 05:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86702">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي "مارك روبيو":
إيران لا تزال تمتلك صواريخ ومسيرات لكنها فقدت مظلتها الدفاعية التقليدية.
لإجبار إيران على تغيير سلوكها التوسعي يجب رفع كلفة سياساتها إلى مستوى لا تستطيع تحمله.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/naya_foriraq/86702" target="_blank">📅 04:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86700">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=uYF3Bc1AMFUnmMN0SfM720_Vz1Alc5OtDXafniIwDbJNnhm7BuucpDll7FZmbLLrSsool3xmNlDtfSJKD7002BUbfd-CUWIYaV2MZkOvJ0hqqiwb9EG26Bn5dhB7Ee7qgnTHOhHuLo4kdktexIkEqYkF_mOiaTqBgKNaY_7wpqf5zhGLPqxHZzIbNyBcivekEJeadcxfbybNyzFsu6rrmm8QJSobn6sftpil3tEyu1muH8_CSnsvBh-VHJRheIfGOCQcpKpICsmoUPwl-sRVWwGkO3vkhz1Puz2lohMHXeF-4TY7r8II8Jm7tUc6POM0eMgSHOo4Y9TDy4mGzcxqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=uYF3Bc1AMFUnmMN0SfM720_Vz1Alc5OtDXafniIwDbJNnhm7BuucpDll7FZmbLLrSsool3xmNlDtfSJKD7002BUbfd-CUWIYaV2MZkOvJ0hqqiwb9EG26Bn5dhB7Ee7qgnTHOhHuLo4kdktexIkEqYkF_mOiaTqBgKNaY_7wpqf5zhGLPqxHZzIbNyBcivekEJeadcxfbybNyzFsu6rrmm8QJSobn6sftpil3tEyu1muH8_CSnsvBh-VHJRheIfGOCQcpKpICsmoUPwl-sRVWwGkO3vkhz1Puz2lohMHXeF-4TY7r8II8Jm7tUc6POM0eMgSHOo4Y9TDy4mGzcxqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/naya_foriraq/86700" target="_blank">📅 04:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86699">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول أمريكي:
ولي العهد السعودي محمد بن سلمان تحدث مع الرئيس ترامب يوم السبت، وأعرب عن قلقه إزاء خططه لشن ضربات عسكرية جديدة واسعة النطاق ضد إيران.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/naya_foriraq/86699" target="_blank">📅 03:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86698">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مصدر امني لنايا
انزال أمريكي بقاعدة عين الأسد ثم انتقلت القوة باتجاه صحراء النخيب غربي العراق</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/naya_foriraq/86698" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86697">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx4PbMm-perIcO5iYcmfbNrqxDIbcYXEA46LgCSqPG8xs87Wd08KjfV3qF0KUyluV-q1yPnlRyHpE_I0WkR3iHIqqZM8lPz9u1Awzz-IbpZyAil3f0QvDjzEpy7GqpHGpS9YnHR17sZ1oyQtXlcDvngdfsbcWcSdAmcVeLRYCJugoZA1mTkiMUDvSz_1dnSDQSU-BJ8ay3ULjdSTdNWJa2IL17aV0fm9AIvrCpd4CjWtfkEb_Ixn1iMHP4ZI90j0FNgs3tPWBvpeMlp_sztq9bUxZcm47kJEEA3BReqtTe-FL2j97fKtjCVtlCoEHJxZaq06ThD_C9NT-DPZjq4Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ينشر غلاف النيوزويك بما يتعلق عن فنزويلا علما انها التغريدة رقم ٢٩ خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/naya_foriraq/86697" target="_blank">📅 02:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86696">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/naya_foriraq/86696" target="_blank">📅 02:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/naya_foriraq/86695" target="_blank">📅 02:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری به مقر تروریست‌های تجزیه طلب در السلیمانیه عراق</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/naya_foriraq/86694" target="_blank">📅 02:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=Jp3VyB7szAAlC3l-syQVQanUNxxw3c_5Z36PGZJZScrEQ0DVKJJ3A9eZHPrM1Gv9BI27QweXw4mUd-zTn1Gym3HNV0rsrNsoKM3e-nB4LhTEqj80i6k2TNndrBVr6TvPTYx3JpKfe_lILnynqTBvnYVoSrKwW5cdPIr5iNBKJQmFoku26r846UxfL17cs-U8VuvzRs20PoYO7r71-7941u405L5oPe2gp8_TTwn6e46MqZP49RHRXaBAUBjdTraNeAFcBX71RsO2UcNoSf8rdVW5AYQPqnwee7w84bcg0atk5BsyFfJVSQzRbsgNHU6p8s-IBI5zpwKOn6dVauY2cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=Jp3VyB7szAAlC3l-syQVQanUNxxw3c_5Z36PGZJZScrEQ0DVKJJ3A9eZHPrM1Gv9BI27QweXw4mUd-zTn1Gym3HNV0rsrNsoKM3e-nB4LhTEqj80i6k2TNndrBVr6TvPTYx3JpKfe_lILnynqTBvnYVoSrKwW5cdPIr5iNBKJQmFoku26r846UxfL17cs-U8VuvzRs20PoYO7r71-7941u405L5oPe2gp8_TTwn6e46MqZP49RHRXaBAUBjdTraNeAFcBX71RsO2UcNoSf8rdVW5AYQPqnwee7w84bcg0atk5BsyFfJVSQzRbsgNHU6p8s-IBI5zpwKOn6dVauY2cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتراق مقرات الإنفصاليين الأكراد في محافظة السليمانية بعد دكها بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/naya_foriraq/86693" target="_blank">📅 02:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=qSvdkWQZImuCxox3Oxff8TwLvgHsu9WX9UNMUBeaKcUUEa3I2ZTytKxq3cB7HHhUTLQLFXSwRAFusRdij4hrANil4pxT3840KnCqxfqQ4gms7Qv6pTnpI9TOQWTmW5tR5LFOD3nq4T6M7AoAYocXQEPsaEC8RWWw6XdvhK2rL7XcrVKUBqey3_tTpPDIiuj25e3gAhTXoc46rnTibsyaQ8LO3k41zna1FFUqwAvgH8lm1Lg8IfercUME8KMLMOrte6Yq7i9w6r42vzZK-QJX2fyk41fd-_Px1wEjXvbx9d39YRaqRfKdYXRhjStHFuiDhDaxdPw9-E4L8yMFULNwrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=qSvdkWQZImuCxox3Oxff8TwLvgHsu9WX9UNMUBeaKcUUEa3I2ZTytKxq3cB7HHhUTLQLFXSwRAFusRdij4hrANil4pxT3840KnCqxfqQ4gms7Qv6pTnpI9TOQWTmW5tR5LFOD3nq4T6M7AoAYocXQEPsaEC8RWWw6XdvhK2rL7XcrVKUBqey3_tTpPDIiuj25e3gAhTXoc46rnTibsyaQ8LO3k41zna1FFUqwAvgH8lm1Lg8IfercUME8KMLMOrte6Yq7i9w6r42vzZK-QJX2fyk41fd-_Px1wEjXvbx9d39YRaqRfKdYXRhjStHFuiDhDaxdPw9-E4L8yMFULNwrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي بإرتفاع منخفض يحلق في سماء مدن إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/naya_foriraq/86692" target="_blank">📅 02:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=ANzpem8tejGdlQIEH9SQjNxByCaWc541z8kjCiKVSUeGzU8vnB9yoqQaHfSsu_N-_XkcgO1XgFE7ZrZu8Dx3dj3ecahuo2Z44OBQyf8ZbFGkMnB5P2z3MClyyakARIzQjOYNLf5ZZep6rsIeD3eN8cjbqVeOUNpnn2Wx2zHm5o4AB_o4JzEr2z-vaiddHFFjWH3voiWakg-W9DokH37hRqR24hz6ydxAM18_IRSIQfR6P_I8bA4pByWMaOnUPj-SjTH247sJrCy-jareXWnXFVtdlQpAVLG7VHV4OdhH-NKdn45vUlf-xE5M9EMTEtj28p4vaFzdh_6cgZFBQBUvMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=ANzpem8tejGdlQIEH9SQjNxByCaWc541z8kjCiKVSUeGzU8vnB9yoqQaHfSsu_N-_XkcgO1XgFE7ZrZu8Dx3dj3ecahuo2Z44OBQyf8ZbFGkMnB5P2z3MClyyakARIzQjOYNLf5ZZep6rsIeD3eN8cjbqVeOUNpnn2Wx2zHm5o4AB_o4JzEr2z-vaiddHFFjWH3voiWakg-W9DokH37hRqR24hz6ydxAM18_IRSIQfR6P_I8bA4pByWMaOnUPj-SjTH247sJrCy-jareXWnXFVtdlQpAVLG7VHV4OdhH-NKdn45vUlf-xE5M9EMTEtj28p4vaFzdh_6cgZFBQBUvMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد أخر للهجوم بالطيران المسير الإنتحاري على مقرات ومعاقل الانفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/86691" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
دوي انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86690" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50695baca0.mp4?token=RQDfhNgdZvWV1aiMoo8f6RUAwqSHXx80N3wd-A9Ss-3zks2YREJnXTYM8jREO5gVKaYF5bK7WpzZn5d3bs9G6UxoGEnLjN1ZxNikfWzXCy7q4qYevWUc9P2yvoOf3RkwZLqRij_pbo0JK9PUk7DxvITmlXkYlu5PoLObANJJZdr1GIIjaUoYUv992qAyRr6FON8VcYG9My3spmnyp-YypF-_n-8MHgOaVk_kfm3dcIPWmycR6C5Mu0nzq4w17xmHWVkz6SRCVmOEIL0ZOqcliqaKnKdrPvqtUdZ_4HWluUxsefjB3cTax7-PjvkoOLPYTLRzIh3Muj3cL97vFlaupg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50695baca0.mp4?token=RQDfhNgdZvWV1aiMoo8f6RUAwqSHXx80N3wd-A9Ss-3zks2YREJnXTYM8jREO5gVKaYF5bK7WpzZn5d3bs9G6UxoGEnLjN1ZxNikfWzXCy7q4qYevWUc9P2yvoOf3RkwZLqRij_pbo0JK9PUk7DxvITmlXkYlu5PoLObANJJZdr1GIIjaUoYUv992qAyRr6FON8VcYG9My3spmnyp-YypF-_n-8MHgOaVk_kfm3dcIPWmycR6C5Mu0nzq4w17xmHWVkz6SRCVmOEIL0ZOqcliqaKnKdrPvqtUdZ_4HWluUxsefjB3cTax7-PjvkoOLPYTLRzIh3Muj3cL97vFlaupg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيران واسعة تشتعل في مقرات الإنفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/86689" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=UQUNzAq0ATuKt9ID5Csb7qmix-sZGA99WVW2bIeacvJa5-SdAd-yZMoDf_bUlVbxM56PeKtiJz7M5zTlWQstOerHO7ywUSKwRFtmy43f_UpDf--9_FfxvgZ1SkjPV9Ffn3FGM0letbLj2wkJj2HVxyvbydtqRyOvvbNRTiifrXrkYVIdJecb9VBu4Z_IhBX6G_v1cbEvFjq3q_tVT4YzzO9ut-70mglM_m24IJ39F6M85M0DjXxT_dx33T-WVczDEwrUqYbBfe5clEncKjmmRMaFpNKdc25fhXyJwPmvgLqw9MXuKRHodcGnrm7sCoiMrffNkZKbgXQkILJQdzXn6p1cVRFGocFp3hL4ShQvm4cXMhtwuhoA8Li_YKGN4CQotEx49IcqfjF42Pe0x-pDDNIohLzTABYPMFf1C1VYNvOUfwh38AW7sODc5NGQVFmCCpW0ARDQgGBpONbjHaB6EpyxVdGh8K31Wh3FaXgI1mDgbDR-sneDk-jeV3vfOgYxgQJNMlKTOsuV4vjnppH_DzRsb-QVxT5tcUIg4aG0n7Txtu5h0ZUDm7bGIHcL7TKGm3VQda6dKs8crRk_PkYKpBaFl2IlMlwDd-QiRbxKTujpvBTUMi7tDa8YTDZ-XukUSkwJEveVcASjMAEASJaRHWy8fZaFDNoJQ2U5qrAe50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=UQUNzAq0ATuKt9ID5Csb7qmix-sZGA99WVW2bIeacvJa5-SdAd-yZMoDf_bUlVbxM56PeKtiJz7M5zTlWQstOerHO7ywUSKwRFtmy43f_UpDf--9_FfxvgZ1SkjPV9Ffn3FGM0letbLj2wkJj2HVxyvbydtqRyOvvbNRTiifrXrkYVIdJecb9VBu4Z_IhBX6G_v1cbEvFjq3q_tVT4YzzO9ut-70mglM_m24IJ39F6M85M0DjXxT_dx33T-WVczDEwrUqYbBfe5clEncKjmmRMaFpNKdc25fhXyJwPmvgLqw9MXuKRHodcGnrm7sCoiMrffNkZKbgXQkILJQdzXn6p1cVRFGocFp3hL4ShQvm4cXMhtwuhoA8Li_YKGN4CQotEx49IcqfjF42Pe0x-pDDNIohLzTABYPMFf1C1VYNvOUfwh38AW7sODc5NGQVFmCCpW0ARDQgGBpONbjHaB6EpyxVdGh8K31Wh3FaXgI1mDgbDR-sneDk-jeV3vfOgYxgQJNMlKTOsuV4vjnppH_DzRsb-QVxT5tcUIg4aG0n7Txtu5h0ZUDm7bGIHcL7TKGm3VQda6dKs8crRk_PkYKpBaFl2IlMlwDd-QiRbxKTujpvBTUMi7tDa8YTDZ-XukUSkwJEveVcASjMAEASJaRHWy8fZaFDNoJQ2U5qrAe50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة وتصاعد النيران من مقرات المعارضة الكردية في منطقة طاسلوجة بمحافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86688" target="_blank">📅 01:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=rsr1mBg9AOQd5TcAc5DCoviqVfAr0jV0tdopDfsbFogK7LFZy4Q4KPq0ns2V5ONFU6hP1hP6hCZXaIii9LhlF0K-K8ch9cpfXLat8yUT1CMjBn-TcJewo1Ws5PppMns6IXmiF0Yj2ODrt8I6xeKcnYyFFzc4aIDfTxz8ERLpB-C_KVQZsyrVrnRfkJsdnVCp-4Jk2rtNnRAoMzjqx9sGlElqY4N4BfEXbvzHm5P3zbyoaCu2ozkqDdVyunVocgAOXN3g3jldYmplRvkXmXGlgJjEkKe6GQ1WqxpPPPZ0Ioo--ZsWBz1F6KFVv9AEpWK08VypJ66yJd6krhtHZCCo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=rsr1mBg9AOQd5TcAc5DCoviqVfAr0jV0tdopDfsbFogK7LFZy4Q4KPq0ns2V5ONFU6hP1hP6hCZXaIii9LhlF0K-K8ch9cpfXLat8yUT1CMjBn-TcJewo1Ws5PppMns6IXmiF0Yj2ODrt8I6xeKcnYyFFzc4aIDfTxz8ERLpB-C_KVQZsyrVrnRfkJsdnVCp-4Jk2rtNnRAoMzjqx9sGlElqY4N4BfEXbvzHm5P3zbyoaCu2ozkqDdVyunVocgAOXN3g3jldYmplRvkXmXGlgJjEkKe6GQ1WqxpPPPZ0Ioo--ZsWBz1F6KFVv9AEpWK08VypJ66yJd6krhtHZCCo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86687" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko4elwKJxC0VHCujy4hv1Ee-VUWpq-nMYGIC1Z6WvhpI-QekxNRYEfveJv2bHlBWWMz-J997v-0b9h5zGsfJMLIXLEPut2vL1ccmPTYohjwYHsxUF-4z7YgpQwrKQpPv3Vd9Eo_fm8ssG1F4uwkmo4KacanaxaM9SZTTxP3PV0ZLr6zRwQbWoV7txjE4czduCZvG2hOKpatrAlfeJi22EMziU7_Bz_sWhVjS4KmCN3Rvj4CcuAAajBuABB91X-e7xO8N17MX1sCH5V2CpvGGusllq9-Hs7prhFVlSCAdgxg3p19NBM3Y9XSkmxk-05ocdg6TjdBsMVRCe8DmYGs8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86686" target="_blank">📅 01:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86685" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc7LFe1JxqufE8OfWNhfFrgw1bb4klwpEmPlzBVilRKL7R3D33nBPjbNKBc3SPRcFDbT3JobOOOmMISYxhQwj3HgqQQFBrSAU0a8a-j7Rh7B0pXIQozD7UH1RrXEPSi4BbnnhBoJP2g0i2PtyR4_xLrL-aB7mteNG0QS-2bTFhgm3l6PCy0a0jJqp4ftNXwxr7pOKWmmgjJG8UaAWU08P6oZR1Tozw8zN82b79lIYbLKrHTVvHjYGxJomm9fd2clxigCEqF3pASeyPi00YII4EBHO7UyXdMZo54dohYG6zChhwcRoUZ0ocdyKBsOkr3uNRr_T-_fBaHGhhoTIGbz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاثنين يوم الأحرار بموكب قادة النصر</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86684" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=ir5qRhoWU7cwXH14GTEk9rl1gjr8iHL3zw8zYffi6TQabsq3YUiEeM-_BCRvUmD-T3Qim0d4MyncxEWm6Ej7S8zh6P2NsOE2i5jrp0XxdCYWREU8P6e10BdoKq1n_BKZIK4CKzEBPu2iNfa5P5IZVEmsh8pS1yz1mps630hYOu3EQc-2S03nxHY_2k4juvnaSRiURvssnsuZWESbpXlD8p1lpAjyGIQQbDaWgYfd3qxyOBE8Hh9yoyXhhluSckQYE3SN4aiTEuZdOlIOx0A297iZu1hrJWQyEXbNTl_H1QBhlKK7ptpugHXa1Q3LZjRDfkYyXblVWrwQV9kln6qYzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=ir5qRhoWU7cwXH14GTEk9rl1gjr8iHL3zw8zYffi6TQabsq3YUiEeM-_BCRvUmD-T3Qim0d4MyncxEWm6Ej7S8zh6P2NsOE2i5jrp0XxdCYWREU8P6e10BdoKq1n_BKZIK4CKzEBPu2iNfa5P5IZVEmsh8pS1yz1mps630hYOu3EQc-2S03nxHY_2k4juvnaSRiURvssnsuZWESbpXlD8p1lpAjyGIQQbDaWgYfd3qxyOBE8Hh9yoyXhhluSckQYE3SN4aiTEuZdOlIOx0A297iZu1hrJWQyEXbNTl_H1QBhlKK7ptpugHXa1Q3LZjRDfkYyXblVWrwQV9kln6qYzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/86683" target="_blank">📅 01:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86682" target="_blank">📅 01:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86681">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=ga33yLf0YKLli7eUwbiP8XndrV3POgNsIxzMyoyEHjs8dYDt1euGylsMH1L4u6Utf2DD02j_3Q_8FfloGmop9pctaTdL05xNXv_BW178KNMr2Ajn08jSwT0JDMQ-FL1cVmjzDkRDjuLLbTvmzqM96_k42c-CWCUTr8WfFCbMdPRoM0Hdf0-ZoSqknrl_y5LqcmiGF8ItMuYWSI1TgYm_wtgkJ_oHq9hHsZ08KmSd_LpnELytdcqg-HYGTq6VRIaM_eme9cE8n1k4SRKmolcxDpTiEtr_0_03T136XdJgcLBJjfJWBmhiwS0DeqyzUO_oEU66iO6CTcGxPZ_HDy2tqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=ga33yLf0YKLli7eUwbiP8XndrV3POgNsIxzMyoyEHjs8dYDt1euGylsMH1L4u6Utf2DD02j_3Q_8FfloGmop9pctaTdL05xNXv_BW178KNMr2Ajn08jSwT0JDMQ-FL1cVmjzDkRDjuLLbTvmzqM96_k42c-CWCUTr8WfFCbMdPRoM0Hdf0-ZoSqknrl_y5LqcmiGF8ItMuYWSI1TgYm_wtgkJ_oHq9hHsZ08KmSd_LpnELytdcqg-HYGTq6VRIaM_eme9cE8n1k4SRKmolcxDpTiEtr_0_03T136XdJgcLBJjfJWBmhiwS0DeqyzUO_oEU66iO6CTcGxPZ_HDy2tqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/86681" target="_blank">📅 01:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86680">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=AgKm80moLQsjZihdq2B588X2QE3hZ7r_YPqkQEOur3t9ezTvF_ejzNK9i3pMY1x2mQgm0hAbIZAKLDdDpqxKcLMXOFnA_hNJL3hMEcDC9z0wp2PHBAJoz0D7TZEe3SYUd1zWC8f67FatafonaUEfu4QUnQG7XtnPsEwFSBZvVMuMa9zUbUkpeMQPtM7u_m0UKHwekAzs8GvqJqJKpkxVWQydvOCs6ELI5JP7tLL7YV2h7T_wDvKw4pXJVYqLvphsGgoVB2F81pSAsv45qbDgbMFnm914nVAIe-FBGETyBEXNOmahcVjs_ch8JkYrS_OIBb-1qJ9cxutYy8j5r1UyOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=AgKm80moLQsjZihdq2B588X2QE3hZ7r_YPqkQEOur3t9ezTvF_ejzNK9i3pMY1x2mQgm0hAbIZAKLDdDpqxKcLMXOFnA_hNJL3hMEcDC9z0wp2PHBAJoz0D7TZEe3SYUd1zWC8f67FatafonaUEfu4QUnQG7XtnPsEwFSBZvVMuMa9zUbUkpeMQPtM7u_m0UKHwekAzs8GvqJqJKpkxVWQydvOCs6ELI5JP7tLL7YV2h7T_wDvKw4pXJVYqLvphsGgoVB2F81pSAsv45qbDgbMFnm914nVAIe-FBGETyBEXNOmahcVjs_ch8JkYrS_OIBb-1qJ9cxutYy8j5r1UyOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قبل قليل بدأت مساجد محافظة كركوك برفع التكبيرات بالتزامن مع استمرار الهزات الأرضية التي تشهدها المحافظة منذ يومين وحتى الآن.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/86680" target="_blank">📅 00:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86679">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9b860706.mp4?token=Z_bc07GvOF4cTiclBOIN7ShjG-EY7fIM8jOSvFsA0mhw0kecGdMyReNfGrNKDItf4LFzipn6fki_EWETR-cauLR9pbyzBbKYviXn2s9HWegsyj7FUKzCyP_F3nd34LHEmgGwE49JNvzIraUby8iCtjtXAkvnn3iUslnq-ugRwEKr9WfYyEDAQoqpoPJ7vrAz6j7F1RTID7xJZ4ds3_BkZQCzlXFmMsYrmfZYZbf2mu5RRy5sCrCXZxxNEq8kM5zlFv1jAETh5u7tmS1vnTuc94KnXWv8DoWcFzhtzsEWB5l9WcUAQTI1_dhZu3k2WVg2-_m_ITy_9LECgPToJ94VEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9b860706.mp4?token=Z_bc07GvOF4cTiclBOIN7ShjG-EY7fIM8jOSvFsA0mhw0kecGdMyReNfGrNKDItf4LFzipn6fki_EWETR-cauLR9pbyzBbKYviXn2s9HWegsyj7FUKzCyP_F3nd34LHEmgGwE49JNvzIraUby8iCtjtXAkvnn3iUslnq-ugRwEKr9WfYyEDAQoqpoPJ7vrAz6j7F1RTID7xJZ4ds3_BkZQCzlXFmMsYrmfZYZbf2mu5RRy5sCrCXZxxNEq8kM5zlFv1jAETh5u7tmS1vnTuc94KnXWv8DoWcFzhtzsEWB5l9WcUAQTI1_dhZu3k2WVg2-_m_ITy_9LECgPToJ94VEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من أمام مرقد الإمام أبي عبد الله الحسين (ع) وسط توافد ملايين الزائرين لإحياء أربعينية الإمام الحسين (ع).</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/86679" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86678">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=MBr7ww6cLKJcXT57JOn43dFqYnrRptMHnyQiW73fYtdSi-KZdG4oj1ULO4F_dS3ug2nlM-TAaf0Enkf_yDZXAvP3OkgTpQl0g1bLmzhJ15H1e1ARQsr9JQCefIUdksGhtxu9A4D6k5GVXHRcmTKxKnbEuqm6zB3-Dl6RXzD4OWPiYfMlo2FoeaBDLWzN7nUoQHGDH1MOryuv57hoCXrYqs8egjHMUckDkXEELWtG8XbsgOUq04mCnzW7hoHf8ldD6Wk35kY6NVVkRrOV4SdycwRnaJ84a8IgBqHpe8cZNoMOPEGtyWvr0dZeUOROxdUqDOXS0Y_XGirU7ldwZfrnWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=MBr7ww6cLKJcXT57JOn43dFqYnrRptMHnyQiW73fYtdSi-KZdG4oj1ULO4F_dS3ug2nlM-TAaf0Enkf_yDZXAvP3OkgTpQl0g1bLmzhJ15H1e1ARQsr9JQCefIUdksGhtxu9A4D6k5GVXHRcmTKxKnbEuqm6zB3-Dl6RXzD4OWPiYfMlo2FoeaBDLWzN7nUoQHGDH1MOryuv57hoCXrYqs8egjHMUckDkXEELWtG8XbsgOUq04mCnzW7hoHf8ldD6Wk35kY6NVVkRrOV4SdycwRnaJ84a8IgBqHpe8cZNoMOPEGtyWvr0dZeUOROxdUqDOXS0Y_XGirU7ldwZfrnWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/86678" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86677">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/86677" target="_blank">📅 23:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odSJTA6Xm0TqagfCuXRinIG9gvFWkJm3rFpPyjQ1fJbdsnGpZ9y3th6w9Sm27sVopq7PDnKX8ixeycY6pdsaWCbyqMT963GzbYwTZTe2_T8Tq0Kr4KSVLAZgufDWNQ7rhkagBF3Xf-NV8g3FopVaoylfXETzI6VYk-gRvou3qRu6qDTFbRlOJfbHdQsb7l_Er_y4PvKHQo5pqOCmsiQuYQYkL1DjCddOOov9C7gEKaJQym-tN7KQta4QolD6_fsiff9PWHTub15giWCDNK6KlgTY7tMiNPrnz5QTA_bUpOkn-lvYmVSllja5Fhgu7RCt0emkqhGmWzB3bKyGWMLySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/naya_foriraq/86676" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/naya_foriraq/86675" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJqQtfpahUbZFolw_1_pRjNB-mSd51W7w_rUOiXcaoBOhJAQGIGFx882V-JMuALAtDaG5gHx35raIPxV_dRMk4pquT0CZOWzXytMV8nsVNUYnmbWf7Q7GgBwM8Cpa06ru27SPK-6tcETKhNj5mxiWBwOPbnrpUxs7kYbqxE2LJBqKo-DTcHXFCr-IQVIh2U6P3Ii95GTnOMMOz1p5pOwnXneL6GF-QoVrBXnRI33gfdWx75A0SlzEu4uYdky25MUh2caKbHo3LxiL2EbdvzDZn3oluXeDGWUKPOVrF2d1n3f6qbWKjqZsSsOuESOjzdhLToj97o_bM6phintvv5LlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
لقد كانت الولايات المتحدة واضحة: نحن نُقرّ بسيادة المغرب على الصحراء الغربية، وندعم مقترح المغرب الجاد والموثوق والواقعي للاستقلالية الذاتية باعتباره الأساس الوحيد لحل عادل ودائم.
أي مسار آخر يطيل أمد الوضع الراهن وهو غير مقبول. هذا الحل الذي هو ضرورة ملحة لن يجلب السلام إلى المنطقة فحسب، بل أيضًا الازدهار والتكامل الأكبر لجميع أفريقيا.
يجب أن ينتهي هذا الخلاف الآن، وستواصل الولايات المتحدة المضي قدمًا في تحقيق هذا الهدف.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/naya_foriraq/86674" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZFHQQkCO1lwhgwIEzPRE3rv-9xcRZDnTd3alpHea5x3XgwJUY30-H0QvucDv1eyFi8zuTat_ooMYMbj3tizZyyxSHehvftlZDz0js_94McS7W3LeBY_oPXOmmYV_NOtXhInDF-lyIXFKsmrtwSLO3kxD2CMv51RLuuiYBXJZLMBMXAR64UYQi6rUL63GxhQmN39oTWrJfzuW1MkJhIYmAwwn9jQg2672w__DrmuvX6KJCoKG7rFj8Lv2_Z43DyiCC4qtOqLdYaKGJrJ3SEXpb82ES4_rldg7EUKxjimd7711ajlh8K4z4CX4dFS2ukkuRygHQzAEBFEQcWMmfoV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fk9y9PfmAHSNp8MZpeF74RCJxoVpqrPS0BvU_T7uSa1i7xfgTJgHx5h5tG3y3EnvBzFUMFoB6z47jtAIfpJ3Y8jH3qq-EjAz0uRUHH3bbgsg1QccEbl-82fPzl3lTipsdj5oH0ESX0FlH4JDuYCrD2-tv8R4iY_qxsst7BtxzWClhMNoMZxz1-IxAc_7fpETYs5LuNna2cgGAkC4RO7PBgxkmIGr4L0juJ7Ehlfxoal2Re08lff3746EjhfUp04f3Fdqjubm9nXBpR9AUPYJ9lJw9V3yIK7pfuXgWw3Ye4UNAoAjMUcPIvVHW5B69pCWxgvSfhUxrl_w10wGaFUbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWkFGHlwAFZ_I5Wy0d0oGicUEokgYemaaDo6TxdtAdlqnEvAe1ZGcWxad3GA_N57kSNKXMqvuTQRkuALHnUh4WzIqpieD-BkvvTALARXfZZDuE9wmDVVQWGz6Ny4diVHzIL_B8am6suhW1PMu_uPaUxJ8BkZCxCXS1t7RtaVhfA2V_310J3MHod2ipJcK_J98wZ6FzW1cZ_JCFT3NxdnVrm1pe0dpQqSTrUBpxV8G40CxDxnKIWp9ATloIaNjLFd4wDPiFMRwwctAtVuL-a5PgkbIuSh4O5GMpkSM1oC3xXXZxywFW2G0_XjmIItuS6eNxUwudwPziYc26uvrJqH-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية: سنستخدم جميع الأدوات للدفاع المشروع عن حقوقنا وأمننا القومي
في بيان، أشادت وزارة الخارجية بالقوات المسلحة، وأكدت على استمرار الدفاع القوي عن كيان إيران في مواجهة التهديدات والهجمات غير القانونية من قبل الولايات المتحدة.
أعلنت وزارة الخارجية أن إيران، في مواجهة التعديات الأمريكية والإسرائيلية، ستستخدم جميع أدواتها للدفاع المشروع عن حقوقها ومصالحها وأمنها القومي.
اعتبرت الوزارة أن استمرار الحصار البحري، والتهديدات غير القانونية، والهجمات على البنية التحتية المدنية، تمثل "عملًا عدوانيًا" واضحًا وانتهاكًا لميثاق الأمم المتحدة.
أكد البيان أن صمت مجلس الأمن وجمود الأمين العام للأمم المتحدة في مواجهة هذه التعديات يتعارض مع المسؤوليات القانونية لهذه المؤسسات.
أشارت وزارة الخارجية، في إشارة إلى دور الولايات المتحدة في زعزعة استقرار مضيق هرمز وتصعيد التوترات، إلى أن الادعاءات المتعلقة بعبور السفن كانت بمثابة ستار لأعمال عسكرية وضغوط على إيران.
وأضاف البيان أن إيران، في حين تدين التعدي الأمريكي، تؤكد على الحفاظ على علاقات ودية مع جيرانها، ومواصلة الدفاع عن استقلالها وعزتها الوطنية وسيادتها.
﻿</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/naya_foriraq/86671" target="_blank">📅 22:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86669">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=OOUgs74LBt3txzl705VSV-eNc1zorAmncBAL-FZ-4CInJQVqTz33ub7sG0HMul9_ZGDNA6egO54hT85MkNCScIVYJu2EaK5ToySjV5qwQUWjBObkM_Ej4mDDU3riJgF1xCbeaer_884pWZovmZ_88gaotRm79T6hVhm0dv_wF-qlEzF_RW5EoCnAwf_TTvdwI62w3WGmvC7EqLXJ4zSrsno7-iOOw2ITFMB6803ALUzwGZfcxokij-2b_fF3QH8hQfi-4Fe3lXJFN6_iAt4zwnmFGSpOQQmaRgx9Urpjy4rXBWbN7iiJzQ8Ccz6PkUF2nPvO46WI8hi9i9eQ-mxvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=OOUgs74LBt3txzl705VSV-eNc1zorAmncBAL-FZ-4CInJQVqTz33ub7sG0HMul9_ZGDNA6egO54hT85MkNCScIVYJu2EaK5ToySjV5qwQUWjBObkM_Ej4mDDU3riJgF1xCbeaer_884pWZovmZ_88gaotRm79T6hVhm0dv_wF-qlEzF_RW5EoCnAwf_TTvdwI62w3WGmvC7EqLXJ4zSrsno7-iOOw2ITFMB6803ALUzwGZfcxokij-2b_fF3QH8hQfi-4Fe3lXJFN6_iAt4zwnmFGSpOQQmaRgx9Urpjy4rXBWbN7iiJzQ8Ccz6PkUF2nPvO46WI8hi9i9eQ-mxvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يواصلون زحفهم نحو مرقد حبيبهم ابي عبدالله الحسين(ع).</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/naya_foriraq/86669" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇨🇳
🇺🇸
روبيو
: أي صراع أميركي صيني سيكون كارثيا على العالم أجمع.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/86668" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
