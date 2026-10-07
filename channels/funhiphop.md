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
<img src="https://cdn4.telesco.pe/file/ur0iFb9FdUVLIqgztRjn6j5I5rKXgIlPryWKdml-VxE-9bmfza6QWIBPDdEjUjkpbxCmgxiRa9RxcYuwjy6zGAGMUmUvgWIw5kA91ZHebYArLOWUOlPVvfua2E8xopyXrBBB-vVeIC0FvnzeQQMDTfipAKCMrIRVi6NMG7R1cEb0X8rI3mMibFsQGn1IoQj_ojNJZwm5QHI7GhcpnjtMLNGKulszzq29qwBrS6tYYbOVSbbeJHz1FuOaDyIFQLshMLRubfPe--KU_mWLX7SpFRDr9rjL4fTbHRQY5jaCy5R7cqQdDLuE8xoVSbVSxhXyOS0sJpWbUP_frKtNC-gMow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 264K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCWMbEdmvYh9m6JYRS3eQEP3vWufSzZHQuI9uNUkp-3c4z7cfSvedV-ufPjy-U3Tzm7Xrzva5KROHOzB7k24eAhUHpEY8YbYH4aNshFtVf7CJDa7ESs20LqBRr4slT5l-6fvouTa1yoxdUhet57FY7WCVIzu73LiVxxPIHVKD58J1jmIeVTZP4XD4wY5Y14mYp7IKJLr-8_e5emJ1HoliAFIXFwqKh-KMTs5AL2rgTUP1HjxL5WoFtRaAO2Jc3a18YAI4_lajSFIZU59zRFQ8pDCFnESPu0QJJ0kHHCtV3q9DYzHZM9YIsVfUdlNrwNuIPops3ooD5KasbUjkUW9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJGlPgCbBv5o5sLwhGU7db4oxMo0P72-7PcgR7xM6z8-Q81LDlVjJW4_ES8U-ZjyPZcm5kwgIlLP31K4rgsjiAYoUAimep_eaMaTJo2HnFSYDzArjDQ7b1PRkw5HUQLPE-jtD6Ih1lUAJoRUAqfrqilCZAEqcDYyY7PlC8ufTosgTcQw1J_JQFxFOytazZkhiNkNJTyYBrsXrehFYmyOVz_q92CzV8Z-jyKMx_FrDW7fc5KFpqMjLmxqoaf8Ibgfr4S2E0X0tDIJP_FsqfjqxH1jk4x0S2LDXz_Xprj1MPD385eEM3Pbl2tlaLOs3HnwmhV4_gi0CEBKFdfsFHErKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=beywME4Rnxil96E5lWNxWSHAWKbAaZD3xPFYqmmRIHjuFX3wkORwEQowV-K-ZyyQ3yoo77P_nMSp3HOpCfO1ZkRuWKBrpg3xQgWcy4V2mS4zHMjsPfAPmIx6ZufVzHTdTnaCjDc3RTU82xiS8ynry03_F9GAcHQjkD36NbfcZocUvMhgVjp1rQnmR4ic2I9jnu9NkvLOabRO9Pzml9V-gZHuNlx0faIH5Wd9Jv1shAXj8nN-mYllgVT8qdiGYkqiD2wtMVRE_oe9ZJTYgNMyUa6TFUZMsbKn6Emcn20GGUKYSIPlmTJ8DCZQT6AKHMHtWlDIPAzG454VegIgT0snhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=beywME4Rnxil96E5lWNxWSHAWKbAaZD3xPFYqmmRIHjuFX3wkORwEQowV-K-ZyyQ3yoo77P_nMSp3HOpCfO1ZkRuWKBrpg3xQgWcy4V2mS4zHMjsPfAPmIx6ZufVzHTdTnaCjDc3RTU82xiS8ynry03_F9GAcHQjkD36NbfcZocUvMhgVjp1rQnmR4ic2I9jnu9NkvLOabRO9Pzml9V-gZHuNlx0faIH5Wd9Jv1shAXj8nN-mYllgVT8qdiGYkqiD2wtMVRE_oe9ZJTYgNMyUa6TFUZMsbKn6Emcn20GGUKYSIPlmTJ8DCZQT6AKHMHtWlDIPAzG454VegIgT0snhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=FYGmTWwBgZWJWBpv_KeXmpE_ApDAQgO1KhrbVm9CKIDfSliP0ZCu3Jki1c4PaYcfQDDmXbr4skicnpNGXmNveDA2WwmsRniR7uv8NsMan3Pi7iZNYsMMfuhRHWYoBFyLLK3g2sH9_wdWgw_KaQNlhUfYe94WRVCEzJ16KWhkPouvkaVSIOUFlcg0DrZZ7icOKJvi_qA_PFpIh-LStAb1kiZPlR6Dgnf2QHSOqN47VpcaCqFqyGbHSj9AOvjrWnjPPOXaHm3s8kU9JQznPVTaztoE2F-uk-N3GOXnVaaOD0pNF8HgIoaG5hNle6HM3vDho-3oGO-o02BGopxWZ4IYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=FYGmTWwBgZWJWBpv_KeXmpE_ApDAQgO1KhrbVm9CKIDfSliP0ZCu3Jki1c4PaYcfQDDmXbr4skicnpNGXmNveDA2WwmsRniR7uv8NsMan3Pi7iZNYsMMfuhRHWYoBFyLLK3g2sH9_wdWgw_KaQNlhUfYe94WRVCEzJ16KWhkPouvkaVSIOUFlcg0DrZZ7icOKJvi_qA_PFpIh-LStAb1kiZPlR6Dgnf2QHSOqN47VpcaCqFqyGbHSj9AOvjrWnjPPOXaHm3s8kU9JQznPVTaztoE2F-uk-N3GOXnVaaOD0pNF8HgIoaG5hNle6HM3vDho-3oGO-o02BGopxWZ4IYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.  + احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84570" target="_blank">📅 22:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phD2cYXff7rgn0D99W3iYSdU-QMA8Qp-NGg34wLe8i3JV1B3VZDdiqxl870ytlAoWrS8kCRysV738MCMhuLOpIIu5ps2X4SXn0itD7_7lwgGj9mnrmAmwtqc30t5U4PtzPgm7YF-nsSnUGSpFGQFYDgPvEJSLUf1HJxxE9r0uXjWMvAXLHmCWckjtYMkRhsObuLhsoN67lyfKJzEcFkjN4HiGb8gDEu9f0aJ3xAMyE8WjFFXuWMir1WeJwGGR0d6B6DlL239LArYLJFvZHvl-WrrU88bidSSFcFAZu-Yhv6ZhJ8XMhoCd1Uv_8hd1sRbuosBpkJdyr324z63P-Zxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.
+ احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل فیلم
@Shombol</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84569" target="_blank">📅 22:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQG-4dYKa3q0Ruah7nH829UGoB-wp_O99_Hv6LI5_9-USG6YOY8S_cGLvV0fopHAR7UPY4Yv_5ghEUNp17LN8pDlHJesjQ0QkiK-Fni_XgDnQb0IAdFBKO-URHehBMeQzpaZ72T36Hk5HHBCkHyhGZIgkCrwmG_hCkqPN-DNSs4zrzlqt-JqjMKBigMpccfvOyixVeO8skAR6aJasnK_8JM5SwUHBwthA6aregJVhrpLoYIJmwhT9V5PL4e0Hw3sT8Q_RFDTJae-Nhf8OMGcN8aCjNS1blccReYHv2z3Fms2be0G6vsJzM8LqGPCBPzWONe0YjFciwJ4IFQKnQLUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aie73gN64MO8-Rkj3Jsy_-QjPE_YUb6PU-ucTZJWact45-LFz4fRoOslgU9kaWXNu5uFTB4CV1iD0Eg1uTZyMajJjjwyn6izlaov3gU8cbuz7uB47osL7bHbammF15kxfZkmDh_eOuPOstuqCNn39nwc5vN929HizTdr5EIEi81zASJxzAA8m5PiIXnGzcuVHXteW0RRGLDXlCdsDe8JFBCnLg3GhLLCoUXGSAkZTBaR2BXHe2GRI1FaJ43_OHc-qEEsmomIUNLMEKBPMoCZ5turD1hWaLLqgQtAkTp6db7eFsodsQ7Yp6hhp6-xZ-2MycFc7eVRj5Jd_WbdZW7SzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJh6gZQeKPikS25xTnj9MNoRX0HWfxQ1OpAntzFSCQ_qDp0FdVHUPkN_fZmp0X5bzmsmamk-b64YFVPHC6JEEnM6EYdMN6T_MPbkEQwUT2v-2Lv2r7ToGRB_58hw1mSq6ai-cHZjpScxFrkGe7Ve5OC5wxz9HS-Vy5Fof11BF7f_Psi2Fok6JLRgGaqiwHlL-BSd6CNv1ko2zVM5HUBARY4Yt2Dv-bNW9JXcFFcwOBQ6DumZNTxacgN-LY8jYd3m0PEymVxNyLtbEoTqBEiIjw0eGJPwN45jQhG-KyyvHqKDiC_6nsXrKk6cQDMCb4-dXF8wabRWtWn4YUB6aaG20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MFWmIEmqiV6bzbLr_pdbbvST-3dylcEmlMv408SrBTczDJ3RyK9PLnuqOnyK_GhfFWsEu_3GBcQ4fV8dq3fY_oKUPw3l00A9qbC6GyWVldKQ1bgqBXCwvVyTy_aeSkzr-neFjamJNjDQd_fuB8GxMpcMfO39AuQ0YUtdQyNw-XCPxS17YKhbMojkG6qtgBiSp2jIscyiC2-F0Mw_YG5P3Cng3glwvXJTtgpiyX1sEMCMk4TrY0kXMns9juZEiC5kUuElmmtkmOWGO4EVDkLCywk3H2qXoC51Ufcg6hjlihcfvr28fkdi0tS5sWQ176MjuaBUPjfrJF-rpgVCO8d6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MFWmIEmqiV6bzbLr_pdbbvST-3dylcEmlMv408SrBTczDJ3RyK9PLnuqOnyK_GhfFWsEu_3GBcQ4fV8dq3fY_oKUPw3l00A9qbC6GyWVldKQ1bgqBXCwvVyTy_aeSkzr-neFjamJNjDQd_fuB8GxMpcMfO39AuQ0YUtdQyNw-XCPxS17YKhbMojkG6qtgBiSp2jIscyiC2-F0Mw_YG5P3Cng3glwvXJTtgpiyX1sEMCMk4TrY0kXMns9juZEiC5kUuElmmtkmOWGO4EVDkLCywk3H2qXoC51Ufcg6hjlihcfvr28fkdi0tS5sWQ176MjuaBUPjfrJF-rpgVCO8d6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63SIZMnxLmAdnISagrsDKpupPU5ATmTEAax7cGgYOs1b7-JJ0UOznH-GZenKxbPznlnaXCkunT-vU84hJJPbOXpVd8ai_oCQq0wsh0s6zorG_TEuog5rXyATAdX7iIeqYOMwmzXXm7ibVERL8Cs2m0L9r6rETKddShL9odXarYs4ADHekmra4kJL8rms36z1aYZPWXRzVNHqMIFmqGl1ql_Ni2MvLrJ_qiPf-BASamiuxl3N9G63dg6cKJOYrVoCcTYzbtruTgNGAAUioQTADQY3ndqLAA7TIHOtzgKfousddmhuxYJkLqN3DmyogU37Vuy5mo4R8bHQ5VsTNj_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKHT0nFanJ1rb_E_2EjHdQbBIE19W1qHDkpzRsX_Pk2LeTbMi_toe0gCYcXshRCHM7GGXMWG5u93omQYFykEbWWOV_crfcl7AdgG7iwAdYwjVDXUrzSyTf0tL5KxWTibJ8l8CbZjtBQB1RNy1rhDj_sj1M2gETv3NV5maVO1Da30CKbRTPSWldlv_e36VvX5Ij-5OeZeyyr6kBDA26vqkcz7xOhHDgnufeDuSU7OrZAB7h_2QBqST2fW42X-jJsWTm7QtdaI7pDiLx0wGznXaDikFbMGOugOgNp_YhCPQHYQSzg6BReEWAwNDKxrEduD5ti4oTA_irre0szB0Odswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=sKuVDAQGcgHCyw_8CKFBZ4foUiTuYEwEETt6f8zqfhU4Io60VETjz3rzGgglooDr73hijkyaMaCOeJhhpWujSsTBfJBVWMw3ZxT12JQ7_yHvF8LQZrPO34AQSZeUJb-eR3b13UirixpkUnTNGyvatYHxxK11CELi0EyPihfdPFlajWkYJ0aF7V-SjzVF-776MmIHkyEZpyRn79yO2NQcgKXgFCpnnhYQBbbVbNQeFikwv8leV9XsdPOmu0Pe8a27VhFKWSNaiYQhuzypWdB8zCP9k9BORuIpc_xaDqZkDMJZ0YgVk0mQ2_ydCVt_THTtVcf0Xzs45Alenj6_YJLAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=sKuVDAQGcgHCyw_8CKFBZ4foUiTuYEwEETt6f8zqfhU4Io60VETjz3rzGgglooDr73hijkyaMaCOeJhhpWujSsTBfJBVWMw3ZxT12JQ7_yHvF8LQZrPO34AQSZeUJb-eR3b13UirixpkUnTNGyvatYHxxK11CELi0EyPihfdPFlajWkYJ0aF7V-SjzVF-776MmIHkyEZpyRn79yO2NQcgKXgFCpnnhYQBbbVbNQeFikwv8leV9XsdPOmu0Pe8a27VhFKWSNaiYQhuzypWdB8zCP9k9BORuIpc_xaDqZkDMJZ0YgVk0mQ2_ydCVt_THTtVcf0Xzs45Alenj6_YJLAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84555" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cH_15zAzFExJYBpzv7GJT_mvfgeEFB8YqTHKb8B-zIXlkKHpkeqkOBSKAQxVRbdOsaKgk-2XOFJhbINpkHIvQb5NX3QMxPmpAmALc2YdMFAh21U5ur53HobyvQT7vZR6p9vNB3ju09brDDzMeBdFAUBzfuKPel_xgKpQsjRnWxVQQGet8gxAw-Lw70tAavj44bCA-XuL9w0a1S2aiC3YBYvZX_o-REZMuhJqWUNEs9UzsRKXLMF5id8KAdeEdbmMMDtB9DLee6GvrP_0n1CckSRAZR1-SPkEvlLuzPDXKI2LI-ENSWVjV9NeDY00HXULgSKIpdQ-mOMauD8BwDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G15
🅰
🛒
ورود به سایت
👇
✅
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84554" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4fVkXDUn770a4HSRuIrzbKiKChIF8PK7aWnSVusZgMKdV_sKonpRwq_ztIeEr-MKS4jqbvl6yqg-IgbyYG0_UZvwKXRpgX5Rym-xepr7UPvEvN7BVaqosqa0mEXgvva3SiM2qG2ZTUnVVEpywNUuj_eEwipjATCXGQoc_aW9qQhpi5_PO9IwJp2zLOS4p3Ip8Oy1Z6PvcYvHguFIYs8oaS28PD6tnr56AJ56SvoP_Pnxgu9A-27EqppBq9Db3PUTWBUWq0fSx88RWaK4yBvnsa58-mpm-04Cf41uJuVcsxo9FeAfDXCs-7i0S3JSl9pyrPvuUeLHIx1X3h3J2FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHcJ9CPvBgLHSyonItt3Ad1FoRY-alI-PlmwQndkoqN4OAbBoJvXN57nMRVEyOvYdot3TAScJaOUDdAXbXWC7n39uvOD0lh27N1Ki4WaKRDj6Xwu53rCOhz4doTbfLE8BlO_d8lt7VEcmTKE93WcpFdNajWq33TFzmaVqQYynmoBB0Xw48wbcGvs_nuUlf0p6InhzCxcyiEaH2ZCLBF_I7rlIVMcqq4NJvD089kM6-oF3l0tBdAtxtDkN94kbRfu4QIt8GpkQfClgoNtsfe_i0XTeK-URhRQs_QadT9iKrXuQ4aIZxp5eZiGz3ePGHJ4314JVKxEaTINEFBmLc9AkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T226oGAFfyiF7k9X0zESDo3jW8awmHNchMXra1oYCEWT_aXJim5BARc1Xwh8eVC6NGgUL0yDKl1YnrUsqTxqR9tYoPdhSBmXVLQgbHEyx1qCZKD3jkfklJdmpd8gysXVt2aRtfDnXWlCL40RSqJcTM9XmWiylLQizPPAJ9w0RZPIqvyr69pY_vYlw1HLWVoC33rZ9C1qc0x8u45CM3E5x-kMyEVXRx88ZdZeQg_aOYVHLsmRJ2KlPLbMmpORECr9NhLua3sW9pZUnxGaiKyRFeXNpkypYcm_-aUnFnTyczE4jPDT2QuMtOEn-pQoqHDIS-5fHdY-G9uO53kN1sSORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=fIKVzwvMB3hmHsyBnc6oXqETdFhHi6ZxXS-vJVYfwPz8jTpiUi4-m61zbV_h_VV93ElBwRp-g0-vdQm5VU-B5yhktBeT_7p_P-yu1zKqssqpupPo_GCv9nPjLJTJ2iFaZ9dwGGIvj5fC5FMaACv4OhM_mMeTQxRshwCStIZ62d0JHQUA8c_D8_GXJxiHQirC_o4kdvb6MubLFw9JbFYQWzc2gBN9Jeh3KAxlU6wNG3je5HoLbGrkXbEjqevnU5RAErZF42CJuAbnoMPVeTNf3H-1o2zLiCrrBPlSLkaXTcV9PM4Mi-4cgbFCkaLg3vfGxyD48rF94NhDfpP1fkEzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=fIKVzwvMB3hmHsyBnc6oXqETdFhHi6ZxXS-vJVYfwPz8jTpiUi4-m61zbV_h_VV93ElBwRp-g0-vdQm5VU-B5yhktBeT_7p_P-yu1zKqssqpupPo_GCv9nPjLJTJ2iFaZ9dwGGIvj5fC5FMaACv4OhM_mMeTQxRshwCStIZ62d0JHQUA8c_D8_GXJxiHQirC_o4kdvb6MubLFw9JbFYQWzc2gBN9Jeh3KAxlU6wNG3je5HoLbGrkXbEjqevnU5RAErZF42CJuAbnoMPVeTNf3H-1o2zLiCrrBPlSLkaXTcV9PM4Mi-4cgbFCkaLg3vfGxyD48rF94NhDfpP1fkEzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Y8YB6IoyXy9DSQSDxBbyswWBWK7p9dZAwSzxcQJmmgvMjKuNXcWcns8nJCYi-y2brt6OIPeag-lTMKwjEaQhTHadQ5nVLeOWL8h6X2kh5p9UICuUlQEqfWBAC9ZoLiPnyTsbp9OK8EbL1WvoW_9W7RIwNY_A31IClJCdAii8ijbYe4b0ilkd9vHuPW4b5a5hX_GNnOpsaCz90w4oJB6o2lvX-Hb3rR0gy399R49gLLEnfuhAMEg31-zqE5c9z0Wxje1Cli31cMFXGjU-yN_g_clHJ1Hgv66p-HckuFwt4WJ5GeqA614t8ljuFvSS3_qjSvZi0VDY5U09PXx73wgDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=Y8YB6IoyXy9DSQSDxBbyswWBWK7p9dZAwSzxcQJmmgvMjKuNXcWcns8nJCYi-y2brt6OIPeag-lTMKwjEaQhTHadQ5nVLeOWL8h6X2kh5p9UICuUlQEqfWBAC9ZoLiPnyTsbp9OK8EbL1WvoW_9W7RIwNY_A31IClJCdAii8ijbYe4b0ilkd9vHuPW4b5a5hX_GNnOpsaCz90w4oJB6o2lvX-Hb3rR0gy399R49gLLEnfuhAMEg31-zqE5c9z0Wxje1Cli31cMFXGjU-yN_g_clHJ1Hgv66p-HckuFwt4WJ5GeqA614t8ljuFvSS3_qjSvZi0VDY5U09PXx73wgDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiRYRrrU7vDOKxWu05T-DSzkxAR6G9bwNqhr9POqyLRgMVlb5TzOsukxiyNE9qqXGHbjxAKCJPle_PLi_KuSyNcQEepb_j9GixGhAtD1WDSAdt_qrZqOVN2Wje7w0OphFr6qT9oM3Euvc8rqfHIiC7-QYjgPwJParzEV1-UPpeXJ4atcp64z0Xpn-tSqPVKwUIMG_ntCFTEeaDdsnQDsgGMVY8GablAUrdY3JoXhRsxwXNGZi_MxnEfXzEDsdlfVQJhR4UDluP7ugiMYBQBBfigV8a_kBuAIrSXXrpz9HBoHzwi7-zu6fbRbPowUNASLCbY-mwVzLiSnj4EzqTi5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=ht0bScNTHclTppT4xwrGIEabYa43rjHI9AjoNZDx8j7FqV9T_uoIowUDS5svGTYvU62PtaHwA9g7BuIDnIYQatZtJkwHsiA9ErZr9l_7bc3f69-pdJOuHnTZ5TZD8oHbX2Otct_OKRxO0pteQX13CWDd8fI0MDE-7iwAfEEK3_HaseYCJUD2kibRJQvmfuzc7Bu_aDlRYoi-pUUBybm4F1QCkt7uQJs65L_8tQdL0MhSzkr0B7fgW9NYorWaYn0wdFQ3pTxnZaCn0V-AyRKl2ZuLJOlF7rOdBJDejVP38VkOGomF_V1C8nORlSdzA74FUyj4B8POZkWi7llvqkQlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=ht0bScNTHclTppT4xwrGIEabYa43rjHI9AjoNZDx8j7FqV9T_uoIowUDS5svGTYvU62PtaHwA9g7BuIDnIYQatZtJkwHsiA9ErZr9l_7bc3f69-pdJOuHnTZ5TZD8oHbX2Otct_OKRxO0pteQX13CWDd8fI0MDE-7iwAfEEK3_HaseYCJUD2kibRJQvmfuzc7Bu_aDlRYoi-pUUBybm4F1QCkt7uQJs65L_8tQdL0MhSzkr0B7fgW9NYorWaYn0wdFQ3pTxnZaCn0V-AyRKl2ZuLJOlF7rOdBJDejVP38VkOGomF_V1C8nORlSdzA74FUyj4B8POZkWi7llvqkQlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvAko_f_DlmfeagDW3XDz74VyX6qK4Cjy1NTDyXl9-HI_NCAXusCTmpCwdxH1ktsUSrBmTGuSm-vvKcsfjFb3Klo8xmW6-QpXexVJR2QdYpnNI3Y10WAyLVsOcQleA3JrJ_xJT0jrtzuPAC8RogiKTc8TkF1sNwCiVpW-VkZIFn6XPpigKyItAFGukXkvTAi-9tmjWLagaalxgtiN6BEj1GruiBVaq16Zu_-_1XxXbMVOpYZxCfTDMylg2ftdTVzqj3gYpCnNrXaiZtDUlHkAeaYLzmXTo70Y72oekleCqI1x2Y7OBNbqJFuK_Y-Fl-OcyLvzMK4fbGlb7Rc4q5tUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84542" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAwV3_GBrujaSBzt81uVE4UpWg3HEgI--mYuFAZkyGJ0WjqFJIlV3sjEqZWIsoLDnj0Tl0uTLaqmh0gGJjahiTKTIiBSS0nZbTLXRx9DDxnCeAzGUPWfKlnb146BfcpYQECW5WHKiPvuXd-0Kqx4G_E5Rjsw7iymYxE807BR1dcPfDSmOcx5oLEoSNB9wGAuz-c7LJ1oXFXHu-rU6Fm0D5Uk0buYLWycNBYkomgS-DcU8ltmiuiYkTKTRMfAORT0J5IfDhbjhQZMSmD5T95YbCkpm7sx0pkA4soWpCLqC1IyWhiUo8fSnh6TR5sp3jvT-o97zPvUfDAhPRQQMvbbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آرژانتین  - بنین
🌎
ساعت ۲:۳۰
⚽️
کلمبیا  - پرو
🌎
ساعت ۳:۱۵
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r15
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84541" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq1KF2O2Nz2B353j0N4q8p0XFfLQbeQurfBue9es0PYOrPguTFUuaJ1QUuDEjdKM4Lokb1KwWuuZVfSl6xKprm2KUDYiq_hohA2yiAWA8AyDMQSm7mV69ouZ3FK1UBYlyFJmY5-awaV5gku7Rg-h61HPx8yyEbRP8efXjV5fSf1ObGlxq_oJ45B05laLUq5gCQL9ww1k2isEtt4dsQjpWIwskFwZ5cvej4ZKMUgS0g09kBEoQrlDKoQDecZMBtgcad1GIcMaoOE3aknOld3Eh56eSQq0WzN4jBR0te6PIPH_9AlmM_aVbAmV5-gXQRvv_7qLkxKBwghSZ-jdiVSzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmAusNHwDf-JZraifWBLVaa1MDr0s1DOyg7toQ2ACsl2wTLz6_inYjTE0RJqmEXxaIv2PJYEYhG5F-ZoPaGKOYvANbhH8Ptnauy9NPS_afBa25eNSrQw6aXUqNRU17FFkGCfGnh1jduN6FtEzPPEBDGZ2QIz6eH1SZtnDB_0WmxqRPTX83WbHgKXxHUB1bG2ny8KBlevHuFV5rfZJjEjXLdWamJ3SqvF7pgyjTji7Aja7jyhdAkKktmPQlFbtSAKZ5iQlPqzv5nBPqDMKnZWtvF_ZfWFUP7Cv25VsVZov6WWXXWAdymmx0ILLj8L41XAQmvTQCBu9YMTfBnX0_5Upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=MAA1ShIXpRQkSNyDKx4R02LMCFS-5imsUlOAqJ5GQhn3V2WzmHTyuEBFmx_XVf8klrN9khz5S5rMBXc0Wyi_8BAxyu1p6hvMlbUeAFdYbaLiodcH4Okxg8uqEbo9v1BXz6itkC-w0Z5VV8qYjO_AASsLIs8PzqHMEMHfUPkXAnMJW7UlzY5-78a-4h06svGPs7MdL7HSjsDmmtH07HZV_xXquqAHhARf67vmLbSgGzb8KCU5xF7q8PK9mMRjghOChJzy6uHTANALpbxijVBN-l27YtcmcEBRRfhNNyGTbSUEicbUlnUl_MLJR68OKe7iOVMool0ymJnHXVCvaDE_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=MAA1ShIXpRQkSNyDKx4R02LMCFS-5imsUlOAqJ5GQhn3V2WzmHTyuEBFmx_XVf8klrN9khz5S5rMBXc0Wyi_8BAxyu1p6hvMlbUeAFdYbaLiodcH4Okxg8uqEbo9v1BXz6itkC-w0Z5VV8qYjO_AASsLIs8PzqHMEMHfUPkXAnMJW7UlzY5-78a-4h06svGPs7MdL7HSjsDmmtH07HZV_xXquqAHhARf67vmLbSgGzb8KCU5xF7q8PK9mMRjghOChJzy6uHTANALpbxijVBN-l27YtcmcEBRRfhNNyGTbSUEicbUlnUl_MLJR68OKe7iOVMool0ymJnHXVCvaDE_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msb9yg5irxbuppXkElMM32cwd_SwW7KVoCEmyak9fImCS8RROrQnOkTHrHHSHcxRH7gGWvT68KyVBIs2oXDOyxtb5u5CJvo8sA08Fk8FGoBJ09zg30qJRg8B9U3WMoINdPElXFebTvvSeZGtuFyDCfBFlZq85du3axx-NDNOA43boWrht1sQm_ZObBvaEI9ITWAXHYDKJNhVQ6sFTahnu7BctXgiYUlrQ3ffExv3R5RG4wEISAelM4CfdHboeSqujbQhz0oZKiH_LSwc842fcZBIcIPOg086eDb5Y5oteA7v1BATg2feqgt_5vRiZsbD9PpJLBaW0s1nBau9_4ay0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONfD5aN9u7I9r_o_GhOgvOH8NcRVxNNGlZTb8VnCgvq-_GJ7Dykfab6zWvITlUtLbCFkEoNUlr0a7Am1nAWvukAkkbHJUjcSHo-0f8tfiDe6y7tMioAFEhm07mcoAk__JRpS_HngTYdFtrXTPrS9X3dhnRv3rufqQFTxAjop-gJNXa5KaxiXoKNe73dMJf6gLwliKowlkbr9Ldu1dt8gnOixd8ViWj_o5busggisyc1HUDZh-Cn5k-MMvAqdj-9x52LsJTiFbvypOXSRwx66mvbimGSt6-ip4bhRroxi6RM8mFe7L0UXqb8T49OPz2gv4yg2AfyyI2j8rsVPemOM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUoCuc0orFzzmkW6pAunWvkiHpURuHLkMd_dZ4IoR4XcIUrPtURdN-R2xP_1wiBvSdCtMglZVCaECxlWf-tZ9R5jIBboBv645-rZe4NIWWXKo-x1jngkpBDR7vr9M5j_fHVe4kPCV-Zy1eWXdZ9kPxgJl28uSZxfAYpX_VMlJ3kYBtagMOpI-snEiXKMUAgWHU0iiypbWoxiIjrLXSiMx31cw8TK4zDx6wzJgN4WJuLgG2VVB4_IAwweNUiI1Yq4hnvie2mC7AeT5YsjMFx7G0eZwnMeRQ4uFggCOZDxR0amJ9DyrUJyufqATuDWs9FfvihHJqplTOLkETTswM8anQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9mj-EaGoXN6P7BuInaeCBaTvtjYVn3K6cn7Uwx1ndEIPY9XG6sSMZ5zfIlWFrrgWCNbiOLBIo-GciwmTebTSgJboq2pkyH_ysLcMXk3jpy3TJ8o5oqfNCavyVgPIQ65wvF7pwdDaC3pfdlc2emcLZpi0qBuN6RvUm9ZVacrcYWSefwCndwHO5Ra8EMj-eAjrQ2SQZ-ahod1Qwss3b8QPYnXoO2C15nWE3cPjkl00rbyj2iB25IU0akJDEJfsotJ3bpiOk9YOed3yD1Ts_w28aGlNk7G_3r3bFTqqAtouVmgikzsEcBanGH-UH-lzIOfQk8C8wsMGOFym52uvrmgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN6oWJknDS3xqU3rLuJVtgyuOdFxJXRABJ7MmuRraLL3Qyw2kYGBDBBalQvfvD_tPNc4DQFSa9tW04EZ3HYoreD4KoHqTGPTtZ5LyJz1jtzRQEa35JOuplpkSabR0aLODQn3rubhcsEutxmqK8uadYb00UYI5HC2iNhGk4MaznLdeLKX06t3F-l_2t8jQj-KBSSCtW7kUf64N06simz9GVIu_7CeKqi1J78nXif2CGeRhGjsPRXv2AzkXG9Nm2FFA6675PdRASoGyFE2Dwbni3x8t1gwPmFLOvG2V7cpfCissnqCAIDweHPof-Has0TT6Ma6ZNUPoz5G9jQQ04mang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns6JKiPKSWurqiGUViO0jVFnqoD7zccIxsddjYGfliirSLBe-P-_AcZOux-SAMR-RYv_pMz4b1sd_Xe8qMOf3mv_RL_rf7-NgNG4Q-apAwC1_Kj_kkuCQJOV19l3T4i_lxdMfDH12vPmVGvOOA8EwKZMvXNMZXB0X06NpWVabksmQUlfh_5tDv1PX_8N48eAF9t6LFLS3RCtSGkpGxGXPdEE0RnFNFYF_PCZXtSc-l_2Q9L2GQBfa2l_pKGQ6t-RKt8P_g1gAsC7QNvfAYbnTgMEEWbO_ABK_egDU57PA8yHws_G6vauA0fpH-hg7g8nKWYsSswfI3ZDHQ7-W1LJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jen1nFMKrWNG6F97Hg1rYQRNbPoP4hKM88HqI-BXZp7QywJwcDUBsMBoFoBAVD1UfXTo5AYY2kOrNtzj3sLAINT_bDMFsR3zm5WDsidEAQ_GzH0Y_vedW6hVMEAoYUYN6KhyH-rc418u-eJExgh88CFGi6v6IGs9CP8_dzSCIm1p1otfLojNhBbkO5lB5A81UvVseslOirhZ6lKW09ND_wrU_bFDJ_ZZ2gLyzifMLMjFrOSu33sq3T3NemKUhiSfVTrU3Ln1Q9SIK9L7w11jKCeTbYedDTfqLpZRg-gifQKTqAYG2dQLuK1YP4var-dZKxwLJJkWTx6aDIm07LWDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKRI0Dc-b9X4rWL6oLQg1KTUHJznvnfV4pR8hN5PF0bdjbr2Hmv-j3dfkG0ZpkWMISuG0gYN0S9Uu9Y2WvIkd_n1bdONR03WjKHsYEvKevhVlBFCkHgF-Pe0JGp9v6aIjhFW5rnS1znzDC3EcH9_-wJprapl0Xq87xR0s8oPmxNsohEs7Li5_Q_dpS8zh3KrhXy36APKz_YeAB_Tqg3WdS7Kkh7d-fPQsdeJ7qLenZdWHqRCNoN6hZmqo6JeeMWCZeiAiVEcHuoICJwVk4OrCctvBiLI8M5EJzUbg3IU9VfYwpAE_o3k5h6cn4o427p0W1LelUWPbkWuW01Ktf0Hvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی انقد پول فیلترشکن کند دادی؟
🤨
سرویس مولتی سرور با بیش از ۵ کشور مختلف و آیپی ثابت
👌
💎
سرویس های پر طرفدار :
💫
1 کاربره 1 ماهه با حجم نامحدود : 148T
💫
10  گیگابایت 1 ماهه : 45T
◽️
-همراه با تست رایگان
🫰
جهت دریافت تست رایگان و سفارش :
👨‍💻
@storkvpnsupport
🌐
Channel:
@StorkVpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84515" target="_blank">📅 21:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOUof7yPTHHSxpGIYtyZSavDqJOKsvhpyvOp_vF2JpcCOl8cj59TIKuj6sUlhLe0yyNzPj6wr9xUVEuuI8KdoPcwMCaqD_YAErfNuf9vyJNCc1d7bfiswV2L3tXTxxBrWweZE7urQq1X9GUBm-EAXi4O7Pq9GbuE8-EiK7FjGqqemoytS9rA0V8IGyn_1eRx6-SMUgdmgZKzyl2hb_wP2QyTp5ggGADKYtwJl2etT0qM15N8Hq-Urnb3LnniKE0nnAL6iBqdgWPRJUdFyHY9OooJgz-9FHcZURvtzYOLPTvnR4aicGRyZU_CoXHHMhQgURWMy_VOcZc1T-7-UM32kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNmLjoCgt7bwlHukAHgbFxvLN3AHycmSC8qp9NduG41Rtk3DGaVoCtpDiHdfyt_eNCyYNQWDcv-sKH8U-hJywM0JsiYNTkmM4vgVxAfkeGJR7FuD_EdrA4rhvyKp-MpBSRQ8WUpsGU4EgoKac5YwqwuQ2hz7dxJ0mu5lVUYYvZ4LG4UxJYXmiKBuLq61U_-qYaalkZTf54HuEE3ibgZt4lZQFVs-mth5Uiey4rYb95NsiUD5mzgMXmn16qYT5qv2HIQ_gsXmNUMRVSdRvu5wR74cXhTtX8xng1hdJNlXTQsnld-iYczHPS9aav78e8wBFEvaFO53EyB3nY3RTg-LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=fVUhQx6Wu0ckp4uQ4Epux6Sgbois-a1hsmxSm32DkZibfuPx0oeO39f8C1D9DBUE_7DVvZclZA-XG_3ZrHwIz7uYk2vE7zDePGjv9UZP0Tk6OlQR8k4xAHKVVNb4oPH19pCuB5v3aVGqQ0R2zm-ldy_6v4gq4GwMd4-L6cV2xOu7a78aKC98lXdwR-od6BzD2cdcdVFkA64w5tZTg5mwFoVd4fxZVim3EdY2CxyJqDeb94Px6Vl_NVP9UCZS8BGZJeRRZO4a60fpKUy0lfnHpI9Nd3IVK4kWqmT46Xrf5yLSvGhpb2IWBdXio_OkAvzds2r6qlhvYIxZU8oWBHNIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=fVUhQx6Wu0ckp4uQ4Epux6Sgbois-a1hsmxSm32DkZibfuPx0oeO39f8C1D9DBUE_7DVvZclZA-XG_3ZrHwIz7uYk2vE7zDePGjv9UZP0Tk6OlQR8k4xAHKVVNb4oPH19pCuB5v3aVGqQ0R2zm-ldy_6v4gq4GwMd4-L6cV2xOu7a78aKC98lXdwR-od6BzD2cdcdVFkA64w5tZTg5mwFoVd4fxZVim3EdY2CxyJqDeb94Px6Vl_NVP9UCZS8BGZJeRRZO4a60fpKUy0lfnHpI9Nd3IVK4kWqmT46Xrf5yLSvGhpb2IWBdXio_OkAvzds2r6qlhvYIxZU8oWBHNIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=cxLHC1tR6p6xOdW4W4-Ju7PRpJ2QlS76aiwR60CANgwM0dx6J8c9ZsnzncU16lW5VqOEbUWWq0LdA1tdNnZlP7b9zWGm8sx10M0Hl2YuzLNeLU8hAA0UMOS2W93YhMJWv83j1PENOX_IL-gRHwgcvaMhPf4FoSp7G53RswmQPZtp2usSiD30KeJR5WmSk4eaMceU5hGgbVTc26KeX2h2AtaVrPmYXeXEX-PVQR80mE3v9V9pv7AEczUuT2_yKZ635u66lQ-mUjUQ3wn6Is8Yc23n2ZCbF4MKzHNrXwQy-8NwtLpZd_SoaglHMDhSksDbYvCKdo0zw7Oy7yqjn0lk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=cxLHC1tR6p6xOdW4W4-Ju7PRpJ2QlS76aiwR60CANgwM0dx6J8c9ZsnzncU16lW5VqOEbUWWq0LdA1tdNnZlP7b9zWGm8sx10M0Hl2YuzLNeLU8hAA0UMOS2W93YhMJWv83j1PENOX_IL-gRHwgcvaMhPf4FoSp7G53RswmQPZtp2usSiD30KeJR5WmSk4eaMceU5hGgbVTc26KeX2h2AtaVrPmYXeXEX-PVQR80mE3v9V9pv7AEczUuT2_yKZ635u66lQ-mUjUQ3wn6Is8Yc23n2ZCbF4MKzHNrXwQy-8NwtLpZd_SoaglHMDhSksDbYvCKdo0zw7Oy7yqjn0lk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=RJR--FsnxItkflCV37YNCtF3KE986ITHTUBkfbwfnPYKRIdh5zdLnsPwS87sxAjxCu3e1TGco1VzuTMseOQ33yPnpQpd8IO-OkGdkYwFyJbh_QF9rZJBB4rkjYJppmm1K5o0fznSsaRXZK8Kxxr7RyinzOTb6GBN8sILwzFxy2aFrzwH1VI59yGo-u12SZ2G10IuKM5iC6aj2miybBkVaunJCkuZaBPDAFVQBWEtDw8rcm-K-AgjB7dhGfzlZXn8IHrRMoU6Y_FzQO8pA9-8LZoFpw5Ivs-o-nu4Dp6DBsMI5lctWzR2ZVxVwT1krR6FzF4hCf9mrPFdwCJ111da4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=RJR--FsnxItkflCV37YNCtF3KE986ITHTUBkfbwfnPYKRIdh5zdLnsPwS87sxAjxCu3e1TGco1VzuTMseOQ33yPnpQpd8IO-OkGdkYwFyJbh_QF9rZJBB4rkjYJppmm1K5o0fznSsaRXZK8Kxxr7RyinzOTb6GBN8sILwzFxy2aFrzwH1VI59yGo-u12SZ2G10IuKM5iC6aj2miybBkVaunJCkuZaBPDAFVQBWEtDw8rcm-K-AgjB7dhGfzlZXn8IHrRMoU6Y_FzQO8pA9-8LZoFpw5Ivs-o-nu4Dp6DBsMI5lctWzR2ZVxVwT1krR6FzF4hCf9mrPFdwCJ111da4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=T7ITokC7GM920RzpzE6B24XxpDuGkCayyiYejW-x6hTsgoyoP3ngjP7IJ1qdsa2hqoKYKEH4HePx-sLQKCoGtxnF7jMo4Z8yo1GoXC98xmCEv46huJbd1aIhDvoxnM2LNfZxYomA8F9Ojn7KX4lPDArOF6h2qnCqCxncuX778Mr1CNaiUPUYbB_Vc2AZPm5wiOzw5hkhtF7ATTYsEUEOBalsRUzxOg_Oewsy9loF1_iidMYrodBtQJEqIZF9EpN5AiOlicRlxTRFfTCPazBjWWnjGJjOxWYnvtCuI2J4e8ZTxegLOqs4TrXxoEABptv1quZgix6Jfw4vLWnkv36B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=T7ITokC7GM920RzpzE6B24XxpDuGkCayyiYejW-x6hTsgoyoP3ngjP7IJ1qdsa2hqoKYKEH4HePx-sLQKCoGtxnF7jMo4Z8yo1GoXC98xmCEv46huJbd1aIhDvoxnM2LNfZxYomA8F9Ojn7KX4lPDArOF6h2qnCqCxncuX778Mr1CNaiUPUYbB_Vc2AZPm5wiOzw5hkhtF7ATTYsEUEOBalsRUzxOg_Oewsy9loF1_iidMYrodBtQJEqIZF9EpN5AiOlicRlxTRFfTCPazBjWWnjGJjOxWYnvtCuI2J4e8ZTxegLOqs4TrXxoEABptv1quZgix6Jfw4vLWnkv36B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJzYDVY7V2-J3D6sGg4c1R0oMsBAF6PSpLNhL-DXBlrICJJGhCKl96D6yakJJtFvboOVVOFSsgF83mSR3KJTVvgHeEzuJ96_PjpQ5mIdKbOX_b8NqjJT5fxRDVk_xrHkmfl08e96Kg7-H-vgG5O7jdv1a3kg3-L0bHB5kgEsIATyrzQuylRNcmK_IcV38emY19vWCmk8qTsLFeWTlUoBrciR6lhguCE_58xb8n60sqBEkSb9HkrQPq1AoFSZZTWjdkpSLHNVbZ3E9Tq1DzM6laLsWiXkh3x2J5xunY1zxef4Nt58ioR3hK8J8FwcI_hovnJ-DSGqD52Eq4_HVEjk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا نامزدش چطوری دلش اومد دل این بچه رو بشکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84499" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=hvkDVzs8BBtHq2Gn_qKUDEuTCOLe6KOiQVl5dPefYCU_wUiVUgyByTnVSt7QCbruzndw_136XIEw6yk2ypT3fwZ4L5_xSiU_JGwTJRQtpbH6843zCzT92iJxgroSGGm7KXyh7FRXQu9zuv8OiygBG1wAF8EimOEWG8-cnowOCouByX8Qb3sDXskV4vAlBkDTT2t7EQPe0o58ruO4kM9Nk68mS6wMm55aCfVl8PVE6cfBKeMC74TEVcQAzmoFVbubI6aVy9nJW6PLUQiMK5QkNpRYvJ4jqbakcwIbY-Oi0s7q0lvJodqEiFgfe95VNyIINxd10dHEUWazjwk7L2-h6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=hvkDVzs8BBtHq2Gn_qKUDEuTCOLe6KOiQVl5dPefYCU_wUiVUgyByTnVSt7QCbruzndw_136XIEw6yk2ypT3fwZ4L5_xSiU_JGwTJRQtpbH6843zCzT92iJxgroSGGm7KXyh7FRXQu9zuv8OiygBG1wAF8EimOEWG8-cnowOCouByX8Qb3sDXskV4vAlBkDTT2t7EQPe0o58ruO4kM9Nk68mS6wMm55aCfVl8PVE6cfBKeMC74TEVcQAzmoFVbubI6aVy9nJW6PLUQiMK5QkNpRYvJ4jqbakcwIbY-Oi0s7q0lvJodqEiFgfe95VNyIINxd10dHEUWazjwk7L2-h6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g14
🅰
📎
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84497" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جوک برتر قرن
احضار سفیر فرانسه به وزارت خارجه ایران
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84496" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84495" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیدین گفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84494" target="_blank">📅 17:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZAOCHcBRmOOS8gbFcCi5liUJ-LS5efHH5qsxSSGddVTxQbNFrdycV3DZgyhKGgE51QEIXiscbXnCb8YtK7RYlK2CuuZ4id8WpKtKgKQlOkxonWHXpTfWqewrUBkwbaekOHBJ8f_EMOTQ_ytTKTSmIGVoA_yNGGWYUR8kIMYzwg-iOqPNA__bmR5hvXtcEQsaLhJ4IxDjKLwQvqc1Rqq0lSsIA1BX-335xaeqRwq1SPtDIe-4TIGqVVOu-J0OenZwC2roTbBTx5aIicoFTao8KlISjVcr1TzwAkMbyah9mIC8OAO48hTL3IZ7-3oazlw3NJ23N8DFyTFVymNVqWGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGiXOZ6EL2UunnUcRN4BnBkbuhnm1_z1H_thpe4t0aO-zn30OuMwU4MzZUak0HWXA0fls5h-kbGzGoS2R7cn0HSoYxp9tXvLHl-5_wS_LpVp63mZIzXTC36dylwUySNQEAKISf_VyozTN1bArRUdeBflUeDdNMO_h1v47tuaZEsrMut5pbdqiMVspF8vp0Gl83JnyaUlLzyXkmSTX5CSzvuJxtcQlB7_BMn6kBpRnhcwanZmr1vGgXWTY0jFsfJhE8cWfS_rNZ7WbvolTHaGmS-MdEfCiza6KhGvQAIQoaXfODxpMYYkzYjK0vNfwuvBrBqpb3_iwx7JvlsPBptPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwUhfm0nbUb6R57ZCBOPhw0sODYkDN1YWW14L56Rt1X17BAhk6CAK_6i6XiYFnwruhdZKmKjotiLB8qk36569RudrIJiS3qGnoa5uoUKveS-GuzVm_6OumJ1r_9lpxP6gmI6lR2YDX6CTZdy_p1Q2ImDb-CNUcd8JDJBEAiSsmwMjBvqvBdsUen62BytPImiZ20nvAaUqu_lBRvu8oZnYC6kWOJcF8OeJC_XaOxGYYdOrA7iNU8lfel1OGC-K5N-kFdxe_hYMux0zJOZOnkBdDao51q9HxsdVXazWdDsOkt1J4y3DtE8PelP9irIWZUb0e8b02TXpg4BGFuMX_6LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هرچقدرم از خطرناک بودن طاعون تو اینستا کصشر تفت بدید من یکی این سری ماسک نمیزنم، کیرم تو این دنیاتون</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84488" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2951b20357.mp4?token=gOJmWFFMjcZU4Yt3DCPdrCre1XC9CzvinMEa6awEamgCmBOp9pZbZVXAVM_-3U5-exn46Hx1GIuZgKApTXbkCjXDGXERNJ-LEuTdJhilX4MRREOMaXWk8kixotHiv1UAQq7mQiBKonbGW37t_ZRywpL2gkcoyAB_H6s_jmPuUPyUSdoFHjPCuCSP-ppBZXZhpsx9Qca75qFgtMIXhxJuERxX7WXj38tr7l9bPMrW0F7nZZr9SWWm--AsrJRBTSNrYG28VcAFaZGFRnPsk-0FIKwKSeK9bkpUuRysDjI03NIqDRM44qI7KOgQ2yLGpGuYm4NLpbpSFi5nePGJZQIoDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2951b20357.mp4?token=gOJmWFFMjcZU4Yt3DCPdrCre1XC9CzvinMEa6awEamgCmBOp9pZbZVXAVM_-3U5-exn46Hx1GIuZgKApTXbkCjXDGXERNJ-LEuTdJhilX4MRREOMaXWk8kixotHiv1UAQq7mQiBKonbGW37t_ZRywpL2gkcoyAB_H6s_jmPuUPyUSdoFHjPCuCSP-ppBZXZhpsx9Qca75qFgtMIXhxJuERxX7WXj38tr7l9bPMrW0F7nZZr9SWWm--AsrJRBTSNrYG28VcAFaZGFRnPsk-0FIKwKSeK9bkpUuRysDjI03NIqDRM44qI7KOgQ2yLGpGuYm4NLpbpSFi5nePGJZQIoDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو بخدا من نبودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84487" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84486" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWL-HL8ND7DqgpiiLo685vAhVeUHjIZgg9XFs2khUB7fxmAyJCj4atRnknFjyEIUADaBNxuMzoRqYSH48MrYOdOAnKo6YXG7LyCk59neNGzsPpAEjpwX95PtVMaNhR9GtS88yUk6ETKP2YpzWSpoZDD_z9LTszj98AmP4KgRmSX1P5RZCzynd_5TsQWc2DiqC8mk3tsXzos1eZ8A-xlw6dCP40xFNDH9st7mj5hF6BUaJmHiAkABQgacGaTIAjOdrSEUiZG7sWkcPssaUi7Q_8g3ps3lYs9BClAE1iLXKfqe0uT6482mbIr6s86c3jXV4w0Df3KsQJ41cvWc3JrgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
کرواسی - اسپانیا
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - سوئیس
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R14
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84485" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwWgEVjfEn9JCnHrAg4sS4Ptz0ecQFOI-34leI2loeH3LxnWAEo49S6MyaTg6UFTaghVlTrA2xhVQ4JGaYTP1kSApjtKybBt4UOwmllwhebI7wtQIFuXOd356Us49EdIyCaMy67RTrlDWYeDrTKP3DpK6eLqn0dVXJWDYv2alS7afPGPwvKy8c-Cq1ya8ycWZmuuYM-Nmv4Yodts0n8Cd1K15PPG4BhG7hE8pGgo4TPVTpvnQeHwSevStzV3yHlqzNCJ3whTo_BT4WqITPzHatkcbLB0mYMsVE7ZTMMneQmIkQO2CU3m-NvmbHWy1L91ZUz8HD-ak-HDsKmvdzyKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmz5qlItkioNBAbaHMH8A1pzJ-gl2-KdL94TLJifjtUTB3Q3pMlrChaYOwPdgl0haO-bGUvfHh-_k023PCDMMyqe1ZCG0z5UgeMTN4g6Q-PG6gbLy4nvJNXOqvzp8L3f7_FLAMLTiOfGiAsLqiuL6LYdJPa-D2g10VecJarNa1N5Y_z0rasFYFqYJa6-grD2KqXojL0pIpfTmmux1ToDYTsemzR0pDPji7LDqhmCTPOQ8-0JKtmBZDsqdEYcvDg1K2_YkYh_4_R2RW-sM8ls03M7-IvQ2axVG-hL-T_JALuO521mCiCgfLkIeXz8QD9hxU8DSezzg8XseNrsZ7Ox5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOqO-vHVhE6h7Uu82w6eE7O7MZb8tmYQy_QEoDUFndO1gBpXHQ3rlbx9gVuKHOw0QappWu62Yhbcy_yX4mB7GfdLjjcq81MepvFA7T2vmhIt6RTswlMsfH8xhT4yQzoM-SGGkvxwy3gW07XMwi7nyrv-eyGVzdpSpavNueqIisH91XNR_atKAbHKTG6XIUYdVnm33J5gk49saDMmYdOzgsOYS2vucCJNU_TtjWHJ7mWMxGJhfgD0EYRcFz4RcokinfC7x8CPaM1m8cxcnqdl-zR1UobtJiB2-tLFL0Q-TEXqRKAU2AKhnfDice7nb5LkjtB4bwTuexlvtXRmJr5GFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGoH9nw-4FAowQ-6dzYHyWeJbIbIDqJoIwO99AeDEcBbIszdR9LWHo7_-0OxgDSTyUF28qs768cPMDiamW2aXdQQUey7sEEZixWSxQrhAZsvZ39P-00U0iES18FF2jyT8Zv0LFLQxsrdDbs8h3IFHExWPwiy6RSjNqO4VnQxD5_biHnDcrhpTqMTq3HDcZoSfzXjcJpbMMOeHYd_cYzgBWBPsq53jrWG04k79y4Rux3dnVLmQIM7_vWdyW493T1LMdeHfzE-uGmyJgV9oABlJvXB3N-itrSWzmLtrpyVfT55_BVv0IepsmHjnIEZEFwRVfpbxmRLNtmIOEGh8oT6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b249c59827.mp4?token=vzTzSm2QPiqqq-t9DM6Ky6NLspuX0LTUZE4Dz0cvgXD_tuc0TtaiiVzS4A03h3LBqO4BI8D4kPUkiBmIUmnBJVpALimZJ6V-hIompvSzWaPA6-UFx5nPmxGT57f-GsavUdBLZhmtSp7gEOTMe4kEQo9uuZnU-GThB28blsgLh3KYDjRphR-Rb2pg4fIlIcylf1vTKWqZ3sDRivbr4hdhd5dZlyOQoXsmvUNkkHtl72_eHmpyQnAzxZLCfusXFUbGdKeXFEwIikSOza-m4TTSFBHKsSSrgFVB1yXqFtu54Ey-Y7mXQ-XTsTSVZ2L9z69sQJGAXys0ncjItbQ9-zb0CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b249c59827.mp4?token=vzTzSm2QPiqqq-t9DM6Ky6NLspuX0LTUZE4Dz0cvgXD_tuc0TtaiiVzS4A03h3LBqO4BI8D4kPUkiBmIUmnBJVpALimZJ6V-hIompvSzWaPA6-UFx5nPmxGT57f-GsavUdBLZhmtSp7gEOTMe4kEQo9uuZnU-GThB28blsgLh3KYDjRphR-Rb2pg4fIlIcylf1vTKWqZ3sDRivbr4hdhd5dZlyOQoXsmvUNkkHtl72_eHmpyQnAzxZLCfusXFUbGdKeXFEwIikSOza-m4TTSFBHKsSSrgFVB1yXqFtu54Ey-Y7mXQ-XTsTSVZ2L9z69sQJGAXys0ncjItbQ9-zb0CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84471" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این لوکاکو چرا نمیمیره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84470" target="_blank">📅 22:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=LcEI8H2FCluCViF0Vh_EdMMDYU3htk7nNJKMxEWxS4WNVQrPe2cdAwQNVbiJi9jsaVZQN-KMGUdD6iHAEkJBzJKVW4RRLsdYHEdkg0rQGmBlRo5vOuDj4wg6Mfad9GGhusaPoCxKr15BrQwJFBnVCJNAVQcOWY4py9TcvbAKNY7e_LY3y-3fFk2J843tbHh6-Vl3vCiMNFZA39tFGIC1loZqJtSn0aREj82noUiZC-oqtQHryfyjg-UIeFUUXqcNC-hC5bqYKgsedFq3DnnrsF1PFF4A89PMgr4xhGOKNe9BMmHTp9xUFKPYgwOU4119Rs__HUqPg0hDNw6XpyRMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=LcEI8H2FCluCViF0Vh_EdMMDYU3htk7nNJKMxEWxS4WNVQrPe2cdAwQNVbiJi9jsaVZQN-KMGUdD6iHAEkJBzJKVW4RRLsdYHEdkg0rQGmBlRo5vOuDj4wg6Mfad9GGhusaPoCxKr15BrQwJFBnVCJNAVQcOWY4py9TcvbAKNY7e_LY3y-3fFk2J843tbHh6-Vl3vCiMNFZA39tFGIC1loZqJtSn0aREj82noUiZC-oqtQHryfyjg-UIeFUUXqcNC-hC5bqYKgsedFq3DnnrsF1PFF4A89PMgr4xhGOKNe9BMmHTp9xUFKPYgwOU4119Rs__HUqPg0hDNw6XpyRMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84469" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خیلی دوس دارم بدونم اینایی که از رپ دنبال محتوا ان تو باشگاه چی گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84468" target="_blank">📅 21:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">منو برگردونین به اونزمان که تنها دغدغمون این بود که حصین زد یا فدایی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84467" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">LCPV</div>
  <div class="tg-doc-extra">Creator (ft sahar)</div>
</div>
<a href="https://t.me/funhiphop/84466" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84466" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzfDEbWAuNL0csQTrYz6qtcp7PXFyrf68IrKRydw0bsrxAa4Cwb1mgoxGobXalnM6qG7wBv_Lr0V1_l8kuHVZCmfJNC5K2WCY3KFCcRgvJA1FyzaI6Tvskdpekq0bKS5LhRh5YsRTwVARJ-d40xpndA_ilMc9yZE0k8fXI6f0KmC-X7RAb2HEln3zXL_toMnIGzBAD96GdvkjRpdqkIR9hOoIhSFVfmolzBcxHALbgdj91oS6pA9KyXAbeaBUwZO-yzY5RwICiaAnGDrD-60ELRWKsNTwXfUua6zrp46pf5UBZ11MJGIw1V6MtwAhzUhbrDoRYCrWkfFpWMl6fGCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84465" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh7NDqWnHhjp9348kPG7rdoFqtyziQv6RHZD-eiH_2jPnf2SG1D_pVXgDEiO3cUwOc64EgaW81XuXd-fB8Z429faoBI8D1_6PU2FKfEcXvHkA3R5tVyPgXprxlTCNX6f2SRJ2oOldUa1MGeId_ypgd4ZpEKyxav8gDPpBSTr_58efmRGEPUMNeL3kPgrGGsnivt0eFQ-TjuF19Wz58V7mpQIU14LY7KyOH5epL4UJeaYOKqeoPaXX8v3V4CADWXfYkLQOgwKEVelpiLDWxNwHTLCAXdjF5kXSm7SZNgbaGNsJvwR9sBA4c2EM2GO0uO57uBEKUz7ARtQwmEZqVNWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-be1zfxJOPYcmAuS_03rnjLymcnHFmnx30Id_3BSBAl2SH4Piw8Po2IFtI3cj90QmsWE1N71W6_44PXRs9DOf47Cb3_uLpx7vzowPbN9tUTkQU040QgmPBltU2CsC9cCUPK_mTek_FRf8Z77DlipN_6l_p9tPjLwEGaJgc4FP1Zfco9-_ATAh2CTfXmMGqCvjvwMyoZ8BSBnX7ynLKhrtTO6AScZl-2xxY9Mhvs1LpEt9cYqZJk0eTzCX2ZmoHxofN2jNbSKK5wz4o7-x-ZNcgEjC2RnAeOoJ8PRN_M4XatVYhAnXi5rI3jtBJfmsYzcR6hZQV28WY87wYVcDopTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dS5VQ0RfDg6CKoH5hf98sApwI45RcMWoLGQWtkGdko7L2bz5xRgezyuaKcEqwXqk9w0_-iU6iLOlPmIdR1yX15t0O3u2tEnqmWWgJ8mWD7NhZqyHKMfCNb1Fir24kQt-36C5uNwkcPdnufQ3Abziws2RiztNnaFyZtbwDyN5FDhVnUM5mP2Iw9nn57RubU5MJM8LxTWiz73PdlkQyYL4OHlc3S9ne5umRZ85iZFhxe2XqZb_KWIsPg_-bqdFlovCs795VRTkGKkS0EHogppf0RCPEVz_D1z44RSEuC4DKoMlWVhc4mYhSlsXCl-vcQOEdDpXDuxlRF_n5fNqeNGnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHJEb6wz1A-Nw0xoHoXQo5b7U8WMY42QyeMTiq9_EjRjzrMY8a5RhKUtfstlSuHmhlW8gUu8b0qh2fjYf7uwnnMvbi6nB8QqCc3eEww2a7uioEeiQiIxy3KaSGMTcW1T6mpZBiagANVJ_LFmuSE8VssB3cclMJoJmSGtf7KBnriau9uylW0qx8umsYH5tHu5oEIeTVE7FERsdjomCIIn3i39m-WZntoSnJdiEhacwkTe5yl3vGnhhTArR8202a8ZUqHanSPXVgjqRvB4KOHu5FJwalcV8TejCqtP3TV7aP08iBifbnYVKlkQs5aa33N0xmWjhb7gIqnsPDHKuE3_Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلیشه برعکس و اینجور پستا تو اینستا زیاد شده و دخترا با این ترند حال میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84461" target="_blank">📅 20:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دکتر مسعود پزشکیان:
تاکنون، آمریکایی‌ها سه بار پس از مذاکرات به ما حمله کرده‌اند و این نشان می‌دهد که آنها به دنبال گفتگو نیستند؛ بلکه هدفشان سرنگونی نظام جمهوری اسلامی ایران است.
حمله آمریکا به ایران، که با هدف سرنگونی نظام صورت گرفته، فقط باعث اتحاد بیشتر در میان مردم شده است و ان‌شاءالله، این ماییم که از این دوره سر بلند بیرون خواهیم آمد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84460" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
