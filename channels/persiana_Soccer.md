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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 228K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=K1gDLrXheoS_G_uRfUSYOMHKLf06S01vugdV-A44C5ya8mMHSqTErqov9yH5bUlznR88ibIryOnJuujK66naHIN0kBIFfF9GKT1LL1-GayUYCd52-6b_QTiLpeYD_iJwVAOneOF4eClqIKzvhzS4qDB9gSz6g4WsS-7TPnqLcdiamlSQ0htyOgcQ5MF85PILVDADckHZteubiqhYBSFLJd7vEtGLlzq-O1MgakArnYDu8kSd5_DxLWGdb_CL7_Ath_YprqsDh4EexF-pufsysO0OQksKQEGmS4raUI1nItu67C8H-HRwGJBG_1GcT7BFBz4-VAM1ao9p6cuh0XV7OIiCPZIYweq9vRgqHEyh1pHnDwXphnSqjN9Wb3mqUU-DsvayY-mrUqWgl64mZ8T3mcTXPZWkJ-O0a0q4XqOHQVD1k3UHOfxDfc61mS3cFUv4ix40oXEnTh4WW_d88s_IPQCvsRGEuaCCnmMs7LHt8qSEcXAlNqnpqQeVb6R56DqfyQjCwjDPtNf_P3sLvVBC5TgLDzM5mdV4SdUGObOtXI94ZzoTdhSmuHZpgAuwWgAP0c2_pueumYf6-G_BD5Eff_1sY8cC92Y7Mu3zFT34uFxn4o-I0zgR-FaRms6955euqmZmBoHFXYPuRQWgG-RGQqkfEQ9D7kB5sq-7plgNpRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=K1gDLrXheoS_G_uRfUSYOMHKLf06S01vugdV-A44C5ya8mMHSqTErqov9yH5bUlznR88ibIryOnJuujK66naHIN0kBIFfF9GKT1LL1-GayUYCd52-6b_QTiLpeYD_iJwVAOneOF4eClqIKzvhzS4qDB9gSz6g4WsS-7TPnqLcdiamlSQ0htyOgcQ5MF85PILVDADckHZteubiqhYBSFLJd7vEtGLlzq-O1MgakArnYDu8kSd5_DxLWGdb_CL7_Ath_YprqsDh4EexF-pufsysO0OQksKQEGmS4raUI1nItu67C8H-HRwGJBG_1GcT7BFBz4-VAM1ao9p6cuh0XV7OIiCPZIYweq9vRgqHEyh1pHnDwXphnSqjN9Wb3mqUU-DsvayY-mrUqWgl64mZ8T3mcTXPZWkJ-O0a0q4XqOHQVD1k3UHOfxDfc61mS3cFUv4ix40oXEnTh4WW_d88s_IPQCvsRGEuaCCnmMs7LHt8qSEcXAlNqnpqQeVb6R56DqfyQjCwjDPtNf_P3sLvVBC5TgLDzM5mdV4SdUGObOtXI94ZzoTdhSmuHZpgAuwWgAP0c2_pueumYf6-G_BD5Eff_1sY8cC92Y7Mu3zFT34uFxn4o-I0zgR-FaRms6955euqmZmBoHFXYPuRQWgG-RGQqkfEQ9D7kB5sq-7plgNpRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=eoCpRhVPSwlXhmv_fklyVOI0nQ8FZ3RTkKzuPz2aGdxiX--jcsv3YDBQ2HXrmBzJs2CwKfrv5aiRRtKPnlIUQ7bPws86K52fSAvVDYWWzyT5vu5ZWztmlE4enDmgfailGGrLvCXo6S_ScleCrN_TLnX3N6bOO7otuKbH665tiwtx8xCubIluIalCa02NArNTEgYFU9PEMmwv3ZEIeM2zwS5fbKP5XPdxNnMOWfSI5e0xuabIvy3HaZDdvDeVEme3fTfDPJnJF1S0ocpssWfzcOqrR_TZWBhg4JKnqr9TpcBU9gDjHgsj5uDZMZLi6DSf-cN5M_yaMGQ8M7nkPQ9fNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=eoCpRhVPSwlXhmv_fklyVOI0nQ8FZ3RTkKzuPz2aGdxiX--jcsv3YDBQ2HXrmBzJs2CwKfrv5aiRRtKPnlIUQ7bPws86K52fSAvVDYWWzyT5vu5ZWztmlE4enDmgfailGGrLvCXo6S_ScleCrN_TLnX3N6bOO7otuKbH665tiwtx8xCubIluIalCa02NArNTEgYFU9PEMmwv3ZEIeM2zwS5fbKP5XPdxNnMOWfSI5e0xuabIvy3HaZDdvDeVEme3fTfDPJnJF1S0ocpssWfzcOqrR_TZWBhg4JKnqr9TpcBU9gDjHgsj5uDZMZLi6DSf-cN5M_yaMGQ8M7nkPQ9fNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RevAyYE8brVi6jnn4LboQ24WGeuo9b0jKXU8auzmoYvRmZGRONDYMAkIwGSMAefOMcZd1Z3XJtDNhvPA-kKF2vsqFkVzYLxV-RSg4DjlTtTJetaGmME-omRyHrZ62mzjQ_kwr3xR1vACTOskSyHsJ2R_Yau-mEeECYV2nyX5QvF5UVOQ8NUbhkbzNl0x15sLpkPYUDc6mdYL5E6ABTnS8mx3AblfNTvZMEsh91pADYHcIJ4ppNUn-_AEWp3KT3Yg7fzXn0LL0csaN3EehW3RS1LDGWpK4yRWU_ynFwb5Q_xvb41tiqWktdyeK4mpmTmwSnz72H71JPARddmKrLK7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=AOe4CBWnsy1sU4GbmiJwuapAw6VnNZ2W3yGffzaBZq4YCyVycqNcMDV7Kk-2w-OgmmcFhohFBKa5HxGgmpN8N_oMGv1hNbQZLoebBuu6RUABDgtjYIEFWNe9aWQ3Haji8A3UPwGT1KytKgPAgvC0b2QqhvXh3-Rk6jYHIPBEX-zJy8rOxLa4vZVKuXhSvQnCiORT2219PL244nEtnEjgDaDV3hU0YsY4u8GWeCQ0CBkGLi5cc2ZbFkQ2qdVWhyUBLQsDLnimbe6hAgP2FSBxJ0WsIeLsZOwEWaJIAV1Os968kn3YnH4tn_287uxO_lfbm2N0PMC9SBC0anaiWY3DKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=AOe4CBWnsy1sU4GbmiJwuapAw6VnNZ2W3yGffzaBZq4YCyVycqNcMDV7Kk-2w-OgmmcFhohFBKa5HxGgmpN8N_oMGv1hNbQZLoebBuu6RUABDgtjYIEFWNe9aWQ3Haji8A3UPwGT1KytKgPAgvC0b2QqhvXh3-Rk6jYHIPBEX-zJy8rOxLa4vZVKuXhSvQnCiORT2219PL244nEtnEjgDaDV3hU0YsY4u8GWeCQ0CBkGLi5cc2ZbFkQ2qdVWhyUBLQsDLnimbe6hAgP2FSBxJ0WsIeLsZOwEWaJIAV1Os968kn3YnH4tn_287uxO_lfbm2N0PMC9SBC0anaiWY3DKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx0kL_ZqQ3DRpL4HmtP2XI3zoX4xFKU5F-zNFzrUvpZFGiLYKRpPUsvsomF2MMxIWeZxC6CfqFxbnXwgk00nf63dQL7kSyBpyETnBcYs7hBh51iM78SW0XoZgCCjq45YMK27hwOvcjvCbr7TAezsgsQd2gpKOOwJNjJZH25PvyCvv2rb7JQ_Vl382jEaFno5Pqqsvtlbb70dFndM--XGHXdOukvxaGlH0FOVy9ca-ugBM6ZhBjNLcmn0Piv9FWSjG6Vbc5zaENv2DGW4jWiDX6kKP1CRwgth20l392wXXzM-Qd2lClPj_893vrspcbZU8JboCuEKdrmmEojfdNjNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUCBUFL_ObnD9yxtGO5MjX36s6W4knMsyW46UMLH7O8x3sUFWonEHWA9RYYRLXPfX86dPVQ7GIT1aCrgVAlRXew5EjwwInJBRqXDXrBGrx5CvipTvQUXC4qPMqB_qn8JoHwigdEy4BRhrbaUvAyemU2XvLJui7uxi5U7c3OGlZXtFZGhfCuo13ZiTfM_HgdOjk9CQi5oQOoiJCoo8wIgJl5D76wbd57vai9fW2zo7LatnZpRGdAiCIFjomWEH338f3rNjNheaA81w4y_SjpHq_jPM0jLL82XhAEQqoSoVDlPUkHXteb71awBNUA8P2PCR4KadM1pl3RDjgucUI6cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnGxng79CYyORT0Fb7Ce_eNDx-8rpOeF-3Yj7wxPvMWRzhN6bw8v6KFveLQ05Uc5XVNNPntwPFUMvx77fXqW131n8FI6U5IAhw1F3hZvGOz1s-zWCXI0FurTPfEldaJy6XV25lC199sHmUrGn7ufVn3Q2I8MpK4otLEvNTZgB5eS-T01UlEoD-bFv-ZF6SUUkgZEeHx-rRt5i5REdeRATTcMMKUYgoMi_deiXmaW0wSsC96zcBi_rT-3D3AAEfuvb_STB211kw5xYfnVtRvZJCEBU0dUgKSAy5bPlN4Iihrpizl25-2TqdKZ-M5AhXVNVK1MHhS8PLpsBorFp_ZFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sppnDpwMWkACN8koQy0YPj2kSUinl6Z4rPaPkHw81Cei2KA_4jvJSFE3P35kPpV2CbDvV-PX9z6SLnbIjL5ZWWIlPZ4ZVeQAnErRcG5Q63e6q7NE-_lyQrqQTHW5igZ4ycSbdF2eAewWWOX5uDgbzlY9Y_K_HUzHr4ZFINq5sB9-5uBFKn8BaoDCCgHQwBvbIolkwMhtfLE0Kbok2IUMdUlCZnB8LTDD28I6VnBgl_UMoAOYkz209TPb0FEVuk9z-faAJj6zNuFcqoqO--XA5AEYQBzaV727L8K5vvXqwjANhvMzUyFigScY2foOGldvZYZd5sANujReyb2EngoWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sppnDpwMWkACN8koQy0YPj2kSUinl6Z4rPaPkHw81Cei2KA_4jvJSFE3P35kPpV2CbDvV-PX9z6SLnbIjL5ZWWIlPZ4ZVeQAnErRcG5Q63e6q7NE-_lyQrqQTHW5igZ4ycSbdF2eAewWWOX5uDgbzlY9Y_K_HUzHr4ZFINq5sB9-5uBFKn8BaoDCCgHQwBvbIolkwMhtfLE0Kbok2IUMdUlCZnB8LTDD28I6VnBgl_UMoAOYkz209TPb0FEVuk9z-faAJj6zNuFcqoqO--XA5AEYQBzaV727L8K5vvXqwjANhvMzUyFigScY2foOGldvZYZd5sANujReyb2EngoWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=iyOwaC07ExokQafg1u0-XG2zb6NBCBgNUdK5HuWM4ZSXTjRBHeLRvGPtZtwenzKz9Edf6PQXMrDM_Q5D8trw2I3AMDMXctHTGtsudrZBlKSCkswYxPUhB8zEdkDNnjL7Zm2HALvGfQJttQ41T1UhcTIG7zuyhTO4aTMS9k58IrY6ooFmoHC8MroCjSAxfDA-NIJm5-rxGPEEVW58x5MQ2yGphr6DzFqf1JcW_vHfbgaBBUAHsmlo2EMCNTz7DcgxWEczh_kPTbP4J6Mv1Zy75SEyudQLmUzTjcYEdPy8OJD3Um3hUCZigbbCZ9I85hed5gBPKiX2gu2drmju9IwMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=iyOwaC07ExokQafg1u0-XG2zb6NBCBgNUdK5HuWM4ZSXTjRBHeLRvGPtZtwenzKz9Edf6PQXMrDM_Q5D8trw2I3AMDMXctHTGtsudrZBlKSCkswYxPUhB8zEdkDNnjL7Zm2HALvGfQJttQ41T1UhcTIG7zuyhTO4aTMS9k58IrY6ooFmoHC8MroCjSAxfDA-NIJm5-rxGPEEVW58x5MQ2yGphr6DzFqf1JcW_vHfbgaBBUAHsmlo2EMCNTz7DcgxWEczh_kPTbP4J6Mv1Zy75SEyudQLmUzTjcYEdPy8OJD3Um3hUCZigbbCZ9I85hed5gBPKiX2gu2drmju9IwMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx7HzOBHzGtYfv4Nqf5LuaZmC8xOwl9NyXZV9xRPGLG2mcNVKC2hsvd6Wm4GxEfVuSma2sKuWHlAEO8X__UR_6MSnNuahmI_REDpEH1JrZRDvXenyT2TnWmWcfWRWrwtUcUJYSQvarR9LhPzqdFKfyF4ldA_gvplvl9c0D5jtfnMxGrfMNDR5xuwFGy85OIuH7SONnCQ3s6pfF12gXid9hqbPvduPZkc91UF4RRhQra571sCqcJXbC3S4xPP-nEzqmDG6RhyvZkAUR0O_Q6Fjk4x5W_Nxv_sqNwoQuCw1xKq6Nn36VSN3D8xs8l_XOkXAYXs9nPwcdqYdoqg47Vmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_1utVaiSF0G8wnc0I0s-6jFu8QJqlNu7neUWlbzKDYl87RgaNm3u-A3eWHN57ywye9nsLKCwydQAW8MuysF8Vn0qhB2AouCp0-huPriUOcHOlxDFUx56gzSk5jNzVA7zCCjL4vqQxNnvXg908l-dSTAzxRcSrWsezmK0k1wzZlEhnFZrPunAQgY5CQIiAJ-4W7szqjb-xLYA_Io1NvEPwMk4AiFQY9YJvPfM8vA-5Aou0HYgoyMoq2HOc7PmDe4RDG5y6_WGzWIne0ELjxfFvRvUBP490q4MSqq1ygf7woJjv2_ueYjclzwC2-5RVuU3x63x-BfDGB7JLXUKZhoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdDPMKRcCDz8t2TMnRSk_KcUFwRquvgDkafU1s6kU1gaugORxI_VrlPp03d0Tfvj_vMcGIKg9ww9_vT8e_4ex2m8ujKR2FcW71B8FS5tKNYc5YGaMFLoHFbW9Y20xuWaUzz2_8ho1aM7tgvGEinDltZGxpT66eI45VZ1CjTDLde4nnoDhnfopRH9qb-fnB0yDzMd66Hdr6tIlbrRmWjiDAbB_s0pSzGavmBU4b-odDSg7HRy-W6fpY34uyXsj-IlaKBsTO6jwMYZPpqVt1jS6M7TfTBwhwir1t-TZvNTof6UXKFTm266jLwCc3vS9YJ6LDF06abPHOzoe1xVfqyaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsJH6uccPco1pRk47QThOFYJg9arHIG7KMV42XCDKvjkX03qd2EHm5QqpSyYVnQ8OneSRhv_LZoKzrwJBYjii1CwSMnsIvGBUnWwntN_FWuIyGKewqNzuTl1Po1hoi0M6owRBzns7lcxv7UfQ73kJBldDUoJZSCF9whuqVMfi-cyIFNElRw0D-_BICD_hl2j8trLuzBrb3wdKHG459K-VLb7nLFFIVSgY3Ph_n1zsVgTdCgyeCMoQN8Xk_Qu1Q92pJNMnpy_6GEttvUxxrfXdks8ctWp62bScJ2tq6ZabzYIOjp6fl7lG7ape13uVnyaAOw8BEULfFD_ytHKx-E9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23226" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOiEeDyfnZdHUdlEoNDvYqAuOzjgHpY6BXvv823lGuonIH84T6t9Tg9KPkbrTLvAc8mIvMtKxYVL0tZ7TdnWoHMSbshEfAfTD8tApwrVib-bpJ0uSfZ7qO2TONhsC5C7a9k9WXzqlFYSouBaZzrYxEsvl5lHnR1T3gtoSpMj0GaU6X0fSGiLrrUgnOjy91g_Rlp8AagXcngGustPcJRLC8h5jG5pYiX_pJhrbQmT3igyCyvF5pgIqaVL5DPtwJSDhENmdVJyGGeiv6SOqG_rdEKouZLdyr5uEpLN2xglfwsP0ZE2xW4Mm76qvZJdPmZdi0qNJcVdAMtD4CcR1lstEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwT_cVvPmUoaEBKfmMDE4NYUNgC8Zu_EgLCHP_h8hyzaUEV_srLwaHwU7415kihpqTfTZHENq35iroE0ccZjhbaN3t1bF8oBIIZZvnewa5mHKV3IP0M7a--cw4NX4dwCc8_aAQR7hRMKgZpETGOyUvUepszIH-Ta5_PWeRwSCGJ-2RE5GHoT9p6Jc1F161bG-kCe0vL6EIGBKdXkn_ljuk_jDHpN5U9jFm-O7bKcJMMtYDIF8MF2bAu7bmElOlQr7XzsPx66n9e0cD649YZW0ySa6UWJ00uLpr5w_PvWMlffjVWJIEY2eNN1TSuhBa84_DLRdwLNAZw6rtBjYx-2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9AXIHalUyQwXdGw14RhtYvDDFAxrKsGruJDiORgz46UUcbWGLFCsKBxpAA_k4m78VUeL2Bz6nOHij8KWz2hi1SNKO8Gzgi0qrYVYYooFpJqzv4gJRBA-bS7fcL7EabOh_GBmdWzhzb2bUB337dz1J3P8g3S0Z_cqQKUwN7v5sXA_ByEk41GgdaJ5-hnLn_wjo1fZT2Agy4i3McP3CAZW3IJo1Vs9ZCCSWnvautD_8XB7BMTtFN_99LYOEiEAWp1J06qsRbOd1654QG8UalOz6nTqQlfzweeOnCM55U_Z_VTjXyfagP2fB-NbzQRqywBXTf9-qWC4pNkoXfnI8hHKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_ajVbf1_Ngn_CjWf1ePAHIKivBzSq2vWcEauuGbOtSm4T-zlPcSvIwQpEacFsFGJ0XrV0e4QXRpGVb5QBC1p31x0rD0eaPZDMMoLxs9OP5iqW6yVEyUrGWxzCJ2AVwhLClAN6evgVz1WW-w-qYgdDWqzcOyDQemTsCNHUXcpGUw-zgaY7BUPwuGeFfVtxQjUNaIInKvgLs12UDERkFkAEG5UITwPyqM9ncedyfZhqXfC-kPqzmYx5Df6kCFfdOZqpL6IbyxyNk1ZhUUcdd_QH4RuKrhzvzKwBN0op_FbI9BPlV6t9aztR1f4lykjRDOLhxlttPfaakYfTtwN3X6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDm-Wz5Nr7wjlrztBQSxE86D2hfifyvwrTak0Uql2Bh160GeXGG9i1UetRxu2H_vVyG7V6d7IvU6jNZ-lKc1Sv4YGc9RtoCyA7-78uXx4FDuPSnba_NzNiGfdYhV-1m_BVUZRoBpthB9bt7L-_FfY3evteE4WW8cB9lbVmbihuM33G4KOWEeJPETociUBIS5Q4lJB6lLcqxww7PSBUM8keJenB4KVqzPDM4EGcMj3BZF2ujyIeQJN1O88qg2i6iXl3tki3cx9a-EpwsjYVZac-xtNPg3EEj6d3rOO1PR6WBK4aRJ0WFD5uTu6OPSPj0lUHE6cdPi5lsKoMdscZ8zdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw4MjlnmPVC3UrCKAqJOPfUzEJGsWdHq3vlK7AoMp_uZRR1fzfx-r0zoqgJC2bkS2MgGGU7g0jBSTRGg2vnUUu7rPRvCq1037h-ACp7JlLxn7LoUS44jewN9BHAy4KWpEhFd6AWxlZyKqNDpWtuS-ukbh5-IAYz_NWIFCEKMUYEuDsJLVCuslZK73u7fsQkhY-5gI-gGHasNFKfgV3p8V4ZURyR5s_1FAvIVz8MQx9RzcWmOn795wm4G6ns_tWaOsW_dpHJp-pZKT6Bw-19cM1MOvb0di4_WXJyuY_QtHeuJHDMbCQH8nGf9Mlp24w9cRY1P4uQj0DppSFxgOrxdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehNjU7-X1CmQAQr6scOwQzMvFVOMoQHs7-nRgrKbD6pgj5dVODS5xUybiR9vCdN6GvOs3Ooj4pvmM91GqbpFs2mq6nxgmhkIloqt1I57qGdBs5M6rTaTYyj8Z7KJ7332fKzvJ1LNdDqtRel9fNvlTsJnHhYrWVw8Y0FZDpfTvfY1-EJcXZgd2XC5ZiIUswZs1_GahOLb6_PXmDWse7gZahLQ1Qq1CXSIhuVi7OL96OGZL9E1sRZeoJFVnsMItdeglceQlt-qKbz5Q8AE57v2YRmuCWppMUNyr93HAywIFAgSez-PQGxvoXxqR0cEh8FcUnah_n1qaAoKr5J3PTujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODZzKTfxpNjhJ9K8tkkLlHjtEBrjXkfecETwRN3MJux3OAIUFZYOTuqeqQtGELlASZY2cMYdzdSGFlNlx8WnVvzGxtMSH9KssGOWU5Onf_BOTeRtY8X9TvcNMIyELskJi1XbKhjgxBH-71f9HTzQQVex8sDnM2-8gspEGmBD67BbPVSBLx_qAXnrmNr0qtVMdO8DZ-sAELoKAthvkNopM0w3n2iSQL5iFo7sFhj6szjAQ-c1sRxV4vYTaLcynmzbgBd3DLq9_hG8sQaL7WvYpIcJCTxxV0PUq8x_658kbImLxrtZpOzniRk9xHYo4PIc5j28wzwseXr1C6EEkS0oqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFWYSzd8c3LCDiVLc8Gnofil7g8vaMwJEceKguBPlN4sF78WuSVeug8yMFsNFQrTlCOBMubJlFEDwvI58Rzkbu2Sv8_PfaBNk-b_0xK2mP3CTDAm2mJeVHG364RZNhugk0UgHI-pTGkvNoYrB9bJak8SBRW1hsHc9h6NIMWkCoAtMBkOevzez4LbawHv5n_hL96Rutv5nkJDUCIF7V8JWGpvyd8TL6JbVEKGZGeTxG0fLM_rm4EfcW8qMBs7Ra_O34zOjL0REwH3Q-EhrZZlfzrC8XFBajXbFpLxAryWKNkEruO4eV9i7iUBtQdFWLuEahWQRTQSgO-MDHfXW7Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L42VW5EeJ5_hdZ7Y6KAhT2cJc01aMKwjn2A_5_jRIbcnaNuDSpzoFcUnDprOoNzLDqkDFmxtSm2fJvLn5_llfM2lg5tb2xU6NKhM9hJAaqNZPoDRgCoYlEx_zEqD-cpj_nI_0sN-3oGcxt-n07tiQ915EGIy-68tliTeP2DxAN8znrwVgL-iEfGFZ9eBGfYU33fv-S3Fa6KOuxnAnUlCnPAK0HfbjA8ErGpCft9Ce-axSSSoAhcq94KvOGpbf91eBsp5CPPib_4hve8YOzrTA_R5-TIp8bn0fjZdfJXCfYbtd_UEXTjV3nWXSQ7xhA6fCIEIM3UgGhtjNX0d-GDFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTusUy8DzuqVvANVkzZ71uEUjBigTeZTiIio1CoNDW8cRt3OqWFM1b7Dj10xSZS94oRXS4t7_6ylDojoX7ce7NhIsz4r3uKVvD0EWKouO_kx_r9RLw-vv18OiPQzKKGd07xTWMeKwZpWWG5Rgcx65lXJ750iju6ptGJPKuDBiXwspypY2HWkW7oQaitdAFVVzoHFfGNCdrwanDk7jbVyj80-fVrHjM5n3a6woLcZ1kU9sd4hmDvMyTRzIsFiVFlMwwMaoKSYRGzqLJj9ZNozNlzjV9rYZ6D0XUxRSXk9TRtYzgtmoFpH3lh9UHyOUAJfiDDBRBZyT451JaL_97eujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Vq_XEWrvs8Piu-YGfeuH5wUXW7qau_aTs4LkIModGPzxw7ECvWuO78STMBjkYLhT3EFD5KQUZxyHPScVTrGhgaxsFsqVhZnqNmHUdBtk_6xqkqDBAIlUkXQDprGShl4bB6ATgWySLv3SOvXTQ64Jfv8ejMggcIbm7gjbnprKF-_LSCxzjB6jux7YOm4RUNcc_aD15psXReC0-jbPDX9OknmHeNqjzYhy8vVhXjcpFef5z8TTDFfKg09c3G-yJ_4E6ER2JJx9gQlzE73--MCOltbCiJAzVkdlkkeLnAztw7tebb_e0I__miWO-f8G-GEb9szHznOy_lCfYZ1J_mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQYH367n-FB8ZB-FSOPex96yrjlX__EdwesqOptg1QWNGOwxHT5EHnbPxnBqfh7nULOYri5yr_Ur6qm3nzkMDktDSTA72iTi41opyrMtYJDITTsZosRQ9m7AbNyFjzzq_w4tx5zyZeM6WrEDu3exO7GzRIvANWbyzxTuSVWULTHlovm3YDYudewxSKOPhWpKuIPDCPl4UPoi6737_RV8-hbptNWBKNoNb_5VDTu9T4i_JNNX-9wWpWPzLQG1G79GsxYE2x9KO1ApdCwKzjQ0M4dEy7Rlc4LsJVWvmQyVYUt-PnRPV7Luezi5dtolbQ6fEySKsQrLvm9HSSiZGBgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6jyR4eIuWmpmTVUjytqF5IFeJykCmPo8WHgyERfKGHFETjIsaq4hXr3q-6g-xlH0mSV6XQsJaDX9OroCF0CijvOGljNXQUI6v-dTMYTctvzrxVWtMrpmnL7W2DmKTMm-h3wwF-pa7gjLac6BsrgOXO8xtexHQhSMmBKgGTdkgV2G68zEr4dNSBUY-c5H7c6ZehD8rHHDCDLtn6N0GExcd02_VtZnSEo5SBkpVwpHs709w8ifaoQhSB5Okeg4rZkUUYRVzo2qNd_GCEc22OyW_XmA2hVS_4Y6ol9ol0NWjBwoQWlE8hC5FXL5uHudVLgtvG2FrGSpL_mbEmabcocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBC9wMqR5ic2Lzvz0mATe1ELFe6XZMhCWYbPJJae-dP3Nyar5vpSgbdVX_j0k61LUN8CuWNSe4JIbyTC7PxuHpSDCatxKdBSH3WvDODC4gcy3FYMvYwswrHHKLHuA6CyAFkCmfpmy62Xs-dksbTtvZskailrcsZPWIMl-GgAme3M79Iw7y7tkE-sUFCJ6fAPg3XedYilZ2m-v8OKwMykCmyd3edwYAWqYzELLU7G3mwwnyPN11NQ9r3eerTrAFcVpPYmiknnve5moNPWZuY99r73KzgBqZLZskqPXfhgWNMFoCsbDBOKYDa32SvYy_Gn8LZD_1Hou_w-7kMXPb3aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQ5kYzkhcAjsb5wo43q0BhglCVQI5rLfkmDOyK5eDUiFWRZzJJqnkCBdVHgeHg-F2im6SbHNG5GaExPxyQth48yua-fxq7Mp_NB_mYNlReB6LM6ZeV9rhlH_Eqd-6HKBUKNGpoMHzkV_rIwk9wi1fP6_mNYZW9uZHBgM2c9trHjBhpjhomL36FaS_lW2gyscJnFfyYn_WYLbkPljB6EJHXWsOmOYPD5W0LIZLmB03vF5hZLu_k09fhtxH5ZGPdB8dgdGFuWXHk8VfJV0OI67sr1ht1n_5kvPtc5UAOEA6DO2TuFNTP_NRY3mbZCQpdMxgYz01x_VCLz3kiJGWomFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWZuN9Ev_SASnpfPkYoJ0N3IkP9mmSUmVqzV_CqbbNqdapgDfxPKHEElPHN3tyH235enG-hLQ6yyQJizNi69sXRpQ6jOUoor1lVw4cvLo2cwn8J1CgmjUTTvneHStf7J8fGP-HhBwmAKvhsbCQ260hwebWcZPYqpN0oWyxIxvfZxJCsvO8t7f0eEkvzVDPCq7HyP4FhVkrlc28o7QxmYrQz1Uc7fR_B7CGZgKOlo527LUg1efvJNlv48uhvJci_ty2yZ0rV9EzpSFXSuBph8sf-rGi2CYZK__sWp07O1psTSc0XWsPLQur3K05TD7DpNrtWIE71Jc_cmKgZOfdAdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8BFp6AOtqg05-uYrj_O3FpV2HrlWXPWNsNOHukSelMMDO6MnCMS4q3YpLZDhLfPlY08tNsB2MX6_oraooeGizwhS_UwOSNCpHk7sccNVvBpICckhwUSot3kNeTSetfPRqtPZ5UTRpoQ0JXbN2uv8D2RWDGCOyxgnnVLM3CthaSM3qPxcSLmU69C96_bNUHs7LoypH2bEQZUp73T6BzPaA94tMwSHCliN7C397en0U8NGcfpxKkRnmhRD-Te9vBGq1TP1gQMcoQWf5m6Alyl9jAzbBauJ0bRZAk6KRWEWqsYLZqVF23pvrwVRha5u2PwIEvX5GVw-RuBwTwa9xCAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2P3XPQejSKOPhba5gRnvnAHQUKaFCAwJJxN8jAThzsz1U8SHu_5BJgbWNeFvGHv1Ou1mgOBbz6_EiKdxuPX1QQkpB8bG9uUcPKzaM8N8KnlLZ_bkqyOS2LNA-yV3bAZZSGsuweuTiNBNvCkT6JSp9RYJGSvcW7BYvUVaviWwn-O_VCjAuSbfz6H1FwXbbBzNGdir9Tu16Kx5P5j3qVL1XfEZHSBKIM_b2pCNXf-Q2jB43BGnqMCi2OjBBwJ4GqQh01bZyGfpPubZ18pOf0lR9rsW7vhUZkQHPxadQ0dFlqzsfEHv-zXBF1Gg-OYAbG1cOJPH_3ASzsh3wgbFqxpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaZyNY7WEQzkBwrMi1fHDAYd9adFiM9Tk9mS2SLpzo3mmJyIYc_NXE8eUXUcFZbL9Q66Oq8TSvcIh0By65ugdSAjt569fDRxOolJZUUoJEni5w-JlM7c3UtxP832Hs8PIVV3Djhu8q1lvvZ7g9yYeHjhaI7yrB6X_UYXyabUoONsSCozD-hhcpv9_iE03a6yhkBv2KYpsxZSqBGN0oRL6r_7Y5bUlSCsPP-ScOfkX_ckeYSfBufB15Mk7BSPeZwuj0wrc740BWXGwwffddRfHHWe9WD6lRGqETNuldoX_hGcsjpN_tivu5iCg72fZgn4Ixphe1VKMKqRW01k8_pIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flpcspEXHEd6n0rPcI4RwCVV-kwsH8A7nZrEDsPrYywvJ5wAAU9SMU6mI6XgYw7KVTQGlPzLOusOB923_LYrLqDBqHiEhAH7uTSl2Vwmat0I4cAxQUGw4r5ryFTB6ZggT1jSS5E6fkORbZ1GY2qHpbeiJWpSh8pr9zSN3kOopyGOiCOnFok1AmcXj1iGGkabQIBNj_pV94m181NSWmAM1ovhTJKIb33cRNKQ5ECp5Xw7Twwqv9tpOEU6m_1ocNni08WU3WROLDl1SY_pD9d6GNQ-bfvC1027LkdF5mldIOy3MCBRAEhRfc815YvsaXOQO2jk0NMb49dnajIjndUAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSwFppBjponuuwkzzXJ_7-rF1X6dYJmkLeQqXIPuKllacymlTOOFv_sUlxLVsAYui5cJ5AVZQMk0xsum7dIDsItWQNuFNqKa2ua45mduR0cl6WnNr8uvDUBTyzMExodgF5hqdMYCbusl2LXeMKqOv09Sz8jUfwRv7y-e8-pau3PV_LIq4ZcqBxGBMjDJ4b79dWvJSwtUc7_vm8n7hVnlGwcYp7MAfAAEWmVpBSKNzWPoJ-cCNgqWCJYQT9rJX7MfMJHR83aOCWS5-ijmoEO87dOIdem6VccL5nhS-k9qrmvEwCG4b0Luyy5WI45nHOtFAilKel9a6rJe7wxOvAK-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDO4YTQ3xrFLqNnGxMe6VhjjbTnlubj1SeccuXWaoGHgKNhEW33LRlPl7XhsZrodQ6WgXYZ4gIrZHuUAP4JMj07adAfMoQBYYgAb7XurHcVUBlShm9hEqOkt4WIpBiZ2OAG3OOrpBdAWy6Yntv3Mx6ypYhT5JAM7dIO_cquA4lWiAYD6GrRjda-323jttnOhMyaQTvmh9SESmLI_y0HgMIe2yCnXkfSorw0VUREdi3Il5VJhmu3misL3E65GRyi81kb3gx8kRAoARzHGgyFBJOABy9acio1r9fNWImvdwbFgRB49mSGKTt9SfuCYV8DAGiaEElyrW7GPDJ68R0uFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsiJ9xRdnn9GtpW_au47JJvEE_qee5ZDgbdJn8FJyVlrd7JhRI0H_xLmb4zaVRzTRiQvrgex9sli_EFBOV1e43rXIEbLPkPhFMhvyCcnMjva_GON074Rct26yGDz3nF1aFychcYEZ-tdiaBwgWds6w3xdqoYP_EQUG3Q_21UGyKd0AhoI1bIMGfQu1PdUUrwqcEVqmKzmSVot2pHjdjNcnmikiYAhjG6TJQvle8JMbILwy8QVK30PAP7DfOSJcF9KYnCGdCWa5mBf1_HM4k5gmRJynjTtl-P3jAkEg3FsWckfZF5MsxjUIgqDf6BXmqYYUteeL6ryvsSgturzA3v6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGuBDWsI4JklrlX63fZ9-spj0v9b4uUCDYM_MHy4T2qZu24ypL2Hatktbd88dcqFR-yvdVKm8cfsiWWqAhOvpfXHs5YtWsRFCFomTJePsRWHENBg6G0-jF_meuSLBYBems9GFVBucZe5hNo5EoL1UpN9qORo6m2b9C8XW5gvRDT0ybVMZ_dpJyCgSZvne3n1fhTKeCUG7V20bzPYK6MNLvr3308Dm005sl8BLxz2yEA9xmQm1b8MjKjqCAQ9DSPGugcDt8ex5n0raFdAaB7Q4oRcnCQgzeZ1VjQRLmYuxqjPZxpDNg1XGibTvK59XRkSccs-L8-4pCRnkKm6xcfyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTySVwZfIey8ZUE2OBeeEYPqkoN6deazvKEYUw7KtOtSwzzi4H4exUhFzcQlCQHRLj3Od96XvQwksiemzQ8DcE9E5i1TR1KIaL67vJRdKOSP3--1onEATf6ah70zaIJAjgX7Mg3EU3TvXkPhy5hElVLkoyp40gY6RKynbXxAr6fXZ_wj2j1ISTGE8nn8WbDbyD0NLTY9j0q34a4oHhSkaVvsGvOmAWMr6d422hXXnSx1o8mpu33leglElilDL98N1tQp3nw87gA9WldChfIemRcfCvue2107DtrenWABCNFzkgJ9cxsZxLTSPuanRISU9WuLj8q6G9eYxAye4TW09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NVH3KzutjmraGx8e9BsOPH-c86hnjxNCfXBYN7GFOMJZnsOy8Xzphmjq0IDDWiK8_gVJavxt4eWrFZh9LfX8Tr4XGxJxRBtA4f3a6PPIenMe-XpFvszEJ8MQDMT5UHh3Q9kS4WwuUQ3zxMhaoo5qoDbfVFAQFY6uFIjM0OA8ztqHSTTv_qNPlMOTw0C5N-0dbmM6ZBIOQ-u3euDOJj4wQPmhURLi5h1sjhpWIwH_q3mTcAFl750uBHlKyoszrtRyxWKB129UYI8jwKJ1t7TTnN8LaariGwKAF063bidRSlgoXg-MSq9P4vHnIUfeFoKhbdULALXrm4s7rYe62LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_3M2vUg0hvtybZ3WEumhcJCWOem_haVxPOFthAhvxS2lwJj6tt5M5WdcpUlfpD7GSJloTvo1bc259fyhWefFcgHS2HE3woipHFMdOqKE_xeD2l8JdQ0Oq7bFEEWwDtDWI7QeSeFm7zA36faS2JLmXzu4QuOy0ipO2lXWsmdAIJsmhSmOPFje6ofo9SZP-ZWhDHu3Ue1J4LUUhcGskq2ZRu0tkDQOaKfJ8Pw9finQHsDKx2P1JNi-BGfSGk3gGRGkx1F-9zWOLRxwmaV6YTkJGBoQ_-Mw0-3I3HywtsazZ8Jwx5OgQZARURwcJeHRdwRVaZBcJV3rzL47Kq6yIGIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0fHxocDBSCnLpUQRRCB5vDs4bJn5bAMyeJ1jMKg-d8Q2PoYPOeGYKUT4P0e511ubsL61AMLFe2dwXZOtcrn4gvAp9PosKTuKTl9NsanxHZQZQy3BpkzHXt3FpVW1hT2UusLjR_mKwaZSc4b2Kjee3vaaPMh1v40XJlghpymfH00CZ6mUge6R5Rgl5737gkkqr7sBNq6jjGWA1q95dcm4MANp8Uiu_aRMuXR18jHfKBBTYhLj8CyA1ZeX39I4HaRtWnJZ_mWIrQXvrGHC7v7zIH2tA_UE5zKxtqC1VLBjaVf73mXl44nUACvrmnC4L2r8SFwz3voejkpf_uIDcsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyZt8ReuktX6a6bcwS0Jl4LARjtb1NHweMx9aCqDccHiInlnqYsmC2JK7GltSHQcxm66xQAJ5JjFd0hX2SyhWsJWnDrgJFMWei9i93LbAe6LJDjpa0r1Lhquayv47BpJi5BlBc85YmK1XgIt7eEZFzqZiTSJyt2YgUgQPejv4uzMU-a9k6YrXqcjZPFD3KPtylA7SA7Gt4P1wpfe18BtNqwRU1PnkO8qGwiS11MbmC9OAo7zXG4_iv6mgP1kMJ8lMpVaERMH1nskAHcnRoZ0Z98iW61YQlJcjg5PEL_UjGcgH8nP8dR7C4NGruLkCtT1DWaLefVy_s3Q-xibSsGcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4o0UwptNahOBlCDLu9EFQyd4OSEMcWx7QS1dCo7H5elusQUeKlMwkhJwjK-oOAjHEj4Yzz1MZTD38iKF0W14-0lV7tcw8dXPPf29fAms52gte6geD4uU7wBa5IRP0S1cMjL4ynju4J8RLT_fnxI8FgVhUK_4RqbN1gboBWz_4cxyqeqncxo5gaeigl-LEM2uTWaNR23bOFzvqQjjeI9wVJDIsppBH2vpGawrr6pxrY06FvLDObYKfaSCfvpcFakwaTc2EOXqA3CTRHbUZ_em4CJNM02-lIDROjvd4b42esXq4zIIw-b88aRbCTW8FHWLCjQUYaA0MRFNKdM3edUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9Hrk9nG5fa9gKFXX2_a70lFysfaOuNvaRW4o2LcTIHot5oh6YqwzytWAP8TxLvWOvCt61lVjS6lcWF6pSAH8XFSA4bz5L-zbsu2uYB3pcd6of1K53f4sXtCZFNElfWVjvk3cRTO14wcLxHFVy8O2Zjrt0pSv0WHtbTElZCTvchINHLIDsX5-_1O2d-1P61wQTUU5m_Aa1o8FjhfInkEgXskYpPlbwa8vLhKIY2tj5U27XRSWrMXcU1o4mgxOJVQpGMjPdd4vVbs7bltQ2BrisZSVkFlJioUSxYc4FuEGqK6jqvh_iYCf3wzPCRPRxdaT5c3fH70lL6r3JX5EzMTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs2x9_rq81HYLTc3dmG05ec880sHJhbp9tlNo_vMEYhq59OGkyLRKZD2is1zXnU08Sya94AsQYhjIH4-wZeCrVlQnl21TaFYXerlDwZmx0JNBp_oR56LccgkDKV9oOf5tjaRlAnm9z86Xsob016K64bO1wssYeYfk2u-UHqEcpgMw-AbeXGIOdhtt2x6Una6-PLee7apJaexapoUFPGDsxZmlbi7I8mkbZGLBlr8gMFSD7_q7tvor4zJBWndRTFFc9ysru_PzBfBAW0QykPRGqLO0e-6MqGK0vgcT1rF2X5U3GsUZ-AoBmlozJF87jpy6k9OKQ4D5ve_6e-hzYByng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWX8dBCyB-o8l61SRRy6zTrl9aCWWdair4c4dE9vslIZOW2jPbweBdo1ZGW4iB9iacoIcongjJ76X6vDFZmg98kEem_c0wM_DUl_CMQyOf_SsDLIbkQRwuKAObkUwz06ne_KJa9P24dUPPvYJTsjCOR81oIn4VGWWWwtVq5BaqR7JLSW6IryVigybddge0Fjd3xat4cBFQ2oPFt1K42T2WPgKcV7gtG4do7Krw6gE6zAD1m5FrpHRx_5S0Xd-5GJM4iwzeWHcrC_NNxLo6nw1DK1gVnM1RUEqKyzpoFHHSgzPzBNU5oSYBTcbe5Gl-lLM2C41924gdbhvSqGqlGcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4PTcxzqtKBEFSjfpweXXEk9nQ1Wlj_tT9DBgmzHs9vccCqPU3Ztlgj3Fdiwv7QlLIpA9YgXLNFpq63b3hKCYIkPNVbNXkTszDyBKVa-H0UE9sehXDQW0hZSrlYahARgwPGz_Yizwm8ydw6u4LdP_SEwhopPNIyZiNr3vYnR4LCi9gP_Vg7AzVZbp0Q6ltAQ1KLGj81ROHw1FJbn6yb4GObL10WLKLnQD_kNJUjOLTnItmNmErGyvWCP7mB-cgU1eSlLmQdxk58lGo87Hzgh7MxkgJvHowOdQarLYI2QwsX-435WQUi2R5Q60zbv5abzKLE0peoUMLua0Cs-7c1R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcQke7jTHwkRkNrkuefXrQsX5twN2zEld2vUHWMKz86pEXd50ZBCQMKKAU0GWATexojGCTWa7wCHr2U_QSguImSUpNvT9hRTUWTl5cnVh2MKkwJj2MN5sBZdkyJLpCrujQ9GnV9jfrL1MHjUqHQ-OB5OfxpwKifsJgGawDy8eShiGySJmX70DnLSFOj_ipWG0yxVm4VP_Ax8pOnXt_OTCDh_MR8NjAFpMTb33oCeoWQhk44oW7mo39WF1dR2xU51Z0w6CvEqTYPb6ZVMOICL53WOeiX5rWgwerIuVYaKbtf8JBwZ6-6xFbQ5jIY9ZF7vz7_-Ew817ZmMisGD9m_uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T893ID1fPActj8WnOa1wxe6qN0nvKwHNpzUznIpflx4X6SOyXF3CHKoHcnKlPDKQo133mTHYxPpzg7_r_3k6n5mAMpOnV9ox7CRY_oMN9hhctu7p1eLr-FZnTw4onMpHQnKYgnJKkUvB_KheZDag2ZXp1M1fEfM2GROwQ2iuOTy7v7dDbvHk03ySh0PTA7tEB9qiMga8taTwAppSRO3OY7C2cNATR9eSOTcHJDkNqV-S_E4X-xUtNThpquGrnbet2aGk0zU8f12A7DyS5O5oTLQCE_bpnFiEw-4WfCgY0ghiUHhWE2hYLwN9nOG7bmG-lB7Dh8LxjbUr-BVwFkFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxNC_mVi120DXUco6stTejWbRPI5Krq6_mc5idUxOmpiJCWBwqbu7djwqpZlZJgabtA_PqxDmL8BNjurDIMVFXRHcVU6jMNG5Na6pb-rNCR59AIgsAVLXF7EloFX9_RyHRjCCpB-G7aU_7zoWmRRLWDcPjytioEhLeRc4eTqK_EiQ-eJjxyoZ8Tg2wF5hhpPdjQEZclG-rbsQTsHA6UMQYDR0JfAwACLz0lzeLhmjQEkfFACsLY4dpLQIJaK8iNTcqv8OOGl38AO_2snSqnVDdjDdVcrOzVqRHJ-5TOXSmHK9d9HQ5SJXBwWYtMxdhtgmEnuX9ZyO9Dhffm01eOSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhVWdLZw5XWbRq9qQHbs_OPcd-zmMUekpqOQoFjCObq-Vh93Ivjkk-LcjLcXGJgY_7UnNZnXImZ70mvKdeZJS4c7J3cwBFQjNRtvFuZwNeGZeYYMEi1QReU-lJn6OmKZXjV6ZkmdGkdhojp9VRtcRI4UrBF2EGq1DS1NddK7IewsFnwSOqpuhm35rcMmee6a5In4U1bQUPdf5hUAQtcWcEJspsxsYozS7tO4Zxg4CseMogPJ0_knZ5QJmyQcqtfp1OS1ipaNvkR4xrV97ATnaDX0yOhyFHwP-6YOdNFTK3-Y_6N7Xb4GSc5n57hRoKE0IgFb23EI0aIX_eFPyPJ6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=HdITn0a2vDhq4sM-p_HaZG_wCLasso09gpb02wGisTtE9EPuSZImT4WfWjPr7EKF22Tga7C83T4Gh-lr4-gRPFmh0rHalXgiwee3GSM8wdYFWNWp2wYUpBJ9Iks-xkFsHduQ2znZNzY2uosMV9EoW5BrNfBJHX7I8t-XhtlAm7BPBFWCZkZAYdfGcU8MzHo9HgJpsmg7ukv2os0d7Bksr-D-gCbDZOGhbxPfi2319B8VZd9zhd8gTv0LJsS0PucHF1NnEF_DnBOyOMeNAQbZ5k_egyUq11Qb34lmIv8MZ4kiyxk6cSefEsRAmZdT5Dg3Wrhvn2wOjBlt9xSJn9dih4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=HdITn0a2vDhq4sM-p_HaZG_wCLasso09gpb02wGisTtE9EPuSZImT4WfWjPr7EKF22Tga7C83T4Gh-lr4-gRPFmh0rHalXgiwee3GSM8wdYFWNWp2wYUpBJ9Iks-xkFsHduQ2znZNzY2uosMV9EoW5BrNfBJHX7I8t-XhtlAm7BPBFWCZkZAYdfGcU8MzHo9HgJpsmg7ukv2os0d7Bksr-D-gCbDZOGhbxPfi2319B8VZd9zhd8gTv0LJsS0PucHF1NnEF_DnBOyOMeNAQbZ5k_egyUq11Qb34lmIv8MZ4kiyxk6cSefEsRAmZdT5Dg3Wrhvn2wOjBlt9xSJn9dih4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnDLNk48DbNsr0KZxWRgNPruKrh4FacaD3oP-DgEHUQsKVdAjIB9-GA7vhrZcASQWRnoxLwArVi9n29e8WrV4vFgS9K3QlXiG9pQS9tKPvw7tMFXxV6NILXZnXXwF_svMKZo8aG9ZcRrm-Ms6Hp43XTYj5FXMWykQSPUa4p5MFukHAka9ueXZvVmA4kQUxoa-wvjfyXi-lClAL-U_ogZPmwtGI4PWS6crY_ALWN2XMRAk0a79Jxsby1GvAJsnCo-cB6QwzuwQzt-UwR7GAE_MV8l1deCvPJsG6jLfJOc7VfLly6QK7AsiY5oXK28WusehqyLqeH2cvkEmAozlhnpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFv6Dk3fd6_3A6HFD7QNtFv6MEAZ_FkjT5wIK4WCeUcxvCv2JAoo1Q1H4gkn3oyGUXan8pw8XvUi60QWnLWCC7clybVSZV-M6rS0IOiypKEUK43skfjyn591a52jtffZ3NtD4t8IJV7kutoUshYNPVON1n-mIdmiFOgSFfejkrFGIp1cO2Zpa1CiX3gRR8mDE4xoYDHt6LDAp-25gMjFjIHMLLXK4KYl3SDBV6w7k4rZ-MP3AAKzVADnga8o1ZNr5NPtc9PEJDgxmkm9TwN98XP41VD9l3kjGO4ej4bfYPQtTHJ4htvSR-58ZiLubQEwZvEWdNS367fMS4MWvCgTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZCCXE7u7K6ey3-SpetuBxfkLCp0DhM62NlYIs1LH3Tj2RPddRTqtkg2MieygBc_P4Nbmn7SxR-z64WF0qcv8Ah01dAqO6gI-ozZVfxZq8YkKejfVxo0M_wBG1t6spOV1nTmjLKxEiHJw_XZq8sX-fgUgFLTNbOXJmdo7gkplsCwoEh_BmHj4MtdlXboXJWWAp1JqdKIFadGOZwfHp4oPtZW14iW70Rnq95peqIFF-JHQhQMmai24IW_UBOkwwi4L5OesAfaPRiWrsHgmXX-ue4-_oPAnD55aUCDXf1X5hoMzq2vUPb_bT5h4IWYs68uekHYZd0SM5bdgPbU5lRe8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=CgjuC5MquAwtW9HG4YjPi1jLp2BJzKn7JEpLtTiDGvUMKaQWPnmwm9fasjCFGtl_Gg0neCMPF5mNT1au0WSPb1afhEnHPo9UaUDEka-UtIF1wGsCcfJOcAFZwM8J_bJ8l3Ce1BOI5iIRKjKB3OjYQu26I6GueeFib1ZoCU-g9kbkVlnRUtRvzm-jY7gW94gFckBjkp0kcqI0nWLkbEFin1JjMJmqEWkdiLndt4EpzaVQNJcFoJ7tiAgRYXUdUk8oXaPgg2vBlBMe3aUaeIoJ9GEBFvTJZ9Uy6hC_qwN3gRcKmNPKoNNTbkt_eKHNdS338e9_Jp1pgPVnQiJJFRGsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=CgjuC5MquAwtW9HG4YjPi1jLp2BJzKn7JEpLtTiDGvUMKaQWPnmwm9fasjCFGtl_Gg0neCMPF5mNT1au0WSPb1afhEnHPo9UaUDEka-UtIF1wGsCcfJOcAFZwM8J_bJ8l3Ce1BOI5iIRKjKB3OjYQu26I6GueeFib1ZoCU-g9kbkVlnRUtRvzm-jY7gW94gFckBjkp0kcqI0nWLkbEFin1JjMJmqEWkdiLndt4EpzaVQNJcFoJ7tiAgRYXUdUk8oXaPgg2vBlBMe3aUaeIoJ9GEBFvTJZ9Uy6hC_qwN3gRcKmNPKoNNTbkt_eKHNdS338e9_Jp1pgPVnQiJJFRGsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRUj9LDQbe9gNhbsO36sdwBm-C1l9nbVRc1wNigw7nz5rE9O_uwKKE985ZLeg-QNsvywixMDE6Gly7YE2nYzWbDeL5xVcOoyOkMgoukMxKh6kVevL9mU3IvswL12n9TrzxL8Z3Rrd3EnqZ502wDiZ7J0c2teSmsPPh880nmufHJAcj17_j8obYWpaQA8JCJptmDBsxPwMbqgdcUFTtlOrSpfqwyPkiw8mxl8WSsESR0qLbexCZYUgem7zNLi7x_h39zpc0DkJdpINkfoyQ9JDid1F0AXqht98YUeLwM2UHNoZ-A9eCG8n-xuBvWlZz-W2JLOpGVE5T_TErbrbfb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKITt7oKUgf31lVzK_aZS2rb83RhuWTWoePb7_4wkIdtRNvmHeF6o1ctOQPKxeQH17QzbmyrbzmezDykN_T-u924kExIKMmYulFxnHFph9ZH5yj6-OdsqDtOWdYye2AmUGJijpjYG3zUYZ55agDI1t-jrzreobtQ51aYy3i4w0Dnfs5L0alDz2G3z3u3BqNjK3iMyXINxgevSZQ8Wyadj9uF850nAvm8TdO5OM0SJ6dcAvR0mpb0HqE_wDGi17PVyOgNyGw4FRwJfr90pawS_qfR7_pciofa2v9jgI7BUn9kJmEDVpeoM-fEjiBmQGBy0e_iHA8HcZvFVti4a78cSXdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKITt7oKUgf31lVzK_aZS2rb83RhuWTWoePb7_4wkIdtRNvmHeF6o1ctOQPKxeQH17QzbmyrbzmezDykN_T-u924kExIKMmYulFxnHFph9ZH5yj6-OdsqDtOWdYye2AmUGJijpjYG3zUYZ55agDI1t-jrzreobtQ51aYy3i4w0Dnfs5L0alDz2G3z3u3BqNjK3iMyXINxgevSZQ8Wyadj9uF850nAvm8TdO5OM0SJ6dcAvR0mpb0HqE_wDGi17PVyOgNyGw4FRwJfr90pawS_qfR7_pciofa2v9jgI7BUn9kJmEDVpeoM-fEjiBmQGBy0e_iHA8HcZvFVti4a78cSXdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8F-PWLqjri1_LY_ww4bZ7JGQZ4a9a8Fycj0TnUDAszSWMNeswH0Uf3SsN_UYM2jfQO6saE_tSe3S-2YE4h9ECYAya8Chm33njzWWyzdNjpecCkYxewPjzXMXJ6xvL9H7qnfub8ggjqbKvPdiM4wZ4Y2xQFeym1CxXu70H6c7QdkA6J10mkyeyGUMvnW1v1FLX_CEDT2srzBR1OIS2KWDNoCzaXHZtsKT_o8QFfEmewQtg3mgyDXrPHGJUdZWCR3fWgbj4Bbk1mUsuHueYUznpYQOMaatmyvW8u6LwnbFVVBmCv1_ISW0HWjaPbSZSY1ksiBLy5TK_7vHI0pSReyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQrUCxMw6_NvC641zATCHaSCQe-nQNdmfohXoCj6P-8bS16srDNgx2DD6t3WfJnxccCVFJ4uqxvqgd-apQHAHcvaZNpCd1hfCElHLTTE3iBkzVV8f4aZJr8VGbQj762aytKPG4lvJSWdLlA09slmvYSWVyMCtqMVPSDu1dgT1WzeG6AAnDwX0_kwlIVwt75gcrJHthZ3mxXoMcWwDrpZ_bdDa0C1Io2F3wKeMJUhiresXaAXncLXJmk9ZllatmF4Vc7Shfi3NYL0-EEg3MZVl6VIVeMATQp98zyerkkZHW2AGZrljmEPrEYf8PWRGq3LnSmNQ5M-bJE8F32mhX-yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=AQ2Kf1aBjVvfnHsdSe5xacxM98cUUrP5iDEkz2AV6NrqRBfD2gYKjdo6R7CUdh3rZxzaFXWTbqR172e7WJH8M0lgO-B0noZenRmWIzNGoyrFe5PtCMiq-FTz1zvVTH3P-LuJSIIq3iwCmhEMcQJqtJxGJsR3Nx6xLcLZEVFTCxXwd9I9drf8__coGSeYlrhbzHfev7p-pW9ibY6haJ1pW89Vy244_YMu4hzKaKJEekndeQtUaI72scRlhXyb256d18HgbMiu6abvBU5YSjLAcIFJnl7ZsBImDg88X-aDFxCPFuqWguhgM9rWsiYSZa-e8k3e5qa2Bol8wFH0l7JTiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=AQ2Kf1aBjVvfnHsdSe5xacxM98cUUrP5iDEkz2AV6NrqRBfD2gYKjdo6R7CUdh3rZxzaFXWTbqR172e7WJH8M0lgO-B0noZenRmWIzNGoyrFe5PtCMiq-FTz1zvVTH3P-LuJSIIq3iwCmhEMcQJqtJxGJsR3Nx6xLcLZEVFTCxXwd9I9drf8__coGSeYlrhbzHfev7p-pW9ibY6haJ1pW89Vy244_YMu4hzKaKJEekndeQtUaI72scRlhXyb256d18HgbMiu6abvBU5YSjLAcIFJnl7ZsBImDg88X-aDFxCPFuqWguhgM9rWsiYSZa-e8k3e5qa2Bol8wFH0l7JTiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=hvD0VVuPB24AldJuqsf5EL_gO7VFtjWJKEr9MYD6QqPr8pYDHDeL5Vsdq1BruBkwRGhV1sTSruZ9dDT9UvgoAIlvcfpE9gZ6vISaUJ86zLng_RVk_ZWUYPIEBgPY-PWLcnSrLG_Skvt1oqeSfwzSxnwgYCOfjGYCNvOsA7O4TeT7o2G_4K_2VBJxqLPkCFhCGub_YRic0gmerHolkgakr7BOd5xJe8D9tq4buXGLFpSw0wrBPA1OYiqgWXOsR8hxzPeVnLNl7rV9PFBiyfnijV88BJxeypKnbiYkDvEvGkDZBR2REXuAayxHd4zUv_Wtgxsc0x13AoMJbVeGqb0Ja4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=hvD0VVuPB24AldJuqsf5EL_gO7VFtjWJKEr9MYD6QqPr8pYDHDeL5Vsdq1BruBkwRGhV1sTSruZ9dDT9UvgoAIlvcfpE9gZ6vISaUJ86zLng_RVk_ZWUYPIEBgPY-PWLcnSrLG_Skvt1oqeSfwzSxnwgYCOfjGYCNvOsA7O4TeT7o2G_4K_2VBJxqLPkCFhCGub_YRic0gmerHolkgakr7BOd5xJe8D9tq4buXGLFpSw0wrBPA1OYiqgWXOsR8hxzPeVnLNl7rV9PFBiyfnijV88BJxeypKnbiYkDvEvGkDZBR2REXuAayxHd4zUv_Wtgxsc0x13AoMJbVeGqb0Ja4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=CqtQKMi_jkCg0rUzBhho2msKmF-UTIPOIUUxhz2ntDUU3t8mieWYa358wDmvV5PmHhZGibHVxMuDuG2iVHYOTIQFDRerVE16CIqtBorfgzth6WWworvZkMdcxvsXalJBDxll5i21NAfhclSbyny0l5QEln9yifgAyV1cvVTYTKryFD6ocXGeKh_5jjJCdw1Cbarrtrx5LezBYcCkdCDTl5cmyPkgOqMzMoeu8Rpl_XfWXq86SBzA-5y8-G9TKb6xaf26tXE8Vx2pv3BnE__rySVs0z3LaQu1GpBnMwtq7TPC1oq_XF6gJkkL3LhHTHxTTauD5jdPPr8i64-HzzQfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=CqtQKMi_jkCg0rUzBhho2msKmF-UTIPOIUUxhz2ntDUU3t8mieWYa358wDmvV5PmHhZGibHVxMuDuG2iVHYOTIQFDRerVE16CIqtBorfgzth6WWworvZkMdcxvsXalJBDxll5i21NAfhclSbyny0l5QEln9yifgAyV1cvVTYTKryFD6ocXGeKh_5jjJCdw1Cbarrtrx5LezBYcCkdCDTl5cmyPkgOqMzMoeu8Rpl_XfWXq86SBzA-5y8-G9TKb6xaf26tXE8Vx2pv3BnE__rySVs0z3LaQu1GpBnMwtq7TPC1oq_XF6gJkkL3LhHTHxTTauD5jdPPr8i64-HzzQfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrioGnTHQ15oaWl2bVLTYXYIroPnLai5Lpjcp7PakkPIJ6Hkyxj6Rgxhn3MlA2fDVII8y0LzGuyADO_mNLzxtn9FNFn14BTVnp_AW61Hi0YzkvhcDWpMyirVBAjumz28ni23htqQlK9cPDeFq2DCJiH52Kdm_IdVgBREUNJKF9Qut57OKFEyoh_ZGT_P30_2poA1Rd2RzAx8KSDi-HUU_TBgi1cEV9yCxEATmS6tARipTiZD9V9reZsNNmIlnfT--cH4UeIq-s2axPLqen_kvbznUmByQcWJSQ7s_B2erA0D3cwkdBmK5WABYTDRZyDdc5t5qoTaFDq-3CMrqWqvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmxamZC8dngOPC5KovQmyto8Z36csxtTzeBMKT75-9NzuEmH_3DxxFXDhebXED5SnJFl1qUQwDl1mjci4OK1sTmwqwKU31LLzQLRYdLH2U5BFAHCq2D-6Yuiz_lIKz5CPh9Xk3fHi4voH7LooAv6wY81uhgyuBnWrNZA0paZMDOE4bIIVkBLQHf47MioHPA0RQMg9h3nqtpQAQrXz2Odq5ZYMlimWcsVWc0rzSBmPPMsAiAXtGkU597EWHXjm_ITuQjPGCYX2jOZ2MEdF_YWWWs-ElwnNEN12CvnqdT0QD-jeOkLcZY9QnL4bqJbHjr_osK_Z1_7CfO7QnqltOWeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEndsGUoNEzZnq2isnAwZRskBMj93PRL6hqe7TxDE0nta_-xGF4kn9QHjfLSccLY84rEv_ERDnoLiFQinW31QA81w19oZr7MfCz1kVd6nT0qC6Gj0ENnDIp0DtAvAliOIqFArqm2gm-Qh09xNoSsy9KPx35sD3wInok1r_6p1RWreNznkRm4OdhVZH8MdZG_iisz-aQ2FjBNElCQO-45lctlox7zqWn-frdrOcLfigrE-mUZzqF9qeuvQsrNazsKID9LingEJH80SFJ8eSPrzjWyj3jTb3GJCRVEjcf5TCxGU8hz8z3BEhdv2pzsOy6Saenb0PqEtUR4rZCOfmEYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO_y5v84isGEUA6MAdlu1DV1LE_PwAroWnKm9eQGga-JlEkz8PcspNqb0QG2mvJY3G1AoHHkKr9DkFmjsRARe0XghJ95rVc6YWrhHuxewSw8tVeyHQr2TRa6Xm5ItrmL4E5WBEm14SB9d3RabDtDPswEe9LAcXi0ZZi_ThjWZOTRSXnb3FgfQT7hNFmIoyPylz9Z40nI8FCdCJ682_e4bEtmiixuVNE-ssZAXeCpvqiUPKtMPgr9n93BuY8RwuF_2UBdVsc_7tFO22Mc21-NVfBb57ncv81H5VUyKtltOwmzzaWuX0vAHliarrTGBJ7y_2aowzNhrl7b26JvaWgw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=dxvHyfTa5jTcRutGr_t2att8rMcGsQIVJ9Gru9X0X9PdxUd7pUe-ZD9_NvxS7R99go7r0hS6tr5ORGN4m3xe8_mGvKZhe7loelDuRmDgFKcd0qWZfw_3xRHuuS-a5OW-TyQbvnXEhTKvkooEfT_l72gDTb-LviXWIF3Pd4YtLeKURMd4JliAc9fdL57LOhxEc7OiZUPAB6qij9jqUgPjXtxREDfkerJXF3ziUmLNGUBOuGPImins8CTIwQbd6l8E9qCPC7nxN4qlJU1vo-x3yfm4sEp3LnLNn3C01x9ciJl9a2rG2WVqCv6bsUkD4Va2Ik4RAECQKOwZsqoNxnvhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=dxvHyfTa5jTcRutGr_t2att8rMcGsQIVJ9Gru9X0X9PdxUd7pUe-ZD9_NvxS7R99go7r0hS6tr5ORGN4m3xe8_mGvKZhe7loelDuRmDgFKcd0qWZfw_3xRHuuS-a5OW-TyQbvnXEhTKvkooEfT_l72gDTb-LviXWIF3Pd4YtLeKURMd4JliAc9fdL57LOhxEc7OiZUPAB6qij9jqUgPjXtxREDfkerJXF3ziUmLNGUBOuGPImins8CTIwQbd6l8E9qCPC7nxN4qlJU1vo-x3yfm4sEp3LnLNn3C01x9ciJl9a2rG2WVqCv6bsUkD4Va2Ik4RAECQKOwZsqoNxnvhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq6lpKs4DnikLOr2S3OHFAkQuci00REEuJBQeupOAIt7n9dtZpE1KW5NnvERHw3_O6mnZxkytgOrHuj3Fbzd5pWaFqQC5_ATJ1OpQ5d-xujyeqUHl0Cyi2xa1TtsYbSY9iPqWrROGmSHmPEnjLvvDlsJ6iUz0Ea0E0AqLnz6BRr5pfptw9GXL_pHU_9zPIpCsetEVF8Xiyw-9hG8NOtnkxHtUTCYGEwudg2eCZ8hMdFJHGiDL6X7w1RATJ-IGa9ZVosY5gJXNQf6J2Mrz4s8wLVWX_bjCEqlmnvl7_FHDta5emAzpQeS7DPh662e2ISi_9O15n_hHN6nlqlPssZ1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2WmhyzDH_-TMOdJo4fiR_V2HO30fgkC4UaO-sBCRgjJ7-VNGwDZ87S2odauhUjzXDlQrCVk91Qvzol6GCCwm9Gq9TWlqcJMJ2qOH3htucHOins1BmdPTjRl17JM2YtiDw0gc66m-mDdLqOMR66lKRoQuAH-YI5bE_X7CdTE48TBmHQdCPxTH0do73eZAVQgm8SnDdWC1dA2PDat_daCYSFjW36BFDBVCyUzKJxvlqY9tMC2m2W2fnb7E5U15guUc0Rd1I6a8N1tbQEdxx_Rfmjiz1IRCqNhoUWhBM-iSmGVFXMqdSV6sUykQnmkSpG5VJjNlSbAolU8s4JEB8Rusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=u9CaxdU5EGqgzvxSmCwsyI8Okj2XnLX0YukEF6R6EXuYRuDpWtEhYJ3ulb5lA13omD2bnHJisxpgWe3D-Eo3WDLzLEtbk4mOz3HVKp945SPyGzL1VYa7oHBG3WqzGTi4t_clX6-Sa_IxQ9mm8e3L5TgxC48_hNv40voWyLoBmqgqEGkOgpRBrWOQCxvEvDQrWqcD72jXheVyHB0cppxFSMTSpLRr4jYLjYy7UOjdfjtfKK24Iq0R-QO8-8uixSU27CjvhwCKB_tWN_0aSrWP8SD9M_JLV4Pe-JlEHaxX_kR7fU0P6qD7UIed4O0YOt0hldLVfUGjknwXu0iR_PIJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=u9CaxdU5EGqgzvxSmCwsyI8Okj2XnLX0YukEF6R6EXuYRuDpWtEhYJ3ulb5lA13omD2bnHJisxpgWe3D-Eo3WDLzLEtbk4mOz3HVKp945SPyGzL1VYa7oHBG3WqzGTi4t_clX6-Sa_IxQ9mm8e3L5TgxC48_hNv40voWyLoBmqgqEGkOgpRBrWOQCxvEvDQrWqcD72jXheVyHB0cppxFSMTSpLRr4jYLjYy7UOjdfjtfKK24Iq0R-QO8-8uixSU27CjvhwCKB_tWN_0aSrWP8SD9M_JLV4Pe-JlEHaxX_kR7fU0P6qD7UIed4O0YOt0hldLVfUGjknwXu0iR_PIJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzI_egD_bAMPB1PvZY57qeNYVooqgjal1BiNBUxaY_BSRBO9nxQwWTrZ-5gagGx4c1h9GZxHc8KVemsDeIuzXxBkUnR0F_kcjQ0zJBsk8gG7HGjJGy_pOXxuyW8i1zVQx8qJJbXTVlNHiw_OsEHaIS3KuWAuztNRcTTOOAqBE3curzcaELWLZB9QxDLs0gMD_zV6cYVYVnt9f2Z7ZsfjAncbGSm4r9kbTf4X7Z7luE1YBWRv_Y1V_QgmDx9dsLB_0d96kRUT04Uv4kzRomMTT6Xk8TvzwbI9IMEIdBNgYu-kitARgmoB1h3svmTwj6pCXOYHRSBkYorzCmXYB1YeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk8z8Iz9O_1m6ryNhy_4-N2FpXzY7EtyPfpDjuigOREZ6BQqC6oCB1X1CUZ6-A328-qFh38XSedn9lFxMZ7z79T5tXTA77CaAOmNYpGf6cXx0gzJTWOJ4oGXyov10oRCPAqrj9oDtyBYcCR3yYABznRWE1Kbf8UMA_vIWvUd3zrt0mO2Gx4YsHlCn952FXXhhE_pwnM1QcZGl7EDhRduZyYmlNbVxiYRv5cJJI3msNLznt7pTxs9BPp946-SZuOQbQkTgosZQXAxjwTSSFI_IJbLN64bAuwELK3duvfBwChIVcq8lXC9johmPdfb_HMguLjAirbzGsg5XrzLR-c2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxeoMvn8llXp6znN2jwoAeefNh6FBZ7iEgVgCh9Twl96gBU-YvRwyUlSgxcEF6YyPxoiOX4WnysQApYU4aieem3OcHc_OYkGbfJmbPXs0E-AVPZm-D3XGNI9qE1eKAX2mfhgyiIjjzbhUVFj296GfcuBgP6W0mwQTSeOv1-TfzgGTqv4cHjJ90OcefGZDyfYxgq54j7LoXnIw118_KqtunXN84eRgXKOqIIWpp_QYn8ThQQrUdK-DqhmSFfbx9u4K666G7PU6NLzQdv22H3D6MWABszntljMFxlA9fcBjUUXTCN4J4hbn0UoIUwWiDxEE-egpkqFCIx_VvYSv9CVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbtIemxkCIi68H1hb6pIFeVQhkPmLCuJ9P29hCd8gm6rUmC4GmVKHBm_ffZsbagL7IBu5iI5uPb4plav8ZHrHifoWtRMW7wcC5WsCnegHBUQjqpIshsLdPZ-7NMa2M4OleWl22TXK3GZ5cuJifzx_t2-cJN2sXxT3Zsm5GTSXAn1xJ4TU7L2cE4wI9eFx-hgr3AZvcpw8DODgD99bS9gVDxFc4OktER_8nXh4ZS9R0_QnL1G8Yxv3eqiJUdGdAUNnBm5WWcl4NIyjei-Lq1Fxkk9Ur3HoFLyUAThQjCOqkMyGsZO31fhIOSEeakLjO7G1DowBErU0t3QfpbRgV6uWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGYH8Jcj4tSfAnbrfBldJAw7XiM1VMEFiM-URPgxe_KHTt0MJ3t1IijvrSXXVtOCX3pJ-VuRJuQwj9maU74f1PhiIJr8DTTypfAZhXhfvePuRJzFzqsXTxTnxieYmdNIz0sSZbN7NGEMiYP6-q3vbJ5Cv-H_mE206BPNmE6ux4Av6TbOngFH37rMl-kcovnHuNvcBrM85VrJoQJHT2YEHqY3BZatKcfTb1qT-KDg7lEOagLua3d1u7-mUpADXqQA0kZpJDXJZhNaeizWz3kQFr1SixKNOshGj20q8Ac8w3PIlvJ0zGfiVCSvC8zvqDQbM91VJcbzot1W8_Gon2hS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8rc9S_V53RcTPEELukS_RWE6-o__DNYFCT4g45aykdVdyTNp0wwGRKYmFQrG8ZZ5FmGQa4OIGKzZRCF2FHisy0EKJSxgYfVVJ44egNCG8xrhTm8SrFpwlm44CZMbtsTsfDyfO0eiQHd2iYOh5X7uNd5-WOIg4sBmeJyzFLidw-VipVm9MJmyK_c9gwpBc2JD5fwjGHw1nAaWrqwuKLvcmL28J9jx5PWx3qb9__okb_mt1oMDFAku4v83cgOBJZrBBenJtvPVz50bB8q5fatXoBF6P7NzrXq8OU7LaZUl0eu7KFMJQfPYRCfICmId328f8lMF1SeCurQ77Vp6QNVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=hlAeK7BNWYFxdhvpalD_2N1sRpWOwT7seOSwaKz5KmrfdHKkCGeug47z19Ee5oK0utJmrOkpBAGE6EReKX-qS3C26vDpwu1QRbgnLXU0otEuiZ7IxJBVNV8qIYMULxEjdcvxbbR11sFzoYTeFRuSauitOCowX6EPysdEMTsE2n7ZxCKxe1h6FMXu74ZZCjm_1mQ3TvELGLR2cvXDhN0h-21DSH4-BUzS7MmUtLjQBdhmdW777xbUrA3gptxDtuduhOrJvRqsLRGSLp78G8A_8gojlBerHQZ1CjrtNth0cYUZFHNiNY0lkky-Wl69Z2gvKH_s9jASMZ7uuCccAkVeUb60J9HekXP7p0ITnLGdS6e7sL5pKg2isagruSoij_TW3yLBEIu2sU_MUw41UCa-6r6WZYzMVI5InOA3HFBy7GbcFOzzeFd95RabB59x1eCzbetYvXf_NsyxiN2vCzebl2stKjrwrltqzWtr3ZbTk1_eJBLGF4PKjnMBinMnLgTPea7P_94NrKmwMcXKPygw1Xlr0Okk0xhiIB_x5FUF32nvWissik2XQJai4Yna8475pzU9s63kfOvGJp0t5rZeGvoItesCtenwFiNzmpk6N4QBwmB9nFXkTdKi-rScn3NeSJZrFlDkdbasLcZEquV3nQjmxbXUtF6CQWtely9zQtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=hlAeK7BNWYFxdhvpalD_2N1sRpWOwT7seOSwaKz5KmrfdHKkCGeug47z19Ee5oK0utJmrOkpBAGE6EReKX-qS3C26vDpwu1QRbgnLXU0otEuiZ7IxJBVNV8qIYMULxEjdcvxbbR11sFzoYTeFRuSauitOCowX6EPysdEMTsE2n7ZxCKxe1h6FMXu74ZZCjm_1mQ3TvELGLR2cvXDhN0h-21DSH4-BUzS7MmUtLjQBdhmdW777xbUrA3gptxDtuduhOrJvRqsLRGSLp78G8A_8gojlBerHQZ1CjrtNth0cYUZFHNiNY0lkky-Wl69Z2gvKH_s9jASMZ7uuCccAkVeUb60J9HekXP7p0ITnLGdS6e7sL5pKg2isagruSoij_TW3yLBEIu2sU_MUw41UCa-6r6WZYzMVI5InOA3HFBy7GbcFOzzeFd95RabB59x1eCzbetYvXf_NsyxiN2vCzebl2stKjrwrltqzWtr3ZbTk1_eJBLGF4PKjnMBinMnLgTPea7P_94NrKmwMcXKPygw1Xlr0Okk0xhiIB_x5FUF32nvWissik2XQJai4Yna8475pzU9s63kfOvGJp0t5rZeGvoItesCtenwFiNzmpk6N4QBwmB9nFXkTdKi-rScn3NeSJZrFlDkdbasLcZEquV3nQjmxbXUtF6CQWtely9zQtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=qtbfT_o7YYbjSeYGaz_mxzwQogmyhg-8A695-6CrVu6hzvKNCGPtblV6O1H5Zvrk6THzdX2JUCi1nlTNKsY_XtCEiPQ-9JJ5M_4g-d6KZ9FHnp0yViENXRbK5FJIZRFblbO3u3qKh3mX59sgJLpcuyQeEd0TX29kgej26idQbnH2PQiTA4Sftj27jFGgni8Z654rCSTx4jpVDxqW5wsfaxxoX0pjCBvQaJ2PaTNwc-6td6NlrZtuMFIDyHVrJSwzAg2bP1YiyyHXI6JtaFZ70cZ5huoMedlSQoEYExAmZeS0wuaLKdSmdyNOwFaNCC8Cj3QjVBM-TQzO-nAKTJMstKKcDVGg4TtOAuVsQB1z3QBrcwcgMlOiFRqR9IYGzd6Hp1Hr1XGRQ9hkNcfm2ni0sqfH3aAWLKhVMoMZJK5PCF4aicP9pRimhbyrRFEXcdcXzJy3qbVtNbyORP0XtGZ9X6Ep_guVbYDMNfdtWFwFv4AvteBLAc1pZUyzWFnrrEGN6LRNBZMZBb9chXfjauKO1X0wZo3eisyVcXLMI_3GzbUosmD8CXoP4PkHz2LwQui4gHn9cvO7sPjG-wK1GfrldhNbkYeDUolZm8pgGx2hcJc1Sc485D8SafIOS8zqoaILB7vaOHHPSJiBRvgbzFSlc8COW2mEJR0dAgik8TRH6pU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=qtbfT_o7YYbjSeYGaz_mxzwQogmyhg-8A695-6CrVu6hzvKNCGPtblV6O1H5Zvrk6THzdX2JUCi1nlTNKsY_XtCEiPQ-9JJ5M_4g-d6KZ9FHnp0yViENXRbK5FJIZRFblbO3u3qKh3mX59sgJLpcuyQeEd0TX29kgej26idQbnH2PQiTA4Sftj27jFGgni8Z654rCSTx4jpVDxqW5wsfaxxoX0pjCBvQaJ2PaTNwc-6td6NlrZtuMFIDyHVrJSwzAg2bP1YiyyHXI6JtaFZ70cZ5huoMedlSQoEYExAmZeS0wuaLKdSmdyNOwFaNCC8Cj3QjVBM-TQzO-nAKTJMstKKcDVGg4TtOAuVsQB1z3QBrcwcgMlOiFRqR9IYGzd6Hp1Hr1XGRQ9hkNcfm2ni0sqfH3aAWLKhVMoMZJK5PCF4aicP9pRimhbyrRFEXcdcXzJy3qbVtNbyORP0XtGZ9X6Ep_guVbYDMNfdtWFwFv4AvteBLAc1pZUyzWFnrrEGN6LRNBZMZBb9chXfjauKO1X0wZo3eisyVcXLMI_3GzbUosmD8CXoP4PkHz2LwQui4gHn9cvO7sPjG-wK1GfrldhNbkYeDUolZm8pgGx2hcJc1Sc485D8SafIOS8zqoaILB7vaOHHPSJiBRvgbzFSlc8COW2mEJR0dAgik8TRH6pU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDX2zk7xfBj47NIvT6uYOuK9qKuMEZHfMHtvNMibhaQJJ_JMy7kAa0sDtbKEeZQeZsaP8A29H1tddV1l6y6Z-2bGOFFbpYITPAOV9EEkVT964PiFSAKnYgbRC7ObBbqX7KUeekYHVCteQ_N9UeAJqYdWbDTgqfB99NA7WyFb7NszEZAdiY2ewaQiyYh79Uw39ZkbiBs34qWkRPl3TCf9AWs4foZU5CO7u8-PrNrvqdGJhSI4wJCXL1lF2F7uXVaP8M1mBZJdxyLvNqztWYNcB2DPE0CTqhXhhJUU0NuarLrckLIgejRn6D8tkcrcjV-tpSgy78qqmxAsYvxfHWtQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTpb5P1_ku0aid587_NsrDt5OTQecOt1B1iRM5YsP7aXgxBlvueLAHN07mMObIcWeMzFKz3b5r7sREwJSQIN5i3NzPeOYAnKEcKhzH3a7VuBURiXrcCr3ZH-4X6YwrUNf3Kzqye_rDLbwzpYqedCyq0Y4lE9UEP5w2lL6u1k4FkCA8dwEIGaNnnhu4cLDf5pOb5v7OGKpdsHkI0J7U0D4NHijTL-2BginIET6ODeinJ0RAnXmPfk1SQRtTIybHsZMMxdje1ZV03qYIKM7EHfz63HPsr7BO8SCHN0Srd4-u5jlkxza8x6419WVqrSQYxeNSMtUUQ-nqMzOhpDcTb4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgDD0IyKKvKcougx18c9qDC9YchkzI6cc1pbCSKnve74JFq6gB9YKH8-yhSOpFtuwvf0ZvW72mJv-9ShrmiJLQECspM2_1Z4FpjdvenVTIhTDvneuFuFSDS3hf01_Gq4xRKBnEoSIDh64C9iBNQn0BeILUsnusTstUeKiXGxDK-_vCyIvzCyucZkl5L38uOQQ_lvT_XfVed5qPl7CwY5DK0mLYrba9_C4FK9fMDtLGw79hEBVnul6FmQqWTtsaWdxKMk5hVPtfas57xD1Tr37IwZJByYBfERNcEB7VvHUbWyG39WWbzW-6SVg0UKTcoQmzQUgXTX1ofyxcMbioelGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGyQtPVtju6PdLoqhVMySMhYd0ZgKWkdanlCiPAwkBKmQpXZuwRJVBbuLHJq_y7ZBDBvTtxqh7Z0Dc9D6oAxWw7kiA6rI3xZLaJEYIT0GcPbBEbq4WaSYInFI7EuuTNaQpas5DAgFdmIdLHIAOf6YW6tnnqsmtWCZHpAQ6c14ryqEUQBSulkWTcDXVQ7nC5ptiDFR_6-BCOE9NGyOkHFSBEylN1BtcYeNuWyw_3PCjJaMk2kleeUBZsPxyKTDUvSc5u1bueUu644FkN1oHCbkYi5JzT5teu5Y0942aXULAGSjv35hZATySsu37I9Ib4n5dO_t6IbhwJUVYNM_eGkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY5GVREgTdtSgQgygKZU6kxPqT2eOnFcH_wvLSoiycdkFMR7sfql-DUaDmehCQOmpPpyOOkb8oHzTqzltMcdVzWURW1dsROHPo9rV0sTy0Bw5ZnTppUH_-2BDRb7m05qFtD25xZpmzOTHbeKwEfTRb9UMUc3-1iFjCBgKz_Rg0jNNHMsT7Cosjdy3y868iypmkmxgGfkgDwKCToKC1RB2lgah3fpoV5cku1svVOno6dyWenGywEojqsn6_-lLKnuFS0M1yfv1a-PGnlZtpu3eYvDuW7cGra8cnSXEpoVaZeq7WRDKFfsGHsoCXWeFSB6Gr-DAxjaAyMat1nK1e_dSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apES4vUxjjQRcRUFdoG_JK0MICcvYD7Iaa7DWxYXLxp0fpgH94UwF4xs2ZcYXMQexTKE7afIHlnUMRQOH6WdOp7XhtkFBnlKDWNydK-GUPh5aGhHsp8TwAsz_7jDPlsef1FuvHAtiWijnL62ezCKCrsvQ43fWbT2HEezpDjvDNCym9LsZXagusjGNrzsAOMbGyYMDBf02ov1E3meA3eyOYjmQgmd4uIQRDpxMgaVOylphtFYVXm6ycNIE3RtV_z1Rs8uQAgaghIUw1AbFG1LmRfAMqVaYX08zMatjgpajK3H1SKf5iwZWoYR7rZLjxOAcsKJd-6UfnxBz4bsPk5uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agusT9MF3pP27vVV3XRJVFDWdKHqfyL6fyzmk-NE0aqBj2x4M8CLxNiRtnXuqnNLjTysM6OuNxEAVuIxIZaLGPMiIi9b1LTQxgu4KOYk1yNiiiCdOeYVpfRFFeEBYbnMtbV8Ysx1VOEgH8lD8QTwimYQnrfqmuHn121p_fpNzLwW5uIeq2bZgNRHZ-4crwZuCE_ASpEPvl-1kTCJZL0bWscLxkQhC4ZKg1if6KZgRjG8J-EicOQhWkR2hPKaRUsoIgyCXnykwfJ3aM_vZxxDhPTocFk1jGeYurK4r7F_DjCASZwlX-v02t7jNgnlOJV7BtCvWAaVbVaMtCuhKIwTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku6e5HdMYwDRBgLmyosZVWIRPy0oFff-2OyiSTST-jeJQJ3jCAPn387F1hyqJ9NazQmcqIMneRWvjLPu1p-7jbSVDfafZsplYo1d9XimHEj2mAMmzGb3OARHstERt7ne6tf_ctWPfinr6BHwr25OUmaf6uE3eVEBCm5Ux_eijTiIult-DdqEaHXWf4uhFwOZgHVJHBYUGdmkCcaYcAtHIcwRPufMHKkB_hf3ZWuRA_ONq16LhcFy7BSE_8C5DLqgsWdGjYQdWOn5Ljtfwnx8vkEFcmX2BRqmRYcCg8-a5BnOOEcgd-OPIoeqz-cWIuhgOvy_osg9ilaGZDDe_b8Vmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=HOpXdoUDMDUPIMsSFJArlUW3Y6gaB8_UPui6OhbRI0Svs3wnQajTwWe9M-Sg9G9Ib8seCywtGhNx6OfCKTlKE2Gg_sQpmAnwfNiS_k3zmEV1310iKQvVW2RnBqeCB8OEMvBPczV_J9HWiOUChcTMZHxzxfWwcqvy0F8vbnUVdj5LPuC6yZnZo2d2UUhRBElDcTtaTacox3Dp5ulacQOCR3Jq9RfV0ioGFtAFjnHyZBbv9mWsTdNpxIQPtuFfU1S4yNot2SH6P_6t7Q7xB6WNFac6Pbxgl-A4uuu1tzx_-CZTwcud6KhFQUYD-3dOlRN3aAaP7H65qskepNz5CBbTKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=HOpXdoUDMDUPIMsSFJArlUW3Y6gaB8_UPui6OhbRI0Svs3wnQajTwWe9M-Sg9G9Ib8seCywtGhNx6OfCKTlKE2Gg_sQpmAnwfNiS_k3zmEV1310iKQvVW2RnBqeCB8OEMvBPczV_J9HWiOUChcTMZHxzxfWwcqvy0F8vbnUVdj5LPuC6yZnZo2d2UUhRBElDcTtaTacox3Dp5ulacQOCR3Jq9RfV0ioGFtAFjnHyZBbv9mWsTdNpxIQPtuFfU1S4yNot2SH6P_6t7Q7xB6WNFac6Pbxgl-A4uuu1tzx_-CZTwcud6KhFQUYD-3dOlRN3aAaP7H65qskepNz5CBbTKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-f7WkFGIweGlEZsEQTRuoQZDg7-qWWEu-gtmbT3f4qQ-arB_6rwSzp5ehrYpVpshydzqPqhI5Minz3zSw4WmMMOq2TP6Bn2urvBAEtKe4EEsYLP97p5z7ZfX4RNnDAPVNCkM8qlglLV0wOB9CDERsV5Y2aNrSAg0SJHo8ir0gAJcQ8pyRltho70pwHg4TUMR6-WaGid2h9G7zHdEghJiDTfzbrjvKS8R0HWfkg4fTRa9j2OVdaiO2jKqlE3_HOxnBpf3l4X-btj2eH3GT4iBDhAgRQ3mvfJSfGuX6eD_gT7YRFYoesBiTD1DlsrW4WvcBYSKRY0aAuh_vumYd7yXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
