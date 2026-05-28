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
<img src="https://cdn1.telesco.pe/file/Uan0wCWYimoEGud5_Bm-atjSy0r3UofOMpcIavbqNtaPkIXapq_S2vRPKDxooFNAQsZdxWHgBa3tjprTM-gQVibpFnsR7Hb6NhZUXeLJYuOqiAfLnKlDSV97hUSxDz20id0NTJ8_Jj3P7Ccl5eEybD6iaBOC5y_tE7FTUAVAtFvpmwHTVhOVjSIfYG3I0b3qbwJWu5T8T52ObU8NfUH1Q3m67NkwoXa8IXlKhvfKiuBJnvdBoY1tC_WOhFCTknp2A4G3p-Nl-49X5z057tUc74lzyv7n1K6kZ8pX75G7Am994ShlM7TtdDN4CvBLIDDMTHcd9o95DqdO6ZR8Nvg_iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aI3XbHzTW56SRZi0WfwaYCXPMfYBlXq65SCbSf2Km4llk4DIUpO7t3bNxmODZXJzcxU3x9x8mwU5IwvIvPdmEckpkmBK_TAIuH3dDQ_YP5mRv4GC1plW3RGMeyWxarmYL1hP7kwnMg6yXTgSC0N6dGsS8OT1uvX-QkqaHUizFZnx1KASoTWXpumRaUtyoBkPnVcSmdl8clD-vgNEYHXRAoyaXArK_pefYJkKM2NmeSnGb2n1cCgFnfwh7hBou77MiLcunCSNuirRZPSvBilXt9T7MUJWbvWQrGC64Zp-bo3atTTy_gWChtvYN-CvWHMEyqf-T_heo1dNIjKnDtJswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTk5ny8pdIFa0X11OWCYOQEc7GlM74153booKc_Vlfwtnqqjphj3-q-_pxxPtKTWmV8WWkDAzugd9t197lHR1mB7DmreVy8l2P25TlrSoQBgfjybOBJsnH-tQoIg9SbtE8w6AzIL3z2jXdvahdwBJWMY3Fr6CTz-dNSXYDAQtYYIQIINyWEwexsxTx1dWXo6-3xIZq-SrF7KIn8A0WUBb8vKstznhpKULcsRmnkMFIotCEhBWzfaKdUhH1nSSp_Lrrym15LqLJyR3Aa0V5zCTeysp8JoOhdgSrhkeLmmvIvVXqbDLelGXDGjeLgz1Gm5llrUM5H8Tdx4LrmlsSxbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N4r5nqEnfaWFFMhEkyXbbT4VEYIFGj15m50jkrKpPweiOfRcgpZQL1ydwO5iMLoxo_s86pkBhlhTZCDPABWfni7oo73tFMxZVLcSMOteQeu5jfQHx8A2hCPKegX9FZg2yL4EcfRIBI74BMfau3_LlrFMTuYpLKScubyRMFtZgjwU0-Ut5SV6K1-Rw7O1wrR3FZ-PUiPgR6vjzDvIgbQBLetdxf4cz0BB2Rrvk6k2ngw_gXuiYANagLAs0f2LaATnQW9O6eVx4DNIVr5ZiDXqdA-C3bk5NavwhIKQAiVsgvRPhkSLgbdwkWKBUcikvyrWlPbMynggczmovNZMZkY5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sJVf3AAm1nfHue6ure9T2NCbJP1_0nGHoKWK80LHsHjVHpQqmg6fVS8QfRYSVWSyc21U_8mQUbvBdASHhHI6YSwQtgw38969zM2VskT5rR_K8SaaH_X4X8IqtdWkR5bDiu2Dp7KZDvoD3xXTjYFX9PDX1MsIFhMb6Snp3Eoi57g6rpw_LO6JKWsZNxPJbYwXOvaim1RUo7IQpmxtPCu5Fd-xWI6aN0jNsXWfNI3Mx2swkvVFCC-7v-OQmNgOLf3We5e_DVZqIinbVA25wqSKoyGupdibX3pnC03hC91Sjty7Tx_oL3V0jKIb97NbOj71YOnJsUpcxbUjx6dz8_pXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dmVRuaqRpP2PYftdNp8qB8tI1pnwe4C5X7N3kFx3mNTHjqrUFdRSy70zcSfKXFv-Xuw62znHvjrKHQhd1IEU3MIXRdZ3pxEfb6KcEyuYPGhqtPrm0pBvFChF3FSKb-mlgAIVIdYc3MK4i76V1mDGw0tdz3NESXqKoYUwlQ-V8V2GRGw-UitiFA77nld8hZMPgxVNlmkkUJpN1887ej8WUT5OPC7YC1pJzF6Axtb2LSKzIV0ApQF7N4bzXOpTq5HN9F_ZICKAr9XRAYZWXCYiSvV7vZgg5_1qjqp6U8eothCaEj3nfdVGnJ8bIquL69_QbZ6yqyK7XttPwptimbKMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZstO9BHIMUE88apHbhlWOt_oP8FMuAnkWkf7mDnirL3d1uo9maFn_Po5M-b_CZQr6FOy1N7UgD_4T_2hk3RfdPOJdiFS2F3Kkwam3YIEXQ1ZK8RLFpb5pCLE85J-MI2dD-r1bmwS8EUlhzZ8MjA1e-Fv9iIHN8AnX9m-ctMQVGbVwGzeAVtYJuG9J7E8-hFs8v2HcwnXKvqsRz-i_7rvVw8tHxc8GZBWoNMkZHFeHAxETBidpwLyhUMUZjErY9uGDCydyUrcQSxOk6kPIrCxCJ6CSgqKtw5_zSBi0E9YjcfYlFggpa1YAv_2tlQFt_GkPz0lxht3HLuB-h4TrmjZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHm8fBNZHt4eEjueouj1T9qCwYN_AsumBiZt0Zy4RDIjjI3d_6jWI0wawS7HBLyX-ow5K5M6o_JD68ufgBhbm_j6KH2wjHR7j_nY7t1p6TfPfmw7Pjd0gb-Rd01uQLaecsbFTdKAkRLm_c8H-r7Tv24Fz4SRtvBaY-fsd2WhOhPtFKQ9i6EuSUIrh0oVs4wKn-k0lUXUbB5y8goQrT-yNNNHsKSCwYhmhKjz5DXoZxWBGvtyoKk1CXh0w3BH8XS_4pif9tcsDgZ9fk4PyyeAM0Y-iEW-9wd1inQ6A69Q4p66mlCbPXOdea-m91-IPGJLxEGOQDF196vW2wL8mjLRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kU2yfE-t84Ac_MOy8516iyoJMR2O1h4NsHAiJllg4dj6K18zU107mTyGacZurSDIoVs4xnGiBMfVv5GAuLDHy5LAoyPgIdAdNLMGq8eP_pOkbMbPqCDTdf-bt3DeABxBxX1POe8hwFmCObzXVRI7H2SoXzimpT6KdkPnI5JAhkt3ImHNCzfDrOMXgCsKGujso5DBFADSwqw_MxNzhJCYwOdEv46_eHC_IPS37o3bFLs-OuwXK_JGcC9YWSoBvFE3RLyEaDw8QPexRslgNzDotQimFWpF7N5_S85PfYrsQiZQV4oMZd2XH9T1oeB-JLeicPPAdpE3NApcLqegvzKSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5K6J9GHmBT1CyyLm3XwFNaaZS9zB7y-btUiFUV4yt7EWMsAGnAZsbUcvNFZXptSE-XFKnpYlogG9kLzWIPTnqgUBPh5Et48IzpGdl-xqeCVOl4YV1OKUlrYTugMUpflRzFNN_w_UtwhqlfPpIIT4sWKt1WOzbkaiOs8V6N6LU3S7W6i9HjqPI30h_P_FwnFJAznXebnfhkTdX-yomHfWjv9vffvJfXQiM1rbcCbhCyM17Wo_0brAAdfnj9XNt8U1vR2n_cCSUAfcop8Eqb7o9tX2DZgpjdHAZ3N5AyA_dTEFkJtJQglcNYkSPiXR8hk1KWM6jwpbwxDFeoJuUeYJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVUcDy_OPwC5p7fA_lUrUJElOJfoPmI6_gLdpdLQIi3y2E76ebQyfJCptO9XhzCnyU-vVYU1FqW19EnnHy_GByVECWvNRraA55NFopf6-o5IGA9lGgmOJmk2cZ2dV0dDDhJAJZdH0FsUBeWDCTL8h9SH3SkmlSWQLhplHGwjnm6xZLarAdckHohWYeP8dTFuPG4gExKzIRxSvCxkf8ffKd-inCQehgz1cmrKmDJH9KFHtzz8Zjy4VlFc-eBL9bZRFGNRrwmVFuqwbZnRLEOZPwKdc2373DLROAF2TjD3MbSoSRqjnn12bJS0l4otSHZ6k8Ckc1lryG6pB_rSuPRuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ji8dFswI5gKRReIipHaStPodZTEEaIAdTCYSKwEo6bPVG4l9GSr8msdNi41cQ82T0ZHwFoQIUn6DLtYu6wU7RXabUx_1o069-xQiFXKDDJ96a4Iesblr2q5fonoCduvAT24sgx1MV2Fs0VHZgYgQrduHcloGzOcjibOd3_Nl0_dXoXr1zpKuv7vMrb04pT4xeV4fqlOLjnDPs66MDzo3DI9Q7fIt3iEETsCJwxZ_T7iLf_VCJP6iarKTmJhXSJzCML4K2HXB8A4WrHSN67z-5tKH4dts1uRAWGd3qzTlGQt4ze6lIGYDj3RiBn2-l-CI_Q-QuMEp7YGXw2LYi09zPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شما رو نمیدونم ولی این اینترنتی که الان دسترسی دارم بهش، هرچی هست بجز اینترنت.
در آستانه‌ی ۳ ماه قطعی، اختلال و نابودیِ کار و زندگی مردم، اینترنتی را «برگرداندند» که طبق مصوبه خودشان باید به وضعیت قبل از ۱۸ دی برمی‌گشت؛ یعنی دقیقاً همان دوره‌ای که فیلترینگِ گسترده، مسدودسازی IP و دامنه‌ها و قطع دسترسی به پروتکل‌هایی مثل IPv6 ،UDP و QUIC در شدیدترین حالت ممکن بود.
دنیا در این ۳ ماه جلو رفت، اما شما ما را ۶ ماه نسبت به جهان عقب‌تر بردید.
۳ ماه از عمر، جان، سرمایه، فرصت و اعتماد مردم گرفته شد؛ بدون حتی یک عذرخواهی. و حالا همان اینترنت ناقص، محدود و ازکارافتاده را دوباره تحویل داده‌اید و اسمش را «بازگشایی» گذاشته‌اید.
اینترنت واقعی یعنی دسترسی آزاد و پایدار به تمام پروتکل‌ها؛ نه نسخه‌ای دستکاری‌شده که فقط اسم اینترنت را یدک می‌کشد.
روی «طرح تبعیض آمیز اینترنت طبقاتی پرو» همه این پروتکل‌ها در دسترس بود؛ یعنی وقتی پول بیشتری می‌گرفتید، ناگهان همه‌چیز ممکن می‌شد. سؤال ساده است:
مگر امروز مردم پول اینترنت نمی‌دهند؟
دسترسی کامل به اینترنت، لطف و منت نیست؛ حداقلِ وظیفه‌ شماست.
هرکسی این توییت را می‌بیند اگر اینترنت واقعی می‌خواهد، باید فریاد کند که این وضعیت عادی‌سازی نشود. مسئول مستقیم این وضعیت، شخص مسعود پزشکیان و ستار هاشمی هستند و باید بابت این سطح از سرکوب دیجیتال و اینترنت ناقص مورد سؤال و بازخواست قرار بگیرند.
خبرنگارها، رسانه‌ها و فعالان حوزه فناوری هم باید بپرسند:
این چه اینترنتی است که به مردم تحویل داده‌اید؟
✍️
iSegar0 || سگارو</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvChM8-jkcYyFWxIRY2ItzbCmFkvrO011EW_y9Etyh_Fpg4iZkmeBzXtiGxzNvgm56daiWKS3vQe5pW4A9qcFIflB_fBm4XOO4y3p1AlrZzrs5UyNGFOGPNBz9guguC5YiaqFISfU7SC99v_AWYzgU2MWlYL8cEruuMTy5A0DvSz92jXISgXfs29Tm3xj4SlI3-ImP0RVf3rboT9E9sgMYItAodZcKl1Be5GlAWwU6X-VbP-X8IbmoyztMH4LtI3H-Lon6LBwG5BttmqjDXT7lqS6ot66MGCCypX7j4nSiruXqwIIFtgF-WhRg25A1MQbGC5UKfhoB1GUCKuXd_mIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni:
certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com, bazion.ir, 8.6.112.0.sslip.io, abadis.ir, ikac.ir, ebooksworld.ir, iranicard.ir, gameq.ir, melovaz.ir, sourceforge.net, google.com, scholar.google.com, libra-books.com, uploadboy.com, soft98.ir, daneshpaz.top, berlin.saymyname.website, epicgames.com, uploadina.com, sarzamindownload.com, asiatech.ir, shecan.ir, par30games.net, 3fa.ir, taaghche.com, downloadly.ir, oldtowns.top, cafebazaar.ir, Shaparak.ir, uploadkon.ir, news.google.com, varzesh3.com, hooshang.ai, downloadha.comfilimo.com, gitlab.com, search.bertina.ir, mail.google.com, chat.boofai.com, support.google.com, search.google.com, vercel.com, farsroid.com, bosgame.ir, 2.188.21.46.sslip.io, divar.ir, okta.com, snap.ir, nic.ir, flzios.ir, digikala.com, fastdic.com, cdnjs.com, 162.159.152.4.sslip.io, hooshyar.golrang.ai, openai.com, aparat.com, download.ir, yasdl.com, pastehub.ir, downloadha.com, iranmatlab.ir, bitpin.ir, Python.org, my.files.ir, post.ir, picofile.com, namnak.com, gov.ir, dl2.sermoviedown.pwmyf2mi.top, nixfile.com, pirategames.ir, balad.ir, supermario.corp.google.com, faraazin.ir, vgdl.ir, aharvesal.ir, chat.smartbytes.ir, cdn77.com, behmelody.in, cup.theazizi.ir, alibaba.ir, zarebin.ir, patoghu.com, subzone.ir, navaar.ir, zoomit.ir, rio.ggusers.com, linklick.ir, gold-team.org, dlfox.com, centos.org, fidibo.com, tamin.ir, guardnet.ir, atlassian.com, 2059.ir, site.google.com, sheets.google.com, react.dev, irimo.ir, m.ulni.ir, 2.188.21.130.sslip.io, f2me.top, myket.ir, dls2.iran-gamecenter-host.com, Telewebion.com, airport.ir, ubuntu.com, email.google.com, radio.9craft.ir, torob.com, vercel.app, rubika.ir, dic.b-amooz.com, mizanonline.ir, 87.107.110.155.sslip.io, chess.com, gapgpt.app, ninisite.com
لینک دانلود اپ
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhAo5XITItQZDhdIqMcI9UIQGyyXsg8eXUU1T4pzCMh6z0qn0Gsw9REAi2bNa61lPVW33Dqae3QZWeZQWbzpLOA3aP9JpEn0FCDb0HT0Xx8YSYrCHOsF-9wQwxoBz7NKMq5Aq9TQXY9kzdthrjHbZ79lYikhdpeKgQOmfkrT14HZ-E07_9fRHVVZK9HPQKoZDhCD9wuFZy3THHyJBv8IedeDJmicfC3VtkzRcpben5iSS6gc93j7-AvY6ExNsHycRf9MmAq4alm8eBg7wvhgBmBROd2jHUmppZkhfqU7LK9JAsE5aWm1OlgR89U4iWLOwuwlzRB-492-ODpHzQcNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=l8a16iVdSlLgbvUO5p7VHC50YwjCqydJnJgBV9vErjJ0UMQ_-ETqF8RTGj_XH6-NkqQih-anChJwCRZtZ7EWwcSEAjwLy7emJ0lizDE88M3GZxkljue0n33e8CkpReu68p7KHUwzrJKX5q0EV5EFs_oSi07gAeKhSvGt-X_eR4okTsfikHpEgRu1L6eRpsYKFRH4aIN_jlMN-JWLRWSTJ_C-NisNJ_YKH4PzV7Ixk984Z7Gfh3ocC5dOmsn4qd6ahhbaD2o95jgANgTKraAUe6OysdDRBjIW80U0T0PlFzMXGwUoxu8m5a8TVRjqF9r5_wLTTFO2DhlLzJvKrZGQeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=l8a16iVdSlLgbvUO5p7VHC50YwjCqydJnJgBV9vErjJ0UMQ_-ETqF8RTGj_XH6-NkqQih-anChJwCRZtZ7EWwcSEAjwLy7emJ0lizDE88M3GZxkljue0n33e8CkpReu68p7KHUwzrJKX5q0EV5EFs_oSi07gAeKhSvGt-X_eR4okTsfikHpEgRu1L6eRpsYKFRH4aIN_jlMN-JWLRWSTJ_C-NisNJ_YKH4PzV7Ixk984Z7Gfh3ocC5dOmsn4qd6ahhbaD2o95jgANgTKraAUe6OysdDRBjIW80U0T0PlFzMXGwUoxu8m5a8TVRjqF9r5_wLTTFO2DhlLzJvKrZGQeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با اپلیکیشن Hiddify (اندروید، ios، ویندوز، مک و لینوکس)
در صورتی که کانفیگ‌های CDN روی اینترنتتون کمی نفس بکشه می‌تونید به رایگان با کانفیگ‌های مجانی هیدیفای وصل بشید. چون مدام عوض میکنه کانفیگ رو، به شخصه تجربه‌ی بهتری از خود MahsaNG تجربه میکنید
لینک ریپو برای دانلود:
https://github.com/hiddify/hiddify-app/releases
فایل‌های اندروید و ویندوز:
https://t.me/MatinSenPaii/3483
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متد SNI همچنان فعاله دوستان. کانفیگ‌هایی هم که گذاشته بودم(
https://t.me/MatinSenPaii/3183
) همچنان کار میکنه ۱۵-۲۰ تاش</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3480" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3479" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjnVdLS7wMNgXtrtX_arZrd-DyiTnrZcY7kefPimBGVvU-ig3e8mLgzdruEhpMZPlt24p3Rnsmp9IOblwQ6tw5l8PZcTe5_qJA0TRiwuh3xLDoEtv6EdwRKm-ZCkUn5x8nRTvQdOTweC-lvEysRV0FK3oOydIUtADSzGKLRfuYlZVWx4f5O8J8rl5dVeebcGPBa5elMYWVSE0ouwFreCXkJZhVc7yS5DEl9Nc6DaXU1fAi-LdoHfVG1xbXAv4YnMR12Okxw5peuWGVcC8-gVmjm1MeeF-KVfYpG83ICVu6I2dYCuNq8pggJbxJHoXLPC3B6ZbI_mWxPIX1CjlI7fLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت اینترنتی که واسه مردم وصل کردن
خط قرمزا اختلاله !!!!
✍️
SamAlpha_</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/MatinSenPaii/3478" target="_blank">📅 18:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gm4Hxx8xm9-tbcthuldiWQCHRRV8mMT5XwSR_3l1iAvKhvtbrksnfOVTSRNPKst351Wbd2f4H9BivELT6HA-50BSOwwOtieMldTwMncbVOYWHd03JDEkkkjzSXXfJxl5MMN0ygjP39siZ34NeuU3nI8engn2C1BYhCRJg-v4ZAANrsQN2MdKeol1QZB8G3nG_1NcUkrcXJ7Y0_BoYm5qEanRpPFp7IMwqAnr8pgSWbQ1IN4DMae_odzMwFWGgvNBrVvH-3k3iShkX5KvhROxHOwwRwv0P4XaT-LW1KEyiy6iylrZAtiveT85jmEN79HZNxNQEdnfCxX2Kx-Ysku27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aDqhhHTZQZu5f1FJV7tIE6PJoFA0CQmeP52Hb_BQNBhyK7edFWUZNAuAwVB4DwB0tplPqUKSiZ_H46xmFJpDopmFdkWJYrbA7PLWaho4SdACBpoHM0Xb5SiLpYAB0gV5_o2H6ddBFgP7BB1ijbjikH2Z4ffLs6i3BTe6qqk0vevhWjA8FE5vkWxjf62mmHvL380uTOuiXehfiWOSbEAaAt91zamslCnS4Pn-lADjhP3I4Sjmmwl3MSJEpr-WVrM4aZ0CDdGCYBLSUl3Q7hVqKpBHlbDJwNIlnQnmID9ahy6Vu12MB29ik4jH6Snwh2bHCxgcRttoENlThVOM4S9Eaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kU6qT8dDDoBZQlKpiAsXiGb68Pu45MgNwRPtVgh0RXpykVHhzJ9WuXrimvYOdvhbqatmC3l5EFES8FEi2vSOA2pe0aT1maQvcVuMglOkIwnXJpV_qGuCgnKLJlLIJf3uHTDPVfKkOwC3xJdX73AmoVTM7U8vkOMU6ODvN9aWGHhXs3gV3NL87iJgSxYX6vIzsvM-FPpc5CaMCGbNwQHR64QI0ULTYJA-yGJW-bekhWH5fDT7NozlHru3gZSSpbDW1qbinhUoYaGNjloap6uMYRUeYphY_7N1Jb8v1WFWUngM435Wt4QPgiCj84h7bQ_V7gFZ2SViaffj-7doko8rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/twzbTF7sZgnGMjLwrn4DvG--YSjYRY2iv-bZH8GPVyhxizBcduCZDMRSuT6pnAj4s5uI2-l886qwkfLIydHhgHiXx-JVeyCfU9GqpWOSDmKNV3up0AHlfIw2D5Ct5CSiAMTKETJBQqtQP-8VCjeUO0kgUxVzIiubU__ni4tUUBpYfC4iZHdyIvB4ElX8ca3czwMdmLYzQnKYzzvWWrv752TU7rJvZDONGlIax1zSFMUHAqijOBx3TWHhmKUYpq_SAVi0usZziA12YAuAx6lXVTIq7r4j3SWqk5uU_kIIp0IzasZgHH7AzBpaE0rDdC02KDYe-8dUdJcqkb4OOsFaIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید برای من این شکلی شده که وصل میشه اما هیچی کانکت نمیشه</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/MatinSenPaii/3474" target="_blank">📅 17:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آموزش ساخت کانفیگ BPB شخصی:
https://t.me/MatinSenPaii/3443
آموزش  Sni-Spoof هم این:
https://t.me/MatinSenPaii/3186</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/MatinSenPaii/3472" target="_blank">📅 16:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxlNuisQHiRVMltZVVzC7BkhEzYKcXb15EhxqTSurvpO9lw40Qlkg0bBzv5kxk2IMb_scPJNub6bFA5y8jY5ze4yp86slfMombIhxumdi57QT73p6pEV_yvTS7PPclBb3VrfRK3xoi98oWsxIRvoQv3Zv7jAekgkYGb4y0kwgw-bKMNQsu14wPgaFTXcjtbd4IHg_p1uJT-oQbcjDhhyN4_6xUIW5_8EprnxWSh4CMRhcB8ze8cc6seTMlskesJjpHwVY2TGaq3NhE2bB5lp_etEB9X8HLBs_Qt-eLHRFUl9Odu55DB8tz8nueiT-Hfnk9-H7BGa7ZHVSpkdH96MPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/MatinSenPaii/3471" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4lSlGnXxP2Mz2eVDd6YHEfBmDhvPYOwt-OiSaaQ4UFR8gfa5BoNGa1lmvQSBiCe7IG0YrlcWGO9RoQHh4wK8NWHIMTbgke1u1G_L0cVr1cNARpi1nFphuDE8oHRcB_id-b2zQT2SyaXF9eBa9HSteAFCPsNWyytk0nWxgFHIb6DW4PAUxOCWOj_2Lw2sj1mPX6wEK8t9cFqAed__KfmfseiA9B65EDsIrxt3qkzz9W5Y62Q8HYpqA7HTE4Jj85AfnaF4KEAEed19KSu-6ia0ZZk5xIyjAeVXM4QA2cgV-XHMkKDPW5FUK642Iq0InW83IrlxsJG3pAIYzoMNY3kqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3470" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xm4ES7rMLkpseV8iv9weIM-Z03Swxta2Tn5AJdsltGsSKdMRDuZOQ3RsKcxrC7B1oarJsh2ee0RLV-5bvAzzUbCDna4InvTEwii9TiidcJkojo-ywGZXPlz6lkgnSuHzZgoZnWuDCKZpK4mtggbsmztbaFJn2qCiWwGnBJ2lBy81aafASKommIAIT5yakwpUdl-BohFd0io1e1kKbHsPEuGb8XfJ2DEiPdww4JjRumon8C9qVPYnIFouvL47fWNnkzx-SqOYuO-fB7t9Iv_fPkAcuinRw2N1d-Tya7p7sC1JuNJ9dzGwpdtpxi4gT-VeiBcPAmvoWV3mYzzl-nds0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اهداف من اینه که آموزش‌هایی بذارم طی چندوقت آینده، (هرچند قبلا هم گذاشتم) که شما رو بی‌نیاز کنه از خرید هرگونه کانفیگ. و هرشخص بتونه برای خودش و خانواده‌اش به راحتی فیلترشکن شخصی راه بندازه. منتها اگر فعلا نیاز دارید به لوکیشن و یا سرعت و... ، می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/MatinSenPaii/3469" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بزرگترین نجات‌دهنده‌ی ما، WhiteDNS و MasterDNS هستش که از واجباته برای خودتون ستاپ کنید! توی کل این 80 روز می‌شد باهاش وصل شد. آموزشش رو هم ضبط کردم طولانیه اما حوصله کنید و ببینید:
youtu.be/6Pm7kNQb3mo
‎</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/MatinSenPaii/3468" target="_blank">📅 10:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💭
چرا زمانی که اینترنت را قطع می‌کنند، درجا این کار را انجام می‌دهند اما وقتی نوبت به باز کردن می‌رسند، انقدر قطره‌چکانی این کار انجام می‌شود؟
1-
جنبه فنی
(دلیل اصلی تفاوت سرعت قطع و وصل):
🌐
ایران اینترنت را از طریق چند gateway بین‌المللی محدود (عمدتاً تحت کنترل شرکت ارتباطات زیرساخت - TCI و ASهای اصلی مثل AS49666) به جهان متصل می‌کند. این ساختار متمرکز است:
"قطع کردن آسان است"!
کافی است BGP announcements (اعلام مسیرهای روتینگ) را withdraw کنند، یا ترافیک را در gatewayها بلاک کنند، یا IPv6/IPv4 را محدود کنند.
با دستور مرکزی، همه‌ی ISPها (مخابرات، ایرانسل و ...) در چند دقیقه یا چند ساعت، آفلاین می‌شوند. مثل کلید kill switch.
وصل کردن سخت و زمان‌بر است:
وقتی همه چیز را قطع می‌کنند، فیلترینگ، routing tables، DNSها، و سیستم‌های DPI (Deep Packet Inspection) و SNI filtering در لایه‌های مختلف (gateway، ISPها، IXP) به هم می‌ریزد.
برای برگرداندن، باید تدریجی تست کنند:
اول routing را باز کنند، سپس DNS resolution را درست کنند، بعد فیلترینگ را لایه به لایه اعمال کنند تا "نشتی" (leak) اینترنت آزاد رخ ندهد.
هر تغییری ممکن است باعث باز شدن ناخواسته سایت‌ها/اپ‌ها شود، پس مرحله به مرحله روی ISPهای مختلف و مناطق تست می‌کنند. این کار ساعت‌ها تا روزها طول می‌کشد.
در قطعی(و سپس وصلی)‌های اخیر (مثل جنگ دوازده روزه یا دی‌ماه) هم دقیقاً همین الگو دیده شده.
2-
جنبه سیاسی-امنیتی
:
💬
قطع: تصمیم سریع از شورای عالی امنیت ملی یا نهادهای امنیتی گرفته می‌شود (برای کنترل اعتراضات، جلوگیری از هماهنگی یا جاسوسی سایبری و هر مزخرف دیگه‌ای).
وصل: نیاز به هماهنگی بین نهادهای مختلف (وزارت ارتباطات، سپاه/اطلاعات، شورای فضای مجازی) دارد. گاهی اختلاف میان این نهادها در بازگشایی یا نوع آن، باعث تأخیر می‌شود. آن‌ها نمی‌خواهند ناگهان همه چیز باز شود چون کنترل را از دست می‌دهند. پس "تدریجی و با احتیاط" اینترنت را باز می‌کنند تا فیلترینگ جدید را تثبیت کنند.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/MatinSenPaii/3467" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">کانفیگای توی
لینک سابسکریپشن
رو چک کنین. کار میکنن براتون احتمالا.</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/MatinSenPaii/3466" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/MatinSenPaii/3465" target="_blank">📅 23:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">حقی که نصف و نیمه بهمون داده بودن و با فیلتر رو ازمون کامل گرفتن، بعد ۸۰ روز هم پسش دادن، به همون حالت نصف و نیمه.
شرمنده اگه یک درصد هم باعث خوشحالی من نشده این وصل شدنه. هیچی تغییر نکرده.</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/MatinSenPaii/3464" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سرعت آپلود شما هم پشت worker و کلا کلودفلر پایینه بچه‌ها؟</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/MatinSenPaii/3463" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡
cfray v1.1
یه ابزار تک‌فایلی پایتونی که همه چیز رو برای مدیریت کانفیگ‌های VLESS و V2ray پشت Cloudflare یکجا جمع کرده.</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/MatinSenPaii/3462" target="_blank">📅 21:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینترنت برگشت، و خوشحالم که توی این مدت تونستم کنارتون باشم و توی اتصالتون به اینترنت آزاد راهنماییتون کنم
❤️
همونطور که همیشه گفتم، زحمت اصلی رو برنامه‌نویس‌های عزیز کشیدن. افرادی از جمله پترنیها با sni spoof، امین محمودی با MHR و MasterDNS، aleskxyz با پروژه‌های خفنش، iampedi و تیم خوبمون با اپ WhiteDNS، سارتو با پروژه TheFeed، سم، مارک، Samim با پروژه شیر و خورشید، و همینطور بچه‌های کامیونیتی زیرزمینی Vasl، عزیزی، امیرپارسا، ریتالین، GuardNet و... که اسم‌هاشون بی‌شماره.
می‌خوام بدونید که خیلی از افراد پشت من بودن تا بتونم آموزش‌ها رو به دستتون برسونم. و اسم خیلی‌هاشون رو نمی‌تونم ببرم. از اون عزیزی که به من صد گیگ کانفیگ داد گرفته، تا بچه‌هایی که قبل از آموزش‌ها باهاشون مشورت می‌کردم تا اشتباهی نداشته باشم و همه‌چیز بی‌نقص باشه.
همینطور از افرادی که به من دونیت کردن و من تونستم کیبورد و موس بگیرم که وضعیت بدنیم بیشتر از این اذیتم نکنه، و راحتتر بتونم تایم بیشتری رو پشت سیستم باشم.
صمیمانه از همه‌تون ممنونم
❤️
ما همه بدون چشم‌داشت کار کردیم. و هیچ منتی سر شما نیست و شما هیچ چیزی به ما مدیون نیستید.
و ما کسایی هستیم که امثال سگارو، یوسف قبادی، IRCF، وحید فرید، یـ‌بـ‌خـ و... رو دیدیم و قدم برداشتیم توی این مسیر.
هفته‌هایی بود که چند روز پشت سر هم نمی‌خوابیدیم، با درد مچ دست و کمر و چشم و تونل کارپال و وضعیت جسمانی افتضاح خیلی‌هامون ادامه دادیم؛
فقط و فقط چون به آزادی باور داشتیم.
زنده باد ایران</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/MatinSenPaii/3461" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/MatinSenPaii/3460" target="_blank">📅 20:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه
مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/MatinSenPaii/3459" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوستانی که همراه اول و شاتل و زیتل دارن، حالا حالاها باید بشینن تا وصل بشن</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/MatinSenPaii/3458" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin Mahmoudi</strong></div>
<div class="tg-text">نقطه قشنگ ماجرا خارج شدن این موضوعات حتی از ایران بود، این افتخارش رو هممون بدست آوردیم، هرکسی به نحوی کمک کرد.
یکی روی توسعه کمک کرد.
یکی با ساخت ویدیو کمک کرد.
یکی با توییت زدن و معرفی توی کانالش.
یکی با استار دادن.
دوستان برای پروژه ها نرم افزار اندروید ساختن و ....
همه باهم کنار هم باعث شدیم پروژه ها خفن بشن.
همه با هم کاری کردیم که پروژه مثلا MasterDnsVPN، چندین روز بهترین پروژه زبان GO توی گیت هاب باشه.
همه با هم کاری کردیم همین پروژه 2 روز توی ترند گیت هاب باشه و اینا همشون خیلی خفنه.
توی پروژه ی MasterHttpRelayVPN، هم همه باز همین کمک هارو کردن و موفقیت های خوبی بدست آوردن.
همه با هم این کار رو کردیم، کار یک نفر نیست.
این مدت جدا از بد بودن و سختی ها، همه با هم افتخاراتی رو بدست آوردیم ...
که همه با هم باید به هم خسته نباشید بگیم
❤️
درکل همگی خسته نباشید.
امیدوارم این روز ها دیگه تکرار نشه ....
همگی عشقید و خسته نباشید، دم همگی هم گرم
❤️</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/MatinSenPaii/3457" target="_blank">📅 17:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/MatinSenPaii/3456" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=WqtW5jQneMaoPGqN3AOfgbM1-PNvaeQudu4c7Pcqg8Vf-OhhSmPFK6k0kfFUF-9qBxOHhEI1OyfO3xlz3z_s7ump4skuIQsRzJhAnWzSSyNiTXijNW89V2J5lxrki7ylISRwZUykkveQ_Ix9VoLDOElqn2kbR-1CUZdqYLlJi4ZQgPb9fzZqSmGI0tbPEfgx4ahjvstJpEsB4qrAUvgt82zmYMxwZJZZEU4PHVqB8_hdmqA0fMeA8OKqX0bOVmGtr_yAxfoLvEQPmknHEOc3dFw34pAI1Cg7pYL6ZFCvpACEhS5YfWO25wW5kRLoXuOtL0itNOdnF_MtOh5rdo7s1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=WqtW5jQneMaoPGqN3AOfgbM1-PNvaeQudu4c7Pcqg8Vf-OhhSmPFK6k0kfFUF-9qBxOHhEI1OyfO3xlz3z_s7ump4skuIQsRzJhAnWzSSyNiTXijNW89V2J5lxrki7ylISRwZUykkveQ_Ix9VoLDOElqn2kbR-1CUZdqYLlJi4ZQgPb9fzZqSmGI0tbPEfgx4ahjvstJpEsB4qrAUvgt82zmYMxwZJZZEU4PHVqB8_hdmqA0fMeA8OKqX0bOVmGtr_yAxfoLvEQPmknHEOc3dFw34pAI1Cg7pYL6ZFCvpACEhS5YfWO25wW5kRLoXuOtL0itNOdnF_MtOh5rdo7s1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/MatinSenPaii/3455" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نت خونگی اوکیه
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%202</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/MatinSenPaii/3454" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قربون دستت حالا که دستور دادی اینترنت باز شه
یه دستور هم بده اونایی که کارشون رو از دست دادن برگردن سرکارشون
یه دستور بده اونایی که زندگیشون از هم پاشید برگردن سر خونه زندگیشون
یه دستور بده اونایی که سر اجاره خونه خونشون رو تخلیه کردن برگردن خونشون
اینترنت شاید برای شما یه دکمه روشن و خاموش باشه، ولی برای خیلیا نیست واینترنت زندگیشونه که با دکمه خاموش و روشن به حالت قبلی برنمی‌گرده.
✍️
Reza Jafari</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/MatinSenPaii/3453" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🍷
بازگشت همه به سوی سایفون + v2ray هست چند تا جدید که گفته بودم میزارم استفاده کنید ip جدیدا رو
✅
141.193.213.11
104.18.38.202</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/MatinSenPaii/3452" target="_blank">📅 16:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/MatinSenPaii/3451" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQpH7oNMEQ1aJuGL9jah20QQpZWBhH5noXOW9C0fG3QCKnZJKvGabEsjaUe0WzPESZMBChLbt_ZS4As3q2xx3ixkD6OHGnN0bA3N1Xc6Z9LJjY-ZqekzdKifPTtXpd8sicqTArO8ataPDwBfoYSEU4naTsSeSeeR1PxJxQ2agB3VdRBSAnBSUNtvypYaAp8vN6kRV5l2pSpwkuUGrshNE7JFXVtYr4NURRbkNCciSqzp2OBkVUICk8HGiQu6hzghU6Bu6iU9KhaZF3gjq6lbF8-bhyeoAl8GV7NjdUTFG1S4d3q9pPPaBpCsJWg63Sz2lvUUGJAD72fIf8ENszuvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/MatinSenPaii/3450" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قطع شد
😂
چیکار دارن میکنن</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/MatinSenPaii/3447" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/MatinSenPaii/3446" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/MatinSenPaii/3445" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Matin SenPai
pinned «
☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB  1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید): https://t.me/MatinSenPaii/1965  2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3444" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB
1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید):
https://t.me/MatinSenPaii/1965
2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB رو از اینجا تماشا کنید:
https://t.me/MatinSenPaii/1980
3- این لیست IP رو طبق آموزش مرحله‌ی 2، توی قسمت Clean IP قرار بدید:
104.19.229.21
104.18.139.67
104.16.80.73
104.16.117.43
104.16.89.120
104.16.118.43
104.16.63.25
104.16.7.70
104.16.79.73
104.16.90.120
104.16.62.25
104.16.6.70
4- از قسمت Raw (without settings)، یا Normal، لینک ساب رو کپی و داخل کلاینت V2ray خودتون وارد و به راحتی استفاده کنید.
5- اگر دامنه
workers.dev
روی اینترنتتون فیلتر شده بود، از طریق این آموزش دامنه جدید ست کنید:
https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3443" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه کم دیگه واستون مرتب و تر تمیز میکنم آموزش‌هایی که قبلا دادم رو دسته‌بندی میکنم و می‌ذارم خدمتتون</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3442" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2rh6Kov1A9U-9e5loYNanebqh-gV9cFmB1cYG_LIbNOODVN5EF_zOiZh98PycYlfCkE_jIlSNAiNMp95XHX7kkIanW0I_E3zbMoYe4YTjVahn3OE0hoxrQYaY7r7KxSibmi5v1bE8NPETC_i-Z6G0aCR0Nhcyuh-UD2BIMSe6YMwOg68uxsGRc2Ops3jRhxw_qzuTDGbgu8TmcfZopnaRmPKnKXqigGuKw5MvXXbmyqBIDBMRJMUMIJeyc_D5W3NaGz-iwDXEvaJvY5c1N_BXD16RRXnUeleCnt1DL8z4cMEV6p7utWyotF5zhACGZc0yFZkbFeO3Ez5VFo8LTz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3441" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با این وضعیت، کم کم نت‌ها رو دارن آزاد می‌کنن
از اختلال و اینها گذشت دیگه</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3440" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همچنین 104.18.139.67</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3439" target="_blank">📅 15:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خود آیپی 104.19.229.21 رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3438" target="_blank">📅 15:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خود آیپی
104.19.229.21
رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/MatinSenPaii/3437" target="_blank">📅 14:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLI587DICAX5-J41XC5dEUMrw1FZ2tN8zd8DvmRnbrq9WRv78QW34g6zD5bMJ__5qvgTgZ0DI1uUzreKqldBidJz2FULY_SToTmcP0yVeHF__8NsUVmijaXQP2l0tYnJtw7ceITD1fi4otZl8jyU7BogHhhUg_VaQb811pCIfnIHBVYBwNcsoIW5YibhoQxtjabfz_ix_SdQsZfCqIonBicz09wegcKLUC6pfgn_OtKhBOtvqC2GikXI_SkABSBSYJwZc28f2xpD7AHQMcJTt8u5Y3tgR9aQM5gRgFxw0G1DrehuK3RZf5hEGKwlRa2cE9drRYjISROn1yXXcCpCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کم کم داریم توی هرم مازلو اینترنت پیشرفت می‌کنیم:) از صبح دنبال اینم که بتونم یه راه ساده و رایگان برای گیم واستون پیدا کنم، اما متأسفانه فعلا فقط تونستم با پینگ ضعیف با ترکیب سایفون گوشی، گنشین ایمپکت رو بالا بیارم و بازی کنم</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/MatinSenPaii/3436" target="_blank">📅 13:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نمیدونم احساس منه یا واقعا این شکلیه اما انگار اختلالی که روی پهنای باند سرورهای ایران تأثیر می‌ذاشت خیلی کم‌رنگ شده از وقتی Spoof باز شده</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3435" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قول میدم اگر فردا و پس‌فردا اسپوف همچنان وصل بود، یه سری آموزش باحال داشته باشیم ازش. همینطور یه سری آموزش راجب چیز میزای برنامه‌نویسی و ستاپ کردن IDE ها و نصب کردن آفلاین اکستنشن‌های Ai و این قبیل موضوعات چون خیلی آسون با اسپوف میتونم واستون ویدئو ضبط و آپلود کنم و کارم هزار برابر راحتتره</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/MatinSenPaii/3434" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QoB3wyzNlBdI0CrKn7j7xNUQeH1ZiTKIsq0BHY5lMB52sWdioRA7stn_wlqSon7IsZ5xu_699hBNA8PVdKiXzr9wMlrY6v1aZWd51KaUcEfyUXgNHulqzPC3661e_cDPvQD_oBtUQgOduxRiDl4KIu4T38YkcH32lY4VVpEH8fjUayP_QC8QoCcR_jAl-RyYoQRONHHXgRmwVTS_Rmqp1D9J8fwcgvQpFjmDyh2VXQYvct9Gvub0M25c-4YqgzQ8ZIp1clEpmRXOnaHcsPLQg6jOVCuGhfurNi_M2AKIKTqT2YE9KNKk5lIUeFttbWN9JLAQvu9PMfltGOlSRBccxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jTRpSNuPLhsoabKWRco14PYmKM_jIPpeOnHVGGpjfCu4XqdtRIl5h0VSsvbo1nyTcZxuoOmkNSuY7nv_onTAN9ZCscNAFiivNLYbMZqutc7knwlEZktJzzmqv9VTpzDVZRPiysK-m2F1IS4UoVVa_fNLwJbFzx_1hboyVRoaVbwHRAmaUtTrHg5AiOO8zFS2gqXEpRpoih3O13sLD9lPePZ7gf2ZlCua5_XL1VOmOnnfVTFjv5oNlzo0oNcyDqnFQug1lDCt0qhRjqCS_Op1zHobWSYTkwlM8ehWKN_1ZeRnI4leiO6VzRMXxBh3Ni-JCumO-uIqYezpiwgbyyqNqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پولی که قراره آمریکا آزاد کنه: 6 میلیارد دلار
ضرر قطع 80 روزه اینترنت طبق گفته خود دولت: 6.4 میلیارد دلار</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/MatinSenPaii/3432" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صدای تیراندازی سنگینی که در نزدیکی بندرعباس شنیده شد، پس از آن آغاز شد که سپاه پاسداران یک شناور را در دریا هدف قرار داد و در پی آن، جنگنده‌های آمریکایی قایق‌های تندروی نیروی دریایی سپاه را در خلیج [فارس] بمباران کردند.</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3431" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3430">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نمی‌خوام دلسردتون کنم اما باز شدن Spoof روی فقط و فقط یک دامنه، به معنی اقدام برای سخت‌گیری "کمتر" نیست لزوما. مسئله اینجاست که فقط و فقط
hcaptcha.com
روی sni باز شده. مابقی سایت‌هایی که وجود داشتن برای ابتدای متود، هیچکدوم باز نشدن و الان ده تاشون رو تست کردم با config.json های مختلفشون.
اگر واقعا شل‌تر شده بودش، روی اونها هم باز میشد. بیشتر اینطور به نظر میرسه که دولت الان بهش نیاز داشته که بازش کرده و هروقت هم بخواد می‌بنده.
هرچند همین متدها، هزینه‌های بسیار گزاف روی دست دولت می‌ذاره. هم برای مجددا فیلتر کردن، هم برای خود فیلتر بودن این سایت‌های ضروری.</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/MatinSenPaii/3430" target="_blank">📅 02:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3429" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انقدر چیز میز می‌خواستیم دانلود کنیم زمان قطعی، حالا که Spoof وصل شده دیگه یادمون رفته چی می‌خواستیم بگیریم</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3428" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XGWBkg350vRqhbp6KAe5KWkMvF6T_h9TmjBglu-vbVJqrhxiaZT8upbD6BKkw3lfXg6qdxnpwSM5N2w0HY210RH1dAXvNbCn-iXBawWni4YaCpH8SjBwMbu8y32Os7tpwZT9DBRDBc13j34cbZt4jctymcqp7AxP8_TDHEUU5CGdZexub1cp3tTQ3V2Ae8_4fDnjdxdMVXIgB88vDQXjFJWm_QEjz063BHnHa78dSLhLrOtYWkA9TYNikcpNWpfIwUjQoTTQhpDwWs3ualbR_NRn-cPahRbtpLkGSTwmPCud4jTM_1XD2uoMv-jIYW3DG9QajLjgTPjGsMAtFtu86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aleskxyz
:
واسه sni spoofing من یه اپ با go نوشتم که به جای اون template واسه client hello که توی کد اصلی هست، از utls استفاده میکنه که میتونه رفتار مرورگرهای مختلف رو تقلید کنه.
همچنین fragment و ارسال چندباره fake sni رو هم بهش اضافه کردم.
توی تست خودم واسه لینوکس و ویندوز کار میکنه ولی نمیدونم داخل ایران هم جواب میده یا نه.
اگه sni spoofing روی نت شما جواب میده، این رو هم تست کنید، هر دو نسخه‌اش رو. ببینید کار میکنه یا نه
از firefox واسه utls استفاده کنید. خیلیا مشکلشون حل شده:
-utls firefox
توی نسخه جدید (v0.3.0) میتونید کانفیگ رو داخل فایل config.ini بنویسید و بذارید کنار فایل exe رو فایل رو run a admin کنید. نمونه محتوای فایل:
listen =
127.0.0.1:40443
connect =
104.19.229.21:443
fake-sni = hcaptcha[.]com
utls = firefox
قبل از اینکه بخواید از این روش استفاده کنید، لازمه این دو تا شرط برقرار باشه.
اول اینکه لینک زیر برای شما بدون vpn باز بشه. اگر این لینک باز شد مقدار ip رو بخونید و یادداشت کنید:
hcaptcha.com/cdn-cgi/trace
‎
بعد این لینک رو باز کنید و ببینید ip داخل ایران شما چیه:
ipmyp.ir
‎
اگه هر دو این ip ها یکی بود، این روش احتمالا برای شما کار کنه وگرنه قطعا کار نمیکنه.
https://github.com/aleskxyz/SNI-Spoofing-Go</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3427" target="_blank">📅 22:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3426" target="_blank">📅 22:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaJXoXoUMSCPk9BJMnwgeNrIZtOBZ0XN9aF4Sf9oxtQxwse94A1jhQgT8N7MwN2Trj6iiqzksXAL5GEFuMXUnipb2kbjQSK9bBcVbf8IUn4ehS35fO8XKU7E45VAUMTpZ5tNplcj-A6qzzGaXZzNgQIwmZe3FxYe_mjAo-YPeh2XLeY2oKa2ip1sqq2ascbjx-yBciAQUbVwSNoQLbXFDeZanieTlTEvsSkXmmuPoJ-HEvQS-5n_C2Dryyl_8-2SCW04VzI00RN5_DQ4KHrgh0JA0fug7soEJ_4g26fSNbc70YUgq5GhEoaSAUI_TkUyi39KLJAob0s1zKj_N1uWzft4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaJXoXoUMSCPk9BJMnwgeNrIZtOBZ0XN9aF4Sf9oxtQxwse94A1jhQgT8N7MwN2Trj6iiqzksXAL5GEFuMXUnipb2kbjQSK9bBcVbf8IUn4ehS35fO8XKU7E45VAUMTpZ5tNplcj-A6qzzGaXZzNgQIwmZe3FxYe_mjAo-YPeh2XLeY2oKa2ip1sqq2ascbjx-yBciAQUbVwSNoQLbXFDeZanieTlTEvsSkXmmuPoJ-HEvQS-5n_C2Dryyl_8-2SCW04VzI00RN5_DQ4KHrgh0JA0fug7soEJ_4g26fSNbc70YUgq5GhEoaSAUI_TkUyi39KLJAob0s1zKj_N1uWzft4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3425" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3424" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GS7k-xGd70vlGlNg_Kx4mwU3ZN5Prl8tzoqZcyE5kWNrT2s0BL1wmlT-MbhjC0QrHWF85nJOXHbwiNSVXYYgGRjljptmpW1dSdqhJHh41H0LjA2UUMce5ma7BLrh4ZkCOeVCL0O0DDcIhir1UxItTGxiBItjSNe4_j_khYXUBrnOEQ-Ivmux3RkGkQ8AlTa3WYcOMLkd1eqs1De93p7421DO7XIjtXTX8vnCasZdPwCnL6tgdUGATC4cKYRzcgY03HGfcUoTgT1T5jq6Sa9Jr-4vrlX-XvJgTof-aMxsfYTwCH2pxYokovVbWWGWHAf1OnKSl65-CuHlahCQGenDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو میگیرید روی دسکتاپ،
۱- چند بار تست کنید و تلاش کنید برای اتصال
۲- گزینه Parallel test رو با تمامی گزینه‌ها بزنید تا شروع کنه به گشتن
۳- اگر باز هم نشد، یک بار MasterDns رو حذف و مجددا روی سرورتون نصب کنید و با تنظیمات اولیه‌ی خودش تلاش کنید برای اتصال. اینکریپشن و اینها رو تغییر ندید ترجیحا و دقت کنید که دامنه و اتصال و دستورات رو مو به مو مثل ویدئو انجام دادید</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3423" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وقتی می‌بینم یه سایتی که پیداش کرده بودم و توی یه ویدئو معرفی کرده بودم، توی آموزش‌هایی که بقیه می‌سازن هم استفاده میشه حال می‌کنم واقعا.
وقتی می‌بینم یکی یه پروژه‌ی خوب نوشته، خیلی خوشحال می‌شم از share کردنش.
وقتی می‌بینم یکی یه ویدئوی آموزشی خوب ساخته، لذت می‌برم از به اشتراک گذاشتنش
شخصیت من اینه. و حسادت، دورویی، دزدی، بدجنسی و رفتارها و صحبت‌های ناسالم و غیرانسانی توی کامیونیتی اینترنت آزاد جایی نداره
✌️</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3422" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانفیگ ترکیبی متصل با تمامی نت‌ها
😎
بزنید بترکونید
❤️
آموزش اتصال ترکیبی
👉
ویتورای+سایفون</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3421" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fibO2tyUJdF7zCHjm5F727x8TdGsJtKNGolHoGYUVbVW4303lPc5IYHmRYdp1VmbIi4_yUHGVcd0151SuMyIw9tHhnFclOvP-vIMJEtN3zuwPFwmLDFTEK_5y20GdYBSX2g7Ise43e14oCrohgQBOnH3uuMCBLmAdNMOZ6-TXkMmsoZiwuqbwZlqFIvULqnHE12ZdgYGtVEn3AAP7DlaZwEdsYv9Iqcy9BduOr6HNitkMRZetC-u10Zeyxfj42TxF2bpN4EKZEP8E6fmMRZxjippXMSbdG2TkKA5WOH--nnhBZZUlGpaeQhfxVxiqbYdvcT0b-904srvrCw3VjYDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر وصل نشد، این خبر رو هفته‌ی بعد دوباره بخونید</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3420" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه. پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/MatinSenPaii/3419" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه.
پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار کنید. ۱- از Codex استفاده کنید که کمپانی Open AI توسعه‌اش داده و از مدل GPT 5.3 High برای دیرتر پر شدن rate limit استفاده کنید. مثل آنتی گرویتی هم دردسر تحریم و... نداره. فقط یه vpn می‌خواید که Chatgpt رو باز کنه عملا. اپلیکیشن هم داده برای ویندوز اما به عنوان Extension VsCode هم می‌تونید نصبش کنید. و محدودیتش هم سخاوتمندانه هستش و به صورت هفتگی هم صفر میشه. کما اینکه میتونید از ایمیل‌های متفاوت استفاده کنید و یه گفتگوی یکسان رو باهاش ادامه بدید!
۲- وسط کارهاتون هم می‌تونید از خود Ai Studio و مدل Gemini Pro به همراه گزینه‌های Google search و Url context با thinking budget بالا استفاده کنید.
اگر هم می‌تونید هزینه بدید، پلن‌های پولی Claude code و یا Cursor رو تهیه کنید. به مدل‌های چینی Kimi هم نگاهی داشته باشید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3418" target="_blank">📅 10:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">متاسفانه دید همه به dns، کلا dnstt و ساعتها اسکن بی‌نتیجه و دنبال ریزالور تمیز گشتن و سرعت دو سه کیلوبایتیه. نمیدونن که من با همین WhiteDNS به راحتی میرم اینستاگرام و یوتوب و تیک‌تاک و...
چیزی که بهش دقت کردم، روی اینترنت‌های متفاوت نتیجه ممکنه زمین تا آسمون فرق کنه. در حدی که یکیش تلگرام به زور لود بشه، یکیش بشه به راحتی مثل قبل از دی‌ماه رفت اینستاگرام</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3417" target="_blank">📅 07:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8tQ13ZaBv1BiYRi6dyIevmQBAtdm3yoe_HAuIZQkxOQCLTzSa4AlSADPJXcnWSP61L2G0hFBielbRFEx3uZvgZKY9XKPK-XXxbtIMUN7gBeVrSfcO_k2iMUlklBu4mY_XImPdbx3XRdMGAMCs-NoRWHJfqmLKkfxS0N7R6IDUoOXAzRaXtVLuRfIP7y7DT2m4-4QR1VgfxA2nW7bMF1Wz982BjGGmV90h3LkutQw4EVyqbqr2922wDQsKvBKQ66XXq47aYRrA73YeZEFhyRcZiXOWHoq7nGswfq5emKdg4ZCA90A5tGyQevpHYQlq-LPdF__72RFo8eo4tfFhhUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه. اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3416" target="_blank">📅 06:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbpSw619y6xLLwqA5LFm9tPjyMk0eoQTsABP-NQyhjYlfHFLqDV4gNJ9TxINcTyc17nYmp91UsW02mpNPQ-Jr3nOLXJHJEBVHXXim-oxXCgOfEthwAuXZoDY-QMps6xo_El3Kv1Bne0WJyar9BlC9LS50LboJPIJg4lFD8eB88y6Svr8q5DqCt_zwbctsB5odWXgkIdTDEVZLlehSF4nr9mgZRisbacNvvRedK2pW6ap8g5hxAmoGK_1KPAHDPFbHbw8pQ7ZZfo_LiDumbzMUyNjwIe4XekFXUxy3MsmnoDP2nZAgSkAbE1L3vGbvFBcnBkKXyg1-5t5ArZDkpbe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه.
اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان کاملا پاسخگو بوده. اینم آموزشش:
https://t.me/MatinSenPaii/3372</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3415" target="_blank">📅 04:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcoF0QUN6Q9uXETCAREwb2qq5ZPYzLA3OvGRuJg_dBFMicE1ZvcRfQi00JSw8y0JK7khp-Cw_yoPbR0Y5I8BMuIU9teEz3ZTQ7-_DYqDFxMjYYFLyfyVvKNB4I099xATYPzPiYTnzrcDUCFIK7SOOsrZayLFkemC9-eoM-Xik00RHOymd5VCxL4ZKGEyoHkpT2BFWEEp7TWpwHhSMUh3DRjnT1NsF9XVLKFo00H5L57qFlxupgqDM1HZTMq_hBu3WO4k6r8THsXtQ1p5EPtQ4-a9ZmlFlMOoY4UPz54vysSdQvX2ain36ZF8o6WTa_QUFweQcus7__GBa823x3vHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنان SNI وصل هستش
گزارشاتی دادن بچه‌ها که براشون کانفیگا پینک میده و کار نمی‌کنه، که خب باید بگم اختلال از سمت اپراتوره. یعنی شما دو بار پشت هم پینگ بگیری، بار اول پینگ میده بار دوم پینگ نمیده‌. در این حد هستش روی بعضی اینترنت‌ها
اما خلاصه تا وصل هست، استفاده کنید</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3414" target="_blank">📅 03:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtVzoERGM2cSKOS25kJDw2sC5gId2zKb5-kQvBkhcVo45VF9pyXDZ1S1XmaS96NoOaHjiYEZzcLoNhpkL_JiVuT5RBpVyIut6_2XJDFdTDwsDzSjyeNborXk_ad6fHlMcfZiVbae2IRQYdh9cjjWu8vYd8SYNozMkcbPDCtMPi3cfsNEBgRKuv_--FMbopNwJMwH1BqDBgpfljNblqKmpQOnpY7-foLqrRhsY9ZhTLKpScWM2IL7VfXI_gupO3MePBwhof4UWoRfynlz_SJFnxt52aLj8C1FBeWIY6xEYp3rEA0ZyovWhUxRLx-9sMOSidJvyrNX9qXrpuTM8w-VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی آدما انقدر خودخواه و بی‌شعورن که انتظار دارن کل کار و زندگیت رو ول کنی، و تک تک ۱۵۰۰ تا پیامی که روزانه می‌گیری رو بشینی جواب بدی.</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/MatinSenPaii/3413" target="_blank">📅 03:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/MatinSenPaii/3412" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برای SNI SPOOFING روی Mac می‌تونید از پروژه‌ی خوب Cloak استفاده کنید:
https://github.com/g3ntrix/Cloak</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3411" target="_blank">📅 20:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گویا پولی که از صرافی‌های ایرانی میاد رو بلوکه می‌کنه کلا. حتی از Trust wallet هم ممکنه این بلا سرش بیاد. ترجیحا از این سایت نگیرید اصلا</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3410" target="_blank">📅 20:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/MatinSenPaii/3409" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3407" target="_blank">📅 19:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">زبان‌های مختلف برنامه‌نویسی، هر کدوم قاعده و قانون خودشون رو دارن و به درد یه جایی می‌خورن، اما یکی از پارامترهایی که می‌تونیم اونها رو بر اساسش مقایسه کنیم، «کامپایلری» بودن یا «مُفَسِّری» بودن(از تفسیر میاد) اون زبان هستش.
۱- زبان کامپایلری (Compiled) چیه؟
توی این زبان‌ها، قبل از اینکه برنامه اجرا بشه، کل کد به زبان ماشین(کد باینری) تبدیل می‌شه. این کار توسط کامپایلر انجام می‌شه. این که ماهیت کامپایلر چی هستش، بماند.
مزایا:
۱- سرعت اجرای خیلی بالا
۲- اکثر خطاها قبل از اجرای خود نرم‌افزار پیدا می‌شن (Compile-time error)
۳- پرفرمنس بهتر
﻿
معایب:
- باینری تولید شده معمولاً فقط روی یه سیستم‌عامل و معماری خاص (مثلاً Windows x64) اجرا می‌شه. و برای پشتیبانی از پلتفرم‌های مختلف باید کراس‌کامپایل کنیم که پیچیده هست و دردسرهای خودش رو داره.
۲- تغییر کد و تست دوباره سخته (باید دوباره کامپایل بشه)
مثال‌های معروف:
زبان C --> سیستم‌عامل، بازی‌سازی
زبان C++ --> بازی‌سازی (با انجین Unreal Engine)، نرم‌افزارهای سنگین
زبان Rust --> سیستم‌های امن(به خاطر مموری سیفتی) و سریع (در حال رشد و توی هایپ شدید)
زبان Go(گولَنگ) --> بک‌اندهای Scalable(مقیاس‌پذیر)، میکروسرویس‌ها
زبان Swift --> اپلیکیشن‌های مک و iOS
۲. زبان مفسری (Interpreted) چیه؟
کد خط به خط، موقع اجرا ترجمه و اجرا می‌شه. نیازی به کامپایل قبلی نداره.
مزایا:
۱- توسعه‌ی نسبتاً سریع‌تر (تغییر رو میدی، فوری اجرا می‌کنی)
۲- یه سری به عنوان مزایا می‌گن خوندن کد راحت‌تره که من قبول ندارم اصلا
۳- در کل Portablity بهتری دارن. هرچند شما عموما مجبوری سورس کد رو کامل تحویل بدی چون نرم‌افزارت همونه!
معایب:
۱- سرعت اجرای پایین‌تر (چون هر بار باید ترجمه بشه)
۲- مصرف منابع بیشتر
۳- خطاهای سینتکس و DataType، معمولاً زمان اجرا (Runtime) تشخیص داده می‌شن، در حالی که توی زبان‌های کامپایلری، خیلی از این خطاها زمان کامپایل گرفته می‌شن. این موضوع برای پروژه‌هایی که با این زبان‌ها نوشته شدن، باعث می‌شه دیباگینگ پیچیده‌تر بشه.
مثال‌های معروف:
زبان Python --> هوش مصنوعی، مهندسی داده، اسکریپت‌نویسی(ابزارهای قدرتمندی داره)، وب (Django/FastAPI)
زبان JavaScript --> فرانت‌اند وب (بک‌اند با Node.js و فرانت)
زبان Ruby --> وب (Ruby on Rails)
زبان PHP --> وب (WordPress و لاراول)
(هرچند جاوااسکریپت و php رو دیگه نمیشه کاملا مفسری دونست. به خاطر JIT Compilation که بعدا توضیح می‌دم)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/MatinSenPaii/3406" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4659a46672.webm?token=V60gjtv_GV6wtT28QWDcjqzsZji5OcUFJWzPnBAJjv9SiLa0Fe_kw5LhSvF3Waw9j4BfS258y6uhUaEwTbUQygDt6zE2olvZZie8U0ePNnaiCXQGaN4VWx4d0UHqOfCRpBSZIje42Yky5JO_GlDm2UFTo9Y7At0E2UOdNEYMgnX136V0l5qzwTq1if3kZmwhijAGdjlbnuY23wqQsGjC3xxI7BPD7ne9B4AG38P6W6TJ_LcINaQzQcmkYJOYQTr7gHAXJgwL_Sqmx6ythVDDtyXgkdsNzSFcTxXY7bnvPzThfjcDQ4yVCrWTuPfQIPVZC01Nztn4fyPRsecS6Ey6Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4659a46672.webm?token=V60gjtv_GV6wtT28QWDcjqzsZji5OcUFJWzPnBAJjv9SiLa0Fe_kw5LhSvF3Waw9j4BfS258y6uhUaEwTbUQygDt6zE2olvZZie8U0ePNnaiCXQGaN4VWx4d0UHqOfCRpBSZIje42Yky5JO_GlDm2UFTo9Y7At0E2UOdNEYMgnX136V0l5qzwTq1if3kZmwhijAGdjlbnuY23wqQsGjC3xxI7BPD7ne9B4AG38P6W6TJ_LcINaQzQcmkYJOYQTr7gHAXJgwL_Sqmx6ythVDDtyXgkdsNzSFcTxXY7bnvPzThfjcDQ4yVCrWTuPfQIPVZC01Nztn4fyPRsecS6Ey6Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3405" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3404" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپوف روی یه سری از اپراتورها برگشت. هرچند با وضعیت دیروز، و گزارش یک سری از دوستان توییتر، اختلال شدیدی انداختن و در تلاشن برای یه سری CDNها بدون اینکه مردم بتونن تانل بزنن، دسترسی خارج باز کنن. که احتمالا سر همینه این وضعیت:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
﻿</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/MatinSenPaii/3403" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">توی دایرکت چنل یکی داره میگه شیر و خورشید جدیده زیر پنج ثانیه وصل میشه، یکی میگه دو ساعت هم شده و وصل نشده.
به نظرم باید بذارید حالت هواپیما و با rangeهای متفاوت تست کنید. انقدر زیاد منتظر موندن هم دیگه فایده‌ای نداره.</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3402" target="_blank">📅 14:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیم ساعت تا یک ساعت شنیدم بچه‌ها گذاشتن تا وصل شده.
اما طبق گفته‌ی برنامه‌نویس پروژه، خوبیش اینه که بعد از اون دیگه نیازی نیست انقدر منتظر بمونید و به همون آیپی تمیزی که برای شما پیدا کرده وصل میشه
خلاصه که اگر گوشی بیکار دارید، بذاریدش سر کار</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3400" target="_blank">📅 12:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3399" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nw14bWh1UYG09bx2SSZgf8Zll1r84yovSpwHV7S2uZGBO0TPG35zlNDReKhvhB_mmAgxM8XWuDH6ZKTruW--9GMOKiv5wB1mat4xWHPOeGglntXPpMydXfF7HlcMBK9MH2THhXOqvhdZ9AxPNBzrrttAbQCh9c7Q7xEvVYBZHqcHj82-DMZCboJBBNT4ahA49ksUciSujnSq7n3gTJ0EZ1ZK6CPz_F6CYBvWqynbhJw1u5aLrB9IUlqd9zzJG7yLD4BwelFITlnG1Ssqu8-7mFDB1Sf4cQ5w2F4R8RvQvnPWDV5-oUe26Kdj6yu99dnQfK7vNHseyaYASvizPJ0R2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jm0GtSoOfz8EvGSKsGs6vp3KARWHdlYttuGGabLqkbnrAEe6ruC-9_lGfrM7o2_aJnwEaMR50HG87s7pgFO0dTbfIhTYD9BoN_gJroZZ_HCeNo61KJkQcu6jVSvd8BX-rj3HazSppJ4Vxa_E-tbRj4Ih0eaBTzbqUk-soyA5BzJHPs1-HDy8mluqhioA5LigikOyO8npLJaYw7i6zI52ql0BjVkbpDYu6JDi-Pdob8QGX7x9Sptnn_K7qcLNeuO3Z7NxLDrJQpN0xp3pDrhw3PsGyZibB-MaM5YStCrpe2xphf5H3D2ZSl3f7VmW2r2iInj6wgUFasAJQwOP6F4s_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JzUHEFL2CJFYspY2pKpaJzn0CVf2iWFyV1jKgAWmn8wwkkJbGeR_ZdFuaYeVYcINJOu4oZc1t8qn65mCDjTY6XH6HUPDzwJv0lUlKKCj_aM6M2KghDXS-LULK_DyneOF1ry-DwSk-oTtMWxuoar15nNDIXw1FTofmV1T__q1_5gznDR8A59RAgIE3PyPJ6YzVtLKZCzX81uRUEwvX15DL6E2IDGp5X4Mp0A2H5VWrMMigXCa6zsa0SMJRthhwApshB14rFICZ1-nsPUf4xkjpbe67Fd29ml4TV-mCBvwyUP9Ead_wsYKGKTkFlv7NAOvRQ9qliQp61AeJojyeSjGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Clrm6gc7gnIn_1oyeEQUQ8fIYSGTYUD-ihWahOx-3URFiIe0wgdxUcIEOogIILRBCwPjNj7ysB_vAsWiaHORCp1H-g4mBOeF465Ifbqws2vrtzdLuNJUSSuH-gqpcFO4_3UexBpRZ31ua5kqs3ywohU3dHJK6i_druYBxYbmfTV7DL5SK6A8-6U7ly2xcnEZu7eaMGx_l0bUECE2p58GhUHohKNTQbsRw80ixtyXvFMWFF3aw4joMsQgiKrPhzVWksPyA9WUNIEvfMwSws1G07zaunIsu3-d9-brmEnchamtvDMMI3k-0iclMYsiwyLAZq0MxvRn11K2YLeP6NWHXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید کلاینت شیر و خورشید 2026.05.24:
- آپدیت Beast Mode برای درست کار کردن روی CDN Fronting
- اضافه شدن اسکنر ای‌پی. برنامه لیست خیلی بزرگی از ای‌پی های ممکن را داره٬ پس اگر در اتصال مشکلی دارید پیشنهاد میکنم تنظیمات قدیمی ای‌پی ها و SNI رو از قسمت settings برنامه حذف کنید (خالی باشه)‌ و اجازه بدید برنامه خودش کار رو انجام بده. دقت کنید ممکن هست بار اول خیلی طول بکشه٬ حتی چند ساعت!
- اضافه شدن پروتکل های بیشتری که با CDN Fronting کار میکنند. احتمال اتصالتون و سرعت باید یکمی بهتر باشه الان
- قابلیت غیر فعال کردن سایتی که زمان اتصال٬ سایفون باز میکنه!
- قابلیت تنظیم پورت مورد نظر خودتون برای LAN Proxy ها.
- قابلیت تنظیم username و password مورد نظر خودتون برای LAN Proxy ها. این تنظیم دلخواه است و اگر تنظیم کنید فقط با این username و password در شبکه خانگی میتونن به شما وصل بشوند.
- آپدیت شدن هسته سایفون
میتونید از اینجا دانلود و نصب کنید و ممنون میشم اگه به اشتراک بگذارید که تعداد بیشتری ببینند:
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3395" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7h9DlMbpVtz1yL96vFVV4ukluX6LgeXp-Zduoj1z-4dise9_kT7kZhjpFmRXUY8Oh4EEhfs3E0sGeMwL5LVcCYEWD3Z5zBDuIKIdS1tdnOdrZnl6LhfefCFLFjcsZ-1QCxeSWe3sMP50itWFR3flhm8e-4kaNhPUFc0PXaiIuWGsL4hvSohvJQsh8SyOiz1FECThtWrJNtHzEzI10RVMwvU9oqmU2dYWzcGW7ZNbDeHq6kQTn3emfgMrPx0xwXfk9AsXWH1MZGiI4bs00bLgin63jHwXkQdIPnE-MD8olSHibi8T46yCCZROLAaVNc7UJoLeWpLj8SHWl_QcVZYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3392" target="_blank">📅 09:48 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
