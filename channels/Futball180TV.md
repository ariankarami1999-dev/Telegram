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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 629K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-98545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=RS1j3UE-45IqWmLGaU5MaGfCHUgY6gujkvddmFJ26X5NOWLa31QPDAGcn8FY-coRYTXqlZrwPNyZZ_mVbivv0fNo6Ab_-HvufGqTWZlVLcgImvqx6sUJjtkxkHhyea-6dGox7a5CfR-PBNY8JS8myMofb7PM4BLskK_iShucKVPCLwqcGfW0WI25h4Sde373Y7-oQjVL1mENrwLsPOOXVTulPiG0VClvq-p9Rj_Mc3m2gPx6KGq69jbOkJe4SyiwtefLH0OeLsuUb7RVMt5C6aLMYZRb-zT5ICvzOF8LyUG8tfnJ0wKocdptnY1Uji8ulVgenbPX7grQslG33f1k4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=RS1j3UE-45IqWmLGaU5MaGfCHUgY6gujkvddmFJ26X5NOWLa31QPDAGcn8FY-coRYTXqlZrwPNyZZ_mVbivv0fNo6Ab_-HvufGqTWZlVLcgImvqx6sUJjtkxkHhyea-6dGox7a5CfR-PBNY8JS8myMofb7PM4BLskK_iShucKVPCLwqcGfW0WI25h4Sde373Y7-oQjVL1mENrwLsPOOXVTulPiG0VClvq-p9Rj_Mc3m2gPx6KGq69jbOkJe4SyiwtefLH0OeLsuUb7RVMt5C6aLMYZRb-zT5ICvzOF8LyUG8tfnJ0wKocdptnY1Uji8ulVgenbPX7grQslG33f1k4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
خلاصه که هیچ‌مهاجمی نمیتونه مثل رونالدو اورجینال باشه و گلر رو دریبل بزنه. اندریک و بقیه تازه انگشت کوچیکه اسطوره برزیل هم نمیشن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/98545" target="_blank">📅 11:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlDSuqrMBADR5zL11YqDBD1VJd04i8t8lRTNS4lHt_k5MWfh6obesnQgGnkr069eBEUktdcijhELIXSFWICzWnJJ3mfqiRaYoNzMOlST0H9rH5yQdF5HKRQUj8fqGh-X0XQ-vYwspIZm3uxRaYoil2Qa6MjyB4asp_pwJCJ8-UBD9C36EQ_z_3qabe4xEnjv7TiPxkQTmhA8aYYa42oCXbU4sVvdo5_ANndA9NjrFTQad7uth2RQsfcU0atgCIPNZiAgmfUUku05gds1O1mxnPYAgjbjay2g5iTVQTv8YsZDnSGIuroVxXPsEgaivSpnPcMvAGy06GdrqR9pinWXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇧🇪
بیانیه فدراسیون فوتبال بلژیک: لغو کارت قرمز بازیکن تیم‌ملی آمریکا در آستانه بازی امشب نمونه واضح از نقض آشکار بازی جوانمردانه و دخالت قدرت‌های سیاسی و نفوذ در فیفا است. شدیدا این تصمیم را محکوم کرده و پیگیری این مسئله را ادامه می‌دهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/98544" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f91878075.mp4?token=TXS8XUy-tRawyKgM5mWJDrBwMgtf3iJct89EPqv2onfrKkRVoCajnIKenMEVX0JKmoJOZQIJX7AB4N1oEr0yYo3tc0we3IsEuf49C-Wpqx7hGD1YBaMoRZjRiBbxbJP35DuRnFplZq6R2ocMrnjBHIWpqDG901h9cAaMWK0oO4TIq7mo0jCTX958wWf6a7yiY_r8EY3DOoJmpCsChSgyMDUGtxa7ea9MCbU2N3ek6d9fZA6Auen5mFGG_3jToQTDw5AeisMpJBw2mqSoE7wgC1M_ACCBkuLwKM-3BJeOIGOsEm-f9gXtOiWu6ir_Gjrd-KIqu2piG8EW6OnMWma4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f91878075.mp4?token=TXS8XUy-tRawyKgM5mWJDrBwMgtf3iJct89EPqv2onfrKkRVoCajnIKenMEVX0JKmoJOZQIJX7AB4N1oEr0yYo3tc0we3IsEuf49C-Wpqx7hGD1YBaMoRZjRiBbxbJP35DuRnFplZq6R2ocMrnjBHIWpqDG901h9cAaMWK0oO4TIq7mo0jCTX958wWf6a7yiY_r8EY3DOoJmpCsChSgyMDUGtxa7ea9MCbU2N3ek6d9fZA6Auen5mFGG_3jToQTDw5AeisMpJBw2mqSoE7wgC1M_ACCBkuLwKM-3BJeOIGOsEm-f9gXtOiWu6ir_Gjrd-KIqu2piG8EW6OnMWma4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🙂
خلاصه اتفاقات دو روز اخیر جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/98543" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=jTg2-WtOwD13ld4ba6oTLPKM2-Lbp-esFnhbkFiQoXBmGR_ZGM3iEbRfh2Na92aYZRwT_Ip_GtFHW0y6RZG7f7mdg6AWMqpEcgd-Rhni1SkAVpRC7W4tXrNkUz-ujOp0yUD7nh3-Z1WryxoAqknviCXz_44Yad6Tc1ikKnTDIbe72T-C0nIeFzpUGvEQU_pxojHvCR1Cyvwow3aY7R4fL_uJ-d3HXwb9lsIzxGdra-Cn87xeiXMlEkjtK-nI0no62JQS8E3SimMtv9yJWbbnDS8LvXdiQT6PQK-UG4UuFhmQtjscHpLzGlXrl6HYxeuAThamLpDqksulhTdZrM5NpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=jTg2-WtOwD13ld4ba6oTLPKM2-Lbp-esFnhbkFiQoXBmGR_ZGM3iEbRfh2Na92aYZRwT_Ip_GtFHW0y6RZG7f7mdg6AWMqpEcgd-Rhni1SkAVpRC7W4tXrNkUz-ujOp0yUD7nh3-Z1WryxoAqknviCXz_44Yad6Tc1ikKnTDIbe72T-C0nIeFzpUGvEQU_pxojHvCR1Cyvwow3aY7R4fL_uJ-d3HXwb9lsIzxGdra-Cn87xeiXMlEkjtK-nI0no62JQS8E3SimMtv9yJWbbnDS8LvXdiQT6PQK-UG4UuFhmQtjscHpLzGlXrl6HYxeuAThamLpDqksulhTdZrM5NpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
پشت صحنه‌ حماسه‌ای که دیشب اساتید فیفا در بخشش بازیکن آمریکا رقم زدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/98542" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=jKB1VdOpj_NMPO98UJLcyWMmdyDi5zFuu0xufHtnBugjYdPATGzctEtX9W-ZaTjXSIxsyKknQsM9hZCx-2xOug_jihK4B6KqE8uzm_gf02TscwGqksuwGNwWxdcT8dF6NI4QGI6eciB0VcPaSFYqLzoWyiD_fEMz5q0rMn3kCx8ADSTpeX8zB-hXYwur4yQkvL-yH-vfKxxGT7kA2ZwDL9fHI4Fc8kCJd5rqY0emJ51QcqXbjye-QGL23cyfE9M_Cwjh2tK6OledLKUkFnGcOTCuOLHFXBEksnL5oTEyAC5iRUzMMCDGydFZWdY9TdOoidE7uPDwMBdj6ijHj-2svQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=jKB1VdOpj_NMPO98UJLcyWMmdyDi5zFuu0xufHtnBugjYdPATGzctEtX9W-ZaTjXSIxsyKknQsM9hZCx-2xOug_jihK4B6KqE8uzm_gf02TscwGqksuwGNwWxdcT8dF6NI4QGI6eciB0VcPaSFYqLzoWyiD_fEMz5q0rMn3kCx8ADSTpeX8zB-hXYwur4yQkvL-yH-vfKxxGT7kA2ZwDL9fHI4Fc8kCJd5rqY0emJ51QcqXbjye-QGL23cyfE9M_Cwjh2tK6OledLKUkFnGcOTCuOLHFXBEksnL5oTEyAC5iRUzMMCDGydFZWdY9TdOoidE7uPDwMBdj6ijHj-2svQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇧🇷
توصیف‌های عادل‌فردوسی‌پور از نیمار...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/98541" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f587817b79.mp4?token=RTQTtt4EvibwzbHHiaCEOa3pKqJbSrPPD0j8levbXwN4xI5QscJ1AlPcvEC8Vboq1icngL3_w2mj4FnmWtkaLs7SKr9T9F9R9O85N_PIdEhsBtW6JWiSSNRdMKw_WAdbB6Fz7TdWp4bYd_Aa35fGJf6_wcyvbWTZ6iMGX0h8A349XKSu_kslLpxrRZR0GIh2requbXgSRYt6xHX-nJrhiq94eNmAAnLMS3tOeHi3ZBt0NmYkwhQrHb2a-s8N-b-CoBP4eIqL5vGdJ-MsGnxNmOtgnFtOPZSDbPv-T05uwznHw_dmLw4VZg7Kw3_yTqcFVJPePOEqzjx_21RagLyuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f587817b79.mp4?token=RTQTtt4EvibwzbHHiaCEOa3pKqJbSrPPD0j8levbXwN4xI5QscJ1AlPcvEC8Vboq1icngL3_w2mj4FnmWtkaLs7SKr9T9F9R9O85N_PIdEhsBtW6JWiSSNRdMKw_WAdbB6Fz7TdWp4bYd_Aa35fGJf6_wcyvbWTZ6iMGX0h8A349XKSu_kslLpxrRZR0GIh2requbXgSRYt6xHX-nJrhiq94eNmAAnLMS3tOeHi3ZBt0NmYkwhQrHb2a-s8N-b-CoBP4eIqL5vGdJ-MsGnxNmOtgnFtOPZSDbPv-T05uwznHw_dmLw4VZg7Kw3_yTqcFVJPePOEqzjx_21RagLyuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇴
خانواده سلطنتی نروژ دیشب بعد بازی با برزیل برای تقدیر از بازیکنان کشورشون وارد رختکن شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98540" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=PXkn2bREbhku_kwVxIcLqZUjicyDZVbLEDlFRDJFTR3hSf5cay3GewX3_7PdbIA1_CHZXoxMtBByMN-A6-W97Gup_986zF-OrAQ4ogfGv1BYWWSdUhEzgqwef82-BxyjL6KwaQRmk4ON936F5OoL4JteX-5u__1KIDevskYuhNw1NKWcuFAmuKRtmZV_HsCe5QiRkz1v6lUdBzEH_m3AEQwJoGP8KZXeNXs-S22gSzgsrsJmlGaWW5_FYW2K6_voa0DGTwDhK2s9Gp9QxaR3p2pXnoK7EXsD1yETDHlCflBeumeN0vmXqM-J8zDg-hlCiHQXbqrtMfXXkc4S-4qz8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=PXkn2bREbhku_kwVxIcLqZUjicyDZVbLEDlFRDJFTR3hSf5cay3GewX3_7PdbIA1_CHZXoxMtBByMN-A6-W97Gup_986zF-OrAQ4ogfGv1BYWWSdUhEzgqwef82-BxyjL6KwaQRmk4ON936F5OoL4JteX-5u__1KIDevskYuhNw1NKWcuFAmuKRtmZV_HsCe5QiRkz1v6lUdBzEH_m3AEQwJoGP8KZXeNXs-S22gSzgsrsJmlGaWW5_FYW2K6_voa0DGTwDhK2s9Gp9QxaR3p2pXnoK7EXsD1yETDHlCflBeumeN0vmXqM-J8zDg-hlCiHQXbqrtMfXXkc4S-4qz8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف برزیل از جام جهانی به دست نروژ.
🇳🇴
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98539" target="_blank">📅 10:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=twTEFQjioGmSuNmPBMyw9pmP1rkVu_dGqdKUlT8gnHvbUIStS6rhZmiSFqQ1JFZO2NkN1UzQfMAAxjOm1R7J9RNGujRcdWmFKIC8nMIpKsBpdnoDL14IxjD2TW3-5Rk1dmikDlK1bXb3G4G6VK8pSXMdLGbhfkzjvIiS7L-P1-Vah02Du6hDniVrlvJvH-TFDeu8jvTDT-Hd_7EfHq4N2hC8aN2bidtukRVBZZhbO88mFJev1FU8qcvlSfcO2YxRKGLjTUodMEXrBSN_gMGj77rW_xAZXldFfEaaz1zxd7lWcSITG3tiXbvMUuSi482mMvSKpSZI4wm5RcVCwB-Vh1xowPeMwabwJVzdrHBkbdus68BNVm6fcUm5DmnoOwqhAeKkOfDjRFRs48KV-0nfq3L-XiijffX1oUd91MQ_kKcPKorvxpJgX8J55f-A5Qjm4iRv6Wl7ekbYPnr89-7f7W-XsFxzH6RFAQWk1V85lTSLy7BbEELmBbKKQCBw8mihigG5lYehouT4L1XF6FvEf7AusBh5o7Ey1TzScQ87blPvtSAWpiXlinNsL9pnzsK0pASqlZmvoLUyQtp6X7B7KKam9EprRAIORIWWkD5Y9bV9Jnlv0NqXsXUo3TXsvPSv5w7FB_nW80xcOVzzUxQj29uM_2Gqdum-vF78Yw4GFnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=twTEFQjioGmSuNmPBMyw9pmP1rkVu_dGqdKUlT8gnHvbUIStS6rhZmiSFqQ1JFZO2NkN1UzQfMAAxjOm1R7J9RNGujRcdWmFKIC8nMIpKsBpdnoDL14IxjD2TW3-5Rk1dmikDlK1bXb3G4G6VK8pSXMdLGbhfkzjvIiS7L-P1-Vah02Du6hDniVrlvJvH-TFDeu8jvTDT-Hd_7EfHq4N2hC8aN2bidtukRVBZZhbO88mFJev1FU8qcvlSfcO2YxRKGLjTUodMEXrBSN_gMGj77rW_xAZXldFfEaaz1zxd7lWcSITG3tiXbvMUuSi482mMvSKpSZI4wm5RcVCwB-Vh1xowPeMwabwJVzdrHBkbdus68BNVm6fcUm5DmnoOwqhAeKkOfDjRFRs48KV-0nfq3L-XiijffX1oUd91MQ_kKcPKorvxpJgX8J55f-A5Qjm4iRv6Wl7ekbYPnr89-7f7W-XsFxzH6RFAQWk1V85lTSLy7BbEELmBbKKQCBw8mihigG5lYehouT4L1XF6FvEf7AusBh5o7Ey1TzScQ87blPvtSAWpiXlinNsL9pnzsK0pASqlZmvoLUyQtp6X7B7KKam9EprRAIORIWWkD5Y9bV9Jnlv0NqXsXUo3TXsvPSv5w7FB_nW80xcOVzzUxQj29uM_2Gqdum-vF78Yw4GFnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
هوادار برزیلی بعد باخت از شدت عصبانیت هیچکی نتونست جلوشو بگیره و تلویزیون رو شکست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98538" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=a-KKGbXJF_JIwgftdeF-o84bZlJ4Xz9GwjXOsG-fmS1051E0aAtXyZweabL-wQ0iAEPnIc7lv6nxP2ThNFQzjWhaHxtZprQIC7ZB9CgfHumn_QkP9KjkcwqRDnuOV5RYWqnx6ln08699yNYZhGvtBil5Ip0IXq2ZWasCEL3syjt32GiJtk0WLf0mMu5ikyul3_kmGTJw_33QDmH8_PI57BHtB61NcsFp7ar0LWYOnY1tB_U4X8UqyH2FLwzVY0zvd1yifbZ3rtdzu1oNrPWH96adAJ8bKMIvrb0UGSAg2W1UP2URywQ1SW7nPOOxmg20ZYBVsNXLPzaDLyVGtJv9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=a-KKGbXJF_JIwgftdeF-o84bZlJ4Xz9GwjXOsG-fmS1051E0aAtXyZweabL-wQ0iAEPnIc7lv6nxP2ThNFQzjWhaHxtZprQIC7ZB9CgfHumn_QkP9KjkcwqRDnuOV5RYWqnx6ln08699yNYZhGvtBil5Ip0IXq2ZWasCEL3syjt32GiJtk0WLf0mMu5ikyul3_kmGTJw_33QDmH8_PI57BHtB61NcsFp7ar0LWYOnY1tB_U4X8UqyH2FLwzVY0zvd1yifbZ3rtdzu1oNrPWH96adAJ8bKMIvrb0UGSAg2W1UP2URywQ1SW7nPOOxmg20ZYBVsNXLPzaDLyVGtJv9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گریه‌های شدید این خانوم برزیلی بعد بازی دیشب و حذف از جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98537" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=dlUyoYbIumTvy0SaVmeyKBnDOhUGJuYGjMeBjTBfkLCUkXSiLAYgICtm6MmxubyhzFmKRoy2MALETl0agKI9ulaqAJVAaG0fVtDuTtyCeoO-A79keIqkCiDBXRU6ZWMJCgSnQQgVDrDB_kCnq4AVUt1s5hiVoDOU29RcW6kgKLH_i8OkCfnRhEYGpFDQRxsNSNkSP727-YxnNmxeOxW_LvLdq8bRWE1Ic9J2ti4L5ZXi82nS5vg0yhUXV2nQscfRnDbMQ8zjG67uQfoWgSTqzvFCZpm6MqEGEuR-CQHM68VwbqPRoxRvrskMJlbQX0qSvQFYxG48JcpnNcyfaoc9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=dlUyoYbIumTvy0SaVmeyKBnDOhUGJuYGjMeBjTBfkLCUkXSiLAYgICtm6MmxubyhzFmKRoy2MALETl0agKI9ulaqAJVAaG0fVtDuTtyCeoO-A79keIqkCiDBXRU6ZWMJCgSnQQgVDrDB_kCnq4AVUt1s5hiVoDOU29RcW6kgKLH_i8OkCfnRhEYGpFDQRxsNSNkSP727-YxnNmxeOxW_LvLdq8bRWE1Ic9J2ti4L5ZXi82nS5vg0yhUXV2nQscfRnDbMQ8zjG67uQfoWgSTqzvFCZpm6MqEGEuR-CQHM68VwbqPRoxRvrskMJlbQX0qSvQFYxG48JcpnNcyfaoc9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
حسرت عادل فردوسی‌پور از وضعیت مردم کشور نروژ که در رفاه کامل هستند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98536" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap39wv5sTn5sSavHNNTB3u_Q_HZTbAZ3RNSCJeuQ4qQajpY5zvfGq9RkOIe6X2VC7KcDVKPR_lPBMysqf6qKsTjt3rCnQhPyz9jBRpm8ELZSzaFsOV-tnipwjpMYkZqMkN1473dTh4ZSc2_2rXSaTJWNhgqHgJOofr_qH15C1ao42eiQaClH2cBdrq2pDFpjty-zoZ_mJ-afQqOUdSnpSLAtrTZgCdIkudqBHd9cBGSwkBuz-uNG6fLZ5HozoH1U4HT45ll6x_qCyfX2tzQDYzfuZtbUG5mOVbn6QzZb7x6wOm-HlI84KSD-I4WDZRrr41F9GK5Qd1qEls2sMwdWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون پخت و پز همیشگی
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98535" target="_blank">📅 07:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZmONiu9Yf2CVmUrqq1K5sqD0McwELbisBxh_q0PHyQMOcUEP5Q3DCNgTupyAqDE5juFGVj3MsroM7zJc-huej9IxAexJOljpuCJBXHzAR8u034bXdEBFLtLlajPguGZAqFtdwncYyNjVMciDf4o0LlGSt-ZUsPvZfg3rhJBc5rrmqsUWuc1oV7mmL9KGcKnQl9YLQ0l2ShqCZ-nbeuB6ckQYQQTWhne2bS0Le3f3-zBDYXXtam_MFj8x6cSkkT4Uzg8Y32upVx2t0SH3R1tAXOiyp9FRrGzqOkvPoRJy_VdBFup4993K6YDDmyLHqBADmmehgfeplAPMZeq4EDcnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس در جام جهانی 2026، یازده گل زده که ده گلش رو این زوج فوق‌العاده به ثمر رسوندن
🔥
🪄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98534" target="_blank">📅 07:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4010363319.mp4?token=tE2oWYqkJAYRgWtho-kb5Y4EREIlaOwMSMCdEYTT9SUDXvmdGV4ocyM-QVfj6Q-dTYJODmSsO2Thd1-2RrHKVEUNyHywwgMsSmy65MkDSQDysb7MJsyMRKnoUxfbQ8W8RHacBoiYqxJMOrubBt2bJrKVCQ0QJbh8YU3YrGan6hR6mRucEZEiRM6eY3SK_BEFaRDgiePYq69JcUQsk8uOieU4_xWtbKNddYa8iMUbJYC4ir3cA_Cu_o4QACOXkF2LsvOZUDxxzljIXTGz5QNopBikLG0XH26XnfqT139GgDxx860NtmYISj2ZCoz-m3-Ap-Oaw-jnQf-Xs3aqyYxliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4010363319.mp4?token=tE2oWYqkJAYRgWtho-kb5Y4EREIlaOwMSMCdEYTT9SUDXvmdGV4ocyM-QVfj6Q-dTYJODmSsO2Thd1-2RrHKVEUNyHywwgMsSmy65MkDSQDysb7MJsyMRKnoUxfbQ8W8RHacBoiYqxJMOrubBt2bJrKVCQ0QJbh8YU3YrGan6hR6mRucEZEiRM6eY3SK_BEFaRDgiePYq69JcUQsk8uOieU4_xWtbKNddYa8iMUbJYC4ir3cA_Cu_o4QACOXkF2LsvOZUDxxzljIXTGz5QNopBikLG0XH26XnfqT139GgDxx860NtmYISj2ZCoz-m3-Ap-Oaw-jnQf-Xs3aqyYxliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98533" target="_blank">📅 07:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsD1ZVQuDr-RUoke6kbrfcmBTl1RzLR2_NaOikbRe3-pX7l44LElbV5XMuS5jXcE1qO8FACznbROykBsGm2uB8HeOOV_NU7E0PENweLv4ysqhgY_mCb02Sbv8zGNxV23IvJTZVUs1OsuDqQoknTFK-tHqiBsU0640SN_g75BjpBICM7VQJ8yTHCpVJnoemJo081XLt6w-N47BWJTFbLl-ApTF-Hb_bjkOADukd6FkhNOoPQPAUWF_h6blrcMugZ_NzBBHgTrCExT_KtcHmSwKHvh1fD7xSMLWfym2dm5q-W9Geo1tFPbuqQ06_mYhpYhCxqQLbCUzKMiZb4QMaA5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98532" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صدای هری کین بعد بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98531" target="_blank">📅 07:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhnO2Uh9djf9aLMfe7ErUVp8ixNP63YcdM2Kcjo_XJ4P9dP7AmrBVdK3yAQR7Vu7qs7xWW783Syq0wW_nUnNzjSLEvhcfK9joVzYUqrOPF0-DyxOkRzi10CvYF5ssMG5EY9ICZqH53uQusnzPUE49yLbabwCdMvxzw3mBZsu_k6qgT38oFMo8VzLnqE9vNqhFlt79CFFJdTKOMPELfIPikPII_umTu_KmZvVQd8XGRAMJphsG-bIjO6ql9wxPnqrk6kz27oYSsUhjN1t1ExLV52SlJOkwgorerF825M2tbg4K92wjuSPLf-NidfoHNpXmXdExCF805BNFxTtM24AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ۱۹۶۶ سابقه نداشت تو جام‌جهانی یک بازیکن هم پنالتی گل کنه هم پنالتی بده به حریف. پرینس هری یه پاس گل هم داد و همه‌کار کرد تقریبا برای خود و غیرخودی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98530" target="_blank">📅 07:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rXQV75fEfROjT6MfyRkwKTuUfaLwu_JUwSSyF6qeTefA9ZoulmldsqU-c00JLN_6dakJfl9fbNm7HKkEJSsugKqs-6Bw6_EHxzai5PY8Sg0d_UW98vMAC-GYODAPtJ6M_beVhWQZ6myKM0JhKtCzi2HpirLP2tN869EWiQsRJrGPTZJVpNtpHtH_B_gK4tnVBJVfpGGHcbfsJrzuMzQPJNxmmuu-ToarlGAm55b6WSORQRYNG6wLx-Q3HkirbeMJd0PoqmXw4owRxK4JRqUVg8dIcnoKSZbOj4rls9K74igVDVJ8WXZMVkvSeWYyiCUVUeIpBZOhrIw7UC1xd_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دونالد ترامپ در اپلیکیشن تروث:
🔻
‏هری کین، بازیکن انگلیس، یک بازیکن فوق‌العاده و بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98529" target="_blank">📅 06:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sunOhVr0-69f_nFiWhxiwz5AyYAXvSBACcogkbj81r1PgDeKJo1sfwmLvwAVIgmTF_DIHRxuMM3kkJBzvY1xQPP98wmU9zQ4bVIzlSrOVt5G6--ZfSEfH-8hFTkV1u4scSfLyd0o_XBAQqvKDFbbanBQgbB3YQieDvYl4niUTaMitqscAN5aeDIc9p7OUdC1ggapXHN9RT7n_rxYOvBLh4Ik2diQsqD7KpC0Pcrwn4wjnONh7s_GX82RREuRwRqPOVXXXDBT9Ukvjrd55-X43w1JZBdrChiwXiTjXhA6a6NIfHjNBWLAEDOw9HPRtwKON18mvfEk75MS2gMt2k0p6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
دقیقه 36: انگلیس 1 - 0 مکزیک.
🔸
دقیقه 38: انگلیس 2 - 0 مکزیک.
🔸
دقیقه 42: انگلیس 2 - 1 مکزیک.
🔸
دقیقه 53: اخراج کوانسا.
🔸
دقیقه 59: پنالتی برای انگلیس.
🔸
دقیقه 60: انگلیس 3 - 1 مکزیک.
🔸
دقیقه 67: پنالتی برای مکزیک.
🔸
دقیقه 69: انگلیس 3 - 2 مکزیک.
👀
‼️
یک دقیقه سکوت برای کسایی که بازی انگلیس - مکزیک رو ندیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98528" target="_blank">📅 06:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YONJhCJoXmsddesSfAKJlccGXVtsYLnG9oLWzNcQNKYMN2ehsDeU3evfI_ar9nUSj7xWJRqwRhDGI1AjhgtEYw_NcbQMMRKVTBgGRygHdvfJ8pL8uZFvW7MLof4le15MTYQCtisz0ht_KimCn2ge22NPwGb7ajpnzUxW15XXtnsT9L21jM5WUXZNBIBdZByQkhpeyjhSgz5fhurrQNHyCDKLj-ZEE6PD8nlx2xp6L-RsRbXb9zr-nlLHkJZasnQEn-1QvR9rEzg3N6VY_7o4GteiKu6YbvUS1wXpLS8ZKBLEbnkAogbMP7UmGEE4wsCsKsN9l9bBzUNbZs-5sIhYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XI9g5nl8PERz3cOl6sL35NnnE7pNwLFEQz1FuCUW3wO6b9C_7cinkBipj4thFLnuvaAYH-LSa0isDvc61cn4XBJRLlSIVjbRRdpBqHt1gY3z3lioFvPYxsRi6fUlM_3h96jkOrmazBtGWiQMrwJhUmqWQNLphCNbFdkmeqS9-1kSadxSncWHnwfv4l-D37zNtn03fDSXkoxh5y8N5zZsaSX_QopiZGRaJECJQJseos9OOBobM8Yx3Fot8lGAOJk9jhiwdl09hxV_gGcidFEdY11-H4Dm3xFFg4FrcFjjbj1i6S33WAxNMx-pA8_rxu7eG7TLx7uqVvtNpfFQpEeG8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوچوای افسانه ای هم از بازیای ملی خداحافظی کرد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98526" target="_blank">📅 06:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtE-H_Wa3C8NHodV2TJH39pECpQ4EH6nBymMl44bWVwzogwtUv9PDToQLYyjHUPJ920Xp3B6HX-RmdmLYRsfcFGyRwvNLR69OPygMctR6k_GG0zuNt7kDwYS2WVJwJtUB_pHptTTMjVmHEM0zD-kXEcviU3_R1esUW7It_eAJHezDjROOaUFU_InXbfObsVPcqFiItlBWgZn7kSpCi07Tt805KrVzrJyoxWufRKB0-s_57GB9yL3il-0Cbq1dCC1MrIb69Ud2yDebGZwlAX9bdGeHyqrNyFyPYX0C_fXr_jxqmy-SIbg-9el2xlsGm89eGrKXyn5AbxdAh3vwdHQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
هری کین در این فصل در تمام رقابت‌ها،
73
گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98525" target="_blank">📅 06:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6vAT_EY6d2gNXOW5Hzujs5C3T-IUDq4vHSobSsxNb4geP_0JuuJ4zVo7ixriUywCmpURxuyDt2MLpXEycM3CVhVYiimSEXnflQkr9j-YiYikygMLh5jlBIFO5hIo4XU543B7BaM4lGpgNdyJl3qSgh3PmzN9jwIiQRkeeUmqaeD8APz7fQoUUw42Jb5D7EuotART1Wtpv_UHW_pUVNYejUHPNmN85tKlUh2jPKMjltWZZQX0iDp2HO0dwqWB1Q6VMV9JT-oUcDkBHX2bkdivhemEILGZMqnc7vwxNM4D9-4agO0Oq_2XNtRoiFr2wZe5jpkGC_2h2r7P3vAX7rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
واقعا مکزیک با این آمار هیچ‌جوره لایق حذف از جام جهانی نبود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98524" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98523">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ-B43WVwvs9M3U9mf14sfzHTqKFcbpNYyX5Rs_3mdefsxULSPvOfYrfSX5har5UT85JnUt8cX5zoFJIJWGI_uFxlJLwXb7iAS7Z6UVccl-qZwUDK2l79Ve8jt5mkQLri3cO1_Pglu_PB3Upz6rh0ur5cBp2Ju9H7gj3BNsiYQhmeT10zx_GbBZuEMF8LgDsVdg1olcFfirVuUax4wQt_Yfm2FrIgMWjerxpVbC3oVwdTgKlSc7p_E_eTJRExuQcnjxj6mI2GqqpzQdDdDjQZ1zRyUWqoU45JsZ943aZhpxTHkXVQoC_ngGthbLda57paljloU-A_OD-IEQg7NdOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇳🇴
نروژ - انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📆
یکشنبه 21 تیر ساعت 00:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98523" target="_blank">📅 06:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz6uHNJSeFXP2NrmlwyVmF1OTWrNhKSyFCnXXQUePDDmps1ELvqPd9AaLtGvCGeH3HQE5FOXqLr7lrtPLz2g08aYjRl_S1vmoUL5ro-af1Yn7KUFLLgl6MvFu6KdwmhfSlac1lQ5VKuhAr_5XJNDST9AZ_pfltEo0_eakoOulXsL5QyCm4FyeK2rkapwJBq32yT-6kvMxk-OHlB3g6JIzLH1Hc5njsFqbTIl4zLjBPFbTveJt0EBII8h6U5dv2TnC1Lh7oIRowp3YY7_OleW_rOF0nVkuKqIqTi4alclOGDuWhB8sU9fs8r7A4tkjGaowD4XDL1q2smny6rhD2T8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98522" target="_blank">📅 06:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikOVcuBDHQ-RcPAltV2sNHeXrxkwyVbCfPyVqnyZ8j6RRNuEaYcxfOv6YJGgiNJYzjhG2r3bUVxwLiqOv2ZdSCA94DfO2fKI07H6zKE7oEbVinY7l2i6DhpuSWZIctKSF3DXPnUBKJcetES90vXDUfbq2QJOViycypPgvA92TQpCmgGoIb64xFeiUmTUUTUvnPLxVt3-pFRnwvF3-YNHVyE-4xerymd2LMVvZd8E0Q51kigI01gaiO8irdRfNj1W8ACoSDzH6vomx4cw7R7q4kduDEnknrACrW-v0pPqYkMqMMN988b4U27SQ_nEV877_2mj3c92mjIjp3meEf92NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد انگلیس ۱۰ نفره مقابل مکزیک در جنگ فراموش‌نشدنی آزتکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
3️⃣
-
2️⃣
مکزیک
🇲🇽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98521" target="_blank">📅 06:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98520">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">11 دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98520" target="_blank">📅 06:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98519">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98519" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98518">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حیفه این مکزیک حذف شه از جام جهانی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98518" target="_blank">📅 06:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98517">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB8E05ljnlviL83hnNy3BNNTRf_s1yNeCkuycFdS_ClOvtto6FE36vemszbMfRoHXoZVWVvZnKi6gngdMBQnpnCNY7nMlgoR9THRfjS_FOANM0MpX1nhcu9wT1GDo-gP3UHjLNbS-CzuI9m5FkyxbVMAM7KnFT_njKf_DGPRltQuuqXFaLxwuNG89wFh51gM1nJdJIpemT7LoRjleNmH58CPgpeQVN-E_CtSJv-6skniVsRKANmoCWUDJudv7bgQd1Fugq3HvvdqCJhGDS-i4XUEsaJcjQpoV61qLrYj76it7CERf4O2ZpC_A0bPiufyFot6n4jUWhYdM6tRkQvYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی تو بازی انگلیس - مکزیک:
⚪️
اخراج کوانسا بازیکن انگلیس
⚪️
گرفتن پنالتی برای انگلیس
⚪️
گرفتن پنالتی برای مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98517" target="_blank">📅 06:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=ggL0aGSQih0_nlCdasZBAj8N2niFYod9SV0NutxzA2uAOzj5buXocJPzFtBVnNktXE4zoGx9kMAqdBZ9x_8rjrzj1elpKOLQkpnuZLIceOCPNRoZcIdTWH5Qv6FbE0WXpX2MkCpIb89agYGsHVQvJ0z0kNLoPkIdThx6oi7cNC6XWQDpnStJkETFxQGvqZxx-2kH1g_etM6zKtG9ivbx83Lyudz-Sd8wBii0GtTeAnMLXCfFbHw_ExFkjGO1MpR8D65EfIai9QwmpWHNdAsM2T-Yea9cPEiKarRMs0reaTrNAmxTnxn7V0t3emafTBMY58xpoHyS5GgXTNSuYL0ATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=ggL0aGSQih0_nlCdasZBAj8N2niFYod9SV0NutxzA2uAOzj5buXocJPzFtBVnNktXE4zoGx9kMAqdBZ9x_8rjrzj1elpKOLQkpnuZLIceOCPNRoZcIdTWH5Qv6FbE0WXpX2MkCpIb89agYGsHVQvJ0z0kNLoPkIdThx6oi7cNC6XWQDpnStJkETFxQGvqZxx-2kH1g_etM6zKtG9ivbx83Lyudz-Sd8wBii0GtTeAnMLXCfFbHw_ExFkjGO1MpR8D65EfIai9QwmpWHNdAsM2T-Yea9cPEiKarRMs0reaTrNAmxTnxn7V0t3emafTBMY58xpoHyS5GgXTNSuYL0ATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🔥
گل دوم مکزیک به انگلیس توسط خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98516" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فغانی رو بنازم
🔥</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98515" target="_blank">📅 06:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه فوتبالیه ولیییی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98514" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98513">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">3-2</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98513" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلللللللل برای مکزیک
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98512" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کین کارت زرد گرفت</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98511" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98510">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رائول خیمنز پشت توپ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98510" target="_blank">📅 06:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98509">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98509" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98508">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پنالتییییییییییی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98508" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98507">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه سوپری شده این بازی</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98507" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وار داره پنالتی برا مکزیکو چک میکنه
🔥
🔥</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98506" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فغانی اصلا تحت فشار قرار نمیگیره و شدیدا به بازی مسلطه.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98505" target="_blank">📅 05:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=ObIPhotl5vAW0v75OVXFCO6ORB6_dQCIHKFqGtDoW6fZvWF7-KRLJyl47z9l1jkzdvpsfd7nrK3LEmVOBwUJyR4VF7fw_WY2SCatFAlVjRJuUuyyZ5kR2SQld21Ta6ZJkhKGqLOPSE2B8lGtX6x1wqlR1xhfKnfwvnOJK8TswLOo0BPwIIcInw7C5lGdZGzNaKgxeNQzCETAnWTf16gDZ-iz7okkicshosuh0TRHp3lCaDPQTxYu9LJvfh1prDpUukGeeMrFk49Dfp6GCGrpqLhe3YTbN6AigsAd1eaSTqoazFF2GTUacGzEtRFdd21cFtzFmPIC6rfwp3FOP9CRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=ObIPhotl5vAW0v75OVXFCO6ORB6_dQCIHKFqGtDoW6fZvWF7-KRLJyl47z9l1jkzdvpsfd7nrK3LEmVOBwUJyR4VF7fw_WY2SCatFAlVjRJuUuyyZ5kR2SQld21Ta6ZJkhKGqLOPSE2B8lGtX6x1wqlR1xhfKnfwvnOJK8TswLOo0BPwIIcInw7C5lGdZGzNaKgxeNQzCETAnWTf16gDZ-iz7okkicshosuh0TRHp3lCaDPQTxYu9LJvfh1prDpUukGeeMrFk49Dfp6GCGrpqLhe3YTbN6AigsAd1eaSTqoazFF2GTUacGzEtRFdd21cFtzFmPIC6rfwp3FOP9CRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللل سوم انگلیس به مکزیک توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98504" target="_blank">📅 05:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگلگلللگلگل سوم کینننن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98503" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کین پشت توپپپپ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98502" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98501" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برای انگلیسسسسسسس</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98500" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پنالتییییییییییییی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98499" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeOUO0c1ANIj76j2AC03aD_mBsVYWtyTHm61SAzYL_Rs1EHCPrGX5g6NMZ1MnhxfSCRpCaHyGX-1hD6OmhX_wwnTnuSHExJAueZFyTw_JFE7nqh3ECGEI9IrJmY0NsgWp9oaLrQHXhplXpCsSN_0J7L1_KiQI7NXDpYfg4vLq5VOiXNapNVmipmTscy8-EUBAh9ff_vvpRaDv0MDlyybv9WAQfHPRrmvzy4EI69KBYd6dF9AfyUiOGwuQM3dQUChO20ICkuxXbE5Mx1AzWr5YR5KSU8upd5dx_bPPz2ypknJ8QuppM7dvI018qD3OcUecq3XoeZHz9YEHpv-SPknNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98498" target="_blank">📅 05:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98497" target="_blank">📅 05:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUgty5cIx_d6X6juofZJIWj1MCTe3KCmd94sc6FxJleeyy3DYD-XM84gsSmu36cL-0YBCDL2xkk0X2mO_KMKmOEIswO9e3kZ7l2Fte8upcG8ZRQxkUnaVLfVjRh7LqTb45kYWI61hmZn-qqL51mTww8tSxYe5TO1ZPbDeZgx0afkIj-JShF3BLpbCmLd6MkxpWGklxn4BMIao1XtPAE6HkkvXLmrisDllll8DfBjYPsRT2VriMZSMvi5aKMLhP8BILrxDgEiv_SUkgOFQTnylkyQNSQwaMEMqlEoMfA5tYhIrK5aotz8IuGco8cjFZwc7HSkPf4jkT0aAgAOrPvW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با گلایی که مکزیک خورد حالا تیم ملی اسپانیا تنها تیمیه که تو جام‌جهانی 2026 گلی دریافت نکرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98496" target="_blank">📅 05:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بریم برا شروع نیمه دوم
🔥
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98495" target="_blank">📅 05:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cp9rphZSsZJITIK9a8qsu3SR2u1EFjLiSlFpokV7GEV5zAWKSbDIvavOYp612jVsiORmyZb6c7ooMDAx6AK_G2f5JJWeSdYA6FUi1kuvk_uJz1qRqgp9N4qt8LZl1-iUp2pfBNILqdatRmTSJXivTkCHQfz0MwSWyQD_RrNkHaO0ANV-7dRBFjT0u6DlRTHgswKfYS2Q1zONPKheO-F8wHgNBiKUI-vSyXJiZhPyAB5rNklmcnKPiS6pVdD0ysPbWXtwasfF2S3RvN_vvleavgSEbPELmmJRIgrec1vCTnbT2d4RATWmEbiriJxSyv-cco2G6baceP021dLyYKHcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">19 نوامبر 2026:
توماس توخل، مورگان راجرز را در پست شماره 10 به جود بلینگهام ترجیح می‌دهد. [دیوید اورنشتین]
6 ژولای 2026:
جود بِلینگهام با 4 گل گلزن‌ترین هافبک جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98494" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPelmUWS0coExaet-xNFKrF9xPmrLf72bUkL-sUmJGFdDMyPylq3ooJBFPVE59mNTO8m-StjfIzWHmBGbN5z3i2DCQWMN8QSgLG7zBPm8RUCF_QSEV_DaBEUnkFp2JekVxxv4VbStOHpTE6FRwsqpJGUfejH4IKYxWJ5TuXtDITUTpRZuk9LDVWDrkG4-lJduJ6tlu7ZPdNp3oO7NtseqvLjksA4_t89xb9paFWITsXzpN_djJXndP0iHnrcg83ddfjT5IBWZV_1KDpZVY13ldvbhymwzsIWvfT7-Ihch5Vfu56q7LxlylA9SRy8JA9tQ11JcM29Xu3K43AAGUUH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیلیان امباپه: 7 گل‌زده
🔹
وینیسیوس جونیور: 4 گل زده
🔹
جود بلینگهام: 4 گل زده
🔺
🔻
کل بازیکنان بارسلونا: 4 گل زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98493" target="_blank">📅 05:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG9XWHOujzdFdcrxADaRqCHNw_Tpg0s_bi7BhsD4vEvafYzXr9C2DHENm_vSnpO2qpuDvPIVokbNZC_Z4lnQnvTsQunigPKjzuXIUoQA7pS0P8mtOsg1bIbEuCy7tpVNH-C083Q__zsnygAhfKQGWV5bRvQB-can3OT75U6DkJrU_uxw9SHqW-SJvaLAmHxxsgz5jlHVSxSO7cN8BQR-bJe4etb6la3QQluGSL67HHWcjnex5jveAuSaINVZUasYhi6Awd4U5ZMcuH6dZ4d6CDNyIGm1OWNNNFMjZPy46zP74PvqLmBrX7XzoQ4dyKwN9MocRYFC99iW8f5RKjh2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98492" target="_blank">📅 05:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOuMlkrr1V3xR5ykZX1-7ssIIdcNOhA8207k0vJMa0yX6FCslX0wr2qD33orHQxtL1-WAOdQu88evz4wHH713yWB-lN3JTkaYIRAzpRBSaWapemB11643GF8tL7EN1mSkUgrZ9E1vKwNdRJkZAlvmAuApi3pAr7icy4uL2ezOtb75ItCHOU1hikMK8VIHmkc7ck7SYLEWV-nEv2nMCV0P-8j2w1dF3zB-ziX-z2fYHoZZH8kiMcGsPwxOLhB2BYHYmC91KhYAPKnu8-p5v-gOg4qGVEwdxVIWY_TXfY3kgASKU4yUZ2QH-CPdH9njajMByZpV7AIFyftSHznO0QVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUUUURRRRRAAAA
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98491" target="_blank">📅 05:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BifK6HRedQ6nxzRWaoeSpNUcwif44FNMpoQKimoDZLN-Xw6lRAca6XRaO0vvspPyvRVTKYyuTQDIxfN1OB7v2cGyz_Mi2PGYqHIP5QWSrD9BSdc9oV1qvPsGSNo5EFoCG89sseSnpBlub9irIwVtjnylr68GsfYUWfxDern3fybRYEp3DkHxzhiW2rjmOFFi9mTRurKDLex6xV9Yw52cXi9BtysScM_O4ZaxpUoFvxgmYRyFKd8H4uc4eS_ZP5RC3oiuJ-V4wDZLyRjSSUl8v8x5MpgMbhPiRIXxkEGLr_p6eyzfHMgY0ELPyqm5wT2AHzUntpQpIuZ0XafKqkvXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
تو جام جهانی 2026 مکزیک هیچ گلی نخورده بود.
🔺
و اما زمانی که بلینگهام از راه رسید: 2 گل خورده در 100 ثانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98490" target="_blank">📅 05:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیمه اول تموممممم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98489" target="_blank">📅 05:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مکزیک واقعا داره عالی بازی میکنه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98488" target="_blank">📅 05:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=q1dlHJ0kAKlUa4G0fCJ_F1S17ee6jRJVk5obB3JxZWvHsQlOdP6Xhe1MMZ2cU3HhJtL1ClwqD5v3D7O-Ez_5iMJ-JEBNc98qwUEJdcEix9uU2l1RF-N-NDjwq1YRJ5WnbpE58nGQP9xfiGIjbAIjdiQAtnr1gOdC42EkQ6XJ5DauJyqsHLX4ddSa_-kMvCBAPP74g2vSe5bio8wFN2P2Li86Nke1JmsWMD-X-niIjiDBI9xhtTIJpYs2wWQUmCmaVXe46IXgjrKwNnDiPivBK1oOQ1iHsSEPRBNqbCZDPYyfe_ur4YoAGp0ZHQ-vrZvtqzH-EzszkaXfBVezhdHz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=q1dlHJ0kAKlUa4G0fCJ_F1S17ee6jRJVk5obB3JxZWvHsQlOdP6Xhe1MMZ2cU3HhJtL1ClwqD5v3D7O-Ez_5iMJ-JEBNc98qwUEJdcEix9uU2l1RF-N-NDjwq1YRJ5WnbpE58nGQP9xfiGIjbAIjdiQAtnr1gOdC42EkQ6XJ5DauJyqsHLX4ddSa_-kMvCBAPP74g2vSe5bio8wFN2P2Li86Nke1JmsWMD-X-niIjiDBI9xhtTIJpYs2wWQUmCmaVXe46IXgjrKwNnDiPivBK1oOQ1iHsSEPRBNqbCZDPYyfe_ur4YoAGp0ZHQ-vrZvtqzH-EzszkaXfBVezhdHz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول مکزیک به انگلیس توسط کوئینونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98487" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کوئینونس با این عملکرد شاهکار داره عربستان بازی میکنه
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98486" target="_blank">📅 05:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تو 6 دقیقه 3 تا گل رد و بدل شد
🔥
🔥</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98485" target="_blank">📅 05:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=M1ydN1kFGc78cisFoCs2goUVPujZ3ntTOymyjsw5lL3W8mzfqAIVW3phiHwVt-G4fAoppHAwgW7mTHUXZfxOdvoOhAPP8o67IaAiLSp9uUQHMJpjO1hUis02PNPQkbUNRPWERja3W71rue8E6xyOQWT7YEE3MXAivj_VacTpkrH-XynIFGt-llZ1L1va1Y6kwGiGynbXzWTZAb2uwoqfvIRriCXZ5Qx4z_yZxWe9qxUxPCfD8LgTyR1IkWLop2vcmILyOAHKiLLfF21p_c3KWf1d4Q6shkNfHZZR7n_LC3w0x7AUhxSJdwoLPksMrjH6YhovX9FD5hXZZLOBVRk2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=M1ydN1kFGc78cisFoCs2goUVPujZ3ntTOymyjsw5lL3W8mzfqAIVW3phiHwVt-G4fAoppHAwgW7mTHUXZfxOdvoOhAPP8o67IaAiLSp9uUQHMJpjO1hUis02PNPQkbUNRPWERja3W71rue8E6xyOQWT7YEE3MXAivj_VacTpkrH-XynIFGt-llZ1L1va1Y6kwGiGynbXzWTZAb2uwoqfvIRriCXZ5Qx4z_yZxWe9qxUxPCfD8LgTyR1IkWLop2vcmILyOAHKiLLfF21p_c3KWf1d4Q6shkNfHZZR7n_LC3w0x7AUhxSJdwoLPksMrjH6YhovX9FD5hXZZLOBVRk2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم انگلیسسس توسط بلینگهام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98484" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مکزیک اولییییی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98483" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98482">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پشماممممممممم عجب بازی ای</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98482" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98481">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=LC6gpaPronubLv6gXpJQ5VSPyK9v3j5HfGq2yt6u6oaYoW0MWlUx7JxfhDZVD3aoyjYrM5W7ly7sycdrOFM8ta1Bzt_tL5iHj9yXxmDkVQd4V7py00yWF_eEcFXXjDOHIvgzs-zrH83r3XtjYJ6lTeK7m9zdIIifO6MszzNx4px6wTwEbuHr05mfwCQ5ECZJfbY5PCRp8_CzwuPYp0wTZ-b7bXfubEN4oq7vUp5oR9JCKe5Fuo6o5sxeY9H7mL6FtFZmT64gYYOp7iftFoLx_r_GIRusjSBPyCgGqYrgnTwT7aNOCL68aMApYznCzv1GGE0lRyFo9swq5V1ohe4QHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=LC6gpaPronubLv6gXpJQ5VSPyK9v3j5HfGq2yt6u6oaYoW0MWlUx7JxfhDZVD3aoyjYrM5W7ly7sycdrOFM8ta1Bzt_tL5iHj9yXxmDkVQd4V7py00yWF_eEcFXXjDOHIvgzs-zrH83r3XtjYJ6lTeK7m9zdIIifO6MszzNx4px6wTwEbuHr05mfwCQ5ECZJfbY5PCRp8_CzwuPYp0wTZ-b7bXfubEN4oq7vUp5oR9JCKe5Fuo6o5sxeY9H7mL6FtFZmT64gYYOp7iftFoLx_r_GIRusjSBPyCgGqYrgnTwT7aNOCL68aMApYznCzv1GGE0lRyFo9swq5V1ohe4QHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول انگلیسسس توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98481" target="_blank">📅 05:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">2 دقیقه 2 گل برای بلینگهام</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98480" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازم جود</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98479" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انگلیس گاییید</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98478" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دومییییییییی</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98477" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگلگلگلگلگللللل
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98476" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بلینگهامممممممممم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98475" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انگلیس
🔥
🔥</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98474" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گللللللللللللللللل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98473" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=tVc5pDO1WjHdB3_y2_7FQZCzPdw4zfyy1Tav30czThTw_wT47DicJWvMonX4B4YvhGEuzsUp1pOC0-bKaQaeK7xLDw89V4N8eODuUHvSsRHbf-q0hMhGqUWGFBOz38sDoKEX726I0-jlk3REC2eBf7JsXfsHoi_5oNR79jbUZdVz6aVgflEbSTblKXoARAueYuYD2XAdGCEo4kU0GKaiG5Dqxeik3HaU0_ctQ7YDiJhc0Da9DTDuSdaf3Jcr46nMaQ-1s43SDp0xUJEFeaIdWMThdEAds7ENhoQ8BXjD1h9AKp7ZKNyx9sXpeVmznoD60ROuht1wHNyyVPsBzDicHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=tVc5pDO1WjHdB3_y2_7FQZCzPdw4zfyy1Tav30czThTw_wT47DicJWvMonX4B4YvhGEuzsUp1pOC0-bKaQaeK7xLDw89V4N8eODuUHvSsRHbf-q0hMhGqUWGFBOz38sDoKEX726I0-jlk3REC2eBf7JsXfsHoi_5oNR79jbUZdVz6aVgflEbSTblKXoARAueYuYD2XAdGCEo4kU0GKaiG5Dqxeik3HaU0_ctQ7YDiJhc0Da9DTDuSdaf3Jcr46nMaQ-1s43SDp0xUJEFeaIdWMThdEAds7ENhoQ8BXjD1h9AKp7ZKNyx9sXpeVmznoD60ROuht1wHNyyVPsBzDicHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقای هالند خجالت بکش جلوی ملکه آینده کشور به چیزی تنت کن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98472" target="_blank">📅 05:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فغانی برخلاف تانتاشف خیلی سفت و سخت داره تذکر میده به مکزیکیا.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98471" target="_blank">📅 05:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داور بازی هم اقای فغانی عزیز هستن واس هر قدمی که توی زمین میزاره افتخار میکنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98470" target="_blank">📅 04:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازی خوبی بوده تا الان انگلیس مکزیک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98469" target="_blank">📅 04:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqu-Ls1dVNveh2YZHoE6z6V3qdVW-r5e7CKY2xyeWs2vFwCZctT3VAZBc9i9jfNuzRvRqKttHSAm5BNPia68t0hFSX5673f4qhydR_krKNEz8Y_fK2KGFF_mokCc6epK2k0KutPsW5KfmAJSMk-Wy6R8nGR7W6mvAnNRTBzQeyLUxFsW18LM_YigTvvTJLm8xSn3rRsP3X37SQ3dMqtaEmJyQGs5vZx65F8chVRYfdlKSLKs2Jit7bho5vrJLk1NC1N2V908Cq2_GemEoFrhcgA10vt4lzgi41kKidRMjm5KTSd-VJp4JJB0fTLWmIQTiUQm4raWkBD1hXMZI47uGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمار در تیم ملی برزیل:
130 بازی
80 گل
58 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98468" target="_blank">📅 03:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoECHQpAi5P9uIPcQn48h128T2QCdo2m8SKIV5Qd4wQigXrSaR0Fwzb1HhCE1i7WislpJtuElDAZfYcEZpYpuAHT3mK136frMUwbPz5Gr8r8_O-k7d2e9LShVWseYaOyW-OAClVRhK1IFxA1uCAESbVSxGSmzGwmq2FCsfVsLr4CJqB6HU2UH0a-rt8QiDeuCKJU96s16qGvVKYg7pjo3NlafHLmxxRpO5QpFhzY32yZlIshZresHq-wWnXEyY8IDli3eXS0nkK8oGKWgoqk-TWvyu-V_2e8dsKTgJTB3y78CdrRb87mMiFvhT2FI_QXTpAaR3ew4spALYhU9vuC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7-hunqGuydCy6v1ZgzbeHwtKEsMYG5P3OeiMSwuuwm-Yl2-9xUtkGuaJrX6KodLMtKRGzQ51-pyc752mg9R-w8AZlzpShdRwuw_1I67du9zRSC3OmyrFht8hpLDQTHJUvbpugjHbmE-IqLh2f49-3Z7ED_wmYXgTQsxsuJ0qNCI_UldII5qgldmOXQJYWvmYuInyIcEeXJuHrh-nBR24JWUFev6z4Hr2yuc0GciMGXi80eBDM0dIyyCytQ2yaPo4gqpa1UNdZSLqhBd6htawRI_zZOeKQRp_TbcMmLbUBOnEtJvDMTBrR02kqzMt7c73cO4ds7Wl7z4oXj1Zlm0Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98466" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98465">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=QAiyvFyOFT3Ku82-kBLmKRbO7FtvpeXq_UCNYBOCmI9bYqOXCI2bz0qCEaK3JRQ5Afz_NyefHJ6h4d7oIX_cq-xqdT96DJPombDDLEeX2vI_c_b9oJHj_jtWmm8vxggtei47c9IYSoT0v01Co8rRZ6d1Owj6Xy4wXJWfWVK7n29k9B23aRaaQhcvXRfvwrrmedM2dgyFYdwllpPIzjnsG5DAoM_27RTwG05ufiEypEgT4zahkaiTNBrBbn6mL1p1_IUwKhs3DgWR-OA49O7sY8Ct7rEEW5pFg-BX2GjSr7yHyeWUtJI1BwVoqB92gurAL-m31hZhu5wjfUQBNlNySRXXSA50DMHzjZ0tYt0JXZVTxg97EaE_MiitSGIK2Hb5-14WlfpUekDp2P9nj0QDQqAdSzf6vaNnptY5gRUqVES8RGOcwOAePjkEeOpyItrhgHCTRQ0RqFeroFpkfd7pSDqWuCrBh-8eh0t2WZCf8WzY1gqmey5q06S0vOn-r18TtWWahf5kpMMS2nVPfBf4Y3CWcijyjbATHTJl-umAA7b_3Wk_l9HVL_iT92eVvN3uGoOLp3kTxZ_e8VgCnB_j6xO1lbhKxgZCQ2b4bgh3SdV1v0Fr6mauIm3-utK9x1vp91qy4nqWC_RbF00ysy59kt8JuAVeURS7vdKOcU3NjKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=QAiyvFyOFT3Ku82-kBLmKRbO7FtvpeXq_UCNYBOCmI9bYqOXCI2bz0qCEaK3JRQ5Afz_NyefHJ6h4d7oIX_cq-xqdT96DJPombDDLEeX2vI_c_b9oJHj_jtWmm8vxggtei47c9IYSoT0v01Co8rRZ6d1Owj6Xy4wXJWfWVK7n29k9B23aRaaQhcvXRfvwrrmedM2dgyFYdwllpPIzjnsG5DAoM_27RTwG05ufiEypEgT4zahkaiTNBrBbn6mL1p1_IUwKhs3DgWR-OA49O7sY8Ct7rEEW5pFg-BX2GjSr7yHyeWUtJI1BwVoqB92gurAL-m31hZhu5wjfUQBNlNySRXXSA50DMHzjZ0tYt0JXZVTxg97EaE_MiitSGIK2Hb5-14WlfpUekDp2P9nj0QDQqAdSzf6vaNnptY5gRUqVES8RGOcwOAePjkEeOpyItrhgHCTRQ0RqFeroFpkfd7pSDqWuCrBh-8eh0t2WZCf8WzY1gqmey5q06S0vOn-r18TtWWahf5kpMMS2nVPfBf4Y3CWcijyjbATHTJl-umAA7b_3Wk_l9HVL_iT92eVvN3uGoOLp3kTxZ_e8VgCnB_j6xO1lbhKxgZCQ2b4bgh3SdV1v0Fr6mauIm3-utK9x1vp91qy4nqWC_RbF00ysy59kt8JuAVeURS7vdKOcU3NjKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت چمدون بازیکنای ژاپن با بازیکنای قلعه نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98465" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98464">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98464" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98463">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_2gRCUy1LyOiNfSvMOCD1V5-vUxYFQ1sV-FXEKfphb5GLFHLGvlFxwxrcq-fuLpJ4uLBBNHHO4xEIqNw9Vp8khfjL9jNGKKJPHuWZZBGixlXnZtLOA1keqluZJVq5ds8kNM7HwkSrcQd9CYc8qKYstFgWnRJcEXAooi86A1y61AUd0ZkPAbyP2TQNah1OTEk2ypshH2bcvCc2gbDxUOAVB3dNFg-cNJWQoDYomCaN9CXV-6uUPP-ZQCWQIB4UOwAnQQ7Gfg13RFfN-x0gfOUybgk04Wq-VPN2njEXhNUeyO5EvVZN0NkwnT7GPInPR3AKEXG78OC7Lx1Udzi0lpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98463" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98462">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=S0ROnXYgJW1byp8Vz5sl4ovdGF8EHH8dVyiugePUbOh1Pv8Q7ssimpOWJD5JSjf3cvzh_OJujR__keDADZFG4iP0JC1Mwp1q4HSUECA4n7iJkLXxCUxxl0_iwEARpa2_9JUyHqV1_kffYjW8y2N0uogzePDdmaolMmCrD_EJjsagUWEL9RypHqaRZtjKdA2Fv61pSNdfLA_MNXuwosDVk-lMaCvTucgbFojq9BTuwYN2zws1yoYRjQQChyrCmgiNZMcthNE1itn7kc2o018AbC5Pd8OM-6UztV6m_2u2iErrlwKcb2JMobi5-i4Q1G3vLXfEj2KAwPH-zVmcTVBN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=S0ROnXYgJW1byp8Vz5sl4ovdGF8EHH8dVyiugePUbOh1Pv8Q7ssimpOWJD5JSjf3cvzh_OJujR__keDADZFG4iP0JC1Mwp1q4HSUECA4n7iJkLXxCUxxl0_iwEARpa2_9JUyHqV1_kffYjW8y2N0uogzePDdmaolMmCrD_EJjsagUWEL9RypHqaRZtjKdA2Fv61pSNdfLA_MNXuwosDVk-lMaCvTucgbFojq9BTuwYN2zws1yoYRjQQChyrCmgiNZMcthNE1itn7kc2o018AbC5Pd8OM-6UztV6m_2u2iErrlwKcb2JMobi5-i4Q1G3vLXfEj2KAwPH-zVmcTVBN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت کارلتو آدامس  بعد حذف مقابل وایکینگ ها
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98462" target="_blank">📅 02:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98461">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aJwTC3Bo5xaXd4NJMDN-ff1wJ3XzmF37gyDxxPplxKpVtxb6QXWQSRRPBmEzrvxm6-oPdARPdgyWLVKmzA9pnZPyq-WTQtHHFd_frAjSzbI0acm6H_TmWGgTyiq179nhVZGfLpYQz1669A4TVh7pOGL8dR1O3C394ZA5NkLeVUEw1p9St3lZ8SdO-m4yonpXhswhKwGJxFuUJE7XXpQ_c-9B4r86TJfDpEEFYk63FyEPvRPCbfKtWmXX7Ggs2zC4G2cc8HwN-pHAoP4Cuc-qYxzcabEGgYR2PKP1aVsLubap8_DxrEZtFGRPWT--ZdAFqG_h88FS8t70Ioz7mLgbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار: تلاش خودمو کردم، خیلی تلاش کردم. دیگه الان همه چی تموم شد. از اینجا شروع کردم و همینجا هم تمومش کردم.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98461" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98460">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=KxVa-U2sergkDC4cYNWAI3b1HJKxaCuP-L0eLTjHk9hZmTfi34KA3HqQ0d1A6vlUJsF-ING68s8h_YIZJqT6Gcbz45E9FB5NSSGN36XgQB6snvbH4Px_3Q8CI5ppoDz82CfBOmX3EBQxQTLHV4InV40DbSB-BIDl3zliZlm3VsU0N1XO3zERR7wiAgeT2kHw6s2ueU88bAHA-60f8O9y9AW5DlyvuvLXsNcAfjo9RRrvZlylBjUIrH3YQQv53-pkykkpnA02-M-40G7dZqYjIdbHNbNKySxat14hntPtgcozq3uRaG91Kde-GYct-RIfexBDgKVSIGv3Zj6fofk48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=KxVa-U2sergkDC4cYNWAI3b1HJKxaCuP-L0eLTjHk9hZmTfi34KA3HqQ0d1A6vlUJsF-ING68s8h_YIZJqT6Gcbz45E9FB5NSSGN36XgQB6snvbH4Px_3Q8CI5ppoDz82CfBOmX3EBQxQTLHV4InV40DbSB-BIDl3zliZlm3VsU0N1XO3zERR7wiAgeT2kHw6s2ueU88bAHA-60f8O9y9AW5DlyvuvLXsNcAfjo9RRrvZlylBjUIrH3YQQv53-pkykkpnA02-M-40G7dZqYjIdbHNbNKySxat14hntPtgcozq3uRaG91Kde-GYct-RIfexBDgKVSIGv3Zj6fofk48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صد حذفه داداش
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98460" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98459">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
بازی مکزیک مقابل انگلیس یک ساعت به تعویق افتاد.
این بازی از ساعت 4:30 شروع خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98459" target="_blank">📅 02:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98458" target="_blank">📅 02:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-poll">
<h4>📊 نظرتونه یه ۳۰۰۰ دلارو بت بزنیم روی برد انگلیس ؟</h4>
<ul>
<li>✓ نه بابا ریسکه</li>
<li>✓ بزن کون لق پول</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98457" target="_blank">📅 02:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98456" target="_blank">📅 02:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrcgCKYAYxGnLhChcb6CdfhPbDzAuuE_STDLqKeahzGho-fTsbNgB_B2ST8PjKMyEsqzJG-HZRnMgm-6r1HThHaruWXN_bSnioxUwMfrRoyt31Lim7kMCqZL-ZnjjXeYmM2MoT50TpUVybHp6gnX3qT44-EQCgo1-8eMomfcBBNV5eH5SL-nRBc10Jwb9CO6rtmlfOhwp9aeGC0c6iUaLXXJSPLmoscOgF0HF7vLlMw-6tiljPuXvFPzawh-cfhcHR_ik0QDB7McXEQPw9MR-tUOmiPODhAIPA-iyYYCqC_8vYIpt96QObtswdHJ0xR_LFxxNstwwkyY5-p7CPKPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98455" target="_blank">📅 02:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Puj1yYTTUzylPwvoOXygE7nfBJEc5fB_dhcpaT94O_fw94jLyn5i0CYYSdw__GwZ6UL4E2-wTylQnm7ZWaEdgJGPOz6zzWi7LVdqX1T2mMHT7iG3Kec9pxrnwIQjAs6bszoaU9FRH4FfKPAgU6dd53O4xec7gYuck3L-OdIKm5LM8FBCahm_2-B2gYn8UbLrDId3RIRzS9gVpT2-zEZ0tSRydAEQ0nHPpjSHn6JDBBH3SY9ja7K3CWtDsTpPhbfkyaV8fuYa0qTrsxn-SoczCI0X74Nh8QyVrQ1w-jcuuiK6GFKLgxl-DTp0zR9EfyUK_MQZrBZCXGqNtoskoD1hog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تو وقتی باختی که پول رو به فوتبال ترجیح دادی این گریه ها دیگه فایده یی ندارن
الانم برو با پولات حال کن فوتبالو ولکن
سال ۲۰۱۵ بود عشق میکردم با بازی هات بیشتر از مسی منتظر بازیت بودم ولی بدجور هم بارسلونا رو داغون کردی هم فوتبال خودتو
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98454" target="_blank">📅 02:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUgdOMdZOOn906nEuJjGA5gDdLcDikZeK_t_nigRUUk5zmIqtC3LPuliiW6rP9sb-mQ094RnUzJRklpMH0xWkiTaZKHKi5TyglVP7g6pIiD08cHDe-u-xeR7qdfsCug5UvfajVXs4iu_MPKQ8WFD57wW6KaiLzayZMEJoLPyEeRHWW0tpbFUlgzUIZ3sGncTuQ7eLq8eSQ7cmGR9t5ixxRPurR6IAVf2SXDhKg8RQh3ftHPMDiZRYJYFXDCpXYBTqOyLxJjM3SOURapOILLwnxVi05BE_IcLyniyVDxh_DghvBNQ5QTAf_XSHogYuPHpvtwbBtbASUkTUBdL2pox7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس مقابل مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98453" target="_blank">📅 02:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTgigfzagPg41oAW0m29dwYjF_gx7CPVYktd4-5gua49xXnE_EGkKSGIgKsMK9qIq_7T-lhv2hlO7gaq2R3MFWL-VJboEcpom0Z8qH6AT9NK1xygDDHt0kVoelxlgYviQaTvv-TQj6m9CTfEjC3daMr5wEdn5cp9ogW28RveiQOLhI03PdJCHRZnG05_0GhJjZlmxoqoZtGMpD-E7jyG5f-RXqXHdPtpdVu3-uGPGzGyxLKOFOr4CDWh4FKIgUukGEdCnuVfD4qJc92kiLKG_9KXfyYtHoOK3iGErZO8wErfs_HlybJA9fBdeHvsojhFBfBesFbKkUwYXJaxfHokcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برزیل برای اولین بار از جام جهانی 1990 قبل از مرحله یک چهارم نهایی از جام حذف شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98452" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL6nOIR7O274mWoYD8QHSmyHUaxR1bYjfEh_5oE-0h9tPCNlfbYkD_aszbCylbOrbBHyBGvS5A9SdGK-TkbQztpPrWWik4az6GsfEXEHv9cjrexFwZWAEHOiriUq0ySsGMvstW6BgRwkNiyxEZa1D5qkUEZ_pjCkn3-SFwyv-QfdRYkPEvV3ozvmbCtmg578ZSJtkcQGCKEbsb5MC6ZakVYEuFDmf5SmUs7HqCvdPxOnDlKEf54_5Pz6Gp0dbiFP9WVU02yj4E27aj6OItm9s0gOti5q9ON6eziteV6provVDY1NPJWwKoxQZYRzzDM9RsKtF9Fq-AomLDoNL2TL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بهترین گلزنان تاریخ برزیل در جام جهانی:
رونالدو نازاریو 15 گل
پله 12 گل
نیمار 9 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98451" target="_blank">📅 02:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leDHkyjNOUluRK0jYuLPmNcX6E36FsPydiIKlUaRee9sr9gqZYloZRzg57nRCDc0RdKTQsATJptLfR419ZO6Vwr4vGPh87BppOmpPp1x7A4OM2_0vWlnUI6kgtGDIDpzS5yBR-aiMMFeyF2YunxYISCB0Ne-v0Eif3j3_X-HlJQSt_S_knUQGmZDt8Uywg6MdZJM0s64J4ErPdwbGSB2sBjIDvJ1j-tHKKzSbNoq8uH64oGk5K0cnnHSKtDIZBim4pjfSOmlZNMIBPLfCuqqoeiJHHQT6axmj4xpsO5iQC_rmhqhyCeeLnaRnflOPy2WDwPTNHw36-WO7BrHHSlMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه بازیکن تا اینجای جام جهانی برای اولین بار در تاریخ حداقل 7 گل به ثمر رساندند:
کیلیان امباپه
لیونل مسی
ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98450" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98449" target="_blank">📅 01:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=pg7g1A14jtiBQHOIm8FNMLNLmalRkInpRZX1brWvJda-_sYz85n6gufJjG_D_FLd741gm5f1oIdwPxYv87YKFKbrbEKje6cIFiCQCJd9-uKWW8xSD_LA6OXupTQxCHXeCXM7svr1jlP6H8vwjAOU-A4rT-Pd8eTBA5M4kNaVM9Bfe6teiZ9Rb2MNAQaJQlcr4q9heVbZ8o4lneWvIYs3ok_OjAULwoMCA8rw8hvsao-ooHv5Svw2R0b3GTmZf2_ZS7KlF_cshftqIBMIXQxgaFNvD1pmyOPnjPf18WHSFCeixdvG6mYD0JticKir0Ga2jUFk4vjZcU1ppf0_CAaOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=pg7g1A14jtiBQHOIm8FNMLNLmalRkInpRZX1brWvJda-_sYz85n6gufJjG_D_FLd741gm5f1oIdwPxYv87YKFKbrbEKje6cIFiCQCJd9-uKWW8xSD_LA6OXupTQxCHXeCXM7svr1jlP6H8vwjAOU-A4rT-Pd8eTBA5M4kNaVM9Bfe6teiZ9Rb2MNAQaJQlcr4q9heVbZ8o4lneWvIYs3ok_OjAULwoMCA8rw8hvsao-ooHv5Svw2R0b3GTmZf2_ZS7KlF_cshftqIBMIXQxgaFNvD1pmyOPnjPf18WHSFCeixdvG6mYD0JticKir0Ga2jUFk4vjZcU1ppf0_CAaOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
جشن وایکینگی نروژی ها پس از شکست برزیل در جام جهانی 2026 به رهبری ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98448" target="_blank">📅 01:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibJHo1_LE-QvcAYMrRiDvO8xAO0fubygLMxegIbbOIlBmPMUgNKBl9bGMkvQbiA4Dmj1AYCBT4jiRAK39zwLiBMyFsbAvynsOSKRAPAamkD2OLMpUH5tmvsiP4qYojaSoMcukl7X3ll050taBRadDt6FpGZqXxUjBednPenguPWjHRJ7PBfl5Plixjf0C29IMNtF51_i95axS-Sn-TDFYbMmBQqzXZNNQ0tNAow8b_oL4Y4M2WDjKm-Ra-09MFjWEg1RZnc-BhMvuJSfj7sfND1UAKQ1qKC5NwPEeDY5lbsH7vaBab4ihT7VVCJFkarg3sIowgjv5NPmg6cRexF7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98447" target="_blank">📅 01:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVsbEmBqMT1jb9H5j_sTMyQbVEjd1_YKDAd7ZgaDcZDU_b3WjknsK3kVmEuL-16uFc8rnC0_c4zjRKTWTIqs5ZmmTb5Fg1efKfmhfWP_2cfoTYo5u2ldJ7siy-XzGiiBa6AfcicJWRSI_J5lOWOxcbmAjsg4nT4g22rJPC3mALph4mH4_Sjb9NvBQ_IkjpBk_dxIdAKlLam7jYD_xdAUlkQ6Y9aCy1axFNSIKNRokkEVfTgbDNo8jozHV1QO19UHuIAkkjz5Q9jDgzxA9BO-kX9LndP15__g9Dw1uveAER8T11_60iTyDqLsDMhqqesbiBtDvKVKfGsOAMwaVD2slQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🇳🇴
تیم ملی نروژ برای دومین بار در تاریخ، برزیل را در جام جهانی شکست داد.
‏
✅
پیروزی 2-1 در سال 2026 میلادی
‏
✅
پیروزی 2-1 در سال 1998 میلادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98446" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAC30WErvyqToQ6e1soajVSp4PgsX_Mq0AO-yZAPI-F6uwxGhU4uYPkw0wLsuBK_yvfSupm2PRKwyf3sqabNGMZsD23ymVatwwt3HmLbhymgiQwqgs9K4F4kxkKA7MIzX21VDYCP-Coz5tv7UZoUBA8Oqj93J6cQq665d6Nw0DedOii1O3_wkR0Cx0HKJ2zLsEdGjdLH-53mVzlOnEft5TcE9fOZdI9EPJJ6nOfxyckY_kXYhfGtzphWZLWuzTOqgrB3z5NLYmg-b8l2vH6DwU0vznR1RenQdsnIdZKaebVzAd6O8t7WD_STsAakHpSVhq5qi4CPcieaFoiS0YqZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
یک‌قلب تقدیم به بهترین بازیکن برزیل در جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98445" target="_blank">📅 01:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98442">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIPsr_fdxugUb-UxN7Kt1hxpifqEMkoYsdDeiaXoozQ49yETkdAKXDc6sdwHeSBGZl9_T4ZzqgXJv3OJOEt_79tls9jrAXKE7h2zPx2vFN_FGuoyPiajHqajbjZNPWGz5VNYvfJAQ-wbSH12fcRDwBfCbzsPyisvIbxPItfHY3pC0Okp-pPZ4MiR_3oqRfUvr3_vnAhgy9GljTu3i1-UrRkIQN_btKtDq7A1dyzz4kk_8KFsywjGVx5PtVF_SHAOw78V5rsNc-TQASjMB8hTJIsAubIbWiGZ_ID7ya4gWIrA0Ymeu7rVKhg2GsaoC0y81gbfSW5HYQLEAzG3xSE9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDwFM_OD_M9diJAkDsZ--Du2Z6dpSrEIdFKhZCWFTuvOnUBVp5-M_My8VatRXWyENsyitL46B5KuFhpEuWuvAccAdrf26udN99_Rz5cJLRsR6cGMSr_4MCcjAtztMRCNa5sbNhMOAbMiVV6Wgy81nY5E0KpvaTOkTQ_ipkga3jSl-LlqM2im0_kCWE9ECex4slv8B51aOTJsq8Hp0zJgyMzJ5k1lFtWjJ64nFJpuFcAqftW-FkI9PMFgqoNn0xgAX0XLF9M0kouFndo_YI3ygNDI0UPlM_GQcez0sclFG8Vs56W7Kn822Hk-Ilbui7-bLGDNY00y104o4yCNJZaBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV1m03z7bt5tcx4W1h2gAiYFqga5pxs-FZEILWTfiEFKiJznlfZUpJIiQh9sOw_7pm9nTuhgfDDtP9jjw-Z0ir9YsxIFj8d2QzFj3ax2_N519qwDTO0WCLO3EpOMpON2TNAgSi034wlBEFsn3ZgqQkSIpNu-BcSVWAHr_cQy-z8wRmvaLlFkKlb2pP98sTKx_sFEZvPGyn7HFXfreCvSJ6l33u7hq51reE_JAuh0WBJcPEI1k3KRMIeE4tzARGQuVHNa8ofnZmJxa_HBqwZtqDLJeiyEzusTy9Ojbi1f0BmXP3T0I67_k17LvHPKpT83N2yXTdtQRr5BG-tyFfxWrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشکهای بی پایان نیمار پس از حذف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98442" target="_blank">📅 01:43 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
