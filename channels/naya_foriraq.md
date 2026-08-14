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
<img src="https://cdn4.telesco.pe/file/KKrb8egOgHuqKidT3erqmFf4gEvE0w2IJb-s0g7Mq7TTDPoEE4Bb4JN_nujb5BbLQO3NyKcJV-XmzQZjEJfggXU13_xRlXzXm8pUpHg-qSr10blaLZFpvgWoVCf29ul_kd-WcA_YUlJ8bOpTi2F9SffiFvH2I68ubufnksRGmokNa-nkLBeW7_zVBKFiDfMPnsc_haa7Zv7NMnCo6r_qVaVjyY9Jo0wnsvn-emY6n-mwHWpcKzDQa3XAH46ciQkrIxqhSIA_Jyan30KQJzDWK4eyZ_ZnR4rpBoEq_K1q9iCqfaNy3Br5PAxHGzeAQ6IXraPjLsUysuJmGijZfUVCAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 00:46:48</div>
<hr>

<div class="tg-post" id="msg-87806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن إيران: كان لديهم 212 طائرة جميلة جدًا، بعضها تم شراؤها من الولايات المتحدة، وبشكل ذكي، في عهد أوباما. جميع طائراتهم اختفت.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/87806" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/87805" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
الوضع بين الولايات المتحدة وإيران مستقر.</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/87804" target="_blank">📅 23:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/87803" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران
: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87802" target="_blank">📅 23:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
We are the king of Hormuz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/87801" target="_blank">📅 23:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
ترامب
: سأضرب إيران اقتصادياً بقوة .</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87800" target="_blank">📅 22:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇾🇪
مشاهد من احتراق السفينتين في المخا، بعدما تم استهدافهما من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/87799" target="_blank">📅 22:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية استهدفت سفينتين كانتا راسيتين في ميناء المخا.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87798" target="_blank">📅 22:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف ميناء المخا من جديد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87797" target="_blank">📅 21:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: أفراد عائلات أفراد الخدمة العسكريين قلقون بشأن الظروف على متن السفينة الحربية "لينكولن".
ترامب
: لا، هم ليسوا قلقين.
المراسل
: هل استمرت مهمة الانتشار لفترة طويلة جدًا؟
ترامب
: لا. لا. لا. لم تكن طويلة بما يكفي على الإطلاق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87796" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87795" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: أميركا وضعت فيتو على طلب إسرائيلي بقصف أهداف في سوريا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87794" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87793" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
مشاهد جديدة لميناء المخا وهو يشتعل بفعل الصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87792" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=Y2KKiShXGRiSUljuN1a9oFfbQ5TxQF9A8HYbLrep3QrED8OiHC3Pf0wEGixSBDMs3y7jrJzL2J2ad1cQ7t0gTP5Q6TI8Y0iydJeeUBQUgl5EEbOT7Sh7ONv3HQy9wQCqNXv-Xelq0gHQfCEJo9PhjbzX5IRtFyKXzd8DekJThGObEsw96elI2DFmPHBTiPMVUS7jJlblCV7gHenXNyp11bdJeihimrOhu8sqSlk1sderT_VjxqSesjwD1pvh9vhHMqHQHbTbre00nH_mSKJwt_NXTOicZzS4DDFrVUzYvLgZNXL02qgdzNEythvWprpZmUy7TVckf40jpFdk_zDb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=Y2KKiShXGRiSUljuN1a9oFfbQ5TxQF9A8HYbLrep3QrED8OiHC3Pf0wEGixSBDMs3y7jrJzL2J2ad1cQ7t0gTP5Q6TI8Y0iydJeeUBQUgl5EEbOT7Sh7ONv3HQy9wQCqNXv-Xelq0gHQfCEJo9PhjbzX5IRtFyKXzd8DekJThGObEsw96elI2DFmPHBTiPMVUS7jJlblCV7gHenXNyp11bdJeihimrOhu8sqSlk1sderT_VjxqSesjwD1pvh9vhHMqHQHbTbre00nH_mSKJwt_NXTOicZzS4DDFrVUzYvLgZNXL02qgdzNEythvWprpZmUy7TVckf40jpFdk_zDb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
قصف صاروخي من انصار الله جديد يستهدف ميناء المخا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/87791" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87790" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=I5M-bZz5e-30eoXTbmCR36IF7mHurGeGtJXiWIUnkvwQfFoWmW4dkKaUSfDRRMV3wAkHvOH1OH8jJtiBVc7TGRi6jcijme1ARtZlCi3bsuPyOd1co4QyOF6bWQ2-n5lVXh_9D4QrnudU4E3ZlhyOhXOTuYI868yKaQAOsa8o7DNXf-x3g4eRcePjhmkG68KWOIl2S93nSpkpL2Q96_GhXct2_DMcoUvZNIG56jbUgre4FKu0WCWQzJ41ohvtpnjhJbeGijn6kXe7Yoxtu4J218uAGxMz7azGPdj8L_1bgBAfSGI_xMoH6YTcbSCiT9Ramicc87YTFt_-JjlHDsbnqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=I5M-bZz5e-30eoXTbmCR36IF7mHurGeGtJXiWIUnkvwQfFoWmW4dkKaUSfDRRMV3wAkHvOH1OH8jJtiBVc7TGRi6jcijme1ARtZlCi3bsuPyOd1co4QyOF6bWQ2-n5lVXh_9D4QrnudU4E3ZlhyOhXOTuYI868yKaQAOsa8o7DNXf-x3g4eRcePjhmkG68KWOIl2S93nSpkpL2Q96_GhXct2_DMcoUvZNIG56jbUgre4FKu0WCWQzJ41ohvtpnjhJbeGijn6kXe7Yoxtu4J218uAGxMz7azGPdj8L_1bgBAfSGI_xMoH6YTcbSCiT9Ramicc87YTFt_-JjlHDsbnqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87789" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الشيخ نعيم قاسم:  - من يراهن على الاستسلام إنما يراهن على سراب ولا يعرف المقاومة جيداً بأنها تتحمل وتصبر هي وأهل المقاومة  - اتفاق الإطار الذي ذهبت إليه السلطة اللبنانية ليس لا اتفاقاً ولا إطاراً  - اتفاق الإطار هو إملاءات إسرائيلية بالحبر الإسرائيلي تُوقّع…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87788" target="_blank">📅 19:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87787" target="_blank">📅 19:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bci4xoPq2SeRL5vwo2x0Ax9SV_XZO0iOeTBWQcWlss5DsWMo1Q4ypAljTMNzZNCs2fqrWuGtp3my-84SKXde-RX3UF0Vwyems9fvxg2ZyXnN_id_7FHmx4AGC0gnjUf6QbQavkuYOrj-pUpDTNzNPXEHiPeHYEd7yei9NLaLBWNTp7XFs6yR3gERNJLeILL9YIU_T-aaNjkK7pOGujJc92x-d3dnu7XRTiQgWTa2D4hQcEKjbExIbyqp6fowoZ_kpDOaxXO-JoR4M4FhFFxxIMa_wc9j9bfJ_uH3E5W723mNXaBVOY1rvZVeAc3ENh9obLF-IZlnGH1hnRNfL6hmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇾🇪
وزارة الخارجية العراقية تلتقي ما يسمى بـ"السفير اليمني" التابع لمرتزقة السعودية وتعرب عن تضامن العراق مع الشعب اليمني خصوصاً في ظل تصاعد الأحداث بين أطراف النزاع وما نجم عنها من خسائر بشرية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/87786" target="_blank">📅 19:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87785">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
الاستخبارات العراقية تلقي القبض على (23) أجنبياً حاولوا الدخول بصورة غير قانونية إلى البلاد عبر المياه الاقليمية العراقية وباستخدام الزوارق البحرية السريعة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87785" target="_blank">📅 18:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87784">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVub8QdMzOTVGTCWOv1v7C4BcGM9cwYC5Jr732IDI-AXw5NeKOvd8JWTK_XFUzfW0qUer_Rq-K-UvElDbBR44nfgjMjfzziyfuheKyQXtTvlkkdz-oZBvpCRG8R4spx0v9gs4rNK6fJXswRPtJoI3MTTuuGheD6Y_Ot7L_PV3O7cYpG19N1BhACXY_CiM0gNvmjM36zRKf71xcHOLDJ9PRpfOvJQ6EpJyIgIub-FAMxB1W43zSv9amyWgnbA0g9qwhOzzx0HjgavyibeH7zp1UU3owrfe6xpZ0Tf4MYAXeluYquRG1pos0VD87bs-XfkCI9ZuDWbw5MFRzNZqV6JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مسير مجهول يجوب منطقة البلديات في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87784" target="_blank">📅 18:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87783">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87783" target="_blank">📅 18:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87782">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
🇺🇸
‏محكمة الاستئناف الأمريكية تقرر ايقاف مشروع ترامب لانشاء قاعة الرقص في البيت الأبيض بكلفة 400 مليون دولار</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87782" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87781">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTviscKMSlmgIJpetp1dC8xQz8u7Wo5zASfAtO8DyuOKkS8Yo9CTjFRUfVhfRvBYhr3Ev9biKBRdTSS02MX4SAhRawY2rY67-P5hChEbVsseEhV-kSwoXl1GkeY5JS_WdkdDARflpXGux9jmd3dFuxyJK0ZqTNJlKb8aYQKP_Jx11LPRXoAiw9wxypt27ky6mj7_MV_m9A99jcsRR8WpiP4-v35kV5Sir81LkUf5ILPka_1SBN7xEf8r4rR9bh_h8IYAEp82mgDa5oxgGMbbDZclbPhTNv7_wJLV5t5Td_GT4tcE8aUisTySCJx_ESMrqJvBCkdiw02BUe9uStbOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
منصات التتبع:
شوهدت اليوم ناقلة نفط عملاقة تابعة للشركة الوطنية الإيرانية لناقلات النفط وهي تقوم بتحميل مليوني برميل من النفط الخام في رصيف أزارباد في جزيرة خارك بإيران. ‏رغم أن هذه أول عملية تحميل تُشاهد في الجزيرة منذ نهاية يوليو، إلا أن إيران واصلت تحميل ناقلات النفط في محطات أخرى. ومع ذلك، يبدو أن إنتاج إيران من النفط يتماشى تقريبًا مع إنتاج مصافي التكرير (الاستهلاك المحلي)، مما يعني أنها قد لا تحتاج إلى تصدير كميات كبيرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87781" target="_blank">📅 16:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87780">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3k15wsRvhtm6xU3p-jsscWwRK69ST2xhBjPkOZsNHc9geupworUE9ZPdwABeyoY5Z9SgL4LEa-bLmVKGFONl-sc95bAxTb94Or4Z6ayO26ppAAgcKb6WRjJ8jfIUh9GXMfNsvJbtMw3m2NZUhkAsZ_zoeolZQkIxZMxePDOpkDt4XmgRV6j5OvVKnhBYSMzxryHTNwVMDOKTBQUiGBhYvFTMRUe899B7n1Comz3VDeHuj7_Wd9z_dX-mziNzJFkkNCz1p_U34XT00OcezUYaNPhRhOEEDbIz5WAbDJKtWfz_g2b3QbqST2p-1P65frJeLwSnthuYT8F81-gNJDo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
لقد تعرض نصبنا التذكاري الجميل لحرب العالم الثانية للتخريب بالطلاء. لا توجد إهانة أكبر من هذه لأبطال أمريكا الذين ضحوا بحياتهم في الحرب العالمية الثانية. أولاً بركة المياه العاكسة، والآن هذا. نحن نتعقبهم! من أين يأتي هؤلاء المتوحشون؟</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87780" target="_blank">📅 16:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87779" target="_blank">📅 16:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87778" target="_blank">📅 15:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87777" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اكسيوس:  في الأسابيع الأولى من الحرب مع إيران، كان بعض أقرب مستشاري ترامب مقتنعين بأن ترامب سيدعم نتنياهو في الانتخابات.  في ذلك الوقت، كان ترامب يُطالب بشدة بالعفو عن نتنياهو لإنهاء محاكمته الجنائية.   لكن مع مرور الوقت وازدياد تعقيد الحرب، بدأت مصالح ترامب…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87776" target="_blank">📅 15:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📰
اكسيوس: تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87775" target="_blank">📅 15:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📰
اكسيوس:
تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87774" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87773" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87772" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
‏
رئيس لجنة الإعلام الأمني العراقي:
التحقيقات مستمرة لتحديد مكان إطلاق المسيّرات باتجاه أربيل ولا مؤشرات على إطلاق المسيّرات باتجاه أربيل من داخل الأراضي العراقية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87771" target="_blank">📅 14:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGIWNVAwDNy1c_ntpCKv3Gl1V1v5dzcqnxqM9U2SGGjRJy_Iak_fUCPM-fIsBRPS6Ds1LeEJKkmjy3KRIXQeNRo4JYRB6CHfS0IUft_UH9z5DgR_hmPqE8qeQbJww_IvZ6LWrPxOnHGev-chLxXPj7fEV66kLDgclNGHvuY8c6w6HLTjlB7pNAzNLPcT7NzrNvsXuZXvJ2oD2keQ05LKZ0-tHjmrJH0hheDBYrCEdofBlRig7In9tpVCKT6DpyCRBdOaOLiZ63cAgRGytnGe5-dn-DkhaCdgisUGQA-aZxRwx5FF-kqeqv4Qc0aH2VUtpAmkhYDQPZBmtyxQDqYm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5dcH2SUvNrzj1rNNxoXeTZ5y4ucqcY3S7n2oycjShrIZpA5u_Y0OY8_GM8opzygVy-iLzv9CeGMQ1eaPREZ9ki03_2WzQFyCfrl1KTgyDeWALYbvxaf3em6djcL8XuQVqc2qpIWiUBuifCx7I_4rUEUSukjhwXCpKzLjnCAjUzcVWPQFahriwgEKotvXwP6L8qIlCFcYficmGwnl_oI8CNX4_EXNNXMgPWHbH_T5352E4MrnEsFBRcHv-ae-dUMs0GnOjMz5musIE8ctF8FWfJbpSCy4XiLXZtSN7gzVy3ruLz50_UZ2MtAYOZkGNjUn3zhVMRmQtuuATmDFSi0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p30vn_LzSWRFxN5RengilYHcgeaqJyTXB4u3vueBh_mF7_Rs9-yJ70fYIT--XSUzgZYgyoDWLe8Iq97KE7kLU23DRxpFdeHsja0sX8ph7A-3zRyH5t5hbrCYT4QS0oXe2Uhk9-45WjFAdALfzvtjt8WgE6pJFzMi-uCUIyXvr_EbbduCzgan0mpQrld2WyInDSYM6bKLo42SQMO4QdNeDse0fbZAN8TDxkhW6kDARMkpjUjUFrZXSQunEH6AOGpyhRDa1aXKdCiRVKJIYIzSV7ZrcAZhik25fAv9dhnuQ9un861f1y087ewHtc1o_a0rVJ3GxQWSkd_GqdvNdsC2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSDiKnjQyDg0cv31qmk_ZuMZgzTlUK91TaD32QuZ6hKlGQrRA3u6zOR9R8PIN9Nv1INYW_fodefsnrydG7lizjhqrYGdojqsdO6rXjNbStvDnohKxm0yEsY3OXKJt6qD4wVGJSf865PiXNdSRZX15oJDnxaNyae2a54AdydgbrKR9tU2uf63t-7PiWJTNEzRmYFJl5hdEzRkR1U0b1JZ3KyIsXsS8AzB6dw7LZIVJ8OXjJqq7he7CTNhxPeZQ44AjciL3fs4x91j3cDi2VupdwUu8Ad7wPiu25nqtXQEy6r4R6qJq-O0ORbUTcvi9T5bMpu_rcFPUe708neKl2Fa5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfHsbTyxuOsPzEaoL2XJNtTkyDIMbB1P35DAj0w3s-oquOzcFWsv71EAPnOgpF8tVy5A1hfW1lqrvYk0SKg3G1Q6y0Nd2p3bS8F70NNcXReIBpRihL2gp5hZhJYbdsigrwqlUm3BA2Nxuj7sltSch_cF511j48pfF-_bEXD8XZlyyNEEs4Wgo91zagCYVIeMTKWwsQeHgnku-aCBH3sD-V8UULexDdpYmzx1AljUZwVZrzSRfZtg0gC39CCQZXxF0qdqBFgfBG2BNLymuHmuWpGu2FyM3z4W5ipprhaB6SligRu41GMV_xmyF30S9HxcOGSRe-KD94JdRp5iC5YPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwOcq_uCYtmdDMjmnpDIA8-CnSNgwUjCGSruBCBGVRVDb2n1LJK65nmWrzp-X74SBdretjNTLKIua0HGPwu39TOuTNdcbvag3uLC_4MqR5n1nUrr0uJcXgpzU_UFVTqZXeJqEVFCAmoxASlTCUqTvewB-BhD6SuE9gVqPIWzssMOu59BNrS0-uqF6XpKnwMMR33j3xnvgoLV2ve5rlRkcCbeKpzNfahY6oX8VW3ls-qPz5ANxfNAXdyXyyo0RyNstrgVPLst0-aZpRGbEXvW2lO_5bTX9yqP-NIi30FneW36rjXmz56hrKSG3z5YhuKDWyPz2MegEC8911a2JviDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lym_qTsMNVo3PsxDfn9SE6oIUsJFWpMBJFH_frLwB1yNOZljXy-UMDn_IAzeahb25mnPgRktZqfGR7ObGGUvouUIhiY5cBROTO-vnV9PZGlaxtJwfgH3qU7PqYUiS23cr8qT7j8Nqjbg-nPUZL6Tqu_7CUi5t1xbV8vJVWnaQN4SYLwJI6T-_9cQavdl2bVmtAfRoeHVKU0gw35qEvgf6roLW2pLdXdqOsbEyV-lH9Z7QHd7kNwiPNUg9IdWOBRcw99Waw5H9QyscaNQIQRv8xawJTceVDymcKiykmOURTcAbPhEnRl4Cgv-cIeFRGKfyzMtJpDfSi0fImd3jp5cEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور لطائرات مسيرة وطائرات مقاتلة أمريكية إسرائيلية تم تدميرها بواسطة
الدفاعات الجوية الايرانية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87764" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مسلحين يهاجمون وزير الداخلية في إقليم بلوشستان الباكستاني في منطقة مستونغ.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87763" target="_blank">📅 14:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87762">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87762" target="_blank">📅 12:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي
لافروف:
لن يكون هناك هدنة في أوكرانيا. موسكو لا تنوي إيقاف العمليات القتالية على خط التماس الحالي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87761" target="_blank">📅 12:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNngoU1ZygIRuMuyS_LNznjWqYDfyJWFz6QxewB4qW-7GTO-Q78BdX4b-4nt_zMQ20r0N_h4wixPC9kfjBR2cxShuGhyxfPmOWyVDvHFA1zJ6RsAmPOnpzc7HgG8jS8DjhPhI0n6_HqD4Stdy4texu5cfR3GJIysagz6ufSu5nusCkfovrteFfbMcbbOLoyk267gGcPW20HHJQ0nvUzmYDyQyTzQ9pkJJvnOYSL4FE0GIfCihLZL1qbaMk9Oj9tB-nyuONoj7pdYGKSjyf9WXo3_Zbq3HJ1YsBVNNTZ1rvcuWrEia4nRfD_5YYhABDGpn8s1JFpugaOL7faKE_2N3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87760" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الشؤون البرلمانية في مجلس النواب الإيراني:
تمت مراجعة مشروع "الإجراءات الاستراتيجية لتأمين مستقبل مضيق هرمز وخليج فارس" في لجنة الشؤون البرلمانية، وبعد الاستماع إلى الآراء، تم اعتماد مبادئه العامة.
أحد القرارات التي تم اتخاذها يتعلق بمنع مرور المعدات والمستلزمات التي تملكها الولايات المتحدة وإسرائيل والدول المعادية عبر مضيق هرمز؛ وذلك لأن هذه الدول استخدمت مضيق هرمز لتنفيذ أعمال عدائية ضد بلدنا، وارتكبت انتهاكات وهجمات غير أخلاقية ضد الشعب الإيراني.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87759" target="_blank">📅 11:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية:
استهداف سفينتين كانتا ترافقان سفناً تحمل أسلحة إلى أوكرانيا.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87758" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=CTzoxchOFNQQxsf-f3pURDrU7m_qPBNc3TS_hsEy5DEVTXWt1LSDg9gO7A93QYQIQre1VQ7O7JKasQBxPKClJvw6cJ8xbBG_4lrzkqiog4I2tPFDt63OXxhyxHKmBIAJSyVHENZcilOo7XIPSHHi3zQ6RZWI0VMkrE2WimCkVecj3QJIwY6oSVHW5xJmghx4I-ZGsUZTFal66t-aDjoMbzyMnvQuAc7pfHgINbyg6EAuaE6uDXnrVTOubIgDaNTvlab0imppFMYPjdZ_BRJE4MKRvPCYRBmcx-v7Zobd0LRfjkDvOHonSt_iwzdzqeqP8V5E3xPjTdJglBM6LRkbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=CTzoxchOFNQQxsf-f3pURDrU7m_qPBNc3TS_hsEy5DEVTXWt1LSDg9gO7A93QYQIQre1VQ7O7JKasQBxPKClJvw6cJ8xbBG_4lrzkqiog4I2tPFDt63OXxhyxHKmBIAJSyVHENZcilOo7XIPSHHi3zQ6RZWI0VMkrE2WimCkVecj3QJIwY6oSVHW5xJmghx4I-ZGsUZTFal66t-aDjoMbzyMnvQuAc7pfHgINbyg6EAuaE6uDXnrVTOubIgDaNTvlab0imppFMYPjdZ_BRJE4MKRvPCYRBmcx-v7Zobd0LRfjkDvOHonSt_iwzdzqeqP8V5E3xPjTdJglBM6LRkbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة انقضاض المسيرة الانتحارية والانفجار العنيف في مخبئ للقوات الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87757" target="_blank">📅 03:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=Bg-xq7HQJPz68Zt6I1S65VlCMh19YOx9wPN8rH4r4yAOZiijisIszkANQmURkuk5de7xDByT6xUYvi_T4PyJ98n5y3VtX3UOVbv0LkqqrsdcLF3wHlKadJfMAkLErgsv7CZ7vFkvvCDnVKCUkqC8j5xxk_9t1kqH96X91c-3a4qaUp-LLgc7tg3HM9N7k3YE7SuSNNyjHvbHrAc8QvwatTzYqyHNu9o9ydj9N57eHSg7L93oJgkPWl9gqSjyJO2q4Bzo2VgCuqkLZkfrjVlz4ae518gsjHCaOwBAYGLLgESNHh0PHq0Wk4ZPMU61xSXgrAcqk5rxBxRG_wwJfUXBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=Bg-xq7HQJPz68Zt6I1S65VlCMh19YOx9wPN8rH4r4yAOZiijisIszkANQmURkuk5de7xDByT6xUYvi_T4PyJ98n5y3VtX3UOVbv0LkqqrsdcLF3wHlKadJfMAkLErgsv7CZ7vFkvvCDnVKCUkqC8j5xxk_9t1kqH96X91c-3a4qaUp-LLgc7tg3HM9N7k3YE7SuSNNyjHvbHrAc8QvwatTzYqyHNu9o9ydj9N57eHSg7L93oJgkPWl9gqSjyJO2q4Bzo2VgCuqkLZkfrjVlz4ae518gsjHCaOwBAYGLLgESNHh0PHq0Wk4ZPMU61xSXgrAcqk5rxBxRG_wwJfUXBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87756" target="_blank">📅 03:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=MewM0JkubLKc33BjFgLm_cLbmk1kX5cpKv1fX0Sa0tgG-nt8ZNf9JoDYQo_lAoj8ZxRZ_hcJokcyBMWJSoBzGK4cUjhRU3e1tecFHZb2bDLDTM1NrP66v_hapaRRKDoqWOk_VwlPUlDDuKksx7gcm3ZAR7qMZt6PJ38-ZVI7a3j8wTv6ve3rTccVtgmUuaiqoxA3k7asbK0BUvn9QlkgHLeFVMXQeeP5g5mpgT1JVJgR5A8TOhnAYYv1AVuatzeUwtAjLksYJPJVFIGr6RjW1ZRGmzA1l4TE83lBcM6ggrHuCmmnBozAf5skPIpcoz49tT7HlO5R2BmTdrPILiZSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=MewM0JkubLKc33BjFgLm_cLbmk1kX5cpKv1fX0Sa0tgG-nt8ZNf9JoDYQo_lAoj8ZxRZ_hcJokcyBMWJSoBzGK4cUjhRU3e1tecFHZb2bDLDTM1NrP66v_hapaRRKDoqWOk_VwlPUlDDuKksx7gcm3ZAR7qMZt6PJ38-ZVI7a3j8wTv6ve3rTccVtgmUuaiqoxA3k7asbK0BUvn9QlkgHLeFVMXQeeP5g5mpgT1JVJgR5A8TOhnAYYv1AVuatzeUwtAjLksYJPJVFIGr6RjW1ZRGmzA1l4TE83lBcM6ggrHuCmmnBozAf5skPIpcoz49tT7HlO5R2BmTdrPILiZSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة استهداف مخبئ للقوات الأمريكية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87755" target="_blank">📅 03:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87752">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=AjbBlgQu3_is7Ij9D0UmJXTmHo-nNSJnBiuuuOFLLDj6n0RJs0s_Y_sToTF6L2goqgZ5pH8fpsDlp6bB3oJbgJlpzSLe-qL_EJgc_F1UUc-u-p_57IPAdDCJ-8VqDg6ZS3UtlkckjM_Uy16TCn9f12GzP9v4HP-Q4C2WKgi5roSCgAIQIfVnFFsjdN8XzFUQp16qlYCRoR3ZVS_6loZ8M4wjOGQldNWtpmKRZHTKwKyVM_y2YQFMdX4ek9iJ7tnNTlE6CkWh-YQyWgmR1pAyMW8YNoH83LeQHtLTdduN7r0DYNlA8Umu8_UxQGGeFW8eZXAB7wQYXdjN8pPWO_R4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=AjbBlgQu3_is7Ij9D0UmJXTmHo-nNSJnBiuuuOFLLDj6n0RJs0s_Y_sToTF6L2goqgZ5pH8fpsDlp6bB3oJbgJlpzSLe-qL_EJgc_F1UUc-u-p_57IPAdDCJ-8VqDg6ZS3UtlkckjM_Uy16TCn9f12GzP9v4HP-Q4C2WKgi5roSCgAIQIfVnFFsjdN8XzFUQp16qlYCRoR3ZVS_6loZ8M4wjOGQldNWtpmKRZHTKwKyVM_y2YQFMdX4ek9iJ7tnNTlE6CkWh-YQyWgmR1pAyMW8YNoH83LeQHtLTdduN7r0DYNlA8Umu8_UxQGGeFW8eZXAB7wQYXdjN8pPWO_R4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف فندق يتواجد بداخله عناصر من القوات الأمريكية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87752" target="_blank">📅 03:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87751">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b228489921.mp4?token=camgN_YyJnPHltueWUz0GTfovG3T-6PA77MkxrROpCQXx0CM6oyp-5As6u2PioaEfrJB5pT4ruB1jy-6CUtMGsfMuPqudkChHuUm8O9PpoSEOdkVGfs5Di-6qV8BG6XHdfLm1PZQfp92KFhj9-bZTowemty-N1a6jo1rpiwq6Ub7t8O9ekk0ENa0OUWoBNgxxVPJmih4JjUJ2O0_PM2GWom9VYNck1ttRrCH4vB5DJNMMfsofrg1qEtcpInCX5wGbMnV2ccPv9AtX-CEI9hM9QS9s9kYKq1ohBAM9CPU6CI4ILv7_Ece6HKZKPvKzXUOLQdl8PGsKnpenX6b970gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b228489921.mp4?token=camgN_YyJnPHltueWUz0GTfovG3T-6PA77MkxrROpCQXx0CM6oyp-5As6u2PioaEfrJB5pT4ruB1jy-6CUtMGsfMuPqudkChHuUm8O9PpoSEOdkVGfs5Di-6qV8BG6XHdfLm1PZQfp92KFhj9-bZTowemty-N1a6jo1rpiwq6Ub7t8O9ekk0ENa0OUWoBNgxxVPJmih4JjUJ2O0_PM2GWom9VYNck1ttRrCH4vB5DJNMMfsofrg1qEtcpInCX5wGbMnV2ccPv9AtX-CEI9hM9QS9s9kYKq1ohBAM9CPU6CI4ILv7_Ece6HKZKPvKzXUOLQdl8PGsKnpenX6b970gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87751" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87750">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=PU-DpTBCPY63JWnj62ZdzCrOhf_7Lp_sxEIlOVFxpRU_gjIGoWBWqrtiHkzRO0vV7ut0xVCMQT2l10Vv90DKmXjF1l9BbDTMlfwVB3c5UtVzuGgPP7a_q_sFJiyNWfddL7DMYBcpoZj-w4__fPH18pHo672OBB4GE2C0KdGrZbnrMY26kuYfdGdYXgOHDZ_AHwRAmWIu59Zp7OeH5xqfEA5umm7TzdaBYZnFNwi7I5zjaUGzXF4Yl8AtaeiTSY7IkTubifUA2K9cwuVeJJkwycqA0k_5_dFRq3yY2HmhSftJ0K_flJjekJ6ppeFX9uON4oJxO2WbDLJMSsza11Ma_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=PU-DpTBCPY63JWnj62ZdzCrOhf_7Lp_sxEIlOVFxpRU_gjIGoWBWqrtiHkzRO0vV7ut0xVCMQT2l10Vv90DKmXjF1l9BbDTMlfwVB3c5UtVzuGgPP7a_q_sFJiyNWfddL7DMYBcpoZj-w4__fPH18pHo672OBB4GE2C0KdGrZbnrMY26kuYfdGdYXgOHDZ_AHwRAmWIu59Zp7OeH5xqfEA5umm7TzdaBYZnFNwi7I5zjaUGzXF4Yl8AtaeiTSY7IkTubifUA2K9cwuVeJJkwycqA0k_5_dFRq3yY2HmhSftJ0K_flJjekJ6ppeFX9uON4oJxO2WbDLJMSsza11Ma_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87750" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87749">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87749" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87748">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87748" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87747">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=aQ5q4JVak56zcE9mG3EsxoFGgnPyCYtosc_YHc7-YSMh5jItPw1ND0NUaj-bCFKwj4is86DCTK4xUeJAErwg3aFe82_O3gLpRKDqYp2Fmx7XQLrmD9IzeYPKC1OZ5OKNLJM2231zEDV9KqynzU6WXgSx-oboEe6NoMpEZcNF7udo_1K9Ho7FqfYIKSzW8seMf4zZV-I4_bvaYKN-GUuBIk3clJ38nZcmptBAKslbh2AH7cuKMeDeMhQ6OgZEw9RRu-wmlOEYj5TPWfKjRkNvx0B-k8CkPT2VSwPVaRHs8nld4KDzDm1MgxDWjaLaWtno4znitup3YOxBCXGWsLthQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=aQ5q4JVak56zcE9mG3EsxoFGgnPyCYtosc_YHc7-YSMh5jItPw1ND0NUaj-bCFKwj4is86DCTK4xUeJAErwg3aFe82_O3gLpRKDqYp2Fmx7XQLrmD9IzeYPKC1OZ5OKNLJM2231zEDV9KqynzU6WXgSx-oboEe6NoMpEZcNF7udo_1K9Ho7FqfYIKSzW8seMf4zZV-I4_bvaYKN-GUuBIk3clJ38nZcmptBAKslbh2AH7cuKMeDeMhQ6OgZEw9RRu-wmlOEYj5TPWfKjRkNvx0B-k8CkPT2VSwPVaRHs8nld4KDzDm1MgxDWjaLaWtno4znitup3YOxBCXGWsLthQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات الإنتحارية تشعل سماء أربيل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87747" target="_blank">📅 02:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87746">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=urTT6j8o0iU6j07Yd_uX4oL0Y-TEPIOq3ETqCPVa8iMFFFJyyObwfYEdppTfjDqcDZqWx9OM746zYrzlw3H4B2IU_BAPjXoxhKi55Rz7DQlbNcKhJGwheBh7p0edaPIxZZFw1Ob_3kPe0rj5jrUug4FQ_29Nza5AwUdDtM-LwmQN4Q9kSVjQkcq7UnCLf6ISWpStRnjSzOqh7xX3_k4grGA0RdNyJl9TNR2xmmYDP-hzttQoYjfDC8DHnrVq01KrPBAsedFnd54DibhKL4jkXaIoJ18I5HN_RbzawxZ80e4O4ESNtNCgliPuSVCVZQFCdbYK-Dgf3IPpZXsQ02qjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=urTT6j8o0iU6j07Yd_uX4oL0Y-TEPIOq3ETqCPVa8iMFFFJyyObwfYEdppTfjDqcDZqWx9OM746zYrzlw3H4B2IU_BAPjXoxhKi55Rz7DQlbNcKhJGwheBh7p0edaPIxZZFw1Ob_3kPe0rj5jrUug4FQ_29Nza5AwUdDtM-LwmQN4Q9kSVjQkcq7UnCLf6ISWpStRnjSzOqh7xX3_k4grGA0RdNyJl9TNR2xmmYDP-hzttQoYjfDC8DHnrVq01KrPBAsedFnd54DibhKL4jkXaIoJ18I5HN_RbzawxZ80e4O4ESNtNCgliPuSVCVZQFCdbYK-Dgf3IPpZXsQ02qjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف بالطائرات المسيرة الإنتحارية يستهدف مواقع الانفصاليين في أربيل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87746" target="_blank">📅 02:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Bk2MyRBemw1dHJZ9u_xk52bD8momK8-xJVYcWFccOxpcpIcV3V7H2vjin9kgGcSeD0ns5G3_DXUWmpNHDxR8SrABXpvWEjViLTTL1T4Iqr0wUvrgJngHFGPrs7DGiBBIDNemPSFkKo67xPfoZZ70HRxIrzmXIkiNMaRKi02Q0HYTwlcAar7Um3msTc80WkGhJ7_Yb11VyZFvMgF6p9LoPhJKXhW_3OWFUGG43QF3ZWJjeoyW8M2SJvl2vBRncWnGDcXMAbfNrq-aeIXW_USBonR-3Iz0v2cXp5ZK_JOTdQN-dVbLy9xc1z6-QeE5gjMU8JsKWAOCs1n9qxRVY4FPMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Bk2MyRBemw1dHJZ9u_xk52bD8momK8-xJVYcWFccOxpcpIcV3V7H2vjin9kgGcSeD0ns5G3_DXUWmpNHDxR8SrABXpvWEjViLTTL1T4Iqr0wUvrgJngHFGPrs7DGiBBIDNemPSFkKo67xPfoZZ70HRxIrzmXIkiNMaRKi02Q0HYTwlcAar7Um3msTc80WkGhJ7_Yb11VyZFvMgF6p9LoPhJKXhW_3OWFUGG43QF3ZWJjeoyW8M2SJvl2vBRncWnGDcXMAbfNrq-aeIXW_USBonR-3Iz0v2cXp5ZK_JOTdQN-dVbLy9xc1z6-QeE5gjMU8JsKWAOCs1n9qxRVY4FPMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87745" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87744">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=KUNt4erueYHJMfDpcL6vPZFU3qLQmI6D18f-JfEnEB_QYrDVqCKnvvRTuZDEBzFwrdwmPAFtn-_6v9OOak0XJRzqTWUq0yGpLbhfjs5QzhNrzASoJLYFxxzCTyoGCmdWZdqViRduzGpW57eK6Z-NF_myabEOwF9woB4NFaRu8MqRtDWKnjzT4NM-AJqX_NPUth4Nw8kmpiUaFkHV2GEcDAYmwNeB5xgtm-m0p2Bm8yo_CNTl4e8cJ72FrKfY-LvhlWjuLdiWdBg64raT4zhNY3wr_zMIxrHOPBh_aOQ9RM5zNrnNnu9QMmDAz9cypkBQBicK8TaGYkm2XQlONik22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=KUNt4erueYHJMfDpcL6vPZFU3qLQmI6D18f-JfEnEB_QYrDVqCKnvvRTuZDEBzFwrdwmPAFtn-_6v9OOak0XJRzqTWUq0yGpLbhfjs5QzhNrzASoJLYFxxzCTyoGCmdWZdqViRduzGpW57eK6Z-NF_myabEOwF9woB4NFaRu8MqRtDWKnjzT4NM-AJqX_NPUth4Nw8kmpiUaFkHV2GEcDAYmwNeB5xgtm-m0p2Bm8yo_CNTl4e8cJ72FrKfY-LvhlWjuLdiWdBg64raT4zhNY3wr_zMIxrHOPBh_aOQ9RM5zNrnNnu9QMmDAz9cypkBQBicK8TaGYkm2XQlONik22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87744" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87743">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=JM2W5j7maXd4lYltB5MRxyaYCdg3s8Lt0hLSNKtcas8r2kZlDVaXvFD46tv6A59411bFYQVIMONjFxZdrYfPlNkxQg6IDYDtXsx1V-uIqmdldt56WIaYv5jpU5OoHlZVpbRD23FfhSs_eV5YadzyWWsLKkiqk2txJfh8q-3itHAkp-1mIKVFxezb2dy4X67V5tbyPDjmDs2TL1gg6h9FVuxl0g5yoB4oVEyKhoVJnsnKrrshevS3xSx3_o84PbIyTyl65aUSJufrEwCqZPukPdIzl4lzyCvfxzLhtvsNcXVvc8Fc_inP6sAsR3BwFKTq74sI-MxFnlP92guKxY5LmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=JM2W5j7maXd4lYltB5MRxyaYCdg3s8Lt0hLSNKtcas8r2kZlDVaXvFD46tv6A59411bFYQVIMONjFxZdrYfPlNkxQg6IDYDtXsx1V-uIqmdldt56WIaYv5jpU5OoHlZVpbRD23FfhSs_eV5YadzyWWsLKkiqk2txJfh8q-3itHAkp-1mIKVFxezb2dy4X67V5tbyPDjmDs2TL1gg6h9FVuxl0g5yoB4oVEyKhoVJnsnKrrshevS3xSx3_o84PbIyTyl65aUSJufrEwCqZPukPdIzl4lzyCvfxzLhtvsNcXVvc8Fc_inP6sAsR3BwFKTq74sI-MxFnlP92guKxY5LmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87743" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87742">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87742" target="_blank">📅 02:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=pLBiYgl0msv7aV9JClqeYphE-AyjHBrY0U4rfcUtVKdZMCeKPFcCT5iNz8c6sgFP_M923ZuWF1zcRG6YIwJQsO5HgWkBX2Z_D1I_xUZRzUmMHufXb08OoTtC4VfTv17o3d2S0DPyGZC9oYu-kWxtJTEcyFtxCzsqkMJM3QBXclrTecYo5mOgraPn__zvSTcQQot23WjS6GdUlpvIaG8OtT9Tah-bbh6g0l3TPD9Dx3wotjf5blVa7Wu4_N7SdhH3RpQMy1yBDJdksuvaZIfvIrP-6h-nHjDfGvDKyDSJ3THZKzBMQJce8vXIo9Jc0YlaW9zl0dHn4_4Yd3J-zDVdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=pLBiYgl0msv7aV9JClqeYphE-AyjHBrY0U4rfcUtVKdZMCeKPFcCT5iNz8c6sgFP_M923ZuWF1zcRG6YIwJQsO5HgWkBX2Z_D1I_xUZRzUmMHufXb08OoTtC4VfTv17o3d2S0DPyGZC9oYu-kWxtJTEcyFtxCzsqkMJM3QBXclrTecYo5mOgraPn__zvSTcQQot23WjS6GdUlpvIaG8OtT9Tah-bbh6g0l3TPD9Dx3wotjf5blVa7Wu4_N7SdhH3RpQMy1yBDJdksuvaZIfvIrP-6h-nHjDfGvDKyDSJ3THZKzBMQJce8vXIo9Jc0YlaW9zl0dHn4_4Yd3J-zDVdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في محافظة اربيل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87741" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=sOARB31MylyDqPCH4lim1TggUBvYUoGf0Wzg0wv2RT44dJWDV5nmzWafkX5OLNZ0ge8LCJDNK2vnMIffXaToqJ8Xl12UzcZ3sCbmLhApddQInaRiEQygO4y8-1hpKSz_OPLkWUDyE0T8TTnoHSGTR3GjlbcUTv-7i2iaKp8zEjpzTns4q_uzJUaQsvf-fdQw84OkgqEodxVaq3ei0MutGrtMyM4DZqwhXR_m_4pcPQ2KrezP-iZt0ubeTOiKsAHrLw_jdRaOyaVFMDKhLjQ1Xq_lM7R5gLk3O4Q8Kg2TYsTUMzvVZOMoUKeUisXiT3wRx2B6sBA4fxLuKqvlj7bnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=sOARB31MylyDqPCH4lim1TggUBvYUoGf0Wzg0wv2RT44dJWDV5nmzWafkX5OLNZ0ge8LCJDNK2vnMIffXaToqJ8Xl12UzcZ3sCbmLhApddQInaRiEQygO4y8-1hpKSz_OPLkWUDyE0T8TTnoHSGTR3GjlbcUTv-7i2iaKp8zEjpzTns4q_uzJUaQsvf-fdQw84OkgqEodxVaq3ei0MutGrtMyM4DZqwhXR_m_4pcPQ2KrezP-iZt0ubeTOiKsAHrLw_jdRaOyaVFMDKhLjQ1Xq_lM7R5gLk3O4Q8Kg2TYsTUMzvVZOMoUKeUisXiT3wRx2B6sBA4fxLuKqvlj7bnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87740" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87739" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل  ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87738" target="_blank">📅 02:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلزال في جمجمال وكركوك شمالي العراق</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87737" target="_blank">📅 02:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل
ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة الماضية.
وتأتي هذه الدعوة في محافظة بابل التي عانت من أعنف المعارك ضد تنظيم داعش الإرهابي خلال عام 2014، وما خلّفته تلك المرحلة من مآسٍ وتضحيات كبيرة.
📍
المكان: بابل – المسيب، قرب سيطرة التحرير
🕒
الزمان: الساعة الثالثة ظهرًا
يدًا بيد من أجل أمن بابل واستقرارها، ورفضًا لكل خطاب يدعو إلى الفتنة والعنف والطائفية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87736" target="_blank">📅 01:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87734">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hc9CBoBQYivvEVj7NdSh4pWzfN6No6nJUqnbfzlWQC7STZOt-oG2zrM3qEiPyaREpVGLHq411Pi4i7T3buQ_QUhNSPw3uffT6XknCs1gCUAQQcsCLNtpdy-El1QYG4DhSxvDgodzxp-_vvFdW_4r5slM3YP5rhHTT5TiedAwVC3DfDq5bUj-dYljIp1kKAKHso32O1UGSO_U1BQe0Yv1dJ1nn_9mZ-rUVKUGG5lhmRz_T1pIVkLh540OCcXptUWCkquPIZDfPQWq2BAmr3NKTxU5Su8UI3i9c--HE3zIhVqtgZttmTDgNyYeC72R5zL418rq7B2JNGlpTqRNfuLPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qc6_-KoFPtOv33ozPix5EC2ISGGLjX3Zl1317Wqru95xlN1APydkRC1dT__HjdeJCwtS82yJVGT2TeoXJ6e-fJztcY8X_p5a3tjuEQjt4FEttNiOepdYV8jPckNN3t5yySW7AQHfZaLTFpdXlVpaR7C1QZownbGQZboVEiwaJ9uToVPMP8wrwpGKQqwIphGzPIqu4VIzPNS---eXoARL-EBKebgWXY5D9KMuZnTlpvUz9kCK-XHSD59_6f_WJFllibR85Dpvlru5Ldr2dBjsTuyltn-KYV5fWz_Bj8Ud6CCoQ0kR33Yp7rVEqTtJzPUENzf1aZz_heCD_jfL1fqFQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
إشادات شعبية في الأوساط الحشدية بمواقف مدير المكتب السياسي لمنظمة بدر، ودفاعه عن سلاح فصائل المقاومة العراقية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87734" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
‏
وزارة الحرب الأميركية:
نراجع حاليا استراتيجيتنا النووية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87733" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEnAD-yy15lobdckLK5LZtzSb6xX6xtPZ2xVkDLLepvLWXL2ipkH4YUywCJu1MDTEnEh8gzvL8UD4__8dUrnxHoc1wlixkXXDdTxKrri4mOk57AM_8_P0sKh4jYvB8_YUTjIfxoZICYm-KQ-Jeqz7egKAih1586DNzfgsT4P_cp_e9-KM-kXfjxZgb6y-dvnLpzu5lf6IDv9WbA5NMmGR-gUv9RVf40lyOPGRiELVXT1y12_8XILhlQEKumb28Jjbe1Z2sq9Z3I5zHiVOGi7-6WmX7uPYgHGO2_Q9LExjB0U7r6qqIJYFVSDt1JYtlhsaQYzFDD8CbQEU4EY5WxvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأوساط الثقافية والسياسية والإعلامية العراقية ترحّب بتكليف الدكتور عباس العنبوري وكيلاً لوزارة الخارجية ..</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87732" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شركة أدنوك الإماراتية:
تعرض سفينتين تابعتين لنا لهجوم أثناء عبورهما مضيق هرمز دون إصابات.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87731" target="_blank">📅 00:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
‏
نائب الرئيس الأمريكي فانس بشأن إيران:
هذا الأمر ينتهي بنا في موقف قوي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87730" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87729" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGu7FgDJ3MowM1Ryx-9cf7GHSRI7IVkr0W1Llwf9-tQa3Xh7JvVSp3J7m-Sm5xOt2rpZ7TdNCA1pcq6wb-4na7qonrRqrVIjj6MrNby6c6ZorOxov967DmWT0kCBxfe230nFwh2avSZuxFN0YdbuI0kLI2wFU64bcKw5cF4RixTSdIMASAfzg1_O2YCGK9ZzphTAEdl9GJWV3GAFIItrwSy8xc0LLOjOoowfd2aoi6tWlj92sFMmDnqs_pTM2dyS2-IVop3qyGuIM1WeyuAcAYC0GywHWgyB9l_-2Ba6LXXJHq9CarxB0YyCioeJ5vKdD3x60ELNGyRVIAZcsizHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
جرف النصر .. كعبة المنجز الأمني العراقي الحشداوي
دول إقليمية تريد عودة مثلث الموت ؛ دار استراحة المقاتلين العرب ؛ مضافات ما يسمى ولاية جنوب بغداد الارهابية ..</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87728" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87727" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في سماء محافظات العراقية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87726" target="_blank">📅 22:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=TlKpchmVs8Yav8D9Gc6lr2619uVhyV4lvk510zM0JUGRzKVboMGBP1PKQDBeg5OV6OWhVbe0r1EGGp2bWf8M698XZu5hZVIbu_DvwYVUe3NHlBOaS614kVvCZY_yjT5egB6vjA9SE5NDcCurCpNEpGgA8_bFFH_ZyouJJrawdAUYrOyRy8u-F7SmibJbqzX8bd9Sc-DyVT_K0pBYTzs9qI0ZWCU_j1kFsoUdGjfCCi0HKhIf3TpV6FplUWo01P64EOrW8-Cc7FYOfsn4yZqdYjTxZS-BwbMbqxSVzjcPt77LV6TDkS2NB_4cLz0Gp3T5fFKYydxW_IMa4kYoixq9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=TlKpchmVs8Yav8D9Gc6lr2619uVhyV4lvk510zM0JUGRzKVboMGBP1PKQDBeg5OV6OWhVbe0r1EGGp2bWf8M698XZu5hZVIbu_DvwYVUe3NHlBOaS614kVvCZY_yjT5egB6vjA9SE5NDcCurCpNEpGgA8_bFFH_ZyouJJrawdAUYrOyRy8u-F7SmibJbqzX8bd9Sc-DyVT_K0pBYTzs9qI0ZWCU_j1kFsoUdGjfCCi0HKhIf3TpV6FplUWo01P64EOrW8-Cc7FYOfsn4yZqdYjTxZS-BwbMbqxSVzjcPt77LV6TDkS2NB_4cLz0Gp3T5fFKYydxW_IMa4kYoixq9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد لصواريخ الباليستية التي تم اطلاقها من قبل انصار الله نحو الاهداف الحيوية في مناطق تمركز عصابات السعودية في اليمن.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87725" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKeNOeADKKo5jQdFNX706QLv9VaLEveIJb2IftX51dy9WusCt96tYfyG_PolXgc-0pHcO6L7xNwkM5c2Ce4Jrq1qPpyQGOIFFvpZMrPCA67cY6Ch8N5h8UsL6si_SlTUPzzGuPuyCytimm7xGrWQTxrxZjwGgub4-d___cZ48EboXR9sruM-nD0qBLvboheq-TirEHztjAKOyc1FLul5FtEYBPS253GvMzpk4azFUGrcR23n3BTP1TBQKpsXZnVVrKw7CXNFR86CxmA7T21tc3v3ZS4djWXk1_UhOd1gKNRSLNQUWhAeb4l9d9k-P7_BIHE8GWetXDQvO0dntUjqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87724" target="_blank">📅 21:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irPdrK1K-CQ3BcJhdiHTEf4MncWxnzHUExFZhxnlxEJQ2uoLjggro6OD8JbTujnaHqMgjBRbw3YFZFLBjA9dyks9biF5t9fQsNj39eX5-CRhtOSTcINJLqFJBjT_AjTBl69wbDOJ4GAV6XsNyaRJu_trJaWPohhtuHE89mdwfy8QmtsgiVo9g4PqWJr6LmlwUFdVvml9Y-cbidtBezU1NczX9dtLxu8ZJV80usfNuIZ3MB1VMs4HSm1n3tKLhlyMu9HYWRFi5z9kCr5zY8Cq5AxnAFEKfLYdjfB9NkrNk7koIqVCLANJy7Hd3Q8XLpKrY3E-oZiyaX9mZQ26PnPWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تخوف جماهيري من عودة مضافات ولاية جنوب بغداد
حملة إعلامية مدعومة من دول إقليمية دعمت ظهور داعش إبان أعوام ٢٠١٤ تطالب بعود تسليم جرف النصر شمال بابل بيد الدواعش .</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87723" target="_blank">📅 21:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfLlkJCIuc_o2_htkCA0KEGrvNpeSZq68AYM_5vecyM5MXBvSVT-ZboTeUSfnSlXejk0Tc06AtIKCI_5djOAmiUoFVJ7HPa3lbTRtc_CSHT8RLxunVUrKtYkfHiUjOSq7Vs_NSoezyOpcTcNMnfYkQLlNz2wNybCJCpGGNuPad3Gmo4NatpMuw6G1kspmWLGA3khJElFV4DEEiDc667zyqUZAGBz2VXjS87VqkD5R6ZtdwOWrykH8_4le9p-RBBrTKf3fIjX2mN0SgsDXyLS3ipGhu_Wk8WGZb4xu2fZwg2Nbu8i3_1iVZik3dlFy7UiZsZMrt-pj_WoIso6x7WBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87722" target="_blank">📅 21:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87721" target="_blank">📅 21:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
‏
الاعلام العبري:
قائد سنتكوم أبلغ إسرائيل أن واشنطن قد تضطر لاستئناف الحرب "إذا لم يكن لديها خيار.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87720" target="_blank">📅 21:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=UYum9FoYg9MGMA6eBhHTnsStMRPRw3MA7KAk_DCdaUBv0c_1g1pLvf1RZfYUefpObR9MpNUz7naWIukpM6fxXWxLj5wICr5NZd8Oec_r_B7kXCbnmjMIUpeIv1-NRJAoQhpEXBkb-AR2bjRVs5E_tO5OQZO3PinpHRsIIG5Ki_6QlnHn9IlyIbMJxyyTQXayQQlabL9AULIBQZEQ7iRpXYMhhc1FHKId5d-jHwpa5S28gF1yl16RDj8SlrtE8_Xkj7St3EJhxFPl7QFapTyWrnzdQuLR1Qj66xttqKbJkV2VGu11fVaoCUGGjmyShxpUZcIXVwMKfy29nQLn5yRVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=UYum9FoYg9MGMA6eBhHTnsStMRPRw3MA7KAk_DCdaUBv0c_1g1pLvf1RZfYUefpObR9MpNUz7naWIukpM6fxXWxLj5wICr5NZd8Oec_r_B7kXCbnmjMIUpeIv1-NRJAoQhpEXBkb-AR2bjRVs5E_tO5OQZO3PinpHRsIIG5Ki_6QlnHn9IlyIbMJxyyTQXayQQlabL9AULIBQZEQ7iRpXYMhhc1FHKId5d-jHwpa5S28gF1yl16RDj8SlrtE8_Xkj7St3EJhxFPl7QFapTyWrnzdQuLR1Qj66xttqKbJkV2VGu11fVaoCUGGjmyShxpUZcIXVwMKfy29nQLn5yRVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
السلاح الذي حرر امرلي والجرف وسامراء و بلد وصلاح الدين والأنبار حينما هرب الآخرين هو الحصن المنيع للشعب العراقي بوجه اي مخطط خارجي يستهدف الأمة العراقية ..</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87719" target="_blank">📅 20:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام صباح النعمان:
رئيس الوزراء العراقي وجه بإنشاء صندوق لتطوير الدفاع الجوي العراقي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87718" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
سنتكوم
: إنشاء أول قوة مهام متعددة المجالات ومتعددة الجنسيات للطائرات المسيّرة الهجومية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87717" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA2EQWPk_m8l0Lg1GDJ1YgpOsgJDaRTd1CMLUa1us0jnfO1-r-nIAn1V9w6SkuG3816FwhWsXTWo6YO0hIVtMw-tyz4GNZk43x29RMZ8Rv5l1xjuF3gVkVBIzXApn-3zMkmNZrka_UE7aEoZIgWq-YaysY0eecOPZgI7MbXVUh7Pqs8xwrwiq_Las3dyElPo_3JoMjUbGnGrgSpSXYNeMWfZlXwI836-yG2kQCVdcYJsObCpFJ1uMDOcuFFtano6SWaJff885L0rw7Dyc-rZDLeI1qG4p8s0O6UGQsMWXFUsMupavOY6GQOKRIHMIi8eqe0QLmg2aqKVo8qwlIOSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحضور الإعلامي للمتحدث باسم المقرّ المركزي لخاتم الأنبياء، مع ميدالية تحمل الاسم المبارك للإمام الرضا عليه السلام.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87716" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
أعلنَ مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف أن يوم غدٍ الجمعة هو المكمّل لشهر صفر ، ويوم السبت الموافق  (١٥-٨-٢٠٢٦ م) هو الأول من شهر ربيع الاول لعام ١٤٤٨ للهجرة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87715" target="_blank">📅 19:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇸🇦
‏
وزير الدفاع السعودي:
العراق سيبقى جارا عزيزا تربطنا بحكومته وشعبه روابط الأخوة والتضامن.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87713" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC5WHxkB71UUULkJL2rEFdeQi5F_SeI8nrAH6PtLX4LCTFYxPWjFYQ6t1x3h377sGwvZVrXfwk0ONkoB-3jwyaEMl9KP5GT3UKJkOujk96oVuoVTQmgme5tgaMSlwfJCgn9AUNyjxh71kCQy_7c3C5s35CWJ-snlHrP3VkRKBSsOxfPzJD8v_sNiZxY4ptOOTDaKttITp2Nd5xe4xi0ArxN2oUKcBuMKFbzKvUUhYbDsMHPa51On0GYB1JValQ92Dk4EJCW10G19Pe3pmXmKfUOAWEJ51lRYB1g9oVdnwmK7yQyNsFipnOBEACRrc26BC92g2nQg5atONglwIAwQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الجيش فقد 45 مسيرة إم كيو 9 في الحرب مع إيران ما يعادل نحو 25 % من أسطوله.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87712" target="_blank">📅 19:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية.. السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87711" target="_blank">📅 18:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87710" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87709" target="_blank">📅 18:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
‏ كبير الديمقراطيين في مجلس الشيوخ لشؤون القوات المسلحة السيناتور جاك ريد يدعو وزير الحرب بيت هيغسيث للإدلاء بشهادته أمام الكونجرس بشأن حوادث سقوط ضحايا مدنيين جماعيين ناجمة عن الضربات الأمريكية في اليمن وإيران (مدرسة ميناب للبنات).
‏
يلقي ريد باللوم على قيادة هيغسيث في هذه الحوادث، ويتهم وزارة الحرب بتأخير تقرير الشؤون المدنية اليمنية لأشهر ولم تقدم حتى الآن بياناً منفصلاً عن ضرب مدرسة ميناب</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87708" target="_blank">📅 18:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEhXJvpcvuDZmwxZykY49Rv7FgfeW9aZMHW59rMfan9Cw1J5_gq3OIaYNEaiv6zy6NZ3-UJzrj9QfYHKgB-KQ5feqz-MVqQdKzoiWG2kfxf-guCsfXSL7BhdWW4GtjIHyfpABvm9jgiTfpzV_lCKmnV1m73JJAAJahgdfBsxm1dYHPGrRGpCEFr3GCqIKxoTB_T1ts-vIyOlaw-uoEx1o7HNQOnMg05ZlG0Obgd8BBqIetwnNYU4QHfy_tUhhAtTtBSNx2q-AjGIkOd2OzKAD59SjTYIXQE1jmJTSwzOR5s93LPhOqlrmpEhBU69rmEOBEYaY2Bq5jtXI6rAM2BSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قادمة من سوريا.. العراق يحبط محاولة تهريب (45) ألف حبة مخدرة كانت في طريقها للترويج داخل البلاد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87707" target="_blank">📅 18:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لحظة إنفجار كدس عتاد في كوليفررو جنوب روما الايطالية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87706" target="_blank">📅 18:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVG_1LO-dA4lfY5i3p6YummsxgOx7w2t8X9DZ-6s1U0vXbX9GoIjUz5mg9YzfGPRm8tTHPd1UmsTuz_4YXP62J6e36tVmc2wP9bfuXdRvuREsVlh7_FA-QIEpSMa1a6YQe9A7mX09Tx2EG4Q3GwbF7eW7HEGrc_ecF_dyyz31GIAiqARfL98GNf-972R8u92_leN2MR369wuJmvBJQhJ9KoDLNAGImV60ei8j2Zn-pSwi0xTi26uiUes3yCBQzfq3A6k1TSjauove6eHHZ8uhkfRmvs83BvXu67jHwZtUGblFL3wD0ml_0BqOoh3hRSA6d0Ut9pR2EuFIdewt-s8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملك السعودية المرحوم سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87705" target="_blank">📅 17:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">السعودية تقرر اغلاق (‏مطار أبها الدولي - مطار جازان الدولي - مطار نجران الدولي)</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87704" target="_blank">📅 16:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ملك السعودية
المرحوم
سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87703" target="_blank">📅 16:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بيان مرتقب للسيد القائد عبدالملك بدرالدين الحوثي حول الإساءة الأمريكية للقرآن الكريم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87702" target="_blank">📅 15:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=DHUTXEIPDL4kKY_JoVA3CM_qRyRBzeRaSt8M3UZ0UNbFmUmRlLXczuaHhpPH-lVK3LkKG56c2oWy_1Q-uCZek7yZrqnMPj6MQ8SwcP9whmXMdPpwwWAwKSRen0IPlTpt5KRKp6wNuQsM-ZjE9dZdCulx_BFn8clLnPH54XqPuqww_YJVp0U7BB47y-34iUMs7KV6DQe_7Rpwy6DjZVNy8OV426xk3NL9H1xxy7zeUVNnBueh8SA-njv7TjlPV6Ql4_z3WO3ER6lUNBhGnFbHpIxPXSPYC9z02Jels3BlWD6LzD9MTzvJ7uR6UxETbPw1Ri6nLDpw3vdTgypemiBHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=DHUTXEIPDL4kKY_JoVA3CM_qRyRBzeRaSt8M3UZ0UNbFmUmRlLXczuaHhpPH-lVK3LkKG56c2oWy_1Q-uCZek7yZrqnMPj6MQ8SwcP9whmXMdPpwwWAwKSRen0IPlTpt5KRKp6wNuQsM-ZjE9dZdCulx_BFn8clLnPH54XqPuqww_YJVp0U7BB47y-34iUMs7KV6DQe_7Rpwy6DjZVNy8OV426xk3NL9H1xxy7zeUVNnBueh8SA-njv7TjlPV6Ql4_z3WO3ER6lUNBhGnFbHpIxPXSPYC9z02Jels3BlWD6LzD9MTzvJ7uR6UxETbPw1Ri6nLDpw3vdTgypemiBHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الهندي اللي يكضي الفلم يتمرن بالجم حتى يواجه خصومه وتالي ينضرب بمسيرة</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87701" target="_blank">📅 15:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏هجوم لانصار الله بالمسيّرات على مواقع مرتزقة السعودية بمنطقة العبر في حضرموت</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87700" target="_blank">📅 15:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:
تودّ هيئة الحشد الشعبي أن توضح للرأي العام، وللمهتمين، ولمجاهديها الأبطال، أن الجرحى من منتسبي الهيئة قد استوفوا حقوقهم المستحقة ضمن صلاحيات الهيئة، وبنسبة شبه كاملة، سواءً ما يتعلق بالرواتب أو العلاج داخل العراق وخارجه، وذلك من خلال الجهات المختصة في هيئة الحشد الشعبي.
أما الاعتصام القائم هذه الأيام أمام دائرة التقاعد العامة، فإنه يتعلق بملف منفصل عن حقوق الجرحى لدى الهيئة، ويتمثل بالمطالبة بتطبيق أحكام قانون مؤسسة الشهداء رقم (57) المعدل لسنة 2020، ولا سيما الفقرة (ثانيًا)، التي أجازت الجمع بين الراتب التقاعدي وراتب الإصابة، أسوةً بأقرانهم في بعض المؤسسات الأمنية.
وتؤكد الهيئة أن هذا الملف لا يدخل ضمن صلاحياتها القانونية أو الإدارية، وإنما يقع ضمن اختصاص وزارة المالية وهيئة التقاعد الوطنية، باعتبارهما الجهتين المعنيتين بتنفيذ الأحكام القانونية الخاصة بهذا الاستحقاق.
ومع ذلك، وانطلاقًا من مسؤوليتها تجاه مجاهديها، تواصل قيادة هيئة الحشد الشعبي تنسيقها واتصالاتها مع الجهات المختصة، بهدف الإسهام في معالجة هذا الملف، والوصول إلى حل يضمن حقوق الجرحى وفقًا للقانون.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87699" target="_blank">📅 15:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
الادعاءات الأمريكية الزائفة حول حركة السفن الاعتيادية عبر مضيق هرمز، والتي تعكس اليأس والعجز للجيش في ذلك البلد، ليست سوى أكاذيب.
نعلن أن مضيق هرمز، كما هو الحال دائمًا، يخضع للإدارة والسيطرة الكاملة للجمهورية الإسلامية الإيرانية، ولا يمكن لأي سفينة تجارية أو ناقلة نفط العبور بأمان عبر هذا المضيق دون إذن ومراقبة القوات المسلحة الإيرانية القوية، ولن يتمكنوا من ذلك.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87698" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87697" target="_blank">📅 15:35 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
