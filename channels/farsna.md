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
<img src="https://cdn4.telesco.pe/file/KRARA2KsghrzjpZ0CM7UOX7J0DPvyG85Qf_0J7ZIJhXQnRHiOmVquN8C-o-P8nX1oE-9ULBqWKbLpC6wGpezzszYT6BybfXMbJxM4MuYeAV8vxkuizVrgqCSeFM4iZn_oSoh8b8M565GJ8i_XIRYoUABbof26sBSVqsRS5DdbuAOFZpnq6yH_lBDWm1VpIYuJOsy7iyPCPP-IfOJBlV4TpX4xumOP3jbMsTXPirCP1IM4GtdpEPoFkO0UQ80aruU024WOC9n7rvcbRxniTkTt2olMefc_jEjVBuwEfZkdPOvTO-0rz7OyJBU47RRt8xs9N_LYcKfcSroNARN_fHQAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 14:42:52</div>
<hr>

<div class="tg-post" id="msg-457733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMEg5eRULrf0NMdgmdylH_Q2VXQFZ3qbayOdG7bUmxkcvGCG5LSc7zree-hO1mfeY3mpO87Nos4qD-9i-ozLlTuYnI_zJ0omv7Tkb0_CA-o5UXAdVFRCXSHIgFR2dVtZCwutRXyqE8ih5xwulRxSSCmcSJFNV00EohhbHkHMfkbFxbPxQAEUk75ClRFXLLfF6vDc6xcQ5hgFrg3ssUCADhR0CNTx7vxcRjfq_Kgsbo9okj5Ne9zBa3qNBhCf7mroYtiG8e-M1PQZebkL1KFct9naES86q6Vmq958mppQOfow4pZ_9IgP9qqVM9rJB4K502tIj-KZtLnDLuk5B4J5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت مذاکره با آمریکا از زبان نخست‌وزیر کانادا
🔹
نخست‌وزیر کانادا مارک کارنی امروز با اشاره به شکست مذاکرات با آمریکا گفت که واشنگتن خواسته‌های «خیلی زیادی» داشت و در مقابل، امتیازات «خیلی کمی» می‌داد.
🔹
مارک کارنی اعلام کرد که کانادا از ۸ سپتامبر تعرفه‌هایی…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/457733" target="_blank">📅 14:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97fa8afb5a.mp4?token=RPw1D6q7jTXCEOB_Yvx6z7j16eg64EfDgxoe0hGVNm2HvQr-32CAmQofOZnkPhbs-0RQ2snBghh-A2L22ndhmVICoee5RPLni5wW62PMn4LSC_TdrH0cChu8hbSFMdmfrSj5ED-LK0hhFZVsZbrN_yDGX7WeDjGvSWN7EfZCBKcr131ITLqb9g8e4lJR7wFcpNpSxeu-Vx_SY7rYxrNhEd08JVwHTTCL7mU-9Opl82hznh3O243EhzmvbZPAcA6oUh-Q4UYPgDV7uiud2lfHq7JLzs3-6MH4_AWdjmOdziehMsDELqA4dqc6o1U_Psf_3HG4Ljh2dWBPQdSFCry22g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97fa8afb5a.mp4?token=RPw1D6q7jTXCEOB_Yvx6z7j16eg64EfDgxoe0hGVNm2HvQr-32CAmQofOZnkPhbs-0RQ2snBghh-A2L22ndhmVICoee5RPLni5wW62PMn4LSC_TdrH0cChu8hbSFMdmfrSj5ED-LK0hhFZVsZbrN_yDGX7WeDjGvSWN7EfZCBKcr131ITLqb9g8e4lJR7wFcpNpSxeu-Vx_SY7rYxrNhEd08JVwHTTCL7mU-9Opl82hznh3O243EhzmvbZPAcA6oUh-Q4UYPgDV7uiud2lfHq7JLzs3-6MH4_AWdjmOdziehMsDELqA4dqc6o1U_Psf_3HG4Ljh2dWBPQdSFCry22g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ حذف حبس برای مهریه‌های بالای ۱۴ سکه
🔹
ابوترابی، نماینده نجف‌آباد در مجلس: طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/457732" target="_blank">📅 14:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d41e31642.mp4?token=WBK4zqyX52uOZDa2f3yFiTxhcrSOIezy4w4E5LGDx36rp6tf2WZwBfLFAm4U7MGue7W51mfJGSrn1jAxOV7DiHGIp7cOY9h0IX-1Z3OVGGB4oUr0kPNXFlJVfV6eDstiQezLwasQclvNReNTOisGcUeMPzaqz0Nj_n4x5Cn2n6ZcG7VG5motvbwFM_Qf5GekLaaaMCwqiHv22AbWhSmDwe-sZMbg0Xrq6vDdvs0A4APYlZE8lWORSV7XonyLkarzZXssScfpbheBFnNhnrz9ljIJAlwqVYBPKfs8XlXd1cbazOmZ1oTf3k9r7kV0w4RPWr3U7YFiIV3XRim-SNaEHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d41e31642.mp4?token=WBK4zqyX52uOZDa2f3yFiTxhcrSOIezy4w4E5LGDx36rp6tf2WZwBfLFAm4U7MGue7W51mfJGSrn1jAxOV7DiHGIp7cOY9h0IX-1Z3OVGGB4oUr0kPNXFlJVfV6eDstiQezLwasQclvNReNTOisGcUeMPzaqz0Nj_n4x5Cn2n6ZcG7VG5motvbwFM_Qf5GekLaaaMCwqiHv22AbWhSmDwe-sZMbg0Xrq6vDdvs0A4APYlZE8lWORSV7XonyLkarzZXssScfpbheBFnNhnrz9ljIJAlwqVYBPKfs8XlXd1cbazOmZ1oTf3k9r7kV0w4RPWr3U7YFiIV3XRim-SNaEHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیویورک آمریکا پس‌از بارش باران غرق شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/457730" target="_blank">📅 14:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=j683ejysHu6faYlQC07nmZzjSmCWBRK3dzLJ0EVTv2pdyaDFW0-a2zl3d_OEMFDJFR4a0jb0UVh_1KYpl9lwb-T07Q1LZqVAPwp6UZ3rjD3VBHcqzifUcGi-eqdZMm_0E65UzkyVaslbESpM9dpC6OCMEcoFKZ4PNYwN0zHQC4ROps-cdN3_-K_7e-PUNp6OoELAa3rNL2fnnKFklkpFVX3UDUq-B-z3egBcM73xXME8HkJMevT0xKCB5WaGAAxt3TacLX-sycYQ5xdHT1nXfTUvhDrOuGsj2j10rhRG6UvFGR5YR408DZ5rTdE9QSDZ1DlRUi0eKuCJb6Z6oGuT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=j683ejysHu6faYlQC07nmZzjSmCWBRK3dzLJ0EVTv2pdyaDFW0-a2zl3d_OEMFDJFR4a0jb0UVh_1KYpl9lwb-T07Q1LZqVAPwp6UZ3rjD3VBHcqzifUcGi-eqdZMm_0E65UzkyVaslbESpM9dpC6OCMEcoFKZ4PNYwN0zHQC4ROps-cdN3_-K_7e-PUNp6OoELAa3rNL2fnnKFklkpFVX3UDUq-B-z3egBcM73xXME8HkJMevT0xKCB5WaGAAxt3TacLX-sycYQ5xdHT1nXfTUvhDrOuGsj2j10rhRG6UvFGR5YR408DZ5rTdE9QSDZ1DlRUi0eKuCJb6Z6oGuT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرخوش وزیر نفت در اولین روز هفتۀ دولت
🔹
ثروت عظیمی در حوزۀ ذخایر هیدروکربنی کشف شده. این پشتوانۀ خوبی برای آیندۀ انرژی کشور است.  @Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/457729" target="_blank">📅 14:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daa67aabe.mp4?token=Z5q0E5srNgfLJp30HK5drX3Re1SFwMnoktXZL0xxlllYgBfasgYIa6Z0-7IB8bGzldI9s16Qd9PKGpzTlrEJah-BhN0NIzWLs1ZtSuChFUdzV1te085zcL0qOAzF_m0C0lumadoMmZIhq_-Omzglz6Lfr5Tw6pQowhoXPItiXj5szNW_ogQoXikTNWLU8xRg0b1SDW4yg40fhJVFCp3SyJEP1UCLxiYyMn44olZ8vCIkJtmYs09a5jOHp5HfkSwlDvynsX5f3pLpnKjT8K065EkukGFRe8Bev_BE2eaQKbGcaQoeoE9Dvrv3njdmlvIwAFdipKQZtU5XT4DFfXEfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daa67aabe.mp4?token=Z5q0E5srNgfLJp30HK5drX3Re1SFwMnoktXZL0xxlllYgBfasgYIa6Z0-7IB8bGzldI9s16Qd9PKGpzTlrEJah-BhN0NIzWLs1ZtSuChFUdzV1te085zcL0qOAzF_m0C0lumadoMmZIhq_-Omzglz6Lfr5Tw6pQowhoXPItiXj5szNW_ogQoXikTNWLU8xRg0b1SDW4yg40fhJVFCp3SyJEP1UCLxiYyMn44olZ8vCIkJtmYs09a5jOHp5HfkSwlDvynsX5f3pLpnKjT8K065EkukGFRe8Bev_BE2eaQKbGcaQoeoE9Dvrv3njdmlvIwAFdipKQZtU5XT4DFfXEfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سوال از وزرا: آیا شما از تهدیدها و محاصرۀ اقتصادی می‌ترسید؟
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/457726" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457725">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae5e0523.mp4?token=uz0pRsrc3TdLtou6vvPMSu4Jakb1uN8tWSnN58OUT3VWZABfj_b4gIHmrL7OzQyCEmz5PHXUnThk_OibOcbfpEvhgwulGKxfPqzWLAtiv0Fj5IsVp5iAXStGejDYh3oJ123mGun-gFmLVpC8MYM5nX5Tt25wALOGoCBImAGrCBmZyZO3d3eSsBOywIb2MhF4UjmHA8G0WCjhzeQDLSO8Tqj1HBqlQBock-hkmSIfl89uR5KteTl_8TP-Brl1c2BckcyKNR1uzy4ms1JW5dmRDsCveeHTLe22b7HfMsk2nYi2O-WgRjwZ8WHzK9qNCNciir7k6KXc6fW5OXRd-38T1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae5e0523.mp4?token=uz0pRsrc3TdLtou6vvPMSu4Jakb1uN8tWSnN58OUT3VWZABfj_b4gIHmrL7OzQyCEmz5PHXUnThk_OibOcbfpEvhgwulGKxfPqzWLAtiv0Fj5IsVp5iAXStGejDYh3oJ123mGun-gFmLVpC8MYM5nX5Tt25wALOGoCBImAGrCBmZyZO3d3eSsBOywIb2MhF4UjmHA8G0WCjhzeQDLSO8Tqj1HBqlQBock-hkmSIfl89uR5KteTl_8TP-Brl1c2BckcyKNR1uzy4ms1JW5dmRDsCveeHTLe22b7HfMsk2nYi2O-WgRjwZ8WHzK9qNCNciir7k6KXc6fW5OXRd-38T1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/457725" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roIvS2i2n6QL6fVfXQGMNoX7cpUsAN1L4207uWcPcsWPgKQ8WZrnZzpN7874Lx1exEWR8oYhMnrnxhZhY6nklGCDiY7rWorXDYL6wV1Ipwb_WdrNAdPHTI_NEDghKRgbcPAkSK6IxfMUI-iiqQ5IBrS8-yp9Au5fj1OndJwokM2MPjA7jcFzduA0DMWczOZleh0ORLwsSLMdKD4-4_VfwN5u87KLWOQu5FRBJ4bc8rDzArk242UPR0iyM2N9QqHWc7Jk3le2MW4c6KtEXjZFkL9z_EejesonNcXIlKhFNP_XaU0To7ZDE1qZv2Qiefcn2fQj2IVyrMyzvD-XisEeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبفای تهران: ذخایر سدهای تهران ۲۶ درصد است
🔹
ذخایر سدهای پنجگانه تهران حدود ۲۲۰ میلیون مترمکعب کمتر از شرایط ایده‌آل است و میزان ذخیره سدها که در ابتدای تابستان حدود ۳۰ درصد بود، اکنون به حدود ۲۶ درصد رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/457724" target="_blank">📅 14:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAzOxgeyUQSstqNsd_L9O7o7q-FnMmFa3QuCe6MmKXFdV3y5NCPygECKarlJ-NXG81ld6H1-c79UaZVZP8sZf5TtcHsd3GyyzG5yjnWc8Wu5eFs9hxMQ-Sozli8-3qaThlhWPonvuymvPog6keFECKEcdFyS920JCKoZO_CMs1GBZB2vQcR-dBpOE5rGL05HCMPNQOEy_lLJhy0-PQgukRtGzu9_hEy5cxXBmA38fI3Q5oKg9kSuVT4K75JRRf-Vs03iLfj2gtvI33VeHWAulzIFAKvQDRy9jYhC3KJRPmHYdM8KySMgH-CmRjDE2rrJop-4ePpQ3A-ynSBePzrd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCZoNDHlxIm7a8_rz-S7fpOhvjAh8S5Ei_wggdxjrOhI-0-7EOOa-JhXtllxPKGJ-t7fEyCphEzG7EThX2_JnoQS-y9fEU4Qe0wOqcLtSQM6oDciMxk9iz2cOZPiCQO4UgjZaOXwrEf8x7kE7cZTdun4ymKjlBF1cd5cOlaK43seZ5wLKoLsrMbfPRgAyaTYmUV7GyFvuHtGKiMVfINZd5oRFHFt5h3GdWYRqjy2-Czd9v5ruMOJPeOyVyeR_k0YicTy9pNQQ02K8hP3QaAl7QD9SF2NlllNYU5BPqx1IXl0ECRJjxySAevObt3J4CRI_2g8xvM5UVGqYb4rqEu9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhVGtTwFso3tPVoj46kE1x-Jnprk1bivqpwVMlIFqDX1zS2ppq4d6F-LtC3JkzbTu756eVS9noQkAS9pq7Xxg3eF5SmIFy2GnU5QTPAFmoKj_is8BwVWIoFYpUr3-ETo8w-pG3oMfN61jkI3yA1pata0MXlvMv1Yb5c7a8wPL4wHQ5wqLr4K6yr7NA9VFyp2NnxsE3Gcq1Z1XzjE0HPWUKcOF7AyCpu-aHMW9jPP66CEllYnxKnp4x8L-54XmfVpKhX1lWJA0AlcHceKlzwr_wV66aMOTb10-GEurlecBQ60SSMLIdg-oii4MpVyQmAQfRmIBbPkn7rYWSVR_zQosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAPRhWY5y3Nq6AlmSN-9LqSVdchWntoDLNAK0cmvCVQTXfYexkVDMVenV18va_ve_--3Yhhun--Ul_eojlvBkM6VjZX_vLBtnhedFNxmR7KX_s8zXKTrWqvduuD55h09efmvGSH25lAO-IFqQQIaIwMwAeHeQeD8rzuFROE1jMNNYhV-AUqtaGIyhg_e3mWNGQwucLKf9HhP3MuwgE8VWrDyWXI02VCFBNAh8K69-XRN6RUZxGeviyWjKM6qJzC2AzR6oAi8QwAyVa1c_IrFS7ArDgr9oz6-t6zpWi-jGh9LyMvg8eZhCJsbB5Ngp9YGI-OhTl9XEyMrHAdK4lPm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiwY17Ne3-D6FUU2Mf4kdhc1DG5cc49s4Sw5nLl3jzdcfJ_zMVRGlG8XRU4s4e2wu9kjBjv_yBkZt8zhEuNOem1a-pjy5dEbR1bU4eUMjrcI4K7MB1fWOk6f4dBVThN3UPWc7wqXm1KAgX_y--SYPLy6HwGCR1MOyblgAghBa5hzeQ-FRMH8tvJkDkjDXGYtAWshDxx-7a0yNL70_k_gpSLCpcHRj8lT0QfgnGanRWVvnpRVmeoWWNgzxeQJ-dYHO2y-EFZUFMb2DpNbnIBrsHskggu1KTcdZidd-8PTmhcWP5bvGVy8PqcMkcYDVDJp1C_7TZkHXES53O1S6l0-Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزارع کردستان زیر تیغ برداشت گندم
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/457719" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5c3ec98b.mp4?token=oFJy0uzDpvLiMR8cEQNPxgeUAOBs-vqDXggbrbuJDKWGUA80bHFCemw5M7k1f_A9yIw8-NEsxvpRuVCVwsNcpg-Q-S61YcZ3lQBJuE1tMbqH04U60UDxSGu6lXhuqhtyGBUgxg4RyLhFA33EZqnXHhnoKA6ctBz0eb_-NUuGZBX-UsiXPe2w6UfAe3GLHXajBZebfw8LFT2ZB5KK3c4C4p2OVK7HEXklxzeBIPJHKfazOAnP3vSLwe2HySmqb1kdUPO_tRJGGD6vzRWkcP0T9umraBQVOMfuVBKNsclo-CyNc8JkLOuZ04FmIyhFvl0X37HZf0-MDfqM7KFOb2M-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5c3ec98b.mp4?token=oFJy0uzDpvLiMR8cEQNPxgeUAOBs-vqDXggbrbuJDKWGUA80bHFCemw5M7k1f_A9yIw8-NEsxvpRuVCVwsNcpg-Q-S61YcZ3lQBJuE1tMbqH04U60UDxSGu6lXhuqhtyGBUgxg4RyLhFA33EZqnXHhnoKA6ctBz0eb_-NUuGZBX-UsiXPe2w6UfAe3GLHXajBZebfw8LFT2ZB5KK3c4C4p2OVK7HEXklxzeBIPJHKfazOAnP3vSLwe2HySmqb1kdUPO_tRJGGD6vzRWkcP0T9umraBQVOMfuVBKNsclo-CyNc8JkLOuZ04FmIyhFvl0X37HZf0-MDfqM7KFOb2M-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ معوقات بازنشستگان تأمین اجتماعی این هفته واریز می‌شود
🔹
پرداخت معوقات فروردین و اردیبهشت بازنشستگان تأمین اجتماعی در ماه‌های جاری به یکی از دغدغه‌های اصلی جامعهٔ بازنشستگان تبدیل شده و زمان دقیق واریز این مطالبات، بارها مورد بحث و پیگیری قرار گرفته است.…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/457718" target="_blank">📅 13:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5ab0ce19.mp4?token=OKmfH2MTWcYiicV4fWMeaGZqniT1VK35D73CzQ18hO4c94XNFtmxitwTqZH42ffezdSKbT99YgON4nd4zkJwzam3p3Ri3xHclU-CHCon9n1lQX38Bf1a-G-C9pGKFODtVfc7nVgBY7Efw2x96H_fH3HGzdDKX9Lh6d4XGu4MQ0EkXi1GN9zNqKM-hxAuauhQnuVzj7xsddvFWttMzYDtFkcxfgMxjXMDd4H31BW9q03VwYpUly1o0PU11fD-Di8F0ItQZPY8EmdJA9-I5nJFE2BPPZLpJ79IFF2-iHu4IIWFxxOFQDGEWCK8E2s123FrQJBeKSTsIqvos4PnK-p_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5ab0ce19.mp4?token=OKmfH2MTWcYiicV4fWMeaGZqniT1VK35D73CzQ18hO4c94XNFtmxitwTqZH42ffezdSKbT99YgON4nd4zkJwzam3p3Ri3xHclU-CHCon9n1lQX38Bf1a-G-C9pGKFODtVfc7nVgBY7Efw2x96H_fH3HGzdDKX9Lh6d4XGu4MQ0EkXi1GN9zNqKM-hxAuauhQnuVzj7xsddvFWttMzYDtFkcxfgMxjXMDd4H31BW9q03VwYpUly1o0PU11fD-Di8F0ItQZPY8EmdJA9-I5nJFE2BPPZLpJ79IFF2-iHu4IIWFxxOFQDGEWCK8E2s123FrQJBeKSTsIqvos4PnK-p_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرخوش وزیر نفت در اولین روز هفتۀ دولت
🔹
ثروت عظیمی در حوزۀ ذخایر هیدروکربنی کشف شده. این پشتوانۀ خوبی برای آیندۀ انرژی کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/457717" target="_blank">📅 13:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b72d321d1.mp4?token=N6jNzRY7xjKOLXTGj_arbO6_TqLluEbgAeus-M3lCE0P4E9PAfWTUQMpdfIM-KUxhUXxqH3n5f1o6WKS3n0MoGF33lRStud0v1ERyGTBZNlwEytbHAkomvEIx8EgKONIGH0sX5ht_Ltd6mQk_B6B7gF5OYaA0FMY-BMU8o5wR6ndqlU5L6WxvKDT4STWqAOSHKCWFsTNrK5QTwegzlf25hR6l979F3qEyqojym9lwlOAlVJMRCahKB3SVMMYuiQKVswkdVGiBEqulq2s_oAG5eOZSSX_Jr1S1irRbFx4wHJniu3RHT1XeV_4E2HW8nDx0f0LBoNtuVA_Bt8asBT78g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b72d321d1.mp4?token=N6jNzRY7xjKOLXTGj_arbO6_TqLluEbgAeus-M3lCE0P4E9PAfWTUQMpdfIM-KUxhUXxqH3n5f1o6WKS3n0MoGF33lRStud0v1ERyGTBZNlwEytbHAkomvEIx8EgKONIGH0sX5ht_Ltd6mQk_B6B7gF5OYaA0FMY-BMU8o5wR6ndqlU5L6WxvKDT4STWqAOSHKCWFsTNrK5QTwegzlf25hR6l979F3qEyqojym9lwlOAlVJMRCahKB3SVMMYuiQKVswkdVGiBEqulq2s_oAG5eOZSSX_Jr1S1irRbFx4wHJniu3RHT1XeV_4E2HW8nDx0f0LBoNtuVA_Bt8asBT78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی تنهٔ درختان زاگرس به گونی زغال می‌رسد
🔹
تصاویر رسیده از منطقهٔ زز و ماهرو الیگودرز، قطع درختان و تبدیل چوب آنها به زغال را نشان می‌دهد.
🔹
به‌گفتهٔ شهروندان محلی این عمل در سال‌های اخیر افزایش پیدا کرده و رسیدگی کافی به آن نمی‌شود.
🔹
کارشناسان تأکید دارند که این پوشش گیاهی در تولید اکسیژن، جذب دی‌اکسیدکربن، حفظ خاک و آب، کاهش آلودگی و تأمین زیستگاه نقش مهمی دارد و روش‌های دیگر و امکان استفاده از سوخت‌ها و مواد اولیهٔ دیگر، باید جایگزین این روش شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/457716" target="_blank">📅 13:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی: با اجرای طرح مقابله با قاچاق سوخت بیش از ۱۴ میلیون لیتر سوخت قاچاق کشف شد.
🔹
۶۱۷ نفر از متهمان و قاچاقچیان سوخت دستگیر شدند و ۴۸۹ دستگاه خودروی حامل سوخت هم توقیف شد.
🔹
در ۴ ماه ابتدای امسال ۱۲۰ میلیون لیتر سوخت قاچاق کشف کردیم و ۱۲۱۲۷…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/457715" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
رضا برکتی در برنامه سرآشپز: هوای فروشنده‌های غذا خیابانی رو داشته باشید و چرخ زندگی اونهارو بچرخونید/من در جوانی بلال میفروختم و به اون زمانم افتخار میکنم
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/457714" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8UTEuesT1IwAJFkhjG-fQg_GQZkUo-irKlLeSherZakZRXxNPyAre-__ZXDS0pTfu5H-YnEZO7HYx_yO38f8ITr37d3IW84e02EoPgz5F0N1GnBDLnYbcvtiM-rrl3Ai4TsDk5NpQKGp4dPFsGRuWTrgzJAPAaZvKox-MyZCgx5y_vgGv_5yrhW9z6DvZJD0_nuLoplz27KGf8szPftHdb-HmtBPAcqsLBYqo8I-bSB07cD1KMNQIRnhRFZGHFKxZ1uiIFcDB_GaE6zwO8HGDR4wP03C4RmzJXIEezaadXstNKsUJj5pf46TZKcnmJhqGfNVjzXOXE4kiF9dueK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک ملی ایران در جهت پایش مستمر سامانه‌ها اعلام کرد؛
خطاها و مغایرت‌های احتمالی را گزارش کنید
✅
خدمات بانک ملی ایران پس از تکمیل بخش مهمی از اقدامات فنی و تثبیت زیرساخت‌های بانکی، به شرایط پایدار و عادی بازگشته‌ است. هم‌زمان، پایش مستمر سامانه‌ها ادامه دارد و مشتریان می‌توانند در صورت مشاهده هرگونه خطا، مغایرت یا اختلال احتمالی، موضوع را از طریق لینک زیر گزارش کنند:
🔗
https://app.epoll.ir/97455750
🔗
مشروح
خبر
…
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/457713" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/457712" target="_blank">📅 13:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d07tunkLksK-xWlardTBGzXHhbLRSNviQ-nfHsjqCRfXALX3Ho3ixjNrIiLbnI_eB7jI5PNyXq9hNZnGow0noYFyIzhyRKnugUcui0bAvrDvUoAas0P5WfYUQsJUevvXF51ceVoOW5BlnoNKzATzZXos4gQmaEmB3muk5QREPtyoTIXGER619_qkttYU9eeRvaFgVLRB-tUEk2x6JpoVq26H7aAkKZWFw50y99IO8H_v-PyScOptNLMhmh-Jrq_aHSh0LBtCZrAzWYtz4p3sRmBpPkNLRuGPydwPtbLf9Yf-8c9NimRTomg4E2Pcf7rs64FkVbpwWLBXfAdZVhin8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی: با اجرای طرح مقابله با قاچاق سوخت بیش از ۱۴ میلیون لیتر سوخت قاچاق کشف شد.
🔹
۶۱۷ نفر از متهمان و قاچاقچیان سوخت دستگیر شدند و ۴۸۹ دستگاه خودروی حامل سوخت هم توقیف شد.
🔹
در ۴ ماه ابتدای امسال ۱۲۰ میلیون لیتر سوخت قاچاق کشف کردیم و ۱۲۱۲۷ پرونده برای قاچاقچیان تشکیل و ۱۰ هزار خودروی حامل سوخت توقیف شد که ارزش سوخت قاچاق کشف‌شده ۱۸ همت بود؛ البته باید گفت که سوخت به ۱۰۰ شیوه قاچاق می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/457711" target="_blank">📅 13:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بهروزآذر: طرح مصوب مجلس در خصوص مهریه، مخالف اصول قانون اساسی است
🔹
معاون رئیس‌جمهور در امور زنان: تغییرات در مهریه باید حق دو طرف یعنی زن و مرد در نظر گرفته شوند.
🔹
ما همه تلاش خود را برای بهبود این مصوبه خواهیم کرد ولی در نهایت بازیگر اصلی ما نیستیم و بار…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/457710" target="_blank">📅 13:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52364ba26.mp4?token=nyvu_TolegLAP3PwU0bDuugoPJB8oKMKrM4oHBGiTFvOxQNKEu_5IYrLLKVBROQwQayfFU1NAvNBkAkd1qA_Cgk995m2zl4d1Jz6d-IqqTTAx5lvMc_gPAIw0G8RbF_EutFjcxlWI01l6exhQfpoh6hF0YncF4QhA0TV6Ko5_QmbiPFpEuoL8w7hNxEQeDNF9Igw8SipbVVdJEEiUfefM04gN7RupNpI7k4Z-89YowpQSzGYm1zNXSgwz1lWviDgQB9Lk4oqwToSkfvZXabSApY0O4994Mn5B3NogVx3AMbehr93H0hxfxseUBMhlISripi1h_v4b0RpGokRlyVcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52364ba26.mp4?token=nyvu_TolegLAP3PwU0bDuugoPJB8oKMKrM4oHBGiTFvOxQNKEu_5IYrLLKVBROQwQayfFU1NAvNBkAkd1qA_Cgk995m2zl4d1Jz6d-IqqTTAx5lvMc_gPAIw0G8RbF_EutFjcxlWI01l6exhQfpoh6hF0YncF4QhA0TV6Ko5_QmbiPFpEuoL8w7hNxEQeDNF9Igw8SipbVVdJEEiUfefM04gN7RupNpI7k4Z-89YowpQSzGYm1zNXSgwz1lWviDgQB9Lk4oqwToSkfvZXabSApY0O4994Mn5B3NogVx3AMbehr93H0hxfxseUBMhlISripi1h_v4b0RpGokRlyVcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسرو معتضد: این خانم مسئول پوشک ترامپ است!  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/457709" target="_blank">📅 12:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBlvPbfTIhujiy6RZ_cxPT4lXAO7bOUL3tBZ4EOeIYvDU7UlJvwq1HETjY4nJxXkdgnlyMm3hv_sSstoPBtvZG4fc_jaZM5Ax_u0zVnbrRLVnNEZWFL7E08EvbHhNwjGOYhqcAbYO1WB0kPLUoN2unOLc3MiezyfUbXCt8PjmBDkSC1Ydlt-TSOOpsBfkaGT4cLIgJF3MruimafsHePMVykQzcEGx4ai4l8ahYCs3yuxyxPI52ZAjPP8h54lHF7IBq6zfqnmo4_IkYBFGKyluU7ZvKzJlkuMwtLU-2RnV2XCfv4DGQRkOd1tHy03zEAYSMUV2DsXl3WoeLWgWYQwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۸ هزار واحدی به ۶ میلیون و ۷۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/457708" target="_blank">📅 12:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457706">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c02276ea6.mp4?token=oW_avWHJboHV2dpH2rkGuzLY9rnXQHSRmFJqOW_D8LWIGlIssAaMP66O5VjhHqS3Tp3Dx5DE-ilcP3JqsS6bDIhxnik7ZAJBkgmGBOAI5LOtMztkOw1KTe4_vvGhtzO0dLvaoQ3yaxDwJU8yIwdkRBBGAa_3H6-JfhdVHBOCLbccYAFe8Ny0hHAtA30H4lF4QeCwK7uGzXep9-aWbsPv-i1iQVGYHuvie69MbvYrqSX_dZchX7WOtFBgkRLqSqjy-2npFhiE7wfVHRxDoqOK075Tv8BjAoS7y0wRL8Bs7QoIfHVwsZ0GQkEAm3aBR1e3S3w1ZcFqENWBwjUrcVcALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c02276ea6.mp4?token=oW_avWHJboHV2dpH2rkGuzLY9rnXQHSRmFJqOW_D8LWIGlIssAaMP66O5VjhHqS3Tp3Dx5DE-ilcP3JqsS6bDIhxnik7ZAJBkgmGBOAI5LOtMztkOw1KTe4_vvGhtzO0dLvaoQ3yaxDwJU8yIwdkRBBGAa_3H6-JfhdVHBOCLbccYAFe8Ny0hHAtA30H4lF4QeCwK7uGzXep9-aWbsPv-i1iQVGYHuvie69MbvYrqSX_dZchX7WOtFBgkRLqSqjy-2npFhiE7wfVHRxDoqOK075Tv8BjAoS7y0wRL8Bs7QoIfHVwsZ0GQkEAm3aBR1e3S3w1ZcFqENWBwjUrcVcALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در نوادا از کنترل خارج شد
🔹
آتش‌سوزی گسترده‌ای موسوم به «هاوک» که در ایالت نوادای آمریکا شعله‌ور شده، تا ساعاتی پیش بیش از‌ریال هزار هکتار را سوزانده و همچنان در حال گسترش است.
🔹
در پی گسترش این آتش‌سوزی که وسعت آن در کمتر از ۲۴ ساعت حدودا ۴ برابر شده، به هزاران نفر دستور داده شد فوراً خانه‌های خود را ترک کنند.
🔹
فرماندار جمهوری‌خواه ایالت نوادا با اعلام وضعیت اضطراری در شهرستان «واشو» تصریح کرد که این آتش‌سوزی «به سرعت در حال گسترش است و خانه‌ها و سازه‌های مسکونی را تهدید می‌کند».
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/457706" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457705">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTxlRyCzn8-l-7Nma_JirqpnIG8S2hd46fi5AOdx7mGIfa3cEQJE4cwVTmMl_8yxqC04X1kYObXRcTdXhOIGQs3OaYXJDTvzjRuDvp582aqLu4w14wR91dahq547TjwxJjbRo6V6g8JbcEYyD_xkgppe9ztsWYJcOC9jxsh7sa0AgibMa7uS-ZlByqn99S0CE7jfK7LSqrV7UewGD3qy2ZIAdgG1QJuvK1FAdXhKiM7PJ5EWA5vLVO9IxA5-M8FZf7yLsNiyldCDerWJkSxYXpIi7-YJNFV3vq6o5UShzdrAA8ahO_1AWHjdLRJacfdFb7yckc1XCqhg-lW43KQU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت عربستان از رونق افتاد
🔹
براساس رصدها، امروز تنها یک نفت‌کش فوق‌بزرگ درحال بارگیری محموله‌های نفتی در بندر ینبع است و چندین کشتی کوچک‌تر در اسکله‌های متعلق به شرکت آرامکو مستقر شده‌اند.
🔹
این کاهش درحالی ثبت شده که  تاسیسات و نفتکش‌های عربستان در ماه‌ اخیر بارها هدف حملات یمن قرار گرفته و ریاض ممکن است نفت را به‌جای صادرات، به‌مصرف داخلی و پالایشگاه‌ها اختصاص داده باشد.
🔹
بلومبرگ دراین‌باره گفت حملات به تأسیسات نفتی عربستان و تغییر مسیر نفت به مصرف داخلی، چالش‌های پیش روی ریاض را در منطقه نمایان کرده است.
🔹
به‌گزارش بلومبرگ، مجموع صادرات نفت خام و فرآورده‌ای نفتی از دریای سرخ درپی تنش‌های منطقه با کاهش ۲ میلیونی به ۴ میلیون بشکه در روز رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/457705" target="_blank">📅 12:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457704">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIdswMqa0ipKi-wHVTVh7S-_-s27eDqmQ3Ku5Z7n84G0pRQSyy_lKaXI8QmkXHtdj22dVuUMLfzJ1gOZ0C25bK-K6Q3YMWBek_HQdIBd6YvpxIZWlCzw3DC7T6B5ctkTuj6jUSTcCT91DP-yjSKaBdK_CrrWlZA8yYay3IjFPPelXlNzqdErMVx3kh8w6ZEnamATVnmuAi6CsvDYB67WyZyRQXnEDWCMVtOJgxqJGvM3dvAFE9wIiGSO8vuuGUpZQUGfbLRgGVDi_xv3wKfULLfmGLZzHb0N7DC6lbXR_BiTtzD0jDJDuKgt9vdxfBLX04g9Mqa8fikPJOFbhjZhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: فلسطین آرمانی زنده و تغییرناپذیر است
🔹
فرمانده نیروی قدس سپاه: آرمان فلسطین، از بحر تا نهر، بیش‌از هر زمان دیگری زنده و دست‌یافتنی است.
🔹
توسعهٔ شهرک‌سازی و جنایات صهیونیست‌ها، تلاشی برای فرار از بحران و بن‌بست عمیق نظامی، امنیتی، سیاسی و اجتماعی در سرزمین‌های اشغالی است و نمی‌تواند شکست‌های راهبردی آنان از ۷ اکتبر تاکنون را پنهان کند.
🔹
فلسطین آرمانی زنده و تغییرناپذیر است؛ آرمانی که به‌یاری خدا تا تحقق پیروزی حق پابرجا خواهد ماند.
عکس: اکبر توکلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/457704" target="_blank">📅 12:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457703">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adca269943.mp4?token=rFOPl_kK3cYR6DBmGrgRgVPmVwZYBeBpVqrrQx5fNhCyiXlKWQNmRJJ0wTTmuqUgmc3fzXQUTss66zxU7smIcBU0NkFPlZg0sW52vfMG2WObmYn14tEntPfn9sWOT2fA_ZrAAby7cbCyb0tvqyn7_qsp8agXtsZsLbIa0YpR6pKWu1J91Ew4wh9XCLTdisHqIPKWL0JRiML9hFdwWTVCvR22nMvqD2Io3Cq4MJS91k9tRxjswrt010Eo0yhM8V6s9ZHNUZv_DOR9SeGYQbzrfSrr4cWpqGTQRE3bgqLDjqyXUyTK17H_Y3b1D-wW0DcyE2oZo3FZ92lKzWwzNb50eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adca269943.mp4?token=rFOPl_kK3cYR6DBmGrgRgVPmVwZYBeBpVqrrQx5fNhCyiXlKWQNmRJJ0wTTmuqUgmc3fzXQUTss66zxU7smIcBU0NkFPlZg0sW52vfMG2WObmYn14tEntPfn9sWOT2fA_ZrAAby7cbCyb0tvqyn7_qsp8agXtsZsLbIa0YpR6pKWu1J91Ew4wh9XCLTdisHqIPKWL0JRiML9hFdwWTVCvR22nMvqD2Io3Cq4MJS91k9tRxjswrt010Eo0yhM8V6s9ZHNUZv_DOR9SeGYQbzrfSrr4cWpqGTQRE3bgqLDjqyXUyTK17H_Y3b1D-wW0DcyE2oZo3FZ92lKzWwzNb50eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران چگونه در جنگ شبکۀ فرماندهی آمریکا را مختل کرد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/457703" target="_blank">📅 11:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457702">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762f3b7b45.mp4?token=KWdSZruTb0u9XKM3x_oBeVrUx2eidytc_07h_LhYDxY1hJHTVb5AkXgEJLsNgv32Ghtj_DGkLztkWrvwAzAzuO9lfAT6iVJz1o4T2jW1MmyGkgSPg8UZ8WX7tZKn-rAmiXVbjIcqYJoVPIiIPZMoyRPmEvy3mJMscL31qiM-CaUIdFwnAaedCEP7hT6t8O1SG5S8oYGN6eL1OGsMPirYyjlED1AU7HlIYERgMPy4hlD0V91co6OhkK6FYXY0CB3ZHq49L8Fqv4ixbyYzAMKcJzclhWzZtVGETOpRAWiGpHZqZcldgwYARDXsryvvcMYKzYySChCosPm5nTjPDC1r4iV6wKKkHgDYid5tqthQBGz9Urkyqpn8kLVTjbnrD37wsRbP60XatidgHmNHwDVmi7ZgjD5THmiSyJ8z_YCgJ7hEzaoV4ZfZs77s_F5bg1VIqxmExXPS855sAjZI-upM096x3AsWKqLpOnqeLIyuIULYsmNnHrFHm8q14qA_9yZVSyYPb31HOUybSdqzZ65lTnYvICrae0zZAO3-y27Tgp3KSxkGufRlKSa_aawHJ0Q3k9Y25zShk7P6f1RSAvxzSmTNV0PsrQkZjKRgFuFUFOvJi8I1g5skUlyTxDhfH-OTf6V17SpFl8GYX3mTLOm-i6Z5-Kz2leCX-0_WtMrxpAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762f3b7b45.mp4?token=KWdSZruTb0u9XKM3x_oBeVrUx2eidytc_07h_LhYDxY1hJHTVb5AkXgEJLsNgv32Ghtj_DGkLztkWrvwAzAzuO9lfAT6iVJz1o4T2jW1MmyGkgSPg8UZ8WX7tZKn-rAmiXVbjIcqYJoVPIiIPZMoyRPmEvy3mJMscL31qiM-CaUIdFwnAaedCEP7hT6t8O1SG5S8oYGN6eL1OGsMPirYyjlED1AU7HlIYERgMPy4hlD0V91co6OhkK6FYXY0CB3ZHq49L8Fqv4ixbyYzAMKcJzclhWzZtVGETOpRAWiGpHZqZcldgwYARDXsryvvcMYKzYySChCosPm5nTjPDC1r4iV6wKKkHgDYid5tqthQBGz9Urkyqpn8kLVTjbnrD37wsRbP60XatidgHmNHwDVmi7ZgjD5THmiSyJ8z_YCgJ7hEzaoV4ZfZs77s_F5bg1VIqxmExXPS855sAjZI-upM096x3AsWKqLpOnqeLIyuIULYsmNnHrFHm8q14qA_9yZVSyYPb31HOUybSdqzZ65lTnYvICrae0zZAO3-y27Tgp3KSxkGufRlKSa_aawHJ0Q3k9Y25zShk7P6f1RSAvxzSmTNV0PsrQkZjKRgFuFUFOvJi8I1g5skUlyTxDhfH-OTf6V17SpFl8GYX3mTLOm-i6Z5-Kz2leCX-0_WtMrxpAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلخ‌ترین صحنه‌هایی که امدادگران در جنگ رمضان دیدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/457702" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457701">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka0u9RiQ553SkDQ2NrxXbDS6SyfK8abmwgL_5qc6ntMkPqpDB5icYwOzpYWguIG1YwhGn-r8qrOWN18y7ADySCLJEumuSLh7M6-vTf79gj_0WXMsd3UpyK-QbcA9ZT22sBY_RXhEcGdqvRT7OTOmUuErEECTjXbSDFMiXjPTl3GyXRlF2wYvO9XTngvWCJNCVMvNlkw0VxQqYX-JZZHTT0L8zhqvaVhs7GXSaI2MkzCUc_mSOKTnEx8Ee5reLzTr3KeVTcg_BJ1pGoZvhsVLf9_fZR2irYhe1sHUegcrriZtUKDaBLuh_Yh06cnbfmvH9Lh1OOGqQQb7SOgFjn-pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: رشادت‌های کادردرمان در حافظۀ تاریخی ملت ایران جاودانه شده
🔹
پیام رئیس ستادکل نیروهای مسلح به‌مناسبت روز پزشک: تاریخ پرشکوه این سرزمین، همواره آکنده از رشادت‌ها و فداکاری‌های بی‌نظیر این قشر است.
🔹
از حضور مشتاقانه و آگاهانه در قالب گروه‌های اضطراری و بیمارستان‌های صحرایی در دوران هشت سال دفاع مقدس، تا نقش‌آفرینی جهادی و شبانه‌روزی در طوفان سهمگین همه‌گیری کرونا و نیز حضور عالمانه و داوطلبانه در مراکز درمانی برای مداوای مجروحان و مصدومان نبردهای اخیر که همگی در حافظه تاریخی ملت ایران جاودانه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/457701" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457700">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwuckm9CXij0bZIESFAeISLinuHA2ua2D-jvahj1hDA24TV8lLgFH632Bw1x7uIuRtEOjIe9Fw5jmEdarNAA4unZmENt0jTUTxc4TSTIJK-7sCInmu__-Zujy8vALfAE61CBRWDupVgYNgpHGfqDmdgBMO_Kc8e-lXaYQns05qR5gQifeZs0kBL4OKaph-hm08-_quNZPccCTJwUFz99m6CTfiLboaXSY3whg689U_yQddSXjLQqAGZ4k-DH2wjSxVqRDeUto1yiUzCERMqN_LJd7JiVKM3in_wWu9daLiJ3DuUa3gg31-XA3gb1_m5kzNEZRQ4UpD1HRjkvK_QyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز ثبت سفارش واردات گوشت از امروز
🔹
با اعلام وزارت کشاورزی ثبت سفارش وارد گوشت گرم و منجمد از امروز آغاز شده و متقاضیان از طریق
سامانهٔ جامع تجارت
می‌توانند درخواست خود را ثبت کنند.
🔸
درحال‌حاضر قیمت گوشت در بازار از کیلویی یک میلیون و ۷۰۰ تومان تا ۲ میلیون تومان است؛ درپی بالارفتن قیمت‌ها سرانهٔ مصرف نیز از ۱۲ کیلو به ۶ کیلو کاهش پیدا کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/457700" target="_blank">📅 11:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457699">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت خارجه: عاصم منیر فردا به تهران سفر می‌کند
🔹
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/457699" target="_blank">📅 10:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457698">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7vrl4jhJERF540QVk3oxY0nd2Ey1WR2q7qioWNA401oOjo7jkiZsdlJljtrQcLQ7sP9oMIkxRaJhdVu3hr_GK0IIRni0-v-KA24MQaaqDnTXyJceoC_ueZGnXJU4-mvjCjYWw1DeETqrOc67nUGxF5InxPordL7eg4K5voV-MWDz4sgMhQjL07InwCGWUp_Pn7UdJ0wPjaWL0e_uNi6PuDosdTGYmsJwtIhsFEVxoO9CpBH_AKciKNq2aT02ODL4YJxvIBqyIxBqfR_exarit1z6qWyAMQBpJa8sP8aqSDT06CFX99TGe8rTNvddgzPf00BHsnIcgA8vl6niMgTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ایران به ستون فقرات حضور نظامی آمریکا
🔹
روزنامه انگلیسی «فایننشال‌تایمز» گزارش کرد که برای نزدیک به چهار دهه، زنجیره‌ای از پایگاه‌های عظیم نظامی، ستون فقرات حضور آمریکا در خاورمیانه بود؛ اما شش ماه جنگ با ایران کافی بود تا نشان دهد که این معماری به ظاهر مستحکم، تا چه اندازه آسیب‌پذیر است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/457698" target="_blank">📅 10:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457697">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRpcdIRXvTwzM3krcB1FWOmN4UQInLBu_uAtndVB7sjy92iiYDuxRknw9beE2JnBs03ZTu8CP8wFWuohaFBMmQXTlRgVWGAuQtEdNOU2OndeutjpjyZ1lKkBnAv4TAZMaM2uNzJTWYZHA7HDYWLW2InuFksEwO5_gXCeV2qAgMn2o5k9big7fBqEcTbGtVYi9x0xnGG9zQiEJKRRYgWbti7xMjXDmSprRbBPE1eDIm7R_M80sOG2J8A6h5YJTMs_Uir-ih_RM2YtYTfkCTnyMvw0_HsY2lE8ACojVU_SJehd7x-mc8soM_w99j0ExowEWYmk1HZnymg26W9PCTFReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرغ‌های تاریخ‌منقضی به بازار تهران نرسیدند
🔹
دامپزشکی استان تهران: حدود ۳ هزار تُن مرغ تاریخ مصرف گذشته شناسایی شد که پس‌از بررسی و آزمایش، مشخص شد حدود ۶۰۰ تُن سالم و حدود ۲ هزار و ۴۰۰ تُن تاریخ‌منقضی بوده است.
🔹
بخشی‌از فرآورده‌هایی که قابلیت مصرف خوراکی نداشته باشند، مطابق ضوابط به پودر گوشت تبدیل می‌شوند و بخشی دیگر نیز در صورت برخورداری از شرایط بهداشتی و سلامت، برای مصارف عمده و صنعتی مورد استفاده قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/457697" target="_blank">📅 10:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دستگیری ۸ نفر درپی فساد مالی در آموزش‌وپرورش رباط‌کریم
🔹
دادستان عمومی رباط‌کریم: ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس شهرستان بازداشت شده‌اند.
🔹
اتهامات مطرح‌شده در این پرونده عمدتاً مربوط به تخلفات مالی، از جمله اختلاس در وجوه مرتبط با مدارس، فاکتورهای غیرقانونی و تخلفات احتمالی در قراردادهای خدماتی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/457696" target="_blank">📅 10:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de0d4f81c.mp4?token=py6ekz7DuqqTshSJHF2mXiJWsi2J4tJa0OcI8JZEWY0u6w1kwqIwjEiaGmJrDR8RGSkLw9H37nwppvFJkctUfSb051zy-wVC4XTJR5ZF64myfT7QKfrTcrsxSRk1b4o5trDUub20iW5-bdViNL1ZbhUe9huQ4v5S0sbIXXNMIUfUtBtydE3KslBDM273W8BGy5rAhxjjdzXCVy37Hx-r_5hM-FMdKR_zG1N8LpdeXNPXiKpwehg1mKZq1MNCLDGcrOosWQwt_yGRQDUfKiZk4rLFUqPffq1sDeEEUeUNxxBLL2EJGy0imUyycPLKFYD4xeMjBhD3snOkeVMt7p0YWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de0d4f81c.mp4?token=py6ekz7DuqqTshSJHF2mXiJWsi2J4tJa0OcI8JZEWY0u6w1kwqIwjEiaGmJrDR8RGSkLw9H37nwppvFJkctUfSb051zy-wVC4XTJR5ZF64myfT7QKfrTcrsxSRk1b4o5trDUub20iW5-bdViNL1ZbhUe9huQ4v5S0sbIXXNMIUfUtBtydE3KslBDM273W8BGy5rAhxjjdzXCVy37Hx-r_5hM-FMdKR_zG1N8LpdeXNPXiKpwehg1mKZq1MNCLDGcrOosWQwt_yGRQDUfKiZk4rLFUqPffq1sDeEEUeUNxxBLL2EJGy0imUyycPLKFYD4xeMjBhD3snOkeVMt7p0YWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من آمریکا را به باتلاق کشاندم و حالا زمان مرگم رسیده...
🔸
پویانمایی به‌سبک ماین‌کرفت از باتلاق خودساختهٔ ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/457695" target="_blank">📅 10:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd6b195c6.mp4?token=ddBEgeAQmdoyxY57fc5OQHuQBTjchRbs75HUPaYgImnQivRsMLr4P62Tghlnrtq2vp_Ae0QM3bgkeLP1O32FEPy_hflTAsXNmNEe8zqJvRQ7z88hV3CCYBAlXTaG8eT_G6xwj3w7auM5pC37yQaWfhRVmR7BkzKuasXomHTedG61NqfLuGX2ebFyk1EXwtXeuE411kMS63eslXKr_VS8oAtbWJwDwFW32Znl2SGHGw6Dh7UiwO6wsfIHgYl6dE966FcwqiHsq7opy3poVh5yvT8Ns9c2Up0cvGgfkev1W_clYqmWs6_Mgk5SX1oYEGtKsa4V0UN02jpYU0lYt0h0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd6b195c6.mp4?token=ddBEgeAQmdoyxY57fc5OQHuQBTjchRbs75HUPaYgImnQivRsMLr4P62Tghlnrtq2vp_Ae0QM3bgkeLP1O32FEPy_hflTAsXNmNEe8zqJvRQ7z88hV3CCYBAlXTaG8eT_G6xwj3w7auM5pC37yQaWfhRVmR7BkzKuasXomHTedG61NqfLuGX2ebFyk1EXwtXeuE411kMS63eslXKr_VS8oAtbWJwDwFW32Znl2SGHGw6Dh7UiwO6wsfIHgYl6dE966FcwqiHsq7opy3poVh5yvT8Ns9c2Up0cvGgfkev1W_clYqmWs6_Mgk5SX1oYEGtKsa4V0UN02jpYU0lYt0h0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرطان‌شناس برجستۀ ایرانی: بعداز اتمام جنگ تحمیلی ۸ ساله، مرحوم هاشمی‌رفسنجانی گفت آدم‌های جنگی و جبهه‌ای دیگر کنار بروند؛ وقت سازندگی است
🔹
پروفسور اکبری: بنده در زمان جنگ تحمیلی ۸ ساله، مسئول دانشگاه و بهداری بودم، ۱۰۰۰ روز در جبهه حضور داشتم. همیشه ساختارهای سیاسی زورشان به ساختارهای خدماتیِ صادق می‌چربد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/457694" target="_blank">📅 10:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4P2pYjmnpjQSZqw8rD5fBJbM2f2o9obvzYkX4YUyQtTk6DFVwyODTGsnuRrGqDe6E-GsPxPorh3y8IbKy65JKITUmi_TMcymTlr2vYsgJ42qrLzBbc0N6Ao3PVaUn_iuALEEJPo68f5ndwzqrddutMydWApyMrmudA1vit8jaRueFzTif0goIB_b0ZKknNX3nU4wHtUh8txO3g-vBLc3ITj7ovQxi54wubz8uP4I7It-kN0uelf56P9JtqksHpsiSGu0o62rFepxsnPS6Vkp7M03x37sqbtcrA8Mar-OVEmrjAOFLnvuCPe70HO7JIr4ALK-M5c-olnXjA57mHJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO3MzwOAtQMFIAIaEkC8gLcMSfh7z4h2ql_-KH8S9wUKbSoZIbyGUUu7QHSq8bEnGPgvUitZ4yDzW2u0QqkDtY729CLEozlWmNDxVEvLA2zAdjgloJUbU4kt6VdH0c1-Y_Kcq4FOjbdmpCUDzaV7ZutO237l3aeSyAxXd1q-fdiMaNC-T6YG-xtUYkaLAOqEsB73o2uXi-cOA7HzuxJhM1VXmor17f5XnyiTGkLu9ABp5URIBtdsNoGGDwN7MKkK7H5KaeiyGSS3qLU_77BDG9lt4acYeg_mSVA8N-70bTKK8AAE9iKpxoNsAJL9253Ueiy3UxUFML3a1lhSvAySlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHktnhSDIPJs-0fxY5Ofb2SmndO3mEk1csCFVtzQngV97oz68y3NSvjlnvn3YvpnhyFM2lnhRE_gcrki35j-br3qEGJbO7xW_K959rJM21p-43I6LIgBPhsrBkKzi5L-UcmkXKZtyDI2S_e31tAJ-7QyOJLTTWnfCBEIPlYVbJI7VvYoKc2x2KptosYENAziS_2VSg0pFe5QxJUKau_EQr-opLi-eIfkEcv3XnRADibyWOG9tPTOxZPdJMLSgAZeCYyFvWOKl3jCLL-HIgu7PZOMadlpLRGepGRRKVEIDtgN7lNrxFPqEfqGbYsYB9O_dYj4JEQdrOigWVF1eQua9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNapineyVPnQjEmntEf3EtJlGwG57joflqwRMB0PPSMxahwCOnsxeFRqyfJf6X9cXDNhcnEC8SbFIl9W6X0wuWUmdmYamwbxDRsE2uSvqn7Vr79wVN94QpfL9sM9QJOnj-a6vtTwrDttERmBs_YFa4f72JnAxL4ZppqtwxfKnjuCaCbJ0HZu8Bd_Y9Q2O1JhcrKFBQgwEScstraISUX4VUtyQBb00kxFOxG-vWm7I9UBxA171B35PCEOV2mqycYemzqwZKZL8dwHt7vEwqd0spXYhNTtHdvCHiBQY5rfxXr0vK4GkFmTOiSrfjyLqOpp6H95K5BK7hubYkpFG9_C_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5tX5AmbEGI2o20tPALU3qLTmpF_SOxEt-Ro8LSUFJIVvj9FiS5zuNbzAAILMzToQgGmli4tpvoUU0MY0dtFkKsGTuUpBkOjUGRQziCGugzUHlnKibRwxxov42OqSV5eYZnRLWoQ6HrhjDpr3U5xuExxzbURdwf-RQHx_oiZZM7seIy-6ofO4jKW3fENUQ2r63iw6gAkmPciSN9cNwV451gHLVkhX95n6JzeDS8YLgwOaq77Obz8UusiCz9Ix2OvZ2CiBRaNowWhng-ZXjI5q2M-k2itslNE0gGz3YVM5QuiOCeDhvtNm9-Hvx8MkFCDSxkp91TjqNkgMOvcUeM-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUAXakjszbfwd0Gbjh9lPjHFlZCoTzFMC7QOZqVJdqLEAeflF2wix_mUKDWr3FDZd3LOPsWLUtV6eFS2c_shpuH6MPFR8HwqukDjSls5oQlmEKox9Po9DwjBEkiiMnyreE3NGVp38aMYW-KqalH4bJYFVEGxb-HBIxCYyapneiKCZmF7aGOaPR4e3sn_I_4YzduxoHaEKlYVKYnVs0nZMzQuG1QTNaqtWPXlndF-7-Vf0vwPzPZy1gCJGOvds4rmRbwdbTgUZxar1YAw2duiCuvaFii7WhFpdrU2KFYne4nc-BBgJVpnRiLppnM5HhhlorXYAEc1ubx9PpQ9JQ5c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSEuDFfXVAEjIHWallX--_ne4nr_g1QsSyzdJmsoVyaFz-IlYWKbHfL8e9L8oVWhawkDQoXYMQBnR9a9uSL_OxgjaIeOycAl5FodQt98tvHuFto_RuGQLFM86jsJHpKULQ100W9-bn04dJO2PyGI_rRN3n0Lb0ta8F-6SuCI2gY2jh3OcAQ8TOX4prK37EeTqcBTqzZBhDjcQ2z--QR3Cy15cqiuw7SRw9Zx4bCdoerIp9iXt_7bZm6Ilx3fl-Of88VbPaJm-KBeqYrYRpXDKJPGaxnOZ8u9fSBMOcWjMYY4xOpVQ4LZa9eHK7UaySaTEQszeXBR5Q_4m61ta8lg8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت بوعلی سینا در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/457686" target="_blank">📅 09:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4880804d1.mp4?token=flZa0Ud4RaxOs701F8CVWVOnBqAJzVmAio9h8mx_yK7sI33X5yAUc0z4hZGxX3Ba36ISadgxanMeKMWuiNyjJs705ClnE0V3gmTwvHjf0aHp4o4OnxBV-i2Da8Y16Jf3mTxnbnMOkDWG6KToxSHZM8XdsIr9vgvELIqtrrtW90ES7BGzNPcanFv-1X1Zulu0W1qfYhM9ZqEmobhhGKkQr-ZxoPncHfVqFFebR-tCXRLSsf3Apoq2dRdvusUU3SOTCVW5hsR-ZDIJ8tDD4Arpy0MoLeC5kWKwyV4QH6QU_1rJspKNwglhM80yRfeQ8Oi3iQ4jjLImE2uSXr9EtB-BTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4880804d1.mp4?token=flZa0Ud4RaxOs701F8CVWVOnBqAJzVmAio9h8mx_yK7sI33X5yAUc0z4hZGxX3Ba36ISadgxanMeKMWuiNyjJs705ClnE0V3gmTwvHjf0aHp4o4OnxBV-i2Da8Y16Jf3mTxnbnMOkDWG6KToxSHZM8XdsIr9vgvELIqtrrtW90ES7BGzNPcanFv-1X1Zulu0W1qfYhM9ZqEmobhhGKkQr-ZxoPncHfVqFFebR-tCXRLSsf3Apoq2dRdvusUU3SOTCVW5hsR-ZDIJ8tDD4Arpy0MoLeC5kWKwyV4QH6QU_1rJspKNwglhM80yRfeQ8Oi3iQ4jjLImE2uSXr9EtB-BTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشک ایرانی نسخۀ جدید درمان سرطان در جهان را نوشت
🔹
پروفسور محمد اسماعیل اکبری، سرطان شناس برجستۀ ایرانی: ما در سال ۲۰۲۴ میلادی، برای اولین‌بار در دنیا، یک روش جدید تشخیصی و درمانی برای سرطان‌های پیشرفته و متاستاتیک (جامد) معرفی کردیم که سابقه‌ای در جهان…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/457685" target="_blank">📅 09:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948f9ff060.mp4?token=owVFg8KbWk7Kk8XK9GJbpAHDS1DzEbD0SO-JThTyzzCqq2RhdKscDN0c8RE3BudlnYxsqEoskzryJt16InmVjyT2FF1h3UYwWRLqgtaC8V58Luxc3-73-eHH_8Gzyuk_PcckCOZzWkItieyu7wxk4ernzXmtgAtI_JrcYNwHzEG0RdWK8yqoataVEe5KoCbAVf7TUqZWyZW60HdWvueg3FKhzWOVEA5U9UGJouKBzYRs2a08ZHGDDi2TpqOSuBKc_sBuF38QER7zx0J4R8KfUIYU_Rx5FHWmF2MXpSI1nHTQhE2vkNpuhN-rYZxtN4j6EVruQz07ZBdOYoLR57Kjdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948f9ff060.mp4?token=owVFg8KbWk7Kk8XK9GJbpAHDS1DzEbD0SO-JThTyzzCqq2RhdKscDN0c8RE3BudlnYxsqEoskzryJt16InmVjyT2FF1h3UYwWRLqgtaC8V58Luxc3-73-eHH_8Gzyuk_PcckCOZzWkItieyu7wxk4ernzXmtgAtI_JrcYNwHzEG0RdWK8yqoataVEe5KoCbAVf7TUqZWyZW60HdWvueg3FKhzWOVEA5U9UGJouKBzYRs2a08ZHGDDi2TpqOSuBKc_sBuF38QER7zx0J4R8KfUIYU_Rx5FHWmF2MXpSI1nHTQhE2vkNpuhN-rYZxtN4j6EVruQz07ZBdOYoLR57Kjdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشک ایرانی نسخۀ جدید درمان سرطان در جهان را نوشت
🔹
پروفسور محمد اسماعیل اکبری، سرطان شناس برجستۀ ایرانی: ما در سال ۲۰۲۴ میلادی، برای اولین‌بار در دنیا، یک روش جدید تشخیصی و درمانی برای سرطان‌های پیشرفته و متاستاتیک (جامد) معرفی کردیم که سابقه‌ای در جهان ندارد؛ یعنی اولین‌بار ایران یک تکنیک درمانی سرطان را مطرح کرده است.
🔹
ما پروتئینی به‌نام FAP را که توسط سلول‌های اطراف تومور ترشح می‌شد، هدف قرار دادیم. آنتی‌بادی مهارکننده‌ آن (FAPI) را ساختیم و با استفاده از یک رادیوایزوتوپ اختصاصی (روتیشیوم-۲۲۶۸) که توسط سازمان انرژی اتمی ساخته شد، دارویی تولید کردیم که دقیقاً به بافت اطراف تومور می‌رود و از درون، سلول‌های سرطانی را منهدم می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/457684" target="_blank">📅 09:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/457683" target="_blank">📅 09:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYsFbDUAuwI_Fs3zXY7rg_kpwU9lwdnJGTUnMLy8-4R0gG94PbLzgqQ73VRfXIJrBsLyXMHBG_vL1OhJGF30TUmHHT4gte8O-9Yi9SEU14OarDhoER63s29XlZq1HkqVpPq-SyDy3g3cC2Lzktpc4DXiw0boBIqnv7tes9Ia0RCNrawPFjr0ojU3nyGXnvDL_okZcEPsmaGP1xQE5PHBxr9ikftesuRmy78uwLKhvr2FI_O2tyc27ZrxTRCGn5lFM_Pvd-jjnhKqwkhUtvxo78w4iECtL0MVoEvJomMA39-AVe8LptD6qpcP1soIFS2_AUjZ-QBSmclzNyUd1_Iclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵ سلاح و ۹ کبک شکارشده در فارس
🔹
حفاظت محیط‌زیست سرچهان: ۲ سلاح غیرمجاز، ۳ سلاح مجاز و ۹ کبک وحشی شکارشده در جریان پایش شهرستان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/457682" target="_blank">📅 09:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=VLMMWcoTMsEw0_rgkSk-1-5OPJ05oy9wK0HFw1AYm9GEHy6zeZ31JU69n02dFFQp5-m_vtqI8IM6ZveS7DC3KXPPcIJzJg43PnABN1vAS10fixRjbn8cIFt-mLx_8w-0oar1V8vk73Kz8sg_WP3OOI_K6Nh_6UZne85ChNQh0u5fu-zsu1e6T9YkpVc01HIddQ82jbx_YMALxHCg6AGS89GtW7D_FKiwXTY3A2NJW7s4hkm_s4-5HFnYoPHKL6k8dNqba5GJ0nq81BoweKCt59hFL6_GWAXngUK8_7NGvhDWtSTADm4-3cla4sBDUO2iMu0RMg7ox7OjtwpCbgHrfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=VLMMWcoTMsEw0_rgkSk-1-5OPJ05oy9wK0HFw1AYm9GEHy6zeZ31JU69n02dFFQp5-m_vtqI8IM6ZveS7DC3KXPPcIJzJg43PnABN1vAS10fixRjbn8cIFt-mLx_8w-0oar1V8vk73Kz8sg_WP3OOI_K6Nh_6UZne85ChNQh0u5fu-zsu1e6T9YkpVc01HIddQ82jbx_YMALxHCg6AGS89GtW7D_FKiwXTY3A2NJW7s4hkm_s4-5HFnYoPHKL6k8dNqba5GJ0nq81BoweKCt59hFL6_GWAXngUK8_7NGvhDWtSTADm4-3cla4sBDUO2iMu0RMg7ox7OjtwpCbgHrfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من می‌فهمم الان در جامعه مشکلات زیادی داریم
🔹
با تمام وجود به‌دنبال این هستیم که تورم، مسائل و مشکلات معیشت، شغل و آینده مردم را به‌سوی عزت و سربلندی ببریم.
🔹
من می‌فهمم اکنون در جامعه مشکلات زیادی داریم. ما تلاش می‌کنیم تا جایی که می‌توانیم از…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/457681" target="_blank">📅 08:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f576d82.mp4?token=RMDX4p9akX4ARFV56IN1s0PRQail79y7UR9VBQWNbdgzcprHrjSyJRmXCCcakSNhdi3xregULS_xtIDa9izGF_7JhV7GOVvyTjkHoSI62hTf3bXEpRWqjl-4O041dgVzA8EnTU-jJins0F1yoBxT0NnjMz4xgJAtw6rfrMy806gH-8zSq0bVELeFQtdg_rJWicbdbMYZ0mMRtkkUZK4wrBYILT4peuV0H5J3m8YRGd_YaDtKpy2d6VrKd9LrfzWD98sWSJxeRGhgOshGufLJTNgaWoGNWm1mSfOIHAU96yQl-x_hX64CRIWITOF6V4gwAsyNc8UGP2MR0cpnnhpfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f576d82.mp4?token=RMDX4p9akX4ARFV56IN1s0PRQail79y7UR9VBQWNbdgzcprHrjSyJRmXCCcakSNhdi3xregULS_xtIDa9izGF_7JhV7GOVvyTjkHoSI62hTf3bXEpRWqjl-4O041dgVzA8EnTU-jJins0F1yoBxT0NnjMz4xgJAtw6rfrMy806gH-8zSq0bVELeFQtdg_rJWicbdbMYZ0mMRtkkUZK4wrBYILT4peuV0H5J3m8YRGd_YaDtKpy2d6VrKd9LrfzWD98sWSJxeRGhgOshGufLJTNgaWoGNWm1mSfOIHAU96yQl-x_hX64CRIWITOF6V4gwAsyNc8UGP2MR0cpnnhpfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آنچه در روند تفاهم‌نامه به آن رسیدیم، بدون استثنا اجماع کارشناسی همۀ کسانی بود که دستی بر آتش داشتند
🔹
تکذیب می‌کنند چون بیان قضیه را نمی‌دانند و یا دستی بر آتش ندارند.  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/457680" target="_blank">📅 08:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=RiKUW0_JrziD5yk4U1RWHf1CNKAWCZD2TpEJBx54Z3MBWmICRwHlCskswxKNxHjCTsT-XOOVeuFZPYU-knV-FryCUHads0BqRCJUewA_LXyw38cNwkRf-ufNcCeUnogkhR-xnusmEUi8qvW14_hCYG53AdLyY38o43RamF_LHsnhsp4r7BrWzt3IK8AaVp0hnykCvcR_-OT5JkB9uib3iP9e5V_0_ag6oF90hA8GCOHKJ1kJyhEToAIDhA3oeKEJ9UVtfbk_g-BXrzDiVbrSyfnqzVkGmhKTyYNLzKA2UhvpCmTk0v1QCfvX9j6XWlP2bigqxKMsZzhPYgKwFpml4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=RiKUW0_JrziD5yk4U1RWHf1CNKAWCZD2TpEJBx54Z3MBWmICRwHlCskswxKNxHjCTsT-XOOVeuFZPYU-knV-FryCUHads0BqRCJUewA_LXyw38cNwkRf-ufNcCeUnogkhR-xnusmEUi8qvW14_hCYG53AdLyY38o43RamF_LHsnhsp4r7BrWzt3IK8AaVp0hnykCvcR_-OT5JkB9uib3iP9e5V_0_ag6oF90hA8GCOHKJ1kJyhEToAIDhA3oeKEJ9UVtfbk_g-BXrzDiVbrSyfnqzVkGmhKTyYNLzKA2UhvpCmTk0v1QCfvX9j6XWlP2bigqxKMsZzhPYgKwFpml4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نه تنها ایران ونزوئلا نشد بلکه دنیا در برابر قدرت ایران حیرت کرد
🔹
شرمنده‌ایم که مشکلاتی وجود دارد. ما در جنگ تمام‌عیار اقتصادی، نظامی و امنیتی قرار گرفتیم.
🔹
ترامپ خیلی راحت می‌گوید ما کوبنده‌ترین و یا وحشتناک‌ترین تحریم را بر ایران اعمال می‌کنیم.…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/457679" target="_blank">📅 08:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef4cb6ed.mp4?token=qwvYOYXloGHNDn3nxf0sbHgu47YC3JgKCUPHBhjcamTEjsVbU_KFmcb0m360VeX_Y_EYC39wUHtb2AV2MUIv_zkQlkNdTjZXWJBLWotUSfeM9FSRA2d233cF-iS-8p1phFEmNmgFExeViQH2rMWXHasVGUa2UJrF_dvDH_B3uVWsKnojPa6b69ZfQPa89DPHGBNir8daJPs2Ej9sLpX_XKMnSdK04K_t8HtOnZTH7wJLo1paRNBnrwrJ6YYXr2jEJ4XuEUzvLDkoEsR0JEDRRxAejpAIX5d7_VrDrkZYbLbTcqc0NyIEN6hy-kNRhVvPEKp5acr5GS2Zt2uv0U_pXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef4cb6ed.mp4?token=qwvYOYXloGHNDn3nxf0sbHgu47YC3JgKCUPHBhjcamTEjsVbU_KFmcb0m360VeX_Y_EYC39wUHtb2AV2MUIv_zkQlkNdTjZXWJBLWotUSfeM9FSRA2d233cF-iS-8p1phFEmNmgFExeViQH2rMWXHasVGUa2UJrF_dvDH_B3uVWsKnojPa6b69ZfQPa89DPHGBNir8daJPs2Ej9sLpX_XKMnSdK04K_t8HtOnZTH7wJLo1paRNBnrwrJ6YYXr2jEJ4XuEUzvLDkoEsR0JEDRRxAejpAIX5d7_VrDrkZYbLbTcqc0NyIEN6hy-kNRhVvPEKp5acr5GS2Zt2uv0U_pXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید میثاق رئیس‌جمهور و اعضای دولت با آرمان‌های حضرت امام خمینی (ره)  @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/457678" target="_blank">📅 08:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f52dfed6.mp4?token=Eh0F_w0K8rXY5bNf_6SSMwu0qs6DHWU8MjYxspeTViJiDLsWEaozA8v6eX8oGZReAKaJ4TbMCON4WS1xp51xIP6KgbF6RYKE9_Ws-zvj8bUAchSsndQUdPr1_UJZHHV8I6lqz6UiqJHABHlDrW19CophbtOOzRbIyIaYGsrFI7ktZdCIHbiVDPcxsJlHxxL1kHZ4SXWXnXjGN4VVmH9yNg9piPaVmCYAH7qt40n5lM1_gs-ryyYlofOo2B2A3l4d4-EkE6Ho-OSFrnF5VeQODSivjzFSOnJBfXwrY2Xs_P4Ny3vtO19AzjqPF3hSPOYvTuY30ZFatMwpW544rS8U2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f52dfed6.mp4?token=Eh0F_w0K8rXY5bNf_6SSMwu0qs6DHWU8MjYxspeTViJiDLsWEaozA8v6eX8oGZReAKaJ4TbMCON4WS1xp51xIP6KgbF6RYKE9_Ws-zvj8bUAchSsndQUdPr1_UJZHHV8I6lqz6UiqJHABHlDrW19CophbtOOzRbIyIaYGsrFI7ktZdCIHbiVDPcxsJlHxxL1kHZ4SXWXnXjGN4VVmH9yNg9piPaVmCYAH7qt40n5lM1_gs-ryyYlofOo2B2A3l4d4-EkE6Ho-OSFrnF5VeQODSivjzFSOnJBfXwrY2Xs_P4Ny3vtO19AzjqPF3hSPOYvTuY30ZFatMwpW544rS8U2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید میثاق رئیس‌جمهور و اعضای دولت با آرمان‌های حضرت امام خمینی (ره)  @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/457677" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457676">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diMdB0-7I-8_vwFUsAdesn6j6P4EfaCWumrspIFVILsFLxrC9laM9ExK4e6rtnXwSa57xilI2a1v5H3neTMbfVX0F3BaJtmEvlIIKa7YHXijXzyOL2no3-sJUgkPFcwUerhvJV2aJrI_B6d4hSrfl78SWNc4YL3e8FvPi1iDsUxZWRJIvC5XCQiFPhx_L6CuTwJYWMoIO2_sezeTXYRPAFXUwE8CPYn-oNnbZBgRxs4FCuaMNv5Y7duky2eASzHkNQ8t3CF1iCsJLVQ4sEYkeDOivTHIzw213r_g1n2ZPaMtih41cagvd22BzKlrlthfuRy836AlfS6mSsoTt-NljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام تروریستی که در کودتای دی با اره‌برقی آدم‌کشی می‌کرد
🔹
یکی از پرونده‌هایی که بلافاصله پس از کودتای آمریکایی صهیونیستی در دی سال گذشته در دادگستری استان البرز تشکیل شد، مربوط به شخصی به‌نام «مجید آدینه»، در محدودۀ محمدشهر کرج بود که نوزدهم دی با سلاح گرم…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/457676" target="_blank">📅 08:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457675">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اعدام تروریستی که در کودتای دی با اره‌برقی آدم‌کشی می‌کرد
🔹
یکی از پرونده‌هایی که بلافاصله پس از کودتای آمریکایی صهیونیستی در دی سال گذشته در دادگستری استان البرز تشکیل شد، مربوط به شخصی به‌نام «مجید آدینه»، در محدودۀ محمدشهر کرج بود که نوزدهم دی با سلاح گرم و تجهیزات جنگی بازداشت شد.
🔹
مجید آدینه در صحنۀ وقوع جرم به‌همراه یک قبضه سلاح کلت کمری و سه خشاب، ۳۰  عدد فشنگ جنگی، ۲  عدد شوکر برقی، ۲ عدد افشانه اسپری اشک‌آور، یک دستگاه اره‌برقی شارژی و بطری بنزین در آخرین دقایق شب ۱۹ دی توسط سازمان اطلاعات سپاه البرز شناسایی و به‌همراه شخصی دیگر دستگیر شد.
🔹
متهم که با تجهیزات کامل نظامی بازداشت شده بود با توجه به ادلۀ موجود، از افراد آموزش‌دیده بوده و بر این اساس در بازجویی‌ها، با رد هرگونه استفاده از اسلحه کشف شده بیان داشت که با هدف خرید لباس به محل رفته بود و قصد کمک به نیرو‌های امنیتی برای هدایت مردم به دورشدن از تجمعات را داشته و بطری بنزین و اره‌برقی را نیز با هدف خنثی‌کردن آثار گاز اشک‌آور همراه خود برده بوده است.
🔹
با وجود انکار «مجید آدینه»، بررسی‌های تخصصی و آزمایشگاهی مشخص کرد در بازۀ زمانی ۱۸ و ۱۹ دی از اسلحه مکشوفه از او تیراندازی شده و متهم با علم و آگاهی نسبت به فراخوان رژیم صهیونیستی آمریکا، عنصر سلطنت‌طلب فراخوان‌دهنده و سایر شبکه‌های معاند با هدف براندازی در تجمعات شرکت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/457675" target="_blank">📅 08:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b07eb7de.mp4?token=ebhgUTWkdPgTHgASOdiHiAo5iSiWcWNWI0ehUSA4teWN9ORmCVIq6K0AM7B_Ap7S5h4zOqC0zlA19siJUn1RGU6BUB__0X4yCJr0d96Efi323QWWtUU4VWSd2kEbSnyni9Ff9qWl2AFkhJRf0pB5-SVsi3brLLmjMcBJ3r93EwKUSXBBWWUlsJOrEcCLNnJmWhgxxpO2NRvgWiIS63StSvg9KcY0toMtolY7mwoHsFvJoisV2fKUI5MP9s7_mG5AUo_ZhaDdu-OhlCs4u4JLSuU8FhbiK4cgjwuHzf_SLJOUPM4Gqmt-nMZdF0cCTK7LrzkhWAMD36uVHwUFOBnubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b07eb7de.mp4?token=ebhgUTWkdPgTHgASOdiHiAo5iSiWcWNWI0ehUSA4teWN9ORmCVIq6K0AM7B_Ap7S5h4zOqC0zlA19siJUn1RGU6BUB__0X4yCJr0d96Efi323QWWtUU4VWSd2kEbSnyni9Ff9qWl2AFkhJRf0pB5-SVsi3brLLmjMcBJ3r93EwKUSXBBWWUlsJOrEcCLNnJmWhgxxpO2NRvgWiIS63StSvg9KcY0toMtolY7mwoHsFvJoisV2fKUI5MP9s7_mG5AUo_ZhaDdu-OhlCs4u4JLSuU8FhbiK4cgjwuHzf_SLJOUPM4Gqmt-nMZdF0cCTK7LrzkhWAMD36uVHwUFOBnubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید میثاق رئیس‌جمهور و اعضای دولت با آرمان‌های حضرت امام خمینی (ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/457673" target="_blank">📅 07:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7oJdGWgSlVDGTiEm8LT-BkZVdkVd5QWBOTd49l-c2FEHnUnOOL5YKFh7lTbcX8tQ8bC7YXM5cdzBeeeZdHk_L0s6kvPRobkgdF6tNXilDB2eYFuFxu5MzSrJTGn97nCUtee8JeOxFn3PADzjg1NRgw1iYrJREVGeBEqarfUQibWSQmv47MHlvWWv_TpDaV8Z0taGhKaiYZXz7eGaIAXGKokXkv6HOmY5EH1WaMEhbscIMdZI4NH6AgZCMJQ0MJvxID2V-PKuaxflqTkz0VfBJDlJqE46bD5GDathvmCmvShRJ3mr0GEX__iTMLaqvXyTJWx2qVXdxes_3IqsevUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مهدی طارمی با عقد قراردادی به الوصل امارات پیوست.  @Sportfars</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/457672" target="_blank">📅 07:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB2XLgbRhymsPZQhCrer2vvwQ-wjyJXLKua2oXhRKnV2zMTlpIxU1HehFEC1a6O0-Rc2fEF88y0vTNkPPd4PFhSJUAXU6BVkAa6USKmK3pXtBCGjqKkG102enzvLXP9JTBtuZPeCNus7rT81OkUqmmVnqdaT7-J0tckQCmOJBvLvuzQgdxcxAHj1IUyS6x9klUdAcNu22WgxICLeZv_gKx6lxLVSDXH6QPHPbK2wUKrltV4VYUj4tMAlm7oKc5aO6ZmslzraCoOIV63lvXtyuxK6G9_WzlXRKmx1e1RQGJl1L23lJXzPITyxrgooMuHe6ffzRV6i19YpgCpzFFitDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سهمیۀ بنزین خودروها در سیستان‌وبلوچستان به ۱۶۰ لیتر افزایش یافت
🔗
جزئیات این طرح را در تصویر، و
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457671" target="_blank">📅 07:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۱، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457670" target="_blank">📅 07:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هواپیماهای سوخت‌رسان آمریکایی بلغارستان را ترک کردند
🔹
مقامات بلغارستان اعلام کردند دو فروند هواپیمای سوخت‌رسان آمریکایی از نوع کی‌سی-۱۳۵ که در پایگاه هوایی «بیزمر» مستقر بودند، در حالی که مجوز استقرار آنها تا اول اکتبر ۲۰۲۶ اعتبار داشت، زودتر از موعد این پایگاه را ترک کرده‌اند.
🔸
پارلمان بلغارستان پیشتر با استقرار حداکثر هشت فروند هواپیمای سوخت‌رسان کی‌سی-۱۳۵ آمریکایی در پایگاه بیزمر از ۲۴ ژوئیه تا اول اکتبر ۲۰۲۶ موافقت کرده بود. هدف از این استقرار، «پشتیبانی از عملیات نظامی آمریکا در خاورمیانه» و در واقع جنگ علیه ایران اعلام شده بود.
🔸
با این حال، در نهایت تنها دو فروند از این هواپیماها در پایگاه بیزمر مستقر شدند که ۳۱ ژوئیه وارد بلغارستان شده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/457669" target="_blank">📅 06:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">شوک بزرگ تراکتور و ۳ تیم دیگر به لیگ برتر
ممکن است بازی‌ها بدون VAR شود
🔹
در حال حاضر، تراکتور، شمس‌آذر، مس شهربابک و فجرسپاسی ۳ باشگاهی هستند که در زمینه تأمین تجهیزات مورد نیاز VAR با مشکل مواجه شده‌اند و تعداد دوربین‌هایی که این باشگاه‌ها در نخستین دیدارهای خانگی خود در ورزشگاه‌ها مستقر کرده‌اند، اختلاف قابل توجهی با حدنصاب تعیین‌شده از سوی فدراسیون فوتبال دارد.
🔹
برای استفاده استاندارد از سیستم VAR، باشگاه میزبان باید بین ۱۱ تا ۱۲ دوربین در ورزشگاه مستقر کند. این در حالی است که تراکتور، شمس‌آذر، فجرسپاسی‌ و مس شهربابک در بازی‌های قبلی  خانگی خود تنها از ۶ دوربین استفاده کرده‌اند.
🔹
در صورتی که تعداد دوربین‌های مستقر در ورزشگاه به حدنصاب مورد نظر فدراسیون نرسد، ممکن است مسئولان در روز برگزاری مسابقه تصمیم دیگری بگیرند و حتی اجازه استفاده از VAR در این دیدارها داده نشود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/457668" target="_blank">📅 05:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1304f142a.mp4?token=uDD9fEPDHyOHyS2iZIIBL8SpgA5RRvCdETxwxk4iJLBvVCqmMKiXPzIDttxKpQKDhWN5frGscjm4OacNtlonaBN5DRCU_r8eq0F9pz4f56B3HMTa3dWbBqT2VeohYfkOzpw34kwT1Fa0e9POQNxUpxSFzk7qYx4JIkzdegLlkUaxTVv_bdsVUrZ2R987rUzqC9-7oXzfoZnVgsrMLag7Z-fPwNZUuq_XAtamX_vlsc7iQQHBSW70jsFj0aOI-EIZPoje04vxqyebG07IE-oVD5U5oEr0EVolTR0-daJRCiJ4t4mLfv_5hzuVFP8wrcefEnZVl46Y4o9dIRO00WWVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1304f142a.mp4?token=uDD9fEPDHyOHyS2iZIIBL8SpgA5RRvCdETxwxk4iJLBvVCqmMKiXPzIDttxKpQKDhWN5frGscjm4OacNtlonaBN5DRCU_r8eq0F9pz4f56B3HMTa3dWbBqT2VeohYfkOzpw34kwT1Fa0e9POQNxUpxSFzk7qYx4JIkzdegLlkUaxTVv_bdsVUrZ2R987rUzqC9-7oXzfoZnVgsrMLag7Z-fPwNZUuq_XAtamX_vlsc7iQQHBSW70jsFj0aOI-EIZPoje04vxqyebG07IE-oVD5U5oEr0EVolTR0-daJRCiJ4t4mLfv_5hzuVFP8wrcefEnZVl46Y4o9dIRO00WWVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن و یک جشن متفاوت؛ میلاد پیامبر اسلام(ص) در سایۀ مقاومت
🔹
درحالی‌که جنگ و محاصره سال‌هاست زندگی مردم یمن را تحت تأثیر قرار داده، یک مناسبت مذهبی هر سال چهره شهرهای تحت کنترل دولت صنعاء را تغییر می‌دهد.
🔹
امسال نیز در آستانۀ میلاد نبی اکرم اسلام(ص)، یمنی‌ها به رسم هر ساله شهرهای خود را مملو از رنگ‌های سبز کردند.
🔹
از ساختمان‌ها تا درختان خیابان‌ها و حتی نور چراغ خودروها همگی به رنگ سبز درآمده‌اند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457667" target="_blank">📅 04:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ba2728cd.mp4?token=uIP8gzWOOx1DwBFPf29fhAl5fpUYrkxW7emO8jw32cbv4IehftvFUOAfhZg8Q7YhTEMpPxGrAidjM5EbYdaGwX0VDK4lLNVVqcIGYaK9icEXeQGjeXR4BB14l_aaxBWT-rTLu-ma_dtXDvoegb23F4JoFlFtfqvqhK5KanbeENWzPQQ5vRfY1rVlUTFAJ8M1A5YdWcspbcob9dQsYEg2Z3nw_X7sRSTO1YQCU4DZW5DWPT0YJc1Rcwki0TBiEk7PaGVJHR5rhhEPIXHm1tGPCNQK5BaeudD0oqwz-gChToquNOodYGKgET2SNKDZ0E_s4pWRCJ64A7uXts-YcFFWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ba2728cd.mp4?token=uIP8gzWOOx1DwBFPf29fhAl5fpUYrkxW7emO8jw32cbv4IehftvFUOAfhZg8Q7YhTEMpPxGrAidjM5EbYdaGwX0VDK4lLNVVqcIGYaK9icEXeQGjeXR4BB14l_aaxBWT-rTLu-ma_dtXDvoegb23F4JoFlFtfqvqhK5KanbeENWzPQQ5vRfY1rVlUTFAJ8M1A5YdWcspbcob9dQsYEg2Z3nw_X7sRSTO1YQCU4DZW5DWPT0YJc1Rcwki0TBiEk7PaGVJHR5rhhEPIXHm1tGPCNQK5BaeudD0oqwz-gChToquNOodYGKgET2SNKDZ0E_s4pWRCJ64A7uXts-YcFFWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناهی که در آن مُصر شدی، دیگر کبیره است
🎙
آیت‌الله بنابی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457666" target="_blank">📅 04:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327be7e15a.mp4?token=Zu9SYaSmXkgIS7YaMN7ct9rhYbscIG7O5-uU9r_0k3zAUjJExDV770fc2jVbTVRjZvXIqptr4VzAlMLEqH4zG1gII6at9jjaI2nx1xfbG9OIysliH4YZzBh30Qi6h0-4486SD_kwOVzfO0IJaMDwfjmE0pwfffW8kIDvjLJZGWecP4PQkuo5yWmPjj491vWQgS6lmW8-_kbmT-iiDF0w4Aq5lGC_SSmUYLEZtna9FIWdrcGvcmeMYbO16daGyNAQDulqnl8x8hi9GLu7vObduK-3uozB3Z9iO_wh2mJg5Pp3Zy4X66n4Lfu1Iq39w4yFe8ktvbay7k_-uab8ebPXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327be7e15a.mp4?token=Zu9SYaSmXkgIS7YaMN7ct9rhYbscIG7O5-uU9r_0k3zAUjJExDV770fc2jVbTVRjZvXIqptr4VzAlMLEqH4zG1gII6at9jjaI2nx1xfbG9OIysliH4YZzBh30Qi6h0-4486SD_kwOVzfO0IJaMDwfjmE0pwfffW8kIDvjLJZGWecP4PQkuo5yWmPjj491vWQgS6lmW8-_kbmT-iiDF0w4Aq5lGC_SSmUYLEZtna9FIWdrcGvcmeMYbO16daGyNAQDulqnl8x8hi9GLu7vObduK-3uozB3Z9iO_wh2mJg5Pp3Zy4X66n4Lfu1Iq39w4yFe8ktvbay7k_-uab8ebPXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رباتی که رکورد سریع‌ترین انسان جهان را شکست
🔹
یک ربات انسان‌نمای چینی در مسابقات جهانی ربات‌ها در پکن، ۱۰۰ متر را در ۹.۳۹ ثانیه دوید؛ زمانی که از رکورد جهانی ۹.۵۸ ثانیه‌ای یوسین بولت، پرسرعت‌ترین انسان جهان سریع‌تر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457665" target="_blank">📅 03:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Epga6726CSQ6Yak7A2AoiWZkWmkEFJdySDQ9M7TwCMj92cyjJ5ustgSJ802C8dMAQqKDF6xqZ5xRGmDqEBdwf5QUi-Kx1icjWEhtDkY97z2AV6mEdyYjN-wbXI_FJPG4kdw1ldwcjhHONaOeL_JeNs2vRchlljz3nTYWIHe84qVfEZ9gGeQkKiB3auNCV5_jAfDm4D2PkxwqgOIf965T6mh6uNG0TJ2Yfrpd7Gi6ArqM4rN8Mz-lp3paf7Ymc0HfRAs35njeFH_RatG_e65R08UAk_j4VNVT5UyhElqjUnudk4fQmlrPtzI3hXe1i71o7AklnCS5x-yE_WP6u9Wccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت مذاکره با آمریکا از زبان نخست‌وزیر کانادا
🔹
نخست‌وزیر کانادا مارک کارنی امروز با اشاره به شکست مذاکرات با آمریکا گفت که واشنگتن خواسته‌های «خیلی زیادی» داشت و در مقابل، امتیازات «خیلی کمی» می‌داد.
🔹
مارک کارنی اعلام کرد که کانادا از ۸ سپتامبر تعرفه‌هایی بر واردات از ایالات متحده اعمال خواهد کرد که در پاسخ به تعرفه‌های ۵۰ درصدی جدید دونالد ترامپ، رئیس‌جمهور آمریکا،‌ وضع می‌شود.
🔹
نخست‌وزیر کانادا امروز در کنفرانس خبری گفت: «کانادا تعرفه‌های جدید واشنگتن را دلار به دلار پاسخ خواهد داد تا از کارگران، کشاورزان، خانواده‌ها و کسب‌وکارهای کانادایی محافظت کند.»
🔹
کارنی گفت: «در روزهای اخیر، آمریکا شرایط جدیدی پیشنهاد کرد که غیراقتصادی و ناعادلانه بوده و منافع خالص کانادا را تضعیف می‌کرد و اعتبار هرگونه توافقی را زیر سؤال می‌برد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457664" target="_blank">📅 03:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457656">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFfAqwXfRzNeF3mAD0ai85cBmGzz9NlrACPNA2oRjPk_QmoMba1Nh5ZCUrhcP3czXG7ukDPB3lFfgkPP6ldsYdECfXUgNgpCHjudUXRDpBOf8LmbqLHQBmyEC1eMspQPaw7A4VyENduh-iCopYM0ixk129eSEZ69MP222cEeB_LfiySRKiO0uZiWTBAzfxp41JHWlxio__Fv6Hf-JxOHnIdIktuFLgJnM_yYMfQiRT10kyQ8YpTIbBBzS6ZFcbysgdaaAGcsQO4QTAPEGLPD_ZMYncaq6g7F6gBR6dl-eFgoAj0OvrNdEzAvzcVrqkbCt-WOn23kNVoIHEGmrTU4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6QE_lWFrFgKSJw6rh48mTDve3eVDmtk4wVUGFrQp5h57yPJPCyeP7GUhii4pPd5DzAMVgMvBu6MByKcMvFi05AF3HDgKFqdC3jud1OnREsfUUzo-8RuMIr3CgIINAx-RcumDj6_lbs0WOREMrhknXk-0MSZ3JK4SIG3e432iVjiU9DgyjI5eSFMLefMde2gDpjhZaL98VQVYY0MWPn_16Je5ZmXyu2_aB7ndwfyh0YpE_a_oi5-UClFQMsGoK3D4rKUrt2nom4nHztMRKiu70bfJejcmL2NFzWiCyTHA4eCR-osFEPdxmLd5zFX75WCsP9F9Z9pN05Ros6vqGu4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9l6r1BQcNyDtO7iFb_0qlU00YQot3Ce6U3wnKdvFClqL93NDPwsVQAZPCorVH2MitFLakgwNB5wxIXp03HZIZ7fNu1Og30SJ-o73KP_ZRHHehvwTt2dbx9hYfLhtmDGPNgtx9tDOjgZEFzxGIR_MX0qpwK9ACfvXjDECPw_DHXKnJf3O-9UTSwhfKO9zKzODUXFLLSqUgysFLQjbn5DSb4wWc7XPXPeXx7Tis2FCYyfHYRRsV5OPzLPPinDDBVIOJXWNL0WMQLNoRpV3Z638Kbwdy3EAvcoyJ03wQ4QNsOA8HwUYcOXdmFSs0mwzht55t_P0tjj_2P5cV-I_-FdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_zJ-DCj9ZPwYYaS1_TiB5yFs6_TrBsvksPGxzjwrjsnbZGWMtZCCrmtDv7YEZa1v0PEexeKZpvPvQDWJ9LOlwSeMxxxd-LbEvkYAe2VITEP3UXWZALBx0NMYFdcWK07WH_eWUknjPb3WhRCQ875O3jvezTkYHQyLBl87j5hkvDNrDHDBNb6CXKn8q6GCUnq3B2GeyCVGtz9flBbhk_qgPDnh2JtE3n3LP3NNfxuTewHmwBGaCSpFkbt3mTyUBOnizyXW2Em2WaZUUabs4p0BB3P9cZjdC14ZsWWdfH64_DqK1NkV3XsBendcVB0G3pX86MpHqvNPJl63krG3gSe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8KxppmT3zJXDJA9hVBbYmwuBrFovllsBvPNZKmCE9kCpSojrk_ABaTRGW54HFWnjnrqnaMRG8Jh39hwwQOGZYZTS6cphio0JZ0KhvmKwFQ9CIH67ScG2BVWjnaTFSDe4dEmzQLji9CDPZmPxo69U3aFnQjmbT6S90F_3FAAPVpRHt43U0ex2grM74lPZfKPCNPOI7MZCxKIb3usXEgXhCprwF8tf_g9XpyzPqXzCo__tEqLqjNfJQvhqSk82ExTuAfaEtueSUdZJMqkECyk_N9KUwO70TgwPt2iJKpgbEcGtxs-nwROK_aGVISfm9Vs-uGNSj4FSURaDhqJNGfCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYNf6oWJfKkmACi95Kn5jVzOSWLUm0LMNfLBpuwke5XaWE36S3mUDm1aI8r7Es_y78Hvl_kAu6_1FY8vrPYyszZw99kDk9C4Amt12BSw8wm1D5oYs5g9Xp-ej30m9pTteiNsXBxGQ5Uctfwiizo-8Ijkj8bops73NifzmUcmUe760cwzFOsUUu4xZZVbbu72SW5mYjfFc9X88LvilzLbX94uNnyL058vKnLyrtK7RkMAuZ58YxIahVUPkKpS-OqIpF4-6ege61zzqgBnv8t9YNb9pb7Pfg5EW6UeTnlS-_J2zpmtRXrpWkAet5XvIYpp5sY0Cyc4O9LXvigg_qvVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PijIly4tH_ZNjxyDHjTiD_oEMHGyyqX9-1oJwecncKP0EDdxKLIXraKRsAuLnI0jJpYV9psn34FbmG8oudQy1rHPZ_fr0SLjp4TeEYF9gtCLS6ijQpWlfoP_XmEuxUjXXe6uYGUhE-V3wZTGTMYuVjpJgFfE66OxM4vdDPEPJZiCBPWrx5HVs9iXUfoWDbMzCMhFcAD8xWmlCdTrgYSRfiBq_9XXnBe9aM9BCAhmxUKdInsfX7zw-fJWjkZ9MlB5wc_dCNrpiwKffJD6JF7RDRtqhAuGHR-VPGGfG15il_ZtzZ-Uau790TjyLIDu3fbrmyg1W2Xe2cN3jG_Q609jnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1Es4pP2uTrrtk_exoGJq0kAlecvNRHLaIhMrKS9ZTB9jTH6dglRYKkXjMK6hzQIm5if_dhbkcsF1-NOvYLF397qRnXehJ9MUFV8XYQgioGLaoltFgPMQX74YevDFnkzZMjlA0pa6eW-7UydjyiFDhC2z5M9ZC2xzz-xaooMu-ajmCw_5PB75rWnCHDl_Jvy_yWjRbu9p-BqwFyviV4RvIMfmldD2EjBC2mw9h0ujA_nPcqhp9bXCugMUHphnCY28HRDYl67_apcxZKjqOoTCMXCp1aQMqdWhTD0ndBZEFvRwQz3p4Fk0kJDcoY2J59liyW-9z_rcGfyypKMBJFtxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم گرامیداشت روز پزشک در برج میلاد، با حضور رئیس‌جمهور و وزیر بهداشت
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457656" target="_blank">📅 02:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457655">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785a0eabeb.mp4?token=ry3KU6BTNl_7szitp_Y2WMh_nQoSHQS8xVd-O8GVYRocefSJ25wVNrrRWjcO3wsBiuY14k31YOcepbTFmF3bRmtDwIaK7B8l5v168Hs0UwBMesJRZy3oUNlhUQIp_d_0vbZsuzWBv2oR0NdY1FW8F_JdTWs7toKGqDQnC0DnI2rp7NTPBy4SlvzEmX8Xl37gCqocAMBjMP4zK14qu0hHX1iOWF1RQ0nF5YHCDZfcZ4ciq7DMbhg360AOVEd_mKtl_QJupYdDqb3Wv-OoqYnonjrrxcnZlb5qVGa8RdXJqYcYTqUqVVTn4E2cKI8MtksqLsdW96Df1isbi5BZD_vu4Jf1TOE9nxegHxiSBNV5GTJEiNGhd_TT19yrr53bXP4w57MFrOa7wEN-tHKnBlQuD3Ic0k4GsSqGPsR0VVd0wSlV5FsOcOAbZLIhxNQc5z9IldB0rysOg5tvPvCYeI96i1k29rMNvI-02o8fzmMvDM6Le7WVwZlg3JEWdStzZtyIpShuJyJ82N38voyA1Xk8Wp_mJ90dCJhamMo7idtDqzpmO6MnlDu3uS5Nj9C76POffdlaIhz_1xOqxS_RwS4YSQbpqHOrlS0VRE7dMap-hC1KLoahUtlw5yYO0XLU6hejGYkZahw0kSU-CKX8CM5hHoAsKXhKIW_KVgk0T2s9ERI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785a0eabeb.mp4?token=ry3KU6BTNl_7szitp_Y2WMh_nQoSHQS8xVd-O8GVYRocefSJ25wVNrrRWjcO3wsBiuY14k31YOcepbTFmF3bRmtDwIaK7B8l5v168Hs0UwBMesJRZy3oUNlhUQIp_d_0vbZsuzWBv2oR0NdY1FW8F_JdTWs7toKGqDQnC0DnI2rp7NTPBy4SlvzEmX8Xl37gCqocAMBjMP4zK14qu0hHX1iOWF1RQ0nF5YHCDZfcZ4ciq7DMbhg360AOVEd_mKtl_QJupYdDqb3Wv-OoqYnonjrrxcnZlb5qVGa8RdXJqYcYTqUqVVTn4E2cKI8MtksqLsdW96Df1isbi5BZD_vu4Jf1TOE9nxegHxiSBNV5GTJEiNGhd_TT19yrr53bXP4w57MFrOa7wEN-tHKnBlQuD3Ic0k4GsSqGPsR0VVd0wSlV5FsOcOAbZLIhxNQc5z9IldB0rysOg5tvPvCYeI96i1k29rMNvI-02o8fzmMvDM6Le7WVwZlg3JEWdStzZtyIpShuJyJ82N38voyA1Xk8Wp_mJ90dCJhamMo7idtDqzpmO6MnlDu3uS5Nj9C76POffdlaIhz_1xOqxS_RwS4YSQbpqHOrlS0VRE7dMap-hC1KLoahUtlw5yYO0XLU6hejGYkZahw0kSU-CKX8CM5hHoAsKXhKIW_KVgk0T2s9ERI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۵ شب ایستادگی و مقاومت آملی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/457655" target="_blank">📅 02:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حملات توپخانه‌ای اشغالگران به جنوب لبنان
🔹
منابع لبنانی از حملات رژیم اشغالگر صهیونیستی به ارتفاعات علی الطاهر، دوحه کفررمان و شهرک المنصوری خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/457654" target="_blank">📅 01:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df528cbbb0.mp4?token=jaGHW3oMGpkrMehfKUAAsHNr32eClejnnHqcVPalREZ1woXp8jQYY0Q27uvHzrqDQPf81Vbdhivi31RTtqF6x5gdJ04y6rCewmwYG1yqabtlVEbXQnZ3F6xgd0Iidk2OWDo4y9TQQkGj3n7Z9_ywbEhklFkFeoQiTVCYWBx3Gs_zYLpYEo2qNDAMy2qqvvympmhz4RU2ogHOvSY-HCnlHxHIVZB6OO1mBrIm5TFeLfwFxOPBwK1XFekD9U34K_hCwYxg4aOAVKMp79zjBlk0fc8Qqg21cigZW55nTq4Yipxd_PmakLR58H7DP6uKKqNFpqDt78fyZGudDCcmf9dPDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df528cbbb0.mp4?token=jaGHW3oMGpkrMehfKUAAsHNr32eClejnnHqcVPalREZ1woXp8jQYY0Q27uvHzrqDQPf81Vbdhivi31RTtqF6x5gdJ04y6rCewmwYG1yqabtlVEbXQnZ3F6xgd0Iidk2OWDo4y9TQQkGj3n7Z9_ywbEhklFkFeoQiTVCYWBx3Gs_zYLpYEo2qNDAMy2qqvvympmhz4RU2ogHOvSY-HCnlHxHIVZB6OO1mBrIm5TFeLfwFxOPBwK1XFekD9U34K_hCwYxg4aOAVKMp79zjBlk0fc8Qqg21cigZW55nTq4Yipxd_PmakLR58H7DP6uKKqNFpqDt78fyZGudDCcmf9dPDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط مرگبار خودروی ون به دره در جادۀ هراز
🔹
معاون عملیات سازمان امدادونجات: در پی سقوط یک دستگاه ون به دره در کیلومتر ۳۵ محور هراز، ۷ نفر جان‌باختند و ۶ تن دیگر مصدوم شدند.
🔹
تیم‌های امدادی و عملیاتی در حال انتقال جان‌باختگان و مصدومان از عمق دره به سطح هستند و عملیات همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/457653" target="_blank">📅 01:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ac6363dc.mp4?token=MF7rHVKKo9fVZWHCewg0FK3XtCSH8L_HlSA1NGJGbatmcNNx5sIxzgQTu6F1ZHecoNlh14pDZIzfwQmGq9uJBbRcJjMaC97ZOPQvMgWimtrj12J2XMC1eHZF4_6Cw_ESgGK-CWNdHSYkYwr1PvnXjEx6-porTbLYSdKJXwF9JK4FInrWF0QE1C4P_7lhgo2FffQO8Bv4R_1aYhSK-AeeFFTRDXqe_oNu7RINO5rIwRRlYzTwBY5wJ5vgbiAXGJpabz_VVR3wo7hZqxPY-yBdQ-RC1BoAipgzrac_6nmn3w3CIqnifqVY8VdNAlsfA97JWdKEuyWmhFlp27a5qVAPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ac6363dc.mp4?token=MF7rHVKKo9fVZWHCewg0FK3XtCSH8L_HlSA1NGJGbatmcNNx5sIxzgQTu6F1ZHecoNlh14pDZIzfwQmGq9uJBbRcJjMaC97ZOPQvMgWimtrj12J2XMC1eHZF4_6Cw_ESgGK-CWNdHSYkYwr1PvnXjEx6-porTbLYSdKJXwF9JK4FInrWF0QE1C4P_7lhgo2FffQO8Bv4R_1aYhSK-AeeFFTRDXqe_oNu7RINO5rIwRRlYzTwBY5wJ5vgbiAXGJpabz_VVR3wo7hZqxPY-yBdQ-RC1BoAipgzrac_6nmn3w3CIqnifqVY8VdNAlsfA97JWdKEuyWmhFlp27a5qVAPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای امشب زائران مزار نورانی رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457652" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxiV5H_damefFaQt4EUlOVZkhf6tfPkkT3BlGwyEG08BJ1AI0TCs_MGufxlKAT-QImzy-vPeTNNv08z1UHQdtEKKRE7dItoprozKmdvtCn_JdERX5qu31OHIaR8-k7XCI6JTVqaHcaQ-OjhkzRSTGs7zMi3h5NoGUGfq7TkGvs-N_zuiKHGrv_5Zy-24dxtr3y56wzzG6TtjJv8ZaiCPFeAThAIyyTwgYxGj-v9OHYSDowMU_DTiRGDvfci71c8_AiRsneBmiymRg-9CfjXfcTkEntGxNMUpINJ37kyjDEvoybpIpzXjRplc6CQq6CHAHIedXuxqBARVYL0VEr7jYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ امکان سربازی مشمولان فوتبالیست در تیم‌های غیرنظامی تکذیب شد
🔹
سازمان وظيفهٔ عمومی فراجا در اطلاعیه‌ای ضمن تکذیب خبر شایعهٔ امکان انجام سربازی مشمولان فوتبالیست در تیم‌های غیرنظامی اعلام کرد: مشمولان فوتبالیست برای ادامهٔ فعالیت ورزشی می‌توانند در تیم‌های…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457651" target="_blank">📅 00:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvDt5dKEsuNU3DWFZ_x4EUbAxna44s5B_gV1QJ7M-05ei1fo6PODuioN0odVpIS_HLlItzLyi6YOUPofC8WK0_JpE58xlYHzGK2iz6OKupyLUDt1H_C4-OK5kG75CPW4Kd7hYKHXN_FZI63iGIRzLeenv01JTLAQYqLE-_z4_dyuete-a462yMMlI4mac-8qmXKVFVltJEzfpUAFYOeKllVjK0L4y5Q96v8HBhk_9zgptZkTEkpXht4CWA-PcXioMZr8jlaASNUfFIY7tOfm8p4XLDA0HucjmFrwOKjIW3rCuPaeGnOSVieepsqJRaBSJQnCldUqvlcPkJjG9rTZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHc3uAP0fNukem9zluxBRSF4jtJ1MXJry3z6mDMTnQIFL04tLcmFdfE5I5U4rZR_zjG0D7U7L7wXVDjevVySqbnHUXH8JTHQBR1dD5-jRSVwKEOgwa0FE9kZzBiBpJTA9tyuoAsarceDco-7CGFt95qhJ78gUgsDUBIhmM6CAozQWtWH-8stcLpsfoOnMKN3GvyycJpC0yU3J35Ba5C2epEyvjmEHNiZyhqVtTNd-WvCseIze9KwCpA97Maw15nVTp5P_vnU2DVFeHBIE6XBS78B-ynOOvk18SeayXqLxcNUhJ5r7OVF-qaC5QXtFTQR22ishEI-IzkuYHnwjZHR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWcohFMp3RPjTxe65kc-_xhRYakJBs9876zUSkD9OwEj7R2KWw3fdvB61Qx3APrkBjx_o3feaU9xu13-aPqS-xSVAhVGmTAErCk9bdM6GCdsBTNs4B6U0F8AfJMHMMQ1LG7fAcKdFCHRIBwV3TmbtFCsj9BNCvdhxPC1VBC8TGYE_G7mdoQ229mA120Op8gGfMKDS381G3rnbg4Z6X_Oyfd3H21idJHecdE7_vPD93s7sUHculVyOMOlIAiuXgBojcoQTCiMNkD4mAOqxCoKG66p_pGQWQEf3D3-1P_AhTIm9LWZWMD1_4WidE0eXCbgn_nYLTOGiST9Iu71QiLEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bdks4RKzauyAkpxIsZdAGbxDqaqs3KCAGI5rb1OhXiuay02TIPt3a4M5OVJHTav9xo9TT7zwGielaEDaFQBFvTzEBQ-9FIEyXNqoEvaQy2VNfbF98QscId0kRBw2XrSpACqxMPqansm2S0xcTtC514ra0LAP-vD0Bjv_lW7wjFIx15hnnk7IkUdGCvMxObvOgxFzcTDQa7tQBQGb3d-_q95HC6Vz9VdO5dF7v4UAq7U79geefO458Ern_GjVN-mbSEkE1HZtSr277ubeX4s6mdj_SZB2Qz7jXFgm_P_vRWyRY5BpiKLafdfGuuvyk3P4n47XsgyT4o8QNSkHQ2o-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiC-6QbYagJ2hWEiU4xL6qkCoZC_X8d3C-pDjaC1M24wag3Mzrzu_HeTKk56xAzjeCZ8EUqVujspoMEfGVvsoy2CPSA6qa9GXGDO9HzLEm8xa6B-ioDnmh8zOXQIZtsHi59BLUhGD95sUf8TjcmpLWUL9qQxPS67UzuVAlIMXskxNYj67xV8vZF1NwKK4pf2K8LPmt6sfe7UTBF7VLUvv2Uzc_Le_f8ca-3Hd8kEaXR5p6bu3TKcl-bI9VMx2mR90xJJhH3JBYYBfXW26kSbUxw20Z_F9_sd14VWWJAEid715GfVT_alyrj0HOE8KvHcjd0RiKxakhIn9AByJMCWCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۱ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457646" target="_blank">📅 00:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457636">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fxJe8Vi9l0XtnJYy9271beIMVzRRf8PEhvH4WRjZQdG0-O9HUHS-MAOP-Wqai6QgXq45lQ-FDoNqWd4DrWZ-YGzxQ8ELPwOAc0X2NME0Jijq6aC_4DnUYFGREyu1cY1vqs15ThXWehT2pu6t-2ZZLEksYVtDS9KN66XTA8t5Cdsxie2vN89QuiFuwasnd5qfuNRAfW14l1GREnVTZGPfDbFEYaZNjKPEInVnipv65lab3WBT59ZNVyjYjYKga2QjNgS1BdCJ4TYtwqt-vcdSyNEXMSo1BMlCS3KySAw-0JDY1S1VX8O6PZ96RDcm0cydKQIiV1a7qBMiNh7Iz0kZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O43OSuyCHjTqaNSOsM4TayqyUdmoCEwfJNvX-IZ9tgTTaBAuksv_ziZeU3fp-Dt4C6uRT0I1kBHYmKcxsFV_A_1tTbYGYh82R2rxDtpcEkeFbI90HUPCFW-0Xd5gvDNEV4v29OQ9IRCBzzC4mWz8M0ZTEoHXarbLgrrxtNeZF5OmbWsCJSvrkf8D5DkJNFTtT5xyIS6-GylSsNcqYN_i8hWMU5X6jxViu9pdbCqNso-VPrcGQujca54UfU1YvxvK_V-gY1QE-kOYfMRBDqilPGQ-lqO4g-7NPFvhwdvMCNwESv2F5BNcMuqdDBzj0xHDd-Iy4cQu18NTBhRO1aH91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhbWN7XvOjZ7NPVowPHoEObfYK54HEd1mhtAWBJkhKObOojUCHoOSeMxtW1UapVmovfiFKB0esqvta0dUyFVg5932jr4PF7kl91Af4s_2Iw1uhgQCegG1hwkidTXN1_JXGOEeHO1iwfamQhwZMtr7Jt4KAbW7L9wZbEgIO3QpXwoT6xRToJl09NYJUcsp8dSLv_g3eDTw746zWIl1od_aUPBnyn2BP445kuPdGb7RK7SbbEE39X7WnYqu9qyZSobxJ9bVuQ1swbfcAYQ8YKzK2UNHWyVlySdZNX8ihBjiCoWt_k9vSP4RbwxQApOklmqWEiRHr9Jfzlg0u89aToKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAXKmN0A2vHQpMsOowVDKT6tB0mEHi7RDaPUko2DSPgJ0So3mZ7pjevXHoMXLG__rYOrATHGoqK_OM23FzpbFhGmvT4u73uJPfX94QTMGk3EMbuJWUtX6zBHckgqynQ2LwR6EvqUMdAK7BBJP0bnKFLTmHhaHtsmTeDLWi6A9f0fbYyEIIvHA88tpL_BFx4f_ux7uBSk5De1fHI5Ft_xx7xqXNSFUE4WuJV45W7pQa7y059eNQlSAve493i-gDdCXoulc8d_a_0ENVO9nhDIdfknOsQF2aBYsYGpRLc9_D4Y_5ruvpMC8HLasCRWMLAOj2-3S3t29XzDp4H8Ii0xdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uu43W9lKUFgmepdlI9lTVWNnczH9jxXH5nP7hlFdnh137SkcU6LANxEM9GS3fagnviJTw7cROT-sW5qvDnDqBzYLkvoIPwG8lfart0GzsUlN-lwjGWf9iCytWKHJT2R0eVexHFqmIXZJLzkYhjedNO-E6xPdaslvZynseRnt5xbEmv6l-J3s84wWGRxcWlsXYAZGc5r2wE7XCES20Fo2sUna0tp3pMZCOI1fq1pAgzVV2j-E0KriJ5Ke1HxLitKS1oZoWyEAe-CV2vAyzcoS_6oZIG16gRXGr2QIbQNvzg4Mi6aH9W15E1IFSJKSCGZotvBUUj-vNk4iGFdh63U8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th_5yHZAXYSgB3R9M62pWZR0o23pcgHfTCdZdmW1CySDVtuvVXUL01b148KEgFYK87mMSyOGMhIIYTVsBPiIBV1R-eT5AYseHmGsFV7dOh-FiQSOvugwQADmfWc0qJHFqq4AWT_-ME0ntDCVgWbxavCxRWTOd2TAsTXmNoXuD1RQhP8QeJiFaC9yUpY4UaYXFTMKsV0xBej4ZpgyrKl3EW5KFEtKyD_todBnNdNuwuwcYv_9qJV0WFL7ABjvUWLevqvHlbKV_tLsIeTa4Jln8c3Phn3A1aS9QgSZFdbUeqPE7mP6qJEee_XU1vF0sxtUXD3FudEb5WX_zwTTyjuMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ro1MnzP9HOGGtc5CQIwo55U7KlAcOsbvx0f44xCeKfa9ikBDXwy2Us8P1WoSJhUOXNAXKh4rZg8RzipjhhNl2IeWwU_0p2UOXthZJbv5VEK8RD70ceM613HYh9NdTeo5JGzigTRhTAPx5YFuzun47qSU1bBWfzr455sW-KWhvN2xIuCtm44UPbqgMZ-LV0dwQlQ_D_-oNbHz9nlq-SroM-GK1cGDSM_RCUg_dorMQsyfMZptU_1vs7hsI5QpdSocRQxX_GDepp2aJyqr1muzYeSrg297OxKWZU-9tkS04Ft6Kzfmt-z8R-xN6Wn-IkIUygf4RZAr00o-lLYDM7ukiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmG_5fyXFCxCu0E6ASZN4a2Al_dZiF6LZJZiS3zH3oOQ-7O6c57RSSFhHIU0cA0iP0MyAdJywplWML_O8_prI34Mom--ZvZPGPU-kTrc4_Cemm6UHuABn29O-AjsywGV-yOEl1uz-1rjTxtfLRRaXxlrubg1PYumS1OSmUmIKm0R6x9BgottiXLp9qnroY7IzlHUWHjgnAHqcwVWEmgx6o0jXyNMWtT8R_6OBBx2hPz1XmWK9cXA5CeFFd2mjE2qBp2lv_qLkTZk98jYcd7yObpuT6ILCaK_kNUa4xN7xv-efe-7JJtOJPNRhIkMe7YxC2vXwAdQ5-W-5hWKChFEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUlMF3CTyY5p5Pp6bQ6KQa73o5BbpK7v9JB0QcU4CLzOyLQNJreY0YQ_OmkRM0rOQqJs58PWUelPtB56raZWWe2FL7I0sftyTBlizZmoVZv5DhoTut4yUcjVKAvJH8Nnv-p6XNR3OK486iSPIxJQE3y9Q4-0Ov7l9-RGomWb66bkJGQX-drdxftAtxgKt9DK8YDZZ2wmJQkyYZGc8h5G5ifxFLHum-oq_wAfSEY0SrPfSmRPoYEJNu33hyNjwg62GNbH_hI6IC2AGLnfldwhJ2utp-566hjl89AzEg80_62mB-w8-PeYGFFgN7oOSM39YjS0FzS6GtCwNM1NQPTu3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAWAOO-pVTqLpNXKONpQjFHva5kFBAHil7M7QYmEXp8hc7ub18mOl6aPHf2Q5xJxbvowNPf3HBi3PV65dTVeh8IVQt7WJdetfqvWsgO4ZWB-CxCpNU5zFDebBkGH14qv0LbmaRe69T03pXtBfQ5Hlxhm2B8IJtj81K-x8FGqrMPgQvTavE3sWmaZ3Ua4G-gyCk3SGFxtfLAt1mM51a4awEQ6feHd1cYRYSAxkY8Nf_McXkvkfF0X38BcyhoveYixwnDvMiH0ApF343KGBE2v5TiD2bovK_J0AxijxCJCEZVBa5_4wPKCGGeG2LRXsT_JYO6cN9wvbHZS9RyPPdUmeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/457636" target="_blank">📅 00:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457635">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuSwbMseKOByVa2kDO50-3sNXkylAoVPQBg1PBFZnXmEWFYHnAwMhZqkqTTrOovcim1POB9VGA-zvjg63qehq5VouQqtcPeOFhfQ-zq6_OVGWIVLNU16i3PMvdP5HvcBGpfZff1nUwjgay8mMCh6eJ4MAXONNTRzC-QdAyy0sTYDRb_vJE7GYTPkviPTiOG4aaxmI5r2Bjn6afGyvMZpvCV_QMkg9K2DbFfPCJGKfbgSSbQpNbtZpK-nrMsbc-FIddSfUsTIeek8IuK3UCHTawfJqSR3xjIkOA3p2UYeJexdGwGF5ctJN0Lg1pKfyk69j37Hg9nPsBPW2PUbijh6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی خطاب به انگلیس و فرانسه: حمایت از اسرائیل را متوقف کنید
🔹
معاون بین‌الملل وزارت خارجه: بیش از صد دیپلمات باسابقۀ انگلیسی و فرانسوی به دولت‌هایشان هشدار دادند که سیاست رژیم صهیونسیتی به سمت «پاکسازی قومی» و «محو فلسطین» پیش می‌رود.
🔹
آنان خواستار اقدام عملی لندن و پاریس در توقف انتقال سلاح، ممنوعیت تجارت با شهرک‌ها و اجرای تصمیمات دیوان‌های لاهه شدند.
🔸
لندن و پاریس نباید پشت واژۀ «ابراز نگرانی» از این وضعیت پنهان شوند؛ ادامۀ ارسال سلاح و هرگونه حمایت از رژیم، انتخاب آگاهانه برای همکاری و مشارکت در ارتکاب جنایات رژیم صهیونیستی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/457635" target="_blank">📅 00:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457634">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=KYc4X2adhSs9yL8LVEw2-XMq7QwAGlFERnKu3jx4t9mlJFI1CPDu0MN-WyBLDt75JNIg8eTG7ast6pL1Ycix7zq3rpM44grOY2_Jv7MXXrAKCPhuxkTL4WHQpqIFmKoFZjRZVp9m4s6SQu3dstAPMBAE3hsbvde_MJGAHwU2mwkheN2ml4YKCcNhfsb4you8wFU9IxMKUjTXgDJe9N_sKUo6L9Pa_FIBdjzW1aZaF_8GQ7VRoHaPGB2fDwbT4CfU4_rXCwSUxKSBiyvdZNMWpWJmIlsoydSkaj6CfJsrmOeJQ_xHyCG-Zgtr1bcgZ4puHz82oVRwNRzQRwqkqO0plA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=KYc4X2adhSs9yL8LVEw2-XMq7QwAGlFERnKu3jx4t9mlJFI1CPDu0MN-WyBLDt75JNIg8eTG7ast6pL1Ycix7zq3rpM44grOY2_Jv7MXXrAKCPhuxkTL4WHQpqIFmKoFZjRZVp9m4s6SQu3dstAPMBAE3hsbvde_MJGAHwU2mwkheN2ml4YKCcNhfsb4you8wFU9IxMKUjTXgDJe9N_sKUo6L9Pa_FIBdjzW1aZaF_8GQ7VRoHaPGB2fDwbT4CfU4_rXCwSUxKSBiyvdZNMWpWJmIlsoydSkaj6CfJsrmOeJQ_xHyCG-Zgtr1bcgZ4puHz82oVRwNRzQRwqkqO0plA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدۀ سه قلاده پلنگ در جاجرم خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457634" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnHYclMk5yEkYZeHByncqDirNXUgfcZ420smVGvMR20BmuBfp3Z4OZGuBVPYPtgUK5pnhjnDmszDXYVr5KYniekwA7OdmOdilygiBowKQY1su6HZsLkdl4aH9NgX5hwLKG4TFmzc6vLrWLj0YZx_tl8rWKCwJpyS8GdpetE67ocDAAgMzAKM-BHQVER9nQK2m4aXZDvp1aJsunTkpLbmkLFMSqf6FptL75qAFiniYhr20LnGMNIFnz7KTIelY7-lSxbLbl9YYwpJtdbzj9kDzDTZIihPls-5Of6NdsDrdZ49lmzt-YX9tXCeJZXnkvFWkr-fA5JNP9WkCs7pE6yqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCIqCvDPw6tvVuESS_7mGKk0n2LW9r6Fkg5K6zm7pfVEqLdAOiYXS9ETejfB98VCmFe57wofLi2r7TSrQtyb0UWD1b6gAuMfGaFFCW0dKOVCVbHTpPFaz0aINyxOhadN3Kz-QX940cTfWqL2GEDG9OA4AWz8nuu2TIG7tDIVw3nI8ULskeUKSPbvgC1Ubk8lpZM2NCKsovYyqvSTf77ymVBL95MCXgHySHC8XC7TQ4xAH-ui75juB3MeE-xXpPm3TODh93Rg3tRgTq82eEZKO1OY58W8Gfu8ypxQFgZWNVzuovF0WeAm1UVXA2VgEHn5NtqdONf8yvVBXwAZkkacVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدال یحیی و منصوریان در عراق برنده نداشت
🔹
در هفتۀ دوم لیگ عراق، امشب تیم‌های دهوک و الطلبه با هدایت یحیی گل‌محمدی و علیرضا منصوریان مقابل هم قرار گرفتند که این بازی با تساوی ۳-۳ به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457632" target="_blank">📅 23:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJEYo6zZ0Bh-KM9GX0EndHMgCg3vA3CFyFK2bBxpEq12_LjrEUCY-BF9bcqvefzk3qQfYIVf_zISIdUvwpmn2aVmf_K_s5N5AyT_87HFuGm-tii7QqUCO7PuJ8AsdUPZrHHVeT31Tb1wVveOCZwO5YRpaGOMsC6p2AvHQYXkR0qFLNnI3Zi3sqogXutzxaV3nlzys3dXh7JLOYD_8VcounruTgcEqdemInBCTznBpec5f3f0Of7WNyeaLsBQpbNvuV9ovu1BEv4NRrrZuu-5v353keZ_GBHYdtUCFgNcGxUPpwlQF94xHVa7qJE-cK5y7hkRaosNi9zkFgJUBxQgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا برخی اصلاح‌طلبان و دولتمردان، عجز را فریاد می‌زنند؟
🔹
وقتی ترامپ و ونس مدعی‌اند اقتصاد ایران را نابود کرده‌اند و هم‌زمان برخی چهره‌های داخلی می‌گویند «پول نداریم» و «نفت نمی‌فروشیم»، این دیگر صرفاً بیان مشکلات نیست؛ بلکه تکمیل روایت دشمن و ارسال علامت موفقیت فشارهاست.
برای این رفتار سه احتمال وجود دارد:
۱. توجیه ناکارآمدی
🔸
هیچ دولتی مانند دولت فعلی از همراهی منتقدان برخوردار نبوده است. اگر یک‌دهم مشکلات امروز در دولت قبل رخ می‌داد، اصلاح‌طلبان چه فضایی علیه آن می‌ساختند؟ منتقدان امروز اما به‌دلیل شرایط جنگی و منافع ملی، کنار دولت ایستاده‌اند. پس چرا دولت به‌جای استفاده از این سرمایه، همچنان به دوگانه‌سازی، دشمن‌سازی داخلی و نسبت‌دادن همه مشکلات به عوامل خارجی روی می‌آورد؟
۲.غفلت از پیامد خارجی سخنان
🔸
ممکن است برخی تصور کنند این حرف‌ها فقط برای توجیه داخلی یا شفاف‌سازی با مردم است؛ اما دشمن همه این اظهارات را رصد می‌کند. اعلام ناتوانی، فشار را کاهش نمی‌دهد؛ بلکه دشمن را مطمئن می‌کند که تحریم و تهدید مؤثر بوده است. هیچ‌کس جنگ‌طلب نیست، اما اظهار عجز می‌تواند دشمن را به تشدید فشار و حتی تحمیل جنگ ترغیب کند.
🔸
کشورهایی که نفت ندارند، چگونه اداره می‌شوند؟ چرا برای کاهش وابستگی به نفت، ده‌ها مسیر جایگزین تعریف نمی‌کنیم؟ انتظار برای فروش نفت و اداره کشور با درآمد آن، راهبرد نیست؛ نوعی تسلیم راهبردی در برابر محدودیت‌هاست.
۳. اشتباه یا طراحی؟
🔸
نمی‌توان دولت و عموم اصلاح‌طلبان را به مأموریت‌داری متهم کرد؛ اما سوابق برخی افراد، رسانه‌ها و حلقه‌های پشت‌پرده را نیز نمی‌توان نادیده گرفت. تکرار مستمر روایت دشمن، این پرسش را ایجاد می‌کند که آیا با یک خطای ساده مواجهیم یا طراحی هدفمندی در کار است؟
🔸
صدور حکم بدون سند نادرست است؛ اما اگر قرائن جدی درباره هماهنگی با بیگانگان وجود دارد، دستگاه‌های اطلاعاتی و امنیتی باید آن را بررسی کنند و در صورت اثبات، اقدام قانونی و بازدارنده انجام شود.
جمع‌بندی
🔹
تکرار حرف دشمن، چه برای توجیه ناکارآمدی باشد، چه از روی غفلت و چه در نتیجه یک طراحی احتمالی، به تقویت دشمن و تضعیف روحیه ملی منجر می‌شود.
🔹
دولت امروز از همراهی کم‌سابقه منتقدان برخوردار است. این سرمایه باید صرف حل مشکلات، پذیرش مسئولیت، ارائه راهکارهای جایگزین و تقویت امید ملی شود؛ نه تکرار مداوم گزاره‌های ناتوانی.
🔹
میان «بیان صادقانه مشکلات» و «فریاد عجز» تفاوت بزرگی وجود دارد: اولی اعتماد می‌سازد، اما دومی دشمن را به ادامه فشار امیدوار می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457631" target="_blank">📅 23:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dd39d620.mp4?token=G6SrEiUg7aZNXPBXKnILVgNxHOcXJzton_mttptqV4LXbtdJJ1RgEYztZpbsNcOd-up2XVPQ2lj5_oB2ud0XNYN-LNzW-qOqJ6tx9z9Kk-dPqUC9OReoOt8hrGJZt362SQ61G4K_M0fypFWnHH_azDJcLQ5tn8C9sF2g7GF1OdS7UvVgSoYygDKbgolmq-upViYx4AZpfsxKchCofgeg4T4RPky5UhwBZbU-x4grpaToZ9vQoFvE-d7olEyAtrn25cx7X4-_oI1k59UdeGbN61Jx0mLhwJViA995FtCKL149ARhiO2BrULywgltHhrj1k8VziGKmKh_u62_03ylc9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dd39d620.mp4?token=G6SrEiUg7aZNXPBXKnILVgNxHOcXJzton_mttptqV4LXbtdJJ1RgEYztZpbsNcOd-up2XVPQ2lj5_oB2ud0XNYN-LNzW-qOqJ6tx9z9Kk-dPqUC9OReoOt8hrGJZt362SQ61G4K_M0fypFWnHH_azDJcLQ5tn8C9sF2g7GF1OdS7UvVgSoYygDKbgolmq-upViYx4AZpfsxKchCofgeg4T4RPky5UhwBZbU-x4grpaToZ9vQoFvE-d7olEyAtrn25cx7X4-_oI1k59UdeGbN61Jx0mLhwJViA995FtCKL149ARhiO2BrULywgltHhrj1k8VziGKmKh_u62_03ylc9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: باید جهاد اقتصادی راه‌اندازی کنیم
🔹
دولت باید از اقتصاد دولتی بیرون بیاید و مردم را کمک کند که وارد جهاد اقتصادی شوند. هر محله‌ای می‌تواند تبدیل به پایگاه موشکی جنگ اقتصادی شود.
🔹
از یک طرف باید دست دزدها را قطع کرد و از طرف دیگر…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/457630" target="_blank">📅 23:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طوفان ادارات سیستان را تعطیل کرد
🔹
فردا ادارات و بانک‌های زابل، زهک، هامون، نیمروز و هیرمند به‌دلیل شدت طوفان و افزایش غلظت ریزگردها تعطیل می‌باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/457629" target="_blank">📅 23:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7860fbb8d6.mp4?token=sc8SqyJ1Ftxt8rLkR-awOifMkKvL9pO9YX4A0vXcHK40sR--hNCA4tnoNa_e58mfTPMLvzuu9uIX6kKiKlQN-orWuwATtF69sO2oVs-mYwNaCmnpUZcfM9ZiXr9fTpcjqlFCJsKQpWKhCrcS8tam4_WT_7x2jw-GZg8V0-aHfqQGFedCSrz8Y9oqc1aMOvLwXN0IEh4Xw9plR89sGosQqGKF5fCGCgeQuuTa84kd7Nm-VkwC25bASnzAFDLZwRwm4Lo7DMzpY1V43zAaCdnUau09xilJAbn4tMLm96wwX60NaP7ZZ_IzkJ9wyGWCmaKFTu0-01D-UvtTPWAHE4KoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7860fbb8d6.mp4?token=sc8SqyJ1Ftxt8rLkR-awOifMkKvL9pO9YX4A0vXcHK40sR--hNCA4tnoNa_e58mfTPMLvzuu9uIX6kKiKlQN-orWuwATtF69sO2oVs-mYwNaCmnpUZcfM9ZiXr9fTpcjqlFCJsKQpWKhCrcS8tam4_WT_7x2jw-GZg8V0-aHfqQGFedCSrz8Y9oqc1aMOvLwXN0IEh4Xw9plR89sGosQqGKF5fCGCgeQuuTa84kd7Nm-VkwC25bASnzAFDLZwRwm4Lo7DMzpY1V43zAaCdnUau09xilJAbn4tMLm96wwX60NaP7ZZ_IzkJ9wyGWCmaKFTu0-01D-UvtTPWAHE4KoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: حملات ما الان هدفمند است و جنگ اقتصادی را هم خنثی می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/457628" target="_blank">📅 23:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cec428b1.mp4?token=ryAVM8BvUw6yP2C3h_2tdmD45nghdAWUTYZUaD95Plzrui1Tm88ikH6AXoIUGUTLs9oSj7iulbb4L8K2eHdsTHduxFczhiIuhTj1sYQinQpsJUSnbmmx7lu1EGWKzly0aSlsQUI02GiLGMsJfHiI_yDXZHEs7jBVbUIjJ_d5CTV6OwxgTIhb_9_iU-kqOJmYdf1KVblJKDU1aLbFEYpRMVrOqM__jqOqul1tODIqmbpXgCo-yYrppCrIb6PPe_fMguZsw-lG4Qkua7BBE1UoaW98P_EbW5Z_QwZ-tBJJduPFi4X1JkEMFCaWESzVcY6fhebp1ytWStFUU0ZBH4I3Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cec428b1.mp4?token=ryAVM8BvUw6yP2C3h_2tdmD45nghdAWUTYZUaD95Plzrui1Tm88ikH6AXoIUGUTLs9oSj7iulbb4L8K2eHdsTHduxFczhiIuhTj1sYQinQpsJUSnbmmx7lu1EGWKzly0aSlsQUI02GiLGMsJfHiI_yDXZHEs7jBVbUIjJ_d5CTV6OwxgTIhb_9_iU-kqOJmYdf1KVblJKDU1aLbFEYpRMVrOqM__jqOqul1tODIqmbpXgCo-yYrppCrIb6PPe_fMguZsw-lG4Qkua7BBE1UoaW98P_EbW5Z_QwZ-tBJJduPFi4X1JkEMFCaWESzVcY6fhebp1ytWStFUU0ZBH4I3Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: به‌هیچ‌وجه تسلیم نخواهیم شد و جانانه تا آخرین قطرۀ خون از ایران دفاع می‌کنیم؛ اجازه نمی‌دهیم پای دشمن به خاک ایران باز شود
🔹
ما نیروهای مسلح تا آخرین قطرۀ خون‌مان را به ملت ایران هدیه می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/457627" target="_blank">📅 23:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfCE3cKl7Qp-fjOTnYqog6qI6iML0x7H8g9d6w1TqHtVu3fblR-40DDq5MdggGiBzlibISW_7HzjIcbfH-JWHZ1eat4Go4T4vVCHbGr0Fe1w1G2Nsfjv_rpHXCth829Jx7f-0IEJEwUtzvkOHSrbEuzTNjYfapNqgisxIcyQvwWiLmw_p994eVlJ-4Z0FPcHNqJrmoFoYgsjykBxr4R--4lH9v4utQ7vDQPqLOW6b7Pbe-f37Zg-nPPFdszGjrpjN6QeDQQUnt6streE8JLvoIaXNc4jWqQCmFUHKJupQekKpsSa8tSDjsZbvea43-dn6O9FakkS9GqS8kLZdlUidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJzyce2MATs74UWbBLwa60kwhjpNqOLMNpq-Ri6xUrujbG3o1g4YplPM_pNL5KAxm0f-0vLAjRHXx7dcb7ANBIlfBh8dgl7lOFJ3_F5m6eViln_H_TnJVtV2Anrw7RNaWI0j4xeSlPe-7F5yUBQqiD-EWMf2Dyfkw1UqN_99PXJPcIuXYfLGdiUwLitTGwoy4fAjeYeNMChtLT0u28rkwCnqZD56_NNU5mkHpyB3pKO62xDtQsBADO5xH_4bah8wteCF2thz51Fega5SyRo7xmOLxmLHeT7pRzJQYeAJFOpU9tU_M_9jHRnBc_Ux_yzKfFhMSo_oe0r6DTbeC5hF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwCbr08VLFGBzsI8ea2pWyPg-b1ceOaWvTmCEx6qGMrQRxmXR6P5YZdRkTkKUOrm-d4Ik38BGFV55uCK9sw2Ab_1SyvXMkeoIF7odBXBKhyfEpK84JCopHu34MRpGousHowoXxaFMs5b5rfKJapORNjynRMAS8RpPwcJ4idpfwyAuPZf_1ViZQEtCx4G2HzK7KCj9YCL330PpchOfclcNCPKz8a9sCqbld-4JNe1ZClwXear1fRMSQvpPjn8bjVuLwodlLdNlzvDS2Q46QN_v9AVXNBfqKvezGzR6tVAAQkef1nbatJlpU2ezK20HToRzgDX7Uq-s8kFAhOcuMgq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baRjjaPV8cmisWytxyG-Ekgvit9Wrz0wJ1RHW_hg7HBiPVLpce08nSUFcS6E2HIIQhlegB6-FixwMVHTEASAnSMa8SUkegDBDrsVDjdPIBlrEBWQyTZY2PGFwPxScwAZwJCYY8tZoc3fVSgK2nPFBRvI_mBsYZfhz-FCSJHoQvd5sewhE5M6FjujdoUM__w-IO39SqJ0A2yRfp_TFR9KKN2qKMra2J9jvbRbRQ4L_S3JRSY-uXNUpmqFsSqcMCbG4Z6c3wPr9DLNGgrV3Rsqz5z9ZCNGGC_wMUVocqA_QYay_HhizAqWn58tG4Cvk8Ih8hYjjkjfdlwbwfkxB34YBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJP3WPhMsHg5WG3uEfQntpArCkxM8NGBwETTweqktm7OE9TJGOQaeSkLiPL3Aeya6-3mLcaYEFZnelJ1NnDyrExdo_xKCoTjdqM-bLtW8naHy683VW_0V6QKPQQ_Uc9yLRuD7SywIpkjooMVTmDuTI0X5q3UQLLJqAhsJzfo-DB-eesoQ56FG-D6g3TPijUQ5scEvIXw2sJPoZKCaI-BQR8p4LFHubpk99HbdebAcrLLszLoXyIDGeUD3_vtse1BEap7b5BAFS_gYjPwZON1nIBejS9ARpN_dcLIS3xppA-Y7RWG4CHnibrS94eNB-_CisqNqCnnczM2B4CdDaYSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srnsGIbwYc4dY9igILXbRAxBCWXjM4R0ThTVYD-0D5l1L8bjqGkKWCG69zeIzR0E8kzt30vxYPYn9grbRpZCEhRgzc_yXXvS_5rohAHd_p0EndqppmHavZBMr3pjLxMz0noWkEv6YEkJUhLt3hEM9Xuh6FO5x0iRLczMvu4CFyV49DhPx-PZhgYZ1-kKUdrucLWrqasFkjazD8rKmW8B6dx1Yc3xDy57QS8CxMaZK25BRVRgYC7qA6Q6IgNVSGK00Smo0lk5RRjTQmppUxOL-agODmhbWp53zpth1r1FNDMPAHURwRH5tM1aef6GAyBBd-KnZ0pZc4ITuRpFEpX86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYUnpcjyQlpiJY0JRn1aC-zi9cdjVregAAH5G20vUmkeACEoaiNIiknGwcoSmmcW7elStY8N7jalviAlxFEVPmL06pQ8hMA78WjjEaryJGzwdOFA30uOTEeMuOLwhp9VFAIHSwMmBGGSRTot7OrPatHe9buD5oIZwZOdaJC8YochhPtqDmZtR3ZWdylSZn_F-qEd4gEhcb_lRV0ego2mKBL_JGR8QL63E9lUqSgYcxdOstWcVeAvEQqJn4k34BF8PoNYPGuUL4ZL3BDaI2u0iqHvsd8zBoqTguEX9OXVNAsU9uzDPpWMSJQa9KOdInW8g4Q0wKXmpRq8xf39c4FXmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نجاتگران به دل آب‌های مواج زدند
🔸
دورۀ کشوری مربیان جست‌وجو و نجات در سیلاب، با حضور مربیانی از ۱۵ استان کشور در شهرستان سامان
عکس :
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/457620" target="_blank">📅 23:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ea101e81.mp4?token=oQ6cIWYI1A-SjSGT--V1ooRripct1rzqUUr8TGy6l4D90thC12wRKD22dT85wa5yAJvgiNM_NYNHe8sZI-5yNFaZVr9D_-l_oYVlt4pxH6gdFstYIdYcWU304VbhAWuM3QJH9fBt0rlVlLWV0tW0jCzT3AILmBxA3Lbtbxjfq9VWrXl-7EzCeLHJDIzM2DoKmt16RiqtXz0vxcEpMESI3kqA40HkttXCwytmVoJOZWI3MBHu0Z3MulZyGq3G5oJTi7uis_i34bOR4X6bOgEUR3fngWuZKdJAOwNVNX6DAAFNV4V2bi9Q6hBPj8pzJTnAzLs7Kl8_fvHivCjQ0bCD3in23V201_7DtKStxWf7FPCaPZO2wyNRLIm6UrUsG0z47sa13s0zcyJ5OSNZMKTGaiZEFzitclr99lAfOnUQci67lh0ooalvr9Va2VstGLTaEi1N7PWSC8NAO8PxX9ZGAXSEcUD2y4XuMZCze53tmOOJ5FzXAeNTgG8Rx1LcWtVKaeShUp2nOFsUWH6MHO6XZFL_IZxZwo8F_bQleGaaT493pOXa7rQ68ohx8iOiYfl0YdgGu-G7ap8ECLI-NBuW_RTjYGnmv2CYrjy8LwIEZWHX5ekbFcp0xyfhRSOPJokpSQ7aRc1I-miwmOblk4ecypNwd8prP5qstUl49UZFEH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ea101e81.mp4?token=oQ6cIWYI1A-SjSGT--V1ooRripct1rzqUUr8TGy6l4D90thC12wRKD22dT85wa5yAJvgiNM_NYNHe8sZI-5yNFaZVr9D_-l_oYVlt4pxH6gdFstYIdYcWU304VbhAWuM3QJH9fBt0rlVlLWV0tW0jCzT3AILmBxA3Lbtbxjfq9VWrXl-7EzCeLHJDIzM2DoKmt16RiqtXz0vxcEpMESI3kqA40HkttXCwytmVoJOZWI3MBHu0Z3MulZyGq3G5oJTi7uis_i34bOR4X6bOgEUR3fngWuZKdJAOwNVNX6DAAFNV4V2bi9Q6hBPj8pzJTnAzLs7Kl8_fvHivCjQ0bCD3in23V201_7DtKStxWf7FPCaPZO2wyNRLIm6UrUsG0z47sa13s0zcyJ5OSNZMKTGaiZEFzitclr99lAfOnUQci67lh0ooalvr9Va2VstGLTaEi1N7PWSC8NAO8PxX9ZGAXSEcUD2y4XuMZCze53tmOOJ5FzXAeNTgG8Rx1LcWtVKaeShUp2nOFsUWH6MHO6XZFL_IZxZwo8F_bQleGaaT493pOXa7rQ68ohx8iOiYfl0YdgGu-G7ap8ECLI-NBuW_RTjYGnmv2CYrjy8LwIEZWHX5ekbFcp0xyfhRSOPJokpSQ7aRc1I-miwmOblk4ecypNwd8prP5qstUl49UZFEH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: ایرانی غیوریم، منتظر ظهوریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/457619" target="_blank">📅 23:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457618">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a14667a.mp4?token=rD5ifXmdaBRIsCv5mmVIZNNyqaYSvOCFXRsDdPuQeugYFRcNdxW8m0Rr4p5W0uXfsVwGDZJq8xL-gQtfubhixMii4CGZPvai79TgcnfXEm3a7xos1WS1ryfHya1RENnzm3BScNlXpBDB_eNRakLBkxLnPtfQlGt8K-BbKQxwXpcWJnUnSeTCDRoNpSQCTjB1-7HXIqMStobFOAnoVoWYDikNGazqkcLf50gcq_DElFvzgpyXO_zZ1lMEIn2SGuV6Sk5YDnzLjftkiEbqnkwtIbf8Hny_FI1LD3nTV2scxbzxJdw_Dtr7SR_QoHvNUpIt4SJASmKQVkoi_tHU6_Ceww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a14667a.mp4?token=rD5ifXmdaBRIsCv5mmVIZNNyqaYSvOCFXRsDdPuQeugYFRcNdxW8m0Rr4p5W0uXfsVwGDZJq8xL-gQtfubhixMii4CGZPvai79TgcnfXEm3a7xos1WS1ryfHya1RENnzm3BScNlXpBDB_eNRakLBkxLnPtfQlGt8K-BbKQxwXpcWJnUnSeTCDRoNpSQCTjB1-7HXIqMStobFOAnoVoWYDikNGazqkcLf50gcq_DElFvzgpyXO_zZ1lMEIn2SGuV6Sk5YDnzLjftkiEbqnkwtIbf8Hny_FI1LD3nTV2scxbzxJdw_Dtr7SR_QoHvNUpIt4SJASmKQVkoi_tHU6_Ceww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: جولانی هرچقدر توانست در مقابل آمریکا کوتاه آمد اما همین ۲-۳ روز پیش اسرائیل به سوریه حمله کرد؛ کسانی‌که فکر می‌کردند اگر پهلوی می‌آمد ایران گل‌وبلبل می‌شد این موضوع را ببینند
🔹
اگر پهلوی را می‌توانستند روی کار بیاورند ایران را…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/457618" target="_blank">📅 23:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63ee9ece7.mp4?token=UtAGAdW1gL8YmmUQAy9YhElnoRaxtDCRyMYywiyzA4P0dCASPVVbwg_byS-j2LTbTXSLcbLsxLA-0bGYhxYimUWkop4W42EiblgBLdpPq1EkWF_XXiyntIkIIcWxX8CcbqRGYJFCtlJrQUbh5kwmFszQYoW2-f-IS3wZjCpEccNhROqw61CnauniDio_CRjfLN4cYO2XMu4HoRd9PmXos1wwhbwcl3nBZf5Eg3aD1Vpa9JB3iER1Q8bx3tGswY59ZMDfuq4OBbMqEmfjfr9iK7Mzwu_pLa4T__3TrSrgVW6bgiFt9Jxdn11G_MVgiTfyBZYasvAvmbRaKSTZfg6Stw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63ee9ece7.mp4?token=UtAGAdW1gL8YmmUQAy9YhElnoRaxtDCRyMYywiyzA4P0dCASPVVbwg_byS-j2LTbTXSLcbLsxLA-0bGYhxYimUWkop4W42EiblgBLdpPq1EkWF_XXiyntIkIIcWxX8CcbqRGYJFCtlJrQUbh5kwmFszQYoW2-f-IS3wZjCpEccNhROqw61CnauniDio_CRjfLN4cYO2XMu4HoRd9PmXos1wwhbwcl3nBZf5Eg3aD1Vpa9JB3iER1Q8bx3tGswY59ZMDfuq4OBbMqEmfjfr9iK7Mzwu_pLa4T__3TrSrgVW6bgiFt9Jxdn11G_MVgiTfyBZYasvAvmbRaKSTZfg6Stw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: بازشدن تنگۀ هرمز هیچ ربطی به توافق ایران و عمان در مورد مسیر میانی تنگه ندارد
🔹
در زمان بازشدن تنگه ما آن را مدیریت می‌کنیم و این مدیریت با دریافت هزینه همراه خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/457617" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457616">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=lahq105LrDwvPjnoAKi6i_x6z58WTFpmLzNRE7SVizoMtp8nlZBpsGayycY-hNixwRKCxXddIGgetr800QvAihjTj7OvP0m_r8o1RLhqpJdDVNPSWtaAeoYFVjGM3PAWOKZFWMqgYsa0oqm-Wj8iPU8-IJ6lUZTCNyd-jAHjQ7-aZ1xRfdiZO2V6M7dW207Ha87dxHLy2cESxz6oHApbYyq-4tZxU5dy8Qy-dhkDq3x6-Q_PUNQg_OgSvXnzF9gll3ZJbp0cexZl15XLE6tfGwpPNHgburRQaIlm5yJKceQcC2F0QcYCf4uI6g58xR0VA7M_FXHcdOEiKFtv6zk-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=lahq105LrDwvPjnoAKi6i_x6z58WTFpmLzNRE7SVizoMtp8nlZBpsGayycY-hNixwRKCxXddIGgetr800QvAihjTj7OvP0m_r8o1RLhqpJdDVNPSWtaAeoYFVjGM3PAWOKZFWMqgYsa0oqm-Wj8iPU8-IJ6lUZTCNyd-jAHjQ7-aZ1xRfdiZO2V6M7dW207Ha87dxHLy2cESxz6oHApbYyq-4tZxU5dy8Qy-dhkDq3x6-Q_PUNQg_OgSvXnzF9gll3ZJbp0cexZl15XLE6tfGwpPNHgburRQaIlm5yJKceQcC2F0QcYCf4uI6g58xR0VA7M_FXHcdOEiKFtv6zk-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: کاملا آمادۀ عملیات هستیم اما با یک شیب منطقی و عاقلانه حرکت خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/457616" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457615">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023bde6b18.mp4?token=hXDZ9a0VYfwqiT3kdSxJpUW-SB0JymVT_IbcooygX2VmaVJskSi-j422-PcJmu65-hzg11duE_zrPLERXh85D5fAAjv6rduxLeArexREeNn_qzf0MCiUaLvA_hh5teflTY___4eiKgldv-7j5TBC9e3BT-ElMiidQQQU6L9OvHwy0CkAxxWueG1XjXBEFRC7pe79ubtP-cZVv0_GtbRhTSd4rvBDP8AZvWKX4ZmMMU0jgKVMaNu64LMCKB5av3VluD2dCjFv_uOphqkzpT_fJp3HmR--c93TGZqJ7u-8BVt3Jc7Md1WGgzp0W_b7ZDay9hrq7Uwp9iCpF4ORPT5gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023bde6b18.mp4?token=hXDZ9a0VYfwqiT3kdSxJpUW-SB0JymVT_IbcooygX2VmaVJskSi-j422-PcJmu65-hzg11duE_zrPLERXh85D5fAAjv6rduxLeArexREeNn_qzf0MCiUaLvA_hh5teflTY___4eiKgldv-7j5TBC9e3BT-ElMiidQQQU6L9OvHwy0CkAxxWueG1XjXBEFRC7pe79ubtP-cZVv0_GtbRhTSd4rvBDP8AZvWKX4ZmMMU0jgKVMaNu64LMCKB5av3VluD2dCjFv_uOphqkzpT_fJp3HmR--c93TGZqJ7u-8BVt3Jc7Md1WGgzp0W_b7ZDay9hrq7Uwp9iCpF4ORPT5gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/457615" target="_blank">📅 22:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=VWTnjQw-9LRichx7MYrB6NpYb9joXQnAz04ykrHZZX7edsmSyvKSMsvA01UgPCxIts7OwSDHFDYrG4SV4wEcw94-TjNceFcqaRaDRDe4PMPJ3pmz8sqL5B_QdbHltKRck3a-7Fr7pAx0oRQEJswdHWGS9HrgyM9EOwcRwLj6OkkAirXBX0EUtEIhi3osS4L-y7lJhEvwiHNVpZdGdSp5DA0tyts0VmvOEjjK6wUy7bR4fkbh-Ghy6B0jwafXPHWxIOTe1Jj2ft9hEylJnAmKksUJ8WI0iCzIfjJivdlr2O9RbN0Py2UlgUMWK-KCGHIWatEk4IZvzYpjE_3-GxJc8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=VWTnjQw-9LRichx7MYrB6NpYb9joXQnAz04ykrHZZX7edsmSyvKSMsvA01UgPCxIts7OwSDHFDYrG4SV4wEcw94-TjNceFcqaRaDRDe4PMPJ3pmz8sqL5B_QdbHltKRck3a-7Fr7pAx0oRQEJswdHWGS9HrgyM9EOwcRwLj6OkkAirXBX0EUtEIhi3osS4L-y7lJhEvwiHNVpZdGdSp5DA0tyts0VmvOEjjK6wUy7bR4fkbh-Ghy6B0jwafXPHWxIOTe1Jj2ft9hEylJnAmKksUJ8WI0iCzIfjJivdlr2O9RbN0Py2UlgUMWK-KCGHIWatEk4IZvzYpjE_3-GxJc8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند.  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/457614" target="_blank">📅 22:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=eMqrBEv1xQqSOtzaePa5bNEvXI-hl2H3MDLG3B5KvEM1jOcOVF3o3tonQfgJchKWdGszCa0ikQXKKzlSrk946v1vdSnU1F_PhutF4jOsf3FP8m9tXu1pbiRV8jkcPrGVGZONpQL6zWojs15Xy4gBxJs0-6ZJRCpDPW2Sl247lb0HHdnnC16pRDCrJ3fpE4OpMYC6UqIqVGyz69E2szljx0xIVECujI2kLdf2CV00FWiI48hu64BYG8X48yAeL60dA9jVy6iR_V1uRUVoWrY0xEtyUBRqP5gqUlvQw5pWa_aPVGC8UG39xrhwAI_mmx9L4S2ryzbvt1e_7bEOsWPLug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=eMqrBEv1xQqSOtzaePa5bNEvXI-hl2H3MDLG3B5KvEM1jOcOVF3o3tonQfgJchKWdGszCa0ikQXKKzlSrk946v1vdSnU1F_PhutF4jOsf3FP8m9tXu1pbiRV8jkcPrGVGZONpQL6zWojs15Xy4gBxJs0-6ZJRCpDPW2Sl247lb0HHdnnC16pRDCrJ3fpE4OpMYC6UqIqVGyz69E2szljx0xIVECujI2kLdf2CV00FWiI48hu64BYG8X48yAeL60dA9jVy6iR_V1uRUVoWrY0xEtyUBRqP5gqUlvQw5pWa_aPVGC8UG39xrhwAI_mmx9L4S2ryzbvt1e_7bEOsWPLug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما فعلا فقط جریان نفت در تنگه هرمز را محدود کرده‌ایم اما درصورت جنگ اقتصادی اجازه نمی‌دهیم نفتی از خلیج‌فارس حتی به روش‌های دیگر خارج شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/457613" target="_blank">📅 22:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=BZZPE7vENL5BgNCZeXfZv3TtGXepbYUGFx903GksoNA6nETH3OMvr4g8LY-971HUM_5bsVFnlap346riel6hfYHouYaYXflANoGTYfTIBHjSlQjYbbkRLI29VCr8YXEzHzXwop5dqHyMfoAazEXQWDHkjIRRZwvBeICJ_jIP8aa8CUsOkFKnthvpEtgef84rTG9YVONIu2LyNFMxMUyA9gt63k3b5yOpBmhhh3y3HVLrZlobW7Nx6vk6i0VQUk20XzfghPsiTLhBMMpQ4oSNChSlgyZF1UpRMvKaTMPGUdPq6zb70fAyIzqxIu1LI_uX0kiwQSRojvmeMiZBICvEYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=BZZPE7vENL5BgNCZeXfZv3TtGXepbYUGFx903GksoNA6nETH3OMvr4g8LY-971HUM_5bsVFnlap346riel6hfYHouYaYXflANoGTYfTIBHjSlQjYbbkRLI29VCr8YXEzHzXwop5dqHyMfoAazEXQWDHkjIRRZwvBeICJ_jIP8aa8CUsOkFKnthvpEtgef84rTG9YVONIu2LyNFMxMUyA9gt63k3b5yOpBmhhh3y3HVLrZlobW7Nx6vk6i0VQUk20XzfghPsiTLhBMMpQ4oSNChSlgyZF1UpRMvKaTMPGUdPq6zb70fAyIzqxIu1LI_uX0kiwQSRojvmeMiZBICvEYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها هر نیروی جدیدی به پایگاه‌هایشان اضافه کنند آن پایگاه را می‌زنیم
🔹
آمریکایی‌ها هر حرکتی در مسیر جنوبی تنگۀ هرمز انجام دهند هدف قرار می‌گیرند.
🔹
آن‌ها هر جلسه‌‌ای با گروه‌های ضدانقلاب در منطقه برگزار کنند ما آن‌جا را…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/457612" target="_blank">📅 22:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f680f0b1b5.mp4?token=IQISc2H-r1Q1YEvnBmyVkj1AIqR6RJHFtVjufZy4WQSWrSXLfTtAaVk9vggt4Ua6329M1aQNcuNrb6aaiVbWbK5MCD9OATHb4JiVt2TzI6RG6X16M4iYTObcX6KwP1nn65SF-UY1zD2p4eI40hFUOiuFXPpXt50AT3VePBSwB-QceI5w1qf85GhVvxFUv4efRAhqrYoYSNqLzlUtK4Ur92fiKyaLafw-R_-P1bexRGEnGflWO6dos8gnhbhPDVnc73zVf599qygHkFBitCr7NVOsHi7f2p5bLe1s6cKgPEohn5m34Jtw7T4cs_6pPFk2zZ6AldmFi0-h-HGB1h0HFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f680f0b1b5.mp4?token=IQISc2H-r1Q1YEvnBmyVkj1AIqR6RJHFtVjufZy4WQSWrSXLfTtAaVk9vggt4Ua6329M1aQNcuNrb6aaiVbWbK5MCD9OATHb4JiVt2TzI6RG6X16M4iYTObcX6KwP1nn65SF-UY1zD2p4eI40hFUOiuFXPpXt50AT3VePBSwB-QceI5w1qf85GhVvxFUv4efRAhqrYoYSNqLzlUtK4Ur92fiKyaLafw-R_-P1bexRGEnGflWO6dos8gnhbhPDVnc73zVf599qygHkFBitCr7NVOsHi7f2p5bLe1s6cKgPEohn5m34Jtw7T4cs_6pPFk2zZ6AldmFi0-h-HGB1h0HFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ ما به ترامپ مقابله‌به‌مثل زلزله‌وار خواهد بود
🔹
به هر کشوری که با جنگ اقتصادی آمریکا علیه ایران همکاری کند ابتدا تذکر می‌دهیم و اگر ادامه دهند منافع آن‌ها را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/457611" target="_blank">📅 22:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dff8f0bd5.mp4?token=TNA81KIYJfHGpIFtbtnQ330XuodYJjVsiiCbcUTn341-ynVOmBgSFfYfrvg3H8crkArV-o34UymboTALXovFmC3FTCs1P-qXqe87swz9Sdkt7rZdOLufO8ph6mYsaV_TT-VNomL-KUf8moPoygkQcktE_zz793JdpRgP8c-OS0KsWiMLYm21Fi5AEtXfoTl4MeMHUQ76DtieSst_I-Rhg3GuzPmnxdeM4PX2whiXhwsmWKM1sRJbcJ0iHb8pv2vwJuZBmMVm5O9BQ0S7ww4XfR3oWOu04Pv03RgFTRNRy3y5JXpMw5NcSSSKNj8Lh3YLyYu25KQo5CAZZ2wJRH3hUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dff8f0bd5.mp4?token=TNA81KIYJfHGpIFtbtnQ330XuodYJjVsiiCbcUTn341-ynVOmBgSFfYfrvg3H8crkArV-o34UymboTALXovFmC3FTCs1P-qXqe87swz9Sdkt7rZdOLufO8ph6mYsaV_TT-VNomL-KUf8moPoygkQcktE_zz793JdpRgP8c-OS0KsWiMLYm21Fi5AEtXfoTl4MeMHUQ76DtieSst_I-Rhg3GuzPmnxdeM4PX2whiXhwsmWKM1sRJbcJ0iHb8pv2vwJuZBmMVm5O9BQ0S7ww4XfR3oWOu04Pv03RgFTRNRy3y5JXpMw5NcSSSKNj8Lh3YLyYu25KQo5CAZZ2wJRH3hUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ به اسم عملیات آزادی ۳ ناوچه به‌سوی تنگۀ هرمز روانه کرد و وقتی هر ۳ ناوچه را زدیم، او ۴۸ ساعت بعد گفت عملیات را متوقف کرده‌ام.  @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/457610" target="_blank">📅 22:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c27175536.mp4?token=rWcXmwXPoDCro2aK49E1bxnR-gMbt9lQJH-ZQ8Ds0Tf04MZ-JiCNAl7r5WbmgPr25zoeIC47KUQjUUoZJYXvLOK9viEh7tyB-XBmO4kdYhL055Gn4XuzymGiNVstV4iMzx26Kdqs5prPtP1Hu3fEDkL5hZGRXXMeFI3tvfeMXwLcvEF3qTeVozPVDCDon6l5hlEjVk1WOpBKL9e3qGFeQxm3rky0IiI4enlJitay-6UVdTRlkmrq8LXaN1NMwU2WKDLA5ICbcK4SGh_3Gh0ADV04c2NBOhbGjhTpGOpHPvod1NKSzKDijmvGb9XswYKE2QAL892fZbdVWn04W9v-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c27175536.mp4?token=rWcXmwXPoDCro2aK49E1bxnR-gMbt9lQJH-ZQ8Ds0Tf04MZ-JiCNAl7r5WbmgPr25zoeIC47KUQjUUoZJYXvLOK9viEh7tyB-XBmO4kdYhL055Gn4XuzymGiNVstV4iMzx26Kdqs5prPtP1Hu3fEDkL5hZGRXXMeFI3tvfeMXwLcvEF3qTeVozPVDCDon6l5hlEjVk1WOpBKL9e3qGFeQxm3rky0IiI4enlJitay-6UVdTRlkmrq8LXaN1NMwU2WKDLA5ICbcK4SGh_3Gh0ADV04c2NBOhbGjhTpGOpHPvod1NKSzKDijmvGb9XswYKE2QAL892fZbdVWn04W9v-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما هر روز به اندازۀ تولیدمان آن‌طرف ناوهای آمریکا نفت می‌فروشیم  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/457609" target="_blank">📅 22:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139d0743e4.mp4?token=aRCjhVt_i4RAiXTT755AsekqkTb2DywfYYrcHYLfU89b2gMf1YUCOKSgD2zp6gP59uMzscZC2J8AKnK1U8oJffp8Qdwh98UTkRtcQRa0o8tlZ8PoGvgw20NMm7QTXi7GQmy-K_LHDbVWpQxyaarhwmqvX0pWN935TG8OIpr97nFoAQf2J5jtxubJJEaUz5cj2kQojfY3YUbAf5x0vfD0moSCuO31yiMSo_vtrJP9MqVdEqhofp2ugukEkcTviW5ZLuHy7bfLGLchfjcRjZxHyN9OjPAZWNDhgBsXwc2luDY2Kn_wYgbdBD6LHxtSr0hWc4EVXiV_x1a_4tIdOYl0sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139d0743e4.mp4?token=aRCjhVt_i4RAiXTT755AsekqkTb2DywfYYrcHYLfU89b2gMf1YUCOKSgD2zp6gP59uMzscZC2J8AKnK1U8oJffp8Qdwh98UTkRtcQRa0o8tlZ8PoGvgw20NMm7QTXi7GQmy-K_LHDbVWpQxyaarhwmqvX0pWN935TG8OIpr97nFoAQf2J5jtxubJJEaUz5cj2kQojfY3YUbAf5x0vfD0moSCuO31yiMSo_vtrJP9MqVdEqhofp2ugukEkcTviW5ZLuHy7bfLGLchfjcRjZxHyN9OjPAZWNDhgBsXwc2luDY2Kn_wYgbdBD6LHxtSr0hWc4EVXiV_x1a_4tIdOYl0sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🔹
اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند یک قطره نفت از خلیج فارس و تنگۀ هرمز بیرون نخواهد رفت و مسیرهای دیگر صادرات…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/457608" target="_blank">📅 22:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e531d1f234.mp4?token=nSplXKuxrvm7cukn45vuxrHSNjQo6YyYDRAPTdj2lqqJfrZiRx78zsKD9Gqft63y9klf9kNhc__FAsoax_4YWySIeICdrBNUeRkOvTtUp0xEi1MyzNpqHbl_DSOIRQBh1moM7_810CL3XmXQAMADCr4ju27GkaOFj2kfj7UhXU9Fpqb_G6q8RXp0thNU8SmK63vAKeDzfPk640EfUD5krs4JFKj4tacEi9IIuZRapj0_jq5JW0Xg8CqY66IJ8zcLoJrkrdQP-17Millr5bUSKEw0ZfkIu_KEzRJIx8wrdVZgncoq-cr-p72EbEeX8tucUwuCEK-KqSFS1xP8oDk1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e531d1f234.mp4?token=nSplXKuxrvm7cukn45vuxrHSNjQo6YyYDRAPTdj2lqqJfrZiRx78zsKD9Gqft63y9klf9kNhc__FAsoax_4YWySIeICdrBNUeRkOvTtUp0xEi1MyzNpqHbl_DSOIRQBh1moM7_810CL3XmXQAMADCr4ju27GkaOFj2kfj7UhXU9Fpqb_G6q8RXp0thNU8SmK63vAKeDzfPk640EfUD5krs4JFKj4tacEi9IIuZRapj0_jq5JW0Xg8CqY66IJ8zcLoJrkrdQP-17Millr5bUSKEw0ZfkIu_KEzRJIx8wrdVZgncoq-cr-p72EbEeX8tucUwuCEK-KqSFS1xP8oDk1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🔹
اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند یک قطره نفت از خلیج فارس و تنگۀ هرمز بیرون نخواهد رفت و مسیرهای دیگر صادرات…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/457607" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedb855132.mp4?token=ZRZvjJt-ImFSWVZXWltHj2pvOfUImgwdEIfX49oC_LyLvlwlvE8KXwnGdw3ZCBjlDyVi9HrV0ryhJHymiD3eZHIKxRexUa4DKY-xeFEIJjjkWUEG7c9ziGdT0Z5MFtpWMB-ZUO41hJIHfEYaHEj1vHyxWLzMV4dctFyGydKxa-ik_VzkE8iuk2eQNBW_cE-fp5_W2uN9LFec3QNlHuCi27jjQDszPUBq5Fem9E_nJdDPYoqbkF8sggC7YyRS8slIcvjewhK6Qf0Pph44AsJC7JZ4kMpVe6Gct11wOtBZ3gsn1Zm64PjHHY2tmqbUYdfY7HVyjjMl8uz5qQChI1CsAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedb855132.mp4?token=ZRZvjJt-ImFSWVZXWltHj2pvOfUImgwdEIfX49oC_LyLvlwlvE8KXwnGdw3ZCBjlDyVi9HrV0ryhJHymiD3eZHIKxRexUa4DKY-xeFEIJjjkWUEG7c9ziGdT0Z5MFtpWMB-ZUO41hJIHfEYaHEj1vHyxWLzMV4dctFyGydKxa-ik_VzkE8iuk2eQNBW_cE-fp5_W2uN9LFec3QNlHuCi27jjQDszPUBq5Fem9E_nJdDPYoqbkF8sggC7YyRS8slIcvjewhK6Qf0Pph44AsJC7JZ4kMpVe6Gct11wOtBZ3gsn1Zm64PjHHY2tmqbUYdfY7HVyjjMl8uz5qQChI1CsAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: وحدت بدون تبعیت از رهبر انقلاب اصلا امکان‌پذیر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/457606" target="_blank">📅 22:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef87d4b16b.mp4?token=WT4iCZVmR1hB9v9jiSBA8c4EphxpLS8MUu3JBkiZSUvpZK88Azw-uQOj1p6C1Hl22hRbS_XCYRSWx8SRZwVRU4Chylpn3OI2EjNbI8v1D-Wb51gfgleSYY0TUszX3Ncl9Q5PZt5UEEXHIEWOZxV2dLYFtiAFVfaoPsH1n34b8Dy1hNMg8_DQ519fnqUiUOwGs2NJnyPZNyBqZbtdxB2fS-JCVXocHD-CnVKkkpiyhFGycm6RLIL3i80IsHZPp8caXOB2fLs1nRtWY6fbd8E9dspD8ykUIORDsbHZF1pvbkHhFUzXuCIKukPzrO5MabpVRXeycOT30VYiopqEx2Le5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef87d4b16b.mp4?token=WT4iCZVmR1hB9v9jiSBA8c4EphxpLS8MUu3JBkiZSUvpZK88Azw-uQOj1p6C1Hl22hRbS_XCYRSWx8SRZwVRU4Chylpn3OI2EjNbI8v1D-Wb51gfgleSYY0TUszX3Ncl9Q5PZt5UEEXHIEWOZxV2dLYFtiAFVfaoPsH1n34b8Dy1hNMg8_DQ519fnqUiUOwGs2NJnyPZNyBqZbtdxB2fS-JCVXocHD-CnVKkkpiyhFGycm6RLIL3i80IsHZPp8caXOB2fLs1nRtWY6fbd8E9dspD8ykUIORDsbHZF1pvbkHhFUzXuCIKukPzrO5MabpVRXeycOT30VYiopqEx2Le5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: همۀ جهان فهمیده‌اند ترامپ خالی‌بند است  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457605" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f05e55a7.mp4?token=iqpngU5SOBhYW6IdKknHb3e5ccnyI1JPPt2HnJZD0MTI2rmAtRVWqgihe4pcHhHdd_v2tYkGoC8gkdTfCxwvyXYVmhpb7xr4ShKupBdW3sfdNu-difY-ik0F9f_RII36q6zR7ZFL8Zv-bRetwFZ22tL7CDUDVKinMSXLmA0M60fMe6dhe0DhMuXzMTmIaT0ZcoCZeW_yWUE6PLGkLY3jJ0eevkTjtdsW30Y08-SyFt-38GtJqsBorkY9DcvnLAEGebU0biNPzS5jdP1J6DOeMvhKBbmX42jiGGoWpt7c8uIE9Ol7OmF9J1TRQhtCqznbhrWLpg8vKd4mASAXrgx3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f05e55a7.mp4?token=iqpngU5SOBhYW6IdKknHb3e5ccnyI1JPPt2HnJZD0MTI2rmAtRVWqgihe4pcHhHdd_v2tYkGoC8gkdTfCxwvyXYVmhpb7xr4ShKupBdW3sfdNu-difY-ik0F9f_RII36q6zR7ZFL8Zv-bRetwFZ22tL7CDUDVKinMSXLmA0M60fMe6dhe0DhMuXzMTmIaT0ZcoCZeW_yWUE6PLGkLY3jJ0eevkTjtdsW30Y08-SyFt-38GtJqsBorkY9DcvnLAEGebU0biNPzS5jdP1J6DOeMvhKBbmX42jiGGoWpt7c8uIE9Ol7OmF9J1TRQhtCqznbhrWLpg8vKd4mASAXrgx3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ می‌خواهد بازی جدیدی به‌نام جنگ اقتصادی راه بیندازد که حسابش را خواهیم رسید.  @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/457604" target="_blank">📅 22:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457603">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=AJ0vTpRRsYSy9M4UX_rF8uGBiPvWrFbc58Z-WY6WS_w77cOVhGXnYP0eN0JWpJqhhVB8seUAQiv-mQ7iyUlwqj1WhLPrBxH5kDtJt9zuIGI5TwFXwLj4VI4sN-bF7Bn5doHE0oAxge5e-ArM5HFI1zIG02oifLDfeoOQBFvLVFzKmT1P2sHsKwZT1B__5qaO5PlCJkpiEcfhxIt2x7Nu_qZJRPrLpB3rkuEApSzJnOIh_fDxce3l7jowCEiWDjpe1fhiHRHsJI4tMnEDX7dFCA2ZjzqDTpvZgcRuN8CwarYYGRSARbOzZup49GzHbpmpA-KeTjQiY68MRLDQONnhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=AJ0vTpRRsYSy9M4UX_rF8uGBiPvWrFbc58Z-WY6WS_w77cOVhGXnYP0eN0JWpJqhhVB8seUAQiv-mQ7iyUlwqj1WhLPrBxH5kDtJt9zuIGI5TwFXwLj4VI4sN-bF7Bn5doHE0oAxge5e-ArM5HFI1zIG02oifLDfeoOQBFvLVFzKmT1P2sHsKwZT1B__5qaO5PlCJkpiEcfhxIt2x7Nu_qZJRPrLpB3rkuEApSzJnOIh_fDxce3l7jowCEiWDjpe1fhiHRHsJI4tMnEDX7dFCA2ZjzqDTpvZgcRuN8CwarYYGRSARbOzZup49GzHbpmpA-KeTjQiY68MRLDQONnhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: حماقت ترامپ دنیا را به سمت دستیابی به بمب اتم سوق داده
🔹
حماقت ترامپ با حمله به ایران اشتیاق مردم جهان به بمب اتم را بیشتر کرد زیرا همۀ دنیا دیدند عضویت در سازمان انرژی اتمی و NPT برای جلوگیری از حمله آمریکا اثری ندارد.
🔹
ترامپ به…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/457603" target="_blank">📅 22:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef3531947.mp4?token=p7kt8nearoYLZ2NqP2OzW24bRhHik1n3q_LcS7aKbr36qDW5oqgfgPjUsMo_WV7XDlbT3c-3rLvx21rjYrD96gQBgkofw4Lzn9BuAQEnzwfTwvrTtVoK30bldTNZevMtDZGUeQO0Fyd8E4ESlOTu7CyMu8W88R9bMW5N1dtmbM18WMuPgpmWbW9mr75n0SgIvbKoxy5Jdsm1fM9p9cuty8Bq8nB6AzOrp0IUkjI9UOBiaaG4xFkIuqEcBZUridrQ10pxTd033JAitozic6nG2hm05If6QOSbQKmNw_FABJ7ktOEYl9H5rL8uSS6aFSPbTjGEZLBqxgIhy3pHQ8ASdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef3531947.mp4?token=p7kt8nearoYLZ2NqP2OzW24bRhHik1n3q_LcS7aKbr36qDW5oqgfgPjUsMo_WV7XDlbT3c-3rLvx21rjYrD96gQBgkofw4Lzn9BuAQEnzwfTwvrTtVoK30bldTNZevMtDZGUeQO0Fyd8E4ESlOTu7CyMu8W88R9bMW5N1dtmbM18WMuPgpmWbW9mr75n0SgIvbKoxy5Jdsm1fM9p9cuty8Bq8nB6AzOrp0IUkjI9UOBiaaG4xFkIuqEcBZUridrQ10pxTd033JAitozic6nG2hm05If6QOSbQKmNw_FABJ7ktOEYl9H5rL8uSS6aFSPbTjGEZLBqxgIhy3pHQ8ASdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: حتما در مسئلۀ ادارۀ شیوۀ جنگ تغییراتی خواهیم داد و در رفتار دیپلماتیک ایران تحولاتی صورت خواهد گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/457602" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb594bb4f.mp4?token=d12XNl-BNK6altPaYxpXwM4PO8dWq0LhXUQarXLU-YMz80wNrEqJr-mmEOQkZcySwbyh39aW6oTek61Mgk2J3opsFQTupA82qhJ7A_0VsPFRrqFdXU_YXFgRUsQToRV1DCfu5w6LdHWZrWoJxDoBYOfo0ScQaMgica4xvG4H2_twdFITk9TdMGh3b6tnlmvmjlsdsTl5KS6gWiidYx_oexR_rfZUQeLKWZ0CURNEkjlYC95oTB5r5udwki819EPI87QYTr-LDig3-s4ic5ZY30EvKM-hc5Wkl9aKUSh2khVA0GmurpKk01H8Wcjz4VXfPmU4FJY5fdpQVGc_61QUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb594bb4f.mp4?token=d12XNl-BNK6altPaYxpXwM4PO8dWq0LhXUQarXLU-YMz80wNrEqJr-mmEOQkZcySwbyh39aW6oTek61Mgk2J3opsFQTupA82qhJ7A_0VsPFRrqFdXU_YXFgRUsQToRV1DCfu5w6LdHWZrWoJxDoBYOfo0ScQaMgica4xvG4H2_twdFITk9TdMGh3b6tnlmvmjlsdsTl5KS6gWiidYx_oexR_rfZUQeLKWZ0CURNEkjlYC95oTB5r5udwki819EPI87QYTr-LDig3-s4ic5ZY30EvKM-hc5Wkl9aKUSh2khVA0GmurpKk01H8Wcjz4VXfPmU4FJY5fdpQVGc_61QUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: حتما در مسئلۀ ادارۀ شیوۀ جنگ تغییراتی خواهیم داد و در رفتار دیپلماتیک ایران تحولاتی صورت خواهد گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457601" target="_blank">📅 22:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa8cb4422.mp4?token=efBQu1zuK1FXLVsPpldtZ0nf6QNa3Qchap6qIAbWE0jBOCNgNUtFyneHZCqSOX95Xe5IUiDASjI30HYw_K2q1H1NfVESEbqAxzuYxNcHq6568I35qAN0OQpqor2AE0L7r4OnOPBiU4lMQDTHpt7fcot2vpTpO7S4rgkSj1d-z0VqWRCC_eEzpj8kCZLtuGAXVduXep-3Xd8C15gSddSXmDC3DfKpFR9zvFNbquSoYSJNnZMUz0Cx1C2fdtrrImOAIcTG7QfzSrThH28rS8QEifOrkFdD8ve5KwNK28QQcdm5ZcwPfLnjDgEMBq9gv72ap4vGtvI6ZVD_3x3WtrKt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa8cb4422.mp4?token=efBQu1zuK1FXLVsPpldtZ0nf6QNa3Qchap6qIAbWE0jBOCNgNUtFyneHZCqSOX95Xe5IUiDASjI30HYw_K2q1H1NfVESEbqAxzuYxNcHq6568I35qAN0OQpqor2AE0L7r4OnOPBiU4lMQDTHpt7fcot2vpTpO7S4rgkSj1d-z0VqWRCC_eEzpj8kCZLtuGAXVduXep-3Xd8C15gSddSXmDC3DfKpFR9zvFNbquSoYSJNnZMUz0Cx1C2fdtrrImOAIcTG7QfzSrThH28rS8QEifOrkFdD8ve5KwNK28QQcdm5ZcwPfLnjDgEMBq9gv72ap4vGtvI6ZVD_3x3WtrKt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: تصمیم رهبر انقلاب برای آمدن فرماندهان باتجربه معنایش این است که تجارب یک‌سال گذشته حتما در نبرد آینده استفاده می‌شود و جنگ آینده متفاوت‌تر از جنگ ۴۰ روزه خواهد بود.   @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/457600" target="_blank">📅 22:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d6787c0.mp4?token=s6AM756HEBq4SqJaxef8pgVAqaPQoS093BsPYLRiv9VRkx-9e-BVKHCuiSZrNRHcp81KluGhhh846bBU9AMXAyaB3fQYqZwPydkpx0bRE3o_7XKI_m0Vf-0WFnFgOsA_JgZlynw101SN_X0_RVuXORhU80uYqnFH__4PHNmpfRPEo2GPcEazBgvMp1TXzmnd-h8SUFz3JoF2fU5qQx8QG9r0euon-SgHFUf5KupBRshuiMxVncdF6EC3JQSFFeiku3QklZvhuAE7OOpUICfOrlZI-39DcxPPW-c28kZ1lEuogfVAy2oLqvZrI8x88b_KnANjcAJ61rFMjCA3V4vDog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d6787c0.mp4?token=s6AM756HEBq4SqJaxef8pgVAqaPQoS093BsPYLRiv9VRkx-9e-BVKHCuiSZrNRHcp81KluGhhh846bBU9AMXAyaB3fQYqZwPydkpx0bRE3o_7XKI_m0Vf-0WFnFgOsA_JgZlynw101SN_X0_RVuXORhU80uYqnFH__4PHNmpfRPEo2GPcEazBgvMp1TXzmnd-h8SUFz3JoF2fU5qQx8QG9r0euon-SgHFUf5KupBRshuiMxVncdF6EC3JQSFFeiku3QklZvhuAE7OOpUICfOrlZI-39DcxPPW-c28kZ1lEuogfVAy2oLqvZrI8x88b_KnANjcAJ61rFMjCA3V4vDog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: امروز ملت ۵ هزار سالۀ ایران با دولت ۲۵۰ سالۀ آمریکا در تقابل است.  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457599" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7086b89ab.mp4?token=iF1Rx1MMCMHJWUCBjMeMHG2C32OmnvwZtYR5BW0q71bCY78KFiVtQQApePj53WfQWRFp6xj4Ng1qM8_c9XT4kFBZmG1Bau0Zvp8gAQns6q6MURf9XLbv7yXLR0Uy4WVbuprNINq2JptzXhyehOdeJQ-3OIkpuuoXx815YCEW20qqpKUQ_aCLXLfIQ5WLgG8DbULGi3DmAK2BsHdeB8EYtotRyVSdtTK_guu3Sbgc_aJ2zSigimNdOb9l5Dk-aKIOp29Sew89dodDsFmw_dnmZ1rRNOlyQQzAfZWag9bWs5BH1Pl2G84lAncCieaStplM30hTTipAWPqpmtnRnx6dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7086b89ab.mp4?token=iF1Rx1MMCMHJWUCBjMeMHG2C32OmnvwZtYR5BW0q71bCY78KFiVtQQApePj53WfQWRFp6xj4Ng1qM8_c9XT4kFBZmG1Bau0Zvp8gAQns6q6MURf9XLbv7yXLR0Uy4WVbuprNINq2JptzXhyehOdeJQ-3OIkpuuoXx815YCEW20qqpKUQ_aCLXLfIQ5WLgG8DbULGi3DmAK2BsHdeB8EYtotRyVSdtTK_guu3Sbgc_aJ2zSigimNdOb9l5Dk-aKIOp29Sew89dodDsFmw_dnmZ1rRNOlyQQzAfZWag9bWs5BH1Pl2G84lAncCieaStplM30hTTipAWPqpmtnRnx6dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی-سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/457598" target="_blank">📅 22:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457597">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d57a058d.mp4?token=mxZnBJGcL0BQlpjuHvIEdtBh53cKPM6KWlJiYeRbCYJ2Sx9VNjb_nZ1yoj1F7kPuGgBxI5k_7NhTtTxxB7Y0SbSiPbU0z8zc0pSVuqw_eGeLGmcI6iprWIoEvt1-uwPy6Kjd2lrJGC7LK8uaxohvdch1e4vmHvJKZFd7y7QgLZVRcV-bz9YsQWLgcxiSoffC_pxPZlh6jxuVIJXdTwIcCMORHFRpAgrHHHGi8SOZaBk2KHKTD6L4K3pXwaTpgjTR_HHirZ1Fjpt72fclI5mYXOzaJL0s-jngW3-2v0jK6G8eqDzsdCX56Utu7JOw0_bL4OK5x7iEkuLTMWuvR_WK1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d57a058d.mp4?token=mxZnBJGcL0BQlpjuHvIEdtBh53cKPM6KWlJiYeRbCYJ2Sx9VNjb_nZ1yoj1F7kPuGgBxI5k_7NhTtTxxB7Y0SbSiPbU0z8zc0pSVuqw_eGeLGmcI6iprWIoEvt1-uwPy6Kjd2lrJGC7LK8uaxohvdch1e4vmHvJKZFd7y7QgLZVRcV-bz9YsQWLgcxiSoffC_pxPZlh6jxuVIJXdTwIcCMORHFRpAgrHHHGi8SOZaBk2KHKTD6L4K3pXwaTpgjTR_HHirZ1Fjpt72fclI5mYXOzaJL0s-jngW3-2v0jK6G8eqDzsdCX56Utu7JOw0_bL4OK5x7iEkuLTMWuvR_WK1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۷۵ از شب های مقاومت مردم تربت حیدریه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/457597" target="_blank">📅 22:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457596">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731f4e0fa5.mp4?token=oMhyYO5ARo9HPKK03ZMZBIMCbk--MWL1xKW3dolFRnsDcZV-oFyzEzV2c3mGWmbcitMX5vDmgEKbZ27876xe4MdRcGBP5MfY-Nc0pF0twf-f9BmPTb3UCHAuM6jOFTQ9VdqiA8932X-Q-AKc2TXMvu0YitUUF28jkpknBllMs8HYc7JVI2yc0NwKQKWgpyroGlWPu1n0brklFEiHTsowx2b_HkYc1qwZ2v4WyaR91ewkYqZcHxdQzUpIkV0ulHXWl5xM2FBfoDx1yvmQWu98u-2ULDSZvK_vaXkxdjrSkbnYjBXwzRzJNNAtcB2VOUFpX_GKfsgDVQEeSzzMiyNR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731f4e0fa5.mp4?token=oMhyYO5ARo9HPKK03ZMZBIMCbk--MWL1xKW3dolFRnsDcZV-oFyzEzV2c3mGWmbcitMX5vDmgEKbZ27876xe4MdRcGBP5MfY-Nc0pF0twf-f9BmPTb3UCHAuM6jOFTQ9VdqiA8932X-Q-AKc2TXMvu0YitUUF28jkpknBllMs8HYc7JVI2yc0NwKQKWgpyroGlWPu1n0brklFEiHTsowx2b_HkYc1qwZ2v4WyaR91ewkYqZcHxdQzUpIkV0ulHXWl5xM2FBfoDx1yvmQWu98u-2ULDSZvK_vaXkxdjrSkbnYjBXwzRzJNNAtcB2VOUFpX_GKfsgDVQEeSzzMiyNR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی-سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند و تصویر آمریکای صلح‌خواه و بزک کرده، در ذهن جوانان ایرانی عوض شده است.
🔹
همۀ دنیا با یک دید جدید به ایران نگاه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/457596" target="_blank">📅 22:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457595">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
چرا قطع برق شهرهای خوزستان باوجود وعدۀ وزیر نیرو و استاندار همچنان ادامه دارد؟ در ساعات گرم روزهای تابستان خانه‌ها برای چند ساعت و گاهی حتی بدون برنامه‌ریزی برق ندارند.
🔹
بیمۀ مشاغل آزاد به‌شدت افزایش یافته است. ۳ مرداد رفتم بیمه، گفتند ۲ میلیون تومان باید اضافه پرداخت کنید؛ یعنی ۶ میلیون و ۲۰۰ هزار تومان پول بیمه و مابه‌التفاوت ماه‌های قبل را گرفتند.
🔸
پنج‌شش ماه است که از موعد تحویل ماشین‌مان گذشته، اما چون ماشین گران‌شده تحویل نمی‌دهند. این چه وضعی است؟ این انصاف است که می‌گویند یا بیا پول شش ماه پیش ماشین را پس بگیر یا مابه‌التفاوتش را بده؟ مگر مشکل از ما بود؟ همان موقع که پول کامل ماشین را خواستند، پرداخت کردیم اما موقع تحویل این بازی‌ها را درمی‌آورند.
🔹
سنوات دو ماه ابتدایی افزایش حقوق بازنشستگان تأمین اجتماعی چه تاریخی واریز می‌شود؟ پنج ماه از سال گذشته و حتی تاریخی هم اعلام نمی‌شود.
🔸
معاون اجرایی هنرستان هستم. امسال سامانه سیدا هنرستان افتضاح شده و هر کاری بخواهیم انجام دهیم دستمان بسته است. از ابتدای سال مهلت داشتند تغییرات بعضی دروس را در سامانه اعمال کنند، اما حالا که پایان سال است، نه تنها مشکل حل نشده بلکه هزاران مشکل دیگر هم اضافه شده. الان نه می‌توانیم کارنامه صادر کنیم، نه انتخاب واحد تابستان و کارآموزی امکان‌پذیر است و نه تعریف سال جدید.
🔹
محبت می‌کنید در مورد وام مسکن روستایی پیگیری کنید. باتوجه به اینکه نامۀ معرفی به بانک داده شده، بانک هیچ پاسخگویی ندارد و پرونده همین‌طور مانده است.
🔸
مشکل سوخت جنوب را پیگیری کنید، مخصوصاً میناب. کارت سوخت کفایت نمی‌کند. با این هوای گرم، برای بنزین آزاد هم باید در صف کیلومتری بایستی تا بعد از ۲ تا ۳ ساعت فقط ۲۰ لیتر بزنی. واقعاً مردم نباید دغدغه‌شان این موضوع باشد.
🔹
متأسفانه ادارۀ برق فردیس به روشنایی معابر ۱۶ متری امام خمینی، خیابان تابان، سعدی غربی و خیابان‌های فرعی آن رسیدگی نمی‌کند. اکثر لامپ‌ها سوخته و قدیمی هستند و فقط برق مصرف می‌کنند، در حالی که سایر خیابان‌های شهر با لامپ‌های جدید تعویض شده‌اند. لطفاً از مدیر برق منطقه بخواهید شب‌ها از این مناطق کم‌برخوردار بازدید کند. آسفالت این خیابان هم کاملاً خراب و پر از چاله است و ۳۰ سال است وعدۀ بازسازی می‌دهند ولی هیچ اقدامی نشده.
🔸
ما فروردین‌ماه به بیمۀ بیکاری معرفی شدیم. پیامکی هم آمد که مبلغ ۱۶ میلیون و خرده‌ای به حساب شما واریز خواهد شد، اما با وجود گذشت چند ماه هنوز این مبلغ واریز نشده است. لطفاً پیگیری کنید.
🔹
من رانندۀ تریلی هستم و اتاق سمند سورن را به شیراز می‌برم. ایران‌خودرو از مرداد پارسال طلب‌هایمان را نمی‌دهد. قبلاً پیش‌کرایه می‌دادند و مابقی را ماهانه تسویه می‌کردند اما حالا حتی پیش‌کرایه را هم قطع کرده‌اند. با خرج سنگین گازوئیل، قطعات و خانواده نمی‌دانیم چه کار کنیم. فقط تهدید و وعده می‌دهند.
🔸
یک دارو یک‌بار با بیمه و یک‌بار آزاد خریداری شده. در خرید با بیمه گران‌تر درآمده: با بیمه ۸۵۰ هزار تومان و آزاد ۶۵۰ هزار تومان. تعرفه خدمات دارویی در خرید بیمه‌ای ۷۲٬۷۰۰ تومان و در خرید آزاد ۸٬۱۰۰ تومان است. ببینید چقدر اختلاف وجود دارد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/457595" target="_blank">📅 21:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36b0dd885.mp4?token=Q9CKfaHptUW2r-n9H6p5ToHJ9gr7G6cuRIjWB8wIumu6_QWXuHSRoFlsagejqfq0x0HyMRd7GT68Dq9uX1eLxCD9bKGoMsfecmlbwJZxPCg-FOYE7i4G_R-A4FnyY9eJd6rLGuqqsIej4sBb5WYkoXTCf_BqT9Eb1ZhP_3lzetAAGjtn-6-7Ud7hjO6AUUPl9dbDrZNi8jRP34pI1IFu8X8zn5QDNdfut3pHpppxgdOkOjbJ0Ha5wtoRw5aFVNAOr76ADVmaM_GUu9sBIIJnjVwMRfmE1Gtz-QhWEvZZOGmEQCD7MdXlN6gkXpHc-Vsm_BTV0UQHZXMfq1rDNgO01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36b0dd885.mp4?token=Q9CKfaHptUW2r-n9H6p5ToHJ9gr7G6cuRIjWB8wIumu6_QWXuHSRoFlsagejqfq0x0HyMRd7GT68Dq9uX1eLxCD9bKGoMsfecmlbwJZxPCg-FOYE7i4G_R-A4FnyY9eJd6rLGuqqsIej4sBb5WYkoXTCf_BqT9Eb1ZhP_3lzetAAGjtn-6-7Ud7hjO6AUUPl9dbDrZNi8jRP34pI1IFu8X8zn5QDNdfut3pHpppxgdOkOjbJ0Ha5wtoRw5aFVNAOr76ADVmaM_GUu9sBIIJnjVwMRfmE1Gtz-QhWEvZZOGmEQCD7MdXlN6gkXpHc-Vsm_BTV0UQHZXMfq1rDNgO01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی رضا پهلوی به اینترنشنال و خودش  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/457594" target="_blank">📅 21:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📷
ادامۀ جنایات صهونیست‌ها در جنوب لبنان
🔹
تخریب منازل لبنانی‌ها توسط ارتش اسرائیل در شهرک یحمر الشقیف‌. @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/457593" target="_blank">📅 21:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92621de672.mp4?token=MdJUujuTim5nMNpoRL6VmAXp_kN1lfDTRCqX40kNhWDm9RjBVOghXIdvL-T2bFU4-Dz7LlIw6X3anER73MxmM9YpYk_BV_f9Q5L_JEUqJhdWRRToKJuFAR54QQMgjf229fQty2EZLZv3c4PP9fN5pGe3Ev_45e2C5z4_I-rC3HyKMwxIRPor8tmOA5CePK7jCRpPceJ1eRPHsEoXeGjepNzyoplVeFIy3aRKmyCjy6BwZC3XldQrU9y_vMtfmsxVFOvUnWmDcAclJRNCTokX1XpQVOQFd7RU5qBuPbxXHJkAXy3xJkaUgfMY6IHoAhXdyEwpQQq5iT3AJFK7hXwB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92621de672.mp4?token=MdJUujuTim5nMNpoRL6VmAXp_kN1lfDTRCqX40kNhWDm9RjBVOghXIdvL-T2bFU4-Dz7LlIw6X3anER73MxmM9YpYk_BV_f9Q5L_JEUqJhdWRRToKJuFAR54QQMgjf229fQty2EZLZv3c4PP9fN5pGe3Ev_45e2C5z4_I-rC3HyKMwxIRPor8tmOA5CePK7jCRpPceJ1eRPHsEoXeGjepNzyoplVeFIy3aRKmyCjy6BwZC3XldQrU9y_vMtfmsxVFOvUnWmDcAclJRNCTokX1XpQVOQFd7RU5qBuPbxXHJkAXy3xJkaUgfMY6IHoAhXdyEwpQQq5iT3AJFK7hXwB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف ایل و تبار ما: مرگ بر آمریکا، مرگ بر اسرائیل
🔸
شعار مردم شهرکرد در شب ۱۷۵ تجمعات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/457592" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457591">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFtU6dBWKM2Nev8xlGTpy49k7tMC_5yICnRlkMzSctfwJxlZdELq6Ksh3YpGwbISGqz-RZQ5Wl0j9OfGtvehseTMuxixWm9CvcUR-DGXRiVKOu6gg9lDhjps9GL6TrtIPT8U2UZYOYJkuIFJlmaJVoqkbY3SNPftzqoJTEUGa6JQ0mlhmlXWIyn5W1UcDB-1XErGjB1lx5fC-ttcgipA5E08jJYkzJ34_f1wUe9OLHUPmnTZggrxWOHhYjps2pLkJXC6QnaaNwpdG8NgaBONl8dQ6BCR0E-vS-XmN4SIjmvm6ZQ5ZQ9W6QLUvf2IfU1Mu25QxinyeFDaDmimkl97-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادکار ۹۲ کیلوگرم کشورمان در رقابت‌های جوانان جهان نقره گرفت
🔹
فینال ۴ وزن دوم کشتی آزاد جوانان جهان امشب برگزار شد که  ابوالفضل رحمانی تنها نمایندۀ ایران در وزن ۹۲ کیلوگرم، در ۲ ثانیه پایانی طلا را از دست داد و اولین نقره کشورمان را کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/457591" target="_blank">📅 21:25 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
