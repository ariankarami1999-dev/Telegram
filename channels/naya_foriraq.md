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
<img src="https://cdn4.telesco.pe/file/UQ0ZApHPQRPVkFLegMYcbsbz9UOoAg1mz9k2UZa8gimmMOewpfsbw9slDlg_4CmKh-Euyk8IZVZpaywLHubeUY_UUDJuOH0J-t-5VsCK4pU5T78kth8D8GZwg0rHhNc8me3uj77t5nZT5iXazWbc1va9dyUg6Z0SVW_mqDFymzypgai3w0vZjvSBWFQPv1BpHRVjHlYNpvbtjYvGfj23xplnTjJWI7SJv5tI7eJvV4d4WoqMKgIML6aF623D-ifTEAG22po0X1wQ6NQofv5KSiZIMO-Tte2lt-EA_7ZteFtEv5dHWzBgXYbX1RSBL0dbzgBdmgrnzbz3XCcpz_g12Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 263K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 03:12:52</div>
<hr>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مشاهد متداولة لإنقضاض الصواريخ الإيرانية على القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/naya_foriraq/83097" target="_blank">📅 03:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e88ce3c.mp4?token=I3x2eW2KJh7pUpve_R0YfWRN0yh1WbX0564hYSO1TY2a6kyONyAHbKmpRuz128dfkRCo2r2O_lqzaaJTNSlnwCaoKGPFYvAJfbyWmNNF5Zq7zNz22Y1i7m-CN2zSIC8SBLe1LNj743UHUg4PUXC2ely8oH-Cx-KrtQDxE_DYg89NefL3qVHW34GwTlAgl-R7bottewtSf9KSaO54l6X_U2GIRWvF_I_7Ce6zraKTgMA1WCZWoyj2A5I68xnaYhcayJoxlw6wt21VHFcjfo6ZDccUmOyN-q10nej7PqlyyhoU1zKfmcSrJR8GZ-MkgYO_u14IQ7YmlJ8mVvB8I6kkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e88ce3c.mp4?token=I3x2eW2KJh7pUpve_R0YfWRN0yh1WbX0564hYSO1TY2a6kyONyAHbKmpRuz128dfkRCo2r2O_lqzaaJTNSlnwCaoKGPFYvAJfbyWmNNF5Zq7zNz22Y1i7m-CN2zSIC8SBLe1LNj743UHUg4PUXC2ely8oH-Cx-KrtQDxE_DYg89NefL3qVHW34GwTlAgl-R7bottewtSf9KSaO54l6X_U2GIRWvF_I_7Ce6zraKTgMA1WCZWoyj2A5I68xnaYhcayJoxlw6wt21VHFcjfo6ZDccUmOyN-q10nej7PqlyyhoU1zKfmcSrJR8GZ-MkgYO_u14IQ7YmlJ8mVvB8I6kkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الصواريخ لمنظومة الباتريوت أطلقت لصد الهجوم الصاروخي الإيراني الكبير على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/83096" target="_blank">📅 02:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عدوان امريكي على مدينة دهلران ضمن محافظة إيلام بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/83095" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f92e4c2a.mp4?token=TJt09IYO4Ba50C739n8ejJyT8Qf_xd-WclpgVDpCKq4fNaTJFDum5BqUT6xQ1l3HUGnKWJp2QFfpPCAxCyNP8ItXkisjs807KJ65ByP8kMEoupC-FFVWiL4lluQciJBXrt5lG_cP50vaKuCVZFuvydAS7PkaMpEiWk6zymLkBbmDLq5IIsRd9AYFUoICyl0_hpt-hNTGAw1ge0rjnW6NC69i6VM4NqM0WBjaTbk_-G-U_2we1DfmQ0y4Na5yHTEOemVQAhPupTMtYvXACoiVXqlJjEDNZLomSWGPHmNQBolktf5aVeaB3z2qQplYu1yMWtkW2HQERoYu8yShh6cn06yogpxbWMKgo9Um6QWc1p_8eEcUTb8Kh4rN5rxc9sweRBwvSRrpPhdLRMRVmrxSZ7K2jnPqVuUroocSPizmZ1UUhoZE7zoNqykMDoRncB0lCBHbs5wY3YJa4QuDuBx0PwiUzFqsu4Sw8eMdO_haK00TxAg_mkhTV3b6aY-__SEHwPkMFEjZFfTZpRNaM14X9ZsUUsEleRmYZ7JqNjAx0i-X2EsPOXq7iEpff7StNeK6M3UWWiseJ--9vSzVi0qvN32KFm-nmA4J0WrwG2nVxWIYrD9VdS6klSTB5sR-Bm4hY0nr7HiicH42HUcRmnOV09R0tKQ_U8yW5QVQNrrhjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f92e4c2a.mp4?token=TJt09IYO4Ba50C739n8ejJyT8Qf_xd-WclpgVDpCKq4fNaTJFDum5BqUT6xQ1l3HUGnKWJp2QFfpPCAxCyNP8ItXkisjs807KJ65ByP8kMEoupC-FFVWiL4lluQciJBXrt5lG_cP50vaKuCVZFuvydAS7PkaMpEiWk6zymLkBbmDLq5IIsRd9AYFUoICyl0_hpt-hNTGAw1ge0rjnW6NC69i6VM4NqM0WBjaTbk_-G-U_2we1DfmQ0y4Na5yHTEOemVQAhPupTMtYvXACoiVXqlJjEDNZLomSWGPHmNQBolktf5aVeaB3z2qQplYu1yMWtkW2HQERoYu8yShh6cn06yogpxbWMKgo9Um6QWc1p_8eEcUTb8Kh4rN5rxc9sweRBwvSRrpPhdLRMRVmrxSZ7K2jnPqVuUroocSPizmZ1UUhoZE7zoNqykMDoRncB0lCBHbs5wY3YJa4QuDuBx0PwiUzFqsu4Sw8eMdO_haK00TxAg_mkhTV3b6aY-__SEHwPkMFEjZFfTZpRNaM14X9ZsUUsEleRmYZ7JqNjAx0i-X2EsPOXq7iEpff7StNeK6M3UWWiseJ--9vSzVi0qvN32KFm-nmA4J0WrwG2nVxWIYrD9VdS6klSTB5sR-Bm4hY0nr7HiicH42HUcRmnOV09R0tKQ_U8yW5QVQNrrhjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لمنظومة الباتريوت أمام الهجوم الصاروخي الإيراني الواسع على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/83094" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71daef6e3a.mp4?token=VKbwhAGV_2BpaG_jveHrQMliyZ9DhpZ67J-Qmw7Z4ZWKOKuyS0-JLLzBuXIMLyJRlfWVd8noGxj99eXJ95HmSaYqP1NA1fgv7WJAW7i29BpVUSM1U_4iBgk7QguG6TFb4K3gxw1WODWUA_cyzxIfmVs1zwHKZS3DUs6DNkYZYemBZJ-sSUltJH-tJdCHfwtDw-UoMFvj3zs2HmOfOeBl_E_vHUMHOhFW-ub_8HxqnYamiYB3J7CeqiBO9zGEbkaX0N9IgKY4mpfI0pW-7a4-b5R3lay9AhTE6tqkRq1ecyIfVIKOVpQsAkqtAvjkjcFGFSTFA-G8dTyT6AvZIUuEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71daef6e3a.mp4?token=VKbwhAGV_2BpaG_jveHrQMliyZ9DhpZ67J-Qmw7Z4ZWKOKuyS0-JLLzBuXIMLyJRlfWVd8noGxj99eXJ95HmSaYqP1NA1fgv7WJAW7i29BpVUSM1U_4iBgk7QguG6TFb4K3gxw1WODWUA_cyzxIfmVs1zwHKZS3DUs6DNkYZYemBZJ-sSUltJH-tJdCHfwtDw-UoMFvj3zs2HmOfOeBl_E_vHUMHOhFW-ub_8HxqnYamiYB3J7CeqiBO9zGEbkaX0N9IgKY4mpfI0pW-7a4-b5R3lay9AhTE6tqkRq1ecyIfVIKOVpQsAkqtAvjkjcFGFSTFA-G8dTyT6AvZIUuEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء الأردن</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/83093" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b68417221.mp4?token=hT7BJiHXpUESMr6Zn5YQXunIWqpYno1K7Cq0YPfAv2TAoh9MeC3uftvIEc7LUjdH4bavMeLxsRtTaT6C-2PV7JXx8ruMAcYd_FVCXTEj3OHSo6vojBf2gXtpnk1N1iwqvVXCaaXN6c1CTr6Abx7DLjEzobtIx-TKf1Vzjarel6JeUlyh3hPTXYUhuJ_DW74hAkOz_FxzDrIBB0WnOaQ65PIioq0dNE03XbRdL-fcTjy-3Pt19UF-anBki_FwowFqWsuG8xEElWkvGpn6A75hhJYbbOnv-RYCQn4ork2Ut4GVEePsRwUWKzArSmAiHFtRIUuwUEufrla6HnAdFFz-pTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b68417221.mp4?token=hT7BJiHXpUESMr6Zn5YQXunIWqpYno1K7Cq0YPfAv2TAoh9MeC3uftvIEc7LUjdH4bavMeLxsRtTaT6C-2PV7JXx8ruMAcYd_FVCXTEj3OHSo6vojBf2gXtpnk1N1iwqvVXCaaXN6c1CTr6Abx7DLjEzobtIx-TKf1Vzjarel6JeUlyh3hPTXYUhuJ_DW74hAkOz_FxzDrIBB0WnOaQ65PIioq0dNE03XbRdL-fcTjy-3Pt19UF-anBki_FwowFqWsuG8xEElWkvGpn6A75hhJYbbOnv-RYCQn4ork2Ut4GVEePsRwUWKzArSmAiHFtRIUuwUEufrla6HnAdFFz-pTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شمال شرق الأردن</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/83092" target="_blank">📅 02:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=bwVy2-HfCagAm1ra3Jws1ShIup9CMUthp3gexPiBgTqoHGnBCMtWeVTD2VfOA4BIRA3d1h3F1NGfRTeCG1f9LaLC7aceDUSm8W9hC4mfcoeMbiK2M0TMfy0Hx62fd1T62jNCJt0bRU9YkmgYzSBL4NVq8Lxk0_U71lXkSmadDLOG2fjHm6dxNGuIIQE8Jhzc0kE7m6RURos9DCUYY0wSvC4nzG4EiaRe-Lwc17io94Hr1Zp1AreEvSl6TxcyvPjDxSgSj2BbiO3GgL6SfnzJsXI-xUe2cUHn2pRdNswBblAnKdT1XmVxRxYDjfLkMyXyI17WhvQxhg7iXI2KillPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=bwVy2-HfCagAm1ra3Jws1ShIup9CMUthp3gexPiBgTqoHGnBCMtWeVTD2VfOA4BIRA3d1h3F1NGfRTeCG1f9LaLC7aceDUSm8W9hC4mfcoeMbiK2M0TMfy0Hx62fd1T62jNCJt0bRU9YkmgYzSBL4NVq8Lxk0_U71lXkSmadDLOG2fjHm6dxNGuIIQE8Jhzc0kE7m6RURos9DCUYY0wSvC4nzG4EiaRe-Lwc17io94Hr1Zp1AreEvSl6TxcyvPjDxSgSj2BbiO3GgL6SfnzJsXI-xUe2cUHn2pRdNswBblAnKdT1XmVxRxYDjfLkMyXyI17WhvQxhg7iXI2KillPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شمال شرق الأردن</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/83091" target="_blank">📅 02:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c912aa903b.mp4?token=bHd2rJ_CFrTNLXh2TxHytdR1gkYPFH-Fw9Uvg2-ujKVtB4BPA-VxHADbtdkBIa8pD34689xuiZaS4nHYQl0rqpr4rUbfuvFz48yiisLlc24pTt2aj3bpsCgb8ipP6CGHfwFa31Iu8u1WsZlUr0qG8QwvfYKpjGbaxt5lyyXX9q8bKeOUj6p-n5vyfYhejpQ3RL5a1O3zEbumxGOLQjz71l5fLb__rlBnw7l82EF48y9_LwpxQhw1xdAGbvwllugj5hNMtnbuTeXsQJZ1YSVkRMpYhrQsrc-EWP9YQP5rvilqPYfgKf65cGXj0Ect09mzhqqhWC1qL-CCizgBktTZ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c912aa903b.mp4?token=bHd2rJ_CFrTNLXh2TxHytdR1gkYPFH-Fw9Uvg2-ujKVtB4BPA-VxHADbtdkBIa8pD34689xuiZaS4nHYQl0rqpr4rUbfuvFz48yiisLlc24pTt2aj3bpsCgb8ipP6CGHfwFa31Iu8u1WsZlUr0qG8QwvfYKpjGbaxt5lyyXX9q8bKeOUj6p-n5vyfYhejpQ3RL5a1O3zEbumxGOLQjz71l5fLb__rlBnw7l82EF48y9_LwpxQhw1xdAGbvwllugj5hNMtnbuTeXsQJZ1YSVkRMpYhrQsrc-EWP9YQP5rvilqPYfgKf65cGXj0Ect09mzhqqhWC1qL-CCizgBktTZ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة اخرى انطلقت الان نحو الاهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/83089" target="_blank">📅 02:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/83088" target="_blank">📅 02:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/naya_foriraq/83087" target="_blank">📅 02:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52fd640.mp4?token=vaW_fZr0q3A24hS9nukORDOcLJ5L6t6vcRAcYd-vpeqk-y8ZlxZ4ezzdjW_iO1V_TNmVtzx3H89frj_SpQm5eH9D48C1QG6WUZRp1sbpjiNLs0wpmIvNzIge48hc1loEZvywiUIeqMG5NN7INfpvgl7jAenpFlZvOe_PTJ17loP8cgHJsjOgGysgEj7588q2eI8ZRGR-_vpUX-IEB3FuZ3_12weBFHSRHM1QvmoJyoMYu9yCt1OMmlrpoy4ZiXvrhxZJ3A91LV0IqgPkJOeg9qVSzQETKamfrBH24vwpMnMy02_zlRS_Hje_fSKGpIjWDvz4XFzAE6_SkYiKBaUCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52fd640.mp4?token=vaW_fZr0q3A24hS9nukORDOcLJ5L6t6vcRAcYd-vpeqk-y8ZlxZ4ezzdjW_iO1V_TNmVtzx3H89frj_SpQm5eH9D48C1QG6WUZRp1sbpjiNLs0wpmIvNzIge48hc1loEZvywiUIeqMG5NN7INfpvgl7jAenpFlZvOe_PTJ17loP8cgHJsjOgGysgEj7588q2eI8ZRGR-_vpUX-IEB3FuZ3_12weBFHSRHM1QvmoJyoMYu9yCt1OMmlrpoy4ZiXvrhxZJ3A91LV0IqgPkJOeg9qVSzQETKamfrBH24vwpMnMy02_zlRS_Hje_fSKGpIjWDvz4XFzAE6_SkYiKBaUCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية كبيرة انطلقت من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/83086" target="_blank">📅 02:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/83085" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/83084" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd162e5ca7.mp4?token=b5xmV2GWYPlwo9ZOMRdodlnaSFNLi7CdnVufGwFQHUg5O-krQwbeCpq_pAOzPK5DM6tpJVnw561Bjh-gerGCqmlL9F5lgat4KjJi3-S5JyTaZDdrQwyD7JtRwvp32Iclr1U1thrU1JCQxxL0ERNQjPDJAJgr8JK6JVgg3eDjVrkomji_DAfy3MobCoprCaBC9uo6pqyZGwwt1nl1a5m_sO909_8RzwwIMP5lnr4WBdYaejfBqgrOYrcGFMKAgGsK4o0uqLkCAMeUDgbmkxmvazLqBGptiBqjXhp8w_1gQskF0ugcwzDkIFki5hOhECgpLePsE5zVCx-EEzAbFWeYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd162e5ca7.mp4?token=b5xmV2GWYPlwo9ZOMRdodlnaSFNLi7CdnVufGwFQHUg5O-krQwbeCpq_pAOzPK5DM6tpJVnw561Bjh-gerGCqmlL9F5lgat4KjJi3-S5JyTaZDdrQwyD7JtRwvp32Iclr1U1thrU1JCQxxL0ERNQjPDJAJgr8JK6JVgg3eDjVrkomji_DAfy3MobCoprCaBC9uo6pqyZGwwt1nl1a5m_sO909_8RzwwIMP5lnr4WBdYaejfBqgrOYrcGFMKAgGsK4o0uqLkCAMeUDgbmkxmvazLqBGptiBqjXhp8w_1gQskF0ugcwzDkIFki5hOhECgpLePsE5zVCx-EEzAbFWeYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بزن که خوب میزنی</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/83083" target="_blank">📅 02:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=PibFFPPeNREpPFhb1uB-fEWs9qF_Na_xgJA-2haA656jkvBDmA9y6kCcVY08l8X4UMxnkOa4uskWB6izNI-RhzRqZ55Q2PCWFDhzZhSIi08Y1WtSi1ErwX8qiAbhfYCCR5OyXjRpI74KikLVw0_0FDsY04GZ3dpSFimgJjZPrHJuBMWmSyKAC5HMQT00CoDYr5Owl6U6Kup-NVGX2nWs_ACabqZfngB3hx2wh73i93yNunIWtAlVw0CD9_BVkR4w1RdN8TrKq9wT3tZ36xWR887dSTfBdN_X4Xq9EWiv1PoK2hHWgYNP_DmqRrQDzYfN9TjLSilq7DpqSJYa2rMRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=PibFFPPeNREpPFhb1uB-fEWs9qF_Na_xgJA-2haA656jkvBDmA9y6kCcVY08l8X4UMxnkOa4uskWB6izNI-RhzRqZ55Q2PCWFDhzZhSIi08Y1WtSi1ErwX8qiAbhfYCCR5OyXjRpI74KikLVw0_0FDsY04GZ3dpSFimgJjZPrHJuBMWmSyKAC5HMQT00CoDYr5Owl6U6Kup-NVGX2nWs_ACabqZfngB3hx2wh73i93yNunIWtAlVw0CD9_BVkR4w1RdN8TrKq9wT3tZ36xWR887dSTfBdN_X4Xq9EWiv1PoK2hHWgYNP_DmqRrQDzYfN9TjLSilq7DpqSJYa2rMRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية إيرانية تنطلق الأن نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/83082" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر
موجة صاروخية إيرانية تنطلق الأن نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/83081" target="_blank">📅 02:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">المراسل: تُظهر بيانات الشحن أن عشر سفن فقط عبرت مضيق هرمز يوم الاثنين، أي أقل من 10% من العدد المعتاد. عندما تقولون إن المضيق مفتوح، فماذا تقصدون؟  ‏ترامب: حسنًا، الأمر مفتوح إذا أراد الناس المرور به. نحن نبتكر بدائل رائعة، بما في ذلك تكساس وألاسكا.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83080" target="_blank">📅 02:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هجوم يدك الكويت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83079" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83078" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83077" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الدفاعات الجوية تنشط في بوشهر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/83076" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8892fff190.mp4?token=VZfH2zyjJBBuXhuht9y6C8SEaVpqDEYyeF1B__74GE111h_c1EikTbDh4V_zzv3H5i98ERFfIKxOAgbjCICjCVuFj6PtqZBdHaBcG6IBjy4Rxd2l2MxtgQcFT_ZFyTqvY9PYKL4Aj3jLvhD4JWRrwoJP__qrRlt1FJp4x49ySjGnW6GNMqZQtyFbXrWDjgmVvIqRuO3iYYyHhkj5eqhr5k4PZ4GjV5INYzkgBdn6AZ64e0TUjgppkOrXKEUWRm8NgoCXDmGLxJj8oEipcv3VTdKVG5h_YwJgtqnuAHdUF1YKUpYPHKwwCb42dVJsjCxKVS1CA1vp0Urk57_o2hhuZ5fUOWfKHBj70xx38nwzTtIHSp0Z1wlsQoreAbzWcuGoBOg4z7TKadUCPPUStNLdYcdsblww5S9ZyKl1dRPRvcAMJQPX91ByngtLdK4yZUTPOQY2zEaP6skOx8-T1nY-vCkkeRizOAQB9iSJy21TjkCMOFNn5WXF3m8JLsfuBBwQV0eFW0b0R-Jz2wh_lVyaTZRXgREvA1ZMyyPd3ZKAj2sNHxLytH3zFnoB7ChaLUIQU8Q7sPk4x6O1_2CvZhtIgVh2kwM47XollEOCbHUhdxerKnyBfc4bDKKVtwm0OhIvBVFxxEyRj-awatzHXQGhEWMg6bSLlzMgzvYrQriDOjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8892fff190.mp4?token=VZfH2zyjJBBuXhuht9y6C8SEaVpqDEYyeF1B__74GE111h_c1EikTbDh4V_zzv3H5i98ERFfIKxOAgbjCICjCVuFj6PtqZBdHaBcG6IBjy4Rxd2l2MxtgQcFT_ZFyTqvY9PYKL4Aj3jLvhD4JWRrwoJP__qrRlt1FJp4x49ySjGnW6GNMqZQtyFbXrWDjgmVvIqRuO3iYYyHhkj5eqhr5k4PZ4GjV5INYzkgBdn6AZ64e0TUjgppkOrXKEUWRm8NgoCXDmGLxJj8oEipcv3VTdKVG5h_YwJgtqnuAHdUF1YKUpYPHKwwCb42dVJsjCxKVS1CA1vp0Urk57_o2hhuZ5fUOWfKHBj70xx38nwzTtIHSp0Z1wlsQoreAbzWcuGoBOg4z7TKadUCPPUStNLdYcdsblww5S9ZyKl1dRPRvcAMJQPX91ByngtLdK4yZUTPOQY2zEaP6skOx8-T1nY-vCkkeRizOAQB9iSJy21TjkCMOFNn5WXF3m8JLsfuBBwQV0eFW0b0R-Jz2wh_lVyaTZRXgREvA1ZMyyPd3ZKAj2sNHxLytH3zFnoB7ChaLUIQU8Q7sPk4x6O1_2CvZhtIgVh2kwM47XollEOCbHUhdxerKnyBfc4bDKKVtwm0OhIvBVFxxEyRj-awatzHXQGhEWMg6bSLlzMgzvYrQriDOjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب: سنستهدف جميع جسورهم ما لم يوافقوا على العودة إلى طاولة المفاوضات</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83075" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">المراسل: ‏هل ما زلتم تنوون السيطرة على جزيرة خرج؟  ترامب: لا يمكنني أن أقول ذلك لكم، لأن ذلك سيكون تصرفًا غير حكيم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83074" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b83e24c62.mp4?token=W7Jv3NFJ3eCiNqzImcEFJriJQvHdRNgTh-DJDYtS6LJDrvIyUbUXHY87x2olJ64fmx4tA0EJCjg3qP2YShvsGtsLWmR-gvC-9eAbwjZ1MZGHKOnkV4j8KIgK2p7XYzhleHS1ToK8zTgKYd7plTiw3AaY39SIfZnZFXQrR12R7XrRew9OTy1nhwQ8TYH8Q7V4_1tfLN73QC72QU_lfJgweXoEtx0QGI1_quTOVC5MgPG-jBLEK2N2K0z_R_9jE6EtJ3qKLEGFbIeyPGJ6z-3kbgpTZzC7BPW38yXx6f8VCTmNOsVwOs4Mj_qMtpQG6585bwftmIsxTO132fKZVxX13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b83e24c62.mp4?token=W7Jv3NFJ3eCiNqzImcEFJriJQvHdRNgTh-DJDYtS6LJDrvIyUbUXHY87x2olJ64fmx4tA0EJCjg3qP2YShvsGtsLWmR-gvC-9eAbwjZ1MZGHKOnkV4j8KIgK2p7XYzhleHS1ToK8zTgKYd7plTiw3AaY39SIfZnZFXQrR12R7XrRew9OTy1nhwQ8TYH8Q7V4_1tfLN73QC72QU_lfJgweXoEtx0QGI1_quTOVC5MgPG-jBLEK2N2K0z_R_9jE6EtJ3qKLEGFbIeyPGJ6z-3kbgpTZzC7BPW38yXx6f8VCTmNOsVwOs4Mj_qMtpQG6585bwftmIsxTO132fKZVxX13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل يمكن تحقيق أهدافكم من خلال حملة جوية فقط، أم أن ذلك يتطلب عنصراً برياً؟  ‏ترامب: حسناً، أعتقد أنها اكتملت الآن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83073" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341826e3a1.mp4?token=BU_K3izNnegM8GOx2dmNVRY-wDSW-ob-yiWZzCn128VkjFhM5onl0XkqZr0wy0f79af4-_U6YJ0TABKHqXSBW2sV26UOZzRRkClaLTSPmJ2M3zKyxYjmZ-he3VYx7JXve1l2iFduBURzExOEz15QnjcPUdlvtM70eQFFdtdn8sT4t_RvMdvibREV9SgXhs9w6ZW2lyJzpTx8jWv1W-atWF47HK4NtJlYZlwuYFi24--us4DUy-pEFCUAv_s0Too9lf7JAIE6mMKtkubmAHCbI7sZRfvxh8AWjOuZs9MAHnu1OPppE7AQVNq0vVtcfHR3goMrlxlaGQtX3DeFKF390A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341826e3a1.mp4?token=BU_K3izNnegM8GOx2dmNVRY-wDSW-ob-yiWZzCn128VkjFhM5onl0XkqZr0wy0f79af4-_U6YJ0TABKHqXSBW2sV26UOZzRRkClaLTSPmJ2M3zKyxYjmZ-he3VYx7JXve1l2iFduBURzExOEz15QnjcPUdlvtM70eQFFdtdn8sT4t_RvMdvibREV9SgXhs9w6ZW2lyJzpTx8jWv1W-atWF47HK4NtJlYZlwuYFi24--us4DUy-pEFCUAv_s0Too9lf7JAIE6mMKtkubmAHCbI7sZRfvxh8AWjOuZs9MAHnu1OPppE7AQVNq0vVtcfHR3goMrlxlaGQtX3DeFKF390A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل ستستمر هذه الإضرابات؟  ‏ترامب: سيستمرون حتى أقول كفى. لديهم روح قتالية. الأمر أشبه بملاكم عظيم، تظن أنك هزمته، ثم فجأة يعود ويمنحك فرصة. ما زال لديهم بعض العزيمة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83072" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0517ad85.mp4?token=gwCfSjJX6le5ajRYl17QebX-SPY-Rvn7Um5ms1V_F39MB8onwdG-UiBhcYKt0J2pcYQ_CFmfnQrPFsGbXVMYm7BmJNIw0S6VUN03dh_56i8B1ENaPsxE0f5hP_zab2oaed4wd83kf-ARm8SOkfcV2Azpij0RC1SgIb-jVljb_hslhRAA8D5M6DZHbLNGh7DbzW6-CvyjbSA2Pz6oKS6QLgy3pttc4OgPP4_mNW6Owu8Tjkz4EkawbNKkXgoGJ1cA5ghdnlIv68oV2nEBPWIdbvDG2BxBbEaeiKULAQqQUWn8NC1mkh7d8gBGWdUYE95eHG8jU6MeDEnlxtorstH0IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0517ad85.mp4?token=gwCfSjJX6le5ajRYl17QebX-SPY-Rvn7Um5ms1V_F39MB8onwdG-UiBhcYKt0J2pcYQ_CFmfnQrPFsGbXVMYm7BmJNIw0S6VUN03dh_56i8B1ENaPsxE0f5hP_zab2oaed4wd83kf-ARm8SOkfcV2Azpij0RC1SgIb-jVljb_hslhRAA8D5M6DZHbLNGh7DbzW6-CvyjbSA2Pz6oKS6QLgy3pttc4OgPP4_mNW6Owu8Tjkz4EkawbNKkXgoGJ1cA5ghdnlIv68oV2nEBPWIdbvDG2BxBbEaeiKULAQqQUWn8NC1mkh7d8gBGWdUYE95eHG8jU6MeDEnlxtorstH0IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إذا نظرتم إلى مضيق هرمز، فسنجد صعوبة في تحديد أي مكان لهم فيه. علينا إيقاف ذلك. علينا إبقاء المضيق مفتوحًا. كنتُ أنوي فرض رسوم، لكنهم يفضلون إنفاق أموال طائلة في الولايات المتحدة، وهو أمر أفضل بصراحة، لأنني لا أؤيد فكرة فرض رسوم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83071" target="_blank">📅 01:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: ‏سيتم تأجيل أهداف الطاقة في إيران إلى النهاية.  سنضرب إيران بقوة الليلة وغدا وبعد غد وسنستهدف في المرحلة النهائية محطات الطاقة والجسور.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83070" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b7d12355.mp4?token=vFTSKu100dX-uKpHeS54IjbCEWWdtNhrw6K_SSGdzc5koFSlcnHQGGvqRfdCBjsyPjcSF1NBeg9H7hHvgW47hcnsU-JVgDQGpOy1dsXk7l88ZP_8akJclkPpCRO3NG1Sv2E7eBxHfl9CFh3-QZWGWRhRnHoJXy14oKCV5WJ13pDq89t8lCGflP0exxSwsOZGiOxAj_HN-1kW_bh6Tqz9Ns92nLT3Sd0jxETMETuplYSWxakmxXxrGiy-hcsXw96lY92CybOg1WBS3Ukz67d1NDr8FAT72bCEpqA-0dEmSZO9fKUCZAQGlLbs5yu-06QfxS4KwU8ij6A7dCTJ9AwHGx9j1ji9RPf6jlVef_JNEQfdCOvFBIr4iiRjJGYqZDQBqLUFTzeXNRvzffyd_HeswDspUMImJ9_TMKDp87KQfYGLJTZ3BWsJnGKMCgTAJMv5CJ1jyvjdzUUSeiLUpc3Bh7TFtEu1_dIjXKFDzV-B5olGHdV2pAeaKJVbPVzUc_XK2F2bsYKPfkMQzY_H93C_lo72qPcByL5szbKzq04MNmLdJGY06X29K3HRbvzA5zbDPUPoEkdh-_e7qxKY3wYhrqTK1T4jbueuSOgLFiWrbi-3w8QlEnX0n4psYsvZo60ryrxjfdD_8ER23qeYt7va_AmbQdvhe6H8RcYdod5DlqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b7d12355.mp4?token=vFTSKu100dX-uKpHeS54IjbCEWWdtNhrw6K_SSGdzc5koFSlcnHQGGvqRfdCBjsyPjcSF1NBeg9H7hHvgW47hcnsU-JVgDQGpOy1dsXk7l88ZP_8akJclkPpCRO3NG1Sv2E7eBxHfl9CFh3-QZWGWRhRnHoJXy14oKCV5WJ13pDq89t8lCGflP0exxSwsOZGiOxAj_HN-1kW_bh6Tqz9Ns92nLT3Sd0jxETMETuplYSWxakmxXxrGiy-hcsXw96lY92CybOg1WBS3Ukz67d1NDr8FAT72bCEpqA-0dEmSZO9fKUCZAQGlLbs5yu-06QfxS4KwU8ij6A7dCTJ9AwHGx9j1ji9RPf6jlVef_JNEQfdCOvFBIr4iiRjJGYqZDQBqLUFTzeXNRvzffyd_HeswDspUMImJ9_TMKDp87KQfYGLJTZ3BWsJnGKMCgTAJMv5CJ1jyvjdzUUSeiLUpc3Bh7TFtEu1_dIjXKFDzV-B5olGHdV2pAeaKJVbPVzUc_XK2F2bsYKPfkMQzY_H93C_lo72qPcByL5szbKzq04MNmLdJGY06X29K3HRbvzA5zbDPUPoEkdh-_e7qxKY3wYhrqTK1T4jbueuSOgLFiWrbi-3w8QlEnX0n4psYsvZo60ryrxjfdD_8ER23qeYt7va_AmbQdvhe6H8RcYdod5DlqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سيتم تأجيل أهداف الطاقة في إيران إلى النهاية.
سنضرب إيران بقوة الليلة وغدا وبعد غد وسنستهدف في المرحلة النهائية محطات الطاقة والجسور.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/83069" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
اطلاق صاروخ ابو مهدي من بحرية الحرس الثوري في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83068" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873fe56864.mp4?token=UDIdGybOBnWwFpUj6gPnIVr1ApSzzkihVEunn6fQNLDVuDrCoq0i14RnZ92lF0ICvJFupNEG2WvlKfgwKonmPeR1NMx_E_SqaPmBp56MNezlTGL7TKD4l8VtdOlLwKp-HDuRTP4Tw1Wg5DSIpmM3XhweWhGGDbvmwUyIjyy43jgex2fU2elJFDYOoUfeDsMEu1h7djxIzAHqK0o8ac4dZsO75MLpAkXypQOkGM44CmzhUsxn-BfPujg0Qinzz_KW3P2VWp5UXmKu29YGoyJBV5VcCa2mx_o7_ZZXpS89UYBjt7TSfA_eQQAdhMdgOCqeRS7LhYdxKLQ-APXfHCf1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873fe56864.mp4?token=UDIdGybOBnWwFpUj6gPnIVr1ApSzzkihVEunn6fQNLDVuDrCoq0i14RnZ92lF0ICvJFupNEG2WvlKfgwKonmPeR1NMx_E_SqaPmBp56MNezlTGL7TKD4l8VtdOlLwKp-HDuRTP4Tw1Wg5DSIpmM3XhweWhGGDbvmwUyIjyy43jgex2fU2elJFDYOoUfeDsMEu1h7djxIzAHqK0o8ac4dZsO75MLpAkXypQOkGM44CmzhUsxn-BfPujg0Qinzz_KW3P2VWp5UXmKu29YGoyJBV5VcCa2mx_o7_ZZXpS89UYBjt7TSfA_eQQAdhMdgOCqeRS7LhYdxKLQ-APXfHCf1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في محافظة الرقة السورية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83067" target="_blank">📅 01:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83066" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ملاحم تخوضها بحرية الحرس الثوري في مضيق هرمز</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83065" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الانفجارات المسموعة في سيريك صادرة عن اشتباكات بحرية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83064" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بندر عباس وسيريك تتعرض لعدوان اميركي غاشم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83063" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62545ed33.mp4?token=MALWnDP9eTPdcMQnBjwBEge1TysFOoOXvIxcLQfAG4_zVYTezvbbOuDi9qhVKS26bJ_JjM1hr8ZB2SXRAjWna0efFqjtKDKreJ_7uPb414F1HtI_1AZKeBmyalEdZNZMY3D7VSamC79Y6625ENARZtA9aEMEuzfE5l5UEU5zp2PjDHqr8XKgTPsJX4I95UoA6mmMU1XRTSx2qziVPFjoaVSp0OdmQrni3tUBtr1sHvToxOK1jvMmRaPCO2PzvyK_3lyirk8aBh5o9ewuzPnIMQKOSrdzKGen0NJSyXjOLsvib8d2LJWlMnd64B_agakguX9gw562Aesz8mYaGYhBmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62545ed33.mp4?token=MALWnDP9eTPdcMQnBjwBEge1TysFOoOXvIxcLQfAG4_zVYTezvbbOuDi9qhVKS26bJ_JjM1hr8ZB2SXRAjWna0efFqjtKDKreJ_7uPb414F1HtI_1AZKeBmyalEdZNZMY3D7VSamC79Y6625ENARZtA9aEMEuzfE5l5UEU5zp2PjDHqr8XKgTPsJX4I95UoA6mmMU1XRTSx2qziVPFjoaVSp0OdmQrni3tUBtr1sHvToxOK1jvMmRaPCO2PzvyK_3lyirk8aBh5o9ewuzPnIMQKOSrdzKGen0NJSyXjOLsvib8d2LJWlMnd64B_agakguX9gw562Aesz8mYaGYhBmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احد البحارين الذي أصيب في معركة كنارك:
رأينا صاروخ العدو، لكننا لم نتراجع لحظة واحدة عن مكاننا.
هذه بنوك اهداف الولايات المتحدة من مدارس الاطفال الى قوارب الصيد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83062" target="_blank">📅 01:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
مصدر ايراني لنايا...
نفي سماع أصوات انفجارات أو نشاط للدفاعات الجوية في مدينة ياسوج.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83061" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=ZGcrB5CbwGPpX8v0Qa28IZIVKY-0ByBU-KhOL75fH7c1QN-YO0sT0firPWXzs_1Q1eJw37VdyZfOyFhd8NpD05tClhwSWJymQCyvq_hrhAidLeMCO334x0ZBxZGxQ6KoXdX83sMCq03ppqFkYNbXZyn44z2by8p1UkQWo8egse5i2RDnXVmU30lziYivmRYZ5pCXB59snXasU3bTIgUtBlapUo1qn1vgogxY-BBlOscNqiVQjp3mEVnKmJiqx7k0qTLZaHv1NIF255Aj0L8Ku35aRiWG-2D15zVs-Ni7qmwolr16VgGEsdAyBE6ZVg07B25xEF0KH9UrV8-Z5_nzNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=ZGcrB5CbwGPpX8v0Qa28IZIVKY-0ByBU-KhOL75fH7c1QN-YO0sT0firPWXzs_1Q1eJw37VdyZfOyFhd8NpD05tClhwSWJymQCyvq_hrhAidLeMCO334x0ZBxZGxQ6KoXdX83sMCq03ppqFkYNbXZyn44z2by8p1UkQWo8egse5i2RDnXVmU30lziYivmRYZ5pCXB59snXasU3bTIgUtBlapUo1qn1vgogxY-BBlOscNqiVQjp3mEVnKmJiqx7k0qTLZaHv1NIF255Aj0L8Ku35aRiWG-2D15zVs-Ni7qmwolr16VgGEsdAyBE6ZVg07B25xEF0KH9UrV8-Z5_nzNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
العلاقات العامة للجيش الايراني:
في المرحلة السابعة من عملية البرق، واستمرارًا لهجمات الجيش الإيراني المدمرة بطائرات مسيرة على قواعد أمريكية في المنطقة، استُهدفت قبل ساعة مواقع طائرات إف-18 المقاتلة، ومبنى الإقامة، ومستودع المعدات الضخم التابع للجيش الأمريكي في قاعدة الأزرق بالأردن، بهجمات طائرات مسيرة مدمرة.
سيُرسّخ جنود الوطن في جيش الجمهورية الإسلامية الإيرانية بلا شكّ الدرس العظيم والرسالة الاستراتيجية لقائد الثورة للعدو، مفادها أن "عهد ضرب العدو" قد ولّى، وأن أي عمل ضد أرض هذا البلد التاريخي ومياهه وسماءه لن يمرّ دون ردّ وتكلفة مناسبة.
منذ بدء انتهاك الولايات المتحدة لوقف إطلاق النار والهجمات الوحشية على أجزاء من بلادنا، نفّذ جيش الجمهورية الإسلامية الإيرانية حتى الآن ست مراحل من عمليات الطائرات المسيّرة ضد قواعد ومراكز الجيش الإرهابي الأمريكي في المنطقة، وستستمر هذه العمليات حتى تحقيق النصر النهائي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83060" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بندر عباس وسيريك تتعرض لعدوان اميركي غاشم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83059" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تشابهار تفعيل دفاعات جوية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83058" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963c232464.mp4?token=uGX42Ygo1zf8_CLMGAkZqXuFqZFnqd7w_dy-7JiOsMpR8Gbf9WbUn0wHPou2RCIpjfhXmmL_jMt15B8z-ebrvWzFTE8grAfJo2X2xUBHGLzWjcUBiSnVW8AS_FuwsQgc-sX0P6Ftt33NIX_4TpTTN_uLyH0govBACPd_nSicfFW2KGBCxK_wAWq9q94OT4IqVrdthtD2uzZCo6d2FiKg_Jnc7wTEPx3MqTAupPY_W2VS6xijhf0CjZlp98xVB_jyRCn26s9q3Sn6SrZP95jyycgogqFvIgFzqnrcp3hVOdgYgDHTlJTHA2ai3O-IDHH3xzqKryghcBulqz1GoUUW8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963c232464.mp4?token=uGX42Ygo1zf8_CLMGAkZqXuFqZFnqd7w_dy-7JiOsMpR8Gbf9WbUn0wHPou2RCIpjfhXmmL_jMt15B8z-ebrvWzFTE8grAfJo2X2xUBHGLzWjcUBiSnVW8AS_FuwsQgc-sX0P6Ftt33NIX_4TpTTN_uLyH0govBACPd_nSicfFW2KGBCxK_wAWq9q94OT4IqVrdthtD2uzZCo6d2FiKg_Jnc7wTEPx3MqTAupPY_W2VS6xijhf0CjZlp98xVB_jyRCn26s9q3Sn6SrZP95jyycgogqFvIgFzqnrcp3hVOdgYgDHTlJTHA2ai3O-IDHH3xzqKryghcBulqz1GoUUW8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
معارك طاحنة بين عصابات الجولاني إثر خلافات داخلية فيما بينهم في بلدة ذيبان بمحافظة دير الزور.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83057" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
‏جيش الاحتلال الأميركي: أكثر من 20 سفينة حربية ومئات المقاتلات تعمل في الشرق الأوسط</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83055" target="_blank">📅 23:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عودة ما يسمى الحصار الأمريكي لإيران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83054" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
بنداء يا زهراء...
مشاهد من الاطلاقات الاخيرة للحرس الثوري تجاه قواعد الاحتلال الاميركي في البحرين والكويت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83053" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الدفاعات الجوية تستبسل بالتصدي للعدوان الاميركي في الاهواز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83052" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عدوان أمريكي على سيريك في هذه الأثناء</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83051" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات في بهبهان بمحافظة خوزستان</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83050" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83048">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f9e1449.mp4?token=QUfP8NdcfGRyPCfTM62X8mBOrrepO0LigyC9s4Xr0Acl1aYB9B1kppuaNXrE8fYutydbpKHz7E2lqIP9hC9lWMhwOYycXtI_Kvw3WSvCEVMD4evecp0ro4H6mY3R81M64HyWMRcgrS1685keyB4qesmQQjfJdveFIp7CqkNGeeWPkfEOWBdu6cVUpyBdaSzEEI_k05UlQMFKkwyxDVbk1rW4ruaQt2dxgg7dIZ83TmKo5VAv8ujN3uTwQHGiMF7Gy5RpLAgWKBBKaDLCV5E920weY0zZLUijlsxBcaFmAI9ZZu0J4QgVXZyVBMAIMIkcMT3rAu0w3_nBSjnOkU_mnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f9e1449.mp4?token=QUfP8NdcfGRyPCfTM62X8mBOrrepO0LigyC9s4Xr0Acl1aYB9B1kppuaNXrE8fYutydbpKHz7E2lqIP9hC9lWMhwOYycXtI_Kvw3WSvCEVMD4evecp0ro4H6mY3R81M64HyWMRcgrS1685keyB4qesmQQjfJdveFIp7CqkNGeeWPkfEOWBdu6cVUpyBdaSzEEI_k05UlQMFKkwyxDVbk1rW4ruaQt2dxgg7dIZ83TmKo5VAv8ujN3uTwQHGiMF7Gy5RpLAgWKBBKaDLCV5E920weY0zZLUijlsxBcaFmAI9ZZu0J4QgVXZyVBMAIMIkcMT3rAu0w3_nBSjnOkU_mnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إضافية تنطلق من الكويت نحو الأراضي الإيرانية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/83048" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
صور تظهر إطلاق طائرات مسيرة وصواريخ "خيبرشكن" و "ذوالفقار" في الموجة الثالثة من عملية "نصر 2".</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83047" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1bef5385a.mp4?token=ndfijsC3fIAp9vRwtHI77f5x5E7MBl_5xdzYSX8heAgGkbOTGwtt2eMNnFFriPKK-oIh-v704lkX8OS9t9w9o1-xElrICdhBN-vcBfFy97qhqNEkboWwEHSrqDXRrifV1jwxrFjiiJDIEU89vN5KYhER7wBpFDJ4C8qmK-YdHwE0aS9mOqDeFJG1mRrj3R8Z6ZEV6LDMJA-dmzHtWd9iCSrPjwVQFpyomrEbmLCb2dIHe8dBOGHBtyLsqECoGF5R9hjtmDXnOxn3Q-XfcbXhHoQl1YTupovYz5kuUCtfuXaKD7tWpaEsPOXA3cdzANGDy9dtgtEr76wlcxcpE9wIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1bef5385a.mp4?token=ndfijsC3fIAp9vRwtHI77f5x5E7MBl_5xdzYSX8heAgGkbOTGwtt2eMNnFFriPKK-oIh-v704lkX8OS9t9w9o1-xElrICdhBN-vcBfFy97qhqNEkboWwEHSrqDXRrifV1jwxrFjiiJDIEU89vN5KYhER7wBpFDJ4C8qmK-YdHwE0aS9mOqDeFJG1mRrj3R8Z6ZEV6LDMJA-dmzHtWd9iCSrPjwVQFpyomrEbmLCb2dIHe8dBOGHBtyLsqECoGF5R9hjtmDXnOxn3Q-XfcbXhHoQl1YTupovYz5kuUCtfuXaKD7tWpaEsPOXA3cdzANGDy9dtgtEr76wlcxcpE9wIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر إطلاق صواريخ من الكويت نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83046" target="_blank">📅 23:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoU6QGsKrextx5uYRWyie3BwtVC0ZjpnJ6l-uDacOeFiN6ZPb0uqAsUxuUUbAH63JbxlWdInNOGXSJvRYZBA978xAweJ2dbVn8DUT9YhJZNWz4pv52wqgw0AML-_Ay9A_ZQbnlQi7xJzxVlTYPIh5A7uGNJSVuTin1OXR4bI8b-DdRB5HGVNe6f94_c7_8-RwHv-x7qF4TH__U4U1K1XyFIpnq4XoyUl-iXTXkJ9kDa5iWsqoKwl46VRyhHMb_K-9DzJgl6Q88uuQRkisjPYS2v9ivDtJljAJRXF1j1eSPTcGtZPLDyMXoXtzAHne_TScH_821sOX1hYJ1X1GDOtSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات شعبية من ساحات العاصمة طهران بالانتقام من فريق ترامب</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83045" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الجيش الأمريكي:
‏
في تمام الساعة الثالثة مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية جولة إضافية من الضربات الجوية ضد إيران، بهدف مواصلة تقويض قدراتها المستخدمة في مهاجمة السفن التجارية في مضيق هرمز. وتأتي هذه الضربات في الوقت الذي تستعد فيه القوات الأمريكية لاستئناف الحصار البحري المفروض على الموانئ والمناطق الساحلية الإيرانية، والذي يبدأ سريانه في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83044" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhLGEUs1xp8Y9UtUPGsvANOR45gbgsXnIMF97xJocn30jg8bC06X3INKua2JGvpAuTFEWZpLnuxHg8oqsA_h-Z_9CjeXydFCqyd8Iptjdhratz8UNKMF5u7tOIRDlXKl02lEDTpHZXp_nccZRBn0ilRNqEfej7ohhMaEi1bj2O3eluzfZGFiUVC_Y6mJ-YsZWwfG8-aBJFR9Tx7M_0FACciSn1dNh0zWKXAAxFgA3TP0Q-anwMUXgOmzuUVaaguz7xaEbWnNDZr2r57IhpUljvyXbtMiX-rBAZ7oDJkQEFwRIw8IdI3K8NniUBB9la8Y4ku8Le76jknuIx9N6B3kfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83043" target="_blank">📅 22:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b3fd282d.mp4?token=ZGWfwP8dG3Xmn7-i8wY6o2VtcdsZTAcjrkVzbx-G2_xYvSCas4xQv6eYZZKCLDn8yD0Wr7_7Y-IXd24mBZXspJYHRmOnci9zU40k2gr8jeOnxpaIRoK6xgBBxwZlG_YRMyT8IND_axxZgvm0hrtXQpCZ3nxbucpvE9PUlvvIFFprKRqzHiCtTSGeoOYYkN018z0vR3FF9oWRo-CY7pG9BM2_UzVIlHH6QHEvj0uAYBUAxSHCL-N7aOCL-MBhxkgbOWYFhFH8R5TwCo-DSEJtLUIu6m9Yx08A44H5D6I3yZd_MHt2lzdpUu_SAqc4hOhTtmcpG06vwTSx0mwthzNF_CnL4pWIdECJFe4mfet1pMlv9xyYwo0C6eN7cs82ZNXoHrL_gtEChVWqFPmWMutXGvV4GmtydPWKRXiNXphy_vVPLFllGOPfU_EnR01I-wdzdKauutRyE5SeUTxDD-3-wmLtYn1SzpZjunGw31wiSVml2lKCVzFQdchx-PoD7nS1goufDTKxK31yUV95LRZySkINpEook7bMLdr6osP9jFkZNk6wMd9Ji0IjBcuM9VuW0acNi3UoIjE1YbENvCi0w-mI0_FFms4-TB3iDTbswGCdDlBBG9zS3S3_pXB3Y3j3BFZFa5438V72Jxp6QSbF_-uzmUw-bGXdHP3-N7z7DpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b3fd282d.mp4?token=ZGWfwP8dG3Xmn7-i8wY6o2VtcdsZTAcjrkVzbx-G2_xYvSCas4xQv6eYZZKCLDn8yD0Wr7_7Y-IXd24mBZXspJYHRmOnci9zU40k2gr8jeOnxpaIRoK6xgBBxwZlG_YRMyT8IND_axxZgvm0hrtXQpCZ3nxbucpvE9PUlvvIFFprKRqzHiCtTSGeoOYYkN018z0vR3FF9oWRo-CY7pG9BM2_UzVIlHH6QHEvj0uAYBUAxSHCL-N7aOCL-MBhxkgbOWYFhFH8R5TwCo-DSEJtLUIu6m9Yx08A44H5D6I3yZd_MHt2lzdpUu_SAqc4hOhTtmcpG06vwTSx0mwthzNF_CnL4pWIdECJFe4mfet1pMlv9xyYwo0C6eN7cs82ZNXoHrL_gtEChVWqFPmWMutXGvV4GmtydPWKRXiNXphy_vVPLFllGOPfU_EnR01I-wdzdKauutRyE5SeUTxDD-3-wmLtYn1SzpZjunGw31wiSVml2lKCVzFQdchx-PoD7nS1goufDTKxK31yUV95LRZySkINpEook7bMLdr6osP9jFkZNk6wMd9Ji0IjBcuM9VuW0acNi3UoIjE1YbENvCi0w-mI0_FFms4-TB3iDTbswGCdDlBBG9zS3S3_pXB3Y3j3BFZFa5438V72Jxp6QSbF_-uzmUw-bGXdHP3-N7z7DpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مباشر..
ساحة انقلاب وسط العاصمة الإيرانية طهران الشعب الإيراني يطالب بالانتقام.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83042" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات في بندرعباس وجزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83041" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔳
الجيش الكويتي:
القوات المسلحة رصدت، منذ مساء اليوم وحتى الآن، عدد (1) صاروخ باليستي، وعدد (5) صاروخ جوال، وعدد (33) طائرة مسيرة معادية، وقد تم اعتراضها والتعامل معها.
وأسفر العدوان الإيراني الآثم عن استهداف عدد من المنشآت الحيوية والمدنية، وسقوط شظايا في عدد من المواقع بالبلاد، مما أدى إلى وقوع أضرار مادية.
كما تم استهداف إحدى القطع البحرية التابعة للقوة البحرية الكويتية، وأصيب على إثر ذلك عدد (4) من منتسبي القوات المسلحة، حيث تلقوا الرعاية الطبية والعلاج اللازم، وحالتهم مستقرة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83039" target="_blank">📅 22:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات في مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83038" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
القوات الأمريكية نفذت ضربات إضافية على أهداف عسكرية بإيران في وقت سابق اليوم
الضربات الأمريكية على إيران نفذت للقضاء على التهديدات الناشئة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83037" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc3a98f98.mp4?token=WsrkC9jTil9ZTJftrhKxPGUu4ZBODiHUhVz5Pmh7YIkrcbL-xIl_rFlC4lsL1rXLqu_xKZN4ysymle1M5Y0n1MkFTGF_Nu4eaP_QA4HBgZ561pFu7nTZMUiLOnkT4TgZXIsmgi9Kbez79u13Hk8qi9U-f-dRKZHzLg9I_2abCS6ycJJGLqSWUWiv3zuWjKh5XyPBDwloMOgLRJ_b65XdYuH6hibwRYhW5AwRDLy3tdBwydqYXd3jAE1DeZX2Qy8yE1juQ1TPZFOOTYvJwQQ1oW8FEnmP-de3R9SQl9I5bv4XdBjhsNnRJfDTHpT5YYw81Fa5D5kmkg_wTkBTmKZZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc3a98f98.mp4?token=WsrkC9jTil9ZTJftrhKxPGUu4ZBODiHUhVz5Pmh7YIkrcbL-xIl_rFlC4lsL1rXLqu_xKZN4ysymle1M5Y0n1MkFTGF_Nu4eaP_QA4HBgZ561pFu7nTZMUiLOnkT4TgZXIsmgi9Kbez79u13Hk8qi9U-f-dRKZHzLg9I_2abCS6ycJJGLqSWUWiv3zuWjKh5XyPBDwloMOgLRJ_b65XdYuH6hibwRYhW5AwRDLy3tdBwydqYXd3jAE1DeZX2Qy8yE1juQ1TPZFOOTYvJwQQ1oW8FEnmP-de3R9SQl9I5bv4XdBjhsNnRJfDTHpT5YYw81Fa5D5kmkg_wTkBTmKZZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
معارك طاحنة بين عصابات الجولاني إثر خلافات داخلية فيما بينهم في بلدة ذيبان بمحافظة دير الزور.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83036" target="_blank">📅 22:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
أيها الشعب الإيراني الشجاع والرصين؛ قام مقاتلو القوة البحرية والفضاء التابعة لحرس الثورة الإسلامية، في الموجة الثالثة من عملية "النصر 2"، تحت شعار "يا زين العابدين" (علي السلام)، وتكريماً للشعب، بتدمير عدة مستودعات لتخزين الأسلحة وقطع السفن والطائرات المعادية في قاعدة الشيخ عيسى في البحرين، وذلك في عملية متزامنة باستخدام الصواريخ والطائرات بدون طيار قبل ساعات. كما هاجموا منصة إطلاق طائرات MQ9 بدون طيار التابعة للعدو في قاعدة علي السالم في الكويت، مما أدى إلى تدمير عدد من الطائرات أو إلحاق أضرار بها.
سيستمر الرد بالمثل ومعاقبة المعتدين طالما استمرت جرائم أمريكا، وإذا تكررت هذه الاعتداءات، فستواجه ردودًا مفاجئة.
طالما استمرت أعمال الشر التي تقوم بها أمريكا في المنطقة، فلن يتم تصدير قطرة واحدة من النفط والغاز من المنطقة، ولن تؤدي هذه التجاوزات إلا إلى تأخير إعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83035" target="_blank">📅 22:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار ضخم في مدينة صحنايا بريف دمشق</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83034" target="_blank">📅 22:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوي انفجارات في دمشق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83033" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوي انفجارات في دمشق</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83032" target="_blank">📅 22:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭐️
المتحدث باسم المنظمة البحرية الدولية:
نشعر بقلق بالغ إزاء الهجمات الأخيرة على السفن في مضيق هرمز وحوله.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83031" target="_blank">📅 22:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هزة أرضية قوية تضرب سوريا وتركيا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83030" target="_blank">📅 22:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔳
‏
الكويت
:
الاعتداء على قنصليتنا يقوض جهود حكومة العراق للوفاء بالتزاماتها الدولية.
‏على حكومة العراق اتخاذ إجراءات فورية لمحاسبة المتورطين بالاعتداء على قنصليتنا.
استمرار عدوان إيران ووكلائها في العراق انتهاك صارخ لسيادة الكويت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83028" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سماع دوي انفجارات جديدة في البحرين</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/83027" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a1709eea.mp4?token=u-lLfnD1LX9ALCpr-WsjTdgfeeMlSxdUPL5m7FxnmL2heQoCLZAtP7WMkTJqE5f1uN_2apNoAMpjBUTSHNyuDN6g0JghZU0GQlkqTV3Z7O8cxfo5m5dpkiFLlTFVktQhSCd9LejNz5bRetWRIXrxuQ6JI-PNqsQIQUt1hJraO2ZaJEi1hCieqWnuJk0WDum1K7euDiqdYDY41qvPEPPYuzjkGll4jGgW6wnTnrwV70b4xq4yH9LeG5lmpaSmEhvJSwWD0AycjOoF-_GFqOQjRVb63DNcOyL1ZmACbpP0zkn4KLt_udh4OsRy64SXfsMHYZ5KdtZ_Zbg4O7VcfH9iwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a1709eea.mp4?token=u-lLfnD1LX9ALCpr-WsjTdgfeeMlSxdUPL5m7FxnmL2heQoCLZAtP7WMkTJqE5f1uN_2apNoAMpjBUTSHNyuDN6g0JghZU0GQlkqTV3Z7O8cxfo5m5dpkiFLlTFVktQhSCd9LejNz5bRetWRIXrxuQ6JI-PNqsQIQUt1hJraO2ZaJEi1hCieqWnuJk0WDum1K7euDiqdYDY41qvPEPPYuzjkGll4jGgW6wnTnrwV70b4xq4yH9LeG5lmpaSmEhvJSwWD0AycjOoF-_GFqOQjRVb63DNcOyL1ZmACbpP0zkn4KLt_udh4OsRy64SXfsMHYZ5KdtZ_Zbg4O7VcfH9iwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلطات البحرينية تفرض طوق امني كبير لمنع اي توثيق يخرج لمنصات التواصل الاجتماعي يفضح الخرق في تصدي للهجمات الايرانية</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83026" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله أكبر
إصابة مباشرة الان في البحرين</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83025" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسؤول أمريكي: الوضع الحالي مع إيران مماثل للوضع الذي كان بين حزب الله وإسرائيل.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83024" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سيارات الإطفاء تنتشر في منطقة الجفير حيث يقع مقر دعم البحرية في البحرين</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/83023" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujR3WT_tzMidtYAxlFB9LZW1uBsG0L7XMWaXBXUKoL1eeT-xMhlkRpC_4KEFslo2M0KvrxkSxYpvGFFYhC0bJCpQ81H5ykO1SsgkvGxScL34VBcZGZav-dGn1LaUhbc42nacYdQ2rStLsY2EBArIhMsyI6D5kzgjrUyrJrT9sJsMmoGPYwH0PTQg5jspaw8AQj152-_xo9NwsShvySZkWoXPkucuke2t0s-bWnuZn8V9sjEeEZrk0oyDS8fFHvdRZWr2nlew0cLzDGuhXaRJDFTQ7nDmbFz45YACZsUb-v7E9S3HQzdCwutsxsqr-b5lb6eaHHeDdzlbjH0E_xtLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج مطار المنامة عن العمل وتوقف عمليات الهبوط</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83022" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
🌟
بعد فشل منظومة الباتريوت.. طائرات حربية أمريكية تقوم بدوريات ومحاولات تصدي فوق الاجواء البحرينية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83021" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
🌟
بعد فشل منظومة الباتريوت.. طائرات حربية أمريكية تقوم بدوريات ومحاولات تصدي فوق الاجواء البحرينية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83020" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسؤول أمريكي: القوات الأمريكية تشن حاليا غارات جوية في إيران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83019" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صافرات الانذار مستمرة في دويها بالقاعدتيين ارباك كبير في دفاعات الجوية الاميركية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83018" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قواعد الاحتلال الاميركي الشيخ عيسى والاسطول الخامس في البحرين تتعرض لهجمات شرسة بصواريخ نوعية</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83017" target="_blank">📅 21:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83016" target="_blank">📅 21:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صواريخ انشطارية إيرانية استهدفت البحرين</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83015" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehkyvmACseNy3XZscZUYtflXm6c4TQd3td_u2IZiC8aIb0uYbmTobHY_p-j7NwDY6IRDHYEAF3lFOKRN578puDNj_ONyQZzCTjON9VwtiL9AeK-SmDnlpN9DPe6-KqvlvQLnHCNmaDGH2K9OUu7PpKyT8f6lNPtwkma802nO4qdYPxqUWJSVE6NqXD_85XnSump_Rd-RIwQsrpGxbRcqu7cjSVXX3bMrSdfbyXnsis6mRmUyUSgVf4F1-5TroOS_g8SotA2r5wKOMW9_43jN3k76UjD_SmjiO3Gbe49TfHjAxb2yEIBVKTgTFqM7EpW_7ZjOMd7mf-bYnK291jtvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية في سماء البحرين قبل دكها للمصالح الأمريكية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83014" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الكويت تتعرض لهجوم صاروخي جديد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83013" target="_blank">📅 20:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83012" target="_blank">📅 20:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83011">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
النزاهة العراقية تطيح بمدير الأشغال العسكرية إثر مخالفات ومغالاة بعقد تأهيل مستشفى القوة الجوية - الرستميَّة بقيمة (92) مليار دينار. حيث تم القاء القبض على عميد وعقيدة و 5 موظفين</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83011" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">إعلام خليجي عن ‏مصادر أميركية: واشنطن تراقب احتمال تدخل حزب الله في أي تصعيد إيراني</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83010" target="_blank">📅 20:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83009" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83008" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
مصدر خاص لنايا ينفي وقوع انفجارات في تبريز أو شيراز.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83007" target="_blank">📅 20:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/83006" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83005" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏‌ترامب بشأن مشروع قانون العقوبات على روسيا: "هذا تكريماً لليندسي. كان هذا مشروعه... وهناك احتمال كبير أن يتم إقراره، لكنهم يرغبون في إضافة إيران وحزب الله إليه."</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83004" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏ترامب عن الشهيد أبو مهدي المهندس: سليماني - لقد قتلته... وصادف أن قُتل شخصٌ سيءٌ للغاية من العراق في نفس الحادثة. لذا لا أعرف إن كنت قد أسديت لك معروفاً أم لا. لم أسألك هذا السؤال قط.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/83003" target="_blank">📅 19:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامب: يمثل النفط العراقي أولوية لنا، وسنُشرك شركاتنا بشكل أوسع في العمليات النفطية داخل العراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83002" target="_blank">📅 19:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83001" target="_blank">📅 19:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏ترامب: لا أؤيد فكرة فرض رسوم، ولكن في الوقت نفسه، ليس من العدل أن نحمي هذا المضيق للعالم أجمع، ثم لا نحصل على أي تعويض، ونحن نفعل ذلك منذ سنوات عديدة. لقد أزعجني هذا الأمر منذ 25 عامًا...</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83000" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب عن رئيس الوزراء العراقي: ‏"لقد كان مقاتلاً عظيماً وكان من أشد المعجبين بأمريكا... لديهم احتياطيات نفطية هائلة... لديهم ثروة هائلة."  ‏"لديهم قائد عظيم، رئيس الوزراء الجديد. إنه قائد عظيم. أعتقد أنه سيبقى في منصبه لفترة طويلة... إنه شاب ووسيم، وهذا لا…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/82999" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية الإيرانية في محافظة خوزستان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82998" target="_blank">📅 19:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82997" target="_blank">📅 19:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82996" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ترامب: لا نعتقد أننا بحاجة إلى وجود جيشنا هناك الآن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82995" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏ترامب: نحن موجودون من أجل العراق إذا احتاجوا إلى الحماية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82994" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامب: نحن نحب العراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82993" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
