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
<img src="https://cdn4.telesco.pe/file/RRTaupuqDauoWbi9cfF3SbNaVVYm6TlIOdDsjHS4YI-ONRs3ioEeO4ZAisRTHCMpM-JUZ-RClLNoqXFjNF2dGWXjpNc3KTaKBRFSfWggJFlfrgRy6dM81fbfcfeZXrs4PzKQC9qpJx5nF7Tlm8pKXBfW-wttNP_x8hSUcc9-QLxP9YQWT9i8Q7A0tVmXGhoZE1w67xDKGEA498wGbQ7jzHQ-Wr2lL2p3H7yQNk2wj4RRJrXUrVs6h-bR2zA8s7PHZHLP4GFz1LpzMmDNorTU9LsInhWSSsCwpElx-Sq56kZUe3yVie2fpcmKqlU4-jiXGpM2TpBC6Npmq5_RP51_TA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 20:16:38</div>
<hr>

<div class="tg-post" id="msg-673056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5814fb1c8f.mp4?token=a0dvtof2uLqPehPftXOQF17XA7TzS0MmabGaUFP3nL2Hy1_-hFK-dFWrfhY0x-zhorg8zENxud0HJUnpIg6T21vQnnXYc167wosVzZqHDCygFG9C0Q06enkBTzpTVCrGc313gc-x3T_iLCDRtI4bJzmyK-rno9nZecuqy1s0aJHwy-X2xeIbneE5loSkufnvpylKZMjwuQfHCDSX2Q1AhydIHUE5Ubl0UaeBGdAkZG6XvsBFgcemWpSl7p-pqwjfCACwms_7HV5shjJO5rKRNb8eZSJ6IkoESscMFToaZs2tupP6vjosr4vZx5CXn7wfGnFMYlz_kEomdeHYMFXlSxF-QIqWZqA_I3vCqL6JpQf-59VNvV34JcT-RToc9BLXEsYg6ZTYn2GApzuNs_sw49AYXVhzNMm20htfr311wD5rxCjPZsC8aPwiOLImqViFGDoJ84_g-RY-wS_00HenzXebYABWe3BS6L20stu-azA21p_oHEfcOUmDl8HcDY_vnQyVCABXAbQAzjge_noLbGWEy40XE7J1DI3GhXTFFCTKi8Ku6w7RWtF4_SG6w8Zde1eNgur_eOaklhQBGuMrw1OGqgZwTZjI-RJ4vceURtKzpNG0L8SVL0XOwgBFuCeICkQyTsRBq3QIF4-3RqeJOAE0-Wqkmt0Md5gIJj1Pnxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5814fb1c8f.mp4?token=a0dvtof2uLqPehPftXOQF17XA7TzS0MmabGaUFP3nL2Hy1_-hFK-dFWrfhY0x-zhorg8zENxud0HJUnpIg6T21vQnnXYc167wosVzZqHDCygFG9C0Q06enkBTzpTVCrGc313gc-x3T_iLCDRtI4bJzmyK-rno9nZecuqy1s0aJHwy-X2xeIbneE5loSkufnvpylKZMjwuQfHCDSX2Q1AhydIHUE5Ubl0UaeBGdAkZG6XvsBFgcemWpSl7p-pqwjfCACwms_7HV5shjJO5rKRNb8eZSJ6IkoESscMFToaZs2tupP6vjosr4vZx5CXn7wfGnFMYlz_kEomdeHYMFXlSxF-QIqWZqA_I3vCqL6JpQf-59VNvV34JcT-RToc9BLXEsYg6ZTYn2GApzuNs_sw49AYXVhzNMm20htfr311wD5rxCjPZsC8aPwiOLImqViFGDoJ84_g-RY-wS_00HenzXebYABWe3BS6L20stu-azA21p_oHEfcOUmDl8HcDY_vnQyVCABXAbQAzjge_noLbGWEy40XE7J1DI3GhXTFFCTKi8Ku6w7RWtF4_SG6w8Zde1eNgur_eOaklhQBGuMrw1OGqgZwTZjI-RJ4vceURtKzpNG0L8SVL0XOwgBFuCeICkQyTsRBq3QIF4-3RqeJOAE0-Wqkmt0Md5gIJj1Pnxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/673056" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای صهیونیست‌ها درباره رهگیری پهپادی در مرز با سوریه
سخنگوی ارتش اسرائیل:
🔹
لحظاتی پیش نیروی هوایی این رژیم یک پهپاد را در منطقه مرزی با سوریه رهگیری کرد و تحقیقات درباره مبدا شلیک آن ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/673055" target="_blank">📅 20:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سناتور آمریکایی: صدها سرباز مجروح وخیم در جنگ علیه ایران داریم
سناتور دموکرات آمریکایی:
🔹
ایالات متحده به‌معنای واقعی کلمه صدها سرباز مجروح وخیم در جریان جنگ علیه ایران دارد؛ فکر می‌کنم تعداد تلفات به ۱۶ نفر رسیده است.
🔹
بابت موضوع تنگه هرمز باید بگویم، قیمت بنزین اکنون به چهار دلار رسیده است و رئیس‌جمهور ترامپ هیچ برنامه‌ای برای آن ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/673054" target="_blank">📅 20:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان خدمت
🔹
هفت سرباز نیروی زمینی ارتش، در حمله موشکی به پادگان بمپور ایرانشهر به شهادت رسیدند. این حمله که محل استقرار سربازان را هدف قرار داد، شماری از نیروها را نیز مجروح کرد و بار دیگر داغ جنگ را بر دل خانواده‌های ایرانی نشاند. نیروی زمینی ارتش ضمن…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/673053" target="_blank">📅 20:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJqF2mPpiwafw1h6fBpv9U891Ghkl5RoXsA63Iy7WrA_ac0jrWFrLfERNoNkxfTyAgsr6wX7eW0HWYHN705Ow59herhYtyBXh4q5Pp3bothl9sBVeVTALfqBhRGJvaKM16uXbF75T9YacUjXSkiPoAJuENH0wHYi-ScGq0IrJd3rGK5ysZU8uz4YV1FWHsXe17KOc8v1STwM0oUTvAaOcJsOkbxUAzxi63NOz6N1k41wlHUc_0VYOTWxksmTT65xr6Un_mS9Jme7OTy9fb8kRCW4cRiNDaNgBAMv16vP1C0mntgyi_kSGsfNArTi-dsEn9NlGrg-JsJa2-vNWUxpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/673052" target="_blank">📅 20:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9fd7ac1b.mp4?token=VW-Ti11J8162Mgn19D64CcrlubLnpVmhX1-7VCivtxrcFueX2x0pPMRX8jbAzzhqQtHi9ftPG_hqWBvaZFd-BWUXHk1LUJ7AWqdSc6ZX1ZVfzPXdi_xkiK3mH1X-6GXtFbSFAPUvEKjsdYsG4sZsuSD1P-Megzsd4l21E5RFXozksI1YEqk_Y_8mYrFJLRGh549NgYADS0r3EUfEScB2yZYAWdxpbSHWGb9TWn8eOyFMDxC50LZGgm5N05ic8KUY4OtJhdenUlbX9Oycf5LkIbuB9IKiSzZQjfmED-ScjuujyPt5SQke7cQxcJeyzL3fGvkEf3mb0sNh_maPc8of1FCujxQRAzDjoIFmWaiiR-jIoLH3kkOtNEfQ7HBZ9-L7otaEuDvbf2ypxd8YI8mMAyClJLG1cOaPArzENLiPqgR1PMQBolcT87_qZoDHbcwqL1BEuZqwxt0mdApx9LFUwUQVCb3NxDgmwMXBmDaZO9YsVyIxUbEzN7kLw4OXjzPE3Y6AGo2DEof7wtTTYu5rLmyCAmB1YG_AtpVo4J39KXLhsOphJRfeqeiXsyd3uGHL2dP1fUFVu0cCv0W0ZHVsZE3O7sdtxqOLRJxddXry1MyfsCzBi5l9Oza4WI3WfundSz8zJVxKNdKebMewHXS_rZYM8hs-E8S5TvkS_K_UkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9fd7ac1b.mp4?token=VW-Ti11J8162Mgn19D64CcrlubLnpVmhX1-7VCivtxrcFueX2x0pPMRX8jbAzzhqQtHi9ftPG_hqWBvaZFd-BWUXHk1LUJ7AWqdSc6ZX1ZVfzPXdi_xkiK3mH1X-6GXtFbSFAPUvEKjsdYsG4sZsuSD1P-Megzsd4l21E5RFXozksI1YEqk_Y_8mYrFJLRGh549NgYADS0r3EUfEScB2yZYAWdxpbSHWGb9TWn8eOyFMDxC50LZGgm5N05ic8KUY4OtJhdenUlbX9Oycf5LkIbuB9IKiSzZQjfmED-ScjuujyPt5SQke7cQxcJeyzL3fGvkEf3mb0sNh_maPc8of1FCujxQRAzDjoIFmWaiiR-jIoLH3kkOtNEfQ7HBZ9-L7otaEuDvbf2ypxd8YI8mMAyClJLG1cOaPArzENLiPqgR1PMQBolcT87_qZoDHbcwqL1BEuZqwxt0mdApx9LFUwUQVCb3NxDgmwMXBmDaZO9YsVyIxUbEzN7kLw4OXjzPE3Y6AGo2DEof7wtTTYu5rLmyCAmB1YG_AtpVo4J39KXLhsOphJRfeqeiXsyd3uGHL2dP1fUFVu0cCv0W0ZHVsZE3O7sdtxqOLRJxddXry1MyfsCzBi5l9Oza4WI3WfundSz8zJVxKNdKebMewHXS_rZYM8hs-E8S5TvkS_K_UkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدونستین ۵ مکان در مشهد که رهبر عزیز شهیدمون باهاش خاطره داشتن کجاست؟
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/673051" target="_blank">📅 20:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای الجزیره: ۱۴ کشتی از تنگه هرمز عبور کردند
ادعای الجزیره:
🔹
طی ۷۲ ساعت گذشته، چهارده کشتی در یک گذرگاه محدود و گزینشی از کشتی‌ها و نفتکش‌ها از تنگه هرمز عبور کردند.
🔹
طبق رصد انجام شده توسط واحد منبع باز الجزیره، این حرکت شامل عبور ۳ نفتکش، ۳ تانکر گاز مایع و ۴ کشتی باری بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/673050" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3Wdkm8T060eT1Cx24yx1w8zmz6o5vZBqDWS9hx4StBMLDWXpvwX--MUv94UjQHd82UkXh4NoxG1dfwsmclh4_SLvdvhjhKZUTn-rWkT7_vCspJtVEqiZHpFLzKgm56ZbOgI_8phPYpejH_XYtU-DJAH79JE_8xQjy-txXdr6rzGnRZQX_lX3XWpijq4dW9t_BOuEfmN5tGeHZp9-lZERlk8TVkXmhkapUbw3_leJhPt-rQ-BMm1vr-lPCByTdW0gftCkos4cW16nTru5dJyLifZQ1H8gDGxrtBlVxRuY1xZ9m9hKAV34f_HpOWfcT6ioTJNDQwYkZPbO8Dr2KAwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxA5lTsRSdDkeOoOkaSdAHAXBgXpPwxEzUyL-TI-Z9o3U1EMRWVlaDVgfhzI63hn5pnu1OIoI7xkUR29XT5s8stcEjXvB3k3TJXU13Cvl7hQIB_QIidwcJ5ho93snLPRs7Fc7eklaWCD-iHR34pXMtwSAvShTwfQsbiO2PsLNK-SIrEYrNTFLfGiDLxXB9p7aq0D4F-vTWdIcmpsN8yAj4HbfKzu3CSxq2mHesBlEkA-T8frwYdvGtyGzJPZaeMYO9ESth0PpXt5ag-YQjRsCcS7J1EVgzirkDNYfk6CKoJXwTMJkqfTCe0WRW0XHJZx__cubpebYC-qrfhYlXB5Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر بخواهی فقط یک کتاب عاشقانه بخوانی، جین ایر بهترین انتخاب است!
🔹
اگر فکر می‌کنید عشق باید بهای از دست دادن عزت‌نفس باشد، «جین ایر» نظرتان را عوض می‌کند. شاهکار شارلوت برونته، داستان دختری یتیم و سرسخت است که میان عشق، فقر، رازهای تاریک و انتخاب‌های دشوار،…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/673048" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaavt_FlK6ELoC7zJ39H6uPg-jilb6sVxhVFXXmSTM6-pGpH5ZuUaQYUMlWFG07lA6PgmQkazNnPVpIpL-0X35HwZ34-X8E7N_dE9ZZqiiZkmNvuiLwv08-KE-UdfYjMJIUmxtOzAsrKrPeAtgakDjFciANxqO2UGlo2htIkr_SYhfDvFYSpkThse2bDM6MWK4o_JfcHgb0uBX1miCVauVuOn6qbcWypZcDNNmPgmggldOQVdPhxePkjAm9clxLnq440ME98N8CzIxXh8igwGMrRSj23nMW67iP_8gEIdjURZw3hw7fGE5DfoNshYfBEHwhc8Vu0b7soaZVe98iwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر قرار بود فرصت صبر کنه...
اسمش فرصت نبود
💎
طلای اقتصادی از ۳٪ اجرت
🏦
بانک طلا
🔄
تعویض با عیار ۷۵۰
👰
مرجع سرویس عروس
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/673047" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1c0_a7NI4PrsZ0Qle4ogXpEoD6sjxgcJoZEcxwsJOeEQjLWc6fQ17DMxNO7owt6IU_Nv5zk3d7xVYnLEqscvAZrmPTLnPnCg3X2kLaH7J5z8HAhOe79RXU4LCcqD39NiyUXcpTb2vcyIVwMDJHObrt0B_q5IuIfr3QrMN5RQDTsg5BYgk5ZqfWKdTLYWdlDsGGenpgqzTYzb4q9K9BICiUa1RqTOpPAmZC-E7a60jqPCsuxaXn2jaVXT1vLwDNMoyTtVnjPN8X1nVe2NseXdsVqSWd4WFBGKeaj2hpKFqd7t9kcpB3p36fKi61YZUMz5JJMOTw-Wlg_YzZ5RimgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد متجاوز MQ-9 با آتش پدافند هوایی ارتش در منطقه غرب
روابط عمومی ارتش:
🔹
ساعاتی قبل، یک فروند پهپاد متجاوز MQ-9  با شلیک موفق سامانه‌های نیروی پدافند هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی در منطقه غرب کشور، مورد اصابت قرار گرفت و منهدم شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/673046" target="_blank">📅 19:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060af6ec9d.mp4?token=OR1RmoqwudXJI40wrlmiqKsRKwwO-wkizPK3ZkccBHMh9t723P466-UCxYvb1UTcEhTjGfvhzehBWEvLwBQgXSOvw9PfDOJTavJNkhcoNOJ54_5hp6qc6hZcmChdA7WkvWZi79OK7gOXlXv9nncD0KAl3lSVIn4X5PMro--5oImZSnuzjPeDN_8E8E-04matlV83mpVjkCe10CNcqmxr3yvRNF-apNkr8WxT0Xn4E9OXe3UJGG_NouTQ1XpckyXcTk7hpBcybCudNG_RDmX40vibzcqiZFssML9Zd3ZbBQsjAyMa8rkCVng3F9s_KqW8MZCh_m5CGCxcSMOWu9-1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060af6ec9d.mp4?token=OR1RmoqwudXJI40wrlmiqKsRKwwO-wkizPK3ZkccBHMh9t723P466-UCxYvb1UTcEhTjGfvhzehBWEvLwBQgXSOvw9PfDOJTavJNkhcoNOJ54_5hp6qc6hZcmChdA7WkvWZi79OK7gOXlXv9nncD0KAl3lSVIn4X5PMro--5oImZSnuzjPeDN_8E8E-04matlV83mpVjkCe10CNcqmxr3yvRNF-apNkr8WxT0Xn4E9OXe3UJGG_NouTQ1XpckyXcTk7hpBcybCudNG_RDmX40vibzcqiZFssML9Zd3ZbBQsjAyMa8rkCVng3F9s_KqW8MZCh_m5CGCxcSMOWu9-1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حال و هوای نیویورک در آستانه فینال جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/673045" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf41133bf3.mp4?token=t_70tpAvTED7GGfBPRnZ8OmheeU7kcSALpFKM68WHJsEOM4Fxnd2mtxEi9SUgld-WkXAGRAAI-lj6ezl7mVkXHRwCGvwBADslIZDOMk8483XS9OHOrEvaGQppkHpQhHEc51A-7AhCe3B6Ze82Hr5WmOqJ_40p84j74uUWnaJhD4zDPpVlgmwLU56GubTiBJpNZAZMpm4Tg6AhpjlZprh0UKEc6g8HztTVR8qSh85rpnthzlGqDDOALXkEvfhNWxgakolqTAGVYvLEPTh-mSYZJFFx2psMyEFKLBcl6tBgC6130-qmqP45c6oyc3IRbhkJCHbQITfZ0ELTpybC74Wlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf41133bf3.mp4?token=t_70tpAvTED7GGfBPRnZ8OmheeU7kcSALpFKM68WHJsEOM4Fxnd2mtxEi9SUgld-WkXAGRAAI-lj6ezl7mVkXHRwCGvwBADslIZDOMk8483XS9OHOrEvaGQppkHpQhHEc51A-7AhCe3B6Ze82Hr5WmOqJ_40p84j74uUWnaJhD4zDPpVlgmwLU56GubTiBJpNZAZMpm4Tg6AhpjlZprh0UKEc6g8HztTVR8qSh85rpnthzlGqDDOALXkEvfhNWxgakolqTAGVYvLEPTh-mSYZJFFx2psMyEFKLBcl6tBgC6130-qmqP45c6oyc3IRbhkJCHbQITfZ0ELTpybC74Wlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب بچه نداره، همه مردن</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/673044" target="_blank">📅 19:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673041">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHZymOrUsq_MBw9vXwgfHvA1unn0x5xIf2efc7MNF9p40K-QcmT81RxuTgLNdrrPrWEgSLLBhOC8j8p6zubtH2iyreOA_GxX9DCgk4wjrop4NOXuy5Qjxv4g9SGZ-W542UM4KKXqqax-ne14BQltclRp3DeabMwWS71_bWw9sfquN-jLHfsXxoT7PdvLCdot5F53OgwU8WdLRHPVj0Lh3_rQYmeGqn0rIoVEtxw55_ZiGQXzu19H3AXswU0e-YwHIzsQAwiY4S1JLWPf7LaBPSHa5bw3HhHB6KHtp2ogJFcavrcrnzPGkGUMBK8E8LZkyzr8iFecnMIvOMetqgfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TU3m_IyoZY9_J_amlvZNdnUi7JR1M8yn9KUT3-1FXDDFeLbTkfvsQkDtCbRZlYT4CyU2vaIlkFDWm33oXXhOBcHbzvf1HITr5MXTTGb9mT5oT6FnecXXs5DAs16zzjAg2yIfCaZPSHxINMa5aMP6A9UOijx8448inQML5qlt2wxMfX6CBaciazR0xg36p6N9QTSMFWU_926XCkHwV05YHt8ClFJhdvBBNGedbnLyvTYnRc7tvaPi40lNgWlMX4T0dCFxZBsUQ4KOg3qRxY9EL_sW2BQc1RrtuCJoRJHHfrSrTChpMD6l0MdqWC5jkJAyDPbRmTlPrr0hfeUOlJWOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ent1azUZrtNdCGgr70gZXE0NZBYDfSGs3wFXMEps_p3HsAiznVIeZWhvRosyKOTMTpqFfnUgDZrB1_baVADAjfJe9GcT7Skbe7hWDs2qhW-9LpRmZ3LEdgvt5ICw6URQyA61D0LtjPQ7UexqPsYHeaDjqtNvOt1q89CJ6aKZ2GG-i6JVOrbxbv5xz-KIHFWRj2WddGvflQFGDWASumjVqXfR5GdsVIBnNDp3S2SEAuKSr4NeLFy66-GAa5aB6OaZ3eE2sYm_qNyeUyNgPbsCb1eoicvSijhCFjFp2KT6J_3XpG3y8kOK8XA4Xv7DFFI39L9yvR46F2o5WZmyDlgJqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تخلیه هواپیماهای راهبردی آمریکا از پایگاه «العدید» قطر
🔹
تصاویر ماهواره‌ای نشان می‌دهد آمریکا برای کاهش آسیب‌پذیری، هواپیماهای استراتژیک خود (مانند سوخت‌رسان‌ها و آواکس) را از پایگاه العدید خارج کرده است؛ اقدامی که اگرچه ریسک را کم می‌کند، اما با افزایش فاصله تا منطقه، کارایی عملیاتی را کاهش و هزینه‌ها را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/673041" target="_blank">📅 19:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673040">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHQs6yZ0gSqsNStfh-cXRgNYHbbEO6R-etcE52-fumIVxOIp07NsqBAvnSJFVx_PQK_5wUJfO678NW9kkGmIWVw6rsFp1-6qokbrqoLREK3HpX79vHZW3zIRFLAaYH4Y-QQtCtsgkVwBv48pDeBFzdmkIxZ7_qvKzRKkifOKL8r2rgHsxDNX2XQhv_II8PGbfcM4QIZbo8FOL9MZaxYyLa3yEoMth0_mKJTPUr1DI4s2C1IdwqzHIAJjYYg9JJUqbk4yTg6DH9XDSd6NbjqFc9jDIQpd0_qHV4T3oTcfsLoVjFRmZCaPOLJDIm4ne94bIdDju-VFnVW7GTVqeSufaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار پهپاد جاسوسی در جنوب کشور
🔹
این پهپاد شناسایی و جاسوسی بامداد یکشنبه ۲۸ تیر ۱۴۰۵ توسط رزمندگان تیپ ۴۸ فتح استان کهگیلویه و بویراحمد در مناطق عملیاتی جنوب کشور مورد هدف قرار گرفت و به طور سالم بر زمین فرو آمد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/673040" target="_blank">📅 19:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673039">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=ZYkzObb5ql2rZl56rnqj5hx8fAdjZ8IrpzAlMiH79CQkUBwgSKCHZn5aVRmXk_xqs5S1ViiCewhvCgJaIAqsrZ53di1jxZlJqrgFyVRm5uiGcDc9xa8wSctoP6H9K4o_-gZGWuw8bhGHJZJy7WOlFDwGdao29a9P8uzGFvsR5M_txJPku4cqbMUIrq_oCpQSQrK38jydAS1fHM3IxBSb22PNYEWQ00QoOCJp7vCbY7Nuc8HdYVrPnlFIuS0o8H5Slgmjo8Oftj4yy2IBfpU4JKxGWzm2J2_5aRG2-EkUVjC9_rLk6INnZc84TdJ2pinSLcaUqjNxfU82thRwrPJR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=ZYkzObb5ql2rZl56rnqj5hx8fAdjZ8IrpzAlMiH79CQkUBwgSKCHZn5aVRmXk_xqs5S1ViiCewhvCgJaIAqsrZ53di1jxZlJqrgFyVRm5uiGcDc9xa8wSctoP6H9K4o_-gZGWuw8bhGHJZJy7WOlFDwGdao29a9P8uzGFvsR5M_txJPku4cqbMUIrq_oCpQSQrK38jydAS1fHM3IxBSb22PNYEWQ00QoOCJp7vCbY7Nuc8HdYVrPnlFIuS0o8H5Slgmjo8Oftj4yy2IBfpU4JKxGWzm2J2_5aRG2-EkUVjC9_rLk6INnZc84TdJ2pinSLcaUqjNxfU82thRwrPJR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت در مناطق مرزی جنوب کشور: ما به لطف قدرت نیروهای رزمنده فهمیدیم باید از چشم در مقابل چشم دشمن عبور کرد/ پاسخ حملات به پل، دیگر زدن پل نیست؛ ما از زدن تأسیسات و نقاط مهم میزبانان دشمن ترسی نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/673039" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dedf68ea7.mp4?token=JUv_4FHy_7ugC1S_zJ5xA6h3LnXMDR-MpENpZSkred00dZuCcfOuCtCyA6dx25LpfxE4tHK9l5JFDYKxdAd5kyt-k6OOnKYyN3rE2j7HDIrr3x0uKPmETRzePd8aDmr1SvEDdUvyGIQO7FcjnE19KN1kHIFBSxNuUFUj-N2EUy9gHmM21PYsBZK6_FdMc_DI8Ff7Fcgw_Zw5ebag4jJd2dEFavqFGk2GexSHBXiu2VK7M8Yvtjev8Pj9C9nDwvHDXfW6gQPwuIfMFILc8bHSrPVGJsW_x4XQlyVzOOguxM21Up-Dt7TUXsIuF31ZSCgO3RU9GJvH8x67dntXUSl9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dedf68ea7.mp4?token=JUv_4FHy_7ugC1S_zJ5xA6h3LnXMDR-MpENpZSkred00dZuCcfOuCtCyA6dx25LpfxE4tHK9l5JFDYKxdAd5kyt-k6OOnKYyN3rE2j7HDIrr3x0uKPmETRzePd8aDmr1SvEDdUvyGIQO7FcjnE19KN1kHIFBSxNuUFUj-N2EUy9gHmM21PYsBZK6_FdMc_DI8Ff7Fcgw_Zw5ebag4jJd2dEFavqFGk2GexSHBXiu2VK7M8Yvtjev8Pj9C9nDwvHDXfW6gQPwuIfMFILc8bHSrPVGJsW_x4XQlyVzOOguxM21Up-Dt7TUXsIuF31ZSCgO3RU9GJvH8x67dntXUSl9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام موسی صدر: وطن را نباید خرج بازی دیگران کرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/673038" target="_blank">📅 19:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlKdLgfT28ggr3YAkhGqPfnKl8sLLVClD4WXNSLglQsAlU6rG_C-n0lvkL_0Pfead1x3slcvHt6O0FYjc-h5jx2Gda9GXeo0Wzx92ndssT45-aH--VhmdL-i-WoSw1XMh3yMv4bFeBnsbBiGtcN39dGxBXcpHZCRDlXyio_OVYpSTGGHfoii22mCKS8p7waJcqS2TSDpTR_OOAiwDfHzOCw5ZUy-4jI0tTjMdicHRhLiaBaTYgqJElB4wOAOD3RiXiNN24oACbmP576yGTDOxj4QIp9S52EC5GVq4PfMSiPmKw9JTIk1lzlV4FgghTPWcOwAxdDOq9_5QkL_hfZBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_lmbKtMgpSDMBeDKo5VliLaBi6QUNfvxylie6mW3SH1fL8gdoOI49T77wF-hzfJMU8CfUXMouWg_1BdrP-9e-EEYN8tTLCCs42Be0EdnbuBzB38bQic8qDa1Drwa-M4pEJF5t-eI9oI7ZimJUbF1kixk1986Px9vJOHdhu3jpB4bbYwzeTPhq9nk5hXuzCtDwEnbwYgRsJAFC666JHp-z7qwqPVkC3P3erGMQV8gF6kH40uGWXOd9P3pmcdRe6kfHJ7K7VUiTXEj4T9_PqyB5xgGNrnBZE9QRzZ2wqD8qP-VMmzhnkQafkMhTNVX2vcpEnauFPJLEsvkczlGpwuLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در پاسخ به حمله ارتش امریکا تا کنون غیورمردان مسلح ایران به پنج کشور که پایگاه‌های آمریکا در آن حضور داشت حمله کرده‌اند
🔹
اردن: پایگاه پرنس حسین
🔹
قطر: پایگاه هوای العدید
🔹
کویت: بندر الشیوخ
🔹
بحرین: پایگاه پنجم و الجفیر
🔹
عمان: بندر الدقم (مخازن سوخت ارتش…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/673036" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npZfWURcE8QByTSIQRTt2bqz118yme7ifqJFna0W6LUgEKP4SVv-j7PnvbouAhD5o9iq-G0WhLlORcSJwW5ZTbWc3d-qt-S3t9-fiP65gNuKJXyjRODcHWITTJgo43NBbAnRPFhw6Ypa9kePC9jFeeEPwlKEyfXlMG8bBwEV5ys0qKWzpqN2Bz3jI8qEUD-A7CrRLTxsGWHbDdriWWV57vGtLzD2u0n7Qq317E9PCvysM8STVqy1Qzcd95gYgAFEkY0EJ2r2u6rGldgevPQ9x_ho2kMIOqW7oylkDuSUdj_hcwH21p4mw76WNLYOZU_U2JKuJyA1JcsfvaPLjaIuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی انتقام از ایران به خاطر سربازانش در اردن شد
🔹
ارتش تروریستی آمریکا در پیامی که دقایقی قبل منتشر شد، ادعا کرد: «حملات جدید به ایران با هدف مجازات فوری سپاه پاسداران به خاطر حملاتش علیه نیروهای نظامی ایالات متحده در اردن انجام می‌شود.»/…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/673035" target="_blank">📅 19:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673034" target="_blank">📅 19:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KNs5qv7FyjI3g24GRCxRpVaROQOUtXexvYZmtkaYMERoRCnpjSP5fX55xrKiZMDFUgX29Z4gYWuWpjrVYcVLqVfNZZKxuijJ2JRcvY9IVIg-Y51vNY1I5wP7MgNvZNSmrKja1pwbtYq0HML9EaDKq4ivwo-4CN6A94SzUL-6uzvKb4orCEyVfPUexZOgOe9AIefJDuS-nAWlQdkl06Etqe_HJC9V_8e_E2lcWwtfDrTkawVXNQqlfjUEApWhktn5Uuz_DPJviCw-tPjdq_PihszPWZQLOVRG9BUZmwkyDvVn8yQY09a_TFJciu7r2N_R3NOivRs_QtZPdMJzmr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RH1HKyvTF6oIOdSTqawUpysD3utoFH8bSmNZeZTxscSP4pXO7CvibKxkwfXoal7UNU9zmZhnuH09wMYEMmXnvUz7fvaDFfcwV-UeuAxVpk7UUO44DGAXUDnx67OC3y2oIpmgKO1GIep-7y54ikN5_5X_zhsja7i-nNU6uBszAnWV_apN1h-sSFKHtS4Tlqazn10OhKPMRBIXy0NxTKrUDm2wlgCE2LE20zVVo76Eic9-5qwwr1NyjLlZWtjcaotSd2tBFI8r0aJscNzqwKy2fNF2ffSoI-fBf5v2Q2QRsYpTflOPS4kDH2JYwUbd9ulvogVrqrcZhXxLEydV67Q-OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر لحظهٔ پرتاب موشک‌های خیبرشکن، ذوالفقار، فاتح ۱۱۰، حاج قاسم و پهپادهای شاهد در موج‌های ۱۷ تا ۲۰ عملیات نصر ۲
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673032" target="_blank">📅 19:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjHTdw99FDtod-jCES1YPMkirLlDa8AA6cYcL6c9z2HigGtLOfk3gHjz_wwohkYRtDZRlqMc6uQpEKnf3aEZ7kt99_WrWeypqVaIAI5_oJD1j8-08jo0MTnjVSVOaTXxLSLhsunUH7TvnTxy4Y8nPYjo1a6IlTbbdRS_ASfnHfbXbjdHIiWMlN-kD3Cij0vGEipnkI7WDF5RTey4dhlhZXGywSXTKy0B-ZSSquIRgtSX36mNukpSX3IpoQ9Giyrl4Qn0AxfmpJ2lqlpHgH_Xb5F31GB9JyyTQLxrMkLu_grvl5dYT_lHamK1kE7WlOpyxiOfu0QbnX6_9PKRR2Sv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664f982649.mp4?token=aIG_SVTqZ-7cxfuGA2poMPyFyHjbDBEXGnWtFQOsPPL2rgdGLbzm-XC87NyaByEgS_PXTYnamD8Vk2p1SEeBV51or8h5WY5GtF6m0NeGW6iXD8PI2ZSxd6CaIrvsQxoBOPzNXbYI2sa9k_UoqBHlhfSIW3A4EcImNhiU11AF-K0YimFkTyBrnSoEcyQ1IBCfiO9oO2M6x5uXI4Adbkm8NAjrOvaOwtJVh0MRbn5t2z7BZ38B821orTc8AsTyTBafg_P2zSpkrHUI09VgHi1o45wdcQGFMuBbdUzkgKN9WWc94lGzRSZuk43rsLiO_-94Hm_7dX3PjjOmabfywGXJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664f982649.mp4?token=aIG_SVTqZ-7cxfuGA2poMPyFyHjbDBEXGnWtFQOsPPL2rgdGLbzm-XC87NyaByEgS_PXTYnamD8Vk2p1SEeBV51or8h5WY5GtF6m0NeGW6iXD8PI2ZSxd6CaIrvsQxoBOPzNXbYI2sa9k_UoqBHlhfSIW3A4EcImNhiU11AF-K0YimFkTyBrnSoEcyQ1IBCfiO9oO2M6x5uXI4Adbkm8NAjrOvaOwtJVh0MRbn5t2z7BZ38B821orTc8AsTyTBafg_P2zSpkrHUI09VgHi1o45wdcQGFMuBbdUzkgKN9WWc94lGzRSZuk43rsLiO_-94Hm_7dX3PjjOmabfywGXJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
پک استوری ویژه شهادت حضرت رقیه (س)
#حضرت_رقیه
(س)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/673028" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473ab0740d.mp4?token=Nqb2PMe2pTXA8tq-0QoWw5AklBnww0q7Z15wWAvrzs6d86jHGqBl8vD4Lg9emvDvKpYlSpmOWRYu7yEbaRpSU7Zx6fAAaZgP1-yat7HT-NjJmuomyZzfzY-C3_kpM7k7BHCBeBQx6hxMQ_s3GPSzAm7V73GPHWCSknUOP_Vdh31KJal02TtJvTDNXSrbKD516tWY3VdHPG43KOV9mmoYaZvvFqH06oi9IeDPelfv18fJKz73YZU0wctwJj_4GK3_HFQhpMLHBv-AkbFiLr1v_HuO6h9_MdpBPAo8n95I_gamV7YoxHPlibcfHxlQV52-_8tZZqJvd6MifgjkkBTdcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473ab0740d.mp4?token=Nqb2PMe2pTXA8tq-0QoWw5AklBnww0q7Z15wWAvrzs6d86jHGqBl8vD4Lg9emvDvKpYlSpmOWRYu7yEbaRpSU7Zx6fAAaZgP1-yat7HT-NjJmuomyZzfzY-C3_kpM7k7BHCBeBQx6hxMQ_s3GPSzAm7V73GPHWCSknUOP_Vdh31KJal02TtJvTDNXSrbKD516tWY3VdHPG43KOV9mmoYaZvvFqH06oi9IeDPelfv18fJKz73YZU0wctwJj_4GK3_HFQhpMLHBv-AkbFiLr1v_HuO6h9_MdpBPAo8n95I_gamV7YoxHPlibcfHxlQV52-_8tZZqJvd6MifgjkkBTdcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از سوختن منطقۀ وسیعی در اردوگاه گروهک‌های تروریستی در سلیمانیۀ عراق پس از حملات اخیر ایران
🔹
گفته می‌شود ساختمان تخریب‌شده محل نگهداری سلاح و مهمات بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/673026" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCPfHuw_2wSD6-zBaACMucmpdIKAMQxu-Rp-XWHVLKtTq1lM9xIpG8eu6JMdfDBDQRGix0EBzWKRDUac12y20Ubac3fE-VREkZd8IclK5QHUXyTmZ-LEUzBTgM21Kc4RgoSYTNDKCzxEJb1XtXb028TDbcgQp-OeOFnMWRrvRBDnUXu87d13zR4gGkgcDswKhhWQ2sXsLwi2v9z45rYgv3yEK_5a_c1Ya0nSEg5CDeFaeNU1RkyNE_qvIqsq_WJUyDVvMprWKwJCtQGCjp2tEJyGR13gxZXZeEB1Pu0MwtoOSzsYFE6wNVoXaEW5vIE4A2TEECldl24YkvwUTwK2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین حضور در فینال جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/673025" target="_blank">📅 19:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673024">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-text">🔥
تابستان از راه رسیده و همه نگران پایداری برق هستیم...
🎥
این ویدیو را ببینید؛ شاید زاویه دیدتان به زندگی تغییر کند، ببینید اقوام ایران برای حفظ پایداری برق چه درخواست مهمی دارند...
⚡️
"با ما همراه باشید
@tavanironline
"
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/673024" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0yUtjRCe9IPYZnn9DlBTKsH1Bb1w2EtRJxJxjum4m-1C8KQFE_j_MB7s4bmswlc7-v_7JNJq58BVhqLEq98Fd9c5fJUlhTIH_ijWIqRTLmJK6zxlWaRcxWBBfrp_tQDLYMfOw-JMnr3q0EnaDpqjUhJpQq_BxmT1kqcYJldMmNWvWZFNINvDUQ5iTxEvW5MY0TW6VhNIy3aKmXxS-IWYBzt3g_mhrJnDKxjdWxeklNAzHHq7GO0EzMKYJpiwysaVAxFsA4c059pZBUiVZOsQXOeiJ6r138nSlH4MJZZ8bRU0aAfXg6SpQrEszrSPW_F1IBnKphZ6wBg3256RT16qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین داستان ایران شاید مربوط به یک «گربه درباری» باشد!
🔹
در دوره ناصرالدین‌شاه قاجار، گربه‌ای به نام «ببری‌خان» آن‌قدر محبوب شاه بود که تقریبا مثل یک شخصیت سیاسی با او رفتار می‌شد. ببری‌خان فقط یک حیوان خانگی نبود؛ در دربار برایش جایگاه ویژه داشت،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/673023" target="_blank">📅 19:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miq7Kvf-dPS7b1jG_fjnOgAVcgyTxu3ktfcQO_HZTn6tmvSiL7vK_3HWlqe5YJOcXAEoaKLDagP7aPLIrt5ZfnvK-9L7O6JTHHnANr1k5pRUWj8WuQRKORpOaUBA6ddK_LZvd2NEiPMVQFUfmGtiZ-mSbkIfQSs2Yq8E0nOKFyDeRk7pwt2w9VkQQpQ8I8LgLKQB6DDp7YxSqSqDmrlR4GCWg5JjvB95MgW6WzWaQaNNzv_1PAzbnXYpWP22H7m9PYyuQso6VOnhHzAV-B_T5d3klAKOln5sorKk1t4VV0_etV5IxQp1UX5gCAnJdpGwk7Nta-0A4KcxTxR7xoiSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران ۶ میلیارد دلار نفت فروخت
ادعای وال‌استریت‌ژورنال:
🔹
ایران در طول آتش‌بس کوتاه با آمریکا ۶ میلیارد دلار نفت صادر کرد. حدود ۲۰ نفتکش ایرانی حامل میلیون‌ها بشکه نفت، پس از لغو محاصره توسط امریکا، به سمت آسیا احتمالاً برای فروش به چین حرکت کردند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/673022" target="_blank">📅 18:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=Ury-Gq3pKX9pAoiTMDOqQpI3Gco6lgKZbcL1c9B-b8RoZ-ykL2kP_9Vor4YQ3II7pixDfbvsmX8UGK7oVELL7CDMEvY1iPfMqa0lKVdETDhrdMv-c06CDwVGeYtqRLVzcMre5bjSSjsOnLq18-gPLFKDGQPnDzP-Oi-vCH20iK_DsH30T3oO5hmhWBJYZ2T3lgwJcHSs56nGvRB8FRF3snCDRpsnvQZjqcar7p5pYGByJ1yRXaQ67zDpTZBFtBtAjBEoKqYPgbVj7a6v483A3hcJ-mRWZc9Ik9nlp59D3pW3aaKVNQjtpjfgnVp6U8FhZVVfxdxrlmh4ZHshG6QQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=Ury-Gq3pKX9pAoiTMDOqQpI3Gco6lgKZbcL1c9B-b8RoZ-ykL2kP_9Vor4YQ3II7pixDfbvsmX8UGK7oVELL7CDMEvY1iPfMqa0lKVdETDhrdMv-c06CDwVGeYtqRLVzcMre5bjSSjsOnLq18-gPLFKDGQPnDzP-Oi-vCH20iK_DsH30T3oO5hmhWBJYZ2T3lgwJcHSs56nGvRB8FRF3snCDRpsnvQZjqcar7p5pYGByJ1yRXaQ67zDpTZBFtBtAjBEoKqYPgbVj7a6v483A3hcJ-mRWZc9Ik9nlp59D3pW3aaKVNQjtpjfgnVp6U8FhZVVfxdxrlmh4ZHshG6QQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس در مناطق مرزی جنوب کشور: جولانی بداند اگر بخواهد وارد درگیری با حزب‌الله لبنان شود، مسیر آزادسازی سوریه برای نیروهای مقاومت تسریع خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/673021" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a70005003.mp4?token=pas4AeR8ylvgZgYdizeiqNwLZh2QsmOWX8GPMPfSmql0k-_UGoAIWLsn1GqCWedBrWvTayroN9sjQ2D2j4ITxRFzie32AkYtw-iv5A_J4Pk4mZeSFHPEovl_V1BjrpGjq2ivI5hV_7UlRBdqePm2qEQqzfigCDdvL2JW8CllZqliC2v7NZVXihv0sST86163OLTPXki8tqiybAk39V_ipH5ATMUAF9qyBuRCeCYFzvmb4pbGy4opo1Uc-GcdGOgOssLpOqDoF_xDuIpaSriAvc4Y_zzCbff1sA904Gr1AFB8G565GBbE_DyAhPWmNqA-voqY-ADiW8V-1Xsh81p_YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a70005003.mp4?token=pas4AeR8ylvgZgYdizeiqNwLZh2QsmOWX8GPMPfSmql0k-_UGoAIWLsn1GqCWedBrWvTayroN9sjQ2D2j4ITxRFzie32AkYtw-iv5A_J4Pk4mZeSFHPEovl_V1BjrpGjq2ivI5hV_7UlRBdqePm2qEQqzfigCDdvL2JW8CllZqliC2v7NZVXihv0sST86163OLTPXki8tqiybAk39V_ipH5ATMUAF9qyBuRCeCYFzvmb4pbGy4opo1Uc-GcdGOgOssLpOqDoF_xDuIpaSriAvc4Y_zzCbff1sA904Gr1AFB8G565GBbE_DyAhPWmNqA-voqY-ADiW8V-1Xsh81p_YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی وزیر خارجه عراق پس از سفر به واشنگتن
🔹
با خروج آمریکا از عراق، دیگر چه توجیهی برای ماندن سلاح مقاومت وجود دارد؟!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/673020" target="_blank">📅 18:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67bbfe4553.mp4?token=v7_K7pP_Tq6gKc80vBFwhMIutiPXNyfDjPH2ngD37cfm0cw-eQ0R28s6xpNbQhASHaM4X5XzFb2oi892iSirVJvJoWD353fimwCFlWUCQqlEhc-cAl3I6Cg545T7iyNKZyFWzmeDkPossPYBaUjKl9r50dvZG5BNtSepxW1jInUiMRMS_z9FI7DIu9vR7dZNy4pvhR_6H5bvqlEp4SY3KeZ3OxlA8kE9ujpjIoRgORBX-uw_pq3Lf6u5dQIax0UBHtUc4UG6yRvgg83jLI9kssLhKUl0AVyLs20spFlO623fvN3L0wQZXf3oqiB8fNgXS1tEX88LgFAjDHmqmLg6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67bbfe4553.mp4?token=v7_K7pP_Tq6gKc80vBFwhMIutiPXNyfDjPH2ngD37cfm0cw-eQ0R28s6xpNbQhASHaM4X5XzFb2oi892iSirVJvJoWD353fimwCFlWUCQqlEhc-cAl3I6Cg545T7iyNKZyFWzmeDkPossPYBaUjKl9r50dvZG5BNtSepxW1jInUiMRMS_z9FI7DIu9vR7dZNy4pvhR_6H5bvqlEp4SY3KeZ3OxlA8kE9ujpjIoRgORBX-uw_pq3Lf6u5dQIax0UBHtUc4UG6yRvgg83jLI9kssLhKUl0AVyLs20spFlO623fvN3L0wQZXf3oqiB8fNgXS1tEX88LgFAjDHmqmLg6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از شنیده شدن مجدد صدای انفجار در کویت خبر می‌دهد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/673019" target="_blank">📅 18:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از شنیده شدن مجدد صدای انفجار در کویت خبر می‌دهد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/673018" target="_blank">📅 18:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700cf4632a.mp4?token=ZcgkZC9E0lsLQFBcVkCeI5alNlxIY55XXQ1thDpkPOS1nl61OFOFEzhdaUYdMw_NusnJTKEM21uiMQ1zYXbg7sr0QCG1UhOVVO12zKnR5y2pGl9mLBR89ucND5ACGBn11zttL-MyVtlBDx5BtSNxqWWof3ThVQ19VDmx7ITKfGG43LLMQc1Cvmv9pcgznbhh0oqyCcx7EQMl1PvYvubIiKtwE0DYCMl9SoFH7pG7NcPPv6pC9Y7TSlWzG_uwxeRespdUV-m3W4JXPqqgZzUA7ctNmVh7lRehyvDTh7EnhOuFnj6Q4hwhf_aXiYm9JtFisgd35gZc_CxW5OavOwb0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700cf4632a.mp4?token=ZcgkZC9E0lsLQFBcVkCeI5alNlxIY55XXQ1thDpkPOS1nl61OFOFEzhdaUYdMw_NusnJTKEM21uiMQ1zYXbg7sr0QCG1UhOVVO12zKnR5y2pGl9mLBR89ucND5ACGBn11zttL-MyVtlBDx5BtSNxqWWof3ThVQ19VDmx7ITKfGG43LLMQc1Cvmv9pcgznbhh0oqyCcx7EQMl1PvYvubIiKtwE0DYCMl9SoFH7pG7NcPPv6pC9Y7TSlWzG_uwxeRespdUV-m3W4JXPqqgZzUA7ctNmVh7lRehyvDTh7EnhOuFnj6Q4hwhf_aXiYm9JtFisgd35gZc_CxW5OavOwb0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک‌های ایرانی به اهداف آمریکایی در منطقۀ عقبۀ اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/673017" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eada6596a6.mp4?token=uHEaMln3aWn0Et6w5gtlVuYOwus6lKNjxpq8tqIDCWh5I3fI7Z2ysUYC1cQVr1BkdDoae6pDEOP5X6kkrSL7ejAFJeF4GrN1Ai_yd1P-TbxVLbvsLvJGNlF-rjBkYB7Vbnr0UQyORdUecO6vLFBT-xpyZmmxR7I8y8jIrk9SYBL39mcYjW73q0VG1LRfdfGhEq_ul_HqwD-nH8zx58E5ia_jUDJKrK4bRVCFaWf7JaSqYydI9sHc114oj50JX6ldry4XpLBsYzrHaQmSUP-z0csHsr3xHYoNwRn_qCzr3V9YmOysBTaB10HUAFl-ClPlVxnp6ehEE-TnzAs6qojZEanDU87V2CTp-NfAs4Rn-KXPpvnEJjOB_3NVbDdhBexPNDoOVOhJomhd4m9nmOeMSzUe91Orqrb9w8-ADzOL_rjAmzUOYxdZekWxS9V85qQCcZQGoyzqzoIm28F7YV9MjHT9llW7TqWmA3JZ3c_zPfcUwpLuQl5AkviB8OAwYDjWSo-ESuhFiRK-72-JwrD1ff12FsigSk21y4wMCzd3dNng2x2pSFtwUUrREVV0XZnqz_kkl93j8V32YcNGrGEYUnm_ZOEUZqhYikRNKZhQoJv5-_gtV9itBqxQfgCjAjhRaAmWZDZp78LeSj1vDv2thgUOMgX0WAec9ab4mR2ER9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eada6596a6.mp4?token=uHEaMln3aWn0Et6w5gtlVuYOwus6lKNjxpq8tqIDCWh5I3fI7Z2ysUYC1cQVr1BkdDoae6pDEOP5X6kkrSL7ejAFJeF4GrN1Ai_yd1P-TbxVLbvsLvJGNlF-rjBkYB7Vbnr0UQyORdUecO6vLFBT-xpyZmmxR7I8y8jIrk9SYBL39mcYjW73q0VG1LRfdfGhEq_ul_HqwD-nH8zx58E5ia_jUDJKrK4bRVCFaWf7JaSqYydI9sHc114oj50JX6ldry4XpLBsYzrHaQmSUP-z0csHsr3xHYoNwRn_qCzr3V9YmOysBTaB10HUAFl-ClPlVxnp6ehEE-TnzAs6qojZEanDU87V2CTp-NfAs4Rn-KXPpvnEJjOB_3NVbDdhBexPNDoOVOhJomhd4m9nmOeMSzUe91Orqrb9w8-ADzOL_rjAmzUOYxdZekWxS9V85qQCcZQGoyzqzoIm28F7YV9MjHT9llW7TqWmA3JZ3c_zPfcUwpLuQl5AkviB8OAwYDjWSo-ESuhFiRK-72-JwrD1ff12FsigSk21y4wMCzd3dNng2x2pSFtwUUrREVV0XZnqz_kkl93j8V32YcNGrGEYUnm_ZOEUZqhYikRNKZhQoJv5-_gtV9itBqxQfgCjAjhRaAmWZDZp78LeSj1vDv2thgUOMgX0WAec9ab4mR2ER9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بکش و لاغرم کن!
🔹
همه درباره نتیجه آمپول‌های لاغری حرف می‌زنن... اما کمتر کسی از بخش تاریک ماجرا می‌گه.
🔹
دارویی که این روزها همه دنبالش هستن، در ایران چه وضعیتی داره؟ و مهم‌تر از اون، خطری که شاید اصلاً از روی ظاهرش قابل تشخیص نباشه... قبل از تزریق، این ویدئو رو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/673016" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_06MxAuvgVSmaY33anzW7YiXuuKmnQR-kbyvM4BUFz1eVSIhC4WNEsyyMEIruUXtQijGxMkLlUmcNOhWLY0ufi7aNjGabLjDNt48tec-3CvOt9FXN7Oqo7svh066U2S7fO9H2VXuqTQX1PekiwHdrKPe8Z8YxJpWqaV5XNqg_MqCKc65tduTRCbpzghXJ4f6V2o8q59_4EnI9kLUma3dnlcQk55pz0-rLhELll_bmHuBkoGg64ucjXZMAiPpNaZqQXZK0ZB3x6_CKFud5VLFz1kPsq6jF7f9x6fsp2roSGwddzqdi02XvmHPRqT6Fg_5xmy6eLFZKKE8wx8dIw-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: در دوره زعامت حضرت آیت‌الله سید مجتبی خامنه‌ای، حفظه‌الله تعالی، مسیر نورانی و پرافتخار مقاومت را ادامه خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/673015" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTxJ3XnYX3DhNMfmMJWFfvsL8BhpNIRA-F6Ffto8DTpEk-cQ8RKH9aHh77AQnAwlB_BsL-WbHSLki1ERNqeXVw1xDsN7bWLShv9EXNA14vFB4-mp2y4uSs3yf-7I64MHDd8vNuYPhw1lbWcQwGXrbatUeKn1pNwhlGhMtazdeMlKOB0akEbjedGQdc0Ap-yTN2ByVruGOzMNXVFdb1LL8CYOzyFpzpGiH4ITk8Yrqsk-PtjctN5KbReimX5O60DG3Firpz7tTFHZw32N6285a3TQoUD567nvhVwInuFRmnVJGmc2RataA-HehXZgA-0u2XvudORyruGdVZ5KJE2QlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی چهره‌های فوتبالی از قهرمان جام‌ جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/673014" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=hp-RgDq7QlAF5CvKBX3cP3crBfy5JzgwkokoC3A1-80qQLatGmFjnf7B9bvYU1ATwNEpCs-i4JOGBc-1WZrmoftec_SsHPeiDcgkzAivSmofAo0E7YeEaB46sWLR6MDgyHluWLlTpS84Ky_wveXwGO4EdsqMH3aXpujokZGhdNVsR_by4RtpHfhAbLUnuxqcAkNvft72yA0jzNvavQMKFA9olaLDZADvTnySDtYwCy2zfbQdyZ8e-irSMKM_41eU49v0QKpW6m7pfNqIK0E3kkVOM6cMa4T0-05IontDHr2L7KKDHPUv15WjKvFDnwUE2albeLP8dZkowAzN2tKbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=hp-RgDq7QlAF5CvKBX3cP3crBfy5JzgwkokoC3A1-80qQLatGmFjnf7B9bvYU1ATwNEpCs-i4JOGBc-1WZrmoftec_SsHPeiDcgkzAivSmofAo0E7YeEaB46sWLR6MDgyHluWLlTpS84Ky_wveXwGO4EdsqMH3aXpujokZGhdNVsR_by4RtpHfhAbLUnuxqcAkNvft72yA0jzNvavQMKFA9olaLDZADvTnySDtYwCy2zfbQdyZ8e-irSMKM_41eU49v0QKpW6m7pfNqIK0E3kkVOM6cMa4T0-05IontDHr2L7KKDHPUv15WjKvFDnwUE2albeLP8dZkowAzN2tKbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مرزهای جنوبی کشور: ایران برای جلوگیری از اقدامات متجاوزانه احتمالی آمریکا از طریق کویت، نابودی و تصرف پایگاه دشمن را در کویت در نظر دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/673013" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2B6ZJVwsFmU9Qa71nBB6DvbV380bF3rIbZVN8X9E34-sBcN78VR47VXUhQA4pr7T69AjTxuki1rFR1yL1vp6djuyxQC7QBXOTfenu1eek8YV-aIika92k15TjAiuAvBwAIjvnV_2wQhkRBYokpZjhWZZk2LfV0K26W6RMPcuEll81oCoHlHE7wdjCWs09BUZmf91vA_CzBcJT1iBpgmbQ0EWow_9mq6_DkgHSot_MVWYNjwcnaAWlWcQ9NkaukygOSdSO75pUHgAsYokApMAQfXimmA-QQH1mDceYBAmx08qq-5B0DYAMo0o5IP_OEUu2_mb8605cizWP302-tlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندا کیانی، در واکنش به حمله مجدد آمریکا به ایران، با انتشار بخشی ازصدای شهید آوینی: «اگر آمریکا تهدید خود را عملی کند؛ و از راه خلیج با ما رودررو شود؛ شما چه خواهید کرد؟! خلیج گورستان آنها خواهد شد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/673012" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
هشدار انصارالله به واشنگتن: در صورت شعله‌ور شدن جنگ، آمریکا بزرگترین بازنده است
انصارالله یمن:
🔹
انصارالله برای پرداخت هر بهایی در مسیر شکستن محاصره یمن آمادگی کامل دارد و منطقه اکنون در لبه پرتگاه انفجار قرار دارد؛ واقعیتی که عربستان نیز به خوبی از آن آگاه است.
🔹
اگر ایالات متحده در کنار عربستان علیه یمن وارد میدان شود، در یک باتلاق عمیق و بحران راهبردی گرفتار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/673011" target="_blank">📅 18:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تشدید گرانی در راه بازار لوازم خانگی؛ چرا ممنوعیت واردات لوازم خانگی یک اشتباه بزرگ است؟
اکبر پازوکی، رئیس اتحادیه فروشندگان لوازم خانگی در
#گفتگو
با خبرفوری:
🔹
با ممنوعیت واردات لوازم خانگی، دولت مجبور به پرداخت هزینه گزافی و مقابله با قاچاق می‌شود آن هم در شرایطی که درگیر جنگ با دشمن هستیم.
🔹
در شرایطی که هم تولیدکننده از وضعیت بازار ناراضی است و هم فروشنده به دلیل اینکه مردم قدرت خرید بخاطر گرانی کالا را ندارند، چنین کاری اشتباه است.
🔹
نمی‌توان سلیقه مردم را محدود کرد، هر کس پول دارد و دوست داشته باشد کالای خارجی و هر کس بخواهد کالای داخلی می‌خرد.
🔹
این ممنوعیت به مرور زمان وقتی کالای خارجی در بازار کم بشود، باعث افزایش بیشتر قیمت‌ها می‌شود.
🔹
ما در حال هدفمندسازی فرآیند واردات و فروش کالاهای خارجی بودیم تا دولت و سازمان حمایت، نمایندگی‌های خدمات پس از فروش این نوع کالاها را فعال کنند اما این اتفاق رخ داد.
🔹
از مسئولین می‌پرسیم این تصمیم به نفع مردم است یا به ضرر مردم؟ به نفع دولت است یا به ضرر دولت؟ در جلسات نشستیم و گفتیم بازه سه ماه دردی را دوا نمی‌کند.
🔹
در شرایط جنگی به جای اینکه اوضاع تسهیل بشود برعکس سنگ‌اندازی می‌شود. فکر می‌کنند ما مخالف تولید داخل هستیم در حالی که اینطور نیست‌ و ما چند سال حمایت کردیم، حمایت کردن وظیفه‌ ماست اما اگر واردات قانونی لوازم خانگی خارجی منع بشود، قاچاق جایش را می‌گیرد همانطور که قبلا بود.
🔹
ما می‌گوییم نباید این محدودیت باشد، می‌خواهید کالا وارد بشود و زیر نظر دولت باشد،  هزینه گمرکش را (در صورت پایین بودن) بالا ببرید.
🔹
هزینه‌هایی که دولت می‌خواهد بگیرد را بالا ببرید؛ اگر هدفتان کمک به تولید است ارز تولیدکننده را بدهید، چرا با بستن راه ورود کالا می‌خواهید به تولید کمک کنید؟!
🔹
برای مسائل جلسه گذاشته می‌شود ما نباید فقط برویم حرف بزنیم ولی اگر هم نرویم حرف نزنیم می‌گویند اصلا هیچی نگفتند. چندین سال است نظراتمان را می‌‌گوییم برخی انجام می‌شود و به برخی‌ها اصلا اشاره نمی‌شود حال اینکه دلیلش چیست را نمی‌دانم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/673010" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
هیچ پرتابه دشمن به آبدانان اصابت نکرده
احمدی فرمانده انتظامی آبدانان در استان ایلام:
🔹
شنیدن شدن صدای انفجار آبدانان مربوط به نیروهای خودی است و هیچ پرتابه دشمن به این منطقه اصابت نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/673009" target="_blank">📅 18:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa95e9d12.mp4?token=VRmhzbuDWUozle3c0z1mhSUbaTqFwzluJPNQ7lUXwbLa7OFpFTlzhOQjs7vxCh0qgiBqZ3z18jYOYKz6JFhiiGgYGupln-AjgHTAV5AsX75yiVmRfTcZgqBvyzqs2oLi45a8oAVt8npogbNQCIY-x_5shyJvxwovbPk7jPCWEst1Mzq1kQeZMiH83gsLVjI3R2tP8WAFxC8Bw18cyNEEsPMAHSoqWJ6MTsvDBBVROz_YA2baT53xcFNmH9b8N3Q3D8iNqEzt48HqxXLktJ-jkeBWMeI77AasldmU5zk698hfqrB3FZjnrSHphpt3r4PWZkF_iWLkovbggLx9w-h_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa95e9d12.mp4?token=VRmhzbuDWUozle3c0z1mhSUbaTqFwzluJPNQ7lUXwbLa7OFpFTlzhOQjs7vxCh0qgiBqZ3z18jYOYKz6JFhiiGgYGupln-AjgHTAV5AsX75yiVmRfTcZgqBvyzqs2oLi45a8oAVt8npogbNQCIY-x_5shyJvxwovbPk7jPCWEst1Mzq1kQeZMiH83gsLVjI3R2tP8WAFxC8Bw18cyNEEsPMAHSoqWJ6MTsvDBBVROz_YA2baT53xcFNmH9b8N3Q3D8iNqEzt48HqxXLktJ-jkeBWMeI77AasldmU5zk698hfqrB3FZjnrSHphpt3r4PWZkF_iWLkovbggLx9w-h_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس آمریکایی‌ها از تنگه هرمز ریشه‌دار است؛ کابوسی که هنوز از حافظه پنتاگون پاک نشده است
🔹
شهید نادر مهدوی، فرمانده ناوگروه ذوالفقار، از چهره‌های حماسی نبرد دریایی ایران با آمریکا در جتگ تحمیلی هشت ساله بود. او با مین‌گذاری در مسیر کاروان نفتکش‌های تحت اسکورت…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/673008" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حمله آمریکا به سایت نیروگاه دارخوین  سازمان انرژی اتمی ایران:
🔹
آمریکا روز یکشنبه ۲۸ تیر ۱۴۰۵ حوالی ساعت ۳:۳۹ بامداد، با تعدادی پرتابه به سایت در حال ساخت نیروگاه دارخوین حمله کرده است./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/673007" target="_blank">📅 17:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgKZFOnasZT-ijyM4LFwb3FAAs3U9WqFy5bsz7E4h2BW5Llke0PmPbhzBesQ6VT8bDfjPphZF2_2y8bEKIhkKSQIiAfd3QzUrF4r7mKjjyII9X9MlrKowLMtrfmFGj771wc2xjrIA5OVh3rnnvjxINiGMLc8JlDolbxpPYjMsNXgJuCknC4s5RL02CRBLtZo27UhfJ55YV5WCU_CFaWGKahWexNfui1jas_aWpkuTVzs8eE757YS9cyFwBGGKoVx9HfNiRu-T-dkVGt6fRYpWNcJUtuyhGBJNYmrN2ukEPpgJDl35mf4OzrxtQyh26PP4HKvsMbPxMeTRBZeCR4giw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔔
🔔
اطلاعیه پیش‌فروش بلیط‌ قطارهای مرداد در علی‌بابا
بلیط قطارهای مردادماه با تاریخ حرکت ۱ تا ۱۶ مرداد
از ساعت ۸:۳۰ صبح روز دوشنبه ۲۹ تیر
در وب‌سایت علی‌بابا پیش‌فروش می‌شوند.
دسترسی به ظرفیت کامل قطارها در
علی‌بابا، رتبه یک بلیط قطار
🥇
قبل از تکمیل ظرفیت، رزرو خود را نهایی کنید
👇
https://albb.ir/5wiGw9</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673006" target="_blank">📅 17:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
فروش اجباری بلیت دوطرفۀ سفر هوایی اربعین ممنوع است
رئیس سازمان هواپیمایی:
🔹
هرگونه فروش اجباری بلیت دوطرفه یا مشروط کردن فروش بلیت به خرید همزمان مسیر برگشت، ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/673005" target="_blank">📅 17:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeAp4_H7E8aisODOrvM3wrRflsqHFKNT-k3_L2-oIqxjV7_Vq6yBRuumBzbXQu6AsX9O03DZ9avUNvZ8muTCWyqflFAy6HjgUXFmyiEbHHdYafWocVRvfJ_kbY8QZPJWsUbnBtyV5k-FI3wggACVsCpkgpyQ7bEfyvwI-l3gHONnH-InsnIMG0zWsfRqr7YEplKqopOaMRGGImw_3cOAY9Es66XXinqs6q-lbLkUI7ekJWTNGipSmF_axDATgA9ybVk60MoMKejh-DmanbqMu6dPciYxzUmn8LA4qhVnLXt3zmGePrP9Ie5VFQ-E3QBJSYtIsxKzSm_YbIu2Yb_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کپی برداری Dior از سبک پوشش ایرانیان دهه ۶۰-۷۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673004" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9ptZzSTcZaQbUMOt3v5tTh4gZdLlwWExN4xCebcs3P_PSAuX8VwoOQKSK4S5qerq1r-eyF3m5-K1UhGvsGjvbhQWxZAtXHUApUmKadrKWZpzIAaueTQ7MY8PyWl-civitx1-4jnfjtf2pbS6TdlePXSTk6IfFG4EQlTjKhsw1j9kJ31rbEc2VRsXdx0EzH_RWGFo3qNNPWupSi25_s5iYN1V-lPXJoLeUFTU9-tgPULl_9_i9NZh_D1GADS1FNk5bsXgRjbH5atKw7URQB3eQt2Cg87l6QqnJ9A-4BHFcn8Jrpn4YQiEzIYxWg1ufDnYhcgtUtodNSoZhjIoT-ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTaQ0ufD14hI7RehPm6t6aE4J7nQgoJ6RDnQmdF9qIs1zGmOgzlWMYn_fEfxWfYVTvln5dvOTvt07HAYLxA0ep2QbFs1MX_sWVIZrB4XQfO1mN39pHt7kv9I-OBYeoxPZKubcFys3OLIWFT7TUUh8Jjg3VxsczVOI8cS-cCdkdzr8tM1Hz9o4_PyCbEKT0tRzURC27gZVVJJO3wZLHygCQkFmbHM_Ev8MoAm3h5_fiebUTEUHIIzW7cziMOaXW1OD8yIxEDpV9hWcVQw6s0kpmhyWBml2omV_FhVLLPttqGK7R2FtvN8zRla4LRffqLjafumK6-4BeYr6FVDdzerPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASZau1kUAoU6GWrx_4Sjzl-Vf8oML3XoAA62IFK_9OQEzwbu1tKWpEwwFTON_MqiB8lrcltnkPJXfRb6I4Fklzj1f56PR4XnYbk8ICyDQAb8w6MovU3hZB5qXsZek6jj90dp3ccjZ3BMmTZzdXVefZsNgh7lQ97Zcs6En52oojHTS9NSr9U0eRXH52qYRfQ3xT8djzOTw4rVa7klYYMVB9yJP93hPnfj1Zn8hrc3x_xGM9PU_jkigYjevpLSUeEWQx-qV_ZLQiNnuLubVpgYnB49XugEylfB_3pko4BkCXjG1BrFmZZvMGv_JbaSvU4YB_rScwB40mJ5sZIkQuMEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0ygU8qxOSuoLJ9vVTj103leWFdM70WIxZZDSdxKhVqrwRHVPyMeL0TESlW0_p1SFdJAG3y4X527-50wU_--Tm5hEqLiALrNNoB3-r8x7aK1PwfTb7bnar8qf7RZsqGe1ACWeEEN5l3Nbq1wwd2DBSEJHX71uzeOXBQNmxpR5PNjs5ynxe-mP1JfbrQRGVSRvWtazUreKzygA0mYG5jSKYOtAOCV0SgPlo_SgXUt99K_HYXmXX7IDVkFzIlEmM5kQSwGpbe1GbSdW36P4Ek6Yjncd2eFcQYI6YF-v6NnHamnQxaD9PHMe0zYz95gmdbODeia-NU38JlyTfz97yy5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2mtA6W2_RSGo3a2WWx2jOyTVymWWxwaZ94dY3NACi7O5hhRz9cxfxJ1NqWQf4QZAdRUhiE0HWi6SvI8vAwhPKdDHJ_1DRDX13PX0cGg4_224-Qcwg2dMDUvSXwCoqPiNRADbv_BvCi8lsnbqQpKBg2p9RTEZIMqGjGPq2LNCd68kdY7xVQ44j-y4eULQ2JE3TLECM7tgrMLByNm7jfscqPW2mOv2liiGRrEM6AQn9Lr3c6CHk9NILC-V5xzqYlA1bx9UEven3TCOc7R0ka7d9-nJKrlZnspTj-ByGJzpOhcz4vaxH4zFyoB9vPRzkQFiZFy_18r_vnRK_J8eo4ztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgW3ldaQma9etea5-4wDFB3GjGsl85WTtpKtfwTISLG257PeZ-JgBTMus3wqLWarmeit84Vs4cj0XL6GK8h57hBXdf76hs2B6EAhz7J_ugKKPxQduYKttIgtOKhNJ9mivM868rdMCi5HoWajYbCYFa7zuPXDswENRqdP420NHc9KbGH6oBqJbnBOG4NT6rwKuQz66JTOYvi_3j6Z6zCCOD2It7jzppj-1_gHRrSiidyXTGeHDVKULi2uadYJhQuWRAzIQWUrje45w_slD0ap5OrlTsJ7XU6LG6kEktq6T4ekvazp9fuWMI4toL5KgGWZe6Jdxn69koRiiPOkoOFXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzR7dPgwVKIucgW7QSOOVHKi0EK_UMHWlgtdrkzh5UsHhQBvQIu57v4cnaxsc78LrcgR9KwTS3dBQXSkxglQX25Bd7Su1eyB5epjFGa3VJ0WBvBCU6q0DqWjD-M16Itbq3lUiVm4spEBYoIxFK2Vt0SK6Ow7diKOAwCeS6KDmJ_O4VmH7XFiUpk8YcHe5xBeDrSDfisYRFq3JToLj3-APPRNbKY0_XhvaoTYLHAYYb68lyaljFwbeGxgAQWzC1Je2Ia3TOlaWT9elNLLd4NCWkRXUqjGu0Tx2aBHfEnvPEmynaW0VCuOm9zdD7AJvNrI5Kcjef4QpRW9PFbfSxkQ6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نبض زندگی در بندرعباس
🔹
ساحل بندرعباس در روزهای جنگ نیز میزبان شهروندانی است که در کنار آب‌های خلیج فارس، لحظاتی از اوقات فراغت خود را سپری می‌کنند و زندگی روزمره را ادامه می‌دهند.
🔹
عکاس: عباس ذاکری
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/672997" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد آمریکایی MQ9 در همدان
🔹
دقایقی قبل یک پهپاد آمریکایی MQ9 توسط سامانه‌های نوین پدافند هوایی ارتش هدف قرار گرفته و سرنگون شد.
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672996" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مهر: هم اکنون صدای انفجار در آبادان به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672995" target="_blank">📅 17:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjWBSJhd8SrIT2hO8jGe3xggDotvqARDuLbmD9w8nDpig6lgzqL4m_PLXUwfU_bjGtbzwqCHn2R532RIwKGNvktyI6Jogj5UOkucdnTWD2TY8qRoijflGTkMYaJv07KkQR9shLjriseI79kO7zEQ6eeeVzXIac9dJF2DJ71968Vw3U3_eGiIyYfjAz85Zy0DRKV12sW7YGvbQv22nbYpo3CI_9xQeeaqR81k1h5TnraTtckJIdI8Oeavj88jNndF6THBipWpiWfvVu_4SPHWGSK--7v_KqrTab0whASfCM7p1Ksjyvi34vGY4flcGFJyNgmkgkbzw8BCESAlsyyb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برگ‌های این گیاه خیلی شبیه پرنده ست و بومی استرالیاست، این گیاه birdflower نامیده میشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672994" target="_blank">📅 17:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تکلیف زمین‌های تازه‌متولدشدهٔ خزر روشن شد
سازمان حفاظت محیط‌زیست:
🔹
اراضی تازه‌پدیدارشدهٔ در سواحل دریای خزر که درپی پس‌روی آب ایجاد شده‌اند، متعلق به دولت و غیرقابل تملک هستند و هرگونه تصرف، واگذاری یا ساخت‌وساز در آن‌ها ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/672993" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه تولید هر کیلو برنج به ۳۰۰ هزار تومان رسید
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شورای عالی قیمت‌گذاری وزارت جهاد کشاورزی در اقدامی غیرقانونی و غیرعُقلایی ممنوعیت واردات برنج در فصل برداشت را لغو کرد.
🔹
هزینه تولید هر کیلوگرم برنج به دلیل افزایش چند برابری نهاده‌ها و ادوات کشاورزی به ۲۵۰ تا ۳۰۰ هزار تومان رسیده است.
🔹
با این مصوبه قیمت برنج در حال کاهش است و کشاورزان با ضرر و زیان سنگینی مواجه خواهند شد. از وزیر جهاد کشاورزی می‌خواهیم هرچه سریع‌تر این مصوبه را ابطال کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672992" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672991" target="_blank">📅 17:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مهر:
هم اکنون صدای انفجار در آبادان به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/672990" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
‌
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/672989" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» با آتش پدافند نیروی دریایی ارتش در جنوب کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672988" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672987">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: هواپیماهای سوخت‌رسان آمریکایی پس از حملات به عقبه در اردن، از فرودگاه رامون تخلیه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672987" target="_blank">📅 17:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672986">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
وزارت بهداشت:
🔹
در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۸ نفر ترخیص و ۳۲ نفر همچنان بستری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672986" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
هشدار قوه قضاییه نسبت به هرگونه انتشار محتوای خلاف امنیت ملی
🔹
قوه قضاییه با تشریح «قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی» نسبت به هرگونه انتشار محتوای خلاف امنیت ملی هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672985" target="_blank">📅 16:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz2iECusU5LwE6Jcz-yePL43coXVBDl1X_tdepVS516o7Rq4UxFh0BQXVl0Y5Rlpia700unkzEF-fpIaa7mnmYj3ukdemDQUPYJI9rm_9-2UI840lgzTR2IS2FS68eHcp5yi-rXX6xMxpHWX2A4epP8Qpw6kQgaHK0OFUubFQKtm_Qi--G1iqIAf5eTrPI3noiFyAWcY4TJgevC7ufvXiAcNpu50fZhuuwJ5nPg7rpmyh9EMuxXgf0asbdThepz1Szw6pd2imiLZirkNrE-_oWBQbMqQnM7KLHfBcTOO8x_SOfTr3RoqLzrfhp314KdDItqf-fS-4xEPZGO5WHfsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از چیزهایی که در گینس ثبت شده؛ قلمرو ایران در زمان داریوش بزرگ بوده که ۴۴ درصد دنیا رو اون موقع شامل میشده...
🔹
ترامپ وقتی گفت ایران رو میخواد بفرسته به عصر حجر منظورش این زمان بود و خودش نمیدونست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/672984" target="_blank">📅 16:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672983">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6295645ce.mp4?token=lRRrqxJVX2Z_LQGBTgkTlas2fdX4qXYdUP2pt6iDTKca3H_Tad7cASErM4XF4trT2cnQ9ZhRp7TZjX_57iuW-0vUF2aEGQIvXOh8OO_KdSrXCJDtn1Z9V4jyFfGULN8eqWTxtI7xatnNfvOKIqs-w6WPNh2gUhwuRTUpvENGLAg9p7Bg7NBZTDPUTYEcmTitaBDZunrMwVr2dJItZmabcXJfplkICmKa9bezoouDbFbI5UGy8sbcJ2mZzVIg7mIa0On4BQW40mKCvY-CKkwEmrp2Ir3RBAND0qvHiczRwlqk3Y6Uoxywys0MpZ0Xcfz4uq-CK0WzJVg9qoGyMqj71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6295645ce.mp4?token=lRRrqxJVX2Z_LQGBTgkTlas2fdX4qXYdUP2pt6iDTKca3H_Tad7cASErM4XF4trT2cnQ9ZhRp7TZjX_57iuW-0vUF2aEGQIvXOh8OO_KdSrXCJDtn1Z9V4jyFfGULN8eqWTxtI7xatnNfvOKIqs-w6WPNh2gUhwuRTUpvENGLAg9p7Bg7NBZTDPUTYEcmTitaBDZunrMwVr2dJItZmabcXJfplkICmKa9bezoouDbFbI5UGy8sbcJ2mZzVIg7mIa0On4BQW40mKCvY-CKkwEmrp2Ir3RBAND0qvHiczRwlqk3Y6Uoxywys0MpZ0Xcfz4uq-CK0WzJVg9qoGyMqj71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان
🔹
منابع خبری محلی در جنوب لبنان از حملات نظامی جدید رژیم صهیونیستی در مناطق مرزی خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672983" target="_blank">📅 16:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672982">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت راه آهن: پیش‌فروش بلیت قطارهای اربعین از فردا آغاز می‌شود.
🔹
عراق و قطر خواستار اجرای مفاد یادداشت تفاهم ایران و آمریکا برای امنیت منطقه شدند.
🔹
ارتش: انهدام بمب‌های عمل‌نکرده فردا در شرق تهران/نگران نباشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672982" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672981">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHTZ6BjEYobde3m1x31ZaZOYdk9kXcJG7Kkg8WHWwxCrXCt2Jku79UiYMX00Bmwk0v3xJgSs_b1qU3zjOVp2tHsi1dTBsZrA8o7VBIpXfAltG3quItiLNWTOkpQxcE8gDVEr4OIEnKGD-pjcegUAOKKLEpeBO56iucZR5dBlU9PmOE-sE-9v9dc4O9He67szp2lFb0NordK_U3mLI1xdZ0HR-8-d1hdq9zH_D182A7lExy086Yn2-xOpS0ggPVGWEaGfmcWzmIIcLjPyztLiDmam-Wl8acLK1hJfhO0IEW-_6Ug5xjjC1tC22F_mHnmKJ4gUOk51bXhodY24puLVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیاتزا و شاگردانش این‌بار مغلوب ترکیه شدند
/
پایان تورنمنت برای ایران با یک شکست ناامیدکننده
🏐
ایران
1️⃣
➖
3️⃣
ترکیه
🇮🇷
۲۵|۲۲|۱۷|۱۹
🇹🇷
۱۷|۲۵|۲۵|۲۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672981" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672980">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a40c4dcc.mp4?token=YKtRybkc1LOAgVENiQRjWgq8JqZbSvyJ2SpsWTS3mJcHmsmRQb6rmB0y7XuOI03jpWeuRv_nR0eIrWlYDbQbSjfMl-3EWlLFcuW9sqdDhQeGUwv4PQCqNJUBTQhcSiBD34BmwJ4vNJQCLL2e6Mu8yNl_dJuj6at6VBRmYik5wXsvAgoiGpq7V-4liqNEb6RX2BasoKYc9uMVP7Qw9Fglk12pYjezj52fx3CBoVTX_pMnGBE5Y04XpQZbqRqUR6RSSpNb-MkyUYwk-sz_5vLoUx6fR80pxnfstkJkazHGCfEf-1zpcUByLE9LsE8adhPdb4GM6Hft1QJFqkvGXtYzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a40c4dcc.mp4?token=YKtRybkc1LOAgVENiQRjWgq8JqZbSvyJ2SpsWTS3mJcHmsmRQb6rmB0y7XuOI03jpWeuRv_nR0eIrWlYDbQbSjfMl-3EWlLFcuW9sqdDhQeGUwv4PQCqNJUBTQhcSiBD34BmwJ4vNJQCLL2e6Mu8yNl_dJuj6at6VBRmYik5wXsvAgoiGpq7V-4liqNEb6RX2BasoKYc9uMVP7Qw9Fglk12pYjezj52fx3CBoVTX_pMnGBE5Y04XpQZbqRqUR6RSSpNb-MkyUYwk-sz_5vLoUx6fR80pxnfstkJkazHGCfEf-1zpcUByLE9LsE8adhPdb4GM6Hft1QJFqkvGXtYzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار رونالدو با نسخه کودکی خودش در فضای مجازی احساسات میلیون‌ها نفر را درگیر کرد
🔹
این شاهکار که توسط هوش مصنوعی ساخته شده در فضای مجازی نزدیک به ۲۰۰ میلیون ویو خورده و خود رونالدو هم لایکش کرده
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672980" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجلس برای خونخواهی دست به کار شد
جعفر پورکبگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
خونخواهی رهبر شهیدمان در سه سطح دنبال می‌شود. اولی حضور و مطالبه مردم در میدان برای خونخواهی‌ست و دومی قدرت نظامی ایران است.
🔹
مجلس هم طرحی را برای خونخواهی در عرصه حقوق بین‌الملل دنبال خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672979" target="_blank">📅 16:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672978">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: هواپیماهای سوخت‌رسان آمریکایی پس از حملات به عقبه در اردن، از فرودگاه رامون تخلیه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/672978" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672977">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34979e300a.mp4?token=rdnro6Ej1LEl4zezh5cEmR4AxexAWswb8CHnSDQoOzKK_Ld663JEwWeyXliHdUfdBq8LES4ltGAkIwJPRwG4xQ1MZp0oKDKi5APJwYbGuxulZoNrWdFwKT-bTMYndpVMNDDvM6Uc9bxupaVFgcCojthdQvNie84RLN7KD0qzf2yg6p0EPIdoJWLGsEgLt0HcFrVQ49K1nWPRZ2-PpfGpHY5ZPAoyIoPoXO0mB-4TipORAwX3InldIz4YSqVYaphL7_3ARkd4vmkCVEY793YYjHTL0M-BoScEvFFVXSPsjzYkFkRgXfE1N4A3J9d9LH0BZge7Dp9Ct1JPnX2X0GCvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34979e300a.mp4?token=rdnro6Ej1LEl4zezh5cEmR4AxexAWswb8CHnSDQoOzKK_Ld663JEwWeyXliHdUfdBq8LES4ltGAkIwJPRwG4xQ1MZp0oKDKi5APJwYbGuxulZoNrWdFwKT-bTMYndpVMNDDvM6Uc9bxupaVFgcCojthdQvNie84RLN7KD0qzf2yg6p0EPIdoJWLGsEgLt0HcFrVQ49K1nWPRZ2-PpfGpHY5ZPAoyIoPoXO0mB-4TipORAwX3InldIz4YSqVYaphL7_3ARkd4vmkCVEY793YYjHTL0M-BoScEvFFVXSPsjzYkFkRgXfE1N4A3J9d9LH0BZge7Dp9Ct1JPnX2X0GCvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمام داروهای گوارشی در یک جدول
ذخیره کن؛ حتماً به کارت میاد
🔹
تاکید می‌شود که برای استفاده از این داروها حتما باید با پزشک مشورت کنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672977" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پلیس راهور فراجا: تمام مسیرهای آسیب‌دیدهٔ هرمزگان بازگشایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672976" target="_blank">📅 16:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11f8aa326.mp4?token=pwxIn_ihI1SRzfHlHP2A-LLidNmIMLOyNVK8VexNot-S4jsr3jL6dM_tNMJkSqhU4D-DBjhsaMkn0WkupZnv4t58yzscnSQsT6QFojRryINKzi4eesfLP4amtY2Dl99MtjEglYK1fZQ_qpF3u8fdBevafMCTLNbFxl4hu8W8zyCbEMxpiTe-dUxRhDEZ2UQ26iGGBKy_V84uLgxblB0paLPbERpp4HKXppbh2y6z0ddfBu2Hl2oSxg9F-PM2P2zwBsPt09qe8JjcaYRW4s435vuf2lpfUYm4fWrEASd_3iKNybbuXNHm9U760Kl4-Q32_bD8OXkfZRhvVASJPN2t6qlzxo-yqXj8l35RyMs9yRAy0wri-SaVN4Kz2H4O19O6twhN7f_DNmDjWF_iRYZ5glXGpkMA7jArX0YPU2TDh5Zbu-hUjHXszgL3SRHIuclwqWrC40I1Bqg9WUufnshxa6OSYIDew2ze26NWZlQSHRVTemxuS-mHW0tv6cBvaEWAe3e4KXl3JOD_h8nu-hVfSyrA6VfUWMCbej4Fh4rtg6RCLg5cTWB3bjNAaxMEHLnxSA1tx49v3FMGDtGbW78QISXtJ6h0zYXvXKAKmwYlEhvu1lLMaoKLKyfzQK1lllJYtc99pqD3XvNDtVudHTzIlEnsf03SCkaFkpEtjXDXWs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11f8aa326.mp4?token=pwxIn_ihI1SRzfHlHP2A-LLidNmIMLOyNVK8VexNot-S4jsr3jL6dM_tNMJkSqhU4D-DBjhsaMkn0WkupZnv4t58yzscnSQsT6QFojRryINKzi4eesfLP4amtY2Dl99MtjEglYK1fZQ_qpF3u8fdBevafMCTLNbFxl4hu8W8zyCbEMxpiTe-dUxRhDEZ2UQ26iGGBKy_V84uLgxblB0paLPbERpp4HKXppbh2y6z0ddfBu2Hl2oSxg9F-PM2P2zwBsPt09qe8JjcaYRW4s435vuf2lpfUYm4fWrEASd_3iKNybbuXNHm9U760Kl4-Q32_bD8OXkfZRhvVASJPN2t6qlzxo-yqXj8l35RyMs9yRAy0wri-SaVN4Kz2H4O19O6twhN7f_DNmDjWF_iRYZ5glXGpkMA7jArX0YPU2TDh5Zbu-hUjHXszgL3SRHIuclwqWrC40I1Bqg9WUufnshxa6OSYIDew2ze26NWZlQSHRVTemxuS-mHW0tv6cBvaEWAe3e4KXl3JOD_h8nu-hVfSyrA6VfUWMCbej4Fh4rtg6RCLg5cTWB3bjNAaxMEHLnxSA1tx49v3FMGDtGbW78QISXtJ6h0zYXvXKAKmwYlEhvu1lLMaoKLKyfzQK1lllJYtc99pqD3XvNDtVudHTzIlEnsf03SCkaFkpEtjXDXWs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس‌انداز و سرمایه‌گذاری فرق دارن، و این فرق می‌تونه کل آینده مالیت رو عوض کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672975" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری، سقف نرخ بلیت پروازهای نجف و بغداد را ۱۲ و ۱۴ میلیون تومان اعلام کرد
🔹
نرخ رفت‌وبرگشت از تهران و استان‌های شرقی ۲۴ میلیون تومان و از مشهد و استان‌های غربی ۲۸ میلیون تومان خواهد بود.
🔹
این نرخ‌ها برای بازۀ زمانی ۳۱ تیر تا ۱۶ مرداد اعمال می‌شود و برای بزرگسالان و کودکان یکسان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/672974" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=JX3zFmXlV4k6uVaEMhKgHKGVHrE7HsRm9xU7b4rORr7YPFfpyDXiSaAr-WLsLczO1c1MEmiRg6RL0KVHpTALvE1cQe-ejUiOUeFzVnf6DtQk5aWaV6uGlTiwpwaIzSiZN2liNFy3Xjef9BG9CuZScxLTxixSc9VjakBIwjaQWYo28Q4QQOJHcIdNliI81lqmn5hiPxryM7z7laYU-YWFSDv5cn3gK6ye1C78gtTcpBFe0JooCZiWcaIPJgyPj-3uAzDUJ6D-2sKDhu1mb-P4inPUJIeNGtbKaPRKdcHClLo6BluTubkThsqV12fV8o6kZp8QMZ5XYH_h1QklSvmQNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=JX3zFmXlV4k6uVaEMhKgHKGVHrE7HsRm9xU7b4rORr7YPFfpyDXiSaAr-WLsLczO1c1MEmiRg6RL0KVHpTALvE1cQe-ejUiOUeFzVnf6DtQk5aWaV6uGlTiwpwaIzSiZN2liNFy3Xjef9BG9CuZScxLTxixSc9VjakBIwjaQWYo28Q4QQOJHcIdNliI81lqmn5hiPxryM7z7laYU-YWFSDv5cn3gK6ye1C78gtTcpBFe0JooCZiWcaIPJgyPj-3uAzDUJ6D-2sKDhu1mb-P4inPUJIeNGtbKaPRKdcHClLo6BluTubkThsqV12fV8o6kZp8QMZ5XYH_h1QklSvmQNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر در مناطق مرزی جنوب کشور: سلبریتی‌ها در این وضعیت به‌دنبال فالوور نباشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672971" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672967">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3d8e8d7a8.mp4?token=QDIOCs00WlvZhxfwdNmZCnW9oA_wL2yoZbAcFE8BxQkzj3LwFNRMn27qvCXgC2A7fx3R-coO_ho1rmxeYdGR3_g4MXrEtXAV1w79H3GddZErZ0CAh9vEZHZK9Rs1uEJzlz-_ZL0S-OyOI3DXBc2w9nu4eqj_NPsDM98ubyQl05gYk3fRARJsJBqmXZJ35PZYcAHh58HOgOqDRaS81n4nQhhngjaE-VX5hfiioB6l95znnJ804eGrelQjhJgNtaOgKVM0NsY6lw3zfu9OcZrmm_1JDUbf2y3ujkuzSRvIYw6WeYdIDX2x7e9-mKT9DjcO58BeunvqRysR90M4weg4ulnlAtJbLEa8o7Ef9rKyBWrqmUOImC8Zyg_GGSw8dihJEngu8nSgOu97mLHgv5q1sltvGnvfyz3NonX3zdCBXkzLFNgRlDHgU7nVtzqpgil8RMtNFNzX3PkeUf3qfxNqamz8KYjYMYJxqTNvcsCyIdDeIqLCWQfPqxk77tfnvBSNBsJq8aUDe_8WRQb3LwNl_u8qr6sz5E8NPHSif6TwV_zlvC-UYx8UqRkXvr6mFJhj9LKxo-3Yigl1w3MWnRgqjGniObA4qLq7Fkd3pUqbL0h7VfeJ9csxBw3470jGCdUVHYC5Iypo9Dzst1qTnOOwmzPnLfCmRIp6LnhfHnnrc20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3d8e8d7a8.mp4?token=QDIOCs00WlvZhxfwdNmZCnW9oA_wL2yoZbAcFE8BxQkzj3LwFNRMn27qvCXgC2A7fx3R-coO_ho1rmxeYdGR3_g4MXrEtXAV1w79H3GddZErZ0CAh9vEZHZK9Rs1uEJzlz-_ZL0S-OyOI3DXBc2w9nu4eqj_NPsDM98ubyQl05gYk3fRARJsJBqmXZJ35PZYcAHh58HOgOqDRaS81n4nQhhngjaE-VX5hfiioB6l95znnJ804eGrelQjhJgNtaOgKVM0NsY6lw3zfu9OcZrmm_1JDUbf2y3ujkuzSRvIYw6WeYdIDX2x7e9-mKT9DjcO58BeunvqRysR90M4weg4ulnlAtJbLEa8o7Ef9rKyBWrqmUOImC8Zyg_GGSw8dihJEngu8nSgOu97mLHgv5q1sltvGnvfyz3NonX3zdCBXkzLFNgRlDHgU7nVtzqpgil8RMtNFNzX3PkeUf3qfxNqamz8KYjYMYJxqTNvcsCyIdDeIqLCWQfPqxk77tfnvBSNBsJq8aUDe_8WRQb3LwNl_u8qr6sz5E8NPHSif6TwV_zlvC-UYx8UqRkXvr6mFJhj9LKxo-3Yigl1w3MWnRgqjGniObA4qLq7Fkd3pUqbL0h7VfeJ9csxBw3470jGCdUVHYC5Iypo9Dzst1qTnOOwmzPnLfCmRIp6LnhfHnnrc20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از چه زمانی به کودک درباره اندام خصوصی‌اش آموزش بدیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672967" target="_blank">📅 15:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت اتوبوس‌های درون شهری ۱۰ برابر شد
مجتبی یوسفی، رئیس فراکسیون مدیریت شهری مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت بلیت ناشی از تورم و رشد هزینه‌ها است و قیمت هر اتوبوس از ۲ به ۲۰ میلیارد تومان رسیده و درآمد فروش بلیت پاسخگوی هزینه‌های جاری نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672964" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69e0e2749.mp4?token=UTurxs-JIX01pI0Ww8d0riVE--R7ggpwtshFFarERAe-Mf3SKnc9vD2MpIU1aUzyVT7zf477yScAGCaW0ZXj_qXhitZ_8Fav7khxtH-6aFN92NvwK59eUXH41pzwDQAbQWnSQK-Waam-9IqQ6AgdKU_nF_BN1Ulu-gVPYMt96DHVSX0LmMCdWtp-xm_gelHVlxNyRp6YpfnAODe01ozDi5pv4eQ8Mn0sN70ezcji8VFFbUYniOf08hGDZWARVhT7VTkQ-qMRA_Ima_WKNzNBNBNCwd8c9rJi0AoCg2g8Sg_eyKfKpT0C66TEnuVzvcPFqqjSrSNgbpcLV7Y64LQpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69e0e2749.mp4?token=UTurxs-JIX01pI0Ww8d0riVE--R7ggpwtshFFarERAe-Mf3SKnc9vD2MpIU1aUzyVT7zf477yScAGCaW0ZXj_qXhitZ_8Fav7khxtH-6aFN92NvwK59eUXH41pzwDQAbQWnSQK-Waam-9IqQ6AgdKU_nF_BN1Ulu-gVPYMt96DHVSX0LmMCdWtp-xm_gelHVlxNyRp6YpfnAODe01ozDi5pv4eQ8Mn0sN70ezcji8VFFbUYniOf08hGDZWARVhT7VTkQ-qMRA_Ima_WKNzNBNBNCwd8c9rJi0AoCg2g8Sg_eyKfKpT0C66TEnuVzvcPFqqjSrSNgbpcLV7Y64LQpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش قلعه‌‌نویی به تصویر ساعتش در جام جهانی  سرمربی تیم ملی:
🔹
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد.
🔹
اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/672963" target="_blank">📅 15:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev4rM63AI84XDqhw2e8lvgZri_sVnB0-BWpoOCz57w4aO8T141QNCbFO2PDksXYgeR2XlAFS3q9OTkRU2l8dOTUpk9x1ELk0M1zwomN2GHEdfYD10GgIFulxCeG-a7LzJvCZZkOdqiDbjdLhQia6S4oETq22Nyh1YvLcgDNF0MSRCaA_oJ6nbh8QK4FVGba8G2zJ7kpXJt7Njg51gh3XptUhNNOHirrdZOffjtvgoXr3XpG6gSEI-aH9tuaiq6Xs7HsYTQhU2othDAH3ei89rBK1ISZO-ta8Rgh5O0iZQnVjuedr6-NJUAfrPLmJ4gSQTSOcCWiSptHqt4V_cNYCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان خون‌خوار: ایران باید به لایحه تحریم‌های روسیه اضافه شود
🔹
«جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندسی گراهام می‌خواست انجام دهد و قرار بود عملی شود. مهم!!!»
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672961" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=bcUOR02YFhrX7Qqx2OFErMJo_rkAJwd88lkSQYEq_Brms77tWRpKQB06wJfzeHpg65bIyGIuFfLL1yUj29dF9v7B1CkmWNtMWAXNVNZupanHZPLJxjE62iciCthANUfKFXWrmLbJo-tmTEjolAZ5jdpwoKVBOG3qSo30L39tf1vkJXbeBsrr2MJkfhHEzmOuiDkkPepzwLvY5lsx4r0bGH4Sk9-KssI2jkgxnYrno-enuN-Wt9gSwjm3A_HxMZ725weqIfrxSYqYxQUoRg7-eRy8Hgjx92Nvj3b-e8DbiJg_MHIDzYRMgkpaKT0E5OhSUXq_nXLmb60xRLAFZLlNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=bcUOR02YFhrX7Qqx2OFErMJo_rkAJwd88lkSQYEq_Brms77tWRpKQB06wJfzeHpg65bIyGIuFfLL1yUj29dF9v7B1CkmWNtMWAXNVNZupanHZPLJxjE62iciCthANUfKFXWrmLbJo-tmTEjolAZ5jdpwoKVBOG3qSo30L39tf1vkJXbeBsrr2MJkfhHEzmOuiDkkPepzwLvY5lsx4r0bGH4Sk9-KssI2jkgxnYrno-enuN-Wt9gSwjm3A_HxMZ725weqIfrxSYqYxQUoRg7-eRy8Hgjx92Nvj3b-e8DbiJg_MHIDzYRMgkpaKT0E5OhSUXq_nXLmb60xRLAFZLlNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود/ حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672959" target="_blank">📅 15:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdqsG3vx-BpU1M30sIUDITm0usn8v99XJBFitFw2eHCbMJMjV_EzweET_c1XsqChURfFWMKDwupvJNJBI604J_30KDVj2gH--0tcG4lghTD9WxwJzxTBmBAnHL71GJ_pnKyhiSUrIKyg0EGYSNemNdCIAq-aam1oRx0coQERIHZXtk-vZuuOKBxbQJ77vIlZ0X17UmFFwucH5s2s0HJR_xkzVzDpPYFZfe_pMpLqOprPqwyygWoMH7Tof4wXtR0EHakChLZB-DLcOHxTfqfweW8xyKk7lZc0MmYF1yLutStIAYoOh7nMadPyPLnfIFcB8ZmDvLHrNcqLZJtcL-CXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدال مسی و یامال سیاسی شد
🔹
دیدار فینال جام جهانی ۲۰۲۶ میان اسپانیا و آرژانتین، تنها یک رقابت فوتبالی نیست.
🔹
رسانه‌های صهیونیستی این مسابقه به نمادی از شکاف سیاسی بر سر جنگ غزه و روابط با اسرائیل معرفی کردند؛ تا جایی که نشریه تایمز اسرائیل آن را «جنگ نیابتی سیاسی در زمین فوتبال» توصیف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672957" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672956">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9af66466.mp4?token=JKox0ET1nyj-Vjrnhagb8WtCIcVbNiLxlrw4TAm1vOgEqIk6D64gdt_Eu7T1settDoUGuQDjQ9BIYMd1lpzXm08G9SqrtHPBSt3PqWM_uaLqkDiWTXK5oXRMzJGUP4hIaLp34I662DhnY-_en_aldGIyGmpFUiM7D8t8lCk_6Dx2H19n8pXTyhKB6JPOuxor7AKM3eCM36NvJgV1Fvdd91pj_n73_m_N5b61MSj6yhmTSr_oSvR25BiDvDlbsSJxs2i9_4DBfFajRRoqBiEUrV-ETBWmvDt3D4DA6ZRdiSk3FxSw-27pc-40CMftQ-2J0yekZc5BCluTsAXuTIUlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9af66466.mp4?token=JKox0ET1nyj-Vjrnhagb8WtCIcVbNiLxlrw4TAm1vOgEqIk6D64gdt_Eu7T1settDoUGuQDjQ9BIYMd1lpzXm08G9SqrtHPBSt3PqWM_uaLqkDiWTXK5oXRMzJGUP4hIaLp34I662DhnY-_en_aldGIyGmpFUiM7D8t8lCk_6Dx2H19n8pXTyhKB6JPOuxor7AKM3eCM36NvJgV1Fvdd91pj_n73_m_N5b61MSj6yhmTSr_oSvR25BiDvDlbsSJxs2i9_4DBfFajRRoqBiEUrV-ETBWmvDt3D4DA6ZRdiSk3FxSw-27pc-40CMftQ-2J0yekZc5BCluTsAXuTIUlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت ۱۰ میلیاردی امیر قلعه‌نویی در فوتوشوت‌های جام جهانی سوژه شد
🔹
این ساعت ترکیب رنگ آبی پودری (Vibrant Blue) در صفحه دارد و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است. در حال حاضر قیمتی بین ۴۰ تا ۵۰ هزار دلار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/672956" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672955">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995fd9d2e5.mp4?token=qDUtXp6RXYuLUWpcxaRTngH9po5ATyV0ArReHBbr0PcnEFYuLGzhbpFgrRqIkvUYTIudry4V_ysolzTitysVNUKemvzlwMxd5AKO0uEGoCdVb0LANweAieNE1XLNGLFNMDZJGrQhsGbMYJqHICUoztz9HDDpxFCXo6CKXKYW45wjAC9bGVu21Gj4vIfmDZJoybOx5egM16-fQGuklvkoCthYMFeOl93vCBXx9h07zlJZcBRCylePer2PRpyFKAMaEYW7sOeEAoNVygg74fyXo_fKlwzVgW2uUXUdUWS8ptBoNenUuScjyEaiq7xeQDQWOCUC2Ah6BVJ8zOyDYLWn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995fd9d2e5.mp4?token=qDUtXp6RXYuLUWpcxaRTngH9po5ATyV0ArReHBbr0PcnEFYuLGzhbpFgrRqIkvUYTIudry4V_ysolzTitysVNUKemvzlwMxd5AKO0uEGoCdVb0LANweAieNE1XLNGLFNMDZJGrQhsGbMYJqHICUoztz9HDDpxFCXo6CKXKYW45wjAC9bGVu21Gj4vIfmDZJoybOx5egM16-fQGuklvkoCthYMFeOl93vCBXx9h07zlJZcBRCylePer2PRpyFKAMaEYW7sOeEAoNVygg74fyXo_fKlwzVgW2uUXUdUWS8ptBoNenUuScjyEaiq7xeQDQWOCUC2Ah6BVJ8zOyDYLWn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشق تو در وجودم و مهر تو در دلم با شیر اندرون شد و با جان به در کنم! #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672955" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672954">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=GiP06afaCqz2nj3Sc9LQo_943rPa99SI_SXrSq2pHC11gE4sgzTY_ykoKCq0Kq2pXSHaS9Q6MBU4giBdbbex-ZJhfzkJ2jng2aXledDTPHcqEWKcL4ARD6fLLb_3ubtoBbvYhEEWpv2yq5pH9rfVmHnECqMdeCB30P8Pok4vqClTCRk6nZiQcYClHDYSl_dgLbvlf7wkcbiD3Jk1z4An6xUrjusiWO7THr0jKwaCL3x0zfG7YsjpKD0aecybKW4HuwLPiIyWKsgSn6TEFRp1JuPpy8Sfv5xBiI9gEF9WhQuQ6zpWY4Zv1DnmJIa9qdyyK_XiVRMEReOqI4pwohH0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=GiP06afaCqz2nj3Sc9LQo_943rPa99SI_SXrSq2pHC11gE4sgzTY_ykoKCq0Kq2pXSHaS9Q6MBU4giBdbbex-ZJhfzkJ2jng2aXledDTPHcqEWKcL4ARD6fLLb_3ubtoBbvYhEEWpv2yq5pH9rfVmHnECqMdeCB30P8Pok4vqClTCRk6nZiQcYClHDYSl_dgLbvlf7wkcbiD3Jk1z4An6xUrjusiWO7THr0jKwaCL3x0zfG7YsjpKD0aecybKW4HuwLPiIyWKsgSn6TEFRp1JuPpy8Sfv5xBiI9gEF9WhQuQ6zpWY4Zv1DnmJIa9qdyyK_XiVRMEReOqI4pwohH0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهارمین سوگواری آیینی محرم شهر با حضور و اجرای بیش از ۵۰ گروه هنری از ۲۷ تیر تا ۱۲ مرداد از ساعت ۱۹ تا ۲۳ در میدان آزادی برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672954" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سی‌ان‌ان: دولت ترامپ موافقت اولیه خود را با اجازه دادن به عربستان سعودی برای غنی‌سازی اورانیوم در خاک خود بدون اعمال سازوکارهای نظارتی سختگیرانه معمول اعلام کرده است./شفقنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/672952" target="_blank">📅 15:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
مدیرعامل خبرگزاری قوه‌قضائیه: هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
🔹
خانمی که مورد بحث است نه زندانی بوده و نه اتهام جاسوسی داشته است. ترامپ در شرایط فلاکت‌باری قرار گرفته که نیاز دارد از هرچیزی دستاورد بسازد. حتی…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672951" target="_blank">📅 15:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K3Ig5UPqg5rzfl-e--OhbYbbysnh-FN5-HQuPpok2I1PNG2wl94ID1ZyhKyvr69u0UFeFxJWHSfMgKiaP1QcM5ZPnCz-TK8NrDhx2h0kVqrm8iGH2RExMn9XPa0C9wOaUijmMpDUpbFugpnZ3m3JAPFFfa18wJtXPo07CMWF2ijQC6fJIHm_K0V3DIG_wrD-PEH40q3LxCtP2V_Csole5b8inoWjcV32RRh5iseJvnAlFkkeW-N9740HPBPlSz2GBxLvq5t206XQjfNRwjR0kxFEGmcT2_f3xCkv0C10PZM21ue9SUYmjJc88dkGn8ivbTW8Vb0r0ZKRHJoG0VzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمایه‌گذاری حرفه‌ای در طلا با صندوق رز ترنج
🟢
صندوق طلای «رز ترنج» امکان سرمایه‌گذاری در بازار طلا را بدون دغدغه خرید، نگهداری و تشخیص اصالت طلای فیزیکی فراهم می‌کند.
🟢
این صندوق با مدیریت فعال ترکیب گواهی سپرده شمش و سکه و استفاده از ظرفیت بازار آپشن، از فرصت‌های بازار برای بهبود بازدهی استفاده می‌کند.
▫️
برای خرید با حداقل مبلغ ۱۰۰ هزار تومان، از ساعت ۱۱:۴۵ تا ۱۷:۰۰ وارد سامانه معاملاتی هر کارگزاری شوید و نماد «رز ترنج» را جستجو کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672949" target="_blank">📅 15:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672947">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d463819eb.mp4?token=SA8ASZrNYMFc1CTw14vYwR6wQtN5BhU_N_sK0jlHm0dN6MeTjeYQbYQSq-ubz4w1DF00wAzJuog6tRIsaw4FybK05q8Sl4SgfTlGRxZl-xaUUyJbU9BCwCkIRLig7EErWdflEXIHgTqswdO40Px04L_HytFtkKXBDjK7IEQP0tAxndsWMgNgTwWLkxD4wKLtjpBz49sE_BMIsR4NJ0qTGy4JwOUYh44jrB-lFEXt608Y5d7dicAiyTxL3D5LFqTeNo1A2fpAiBJUJp8_5wnyV2_3hEwmU5_OAykzVs9-ew2T-lmvF_LMD1XIbLfVECCMzoYWFc1gMuPTv_t5rhA6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d463819eb.mp4?token=SA8ASZrNYMFc1CTw14vYwR6wQtN5BhU_N_sK0jlHm0dN6MeTjeYQbYQSq-ubz4w1DF00wAzJuog6tRIsaw4FybK05q8Sl4SgfTlGRxZl-xaUUyJbU9BCwCkIRLig7EErWdflEXIHgTqswdO40Px04L_HytFtkKXBDjK7IEQP0tAxndsWMgNgTwWLkxD4wKLtjpBz49sE_BMIsR4NJ0qTGy4JwOUYh44jrB-lFEXt608Y5d7dicAiyTxL3D5LFqTeNo1A2fpAiBJUJp8_5wnyV2_3hEwmU5_OAykzVs9-ew2T-lmvF_LMD1XIbLfVECCMzoYWFc1gMuPTv_t5rhA6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مکزیک زیر آب؛ سیلاب خودروها را با خود برد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672947" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3595950301.mp4?token=bgUp8r3eM--csrI3ZF2QI-VSbvFdUX1j4XGhQLAVHEghVN0LpttI2VUGqSQZ6e7QcW6HFOLNCY4Vx6TfwFfEDQkFCZD_ixHgfRHmXJPf1nJiOmEazuvu-WhC080j7TN-LBQGFJisiTqD1W_gCa7tnBoxTMM3QdBr8NIFpPWrfYHQ3JUmjshF6vAp0lVyikWPiFETrkBm_NXG3ihe5FF_NBWdfqcPeqfmP2T0XvSQJS2IhZwPQQHQWaXw_Oqw9OdmBmueK9whWy85ebuF0ijIlxqgGPpdy_9QaYplwlFKKQxF-fgXT5B0o8BlJ8KKMP9Cri4rXQXvZgg4hrm9Hd7c2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3595950301.mp4?token=bgUp8r3eM--csrI3ZF2QI-VSbvFdUX1j4XGhQLAVHEghVN0LpttI2VUGqSQZ6e7QcW6HFOLNCY4Vx6TfwFfEDQkFCZD_ixHgfRHmXJPf1nJiOmEazuvu-WhC080j7TN-LBQGFJisiTqD1W_gCa7tnBoxTMM3QdBr8NIFpPWrfYHQ3JUmjshF6vAp0lVyikWPiFETrkBm_NXG3ihe5FF_NBWdfqcPeqfmP2T0XvSQJS2IhZwPQQHQWaXw_Oqw9OdmBmueK9whWy85ebuF0ijIlxqgGPpdy_9QaYplwlFKKQxF-fgXT5B0o8BlJ8KKMP9Cri4rXQXvZgg4hrm9Hd7c2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: پاسخ ما به حمله به آسایشگاه ارتش در چابهار برابر نبود؛ بلکه حداقل ۳ برابر بود/ تلفات آمریکا در سوریه بیش از تلفات سربازان مظلوم ما در چابهار بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672946" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672944">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dviPsx0H4QZszkbPjxLC6A4gldOE-o_xS4Im8vm-Mm3Q4znWL7HRerJVMlUkh1zSi4hhe-OXjClOxX3xGldy-4BkIvbOEImFBGx2Ymq0QvPpR0RDTSx4l5A_RXoIYD3RJkfwZYzuz9hqXhYgCEtTf5hQltazfmPtB06odW83aSoNG-E1U2nsHnO7-Ql0xjigRjQ_ToSHGoJP3jT1PtH7m8vVcy1l5Dicsfmeovo8XgR8lTL_HdkmsP7Ng3aUJQKl0WQ-mFa8XuHYY2AQZT1Yeuxr9qSDy1_jV6s6njgy6-BZHox2rpdkkmG6XQ3C9Bvrwtc8xG_O9mWcAIYyvboRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل خبرگزاری قوه‌قضائیه: هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
🔹
خانمی که مورد بحث است نه زندانی بوده و نه اتهام جاسوسی داشته است. ترامپ در شرایط فلاکت‌باری قرار گرفته که نیاز دارد از هرچیزی دستاورد بسازد. حتی خارج‎‌شدن یک شهروند ایرانی-آمریکایی از کشور.
🔹
این عکس از دنا کراری امروز منتشر شده، بنا به ادعای رسانه‌های غربی، او دوسال به جرم جاسوسی در ایران زندانی بوده است اما مدیرعامل قوه قضاییه ادعای او را رد کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/672944" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672943">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4nyU7bVv7nR987BJRys0U6j_viaZxJiVABmkk9qpy4AysfXFMzqY0c1_9kWHPLVbT1DykQKaQsSEyKXycMrkBlizTnEPou_iZFJvAQaN3EnRIfW9sULGNvp_x2nmZgJmhnoME5iBVXGiEhWNOM04E_Ees6gODUywvv9sX48T2RihR3isP9erlt35_2UaPMBm2giPPKxkakCe8nIlP98DF8OP91phEJbY6hJgdlEF6dYv05x7nyclkOvAhLjfmny5qr9yL14KmYyhOKIggbq4yDJumzawZfUTX7eJaTMb9c3j9QDhpMB7i8qBZsVOOnPFlIdBiGZhbTbHVVNDOXZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وریا غفوری به شرایط جنگی و تأکید بر وحدت ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672943" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=tNjNOYMZjeaKCkMlQhjFvOiGDXihPaKkdP-IZeQ0OIJa-4D5toF_6e2i79Z0gTb0iC6qwN4VDX37Pf7AeAfLRrVLBxv4obhePyZDjfUoQK3wubhFMuFPzUx03w8YXK39pklzzxWkws3at-vuEddswqTIQSFXVwV89xlAsorNvzbiTQdOLSTC3mGNjynfpOJPiJr40oWUaxxmCYOQl1trYw9bg03K7_3F4IekSsZJ862astlYgiioWwn7ZK9-JBOzVyG71mEdKBffl-6ElkiVPEda0AX-kgUz3iFnnhnFNU5GokJ7L2e_4qUAWGWH564xS_oaVbjPBFHcueaZ-lX6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=tNjNOYMZjeaKCkMlQhjFvOiGDXihPaKkdP-IZeQ0OIJa-4D5toF_6e2i79Z0gTb0iC6qwN4VDX37Pf7AeAfLRrVLBxv4obhePyZDjfUoQK3wubhFMuFPzUx03w8YXK39pklzzxWkws3at-vuEddswqTIQSFXVwV89xlAsorNvzbiTQdOLSTC3mGNjynfpOJPiJr40oWUaxxmCYOQl1trYw9bg03K7_3F4IekSsZJ862astlYgiioWwn7ZK9-JBOzVyG71mEdKBffl-6ElkiVPEda0AX-kgUz3iFnnhnFNU5GokJ7L2e_4qUAWGWH564xS_oaVbjPBFHcueaZ-lX6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: فلسفهٔ حضور ما در جنوب این است که به آمریکا بگوییم «ما آمده‌ایم که پدر شما را دربیاوریم»/ حضور ما فقط برای دفاع نیست. طرح «پاسخ پشیمان‌کننده» در پی حمله به زیرساخت‌ها در حال نهایی‌شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/672939" target="_blank">📅 14:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e259eddc1.mp4?token=rXRs6nwZpXZ1470SzU7q3_uaCSUrDxh5z9mIJQPYNta-Uh9soI7lDqC6CvZbMRGgjI5F8WUmCzYlPbZ_f00Pp5SiDwQuoLDMOVdJ5XY9NunYIJ-zYQEUgp18PfSBM7WWUEsiGafTVdivdUzHMBAJhFBA-bpj5zWqjy75Vuqo25IamY-2jj-HkTzJ9kFP5l6ax-DZ2OEK7l1lOAmAf67UglL9zq0p4X6XY4YIhUGMH00ccmiH3rbo9_J_Q-Qa41ftashphIZrQz8333XRpWlu021h_9VzqcxJY_niEN1FVyPSo2LGls_EJm1ePKompX8RRuv7E4J9oIKrFKsKq_gIF5oIQ7-AcIi6n0So-Z6so6K0xh3pOd1K_oz60mpIyOyL_7PZXn8NYgwmNJ-_w3w6w_c9vh_AZQDuJfkIxvTiHD7i6TEY3aAkIepioYVMsaKdiX_eO06gykI29srg_lrtqyEQ5QOiarwJmubDCA0aKRvrAX3Yfi0Sx6TwQiWQ2fdVg1bzxaCXjtCcs3mzA83NZsGECx41FBrgQn8H7sgn8SB6FfJn4Z5AIA-QznGA3_D_SGLGO8vMNiZEbcCfKFnCg9qdHqhcir3rMXbEcNrXUz71GB8Q5Cs1HbJjY1ZppL4_6SfGhaPBFlIIcu6FJL-JvCVL3g0cA3Kd4xYTLbO_sjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e259eddc1.mp4?token=rXRs6nwZpXZ1470SzU7q3_uaCSUrDxh5z9mIJQPYNta-Uh9soI7lDqC6CvZbMRGgjI5F8WUmCzYlPbZ_f00Pp5SiDwQuoLDMOVdJ5XY9NunYIJ-zYQEUgp18PfSBM7WWUEsiGafTVdivdUzHMBAJhFBA-bpj5zWqjy75Vuqo25IamY-2jj-HkTzJ9kFP5l6ax-DZ2OEK7l1lOAmAf67UglL9zq0p4X6XY4YIhUGMH00ccmiH3rbo9_J_Q-Qa41ftashphIZrQz8333XRpWlu021h_9VzqcxJY_niEN1FVyPSo2LGls_EJm1ePKompX8RRuv7E4J9oIKrFKsKq_gIF5oIQ7-AcIi6n0So-Z6so6K0xh3pOd1K_oz60mpIyOyL_7PZXn8NYgwmNJ-_w3w6w_c9vh_AZQDuJfkIxvTiHD7i6TEY3aAkIepioYVMsaKdiX_eO06gykI29srg_lrtqyEQ5QOiarwJmubDCA0aKRvrAX3Yfi0Sx6TwQiWQ2fdVg1bzxaCXjtCcs3mzA83NZsGECx41FBrgQn8H7sgn8SB6FfJn4Z5AIA-QznGA3_D_SGLGO8vMNiZEbcCfKFnCg9qdHqhcir3rMXbEcNrXUz71GB8Q5Cs1HbJjY1ZppL4_6SfGhaPBFlIIcu6FJL-JvCVL3g0cA3Kd4xYTLbO_sjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار غیرمنتظره وسط آب‌های آزاد!
🐙
🔹
هر صیدی داستان خودش رو داره؛ این بار مهمون قایق، یه هشت‌پای جذاب بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672938" target="_blank">📅 14:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672936">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حمله آمریکا به سایت نیروگاه دارخوین
سازمان انرژی اتمی ایران:
🔹
آمریکا روز یکشنبه ۲۸ تیر ۱۴۰۵ حوالی ساعت ۳:۳۹ بامداد، با تعدادی پرتابه به سایت در حال ساخت نیروگاه دارخوین حمله کرده است./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/672936" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64f806a19.mp4?token=Rdd16VcYGz_Rwz6gH7G4roTcAPAbLnsNFEfYov1zKXbOSgRLMflaSbGXR1FW_WEajCJJFYfMBzWbdbq89vU54_y7vyMSxbgbrhZ-QN9X0a8ZkDSkHeesWBO5B-gRWSb8noV3zXsiesq3vH5CrDP9z6FQg8DcGMq9ZDcFXO2f7sEnmH4xy3BpHEQaVk5NihiCttIkFgBAHl4-n9LwPeT4aLx3SRq6f5sJ-6KAAIabcqhv2kYMmYn_dSoT2clVFcoJQj5fSLI6xlarPUxZ1_iSBHBk4v8OA9SQDenDblv77e3JuK-4Zdxonm1umXmwVcle6pcfoqEVwbUX45SzrRKX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64f806a19.mp4?token=Rdd16VcYGz_Rwz6gH7G4roTcAPAbLnsNFEfYov1zKXbOSgRLMflaSbGXR1FW_WEajCJJFYfMBzWbdbq89vU54_y7vyMSxbgbrhZ-QN9X0a8ZkDSkHeesWBO5B-gRWSb8noV3zXsiesq3vH5CrDP9z6FQg8DcGMq9ZDcFXO2f7sEnmH4xy3BpHEQaVk5NihiCttIkFgBAHl4-n9LwPeT4aLx3SRq6f5sJ-6KAAIabcqhv2kYMmYn_dSoT2clVFcoJQj5fSLI6xlarPUxZ1_iSBHBk4v8OA9SQDenDblv77e3JuK-4Zdxonm1umXmwVcle6pcfoqEVwbUX45SzrRKX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پل در تگزاس آمریکا به دلیل وقوع سیل فرو ریخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672935" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تیزر قسمت ششم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای فرهاد قائدفولادوند که در اثر تصادف روح از جسم جدا شده و در حالتی که جسم در بیمارستان و در کما به سر می‌برد، روح نظاره‌گر دعای مادر در زیر باران، نگرانی و زانوی غم پدر و بدگویی همسایگان در مورد خودش می‌باشد و با وارد شدن به دنیای برزخی، خود را در حال دست و پا زدن در منجلاب عمیقی رؤیت می‌کند اما در پایان توسط آقای بی‌دست کربلا، دست‌گیری شده و از کما خارج می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فرهاد قائد فولادوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672934" target="_blank">📅 14:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHwtyByG2KJijutR0MjMEOoZnCwxPBhRM9w2THu9j5RmvUedbH9hF2md0yOrR5CP9p2tYSieXWTE5mn69VPr7j9lBhSfnlNYPup_ibsMMF3xnP2_38WXufJhNwxRrb9ysLQse9_0kZcq6NOxyGRKNF9a955gu4MOz1f_2-OM6ipHUsi7G4vo4fUilWORyiOcSE-rqmiiU_6qvQLS47zA8K4R-trKjtlBDWRJJFN3f90_QSDCmKxfBh2yme8UTa6BF2IgWX5halyjng8RpZXzltMPEhedEFZfujND55NywYJBgvj7c48VW0iCQ3PESwt9YGF1W51YOeQIJXPTWr73qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQHr2XSiP_9rGxIFLYkslAzPjpJkY1K97IuYtd2oJgcH4eP3J1fSkbYjDONXdrBt28t_B3dHC_HRldo81e4SANV54XPSifMdfZtAwUdeC7exfmGcnDDblDqrBQai6jr_mnLTAXFO_3E_7oIbwEnc3vbwlygwcmd7MDIMiyNTK_4VGDBYmhPHcUTbmeVeyBSNecQydfr4YTInQXBcj1NJBrE5AlPBbWKP5SEosUFOFhvLSeTVzQqyG3TDTgasxg2pWY7_CKdhYn-L5jV43QVFlznMK_j6AQTbe4savedt-ZC3qdQGPVFS4NFijzbdPY9BybbZ9mAwlSK3kWNRn5g3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VI2jqqag7LOgFns6iPT76D3VdJuMnCQC5R84dx_JNi9tiY1rSL-E7J3HXrcYjYpTHmZotuarxI5KRgS173SWkJjNUK1cMT0L_ETSoTzQQOUwGieRQ52Aoi2Y5-Q8wz-KZdv-xl9PHre43cwe4u5qxTKh2zA_6ccJR0ok9ICy7uYK6_yNiIgyQwzdH4C9WW3iWL9biTSnshx_nFbAph1B3_l5qeOLXWGhFm26_FGY47B-OZ75gUm_JaF2OL4zFHoEkg85HvH7M9ZGHHd-Re7boj2bJSPb7kOsinqxPST232A7aZbfCEB_BXUnXbEtRwbly4YI9NbFfnaCnIidp2eWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7bvS72DXTH9iFCG_LyM0mItkCFM9GBqKuex1FIaeL627rh8Z0EB2FsLr-n-VBvlfbl5hTht8meP2WLs9VChAXy_L_tjrXNHCVArx-fGc4YjZe9cOO0M3UBp0sB8Eb_rc34oEqwPqqlZyNpKddLq4XTX0JDnguovLR9PpD1oKNKp6DSQHkoIFOlEJnp22qdNhV6Vq45Xka4bjS8K3d9l4Qet-l6bDHwaB6lQo--iFXbg0LdmLmP26A9HiaIcflUj19b2MkuZoYple0y96qsd8GcpNx_YygAHekdAu6mOHuz4Ks3HW0RmcAEmYMsa6HNC85WoHtaV_JQNpU_rldz24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFaJd6i-WauH743Gh8O3cd7TwgMJF01AOKTLVsEEEmaM62kZTNKJv2QVqKRVgyc2qWd6vS71RpxEkvyo2trD1czgwcJSTnIspYkG6t1-HKDL0qYaaUb4R8u_3qs8m5ASqaaMOaA3Rnq9HbVy4lWtLsAGCzD1ipo48YMw2SyfNrw0pa1jhU15UD6wq7qWxzvNQMTuxn4HhSA2subXhRcMp-eF9_YQmMjPrfurfAzg-IrXDBqXLewrIBOHqf3D3F9rHWHr2VhRIpo4bOv0HJRiDz5JQWBv8X1hEFhJ4Ufxo5loYPHWkjLLVMtxvoObfMeAKP-H03lxSz1KGMi7wI8YeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtI9_ZnaXSse9o3OXhBZIR0yNq_dcpfUGGsL5hrlHzP3ZoNCHKxm_QhScujo28M0B3VxcgJZyZIDgl_Bff3oTNIobNbgXVTL4Q0lYrGzsddVlMjg_77FUq3S84q0Mgbpz-r2jGwwNPsMT4MwHeDck5ThC9vyjdmdPixXiVB9NJ7sIIV9DohtQO-OCFVIEIYUAKMVbvZPFe55TXdcJQoKW75kwPFNP8arM7BmCwDDcPsbYGTHM7FVpcDe396kxTzsn0zR2ffKb8PkTIrvdvKrF-E75yAyIDLvwJyvcndN-QLEDr6AOltvmniXA0p8Cm3pEw13dyOSNcld2FBiapVerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVOoP89s6x104A9XTC4mQmOFS4c7MUQGOb8l8x7oM5vJKi75jlbB6Qxaht2lnzEFVBdHEOJ-xo9kYStFzJDCeFBbhOpZZoMEjQLkuYQEcSGM28eFGb-LwW0jLYo4kj1cW77DO_F8sjiKNfhGCUH3Nw2ZfSQi0iSWfn0Jtl9Zls_RCVZCQNjtSsHz1xNlO8FQENq3xYWepSgWWsjQqHOSFddQlF7dgN2TkZs7Nq0mXgsa_G5xYzPNkHmOtOAEY88H-oGhMze8xQ4eRIBSsQjplat92n4Z7vv_mZKNFIW7uOOOHSIml_5wY2BBu55cyMXrWarM_TEJVtQndAz3oYvtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-4KB86trxOkOyNA5M4nCH5g0C7fUsgItNOtFL_HKjU3bpPhtdXlYEJuG5ePZnKrBUYaCOQSIxvQcRqxMoAQnF9GQBf9vawr_Vo2KzcfLa0yzDy4f5iuIzaYIXgrzkvPyGWDdcmIuBNynLEjFgfCHSN41btcZEIAosew5_YJxCFprvMr6wW4mTMu9aOlfFXOq6W_cQim5azAXOO106OaifkZ61xVlRh6qcHBNUjfBZ64FDBtVrg5AcHlyrGs3I9aW1RejZZorhxr-uJzKf0X0zDBo-mseT3PE_zQd4rSMmM-vJeVl5eiT3ox-THQBCUOK8lyjCDRs42388Fb9x_NtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx1u2AFmZ1Zxint1_n0jJTCQ1DRVkuJrs-KnOiwfnxniUSYmEh6GLemH4fA2YMJeBJcRRTnt1Y5DC5ABza5DQkfXDCmpvBeIMbAjHCc9EHHKadI4KET1AfYplR--j1j74kXttSQyyV3QS5D9k1sbig8g-yGRgohHj-BFT_rR4CFBM0vuRdsyCY4ynzIAHaImphbeMuoABU6Z8Liq7sSfZd5keLXerIF1Lq-Q8hnfuJzK2w89E84cbfPDFroCfUiY_GIFfwv_Y1SjoWHNgzMy0tz88nRm9Q3kMJukPSzpHPdm20yiwaNzZJ3ve9y_4J0NDQRhfN1NnOPsIVNeXSeDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQaYY482fZFYlLjfCgDYvKodXQB-82icLOxEFpmn_iVtQQ_wajmFNi51yjZ8EqK8LyE-CG5ztIDEcukhaZuUPUvCJu5dXT9T-REIA9PCFr7zesBcxuDzZ-MmhRA7j18vq9ssFoH3Y7cIek_KUS62ODpQNaSGH5VQx6z2676catOzITCKc8g-43bWm4WAMF1bdsIEgBjGOEcqi5Fa45SuaDJWN9EuIrJV7Xrn3L9yl9ZKhuUCeiuKP7qykiK2xZTjQq9zCx4_M8E2Q6ODaOQFxdANW50thYvnqNokvmuo8awoq8t2UPixvEV1GFjcekEl99FXKU0Fy_gR4D8ONginkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر نمی‌دونی با هر شلوار چه شومیزی بپوشی، این راهنما را از دست نده #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672923" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672922">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c485db783.mp4?token=WeHbEDA7ofqUje37nXx9aEvyBEO2qecikn7fdrE3ptRk6Qb93ZtFoL90ahq2Irirvt2i_yhDcHRXAf-vezvRZIMyX6i8EhPHqPxVK4Tw5exhOn84vQZIjeW5LRb0xh9-kyigxKrUwQssz8TvOMYrJ_4dOMuGTZ25mIdCjp_SbmCuvoNzTtHl_ZzYERbqBBAriNZLoJWumv4hjhZM6qFn-6Bw2X1bV7nnbpv9lnP6TVhywYRXkKEXJaRBwg2qHhoEqd1cT6g4MvovSX2Vou95tGpyeKdDtDR6EU0FVWOR-TmE0f0K1XK0d8aaAhONrFrd0btB4rVnnMqlR_w53no2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c485db783.mp4?token=WeHbEDA7ofqUje37nXx9aEvyBEO2qecikn7fdrE3ptRk6Qb93ZtFoL90ahq2Irirvt2i_yhDcHRXAf-vezvRZIMyX6i8EhPHqPxVK4Tw5exhOn84vQZIjeW5LRb0xh9-kyigxKrUwQssz8TvOMYrJ_4dOMuGTZ25mIdCjp_SbmCuvoNzTtHl_ZzYERbqBBAriNZLoJWumv4hjhZM6qFn-6Bw2X1bV7nnbpv9lnP6TVhywYRXkKEXJaRBwg2qHhoEqd1cT6g4MvovSX2Vou95tGpyeKdDtDR6EU0FVWOR-TmE0f0K1XK0d8aaAhONrFrd0btB4rVnnMqlR_w53no2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشی وضعیت لبنان از مناطق مرزی ایران!
حسین پاک از خط مرزی ایران: پس از سه سال حضور در جبهه جنوب لبنان حالا در جبهه جنوب ایران هستیم. جنوب لبنان و جنوب ایران باهم در یک جبهه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672922" target="_blank">📅 13:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsnLE49XdF0y4YlxOwuoztTNOWTbc52g6BVUuaSVSwbd7az7zJCOc6JDFywvTama8dr67DhUu0I3h0YvTdKNmgBTY2OANhB-_A3OSkqZwdVFPfbgc4WdkCpC5KiCKdPXDelAPEblS6YRoRTOUv2oD-mIMYEd2UdiJc5BwZtFI7gcRpMAxFp9z1NyruS5_PSVtEpUixQ-ZdtKtcz5nGZUXt71mT4dhrNaRCtRfAUjLtEHnUy6HILgeesFqEQZFq8tVo57IobTWXPtysV-x98RAYMaTLyTeZ74kE7_sCi2U2lOlMwsQqdlQBhuzRGhwvWhUS9MwJVnj9J_IvvSGZ4nOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸۱ سال پیش؛ بمباران آتش‌زای اوکازاکی توسط آمریکا
🔹
بمباران شهر اوکازاکی، طی ۷۸ دقیقه ۱۲٬۵۰۶ بمب آتش‌زا بر این شهر فروریخت. این حمله ۲۰۷ کشته، ۱۳ مفقود و ۳۲٬۰۶۸ مجروح بر جای گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672920" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672919">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030701a507.mp4?token=hh5d8WmG6wD93AnSg4QY_XCVsVytBoLCd8pT4YViy-uOqqqKVQ8HFYBMmQYwJXs0e7eRgrOApIGPMgGrPtiB4I3Ml1hpUOpVRN-nRZ6aTW0WouT6P80ZvVOPDurUXqE8DlqVEWbUVgp7KNxVwDqSmrle86WUIK0gDnFSKHwrMuKiq9RfWatAEmf4HbvNJ9RIupumBXgCLNvMlS5siM0fta_PnvwcRcFn4F3H96MlyJ9GdprLSUx3EXj30hO5Br9NQez3pVxgM2CHw25wE6j_mxo30BKufBWWjjwzLQ85Ap65U0V5ayTNNPnb4k8I68IJnCLyPNNFPG92vn2CxWd_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030701a507.mp4?token=hh5d8WmG6wD93AnSg4QY_XCVsVytBoLCd8pT4YViy-uOqqqKVQ8HFYBMmQYwJXs0e7eRgrOApIGPMgGrPtiB4I3Ml1hpUOpVRN-nRZ6aTW0WouT6P80ZvVOPDurUXqE8DlqVEWbUVgp7KNxVwDqSmrle86WUIK0gDnFSKHwrMuKiq9RfWatAEmf4HbvNJ9RIupumBXgCLNvMlS5siM0fta_PnvwcRcFn4F3H96MlyJ9GdprLSUx3EXj30hO5Br9NQez3pVxgM2CHw25wE6j_mxo30BKufBWWjjwzLQ85Ap65U0V5ayTNNPnb4k8I68IJnCLyPNNFPG92vn2CxWd_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نباید مسائل خصوصی افراد را فاش و یا به آن‌ها ورود کرد
اژه‌ای:
🔹
ضرورتی ندارد تلفن همراه فرد را در اتهامی متفاوت و غیر ضرور ضبط و همه محتوای داخل آن را مشاهده کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672919" target="_blank">📅 13:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672918">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
بهترین رده‌بندی تاریخ!
فرانسه ۴-۶ انگلیس؛ باران گل در میامی، سه‌شیرها با طعم افتخار به خانه برگشتند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672918" target="_blank">📅 13:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672917">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=vAdKPqz0nCvMgN0qb49iIMXxexQO1ov_Aue_A33l7w4YllsDDfmbcSY-RN5Nnd4Lnl1szUvyLCyzniCmsmWz26thX_331NlMHW7XTq1YYGiPc-HdldVucFthqC2InydV4KTLAS3Vvr9XsUrdhDSNenj9QkMhXtJNwrQM7a-uharb6JaxJCEdxSSE7MmiuGsOET8VuKiWCrB5MnnccPmDgICmDnLTuMSzG2feA9xZWWagvkr61BTypoRzLhe0fs1nfQE1tb4Ase7T7FvwuPZYTl1jMYp4RYf6uv9BejOT-RCzrw9Eaf18B2lvdsNhS2sldPcZMz6pPvkvjqrzfGCsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=vAdKPqz0nCvMgN0qb49iIMXxexQO1ov_Aue_A33l7w4YllsDDfmbcSY-RN5Nnd4Lnl1szUvyLCyzniCmsmWz26thX_331NlMHW7XTq1YYGiPc-HdldVucFthqC2InydV4KTLAS3Vvr9XsUrdhDSNenj9QkMhXtJNwrQM7a-uharb6JaxJCEdxSSE7MmiuGsOET8VuKiWCrB5MnnccPmDgICmDnLTuMSzG2feA9xZWWagvkr61BTypoRzLhe0fs1nfQE1tb4Ase7T7FvwuPZYTl1jMYp4RYf6uv9BejOT-RCzrw9Eaf18B2lvdsNhS2sldPcZMz6pPvkvjqrzfGCsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مناطق مرزی جنوب کشور: آمریکا که قرار بود امنیت کشورهای عربی را برقرار کنند، امروز توانایی دفاع از پایگاه‌های خودش را هم ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672917" target="_blank">📅 13:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672916">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiZzwVX472FvVbohdbW6JXvHGipKWkLuhGkWWlqG6lbTp4Qtqo2uU6vEhT8eknC67njUvutxa9AyKc4X-0PF3vRnwMUsj_6IujYuFsRFcOg1zG5TlvkVb-4sUfwbImkcKHhPomOQBDQOcUVvSAYxJuKfyZYm_Wv4ZdEmvyKfjUF2Ib-AAjfuRpuFs9-vrnKHaLYS1yv0F-V37fdvKVjA669Gogy-MNum9EHu3qgyNqal7jKvUGoVI-4BQafQweZtyqPfEmIZ_tI3osFduGw6LI8B44KdLS0AHNz8SlArlqmEFBK-wC95pzK-fq_eOyTLlovqUHIbUQx3T9LKaa69mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور رهبر شهید در آب‌های خلیج فارس در تنگه هرمز
🔹
در جمع دلیرمردان نیروی دریایی ارتش جمهوری اسلامی ایران / مهرماه ۱۳۶۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672916" target="_blank">📅 13:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8faf84a6.mp4?token=slAjXSpiics99YlgsTK-SnQnGWCdjcOF7D7eQ_mkz2HSTNSHYYvtN0_Dn_ron9tCS3yfquWJiiYxMIkn54OkFmvSrstEDyIvFeYNJufY_bMFlJBfiS3i_7CtKn05ExBMraWxlI7CaPtCOT6spf1RaiKefuKah1Z-jI6IxdlPfN5LHzGlqDdZflNhJ0HsFosn2SCKvBKeI0Tb5LDmo1GskOMz3vdmi94B-mSvkTT8VQmnseRLUjt25lHk5AkO1G8PswWR8biaonu7FEKp1ba9LRbmJ8IwW9DVEHKK28mUHTg5chRUC1q4CV3ultnXwksbj6U431ZW4IhvvX-Wrop0RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8faf84a6.mp4?token=slAjXSpiics99YlgsTK-SnQnGWCdjcOF7D7eQ_mkz2HSTNSHYYvtN0_Dn_ron9tCS3yfquWJiiYxMIkn54OkFmvSrstEDyIvFeYNJufY_bMFlJBfiS3i_7CtKn05ExBMraWxlI7CaPtCOT6spf1RaiKefuKah1Z-jI6IxdlPfN5LHzGlqDdZflNhJ0HsFosn2SCKvBKeI0Tb5LDmo1GskOMz3vdmi94B-mSvkTT8VQmnseRLUjt25lHk5AkO1G8PswWR8biaonu7FEKp1ba9LRbmJ8IwW9DVEHKK28mUHTg5chRUC1q4CV3ultnXwksbj6U431ZW4IhvvX-Wrop0RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک میدان نفتی در کویت دچار آتش‌سوزی گسترده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/672913" target="_blank">📅 13:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b42b0015.mp4?token=gu-01ayOGfbSaCVV6xuoYHPGPieNVVKNBUtYYfG3CjoVyPDetCmJLzdUxPa_Jq-PnRV6T6ZhkKKB5fEGjggM296FtpCMMe7OSPzL49RUAJvN9RHvjLFpcyeQMpBgkTSsi5H0hxY5Y6CwQYlnkspBlwMZr_jZraenzwDWg3pWt7PO2sOo4F9Hi_hUrlpsnfRvVX8BYYYXYc1yYMXuJwlv50gDD7fh7A-bYoetjpFa5-e8Bw5gRorDR5ZFtcKZ2dW-R0MDbbRmfU-6Use_kssgaXbh0EC4ZVd5YxYqXh-yy6_8z9YUDNKlTNV-lK-igDG4nxy5se42HHg459lN0aAMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b42b0015.mp4?token=gu-01ayOGfbSaCVV6xuoYHPGPieNVVKNBUtYYfG3CjoVyPDetCmJLzdUxPa_Jq-PnRV6T6ZhkKKB5fEGjggM296FtpCMMe7OSPzL49RUAJvN9RHvjLFpcyeQMpBgkTSsi5H0hxY5Y6CwQYlnkspBlwMZr_jZraenzwDWg3pWt7PO2sOo4F9Hi_hUrlpsnfRvVX8BYYYXYc1yYMXuJwlv50gDD7fh7A-bYoetjpFa5-e8Bw5gRorDR5ZFtcKZ2dW-R0MDbbRmfU-6Use_kssgaXbh0EC4ZVd5YxYqXh-yy6_8z9YUDNKlTNV-lK-igDG4nxy5se42HHg459lN0aAMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید، جنوب تشنه خون شماست
رجز سعید حدادیان از خوزستان: اون دست هایی که نرسیده به تابوت رهبری می خواهد بخورد در صورت سرباز آمریکایی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672912" target="_blank">📅 13:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHAVq2pPey-rYltT0QtcYhIfYeD0ws5w6P-1ONe10iv1F3zxZe_FPQA-kdS1-CpFMLPr3FzeL1v0jUcpFrxgLFptEuE6RoOVP1dsvUlq_xN9Sb0LTTr1CohxC63YuHuvWCnPAOZshOt8jXLb-FNkejiQqBuYzTScVwQ6UAf7uxA7a1zCZ6KqeTkZ_os5KJBysMnMEoKYtLJ_g7_DydWeIGJxcqVAPIyjWLCvO0MRIu0zqFfIye8iun-YsCgvZk9hU_mdxXuRp27RStbwBXi4yKhUv-bRhNEXI9Gzx9RuWD8qqGox0csjnH_wCO_-3EpMbDp-9X_kiYnBKM6Jg1NDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnzjzkkELShU0zWUXd3wqVpkIPTK1qEOWTa4cnuwI_Roq4vsz9qeK8TYU03gdKEgvC7G8mUuVm_johNVQd3YE6uEmPCoM9cXZpsYROeS52WM0cVHJCF314q-Z-z8XFF5k9m3tPNadTYrXt1HgOqd3GDto4OEfvNC244cArtjd6mEanQehldLPu7H3THEWmfrkOYbMlRXUEnvTVbD3sXzjagGcc73FR8Fj-Pze4QQRGWl6S6SYZAiIWrBgZr-rhUVUOZy7RVfYR8uMWEzHkatQh3wXBHw16xRL1CgIwvyjZTPLLaMT6sCnDpi568YWor_a-D8_ylIF1ONF8BoZhT6Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اقدام عجیب مارک Dior که با واکنش ۱۵ هزار کامنتی رو به رو شد؛ وقتی پوشش مردان قدیمی مد روز می‌شود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672910" target="_blank">📅 13:26 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
