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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 685K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-96885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsKHWejrq5BDj49QlC-0jMfu7Mh2SAsV1Az6S7N-CtXNpbzOArHYpANoit6FzXo6EaI2J7w8VnYxRa6ziXMM8h6y8xsNh-wMXDYC0ke-3soeGLv5l5LrU-NSz_ggzLM7e3cCFakxGWrS2D63ILd3BFMpCo9IS5ZbcO61SCsovdEBniPSRDXTdld17d_WsxstPPSsbcADolLbzcCDFPCKGU-4KDU_5NK6x29fkQjRL1Vu_rsHkg8LbL7NWZTKLdJYQEyxbhYsz-wYasnz_DZG-vqANnnU17pqiLMfdJc3Ehequ3VwABy_2Dx5ilv572Djep5wuL0Mt9pg_j6cMblPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
📊
برونو گیمارش در جام جهانی فعلی:
💥
‏• [4] بازی
🪄
‏• [4] پاس گل
‏
✅
👑
🏆
صدرنشین فهرست سازندگان گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/96885" target="_blank">📅 22:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇧🇷
🇯🇵
متئوس کونیا به هواداران ژاپنی: "ما پنج جام جهانی داریم کسخلا.
🤏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/96884" target="_blank">📅 22:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw3FLbhwaCdnaECrKqyhMR8WGBNHWzR7UpTwidPXbpvP_EE_Yx5gKaQ3NL6TZ_oqpBsw28fdEGTp0HDiEof5-gxEN3QZw_inC_fZzwiXq7w7sSVDFGHq30FDaKhtegekVCWDFIB5GNadAsJwL1iKDo4FI2RsV2rS6caGILBYDWcNURXSqW8PO5DjzilBlZ67sEmW80n9RRoyvT9JlEb6EGy6NisjRcqoK1SI_40PrG1Oy6XydAz2tg0aMGV-tuupR168SWvnEL0WIpk3g83KKQcLAHDvuFE_bS9ARRBrSQ4CNGakgiJBtsA7MFokF-ZZaSPEBG7UroGOQgjaLUcdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😶
🤯
🇯🇵
ژاپن در ۳ بازی حذفی آخر خود در جام جهانی پیش افتاده است.
❌
🇧🇪
مقابل بلژیک ۲۰۱۸ — حذف شد
❌
🇭🇷
مقابل کرواسی ۲۰۲۲ — حذف شد
❌
🇧🇷
مقابل برزیل ۲۰۲۶ — حذف شد
۳ بار پیش افتاده است و ۳ بار از جام جهانی خداحافظی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/96883" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eohAnGX-xFqSucubTmnV-y4-yourLEeSUu7zLUaWsevU-D3W2AbRmglVZr8-AOzAV920HwQ-ObvpU8YSR07dZv3JRtDvX-HVokQjGYtnopOpk4EvKsfPNV5_hvRngzzKCVwH72UQtEdrcmVGsFp9RLUL9KIQmH-9exXh7PljMMQ-G1qgrkEVeSVkroWur2RMlKZf6txUCtkpzw3KELOpCIgr5FjVUr0asODQCXDHuEXFo5iDHv15FSjhdyKiMAY7EXGJxg_y2EaJ2wd--2Np6mHDo6gAxQkSgTzSWH52C0fE6StY-gUCDM5YyoaQiHwR21NvMJGwnG5x9s0Sn7PaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇷
🇯🇵
متئوس کونیا به هواداران ژاپنی: "ما پنج جام جهانی داریم کسخلا.
🤏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96882" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/df792jo1Gyd-wEodr8FfSwNrFpuL_y-KFmWZj-ZGahVrCRPGrbcPOIP5jmcK0uOFXOy8tEs9O4tBVvtqB30i-MgVfEOAIxjUfaj2MnNipIekS8GPHZdX6ac-2v6QgU-p0rinAzigOKZEP07-kG6mhp9cnWyIAgVlTJ0qXCaLn0IyZBFVogdgHJrNpbz0loDA7nPAGOKgBTpWtLjgn5rcl0tLwdplJA4mpYxQj7sQy_G8ev7ZIwoPee6URWmJTawEqSAHcqPDMzyfIiTCdX3o801Drk_k3EyX3B3g8Y4beoz5EqYWGWrwYwn4eRwNiuUR5gamZ4D4g6WNxAY6CCW7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWLSSQ3iP7j68JidTX4RDp8WhGFYsqYYHX_NmHs7XfMVZ-1d0eCsSFTGr18xfgNKifB1u0-1p9E6se8D--Sl2iTVRZAeXJAqtJJcmzGkBtqXkKXfmYpovRsI6gg6Y0lQdbgrPXXghQz-GI-R0pnCiR4CixiYG9HyAVGgawF-2Fqw9IAvLaRU47ZTSnu3lPca6fDfHSuuQSxaownnhcv-wQspLrdkJUdrZ42Sx7IcC7Nbev74V2x0KgcQhV-IUayNrwMxEarru1IDN295WqrzxVFcmKIlFKso39CvEkPK4xKfKY9rC1P18q6pKCfLUAl1lMHN3gfcDgKaADT3wW5iHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🇧🇷
کاسمیرو (۳۴ سال و ۱۲۶ روزه) دومین گلزن بزرگ تاریخ جام جهانی برای برزیل پس از پپیتو مقابل دانمارک در ۳ ژوئیه ۱۹۹۸ (۳۴ سال و ۱۳۷ روزه) شد.
👏
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/96880" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ta1n7QFdOyxRWlobCuO5AicT386yJgJXzry8vwtw_ax6KKReIl5-8XCJef3NK9_hpUg2uVmM0GjnI-1w7NA2c8UngfO63GdDXQ-FpnI9skZ8lzJWhLL1-0a1_TsG3xKuqeRGGlXLLJACRzufw7O6oFA4_NuBBTVZQmSOz6eSIBolBoytOR-t1GCSZUpf5aUOWYRZSFzKAaBhm7qypT6eS8PEnmw3MJ_UECUep40K8GK3syHxincf6j7OIMfG90BNuamiSK2PDt30sFkcexXamJmIM06A-1ATie5o_zifWBELBh_hv97knWvxY-Bh-Y2JPTUGrWUAre9W2hLmVFXyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vdn1Q2sUpJoJQJNBPsCYa1yFRT2QypKZD7ayTdByIUTq-q5cwMxz_zcYvC4lWOG7Lqa0FJ9jQhodSRKcwktAq7dL_Ku_W7mpBEiJCH9sVohj1ixvhZ_MoNPuGDN0QQcsOQz234C-unaQaCl_-hSIPHLYciLB9o9Lb5-Arl8E-1IJTntHs2L_3WsHbhpfMXxPzOCy499GBSTfBHpDBMaYhX373VJsCET3Z8N6NguhPZ34jCYx-vph2zs_jYfei5kxd_1JaT-iW52DFk3qr7atWL3ucDib_OIDYIfXYmxsIaodSAl7poawvVzwyQyPxYpugng5eXy2H7RGAMl8WZAEFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
🇵🇾
ترکیب آلمان و پاراگوئه، ساعت 00:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/96878" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIXcvXPJKTrgGGD3B2pgmiaWJ8VGNyom5--w1pwlDqx8KFyJZv3sRzIMNd1twubcvVLkvjkbEZQjJlnIW5Jtx8_4PRInrt24khxK6EgWPklxPtVyfCMsVtkJ-qlllAaCtqx59cOi-F_55sjQ0l79P9_3MRsCabPlLvnkVr00YPYNMQWQdEhjgKsFkoHdx56uCw3WjNqbj4D0GLa8tGqaZwkA18sGX6VhYOjW8Lvfrs7DJP9hUles1SS1nh42A45ER3iyJXtpSJI35WBKkxjelS4hFNxXhkQjmAmTRrXEf9kqrpxvdpLQSYPl2088nu_xHdEimAD0puffUZdEsqMoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنجلوتی بعد گل دوم برزیل
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/96877" target="_blank">📅 22:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVV7vx5p-G52glVbKFw_jSaIgHXZt3KqZe7Ily9KAo0xP8Ne6-FyCbj_AtsUBFSzFDttKu3z2FIV_Ff_Uz91i9fLaveAu5U0J8twk4gf3VyeWoCTQJUmBAbFA9fWvLDLLppS6CoFio_bRUyC4FhRHHfC1qh3mIY2dUOy96uQRpTBRERkczKDeHcOU2iJaeixdV3dyCdTLE3U1HA60ppDtJmiJ-gwc4jzOQB19zgobFqKeGYn2saw69-kWMcGEqyn71fS6aB4hWcIE5yeqiffc4zoy90y3x-rqdlyX5PvW00FWJ633Z1xVMkIysR6iX8s4TbOm6UVFhyM5NfzT8K4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/96876" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Plwk5jePYxxa_0remOnPqXA3cKMoM7ruCVTlRdivh7aTiRP6k1-ZfldgGGahSu4qzmczHnqgnCsBX99K9m2_RsX7DzAR7ddYAYkecLGJlSIt4ntHYiHqoXlT6IfNKeSPBSFLPA-pB6FhzB2phE2qsPYWmkejG7D2uswzSq3bsbp6wEhRB9JFPOx5F3Q10SKVX8rwob6VUmYb4uk-EB2kL9014ZRFgF0DV5mrIxMhRHwyFQ9-d-z_A3MgfVDhh4-K8cZda3_kUMB7eCIRrQEwSWHZ_YjF-QCHvAJW_wipXafDgYb2Vg-m2N1Imx0ONaCHEnzo2RzcmmoTQbLhxQby9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییی
🇪🇸
رئال مادرید به توافقی برای ماندن بازیکن نیکو باز در فصل آینده ۲۰۲۶-۲۰۲۷ در باشگاه ایتالیایی کومو دست یافت
✅
.
- گزینه‌ای برای بازخرید حقوق نیکو باز برای فصل ۲۰۲۷-۲۰۲۸ وجود دارد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96875" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGlPW_h6l3Gi0scSqg8JjNrkKPRV0ihmcdRDlKhijgyWieQsj24u40nkuAFGNm4CGWqfjztF9kHNP5JUAvB67W0X9tVJ_6gB6KU3hXTsMaFULk5-qTx2syTg1pR5nuwOUsf48Uh-aMy2xFYfY3DQFxP_DDwf8ivwi1FAzsUfp-TM7XFhK809Kf__t7_xkBtt6HlNgI3iTZLG-GT9A3R3JpXPgQlc8i430s7gJvaWdb1_nm3_N3NDiSp7ZI2h5C8v7e_xCnrBwiYkidJPLnBS5dfA91JWUWEhy8Azfb6QYriJ9lI6Aic4e2ZBCGRMeQZDWpI7Y1UdTdB3SArIr88kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم آنچلوتی
باز هم کامبک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96874" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQDCLwIgy61ZPxvANrmL2W7kpJSOA5qbMmuTjfqYaUuSA5n7_RjzXCcAxSRyFehOLFhHobanDsnpul7wZf0Lt2xhmiKNOzMSYJ1U7tpUp8xYY9439ADTF79ApsISmtfscsUvmAPfm2RJnskErMfq1TN8XmKqjr8Ox-WEVMXn2OWQfJ51JHgH4XSL6zHL2JwtQ2YAQl13FvETKMbxw3eMegw44QRU2d0zp3cBVgz3AT9s4MEcZAozi-pjy9rwicEMAj7nuU6vQyqwr5ptG5OQw7AIDCHBjpKG6C7BxIWI2zSEn39NcznVXEACxwKVXa2oVU8KgWn-Y87dcqm3GkRRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پیروزی دراماتیک برزیل در آخرین لحظات و حضور در بین ۱۶ تیم.
🇯🇵
ژاپن 1 -  2 برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96873" target="_blank">📅 22:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/490bef5d86.mp4?token=LR-0CJvNy8GLL4fLmbIaA_mEt0LrLxMVaKKR2sfP9Savd2J9opkP6puS_VhanqfBxtx1Vd1moNbZuK2J1L7tAJXltW_rSd_WuvgyVbrdQAreoLWRo-_TP7yh_wN1_x36iiuj-gjG1SqPduAzHjaAKbDHesNRiGDdCZyGKs2gLmZxE0Jte9-sbTDBXurYIu6MK_nqy0pkbk_1fpY5tIaOU6K2-ZAlG3Zw0PrKsGV0-aP3NHtfRbTcM4A2jxCrGxWO48g8JWkDkruDPX0BVUWqtIvbCgS03m6vLGmSDm7Aco-BCPRjKfbjdz0sigtPTeohYAPDWnBGSFWaMPmE05FZh5gvobb44_rmC3GqKuuNtNdOXbZbDHYEmDzlFSQc8LuWEgHlivfkqLYgZ3OGGqDx9lfPb90PXUt4n51UH5fFLN8AYbInoXTd9WONDzBGNwskVuVioo_-n29zFSXJlxvmthDUePer7ixQeOmQ4H3_RMBqZoYcvzJ3bt7yLsENVWnVOI7rtV8s3l4CjE2-GyVHI37-53T9ODfJ1fjvfh-tfWJH_-xwKL0sxxF7LKbiTJJn1I8vkakNEnO4_6sXzu-OR7D_kHUNKP5579bUSu5cZch93tqnLkiJBrzy_4bYMFK-fse0vpH0l27IlGVdcWmL1b5LVFmOg0r2LY_-MQRHXXo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/490bef5d86.mp4?token=LR-0CJvNy8GLL4fLmbIaA_mEt0LrLxMVaKKR2sfP9Savd2J9opkP6puS_VhanqfBxtx1Vd1moNbZuK2J1L7tAJXltW_rSd_WuvgyVbrdQAreoLWRo-_TP7yh_wN1_x36iiuj-gjG1SqPduAzHjaAKbDHesNRiGDdCZyGKs2gLmZxE0Jte9-sbTDBXurYIu6MK_nqy0pkbk_1fpY5tIaOU6K2-ZAlG3Zw0PrKsGV0-aP3NHtfRbTcM4A2jxCrGxWO48g8JWkDkruDPX0BVUWqtIvbCgS03m6vLGmSDm7Aco-BCPRjKfbjdz0sigtPTeohYAPDWnBGSFWaMPmE05FZh5gvobb44_rmC3GqKuuNtNdOXbZbDHYEmDzlFSQc8LuWEgHlivfkqLYgZ3OGGqDx9lfPb90PXUt4n51UH5fFLN8AYbInoXTd9WONDzBGNwskVuVioo_-n29zFSXJlxvmthDUePer7ixQeOmQ4H3_RMBqZoYcvzJ3bt7yLsENVWnVOI7rtV8s3l4CjE2-GyVHI37-53T9ODfJ1fjvfh-tfWJH_-xwKL0sxxF7LKbiTJJn1I8vkakNEnO4_6sXzu-OR7D_kHUNKP5579bUSu5cZch93tqnLkiJBrzy_4bYMFK-fse0vpH0l27IlGVdcWmL1b5LVFmOg0r2LY_-MQRHXXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
گل دوم برزیل به ژاپن مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96872" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشمااااام</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96871" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چه دقیقهههه اییییی</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96870" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللللللللللل دوم برزییییل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96869" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96868" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUmDLBct9lSpIaC8FDB0Wt2HVe3cEkqqXWBzoxXkkJ6gKw_YQnHypYcYiD5NCIFAWvmWITkR7gUtVZB3APy1h7SvT9jPBNj9huUon21QgkBAtOQfgoXy8TUTn5bbZSkAye0jwc2qYtrE8QqsKUsO-DKLXvLY_ZaYMV3kesedyQfZw-ixp7C2L56jZKqPK6HFXEx6J4q5Vqrs_fkf7cIwygJ0-aOcJ-edcCpS9AwUw17XQ0tr16oH3qxIwJ1VqWLEVLPbf3eYKg4ouAI4jSA1fjQg7Gik_YI-dwOdsFsLXHLoboDX0SjvQt7xSRBkfilfi39_QFP8_X4pZpZZYMiD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سانسورچی خیلی کم کاری میکنه اخیرا.
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96867" target="_blank">📅 22:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnR2_ASNaHRdVS49b3OcwkWrkvO3kpYF7vgu5l21vkCDsJl21Y7S21Jnt6Z8YK_iag5qBQzJ3VXRWZYW7oTVvOMrEVPB4F1rX2Odf23CjpuYwZj3KMsyBygXgJTFsI4MOlUxxT3ZOeEj_pIgtpdCUObjYQa5tZg4_Y8pymeDfJJjtGl9YO9Kn-vpbc91TpPmP0Kc9-GKLaDi1oYmN6oLJmx0JdeBGklDHn9xmgI8gJRriSgfPg6Ay6IENNd1zwvaX4wuy2OhKYWHoFKquf90jtNBKYKCBt4pdatA3FOu7RNRTcmDFy8WkQpgw_XzyzGb5VewczXCphlBaRoE-FdJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96866" target="_blank">📅 22:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آنچلوتی این نیمار ما چی شد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96865" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گل میشد این توپ بهترین گل جام بود قطعا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96864" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عجب بازی ای شده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96863" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تاییده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96861" target="_blank">📅 21:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مشکوک به آفساید</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96860" target="_blank">📅 21:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/60a5747017.mp4?token=f5uuOa0LgnWdHcIym2vvuZpmSs7-PPUaCxdkumtwQjIrBh08YW6joVar3Gpm4Dk6aH29fuUN_96JDUAVXJWl24hl24k_VLENgR3A9TMmmiI5P_nBi8iQ6ap85dhm0qvvNhVJawmTxby7-x9-Z4zGOjQv-O3QO1F8azI7NE5br56Q4pIuKLda0mHaAgArl2zXwmGihlYTlblIu-DxbyuZb00-ivHd-vwgCm010I9-efAGU4aU9cATp3D6Vm6oKn7gVly_tJznJTS8WA-fUqmaDrETYOyJpJCA2ox2QWp4WOaV5BtN-XSo9FxEqBzw_gk0Mhf5mwJV8FxodB4oiSXvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/60a5747017.mp4?token=f5uuOa0LgnWdHcIym2vvuZpmSs7-PPUaCxdkumtwQjIrBh08YW6joVar3Gpm4Dk6aH29fuUN_96JDUAVXJWl24hl24k_VLENgR3A9TMmmiI5P_nBi8iQ6ap85dhm0qvvNhVJawmTxby7-x9-Z4zGOjQv-O3QO1F8azI7NE5br56Q4pIuKLda0mHaAgArl2zXwmGihlYTlblIu-DxbyuZb00-ivHd-vwgCm010I9-efAGU4aU9cATp3D6Vm6oKn7gVly_tJznJTS8WA-fUqmaDrETYOyJpJCA2ox2QWp4WOaV5BtN-XSo9FxEqBzw_gk0Mhf5mwJV8FxodB4oiSXvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول برزیل به ژاپن توسط کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96859" target="_blank">📅 21:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برزیل زدددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96857" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96855">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96855" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96854">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjqa9koTTOaGYhx35niVMMbFupl92Aqf-5Eu70mW4wF7F7GisrLUQ-hVLy1nVoz2NZtda25bYdsl-8hv5w0FWaceaj5hfrWJ_aKw1K0mpLJfhwUnCtZvSpz50mkCcWoTmyiPUZJSg9zTswVA2RWhYEn5ihSN-RVl2w0TEJsweAuwjPGLHbyBx2-njmsquipAHyB0k4Rw7ljRxEWBGVM5nZDxejXqfWZ4G3zjXhLegxBvBL9BTjmvDPiYoc3Y_eHw1soDT_iCcTDN-2ShW0K6_6cNmgujKc0LvFaTRKKTVZr36l4QLGWd2mzi0K977XMnHk6CB6iQ7U6ZBn11Wg6HJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری گل نشد واقعا برگام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96854" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96853">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این چی بود گل نشد واقعا پشمام</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96853" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96852">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برزیل خیییلی خوب شروع کرده نیمه دومو</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96852" target="_blank">📅 21:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96851">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشم ریزووونه این سوزوکی</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96851" target="_blank">📅 21:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اندریک جای پاکتا اومد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96850" target="_blank">📅 21:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96849">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inqlTpBS6lQDrGINw5MPEiDija9ktonrZaIww0kiRAjFkFiOcWBA4H9pu1iZAIfIfSbHGW6IHM5K3vi9AT9lbBh01IRRLn_2TD-QTGsx4dtp_EnF04FhA892P8o5e7uypIvL1R6nCrpINprh9FpDU9DzJcsTbTPRl1lRFJsy-txD4qHmuNQX4KrJ81eSCw6TPtJMEAUZsjCbME_9smsMKOtaLiVBI3FOMN-eeSZanCoLrI1WTnIRb9Ljt3sPg95LTvIIiG0MPLMocCYALOWZeCb2GdeGvBdbT-ZN2UMlbmECNNLtuJ-vRmkzV6PjpOJSjqvG4qi4MvOP22dvvphFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ژاپن تاکنون [8] گل در این مسابقات به ثمر رسانده است، که بیشترین تعداد گل زده توسط یک تیم آسیایی در یک دوره جام جهانی است.
🇯🇵
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96849" target="_blank">📅 21:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDk8YYVhQFuGBfadW5s1Ob79MTDfVfXnZpRcteWqJge0QhjpRzyjFx63CCaCdMWKWOpgof2xOznitEsc4ZJgeqpEbYoyCpgT_EoC8X1b_glgyG3yMU07yD32atqe_GQnEYty1D4x3MGbVVQHdRgQBCpi7pnYR6-eOYTt2bzq3N31iiRKm8mvdl_9JdGY-WDGH4F6fgc12-Yde0sJgYrSoqnTGqFkRD8OvkW4ZWzo-D6JMAlZho6kxFFpeNX8hNZZyipe0oEKW60JdEJ5xRcObMdrhAeOI4pFk5GX-bszla5Rk16OA3hmU3PNBQ_NsmJ-jX5w3sHVOSFYJvONHGN0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و ارقام نیمه اول بازی برزیل و ژاپن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96848" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96847" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtdY5uXHYHCSYAEuxFNSIIXICkz52_rof-V7_hoPlRzchz-Em2B-b4YUD0XS_FS-kH3tEK4IcR4TdHIjnsJ2Ihn6sIOIxl09e35cK282MXQRGZuqc39Y2tR7tNDFNOCO1tQfVIWWBmCyWSwodCd4cTSkNuP3zaql7q-LkAnKooMT6ZigAWcq7GSUoVuwu7TFsy-vhprk9MIR9bu4voNPu8DrvUiNXmIz76R-8zABOa0eYuCus5YcVAvItbEGNf3wGXBnXC7Shw2paxVSwbgyQKK2N5IsmYlFjGddHpMlwNgNd0rW6MLkRRTp4I56zwmCPojEctcO98MTDAkXUWtfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96846" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5K1C5ktG6TiuFtrUh23660DifG8CiGTwmUk5ugUUiKKouogPlLyfWITBZJqv2YV4M6hEAcPBmiucZQS4I3UftHQikX01mpJDV5VZGAeI1r4lyL68lG8vrGBolvxrLzUZmpmUiwERQsWLA5ywJuRBCfJTYvDaJO3Z9x2TRqphNil4y5JthZjPDn8V-S1GMZMwh6FzTTnlPPAT4CGdcs2HF_-L9ygCs8Dlqt4arKP-QAUPtJYmvlxHJjo5TmKEYu9tTYSr-XYrnx-CV_F5WLW12EWc1Gaboq9utL1bspMFlKQhWxNUdVwCMsKetzB2fcNmycQml7f4f2Bkk8eJe2E4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
برای اولین بار در تاریخ جام جهانی، برزیل در یک بازی حذفی مقابل تیمی که نه اروپایی است و نه از آمریکای جنوبی، عقب افتاده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96845" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پایان نیمه اول؛
🇯🇵
ژاپن 1 - 0 برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96844" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWfmJxzCPa24bavDUuZImq7t6328c1KwTH6dg1_VuPVAvoO5RV-q3Vhu1iQGoakJsw7HovP-Ki8_u9d4gK0XyZFq5Db1es5VpPrZ0NcmvPnnBxSJbuOd5BiuKKjv3GZ93ziRmHP4r1fHOz4fUGhjOBLfq-9fJ94ouci60cviH_8dH9ooa8wbEWvLLRKj6DgBci1as4IAYt6uRYeVDPR4AhvjwKKsuhoRusVbQSR3PznHrPRHyc3XNzL_-uEQg183kCtFXz4tmQnheMyNJXzGFrlOMN8X3hUYiTvg0KRzdEiKY-iaiGv-FeeVS4-0Vswu1RNV0HFa1TTXe8CK9NFyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96843" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کاظم داداش چته</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96842" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_T9exgvPNyN1gILfyBNxfq-N0U_6kWTX9T1BT2zhoBXqBB5fEff_cdDVR2M1cYc8LFbOGdUuz_eMnopTon89R2CGD4NU-zf-zI2rJbDCSue2cQgNiC0vHPD59MZQuqm2GYdnXH0_GRwepGzCkn7IYdFbzNfoJLdf1FGPvhlhl2zosOJIbyjOKGvawE9CKgWLTB5GlALSg14TGPHmFyA_5OEkl7n5gyRMw_NiPya4n4imprZDxFQk2hCSUUQU_TMBB6qYvjcdqXfuyYthIB_j9lWI_eMDOqeQV1_Iykezj0NlHPQYSrp_c43uO9imbVVrlxrlnye9pHiEWCMlwXvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون ژاپن بازی رو اینجوری پخش میکنه.
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96841" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDcyIbPG8U41FICv4YqnPIYRVLGzUEgG7VQy_frfDhLKnFOlr5fFQJFJkaeiv6KptEZ18thUyYbYG-YZZjF92oF-i9_Vqa9nVHexZ5I4oMocEm6JAJq0e1pca8CKOZsQbgixgjM9n9RQWoafLKqFByOkdAdZtjPNx7B-NMUp7SNp2d7RkZm6geTQGlhaKEDxtOaL-muzFeUuuh232OfdqDMBYYQnQNF_2AQGO-SHTAeSqrN7gNlUfMWJ5NHbX5P6VOr0tOoJVelYzGIRCF9et-xAlyCzWujaEKwKIubVHEOQyHKW1sAR_A3jepKfaW4Yi13sS_wKJQmCF86zwaH6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
گل اول ژاپن به برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96840" target="_blank">📅 21:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خطای خوش جا برای برزیل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96839" target="_blank">📅 21:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خطای خوش جا برای برزیل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96838" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">با ۵ سانت دول با چه اعتماد به نفسی بازی میکنن واقعا آدم کیف میکنه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96837" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e64cdab91a.mp4?token=Ie7wAzaOtDIRYeGoAoiCJ6tfmj_52hhXbV-iWq-TISzzmua8QUqcpVBgVx_0rqWMjOEIrH-5aTdVvsufi7BuTkc0PzvvWd3Pg0DjcweNUKhF48J6DpclZzPvmc5zs4d5sIFctJzU0u0-Ynxqf3RLMuXxy2PNZOPyqhteSspZUJxrDsssh49GdFte2Taok0PlGq_X-sqQGsLt41pefUGpyQExVLVFAzX3zzb12g7mopNVnTqeg5dF63u5xwit7k14ZmbOPigAx2axX0-C2Wr8X_VqOO1EfRRgCK2CMcGzxqEijWx0QPlMqbP78knHmrWnkEkSk0lM2HB_7P2_H0WUIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e64cdab91a.mp4?token=Ie7wAzaOtDIRYeGoAoiCJ6tfmj_52hhXbV-iWq-TISzzmua8QUqcpVBgVx_0rqWMjOEIrH-5aTdVvsufi7BuTkc0PzvvWd3Pg0DjcweNUKhF48J6DpclZzPvmc5zs4d5sIFctJzU0u0-Ynxqf3RLMuXxy2PNZOPyqhteSspZUJxrDsssh49GdFte2Taok0PlGq_X-sqQGsLt41pefUGpyQExVLVFAzX3zzb12g7mopNVnTqeg5dF63u5xwit7k14ZmbOPigAx2axX0-C2Wr8X_VqOO1EfRRgCK2CMcGzxqEijWx0QPlMqbP78knHmrWnkEkSk0lM2HB_7P2_H0WUIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
گل اول ژاپن به برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96836" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چه خوشگل و راحت زدن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96835" target="_blank">📅 21:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برگاااااام</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/96834" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلللللللللللل ژاپنننن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96833" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دول موشیا چه بازی ای میکنن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96832" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTV99gUSWCtStfGf1Wp9SL2yBWLClrfPEWG4WmafghU-GfiCU6uyLLjYnh_CsWYS4yHOS8JCs2hBFbscyS2GTc4PoNdmE0oZ53SCADVAb9TDfyeEWsh1v6SeJyjPUI417Ua3yVbjU6dwXbjOu48LW5-4IyocMeOCbSCIAb8YzsFtaZQ4R6N777lW0tiK-1BV_G1J7fDR1cLXlZeSE60vYOi-yqDQQz17sBamLNGAUY4W3-jca_hqtUBf-pRhc661sLE-4AUITpND3DOuKcRC0RcpB1HFIlfj73y8YSMvacQYxfGsB1VHFMNz3IoVWb-ljEqy54zMSEz4feT2UxNk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرشیووار: بازیکن ژاپن باید تو این صحنه اخراج میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96831" target="_blank">📅 20:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سوزوکی چه سوپریه امشب</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96830" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برزیل داره فشار میاره</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96829" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZIyfmOUekOHx_rzI-5aRQdeZ4T4v8n0A6sQ9Epl8XysioqdRnZsS2cl3PK43ZFFP2PlQgaUjmty0JhW26w8gcmNKxSJNVlkg7Y_Gb6IefbszvpacO7gy9B2eRJCNt-tEc1OlARJnWRmzXr2q2fG_doDIk8rq6BcHhsU1ERidVSZX3VJr8X4BnLg8ieLCtR9wjd6cNu55aKz3ezykxX-1OcTbQxdJKDQw402yEB-O1zXHn4rXT2BSTD8I6CETeXr6QKVDNam9Itf5fBaNCohpa8jkDC9yA5uP4psr47ML208dxoOo8t5BSK9539Q7SQsWosjdtulm0dnXTqJ8BznCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقتون رو نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96828" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موریاسو همچنان درحال یادداشت تو دفترچش</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96827" target="_blank">📅 20:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شروع بازی جذاب برزیل و ژاپن
🔥
🔥</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96826" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPHNLhGOLAtFTv10IT1fLpKbnb84yT1C_mQ1IqniGpuzf_sSgL6b1Gj0JRm6lQ_yK0bjrNc49eA3wVvJRVxPec9u1Y_i9aN6H5uAHswf1S1Oc5CoNyUKELlyAWzgCQs_ekLaf47C7lY_IgaagCACOv8185xIdPbFgnsw619Fhaz6QsnYYMuWp903dGhjDn11Z3nh-dWpP-o0r8bLtDJPjOjjoREXSN-Mmb8NKyELfD4eFv7Fh-oLwmG8UI0qUjtk0NFyQDVWwY-fVo3JOfB5mAB0KW1aV2ygXYg8ocT6Sbpu8PoDQTQOfDAnAzmGfsCDx4C7EJM01Wb3djrNizOYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور رونالدینیو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96825" target="_blank">📅 20:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=b0fYNpTqZ3071DGUEI54P0jj2r-0MGTUAcIZJZhaQs85IDGZ2AjfwhepqSMP6Qya1Z81ry-eBFi2uqMKC35VQ0tXZBARt7Jue4_FRaJvOvBe5p_SHmX0_7CU9w8YrEjkxW8nt8qprnlSmdhNosS3PQJU-GOgcv1Q0reqQEC064dou5p-WTXpNBw223E1chREf4RDRo4DsEjeacaCeZCdmxcC_j2xbGcG8jCweN2QABTOg_K5idRhBlpcH5za1FgU1BSdrQK__t425Yr2gFJ-1dbUe4JhD4p9BBiVw4kcfCYESvTNjibkHxBbRDJp509_1Ua-FY-5E6oCjcs9HizhCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=b0fYNpTqZ3071DGUEI54P0jj2r-0MGTUAcIZJZhaQs85IDGZ2AjfwhepqSMP6Qya1Z81ry-eBFi2uqMKC35VQ0tXZBARt7Jue4_FRaJvOvBe5p_SHmX0_7CU9w8YrEjkxW8nt8qprnlSmdhNosS3PQJU-GOgcv1Q0reqQEC064dou5p-WTXpNBw223E1chREf4RDRo4DsEjeacaCeZCdmxcC_j2xbGcG8jCweN2QABTOg_K5idRhBlpcH5za1FgU1BSdrQK__t425Yr2gFJ-1dbUe4JhD4p9BBiVw4kcfCYESvTNjibkHxBbRDJp509_1Ua-FY-5E6oCjcs9HizhCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امباپه تو جام جهانی وقتی هر چی گل میزنه میبینه مسی یدونه بیشتر زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96824" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔵
🔴
اسپورت: بارسلونا قصد جذب هری کین رو داشته ولی طی روزهای گذشته پس از پرس و جو متوجه شده که این بازیکن از موندن تو بایرن راضیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96823" target="_blank">📅 20:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=ULZqFfULDYNDebxO8PDhOgfT0ju1x7HptfK7-ySyPxDo2LrUjIbZIr7XNK2_Fofx2PCulcyocMG9_9vVyszP7Sy9TcLWMKEkres-p_Y2Q_TvmoByRZAKac7gCloTIeVZSIAUm8MqHLC1u_nsWaz6adyPRR0DUMn9CA84LzWKIB2gxnYIdfBCk1jr5BCD8ZhsKH-JRmXZ0RS6doMIdUpPmvxCEUcHkIiQA5Rw-isqaqvFUMPkPxx7wpJbULcLj8GXtGjBWGsJN3hrsWnXj-cQdRXFdk6_G7Jash_AsyxlPl3wRrOuoC0RnjlaQkR0Le-n6jn5Amn1VGx1SbRXlEZYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=ULZqFfULDYNDebxO8PDhOgfT0ju1x7HptfK7-ySyPxDo2LrUjIbZIr7XNK2_Fofx2PCulcyocMG9_9vVyszP7Sy9TcLWMKEkres-p_Y2Q_TvmoByRZAKac7gCloTIeVZSIAUm8MqHLC1u_nsWaz6adyPRR0DUMn9CA84LzWKIB2gxnYIdfBCk1jr5BCD8ZhsKH-JRmXZ0RS6doMIdUpPmvxCEUcHkIiQA5Rw-isqaqvFUMPkPxx7wpJbULcLj8GXtGjBWGsJN3hrsWnXj-cQdRXFdk6_G7Jash_AsyxlPl3wRrOuoC0RnjlaQkR0Le-n6jn5Amn1VGx1SbRXlEZYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😂
پشمامممم اینو ببینید امشب جمشید خیابانی دوباره سوژه درست کرده و روی
آرناتوویچ و خداداد عزیزی
صداگذاری سمی راه انداخته
خداداد عزیزی رو ببینید فقط
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/96822" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDateOpiE8fXZFLMB4d1JWJ5YgPVqQHsV0CsbenbqYvfJCmEkuevGaMTfbD3D8nTyrHA1MboXi81SEpaPAUSPTYjjlMwJLzIuINwjGwR3qWAm7cuxZlP7jZi-8e-SepI0maLWXAPWqscLkz7oj9qjAlHvvJUi6DwF4djxn4Xk8YNImKBCWWlu4fjAcB1k80WZyV9zHSOJpaWXBm-k_kit-zzZmnqYhVcrDgF3Qgx75LK7oZ9bwFpKmuIKfGIg5SBkCGvW9GDEVTSobqfi8YIZG-Ncc7wXDLdVvEsdJ72oTlomxsszM6RlQNx42gid2uwvNNXA1bFXIF6LBo6cwa2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇧🇷
نام‌های فرزندان نیمار روی کفشش.
⚽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96821" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLOSW3ovr77yviiIWgYwkSNAUMfwTJMdBJE9-rb0ABIP6b4RGWN7zgRtaNo0KHc0GCOQkTnXiJRGdcG5qUjAhkhfTZW2ExiCSd9S8pqCBFwW5SDEoQCpmfcs7uGEkQYlq40TcSM8MZFnGJ8Dzh6RjvJb5wlm2ZNzj8wRzXT1j4talNSzqgVtCUtNVyl3MoBblj-rWm45GZ-ilmXLDf_m4tz9jS27dnV7cSFyLs7lZ4Vh_FHMCEaP5x63-yWntm9nt5gXwqvlEC5-MpTZd4BSfz2F1_vXyYUoZiJZQ6OMTZ7ZVB-nIKaXYTLzm6Y95ueVfrdjdG_DsnpLB5QIvRKMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
پرتغالِ قبل از رونالدو: 0 فینال در 75 سال
🔻
پرتغال بعد از حضور رونالدو: 4 فینال در 21 سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96820" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em7esDFFcrest7UO5jL4h8ThMyoB1lIVZZSqBAy6bHlvOxoruObVZ5l5WoLjy-xGWu1IgOzEQ0MHzndgvG-c-R_geLO-u_oCk9jZvctbQMyfj240nQ5nSKO4edCuFejPhSUv75j35gWkmmUlJ_c3ntPkrbjJRw7qxFgxRvptqX2lpoU7GJC1lN9GzQPbUMVAR-hYNTWE8YRHfjg-RdRtcoPymQkS5BNSgYc70faxwOtuLnqlCy_yrxHhNVilJ6sZOGN_8VnKV5g8lGq6i63kAH1ZNmh0jkhla6u0dOC2ngWqdftovFLVfmNR8DHKAFlVr8thPvrf-dIQIc28zENr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برنامه فصل ۲۷-۲۰۲۶ فوتبال اسپانیا
:
🏆
قرعه‌کشی مسابقات لالیگا، فردا ساعت ۲۱:۳۰ به وقت ایران برگزار می‌شود.
🌐
فصل جدید لالیگا از شنبه ۲۴ مرداد ۱۴۰۵ آغاز می‌شود و یکشنبه ۹ خرداد ۱۴۰۶ به پایان می‌رسد.
🏆
سوپرجام اسپانیا از ۱۱ تا ۱۶ بهمن ۱۴۰۵ برگزار خواهد شد؛ دیدارهای نیمه‌نهایی در روزهای ۱۱ و ۱۲ بهمن و فینال در ۱۶ بهمن برگزار می‌شود. محل برگزاری این مسابقات هنوز مشخص نشده است
🏆
فینال جام حذفی اسپانیا هم روز ۴ اردیبهشت ۱۴۰۶ در ورزشگاه لاکارتوخا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96819" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDPHuElBlsP6GrDxlzcJzRiFzmMwDI3mRddZhOQhfs1J_-CT4F-LqweuMq1klsNhA8KcHclUc6synkfJDFN0L-mrrKUGSnGJAxAHR3dvXY8uweyNL2QTeo8cKSq1EmGvzyWR7vjGdTz8ITUp8o5XFPUMoKNjSy9vG0nnkUvZcSiZP1hFlqtCCLgSCepM1Q61aRKNt6bt7aesKCq3dfRFXuIeBNRYcykqENeYW49z6NB-PuSoILH3YAslA-YCuuPriow4GPRs3Q0pKsqQ0wOy6vYExaDlrqWzASaJ7fOJtrQn84WDAkE7p_0Hq_A7D2oSTG72cbWSjUBMGO-A-q5Rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
برزیلیا در یک حرکت فوق لاشیانه پوستر قبل بازیشون رو ناموسی کردن؛ این شخصی که میبینید دوست پسر مادر سوباسا هستش:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/96818" target="_blank">📅 19:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4223b69552.mp4?token=IJ-okd0587bEmZbO_WV2nJZ7NVV_zHO3mvi3vqyorxxnb1EPagdrsAXuIvOBVvyVNUxA2pliE7u0vCOUi5oWMkOB4j__47hTk27a-GyHGOnnpN-Tf5Px4cfjQqsinl1ssSp_y5zDPXwabs4566wqMESd-rYZ07_biL_aSn2HN7c1LiR3jskTNRcRJg3_1lO2x4J8Y86Wqndf082jIFXyGPoAqsLHcDiZpOq9PRzUYk-pUXQnTrODUlpGxOHbgqrePE2-GPArMnEo7bXmdesxQZjfy4yFuebSDOl9kdALwhy6UXP2BIbtBtkwiuYugbYBEM-hyNp0Bui27t8hQ0yFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4223b69552.mp4?token=IJ-okd0587bEmZbO_WV2nJZ7NVV_zHO3mvi3vqyorxxnb1EPagdrsAXuIvOBVvyVNUxA2pliE7u0vCOUi5oWMkOB4j__47hTk27a-GyHGOnnpN-Tf5Px4cfjQqsinl1ssSp_y5zDPXwabs4566wqMESd-rYZ07_biL_aSn2HN7c1LiR3jskTNRcRJg3_1lO2x4J8Y86Wqndf082jIFXyGPoAqsLHcDiZpOq9PRzUYk-pUXQnTrODUlpGxOHbgqrePE2-GPArMnEo7bXmdesxQZjfy4yFuebSDOl9kdALwhy6UXP2BIbtBtkwiuYugbYBEM-hyNp0Bui27t8hQ0yFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96817" target="_blank">📅 19:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN6-T4hVCmMW7rB7L9pvzWL6PMEaZCwg6-dXLSquudv-ECbkbphzoimyEO30lXXRNm4yPEDGmmsHs98AMrVN6Gb4Zidxyo-Y_XWysJjoma8ISFpMLNKgmdpr3ryyqHTKDtrngVdMP6oicfa-ToXhHdC4K8N57cBVyBMk5HyPAi26zEuSp5ebESkHr-0ddU4XtedykAnlBL082hbsGD28Ql-2A6394iGA1jpjVjWb-uVlQRy830jbPifC8DH4PyzbMJoJ1PmFGrW0IHqUg0TrWobY9kmz2e5pX2wYSd-VrkOC8cw0bECXfEP47sSQOsHQElPG7tiD2IGD6mo0j0L60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نازاریو: وقتی به امباپه و بازیش نگاه میکنم یاد دوران اوج خودم میافتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/96816" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96815">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekE6QTNxYJLIaIwzkXw-vpeRG4SKyK3F8DS9XYkG2E0vKFslA6vgrHgWqwS9AJsQ3QVPnRL7HG9i0tITN1igefa5VRXBvnySID5KofpnTfW3PGhLwoRnV6I_dWAlDmZv1m3RuGiVRrS2n5Vf-FTwBdew0Gg4s_qYyknDRiGZCaJSThfUuB1VPtGK8Wrx8fv7rzuDF7I-qEjRRnAY2m-8WY_VmUgcnp1TooI6wEteyWp90tQFXC2BvvGxWaJlcM2IjwkUOHbrUJ2-1I_e4pK0umuzf58MUz_BsZdJvazppFn26rL7mYRKGqA65WGAdLVe5WK_j1n7JW806h0oY1J_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/96815" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OE976JbBl9R2m95Vx1LA0_6aCFlhUQvYskEs6IbfMl2F8F86X7QwibZOYNu9SwPgo8fCww5ZZICNMJqKDvPWATxioVe0E68emWguQU1MbV45wQIx82w_uxESzkaI5b5NwgQnMK0mxGs_ygZl-fOb9cH0Yfq5gEsXnHU87xm4MdThvIIDpUk_rdMTbv8r46dqQe5Vs9sILM4SIZYuMZqqM8aLpBLi3xFKy02WitW_x0KiHcGnucTP6eQ19TCXLjA4fmiFQZOZY4Q5OlXwp2b1Y1IQFJje0NaJq7qoq6sbVnqNY8acOHZAxtl6fsuKWfTPBrijLGZumYwH_RPoS01eAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4oOp7OVRdnS_BJz8Px71k_S0BiuUI_REf3Qr1AkRwmbr-YnshIpvu9coqz81AJ0Z17F5vU_b8AlAk3NgqApnLZiMMtenqtXezv5juqMuApCpNn4gSgwOF-6IQLbJuZn7j2xswrexdxtTHhs-0K9L_2EuwGG6XJLdre6BY_YNRaoYg7UiLbhLcwsfBiFzHS4Tse27uBcdqPom0v6Y-te2cUSQXMVe4LGExH-xBg79ThOPDa-En6kt_8f5YklND1QqAIKc4jV0bxukFDewwyf3LsOtSEXawbESfkowCbS31ikGquyivLsDKa1gVvlFAyLrzapWbkIplFYpt15Fzn3Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96813" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmXMgrZnSeE_5gsc6dBVfWiq2zWmBfubxLx184EMn02LaH3QcQDZ1wNgP-eFJVqJXKbW92fnUJB-Oto1v-2ukPy0UJGxcheEIXBb36nAH3EwGNB8-yFPD64uczPkYesgvgyTVLtfyh0ARhWYtaSy7O_5cuQcMTOLZ5ow3LYVgtrxvZgwwuGAuH8nctovPM4cRszMP_t9PLKIFigY2l2lA3IJMj7Ko9Us6UXK4NZztcpFLVkBP9_5Uz3uMBthnniaR0ypGeHCxvkFw2MWwlRZ5uOcW2S0Z6HfsgxrKgKvCINYhtkFVekOMUMiYP7qOa-iWea515tZNx1RMSWrcamWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96812" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96808">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEy22kuX3IXWnYnG8iCdNAc4X7e6BrtYcdZ4r292AUJOuTXYvzsFsieXkRAO9UQAoQ7dQdvy_6Z4neBvaONjRMoKYS4r0VeOPg-maUQNofj9cYrjQXZZxFnYWcTV1CcMU2tUzVmnNPq1EkGdG1C3FjhrJljKqrhjO9DOAq09nevTIh1r3WhCJUkxHAz6s4Pm7rXjlqXriPdJjDK_1FBBaIIUF8P3PZO7G7rMs1q2FIatmkscJ3YJHqEVYCw-xfBTrsYUnOSN91BD0n9lcdXsvaHcZsFQcWw7WRfKjSzSwc9suU25uT2ztIqZ-J3_20UyaBvJUI51WRdcmW7O5F1jCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKbdgH6Hxi9M7t7X6TpXhhVQX-nnDvnoJsL7P2IEGKVo0oM5M21MKdg3dgtmSceh8WLJG97vtmR7b6Wbv6_QUWFCQMIrF0vdEUvt3UO27NSRzbvLgNARyMMMdM0-gjVttw5a8aMlUXCyD449dDLI96S52h8EBSt2gpSTdlDX96wnCOGf0xNTGMkMasaadkysr2XcXVMXD5dgfRldFnnZm4JzeaZq0tIcMnTgpD39p39Vz2zK3MSbVQaxIr_tr571-FOXSKk4bJazVYaY3LqEhUgfRko8I8YkYKfoE158GD53prPRiLQXRfJsWYYGSdjr3AgNEDaiTMBf7_hyMYMiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFArsZOQTb8rifXAwBburXCao6WcMUkZ7rUXgmrbm4jRyQoJlYmYI4Y_JoF-EEnTMWCIWpOa6MHHkwlMhbJ3arXFIBHyT6JPnhMO8oEsZngynJ03g9KRQ-PW1tvtx5Ccp_C9OGPRJME-CJO24Otxjr2-OQR3au_EiiTkOcwLYSa_MiaZpfeZvPTyAtsXZE0miyV9_70dUDcUQm6TLQwdpsD1N_cSNyeTF5aRQDBYRte0Fnu-mLknKBr5-irlPf1MrqJQ4NTpSvbwAvBViB6Zkgba6uMmW5S1QSzdMt_7_zuYc12cchI1OfdY3tAVzmXFISvDk5I0RT-VxeBmy2HNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwCBhDWNNp1Qy_zPKA7k8z1Te6wZBaZXxf2WbvsvNYNdsE4w_aNlKtZfdCN-1vIdfzORxarCJJ7t-2ZoY3Dl_Z14UG9coMDf9V1FVWsYJ-4zdEoyQfANw94rLZ0QYacJedUVYKVk5ucA_f3Ljnc4U17GGmdEWia6yDmpfqXXlWAVQ9zfDbYyZtPC5B1oVOo96RklUeCBOu4JzvzEUoa2iEjl6sHq_nX4XjuouRup90caAWXFWRLxL7T1OmrpLV8RNbugUyN4GatvpRqYS8RzhWnehjqPEDHqmJpWzFIyjMy6A7t7d19daHX_bGAHOYIUlVrQMKeUr0O7GFOxBbQ8ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇨🇭
خانم‌آلیشا لمن بازیکن تیم‌ملی سوئیس هم رفت قاطی‌مرغا
👍
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96808" target="_blank">📅 18:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96807">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fymN9I0Fsi5T0jB67zyGDp95c5RNI_OYTHvGIIgE7CElPhIdMWGE3x9Z2c3xLuy-6tKeYSOzlIbb8CRkPiDsWscDDg3QMu2t43rpTSGT9u6-o7Q1hSVTV6oYZZbAqYmukap--o9Xj1uuDsHfL4DJrPNyBGeBSBDJbmUgst0lXdnOXEfKxtiBQfGFss7blFfhxTuxZCQpzEj9FpZcBw-qaxh0KtgAJnVn8yTtDrpJ9OfgnZ49Pd-cLvy0aOGYmvRGiZeHbqtZC2OAaepvElAC4mBkatil2DyyP1DIbFo7TzZ9XQSd4beSK7KQJAu_Nrn6afS1nrMXXvkErPnAoRO5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار دو تیم پرتغال و کرواسی همزمان با اولین سالگرد درگذشت ژوتا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96807" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96806">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=eFRsNyLkuzfG8F-MhtZ7TIvY6WxWZ46Pq_5V2YEO4bBmIPLkVObADyoWyPGgN_EYyaWdxiYDNLLEUIYe-GxA0ZcyAOR0LlxauoKYs4aTzrGdK74fnZRsdpEzC1ywY0rFJtJJLvLIeMrG3m0h1krQ-6tle--7_n_YqnSiielB2z5tlNVtWS0q8-ITeVL2qeZxu0K7ebc5miGOdKyZKM8gsuh64GH5W_1-u7ti4QQTI-YiPZOE3J_kJvUAv5kLvqmLsvXLCRZVmM89VtYYoPeyW0FojgpiM2Bay3LhJkZBbiHeA4ZnICPXltP7S9wix1mhVB-3iWHhumPdwPI-x2WH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=eFRsNyLkuzfG8F-MhtZ7TIvY6WxWZ46Pq_5V2YEO4bBmIPLkVObADyoWyPGgN_EYyaWdxiYDNLLEUIYe-GxA0ZcyAOR0LlxauoKYs4aTzrGdK74fnZRsdpEzC1ywY0rFJtJJLvLIeMrG3m0h1krQ-6tle--7_n_YqnSiielB2z5tlNVtWS0q8-ITeVL2qeZxu0K7ebc5miGOdKyZKM8gsuh64GH5W_1-u7ti4QQTI-YiPZOE3J_kJvUAv5kLvqmLsvXLCRZVmM89VtYYoPeyW0FojgpiM2Bay3LhJkZBbiHeA4ZnICPXltP7S9wix1mhVB-3iWHhumPdwPI-x2WH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
💥
خواب دیشب مردم برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/96806" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96805">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX6ua-OKxXxUD9BBh3ZP9kkGgDFTboZjJFHdEUf5N8SN69NlKo0onsX-HMRD4ncxUM1UqVe_deCxo-id-A7HCWgPt6mhxxLi8f0OU_SsH0Qa4PfvZhLQBHpuq_4S5q1q3MSckpyq4AML049bTYQ2p_S1F5CQaG39ICN_YGFTUB325sOU7y4husv-5YEPbbSFf0VyRDCp0_o63_VN8eJnZtxGe_wjDU-F8yJab_1nzhdJ81jxqYzuFginZ5WeQed8Y_54etWYXzjEfjP7LKyDAtv1Q_GlnasM0KrMHmR9pBdqiymFZcnqKscYmZXA61h-jpXZbAlt-qkJ8joKFiJBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
68 سال پیش تو چنین روزی، برزیل برای اولین بار با پله 17 ساله قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/96805" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96804">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیس ابوطالب به جواد خیابانی در برنامه جیمی جام
والگلد قراره یک کیلوطلا به شرکت کننده های بازی جایزه بده
و اگه میخوای برنده باشی کافیه توی بازی های پیش بینی جام جهانی پامپ بازی کنی
تا فرصت هست ثبت نام کن و بدون قرعه کشی طلا ببر
اینم لینک :
👇
👇
👇
ثبت نام و دریافت رایگان طلا
کانال تلگرام
@pump_vod</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/96804" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96803">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK22HKhpGJRqN1jbRuGcBTN38pCg71Dzz6AERibuVRcbD3hoyMMsUWQqcnxev0bDhZbLVPnx1ut3fDCjUQw73aRD7x7XUYTYcWOVh6lDxnUTYvwaFlmkT6hWfIsNinpcG6t4tyRnz4wDx2MiUqxSIk87W7aJ7jdlVFEWTO8nuO94CvFELKnS5nUg_OyBynIA3XgNgD-bAMMGykyYAMTp6E1APdVgblXknrbG_2FekSuclrfv7rvVoOitJIAOWtHyfKywk6bL6uJdsWml5UHNLgVwpyCFQkWYTczm9i8ckvo2ahooPvlraEcqiCwlJcYzv0L7azskz-87Tgu4XL_Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت هر قاره‌ تو جام جهانی 2026
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/96803" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96802">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3G-Jz-Z5U7DzYCH0lKpp0vT8kd_ZrWpgumQBAcbQKiFutg-98jdtOW5LzH34pxiYKhjxhZ7M5iZUxCdwdKR4xPEh1WFzTPw55H9Kc1dJfYug0DLcbW76zJ9WMZwUu961OCFeNOra6AktV2ygAufeH3p3D2HILvu9ovzLeYIyWTbDGrBxQRM0zaFTB7YMru5l1LAJ5W2XQjbR10mDZAdjroTcfqz4BNOnUnVe5xIYdYw3ehT7Ij8ziAc_Hd-I97gLRIOXbdUE6N61m_TkeGgDIyFM8auslJM0xHEF6Iiqc8oEFNLNuyLRGalFGwaTF4ZyjGGVOC5FKP6v2Zx_GuVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فهرست بازی چادرملو و گل‌گهر برای تورنمنت سه جانبه آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/96802" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96800">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG5dY9ae5go9KbmYkR9TuvCX3L1S-UPhoooyxh_06o0W1CLJaQFkQGH6TsAYYbEcWvSiSebxKXCmYNLnNXLBPffVNwq8XegdRi44VTLhku0Xtc67P7286z_0XtXuXab59aoLBAoF35_gemtdlhcg-OgkK5dVrtBgMM_cea1-YIceCJrFrJYy2Z4X_uEGgwqkzpTdRlqHM4LfhrtHtmP6N2VSVPPvb3ZmWyP6XnX3fMIbRaxynRIxs2yp8X39KJ1wKkMTWzr7YO3gSxL8wk7vZyKUBryHa40r7GagsSIajGoEY3oQmqWUr5cOKKcaeofwBaANHxqgzymqKBtR-n3Udw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8K3oERr1wzfSigb_eLzOqmbqT76pGA-WxxuOLqIdZbcVnv5xYtH3qFDN3ExbFjc65E4PvdUbe7NcYB8Owh0EFJjuaAtjpAoib1Pq3Ct9KC9-nMkNUDwo1qFwzthenEKwMFBW-5KxiPE3RQEDE1tFagNNXnu2nd8-46Pqb0rO_obcbrZMKQt-vCWoCO32iFOnsceQ5nZXzbsYzgumeDDAKo-PaI9zKwPp5RJDSe0hkmALttC4y-PU3TCXvRmioNxgWcpK-SLTG8uT77ar0thbV2u1DjcihRHCBBgPKRq6uNvnS9zB4ccTFuUPC_SCJYdOyDdLjla7gL7BtAbH9Uiwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇯🇵
🗓️
۸ تیر
⏰
۲۰:۳۰
برزیل
🆚
ژاپن
📌
برزیل مدعی قهرمانی یا شگفتی سامورایی‌ها؟
⚽
🔥
برزیلِ صدرنشین برای ادامه مسیر قهرمانی به میدان می‌آید، اما ژاپنِ جنگنده با امید خلق یک شگفتی بزرگ وارد این جدال شده است.
👀
🚀
⚡️
آیا برزیل مقتدرانه صعود می‌کند یا ژاپن همه را غافلگیر خواهد کرد؟
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96800" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96799">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cykNGjOu1YUhFX03fYVJw2jvJoLjW4DCwZXanHexRMifWCOGR3USLQfJbMpvZdzUBTxpXMMsvmKbsO9yfyF-PQIQGwv312hcsQ9SAM0GJcmB9cgaggIQKhAa9pj0J7zujbc75ezhQLygyWD4WF1GOW5sDj3XWktLt5IQpf47UBXDd61M5vOatymohfIhVUMEVjLuQ8Z2VqIMBZbFu-n04QUV9m3ImtA-9r77ORTSL3z1ePUYeu2P3lpIXG6xmgAfWhM5aM0yoxeHQmRJ_C1rZU6aXDGuslnEZprquh0tX5CYSNi9aGbnBAiEBskxbVuy03sJBKVBOiXOOp61OrcwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
فکت؛
فقط مسی، وینیسیوس و صیباری موفق به گلزنی تو تمام بازی های گروهی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96799" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96798">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/96798" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96797">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn9QJ_WR8xip7c-QmS709170RuD0QTnT600VpUd7h2i_GCUw2cbnROLXPsMuV5Z3jDv-la1VnJR_mohQDl9G-Yl_QTOxt8b2Dh_Wq_IqIvAR3WAKI0GpA6wIDeknMl5dXlAvhSNCAY8_8vxpQyZw8n8Bp6YbvENvAm7jhjQyX3P7go6TEiebnBj8nSIDSVs-yrPaUk42Ep143nSxyZrSb-1d5Ocx2X3wUXmQBDxEDCwHbgfhrwwn9QI8HPKEy6UuvGDmLlrhKMNzkQbSu7GEtKB1V3aYUmwZGOvTV2rhgaMexJDH52hVMT33wANNDgdPnUIR-rj-9k46hYgFjIW2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
پشمامممممممممم
🇪🇸
‼️
رسوایی بزرگی درباره بازیکن اتلتیکو مادرید، متئو روجرری، امروز صبح فاش شد، پس از آنکه زنی پیام‌های خصوصی که او از طریق اینستاگرام برایش فرستاده بود را منتشر کرد.  طبق آنچه منتشر شده، متئو روجری به ازای هر پیام صوتی با محتوای جنسی که…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/96797" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96796">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
ایران صعود میکرد اگه اینجوری میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96796" target="_blank">📅 16:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96795">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE4PfhhpbayEioql6Tc1RvnQPhrWlu_aKz969I1LODLGaS1gxc32g4X5kFevQqQMng63Rp05KyO8DX_ESYSPNcR1r2iFZPH2fmwd_peGu4NbKBXCuhkvU3sKUtFUC3BYBRq0vDEz2cX3fDnNNU2mxvNFszoMMdnzxbD7i50f1wRjrzjOULhxuYZtxO6LtzgfbKQwfeVlQSy0pum61-GpMBWd6BEI-JPPAM5JfCkYAcOCS9oIQX6EEP-wvh4-7i2shH4f0BhdJJBpu7T8XB_szrgguImDbBeFKD_KlJBROADN-1RQ75JqiuQ90-75mrtaJAl81LoOi9jCp3oEfW-3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96795" target="_blank">📅 16:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96794">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDbmZDmWtN1UfnbVFgFh31q2u-UHGPyX4ecxsqPh3UTp0NggO88wHelCQAGs4d2i1RSv6KNyxvdm740IX67djg5hydAkcT35j1UFy9M91oIV-UVKAkFhTYHiSLQF4sd-Djq12vok8KsuiDpekIbmPfBKFBowCVUBSvEWGh_C-tMij9P7ONV3VTHXDaDSEKnoRQEiY1nnLKreh7XZhocXNeNklSO4O4T5I84TRJ6r_FTmN4TNLZtsOWbl9wzSfV37XP5P0lwo0Ra1TCe48ygw60EDMYoy0KQ1kLcuze6kWHCNhgtXCfKD5GL7fZkfjn_iU_bmTV2Lyh6b11ZNDJrfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
لئاندرو پاردس و همسرش در بازی با اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96794" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96793">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=g7c__E_Ev90k28Vezyf0fHz4t-gPSSxy7ZNFQyVNEkmqRO-uFBXiNDySNhReTkzfdd7ri6RPbh0hlRPEqucesysk05uJxVLnjdDNLcqyFzOBoUjfVLK3Xs8hr7PBuNRFUnmIpLg2M6SCiuUL7tW4DgUEzTJ86Nia0xn7Djcf2u3wmo4Z_mq3yQJA-8zmOCOI0BbG40m3LpCQ69QfOQkoqlAseSZCkBt2JeFR0TtCOycIQABJPqJh8epn4sR77D8KjjyvmAv1s9GKdcduNVyJXqyP1oOShF26ITzoXqyV3t5EKUKoJk-nNBphD7vWgE6mZo3_-YJyI-XssVVpqyOdyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=g7c__E_Ev90k28Vezyf0fHz4t-gPSSxy7ZNFQyVNEkmqRO-uFBXiNDySNhReTkzfdd7ri6RPbh0hlRPEqucesysk05uJxVLnjdDNLcqyFzOBoUjfVLK3Xs8hr7PBuNRFUnmIpLg2M6SCiuUL7tW4DgUEzTJ86Nia0xn7Djcf2u3wmo4Z_mq3yQJA-8zmOCOI0BbG40m3LpCQ69QfOQkoqlAseSZCkBt2JeFR0TtCOycIQABJPqJh8epn4sR77D8KjjyvmAv1s9GKdcduNVyJXqyP1oOShF26ITzoXqyV3t5EKUKoJk-nNBphD7vWgE6mZo3_-YJyI-XssVVpqyOdyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🙂
این‌خانم نروژی بدلیل شباهت زیاد هالند سوژه محافل ورزشی اروپایی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96793" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96792">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29b044b968.mp4?token=QvRgn6nAdgqOyhZFPzCfHSSJGZqe9PBiw8y4I6-n5-wIPmXjONpJdHLEyuoywdv83GDgbPHr_qfhRU0uTPe_SA2oB2XRkCxZTMOkgIkbBidyqDQjtuEkX4NZGUdzbB_fE9HXydu_fHEueaUzQeCRONUKEojlkw_DRpzLmt7bCLhN3D3LomTsk9C3PZnzpN_zczvgPFJHQUYtXoKeuK9anLQEyONcob_IFdi90Qfi4c8dMP9YKm1mDUev02jnYSah4mTBbbJNJ_dRP7rULUBDIZ0-F61KGNYgDvsuafj23sCnygXqlJnpa1bEOH4WaMAaCBbCtn5GRrh75x8fdRpoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29b044b968.mp4?token=QvRgn6nAdgqOyhZFPzCfHSSJGZqe9PBiw8y4I6-n5-wIPmXjONpJdHLEyuoywdv83GDgbPHr_qfhRU0uTPe_SA2oB2XRkCxZTMOkgIkbBidyqDQjtuEkX4NZGUdzbB_fE9HXydu_fHEueaUzQeCRONUKEojlkw_DRpzLmt7bCLhN3D3LomTsk9C3PZnzpN_zczvgPFJHQUYtXoKeuK9anLQEyONcob_IFdi90Qfi4c8dMP9YKm1mDUev02jnYSah4mTBbbJNJ_dRP7rULUBDIZ0-F61KGNYgDvsuafj23sCnygXqlJnpa1bEOH4WaMAaCBbCtn5GRrh75x8fdRpoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مود پسرها در آخرین روز مدرسه، بعد از اینکه کل سال از اون متنفر بودند:
🔺
دقیقه‌های آخر زنگ آخر؛ زل میزنی به تخته، به نیمکت‌ها، به همون دیوارهایی که کل سال آرزوی فرار ازشون رو داشتی. یهو یه موج عجیبی از نوستالژی و دلتنگی میاد سراغت، با خودت میگی: «یعنی واقعا دلم واسه این روزا تنگ میشه؟»
🔺
اما این فاز سنگین و کلاسیک فقط تا دم در خروجی دوام داره! به محض اینکه زنگ می‌خوره و پات می‌رسه به بیرون مدرسه، انگار یه آدم دیگه میشی. کل اون غم الکی جاتو میده به جنون و آزادی مطلق! دیگه نه بیدار باشی هست و نه امتحانی..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96792" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96790">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is57VvJwrlIndC1leo_U0mQHumhOrryTekiGS1RV4v8-yWIP4LYLACuF_ezqfCsDTxI-8hUYgZXt1ZBSvQ4nS4IiyXc1IqFJGe_bXfqvybKwV_oTERKfHQMKQGps8DyHaJh3MpC3pPBdetZ22kfHSc8gZnhF02bN0A4NgulQerzVCy3SrFlEAf6x7_UOwPe-nshYe95Eh5x9o0YRHAmLGGq-xnhRctDTSFRK4Lt4EaAVjPi_bs6Tb6Hrg91qg597QMxr0OZgEpylCTvE87VcoWBAWZe3zoGqNWqPg79ZPQSy-18Xr5Khy8i8uFhJHVjO9cEbYPY7746tAPkO9bUlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6n179r47qBU1pGG3Pl_12mIsDVXqw_gr93EAH6I5sd7_3HJIDnZGR4FB5C_muyW26oMnUI5N46X-WnlbQlfoCiFUrb_uu5_ho7z-AO3SimmtEgreDIzcuoTVD0kcgRM4lv0lix0-7RZg7FElUBGMDIynUGgF7Ui4D7lL4mm4FIued-PJufT6yzfT5vKzQuesfgMPgYw3HT5kU8MjVVejLd8W-lsyCTy56IsEjKfZOanqcIXcSPhmrJhbAX9MoKMp3VWcSP98IQgvw9XEfucIfU4i2SzSoaWV9FQV3fNmxNObghOEFaD1rto08YRpgx9A3zWYEe-P4Mwgw6z0bXaLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
⚪️
میگل سرانو:
مورینیو به کاماوینگا خواهد گفت که نقش بزرگی در تیم نخواهد داشت، و این مقدمه‌ای برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96790" target="_blank">📅 15:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96789">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY3oOsgfaX-CKXUvD4DjpHyEQS8JzHyE7jpy3mBoaPBZ9Vn5bPrnkT3mKPnXVMA36tC3L7SSOfC7u4Ch2QjXsNuRmnoSqpl08Xd1Pdsepkk148LadmaKX6Tou_bZ8W7qA4TQQQ5ag3M71Du6U4Xn2y7b7szewVox3D8zcO0yz111ccxHBkIo3XPmhamRQkB2mqPGVZejwVQaZlNL54CmiiB0DQ-GT8zxYuUF6ODqcohPvX-udv_DLbSXfo224F24db3X9HDZQUAeDauJ-gPicrcFBD3rwmwtbe_qbFrYUFlL19W9QsF8uzNG7s0jRh1QOvHUwyyCE16LjPpIGmxg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اینستاگرام بازیکن های کلمبیا بعد بازی جلو پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96789" target="_blank">📅 15:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96787">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxLutczwtn-UaFFyiLBFIqv793Xylj0c8OkJ0ZFPMrugHMfKyeUPMgnmDgVarQfxzSe6JckceKqMoNmdGgV3qqSPZwUyLBMbvB20v1C40_yyiWuyEo6w7GAEGZHsFPKXu1UVcuhVlgTfZLO1xfzh7A4a9EE2Z1zQJnutKum7OPNGVA-ZMyn_38cMyzE6NSS5aR7d3vW1t2H6ghoLhwbn55mQWBklsWGX_GdBUSGZZaoNgLhUolCtDdvpyVPKI8RFB-Q80gXykiHmGKWq-_9pkid1Boj6q4mRDEeLO5OrVLPw_5ZAbxuTiyOriQBfUhGQorfr3Ta0a9YwA25_84hgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
🇪🇬
سرمربی و بازیکنان مصر بعد بازی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96787" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96786">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49365cc36.mp4?token=OjEeGUTBECslk7YcH2QV5k2pf0y-IW0JRr1thmmBzkrub8xLsqXNC1AFI2jnWKHDQhghL6zUsdFzCvHiTxDwvhy48-1P6n-zvly4XbxXXBdY5iNIwxcbvSKOlpGOa1lltNhS7Eac_yfviYubEMPoRFM1cslGK1cuJhNeYCKw3h_jR8I8wv8voO_dZ4KlfBuA__U55jY19JHxqSfuK8r9OBSV6gfSuR4ypklvaXY1ldPXcJtyu5ZkxBk8QRqyi2jK1M2IqCBKcM-vRf2nMRdWG18Pp1EJ892iGPEoeTj96KwYobruemrvqnqDVRe2A9_Trm7tROYU1ggxgulRbUvlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49365cc36.mp4?token=OjEeGUTBECslk7YcH2QV5k2pf0y-IW0JRr1thmmBzkrub8xLsqXNC1AFI2jnWKHDQhghL6zUsdFzCvHiTxDwvhy48-1P6n-zvly4XbxXXBdY5iNIwxcbvSKOlpGOa1lltNhS7Eac_yfviYubEMPoRFM1cslGK1cuJhNeYCKw3h_jR8I8wv8voO_dZ4KlfBuA__U55jY19JHxqSfuK8r9OBSV6gfSuR4ypklvaXY1ldPXcJtyu5ZkxBk8QRqyi2jK1M2IqCBKcM-vRf2nMRdWG18Pp1EJ892iGPEoeTj96KwYobruemrvqnqDVRe2A9_Trm7tROYU1ggxgulRbUvlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی برزیل و ژاپن اگه به ضربات پنالتی کشیده بشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96786" target="_blank">📅 15:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96785">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b94bb0e26.mp4?token=Mlac00Vn5MbhkdFPt3IvNBlJy4mM1hc4LzBc-64QCDHkxCE_YXBk4QM6u14ESYeRVW2CvNajloIE1ZfInOw5hBUL9Bjmm-vzwvOyqup-uXUGufM5LrObUSHPL7hHB7_1I3L7ChS4Z84JAPiyPdngb2CvCWNEmKspJa7pYXt4Jj1OgZuQXBAIRGQay9TQmPUv_pS35iWmL_JYnnGgOgF4Gxq7IdGVs8e1eSfkaF6usgp0s2fjlz1IcERwpX4lHMZrQOFeJl1-EtEU4yEGkprLfk5LR43ZYdRzlbdXpaMe0JqESr-st034UVXztGZpeLxhsL1HLNavlFAYg2e-j8Kabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b94bb0e26.mp4?token=Mlac00Vn5MbhkdFPt3IvNBlJy4mM1hc4LzBc-64QCDHkxCE_YXBk4QM6u14ESYeRVW2CvNajloIE1ZfInOw5hBUL9Bjmm-vzwvOyqup-uXUGufM5LrObUSHPL7hHB7_1I3L7ChS4Z84JAPiyPdngb2CvCWNEmKspJa7pYXt4Jj1OgZuQXBAIRGQay9TQmPUv_pS35iWmL_JYnnGgOgF4Gxq7IdGVs8e1eSfkaF6usgp0s2fjlz1IcERwpX4lHMZrQOFeJl1-EtEU4yEGkprLfk5LR43ZYdRzlbdXpaMe0JqESr-st034UVXztGZpeLxhsL1HLNavlFAYg2e-j8Kabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
واکنش ابوطالب‌حسینی به حذف از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96785" target="_blank">📅 15:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96784">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJjSg1_nS6SZRWhdhoM2JBDNM6igOqfxBNmwjdw2n6DjDZxhmGVE1vpEQLkGjyQCtlVoYRXT-X3ScSGXfqIjXERgKURPqbUvwkA80krPel1YYI1SIPBkYwnd_wgoOrM6576kC7Y18S8l4Yy-r2FfJ8E4k0n5Pm_bLrmFugUa36DU-6c9r-YNlM1Xeqe1XGYSokEtHlPZMeRx3FCdTClea3yd4DJ3HtRN-Qu0oNfM4Ng_pz9rCLEd4zlUddT-rbqyihZhDDhaIRzIbppghaulJ5_dBUPTAGhO7GdGkdSgXkF_52a2ZvlFDscC_3QVBIyJQ4YMMFN9fzDNoNIYnc_Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بارسلونا فردا پیراهن خانگی خود برای فصل 2026/27 را معرفی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/96784" target="_blank">📅 15:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96783">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW_1oPPaV852tI4h_YbX9O21I8ko5vccS35JhpMFELSvLF80u34g-VWEwf9IpxWRxdDk8_i205C6FAhRGX8UxykUPJ4HVNoM5BKosbBScR4N5ED64V6pWjRu99TJCeVV1Y_-YDk7NKhi2GVhp9Mjeeua7FcdDhTsyBZWDpKpGzXUn_sGLO1SZ6Hh-bkUulM2GsVlpyckbiYd5vumrbRbFiKF1daVZaHcQKv1LDVO3muBt5MYBRVppiqjhb9uEC1N713tXHxjRViiiSCwBUZ-LckrIRFjhjaOQFlLp8duJBW6bX_keFkC-5nka7JYPzdw9wmjno1gZnQfSKujJLdVgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
الگوی فوتبالیت کیه؟
🎙
گاوی:
ایسکو و وراتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96783" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96782">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96782" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96781">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bd9VrJ8lbLsjcHmY-3j4pGc6c6hXcIROGY06BBuu4ZElof8bnUKneQY0DJFRGfxOBUDveWG4URkkHln7GQaKdazltERI1UqQuzekesD3F3o9lbVf5vwqZ_Z9sD3ElDMjJyQkiu_58fblFXoeRWkvxPdXVMNhi-6SdtQaApEDIPC1GZv69ckNBYKMmzsFv31g7Jo_FvvSlNyZVzLZKbbI_4xOEPqTcCLNC6TI41PE5OeosolBDIDzqimTt64f0wCwVvF9L5tXK1obh8teqFlo9Ne-fLr51kB9EqPNcDmMFRdbRrSkfBCMzFXlRcVgaS66KzegvEfQ-v3_2LQSq1L9iIolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bd9VrJ8lbLsjcHmY-3j4pGc6c6hXcIROGY06BBuu4ZElof8bnUKneQY0DJFRGfxOBUDveWG4URkkHln7GQaKdazltERI1UqQuzekesD3F3o9lbVf5vwqZ_Z9sD3ElDMjJyQkiu_58fblFXoeRWkvxPdXVMNhi-6SdtQaApEDIPC1GZv69ckNBYKMmzsFv31g7Jo_FvvSlNyZVzLZKbbI_4xOEPqTcCLNC6TI41PE5OeosolBDIDzqimTt64f0wCwVvF9L5tXK1obh8teqFlo9Ne-fLr51kB9EqPNcDmMFRdbRrSkfBCMzFXlRcVgaS66KzegvEfQ-v3_2LQSq1L9iIolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96781" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96780">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b31d932a.mp4?token=TIcTtnTLjgxi3e9Cb67FFFnb0wNq2Mbg1BAV34tzjWLJT4d39-S5jTRm8Dcta6QtBu1FUSoRJ0jDppc4fOYJ3zTK54ZfbL8cl8MxQlWoc6-BrvvRHFKFu5kDaMsSnFOd4pNwsdIVwSX8_sxM9tp5-LZUzNLaXfwwJy9CzdN1MMp8J6X71a6lUTvhEvMJkhxiC7G6EeWMCzcByZGt_DW5CElCpruQmcXokJtpsNKdsU_JB7rF-sbeUSvQ85qVSJ21ei69pedbgqkN7C_84QOQ7hPIjLd_8Tdevs3b8untm32a-xlWar__Zhp2n_7N6qZ3mN1AWelsLJ8QAHsBh8WU-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b31d932a.mp4?token=TIcTtnTLjgxi3e9Cb67FFFnb0wNq2Mbg1BAV34tzjWLJT4d39-S5jTRm8Dcta6QtBu1FUSoRJ0jDppc4fOYJ3zTK54ZfbL8cl8MxQlWoc6-BrvvRHFKFu5kDaMsSnFOd4pNwsdIVwSX8_sxM9tp5-LZUzNLaXfwwJy9CzdN1MMp8J6X71a6lUTvhEvMJkhxiC7G6EeWMCzcByZGt_DW5CElCpruQmcXokJtpsNKdsU_JB7rF-sbeUSvQ85qVSJ21ei69pedbgqkN7C_84QOQ7hPIjLd_8Tdevs3b8untm32a-xlWar__Zhp2n_7N6qZ3mN1AWelsLJ8QAHsBh8WU-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
مجریان تراز صداوسیما و ورزش ایران که هرچقدر از بی‌عقلی و عقب‌ماندگیشان صحبت شود، کم و کم و کم است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96780" target="_blank">📅 14:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5IDwdmZaUo0rOYd5Fsv9nwRQIi-4p7r22GcYnt5894Cx9_FBwzCMsOigZWEzsC1kzrYBm3hOHJujST0vzC7Eskig7nJJ_WWJq0x64hXhPBAss0yMazmb1tn3xmQ3rYnYk7PtXQgme9I_Op9KWPSGboQ_Qk-VKMLglfeUYJGtXg9zhj_zpeAW3p0fXXC-ZBUK2jjP_ft-ySX_6LQPDxWrABRfemSPwaOZNW6bHw9Xm44ryYMrIOZUwPomNCHOfJHGxUEti03BbqnqQWOyocZvndiEw-OzGbmN-eLCcixjFJ-Q50gQ02Obd_zhG8zKmbQA0FdK5lwXhjm48qOIQn7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇯🇵
هاجیمه موریاسو سرمربی ژاپن:
رویای ما قهرمانی در جام جهانیه و ما اومدیم که دنیا رو شگفت زده کنیم، درسته که برزیل تیم قدرتمندیه اما ما هم تیم کوچکی نیستیم و برای پیروزی به زمین میریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96779" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNAAWZgDT6hhOKVepStkzoTbTEsCvfcYm5x8hJP3xZHJtW7DjU1E0Aw68zEWZRVStiXYYrCexBYaRyJQ6ROCcrkJzloofz2o_HEUOA6F4d5wzU5WkpTN0J23j40IrWvgzmMIaw72DhoFdH0IaTjJByfE2QAKjWpXHauwwnLS1O488pLUfK0UgVWhIeKf-GV8_q4Vy43pE4FyQatlQ3dSjHfDEs6B2DHSRuLbkB_90qDD75q96M9oQyV-PauOQVQUXXEGen1XbolnZXk7UrmpsXM8v2nQ0fcJUghAqQHMKcENfMnNkPVfEIlpQvo1C3cZan87Rsthj7wtTC8errx3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
اسپورت:
بارسلونا قصد جذب هری کین رو داشته ولی طی روزهای گذشته پس از پرس و جو متوجه شده که این بازیکن از موندن تو بایرن راضیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96778" target="_blank">📅 14:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXXeily21xiKi7KrSyu1UdlJktvLFF-HnTc1BA0q_SfO1RKtgIGmotg2TS6r9qOsoLKmMd2kF5C1xkZg9YfmSdgPJN8z3FDm4pwf_tYYd8AAzTteBbQUi-OVrSJl8vhnbHT5-5pHuZFqIlgWt6aAY1pGGXNdYBHbRcSirMSs1OFTHpx9c3L8dmkUjyGsRQUvTZHPf2HkZfEQtbGmySaqbUkvk2LxbogdIOTzOGefefccUrZZkNNoL_w1AXfC_gHTqbQcyQcSXQnDnIZvJKpemnlkR4gRMfiYPRXShQyGe4uJktVrvFf2DkTg5kJHNs6gsfO3dCKaWfbg6GUMB5QHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اسکالونی و فدراسیون فوتبال آرژانتین به توافق شفاهی برای تمدید قرارداد تا سال ۲۰۳۱ رسیدن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96777" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f63773e9.mp4?token=EWEXpYMeOPSnClnDmOnNRfPQvCVGqzkXhBcWLuhfOdxbFXxUyP6N88CD0_m4DYi1lvBGQTkdDIj-LQq0qbWXhhTaULeoEfOwVcM1t0o3cM2pPf7AKYvaOlMbPBtEbTE6J-9_Qv0heuWgd8IxhzFCsYuwHpaVv-1vEyVRhgwalPq1I2_waQDmUAIsMEwT-9wMLRZvwbHg2fklSLI7ya_OB-p1IQEmhPHTmmKRT_639-SkJoZWACg_giGhjeAu582nIeS-io8xHtjhqm461hEEw_8_g0o-Uh6DgueTJqJg3-MX-Dx9bCQB9uemShB-bdvOvjL70qF577XajEiMTGDBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f63773e9.mp4?token=EWEXpYMeOPSnClnDmOnNRfPQvCVGqzkXhBcWLuhfOdxbFXxUyP6N88CD0_m4DYi1lvBGQTkdDIj-LQq0qbWXhhTaULeoEfOwVcM1t0o3cM2pPf7AKYvaOlMbPBtEbTE6J-9_Qv0heuWgd8IxhzFCsYuwHpaVv-1vEyVRhgwalPq1I2_waQDmUAIsMEwT-9wMLRZvwbHg2fklSLI7ya_OB-p1IQEmhPHTmmKRT_639-SkJoZWACg_giGhjeAu582nIeS-io8xHtjhqm461hEEw_8_g0o-Uh6DgueTJqJg3-MX-Dx9bCQB9uemShB-bdvOvjL70qF577XajEiMTGDBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
ایران کی حذف شدیم؟ دیروز یا مدت‌ها قبل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96776" target="_blank">📅 14:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96775">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgsFpqMFV0fIgQGP2G5adCdUJVmJlVTz0dQQMESHVixYxBvMOXN6s0cea8GYnkb2vD0oomFeyXPL66LUnmt4Ci6L1uTziZLmkg32QJzJs-7cAG431XzoKdMQMLyaiAoKG80T7qCOVB5wmw7xGAJ64R-gjTWNdHXH5IXA7zXHY08aH9j0Bl7CW0wJU1aLVqm1OSMUKtKD6CbDOKyqH3Vxjhgs3yXcroqnjyXj599ik-T0meicqpb3vtD-Dg1ptcQRo23b63iOVqGbyKYBZlOFgPGfRh5mWnkY8Z8vnb7UtHVt0oJhXwo6kRdSZfreNDkS96kp3VNYHmsPvQ93e3itQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس جونیور:
من به تلاش خود برای مبارزه با نژادپرستی ادامه خواهم داد، تا نسل آینده مجبور به تحمل آن نباشد. من به دفاع از همه افراد سیاه‌پوستی که صحنه یا صدایی مانند من ندارند، ادامه خواهم داد.
✊🏿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96775" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96774">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🎙
🏆
صحبت‌های تند مرزبان مربی سابق سپاهان خطاب به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96774" target="_blank">📅 14:20 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
