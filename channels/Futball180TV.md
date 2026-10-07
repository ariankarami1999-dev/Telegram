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
<img src="https://cdn5.telesco.pe/file/CBhBu_JPh70SSe_q3tj9nA8r4BprJ77OFkfgr3vpDbZcSl6K8HEMx6-hogzVkvcZP08XG1wr0qykUTSd8JqpqcaJf3wi3iM78jyFFpx6_bPp022x7Pi5YfsFCXn8XEmC7t3sU9m6S20FT425TGgGOI0uVuHHxKsEoYh-gxwnr6dLS-sACzyfpBnbIwmKE1M7tooYXnpAOvo5rfmjH5ccYKIvuEqgXJZfsNdQPT6S2UfCKXsPiKnwm6mWbR9UyqFdd6aiIqLuiLGtjjxJF0JOXBxGdNsui-iJDRnLFJU0-SEenTfOSPKryXbrP2dCsNWJBX9Vrc4YJEtHBmH_wk14qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 389K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-108032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🥹
لیونل اسکالونی: "اون «جذبه» یا هاله‌ای که داره. من تو تمام عمرم چنین چیزی رو تو هیچ‌کس ندیدم. اون شور و حسی که مسی ایجاد می‌کنه رو تو هیچ‌کس دیگه‌ای ندیدم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/Futball180TV/108032" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌ویژه ابوطالب به قشر دانشجویان عزیز
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/108031" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«یه روزنامه از ۵۴ سال پیش…
تیترهاش حسابی آدمو به فکر می‌بره!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/108030" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmE41YSpFjO26sF25YbSmdAcvo2kMauVi9gnlKS3U8-ZgIWlHZGsLmXvaHgfAjNhkvvfigwic-bMtM2lt_pIOe-KGP4ZaZN_Q0XaxdJhOgpXKkcv4h0D8bl9AjvIawtnSTISrW6qkopmaFZLXxOP37bS86hPmXDRqiXPpGzSoWslPHnvmPimU1wLJgIPGAyae43shP37ysYJsmcYXVD5IAiF2iHTcSr3eueT74KM7bmvhulUHGOt26jxC8WXkfWos-RhGz2ZwR_asU0X7aVzqqEawGAeiyDjO05a4plDKoaaWzzQHsoNXGk5fhGrNOrFm-t7TVZRw15XirpkawtpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
تمام 126 گل ملی لیونل مسی به تفکیک هر کشور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/108029" target="_blank">📅 19:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اهدای تابلو فرش به صالح‌حردانی توسط تبریزی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/108028" target="_blank">📅 18:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
🇮🇷
استقبال گرم وصمیمی مردم تبریز از اعضای باشگاه استقلال در هنگام ورود به این شهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108027" target="_blank">📅 18:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108026">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
🎙
چرا او آقای خاص است؟⁣ وسلی اسنایدار در مصاحبه اخیر خود با ذکر یک مثال به این سوال جواب داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/108026" target="_blank">📅 18:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🔴
دریاچه ارومیه پس از نخستین باران پاییزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/108025" target="_blank">📅 18:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
حماسه ای دیگر از آقا جواد؛ آموزش زبان اسپانیایی با لهجه ایتالیایی‌فارسی توسط جواد خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/108024" target="_blank">📅 18:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewe4a4PkkAtYLJJnNd4j5ywvujW3JRJgnsgD96tiffHndaAYUbdL1rWXT-cZEpwp7XNZVKzqo7F5XDZ0kUZdW_08e9pinafaMblVYSgTPWM4leOaY3YQhluHqL8KYGEqvpaAQCemWUo0twGk_9m7588pOdC-JStpzdp9u9Djatb6wTUSnld1fd5T5Cb1Nd7MxtMN-p80-I0jBg7ZehBIgh40vVxriwjX00-3ka4VtuOQkvbjqix3KnMpCjKdWfyS9UEmZR3U0EkZFn9KNX6-_vGF4jz5gA3IEj3gd7iOEweirYdFkQsA7qpKlFXm7yGOea9hyBcyADSxKRbZvON2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🎙
لوکا مودریچ درباره مسی:
لئو کار فوق‌العاده‌ای با تیم ملی انجام داده؛ او جام جهانی رو که می‌خواست برد و یکی از بهترین بازیکنان جهانه.
تماشای بازی او لذت‌بخش بود هرچند که هم در سطح ملی و هم در رئال مادرید، مقابل او سختی زیادی کشیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/108023" target="_blank">📅 17:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خواهر تتلو شایعه عفو او را تکذیب کرد
خواهر امیر مقصودلو در ویدیویی اعلام کرد خبر‌ ادعایی مرتبط با عفو تتلو، صحت ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/108022" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108021">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108021" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/108021" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVp2nv51IYLy6HSHqPFmvcn_jZfsAq7yHX4jqUR3B5ioGIyRzIPTgWa-rMYURh9ejDkTTDuLnNvVQXmWx7Woy2ZuWp0c2LFr2cwiZYuN7SLl1m3-YuEmh_N7mh4TNLBOEokeJAfN6Ji8yno38LmM-jIoHAxZuA5k7B9biUV4OocFsQOgvcNSQSEwanUTryxNWjlRY2cY8o0tcI1nKQYoDfc9YNP_kjsUKa_GO2mCjcnUc1who4CVaDl765120nua7hy-L8OPYF486Afbt0WZrRjp-3MFLnvpdhvpcj2tmJlss7GcMZD7OnCKBJtCNfMRBBaLU1XqA6AsSm5IjO_CTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/Futball180TV/108020" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه دیره! خیلی دیر جناب ماله‌کش اعظم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/108019" target="_blank">📅 17:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922b32f940.mp4?token=Bsn4W9sWqabpA7EzLmn_i-BjBZJg_y8BhRaYWdPWiDW7qrVhSddw3Lh1xIBRudNo2v-6KQqR2IzUCuKolg7UUo7dckyMDWGZRcuWMuks85bxEMLSK8DceG-HD94I_AtgR8yY8x9A_y5dCGXbulbebaY293I5kGTDuJeevLePi0RjnAs6tv1p9cWzz7o7-yNQ5vQaNJv3q1onbF5bL36yWAXTXgTCvQk_xeZcHEyKGmsOP2HksIgpXsSpTuh3K5aUCLrI6pMxYShKe-OSBf2h4-BCJ2JvuQNc-9DtFI6L2a3UgopMHw1r3AGIxUZCyNuNceG9hcPVfHE74up5MOYvKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922b32f940.mp4?token=Bsn4W9sWqabpA7EzLmn_i-BjBZJg_y8BhRaYWdPWiDW7qrVhSddw3Lh1xIBRudNo2v-6KQqR2IzUCuKolg7UUo7dckyMDWGZRcuWMuks85bxEMLSK8DceG-HD94I_AtgR8yY8x9A_y5dCGXbulbebaY293I5kGTDuJeevLePi0RjnAs6tv1p9cWzz7o7-yNQ5vQaNJv3q1onbF5bL36yWAXTXgTCvQk_xeZcHEyKGmsOP2HksIgpXsSpTuh3K5aUCLrI6pMxYShKe-OSBf2h4-BCJ2JvuQNc-9DtFI6L2a3UgopMHw1r3AGIxUZCyNuNceG9hcPVfHE74up5MOYvKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
کنایه امیر ژوله به لغو بازی با گینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/108018" target="_blank">📅 16:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=UpRwikS1U6RbMzVdxK0TPpm_CWwnXKQcDZJwB9ma46XBkRYuUvZS-4L2XjMY3uT0DQqbrUw2f6rY_mWq5qbDnfAzpjIJic_3o91QweXhmFFtVrTpclSE7Emlom2XBxwagjW1J47JDd22Jqk13ovtGF4IaO42RNjYOOGSQEv2ZmXb5V5a4aGiYRKbY65J-peOvr-0j1yanYxq0ProHwkmgkj9Qm_m6lbWtxei9u_k0VAlxzw9nyUzItTG7goWNNZoV9tdsOQiAcWEx2VEVYYuMV195GrR8QZpp080C_5HmL_YUsvNF2KjCKKew1Z9gE-luMFA6rKjrPKl7-cfGRAmbyIoHp1NwR-QNz98U2FQ8JQWMPcxHriGOABcUw3DHqRuZ_he0xMTETmLpehoHJbJXvauKmqLO-fbIw0OIjyqDd_W7GOUqlos2dO33QTLWpfL8p8BrjpQl1JiQ3CzjrTpwvjD5QflA2lDKQUOJbvZLXkc2S1fkpyakNEqtmlUgHaTGL9capedOG_Nr9KMDzWK7J6QASluhi1QaxfpxhT07JJGFKjwI4E3F4rm5zqZ1SXL_zYweVKJmjvsJBl5ANzS_-CKVr0OpSsteAwmGJ7WIrQDt9-quoWntX5vKWfvaSZnP4IwwAKcclas6WeMJ-gWNccteNIEu_zE5jRGDcIoQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=UpRwikS1U6RbMzVdxK0TPpm_CWwnXKQcDZJwB9ma46XBkRYuUvZS-4L2XjMY3uT0DQqbrUw2f6rY_mWq5qbDnfAzpjIJic_3o91QweXhmFFtVrTpclSE7Emlom2XBxwagjW1J47JDd22Jqk13ovtGF4IaO42RNjYOOGSQEv2ZmXb5V5a4aGiYRKbY65J-peOvr-0j1yanYxq0ProHwkmgkj9Qm_m6lbWtxei9u_k0VAlxzw9nyUzItTG7goWNNZoV9tdsOQiAcWEx2VEVYYuMV195GrR8QZpp080C_5HmL_YUsvNF2KjCKKew1Z9gE-luMFA6rKjrPKl7-cfGRAmbyIoHp1NwR-QNz98U2FQ8JQWMPcxHriGOABcUw3DHqRuZ_he0xMTETmLpehoHJbJXvauKmqLO-fbIw0OIjyqDd_W7GOUqlos2dO33QTLWpfL8p8BrjpQl1JiQ3CzjrTpwvjD5QflA2lDKQUOJbvZLXkc2S1fkpyakNEqtmlUgHaTGL9capedOG_Nr9KMDzWK7J6QASluhi1QaxfpxhT07JJGFKjwI4E3F4rm5zqZ1SXL_zYweVKJmjvsJBl5ANzS_-CKVr0OpSsteAwmGJ7WIrQDt9-quoWntX5vKWfvaSZnP4IwwAKcclas6WeMJ-gWNccteNIEu_zE5jRGDcIoQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇹
اینتر تحت هدایت کریستین کیبو با تاکتیک خاص خودش یکی از پرس گریزترین تیم‌های اروپاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108017" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=Fuy2Qu7iJGv9vSvii8Oh3RhtrANwSfLKBCvWqrpufVQcF7EXMrlh8Mh7MvrbPcadWz5mxjKNnGkMoKIk72FanOyoaoaWQMonHmbqjYY8BzqIXzoBihhr6afGQ3CZt3AwCYPE7xZqMTqjZAbp09aExRs9kguh8kVNLptJXx1qaucMsPwgRPecJ9BGja0dSShjLfOeStsE4FxbTC0jij2P6ZmTneH_FTAjcEgqINhWb07Q382pnYclkxm5tsKKYKJpuPnKgXL6rG2YeQ8JdSAm0N0xqFpgBV3-AFhvry4C5x9-y25aIzMNyGEDPvNl3bvRW__OCXr_UahoVsT_JypXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=Fuy2Qu7iJGv9vSvii8Oh3RhtrANwSfLKBCvWqrpufVQcF7EXMrlh8Mh7MvrbPcadWz5mxjKNnGkMoKIk72FanOyoaoaWQMonHmbqjYY8BzqIXzoBihhr6afGQ3CZt3AwCYPE7xZqMTqjZAbp09aExRs9kguh8kVNLptJXx1qaucMsPwgRPecJ9BGja0dSShjLfOeStsE4FxbTC0jij2P6ZmTneH_FTAjcEgqINhWb07Q382pnYclkxm5tsKKYKJpuPnKgXL6rG2YeQ8JdSAm0N0xqFpgBV3-AFhvry4C5x9-y25aIzMNyGEDPvNl3bvRW__OCXr_UahoVsT_JypXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سامسونگ از اپل گرونتر شده!
🤦🏻‍♂️
یکی هوش مصنوعی رو از مردم بگیره، رم یجوری گرون شده که شرکت تولید کنندش به خودش هم رحم نمیکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108016" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=EQ7-mLP46DvNn-9DwA2uloqiwHGPi7F-p0D7hYGZhi79TYFOaadJRx4BFlznSQDS7WFT7a0aNR5_31MQuCAF5HnIELRiv-4sRNg9eQKyH5uB7_QhiYgpyWsP6i5szfoF3an8VXwrxyAXt_3JXILuki3P3Zkcumt4Pqz4V_lgNVjUqZvkb9IQ535OlvIGqFKo5mEwDSSfBYp2fvdZhgwhqb7eCG-aWlNq2ig93AQnUxrvOkj-5nsNczwZGtQFWJnFVyint9MkLnWmdKvKYO-iR4UFMmlzYRfJ-nlEJG9VHX9fNxQHs6vfQI7B4bD886ruUiOPAOVevzpCeGsykQEMK4iyBYMGNnb57Po0tUI7eUrEIv22T1EgQ4b1cY1XJPbsY-uDWo_CLkdvf8OKgvCfOU6so9lQv8viRBPrOii7QaqPO9iy4RwOsZ_SkfLNioj-BFF5UCrw-1ia4dxZZHtKUQbB7tx7nL4syIwFBMjVIUVIW2waLJwWUmXQD8EfqBsAiOMAZzXurhdk18FYNU266OIPavuqj_BAJOXpB8i0jo3SqDV0If2r35DmzkpDuWibzzbZ4p-Fx5_vi7ZI--xCNN0tRHOro52bbx-sjxdaTV5Kcd_oty7nE1R5gFA4T2GmACcKtSYd5ohwiLLlGkbr2WmCKRkhfWQrChSoiP_Id2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=EQ7-mLP46DvNn-9DwA2uloqiwHGPi7F-p0D7hYGZhi79TYFOaadJRx4BFlznSQDS7WFT7a0aNR5_31MQuCAF5HnIELRiv-4sRNg9eQKyH5uB7_QhiYgpyWsP6i5szfoF3an8VXwrxyAXt_3JXILuki3P3Zkcumt4Pqz4V_lgNVjUqZvkb9IQ535OlvIGqFKo5mEwDSSfBYp2fvdZhgwhqb7eCG-aWlNq2ig93AQnUxrvOkj-5nsNczwZGtQFWJnFVyint9MkLnWmdKvKYO-iR4UFMmlzYRfJ-nlEJG9VHX9fNxQHs6vfQI7B4bD886ruUiOPAOVevzpCeGsykQEMK4iyBYMGNnb57Po0tUI7eUrEIv22T1EgQ4b1cY1XJPbsY-uDWo_CLkdvf8OKgvCfOU6so9lQv8viRBPrOii7QaqPO9iy4RwOsZ_SkfLNioj-BFF5UCrw-1ia4dxZZHtKUQbB7tx7nL4syIwFBMjVIUVIW2waLJwWUmXQD8EfqBsAiOMAZzXurhdk18FYNU266OIPavuqj_BAJOXpB8i0jo3SqDV0If2r35DmzkpDuWibzzbZ4p-Fx5_vi7ZI--xCNN0tRHOro52bbx-sjxdaTV5Kcd_oty7nE1R5gFA4T2GmACcKtSYd5ohwiLLlGkbr2WmCKRkhfWQrChSoiP_Id2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
نکونام: از پرسپولیس محبی و بیفوما و از استقلال آسانی و کوشکی را بگیرید، چطور می‌توانند گل بزنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108015" target="_blank">📅 15:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b905343406.mp4?token=ImrOAGjITDQP9IMFUWc3JAs8vw1v-B8MXKsrxdU1OLuJbvqbiEyebKpvGido44UPXAjUAIqorrDK_Xsds5WrdIpYlqLzGFMNnOaHMFbR5YrAG66p2zs9RU1v30HomX1UbyTbXB1ti1G_8iSzts0RT7rFB1tubo0TALTl8jwlnBJIyjv9-MT7UmYMkfsftHH3gdAjJAR7llP5F6OcBvP9ukVLQ_MsSo2gklPUG5WhyfjkRBM72VgmcwedJ_Ggm1bvyZvWCWo71RK_I7jtzG7w5SJ0kCN8MHQvhPtf10RcIOwBwhz7i_DtpV7UKIqR_jd6fFm_w3ID42FRNz6tcfA_8S3wGdAiRkr3VyfKbQKadLdqhIyJdoDm_q73nMF5HoiXIYIJjxoFZhHLMB7NzrUZqOjQEw5qdyEmJ_dOQNzL8Y2dXJe7X6PO5ce3FsAEwntWA2Tfom7L8tMy9zoSFMQqAebpYQzjCnqwfRdoiqxfQQqfYWQPxHXziTieGYYFtTYyEt9WltsY39kQjYYde2kLahdpvOG8ONAwA5qgWCfD9bTwEOkihTuXgdugMqRnqAggPF5IVu9SpsL8PJ4VOK83SGDwxzKQZbB4rwg6lWfra25sXE4_k-wV66ero93DZZuh2Cs4lDiqH0NWzDOnRpsOOtqhpJTPrihz0k6pMveKW0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b905343406.mp4?token=ImrOAGjITDQP9IMFUWc3JAs8vw1v-B8MXKsrxdU1OLuJbvqbiEyebKpvGido44UPXAjUAIqorrDK_Xsds5WrdIpYlqLzGFMNnOaHMFbR5YrAG66p2zs9RU1v30HomX1UbyTbXB1ti1G_8iSzts0RT7rFB1tubo0TALTl8jwlnBJIyjv9-MT7UmYMkfsftHH3gdAjJAR7llP5F6OcBvP9ukVLQ_MsSo2gklPUG5WhyfjkRBM72VgmcwedJ_Ggm1bvyZvWCWo71RK_I7jtzG7w5SJ0kCN8MHQvhPtf10RcIOwBwhz7i_DtpV7UKIqR_jd6fFm_w3ID42FRNz6tcfA_8S3wGdAiRkr3VyfKbQKadLdqhIyJdoDm_q73nMF5HoiXIYIJjxoFZhHLMB7NzrUZqOjQEw5qdyEmJ_dOQNzL8Y2dXJe7X6PO5ce3FsAEwntWA2Tfom7L8tMy9zoSFMQqAebpYQzjCnqwfRdoiqxfQQqfYWQPxHXziTieGYYFtTYyEt9WltsY39kQjYYde2kLahdpvOG8ONAwA5qgWCfD9bTwEOkihTuXgdugMqRnqAggPF5IVu9SpsL8PJ4VOK83SGDwxzKQZbB4rwg6lWfra25sXE4_k-wV66ero93DZZuh2Cs4lDiqH0NWzDOnRpsOOtqhpJTPrihz0k6pMveKW0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
و این شب دارک در ۱۴۰ ثانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108014" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79183c9751.mp4?token=lqnSuHsgaNTQpspu4uBV5kXgFIFRddGd5wcS5qkgNN2K-ALL5hgDYjqnmr8LrNNitPjcO5wBCSzzg83_gEVB4B9Mhi7v6YYZ0DnN5JtfSl-M4wjzUk9491LQM_uGDAaPamCzEut8o_nyanD24zUU_otffwXBAd7AMxxLARaugXomoxNhVmy61gsGiAFLJWE4DX01xShi5J9jPVdkSHlsaUgIorEqtrAaLdjRMnExza9colzblWlqpNXB3YdSOBBDxsBt_a0UTYe12WLqj_mQNSzXIYGF0XUKscoegVWDdI2a9Ti67Gt5i3ZESL8_qVbAaAzhZTgh1NOfucO-11W9z2w4DqUy5SnBknZahbbOncOkyBGxRSxT4Qr8Vxs66_zAK9XZ_90ggT5rpu1eqwdElEdQi02bUeoSqV94jarjp_67xPNIsRul_EvlrVdhSOu2vrvFKvVQpODRUoCtNkXDei0cGouLhf0d_PvwqqX2wryrSrGP7ycTwNkkphV42NfncwrOlUvz02izXTvJcyKUSunAul_ecOndamjnsPuwLG-2rLea8SzdxNcJ3qEGJLsqZ-n1-q22SvT6DXTt9QPk7XenSUXJMvKBpkyOk28EHIsZeabmhurFUjUXGSYpMe9SzTLUPai84viUIiEFcVuXBHGDB7OHAOikgwb6UHrfGEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79183c9751.mp4?token=lqnSuHsgaNTQpspu4uBV5kXgFIFRddGd5wcS5qkgNN2K-ALL5hgDYjqnmr8LrNNitPjcO5wBCSzzg83_gEVB4B9Mhi7v6YYZ0DnN5JtfSl-M4wjzUk9491LQM_uGDAaPamCzEut8o_nyanD24zUU_otffwXBAd7AMxxLARaugXomoxNhVmy61gsGiAFLJWE4DX01xShi5J9jPVdkSHlsaUgIorEqtrAaLdjRMnExza9colzblWlqpNXB3YdSOBBDxsBt_a0UTYe12WLqj_mQNSzXIYGF0XUKscoegVWDdI2a9Ti67Gt5i3ZESL8_qVbAaAzhZTgh1NOfucO-11W9z2w4DqUy5SnBknZahbbOncOkyBGxRSxT4Qr8Vxs66_zAK9XZ_90ggT5rpu1eqwdElEdQi02bUeoSqV94jarjp_67xPNIsRul_EvlrVdhSOu2vrvFKvVQpODRUoCtNkXDei0cGouLhf0d_PvwqqX2wryrSrGP7ycTwNkkphV42NfncwrOlUvz02izXTvJcyKUSunAul_ecOndamjnsPuwLG-2rLea8SzdxNcJ3qEGJLsqZ-n1-q22SvT6DXTt9QPk7XenSUXJMvKBpkyOk28EHIsZeabmhurFUjUXGSYpMe9SzTLUPai84viUIiEFcVuXBHGDB7OHAOikgwb6UHrfGEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فقط از خودگذشتگی مهدی مهدوی‌کیا رو ببینید ۵۵ تا بازی برای تیم ملی نکردم تا به جوون‌ترها بازی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108013" target="_blank">📅 15:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=FTqUMZdnq4upgwC4Ptjualpqfld3WLHhNfAPdI4xssunRWKJXWGYfMmFecX0kTFw-uLRkpb9LmD0LnHCO2ukpI0bLP8HBZZGqc_t2HtO_nO1963BnQjZD7Vm1ZYtW6uE19WMZgHDeB37XHb82LYM3fHAWaHAGFkE1UqC_jmbYV3BOSuaJR-EWCREyEedgDUeUyR-QAm-OSXGDH8T7JMFrRcSwsd8wj-izOgXc4bzWeSMJd2UZzgAYqBRzjUtO9lXP0T-Tl72en8cVzBKM2KPn91QCY_hilirNAd64PdmjDDFWdiw1n5D21v82TSaKsr7EhKoOcyjrC4Icrakc5TFujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=FTqUMZdnq4upgwC4Ptjualpqfld3WLHhNfAPdI4xssunRWKJXWGYfMmFecX0kTFw-uLRkpb9LmD0LnHCO2ukpI0bLP8HBZZGqc_t2HtO_nO1963BnQjZD7Vm1ZYtW6uE19WMZgHDeB37XHb82LYM3fHAWaHAGFkE1UqC_jmbYV3BOSuaJR-EWCREyEedgDUeUyR-QAm-OSXGDH8T7JMFrRcSwsd8wj-izOgXc4bzWeSMJd2UZzgAYqBRzjUtO9lXP0T-Tl72en8cVzBKM2KPn91QCY_hilirNAd64PdmjDDFWdiw1n5D21v82TSaKsr7EhKoOcyjrC4Icrakc5TFujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Goodbye, Leo…
💔
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108012" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=sp8aIOEaPAiYmB60y8svOEA4s2Pap9gM7pHWEtcMlKsUbKBfJSC3j4qOzen86f65UUs4rLIeUfL6z4e8_1yjiK9-PXr5aiFNzAXmHDPWiznweFgO7Drrx_j-7eWMAij5mdGdDzs5PAzpdOZBfOqxlsCFW9yF6ULNlR4a5MIYhFWcDgpGTNMsWheCFzYK9tZZu5nIk361UJVNjkmmnJmSbwWjbM4ov0gt-lNGvxcD-uYM7Wvrmx4FBR6Q_OQyPQQAG6BydCIrYl05nUNGxDd_cuLj_rsz4GBSwfSZZT1pf3lgaaQhhD1nhvqAinoKNgQLeWDBAKvHy3QlRvv-smHZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=sp8aIOEaPAiYmB60y8svOEA4s2Pap9gM7pHWEtcMlKsUbKBfJSC3j4qOzen86f65UUs4rLIeUfL6z4e8_1yjiK9-PXr5aiFNzAXmHDPWiznweFgO7Drrx_j-7eWMAij5mdGdDzs5PAzpdOZBfOqxlsCFW9yF6ULNlR4a5MIYhFWcDgpGTNMsWheCFzYK9tZZu5nIk361UJVNjkmmnJmSbwWjbM4ov0gt-lNGvxcD-uYM7Wvrmx4FBR6Q_OQyPQQAG6BydCIrYl05nUNGxDd_cuLj_rsz4GBSwfSZZT1pf3lgaaQhhD1nhvqAinoKNgQLeWDBAKvHy3QlRvv-smHZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
💔
یادگاری‌دیشب داور بازی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108011" target="_blank">📅 14:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5irj-U9b6FhRuQY7M7iOIf7DucHJwxB4mvIdjBUoQRuLWs9dIQbR7FprPW6OsPelZLDtRw3rEb_YYrr-g9BVfktJXjeo7o47j8xPDTypeWqgf1tQKVR3-JopDRiXTpYqWR7KhTcDvxVl8e0j5ui0SWijkiaZEVi65MA72SoeFyYwTORUQMNFmOBxSXDQw-EHI_zNmwAU9OmYFcj3AFqKiIK_TB_lkj4s707o0oFWmcZ5ahfy6OcYnA6Rv7S-gLrdMmyQAaNfmuR4A7uJVtarVPe9xp0fqNoliXqFoSrczQ_5nympSqHfU2cslVfjlVHLUaQb4xfZWFjWf0Zw-a1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
هفت‌بازی اخیر پرتغال بدون حضور‌ رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108010" target="_blank">📅 13:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-n6sAN2nM2zkz-lpbFdJ1bjaFP-v_Uk6IxSk5kx-3ySCWSDj0d1c0U2Q3I_vH6YKcTrkEdc8zmqjc689Funvt0CP5mkKLsPyuwyPDr8mE6ze3CXP1WjIxeY9lGmQbQqeZzujpJLaRNbjEahSPdeFGj2SKhI33OG9VTVeA0WFQvyWV_caTzPXC6CCOoau6UZEUia8r4lrabIfMWkyHSfBVzZPHqbOQ1aa6MTJ79lLBfWeA3mxBFrTFqxZeIiOaNH6xtjaim1PFdTg7wdJdmzNGHCScL9KD6Bdm28c7nyF-RNgpQcsjcB_tZEWMb-xtuRm8_kznf2NX0sy8zvaSArWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108009" target="_blank">📅 13:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsN4TRNmSd8lB1_Tj6TyMMzuIoh1d2g3InJD_usKrywqlhkm8BbQ_REAVM1KGdGcCsCghL0lbjOPKJ4aRRfi93FF8NRMhxkYdHKHWcXHaKwUxFeN01YUhZI_XUkvddG1VDBEVbccWCXdUjKxZ8n4n-XbJRP1mfh9MbOJfuH9xWdRKs3KUVBmfEPegI_-e_qLHxRt9VV47fsVrGHxnQ556IIzOYhr9l9UHuBaGAI43GnV86LYtuPTNnW-mbNPVTP6OFcL_LcBKi7JlwJWBOAySAC9tCVwGucENAtCbeJoegnu5v_WGv8B5YDP_MQUllKMMK1qCQ1k0RAPvLJVqdw94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
فرشید سمیعی مدیرعامل سابق استقلال و کارشناس حقوقی: هیچ خطری یاسر‌آسانی و استقلال را تهدید نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108008" target="_blank">📅 13:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2ZldI3j2vzfxPQ-9pJ6OuOqTd2Wli70j0ODuwIcsyYCtz17mmq-8PKkzP62qjit39Bnb0LQyokqDtY1Kkc7gNedHCIDPdLR8mP4V2B_kpqaG9CCqWCo7jkrv-Lj4_x8pp7IIz7GNP2fFYhuoI0uuOelv5n3juLA_anRIG-5EJ71I7sYzOn_6sXzhsq38OlWdPPmkLA8-_HPSVcW3Q2uO1jzA-dAoO7yp340yiJ-UbOhFGufZVICrbBp0t8S4Sckar_HHA3fXy_BjmHdZrhGno0DeD2KreM8GiWhqdTAutcDoBMMyjUcZnmZPejJy13BC8f5P55mhUbCv2dQvs6oUHNFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2ZldI3j2vzfxPQ-9pJ6OuOqTd2Wli70j0ODuwIcsyYCtz17mmq-8PKkzP62qjit39Bnb0LQyokqDtY1Kkc7gNedHCIDPdLR8mP4V2B_kpqaG9CCqWCo7jkrv-Lj4_x8pp7IIz7GNP2fFYhuoI0uuOelv5n3juLA_anRIG-5EJ71I7sYzOn_6sXzhsq38OlWdPPmkLA8-_HPSVcW3Q2uO1jzA-dAoO7yp340yiJ-UbOhFGufZVICrbBp0t8S4Sckar_HHA3fXy_BjmHdZrhGno0DeD2KreM8GiWhqdTAutcDoBMMyjUcZnmZPejJy13BC8f5P55mhUbCv2dQvs6oUHNFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
💥
عملکرد تماشایی دیشب لیونل‌مسی جلو‌ بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108007" target="_blank">📅 13:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=IdL147opSF6ig21HCfV357RDfPS7KWwnSpOZ3o-eoWDDzaxaPDuPVR4BQcbXjDKPI5sd1Hogyg3Fan6D_DTAtVZfoUvLNd7FOvhWG3quwiuanLaSVjLe_nIYeBUPgeiKrzWdHUhLlOm-8P-mUzhH7cz4fGtWeTL7lBTD9yVR2LhefxEN1IwlwduLSchZ88nCL47ebG5mxp4QYkDBR0kKGXWuYCTpJYBhNTBXx5JFxcalYxhSBUZ60fhx1Fs8l641Nr__iW3jHblhLbEBqM72SqKRjEI0Kiyzcpoww_ns8fd-3YwL_tdHuqEjMCB5FNOI3QoXBKM6m4FXqNnoLHIdUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=IdL147opSF6ig21HCfV357RDfPS7KWwnSpOZ3o-eoWDDzaxaPDuPVR4BQcbXjDKPI5sd1Hogyg3Fan6D_DTAtVZfoUvLNd7FOvhWG3quwiuanLaSVjLe_nIYeBUPgeiKrzWdHUhLlOm-8P-mUzhH7cz4fGtWeTL7lBTD9yVR2LhefxEN1IwlwduLSchZ88nCL47ebG5mxp4QYkDBR0kKGXWuYCTpJYBhNTBXx5JFxcalYxhSBUZ60fhx1Fs8l641Nr__iW3jHblhLbEBqM72SqKRjEI0Kiyzcpoww_ns8fd-3YwL_tdHuqEjMCB5FNOI3QoXBKM6m4FXqNnoLHIdUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
کنایه ابوطالب‌حسینی به مصاحبه اخیر مربی تیم‌ملی: امیر خان ما رو بهمون پس بدین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108006" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR7jtsasLGPz0Ukj-ybERu4vFGvA1PqkEp4RdsW0mQH_q5uWDg1DKR9eg9QvCaogd1BEtM41rSo7JGFaHaBuCr62osu2CbOO4aoHMyZnYv-nOCnA9oI2CRWDFzVwmzidMyfQRn5vqam1YlHd_LCcM8Gr3KxE_-4zlr3SG-Yd9NCSecgk7Onc4GQh5lohxuyENGMdbZrRgmFy0xz8nwFnGbqKdEdh8WNv38XjPPPLTf0lsCVWiwzyEyBy9TNe0a9ONI2bpvGKpQf0PXsF3AVW9T7H-PCWGxtr_Gx0w4OlQ31GEp0nChNdvKZlv00XST9oTUMU_ljPTa3AzasTC55__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای بازی با تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108005" target="_blank">📅 12:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108004">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TZ9S4P5pNjCWiqC3kg58JUXkSlM-HGVEnvsvP7mSARAudpf0WUoa5njQhATk7BXDIgmqdmxqy16Z2cSiWFDjqA007orDvNinfqbNm8Qd8ZNka45J8F2YdzdbzDwdjGbzwiVrtM0MF_yy9b425WNSWrkKJbsCEr6fvJ8LwwzGP2weCmVJpc5ZMv1KzDO6OoQffOS8on76UjtZzm1Pn_LakLPyGLdiamslT1MzfpmihFvWDDlGS6thpomgF30pzqKJ_hq-ClFU2DaMv7BuxT-S88A3-VrTEsn2sHJ_WiW7dfJdVNYgE-uipaqti80Gg1Khnf2md7yYpBOgS_KHKnUGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TZ9S4P5pNjCWiqC3kg58JUXkSlM-HGVEnvsvP7mSARAudpf0WUoa5njQhATk7BXDIgmqdmxqy16Z2cSiWFDjqA007orDvNinfqbNm8Qd8ZNka45J8F2YdzdbzDwdjGbzwiVrtM0MF_yy9b425WNSWrkKJbsCEr6fvJ8LwwzGP2weCmVJpc5ZMv1KzDO6OoQffOS8on76UjtZzm1Pn_LakLPyGLdiamslT1MzfpmihFvWDDlGS6thpomgF30pzqKJ_hq-ClFU2DaMv7BuxT-S88A3-VrTEsn2sHJ_WiW7dfJdVNYgE-uipaqti80Gg1Khnf2md7yYpBOgS_KHKnUGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دبیر: اگر اسم قوه قضاییه را می‌آوردم باید می‌ترسیدید؛ خداراشکر فوتبالی‌ها دوم جهان شدن را برای کشتی شکست می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108004" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108003">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=KWUrYLOslc4PLufWFTGt2cMQQB9eY1NqjO833KlpEsj5woqTUm8yZgZrjY-p2UN4z0Te8gE3Plyp1K7UrNSez2oKYfhd7ahsWKbEk4Cmoor-ooEw0XFYUSg717ktUX9vsyX_Ut0FDPvOtk89OwV0rNbqn_2C1Dpa3bIgOz-uttRou__WPxCJYrRJCxgRfGdKOOYJv6LhQQZVwxTHgruGfqwHNsFa7tSwMriqFJ5SG6Yt4hxA78A_JzpEQRvtbRnXq8ycvTiP0ckHBDWp-M8M_qAnmQZNmnRMqbLiFtaYF8NEd6UaAlEK8FaJyl3Na5JiDtcZqMilGiJTpGxhGY7Vo4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=KWUrYLOslc4PLufWFTGt2cMQQB9eY1NqjO833KlpEsj5woqTUm8yZgZrjY-p2UN4z0Te8gE3Plyp1K7UrNSez2oKYfhd7ahsWKbEk4Cmoor-ooEw0XFYUSg717ktUX9vsyX_Ut0FDPvOtk89OwV0rNbqn_2C1Dpa3bIgOz-uttRou__WPxCJYrRJCxgRfGdKOOYJv6LhQQZVwxTHgruGfqwHNsFa7tSwMriqFJ5SG6Yt4hxA78A_JzpEQRvtbRnXq8ycvTiP0ckHBDWp-M8M_qAnmQZNmnRMqbLiFtaYF8NEd6UaAlEK8FaJyl3Na5JiDtcZqMilGiJTpGxhGY7Vo4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
🎙
👍
لئو مسی: از همه کسایی که کمک کردن آرزوی کودکیم برآورده بشه ممنونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108003" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108002">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=mvj5I6G20s2HuKeG9oqTHtJ0WBeHBUu0Js0ba-7JkaApAbGvlcKYeNPMPsIlUnAtVaif2U7a7W0WtjzJu9XD71xUS9ARnzJOTboej30o2GebWdUdakAw7eUrbM84SZtZZyl3qqNhArXfsjeSRU3U125rIL5FWFr5oQJMQ-K2hNNK_0M5-L4Og5MJD7ZD1tTw8Ph6p-WgnZtODSOcVBfunsbwQbZWvoAlr5ncfiDzecFchn5pzRAzbbTbizBkbiBo--w2MNJI-Mx7gVAxfXKkCTysYmYMgZZNkF0ntUHwQqA83r8YBTs-u7X0Mj4EmVgUgetTHd8vfj0DZK0sCLwkpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
👤
طنز فاخر ابوطالب؛ ۸۰ ثانیه تلخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108002" target="_blank">📅 11:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108001">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
الغرافه قطر اعلام کرد که استقلال بدلیل تحریم خطوط هوایی ایران حق پرواز مستقیم به قطر را ندارد و باید راهی جایگزین برای حضور در قطر انتخاب کند. آبی‌ها احتمالا باید ابتدا به عراق سفر کرده و سپس با پروازی مستقیم عازم دوحه شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108001" target="_blank">📅 11:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108000">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=RtDTM5vvC_MzOmO-V7ZaAiaYsodhBnXqrvk_5oVR9YGrSqLviz7HlM92DnPviPcjPjZbXWcLzpB9rlKja7uyrWv3EX1dMF8umVfdWu4eDUthxArsSK4JgcLQVsLfhTwhrYLPksrolIPSaO4NUPAr0nIvlRAIjbYcj3Sr5z3HW1IpOQK9qTNLHRKgqiO-GBomPWQ1Jcd1XGY6zr0f9HXiqNSgMf1xuy_cfY2rpTjea95qgn8256rV6lZtgWcjEElK6lIJKfJypVuNdBfk6Aez6ojY__FpuEjUO-A-B71HT80X4ROtnz-GNFJSHjsxebRvCIE6T6T11o5NxPMFmZSyLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
پیام‌ویژه یک مادربزرگ ایرانی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108000" target="_blank">📅 11:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107999">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFsU2eywaa5lQ1aYfOxI54SMkRVtObGuGVbcP4XaH4FF-4vTTTgowZ6xt8QLyk0i83rv_vPF_IKq8irRpFp63i2e4_DXjsqAehpSlWUhsFQtd7IzFRtYUOVD0uVZ61mjJEEKqFdB8GAT47vA98iJ04YS4UD9zdp2pUAphUBs6IcmewjufICLU87ijqeqX2OJmT4zzamJi4zsqkBdc-c9GX7Veq7SNK9xSOR1Mk0OTPOFsEbYVrQMsXPRZi5tYybJnptkCrm7ezqspj9UrwoKpM1rw1TeSsyVSpajSxmznA2QICFzmvFZC0gRTP-wa7Zy99HVF5R4CsivDz_gdEwa_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🐐
☄️
لیونل مسی با همراهی استفانو دی کارلو، رئیس باشگاه ریورپلاته، کارت عضویت خود به‌عنوان عضو افتخاری این باشگاه را دریافت کرد. همچنین یک پیراهن ریورپلاته با نام مسی، به اسطوره آرژانتینی اهدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107999" target="_blank">📅 11:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R36X50Cks2u03SyfhChA5dEYOUkj2E2IlRUcTQ3ESItBlhC1DvsNJ60lKBQuXivNjXDRUZWf-012PenQCdnxgDaAbs3MTez6p8OnpjNchcVr1G6vuGroOWZCzPU60j_txBOYeIcHjIWlWdxIoYb7takT5lmmXh2QQGjZ47BddZTh2vfA73YsnjFWDGLsa2CTrdoBcGbmLRHsVbixqyONaIFwzkBOIOmVBrj4tOLUGMO2rNg09hsF6kBjlUgDhR2YwClK3ODYSAVJRdl5LqaSncJwEm1XqP-lriZDz0oz-XJmZdX4BUjn_G7TF7OegO_BwLL7Ww57FFkZs8cQymw3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kghIR-ZmaQgw6_o44uDwgG0AKyM1pUTY7Nl6uT42BDsfpBVy35gXytu1abbAKKrFy03VCNxp9vptOPkBAhpApohRnTnLAeepwoxvtRlF1_6F4mxjJl4cQ_y5kjrTM6JtBLrF41dpF7IHZBcpEofCTpQIrte-ho3BcydR7Ip_4-VQCqOiYrH-a--lEPZMmRzjZ_kGJqhI0V0juMvWn6uAGm6R2obrslQOubjIP-iLL7TvzysKZ2y0kRp5pytZrB0lCrtyLi0Oys35SADzyTgzGTujYzCBixXXToGOJaPVN9X-gnTd3k-Y-36HGai8tJUdWJ7vfhgXrNtDIKT6JfcS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUFt6GsHZLtjZ8p89WJZszZ50OGKDNKSGXks7IqplazYg_3soVLXBCQN2AyoJhs5hKjxKyPoOSe22ee6Htv-nrW0Xf755jrsMeLwYLD5_uAVEC5LaAx1J85Wbda9P9XxWHE1sxgPmEfyuks8_XXqcOsgVYDFOJgKXvjsXfQO_Xoffl6Jh3v-ryz7sqKb-EfP-7_HN6VkNv5ZlA6FSyRcrptn158q1jkf8_ZziMPxLLIgkKSZuq1naMTA1xjBMnFubiO2A3iDw5IrtN_g9Wh8oUrxPmtK3mwpjsc03blv6NgssaQCrRrg03tFhq4tdmsJrqFvir3vjFIn9sUe4sblqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9trBph3UrAvERBPpOuR2T_GjT8MOr_wi5wKMe_Y5uUV9vIo2Pnv7RnFzLR4iejVxEzvuNOd5mHjlySLqbbOxbPjI9b9qDUGdcn3LFj_kK2sfSdHMgon06SgZyryFY4mNog6BmD05LPvAk8HpFEqjDpyBwnQfaqTYrUO6KFlmdiV7VDLj5Bq4rNBDt6iXd__40AvKiVL1h_1iMjmeR4mPpp-efOb0iY5dFeco_ZA5Tmv_PIMreSmqGEtqUJtx4ERP2iRrg5-CN_LVEXtPzrJqYTNEdopcHRBJk8KN66pHDiX8KHN-KJz7GcEXSuHEi63_6vRGcUFmN4JRy_NQPEwVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚪️
کیت دوم و فوق‌العاده ملوان با الهام از تورهای ماهیگیری و امواج دریا رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107995" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎙
✔️
😭
لحظه گزارش آخرین گل مسی در آخرین مسابقه‌اش برای آرژانتین توسط جواد خیابانی، رسول مجیدی و نیما دلاوری⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107994" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107993" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107993" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnFJ1-opgG4u2WZj82GwT8w58a06x9VOYj0tT00gt40a7mEaKYcbIBfPLpLejXvUHFrdFidfUJ9XRtWXpklOHump3d9_LL52NctqByFuI8vZtmC5ay95N7HBbZ8hFE-toDZAWxvIPA42YaFRS9I28uySKbNlNj9Te7K-qXNT6un0L8arwpw1-Rt_L40utWKIV4EEmpqvrnvtTIDx99VB6GoaAXBg9OC-4AOi4LNe1_jX6TazffOzK7k3u5kPTHm6U67ek36kdYsfZDTGlR0T4gj9rqLH79pjba3uaRt0I0JC8ic_BUvBQeC0g_auuHM5swQ2idGHjELF02GEED3jDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107992" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=F_9zWMCNA00s43G-VpveLVY0w2C2ihNoFMKO6oQ1Cv1iK3WeIOPXAtLhuMMBfE5mHfCxKojK3GM1K0toiFlbBlq6kLD1z-NBhUNPMgrG0qMELkQq3fmuU7ve-Qtcl7Ytx3WS4n6P8JdlBf2b4Nyq1aKNyjvrbuG_rWwCh4J7ZE8YK711OQvMFfyg4ZHrAJrBWBTB9orgA3wBL3MKXERWzvXU6rnzseXdU3zukcKcDeD0P2uCVAspO_20PXzpWojQUuXAAwaEbzYc_j2C29GlkCCTDlkiSjt91lfdJSkgY-ZQL3yIMlqzft6zXJWiS9aggp2Oj6vZIs9gJP2000E6R0TMvTzLC_q9lnL9cTO1b4aBZolzViyRqb2oWxgnEj6k3CPOxoNaAosAEeBlF2eb3Cd8M4BsKmCHnQ3kl4Q4nmyW9rREptpELc9HUUAF-pxj5dXYhewzz0L0WFXByPIrHoET12bFCNUdjq5rmvKYHbergndcYTPPAb6FbJfIyteZEWe3L3DsBdcPkS8LwWR7XA4Ay3WTInLAPXwCHmJwvlc6_OfGuzbToLPTy94vWVmx07UaE5s4d3JeM-HGBDeESYOOTFT5g7zqBKxOWDRVJ3lCk_SkO2A96pavskNYrOGdk8LRRBjfb2-EIXT8OlXI63TRsjClAEeVHEVE0Cfc5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های تلخ انزو فرناندز در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107991" target="_blank">📅 11:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=ULnuGYp9J1lGhp_CnL_1xmnYmQhjJPZvbr9lUBnaeMDp5qXa8KXrp7-mkkon9BRXmJXcr8dbApIKk0AsMUbf_3PVXhoTuXsY95qKsTlRgsUFttBKmwkekB85jmenwL7H_iWLoatU5gRLlxtQ8KD_CEBxbUBP_RJGSFI_vyhIePxPjuin7odicDb4ercW3AWDxRL1sB9_gkJjPhK0eNSMThBeohNhnF2tBPVMyPWDUjcE8Eakc8QtzBLN26iVPxnj5JkdBcVBLHwFzvxNJrcowFkhgXIVLUs4Nv3lAhZ_j4UinUPSZVkzOAHS6D_UnAX5Di6MGuE9sjCjhq9FzgRQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
😭
خداحافظی یار و اسطوره بچگی‌هامون
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107990" target="_blank">📅 10:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvdWFuv5_XRf-HpXnqf3xEfTDIoL4Q3BH_tbLtFinpN8Aa10C7K_DYqU4hLYAk_qcrsdBuNjMFC7vvvWb9mNxAl6vJkLS9-NyOBxAQs8UgXOy63AKIEqFoHddVrHUWaViw3CxjK4cjw3h_HiU_D2jPBrBC5kZ2yx0KvJ3u6RFFZkKC8j5FyxU_u_6IP5XoTHGzWR-h_7dQNk8VFHR7A2jIzZ2Em6TGyCZi-npMVIreSjrV-lScJLc1Rnz9_KVEu_Gc7GT5B1tpZCwIxkCofSzf0whUZyvzk_nHBX7ihXXAGTtOnuAcAmKosDa3Se-uZiJIFpr2K3KnC2LnOK5RzMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🇪🇸
🇪🇸
مارکا: هرناندز هرناندز داور ال‌کلاسیکوی پیش‌رو خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107989" target="_blank">📅 10:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=lbOKMBmhg4OraO6ci1_OYVo54wYxF2oVBF5W8hyNnpoUDvRsCjwrX7mjXYF0AoxpmX2UwZx6sBr1Skl559N6VthclKoF50RuSkzgeeu76kJsRMDN_ShQzsR2hRgmTSB4OX3vtRs5JSQ2Jh3P6RHswKOdk1lAmk4rgBh4npqJTUfGhQTykxkA8qq_9-o_VcO6TICyv4Z0m5n8cYZe6lUTyKz2YunrPDeiaX7NTyxPYmXHZ9KORzU8ZrjBvJxVAjUOSYlEOI3PuioR9bselx8a2L93RS9K7Js7J_IB9AQi8wc-fBk8Nl5Hv4Ev_Vi40vMo0hP_Hdn6ou0DYcqCtjAqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
😭
بازی تو دقیقه ۱۰ به افتخار مسی متوقف شد و کل ورزشگاه مسی رو تشویق کردن. همه هم گریه کردن و اسکالونی کنار زمین همش داشت اشک‌هاشو پاک میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107988" target="_blank">📅 10:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=t1rTJQn_-eevXYTfci5TVASv5Qbi47lhOE51JLWq7MWAi74a2JA8MX4ljqxtVMf1lT_O262dmVUpRyxM5OpH5t_nWTsL8HnlNBeHs5My0tStIe0qAynRZKZZyqNmrGY8gL2k1Du8yBunnsWdnZOvoGy4-HQDlKoTrDdKsIe71F1p88l-q68jHDFQJC_nsv-FSP0oTJ5BOu8hQ_Q0fM6U7oc8lbwLMZ3ZDQsEdQPmbhUxqMOA9_N2L67JCvfa5hMhRhSS5InWo4IDFo-4bo9gohVbGg9ZQksu97gm8dRAHQJwbdpmw5xGLTXp_Bg9KGE9vmsw6xcroiHJ_sE1aNYItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌دیشب اسطوره از نمایی متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107987" target="_blank">📅 10:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=ndXrhLdB40gLJrUOrTp61Su0rtHKlstk0So4UZ7tPZiOMj0n7CGieqcao_wk-tNuMAlryh81SdSis_46nr4uzRTQkdxOjD486j1L66plSblHJnNqvXkJXo6L-9QeCSvjHrQ32pHdH-WjoskBWPAAQvHMhtPLEo__DfwbrRd_3htxGNUzjl4G4eRfSsZaWTC2P4P5eoX2gX7S5LTiQuvJYTdZkVNhxApARlx4vaCLgvVoHl3OG6k__7MYDm6LFpzJ_cyMJ9KOHaeHTlwC03koL42YwaPKFgN5aH-zCHzkjxTu0uFBTDG6P6jIgoHM-ufjToQLwP4tWgdsWGaqr73j7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=ndXrhLdB40gLJrUOrTp61Su0rtHKlstk0So4UZ7tPZiOMj0n7CGieqcao_wk-tNuMAlryh81SdSis_46nr4uzRTQkdxOjD486j1L66plSblHJnNqvXkJXo6L-9QeCSvjHrQ32pHdH-WjoskBWPAAQvHMhtPLEo__DfwbrRd_3htxGNUzjl4G4eRfSsZaWTC2P4P5eoX2gX7S5LTiQuvJYTdZkVNhxApARlx4vaCLgvVoHl3OG6k__7MYDm6LFpzJ_cyMJ9KOHaeHTlwC03koL42YwaPKFgN5aH-zCHzkjxTu0uFBTDG6P6jIgoHM-ufjToQLwP4tWgdsWGaqr73j7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
فوتبال ما شبیه شوروی است اما در مناقصه باید وعده اسپانیا را بدهی تا برنده شوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107986" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=NeN_uIrAKOitxNPURO5hAcXCnnfo5lC1dvMvLXm_ye2ZMr3u8lm3Iq9RjtHqesnilux3ZhNVGDOXlv0URYR2duLUr2jS9S7vJf9RBs5n8ZC9fJnoSqKg9DnLpGWr2KhEHH2KL2AjqxerSpi_1rJrKOGqiNGx1BSvx_6v0ar-Rs7EFqAgv2bIezgcy8zN3D9Y1-nvk9-sgI_SQXKz3JQ8yzZIMs8a-oSyhwtxPZP9yjHnlWPNgmzIuKeb98Uv6VCxet6X9ZNrjSUFYpJGeHS2YaTY7QLUB9wCTaPP3i7sOupnpFw01RJPJW5pmOihwswgyzZNDkvecR34CkGrBXBcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خیابانی: سه ماه دیگه صبر کنید تا بفهمید اسم واقعی من جواد هست یا جمشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107985" target="_blank">📅 09:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ufXsoDdY8CMfZaR7dTbtdBUd0Y7ToOT63j5mrxtwJ5hozH8bmGm-OkCk9RCRC296h5T1qdD9LkWtQ6TH4kPjk7azkDDNx6kBeZ0ihLO2fBlqOXloYtDKRkDJ_y0KDlxkntaU6kII9NoLccge-H3IoTdUh7dbTb0xY0ELqoEBqMptH60_CUa24h2QgLxv41cLAwkXaHzQzBObZtmXBrwq8MEXvxCouE82ljDtROQVA3G-tfz_weGsMe4ct_c9aNsBEwtzc2FrPMCPs4EI5zX2PoAm0yCXLnFBXJvNHv-Y43_Vj68baJaYvraj2cszFcOaushnAdmP0PaKyw12tqOM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=ufXsoDdY8CMfZaR7dTbtdBUd0Y7ToOT63j5mrxtwJ5hozH8bmGm-OkCk9RCRC296h5T1qdD9LkWtQ6TH4kPjk7azkDDNx6kBeZ0ihLO2fBlqOXloYtDKRkDJ_y0KDlxkntaU6kII9NoLccge-H3IoTdUh7dbTb0xY0ELqoEBqMptH60_CUa24h2QgLxv41cLAwkXaHzQzBObZtmXBrwq8MEXvxCouE82ljDtROQVA3G-tfz_weGsMe4ct_c9aNsBEwtzc2FrPMCPs4EI5zX2PoAm0yCXLnFBXJvNHv-Y43_Vj68baJaYvraj2cszFcOaushnAdmP0PaKyw12tqOM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پاسخ جالب حمید محمدی مجری تلویزیون و برنامه فوتبال‌120 به دعوت ضیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107984" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نورپردازی و تمجید پهپادی از مسی پس از پایان بازی آرژانتین و بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107983" target="_blank">📅 06:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIfzUVShNmXMOQr899369nPXpYDEUvo_0Dq3WOFQmk0xCfKK6h401QMG0vPuyE-KdnziG_OmTETRsAk6q9YyqpHbxLCClhUbc2P9MhUtV1sqXIke-RnX34V0eIw3ByVVK3B6NoshjKDgyVXp0mGNg2I8G-Hz1s_gxkciqX-sWdcZZgB2XfU5u3KsEnit3R5O09bIKhevGhXjMKmF57pkKh3rdADQIEQz4gavdM2zmZFSkX6QjEl42V7VEfl8ITkrFllPaYP7aGj6F2a2b4elH46LTP8FG5CFSbMLvoY4PGQ1aWsO9s4sL6LLm_wbqfsRAbCU513DQJde9gdpbW1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeyBH-g9Osr3rbjOZB5AWY8XcU9t3mxXhCkvAPu5dasDFujmPHno-9QKmowgpUT1i79v6JDVVBH5GG1E9hsjMWKLBNPptQyBWyyVr2qU-ej3SyFieofcWvCqQxvRnQ4wj3ezHJoIyyYuLfmvWOIphnyvN0iLvaDLSPFJNbECv0_H7W9pkxoIs-lyobDip3IBaR4ghtHLi62X0EYTAq0GkvEkatF7iP-Gw_60TKHY02wpmPYh2NbS00gXrJJZcTBhuCtzL0KVc0ImsaVol17hFdrnLeeGMyxY6nl77lFgSwa3oXTcqPSKUf4VMLy4PLDu4bNbpD2PKH0vpr0Za72_kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😭
😭
😭
اشک‌های دی‌پائول بادیگارد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107981" target="_blank">📅 01:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107980">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=e7hsy4ERrCL9RHGH0MiFCdU5LF5I_H2RFAT2vVSzZzssuDiZWBsgghGMlxnOvxE1tcGe-sA6ChX1Hg6KxcNB4Jo1F6r1Zo9yPpe0mq7jaJ0uC5dwUgXSwtHOCKlFp6RZXQ_jWg5HAunqGaJogOftVQ5HTR1CHVMDs3paGI1PkVlLFbXEW1bnq27894X-azOM3FwVPlOp243vmyImiNaaZy1zTPWfLXwib7HjPloPTqpuLCAoUFZ4MbdDsjIz2T-ir5PrH5mvOmv-Iqa02N0TeNkJ6I4YUY2kLFBQR1vP1FLCfnV4jIoGGn3DTJ9i4PdX5TMigicqsh6acybE5swqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آرامش‌خاص و لبخند‌های لئو در حین ورود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107980" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL89O6aZGuytaMldxL3nS_cc73r43jkHqmd5KJCwo7sI2rRHWmbdorrJN2wQ3QF7xRFEUOIpK-OjC5ZjyOTquP-SXDE3Y9y-bDRkG9VCxXh__MAlpkACcBU6_7A11U1PkXsgz1vVZYUGd80-cipV5mYX-_0Z_kDHz4XJFrxztKcg1-xhJfD2EqKqwtgGvi95SwgRfVf6zPaLuft69PHIEpJ5UwnUTLN3porQQx6bkNyTxIkk4UkXE3rIbPVTaxcjenppA_HNhg_ObTeZPe95oM7RD7KM2u1HlgnLfFzP-7N852CvV8mtbuMk7CImIe5ztCMpQtiUNyPOu5IV_3ImhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لبخند زدن هاشو ببینیم
🐸
🐸
🐸
🐸
🐸
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107979" target="_blank">📅 01:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107978">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvGNSJ5RvHSZF1jupKTDiUjQh0Jma_3k7Ufk8QT8DK6n-6eogJLwoeYu7arBaj_RgD5nf5R8sNdDZyVEhATjLPc_Bp0VcTMEw4GYhOjm8IIHhHNwwWEgtO4bK8U0IT_SSePGun_kZRg0IR7Gw8zlln34_ZPHNRX8ESF2QsU9Ly3WXvwJshEjqPp4NXuGOZyry-2B8lvHsl7ee5Cx3-MCJkz-LFIZnpxIyzRoFbCa0JOZLatUqNesfiXOdab8qg-LB7WVE2n38N2fl6yYzEDCk9Tiun1i_epeww-uLBzNCqXRclfWSKIcaRPj98l6AUGliIrEK7xoWWJyofylEqxMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
لحظه رسیدن لیونل‌مسی به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107978" target="_blank">📅 01:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107977">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0rzl4DMct1_KEgmT8sugGU3GmlNYmHTBZ9t-IVs4eMisE-O5NBpjlRycX4R07A9Up-j_QizRsL990xU94bDob9fnTJ015AEQyRO2L6fCFqOejiNqIILwlykKevOSsCfcfQOeEII63bp4LiKQbfjHblilmCdmIKYj1yFMq1N3s_cGxKKBGbAwQf6ZPOr5EgZFFJhF7ra-BI1cdpghfwx92ycOjHn13lscoioceWA71ioRwKhIaA2POOTbgvFSBMxqIZcR88-DOwU8F48X8DhanjqmbcCtgTl1rGoGzrrpcgd74FCiCSWyG9MaPMe2_To_jZyiZ8G6esDj7xfimGdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
نمایی از استادیوم مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107977" target="_blank">📅 01:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107976">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=gp9BiivM69e6AWyQNDUz9uJw041QTIk2zl-Hz79Uo6dvS2po_tBlmkQkR7RLxhGwECFvsVdroAWVcOhvUhoPqra3yjix6vyG5O7atOSWqbVxytbYmk01UBRfiL5jJb_DtC-ec3LnpEPZiWs5z58KnPNZaK_bGwaRxqsPKC8OMv6FPrOaSOhdO0Crc0QU34QcIIEtw1dLy3h0dF-oq3zxswBcnKVblG3nsOqszszk_NWrfc5_j-xweXxVdIhQCVH6iT3bbH920IbaWagzrCt9sPGhM9N2MTUF5auXOVK8LseweJVyGC1vKg3wOaiXD8JhmVMMZ0vYJ6KHfwcuRXhwcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😭
استوری امی‌مارتینز از سیل‌جمعیت اطراف ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107976" target="_blank">📅 01:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107975">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=Og7Nl_6B5rsJt-0hIjsN8MoDibiwQVElWCjBfDHC2_goNNaUbE1fgcQNnUbydyI7saW5ZXXbolmt8H_pD5_1lw4tt4MG7Tj3mjpMRR0vWoB6DxD2bHOMK2pGFSEvP6PkKekfx0maBnlsVsCkKSxxko7FQ2rru6LiPFhBHtcPj5rk-WyZzK8C8TF9nHtDxEBMnOpGYvTo0oPA1H0GLbUxxWjVNJSAepQS5NYviW5wPZodFH8ESDAQetIuDfcI7u6278dU49fz9u4a4lv_LXtTlTrJu8Zdo_82eclXkswF9G9ygR7_AFBwolL5cGfl9bJlMp994Q4lDQCkk90yRkR9kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو فوق‌العاده استادیوم یکساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107975" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZN5Twh459Q9e_3m1cHhtyHt_VlEMVtGQmk-QV9JUO7A3rIsHKJV2KaD1wB74FoXbl5XN_NQYutvGlFJnP-ptkgF5icn7sJ6iR0N-TOSlplMBSLUHUzhTJyNPvXHkhRG5_LwQAAf_R0nCCZZMRpNcuGF5hZ0FzPhQP-ET2ChvCK_bnwEyOxsCRc4tWIM8O0My9E0PSCNFYGsvdFJmhSwkzQ73aableMRMmwW5rfE7UWy5upzSRDT0EzXNJclAXEuDboLKmQQ7128g5R253hz7ugvzRZbeK-JY96QHgwmuEgMZRJGytf-Pueenu5UK8dK2HpyTRtNDGYRMiNcPUIzcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URIIadWTPZrdXt02PCP39SGDR86XEYisZsPNnROo9-Z5PPI_gFZe9_qT_-PRWfSj_CsFdWi3wYACtRhQi3cUO5bM6e7Fd19EAyShtjNPhLncOAefQnPmwLfL-vtPxM6WMBPVA8NY4RBI5SZj8UsLFb5jllcFn2v5X3lyaHUpQhu5rgAmAFeLcQRDKNMvcaV3msgKD-agqQ8Ym9P93jacgRQ-PSn1Wvy_PcoNJ1ldERuIovFYonJoNJ5Mi9i5krbXsIpo7YzssxfX06wmAfPrmDfY0U2YpYNdqHyTA0sIPNBbtALEO1AjkNv4IZ91icCU1gJR9e7yU718Oymlbe4aHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عکس پروفایل آدیداس به شماره ۱۰ آرژانتین
همه اکانت‌های آدیداس در کشورهای مختلف، عکس پروفایل خود را به عکسی از تشکر از لیونل مسی تغییر داده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107973" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینقدر غم امشب زیاده که آدم رمق پست زدن نداره
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107972" target="_blank">📅 01:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVihbgWdk_nkwjvtffm6TuyfXePwfM-8apmMuLTSEmHhkDvRhcLsSo47oFLh-Xdg8QAHqYtCgMeatDE5TxKuco_2XWKta7HVu-5Bp92Qi3rFRKPQLPseO4004DkEtHqs3dB1dtAnAWKY1h0yN6Ok2E-536QDOUsA67dkYMasLyhlXfxTpThlgfkTBJoTuZ_ltb5pO0wjjM_zhna4ajfdSvIa5-TogG1BKd-GBJJA13qgG8z6fgTWPNtAO8b2i8sVyAX4mneK8pEqusGTKgYMTYix_BwcQFDZoEDx93-_YJxWohaSAaQl7tNLSXk3fgXe3q-5y2YDigTNFFs3vWrClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
⚽️
The Last One...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107971" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZRIj3DrmDVYUGwWmR3fErmvsArTlcZYrcbOXVlN5qvyRAjABGmWDamFKBU8C64WEsziBNrYxbC8reQOMcnHFgTC3Q6dbSF6IgVE5sUyuxHr3zBcjHf2Ydxzap8acgTsqc9hc-NIKQVJ8uVWI8l1MVWKEqyx7faiBFUZcM9jK30bo4Kb9gJEAHZN_yJKMgI3FaZddJrPnibUxae4lgx6ZpTZBzB5RX3w_tGIO3Kq_sORkbOo4g4UXmce2g9hDULiCTtzdO_U_no3S0oRMiGe_I_84Bk4Uzns9GPfQkeJyo_zRF2_0uZswBNP31-JK0XcA9Ek6FL4jKuPtzI7wiU2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107970" target="_blank">📅 01:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFGozWRUJwD5eZarQj9xjOJyTt4HxcoHvSp2I9gorAqPioG0TjX9YKl9gABL5KwilWiWc0ra8N5OExOB1ySJgWq5Xdx1psedJx6FUScWGOGowmHM8veZfKZ5fuO3i_-XNrnYuJzYjz9xcDhHzZ56jHXeN842-dLgnxosrY12ObaYMqwvukJibXjyHpVx5eDp1bmXTt9M5aQz4dtWRrvNOnSULE2G_8wv1lBXLh1TWYUfRx7Zn317zzE9hYCj0WcEqIJIv1zGWBmoCNTO1SQ4hBBlPPvliCVgfFauqx7KQCL1cCNSXV2F1XJ6flo-5D2YQaV-BiOBFtUJ3CibEkmxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107969" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeC_JWSgR7EycF0wosFS3hCU24Xphz2XCvkm6jzeEMqp04Ew0B23JxtmmrXw5jazJrLtzbN6aVZO-0SASzt9QcAExuzE4S6QPDO1kb_Ms4zRolFcS3QpI_b4X0WRwq9zpveAdjVy5Y4yXsdgtShCfKn0Ft_B7znlCIGfrlZ2acZlYd6r7yNbAqi8jaQda83HVJlLxwT9KY-VEI3-NfpusjGderT0oJSIfegYHwoJPlC9U00fcO49itpVdpQkp2r7No55BBi6_aNSneF_phblsng6T8uOw2esEw5oGr9fhl_NwKgkijRIThHIpOEuH9sTwweVIQq8sWAUOW_XJyT8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
آمار فوق‌العاده مسی در ورزشگاه مونومنتال:
29 بازی
⚪️
19 گل
⚽️
11 پاس گل
🅰️
30 مشارکت در گلزنی
⚽️
🅰️
✅
هیچ‌وقت مسی در یک بازی در ورزشگاه مونومنتال شکست نخورده است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107968" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=PSA_Dq2InnS6JF13g2P9cprvoT20ZeUqOQo8mFBN9y83lQ7anDPA_LlLIJE1RZSC8ixBbrPwax5BntMU9ErnNMVfcDD3x6fK9sDsq6P6K3_NrMDhb0YYJWu9agq_Cj9r5-pQhAa7WNXFSQwhoqFHLiiYnbFbpp3iR9GOWIax5Nv_h6dxFGAzC9HDjMkszK2Myk-ZO3IKv2V21Pbi2m1shqy-D8zP0uVKG6jI5RfOlSOcpT6ix_NVfEEf3ecmrk5MJoPQAw0bQG-z5-DBvb7mQ3S-DzxcPZEAUZaTc1cLkGBgWGlM0Ix-Ujudi3jKEs0lmwmJnCgiwWibSW0m7uK5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=PSA_Dq2InnS6JF13g2P9cprvoT20ZeUqOQo8mFBN9y83lQ7anDPA_LlLIJE1RZSC8ixBbrPwax5BntMU9ErnNMVfcDD3x6fK9sDsq6P6K3_NrMDhb0YYJWu9agq_Cj9r5-pQhAa7WNXFSQwhoqFHLiiYnbFbpp3iR9GOWIax5Nv_h6dxFGAzC9HDjMkszK2Myk-ZO3IKv2V21Pbi2m1shqy-D8zP0uVKG6jI5RfOlSOcpT6ix_NVfEEf3ecmrk5MJoPQAw0bQG-z5-DBvb7mQ3S-DzxcPZEAUZaTc1cLkGBgWGlM0Ix-Ujudi3jKEs0lmwmJnCgiwWibSW0m7uK5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زلاتان ابراهیموویچ برای تماشای بازی وداع با لیونل‌مسی در کشور آرژانتین حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107967" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=YLliCsorj6KmvBWR4G_hciPHQAK1LB5sgkWNkDydYiEc13ctnQhzDGW2LjLwkGwfH1zA9ac48PCeA0weWp78mlAChGo0NLZgV4uaizwyrtLoMNPpjhGrxAXPSnG6XpApgqDTLtt4d_YyunXX7yZ-Vk85fr64w1NHBMW57nqgzfs2Xzd85C6kJp-GZ47YxO0xTSOOfP7kRAXj1gqrn81ynZvxQIreGNkACCvN4_QvxP_4ebItdYFansa7pFm34iBb_IWIjDBo5uahWc2X1Ml3bKkxyTt7LRRFhtz-ot3XI45acIxoynOaATu3TgmUyV39RBsoIRD-a_SNbtHCLVVN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=YLliCsorj6KmvBWR4G_hciPHQAK1LB5sgkWNkDydYiEc13ctnQhzDGW2LjLwkGwfH1zA9ac48PCeA0weWp78mlAChGo0NLZgV4uaizwyrtLoMNPpjhGrxAXPSnG6XpApgqDTLtt4d_YyunXX7yZ-Vk85fr64w1NHBMW57nqgzfs2Xzd85C6kJp-GZ47YxO0xTSOOfP7kRAXj1gqrn81ynZvxQIreGNkACCvN4_QvxP_4ebItdYFansa7pFm34iBb_IWIjDBo5uahWc2X1Ml3bKkxyTt7LRRFhtz-ot3XI45acIxoynOaATu3TgmUyV39RBsoIRD-a_SNbtHCLVVN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دویدن مردم آرژانتین همراه با اتوبوس لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107966" target="_blank">📅 00:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Hykz0v0nE0vqpcDudWYQyhIGcZKTDvSi04LGAgxVZaIEWpcpwdHSFb1SC6gqDaiMAjalPWJvlPw4APLxu3xuI3ku2Sd1IrjCvK_GkPZmsYpygpZXz-KRDonI9QguXoltdZHCKsjyyOf6ijkxjWREXq3KI5frd23k9hTmWVHhIkUr8LkMPPCTU_a0iUKw0I7jdGaWvy2j6H-CqRs9DyHx4TOXfzNhBs2Dg8JH-q0ObY3QiphUvFYV3PUU6zeBlLnvV9R2cb1hjZtfVmdhSFadPoc-mJQQ5L8TSWZvUB6kDMwutKgbHwnq4QhDbLIbRYKifDBxVbRUMc1tY6IXUo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽
رتبه‌بندی گلزنان لیگ ملت‌های اروپا پس از پایان هفته چهارم:
🥇
هری‌کین — 6گل
🇫🇷
مایکل اولیسه— 4 گل
🇪🇸
لامین یامال — 4 گل
🇫🇮
لیو والتا — 4 گل
🇮🇪
تروی باروت — 4 گل
🇸🇪
ویکتور گیوکرش — 4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107965" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BI9-XTdus3CHucnPeR28hwWV0ktvxZCOGfGiybWzwNZ5Ni5VmB_Dg4ZX9oGlL8BXu73aLnytDa9__suBbNNDmQxvhtNkVJsTndu4oWeUYPLwihJC7V_apO3U43yxQ2GyXWEoD6ERYHPEn-_Zz5PKmWVRmy3zQR_FVN_N2N7_-rzf2hBwAoBdWafvjTbE4dLmsXOe4RtwM1uqWY9PoEaw2txnLToAKVuPyqeIzyzvMatVOTTvW9Lbr8_M-ZIxBOtFy0dUlI_sfnidXnTY6_Sh41FD5ldC1eAJiRbrfyUEsHnDIJ7NUOd6OnuUpTZx8_TvUM3iGRJCnkLCmcqrND1joQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره در راه ورزشگاه
😍
😍
😍
😍
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107964" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=E4BXraAYXnyudzVOCM3JW5hk-DBICaJLOddzt743k-kLEvPAvxGW-jvvfnMWIj4WagafrDaPD52n2b6CpZiYXmXfm-FT-BlsYMcIj3esxbfNR_tGMkq2oNNs1rMiWztLRjyTedZu8pLaoeZGlG9espCY6lNW2hV5g1XQrwmkY31EkQg1b03xOCNNNWXndhxumQQTT8lVeepodKKfv8v00L_djQxuQo7b82YlG_AJnH_QKpkM1UrprpJlTacauCi-7HJIFNTVZUkZYZ97EU5RkfKJPsXcop1UsAee7Oul7qvQ5I3MJFXzgRbcfG-J7Y2ZuQvB1XTDkWTd9SQS_6FENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=E4BXraAYXnyudzVOCM3JW5hk-DBICaJLOddzt743k-kLEvPAvxGW-jvvfnMWIj4WagafrDaPD52n2b6CpZiYXmXfm-FT-BlsYMcIj3esxbfNR_tGMkq2oNNs1rMiWztLRjyTedZu8pLaoeZGlG9espCY6lNW2hV5g1XQrwmkY31EkQg1b03xOCNNNWXndhxumQQTT8lVeepodKKfv8v00L_djQxuQo7b82YlG_AJnH_QKpkM1UrprpJlTacauCi-7HJIFNTVZUkZYZ97EU5RkfKJPsXcop1UsAee7Oul7qvQ5I3MJFXzgRbcfG-J7Y2ZuQvB1XTDkWTd9SQS_6FENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه‌ای از دستاوردهای همتی در بانک مرکزی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107963" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvCmMJMjHJxNEo5JTObXCxmOD0rVrKaO2XfyrLMKi1ljo57m_6nggYX1WIrcb5JxQrj71orrf2auID5rKrwnX8eV5EELar65NX1RR9WGNI32Q67wza19LkivJ2E_mAIHN4VIMLLu5Ep3rtn_DqIFVvcgljraHdGJq-d-kXuUoyF6M7Gtl-Y5MXRrAYJN9zhlT7HijI2oCB8OPAwP4g2RZ771UI55wYCSwiFU3oxS266ts-mCL0Li9aCVuYExvkoYoYi5O_ZBtiX-6-LwAA478rUUpV-7Lvvcijge_agnNcu3L7XJ7XS8zROdvZ4BQSHUvlG1GpQ71Y8t-JFxIuisPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107962" target="_blank">📅 00:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107961">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcTg66lKWGQQ5nICipBIeMKb_sMEYbDwEtcG65hEXI72z0_2dhq3Q7r3f_2BB8_DxrzJBXpeUxYLj_5W-n67_ou28ontX0Cc7M56HIovhn5jwRTTyg4VmyPdmHwrmzFyy1YK90CL4bxf33wpwvunh5BHH6TMTtzHq92W8hIUNf_79VRopIMH_laEOZyabYNCzVeMk6Jd_u0tAaFRiCZxgHAv3snN91m5QM8Q_5lQ1_nWIcVmRv42XA8NOL_ERjB_2hRSUwRmQUvwRolm2BdSn1gGTX-8w4_YP7vT8HN8u1U-oo5wY7lcjfaFcznYUIFnX0fWpgTPeTs2P1dlqaWpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا به مرحله یک‌چهارم نهایی لیگ ملت‌های اروپا راه یافت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107961" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107960">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107960" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107960" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
فیفادی کسشر و طولانی سپتامبر و اکتبر رسما به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107959" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107958">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=RbBHXWrv8ZGkBlYZK6SxGgtMVpTfavgIEEOkIonmeYjnU7EPZ6MDF-oYv7uxQXUZPhzX_5w7xlNqiC2konEqTBhmWVzYVc3sqs1k00eg2-KWZiQpKF27mSkanUcji9MtPSm9CZUP0kMyzXmT-Lp06npYxZespCEoUSs_qgFc2RwbriBiOllewPIAgtrt-JVt3z8ZTluu-iXGPUTWMV06qcrrDfLD92lgE6hCWbQmj6kWIZUShST5pT_wldbeu1Dp8D-h3dy_z6Ow8m8_ARvBygVecSNhLYwLKZat1pPyj0qjIOh4vnnDJk381i2Yp8DH858p4zBaXqRmFBNquQz8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=RbBHXWrv8ZGkBlYZK6SxGgtMVpTfavgIEEOkIonmeYjnU7EPZ6MDF-oYv7uxQXUZPhzX_5w7xlNqiC2konEqTBhmWVzYVc3sqs1k00eg2-KWZiQpKF27mSkanUcji9MtPSm9CZUP0kMyzXmT-Lp06npYxZespCEoUSs_qgFc2RwbriBiOllewPIAgtrt-JVt3z8ZTluu-iXGPUTWMV06qcrrDfLD92lgE6hCWbQmj6kWIZUShST5pT_wldbeu1Dp8D-h3dy_z6Ow8m8_ARvBygVecSNhLYwLKZat1pPyj0qjIOh4vnnDJk381i2Yp8DH858p4zBaXqRmFBNquQz8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107958" target="_blank">📅 00:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107957">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=fEfKHaq795TgFEgjAz1LMF90AE7jX_Dr1DTikSlKLGHeNERSSLQEnTy4I5gXyxqVCeH-4wgEQ3vmVhuniIVeAmo-aLiJTdWeDOerv-sP6tGIKu_WA9xm5JeJ0Q4RGADK6VD0vv9GOCxbizRsxY-Nnq5Jvb-MUvEvzXJd25uwl7qv56V7L425kPpTd728hnlzhBmAj0NRRUWC1hFwvXe2EoBtXrKouyqB6Re4DjXAmgChsmknj6P7qdDcPyQkWNcM-8_uwoDnZMtq3QhSSvWxrZbIiqLdAAhrqcckvPxcfVFXDs_7v2E4eZBGqLRaWjVC5ZER3MKUipq0Ggew0I5i_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=fEfKHaq795TgFEgjAz1LMF90AE7jX_Dr1DTikSlKLGHeNERSSLQEnTy4I5gXyxqVCeH-4wgEQ3vmVhuniIVeAmo-aLiJTdWeDOerv-sP6tGIKu_WA9xm5JeJ0Q4RGADK6VD0vv9GOCxbizRsxY-Nnq5Jvb-MUvEvzXJd25uwl7qv56V7L425kPpTd728hnlzhBmAj0NRRUWC1hFwvXe2EoBtXrKouyqB6Re4DjXAmgChsmknj6P7qdDcPyQkWNcM-8_uwoDnZMtq3QhSSvWxrZbIiqLdAAhrqcckvPxcfVFXDs_7v2E4eZBGqLRaWjVC5ZER3MKUipq0Ggew0I5i_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107957" target="_blank">📅 00:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107956">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=EEyXA5qR1tFf5vpHcTYmhxk5Vxlczo6IoMBA9hODDlACHpoDwEOC_i9UyR7_hdgNHf6zhASCykNaePK80SKbpeY-AxFOeguGYXlrAa52xl2iEJQjKE6N9XNc3Vfu8dQrBlHJVBPSgbSUVOP2xFAqSnz6Neb87Tc-QA95hDHdBbnxahdjmZeHRxyCFhWx3Kj_53tF21CDGcqf58diAGt2PwHSHn4iyN_mD2dFJN5xNeHLt7ACwSZ0ePx-x6-sR9wAcG9nR1N54IjOhzMSteQwb7Sj3U4dJKBtdBxK-7sX1c_68j_gqcnV9zSbWOU5DmobsEZ7GSxSlkqe8mXh0NvhwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=EEyXA5qR1tFf5vpHcTYmhxk5Vxlczo6IoMBA9hODDlACHpoDwEOC_i9UyR7_hdgNHf6zhASCykNaePK80SKbpeY-AxFOeguGYXlrAa52xl2iEJQjKE6N9XNc3Vfu8dQrBlHJVBPSgbSUVOP2xFAqSnz6Neb87Tc-QA95hDHdBbnxahdjmZeHRxyCFhWx3Kj_53tF21CDGcqf58diAGt2PwHSHn4iyN_mD2dFJN5xNeHLt7ACwSZ0ePx-x6-sR9wAcG9nR1N54IjOhzMSteQwb7Sj3U4dJKBtdBxK-7sX1c_68j_gqcnV9zSbWOU5DmobsEZ7GSxSlkqe8mXh0NvhwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تنها سه‌ساعت تا پایان افسانه لیونل‌مسی در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107956" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=PK5w4mOmqsHaEBQWICbylI9t8R7WW1wFwpzTEauGr3OkibSmyo2BHQeWp1AiapkQ4DtESAso9DMipCzxyqRGCNWFyIJSS85xXM_c-yR8vv7AdouMlQJTr-tY2b73iOgo1h2IW3dMVegTsINqC4ivn17pRTBEui7IB-CYgx86oEGfnvnqUsGwFAlXUUljmXRdV-JXYudldGFg2FlhB8fsnrC0n2UqR_xS-UIX2GF7yQ2YwsKLCNXlJ5b269nimZSsHvMBfIaOYxOQ4GOHYL-n0dwd-zrHxvdviimJG9RayETNrNYrtJ7GM3S_sfOGHYeNrUggzj2SAJFL3zTyLyTrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=PK5w4mOmqsHaEBQWICbylI9t8R7WW1wFwpzTEauGr3OkibSmyo2BHQeWp1AiapkQ4DtESAso9DMipCzxyqRGCNWFyIJSS85xXM_c-yR8vv7AdouMlQJTr-tY2b73iOgo1h2IW3dMVegTsINqC4ivn17pRTBEui7IB-CYgx86oEGfnvnqUsGwFAlXUUljmXRdV-JXYudldGFg2FlhB8fsnrC0n2UqR_xS-UIX2GF7yQ2YwsKLCNXlJ5b269nimZSsHvMBfIaOYxOQ4GOHYL-n0dwd-zrHxvdviimJG9RayETNrNYrtJ7GM3S_sfOGHYeNrUggzj2SAJFL3zTyLyTrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
💋
پرواز لباس غول‌پیکر لیونل مسی
به کمک هلیکوپتر بر فراز شهر زادگاه وی ، روساریو ، قبل از شروع بازی خداحافظی لباس غول‌پیکر مسی به پرواز درآمد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107955" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=NnaUFAelb_bsMQNJKC6a9kUUUD4Mfj7Ffu13HDeoRjTMFl2j4ju3B6wWazgrhQbTgGqZL4X4kC3MOCiGNQ1xbHJFcMq_0ZLUt13zGx7PM-ZEdXDcjZarF1q-ySCGn5-WU8FYOFotcQcySSAfZczgKGy1pbTUt5zkQZ7NLV0ycUVYC4VN0AnlnEor_9UzDu4Ow5fviS1l_VnTN-gElKCMsmS-4juKnazvCUxzzb0ztl58YA5rjjD2PX-ooeigkzIqyqsVa_lhkLBLD4kTXrkB4MM5SjjxajFURAedjfqJIJFX1iHCPiCfGRdSDGcZkfooZbNeAOBPxi8vGoDm9mfFPiBbNquRqvlxbKQ81VL7BJ1WgvdGjvEZSc-wyhIUZhdY6i_Y0negpu0SXjXP2xxAAS2Kt1HzR_G4KFsC_YoUQa0QufKNOfXs3Xdzy7I0-hVzlSyHP7u2DIw5ejdGJ2zPlBXf6IAAWcOjn0sg5FdgGAcYcHB34XbhH5wuJ4oQsrX0jJg3osw4EP_-jm2zasuh4g9FyiOzwOdbzeoan5EzCsp-vKO_0IfUCgQfCM4J6pFXgTx3-oBUZjYO4iJn3jC3J7Ain6VAKs5HNTAJKPsIjVevo4pObIdZRt_dSDUgSgR06DsqLLPPKyoyftMdA1B1nPwpKvd2wJ5OQKdAgp8tatk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2d316bd4.mp4?token=NnaUFAelb_bsMQNJKC6a9kUUUD4Mfj7Ffu13HDeoRjTMFl2j4ju3B6wWazgrhQbTgGqZL4X4kC3MOCiGNQ1xbHJFcMq_0ZLUt13zGx7PM-ZEdXDcjZarF1q-ySCGn5-WU8FYOFotcQcySSAfZczgKGy1pbTUt5zkQZ7NLV0ycUVYC4VN0AnlnEor_9UzDu4Ow5fviS1l_VnTN-gElKCMsmS-4juKnazvCUxzzb0ztl58YA5rjjD2PX-ooeigkzIqyqsVa_lhkLBLD4kTXrkB4MM5SjjxajFURAedjfqJIJFX1iHCPiCfGRdSDGcZkfooZbNeAOBPxi8vGoDm9mfFPiBbNquRqvlxbKQ81VL7BJ1WgvdGjvEZSc-wyhIUZhdY6i_Y0negpu0SXjXP2xxAAS2Kt1HzR_G4KFsC_YoUQa0QufKNOfXs3Xdzy7I0-hVzlSyHP7u2DIw5ejdGJ2zPlBXf6IAAWcOjn0sg5FdgGAcYcHB34XbhH5wuJ4oQsrX0jJg3osw4EP_-jm2zasuh4g9FyiOzwOdbzeoan5EzCsp-vKO_0IfUCgQfCM4J6pFXgTx3-oBUZjYO4iJn3jC3J7Ain6VAKs5HNTAJKPsIjVevo4pObIdZRt_dSDUgSgR06DsqLLPPKyoyftMdA1B1nPwpKvd2wJ5OQKdAgp8tatk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به جمهوری چک توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107954" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=XYrGMNnqhWGqgmVMjdLNhot9uxEAjemKBPqXHaJc-Um4WjO9dWCpScY7rgmla072YZEWxj-25G3cqqx-k9m4WJLtvI4Nm6tkqfgowPIz650YmOHCBCqNQ5muegiam_lAAx4CSiIuax326wiegZ7EjEWzc5XVWu6btKhg1YV0O8KTwTdaNzwEu7uOfaUFg099KiK1EBiltXfEtro8DM_4scO3UkXS_MSOYOny-t10gh1MIraQVx09kRKfmyAWDpKl_TDwzZkj-ot6EAYcaUSYqwz8FRVw6gjXFHtzuwdZXfEfTB7P_-n8Hjs1YHkdX5RwtK1CMOE9KaWxNa7gr9Jv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f36f54f3.mp4?token=XYrGMNnqhWGqgmVMjdLNhot9uxEAjemKBPqXHaJc-Um4WjO9dWCpScY7rgmla072YZEWxj-25G3cqqx-k9m4WJLtvI4Nm6tkqfgowPIz650YmOHCBCqNQ5muegiam_lAAx4CSiIuax326wiegZ7EjEWzc5XVWu6btKhg1YV0O8KTwTdaNzwEu7uOfaUFg099KiK1EBiltXfEtro8DM_4scO3UkXS_MSOYOny-t10gh1MIraQVx09kRKfmyAWDpKl_TDwzZkj-ot6EAYcaUSYqwz8FRVw6gjXFHtzuwdZXfEfTB7P_-n8Hjs1YHkdX5RwtK1CMOE9KaWxNa7gr9Jv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
مدل‌موی مارتینز به احترام مسی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107953" target="_blank">📅 22:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu0wgfukwNO-EmeY1nL1_D1Isvtt6iJ9Yrvujshe5DoyXnTA61CAq4UNR64n39VTxlZtH_Rd1NGP7M0YBXvG0eMTmlojI_-oNZY2Nyhmu5AXEdv0YMQIY_oPyfqtY7Fxea8KBpgFOeKzsiJBIVhwNHdnj96uQ_C4OltxtsS7NyLeRRFIF-hfuZfBM7VZRkMx38XbEvWxF-i7kaDZs0LIgArh4Yj9nRBeLLo2BUkfZp0sKlkQZGQApY7XAD2RaTYR8S_8KyTWiXNilmg9QFxQRiQN7nbqYekS3sX_ukYIsSHAQk9tpChAt7iKKDtyVB45_O82YqP6wpVt_tb6MoFpXj-yc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7217759036.mp4?token=MBl8W_3COwstYGUHVLs3B4uSJ4_SCXW4B1hntfo2UDHMi8P01VtcJ3rVXIq2qMh9u6uwzTZ1Fw7JXkYq0owItEfJdt-DEKj5ELJCsFxePoGB-_Scb6T-T0F1OPKQweWL-TqMjZMOZZwHYiG17H-e6MZVrn4ORmDYYwRBGzdFYq6NYWYPzNnP4mnxrbddcBhqnhfsUOcsyL1DYIL02BaB3rrYWbcPyHKqbTmj_LfrblfdH5X6nVwcGRScbhLw33mbQIWyiNh8bkmsttleWZBGqg56aXD0vsMQO8SVe5fbx0pQpuXZXnWWzsmFpKfwB9BS79hB0KdqxVnuAxPAfpKu0wgfukwNO-EmeY1nL1_D1Isvtt6iJ9Yrvujshe5DoyXnTA61CAq4UNR64n39VTxlZtH_Rd1NGP7M0YBXvG0eMTmlojI_-oNZY2Nyhmu5AXEdv0YMQIY_oPyfqtY7Fxea8KBpgFOeKzsiJBIVhwNHdnj96uQ_C4OltxtsS7NyLeRRFIF-hfuZfBM7VZRkMx38XbEvWxF-i7kaDZs0LIgArh4Yj9nRBeLLo2BUkfZp0sKlkQZGQApY7XAD2RaTYR8S_8KyTWiXNilmg9QFxQRiQN7nbqYekS3sX_ukYIsSHAQk9tpChAt7iKKDtyVB45_O82YqP6wpVt_tb6MoFpXj-yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به جمهوری چک با گل‌بخودی عجیب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107952" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107951">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=RKNjEvLnoAZSNFglL2PNsUf_QrpjBie_Zndhd3ele6I8imnHNa6uE3lgDrk5aBuKeJnevNMI8Vv2LQiWoFetQ29Q0etpYD7KHjW0Czuy-nBgXQJhWn5zx_0l8itJIY4C8jhEOSOb7K5VGGrEEYbx2-qSoTGmCNcbWZgHYDCBQa47ROH3wHXElB6Kd3d_Z68RoGNnEE-BHfGYXZkXotMsdjyhDAXC0YN1xqTnUF-sEKExnx1CppKHZ2Y_wTbcR9tiu04zznUKwcorPBT2Sd9aVYSzfw-oxb6A4ry3xxahNWYbybHPMXhO7fWFgEwvT6iOMNhB32tJFNEXD6v0k7WU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=RKNjEvLnoAZSNFglL2PNsUf_QrpjBie_Zndhd3ele6I8imnHNa6uE3lgDrk5aBuKeJnevNMI8Vv2LQiWoFetQ29Q0etpYD7KHjW0Czuy-nBgXQJhWn5zx_0l8itJIY4C8jhEOSOb7K5VGGrEEYbx2-qSoTGmCNcbWZgHYDCBQa47ROH3wHXElB6Kd3d_Z68RoGNnEE-BHfGYXZkXotMsdjyhDAXC0YN1xqTnUF-sEKExnx1CppKHZ2Y_wTbcR9tiu04zznUKwcorPBT2Sd9aVYSzfw-oxb6A4ry3xxahNWYbybHPMXhO7fWFgEwvT6iOMNhB32tJFNEXD6v0k7WU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
سیل هوادارای مسی برای خداحافظی در آستانه آخرین بازی مسی برای تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107951" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107950">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=wA-D4wPWXynqIhwZNjxLmRLPOkIAmEoqYfuc73jMJee5Sm0-lhF009muyoF8aTHHBpHHsBa1g8kKxIpWb1DOEEI75CTGcOanPJtf_usZnPd-ZjA_PjYxZxgPQXMTDj9BOW1-1GwpFyu4vFFuLlK3Zgxn_ZFDF_1IFrvtSFZkxXnySpmj-2xi6UTQDAsoUlzwjyQwPhYWQ-QaxUhFVRJ0AAohrj_KxL7I6HW_0OYDTojWQVx1GgR6t5CS5z-_vnM5UsmDdPr1RC8z34xgoz1BIcnplWMfp9WPc0Sb7W5xgnQ1ghmRpX_UxrkXmLDHuHJJGc2N_T-SmBDFgfiqpI28sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=wA-D4wPWXynqIhwZNjxLmRLPOkIAmEoqYfuc73jMJee5Sm0-lhF009muyoF8aTHHBpHHsBa1g8kKxIpWb1DOEEI75CTGcOanPJtf_usZnPd-ZjA_PjYxZxgPQXMTDj9BOW1-1GwpFyu4vFFuLlK3Zgxn_ZFDF_1IFrvtSFZkxXnySpmj-2xi6UTQDAsoUlzwjyQwPhYWQ-QaxUhFVRJ0AAohrj_KxL7I6HW_0OYDTojWQVx1GgR6t5CS5z-_vnM5UsmDdPr1RC8z34xgoz1BIcnplWMfp9WPc0Sb7W5xgnQ1ghmRpX_UxrkXmLDHuHJJGc2N_T-SmBDFgfiqpI28sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به اسپانیا توسط ایوان پریشیچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107950" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107949">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گگگگل کرواسی یکی به اسپانیا زد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107949" target="_blank">📅 22:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP5cFxSnMyGwG2M26rPQ9Yd82kVX3YmNS9bJdp24YuYfUx0IFBOGSY-0SzDNNi0i6Fge4sWG7nRuyjJQdaEwuLZ2Uks_uJ8uYqG-m9SNpETp1y2ZpB6_VVAHRZEBHFC4_VY6w9i3hIZQqg4Pn2HNFe8fGesRbqEVXH02ZGpTsl5gklcCz6uPVP6MzxYsXe88LHCUAKgn4NNSAae920THK9G7REmM2DCaPNOBJzQz3sj7X2cc8C8Wig4a00VYJY3iYRP9ZtPKyLUMc7lUxizuoZFYLv9w-1X_9j6zQiq_OGZaZTMEur4q16qAU5luqCT2972BDOAy0GbUdjEmFq4R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107948" target="_blank">📅 22:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107947">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🇵🇹
اسطوره رونالدو:
🔻
بابت ترک‌ناگهانی اردوی تیم‌ملی از تمام بازیکنان و مردم پرتغال عذرخواهی میکنم. من به عنوان کاپیتان تیم مستحق جریمه و مجازات بدون هیچ تخفیفی هستم
🔻
همچنین به مردم می‌گویم که اگر شرایط ادامه حضور داشته باشم قطعا دوست دارم برای کشورم بازی…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107947" target="_blank">📅 22:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107946">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs0rbJ8uo8vV51Rj56xxCR7SWMJww7VyFbSThlTgEYaVVJHQpUeHd12EC4Ii4LXmLOSJTQ-r4gqminayWKLuiLX0sr3yGOJU3awaOq-H_5QsXvS9IiI8Z7BDdw3QG4TV1K4BkExHB9nGtHmNXzsiHS3waFlEqS6vPtUXWW09cdkw6zKF6iY5N7YxTG0ZExf6EA4bEXePeHpKdhvoSN5wjJa6sUG9YcjceK9MQg0IxeCSmMtj02qLoQ7Kg1lfMVignKtYnlGVbuiIHhP9QoKXaCPgGvFOb0V8_mg-WPQtFoANX2iriwPN5QxGWbS4E76Kbt-0LjtoQQ_D8Nu0qKLGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره کریستیانو رونالدو:
🔻
جورجی ژسوس برای اولین بار با من تماس گرفت و گفت که مایل است به صورت حضوری با من ملاقات کند. من موافقت کردم و قرار گذاشتیم در پایان تعطیلاتم با هم ملاقات کنیم.
🔻
آن روز، مربی به من گفت که به من اعتماد دارد و حضور من برای…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107946" target="_blank">📅 22:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107945">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107945" target="_blank">📅 22:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107944">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال از من خواست که با تیم ملی به همکاری خود ادامه دهم، و همچنین از من در مورد انتخاب مربی فعلی نظر خواست. من به او گفتم که این انتخاب، گزینه درستی است. بنابراین، از انتصاب او خوشحال بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107944" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107943">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaclK2KMHF8tXljIZyh51n04bW0bLIQKJeqW1WC-nxL4hsKWZwUbj76p-qc94Z4uDpAj2MpWh8-Fs2fyapZ87Uk4oz4WhblsTv3qs_aNlpVwnDu8sMv4vh2f_ofAHfMTdC6dugCkgdVEKRv1MMWNexUgikRKCJON32mU0ltVBtkAp0P-8hINS97ZsqZ5FZUN5_HnJl8GDZBSokp-ympSc8h1fVmZ1V1NCJUDwP_vpzmbya5UPv-kVPSSPdny_SJDs6MSIle9XmoObTliALsRMKhbbmoY7VMizHEGk7DjpvrzR7287l4Og2ABeKvUfIvD1xmYvBtmQBol89xjkEtGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107943" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107942">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=b8qGmpRzoUEJs8mD29raYYEzshAoaNxZzf_3om-Jdq7HhMLq2Vis1v_8oDz9PVac14McL-JFm2FJEVeoj4KmJR6CDHoEnG0_5BzYJOVkkD7uX81sgFHAUC3L8mMXojbe1ZlLMjlpirquD-DE9APLpvV0Cl5q_g_3qQUHvtADkiLhLVoAKgoKniAChMVzLRUDgZukz1bLXMm9D9C-hC50Mm4qUv1FGURF8UHYfAsmgTp2604yCY0f9Bh-CD5PXFEZpf9VGEBhjwiOxj-SILWt4VyL2w9DCnOkeiZfZmKVfRvwAN1AS1FghJ8qrXfcMwgKgchLjhoAwkWOnuAjF-SJww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=b8qGmpRzoUEJs8mD29raYYEzshAoaNxZzf_3om-Jdq7HhMLq2Vis1v_8oDz9PVac14McL-JFm2FJEVeoj4KmJR6CDHoEnG0_5BzYJOVkkD7uX81sgFHAUC3L8mMXojbe1ZlLMjlpirquD-DE9APLpvV0Cl5q_g_3qQUHvtADkiLhLVoAKgoKniAChMVzLRUDgZukz1bLXMm9D9C-hC50Mm4qUv1FGURF8UHYfAsmgTp2604yCY0f9Bh-CD5PXFEZpf9VGEBhjwiOxj-SILWt4VyL2w9DCnOkeiZfZmKVfRvwAN1AS1FghJ8qrXfcMwgKgchLjhoAwkWOnuAjF-SJww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حمله تند خداداد عزیزی به مدیرعامل تراکتور حجت‌کریمی بابت مصاحبه دیشب در فوتبال برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107942" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107941">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=sHQBR4_mlqlUiwbFFW3AqzD65OchfV7SSJLQNYpCdx05cd9BtsYhM01HQ52RptwMFrc7JClIl_g5HJAuJgOdbeScFB8BBqpqkvnEtiZ8q2RwN09HicaBKP4Ivfcga904y3bqR_cFdiiD9snsVo3tFpwNDX7eofYKc4qhr6LCSxMtN1fmtBAykZap0euNMCIHUfwNeJAVsLsqjbqBIJhwS9ZZCSSr9WZXipNuuwdRA9MrGvX4fO9qzOWZhQD78CDY65GgkgB51x3Vyi0VtfhdMGXTekW_ZQleiNogqUHsSn2KW8WTY-kS_07Rf0b_mbiifGKVbhywqNHjGBAgcanP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=sHQBR4_mlqlUiwbFFW3AqzD65OchfV7SSJLQNYpCdx05cd9BtsYhM01HQ52RptwMFrc7JClIl_g5HJAuJgOdbeScFB8BBqpqkvnEtiZ8q2RwN09HicaBKP4Ivfcga904y3bqR_cFdiiD9snsVo3tFpwNDX7eofYKc4qhr6LCSxMtN1fmtBAykZap0euNMCIHUfwNeJAVsLsqjbqBIJhwS9ZZCSSr9WZXipNuuwdRA9MrGvX4fO9qzOWZhQD78CDY65GgkgB51x3Vyi0VtfhdMGXTekW_ZQleiNogqUHsSn2KW8WTY-kS_07Rf0b_mbiifGKVbhywqNHjGBAgcanP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشاگری بهداد سلیمی از ناداوری در المپیک ریو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107941" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=b8ByeJf7cCa-e7yh9Td80w0PClIWAEzOasII_JVWV78LQzMvwucfS7bY5C2LCqHri-94zd1prOU7z-H0jtfkNRZ-LTShU6A_jRI4bswnO86ey8FEYN7-n4iRCxC9k-DGbazMemMUmRUhnRKPc7HijWTWrxZBbEETYecsHCynWNffZOur3AeQCpgDmkfVHf5bIyVH_DjA-9ANqTzUi34Dc28Oi_k3vXqt64a38x_PLh_3KVzdrm2rKHO2RuUxqK0DhT_IA0-UkyO8EhInZ9VPdbmWXCzaogdIGS8qMH6MpP3qPU28beOM-yIuQEbOB4GpJAvIPu3PX-CgCoAF8Zq0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=b8ByeJf7cCa-e7yh9Td80w0PClIWAEzOasII_JVWV78LQzMvwucfS7bY5C2LCqHri-94zd1prOU7z-H0jtfkNRZ-LTShU6A_jRI4bswnO86ey8FEYN7-n4iRCxC9k-DGbazMemMUmRUhnRKPc7HijWTWrxZBbEETYecsHCynWNffZOur3AeQCpgDmkfVHf5bIyVH_DjA-9ANqTzUi34Dc28Oi_k3vXqt64a38x_PLh_3KVzdrm2rKHO2RuUxqK0DhT_IA0-UkyO8EhInZ9VPdbmWXCzaogdIGS8qMH6MpP3qPU28beOM-yIuQEbOB4GpJAvIPu3PX-CgCoAF8Zq0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
علاقه‌خیابانی به گزارش بازی آخر لیونل‌مسی در تیم‌ملی آرژانتین که بامداد فردا برگزار میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107940" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=GGn4WQkr8EoinzBO95Gl39zbmGWJ30ZHChcrdbkX7t4_Q_YsFOjLBaomRCbXe97GTRfFsZ-U3pbK-Mjc9Bqv1lsE9DZOS19Z7KU5wJFk2RG5L_XEbjnX-aNsTZw9_qqifKBDX3qBr30FvY64yCQHqBUWz6AY44ItVndWv60DwoxEejWc_tFhzSSya_F27ImstWdBOBU8S7mI8FQNsVAYBDOoijU1e4rXJHHW5ka36d_zD-O5J5GMk0H82LrdUInbK6zkpwsFCHtNnwWdMmRtX8yl0XnesMEtTiCDSdPIaBoSL-WA2_E4uwgM9nm78Q6AKFqQc3tca9MS4SRnLJSzeiVFwmRlV3SFYDeOvygMg9wcYtDPGi5s7Zpv6x99Uw2Hnre09oUdxr_PIN802_ZraOYYe-ZR1vnJhCqhX0NZ52LtmUDaxQOgoNvnqsrD0vcj-VU4E32i9v0Hex8rmHsxQRvwJfMWEL1xBEHmseN_GXteflIGrvIR0br-szmZU5EodlY6gUCWEjL-7xtspbfH7fbqAKCGw1K86vMj30jGVoHnLjdcpaNc-VPB6_Hpw8jVJm8s9yYT-TgX8KkDwW-Lgzv-ix8IellcWcka-V41dMzTIo4TrzAwy68gjL08Z7mPpqDCFIhiq3y2U40UYIYHUUBt7r_D1cBGt0MgbA0Wnm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=GGn4WQkr8EoinzBO95Gl39zbmGWJ30ZHChcrdbkX7t4_Q_YsFOjLBaomRCbXe97GTRfFsZ-U3pbK-Mjc9Bqv1lsE9DZOS19Z7KU5wJFk2RG5L_XEbjnX-aNsTZw9_qqifKBDX3qBr30FvY64yCQHqBUWz6AY44ItVndWv60DwoxEejWc_tFhzSSya_F27ImstWdBOBU8S7mI8FQNsVAYBDOoijU1e4rXJHHW5ka36d_zD-O5J5GMk0H82LrdUInbK6zkpwsFCHtNnwWdMmRtX8yl0XnesMEtTiCDSdPIaBoSL-WA2_E4uwgM9nm78Q6AKFqQc3tca9MS4SRnLJSzeiVFwmRlV3SFYDeOvygMg9wcYtDPGi5s7Zpv6x99Uw2Hnre09oUdxr_PIN802_ZraOYYe-ZR1vnJhCqhX0NZ52LtmUDaxQOgoNvnqsrD0vcj-VU4E32i9v0Hex8rmHsxQRvwJfMWEL1xBEHmseN_GXteflIGrvIR0br-szmZU5EodlY6gUCWEjL-7xtspbfH7fbqAKCGw1K86vMj30jGVoHnLjdcpaNc-VPB6_Hpw8jVJm8s9yYT-TgX8KkDwW-Lgzv-ix8IellcWcka-V41dMzTIo4TrzAwy68gjL08Z7mPpqDCFIhiq3y2U40UYIYHUUBt7r_D1cBGt0MgbA0Wnm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ترویج دروغگویی به دستور فدراسیون و کادرفنی؛ لو رفتن ماجرای تعویض زودهنگام محبی مقابل روسیه در مصاحبه احسان حاج‌صفی؛ ناراضی بود، گفت بخواب زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107939" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=Bp0ZQt-XhJx4_uZKiZ4jfRS3QNlFY6fsoEHLafwxjH620aNuNMGMJHMaR6xKiRuczvKuCLrwvy6aI3uQ6LiAJOCWGVctjU_IFLfPk1OEeouOFJVVi37aBhn5nsdPz6ewEnoY-ftCAeL0W076WZUOhB1mt_EkoR9hFZtMqgG8GzkCxAlyKvT4gxiYOEo_4HbbalKmAMfGZIQDk91Rs78S3NLjbO4oD9j9dNw_N5HyU4E4yrO5rgvs1Z-O7AnYh1r4zn-HbuH-pXQB_yq6LLSV3svU7sWXbg2ErUC8Ng4cOqTKSyzgmiCL9O63W9_hdifcpJly5TtU3WAIcdBBVDtvpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=Bp0ZQt-XhJx4_uZKiZ4jfRS3QNlFY6fsoEHLafwxjH620aNuNMGMJHMaR6xKiRuczvKuCLrwvy6aI3uQ6LiAJOCWGVctjU_IFLfPk1OEeouOFJVVi37aBhn5nsdPz6ewEnoY-ftCAeL0W076WZUOhB1mt_EkoR9hFZtMqgG8GzkCxAlyKvT4gxiYOEo_4HbbalKmAMfGZIQDk91Rs78S3NLjbO4oD9j9dNw_N5HyU4E4yrO5rgvs1Z-O7AnYh1r4zn-HbuH-pXQB_yq6LLSV3svU7sWXbg2ErUC8Ng4cOqTKSyzgmiCL9O63W9_hdifcpJly5TtU3WAIcdBBVDtvpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😱
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107938" target="_blank">📅 19:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107937" target="_blank">📅 19:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba2OJSTAcgDf7p7Z5TGjcOtMQzmgnf8sI4L8f3wiStOQcHhWi65ipHTTGjr2HPuySFDNEUe7HGIXkcmUsJ9Gg6hYQut2ZtgUnHA1TWfVOlO6nebaB9KSs5dKmcOsYoogCkEJ6NqkjDSfE-QMKVho6GLtVPR0piUXzVruUv71pHsp97UVo4DpiJ_DHzWzBriIrh7lX7qokcqMTnq_qjHW9rKDhwJzKMrqdjbeTgjx1R070gvqh60oeju2KIvqWmIn4Yg-n2y16qMstfEtRxpSMk1bUFvx9UZmeiW6d4LY2PTIYAxjT0qvrMSdYzkPSvcTFYdQCSTQVsq0z6frgXYCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107936" target="_blank">📅 19:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=KAc0oBj_BFpuUDVsmUFXhmr5lCbAylfcm8A8CclED42BvsNuxB0t4n1MmufG5rrDUQmYL6_0OklzCpsRrNN__Jq-Krq8JutOa-G61f6YlytI-DFfnwB1bGxhpjctO8hW4UFHkRLdIZiZEaQulRyanhhUHIS2sYRohzm11M_5yseSFJQj1RGuRG8QGesRZr1LQ80etDQ9JkNlOa11iPEYrM2X0lPqZOGbVHvhncIfLsAaes8ZRF4OsUQ_ffmuO18vdBYFHrxDS4dnGo2zgbVSGaK2sAN9LpHz4ErP9orYzoIq8JOGXN7SQYv89pd6GEnZ9yOLE7iVWvD92QvHrLNV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=KAc0oBj_BFpuUDVsmUFXhmr5lCbAylfcm8A8CclED42BvsNuxB0t4n1MmufG5rrDUQmYL6_0OklzCpsRrNN__Jq-Krq8JutOa-G61f6YlytI-DFfnwB1bGxhpjctO8hW4UFHkRLdIZiZEaQulRyanhhUHIS2sYRohzm11M_5yseSFJQj1RGuRG8QGesRZr1LQ80etDQ9JkNlOa11iPEYrM2X0lPqZOGbVHvhncIfLsAaes8ZRF4OsUQ_ffmuO18vdBYFHrxDS4dnGo2zgbVSGaK2sAN9LpHz4ErP9orYzoIq8JOGXN7SQYv89pd6GEnZ9yOLE7iVWvD92QvHrLNV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
کنایه‌های ژوله به مصاحبه‌ اخیر قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107935" target="_blank">📅 19:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=h-bciQZ5y3ROqkQDl67baHxg64B8quwHiY_6BfgPuBolJmSAVy3MArkgeR9MtyQyAj0m96bYgQ1ASp78hV6PonvHMh6QHA83TRRgn_ToI8PjYylwIrjrZ5dRpUrbCRQV-x_m4bAlLgLuKyEaTYjl_y-WR6DLcaccSKJWCHPAU5DST-_G5Bsh8BZS0abntPweWodiUq4PfO_aBQ_onamN7au-mp4cL2PXtLZDtJtryIiIqKNGp17zI3x__SNqCtSKqPjX_igF0bflYYK7yDODWzfAULfh10gmNV8kcuFhSE7oUMCnYM4B7BX5pupnw_C21nsry8BRMFeRdM7jN6zFxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=h-bciQZ5y3ROqkQDl67baHxg64B8quwHiY_6BfgPuBolJmSAVy3MArkgeR9MtyQyAj0m96bYgQ1ASp78hV6PonvHMh6QHA83TRRgn_ToI8PjYylwIrjrZ5dRpUrbCRQV-x_m4bAlLgLuKyEaTYjl_y-WR6DLcaccSKJWCHPAU5DST-_G5Bsh8BZS0abntPweWodiUq4PfO_aBQ_onamN7au-mp4cL2PXtLZDtJtryIiIqKNGp17zI3x__SNqCtSKqPjX_igF0bflYYK7yDODWzfAULfh10gmNV8kcuFhSE7oUMCnYM4B7BX5pupnw_C21nsry8BRMFeRdM7jN6zFxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پادشاه مسی:
🔻
لحظه‌ای که منتظرش بودم بالاخره رسید، با خیال راحت میرم چون هر کاری از دستم برمیومد انجام دادم، این پیراهن برای من فقط یه لباس نبود، رویایی بود که بهش افتخار می‌کردم و تمام زندگی من بود. ممنونم که این‌قدر دوستم داشتید، همیشه شما رو با خودم خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107934" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih-pFliFHsmf5p6rCRAOdh9j2R98-h9JPVGgdxKLs-DDFYs-qCrxWkm0t70YDTaMskVnJwY_RTxjhMN5VcLaL_ukUmaFJ7WnPDGRy5mAWs5YCL-SmmI8dEkr6weoArOsCteFvHj7sYzF4P6_u5xMn7m_JA-A5kMwh4opdkt0UKPHcdrkim5Bdm0xNJBineIVCuWv9jLaCZMYsOU485UkNZEzpGZN1oh4P3DLp7sOEZ6IrJgs7Et_QC4D8NST4vo8ElbwnJuP8696f9dxeQwGN4_RswEXHNrI_dT69l37BrhKnJb_8SOib9I_8_uExWRhhBcbB4O7aVr_mrwmzUvE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنی‌کارواخال مدافع سابق رئال‌مادرید به ختافه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107933" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyToZ6XPLCIabOaHrFHPTXYBv920H87Fgq9TGFxA4DiDaZ4srd1OEeeQmX7EqKj-ZF0BR3Xf4WVVvfMLA4ZdR2PehW5RiSBTEgvwlg47BdYs4r_uMbObCCLKQ_0rQJInTzYXCbM-HyUOuZ_BlKvDv399ytvm3sBVRUuVGtA94O0OXBukKcfLxI33M6n-RQ_MnHC23OEz24LOFDVvpEHVZ-yolud7Emnnu9u0PybuVh4LZD16Bi0ftAoyzBIKHpCQgCDwEFY8cHPOBe8KirLEHAGnzQAW4l0GyEr3u1qzqt9gTkHyODuyC0wZyh4jWtVIJGpWlSAD_xa-SQtfZiOS6j1j8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyToZ6XPLCIabOaHrFHPTXYBv920H87Fgq9TGFxA4DiDaZ4srd1OEeeQmX7EqKj-ZF0BR3Xf4WVVvfMLA4ZdR2PehW5RiSBTEgvwlg47BdYs4r_uMbObCCLKQ_0rQJInTzYXCbM-HyUOuZ_BlKvDv399ytvm3sBVRUuVGtA94O0OXBukKcfLxI33M6n-RQ_MnHC23OEz24LOFDVvpEHVZ-yolud7Emnnu9u0PybuVh4LZD16Bi0ftAoyzBIKHpCQgCDwEFY8cHPOBe8KirLEHAGnzQAW4l0GyEr3u1qzqt9gTkHyODuyC0wZyh4jWtVIJGpWlSAD_xa-SQtfZiOS6j1j8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
شور عقاب‌های سبز؛⁣ هفته دوم لیگ مراکش و تشویق بی‌نظیر هواداران رجا کازابلانکا در اولین میزبانی فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107932" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107931">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh6r6OneSWOudfp855FlDYiXIHzdsu6o19cSY-Xg4czmcdI7jgTI5nnpNmcLZF8urhsPc6zTHqAKMHEZR_2UdRyS_iJdQGoO46F9jLM613rcJ26ANk81IB-lwU4AvPCqr-21YJkMVfMUWQt27R-vnrF7j44AKpBkgH6IWCOipy5zrPebxhA2Cpi_eil4jbq01DsaS_WzMr9i-fIz-sqldWbuYWdUnaAjAl6Jb-N1c8OtwZdol_2JhB1KCysPQdswtaPwz6gx6OJVrbdSZSKudhv1p99B-0WcSCfD70ZA6l9dInmjFBstpVAWjGvvSXilWYZQ1urTbxcHrGgBtWaoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اسطوره لیونل‌مسی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107931" target="_blank">📅 18:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107930">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=Naz_uJ0RzG2L0HSCdfr50IaZdiNABCUj9_0rK6IGn1QyGGIrc1kxNLLEUg-11lmz_CCpFzrbSi1_Y_JN9HMSiHVq7pjV9TLQ8xPYsWoE4VmM6wxBTZItCj_fLg16Vy2cthjesn7KBCrU1pHHkRA3XDL0fJcvK_CAnGip2D54UwU1tvaJENbVWkm5c-KirobseGCIu3K5oHgzy2b8q9Wuo80wlezD1ICFlAHpS82DBRtpRrF-_E5Sj0xaScRb8APJWx2xeZZWy7L0SGKBdMRF2XE9V4ycxHpzghFY8wUJ0Y8_ru9mLWBFLLzYLKcSM-UJBzqdcjxkWyNoehjdwoFVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=Naz_uJ0RzG2L0HSCdfr50IaZdiNABCUj9_0rK6IGn1QyGGIrc1kxNLLEUg-11lmz_CCpFzrbSi1_Y_JN9HMSiHVq7pjV9TLQ8xPYsWoE4VmM6wxBTZItCj_fLg16Vy2cthjesn7KBCrU1pHHkRA3XDL0fJcvK_CAnGip2D54UwU1tvaJENbVWkm5c-KirobseGCIu3K5oHgzy2b8q9Wuo80wlezD1ICFlAHpS82DBRtpRrF-_E5Sj0xaScRb8APJWx2xeZZWy7L0SGKBdMRF2XE9V4ycxHpzghFY8wUJ0Y8_ru9mLWBFLLzYLKcSM-UJBzqdcjxkWyNoehjdwoFVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
در شهر روساریو، یک پیراهن غول‌پیکر به عنوان ادای احترام به آخرین بازی مسی رونمایی شد.
😲
🇦🇷
این پیراهن در مقابل بنای یادبود پرچم ملی قرار داده شده و روی آن نوشته شده "Gracias" (متشکریم)، که نشان‌دهنده قدردانی از مسی به خاطر تمام تلاش‌هایی است که برای کشورش انجام داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107930" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107929" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3cZKMXevEYNlHQMl8iZg8cvF7V4XyZ7AW8Dl4VObTiIHQVo4IiKSYI50_WwZuc_A5h6IGd1bTcoI4Om-zwepknqZNCgYM8hW_Y85e3sGFJIRa0ud6dN2IKyAL9PQkfJsvbq97WCCB4nUXFvXwI3zTYklZI8GnAnXuMBUbWAmfQGLCBy6trVgQ7oEJTJ3WKFxu7kdzUHOvU-10MCB_Vdr98lvoF8O45aEl-xuK_JV03dZK4eQa_AYwLWqIiEEoWYhmk4fXqFR3326YqqjoOlp7DvMfI5M7AEVxVw8qWFEXSCwjvYVSPKkgI7bWcY0pfuFX33Pn_6hKTSjzPMJUSuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107928" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
