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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prgNmX9H2Kr_Tj3vw9zhkbLcvRjDX1E98_vQm7-eFKNR4RnYZa-89JBCfKoS6JMvk4WAjFbeQQzGMapOdBeTnyhPzVQ-xYfLi1ICDIFkk_7PrwP6INwlbK4U35M6G2t9uIrmg1ACnUOSDUqjQs-EsVOSQQZ3-mjDNRQGmRMmnqR35m272pYB5ZWsTpYCqkLA4ekyfII5nseIVPd0CP5LBLJQOAYyzy71C65W4R51dGqfpk0Vl5eMuMDBRWoL23IXFJOODms1G-81sHtlv6c4KoFkOsZsRZ1nhy-THzX9nye_363X7iNdesFCC8ZQaE1U2aZdNsEWBeZDWr_zVZkgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk1eKhpx_A6YTa5gl89rretYos67CqV66s8Qp9UyOSeUS7njvbY1ANha_dgIVrTRMRz5BhfwujEMN7p3jpu7A2Dj72W83RZBgjeHCPtODbYm34kiBHJ4DGdHdyFutlcavwGSVJwFyitSeVZTOREmjsEsg-LvbSf2iInsj6ed9UaH8Z1gDz4sOc538qLP6inYGKGlkk2v8tv2dZq8MQnzGn70Y6aRTnckisCCEtKB3nQHZcF7tExlZc8sn1x15LK1l3oy9d9EJ9IJCRd9ZNTM4bv1GdaDjjkepRK7QGZHkY5J8yYS2LwYnO52Ns3LqwrMrW1DH_ZH8SJbkl8B_LJqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3HwToLVxFasxwAh44xLl3CS17vz1RHoMKsf0KjnFLRhZ2evvH3_qcF1OQbga8QOEpUSFf7tKxvdBhw9jp3phMUslPyQzz38VvzBdkBnnLhRB49GO6VVLvP08_srv5dwUl_cjbwjjpC-05U7GLXzHf379ZadtC5lSZu92qhIjhzFVB0HoIw_e_b3qJzhTTHtsJb26FmTW9neRca5yMszJkCPGCaCPiMiI8DLUqDmh6e--xyREWI3B8XVRwcc6eQABohvekBrVCE1InyRinea0t-e_iRAIbli2MOoqboN6QCUn-2Y0eeKPvbW-T9g8VecR4FjwNXEOjaAZ3Roh8ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=KowiR8ryM0fUyiyUN_DCZttg9H_gmUuBgBnKDTGbPcxgxZQA-q5aXUZmcAx2x5LgmieiBxM2Dwfx6xJ35KjqghySdFaPzqchTvRdp5C9vh9UFhEu56NlQ14-Ps2kkVABx6M4Br7s47ATIKT_3O9P6UHuvrGHDBVBK5ed-Jx0JJ_gvYt7aJbOQdL1zVJRuMvUbFi8BG36C9MSoTXctWgevLbWwb3NYQV0Sm3sogv6x0Z0v5T1HJoP4o5TR-5IzgN1n32s-VdH4-yNSXY_eM1L5-_YdJjzu9x1f549psgyEEtMDNNWcu592D4afzehc8U0QCe5LnLMYQ9uba_R5iRXCoZCcnatS0e0qv8c-M1swIE-XffSHPzJLtglec0l-El_s_xAa5mlTanmGfH2VD5ldaey5WkKS2ZIycfZVr08W7tzbCFQGUt0Cu-_DpndbIuNh6wn7DZfrg5Uu5DxHWJCAnCq-E7Zl-E_UNIg4XUS2F4deoNi05WlEawtSpFAwm9Nma7NicQPuCp4oxvA3HlwqLcy0qqrxI2wxgKyVUta0sbkw-n9pabIOCbQ_E_nuOptMkSNkkEDGC9svpyerLTeeGeUHfffIto7XMw9MFXvHqTrYLBCUlF_Nls9EpB8EBw5cNtHMDlFYVR1fmOdMzsekUrDnyoK4pRrUTZdvNHCHhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/667106b64a.mp4?token=kz810Gvf8Mwf30Ra5_kvfIYAsJhiFxtjmbSQy3ZfBBxJQGT7nF98mPUcPTSzyMALefRjqaGEWaaK_5IH8fQ2yv0TEKc665Zz6nfKBSy_M5I0e6yRow8FY9-J7BmX9RZxKOnmYwW0tl9AsYJhGZknH_huWZdfActUyabzudRFp-pWUlMKNP6NrlPhoYhNr4I_aDzQXb8bvH9_q0FcXYlW5Bkh1WuDGumajeOBqxBBFXdRppfhlILC4Gn2Pp2u2rS0Ecni0_SS81uObl5OTaLQZscgJG0dqxFtD7_YzfF83x6HN0Kr4NnAX0OIYuvQixcj9SOOVK0EKp2YL4-hDwds-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موزیک ویدیو کامل آهنگ جدید توماج صالحی به اسم «تو چی؟» که تا تونسته به رضا پهلوی دیس داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/131684" target="_blank">📅 01:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم  «تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/131683" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiNsjJ1iavbklIhh17lVhazii-izRmAG13PmIqfUhLeHA7TTggndo8hMaRkAa0npv-jdtWon8-PolzpdWxfF5UxYHmyhwziPZQNwB5cA0iE_2Ofuwtf30kjHlvDB1WA6Aklp5ZWtSmnFocIz4FE1y5lFoLBJRxRQVtHgtLRVshGvXAbeP3_iMRjmBQNT_wofMpvjpkxsKa7CRXCxaSm-MMDFLTMroGT0M0JelrG5MDzpIb0ZcgTi6tUdAp3yk5LWELElkCQVVj1xCEqyRiPwvJiFBgiT5QsYMgGeQ5Ou6vxmyfnvfAvMXfHwBwMiFSaoqn0zJFPHyCRvchrNWI7LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131682" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68bfd54e.mp4?token=drwhBEDjuPy4H2IOYPXmhK4M1jvZ3HK89nuS9OArC2d3I3xz-U09Yfjhncj0BzWO9HDE6kFQPTYJfBeJwm4C_k_Auh4rldP0tpjMbUnIAWCA6DVy9EWXZdHSFnFq_ECIMWSWvb80EEfMGd7CFkwhOVaz04UeJE3pKVFoIC9HHAqJcaBZrRDuzO7JhxoC70U2fakt_h2o5DDjiv9K6itPbGNY5EJ8jGI32ej3bOeRZxFosurulf2qQtikLyje6FQVwDFXBCiEtYCPMcCUlZakuK_GdAg4e8ZGh-dxZNlR8xTzxBWxba9_KFtyJ6FHOhB0UB7OiswBPAmgz7kMm3CSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توماج صالحی یه موزیک ویدیو به اسم
«تو چی» داده و رضا پهلوی رو دیس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/131681" target="_blank">📅 00:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت
🔴
پ.ن : تاثیر گذار بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/131680" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuVr87DN48mRkKzD-3lTLZrsNu89ecgxAHRaS73QpafudGMGb6x7TePo1Dvq7f20Fhdb7og5Z1X5DyBbUF7RppkUvQoLy5doKTyByOFvp5i_FL1kwXoQkCCLEv6egclqgqYacJHJd-w8ntckIRo2tb6QEvZpXadp-0YONTP31mI_5YtINdS1LZSgqo1QFm2XWizXkK6Ac3QLnpTnFphxmXMf_4s4uIZQkZrRIcFwQ7qQq48-2AiDYg_vyA7kz9Zs7J-hqqxZrqf1_lzyshijDgxJVQ2x8_oBib8kRojkrwLOaS66IjEFTAQQGM_aouLHInDpkCA8GcJv8sCSUR42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان بعد از ایران به ترکیه رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/131679" target="_blank">📅 23:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/131678" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131677" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brMBg6fgltoVq7NRa8ynlR4mSt2XX9UQnbrYkSbPsGoiGAz73MgVpRHjczbkV3NHc-5m8NAOexCrcugZhzgLqqc2m7PcAEPRtvJrQm90w3WZKCgCCUtoAJ9R507bLE6q2zLlIY1vN7e2WgCcBwmw5Sbvlgm0jbZYAAsz7AAdQrFRoq5D0fbGRL0wE11OReq_yjKNUoVk5PB8bpXwyQ3_HJa9_KuDtvTF3e7R1IbJ94hHNI8l_FaSbpRSI4SPQYe9pbUyBXA84Qh9ziVuk9p3MizjtGnQnJAv4lnbq2TfAGfx4OJXNGEUzDzbAcP_WC2bEFTQ1xeuu7dxVBw5KXW7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی: ابراهیم ذوالفقاری چون تو مراسم تشییع رهبر شرکت نکرد،پس صد در صد مطمئن شدیم هوش مصنوعیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/131676" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrvzamxIC3wOvA446rIRbiZ_bexqkNA7_iVBv8bdc7HSmXlufCIhyLNbQTThzofAArM1DKV9E-I-MPJQAmu35KPUuMdmrHDkAqXHuYM_aMkvr_R-w7euXEKqm4HonR78-Gf488zWB9mSMzdrhd22wGN91xtWzosrUJ4zyX3dugu4P6cQZNBZkQyJjiOZ-p5zakpTyQBLoY8zSS91oOvhuG0eancsYU87r11mzbfx6b8bykMY8fPUEIW_Q0XrKyKeSltQocMNQMUvbSDZiFWjkebLJDDyzTdiOPOS_fKGP4LX0hRFGe6QKAehyoUpqzagle9tCaePjEWARrQisbX3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/131675" target="_blank">📅 23:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff6ec588e.mov?token=b0W5o2yKFNszC8w0oHx3achW4XVcbjZsuVf_8cSjAZkmwqwOP0VjTUUezjdVhYy7le6eYwFpFI1Gpf15FA0M57-m_oK1zKFJBiafTzLuSKq_M-H6GYOhm7Cg-TODXhBPZ9T3fdF7nWZcLonYtupYKcP-sIYpv4kA1teNZ4wiReJWZC5Lrj-yFhLWqFogBZejYgSZuNIpFCN4rqMzacjAUz_EEauOttEq_SqYH2YTtC81VXMfC3Kz9SZZvs1SeUucBRas89ygqH1IkxZ3GpOkcyGmjrLrOPBvp26uxyvLdXY2sfx0XGQaHD-aGuqNZDeJkSJn7PtzxkxfKVoJ8Td1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین یبار دیگه با لباس نظامی ظاهر شد و گفت که نیروهای روسیه ابتکار عمل استراتژیک رو تو خطوط مقدم جنگ در دست دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131674" target="_blank">📅 23:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین دستور داده تا به دقت تحلیل کند که کدام از متحدان کی‌یف در تحریک ادامه درگیری‌ها نقش دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/131673" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9r7cyrgy8w51x9MPpEpGXFvWDnJ1iE7kPK-n9mgvqU5qulnh4UZZgdJROVf-d1c0M4KSZImMoLCJcKAuMzwjqtkOhvDrJJ651Fxw1Tlo2cSuiiNPHun0GS7E01Eofvh-i9Xa5J4qBcnNVLA2Zlmj_9m0NTMKOJZv-hjSr48wC6JQYbKh08bO5RW9pvupIDHRAgFzdLgM_XUJeZhTiAC6dfekPQCmhlZ_11oHbItBeR5pxaNQNTX_k5C7l_sCMOfixpkPBlfoYSoyqY-41WS7V_WCtMxcSGA5vlCtjwLra4qdkEJcqVtLElzcgJwjrYVZy_LX03p8I1CjlvPE_SRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: افتخار بزرگ من این است که همین الان برای شش نفری که توسط دولت بایدن آزار دیده بودند و در زندان بودند یا به زندان فرستاده می‌شدند، به خاطر «تعمیر ماشینشان»، بخشش امضا کرده‌ام.
🔴
در حالی که می‌دانم این موضوع مسخره به نظر می‌رسد، با این حال یک واقعیت است و بخشی از تسلیح‌سازی و احمقانه‌ای است که کشور ما مجبور بود در طول چهار سال طولانی خواب‌آلود جو بایدن تحمل کند.
🔴
من همه آن‌ها را همین الان آزاد می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131672" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6ccf94e0.mp4?token=ixas-OZBS06wVB0oHDOZhyhm85gDaSH7KxrNVfWFlSNrDOaFNbyd54sX7XgKmCLn3AuWuRZowKE67Akpd1_X5sDnO5loqybnfXzgcsT7Mb0F6CODDjlmxJ9Uq6F4h5tKhUb5XxscMyo9RxO1CQgh0OOO6gnJyuKeA-ZLPCGyqiWx7tmLlEimXFBXufvyZXGbQJEsZU7ougVPTft9feGn1gQgP0EPjyVAWeSACEpZt2mQMz9OKo4RPdyXlQOEpv5P6x4PDEgC_S0f6RFpW2Xt4TwvxP2E-DFnvR9jdgLYcO4MNfSdkz4uHswL4HenabJZolbEWvk-eiV1Qf0X0ulVgy4hOFUdfnsm-s-ni-nQgRTnHR8xrJRCG919NsVkraBRZNBG5cixACQWjpxawuxg33Th0_kftPDO9cv79ZAkh8M0_14esTCmmaWotuTFYNDZxpBg0cggyEh2eTpmR2MrrFbd255jtTtXsvJPDQwSR1bbKLVWXGkP143WJCnKRVNgU4a_P2SUmlXLZg_UkZHMZ-q2_is3BxbPBPpzkTRKrS1eKESRLSFHWp8sgviySGgJ6yzpB-k0JaWjRhXtYdAaGWGWcsOJ-YQJ5BvWnTG5rT5AWqgMyY9mHHEeS0iU6zJcVyCWPnqy0e19XR0zQKBNdvxyhvqlKOo5uI6UYSsIfN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع  می‌گوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131671" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
بر اساس گزارش شبکه NBC، حساب‌های سرمایه‌ گذاری دونالد ترامپ، رئیس‌جمهور آمریکا، در یک روز قبل از توقف تعرفه‌های بزرگ، 327 خرید سهام پنهان انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131670" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/131669" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6d85daac.mp4?token=tbHLTnfNKthFQA90M0J5Wrf74fGos5pK1kb_B0JQ5L3bi72NNDfHs9NEnHr0xog70VZcwG6wuvDtDkqPewlhDGI8eVWisEQO9hNEeaJXRsFP2Z23HHD0v9kJEWj0xL-6-Ql1flrNDd-kkXkFHoPZY_1zsfxq5paV1Mw3AWG4QSDfcawrej4WEfhIl-ganDJ3iavAmREAO-NWOQO_RoVsgi2WtLMkbDkyFUveGuq60PpNvyl_TO3rGl0zQ1GCEr_hGKnd2_FPXvwcWy537Ar5PIJ5Me4JrFrxvpQ8H-K1xXYJv5ve2UAxq7Yof9cAZkqRKLucB0mR10c8ElkVOe4Reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های آشپز برنامه "به خانه برمی‌گردیم" صداوسیما که تغییر جنسیت داده و دختر شده :
تو 5 سالگی، یکی از آشناهامون بهم تجاوز کرد!
من کلا تو خونه پوشش دخترونه داشتم و این عمل، تغییر جنسیت نبود، تطبیق جنسیت بود.
من حتی دفترچه خدمت هم پست کردم که شاید از این حس فرار کنم ولی نشد.
تا 25 سالگی به کسی چیزی نگفته بودم ، حتی اون زمانی که تلویزیون می‌رفتم هم از همه پنهون می‌کردم.
2 تا خودکشی ناموفق هم داشتم چون اون موقع حس خوبی با جسمم نداشتم...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131665" target="_blank">📅 22:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید کاملا مورد
تایید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
➕
با کد تخفیف زیر میتونید با ۵۰ درصد تخفیف خریدتونو انجام بدید(فقط100 نفر اول)
✅
🎁
کد تخفیف :
Express50
.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/131664" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 100,000 تومان
▫️
۴۰ گیگابایت — 190,000 تومان
▫️
۶۰ گیگابایت — 280,000 تومان
▫️
۸۰ گیگابایت — 370,000 تومان
▫️
۱۰۰ گیگابایت — 460,000 تومان
▫️
۱۵۰ گیگابایت — 680,000 تومان
▫️
۲۰۰ گیگابایت — 900,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 1,150,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 190,000 تومان
♦️
۵۰ گیگابایت — 280,000 تومان
♦️
۷۰ گیگابایت — 370,000 تومان
♦️
۱۰۰ گیگابایت — 505,000 تومان
♦️
۱۵۰ گیگابایت — 730,000 تومان
♦️
۲۰۰ گیگابایت — 950,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 1,350,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 480,000 تومان
▫️
۱۰۰ گیگابایت — 555,000 تومان
▫️
۱۵۰ گیگابایت — 785,000 تومان
▫️
۲۰۰ گیگابایت — 1,010,000 تومان
▫️
۳۰۰ گیگابایت — 1,445,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 1,650,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/131663" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj1dqY_GfdkUUP0gn6DDDWKCHOAbHKvF_1hhjwOpH3qA_8A915ZjMF-_BfjuM6vHKRNW7-kt-SOE4MdiTmnyTNL3o7iIsgehX30fwDtn-_cfw534IyNAGXHHbO119Y0aUFEB8z2DqLheOQoQkVq7CWMa64bnK0f9VSkO1OxJy8votd_cuNUEac1hVuOiEFe8Tcg4LNPZdFxVtszgkBpWJYNbg0L36B_t83IcElZ2W0veSkO4M51awab7-0_2kXGjuPvol3K1wmPoEN0plRs_JJM2Ilnqfmp1HH6QmlOiLyfXmW7Uj6dYVEc6Azfkg6Y4cacSbKYIh0oAVOV6aY1R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف به ترامپ: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده.
🔴
ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131662" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
حسین یکتا: ترامپ که می‌خواست ‎۳ روزه کار ایران را تمام کند، هنوز خون‌خواهی ملت ایران را ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131660" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoThN3hchJWvN12i2xx-NdJv1k55QxX__Y8gZzkNdFvXoKoGz8fWk8NJnX_MKuMmd6AlF49Bq3bvg-r9Wa7iisIEyTNMcE0tiifmNVIxiYXVr5xdZWoBVxmRroE3vaBNNwaopKGKKHvFi06wtDw1B9Z7NoRjgUbptLaZyWNmFArgUxfKT_h2vZqLGGfYPdiPOmWGM5tgCmAup8GYiCqiHQhS4ShqbEhb7aJd9hNJUIuIMKgGGpIUXqSJ6-ViqvDLua2WtARjoay8KLrTnoPXjziHx1lXUELiJ6ZcZN5gTm1bZHVLxQoEalujUSJMc14-cmXHk_5siwYxyTTSdRxfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال قبل در همین روز، مجله تایم عکس سیدعلی خامنه‌ای را صفحه اول گذاشت و دقیقا بعد از یک سال روز تشییع جنازه علی خامنه‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/131659" target="_blank">📅 21:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: اولویت‌های دفاعی تعیین‌شده از سوی قائد شهید امت، دست نیرو‌های مسلح را برای پاسخ به دشمن باز کرد و پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131658" target="_blank">📅 21:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
المانیتور: مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/131657" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌ان‌ان: رفت‌وآمد کشتی‌ها در تنگه هرمز در حال افزایش است
🔴
هفته گذشته ۳۳۵ شناور از تنگه هرمز عبور کردند و پیش‌بینی می‌شود این هفته نیز تعداد عبورها در همین حدود باشد؛ به‌طوری که تا پایان امروز، شمار عبور کشتی‌ها به حدود ۲۱۵ مورد برسد. این در حالی است که پیش از آغاز جنگ، به‌طور متوسط روزانه حدود ۱۰۰ کشتی تجاری از این تنگه عبور می‌کردند.
🔴
اگرچه روند کلی فعالیت‌ها در حال بهبود است، اما بازگشت کشتی‌های تجاری بین‌المللی احتمالاً با سرعتی کمتر از ترددهای محلی و منطقه‌ای انجام می‌شود؛ زیرا بسیاری از مالکان کشتی، اجاره‌کنندگان و شرکت‌های بیمه همچنان رویکردی محتاطانه در پیش گرفته‌اند.
🔴
ابهام درباره خطر گسترش درگیری‌ها همچنان پابرجاست، به‌ویژه پس از آنکه حمله ایران به یک کشتی در هفته گذشته، عملیات تخلیه دریانوردان گرفتار در منطقه را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131656" target="_blank">📅 21:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
باراک راوید: ترامپ امروز با نتانیاهو تلفنی صحبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/131655" target="_blank">📅 21:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/En7BOMnzLTvP48ajB25RqWND0O7hmoE2PTAD9tcRM4AeqqxlEqGLNUyj5CcQ1EtTE7yabt4XofNii-TUAHafmcmfUN_dUF7DPlIHoO9HqK2igbPi4fn_yJeB3wMJSjcwXF67dSdsx2PTplHFAUv1pxA9f5FxTeWlbLZl0CNMC_dtlOORz8-LIJOtNy7MFNf9TrjMmeUJqcFkjwZxcYOKngp8Rb2sDRhfPcsKsZJ_enrTmVEUY2iUIs42Ww9Ed1Y0r-a3opTCjA2fMJCrhIceomymsiItJc_ATEcu6azlwpc8FaeA4hawogrbziXIVH4Bgt2wV5ypHHGPdM7pLdYVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@AloSport</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131654" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6feb8e70.mp4?token=JZCUOqbs7Fgo6AhT0HPiqTEWY43u8CkkwV7uZZmczyOjk6XaPdMlcapqXyowBKMyyX2qQ0x7Qzk3LxT9rnee3zAZ4KUmnxqEPzJ-P_FB79-U9mnY0hU7B7HSCV7CDIkuJmE5bQoErzPhbcZvWEiJFzA0qU3QNZsS8ybWqKc1lJvkzQGCwz5GZ_xt1rwaEwT1QRWCQvUTcnUMPchyM_vhkrR7AOvmNsOexqpjz6POU3JtzS2JXdG7wnBndZ0aQHfTf1uuMeLXYFfJnbg4HppXrIUzSOItC-9Taw3qMjmlp-EZBbAUKweRrHnCo7jGb1m9LpTtScvdIo7NDsxwFW2A2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم نمایش‌دهنده جت‌های جنگنده F-35C نیروی دریایی ایالات متحده در حال پرواز و معلق ماندن بر فراز نمایشگاه ایالتی بزرگ آمریکا به مناسبت روز ۴ جولای و ۲۵۰ سالگی آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131652" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1445c04c7c.mp4?token=ga0sJUmFhy-uG6QOA957VC0NlFJTs6jsrrJ09iBCtaqAO9OfCf08FNEZ82OJIvtDk_5e9rHc6VZS_Sh01cDTlCvd6YsJ6-37nqX0eel2arB1JFySHYYDRGqr6ZaM28llj0PHjv0bULbW6YrQoag6fs0A65Ic_QEjbbAXxFqufhPeDl0J4Qz4IM03axs3Ovl-zOpaZAeH9BwjXqtxWDn-i5VGbr21r6vKhB3RdZLEljUpacsdFj04-i_pJJGN8D3AcOaUUbGO2ux6oNdb5KEeRIDkAOt20-8G-0p-NqWrnTpjxwJAkMUupVvsG_jXz34v5rBWrYWbydV9JO_x8JMKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توکیو به مناسبت ۲۵۰ سالگی استقلال آمریکا آتیش‌بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131651" target="_blank">📅 20:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/131650" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPKqrUt4MDxIR_IFuZhTFa8yH47EvsJW3mLQOtoaeBrE_7_gdYzgUE76nMmGRk6NeGjirPlycZUc_pZxK-ubVVEZXTYLwW36rWPx5YOPWmXZ2ihTEOi2MyzdnwCpQELWaDkHUqurPVxSE0kmnpjdFt9-Am6yBrBf_m65nvnhbp5ch0g3DL6cU3o0Ltg7xJPmFp1onzP7C9kbfof80bQlVTL8P9bgTxh7NDFAnOvmx31B5hOku1EL7smoOvtub7hwPINBwmxevrm0RmJvBb6JTCTuSM7hpQnqkWGRG0dhLTtH5Uv2VpCUJwwNm4j5Q8TSLzuty8IiJcCa6mQUUAjq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست: رئیس‌جمهور سوریه یک بازیگر زن محبوب تلویزیونی عرب را برای مجلس انتقالی جدید کشور برگزیده!
🔴
رزینا لازکانی، ۳۶ ساله، به‌عنوان یکی از ۷۰ نفر منصوب‌شده احمد الشرع در مجلسی با ۲۱۰ کرسی انتخاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/131649" target="_blank">📅 20:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3767bfbca0.mp4?token=FkAW3X1DQPeAqMFkFk2iIx6HeGCd8ZYXw9gWIU_yW1Fq_3yZHSAxDwEAh3TpgVDHaJXspyDfzL9IoaGSlPBMRycCCI8YH9th0p_BcHW731VJH9rEJAuEHOnFgTN5UeSFv3l2UmJwRwR334hjBfGRoW9bPBeBq04zRiS0UJok265ZPsR2pq6z8oMLMSjtBGY2sfYWtbCegPKWF82hAJUsNCM51I1I-PnDAKzJ62zQ4PmmKcLtIh_xLleM_XZlV5X6gRV4FVV1zVp6cuD8pXGzkotFgKvSnQ0CQDxDfJ6CFqgzAw_uKJKo2AIJDPHdBC47rWO6aHs5jZnd4WrqZ58VYx58Vfv3lKiX9gHh5faceaFb00WSjh364NvNonXV1aLob3NbYikIqZk0HTRkUxcbG4xqL0B3b5GOYbP3B3vbiVZIqOBXW3d-eUqirdukjbI-p4IH20sA1MAdEhU8hT-qDYNGIMnt0TPvx8MvsZPcoJ7HOvE-7hWncr5GOtFF-LEsoZ-fy0Lz7aK8EGmHfPKgrLkDdBOkbKf9kQFwxcVkf0Mr2lPvrZwtBuuxw2HP9c-0PVLG3t_acJwS-8HbynneoNG-_cEd8PKrcezpuz7ehW6Twiky0MkKIMHJYBZuIvlKL2Ap7tWmcEQKSje8yzhjB4k2_vvkeEDOymOWj4PQSg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چتربازان و هلیکوپترهای گروه "گلدن نایت" در حال پرواز بر فراز نمایشگاه بزرگ ایالتی آمریکا در واشنگتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131645" target="_blank">📅 19:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COifDbQuOexX8hJ4QSnR6-Kmp4EjxRMMRRPKjbCm10SY3Yi8ldFXF515AyP4wZSpcTbBiAIEd7bap2rlIOijQ94F9VvZ4ZfvN9F7-VQNJ6nbNtO6TgTOkGdfXPrZxx2nN5nf4bhOXHX-hIusLyWxTy0pTzvd7XiYbaZEV1hknt8_V3Bo7UawStdJeAI4Kaha3OBXYi8tUrsWusW_vtQ-IyyXXF_bB5P-87cv-cR5OWGDWcpe0pHE2wZGzweMEWTFeWvI_NpwnskOtnVwFNBOoD4W5WYUn1XAy1-eWBrPoPag23OgvRrPjBpiux2ddT9hBnn8R5LxwE55iTOvumcOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131644" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131643" target="_blank">📅 19:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: اهمیت نداره که چه DNA تو بدنته یا چه چیزی مصرف میکنی یا عمل میکنی، وقتی به عنوان یک مرد به دنیا بیای هرگز نمیتونی تبدیل به یک‌ زن یا جنس دیگر بشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/131642" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حوثی‌ها اعلام کردند که جنگنده‌های سعودی را از حریم هوایی یمن بیرون رانده‌اند، پس از اینکه این جنگنده‌ها تلاش کردند از فرود یک هواپیمای غیرنظامی ایرانی در صنعا جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131641" target="_blank">📅 19:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eizXhXu9KW576QlhLPD5VVogKrNaARrr9ZQ6CrI2swJOJq-8jBMDs3EkwOT9E7bfvudMNXpvX5UZnKDosjTY4ZGEl4AlPTit_EuHRez8XLn4XxHV3Ile-NlnZa2DdhNnPDO7xAn21zIt8r08NfXixHTQsUOYCKtLi27N0WGBPWfQL8VMRkGEqe5sCnv52bWWGL4osR3xrGHE40xvXa1Se0sOoAwDudnUS6_lkP0XBPvlV5FFpiANefERx9jvVl9xajAIG8iyluz52srZUEF0skrP51m2MTQEmcb97gxjlL7LELxj5vaXV8Jsuz5FrYRN342-K2ucXwFx8hGTUUduvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل، گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131640" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگویی تاکید کرد که افشای درآمدهای میلیارد دلاری اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا از حوزه رمزارزها هیچ‌گونه «شائبه یا تضاد منافعی» ایجاد نمی‌کند.
🔴
بر اساس گزارش‌های مالیاتی و افشای اطلاعات مالی که اوایل هفته جاری منتشر شد، دونالد ترامپ از زمان آغاز دور دوم ریاست‌جمهوری خود، حدود ۱.۴ میلیارد دلار از فعالیت‌های تجاری مرتبط با رمزارزها درآمد کسب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131639" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/131638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
ویس لو رفته از ابویسانی، مشاور وزیر آموزش و پرورش که دانش آموزا زنگ زدن میگن بخاطر مراسم تشییع خامنه‌ای باید امتحانات عقب بیفته و در
جواب میگه خامنه‌ای و مراسمش چه مسخره بازی ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131638" target="_blank">📅 18:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emRrvHxux-g8JtfiqGDx9cONJ-dkYKs1Hnuc7_jdXADzEZEZ5WKzZDFcWaYZul0BdZUpUoRNdiwE7eSs0j3l7hYGoDi84Pi2hZoHcjJKcXHwpvKNGgbfl9iIhheOj6aGry30Y0usDcqcdcpHLKFUTJvt1LmURH0BmTzbU7IH6ooQO7mJS-4mkzSPQPHc4WwNRGC8lqY-fMB0V1daJ6xoybNg5KV5fjh02-sL8ZRo9tyqrVqL_VtRONgphdnjEr-c4EUP93mYFrJOMzeJBnPQ0Xtm_wVlxLC0urmgecuT92xdF6w_0km2RbAciC8b-zgW3ldWjN1Fqh-Q9ydicYjmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاه و تعجب عراقچی از گریه قالیباف که مورد توجه فعالان فضای مجازی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131637" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دونالد ترامپ درباره باراک اوباما:
من نمی‌دانم که آیا او یک بازیکن بسکتبال خوب است یا نه. من شخصاً شک دارم.
🔴
در واقع، ورزش مورد علاقه او گلف است. اما او به زودی در مسابقات "ماسترز" شرکت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/131636" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: رئیس‌جمهور آبراهام لینکلن از سوارکاری با اسب لذت می‌برد. من هم دوست دارم سوار اسب شوم
🔴
اما وقتی از اسب می‌افتید، من شاهد اتفاقات ناخوشایندی زیادی بوده‌ام. افتادن از اسب اتفاق خوبی نیست.
🔴
بنابراین، ما یک اسب پیر و سالخورده خواهیم داشت که بسیار کند و تنبل است، و شاید من هم سوار آن شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131635" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=F-QDgzll32hUeiFvu7IE4k9JRK27bxu-5ecktBW77pC7D6x51jyDmKtEEWj1E-eMDmoWgxuxWeFAC1pmXWC32dN1J0PGYrpMqztjfOVoLdTblZ7wW9JUKpuTOY8X0FNexpKVcrUHPXTMAhP0dZGsMWR3wtwYTs7VUZBkCLQNTxVM70u9S19YbUB8JCI6G5kyVDh2oL-1tQ09FcTbU8o5VC3_P517qF1dDWjlbtjowpSgqzEJbqmLNvUXAKSFyPfn8aZ40WpjzVWkY6PqW3_cmLPUQ3KcuNLZ_wX-vbD70IUH8DkbB1YbscGy8jSh2Ke8-_AcXn27rKHfRp5TqssPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a185ba29be.mp4?token=F-QDgzll32hUeiFvu7IE4k9JRK27bxu-5ecktBW77pC7D6x51jyDmKtEEWj1E-eMDmoWgxuxWeFAC1pmXWC32dN1J0PGYrpMqztjfOVoLdTblZ7wW9JUKpuTOY8X0FNexpKVcrUHPXTMAhP0dZGsMWR3wtwYTs7VUZBkCLQNTxVM70u9S19YbUB8JCI6G5kyVDh2oL-1tQ09FcTbU8o5VC3_P517qF1dDWjlbtjowpSgqzEJbqmLNvUXAKSFyPfn8aZ40WpjzVWkY6PqW3_cmLPUQ3KcuNLZ_wX-vbD70IUH8DkbB1YbscGy8jSh2Ke8-_AcXn27rKHfRp5TqssPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بیل کلینتون: او در واقع آدم خوبی بود. من بیل کلینتون را خیلی دوست دارم. هنوز هم همینطور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/131634" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCq4WaQcQx3QG3IAMKgi4aoVODpOdVh9gk30RIG8gRUZXcJMS2Fr3aEk_zKwxstkfBGRrFYIs73xj_03cLxNhmgkr_xtre8cpBjey1Q_yBNd8Q0Kota7dtn-xeOU6pi-cgTTXbOuDdxl4Kqsq6dm-_YnukyL3KTpSxHFoJN59MZA87PqgFqDuRQOYLX-X_McIg0LbksSYfsMFmXEVKwPrZCOTuJ6mBi1EMcgGqnDroXejtlC8d-2QWKI0Gwl262TGrDS9oXUaTYFGk9MAxn1D6b4yftuovOTmzJpUKj6aaVsz0rScHqPftfXhuKhbo1Y19Si2nPODRHJ1deRFe_WiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو این چند روز اینترنت رو قطع کتید تا دشمن سواستفاده نکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/131633" target="_blank">📅 18:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGS8nPezzPwbpynfIo85KMEgQ_kTCVRpw1dasKq0__TNQcWqW1l8Yya6F5WZm_KmuNUZgvxHvyvI3fwnHcWUDo_B9FtVIzBoFtP_d0RGHzFA8vRaAnY92ayXHuqWQ9wFc6Hn7HLk3isvDneXGhwNjyO0pMlVlZRNQnJeqTefxbpGFwBxPy9YDDlBQcpu2GZw6cRWTnPXIiFH8RsrXRXWyAXMUaPSEZY0grVHkhhbHyUFyLgPD5VWbpd9rH__jPzrs9P7eypu1Copd3qhZSt176KzSyS0twBdjy3d04WrTP7kQynuXa7jzlwQ9MBgnLsCEYGEfF_sbgFEVq6gbu--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس برآوردهای کارشناسان، هزینه جنگ ایران برای آمریکا می‌تواند تا سه برابر رقم اولیه کاخ سفید باشد؛ هزینه‌هایی که شامل جابه‌جایی تجهیزات، خسارت‌های جنگی، استقرار ناوهای هواپیمابر و سامانه‌های پدافندی، استفاده از موشک‌ها و بمب‌ها و حملات بمب‌افکن‌های B-2 می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/131632" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
🔴
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131631" target="_blank">📅 18:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Ou-kkfOmOeXaGyn_OC8tDa27F_CPdnPzWtv2oqKnueU5bvqB-fsvjUbnahczy6z2aTy29ZXBwy2xnlhHK3vmBLVrPhxVVhQjZSQCEz_T0dynt1oiN_9NzWzA9l0Ye-OK4trn49vJcateYyv00QIxArW7NAWOUppua5IbKrbHC5dswN36BLocT7eV8uRXmI0U1sWj5memAlakLbXNAjcTiDWoMnKrdyCjAFl528SHqxGGwC2y-sMujOm4_0VWB9D_SvOjbFqi0iKYukemutYsebMeXEe9SIbWGSucL7jE26wm8QimqIBQQDXMBECeWbC_zje7PXkVEdv9M8swBmoivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=Ou-kkfOmOeXaGyn_OC8tDa27F_CPdnPzWtv2oqKnueU5bvqB-fsvjUbnahczy6z2aTy29ZXBwy2xnlhHK3vmBLVrPhxVVhQjZSQCEz_T0dynt1oiN_9NzWzA9l0Ye-OK4trn49vJcateYyv00QIxArW7NAWOUppua5IbKrbHC5dswN36BLocT7eV8uRXmI0U1sWj5memAlakLbXNAjcTiDWoMnKrdyCjAFl528SHqxGGwC2y-sMujOm4_0VWB9D_SvOjbFqi0iKYukemutYsebMeXEe9SIbWGSucL7jE26wm8QimqIBQQDXMBECeWbC_zje7PXkVEdv9M8swBmoivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایا: تصاویری از حمله امریکا از خاک کویت به ایران، با موشک‌های هیمارس در زمان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/131630" target="_blank">📅 18:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ارتش باید در هر زمانی که لازم باشد، آماده انجام یک عملیات مستقل و اسرائیلی در ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/131629" target="_blank">📅 18:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی - دیپلماتیک اسلام‌آباد جواب داد؟
🔴
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131628" target="_blank">📅 17:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f227c1ee.mp4?token=NcpzDLS8xRyx0xxPatfDpUIhaGFlne3G1aQUYMbnWlLGyKuUfHM40mkO4Ot_ifa85G0FEsWoPODtv5yo1lJ6GGXavpZaT2Me8JDVXsicysv5nJdn6QGngZhGJqUwonRudFcAatjQfpyhrv13zf57D4EFO1IAlka87eZ-hjUAYuQf4jYcfie8HlkjCTk-he2LVptHTnnZMR8IfHs-RtWL3FrZ555oHmXBRJas7CwJRroHkXTAH6pKKG_42-zQi43eFYHdZ8nmOKVAyKEe_kuG-8TLGTq2DzfY_X9_pMlLPsHu9m4_KMx4DSMSmCBr3uvXRqyCQTc5xZvYrBs7Bu6PgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر وداع عاصم منیر و شهباز شریف
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/131627" target="_blank">📅 17:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu_LVWlrb0iAwDkm4TZem4vNIWu3Oj7YfeeZ-IM1HyfhmMfQzY08uBzp6A57c59DZy8J8Iv2z9MfApZjK83ODomMuRQEiIEbnU7e633YiYSpWYLe-tZ6f8AqlnYMVx74kJlLgZLUIQdc2ociIGyD04AvxfJTmGky4AMex2hXzc30Ugr8TKP5IzYwjagyw5aRmG3CHMu-3zlSxYylLCwTqhhB3hO8-jXweqAIj8rMk6b1wX4eL8gpM2rfyJDDKzbLitjoQ8UtZF0NHNm4W8Ew29q6RAW90kRo9WU9rfvhld6-1zuxfTc2hoF2wzNw4QVpTvuWQlWr6wzGTPb332P5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
به سه منبع ایرانی و غربی استناد می‌کند، ایران مذاکراتی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است، اما خریداران احتمالی به دنبال دریافت معافیت طولانی‌تری از تحریم‌های ایالات متحده و اطمینان از ایمنی تردد کشتی‌ها در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/131626" target="_blank">📅 17:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=TOSHcJ0c_3ZUAeEyKvv4WT70CzQDRfHq31ypc-_NMcIPYuLd5YGokCsNXrDIwrAEnbC2bb9XK62vtiRkBHUSIvLDcRcMXbo1HtCVLN6Emy7IaxnazNLwEs-213PtRAcFZvipwLEB8zqG4iTa1OeRNoq_NS2_17gghBWLeMcereDvzU-PTg82UaucxIOrXsd8ogS7p7T0uJ_YD-huJYjNqmNuYvyOaoodwl8tEFPk7yyg29_6MMMUJAIs56yBe9p9bIbfoWryZUN5qMjzVB14qVLIe9VPvdvBTJHC3Rz2XGMQyi6rTdss6KKhW0gQvu39TPgpEQdMLrK_8VXGeBbicw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f37b08bded.mp4?token=TOSHcJ0c_3ZUAeEyKvv4WT70CzQDRfHq31ypc-_NMcIPYuLd5YGokCsNXrDIwrAEnbC2bb9XK62vtiRkBHUSIvLDcRcMXbo1HtCVLN6Emy7IaxnazNLwEs-213PtRAcFZvipwLEB8zqG4iTa1OeRNoq_NS2_17gghBWLeMcereDvzU-PTg82UaucxIOrXsd8ogS7p7T0uJ_YD-huJYjNqmNuYvyOaoodwl8tEFPk7yyg29_6MMMUJAIs56yBe9p9bIbfoWryZUN5qMjzVB14qVLIe9VPvdvBTJHC3Rz2XGMQyi6rTdss6KKhW0gQvu39TPgpEQdMLrK_8VXGeBbicw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام دیمیتری مدودف، معاون رئیس شورای امنیت روسیه و فرستاده ویژه پوتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131625" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63e838adce.mp4?token=PH30KMGWD83z4asOzon0WMJWXCgI7Xgr-mhvgV1tbvv0PeqpxRic0x3C2KbgihMH4-Y7zsYR0G0sWlT371obu1qSji_vZQRNHvvCwreQAfb3xtXo4k1ve1-EZCDosIhh8k3WPHlFxb8EINyRBSqIPOZhPZG79d_QBnsVOH5u6hkCeBIkBS9dV6SQ7v1kTIRjjQ3BdTpwiKNyzS3aOLpKSv7dWZo8D3YtEWYcz7cC7Jsrxg2JuCaUymnnutKQmkLdHkSYxWX7SF4AGXuHgp8A-AlolS9crvmuQWhXl7mIBaPOW4Vq9BYNJvHew3TLA_l8rCThofqTHo2vx07A494R_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر آموزش عالی گوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131624" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
معاون اردوغان از سفر احتمالی رئیس جمهور ترکیه به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/131623" target="_blank">📅 17:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBoUZDzgzlLe_CvzrD7c0yFLfIMal3DMB_KVAtMxmxFbvr0sksQkQO_2pZ1ojyrTvQwVfH5SamdG91x5oMEwhig0ZZWf1z9livAE2n_TaNU4skMtKG65EQLN5IzUO043B14dRla37h_vd7edxV9iU2a2Q80XDLLSjXjumiGcf-9EbygN74ko9eTmTT41iMrDu0FBDaywWW9VHRx7xwXPVvXM7aiVHAsZQN6xijVcJCEqGWC-5Ii4xmO4_yyIMVkix22kk4MyiFD-sA_v2Qq4f_gKjhuXCD8Z0tHYmxC-bXKTQrbRwwmRb7lM1KaoBG4AGyUPLc4V6RI86WJUgKOOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز یک پرواز ماهان‌ایر جهت انتقال مقامات انصار الله به ایران وارد صنعا شده و پس از مدتی به سمت تهران بازگشت
🔴
این اولین پرواز مستقیم ایران-صنعا در حدود ۱۰ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131622" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رایزنی احتمالی OpenAI برای واگذاری ۵ درصد سهام به دولت آمریکا
🔴
به گزارش تایم، شرکت OpenAI، سازنده ChatGPT، reportedly در حال بررسی واگذاری ۵ درصد از سهام خود به دولت ایالات متحده است؛ موضوعی که می‌تواند ابعاد تازه‌ای به رابطه دولت آمریکا و صنعت هوش مصنوعی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131621" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز: ایران گفتگوهایی را برای فروش نفت به شرکت‌های ژاپنی آغاز کرده است!
🔴
خریداران احتمالی خواهان تمدید طولانی‌تر معافیت از تحریم‌های نفتی آمریکا و همچنین دریافت اطمینان درباره امن‌ بودن شرایط کشتیرانی در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/131619" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=pIRHyCmx5naPIHUGR4UdnJnp6y9LvMCKgyic8KuzdyqcnfBUfk0nBwGuaWWUH1MOKEGJid2zoWQah3xNE6fxdtzfwBuMsT8_KsKIf1k4bLJ_K5iRcRuEqfsz_ImXSqRgtdvN8b1OpOkDIH-eZyz6uezRZHZwo2Z41Ia9iiLMfQRHzQdekeDu2TEkJN-2xMUJAKmIiB7TV2Ow7XmzB4U_V3hkstnkZ13k-WzrN7Lrk8-i8Pzxd9edSYK_qi0viSy7l826HKdnqRgLBt8mm3TLfvz_q15jqZYGkNpRK4F1AqwsAXpeWuu8es07uldU1vVRulke6dYtrupA2z-HSXP8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af94fcd247.mp4?token=pIRHyCmx5naPIHUGR4UdnJnp6y9LvMCKgyic8KuzdyqcnfBUfk0nBwGuaWWUH1MOKEGJid2zoWQah3xNE6fxdtzfwBuMsT8_KsKIf1k4bLJ_K5iRcRuEqfsz_ImXSqRgtdvN8b1OpOkDIH-eZyz6uezRZHZwo2Z41Ia9iiLMfQRHzQdekeDu2TEkJN-2xMUJAKmIiB7TV2Ow7XmzB4U_V3hkstnkZ13k-WzrN7Lrk8-i8Pzxd9edSYK_qi0viSy7l826HKdnqRgLBt8mm3TLfvz_q15jqZYGkNpRK4F1AqwsAXpeWuu8es07uldU1vVRulke6dYtrupA2z-HSXP8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام وزیر کابینۀ نامبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/131618" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=aI3w7-rhI-B_9rbYIm2t3bpuFIW7zatOWOt_wju1GUgKPptEK6lTa5eI3R1l4bd5-VX9qV8bxMNgGNkVjvDa9mA_SlxI_4RkCa1aQtCJWWzELHlKMvfNWxDTVrFAOI4Jer-6LRoCZniud5SCRym5vp8uq8SGhFR9BuwJUNhRl6EKOrhNCbHewsIdWEbuz5V5gEpdT9oP-HuOJQESqXVze_ZlssBRZNFkMmZ2wY_OOJRaARvVY8oPbP6fsZHjtb7k9eLaWc0YmPIVxj1RRoaVdlvFm4ho5jaWAwM2Ou3VbWeCnXNYMS3d0v79FGbb8RzF5UtKwk6rWBjt43Ribhev4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1def7056a.mp4?token=aI3w7-rhI-B_9rbYIm2t3bpuFIW7zatOWOt_wju1GUgKPptEK6lTa5eI3R1l4bd5-VX9qV8bxMNgGNkVjvDa9mA_SlxI_4RkCa1aQtCJWWzELHlKMvfNWxDTVrFAOI4Jer-6LRoCZniud5SCRym5vp8uq8SGhFR9BuwJUNhRl6EKOrhNCbHewsIdWEbuz5V5gEpdT9oP-HuOJQESqXVze_ZlssBRZNFkMmZ2wY_OOJRaARvVY8oPbP6fsZHjtb7k9eLaWc0YmPIVxj1RRoaVdlvFm4ho5jaWAwM2Ou3VbWeCnXNYMS3d0v79FGbb8RzF5UtKwk6rWBjt43Ribhev4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیمیتری مدودف، فرستاده ویژه ولادیمیر پوتین وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/131617" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-qiS_QjvKpsJnZCKQVseSf6p-T-tKLL3aeW7o0ZtwASJ896sRX788-_hY0WL3IF2oj-wUalDj01j1ca3rMAzKLlvp-SLDS8UM53tcEr1Vc0hN2oChSpz-1qLoBWKyFt2i-DOSnqeMQWeIVFs_xxW8q6_f8Uk9j67NhR7QB2eec2RIj5I3JAnQHTkgKSYdoDRNDjS5X6wbaKKIHfJ_SHfvPw4nW-O30BIEK86dwpgUoXI5XkboswFdjg_lK6AVPR062vI9fhRND4wSmuuHBQBOBOw4NFnXNbkk7c-Zq623fFWZFvMJagXetsiortj1c92Mnx0JNXy-X6LtBLtmtF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره ناتو : برای آمریکا واقعاً مسخره‌ست که همین‌جوری توی یه رابطه یه‌طرفه بمونه
وقتی طرف مقابل هیچ متقابلی انجام نمی‌ده، اونا هیچ‌وقت موقع نیاز کنار ما نبودن!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131616" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/131615" target="_blank">📅 16:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ارتش اسرائیل:
روز گذشته به زیرساخت‌های حزب‌الله در جنوب لبنان حمله کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/131614" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzY8_1d7pWekGWA6NLSPyjymwTOW6s6J57bqz1L1B-jXG79R4QyjZYKvzMv5AYcG2nKCoCJjvWnr1h3lfZ1mSQcC2DQG-LSpfzuh2zWK85VW1JPydUjcSqOdak9ypwcylMEcQbD5aowYBH4vj9hM5XFC9BuimTUEHwDXFJ037O-Uz_DW-GuNykaRgQa6aKmywNpoM_v09Z-kWY9xTQaXqv1t56iilc-JTEZZO632sOkqeNzxvlH3VO0IUhPx-XZlU7qPL6_b6-QjunfOPghclXfNcC5QlVX_AwKiYKepJR8E4EfOk25tMxr2DBLuNBGPjnEAwAy5_5I8v5KnZ4BBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
میثاقی به اسنایدر:
ما بدون باخت و با سه مساوی از ادامه باز موندیم
🎙
اسنایدر: وقتی صعود نکنی سه تساوی با سه باخت فرقی نمیکنه
@AloSport</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131613" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7uuBtzNL2tj_UB4LbgMJPuNJwj-I_kAlSCeXbg3_K2iNpvYQ9Ko4tQiOEETIgYV_tVbol2TQscAj4th59CjY5vB_gL9MmpvdiXnlH2gh7kYZCUpEphKOd6LQtb5vQafh2mvmVHkQDZk4xiBy5Cny7u6BYBSlim0W525BvLwSSttiX1qctScmHBRlRSxJV8KK-M_LETFa3YTPcehqZQt8qC1dhXyymBP_AT7NajeQbGV-iaP2uuZmTZT7M4vZ_-PRd29wuK9X2KdgpIvxS_G9ThQ5bnBiPrdKxfSHUC7Oz7EPGoSkSxysKYg55v9soZR8buMEtGDkSRM7w8BsVt-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: پنج فروند هواپیمای بوئینگ 777 که قبلاً متعلق به شرکت هواپیمایی سعودی بودند، علی‌رغم تحریم‌ها، به شرکت ماهان ایر ایران تحویل داده شدند.
🔴
دو فروند از این هواپیماها در فرودگاه مهرآباد تهران دیده شده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131612" target="_blank">📅 15:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2SHmMKo2T-k_ldDRg1BTm9IMTFvKNln3wXq_ZPIsp6y9o-To5955ffhPZ5GYehr5NaWQB_ZIs-k9edHjfBbK97xzWJ3bmubC_74ShOL7wszj6hxIeNqpLlD5Hg3L0diqjUgSW6H3vGHCboW8vDlBB1SvMblBBJ5J2E9czzMRWHK9P4FOC2_4_HxOqg6W75wqaVBDIpbksXvJrjMcaZaBHS8lr9Hio8zQflBv9edQZnw64dB1W5gGSHlUd3E_T5njw2kh-IOs-i9A8BwL8PfivKqj51CAr9Tj_1pQ9d3C6meRRom3h3w-ZQ6WQAVsJqOZ3Wn1Poughvmu8WCdYE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش آشنا به نبویان: راست می‌گویی در حدی نیستی که از بالا تذکر بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131611" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=GS6MsbRGOT2M1Q5TZFF0_rhIoluB6ybiwFl9oB8bZZABogNS5VnQwZHMn1aLd02-HRorfqSytu-02Ib55_u9gOD5Aetft7gFjE1dZM9BIDdUfR2MVK31UNvLe5riMkc4K1tgd2Y0bnFNv5OMajXuY-cCwZUEvOiyUH1k8TCEd0I-JsS37FPTcpZ_LYy52S3CadHFWPOXG-J-8fY4j9myDbU2rLUMsh22daOzikK79CatCkqrGIsMXDh6pxusbJK8GSQK6kP9QC8SpuxKm-9uNl_3t96MjNJdCOAAfGJEnsVpgS7Pb8FVpHhOkXbJbHRKS4f02nswgU57Uuty-206pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=GS6MsbRGOT2M1Q5TZFF0_rhIoluB6ybiwFl9oB8bZZABogNS5VnQwZHMn1aLd02-HRorfqSytu-02Ib55_u9gOD5Aetft7gFjE1dZM9BIDdUfR2MVK31UNvLe5riMkc4K1tgd2Y0bnFNv5OMajXuY-cCwZUEvOiyUH1k8TCEd0I-JsS37FPTcpZ_LYy52S3CadHFWPOXG-J-8fY4j9myDbU2rLUMsh22daOzikK79CatCkqrGIsMXDh6pxusbJK8GSQK6kP9QC8SpuxKm-9uNl_3t96MjNJdCOAAfGJEnsVpgS7Pb8FVpHhOkXbJbHRKS4f02nswgU57Uuty-206pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده ای از مردم هند در راه ایران برای شرکت در مراسم خاکسپاری سید علی خامنه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/131610" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac7N7Bd7LH-HjwT373e1--HxBs0JoYoQScj7NenRinjwfl417ZBQ3qwJfly0gBr1LkOW7Q7GUoh9egNux5f9LN2-jxJOzxKNT1kAQRirJjS61yuTPTo2Z6pTrXUCmeDk3iQgf9k8G7Ck-Nzl4JHyv99NOa5Ivc-H61tMG3U2cOHP1iAGEqlYTTqL995eyOlRY8OsrLdGCEqFNTy5SRXRIkkmmRDc33sTjMeEkS9VVCoLluCokzgcrU289rWo-RLywO37RvzHuQvHhVf98Fs_o2LfqOzEQxZDAVZCky5u5eQiLbmuCcWbw9_KGt5YH9DPgPhkq9I-1IE9OpRe_VtX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهره خوشحال پزشکیان در استقبال از مقامات کشورها با انتقاد حامیان حکومت روبرو شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131609" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
احتمال گسترش بیماری‌های عفونی و آلودگی آب‌های زیرسطحی با برپایی تعداد زیادی توالت در سراسر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/131608" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: اگر حین مذاکره تخلفی و نقضی را از آمریکایی‌ها و افراد مذاکره کننده در طرف مقابل‌مان ببینیم، در میدان به آنها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131607" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
واشنگتن پست: اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
🔴
واشنگتن پست مدعی شد: مقام‌های آمریکایی اخیرا فاش کرده‌اند، واشنگتن طرح‌های از پیش‌تدوین‌شده اسرائیل برای ترور عباس عراقچی، وزیر خارجه ایران، و محمدباقر قالیباف، رئیس مجلس، را خنثی کرده است.
🔴
این اطلاعات همچنین اختلافات و شکاف آشکار واشنگتن و تل‌آویو درباره اهداف جنگ علیه ایران را برجسته ساخته و نشان داد که اسرائیل به دنبال سرنگونی نظام ایران و براندازی آن بوده است.
🔴
طبق گفته مقام‌های آمریکایی مطلع به روزنامه «واشنگتن پست» دولت آمریکا خیلی زود به این جمع‌بندی رسید که این هدف از طریق جنگ، قابل تحقق نیست و بنابراین تمرکز خود را بر هدف قرار دادن توانمندی‌های نظامی ایران و ناوگان دریایی این کشور گذاشت.
🔴
نقطه عطف، ترور لاریجانی بود؛ در حالی که واشنگتن به دنبال فردی در ایران بود که بتوان با او وارد تعامل شد و ناگهان چنین فردی دیگر وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131606" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / آغاز درگیری ها در یمن!
🔴
گزارش ها از پرواز جت های جنگی عربستان بر فراز آسمان صنعا، پایتخت حوثی ها و بمباران مواضع حوثی ها در نقاطی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/131605" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تحلیلگر عرب در حوزه ایران و پژوهشگر ارشد مرکز مطالعات الجزیره: آماده‌سازی‌ها برای آغاز نشست‌های سطح بالا میان ایران و تعدادی از کشور‌های شورای همکاری خلیج فارس و عراق
🔴
این نشست‌ها طی چند هفته آینده آغاز خواهد شد
🔴
هدف از این نشست‌ها ایجاد سازوکار‌های امنیتی و نظامی است که منافع مشترک را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131604" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خروج بیشتر نیروهای آمریکا از عملیات ضد داعش در نیجریه
🔴
به گزارش جروزالم‌پست، فرمانده فرماندهی آمریکا در آفریقا اعلام کرد که واشنگتن بیشتر نیروهای مستقرشده برای عملیات اخیر علیه داعش در نیجریه را خارج کرده و اکنون به درخواست ابوجا، پشتیبانی اطلاعاتی ارائه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/131603" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcQCR4ETnTcRDX6CoH2MpzEua9xs1QguPQcZj-B6Cdj_T57YIFiYab9oHIaBx9eziwuRDNLxIWzju92Y88pTIJnKW4QKXj-xnUYA6HJUFpCzN_LdFnFhIdhZmxj9PCvoBahuMafBk0ix0vrCFMG5_d5sGApHnx5cNxfuFZpdqzyS5PLNDIu2vlfffpK-TU962oGCZSUVJmtKM7eNA2F72IpjlwkJoFcc_SivDLN8nk1uIDRznljoEv0XY_UdMticT96n6wg12z4uCjzTgdOVH2FUvq1gUAzXczIbUPWCDrwXk54Fni9AqytibFKugSagkZHMdH2-bhpmiyPxDYrDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYyPZYY2RPKsgTgFaKcdGt7DNVpKxr44ZMLXlWLNwg9z3r87LOdY0wxtPZTDClnlwZtKk5qmVFrHd3cGSOJyOzj0I4JT8ME-uiyVeZylxNlhu3Bqio0b-HRuuvz0eKExZUF1mQca8u29gbNXNJW-Zg4Fc3mecpaspGl3u9niZSjB9FpF8TtGTlrrQ_O0dP86d7xlT6yoG_4OGlGeSEKsRKVM2EyQVOFVaqjexe7bxVhkk4269y-zYKwi4s1V-Ebzv_E-RZrMNy1IfOWR46eusADCnKnzNuL8kDo9hRndISyqSbJmds9fpU02k-E7sb-sWMHSVCypz2Ib_BJMJ7VeQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجله اکونومیست حدود یک سال قبل یک تصویر داد بیرون که اتفاقات آینده رو پیش بینی کرده و دونه دونه داره پیش میاد
نکته اینه مجسمه دست خامنه‌ای هم تو مجله اومده بود
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/131601" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131599" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/131598" target="_blank">📅 14:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=o9vQqmn_l-YV9TuI2Q6pe0zQ_hwu5I7E3YypUOeXJeub4_XAXnD7DUqP72u490SB4SengJyfjU6G9gL3snJodg3gts6gH4mFEncRyqd0SCZ3-M06AGonEAe3CXr_fmvvXbP5Rm_7Ih1n57_AeKyUO9dGTz09U_LKbVEnrfiCpfVDlbKWb3ILtHZv5VzLvV7o2TgcFNMnwK7KJM0ZtRp9ogRnUfZz0r9WezTtm88d3VxGnoToO7ZLUTT8FxHu7drbBNZH2zBScO7SY4eabajlXHX9oSikcfAQuVGm1924CX-kj9Bl8D2AsnWTiTUY7ExVNgd6LBVZ0zXvc9ZBXh8PUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=o9vQqmn_l-YV9TuI2Q6pe0zQ_hwu5I7E3YypUOeXJeub4_XAXnD7DUqP72u490SB4SengJyfjU6G9gL3snJodg3gts6gH4mFEncRyqd0SCZ3-M06AGonEAe3CXr_fmvvXbP5Rm_7Ih1n57_AeKyUO9dGTz09U_LKbVEnrfiCpfVDlbKWb3ILtHZv5VzLvV7o2TgcFNMnwK7KJM0ZtRp9ogRnUfZz0r9WezTtm88d3VxGnoToO7ZLUTT8FxHu7drbBNZH2zBScO7SY4eabajlXHX9oSikcfAQuVGm1924CX-kj9Bl8D2AsnWTiTUY7ExVNgd6LBVZ0zXvc9ZBXh8PUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه پزشکیان، قالیباف و محسن رضایی در مراسم تشییع جنازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131597" target="_blank">📅 14:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چندصد تن برنج
🔴
چندصد تن گوشت
🔴
چندصد تن مرغ
🔴
چندصد تن حبوبات
🔴
چندصد تن از همه چیز
👈
فقط برای یک مراسم خاکسپاری از پول بیت المال هزینه میشه
🔴
اونوقت به مردم میرسه میگن کمبود داریم و گرون شده و نخورید بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131596" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی ۶.۲ ریشتر سواحل شرق اندونزی رو لرزوند - USGS
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/131595" target="_blank">📅 13:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=WSONEB97xG-pb-rlpHjaeaUiMniU0rkCO_PUg7vtKu3LoiHeGdW-iR55ddOueZ1hi2O2UnCV47LupmybuFBcafo-fmNje3yYt9zINj1LrqmhvTerXAIoGAWVwl9dkN2kU-EpJnDhOzxH-2pEvzLFdOpTINqqsgtTLIlr30_iFsWiolBbACFfnP4_TT4S7S5cQWGEigK8AKPoVgtDnVKKn1W-9hepAtA3CYgdL0QAXaW2TSZIdLnWdALKWrgNyNTWv_H17OIz_4i4gKcwtHNhogNpV-IDKwN7bnpA04PbCU4jInmV6NZlFdp3gG9SguRssfpLzZSYgf0cCZtSM4sVTpoJGjTEvmhXxdOvKVv__cZiNSLEWXOiOG52ACGexy8_d_XDcUCr5xvaz9RvYHXO0Wx7OUK_ZO5ivAbNho-OMtbX1uFlaxWr3EaOnr9QcN0GgbEMHQqSRebTdDLQCeCqXJ5q1b0D01bn5JnMxisKWOuK1ywwGqRYOfeQyJBIUopQb2ITDr0i7SSyLzE3QkDNCE43epb_CtbKEV7NTpT-sGuX3RBO-e7tHQGfGAvZeYRzRktjdIDFBI7_2ZLdXZvudOLksBodfZU8kF2uVojYotknTlqXRfqoWmaeCTbh6qaZptAJO-46luKNOUdplRC61p5MpnyrHUTFCFRsHtcltpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=WSONEB97xG-pb-rlpHjaeaUiMniU0rkCO_PUg7vtKu3LoiHeGdW-iR55ddOueZ1hi2O2UnCV47LupmybuFBcafo-fmNje3yYt9zINj1LrqmhvTerXAIoGAWVwl9dkN2kU-EpJnDhOzxH-2pEvzLFdOpTINqqsgtTLIlr30_iFsWiolBbACFfnP4_TT4S7S5cQWGEigK8AKPoVgtDnVKKn1W-9hepAtA3CYgdL0QAXaW2TSZIdLnWdALKWrgNyNTWv_H17OIz_4i4gKcwtHNhogNpV-IDKwN7bnpA04PbCU4jInmV6NZlFdp3gG9SguRssfpLzZSYgf0cCZtSM4sVTpoJGjTEvmhXxdOvKVv__cZiNSLEWXOiOG52ACGexy8_d_XDcUCr5xvaz9RvYHXO0Wx7OUK_ZO5ivAbNho-OMtbX1uFlaxWr3EaOnr9QcN0GgbEMHQqSRebTdDLQCeCqXJ5q1b0D01bn5JnMxisKWOuK1ywwGqRYOfeQyJBIUopQb2ITDr0i7SSyLzE3QkDNCE43epb_CtbKEV7NTpT-sGuX3RBO-e7tHQGfGAvZeYRzRktjdIDFBI7_2ZLdXZvudOLksBodfZU8kF2uVojYotknTlqXRfqoWmaeCTbh6qaZptAJO-46luKNOUdplRC61p5MpnyrHUTFCFRsHtcltpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۲۴ میلیارد دلار منابع بلوکه‌شده در قطر و چند کشور، به‌زودی به‌صورت نقد و تهاتر آزاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131594" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پزشکیان: ایران همواره خواهان روابطی مبتنی بر حسن همجواری، احترام متقابل و منافع مشترک با کشور‌های منطقه است
🔴
انتظار می‌رود هیچ کشوری اجازه ندهد قلمرو، امکانات یا ظرفیت‌هایش در اختیار متجاوزان برای اقدام علیه ملت و حاکمیت ایران قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131593" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
به گزارش جروزالم‌پست، محمدباقر قالیباف، رئیس مجلس ایران، در دیدار با مقامات چینی اعلام کرد که تهران و مسقط درباره تنظیم تردد در تنگه هرمز به توافق رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/131592" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131591">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131591" target="_blank">📅 13:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دلار هم اکنون 175,700 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/131590" target="_blank">📅 13:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=Bfsedvv_l-l6U59Wqu_KEO2pEU-sSwnqSDSoQFJzJ3g-7oWcgA3f4i_KKiObGMI45AsCQ5_2Rw-AOgmjlIvmVos9_Ws16ne1-06ul2xIbCFvkNV74pzd1W61yrc2kZJDea1-092y7lVn9N2Iny9rXR0hR5xmPX_5xQMHCJdNshB8FRfCMHxrxGHL4KERUz1mFBwk_n93tfjwcdBe6DI6SVWCjbjcUorrjAEpr7FXaDPRuv7aIACCK-A2P7Hfv56s-afa-Uodlqyrfs51-l4tgPxfAdHb2VyJOqpWzDvCVxHqG70B2B2fgzfN_Mwg528zhnTb5UtRTzV4BNU4kgrljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=Bfsedvv_l-l6U59Wqu_KEO2pEU-sSwnqSDSoQFJzJ3g-7oWcgA3f4i_KKiObGMI45AsCQ5_2Rw-AOgmjlIvmVos9_Ws16ne1-06ul2xIbCFvkNV74pzd1W61yrc2kZJDea1-092y7lVn9N2Iny9rXR0hR5xmPX_5xQMHCJdNshB8FRfCMHxrxGHL4KERUz1mFBwk_n93tfjwcdBe6DI6SVWCjbjcUorrjAEpr7FXaDPRuv7aIACCK-A2P7Hfv56s-afa-Uodlqyrfs51-l4tgPxfAdHb2VyJOqpWzDvCVxHqG70B2B2fgzfN_Mwg528zhnTb5UtRTzV4BNU4kgrljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارتش پاکستان با استقبال وزیر کشور و سرپرست وزارت دفاع وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131589" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
امارات : یه حمله سایبری به نهاد مالی‌مون رو خنثی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131588" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=d5mWEvTXaR7bgPQNjGl_HOSy7u7pid_4QRFms0CQHtDJG2O55x7bVhoT_ARAbn06xpY5YCoWw4LzVw-kZ2LhlhC9h5_5og1Ia6e-bMKQMtp3b8kzTXZILp1G1GN1dwJjiuEeJDXk15dm_nCl-Kp3-sMxN6UtofMaj7IkdODCgpYXHVCMwdsEwnE9oGOgudsY-hU4EteTiBk8SmFiZHOyM3nB_wC4RXocPudK-TjLuoU4ZgGCHcO9BBMwmit9XOt-tngFfshDXWHO0cIxUsK246KN-Hpie84jPz0Z_Y_IVAqCD2kjWnM6qzZaVbN2XsSKKvz9q3g8gWRTDGjndktpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=d5mWEvTXaR7bgPQNjGl_HOSy7u7pid_4QRFms0CQHtDJG2O55x7bVhoT_ARAbn06xpY5YCoWw4LzVw-kZ2LhlhC9h5_5og1Ia6e-bMKQMtp3b8kzTXZILp1G1GN1dwJjiuEeJDXk15dm_nCl-Kp3-sMxN6UtofMaj7IkdODCgpYXHVCMwdsEwnE9oGOgudsY-hU4EteTiBk8SmFiZHOyM3nB_wC4RXocPudK-TjLuoU4ZgGCHcO9BBMwmit9XOt-tngFfshDXWHO0cIxUsK246KN-Hpie84jPz0Z_Y_IVAqCD2kjWnM6qzZaVbN2XsSKKvz9q3g8gWRTDGjndktpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
دیدار رئیس‌جمهور گرجستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131587" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: انتظار می‌رود «اسرائیل» برای مدت طولانی در منطقهٔ امنیتی باقی بماند و این منطقه همچنان یک میدان نبرد فعال باشد؛ اما این بار با اجازه و موافقت دولت لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/131585" target="_blank">📅 12:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شرکت آمازون سرانجام به تعداد ماهواره کافی برای راه‌اندازی سرویس اینترنت ماهواره‌ای خود موسوم به لئو(Leo) رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131584" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
گروسی: درخواست دسترسی به تاسیاست هسته‌ای ایران را ارائه داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131583" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
🔴
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/131582" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emp5sCTpNo7XzhsLkUd_h2CkdEuXzn6Bu7WC6YOed1pbx27A_byPkdrGMnHFH9kT8j9dtF-ak96t7vCeZmqb8mrxbzCVQFUr6lbGVy1UbZ8c7LsK7ti1YqXwocXJIZR5ITvMyuPU5yk9N_b76Ewy4mlbNh0s36xdIDbLPHpkKMcVp_R2fl3_wKNQASVQAJlcKpfgA3r6ZDWUmoTHW46f3RU_iszj_TcJaQGzeSY_xQ1JnTm1_x8Qgl7uYvVFo1n5ltYxKPT0nxKLO-yylplVcJfSu0Wv55jU5xEf-7rzbL2lmNac95PhD-lSej8A6ONOWMuGwKUe5gCxqMVhY29Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
15 سال پیش در چنین روزی؛ احمدی‌نژاد: به هر خانواده ۱۰۰۰ متر زمین می‌دهیم
🔴
مردم بروند ۱۰۰ مترش را خانه بسازند و در بقیه زمین فضای سبز درست کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/131581" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=jhrBY3B9q2Be6OezRg_icYdZKFiekW1A7i6Rz6vEEZeOQUQX1pHF-qqmIKQRjN16cjF1Dag404nAkKCSBQMKEuz5Vh6VN2zst11oGKDHzAAbFJ7ktpwQ07k4IQWaX3wf1AP74hXQ6eEnn9CuCVLQ41mofsb03P9eR8APH2p6hOXC7TOYGWQ6oYmmHVR8sy2Ti98y3yoGsm70H3Jn4yItc8dYb0s7_95VtLHnC0A9iwDATaUQEBhqhilkeS8AqpF20Y0sWGI7BVKLrA6TcBGR0Tq_x_lCH5-LEfnN2cTyfonVFnUCy2l8tJ9dl_kybJMq_snOiXimaMPbJZXMK3i6tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=jhrBY3B9q2Be6OezRg_icYdZKFiekW1A7i6Rz6vEEZeOQUQX1pHF-qqmIKQRjN16cjF1Dag404nAkKCSBQMKEuz5Vh6VN2zst11oGKDHzAAbFJ7ktpwQ07k4IQWaX3wf1AP74hXQ6eEnn9CuCVLQ41mofsb03P9eR8APH2p6hOXC7TOYGWQ6oYmmHVR8sy2Ti98y3yoGsm70H3Jn4yItc8dYb0s7_95VtLHnC0A9iwDATaUQEBhqhilkeS8AqpF20Y0sWGI7BVKLrA6TcBGR0Tq_x_lCH5-LEfnN2cTyfonVFnUCy2l8tJ9dl_kybJMq_snOiXimaMPbJZXMK3i6tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور عراق با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131580" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قالیباف: آمریکا و اسرائیل به تعهدات خود عمل نکنند، اقدامات متناسب خود را از سر میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/131579" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmhcBlZFeDdBlmYhxiEXQ0J_-KpOI-JysnaFcv7gJH7xS9j5x_77Aq8bNLWRPDmKTu2OIPhNzKowH8KnWU6WgmJFdmgOxaOSsZZ97kteyHS0nIRByesPXDKmeCZN-iZN7-_LP0zPQLjdwAA1F3jz3jAUl1slnG7eI4kvzhgtreYx8nCMy-x4W-CsuobstrUk9Nkse9-wBGOaM9epZ1qPp7YDzbtCSCcmqZkYow2htta5n8aeobrEH78ECdrTfNiQvLwMY5XOZMnCtezUnFhnSO8KTwsK0yz543mqZqf2A6QmGTMrNlkMphreSy590ANDS0GLU9OU4OAsqVwqYOUvHVKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmhcBlZFeDdBlmYhxiEXQ0J_-KpOI-JysnaFcv7gJH7xS9j5x_77Aq8bNLWRPDmKTu2OIPhNzKowH8KnWU6WgmJFdmgOxaOSsZZ97kteyHS0nIRByesPXDKmeCZN-iZN7-_LP0zPQLjdwAA1F3jz3jAUl1slnG7eI4kvzhgtreYx8nCMy-x4W-CsuobstrUk9Nkse9-wBGOaM9epZ1qPp7YDzbtCSCcmqZkYow2htta5n8aeobrEH78ECdrTfNiQvLwMY5XOZMnCtezUnFhnSO8KTwsK0yz543mqZqf2A6QmGTMrNlkMphreSy590ANDS0GLU9OU4OAsqVwqYOUvHVKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور تاجیکستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/131578" target="_blank">📅 12:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس مجلس عراق با قالیباف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/131577" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq_XQ4wOBU6qT1JHZimRkGg7KlvRuDpSFIZ103k1IBqZiMi9-xRlBqDJS241_0G-BPXpHYyu4dQ0dI337gxftRstdjBPYJGtkcLHtsWJD799wCTyuGRq6WdBhZR3ErioDnWq8-fBWl_a3ALzSy-DYHkXsz521yQnkv1tNmq9PCkIjh8-maIU0WKgpBl9vzRMcJ53X8fDKcBUvHuMD2B5orbAqxiV6t-fOfVDjy1yfBN8AM6jedRJdWxNHXGpW2vslOZFmYXeL4dlHiz2Yp55qCPtjeKV2JoZ-HzoWNNJ6UFm7CGN3Ovj719etbwen6Qt8gJpKWwPNIRAu4MR9ASnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس حوزه انرژی: با روند فعلی تنگه هرمز، آمریکا به زودی عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/131576" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: فضای هوایی تهران دوشنبه به طور کامل بسته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/131575" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
