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
<img src="https://cdn1.telesco.pe/file/VqqqbYgS4XIGz7C0D6gGx-nTEVrLOFHNjAcdKhD1LbUygHINnj8595RHNjzVln9jtawncxONXVq0FT4Ezp3XTjii8HcxKvFUwdVGC9p4h2yvz4Gzb-7sOstDH9JwVlVFAbhePG3p78FZgY-yYiWjr9TmX2rHcFIF9AlTZuRCny7jUEqA_7fgE5sc4EubgPuAtKZxzG9j1FrXcETSaHvrYKSDi1jJWbZ6buQ3FjX-TZxPHOILWMSkprnNw_AKvNnl8jAbHz86ZofPnVbCIMPDLUCmdcRU5NEoo_43Ghi61NoxbTKmGIMRkKqUR3AtIyRc_xolEuOtU0o8aYq_diFr4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NpcdjgVgNrqNLCSWFZVUBAZX5eqNAJ4RHoMAv6Vgic6e149-S6jpRL9kC810-eQz3rE0-nqh2lZy5bYesZVAOm0bGlhdiDxeDk8CQdofCWGjYeOictcry2FFueRuLRrEGDgiWTwXtD7EnGJqjIwkLO3pik8Tadm-8-Gg1P_hr-qvKbHp55lKVGNO_YYt2sP6SgkJQsP98CJ6jqZttZUf8vqVHHghHKaU_Jg77FYta-ixd9AYwi9bBEQFq1Z_rfnzgiu4SEuG8GGKaUq5pNi0q2gfNfHP9v5MBnJnKXdZbjrw1d0FWlcY2rMuEdxSWlgM1bCfgLqfgMGBx5Qbn2f0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l5KERwNeHIu-SeuoUJww2wGkP_bmnR_4xdy2K4301zaGJ-HbMAtyI29_3P1J8CnTRwqFRmYtjxSc-W1s5B1KpBgLuUJ85yzq28NviG-9BRfUYYdW_2suE6qKG9qH8vOLQ9jiVHmg9t0VijAq4-bVxEECngAaU77gzOqSmqA9TWu8a7wbAwfPw2saK5r_d78KB06vtlm4llwPykzpnD12AoFbGOY4RJfCMCHQPeE-L-YNZdufSJ_ImTFz2ls4CJeOcQXg5byUByKc-66pj8G-FtqDS4S9y-x2aDXFQsXpBqttZg6eVTQPY5RjipZmkqq1MCMhsavepHDNCoORVPAN7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBPVWZ4ZHV8EySLP5SEh3Fb3t8Ew1rGB-QzPCv8QYrYeJQw4oO1-MgyzKEGVEk1K3qF9hv0eBl6ed-srJFm0j9xZRmiCgf7OoMI03zHr02kG6byY6R0dZ1vKjl-1qOcPYHmnsaMpYo5c3Ks96vECHqhvdWqc-gj5Q2VK7ZTdPmCp9JdXkhityoxx_40hiZcR7Wb40nODe7e82AWMcUzgG5HrQBwAee509cZkegE5ipDxfbqaArmcQU44Ulr4StByAGfyHU3hs_zbM9WboVbH0soTp1KFpD78DSgBc9m-W1VredSq9FtYjg2ASl3Im8s317dWquETRvbMJxWatAqKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=cZygWc952R1O2b-ouyIBYf5m2RRpI8FuD6w86dfHj18zSp4WUzxNUNooWRINBBZQOJUpwseE1KymtkJ28a4gVbPhOGVCB-_XLZSuT8b4DhT4MQ_XdcjKhwK6WVaqZbZ6lA5UQnDUGUs3K1eHOGtvlxT-Zilad4hEndzvHOtnt1g4zBnHGdw3KeLah3P5OllzBVSFr8gVXrMOGVapCB1oAthOM5h9n_VmvJNVnxAgelckL3486--pZyPQ5oACyNIqy9O0FY_05rjC_9rH5DV60atnutLbgX5lCcYMi9eLr9w0jHqrLwti4jRKNQovDprUdwyTy9PRF3131oh7dF801g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=cZygWc952R1O2b-ouyIBYf5m2RRpI8FuD6w86dfHj18zSp4WUzxNUNooWRINBBZQOJUpwseE1KymtkJ28a4gVbPhOGVCB-_XLZSuT8b4DhT4MQ_XdcjKhwK6WVaqZbZ6lA5UQnDUGUs3K1eHOGtvlxT-Zilad4hEndzvHOtnt1g4zBnHGdw3KeLah3P5OllzBVSFr8gVXrMOGVapCB1oAthOM5h9n_VmvJNVnxAgelckL3486--pZyPQ5oACyNIqy9O0FY_05rjC_9rH5DV60atnutLbgX5lCcYMi9eLr9w0jHqrLwti4jRKNQovDprUdwyTy9PRF3131oh7dF801g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4hlvOef6jHrm2B1JDcFkp6QOxHOQrVY1_IiQ8TU6xGNzyd27dENWJ9ddHPwu7vapo9IrxKZdU39GWBCyZjTOLkVPhyHpLkDva4dUpT4Y-avU9_rZ_TBTeXHOlF5dKinqwPNSLOIOwvQ6uQ_vryv4yW0jptqwOFa4E38D_sxBlMOMqOdsVg68a431dT5BeKIP7FRxNLUXzD3ri2MuoW9EMFkMNg3QdTcJqnSL0ILkoCSVIW9XZQTX2DKxMcqrRiBBJFW84Ds-l72-RGschGTeU7ABrBongbMrxJ_HJIMMxFR4cdRxz4NjSUVNZkxyStax1vDpvVGz5mwXtRZN2LY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izga9fa7Zn8AedIR1td1qbybOJII2iR7eVw8ZvJ6g_hfxlA_-esRiqj2xir8-uiEKP2SNI0_xfbAOn1KyaCoXqEWj8sYB9Z2kyu5GwK1YJ9o66kX6b6LmV1B-pRMPPhyfIgQ1ccazfxdoB8mGLws4lisvz0oel6_2Gb_DoMmsKxL17tA4qYUj-36iIBi45HP1HBGHVLhclDa98e-mBGApKg7ArlHqdW7LY56d4qhC1dJg5h63ZD_PgqMylgPxxMFSIrQ6mmbVrhpOKrWHKp2BICQ9Doxf11X_tqwq3bj9RqU3-Kcpa2rJTDFIYV9WKnUo0YGRm4qyjzQS0nVfWZ9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KCZjihXs6s7ifTS26YvOe6afWva2e4qXust47LjmzA-QRHtCEXA0N-E9kzPt82DFNlRUAaAN7YszvSis0iveqI9G0nsX5_9fa8NSbXeaG8hG42EV1R1lk_CJODi7jFHRzwI10MByaVq2onV4EqAfn8ZrrsBkjaKKFyeNJAcOio0zoOPUEixvK_E2SN8oBq8t3o9h6xI2CUEDgSkK_VNlRINjs2Pq_jxdpYSYQUm6dEmLt0SeRCpuU9AEXftfsqHpa1DttvXePgHhCDsUw6kdr8Cx6GAVxlXrnfYWwJ7SkibVgOe5zm09vkkI-5YNN4QNDDl-1Ut3ycG02DyTU-2I9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EhjNMXFAdv1TOutLPR_24F9xxITtd3Eod5Hj1yB-Sjyx9bF2Ux2_-GsZOpicS7ockzWiPVtUYjI502ByHB4Uu94eQ-wqGhl68GSyVWdlqtMkAedtP4uAi_T6Vax_Fbtsmkzw5qkqrBQL-18to54bMtQdj8wmwkH2H6Y4-33L24UxOVhglcXz1Yq4WPVLWTfwMWs_WGQMq2I0hRn0X0HXeCc2oba9dm_1cgftSeCY-Mr4eCsc9LSQc62oprkg90Bgk9_ml-oPyn8J3uJDqeqevVx4r52MiugwstwV7Ut6N19L5Hm3BWsAFjyIZZ7Yv6VWJiIBGtN-x9fBzSFD-NTgwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxgMIIz7jcSkemTvRyWx5H52Hp6QbYpRGFNbbW9CRaSvB7R5sTqvC0l7RHQIrinvhBOrGJ-3EXYbRikI3j27t-SDXkwwfHMgHGNjMISYcGwMzTB-TAHkyTMMbp95IyuzQGnjB7eTPIvPwL3tD30Fbr1izie6EvppQRB4yYeas9XeBl6ewrJKnpToBfbjU4knt9rDhBTsbew6aUIqOavS5gagyaiSuHzPcS6-bjyl-rPpBABJJtoELX3aky0QhIG6YrFXi4VUgXL-oH8hOSQBVhmfit-oMOQdlhoj0zAo6tITnxO462h5yjoUqEW59j6EBxrbs-UDFBP5h4eoO5-4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سالواتوره سن‌فیلیپو، هکر ایتالیایی و خالق Redis، توی مقاله‌ی جدیدش توضیح میده که نبوغ واقعی لینوس توروالدز(خالق لینوکس) فقط توی کدنویسی اولیه کرنل لینوکس نبوده، بلکه بزرگ‌ترین تصمیمش این بوده که خیلی زود کد زدن مستقیم رو کنار گذاشت و روی رهبری، هماهنگی و تعیین اهداف پروژه تمرکز کرد. برخلاف خیلی از مینتینرها که خودشون رو درگیر پیاده‌سازی جزئیات می‌کنن، لینوس فهمید برای مدیریت پروژه‌ای به این بزرگی باید زمانش رو صرف رهبری کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4702" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پشت‌پرده بازار فروش غیررسمی توکن و کلیدهای API هوش مصنوعی
تحقیقات جدید نشون میده چطوری یه شبکه‌ی بزرگ (عمدتا توی چین) برای فروش توکن‌های LLM با تخفیف‌های سنگین شکل گرفته؛ این پروکسی‌ها از طریق سوءاستفاده از اکانت‌های Trial رایگان، ربات‌های پشتیبانی ناامن سایت‌ها و ترکیب کلیدهای API مختلف کار می‌کنن.
که برای به سرقت رفتن اطلاعات مهم استفاده میشن یا Train مدلهای AI چینی.
به زودی بیشتر تحقیق می‌کنم و بهتون میگم
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
اینم لینک مقاله‌اش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4701" target="_blank">📅 03:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خدا لعنت کنه این جاوااسکریپتو با این سینتکسش من ده تا زبان بلد بودم اومدم بکنمش یازده تا جاوا اسکریپت رو هم اضافه کنم بهشون، همشون رو یادم رفت الان فقط جاوااسکریپت بلدم
@Linuxor</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4699" target="_blank">📅 20:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">روی اوپن کد هنوز میتونید از nemotron3 انویدیا استفاده کنید</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4698" target="_blank">📅 19:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فعلا میریم nvidia(با اینکه delay زیاد داره) تا ببینم api رایگان امن چی پیدا می‌کنیم باز</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4697" target="_blank">📅 19:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مهم
راجب Mimo
😭</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4696" target="_blank">📅 19:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v3CmEuuY9zUuVk2N10q6WeugR_ZcvOqfU3LGnmtB5tsdFDgaYkFvigA3EWWsBA9Gpnm4hU_erFlL0ZbiGIpVLX8wpCcF9jvEnZntOsQbquchUb5h7xZD-O7EntRQK1ES1Hu6BJCXkowtWe0P5PeNbdnAXQoFiIkoT7kaD7nMRByD5s9eHr_GUcizDm5-5ErbsJJRCGLQ0zCode4QuE45njmYwR0MvAZlpYPtdrjVVrChTTNIX_J8iODI5awlpJgs4eQCCuOKnLPAcdIly1ws0fD-iR-4Ib-8gfW_WuhRGFxG1rHaL3DzRU5-Bzy-0JUatsshyesk_6MSHoUWG0nb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-QfCkgyDGuG9Li7WwsJzp5gHaYJUaHouJpBbEaVHtjLVDAl8J04m4kY2wI3SS7elr9xnNNrG-RVt8RlGJWM5s7Vt4lfVHt1KCHaEUATCQQQbpP-zXugLQ1gg9GFii5goslXCvZ2qRzAK_dJT_nibAurYgGehYCcR_9Jsnip2LlBG510l1sT7tqPKaDpCOkX7rjhD0H7dvdzgf7694jssIalFPpu0f-Jw9WZSrOhvlfCwJYipKy0_LipPMyrNfBQapECHnBTLwNHzmJj8mTznO5Bvdh9E4oRiNX14QJXJ2MK_B-Kn9sgcKX5WB55G_CFppM69v7QUrWlATE--thgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YscdTNPs7fmxCFTiEaYkiLCEz9eFEfc9m7LTm1fl_N6rVY7RSSxUyfq2mD9GWAJYcJPrKaN-xH38IbHCKiGKBzQk0uKTa5dkYIJKmsrd08Al6LkPpcPXLt0Ys4HeYSK6X9_U0xSeMj24vlxjpx3G4QY_MngGMkYnvJt9sMHqAyLlDaPNaJHSASfTEoEDqC4tZAAPlQCp4ewNcbjfBocW4soflLDD0qtEs4rNZHt_G88cQd270j4JOnj3OaIR64BBrdfphpuUoZidR1I907RyPhv8ml8xF50QEejtGieLzc-a5WWCm9l01EcyCIkBJUrRORbWho2gY3Rfdle3v4qjHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای این از proxy relay کلودفلر که توی ویدئوهای قبلی یاد داده بودم هم استفاده کنید مشکل برطرف میشه دوستان</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4693" target="_blank">📅 18:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4692" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4689" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LVWNs_dXqezgNXDPOLd9PqjOs1kgngfuhnOmvs35dE_yz_uZMIgwmdWG6bp1kAAXQZ7Iw7Z5N0BiBMkYUQAXNVTGNUcW2Vj9GkPmhvjpecENPHM6Mo1c6FswFKubGcigJOtsEfgI2r5aw2nLvlmNN9jkzCKAzfNNm8rsATdUOZKM4Pt0l1rKAhlxVMCLCTb3zOOi3wInfrqdgbZRmWmkDZMoNu3Az8hPjNolojYQjApx69pXehYsfouDaomd1roNGRfAh369bRIIqosY3tDN63Rk0OUiuEQJd3By3S6NjHuuXkClhwJqozSa_gbZtsEx_QW5pbCVvpGko4VN13beYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش
طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4687" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خوشحالم که این ویدئو برای خیلیا کاربردی بودش
🔥
روی یه سری آموزش دیگه هم دارم کار میکنم واستون</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4686" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUIM3abwV_4XlyUtEgFeQMfYinGuP5XiIZkS9F0MXZryexfqRP7MPuV-z5DESnuon95SX-87cy4-TVlig2EdVHWDFYXvJsNzGTahn3Xl20RGloZQtCZgaNwrqsfKKTJxNq9ND74Pai5Cr0wGDlYbzG1Ch9A5-IyTV_mu3UzjPQE_w5CzD1u2UuYN61FJpdmQ7TrKGH0-tlD9ttXxS7LdxhHHKWv-L6nfMjazTXksrS-WgIBTkKGQAuf6fI1c89HERWgqtaLs4prRxBz2UasiEfvIsAL9ClMILK5pr1vB0lkctVvaRTLQeygrCof5dZF4fBSbOucQ4PLyrVUIijEW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اگر به ارور workspace has been restricted خوردین، باید یه ایمیل جدید بسازین، با ایمیلتون اول اکانت گیتهاب بسازید، و با اون اکانت گیتهاب توی railway ثبت نام کنید تا بهتون گیر نده و فکر نکنه اسپم هستید. خودم الان یه بار با continue with email ساختم دقیقا به همین ارور خوردم بلافاصله بعد از ساخت 9router، ولی درجا یه atomicmail تازه ساختم و باهاش یه اکانت گیتهاب ساختم و باهاش لاگین کردم، سریع ساخت 9router رو و گیر نداد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4685" target="_blank">📅 05:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عبارت VPS هم زیاد درست نیست. صرفا جهت شیوا بودن کاری که قراره انجام بدیم بیان شده
👍</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4684" target="_blank">📅 04:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4683" target="_blank">📅 04:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrOlWGa4sjMrHL5z0CQgl4IxqYkyH-oKj7xhIyoMmTju6HBn7i3_egKPLsMR_E5kUnfORKRP_Rk9Psq0tvob4-WzYiCLfdNG0r4Mv_OiZVgyg8l6CxHTu1gNtNsvh7Bpsnad9j-lMamTBf83iZagxcheIpQ6r5OeOdvpruwZkqRXJxibRHh02960HfM-rFjjT-Jx7tU6eElw4RGPPHznfeJG5KdahP-q3PAQwQRbuJDshw3DDXYBZlvSzsJk7Kgy5UYUQIprPpftde7j_KsdeppYvI9gA66bd4txa-x2jrExPne00NNQjGFNyBgH_2xvDPLGdta0BYZM-a6jzTD64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4682" target="_blank">📅 04:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فکر کنم من تنها کسی باشم که از اینکه مردم از کانالش لفت میدن خوشحال باشه
😂
به خدا حس میکنم هرکسی لفت میده، جمع اینجا خلوص بیشتری پیدا میکنه و اصلا کیف میکنم
شبیه عصاره‌گیریه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4681" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن و از تلگرام باهاش چت کنن 24/7 خیلی باحال میشه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4680" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9pR04iTL4tKgrMHxshrshF5zpvvHV6kp_ayv0uf0zScsC0uf1Z3lMAmyDGMO6x6dQ1p0x5xDetyGnYGRTw9zq70oIWcXSRHu5wA3ORbmm9FiYnhg40BgYLE567mVPeFSodLzHaFVSaHyerkXx4qVsFK1dGeF4zQQvDpHFDXelPT4wOk_sOeXT-01P8PkovRO1nDtIWRiseFzUiWyYy5HZxhIocmKqcTOOdaXqCCmPhZY8AZh9MQ3NvpnVskcExVIzW3Wkwdz4mUpOlP_dPd-QhLjNCzmv4vwGfx-ceg-RCkC_4WLsg3G1PQFaKOmiYu5ad8pdbXQ9_lSRedHBYHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم
که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن
و از تلگرام باهاش چت کنن 24/7
خیلی باحال میشه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4679" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برو برو
🥰
موفق باشی بعدا میتونی معرفیش کنی خودت و بگی چطوری توی تحقیقاتت کمکت کرد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4678" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خجالت کشیدم، میرم پروژه رو راه میندازم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4677" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تینا شاگرد نمونه‌ی منه و به ترسش غلبه کرد و هرمس رو راه انداخت
❤️
پرسید، تلاش کرد، به ارور خورد، و آخر سر تونست با اینکه تجربه‌ی چندانی از کار با کامپیوتر هم نداشت</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4676" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">باعث خوشحالی منه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4675" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من به شما افتخار میکنم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4674" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">در مورد این، یه وقتایی به نظرم بهتره آدم کمی پروژه‌های پیشرفته‌تر ببینه که هم بدونه دانشش در چه حدیه، هم یه دیوار جلوی خودش ببینه. نه برای اینکه بترسه، بلکه برای اینکه بدونه دیواری هست که میتونه ازش بالا بره! و انگیزه‌اش بشه. من خیلی از مطالبی که میفرستم اینجا…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4673" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4672" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم. اما خب، شاید برای کسی مثل من که کلا هیچی از دنیای کدزنی و چیزهایی که آموزش میدی نمیدونم کمی ترسناک باشه این موضوع  این‌ روشی که بهش اشاره کردی رو توی کلاس هم پیش گرفتی و اونجا به من هم حس اینو داد که خب وقتی متین نمیگه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4671" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خود هرمس و راه‌اندازیش مثلا شاید یه دیوار بوده برای خیلی‌ها.
من و بقیه‌ی بچه‌ها توی توییتر و تلگرام و اینور اونور، طبیعتا تجربه‌ی کار با کامپیوترمون بیشتر بود، زودتر راه انداختیم.
انقدر نشستیم بالای دیوار و از منظره تعریف کردیم، که چندین نفر دیگه هم ترغیب شدن و تلاش کردن بیان و بهش غلبه کردن.
چون واقعا کامپیوتر، و همچین مفاهیمی که شاید برای یه سری از دوستان ساده به نظر برسه، برای عده‌ی زیادی اولش ترسناکه. و باعث میشه فکر کنن خب، اونا که تونستن از پسش بر بیان باهوشن یا هر چیزی، و من نمیتونم.
که اصلا درست نیست.
کامپیوتر و این مطالبی که اینجا قرار میگیره
همه‌اش مهارته.
و هر کسی با تلاش و پشتکار، بدون استعداد، میتونه یه مهارت رو یاد بگیره.
شاید یکی زودتر یاد بگیره، سریعتر متوجه بشه، ولی در نهایت همه با تلاش می‌تونن بهش برسن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4670" target="_blank">📅 00:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اما تفاوتی که هست اینه که تمرین‌هایی که توی کلاس میدی در راستای چیزیه که بهم قدم به قدم یاد دادی اما مثلا اون پستی که برام فرستادی برام آشنا نبود اصلا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4669" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4668" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به نظرم این شکلی یادگیری خیلی مؤثرتره
😂
موافق نیستی؟ آدم اگه 5 بار هم قدم به قدم جلو بره با ویدئو یا آموزش یه نفر دیگه، خودش اگه یه جا گیر کنه ممکنه نتونه انجام بده ولی اگر خودش درگیر بشه، واقعا تأثیری که داره صدهزار برابره.  بچه‌هایی که تازه اومدن توی کار،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4667" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من تاحالا وارد گیتهاب نشدم، پروژه گیتهاب دادی بهم گفتی برو برای خودت درستش کن
😭
😂</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4666" target="_blank">📅 00:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">:)) کاملا درسته بانو
❤️</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4665" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.  دیروز یه پست برام فرستاد از هرمس،…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4664" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده
اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.
دیروز یه پست برام فرستاد از هرمس، بهش گفتم من هیچی نمیفهمم:>>
گفت جلسه قبل بهت یاد دادم چطور چیزی که بلد نیستی رو با استفاده از AI ساده‌سازی کنی برای خودت..</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4663" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک کاری دارم میکنم مربوط به هرمس و مدل رایگان و ران کردن هرمس روی گوشی بدون هزینه و 24/7
نتیجه خوب بود بهتون میگم
😁</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4662" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیش از ۹۰ هواپیمای سوخت رسان آمریکایی در اسرائیل حضور دارند و هواپیماهای ترابری به صورت گسترده و بی‌وقفه درحال پرواز به سوی اسرائیل هستند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4661" target="_blank">📅 22:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">یکی از دوستان برای OpenWrt یک پنل مدیریت نوشته.
این پروژه یک اسکریپت نصب برای Aether روی روترهای OpenWrt است که امکان مدیریت از طریق LuCI و CLI را فراهم میکنه
https://github.com/moein8668-git/aether-openwrt-client
خودم تستش نکردم
اگر مشکلی یا باگی مشاهده کردید لطفا به توسعه‌دهنده اصلی گزارش بدید. (Issue)
توجه: این پروژه فقط برای روترهای OpenWrt طراحی شده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4660" target="_blank">📅 22:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه بک‌اند کار می‌کنید و Go می‌زنید، پروژه‌ی Gsxui احتمالا براتون جذاب باشه. این پروژه کامپوننت‌های فرانت‌اند استایل Shadcn رو مخصوص اکوسیستم Go زده که اگه با ابزارهایی مثل HTMX ترکیبش کنید، می‌تونید خیلی سریع وب‌اپلیکیشن‌های تمیز و مدرن بسازید بدون اینکه درگیر فریم‌ورک‌های سنگین جاوااسکریپتی بشید:
https://ui.gsxhq.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4659" target="_blank">📅 19:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4658" target="_blank">📅 16:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
برای اینکه مطمئن بشی VPN درست کار(نشتی ip نداره) می‌کنه، می‌تونی از سایت BrowserLeaks استفاده کنید. این سایت IP فعلی، موقعیت تقریبی، اطلاعات شبکه و همچنین تست DNS Leak و WebRTC Leak رو نشون میده تا مطمئن بشی
#اطلاعات
واقعی اینترنتت لو نمیره. اگر بعد از اتصال به VPN، آی‌پی و DNS نمایش‌داده‌شده مربوط به سرور VPN باشه و نه اینترنت خودت، یعنی اتصال به‌درستی برقرار شده و نشتی وجود نداره.
این سایت ها
#امنیت
سرور و نشت در اپ ها رو نشون میده:
https://browserleaks.com/ip
https://myip.theazizi.ir/
@xsfilterrnet
👑
@xszapass
🤩</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4657" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تا اکانت گیتهاب سازنده‌ی Aethery اندروید درست میشه، به هیچ وجه از پروتکل MASQUE روی اپ اندروید استفاده نکنید.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4656" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZklRY5MHbm3h8R87h3OweNtOVqMT3oYG4eDyh3ahQRs1KFRV_SygfOOqJy4WwwTZNmeDc2zs3AbxaYwJsPwUBJtjfyHls7PUc3K07VrIaSkB7jkOyhA39C-EsgfcQRF9haKMIpEJF7AgX0w4mQk3AEKBBCU-EwtCc5SeyhVA_5vU2GtPQ37o1rgSi9MCsfIEHL7C3sEVNLj2teZ98ooB5xLwBoseZ1ddX_QuA0BWzBhFRMjcd7wbwZPKNLI_WaNcKI7Tn_4W3VNw24-k4R7zWsJAamB7EHLpJOGiKwUILLlYr-LQx20HSgmMYzqwl79E-wXv5Xw8-lo9MHXC4FcrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4655" target="_blank">📅 05:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_SeqJz7Dcg2AYqp4NDMZq9rjLpxrqY1eFrnyQ5cNNDzFn-w4yRXsUy8C_e0N4g6xkoRfFSVvYxrHDHY6PFmLiULqqJUvpqwe-bLo7roUg5sgIHWLwYBzfUIzHgyW4mBtJosQNIeCUzcTcYZn9t5jyg6IWCUxrrnwaZq2_N7vAPoKpOUcw6gujm0H1NL-A00siPldSbzShXHQwWSxXrWxB-JtOAqwV2glpl9hls8djOrwf_FxR38KYKr-k2q4RhyYxnLboYI5nE1b51vgPznhMN8yQvaCCVWknsqbrw0Lf3nYg4kdsrOx91-uv01a44cIptl6AzT9MJFqp64r27qNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با تشکر از علیرضای عزیز بابت تیزبینیش و زحمتای @CluvexStudio  این مشکل خطرناک که شانس MITM داشت حل شدش. حتما aether رو به نسخه‌ی 1.4.0 به روزرسانی کنید. آپدیت GUI هم به زودی منتشر میشه https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4654" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آپدیت جدید Aether v1.4.0  https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0  توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :  فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4653" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.4.0
https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0
توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :
فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد (verify کاملا خاموش بود)
یعنی از نظر تئوری یه نفر که بین شما و کلودفلر قرار بگیره میتونست یه سرتیفیکیت جعلی بده و ترافیک رو ببینه الان اضافه کردم که سرتیفیکیت edge کلودفلر با هش‌ های واقعی که pin شدن چک بشه هم روی HTTP/3 هم HTTP/2 این رو یکی از کاربرا (Matin Senpai) گزارش داد و خودش هم pull request فیکسش رو فرستاد بررسیش کردم درست بود، مرج کردم :))
فیکس مهم دیگه روی WireGuard و گول (WARP-in-WARP): گاهی اوقات "Connected" میزد ولی داده رد نمیشد. الان هر دو مدام چک میکنن که واقعا داده از طرف مقابل میاد یا نه.
اگه یه مدت هیچی نیومد خودش میفهمه تونل مرده و خودش دوباره وصل میشه. گول هم قبلا اگه تونل بیرونی قطع میشد کل برنامه میبست. الان اونم دیگه ریکانکت میزنه.
یه لیک هم فیکس شد: هر بار reconnect میشد (روی مسک یا وارپ) تسک‌ های پس‌زمینه‌ قبلی درست بسته نمیشدن. که روی نشست‌ های طولانی با قطعی زیاد رم رو الکی بالا میبرد. الان هر reconnect درست پاکسازی میشه. :))
--verbose
قبلا همه‌چی رو یهو میریخت بیرون که خوندنش سخت بود برای بعضیا که الان
--log-level
اضافه شده با ۵ سطح:
error warn info debug trace
دیگه راحتین :))
حالتِ info آرومه و عادیه
debug
جزئیات تونل رو نشون میده
trace
همه چی رو حتی تک‌تک پکت‌‌هارو
و...
Aether
الان موقع اجرا رم و تعداد هسته سیستم رو خودش میسنجه و اسکن و بافر ها رو خودش تنظیم میکنه که روی روتر یا برد ضعیف زیاد مصرف نکنه. با
--perf low/medium/high
هم میشه دستی مشخص کرد.
پشتیبانی از OpenWrt کامل‌ تر شد: علاوه بر armv7
الان بیلد استاتیک برای x86_64 و aarch64 هم هست
aether-linux-x86_64-musl.tar.gz
aether-linux-aarch64-musl.tar.gz
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4652" target="_blank">📅 04:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدل Opus 5 توی یه سری بنچمارک‌ها از Fable 5 هم قدرتمندتر بوده توی کدنویسی
با نصف هزینه
ای کاش زودتر بیاد توی کلاد کد تست کنیم. فعلا توی اپ اومده</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4651" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=gqkxNQihAOYMzm8DALPr7e-PhSsg1JbgH-TPmc0COI9FEGCpFoCcIc8QgANJF_2hT0BMS8dJgxuPkGu0O9KgLODF7ptConS9gu2LqswGXviTIub95Jw4uBDFWtHQ1o93Pp31KfvQOJS9wDAalFrqGu9NoRb8UfI_vAhNqpRBTpj0AINvuQRmN5tBo6UCVSUTOUNPkK0Ksz_z0pnEkK3JHIzdCm2Ay5_qxhlIucCKq72qKedaTppta2vSDe8fGHEYenUcy0yedh4nrVcAMmcW2wR0i3fAtti_vATXyElTQe7kDElvmgZ3rayOtk0nCvw6nLsbPAyNeQSvIrGhqAg8eMANN6hWfI9xICl1w8nGgCaBG2Mky-PP3Nfh3oZf0T_W2kNGGSQDFf1aWB7IwZGvrYsQyrvdNJEwLycA8fYcjUv4hPIrsr5A6WATd4HeHV368MDElwsfkqvpiPFzb10CN_jeGP2ZoevvuUqVcf7Fl-QqfityC4aGuC_XuFvqySPYDC9yAyhKNBg77A0Y6PQZA9pCn8idKyosN7eS9gS0ufHuAQtPcQYSyv4qpR52IBVwQJFGE8nNGRfN2xv9U8y8CAtjPcY2hI72a-FJwe4DguS1qzcEpOGqebqml531511kjhA_M8Z72SJfq2vErBNK1J19W2eqlZZ7buWSwjQp6Fo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=gqkxNQihAOYMzm8DALPr7e-PhSsg1JbgH-TPmc0COI9FEGCpFoCcIc8QgANJF_2hT0BMS8dJgxuPkGu0O9KgLODF7ptConS9gu2LqswGXviTIub95Jw4uBDFWtHQ1o93Pp31KfvQOJS9wDAalFrqGu9NoRb8UfI_vAhNqpRBTpj0AINvuQRmN5tBo6UCVSUTOUNPkK0Ksz_z0pnEkK3JHIzdCm2Ay5_qxhlIucCKq72qKedaTppta2vSDe8fGHEYenUcy0yedh4nrVcAMmcW2wR0i3fAtti_vATXyElTQe7kDElvmgZ3rayOtk0nCvw6nLsbPAyNeQSvIrGhqAg8eMANN6hWfI9xICl1w8nGgCaBG2Mky-PP3Nfh3oZf0T_W2kNGGSQDFf1aWB7IwZGvrYsQyrvdNJEwLycA8fYcjUv4hPIrsr5A6WATd4HeHV368MDElwsfkqvpiPFzb10CN_jeGP2ZoevvuUqVcf7Fl-QqfityC4aGuC_XuFvqySPYDC9yAyhKNBg77A0Y6PQZA9pCn8idKyosN7eS9gS0ufHuAQtPcQYSyv4qpR52IBVwQJFGE8nNGRfN2xv9U8y8CAtjPcY2hI72a-FJwe4DguS1qzcEpOGqebqml531511kjhA_M8Z72SJfq2vErBNK1J19W2eqlZZ7buWSwjQp6Fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از کاربرا اومده توی توییتر یه مقایسه‌ی خفن بین مدل‌های Claude Opus 5.0 و Fable 5 Max برای ساخت کدهای فضای 3D (توی وب) انجام داده.
نتیجه این شده که تکسچرها، نورپردازی‌ها و جزئیاتی که Opus 5.0 تونسته خلق کنه، اونقدر باحاله که هیچکس باورش نمی‌شه همه‌ش فقط با کد زدن ( و بدون نرم‌افزار گرافیکی) درست شده باشه.
البته مدل Fable 5 هم این فضا رو با یه بار تلاش (One-shotted) در آورد، ولی خروجیش جای کار و بهبودی داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4650" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگر نمیدونید معماری پردازنده‌تون چیه، این نسخه رو نصب کنید
Universal</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4647" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4642">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4642" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4641">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTPLHGmM0Vy__0vbawFaXkXN4VxFbacnzIRfs8d4LKbKfUu8_XNZIpqLhdKFcuDGTKEVcZxaf4FLd_UAI67obLdEFMWa-oeWduzmzliQAWape86k2Ex4Hf6oGE8IolB5PW9UNhQwhr_wQtFtg4801hDDGKUIbCoUMDAmFLBekMiYeP24_8CIC4mwZop4-2ZK1OGLSe96AHjnb49gX906gMq4Ea1YbjGdWYwz97eQEtKZqvgBNHmPfMONe30BVHgOT7h7cl92bSWX38jscCP4n6s9-yBUNb4b_8cu6HYxRThcAIxdAENAaGtZk2XR2q418kC6-5KBbsBb_6tKJh3esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4641" target="_blank">📅 14:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4640" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SkRMnbsQXotPp7LOx60Ta2sXGFCnNRREZpbf1dzIXfbc3J2TB18kBSowMai75ujVzr4TDR98Io6e8GpWA_09TtAwaUt8R_nPWzY9AY019fXMzHXOrcQI4uGGFNrbWV8WfoWh71pIp-OtwCqOZ4cBfP-U9LNGSZoF1x2XLI-f2H0S3gg0qfMXQ_SRXyYEaQ_U5uEnniOWaY9Hz3OxblR5NWaMbMYH8Ddvz2fXNke_t6Y_xM_-022a46ApimgZUASMFGcmeEcokqbK_nTu38VYLtwesNkolvVNg3EFxRMBW2JBr2NQsmA6gkP47730a_3_E5dsT-gMRVYu6diwAew2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارتاپ Screenpipe ابزاری ساخته که تمام تصویر و صدای سیستم رو به صورت لوکال ضبط می‌کنه. این ابزار به Agentهای هوش مصنوعی یه «حافظه قابل جستجو» میده تا بدونن چی دیدین و چی شنیدین، که برای اتوماتیک کردن کارای تکراری و ساخت SOP خیلی کاربردیه.
میشه گفت رقیب اوپن سورس کلاد توی این مورد
https://github.com/screenpipe/screenpipe
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4639" target="_blank">📅 01:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انگار دارن یه چیزی رو روی فایروال تست میکنن</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4638" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یهو خیل عظیمی از آیپی تمیزهای range 104 کلودفلر واسم از کار افتاد
ایشالا که خیره</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4637" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmmLLAU1H5zTfVqSjCZ8N5VAi29ZJagII98StiQ9_kCANYQ0n-2kicvuN-O3mT6gXsTQNXc2mWuLce_7cQ8cqVvc8Xj45awTwrDXNxSf4S8WI0f5GKqIpLXJucKYxLyK6V4S9DhJgHZE9Ltwukh3c0ikSIKnE9KWbfzMDPGYHR2lKrOIK0xkhsvxQODH0mcNCHadbbQxgrcvn6xjQCgD9pnuEeuX_w9qnmTy6uAhrwOCmXLBgKFbDQKOUj7UL2SgmZ7YfEyE1gDXQWuOA_KE3vm3ILHPLfMndePJ8O4OxWfLt_LV5zoTFSeTHAaxxS4fM9CIFt8-V_Jpitl3Q7nk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4636" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAnymipATiOuJkqG0Ljoc4AC_VdJhP_eW-6sNrd0TwwHq3jKjEkGPS_95tzQDZrOHG1Fvgoz72ilP8XpCy5_JH_9ob31Tj5Kceq8Ss-V7Ys-mFkiLc6qTrvI7I5e_M25qUhNiTFsV7VO4sKeUIDkiIaBW1FIbtYCMR90_bOYLtgs6V1sLkmxjoSyUfHaxTqXC1XZacVrSgjMIt093uvfKKmD1HPYewElvbChgMZGmMbV7i0XaZhAu9Rm26ou2ID8s07kt2Qgfw_T-SPzTPtnliz52VDrrTaG8oOF_bUJXb5L0IrqK1Jlw5FLZpRN435cPOilsUOMb4Vb2hO0M9tQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام
😭
اکانت Nous Research سازنده‌ی هرمس ریپلای زد روی توییتم
ولی واقعا قدرت این ترکیب hermes+9router+opencode+mimo هنوز باورم نمیشه که از پس این تسک پیچیده بر اومد</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4635" target="_blank">📅 04:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بچه‌ها من اگه کمتر هستم این روزا، چون دارم روی یه سری ویدئوی کاربردی کار میکنم که اگر اینترنت قطع شد به دردتون بخوره. و یه سری مهارت که تا اینترنت قطع نشده بهتره یاد بگیرید که بعدا اگر لازم شد آموزشی بدیم، بتونید سر راست برید سراغش</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4634" target="_blank">📅 02:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4633" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4632" target="_blank">📅 19:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دقیقا. درخواست نوشتن راجب ریتالین هم داریم چون متاسفانه خیلیا به خطراتش آگاه نیستن</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4631" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">متاسفانه من مثال‌های واقعی زیادی از مصرف خودسرانه خیلی از دارو ها دارم میبینم و متوجهم که ما همیشه دنبال یه راهی هستیم که زودتر جواب بده، اما همین راه‌ها هم بدون آگاهی ممکنه شرایط رو بدتر کنه
❤️</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4630" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4629" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4628" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdQhPF6Wxz8phYBRqYFqwVPPsPbLRXi3uzeHSMU1Z-WeNODfcGaqqEW53o4m85nbGj0yOe1MgFVCXYSbL6NiHUavd2laL6XCEdJWVFdhw58HvEcJXgxiKkvLWj1sdA3x1iloicc5mIJ2TnSnF-8S9VRITn8yIhBHITjrrfyZIvkcNKAO6BYk3d6UXNbR0kiMg30w8YhGvSG5XKyaWHVDr_cRU00_sKybjfJr1PfQ-QXvXDmySzYCmzTqpbtGFaoxqgWl_DeuxE_3B4l9yWhvkPWH7b3n86vuGZsO6yNjoGdZNNWd3NCbo3UKTSpBUR4_9G0B5JLub2u-G3JKa2H-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.
ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد ایمن محسوب می‌شه، اما درباره استفاده طولانی‌مدت هنوز اطلاعات کافی نداریم. بعضی مطالعات، مصرف طولانی‌مدت اون رو با افزایش برخی مشکلات سلامتی مرتبط دونستن، هرچند هنوز رابطه علت و معلولی ثابت نشده.
از طرفی، عوارضی مثل خواب‌آلودگی روزانه، سردرد و سرگیجه هم ممکنه در بعضی افراد دیده بشه.
ملاتونین
دارویی هست که به‌صورت آزاد می‌تونید از داروخانه‌ها تهیه کنید؛ پس تحقیق درباره نحوه مصرف و حتی مشورت با یک متخصص قبل از استفاده از اون، اهمیت زیادی داره. معمولاً پزشک با توجه به شرایط فرد، پاسخ بدن به درمان و علت بی‌خوابی، دوز و مدت مصرف رو تعیین می‌کنه. اما اگر قصد مشورت با پزشک رو ندارید، بهتره از مصرف خودسرانه و طولانی‌مدت، به‌خصوص بیشتر از یک ماه، خودداری کنید.
جدای از همه این‌ها، بسیاری از متخصصان خواب معتقدند ملاتونین نباید اولین راه مقابله با بی‌خوابی باشه. تا زمانی که سبک زندگی، بهداشت خواب و عادت‌های روزمره اصلاح نشن، نباید انتظار داشت هیچ دارویی به‌تنهایی مشکل بی‌خوابی رو برطرف کنه.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4627" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ai6MLcpZEGts3Nau0fLytifSrHoER1mPniXN51Os3ZIMTNELaD6YDN_YTZufqaLgQdFmCeMRtmPWzAuPEedNbzkInSWb8DFIrZNr99JeXNUtrHUC0FVmFvDim_D4nox1n6BznAte-HUTugdiMpZ1erwc-UJ3iB7h0Ab9BVH_c5uyPFRqLOm6YHdpX68CHjAtRqGc_le4lS0RUxpTCEsZZOo6jqjRKSKujCOySietppEQp6GIsSpKd5eYQFE5IG-SDazv5-ugq5ae-s1amMdTBTe1BkraOUwjfqnlgjvBQbgzEAIfDC781OdMNxcn21fKn9v7A5E992FDl2uqle3yQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فقط داره گند میزنه
الان نفهمیدم واقعا چرا نیازی به 3.6 flash بود
😑</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4626" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بچه‌های Fireworks AI یه بررسی تخصصی منتشر کردن که نشون می‌ده مدل Kimi K3 نه تنها با Fable در حال رقابته، بلکه ترکیبشون به سطح SoTA (بهترین عملکرد فعلی) تو خیلی از بنچمارک‌ها رسیده و می‌تونه انتخاب خیلی جذابی برای برنامه‌نویس ها باشه.
البته برنامه‌نویس‌های پولدار متاسفانه
😞
https://fireworks.ai/blog/kimik3-fable</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4625" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4624" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4623" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4622" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4621" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4616" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4615" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4607">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4607" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4606">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKWoBRtwVx6qVTUfJJnNxarwNBfrarZ4rpAsGsuUiUuTxp4fWszpMsiGBtfcJCH4eESp6ML1rOz4Fm-pOVq9L6E5c8AC40OEhr6AF2sdO45i1A-8hrDfhPX_cQ4WtqO-CIMB8Q6qo39cBILCrcgKlU5c87Fp9sEYbN5xu_YkP0AaLtOcVYee0UZtrSvDw4UI6ISWg3DiMJkMTkjc3v3uTUEm7xV_CSWVI3-6O1nkY3yxHWeZyGfJwbxZ_JLhNibNMj0kTEYEEB6x5XCutE8kLh8E2smcmru9Ig9nTJKLCf59s_9eYHWpcy5RoiBV5q3-GoHJU3555OPHnpwWphARPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4606" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4605">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه مقاله توی
exe.dev
خوندم، راجب این بود که اوایل سال ۲۰۲۵ خیلی‌ها می‌گفتن هوش مصنوعی مثل یه «کامپایلر» جدید عمل می‌کنه؛ یعنی همون‌طور که کامپایلر زبان سطح پایین (مثل C++) رو به زبان ماشین تبدیل می‌کنه، هوش مصنوعی هم «زبان طبیعی» (مثلا فارسی) رو به «کد» تبدیل می‌کنه.
اما الان جواب فرق کرده:
نه، کلاد کامپایلر نیست؛ خیلی از اون بهتره!
چرا؟ فرقش چیه؟
توی دنیای واقعی، نرم‌افزار لایه‌لایه ساخته می‌شه.
مدیرعامل استراتژی می‌ده
👈
مدیر محصول فیچر تعریف می‌کنه
👈
آرشیتکت معماری می‌چینه
👈
برنامه‌نویس کد می‌زنه
👈
و در نهایت کامپایلر کد رو باینری می‌کنه.
هرکدوم از این لایه‌ها دارن جزئیات رو مشخص‌تر می‌کنن و کلی
تصمیم‌گیری ا
نجام می‌دن. مشکل اینجاست که ارتباط بین این لایه‌ها پر از اصطکاک، و جلسات خسته‌کننده‌ست.
کار اصلی کلاد اینجاست: هوش مصنوعی می‌تونه
به‌صورت عمودی توی تمام این لایه‌ها حرکت کنه
. کلاد می‌تونه همزمان باهاتون درباره استراتژی محصول بحث کنه، معماری بچینه، کد بنویسه و بهینه‌سازی ماشین رو انجام بده؛ بدون اینکه نیاز باشه واسه هماهنگی اینا جلسه بذارید یا از کسی اجازه بگیرید.
یه مثال واقعی
:
نویسنده‌ی مقاله می‌گه برای سیستمشون نیاز به یه سرور DNS توزیع‌شده و سریع داشتن. به جای اینکه خودشون بشینن کد بزنن، اومدن چند تا ایجنت هوش مصنوعیِ موازی (کلاد و کدکس) بالا آوردن تا کل سیستم رو براشون بسازن.
نکته‌ی جالب ماجرا اینجا بود:
وقتی خروجیِ ایجنت‌های مختلف رو با هم مقایسه کردن، دیدن ایجنت‌ها کلی از مشکلات لبه (Edge cases - مثل وقتی که دیتابیس Rollback می‌شه) رو
خودشون متوجه شدن و بدون اینکه از برنامه‌نویس بپرسن، براش راه‌حل و منطقِ کدنویسی طراحی کردن
.
هرچند اگر نظر منِ متین رو بخواید، ai همچنان نیاز به یک متخصص خوب داره که بتونه دیتاش رو Validate کنه، پس به یادگیری ادامه بدید دوستان خوب من
🔥
🔗
منبع:
https://blog.exe.dev/claude-is-not-a-compiler
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4605" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4600">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4600" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4599">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4NGTYSbb1lX8hG94Nsk93pz13jTWhrBCghxlwEx6mIzjmj4w4GdC7sPEfyzboejdDjdYrKDwAE1pwB6zkc0JWXJWDlUKVrggVWsl44x4hAbAtlj-woB4sF1zP3v2WDINlKKd0S7zzHCAJ87DqFof84YP6FS8DC-uOhriiar5M6vK5JEBolVJIBIJ73ja9wtB4Huac3RhJpxccSziiXS3YnPHBsEPnwapJD34JPRIx7qoX2fqxJTwSMnpV16oUGF4-CtVhBczPsItuFD0EYfVfY2litq-VOyf4Mruovd_Nm1iyb_Ll3bY8D2o2Pcafvwo3VjH3lNgUavHO_Gya3jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4599" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4598">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده! فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن. در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4598" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4597">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4a1uE33xOB5G3y4XpeJEYrG44d9WCHWUSwrD4QRvz1j5C1r_ia_GqisH5ci83ZVMPQMtqcNi0UgWNVpDwgkYiafaZyFzmJHGATBCrHwCSJ7LvQABQ3N9vrOOGf0ET6NddnD_UHq9Ah_uUHuRtbB43DjNthIGhgI0BEEx0iMOPhwu2vr8-GA40onn_n7qrtChPl3554fgD1qlceW44IuUCg46UbCfITnm80PxQoRQnUicGM2m8Sw0QUTvB-2h5LhDW31T0tfWGB7bw2pBIDiUZVZiuGNvQMtADTz-jpROwLsmc-cxO_u3ylfXVFiefaa0sIL8bOsw-PAYEAepCjFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4597" target="_blank">📅 15:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4596">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQbQk-LjxbrRGXZ-cQMWzPL-1p4pth6OniX_zrGEEQkZmfzep3_thPt5zHYl1uSnxKCppNarFNAzSQlMUtYU5o6V42jnNNxBvFq1ogOhxGLyQFaYPDA7rGg5GusTKJqFpSSS5SKRwIudtza9SnL19JGineCpS4IQZoYBt6BHUJp4DEZ6pQ7KERN4hEX7QkJM7r3JAqL0_qDCl7FI3LE_CHtNtdr8tnvL6Ds0yLDL4IH03zkIMkCbQl8sE4iqlRKU2ShFAk_7vLkQSInExXqBDR3eWUxS5xRg-2dEm0uWFdO13HzUG1GXOhExoKU34oC1UhbMFadufwqsQck7Zfms8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده!
فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن.
در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت وزیرمتن، از همین فونت استفاده شده است.
کافیه لینک زیر رو به Claude بدید و ازش بخواید نصبش کنه؛ بقیه‌ی کارها رو خودش انجام می‌ده:
https://github.com/m4tinbeigi-official/claude-rtl-patcher
به همین سادگی و خوشمزگی!
😄</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4596" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4595">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GHjuloTRRFFuo9ZrpMzMoybJLsp7ZvOZqmc6olOEhdmrv8_Z25dC74QZ1eIGyyEeeB_w8yeJfwnHnkazplycOlFLd_YKAo8QYaxTbwte0vbevxeOHVzUZj9ojQQjWyVACt41OnNKGKhazHWZpgmsS7rnTEzG-ohBfrFHKVG1TkigQhhqd8JQzuR01SnnN2BcSpab6TFISUT8PreNVdQLUt_ogm9G-mYvnrI6pw--sryLfomN7pIxNNZF4gOso0YDtahfmboDZPblGDJRKciW7THRpTRim8UppHjw4HJMFs0HnCo9bZhP-zI3JsbqPVSeauh2Q8g25PpRu2stF47ulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
@whitedns</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4595" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4591">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-poll">
<h4>📊 دوستان پروتکل WireGuard واستون وصل میشه؟</h4>
<ul>
<li>✓ 1- وصل میشه توی Aether، اما پینگ نمیده توی V2ray یا تلگرام🚫</li>
<li>✓ 2- کلا توی Aether هم وصل نمیشه🚫</li>
<li>✓ 3- وصل میشه، اوکی هم کار میکنه✅</li>
<li>✓ 4- دیدن نتایج(حال نداشتم تا الان aether رو ران کنم)🤡</li>
</ul>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد(با پشتیبانی از MacOS و Linux)  توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.  تغییرات…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4591" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4590">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OKwg_DgwvavSDB8AmMWuLN2Sw2l4iyDVkL9_WTzHQ1pVWc9ICkyvb-PrG88sZjSL-PvMWc1p7a2S6zg4QYu8ICvrAHg72hhV5wnSQaobRIx0CAngZJb67w-pCquIXRzdcWiePziV86eHM-2J9fIebWdSzp85TYaxxjkTUjtSf8Iv1US2ueog1u4rLobUhdXEFpRTDaU-0t2qrLCLYC4SGGBtMJEG0U0Vs7WFwwNzrV3MJgn2HWFCkBg4VFTphZpGvfzfrHCBkPGR-wgmFQ1Q1Gb5LQp72exShbmCmqi6qAcyHb3Dt8Vqirbm80OfAW1uQcF9msZmKmVdVCy0A16cOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد
(با پشتیبانی از MacOS و Linux)
توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.
تغییرات اصلی این نسخه:
1-
اسکنر قدرتمند Ironclad:
بقیه حالت‌های اسکن فقط چک می‌کردن که آیا Gateway پینگ می‌ده یا نه. اما Ironclad یه تونل کامل و واقعی می‌سازه و یه درخواست HTTP ازش رد می‌کنه تا صددرصد مطمئن بشه که کار می‌کنه. یکم کندتره، اما قطعی‌ترین حالت ممکنه
2-
اتصال مجدد (Reconnect) هوشمندتر:
قبلاً اگه اتصالتون قطع می‌شد، Aether می‌رفت از صفر کل آی‌پی‌ها رو اسکن می‌کرد (که تو حالت‌های سنگین ممکنه چند دقیقه طول بکشه). الان اول همون آی‌پی‌ای که تا دو ثانیه پیش کار می‌کرد رو دوباره چک می‌کنه؛ اگه واقعاً مرده بود تازه می‌ره سراغ اسکن کامل
3-
اضافه شدن بخش Obfuscation:
این قابلیت دستتون رو باز می‌ذاره تا شدت مخفی کردنِ هندشیک از سیستم‌های فیلترینگ (DPI) رو تنظیم کنید. پروفایل‌هاش با توجه به پروتکلی که انتخاب می‌کنید (MASQUE یا Wireguard) متفاوته. اگه دیدید رو حالت دیفالت وصل نمی‌شه، درجه‌ش رو ببرید بالا
4-
تغییر پورت و Bind Address:
الان می‌تونید پورت SOCKS5 رو به دلخواه تغییر بدید یا اینکه روی آی‌پی
0.0.0.0
ست کنید تا پروکسی رو به کل شبکه‌ی لوکال (مثلاً موبایل‌ها یا تلویزیون تو خونه) Share کنید. اون باگ کلافه‌کننده‌ی پروتکل UDP هم بالاخره تو هسته فیکس شده و الان بدون مشکل توی شبکه‌ی لوکال کار می‌کنه.
5-
پشتیبانی کامل از مک و لینوکس:
این اولین نسخه‌ایه که کاملاً مولتی‌پلتفرمه! فایل‌های نصب ویندوز (exe و msi)، فایل‌های مخصوص مک (برای چیپ‌های اینتل و اپل سیلیکون به صورت جداگانه)، و انواع پکیج‌های لینوکس (deb، rpm و AppImage) رو براتون گذاشتم
6-
رفتن به System Tray:
گزینه‌ای اضافه شده که وقتی برنامه رو می‌بندید، به جای خروج کامل، بره تو تسک‌بار پایین ویندوز و همونجا تو پس‌زمینه کارشو بکنه
ممنون از
@rqzbeh
عزیز بابت مشارکت‌هاش تو این آپدیت؛ و ممنون از
@CluvexStudio
عزیز بابت زحماتش روی هسته‌ی برنامه
لینک گیت‌هاب برای دانلود نسخه‌های مختلف:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.5.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4590" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4589">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بعد میگن شبکه‌های اجتماعی چطوری پول در میارن
"Data"</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4589" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4588">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4588" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود
فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4587" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه مقدار برای همین طول کشید. اما خودم هم بیلد رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4586" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
