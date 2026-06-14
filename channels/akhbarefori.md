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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.54M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-659456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBLU3WbjI8gCAHRT9KQC6Go4X26zttfOknb0eKdpfAWiQgtZWJ3Z-5kv7nWtjC-nJmbmoe7chV8AVSEHj1-jFZzpuRrPBxVUKbws70Uw3HX_SIy3PBdBsnFbU2npsJ6s15m97ttIV_Z2bk3JcEgskmk9psLXsHV6omKUlNKHd9maVfkCEojsN4KrfBfL2Pd34Hj9S_Ph85hwrL5NUk2IXmzNIMAvNc13UqQQa0jWSXkV18GjbXbMMfuY14JABVt29o7iMWqGL_1KNQP78ZZiq6oTmFCnZZkgZLj-j-i-fZcxj78UhGGbzbNyrKh8W5SiZ3LYV9WhrbUVbKgXTHSyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffGifxHmSLMz3L1fuLGoUGJh8gIlhGLeV7XeyNBLB0Vntyd4kAya5GRCYHnj7BgeKZ7YZkc5Uek3sR8GFJkJZivk9j76-sPcFzv2Ecw2eECPbEg7EDsuiCJNangrLr6XtM_pKZNX2ZWCqHSuBim85_SC4aIKaEHWqcgWUGuJirZ6JG9qPpJXftfzx5XB4JWEuju2ozooAceQV_iODuU82oPgxt2MPlTqPrEkioagl8Pi0G7b9sIQ7XXCEQTziRYWxsmJCkp9ni2JxjaLqBh9a-SP_YhUeFlfCAqDBcz5n97cu0cNrGq2vQfaUtcf14LPykGMVfF3jintqqirjgi9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC5mMRMZl38SA7QWLLa0NPtrETgiYjUpp3ZE6HfAcHGLbPOONYmRBGOa4vAgBBvcEi_vtJLkWxsbWz-s30yHhXSu64orgtNLjpIYbfSuKQ6RlVYMIQoAbr73RoOU7luT2lmQPVXhw2L-J2v7KwHB7T8oXS1L4_QjYybFi1SbP8HRfTyPG0qoI_YjQcrt4AKKkEZdxSK19cO0N9ul7bMzEeFHwwARL2E23Fsanoz8dOvPA-4VcayBBxgBodANtU9CcP7Oue9tq5MfWdFanQuZ4hWRxAkF36l65hyq__O1RBltPdEhIGng-rIgPoOOHTSaZ1k5EedBQo5aoQyilkE5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joMrkQjcplX40CFrWoKph4WVAqKNsmNS_Neg8W5RhGHN1J4YqTp7E8RxQ_0Wpq9NotvYov350_BSUQ82BaH1tCnx8ttaCd2jtDWREb7CBcGjrkCaSaJvTg7iWbJ-Jd4V5efmhqUR883uxeaQ3MLw5tAQjUF2ckVRyf0kPtOdxmWlinrqEWqkHbTqgL63WoKUbrGQ1WZBp4P8uewacDsg3LgHDdLJYMjsolLNrO7O2Yt7Yhxl8WfOBz7ugwpr-F0PH6Odafs1KkaLd1vC3uSRCYA4SJa7SHRhuFtRwYeWotsgIv_0JJT_d2pAdPTZXwruNroxzvysnL7UqZiAbYv55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAA5fVOo61ZNxPcIRtMBQfszab-E2Y4TlUaBkas5gemjNUcAJa7WA2qJdtBtVFJIWY-SBOCyxrz8lNSaLAqhzP58gfeguz-YXOacUVtjshCPfM2dE-i1zzUg6MI_ojq1BuNimxYRtH_9b1SVYPCC6UAXZttf1uHiGDyaNqzaI94Ub3N9e7JrvLBYBnuuFBK4fkF638Oj_NA3OaeXCbaryb3399uamoFKIVgCQAglMWBvE_MxLg7l-DImNljEBssOHdLR5Mg0j2AcZSIWWiD1ex0XQkXGWGVDcOosCh38Fro_q_0-tbgwalCuEeuesTMCc-ohR2_yYOqT14UJJOVjog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا نفت هنوز ۲۰۰ دلاری نشد؟
🔹
با وجود اختلال در کشتیرانی تنگه هرمز و گذشت بیش از ۱۰۰ روز از آغاز جنگ، قیمت نفت زیر ۱۰۰ دلار در هر بشکه باقی ماند.
🔹
این در حالی است که در روزهای ابتدایی بحران، برخی تحلیلگران از نفت ۱۵۰ تا ۲۰۰ دلاری صحبت می‌کردند.  پس چه چیزی مانع انفجار قیمت‌ نفت شد؟
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/659456" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz2hgawWGBF1P7lFKvDTuK7JLrLmCDCR9szd6lnqUnvjJTH-EIAPnQtsjqYPoah3UNApBSGRv05sNzMnkStbyo4VcKener0NXQeDNmTAGhD2Qdc1-Dix86Lqepegj6Oi47H6Syy1hadVDyFcRcygpp2l-QacZ-NmuiXoL46WphapwOl5aqmW9kNxkg1bSL1T37W22g6XYYYFAKO1gErrNgZLN4uwvs-f_wyysaEkb3x5fiuVzzTcK5om5bR7g1_OR6UNbzEgrThkQrjDPqJHyJ7zgt6Yx-s8WSDHI9nBdUqYJ3MO4E7zMFv6m_B161r_Sw-ml0bVQmREGRrfd83KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/659455" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشور:
🔹
درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔹
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/659454" target="_blank">📅 22:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
🔹
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659453" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImKZdOikNP9Pn69UECaQo-A2AnSqjZE_Zena2zkml7eMtuHF4riFoCp80RtthSEsQnNSSVrBOQIVGPdJSGncW9CO5DrverqDTSVCCy1Tk8VwxrU6f0vx5zc87ciIkICDbJIRztU_0L_1yJizn_11_kQzFUeSoRr1W3mqsMDw-gGiQGriDGYm1UXMAoqWFIVwS8CUhJkwrfB2boWQpzlm8-kLHxOOglMNlUXhX3QNkTJQCDP9LDFzB57cb7rczODByd-TVRmC2DRz85Q0gbZqYstk7UTpRlN1C6cgD7AfLk-1Okt_cm7c9GmdJ5S3oykoJoHN-g1VSvCTE3FFT9DTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم رونمایی از اولین لابراتور سیار خلاقیت و ساخت | Fab Kids (فب‌لب کودک) به همت سازمان فناوری های نوین و نوآوری شهری شهرداری تهران
فب‌لب کودک یکی از مدل‌های تخصصی‌تر و نوآورانه خانه خلاقیت است که با استفاده از آزمایشگاه های سیار و تجهیزات فناورانه مجهز شده است و در فب کودک برای تقویت خلاقیت، حل مسئله و مهارت‌های علمی و عملی کودکان راه اندازی شده است
📅
دوشنبه ۲۵ خرداد
🕙
ساعت ۱۰ صبح
📍
شهرری، میدان صفائیه، خیابان شهید طبایی، مدرسه وحید کیهانی</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659452" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد در ریودوژانیرو برزیل و جان باختن خواننده معروف
🔹
بر اساس گزارش‌های منتشرشده، اولیور تری، خواننده و ترانه‌سرای آمریکایی، در پی برخورد دو بالگرد در جنوب‌غربی ریودوژانیرو جان باخت. همچنین در این حادثه ۵ نفر دیگر جان باختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659451" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل هفتم آلمان به کوراسائو توسط هاورتز ۸۹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659450" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: شورای عالی امنیت ملی با قاطعیت مصوب کرده مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659449" target="_blank">📅 22:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtlW2lyRaZKYoLfS69GFmb0txjWbuPI7Zedq7AVeml1JZqsgC6HE5sGq8QIgrbpUs24zG4lRjs7MyPjpEL0irJCJ_Ek8Uk73EwBs6B7-P0Dhwjc8cwVY2zLZfrkTk48mwgPO90wdNRru6XXLEUVye0bPfm81eaj4nkjtcSPKXZHFeEkMNNa6FG1W6Hdoc21Z-UqYXm3pHXvIUVuMurt6ZtGALhg1gw-NgoCOei5DaOI5EcQRsrLUs4Bqevy-sx21sd3liEN3eQhJq5WuAI9uydL6phhMwDuaAYvT7C3u5ze8Dhla4R0YqAgOAd_YrLhKZa2MCGHqB1nQkWOyugeO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
از فرشچیان تا کیارستمی؛ مروری بر شب درخشان هنر تهران در حراج کاویان
🔹
عصرگاه جمعه ۲۲ خرداد، مجتمع ایران‌مال تهران میزبان رویدادی متفاوت در عرصه هنرهای تجسمی بود؛ جایی که حراج خصوصی «کاویان» با حضور جمعی از فعالان اقتصادی، مجموعه‌داران برجسته و علاقه‌مندان هنر برگزار شد و مجموعه‌ای از آثار شاخص هنر ایران را در معرض فروش قرار داد. آثار ارائه‌شده در این حراج که ارزشی بیش از ۳.۵ میلیون دلار داشت، طیف متنوعی از نقاشی، خوشنویسی و اقلام کلکسیونی را دربر می‌گرفت.
🔹
در این رویداد، آثار هنرمندان نامدار و تاثیرگذار هنر کلاسیک و معاصر ایران به نمایش و عرضه درآمد؛ از جمله استاد محمود فرشچیان، غلامحسین امیرخانی، حسین محجوبی و حجت شکیبا. همچنین آثاری از پیشگامان هنر مدرن و معاصر ایران همچون منصور قندریز، پروانه اعتمادی، ژازه طباطبایی، نصرالله افجه‌ای، عباس کیارستمی، کوروش شیشه‌گران و صادق تبریزی در این حراج حضور داشت.
🔹
در کنار این آثار، مجموعه‌ای از کارهای هنرمندان شاخص دیگر از جمله حسین علاقه‌مندان، منوچهر نیازی، علی شیرازی، بهرام دبیری، رها محسنی کرمانشاهی، علی رخساز، محمود زنگنه، ناصر اویسی، خلیل کویکی، مجتبی سبزه، علیرضا آقامیری، رضوان صادق‌زاده و محمدعلی ودود مورد توجه حاضرین قرار گرفت. همچنین اثری از «آدولف ویسز» که در سال ۲۰۰۵ در حراج کریستیز ارائه شده بود، از دیگر آثار ویژه این رویداد بود.
🔹
یکی از نکات قابل توجه این دوره از حراج کاویان، عرضه اقلام کلکسیونی در کنار آثار هنری بود؛ به‌گونه‌ای که علاوه بر نقاشی و خوشنویسی، دو قطعه جواهر دست‌ساز اثر ریتا نیک‌فرجام و دو قطعه شهاب‌سنگ کمیاب نیز در فهرست آثار ارائه‌شده قرار داشت که بر جذابیت این رویداد افزود و توجه مجموعه‌داران را به خود جلب کرد.
https://www.khabarfoori.com/%D8%A8%D8%AE%D8%B4-%D9%81%D8%B1%D9%87%D9%86%DA%AF%DB%8C-69/3223046-%D8%A7%D8%B2-%D9%81%D8%B1%D8%B4%DA%86%DB%8C%D8%A7%D9%86-%D8%AA%D8%A7-%DA%A9%DB%8C%D8%A7%D8%B1%D8%B3%D8%AA%D9%85%DB%8C-%D9%85%D8%B1%D9%88%D8%B1%DB%8C-%D8%A8%D8%B1-%D8%B4%D8%A8-%D8%AF%D8%B1%D8%AE%D8%B4%D8%A7%D9%86-%D9%87%D9%86%D8%B1-%D8%AA%D9%87%D8%B1%D8%A7%D9%86-%D8%AF%D8%B1-%D8%AD%D8%B1%D8%A7%D8%AC-%DA%A9%D8%A7%D9%88%DB%8C%D8%A7%D9%86
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659448" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل ششم آلمان به کوراسائو توسط اونداو ۷۸
🔹
گراد؛ انتخاب نسلِ شیک پوش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659447" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659446" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
لغو پروازهای غرب کشور تا اطلاع ثانوی
🔹
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659445" target="_blank">📅 22:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم آلمان به کوراسائو توسط براون ۶۸
⬛️
🇨🇼
1️⃣
🏆
5️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/659444" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اعتراف کابینه اسرائیل به بن‌بست راهبردی
؛
پرونده‌های ایران و لبنان تفکیک‌ناپذیرند
🔹
وزرای کابینه امنیتی رژیم صهیونیستی در ارزیابی‌های داخلی اذعان کردند تلاش برای جدا کردن مذاکرات لبنان از پرونده ایران به بن‌بست رسیده و این راهبرد کارایی خود را از دست داده است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659443" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-6zK6JyDWONv1-VGMLG08emBhbQ9uHOl2PMQpKpJtGND1MbaQgx8rg7lFzEToriA_Qre96LXs1XF0fKQaZMioyVByidiFyyLzzbErP0xTDitukGSsLJDOG5JJgUnXDN9h7yCSkAiwzyxjim-O1frqa2amE6joAmxZbl2HZXq48UGi6rGXsqjZ0m8fs9orZPi92Sqzb8J3Pu1uJx0wlJlsjPoIRf9jIk0K6fZgL0M-xscHAmc5lexrLd8UbVCWQZtCMYTEKn-wmi6X4J9QOWkMFE-dunKsondAeWZkQWGIjmcSNiVXMuXrSmB1LeZG0I_34iCdOb_zgO0ZZBP-y0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند جرعه بنوشیم از حکمت صد و بیست و نهم نهج‌البلاغه
🔹
سوار هواپیما که می‌شوی و از زمین فاصله می‌گیری، آدم‌ها، خانه‌ها، مزرعه‌ها، شهرها کوچک و کوچک‌تر می‌شوند. آنقدر کوچک که در نگاه ما گم می‌شوند. ارتفاع، اندازه‌ها را جابجا می‌کند.
🔹
امیرالمؤمنین علی علیه‌السلام…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659442" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYv8dZy0sdQTz7gEbddXS18Ip1JMf5KlrRijctpQ3TCxozu-s0dUSlvstAfsj7ad9tW4skaZsLnHsFKU0xcQcze-YiCsjAk4ZhIer3m2D06eHlF9i8UD8nDwFWuqBF_G_RNfMChJ7mVKcwqXLIvYROCUs3cs9hOWCzI2-plcVECq_QFZVtg-WZHu_PJGuxco5Zy4G65ZsXd5MIUT45vraUFQtJViqWUAbtblAwAXpgXlQ-w1BmpiNdqknVSoa2zxLx3pyuwuElW-QDN2HDEqJPRL0DtcZeFs_5Fpps5h6q4aoENl_gFLljMJkBE_5El0PtNpCa6EbAq8uVp8bav27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آسمان منطقه و ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659441" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: ترامپ در جنگ با ایران شکست خورد/با قلدری و بمباران به هیچ جا نرسیدیم و در بهترین حالت به توافق قبلی برمیگردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659440" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659439" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
واشنگتن‌پست: قطر «توافق مخفیانه‌ای» را قبل از جنگ به ایران پیشنهاد داد
واشنگتن‌پست:
🔹
قطر پیش از شروع جنگ ایران با آمریکا و اسرائیل، یک «توافق مخفیانه» به تهران پیشنهاد کرد.
🔹
توقف تولید گاز در ازای دریافت تعهد ایران برای حمله نکردن به زیرساخت‌های انرژی قطر.
🔹
هدف این پیشنهاد، محافظت از مجتمع گازی «راس لفان» قطر در برابر حملات ایران بود.
🔹
این سایت در نهایت در ماه مارس (اسفند-فروردین) هدف حمله موشکی ایران قرار گرفت و خسارت قابل توجهی به تأسیسات وارد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659438" target="_blank">📅 21:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwJ7YdhvFsW3wJQuwdefWx3zupw8z6tFoV-4qnx_1smmQaF80jBvpj6QErEMP_QD2rmlJ2ET-U3h4ilEOh3Of6xyRota3MK0fEneH7T6lJLO3ZGtjqC-1as3k-2ElUOOZZbzvR7Ox-AA1n0sNGyO92N3aQRCX_pIFgOdSoh0rE0qEpegRYV3nm9b5wYmii_Hi9SVODvRt1i0entpyobowJeUaRkIp2c-l2yS0G7EHYbDltnbQh2oEZhoxf8bmotwohQYbVpHf6cVw2wHiPrMeJCHmMu-o7pgrIQcKBu4nQ9YPWgLzVJc9O19yOjtlb41Svl-UlYLcQsYqxU_JvPljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه خلاقانه آرزانتین برای برخورد با افرادی که نفقه نمی‌دهند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659437" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659436" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr_jkDytvVbZM63yT26K47F3GVINjWkd-QyQ6IHgbWAiAZGnN302EWP7UolCPqANvg1aS0tgmP2pviv1w2lmmigOSwFYIteWVtA2EUfDYbu-qAzSbYEBiVnk572CW4SWV1xAeIAQmEFfRNYmb0CQjO_93GF9vn4fCAsxdbcRXDdzHdawkmLZvo2qkaB6pQhTMR7IW_7FBapc2pLjY4aQMYkdLZxFM0KY8G2nTndjlrVaf-ldekDZKZ0Xknpa85jHHqTXVwwung3APPWuT_FQYDYMgyp3DLZnvI-VNOBAHfdJplOQdwqd0nBzCAFxMkugdh2H4m9jDa736igLiE8ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حتی شاید مطمئن‌ترین محافظی که داری، مامور انتقام تمام خون‌هایی باشد که ریختی
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659435" target="_blank">📅 21:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659434">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رئیس اتاق بازرگانی مشترک ایران و چین: پس از مذاکرات، صادرات و واردات از چین به بیش از دو برابر خواهد رسید
حریری:
🔹
با رفع تحریم‌ها، تجارت ایران و چین پس از چند سال می‌تواند به بیش از دو برابر برسد.
🔹
واردات از چین در ۱۰۰ روز اخیر کاهش یافته و بازگشت مبادلات دریایی به سطح قبل از جنگ چند ماه زمان می‌برد.
🔹
مهم‌ترین دستاورد مذاکرات را نیز رفع تحریم‌ها دانست./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659434" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355711d5b9.mp4?token=Fm9iWknq6H0cj4EZBb7WsQAXr6gT2B99iTendrS1MZfTyt5H0NBSUf-ubvq6QxKMjiIy0l35oEq-T3iRw1gZsmeqcEztMXm2VNVK3mpiWe_wtv4YK0evu7h5zU5hez_R4Ty-T6kz1wN7b7lFr5vecgmQau6iK9ohCiaBgrMSB5J-n9YPYrP5DRH7JHdsNzYEwMjQVpKDrhzZ5e-_TJP4IO5ZULoKHBRi-5CGBUCG_VeURbMHkwq5h9rk-D7-rmglBQr_IuHUQRK6vHbshnHHv6j2hnu8olKBRQbgUbcDOOEJmH8K4JAa3ParkAElPfolGMPHFqITMugOjl3V1SKiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355711d5b9.mp4?token=Fm9iWknq6H0cj4EZBb7WsQAXr6gT2B99iTendrS1MZfTyt5H0NBSUf-ubvq6QxKMjiIy0l35oEq-T3iRw1gZsmeqcEztMXm2VNVK3mpiWe_wtv4YK0evu7h5zU5hez_R4Ty-T6kz1wN7b7lFr5vecgmQau6iK9ohCiaBgrMSB5J-n9YPYrP5DRH7JHdsNzYEwMjQVpKDrhzZ5e-_TJP4IO5ZULoKHBRi-5CGBUCG_VeURbMHkwq5h9rk-D7-rmglBQr_IuHUQRK6vHbshnHHv6j2hnu8olKBRQbgUbcDOOEJmH8K4JAa3ParkAElPfolGMPHFqITMugOjl3V1SKiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم برای آلمان توسط موسیالا دقیقه ۴۷
⬛️
🇨🇼
1️⃣
🏆
4️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/659433" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659432">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_BktAsy_1dgZesuY_XIXDTgMjWgUDy349nFMM81-comLc30r5TI8VC6h9S50UAP-VfTr7yKNfnLbI7dp1ZMrMf7RtaTKA91UQEw6crnNYcsGoXRifV8XxLhb1gzVCEkmlyIx5Qtq0OTLpQP4_NQcJhV4-mu6-E3v8FRQWCZnqnkf4AaUm3-Gr1O3EAsPXaPKJt6BLrcEuu_5-IZ7t_dQTh6MxrPBXfEZLWqRH2dUbC_WGrCHsH3YEsG-a2UbNC41GuBh7ioIzB6IeXc6tJWhlbXKuyh5n42dUqbvMmcbxsTrQ-0-Wd2-AqGu6Q9ESKIzAeMgRzqpk39YYTcF2PySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیروزی عظیم حزب‌الله در راه است ان‌شاءالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659432" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659431">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند.
🔹
ارتش فرانسه: ناو هواپیمابر شارل دوگل در غرب آسیا می‌ماند.
🔹
دست‌کم ۱۲ نفر در سقوط هواپیما در شهر باتلر در آمریکا کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659431" target="_blank">📅 21:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659430">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سرقت ۳ میلیاردی طلا از زن سالخورده با ضرب و جرح شدید/ متهم: پول را برای خرید طلا و ازدواج می‌خواست
🔹
مرد جوانی که با حمله و ضرب‌وجرح شدید یک زن سالخورده در شرق تهران، طلاهای حدود ۳ میلیارد تومانی او را سرقت کرده بود، پس از دستگیری اعتراف کرد انگیزه‌اش تأمین هزینه خرید طلا و مخارج ازدواج با نامزدش بوده است.
🔹
قربانی پس از انتقال به بیمارستان از مرگ نجات یافت و جزئیات حادثه را شرح داد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659430" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659429">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7013e1863c.mp4?token=vw8TBLaZG_O-IdZdVI44cT7m_K8r7nrKsak-hm9T_o25WcZFeN_de0-ry7vtCVXiIw9CWSxZmujdDG5ziCNIzd6CZ2auuVwZ0naSLHx1Hr6u-MjGfv2CPOq7wNaEgzd3-nIrwktoe2CQHYImOmwQRMj2Sh73XFJ3IqsU8UKRezTo_XRupVNowiWuo2tUp3hFYg-vzCPYY3PkggQ_ep0WYkx6icgZX5cVMbnJk-Y_QYE7UcZ2ZWU3C1d6pZvj91P8hDYxre4GsWp4kd_Ofzv1VTpigP6bAoifVqBccauiJLt_6-UdPd5NdY642xhfiC1Z5c-WvikTxwsFIBzMs2U3QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7013e1863c.mp4?token=vw8TBLaZG_O-IdZdVI44cT7m_K8r7nrKsak-hm9T_o25WcZFeN_de0-ry7vtCVXiIw9CWSxZmujdDG5ziCNIzd6CZ2auuVwZ0naSLHx1Hr6u-MjGfv2CPOq7wNaEgzd3-nIrwktoe2CQHYImOmwQRMj2Sh73XFJ3IqsU8UKRezTo_XRupVNowiWuo2tUp3hFYg-vzCPYY3PkggQ_ep0WYkx6icgZX5cVMbnJk-Y_QYE7UcZ2ZWU3C1d6pZvj91P8hDYxre4GsWp4kd_Ofzv1VTpigP6bAoifVqBccauiJLt_6-UdPd5NdY642xhfiC1Z5c-WvikTxwsFIBzMs2U3QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد در ریودوژانیرو برزیل و جان باختن خواننده معروف
🔹
بر اساس گزارش‌های منتشرشده، اولیور تری، خواننده و ترانه‌سرای آمریکایی، در پی برخورد دو بالگرد در جنوب‌غربی ریودوژانیرو جان باخت. همچنین در این حادثه ۵ نفر دیگر جان باختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659429" target="_blank">📅 21:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659428">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وزیر علوم: از ۱۳ تا ۲٠ تیرماه هیچ آزمونی در کشور برگزار نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659428" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659427">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c9c5aa976.mp4?token=NtN8l67ngx_b-x2e5c1bhdFGm2mIPwUnxSgjRoIn6-Wf0RxA1OvRNIk_GE-dtDtKZBt_eXgAddbGGXvjy0XgMsVnk4RNg-RBAaB6LxpZIUZR79-yrpP_XJVrKFwZ4q5zBaW4z-O6O8y0U_7YcOfQxGbVBSKHUbrGS0-XU2brXx95m_SliFQ3Qz_8CFK6LwvDz2vO94fkEwkIPpHxfIPDdOJvp7SMoGUnrHQOFq4VzV1E6zULpZw4ETaFt-TdquS0IxJYJ2VVmoAVlX98ehjtQDIoE9aye_3MiZZhFA85pI8QN_zfaBGRwEVPY-blODTS1qfbrMGRQpU9v80Y-NsdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c9c5aa976.mp4?token=NtN8l67ngx_b-x2e5c1bhdFGm2mIPwUnxSgjRoIn6-Wf0RxA1OvRNIk_GE-dtDtKZBt_eXgAddbGGXvjy0XgMsVnk4RNg-RBAaB6LxpZIUZR79-yrpP_XJVrKFwZ4q5zBaW4z-O6O8y0U_7YcOfQxGbVBSKHUbrGS0-XU2brXx95m_SliFQ3Qz_8CFK6LwvDz2vO94fkEwkIPpHxfIPDdOJvp7SMoGUnrHQOFq4VzV1E6zULpZw4ETaFt-TdquS0IxJYJ2VVmoAVlX98ehjtQDIoE9aye_3MiZZhFA85pI8QN_zfaBGRwEVPY-blODTS1qfbrMGRQpU9v80Y-NsdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان نیمه اول|
گل سوم آلمان به کوراسائو توسط کای‌هاورتز
⬛️
🇨🇼
1️⃣
🏆
3️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659427" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659426">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22576d836.mp4?token=Ea4bTXs45ZPHS7JDdpeTQUo8aBYJk8-t_KMouFvs8sLKdheJK1PAuweDpBxHxWO8hw_kWWtigjhRN4lExvVoj1dNAcTq5z3WRTQ3l3CCEhGs6xEPxJ5iimvfLgBhd518Zdq338hoAtjlLhss_GQnIjvVTmEtdDh2gOegetOur9eTlkpbOluaYpHh3FHSH6k85L4P75uR_nXSFU9POO76w88K88SfwUS4VcfDBENIAFI6TJ2VOHquDISedTDtwG3LbK310lNz9WBkFcxcJXuQ4ygiMdBWUTmoBIEDpuGqBmIBcU5Y9ICb_nZhlBUAiw9O8mc0IUOhem2ZnxvisYxV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22576d836.mp4?token=Ea4bTXs45ZPHS7JDdpeTQUo8aBYJk8-t_KMouFvs8sLKdheJK1PAuweDpBxHxWO8hw_kWWtigjhRN4lExvVoj1dNAcTq5z3WRTQ3l3CCEhGs6xEPxJ5iimvfLgBhd518Zdq338hoAtjlLhss_GQnIjvVTmEtdDh2gOegetOur9eTlkpbOluaYpHh3FHSH6k85L4P75uR_nXSFU9POO76w88K88SfwUS4VcfDBENIAFI6TJ2VOHquDISedTDtwG3LbK310lNz9WBkFcxcJXuQ4ygiMdBWUTmoBIEDpuGqBmIBcU5Y9ICb_nZhlBUAiw9O8mc0IUOhem2ZnxvisYxV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت بزرگ تلگرام؛ پیام‌ها حرفه‌ای شدند
🔹
تلگرام در آپدیت جدید، امکان ارسال پیام‌های پیشرفته و فرمت‌دار توسط بات‌ها را فراهم کرد؛ قابلیتی که تعاملات علمی، آموزشی و خبری را حرفه‌ای‌تر می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659426" target="_blank">📅 21:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659425">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اتباع خارجی چطور می‌توانند در ایران ملک خریداری کنند
مدیرکل امور اتباع و مهاجرین خارجی استانداری خراسان رضوی:
🔹
اتباع خارجی فقط در صورت داشتن اقامت ویژه یا فعالیت اقتصادی و سرمایه‌گذاری قانونی، با دریافت مجوزهای لازم می‌توانند در ایران ملک خریداری کنند.
🔹
خرید ملک به نام شرکت‌های دارای مجوز نیز ممکن است، مشروط به اینکه سهامداران ایرانی و افغانستانی به‌صورت مشترک حضور داشته باشند.
🔹
هرگونه خرید ملک خارج از این شرایط غیرقانونی است و سند به نام تبعه خارجی ثبت نمی‌شود./ اخبارمشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659425" target="_blank">📅 21:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659424">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aeaf8fb29.mp4?token=YG7Vr239iZc7gpflEm03eqWSr7tCc_W1HU5KCaTNqwP4S-aI9wLqA9g54xrQL7j_k-l6HS4Gh4g82NFFyazkUGbZzKGBu1rvu1kzaAf5auy0d8hcTGV60qSrNRwz2s1_dvA-hqT9bYw3nIIiGy4ko-Fxv1e4sHcFqbhvmot0lfqs2vMW1_Fb_DZr5_NcQJjZFuVxf5GUkAcXM0mxWqY1n-6e7EcLeVRxr2BTAZTnOgBuxutg6RE6o3T6qox2QDUa6g9jp54xAgLaKrhQT8wxfYGtM1rkhsYNOC-hCER5jR5A3vLkCMql9ZN4A7E6jKjr9FCnYmM0ogRx49z4FMrC9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aeaf8fb29.mp4?token=YG7Vr239iZc7gpflEm03eqWSr7tCc_W1HU5KCaTNqwP4S-aI9wLqA9g54xrQL7j_k-l6HS4Gh4g82NFFyazkUGbZzKGBu1rvu1kzaAf5auy0d8hcTGV60qSrNRwz2s1_dvA-hqT9bYw3nIIiGy4ko-Fxv1e4sHcFqbhvmot0lfqs2vMW1_Fb_DZr5_NcQJjZFuVxf5GUkAcXM0mxWqY1n-6e7EcLeVRxr2BTAZTnOgBuxutg6RE6o3T6qox2QDUa6g9jp54xAgLaKrhQT8wxfYGtM1rkhsYNOC-hCER5jR5A3vLkCMql9ZN4A7E6jKjr9FCnYmM0ogRx49z4FMrC9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آلمان به کوراسائو توسط فلیکس نیکو اشلوتربک
⬛️
🇨🇼
1️⃣
🏆
2️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659424" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659423">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukp9WFF9dYHNzTLKuUPmVG1vGILStubk4DVOxI-PaqILFnvXzpKYtv9M3DpBaFXq8wdSur0RWwHklHWlXoac2La_63nGgXsLvVY8weSSNZ2Lv1CroidHBNgfw5R2u75JzrSP_XYy8Vr37HOobpS0VAK0XAmRiZ61QtxDghEEYVsiQkF4LX7j69Ktz5OzDVLVqxlOTD3N1g71ftQ2Kg7u530k9sN7hV_oMBf6e0OXRhaeQ6kfX19tbHoG6i2vWGaJtBUO51D4Sml_VKlUtu0bFYOuUbLzpvGUJTbGaC5HvDBhNgD5m4vVcY61BmSX2KXtR4o38vD-23PWMj_o08NKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ‏پاسخ رزمندگان اسلام در پیش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659423" target="_blank">📅 21:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659422">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خدمات و‌ کارت‌های‌ بانک ملی فعال شد
🔹
خدمات بانک ملی ایران پس از بروز اختلال موقت در بخشی از زیرساخت‌های مشترک شبکه بانکی، مجدداً برقرار شده و هم‌اکنون در دسترس مشتریان قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659422" target="_blank">📅 21:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659421">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای منابع الحدث: یک هیئت قطری اکنون عازم اسلام‌آباد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659421" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659420">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07526040b6.mp4?token=sia2kmzCgjJlPBr0TGupwwJ-qPcIAOlIUKeMRyrZPiJUQUsy8E5z9CKugax2Nw9-aQFFWsIbBRDRCK3jycZ6OzjyYjS-T0dcQYXfjjvvr1NaWmGwbRvjAz8HQJZhsdrtsWczQqN_VR1FJUsA9UViFVMGDUy9sH3nWT8OBRRIecn_P6Z3ZwkFbeJeqLzFLS1mt95RyMxPb9-bilGrPgUMCCP3ffhGdeR98KGiiY1e_Fqqjy3rAxPE246XQt5abgl2pDEbM1gG2o5xN00wwd5VlM4Z-cC07t8J-xImMvFp3GF9dKvSxad7FFiRfpZ1Hhloy4wPkAJf-TYw28Bb1z3_bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07526040b6.mp4?token=sia2kmzCgjJlPBr0TGupwwJ-qPcIAOlIUKeMRyrZPiJUQUsy8E5z9CKugax2Nw9-aQFFWsIbBRDRCK3jycZ6OzjyYjS-T0dcQYXfjjvvr1NaWmGwbRvjAz8HQJZhsdrtsWczQqN_VR1FJUsA9UViFVMGDUy9sH3nWT8OBRRIecn_P6Z3ZwkFbeJeqLzFLS1mt95RyMxPb9-bilGrPgUMCCP3ffhGdeR98KGiiY1e_Fqqjy3rAxPE246XQt5abgl2pDEbM1gG2o5xN00wwd5VlM4Z-cC07t8J-xImMvFp3GF9dKvSxad7FFiRfpZ1Hhloy4wPkAJf-TYw28Bb1z3_bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آگهی تکان‌دهنده‌ای که یک بحران خاموش را آشکار کرد
🔹
بیش از ۴ میلیون دانش‌آموز آفریقایی به پد بهداشتی دسترسی ندارند و در دوران قاعدگی ناچار به استفاده از روزنامه هستند؛ واقعیتی که دو روزنامه مستقل آفریقایی آن را در قالب یک آگهی به تصویر کشیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659420" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659419">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147dc7a2d4.mp4?token=BFsGRyGj7PG09lC8lvltR6wKcgDebK6ngnunwkzNkjj8pBPbUlAtK2fL0h1XlJk69yjeff75AreChIi0VcOwq4oVe9Z7-xGzDXryby6UItMMRt8RKrF0oQ0gmLvg5s6bhzOQLOAXLZFkTcjbd8UepJnF1jJhGVv8b_sYw4a5reoNGOdWiBK3yvC6vAfr74bGlfHYedtTJ5yoSten4Et-H0F8y8kCAVyDRetfdvTeaPQZzLkLHfKuqEuBE_Pu2nTcEBFy3H4D9DKeucpWb6qSdWCacRM4Zm9OC0S8Vn0NY2-lO_0vFsMiEuT2pGmiH5WlF7b821uGvebI3EDrR1mG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147dc7a2d4.mp4?token=BFsGRyGj7PG09lC8lvltR6wKcgDebK6ngnunwkzNkjj8pBPbUlAtK2fL0h1XlJk69yjeff75AreChIi0VcOwq4oVe9Z7-xGzDXryby6UItMMRt8RKrF0oQ0gmLvg5s6bhzOQLOAXLZFkTcjbd8UepJnF1jJhGVv8b_sYw4a5reoNGOdWiBK3yvC6vAfr74bGlfHYedtTJ5yoSten4Et-H0F8y8kCAVyDRetfdvTeaPQZzLkLHfKuqEuBE_Pu2nTcEBFy3H4D9DKeucpWb6qSdWCacRM4Zm9OC0S8Vn0NY2-lO_0vFsMiEuT2pGmiH5WlF7b821uGvebI3EDrR1mG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کوراسائو به آلمان توسط لیوانو کومننسیا
۲۱
🇨🇼
1️⃣
🏆
1️⃣
🇩🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659419" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659418">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i11-FA16LBu9OCDiL2xG7bajXOb84CZO77Z0sVeZAAlwHFUg4dcIYpfxYn6luxtNCJ3FTLtMc6XtlGcfUREAjbYSCcAkV0pqyAhr8oyzpZLzwixeKNlCVpY5xhESG8maX9pwPVnNlBpETLbAxdGE0j2kBhVB0wfa-vZk0K7wCNWk9JXC1YIZVNXu_Hl5oxDywQNYufSjqGELkCTIlILGHTZuq0J_BKgGSVEyUny2epYYLwJopBXZ46pJhjKIGjRZyopZEPf_rG0iHnKocELw0-2fbrgG-PLygLFiAnzr3wHnJfFW9Vy2FjjSE_PON2q4CFpGEva2_ZmNjdPS0dYdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نقره در ۱۰ سال گذشته؛ رشدی که کسی باور نمی‌کند
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659418" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzc7j3U52VtRxIoRgEpUuEEr-0F-jzI0t7aEPrjKVj0JqfmaEqN90z4sPyBRuG0jRQfJ06VawR9HgJD403gLot-vXsN3Er3_4XV4Z85oVvR9MS4SVInLlmdLM25agk050ljOYFvMEWs-VjjiiNFBkRWcrQm4x0hQBGd-iG3VstK5GA1N5P-IQGbzt6uw4Tg7Vh5UT1EZfHkaGyRc1pc-Mlk21QdUssHi9FP4CTg3pAZGBw5bUydNlXJAfvHU0UxVVTQuOL42Xxi3rpVjjvB6YRiUmeoPLC7tx8KLwLS0Dd3uIToruY7282iOQ-SMfsOhzsKmnXRbPq1H3NooFyZJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659417" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
خدمات کارتی بانک ملی تا ساعاتی دیگر وصل می‌شود  شرکت خدمات انفورماتیک:
🔹
ارائه خدمات حضوری در شعب بانک ملی از ساعتی قبل آغاز شده و خدمات کارتی این بانک نیز تا ساعاتی دیگر برقرار می‌شود. بر اساس این گزارش، تا ساعت ۱۳ امروز بیش از ۷.۶ میلیون تراکنش در بانک…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659416" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست
🔹
تیم‌ملی با پرواز چارتر از تیخوانا به لس‌آنجلس می‌رود
🔹
قلعه‌نویی و طارمی ساعت ۴ صبح در نشست خبری شرکت خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659415" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a462ceaf5.mp4?token=GmYJsBXnX9ILvPHNktQGUwqnE0RLVmevYvUrSUszDA6zpVp110hsUbRM8MBjJZQrxWyAgwPaA3RbAjEdEQSWO78TbfQotH8Uc02FBf8A0WBRTVlG5DYuSaZ8h3gpKfYvOBaqSoC50qMyd-Y1UFFt17XIfR24fp-8udnWzlhec2WCppXMGKKeC-rg_K2i1yNFlNQb7y65P3ruLQYvtzicdbey0NAh3n1uPVOiAP6P6dqYzCe9r99qUNxU8C8eC97f8Ndbnn6JQACP-ilRFoNEsExxcIWmpNWsw4bEZvnlN2-VSruU2lX3LUNr73kVgRNwiR8EPoeURdZl2a2q3EKLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a462ceaf5.mp4?token=GmYJsBXnX9ILvPHNktQGUwqnE0RLVmevYvUrSUszDA6zpVp110hsUbRM8MBjJZQrxWyAgwPaA3RbAjEdEQSWO78TbfQotH8Uc02FBf8A0WBRTVlG5DYuSaZ8h3gpKfYvOBaqSoC50qMyd-Y1UFFt17XIfR24fp-8udnWzlhec2WCppXMGKKeC-rg_K2i1yNFlNQb7y65P3ruLQYvtzicdbey0NAh3n1uPVOiAP6P6dqYzCe9r99qUNxU8C8eC97f8Ndbnn6JQACP-ilRFoNEsExxcIWmpNWsw4bEZvnlN2-VSruU2lX3LUNr73kVgRNwiR8EPoeURdZl2a2q3EKLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آلمان توسط اِنمِچا در دقیقه ۶
🔹
آلمان ۱ - ۰ کوراسائو
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659414" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th2mOTOxImwi3VxYe2mx7cgyTWFttRot0ZzsMO3y42-nTA_ng_2HU9e6ACw5SEwE9CF-H9Y6u1YDGmvIPIif_qOZDq6gfk16pH7QXJMI-baQXdK89vhj-NpK4ufyHBxDwptqWz9hjSCEwRsQRPVBRWgck0Kye_p4d7dPRigfl0l47EIDOC2X02msn0gbP-rQzJgvdwsX0f4DjOhOhBPRqJ2ms_8O8uSXxvhWzprkHyK9Vkso9eNPWId2PHlbMQds4QY9nvbL9hzhuOLKqXYdSuYLF43ycArBg6dutKamujfjpaGcpuX21XNmOem5UWBeMUBhZ8jJM2ZVOZ3e58tlvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم الانبیا: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند  سرلشکر عبداللهی:
🔹
انتقام خون امام شهید هرگز فراموش نخواهد شد.
🔹
نیروهای مسلح با توان رزمی و موشکی ارتقایافته، «دست به ماشه» آماده پاسخ به هرگونه اقدام دشمن…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659413" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjXZ178j9ADvGslZEDw-kCKwhFjAzU5dM0rmBPMW2Q1zdq-i_nvpHmLVoz_Xggd49LdWqG1g8kUsSMYOpWc8bueDAMSHmKNishjs5QG_XY_9gnSd4OWRU7ldIZ0pfyy8SPTjyQFDQsYzmeU58TTTIJL3GGY7xiEI8BHYoB5ymfMjQa0IXcNQ3q61Rn-QxJlvSIiaRE6aXj7aAhMumK06DT4zd80OzD21uVdfxXosOWDNsXpBDy0wdENTQFQ-2zLCiSO14d9I5T5bCKyqpTvwit_ZRnXHLT3bZ2u0ApmE8dgcb47-opds5cMPQgOf8XTsuZPtM4Vq82iO_ts_d6I6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659412" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e324ef00.mp4?token=D3AMmbRgO4wzGDQMm91z33354bpVwUGHDzCKk3ViddFpn_Yu4ea65LKTdn20fD_MHdzTyxeVwEl63-etM6qRiXjFODjQ5N5C3SaLaTY8SLIVQGU2e7K_plCBhSHZ78drK6E2PsEJK6uFdbDnIhSgSN6P8I1KtpLTeINScTGjca4PcHHPP9weLSS654TVGdWxt2qWXQLt5yPG_tRVYd94o0Ba5hLXyE5bNKXWKiJO96tzEJ4OfcT_gshW_LTLCyIyqBAYYK8MjB0j7qLcJJd3nd4rr5Fe5KiTKiISQu6wdg14O2jifzYpAjCoTFjbvLqyySHMXkF7AwTBuV3fq_SyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e324ef00.mp4?token=D3AMmbRgO4wzGDQMm91z33354bpVwUGHDzCKk3ViddFpn_Yu4ea65LKTdn20fD_MHdzTyxeVwEl63-etM6qRiXjFODjQ5N5C3SaLaTY8SLIVQGU2e7K_plCBhSHZ78drK6E2PsEJK6uFdbDnIhSgSN6P8I1KtpLTeINScTGjca4PcHHPP9weLSS654TVGdWxt2qWXQLt5yPG_tRVYd94o0Ba5hLXyE5bNKXWKiJO96tzEJ4OfcT_gshW_LTLCyIyqBAYYK8MjB0j7qLcJJd3nd4rr5Fe5KiTKiISQu6wdg14O2jifzYpAjCoTFjbvLqyySHMXkF7AwTBuV3fq_SyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور مکزیک به دلیل هزینه بالای بلیت، به جام جهانی ۲۰۲۶ نرفت
کلودیا شینباوم:
🔹
به دلیل قیمت بسیار بالای بلیت‌ها نتوانسته‌ام در بازی‌های جام جهانی حاضر شوم، قیمت بلیت ورزشگاه آزتکا ۱۲۰ هزار پزوس (بیش از ۵۰۵ هزار روبل) است.
🔹
من بلیتی در اختیار داشتم که آن را به دختر جوانی که عاشق فوتبال بود اما توانایی خرید بلیت را نداشت، هدیه دادم.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659411" target="_blank">📅 20:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3D2SEhezGCmopEB66RgpF4CxI1pSHgwxjAXoIBP-7IbAdKZKvoDMf4lQ7-j48w-hZO4gi9QFPDapW435D5c3AxSBQUJu7aGRTq5TEH4mxSTDvpokPhUUk3crx7FGNNJOnDlRPd3m2sXAnDHlAkX1ePgaml5YODCMqLnx455oWg6Bveao_eZlgqS29mh9dC0cteMDxXuHOBfB59Gwk1V4VgafQm-IWNcmDkLTYDHWxcuwzGW9vxhsF1MbqZcxeymJ36wZAJ-kiwBBHy8kAHcc-NQZ4KuVB2W-wmQQnMMyEtZSDXhI4klrQiw4qVmYWjoX7PGC6jOOR1naCewgVAfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TggUQTGv3gYDibXorgCTy4PHLlH_HfWKGCjTq-Zlo4zWDfj_sLEvCMnKgSpblU5Vf9qzFQxdv8Wo4Uqs3wZEGrgousIPXQJDeUvrwjm3SYS8EFvLSiKsHDcdotqEJshdmjQ910HOtWqHke_roI0zaQ5ktGjVvvna8zTU0y0cBtt8WoP1VA37eAIr0zsxEKFOEYPYS1-dxExpRsY2sV69Ap3171zs5t211mRto6UEhgpET57If9dvyplq5od4JHo650U7oVFLtprJLQgLernMW4Kf4qa6Ood0BgiWG5tr_KClFCy5G-BxQuWKT7kHDdi9QXzX-u3WKCnPkGqENkKX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV5nsSJdinSx7pwyGIQ0uj3xZt1Hi3Veb8rKhWtv-dvqBGHXztqZU9wxuLS29MGZSbFVOqsTtjLRxnOYrimf7AUTQmdGADS9hqeAdOMFLhEupc718pSJ6-MRUaO_hxsAc3842kXcXMJPjZWev6_aorY7hBQ4pN8OkfXh3_oPDtvG4yTZ3GDal1fhC-gVS5y094bRdvYb4wYqu3omjLN_8F3vz8C2QSguPCuNLwy5xkfVxG59nRk6FfY3iFJhv9G6BQsjwccM6Fo7j2vvmOWhjuwOox5LN764-5MqMNNiX6jMepsdxcwGrDg2nmX111tMIIyhoAb1ySiIQ7QpQ3IBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ry6t1iJs36DwXRdmJdiOjphhgn4c1KuN_WZULGWFxvosvS9zdRqvfJcR2acP6SeeCfFj00w5mWMSzOZ6arldBKCrq2uh33Zo9GyQ1gm2hbXUMXo5Jx69679qH_AgNecLwcVNC_bKuvXvyVBYezSdZEDudJKNBSdaCoCl9XkMb-flwybOJlrdstwLUeXlYos5KtAFnmquqr4SjDuqYqLATqGiUrNDlRFRALASdyelqd1QNd_720cQwJwkOchYa1l65JQJ6wJEBaYAh3rDc73LsJOmjDkRAP2qFeJSR8XSYB7q3fHdAd6nmFXlRgNIoadbgO0kzqhEyJVMN2TOuBauWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
لباس‌های بازیکنان و اعضای فنی تیم ملی فوتبال کنگو در فضای مجازی حسابی سروصدا به پا کرد
🔹
این تیم آفریقایی که دومین حضور خود را در جام جهانی تجربه می،کند، کارزار خود را از ۱۷ ژوئن با دیدار مقابل پرتغال آغاز خواهد کرد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659407" target="_blank">📅 20:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام مهم فرمانده قرارگاه مرکزی خاتم‌الانبیا (ص) منتشر می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659406" target="_blank">📅 20:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
اظهارات تند مقامات اسرائیلی؛ ترامپ ما را فریب داد!
🔹
رسانه صهیونی وای‌نت به نقل از یک مقام ارشد اسرائیلی نوشت: «ترامپ ما را فریب داد و اکنون در شوک هستیم. آمریکا به ایران امتیاز داده و ما دیگر نمی‌توانیم بر روندها تأثیر بگذاریم. ایران توان موشکی خود را تقویت می‌کند و اسرائیل باید هزینه‌های سنگینی برای دفاع بپردازد.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659405" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbygljE4dChupfCP1snY6efi6dPlBFpriSfpOt-1KB6Py6gY1Cdx-8V9_Fgo5TGpNzdWnVYkC-BxvKaudOG_s0utYhx9v0ONYy3Qd8OxyIClzYygIsdKSnzDfeZPD-1R77YqheisEwx4KzPR-f0JTlwoQiDtBAel19x5Cb76B61sqFB2XfdYMnwdFZGrH2x3k79UhX8Hghfs69fJlcxcThN8TULj8Wd0hKP5Ke9-OK7yiwZ7zoBWm1IQYIYIWyOy7vfK72TNa2bZ7ReCcZXdUTVvCvKE143VJM8Y53TjFuVE6rVV4c1FwONMsupDJUC7g825fpW35oYe0izBVnTFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین جهش سرمایه تاریخ
#بیمه_البرز
مجمع عمومی فوق‌العاده بيمه البرز، افزایش سرمایه این شرکت از ۷ به ٨/١ همت و سپس ۲۹ همت را به تصویب رساند.
▪️
افزایش سرمایه چشمگير
۲۹۰ هزار میلیارد ریالی
▪️
و تمديد مجوز قبولی اتکایی از داخل
دو بال قدرتمند بيمه البرز برای راهبری بی‌رقیب در بخش خصوصی صنعت بيمه
بیمه البرز؛ توانگر و‌ماندگار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659404" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haG2o64uxPnI0hZBfsjdB2aiDbQufzfKNV7qQ36fFk3j0-xirsbXmNLeH4XMOv-gbyUjs3YZK9Iv2b2tE6Zlvi7KSnnr3OCv-TMpzhbnezwwgTT6bAQzYy7D0xpjQuuGiVH-3P8A5MOVIekuOJ_lRZ_8jZSmlCCZ9sn2d3Yh-UwRCdlWuhCWVWl40c1QjlsC5iLz8SLJ3Qm6BFkXURZP7WC9uLZvsLWttZLNt5roGCIOSpSuNPeIvOrushkk59w16_w_wtW3SxkDdiKGBTizxWjXo3l2oQ1LnMFbUTyV6pPbLVFy1Vnru7cAMvj_jG2gaSe4jDt3lX-u_8vYvxhKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNZ4wO-MdAJO7NfhTSIyFqfRmu3i5V0_5izR8PT6qRCdjHLVXM_tH5NuvaufTnck4J88wR0xYIccTb31bk49IAdjXE-mxOqnVnqvTw0foBmYSkW6ZzNWPPoygX-ISSftif3AcJA7wDHc8qSWL-YpcH3o6ijYxDq6ezfWYIVOc94Nuvxx-sHnZ6yB7Wl3AsKXb14tdTENT9P_mXNKe4v-gxgph2rfMvGucOZxLFrrJFchOSgIFqL0jkD-SXNsGIKuyUpBxa3l-NVbepHwqh7uyDtYQanMfXzUBtx7exTEqn257HUAYPdEXSvr7quaGx7etd7_g_6smp-ssA_Gzm78HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بر جاده‌های آبی سرخ
🖋
نویسنده: نادر ابراهیمی
🔹
کتابی تاریخی داستانی که روایتی است شاعرانه از اراده، مقاومت و هویت ایرانی. این کتاب روایتگر زندگی میرمهنا قهرمانی گمنام است که استعمار کوشید او را «دزد دریایی» بنامد؛ اما مدافع شجاع ایران و خلیج فارس…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659402" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
۳ شکار امروز پهپادهای حزب‌الله
حزب‌الله:
🔹
یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659401" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عطر سیب این روزها در میدان آیینی امام حسین(ع) جریان دارد...
🔹
بیست‌وچهارمین رویداد فرهنگی «عطر سیب» با حضور هیئات مذهبی، خادمان اهل‌بیت(ع) و عاشقان سیدالشهدا(ع) در حال برگزاری است؛ رویدادی که هر سال، تهران را برای استقبال از محرم آماده می‌کند.
🔹
اگر هنوز به عطر سیب سر نزده‌اید، فرصت باقی است...
🏴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659400" target="_blank">📅 20:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9NYS1TsPczvO-pX2JaT_2kpVcFO__aA2cHqv4dn_BmIx4jPC-mbXYk7TYHruh4PAWChfe0g-SdSmqcq2ns74s_8G_d3Bu_QjYIUF96BPEaCrbWgQtWzcL_3I0n59Aj3uZYFZAAXvs91zom9u5HuVYowz42U8YbqW8ShpcMk5Pvf2AM5XHJzVSqrW9rE1DBR_mPEvCyTq6mKHraeae4pSgvhHasQepm-LIats3RiwRwypMyZGwfb3mH4KlaxLk-Q5bbLnn8wTTxX6nkYFMGehjqbe1gpU6b9Je7cLW9MCU8DX5nsbc84sfo2KcHGpqvjwCImZMG8aEAcIdQtG1ZnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ کامبک کامل نشد/ شکست شاگردان پیاتزا مقابل بلژیک
🔹
ایران
2️⃣
➖
3️⃣
بلژیک
🇮🇷
۲۳|۲۲|۲۵|۲۵|۱۱
🇧🇪
۲۵|۲۵|۲۳|۱۷|۱۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659399" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQk1Fmphld7IaXDqXleTmRBxRS0hrCD82GC4l6KEI4bB15z3lF-880__uf-iF_v6QYadsFOz4ciZwgfLtc2T-uel8_nNT2YQ2Q_pnFhS6uodO_Bz8Reab_7UrhWIGazLXNpD_ESDUXQj14WgB42eLQxFQjB5MZ8f-pClwp8wI3jY96v9NHnHLccJUOvg4emYFcfa7OqCIVtv9tas0_b5zbC0AiR4ahs3axkdDzBKEtbF4yQfWZ3N6erHKVd_6ay2YqC6LoGMJU0EVuNpB6RInRpiQ2oVYTW4oHImbUulYT4jJki61eiBcKOovE8tUnVy_BNeG1BZW5YEUuYMDza2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پنل تخصصی همایش «نقطه تصمیم» چه گذشت؟
🔹
فعالان اقتصاد دیجیتال در پنل تخصصی همایش «نقطه تصمیم» مهم‌ترین چالش امروز کسب‌وکارها را «عدم قطعیت» عنوان کردند.
🔹
دانیال احمدزاده، مدیرعامل ایران‌سرور، عدم قطعیت را بزرگ‌ترین چالش کسب‌وکارها دانست و بر اهمیت یادگیری…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659398" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ترامپ: از ایران درخواست کردم به حمله اسرائیل به بیروت پاسخ ندهد  رییس دولت تروریستی آمریکا:
🔹
من از ایران درخواست کردم با حمله موشکی به حمله اسرائیل به بیروت پاسخ ندهد.
🔹
به نتانیاهو گفتم که هیچ حمله دیگری به لبنان انجام ندهد چون این اقدام توافق با ایران را…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659396" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659395">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام مهم فرمانده قرارگاه مرکزی خاتم‌الانبیا (ص) منتشر می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659395" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ترامپ: به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی؟»  ترامپ:
🔹
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔹
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم. او اصلاً قضاوت درستی نداره. من این رو بهش گفتم/ انتخاب…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659394" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مطالبه ملی از قوه قضاییه و دستگاه دیپلماسی برای پیگیری حقوقی ترور رهبر شهید انقلاب
🔹
امروز مطالبه خیابان‌ها نسبت به ترور رهبر شهید انقلاب، فراتر از محکومیت سیاسی این جنایت، معطوف به پیگیری حقوقی آن در مجامع بین‌المللی است.
🔹
افکار عمومی و گزارش‌های رسانه‌ای نشان می‌دهد که مطالبات گسترده‌ای برای ورود جدی نهادهای حقوقی و بین‌المللی به این پرونده شکل گرفته است.
🔹
در چارچوب حقوق بین‌الملل، ترور رهبران سیاسی و دینی کشورها نقض آشکار اصول حاکمیت ملی و قواعد بنیادین روابط بین‌الملل محسوب می‌شود و کنوانسیون چهارم ژنو، پروتکل الحاقی اول، قواعد مندرج در اساسنامه رم و همچنین بند ۴ ماده ۲ منشور ملل متحد، چنین اقداماتی را مغایر حقوق بین‌الملل می‌دانند.
🔹
امروز خیابان از نهادهای بین‌المللی می‌خواهد که در برابر این جنایت سکوت نکنند؛ چرا که بی‌عملی در این پرونده می‌تواند به عادی‌سازی تروریسم دولتی و گسترش چنین اقدامات خطرناکی در جهان منجر شود.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659393" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ: به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی
؟»
ترامپ:
🔹
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔹
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم. او اصلاً قضاوت درستی نداره. من این رو بهش گفتم/ انتخاب
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659392" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مدیرکل تأمین اجتماعی یزد: منابع مالی کافی برای پرداخت حقوق خردادماه با احکام جدید فراهم نشده است
🔹
حسن زارع، مدیرکل تأمین اجتماعی استان یزد از صدور احکام افزایش حقوق سال ۱۴۰۵ بازنشستگان خبر داد.
🔹
وی افزود: با توجه به شرایط وصول حق بیمه توسط سازمان، تا این لحظه منابع مالی کافی برای پرداخت حقوق خردادماه بر اساس احکام جدید افزایش حقوق فراهم نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659391" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659390">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw6tmP271sMuI524TP3kytBgHF3_3VCVILRu4M1B-8byXm8ksr4_H-7jfc-nbGr5oaifBhVLucw-1hH7aplQbCjD5R_dTSg3Ic3CElxomxrTZtbBpE5VpMbNsUMrmzb9uugfRs7QiVKxolgtm6WQF15QHipIbP8biKBDHm5FDdFrnjCEqn2fabj_3WzSmH9n5xeWPQGMTYWn3zKxliOCLjFgIr-Taix-nhA4qjrjXkrtxxqCQ9BKcqv32ewnpOCsFt0bAzvXUwm46yp55mkIGirKxx00Eilg7vl1MSpmtXalbnKn2oa_nFpdJIJAjkxBy6JB2N9P_MkWBK5Nq4CEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنچه تا امروز در جام جهانی ۲۰۲۶ گذشت
🔸
جام جهانی ۲۰۲۶ از ۲۱ خرداد ۱۴۰۵ با میزبانی مشترک مکزیک، آمریکا و کانادا رسماً آغاز شد.
🔸
این دوره با حضور ۴۸ تیم و میزبانی مشترک آمریکا، کانادا و مکزیک، پر از شگفتی و بازی‌های فشرده دنبال می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659390" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659389">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی پوتین و ترامپ درباره ایران
🔹
ترامپ به پوتین گفته است که توافق بین ایران و آمریکا بسیار نزدیک بوده و ممکن است امروز اعلام شود.
🔹
پوتین نیز از مهار شدن درگیری بین ایران و آمریکا که می‌توانست کل منطقه را شعله‌ور کند، ابراز رضایت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659389" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آچمز شدن وزیر جنگ آمریکا در یک گفتگوی تلویزیونی
🔹
«پیت هگست»، وزیر جنگ دولت تروریستی آمریکا در گفتگو با شبکه سی‌بی‌اس مدعی شد آمریکا در تمام این مدت بر تنگه‌ هرمز کنترل داشته‌ است.
🔹
مجری برنامه در پاسخ به این ادعا او را به چالش کشید و گفت: «اگر چنین است…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659388" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازارها چند درصد روی صعود ایران شرط بستند؟
🔹
همزمان با آغاز رقابت‌های جام‌جهانی بازار پیش‌بینی‌ها و شرط‌بندی‌ها روی تیم‌های صعود کننده داغ شده!
🔹
حالا ایران طبق این شرط‌بندی‌ها چقدر شانس صعود دارد؟ در این ویدئو بررسی کرده‌ایم
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659386" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان: عبور موفق از این شرایط نیازمند همراهی مردم و مشارکت عمومی در اصلاح الگوی مصرف است
🔹
با وجود ناترازی‌ها و آسیب‌های واردشده به زیرساخت‌های انرژی، دستگاه‌های مسئول تاکنون شرایط را مدیریت کرده‌اند و با مشارکت مردم، بخش تولید، صنعت و خانوارها با مشکل…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659385" target="_blank">📅 19:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
♦️
پزشکیان: مردمی که در بیش از ۱۰۰ روز گذشته و در سخت‌ترین شرایط از کشور و نظام حمایت کردند، اگر با تورم و مشکلات اقتصادی پی‌درپی مواجه باشند ممکن است دلسرد و ناراضی شوند
🔹
دولت خود را موظف می‌داند تمام توان خود را برای بهبود شرایط زندگی آنان به کار گیرد.…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659383" target="_blank">📅 19:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
♦️
پزشکیان: مذاکره به معنای چشم‌پوشی از اصول نیست و جمهوری اسلامی ایران در برابر هیچ‌گونه زورگویی و فشار غیرقانونی سر تسلیم فرود نخواهد آورد
🔹
مذاکرات تنها یکی از ابزارهای تأمین منافع ملی است. دولت همزمان مسیرهای مختلفی را برای تقویت اقتصاد و ارتقای جایگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659382" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVEFxPykYGRdiBB52kbXcEjeS9OqLgrzyu0AyUO0oc9J59C9NTLUQxbmYr8r6iCs3_W1glsQ906rPwqhzXO2Pr_m5SD8WMNJqPigIKLRTCk74Y8oQ_OexN0Z_glXRz3-13cmPfbQ8DvygwsNWS1-y2TV-VAKstMhsaMamKV1vsEmB_KY9IIcdWogNcbQ6Yf15jWiWkNy_ozZBRSDXy-1Jfzz8oVRKTl2SDSLgOWieeHni2Ar61SwjGulGEBIzfCf55ZT01jaLqSpzN7IvOhHgBNMruyVC8d8Eq1vt1om_5gN-eReXtTU4UMJTTIG5S_cs-9hZRy2OlNncgCMZ_2d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پنل تخصصی همایش «نقطه تصمیم» چه گذشت؟
🔹
فعالان اقتصاد دیجیتال در پنل تخصصی همایش «نقطه تصمیم» مهم‌ترین چالش امروز کسب‌وکارها را «عدم قطعیت» عنوان کردند.
🔹
دانیال احمدزاده، مدیرعامل ایران‌سرور، عدم قطعیت را بزرگ‌ترین چالش کسب‌وکارها دانست و بر اهمیت یادگیری مداوم برای بقا در اقتصاد دیجیتال تأکید کرد. یوسف مذهب، مدیرعامل آموت، سیستم‌سازی را راهی برای عبور از بحران‌ها و ارائه خدمات باکیفیت عنوان کرد.
🔹
زهرا مکرمی، مدیرعامل کیف پول من، گفت این مجموعه در شش ماه گذشته تمرکز خود را بر پایداری سیستم‌ها گذاشته و معتقد است باید از دل تهدیدها فرصت ساخت.
🔹
امیرعلی نجومی، مدیر روابط عمومی سپهران، نیز با اشاره به توقف توسعه در بسیاری از کسب‌وکارها برای حفظ بقا، از تأثیر رشد هوش مصنوعی بر کاهش برخی فرصت‌های شغلی سخن گفت.
🔹
صادق شریعتی، مدیرعامل اقامت ۲۴، حفظ نیروی انسانی را مهم‌ترین دستاورد ماه‌های اخیر دانست و گفت صنعت گردشگری با هر بحران بیشترین آسیب را می‌بیند.
🔹
وحید ابراهیمی، مدیرعامل گروه دایان، نیز تأکید کرد حفظ سرمایه انسانی در دوران بحران، کلید موفقیت در دوره پسابحران است.
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659381" target="_blank">📅 19:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
♦️
پزشکیان: بخش مهمی از تلاش‌های دیپلماتیک کشور در هفته‌های اخیر نتایج مثبتی به همراه داشته و بسیاری از مسائل و سوءتفاهم‌ها با کشورهای حوزۀ خلیج فارس در مسیر حل‌وفصل قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659380" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
♦️
پزشکیان: پیش از این نیز گفته‌ام و امروز نیز بر همان موضع تأکید دارم که از بابت قرار گرفتن کشورهای همسایه در معرض تبعات اقدامات نظامی ابراز تأسف می‌کنم
🔹
البته هدف عملیات ما پایگاه‌های آمریکا در خاک این کشورها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659379" target="_blank">📅 19:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
♦️
پزشکیان: تصمیمات راهبردی باید بر مبنای عقلانیت، محاسبۀ دقیق و در نظر گرفتن توان ملی گرفته شود
🔹
در کنار حمایت از نیروهای مسلح، باید نسبت میان مأموریت‌ها، امکانات و ظرفیت‌های کشور نیز مورد توجه قرار گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659378" target="_blank">📅 19:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
♦️
پزشکیان: مهم‌ترین اولویت دولت، بهبود شرایط زندگی مردم و کاهش فشارهای اقتصادی جنگ اخیر بر خانوارهاست
🔹
امروز بخش‌هایی از جامعه با مشکلات معیشتی جدی روبه‌رو هستند؛ درحالی‌که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659377" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اعلام زمان تعویض پرچم حرم امام حسین علیه‌السلام
🔹
آستان مقدس حرم امام حسین علیه‌السلام اعلام کرد که مراسم پایین آوردن پرچم قرمز و برافراشتن پرچم عزا و سیاه بر فراز گنبد حرم، غروب روز سه‌شنبه و پس از نماز مغرب و عشاء برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659376" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
♦️
پاسخ پزشکیان به دروغ‌پردازی‌ها در مورد استعفایش
🔹
بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام و اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659375" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct_R0Xxzh2FnoQPKlRI7A7DiF2n8ygspGAqjSCIkq-KCPw2nG56maO-aE0JMZzM1Uey-V24s3LD5JhFqNYdjQss0wBzHnaG5Gl-3Ko7kDELL6NOWuMhVrbk2hieybFJIeG7aFHkuOtm7Ch6LOWL5i1Q-Bl0cClGYLI5l2HsohFcadJo600lIX1GMloQLem6IxoLvHr39L1S7yk6Z340PTuNl0dvHjXU5gu2Fcl4x2Q78GPfXU20SVXoNe55iWFRFay1Elnb5AN3sQe3Uf7SBcBPs0NFIbuUJbsIvTSKTiDI5rJ1x5tJu5xfFL2Svj-mNzvNTnRyFDZsjmSbaQOP49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پادشاه خاتون؛ شاعری فرمانروا
🔹
پادشاه خاتون، بانوی قدرتمند عصر ایلخانی، در دل آشوب مغولان به فرمانروایی و سیاست رسید. او تنها حاکمی زیرک نبود؛ شاعری خوش‌ذوق، خوشنویسی چیره‌دست و پشتیبان فرهنگ و دانش نیز بود. قرآن را به دست خویش نوشت و دربارش پناهگاه ادیبان،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659374" target="_blank">📅 19:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
♦️
پزشکیان:  دولت برای حفظ منافع کشور و مردم تلخ زبانی‌ها را به جان می‌خرد
🔹
ما با تمام وجود برای خدمت به کشور و مردم عزیزمان و همچنین آرمان‌ها و ارزش‌های واقعی خود آمده‌ایم نه ارزش‌های کاذب و غیرواقعی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659373" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌ ‌
♦️
پزشکیان: [در مورد مذاکرات] حتی اگر نظر شخصی بنده متفاوت باشد، خود را موظف به تبعیت از تصمیم نهایی نظام می‌دانم؛ چراکه معتقدم ایشان براساس دور اندیشی و همفکری با عقلای کشور و در نظر گرفتن مصالح و منافع ملت تصمیم خواهند گرفت نه تحت فشار جریان‌های سیاسی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659372" target="_blank">📅 19:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
پزشکیان: ما به دنبال آن هستیم که از مسیر حفظ اقتدار ملی، برای کشور گشایش ایجاد و منافع مردم را تأمین کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659371" target="_blank">📅 19:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
پزشکیان: نقد و مطالبه‌گری حق طبیعی جامعه است، اما تخریب کسانی که مأموریت مبتنی بر قانون به‌عهده دارند به دور از انصاف و مردانگی است
🔹
مایه تأسف است که افرادی که در چارچوب مأموریت‌های رسمی و با هدف صیانت از منافع ملی و عزت کشور در حال انجام وظیفه هستند،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659370" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
♦️
پزشکیان: در برابر هیچ قدرتی سر تعظیم فرود نخواهیم آورد، اما در برابر ملت ایران و مطالبات مشروع آنان خود را مسئول و پاسخگو می‌دانیم. البته منظور از مردم، همه مردم ایران هستند، نه یک جریان یا گروه خاص
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659369" target="_blank">📅 19:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
برگزاری کابینه امنیتی اسرائیل در پناهگاه‌های زیرزمینی
🔹
شبکه ۱۳ تلویزیون رژیم صهیونیستی از اتخاذ تدابیر امنیتی فوق‌العاده برای برگزاری نشست امشب کابینه جنگ این رژیم خبر داد.
🔹
به گزارش این شبکه، به دلیل افزایش تنش‌ها و احتمال پاسخ مستقیم ایران به تجاوزات اخیر، نشست امشب کابینه امنیتی سیاسی در یکی از سایت‌های فوق‌محرمانه و مستحکم زیرزمینی برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659368" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
♦️
پزشکیان: تحولات اخیر نشان داد که هیچ کشوری بیش از خود ما دغدغه منافع ایران را ندارد و به جز خدای متعال به هیچ کس نباید متکی باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659367" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659366" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659365" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVX56Cyeu_F1mtIk0dGS4Y05ApS443A_6afWtAmSKdIWft5CXe5f0P3hByXXCRbcl37EWJlliGSlQ335Z_y83-nVok6UuLQmXoZP29YPaCwYtUzY86wdW64LkRd79SZvJuorT1xtLAIlPHEYfSkAt3Hs3JObN2Dxl1SeTcA7TANO53NQKFstwmQnEtLUJUnVNNIyKh4CebgUsHtbhAfYrhtenSzY-ecGVLtg0GZYoj_kOKyQKnQFFKHR9F6G8kBVM_M5cs3QGQyEQk9VN5-7f0nR4pgWjQCYwKrHdsNLjb7glsM2XMi16c-7zfc_cnrLXCkHfRbZlfmw4ANqM1Zwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده هوافضا: گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659364" target="_blank">📅 18:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDbjNKuATXwEo1S4NSJUYDFdt_U3sq3xXXausy0Droo_PAsRjZMHEdrKFbooH_cuO_QxAb0sTtD3E9WI_GsyQ8dchS5c7LvHVwshdtOoGz-fCVKb5q1N9XNe8tBMoBlSjj8LsfCDe6v017L5BDbuDunB1GlELjaV8E7tUzyxTIQ1bPOp-Q8iWSTESN54TGzlERiBr72azwKMsab6Lhho5Ej7zhbEzdW4YDmUlrLZXPBtJDUJf6HmV4ffx4FuLaPtm7Ct7PAVFgnhQim29jgBgtEAC8BbUVGDDLgmnlYXPaTeyftNrRYk4GS74SO_G-yAAMnX4ilJkR8grs_bkakFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659363" target="_blank">📅 18:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOzzWbgWW8mebUfeb9Db4nmhL9Qgx_82juhM2Qi1PguUqf-X_dW-V6pufeU-BY4b4LT9MpuwNnhXVm6tTQ6Q0jcquZXjW8_3M_CFMrQlFUHbG59FscJYiFrPTzaz1Ga_wSQnrAm84GcjJLIhTCWNeFqxXEJ_Ejk8nLEKO0moM7LhBcNrlkTRsue2D-5B80e3JC3jaPkMV_sfmKkp8Q3oA7MYoNhqN94HpNSj597wqjhw9mHQ6KEWBCwkLt1S_uJJTDyAf-bPasP5uuTIEBOS259C1RAW29cNlrzTr0nNuDzkpW2fZrUYLIBGJcuTzOu0pUIrXCazKIgnsJhVMalUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه کان اسرائیل به نقل از منابع امنیتی: اسرائیل با توافق آمریکا و ایران از جنوب لبنان عقب‌نشینی نخواهد کرد
خبرگزاری آناتولی:
🔹
منابع امنیتی اسرائیل در گفتگو با شبکه کان اعلام کردند که اسرائیل به دنبال توافق احتمالی میان آمریکا و ایران، از جنوب لبنان عقب‌نشینی نخواهد کرد و عملیات نظامی در این مناطق را ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659362" target="_blank">📅 18:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تشکیل پلیس اطفال تصویب شد
محمدحسین محمدی، نائب رئیس اول کمیسیون قضایی در
#گفتگو
با خبرفوری:
🔹
در اصلاح قانون آیین دادرسی کیفری، حدود ۱۰۰ ماده مورد بازنگری و اصلاح قرار گرفت.
🔹
در این اصلاحیه، موضوع «پلیس اطفال» به قانون اضافه شده و دولت مکلف شده با همکاری نیروی انتظامی و بهزیستی، این نهاد را برای حمایت از کودکان و نوجوانان تشکیل دهد.
🔹
همچنین ماده ۴۷۷ قانون با هدف تأمین بهتر حقوق مردم و جلوگیری از اطاله دادرسی اصلاح شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659361" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f8e64c4f.mp4?token=RCwZ46AK2gOlYkQTUOD_jJ0v3qgNFrq4n6bo28ZvzB4r6fL5FheFRrSjft35G2IF8W2WV8If0ylePGcT4Z41xMNkjddqs7UE85XOs24ykEZqHQO3YtldQdsLKbOgiSl5RsnmFDxKOXcF3PSLjJF6Fvw9HFnKUdimOjSD3mCqrQREUf0XVb8Rhi9wqsHJn_rX-eulCclf8sjrZrd-L1dxQeHCekL5YAcYil6Unbd7KMjNoRAFuFDRcoMmoiqTjxXoht4gh8QQl5UqPICeXdFPBbiQ_Ov3DDu_Ai5KuRlC5zYXUxdU_wEx5i7ddHTAK5faTyFZf9iia0UdDAQ5wxkFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f8e64c4f.mp4?token=RCwZ46AK2gOlYkQTUOD_jJ0v3qgNFrq4n6bo28ZvzB4r6fL5FheFRrSjft35G2IF8W2WV8If0ylePGcT4Z41xMNkjddqs7UE85XOs24ykEZqHQO3YtldQdsLKbOgiSl5RsnmFDxKOXcF3PSLjJF6Fvw9HFnKUdimOjSD3mCqrQREUf0XVb8Rhi9wqsHJn_rX-eulCclf8sjrZrd-L1dxQeHCekL5YAcYil6Unbd7KMjNoRAFuFDRcoMmoiqTjxXoht4gh8QQl5UqPICeXdFPBbiQ_Ov3DDu_Ai5KuRlC5zYXUxdU_wEx5i7ddHTAK5faTyFZf9iia0UdDAQ5wxkFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۲ بالگرد در آسمان ریودوژانیرو در برزیل
🔹
۶ نفر پس از برخورد ۲ بالگرد در آسمان درجنوب غربی ریودوژانیرو، در برزیل جان باختند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659360" target="_blank">📅 18:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEjTQc6cjw3xL9P5thdfeAu2fPaswB_Pew9onrKhAbCe1EvRbsmFmr_SxFG7Ak_upCp78HeyJnj32L0d-TUFv7dRTSv_14MxFFR9AKZxevbI1zmEF-Re_4vYa8mJNkNurkNeFnA3abM9E-1Ms7tl6e01OXdYnWCQOJJH_WWTYIq3q8Oil7WsvrCMIO33_304dEAgCUhj2yIiHjehvuK_toFfW0xBLLbsjHGkFIQRNHbwXgQ51vPj7-DvWF2Zj_ey8uXy34Gxs6qhH8SKGYKBpNjFGsNVVj0vdMCpTnfJqmo42S-aGDcul1Wnt5JJSolqz75oCTlBZNolXQe0Nt279g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه / در کمتر از ۲۴ ساعت؛ ارائه خدمات مبتنی بر کارت در بانک‌تجارت فعال شد
🔹
ضمن قدردانی از سعه صدر مشتریان ارجمند به استحضار می‌رساند، ارائه خدمات انتقال وجه از طریق خودپرداز و خرید از  پایانه‌های فروشگاهی و سایر درگاه‌های پرداخت در کمتر از ۲۴ ساعت پس از اختلال، صبح امروز ( یکشنبه ۲۴ خرداد ماه) فعال گردید.
🔹
همچنین انجام خدمات مبتنی بر کارت از بستر همراه بانک‌تجارت امکانپذیر است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659359" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f547678c0c.mp4?token=RnxaMNIVp0DQKrEgbYQKt5SBflHku0WDgYm52fZkWnPSQ9eeXXJw-zD37jarv_H5unZxcg-x6nJN8scu65O6ERMt0mVopec1_HGEMw-97d16oid_WLymBCgaH6vYITTAlCkfHJLh0k-R4v0F5M7Rqtq5Xij5lvW4AXknpLU96jb9OfdlzIUQdPZw7K2XE3JO6Nuy_36ZCIoBI6rDjpHoTByKbxfuxrydjV7NjFbHIS4W4ZDVZruhEnM76R8JCp5w23qPHh-jrtANiTcDoAAJ-WnICAo1qEo_S4DVezvbrIa1gYy8tCDn-uSfCPnHpMB7fXRNpk34S7wC03MZj59ULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f547678c0c.mp4?token=RnxaMNIVp0DQKrEgbYQKt5SBflHku0WDgYm52fZkWnPSQ9eeXXJw-zD37jarv_H5unZxcg-x6nJN8scu65O6ERMt0mVopec1_HGEMw-97d16oid_WLymBCgaH6vYITTAlCkfHJLh0k-R4v0F5M7Rqtq5Xij5lvW4AXknpLU96jb9OfdlzIUQdPZw7K2XE3JO6Nuy_36ZCIoBI6rDjpHoTByKbxfuxrydjV7NjFbHIS4W4ZDVZruhEnM76R8JCp5w23qPHh-jrtANiTcDoAAJ-WnICAo1qEo_S4DVezvbrIa1gYy8tCDn-uSfCPnHpMB7fXRNpk34S7wC03MZj59ULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش ویدیویی از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659358" target="_blank">📅 18:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da291ebc.mp4?token=qw-cFMhQjjwd6G4R-2X330JFmV37B4GxCcEEdIU8aO8pUSxgnT_0ARcEtXsxNDSET3P2JQFcS3YBS_-qCQugYdHDphBE0C8UvHbRMGc11jywcOqKXMjd7XjKKMvpzbXVk7J0yox5f911kTd-_sY4h4mqZb-yKTk8Wg_XIAJ2fSxN183NmpluLKXcVMyaRrF4OChhhA6w_8yZO3fBcSOWS3-8gG4eESAQEeLYBcdWJqCV_QnvkREzCmWgFtQdUZsh9iXJjjdcHmqBk4aTL7FkUexSuDHMaKS5GRw8EpVSwqimbEUAEfOhV6tl44PjDlhkM0n1d__5xLhamUT8tqcptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da291ebc.mp4?token=qw-cFMhQjjwd6G4R-2X330JFmV37B4GxCcEEdIU8aO8pUSxgnT_0ARcEtXsxNDSET3P2JQFcS3YBS_-qCQugYdHDphBE0C8UvHbRMGc11jywcOqKXMjd7XjKKMvpzbXVk7J0yox5f911kTd-_sY4h4mqZb-yKTk8Wg_XIAJ2fSxN183NmpluLKXcVMyaRrF4OChhhA6w_8yZO3fBcSOWS3-8gG4eESAQEeLYBcdWJqCV_QnvkREzCmWgFtQdUZsh9iXJjjdcHmqBk4aTL7FkUexSuDHMaKS5GRw8EpVSwqimbEUAEfOhV6tl44PjDlhkM0n1d__5xLhamUT8tqcptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آچمز شدن وزیر جنگ آمریکا در یک گفتگوی تلویزیونی
🔹
«پیت هگست»، وزیر جنگ دولت تروریستی آمریکا در گفتگو با شبکه سی‌بی‌اس مدعی شد آمریکا در تمام این مدت بر تنگه‌ هرمز کنترل داشته‌ است.
🔹
مجری برنامه در پاسخ به این ادعا او را به چالش کشید و گفت: «اگر چنین است (چرا) شما در حال مذاکره با ایران برای بازگشایی آن هستید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659357" target="_blank">📅 18:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oODkHzffYytgrJQzRaTEVTzziai4apmLgHk3J0wuKPnwhoG3V5DqUdoSTNV_gWkhh5wuWw3aqVfyAjEyxzuviEEATzJdgf-0ZpcOL-UCelPQmekwIry78a8-1D_pPsyCgGoKPhodvY3xjbRVmDihxp-8_u4Xlrd71UdftAIS8-_3bLIAfa6ZltugW0K9n6XNecs2tmyjt2TmwiBZyZ-ID29gFjAmJKO2UmB4OhXZBXfiMxu72RiJ84p11VmeynBA6OQlq9iLtqE605zKwDu8sQ3xaEOCpE3RiW1vgrpow6hgchjgJHAiL8plH51ZZGqyfqPkdkfRvXFa9vg_V_xEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور ۱۴ کشور مسلمان در جام‌جهانی
🔹
مراکش، مصر، الجزایر، سنگال، تونس، عربستان، ایران، قطر، عراق، اردن، ازبکستان، ساحل‌عاج، ترکیه و بوسنی کشورهای مسلمان جام هستند.
🔹
جمعیت مسلمان این ۱۴ کشور از مرز ۶۵۰ میلیون نفر عبور می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659356" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCb7C1LkfquNIehFdciqaHS_zz5Nx4ZEyCvJBi1xnfTNTF-Vg6QJWt9BBmghQ25ACjEyWv4gjkWjzfEs9E0cmidPYVcBD9FlK-x-ldKKOOof4CkpwXMhB6CJUgafsxDHND_LGojB0Kbpa76FF9TOo4YCQ7B9vWjvpjxDrxWpHjaaHpGsYfnPmSsqpIoh1yDH0_xA7MDoa24gUJjz73tAKw4pHtqcIIirrg2VUTH8pd0Ody0dDCXKAGmP6YJ8385HmazqmIJeILvzEcqjfZnCU6RFfcRf9U5j5xpC4_EK90TaphWI1pzgQp6Y24oXhZutM1Yf550XWCKfUqGQEZJIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم
🔹
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
🔹
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
🔹
این می‌تواند آغاز یک صلح طولانی و زیبا باشد؛ بیایید آن را خراب نکنیم!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659355" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پزشکیان: تصمیم‌گیری درباره جنگ و مذاکره بر عهده رهبری و شورای عالی امنیت ملی است
رئیس جمهور:
🔹
حفظ وحدت و انسجام ملی مهم‌ترین اولویت امروز کشور است.
🔹
همه جریان‌ها باید خود را ملزم به تبعیت از تصمیمات مبتنی بر نظر رهبر عالیقدر انقلاب بدانند.
🔹
دولت همزمان معیشت مردم، اقتدار ملی و توسعه روابط منطقه‌ای را دنبال می‌کند.
🔹
با انسجام داخلی، دیپلماسی فعال و اصلاحات اقتصادی با قدرت از چالش‌ها عبور خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659354" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بیمارستان‌های اسرائیل در حالت اضطراری قرار گرفتند
🔹
منابع خبری گزارش دادند که به بیمارستان‌های رژیم صهیونیستی دستور داده شده در آستانه احتمال هرگونه حمله از سوی ایران، به وضعیت اضطراری منتقل شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659353" target="_blank">📅 18:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای پیت هگزت، وزیر جنگ ایالات متحده: ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا می‌کنیم یا نه، بلکه این است که چه زمانی/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659352" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_l5P8JEigYhuScuSKUFf5hOPTel0QrdE_59tvDYx6Tb3m9vNI-zo28v1MG4e0qcUK5xki_iN5oXKakkNqx0dko1KBmoBmHDQAEue16D4cVB39nZwbwKLhkF-2XxM1d59BbSHjjMPkXglk2fLHeUbxgRGiK-ZzKGtjxPBKsRtwGsWAEiTC3RVH7RblsnM3Zne2bsFcPqxhRbvASaPHWeZJoILShtFDwMd98Tif0_0l-r2TeEAe9-Dgz3Wru8T103ZMQF26Ai4sM65UOIID2z-qZ5d76foMR4I-xOu6UkmJIqbN3rUWlqSBYzCLRJmXzH11B-y37HcqFWVTXlBQWBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJZVC3zvt5x1xLiMTZc1ftzgEPAf11umzlNCn1eNFvWzGhjSGCVN3RtW0S8PSMgfQciGVZTRC313SnyFrfb09PTAvdu8GTQGvrENim4Bw6zhhRWj7Jbftw56aHm73vIdPFz79pnqAP5ppMaa5IpuRm3uo0EjuuHOQEUpf_TnF_HckmU2nOLh_EQBFSx_YsHfCvKvni4MOAFFL-BST79LAbm21ll_PUDF16TjZz3x-Uhg4b3vo4b72_O3dz0Q5UxIQ8ndhoOStF0KQyFgB6LG9vrVSnT_hYyKjsaWO1nPbKrXaYp59pwiq98UZwAvK0LhPg-tewg-45jnQM9IsSWENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDBdzbevH2OuNKpMlUOVCSwGLKMrjCqdl5202Pyq89xtrRkw1NX7w7HHdI4YVCP1zgs5D1nvabDn3V55djI6Mb-a9YqDwks56hWrTCey-SC5tR15WADN-s3yA58Enu8vcGGz9ugqVIPOR_3dOExHDwv0UaXnVowZYxWhPFAlm6IcpIHyYmVin4eLHG0Q2-iPpFogui6q5XC5jmC0jNgUwgVzXTyNRdiwxf7Ykn0k51ihblZYM0Ydc3ZShrJ76dTg5SNhWwy3ORQsxXOT8eTUewpvOROfgpR1VXF44_r9LTaHlZhNZuJvwPZwARYbM540uVxkQdO5NByXpoO8VEWzhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام‌جهانی از کاپیتان‌های ۴۸ تیم حاضر در این مسابقات با حضور علیرضا جهانبخش از ایران
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659349" target="_blank">📅 18:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svn7KanoTEOA96Eie_YECNuSaF2F5Kfb-vTebPkcvtsFyhbnF8L-8uQoqvR_e8XCwOUApIrbReC4VZFQ6jLZ0CJEYnlYmBPNJQ_Fy2p8fJXKhwIZC8nBlukU6kHliviKxIPWz_w5XOLObhKxu2El6-nWQJvxNKJi3qh4RMhhTR2pt4i5QRsTRZ7RVzG0x1QtKimshCcDaU0Cxxs2HJJI-RZyI-9Ww1KxiaLGO7QtO0ss3E2WKZo48iANgadc1Z1Qde0M8VonLzc8vm58hGMS0FL8yTlmRYQjEbCSDsRGxtx28T3CbpJFdLfz9LOX1ttZoh8o-tZdHL8HsJesNlXnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2z9pUUz4C4L5OQQjZI_jelD_yB79OA1U9p21va3_VGAJV01BQH2JpyrdskyWvBhFviZPucSSAq9zUfeyNfVP6shRKnPnxqQuarJ0WL7JLG1XsHDyfchTNL_uoHrbrTTdgjAMn6Mn2FEPEaOJFZv64nTSQwEKy2iO6b_CoYCN1-N0uej3Qy7cCejoU1Hwxsa5dSqO0KO7QxrrzHfEXLkrBSTE7HvmfeAop-BvbNOSN6pAha9jTGvvZBPXwlL-9AoK236sYkmXMqq2p9xISfG7RFHypw69Sd0uS1olLo9ueD7sdhPQEzOvu3HIxGtFQLgyXXReHduNL4qj_n6TYZLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOe5oaYGxd1id9oqDWvC09NUmL7fZd8ZEKCJ5c5Q6oPRfRDdwCjVboliezURoRm9Ec-6OhO3iFkzAPH9jYKsdzqMQrui378BiGO4oNWvcgnwVlsF3xi3DrDLsSNdbEyF_8TZDa_MzD1OTy7jt83z_KmYWl1CpUiELRC-vvkhJq3H_XLoPK3ZNQWFfM154ZJrJ7v8vyjGHDcWND3UhLzVz9EBRmk93TS-wgdkkUr_q4eyagYh7Up7NLtOd0Gq3P5GCBdxvYg1D2my6PCqdkFkWlYUg_4zQPF-SoanSeZwWMXAu6IWFCe8XiM2XvxU9FiS717HprHzcIyFfDQmquUb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk3_IBtQcGyd-HgiKgKTrSGvKDef7HgeC-6EEVtbumMFzJ9cnIPJMpMx42NywFjG074X6dN3p2kBWm9fYGyrDXp9sVV6Tg1arqMbAAnoXpmIXN0Y3DbYRAt2xKHgf5wT2XMzyvdYqeh3D8ZHOwahQZurxb5BszRWm3noIL2c1rX1Wn7JrM3WE_AE4ffp7q-E6MHYmvPrGnHahqQEp-th2Gh8YHkUUS4vIzbN1kSXU9jzRjl2r4D6BFAQGAEnYC10hjVmbhgGrQ66umie3lwR8OA2mFrDVe9YMMVAJms-26FWqI1z8SH82Kb3vjfpray_RrhMClQ_0JCRmLs4JiGpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrTtRy6kzJj-kB2LXJziCerDYmtCsN7ZNM2Z0IhgMxq9qMZmbGlX2v2dpGZt666xCg1bHY_iuj7y5Cjr_h5k5qkiIOCVWdZDHDCbFKsrOzLlZC3ZWQMmBn-T6VCwZZPn3Ww7Xb3hhURY9M9-PFY5PPcSO9pU1OPmgZmOSpQqpNmbIDW4JaL2iHTQDqB6zBnM7CjX-gO0tond3KYEr01vy4a8VKGadu3REaNv86wjQJ3slLaBORAw5efd2mGj4GVXuuU5YiGtKif-6R2mDwapgZ1eBs0R1v9L59U3XIkTysduRmn6pDTT5f4ZH9To9x7vPR5O71an3cHE7FwnAmB0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeyxzgSnVwR8MJPyX47j4Sxy5R24xiZc9Kb8ewCSuKS_9GE8B-c0Wj2JUHn4CSuOgLN39Wh4NhwXA-0XwGcxINsGNA_uFZqOh08e6CypNc76M5bSm_PSgYCh5yT72ZO2hp7acJYcPTfvAq68Xkvc5_MTVFTeFhZD_HVUxD-i4IpJGEm8eolIbDHhTK1rVtwFyowCF76SmVviBRiIIguOkhhYPuCDnpuTz403o-OWK-K-CfFA1pteJpoiD9q-2m__9ELCJ56MiM8_oRqKn4Bty0B3S1_hdgnpDvCkXLIUuPEGwEMpshbNX906NbKUuCdPlVL4TxK4CrH_iobXcfe1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2IQVFTOU_dnMDkWpHONkZUIHdCEPTjQ6bQRRkTdjoRUD4M9b5O_utAAqQWWd45VFvgodRvdZ_snqpy0T3JyqCIbSawYq20tFkq3B65o42Sg9OAqCvF5HSypjY_Ow2LqCwaTsVMtL4BdSsBdGf6lw0pS2oSV9Urkg_momBOaUDXV9oOkr3FdVCLMRx0b2GVOHA5E_v89WLxoLvjmQ3MsATi7RYHJ3QzWIq-C4SJkrMaaKMkXrYp1MkMB8FLQwNf_Zpoo4vsjj1E_HiIteKSrzl8aLyZVPSvt60JHhMgwZBdANsT6u-nWpwUXj2EsxrBBTQZ07C6EH2xAx-CshN6U5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV5DUkYTSCzGSgzH7qiX7fSxpnqA9F-r3MXAzVkYDEZvn4-Uizct6UXi_Xsb1qT4HHl3bGgNQfkcTkU5j_OKhXdH-pNi6c-aJE3wNYDkLTCXs3j_y8pQnlBd43P61WKD46hK8BP61jC2gLhMVcyqvGyRFvKFsU8bzcZZrHCukTb0qBlpiktl5caH-ghQPPYXDCfxCT3XZoHqDn2vqcz7od52CWCegjHGdOs2CkhQLqgTaXZpjEWSjFmao77A-e2M1AqzvkW2rN437IPigVmeKFrkYzFyYDpsiQ4G4nblyDknE0Fcro-ME8w-6ekDguz3D5yfj0fxhGmadLN6DZ_67w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش تصویری از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، با حضور احمد جانجان در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659341" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
