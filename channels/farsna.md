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
<img src="https://cdn4.telesco.pe/file/djxZJL032Xjs2Lwb5RTCxPXPPL9rgtkBICFLTe8nQTjXAN0fsk6XzLiJTv_vtJ66LGnY_ea-F5X4WnygEeZ1pjUhuNBCsu7v72T98y4-pot-s3HbCuY00GEQHW4ZgIJBoqHchyUP5lyu8ie7vVrai4dH996zWAp5scvna0PpVMSCsq_ebPmgbgXvAo9nn08P-ta8lJyOxLi6yofK0zxGSMrZ3-s5YVqPsYfNCFVqm0LyqX_3TFcKgtJwgzuY3uXHhNPcjRPAzjIlVkO6P_xg_05sfco92W4OYKMt5W4PizUfX9MppfT0eQLrBZPhVqkH1_QWxVtWB1q60gQRfH3FBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-447874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fZDTANAZ1pBoe-4f7B6t9XxYH0O62TRGcNI6XCKx324PHKhL_m08QrG6StqsKzhlvu_7HMrqCHt3kjp7q5v8RL2XZBx0lkqmc_yjfqD3O0A0nuRKl1LB9ZBmIr88lFAyfkrfDmurUTh2vUP0TaLlV9WM5gWFQRJxY-jSp_2tfVk9qSc3FnqE9IFK201pOpVrU7jSPvf2jmjUoQdp2bZ9UjWHOxT6Y3szMDX7MlT460lgt_rjHBOFdnC7FB8FmkBz6zznqL0VCM7W8XAVpqxcFbpWkYZ35pQ5GdlIr6wpA16BZoFTuvl4nULNQSo_edWTi75x4xzMZtC20KaKQxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عمامهٔ مشکی‌ات ماندگار شد ای آقای شهید ایران...
@Farsna</div>
<div class="tg-footer">👁️ 330 · <a href="https://t.me/farsna/447874" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از موج جمعیت در تشییع رهبر شهید در قم
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/447873" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای شرکت در نشست ناتو وارد ترکیه شد
@Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/447872" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک محله در مشهد برای تشییع رهبر شهید پای‌کار اسکان زائران آمد
🔹
در آستانۀ مراسم تشییع رهبر شهید در مشهد، اهالی شهرک شهید رجایی با راه‌اندازی پویشی خودجوش، برای میزبانی از زائران پای‌کار آمدند.
🔹
ساکنان این محله تاکنون بیش از ۳۰۰ پتو و دیگر اقلام مورد نیاز را برای تجهیز محل‌های اسکان زائران جمع‌آوری کرده‌اند تا سهمی در میزبانی شایسته از شرکت‌کنندگان در این مراسم بزرگ داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/447870" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرودگاه بوشهر از شنبه بازگشایی می‌شود
🔹
مدیرکل فرودگاه‌های بوشهر: نخستین پرواز فرودگاه بوشهر پس از وقفهٔ ۴ ماهه روز شنبه توسط شرکت هواپیمایی ساها انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/447869" target="_blank">📅 14:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مازندران فردا تعطیل شد
🔹
استاندار مازندران:‌ در راستای تسهیل تردد زائران برای حضور گسترده در تشییع رهبر شهید، کلیهٔ ادارات، دستگاه‌های اجرایی، مراکز آموزشی و دانشگاه‌های استان به استثنای شعب بانک‌ها و دستگاه‌های خدمات‌رسان فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/447868" target="_blank">📅 13:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مسیر نهایی تشییع رهبر شهید در مشهد اعلام شد
🔹
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است؛ نماز در حرم مطهر برگزار می‌شود و خیابان‌های شمالی هم محدودهٔ نماز هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/447867" target="_blank">📅 13:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6b053ed6.mp4?token=TPiH2RCk0C4lRqrhPV688aolRQyb8twCUUcY7FhkW9RU9hksKuVWWOqm21G0l_fax2Pp2jH7CGFZT9Dzs46QmYOElimd_d3LbAQ3LqwMKNJg1SlqWWxAG_UpyReKeF7TQb-z3fMCfXngSQ9-ZcUeOUzRbcCey7sieaZnO63EPhqmqwKtSMALKwmcW9gx7P8XWvlHrWD0n_qL-pEJz--wi7hXctU4kwUnTPCQVAJ2oc_XwCg4eACcPxNn1evYvPuO4h7EQ2snfRNhoOsigYTllP4_P46_lZcuqhKyyO0F_xSl_0BXt3O5u8xo2DhHunsJCE25HDmBUAI6MTKAC6JKhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6b053ed6.mp4?token=TPiH2RCk0C4lRqrhPV688aolRQyb8twCUUcY7FhkW9RU9hksKuVWWOqm21G0l_fax2Pp2jH7CGFZT9Dzs46QmYOElimd_d3LbAQ3LqwMKNJg1SlqWWxAG_UpyReKeF7TQb-z3fMCfXngSQ9-ZcUeOUzRbcCey7sieaZnO63EPhqmqwKtSMALKwmcW9gx7P8XWvlHrWD0n_qL-pEJz--wi7hXctU4kwUnTPCQVAJ2oc_XwCg4eACcPxNn1evYvPuO4h7EQ2snfRNhoOsigYTllP4_P46_lZcuqhKyyO0F_xSl_0BXt3O5u8xo2DhHunsJCE25HDmBUAI6MTKAC6JKhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از مصلای امام خمینی تا حرم امیرالمؤمنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/447866" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسیر نهایی تشییع رهبر شهید در مشهد اعلام شد
🔹
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است؛ نماز در حرم مطهر برگزار می‌شود و خیابان‌های شمالی هم محدودهٔ نماز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447865" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d8f2f20f.mp4?token=YC7zUisd8cauekuwSE3JN7GpwZNYxzD_ZQ19la4l4vbgU9F5EHzzqjSTmMfVuBj3AmqSKSex2HESA0_DTj08P3BLSLiyEBNOraZ7RxfBALW3uLiUe73e9UA30uH5fKRvG2ZNf-abtLb_yKqUJt6IoIaSHTPFiEOlMekfxEwAkxxPysJWuVG6dI9MYS4lF8qTKQDliN85HmAb7pTI13Otgg8QAFiZvC9hmAK8Bd7LsKqmJ1hXXfQZOlb7_Oy5iPSc-fNi32Xk28pUmPH36rWNBTHWzIg31P-hc0xckYurKf9aQkBl2EWQ096uCHEfHhkBEn3Qx9CMCtLgG6YzbDr5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d8f2f20f.mp4?token=YC7zUisd8cauekuwSE3JN7GpwZNYxzD_ZQ19la4l4vbgU9F5EHzzqjSTmMfVuBj3AmqSKSex2HESA0_DTj08P3BLSLiyEBNOraZ7RxfBALW3uLiUe73e9UA30uH5fKRvG2ZNf-abtLb_yKqUJt6IoIaSHTPFiEOlMekfxEwAkxxPysJWuVG6dI9MYS4lF8qTKQDliN85HmAb7pTI13Otgg8QAFiZvC9hmAK8Bd7LsKqmJ1hXXfQZOlb7_Oy5iPSc-fNi32Xk28pUmPH36rWNBTHWzIg31P-hc0xckYurKf9aQkBl2EWQ096uCHEfHhkBEn3Qx9CMCtLgG6YzbDr5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از مصلای امام خمینی تا حرم امیرالمؤمنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447864" target="_blank">📅 13:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5VlnQ-RAEAMWh8dghEYU5WK3bwzZ-eIOdMSOk297dvIcPH1w7Y7aCujpRyL8p_W_S80uP2UzNankx3GuhiRFtBymjq0zsjqCpzsH9GVVl2X-uSktVShWvaX7iMK8BYOFailRY4uOnVE-FVxG5rqP2Djzgqa-9se6y5qwH05z0rZeNHD7JvYrckak-pz2XY78Xw4hqL3ptKxDX57Mq98Akg30oMzn6Sj9_VlAwGrAhJ81sjleJ5vUjrmhPNYULjRlttA-LKNRGzyRvCje_wTWuavmxGY6-eFehPGOj0FHRR25OOObyAclV7gcCWKQjWuawvWHnuhFLisEQlsQFEnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق خط سرخ خون‌خواهی را پررنگ‌تر خواهد ساخت
🔹
فرمانده نیروی قدس سپاه: مطالبه تشییع رهبر شهید انقلاب اسلامی و برنامه‌ریزی گسترده برای این واقعه تاریخی توسط دولت و ملت عراق، عمق پیوند معنوی دو ملت بزرگ عراق و ایران را به همه جهانیان نشان می‌دهد.
🔹
حمایت مقام معظم رهبری شهید از مردم بزرگ عراق و به میدان آمدن مرجعیت عزیز باعث نبرد شهید سلیمانی در کنار جوانان فداکار عراق با داعش و آمریکای متجاوز شد تا اینکه ترامپ جنایتکار قهرمان دو ملت را به همراه فرمانده عالی مقام حشد الشعبی  ابومهدی المهندس به شهادت رساند.
🔹
تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق به مانند تشییع با عظمت شهیدان سلیمانی و ابومهدی، مشت های در هم گره شده دو ملت دربرابر فتنه های آمریکایی را محکم‌تر و خط سرخ خونخواهی را پررنگ‌تر خواهد ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/447863" target="_blank">📅 13:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادارات گلستان فردا تعطیل شد
🔹
استانداری گلستان: در راستای تسهیل شرایط حضور اقشار مختلف مردم در تشییع پیکر رهبر شهید انقلاب در مشهد، فعالیت دستگاه‌های اجرایی و ادارات استان فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/447862" target="_blank">📅 13:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f7a5dc84.mp4?token=h-Cf1P5cqjiDwj-yBWRxdBIQ2IqDM5CBt4Q9A-S4axdElSpPN6TWxDtUdSHDXD7_Ksr21M9UrzuX9Hi1OrNzCo0sDCNiZESZEVdEA7AJq1sY11GWcxcSW7fMDVk7DwIjceExo6e8MVLGedV0SQnbFvJVTUWa5_NQkeokjDPDkiqT-1ksmCj81n_2tnGTopUi-0Utp0WfPkOfNdUXSsQIGeNRDwEdxLG-BbFuy9ezqNUVYekES_VaX6O-ci27pIudGY6yprR032MXfxhMJcYfhhI3aTe4dw0r8slfqGhEnmau9rWfquemPn9XhA6zi1y1dX5_T3PLUMhkxAr9kQHiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f7a5dc84.mp4?token=h-Cf1P5cqjiDwj-yBWRxdBIQ2IqDM5CBt4Q9A-S4axdElSpPN6TWxDtUdSHDXD7_Ksr21M9UrzuX9Hi1OrNzCo0sDCNiZESZEVdEA7AJq1sY11GWcxcSW7fMDVk7DwIjceExo6e8MVLGedV0SQnbFvJVTUWa5_NQkeokjDPDkiqT-1ksmCj81n_2tnGTopUi-0Utp0WfPkOfNdUXSsQIGeNRDwEdxLG-BbFuy9ezqNUVYekES_VaX6O-ci27pIudGY6yprR032MXfxhMJcYfhhI3aTe4dw0r8slfqGhEnmau9rWfquemPn9XhA6zi1y1dX5_T3PLUMhkxAr9kQHiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند قاب از آماده‌شدن نجف برای استقبال از قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/447861" target="_blank">📅 12:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPXnYlZEQju--aC4FCbQAVxn_w0fPhjxs4Q9_mP_kj7ZhrM0EdUmTGPaazahFJIHEjLqVkcTxsjI4fqrc2be9Lxy2DjVXxivyvxsQxWcUy4rExolI-pNVgyXi6GkCEH730dvhe3aj9bndzwgz0XFONhNEntT24JUMCy4hK7VdKLiNnrDdApVF0YeWz0Q_T5Lr3DqW7T7EfFZxkSr3yaPVsbqxD2X5PfAA4j4TtA9WQ7yQDrkFtlQ1l8ZbT4yLzSNODvAyXYgwR5tLsAwSIrz2_m3Ex7EWUBN-j1Y4HjIoNmW6RxMQrvxZk1jVQOf9W49IlmvSUfKIEnF6ITOhkMcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش تاریخی بورس پس‌از بازگشایی بازار
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۵ میلیون و ۳۱۲ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/447860" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc49333c2.mp4?token=vEQz2xKfsmouFZlu-aVBjpxMTOfzD29HllfhvC-eLe-4Kx_qTW5avFEZi1Rh2mHwHGGSMYIqevPWaHS7shuqwPTtQs_XcRJjsYrb6czDyJqmg7Ry5APyPtSvpKgSZp_bTnfr3xCY5ln9L5A7WL4C66Sjt_A71TmB2-QKygcRDylELk43Q5BUzYWZBl348Z6SUyUvVuEhKjN0P3HquKVxMXzKzcLDMYgo0fndz3JJ7XCGNW3svnF9x4xaN91yyjxwji118bXMjagSRsjl2YJEdEkCbQArIwhCfApCgrPfiqgXtgYj_9AFOzMp7zxG8Tr4INu3QiaR_Fd57QK7qbUFzkLEFVkYl-oPIJSPXA6w8DRH4SPi4UwTxuKTXI0-aPR3iAKUiTCAEwq4ib8Um3QJpALIdI_kZNRFUjQho5flgypH0PR4P_GdhGBsmzznooIaLLs0zYbNcu2FC1CbPueUjPTP6j5aDFONUCVYFAsfUIJ_QrVEp9ld-9pN3T4A3xtpQH2Z3fptwyA9Dx4ordZDld-JXaBc1JAbmO6AmS-OTb6Gtea-3Cmk-VV46fRfJ4iCw6yj_wWMxc867Iibl0mLQm0Neefknd5wDL_TjfGtHRv_i5GlltOtPprVE3iy-SJma2XWLrNQpHgzQMut87ep9qbW8Cv2OOUC7nH3qnf5Eeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc49333c2.mp4?token=vEQz2xKfsmouFZlu-aVBjpxMTOfzD29HllfhvC-eLe-4Kx_qTW5avFEZi1Rh2mHwHGGSMYIqevPWaHS7shuqwPTtQs_XcRJjsYrb6czDyJqmg7Ry5APyPtSvpKgSZp_bTnfr3xCY5ln9L5A7WL4C66Sjt_A71TmB2-QKygcRDylELk43Q5BUzYWZBl348Z6SUyUvVuEhKjN0P3HquKVxMXzKzcLDMYgo0fndz3JJ7XCGNW3svnF9x4xaN91yyjxwji118bXMjagSRsjl2YJEdEkCbQArIwhCfApCgrPfiqgXtgYj_9AFOzMp7zxG8Tr4INu3QiaR_Fd57QK7qbUFzkLEFVkYl-oPIJSPXA6w8DRH4SPi4UwTxuKTXI0-aPR3iAKUiTCAEwq4ib8Um3QJpALIdI_kZNRFUjQho5flgypH0PR4P_GdhGBsmzznooIaLLs0zYbNcu2FC1CbPueUjPTP6j5aDFONUCVYFAsfUIJ_QrVEp9ld-9pN3T4A3xtpQH2Z3fptwyA9Dx4ordZDld-JXaBc1JAbmO6AmS-OTb6Gtea-3Cmk-VV46fRfJ4iCw6yj_wWMxc867Iibl0mLQm0Neefknd5wDL_TjfGtHRv_i5GlltOtPprVE3iy-SJma2XWLrNQpHgzQMut87ep9qbW8Cv2OOUC7nH3qnf5Eeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با خروج خودروی حامل پیکرهای مطهر از بزرگراه پیامبر اعظم، قم برای همیشه با شهید خامنه‌ای وداع کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/447859" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpYlX8dVhGGu8oXRCk6P0QWWIEpSpgtkPaf2WqMs-sVGfOCb5Xzxmq0sZtZYZBssYWp7XcNyVMPbEzvnzOwGBkKWStQWXWkS2ZjN9Y2ptf5g7bI3gz0QL2WKuUuUNmhsg3ymD4C8F2pGdxbk833PQG672rsV3IBdQPlNxQsGCG5NuWPQSF7Zxn9wx53fy6pRQ2ppJjP6h0FfbyeMOLagQDSl0WcuKyThUoSb31BhSyStsaq43_DomAtMMoFmlmkNSCBAvORUvCs8Sj9OPbDXyrcKtMRVUWLXcN57u4scP19f1rEAZMrE2NzpKSNBlAoC9OLpHk1ayeyXzuN4QmOnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNvvDJIOGzwlQsERgZ00DgTqw5xZQUNO4M_H8A9m48cyZmT9ybZPLxwbUfDG04M50MOKlNSxG0rCOoYrdG7nD-h_iuyoeaB8PbuEyUi6PLeGR7mQQrO_2_XPaUqeWAt2-2Wv1SKemR4WangVcxbz0Pd-C1sTK3ngpnCYSNTLQbcYRsaybzZitzRU8HZsYahrpU_4K2aWSvbBF8tnpVng1cHdyfLXhUGPGPq3TT5A21cAQk4tJsvsL8JNKTcficZuI2C07_-DAGEv15BMXfW2O9adSYSDANia8c2p-me3a1OtAln3AYk8BMtajiAqKr3hEipdZe1yyAq39pxBiFCKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdawiFAi_nFLoRclCsofdjimQDvd5XKaMfRh0HocVW2E3YVoYiAQzhSZvVCF-3D0yMxwg8NGkSvnn2fFmAOYAqmZyMN3qtVk38Gy3b-oL60--7ZMNbeCJ6vx5_WL_zKFqL2ZOIOLbF41prhoVA2e3parOzn3vrn-3s09Z8uRf1nFRke0shzlhRRDfkhvT_798TBtSaKpv4jdSrRCeeFQAyKDFF8UwxF_MgIpy1aYeC9EMLM9-34_-Ab-Ng_PyCDyHj71qgBv6Vuj5L9kLJftc63-Miwd1oOUgZhZU6fML6UnXM1cXV9m9--kOGMFAFxhG1gwUeAZ-nMvhWyfiXt9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbwzMDTLLR0vT3hdRFccr0-zhh3qMx2bxc0GD9kmURWBrhxWbOGJBGUA-6MuiI4Th8saym6byYKiRiIv_UPOZcJW4rlo4OExW7rZehJNJl2nbVyuho3KqyPXE3Q0A5ilyosEW_aIjTCsMUkEhI8v0J37xyTF1W8rZ5FBJMJSRWSbpFhIRHXNajbk6N11jmGFxbXo9gfAVnMwFMz0JjNTT08uuPetc4LEh8gByJ8wAMR5TLhYfUiL2GEEYRQQh6XNj4i_WT3iDgkOGpc6z_4VAWLkl8sx21XYmXap64-8Tz7rQ5JguQvhhlg6b9KDe7qLdE7jBcgeh_xzQSH2uUU9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYk_doX0K7ct1TREax65e1DDmijLoXBkd70-GDlecOMe5E4kNQ5pHm5SQKw9Wdp52v8EnlJzpiSNkgi9eQ-FS_0e7QzLSgHqO29cPmJQp57rRw3K5xMtf0FYJUqnYMceeYDKbEJiEMZhJFaMeuYQVq_2jz-3R7dWlPJDLyyX4mjyEb9_hqHZxf3HKyIGzuv-lzhj735jQtWGlBDfCFs9-dE2F_c8clpaYUEV7xpV1yH_wMPYxlA-poJXYnelcFGIMOh0SBHkhe1Jjogsc3CQu1hHlHFiEHVjgHoQCrO9qPKJB30gmFEKqbY8PYGE_T0rOv0kYy6TtX2lhmQqC7lFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/na4n_R1P3bkAE_-5rxMs50fsTXNDj4Yo7j6baoErDeZ5fYKFSdf_-tQ16EaDkOAaunjmJOkdAt_-oUQsSE96TKndAQKiqwgztZYyySOSd-AFnKeMWRrDyVh6vqmQAG0LuD5VNC2ZkzBildw271k71K-KbKk2qLhI8zdpFznYcvweCDFE48MBxW0-4EaflE_ljnxGQjFoyOig-N5cWyzv9ESNHtKYLFHwbyXH-CEzAk-6YVbFBD7U7k0UtUSHAMsrz6mtBpJ7dwGU1dwlJsceFqc1EgfyrW07Y-2z8eV4YseZyv6dyW1WqW3lr4XCBgGvJqDx6lqvgjfEwccbtQAlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZU5l36AEtsRnmFrcO27QnMrP9xFTksiSb0M-U8j_VZqfJ0rCsPDCe-ta45ImStagB6WamDJfBI_fFtMl09I6HPqjUoeduw5bgesQ68GKnhlXFe8BMEQbqW620MzDVQSdEJT3sqiIaVSEecZnPUi6JmDVOPtAP9_5szJRFPUx2nj1KvplRiVpDL-KAK_Y903skRJoRCOJ3CoWOZmEGJxuA3eg_P8xxbdPmBzRD7qw__eaSXyw1pa8QrFtGjP_3VpL8jIy_st7LgErP7bkHagb5K50uoGDjZc_zVx8CEenxbgSv_enIZx0X3eAZBXNtEc93pvdPMtxN8db5E3rb5Tguw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پرشکوه پیکر پاک رهبر شهید در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/447852" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447850">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53eddbf811.mp4?token=Y2zP3vINBip3FlkVDhpvtW6JXsFgZBlTV-ZWvmCImBE7BCBgkVvDJaewEMTQW1Lv9fBfkbgm7vvOiOrdkzBp2iuChAV0-3iufD7ZWtJDukdgbnVpSxW312b9JOl9LLoIgn1n5yKpNO0QwQi9uKQe_tupoEPcGn_gRgOpn6Eni4d6vkeQyPUgkzQ6NTPUcaCJ8IH22XI-tt-nn2YmK13rniQTFf2u5YBvlFS9Mz_Cjge8qiYlc7HX-ECJWSksID9QSUfnn3v5IStdUe1hvGHrayO-eTFOJUjUT9xSNbzfzVRN43MVoeF4iKxsWfxYb1eosA8ePsf2Iapd6JvWgqYq9SbfCqhdWzll9GgUiRVEBSJi01TmLlXGLZDdEytrUR7d35UElEYHXsYI953uL3TTSHkbl03nqJInGSw6DXBYHIEf-eGW7-flV0oBOt_sberC4OqQDGZv6fQa0cIFh-aOMXUg_YEfGN_2zP78BO8N4DHlgWwwtXoVbVZZBveqGxywtFAlp6mR1Dr6kp3cq7JBkNsFw5FUPMKC2XqYP6cFkMzawG8RtGHeb9urP1zFac9zgY44J2hCCHEYap19UDeuhfVd4VLH9LkF_Mwh08CEi7RQNgf5OrCUUVvDoVMyi3p2xYLwSYAZW1fRIRmi4qTRes1OFaT9b5iGl8O4mFbda_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53eddbf811.mp4?token=Y2zP3vINBip3FlkVDhpvtW6JXsFgZBlTV-ZWvmCImBE7BCBgkVvDJaewEMTQW1Lv9fBfkbgm7vvOiOrdkzBp2iuChAV0-3iufD7ZWtJDukdgbnVpSxW312b9JOl9LLoIgn1n5yKpNO0QwQi9uKQe_tupoEPcGn_gRgOpn6Eni4d6vkeQyPUgkzQ6NTPUcaCJ8IH22XI-tt-nn2YmK13rniQTFf2u5YBvlFS9Mz_Cjge8qiYlc7HX-ECJWSksID9QSUfnn3v5IStdUe1hvGHrayO-eTFOJUjUT9xSNbzfzVRN43MVoeF4iKxsWfxYb1eosA8ePsf2Iapd6JvWgqYq9SbfCqhdWzll9GgUiRVEBSJi01TmLlXGLZDdEytrUR7d35UElEYHXsYI953uL3TTSHkbl03nqJInGSw6DXBYHIEf-eGW7-flV0oBOt_sberC4OqQDGZv6fQa0cIFh-aOMXUg_YEfGN_2zP78BO8N4DHlgWwwtXoVbVZZBveqGxywtFAlp6mR1Dr6kp3cq7JBkNsFw5FUPMKC2XqYP6cFkMzawG8RtGHeb9urP1zFac9zgY44J2hCCHEYap19UDeuhfVd4VLH9LkF_Mwh08CEi7RQNgf5OrCUUVvDoVMyi3p2xYLwSYAZW1fRIRmi4qTRes1OFaT9b5iGl8O4mFbda_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران قم در بدرقهٔ آقای شهید ایران
🔸
از مسجد مقدس جمکران تا حرم حضرت معصومه(س) ۱۰۰ عمود وجود دارد که تاکنون پس‌از ساعت‌ها حدودا دوسوم مسیر طی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/447850" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qT4sKYi5NmU2mblSIu4_lCMYS_vIAqnNNz_BfA1-Ki4-S0255u2_pDdICtJM6Rj9eGt3oKEaPk6jqV4IKruoptuwSKfXIFYBcAz-ZE2vEdsUETvChCFjEvTvX25v5jeDgUZEv9nNh2f8xAbfBSm7TMe-vS_C76zJB0mT-5rcw8ECsLcI4LOgELkBovxN8Sd7R3tuDND-irhXyaHV0vomnqBvkxxGVsVyi12m1OoTtdbXm1K6NBLmPAuYc27yROXNZOLamo50iuBu3V1p9QAH2B7T0y-tjoAdZaZTmE2Bl07nllqAEsI6eZSf2Mw0Z0m6CmSq8llA7lrcwBCbWCS74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXb78PU7FIdPch-QiTMmrJLTgqUzCBKoZSHKRRYlzjRecPpqlEhrWW_dWeRvhdLSqVTwYzWWbyJ3u2Xxp3GCrLtIb20NnF-CNs3zNVGK2UU9bhMC-PtGpVajKBRtV68iFdE5mdj1YbiXHagh5AoJUtLi33OZ0kVM78cWRZ4xK5UEDL0PvN4d_WZGVOiDvISI__zTNdoJdyZwra2s1rOEDuKlYjN75OW126GFheIyVwbO5uLcNcNyCOE7KWjFnOPXqsM4tSIWasGJNcUifaFZK3aPJ1XvJEWmTw8TZT_WxgDKELxMcowxxsdK7zsIxr4rO-ZIp0x6Z9pUBgz4TRVj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZGqGo2GMTSEzlfpfYgpuXH9Fsa9TUZLxUx_8pUTUx1pjLaINgbtR20Yk7j8brNcDRhTDnpr9jEt3LyHPqkL7TmM-OQRZz9G92HdTgFvi-tQeYzKLidfdBL1uCyXdv2DlA_qFuyv6fk3Fbnklw49bzO9StoU-9qDiYDyiRSTcLyjtRILJR77W9KMzyoQE2eNwjgcXOIG1rnPBft6cY6sqCsehfXyPlSnjsAKfzDBPSK3YyNVpgbh8-8_LbVLQ3P-BqAvSRgrYuPH8UiUhT7i2Uo7wdFpa75eNuEGnW6xnOE6ol5ccw5u4OovkyQRDR4fVR7_qMJS-IYSnAp8k6NvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4Cxa_CeYGUtIX1eEmV7nbCtdu7zPtSMzVx5qhnJnogxGwqdMkYCgNSMMjI-zYbxJ1v2z9Kd_yZ8-GxdUoHArlVaJQ38GNpXvnt2ZbcZX4b3kzEfRwr6uHj516byKGlwneaFpsjfkqKT7GQ9s8w0pLu4pXMOoCqgR9pWH7eT3p8KYed_rrHI-eRNrkmO8-iboduXYr2G1TbviTig3qSsj7dbw_PkpTG0cm9V1ZHz4LE-enP7oKoP62acFiM3BVhGJMrzXmFWiP3vVC5xmjgt_AdepnBU-oP5jc-sYY7J3xbihKTnhPNSkrb9ZdGm5td976IHVGNLVmlthupald9-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDnDExoxgY8V5LIk_YPCBe6NId0qDeUnoob9wvTsV9oul8ZdcnhY1SiacqNj7g-AzZ-XNoTfQmhZyEh0FwPPYrtqsXzbIltAqsJnIre3dSn5s29602M7J3trj252GdwsEK0ecSebPzcsc4or-QVlTusnRNxcBsrOTgKEW4MmMDnJ4FtOlqtqaDrvxMItaR9jzIZR3PC3JIPEehYaLv9X97YEKsm0uLH1o-JpkDESI3xpyO4cPViozdudB1pgq6RAQOwrhx5natOW6ulkeTgWhSjfLKHwrGnYk2FQ0RvZ54wmyCl81zzMoEEH8r65SBVaQ_aUYVB4lWj3aqbzYoS8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4um2z2-XU2HRMvC07q5iddeeHJKEeM075jplHtOdLIKD9JfH-KIFZ0xeg7HmEk9SJ0fUo1m4nEN_xlRb23vrE0H5oOIXgybnHe7SzL7lBrPse_8a0tYkwjhY4QCbh9qFW_Nvmc5a1w-W8Orq11pTh7_wxPqTMKpY-hmEvTs49EtB1mz9mGYKDqbKjt-UL8Yv81cZVUMJFK0TmTo6QBKYQRE1A6Bd7ArXwy6g8dsxi2-dG2DsBHNLDbJqO4idic8CxYX43P1Kg31tEpZUmhMa5gSCrjFaLL6fXx53bA5BUeJmp1Uwq16t9aUbm1peWL_mjNXgJWYjpFnsM-DWBq5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbvLfTRZl7TKuYdeB7pgaQ9ymJUSM3croaIhex9x8FcovYCf282V2FOGbp_X4tXx7QPFtsm5JQcRLVbV9G5gZ8BMT-kx_eZzPEvREaRx8LEd9sypUgjTaqtzXP6Ddk8WGGTW85z5tPo1qDWi2Pf5Q7nZ8HEepTnhw2jqRMCeLljPhSO64VqQ6yXhPl87P0hUO-qaEeic0aoPOXrcXOoD1VLhFoYd_ZRtbeeaTbYkuaG34gpQr-FqPixrxIlaVwE9I8X-L8yXTXLXLD6V4id7VAnZNT4h40Bmu917FjiKnELiP_SZvYibAmAHuU5VPLReUz5C_WOIlBHiDK8n9Zqkdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
نجف آمادۀ میزبانی از رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/447843" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a691fdee.mp4?token=Rq98JysMlEhTttCxuRHTvHK5zjGztZ2RrPWoL_ubT7RTKsukcrkVqOAx7ZlFKZq7DcvEbJJcxuZ6Pq-slLsBlx5AI_oNkld_1RRidowjSDX9Mfqn_sXcuURt42GtFpmI4jQdfX0MaPWmWKd8ThqogLAISkOEvXxtt8TwS4Pez9AaklcqBiqWqn3SKYu_tpwAfaQyIXObCm7JH4mIpBebCgb9JdA9BWlfciLh8JfA1FS07oLnRPw6BVcSqjWeIZ-hF5_NMAQkuWVbp1Nn98ZsYeJ0oeP7gZ-cvrFdzdgd-G9QG7TsDcHd9vp9ClUBYo10tUtxFvyry_8cP0GJefyeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a691fdee.mp4?token=Rq98JysMlEhTttCxuRHTvHK5zjGztZ2RrPWoL_ubT7RTKsukcrkVqOAx7ZlFKZq7DcvEbJJcxuZ6Pq-slLsBlx5AI_oNkld_1RRidowjSDX9Mfqn_sXcuURt42GtFpmI4jQdfX0MaPWmWKd8ThqogLAISkOEvXxtt8TwS4Pez9AaklcqBiqWqn3SKYu_tpwAfaQyIXObCm7JH4mIpBebCgb9JdA9BWlfciLh8JfA1FS07oLnRPw6BVcSqjWeIZ-hF5_NMAQkuWVbp1Nn98ZsYeJ0oeP7gZ-cvrFdzdgd-G9QG7TsDcHd9vp9ClUBYo10tUtxFvyry_8cP0GJefyeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ارامنه از کمک‌های رهبر شهید به کشورشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/447842" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee4630bf4.mp4?token=DJ7zdaJvBnrSF3Tf-qNtNhqICLMf-r0dUBobIK0ijYAlTOJp3GZMsNOCBvNtCsIVBoncs1MhcP6eV4lOK-2ORU21hr_30nmAOTgibs652Amd5HKiZ5kPH7iUQwkNvAMEhBUJpQhIn_OOerlqQSzfDMvdaLuYdwa_DkVT5bhS9Z_Ak88jqYCpaaCn1RRS0kBFZKg7f8N7uUDWRXA5PuvbVaFcWlRGH3DlCzc0rHYpN2ajA3C7-iRMCzd_forgOoQ40mLXP68BqsocBXXjhOCtgoN-BQ1L7E0ofaoAffTKQVfe_3dud_WQoIDiC5wHzWTZTUKS_M4JWwBZ3z81gqpDZ7lYJRHqx6UQvXonRu8jC8gb7TtHSnTgLak-OS1zLs74d4IfgtrlUmnMG4IK0eBdQFe1RVfTNwmcOJUb7LlYpDX83xSDTAjXl9qo0VRxG8xGrpkq5BTVA1s8y4t9BsjWuXCc9pEycY3eMQX9KrAfRxrk5lixNUp2Da5449Yf0pI3jdJ1Nmlr_9mwv2y1A2S9jXEFqQkM6uQM3mRCMZdXclcXF5yrtC6Wzfk8Ff0TroIAIoRUVvKNuIukdpPb_gmc6Ey_si2n1m4k_1w9tq9Z0oeyIBEwmXie7VogUK4lmEhwPhqeU4XUwORX-XU9KWwaJ1PvKrs0vjhPOA7ZO_2to0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee4630bf4.mp4?token=DJ7zdaJvBnrSF3Tf-qNtNhqICLMf-r0dUBobIK0ijYAlTOJp3GZMsNOCBvNtCsIVBoncs1MhcP6eV4lOK-2ORU21hr_30nmAOTgibs652Amd5HKiZ5kPH7iUQwkNvAMEhBUJpQhIn_OOerlqQSzfDMvdaLuYdwa_DkVT5bhS9Z_Ak88jqYCpaaCn1RRS0kBFZKg7f8N7uUDWRXA5PuvbVaFcWlRGH3DlCzc0rHYpN2ajA3C7-iRMCzd_forgOoQ40mLXP68BqsocBXXjhOCtgoN-BQ1L7E0ofaoAffTKQVfe_3dud_WQoIDiC5wHzWTZTUKS_M4JWwBZ3z81gqpDZ7lYJRHqx6UQvXonRu8jC8gb7TtHSnTgLak-OS1zLs74d4IfgtrlUmnMG4IK0eBdQFe1RVfTNwmcOJUb7LlYpDX83xSDTAjXl9qo0VRxG8xGrpkq5BTVA1s8y4t9BsjWuXCc9pEycY3eMQX9KrAfRxrk5lixNUp2Da5449Yf0pI3jdJ1Nmlr_9mwv2y1A2S9jXEFqQkM6uQM3mRCMZdXclcXF5yrtC6Wzfk8Ff0TroIAIoRUVvKNuIukdpPb_gmc6Ey_si2n1m4k_1w9tq9Z0oeyIBEwmXie7VogUK4lmEhwPhqeU4XUwORX-XU9KWwaJ1PvKrs0vjhPOA7ZO_2to0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از اقامهٔ نماز آیت‌الله جوادی آملی بر پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/447841" target="_blank">📅 11:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
پیکر آقای شهید در میان عاشقان بدرقه می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/447840" target="_blank">📅 11:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d28ec779a.mp4?token=HKpzPFvHJWBduuoHSi8yoxdOSBxjup8naOWJgsPIIDkjpmOf3c-DQxqaMo-WcG9gW_7e-U_C5FNKxow3RLporsqWB412JVR7H2sqmgwZLZwrUCVepRuKEjxO0VNuUOAyZ2wJBrHzCH_3IP5uH5PyFvuZCLuhFLuraKf1svuxOJ6Oq1uXWGGGXxDbZUZFksN2cDnabGMx4IG7nsUGJy_RZBHk_RAOHc6kgMIdfTeNSleROmAgJ0LJKBk9R60YlNjg-mXdzq057Q2pnPSgBpaq5xWJ_kTwamWj8ilHUtAPeDZJsrzYO7w82bFesBC7Us9SQkA_Vpy4oSAUDGZ7OJEvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d28ec779a.mp4?token=HKpzPFvHJWBduuoHSi8yoxdOSBxjup8naOWJgsPIIDkjpmOf3c-DQxqaMo-WcG9gW_7e-U_C5FNKxow3RLporsqWB412JVR7H2sqmgwZLZwrUCVepRuKEjxO0VNuUOAyZ2wJBrHzCH_3IP5uH5PyFvuZCLuhFLuraKf1svuxOJ6Oq1uXWGGGXxDbZUZFksN2cDnabGMx4IG7nsUGJy_RZBHk_RAOHc6kgMIdfTeNSleROmAgJ0LJKBk9R60YlNjg-mXdzq057Q2pnPSgBpaq5xWJ_kTwamWj8ilHUtAPeDZJsrzYO7w82bFesBC7Us9SQkA_Vpy4oSAUDGZ7OJEvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های سوریه: صدای انفجار در نزدیکی هتل محل اقامت ماکرون در دمشق شنیده شد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447839" target="_blank">📅 11:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcl6vEAaEdHiKiuyl3zw1weSTVi5ONix5rruceZ9XcgoCzssIw3tAtuh6H_XWWe4TXtSa9kAchJS1VzQSqVRYXZtFr4Pk61ExDdrNW00ZW3HJ0mzG_kHrzr-rD2vyex6ib7ddsgOypgocHOYxRLszmeV9CvWImJ1W8QQRRsGTRPhFcwfY796xOpRVNmtPMDZNSsRKUBPuZMTv4iwDhnSDjeGVwn-0SQO1lbFvGI_p0-UBdYEIkOrcGd_aihHkG-30HThsi74VQM3tAsBIMmJCL8CRN6BowoullIQpJdN6cnzijxqVVSQ_s91rSatWkAA5FYXr1hq8z9q583ZMs5ycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه اژه‌ای به رهبر معظم انقلاب در پاسخ به تمدید دوره ریاست خود بر دستگاه قضا
🔹
با عرض تسلیت مجدد شهادت حضرت اباعبدالله‌الحسین علیه‌السلام و یاران با وفای‌شان و همچنین شهادت امام شهیدمان و فرزندان و سایر بازماندگان آن عزیز سفر کرده به پیشگاه حضرت بقیةالله‌الاعظم روحی و ارواح العالمین له الفداء و به شما رهبر معظم انقلاب (حفظه‌الله‌تعالی) از حُسن اعتماد حضرت مستطابعالی و انتصاب مجدد اینجانب برای تصدی ریاست قوه قضائیه تشکر می‌کنم.
🔹
از خدای عزّ و جلّ و سرورمان حضرت صاحب‌الامر علیه‌السلام استمداد می‌طلبم و توفیق انجام این مسئولیت سنگین را خواهانم.
🔹
بـحول و قـوّه الهی تمام همّ و سعی خود را به کار خواهم برد تا به نـحـوه احسن مأموریت‌های محوله را به سرانجام برسانم و هدایت‌ها و توصیه‌ها و مطالبات امام شهیدمان و مطالب و نکات ارزشمند مناسبتی هفته قوه قضاییه سال جاری جنابعالی همواره سرلوحه کار خود و همکارانم خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447838" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e320d8a2.mp4?token=ErmUg3fY6kXTI3CyniRJQVpGZDTvEP9VHlQUVHwupmr3koeXYNmIrYYOW3LZX-b8TAhtl8WyFFhs4MtY-4IeFDOAwurCpIQXdOBlGBETZ7SRRyCy-Gyzyg2KNfj3vP_r1NC1hnjtSjE2KmDeINXDVxGt-HsxTzFzJSz06npJpUNeV6E2NYKK2D8AZgxFLafW-mwCrkRgrlNfI6uQUsZd1ltiuvWAd-O3epm9UvaeaRHn8tkOkLIjL_Wp_Knza7y7FEnYHMMJK2XBPSkpCbft3qsqw1MdHehxBb2UnExlVf62vwZYYci3YHsH4TzCLvxq2dE0UYHvKCVAe02xTOzC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e320d8a2.mp4?token=ErmUg3fY6kXTI3CyniRJQVpGZDTvEP9VHlQUVHwupmr3koeXYNmIrYYOW3LZX-b8TAhtl8WyFFhs4MtY-4IeFDOAwurCpIQXdOBlGBETZ7SRRyCy-Gyzyg2KNfj3vP_r1NC1hnjtSjE2KmDeINXDVxGt-HsxTzFzJSz06npJpUNeV6E2NYKK2D8AZgxFLafW-mwCrkRgrlNfI6uQUsZd1ltiuvWAd-O3epm9UvaeaRHn8tkOkLIjL_Wp_Knza7y7FEnYHMMJK2XBPSkpCbft3qsqw1MdHehxBb2UnExlVf62vwZYYci3YHsH4TzCLvxq2dE0UYHvKCVAe02xTOzC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربلا آمادهٔ میزبانی از قائد شهید امت می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/447837" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aa8dde97.mp4?token=jEZqSVx6yOnqr-YaSzfYg7A6kNHpAbmPzSig5stwHoxvJg9cW754QgOkoG5s_a-zu22qPYDra4zaq-AkoSU3xGrQkcDHylzWQQVxabGbUDn3LF1Bt2xqrLPWRJ7rIMFvAYgDaJvNBBt-HxzYqej10ArJS3TZjOXzlrXis6cnYSiFupIK_j-aUQsnQn1VmzDwx5u80vVVBgCp6B580WG1pwsZeDkX8A4lbLKf4eX7q6G9xz88MhW-GhX9lUrGy88DrW8dB7xx8vlDimr3-yk-DpVPNYLJe0nAjbPsQII89BGC-jcajFOYh85Kutb7U2MvD22FE49LVgPXofCejH3VcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aa8dde97.mp4?token=jEZqSVx6yOnqr-YaSzfYg7A6kNHpAbmPzSig5stwHoxvJg9cW754QgOkoG5s_a-zu22qPYDra4zaq-AkoSU3xGrQkcDHylzWQQVxabGbUDn3LF1Bt2xqrLPWRJ7rIMFvAYgDaJvNBBt-HxzYqej10ArJS3TZjOXzlrXis6cnYSiFupIK_j-aUQsnQn1VmzDwx5u80vVVBgCp6B580WG1pwsZeDkX8A4lbLKf4eX7q6G9xz88MhW-GhX9lUrGy88DrW8dB7xx8vlDimr3-yk-DpVPNYLJe0nAjbPsQII89BGC-jcajFOYh85Kutb7U2MvD22FE49LVgPXofCejH3VcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش وصف‌ناپذیر مردم قم در آخرین وداع با امام شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447836" target="_blank">📅 10:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شرکت راه‌آهن: فروش بلیت قطارهای فوق‌العاده برای تشییع پیکر رهبر شهید انقلاب در مسیر تهران-مشهد و بالعکس از ساعت ۱۷ امروز آغاز می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447835" target="_blank">📅 10:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43325970c0.mp4?token=f0DVVfPVJm-Zh1U2_W1yp1dp9DDAz-2XyuQHZz2ILQPtCsh_gRwEkDETnUQJoLdyhSQA0NW1-aPcIXlNxGF9e0OrBNDSQjTS14-53F4zq-PLKn4EfWPRWPNUnZ6aT2fwskn1UW-kxUgvvqApNPw1-N35R7brEnuti8yVbmSgwhNFWFymuBqG88ANGWl9f3aG9PAl5ouh56Px8KPCyBdxs7r7v-5dejePIOIe9VyGXDTumVnYSlX6_9RWrQTmijmH4aqlXKbrPxcHlllzuhufSxkOEgQ_e38KiE34Dx6soSRNlXDKtJTdxXhHXY9Oqwq9fDEUA1vXenGKYcXLxSiHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43325970c0.mp4?token=f0DVVfPVJm-Zh1U2_W1yp1dp9DDAz-2XyuQHZz2ILQPtCsh_gRwEkDETnUQJoLdyhSQA0NW1-aPcIXlNxGF9e0OrBNDSQjTS14-53F4zq-PLKn4EfWPRWPNUnZ6aT2fwskn1UW-kxUgvvqApNPw1-N35R7brEnuti8yVbmSgwhNFWFymuBqG88ANGWl9f3aG9PAl5ouh56Px8KPCyBdxs7r7v-5dejePIOIe9VyGXDTumVnYSlX6_9RWrQTmijmH4aqlXKbrPxcHlllzuhufSxkOEgQ_e38KiE34Dx6soSRNlXDKtJTdxXhHXY9Oqwq9fDEUA1vXenGKYcXLxSiHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف آمادۀ میزبانی از رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/447834" target="_blank">📅 10:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86162004cb.mp4?token=Or_dQa_PjYqXwG2FOQa70nWSL8TzQ1nM8fHuSy0L4M-f4PscAFnlRc6isFqxo9Y2kZpa56HSCu0VfTEVk5oIN9wR4LkvxRpPVi3N_JLVUahSoBo5pqk0CgNDQc6ZMGNvxsBrCmNS59JeXjYF3roN4dNgxxluBNBxL8Ofppzrnzs6NU8q7E8QFz-knUJGKLERD0bV0Amy9O2bNt0IExa0XFOwyiQ-R8ktzKJS71Q1TOLHkOM7zRWsVPDgGigSwlS7E9viGwNXh-i3ctCK43lDu8iaxF8cvGlAbcO-CnVdq_jxnnfGz5x0a20nsJHAb-NeOYv4QwbtINxuKNAjWPcyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86162004cb.mp4?token=Or_dQa_PjYqXwG2FOQa70nWSL8TzQ1nM8fHuSy0L4M-f4PscAFnlRc6isFqxo9Y2kZpa56HSCu0VfTEVk5oIN9wR4LkvxRpPVi3N_JLVUahSoBo5pqk0CgNDQc6ZMGNvxsBrCmNS59JeXjYF3roN4dNgxxluBNBxL8Ofppzrnzs6NU8q7E8QFz-knUJGKLERD0bV0Amy9O2bNt0IExa0XFOwyiQ-R8ktzKJS71Q1TOLHkOM7zRWsVPDgGigSwlS7E9viGwNXh-i3ctCK43lDu8iaxF8cvGlAbcO-CnVdq_jxnnfGz5x0a20nsJHAb-NeOYv4QwbtINxuKNAjWPcyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم قم در آخرین حضور امام شهید انقلاب در شهرشان
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447833" target="_blank">📅 09:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447832">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
پیکر مطهر امام شهید انقلاب در آغوش جمعیت گستردۀ عزاداران در قم
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/447832" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dfbb44f7b.mp4?token=AEXjYFUv7CNy8rwcwM5DDk_qrn-KyRxQpJbayo5JLaqIWkK75EVKrUMhTWUSLdRX9utG8p2ZIWnneL_4uWYcOafo_JMnWhTBln9E4WVhtlSY5LZ8VpfSJqGJNgYP2lUA1Vtci6wCeUki9dz0hK3Cos9Ztd4E0irSva1joTXiQnWsxNK1hAtG2r6HZ1LXlPFgrnQ_4LE_2GV323bSiidbcKCFZn1nbpigNMLcRNEahrxbhJxv5WA_0bqKF1KpzAFtURTzCWoPamHEcAbrUFNpzymlujuFY-phJ7YgpAe4KnB0wfF9iHjnEtH0HCOAmqMtExz9vVv_13F3eb0WgKXAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dfbb44f7b.mp4?token=AEXjYFUv7CNy8rwcwM5DDk_qrn-KyRxQpJbayo5JLaqIWkK75EVKrUMhTWUSLdRX9utG8p2ZIWnneL_4uWYcOafo_JMnWhTBln9E4WVhtlSY5LZ8VpfSJqGJNgYP2lUA1Vtci6wCeUki9dz0hK3Cos9Ztd4E0irSva1joTXiQnWsxNK1hAtG2r6HZ1LXlPFgrnQ_4LE_2GV323bSiidbcKCFZn1nbpigNMLcRNEahrxbhJxv5WA_0bqKF1KpzAFtURTzCWoPamHEcAbrUFNpzymlujuFY-phJ7YgpAe4KnB0wfF9iHjnEtH0HCOAmqMtExz9vVv_13F3eb0WgKXAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فاطمیون افغانستان با شعارهای بیعت با رهبرانقلاب برای بدرقۀ رهبر شهید آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/447830" target="_blank">📅 09:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=vN10R5mNHTYAPU8UA8jvinyudY8NGBdK2qakAr3KCfnAPRFPenlkOQSSA77HN4PWtKPt45s0xY5ZuTF70_Gv2oWHqBA2k-j0nbNYUwR-iLiGkm0xtQS_PVVaBQDIjOPvek9vIkpi-be7-kfg6CLzRM8kb6tposMmsbbtKAT8vJvVVvHbm7sIoTJsSkBZ-x38jzIvcODaoNzw73fR4Oz8GU0gewOuG1KPiHcPOuUBHo7Dk5hsSIm6-AeVmQTJSYkeqt8lnSNPVQejmzFu7mg30j3CcLv9YigIV5BthZ1MZSNl3LqD3Y5JZRL6kKwe995LMO8Jcge6TuYyzD5Y3u00NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=vN10R5mNHTYAPU8UA8jvinyudY8NGBdK2qakAr3KCfnAPRFPenlkOQSSA77HN4PWtKPt45s0xY5ZuTF70_Gv2oWHqBA2k-j0nbNYUwR-iLiGkm0xtQS_PVVaBQDIjOPvek9vIkpi-be7-kfg6CLzRM8kb6tposMmsbbtKAT8vJvVVvHbm7sIoTJsSkBZ-x38jzIvcODaoNzw73fR4Oz8GU0gewOuG1KPiHcPOuUBHo7Dk5hsSIm6-AeVmQTJSYkeqt8lnSNPVQejmzFu7mg30j3CcLv9YigIV5BthZ1MZSNl3LqD3Y5JZRL6kKwe995LMO8Jcge6TuYyzD5Y3u00NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریستوفر هلالی، روزنامه‌نگار ساکن آمریکا در برنامه پرچمدار: رهبر شهید انقلاب به مانند امام حسین بدون ترس شهید شدند و غربی‌ها چنین چیزی را نمی‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/447829" target="_blank">📅 08:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94196c376.mp4?token=ViSrZQLh-YB4v8Oo2OkPNC8tvAt3ClodRVZyoJWbr7-5CwhhTumpVl_a1LrBVwmPDUSM5p3oJ2upwOUU3ckm2SdovjF0e_7fpfyr7eS3omqOChMlvVMY0-bam1xR8oS9U6shxQHWKPfJfz0wcP1Rtnyr4iEvXIk-IrsO2WcjJmJ5E50QqEj78FLi6-DSHxt8aPsFPVV5xeuqVcU1rh5Od8xwxFwsI0gavxTaI12MEnbQGD99K5XOnhjJ3aU91NgDSwHsN6bI5EdduiiPIMPUW0Ia_FRff687CXz5I525WuZojlWk4VbXq_Pp2nvv2Mktd86TUzoO1MMR5r0D3aV4S6tqlshxyxNwokOtWFOt-MnBq5jaI9zBoAt5gBE0QZZZc-FVroV-8ANyvwbSCsYolRb18Uc0nf5uK7foIJWDmTMr1ZLFGP63PNQVItDoeKb2wsOhKjJEjIVNpJIfh6DPNw7tz6U6_tut1Y1ozqybcJz2mi6uwJ_a1gmuV59wxZHFFmeZSnchKLdJoi1g1OgyeAKd1jR1IVjJ0Djq8gOSd92GsojHU5bL05_Jz0fcGWQud1IYr1RBVQYxlesXPgvXMwcCa8vYxieOYUG6CFvo8qyXh-ChK7Dz7vixvvIn2IQkukYuO3Xn00Az5UAAe3CFItn7hoRNQJQ4lWI-HYi0_gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94196c376.mp4?token=ViSrZQLh-YB4v8Oo2OkPNC8tvAt3ClodRVZyoJWbr7-5CwhhTumpVl_a1LrBVwmPDUSM5p3oJ2upwOUU3ckm2SdovjF0e_7fpfyr7eS3omqOChMlvVMY0-bam1xR8oS9U6shxQHWKPfJfz0wcP1Rtnyr4iEvXIk-IrsO2WcjJmJ5E50QqEj78FLi6-DSHxt8aPsFPVV5xeuqVcU1rh5Od8xwxFwsI0gavxTaI12MEnbQGD99K5XOnhjJ3aU91NgDSwHsN6bI5EdduiiPIMPUW0Ia_FRff687CXz5I525WuZojlWk4VbXq_Pp2nvv2Mktd86TUzoO1MMR5r0D3aV4S6tqlshxyxNwokOtWFOt-MnBq5jaI9zBoAt5gBE0QZZZc-FVroV-8ANyvwbSCsYolRb18Uc0nf5uK7foIJWDmTMr1ZLFGP63PNQVItDoeKb2wsOhKjJEjIVNpJIfh6DPNw7tz6U6_tut1Y1ozqybcJz2mi6uwJ_a1gmuV59wxZHFFmeZSnchKLdJoi1g1OgyeAKd1jR1IVjJ0Djq8gOSd92GsojHU5bL05_Jz0fcGWQud1IYr1RBVQYxlesXPgvXMwcCa8vYxieOYUG6CFvo8qyXh-ChK7Dz7vixvvIn2IQkukYuO3Xn00Az5UAAe3CFItn7hoRNQJQ4lWI-HYi0_gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از سیل خروشان جمعیت نمازگزاران بر پیکر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/447828" target="_blank">📅 08:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI8knv06OwwW-_lvT1wl2T9hWpt6WLz1eekHSoW72aHVpqjxbTnm4EC7vmgr5JDCsns5dX2JpM-H94GnVtrH3TW_cxzgRoffbS4-RGb3YppxehzZuBDpvz26pLG2f07vYS7B9aKWH13eGdTXmHDUppGNDJBc-d4rE7LHTaBm0ktpZVKRoBxnM9qNIcDRcUD6Mnbb7sT1ETeQrHRZZZNDk6R9UvL2rMQEmGLjByqN6CIt0VVjEMNI0MboKaISeg5QHTULX0yuOrtkfFd_hRAUcWYIc1_c54LpOCSmsZhQy2PQY_E1ufsF2sWKb_TOzxJ3uhmqMchvZfUdvVq0zf7Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL9bo-Z4b9dlTqlitGpk01S0nZPWYrzAQWLmFgPi2Yez3TqDIzhIdSCNSPmzifmiY9qopbftoLCH36D3rr3hL_1CyN6-GMmovujNsMQ3pkbP-Xq4023GP3xNJc544vtYiBPVwWllSlQiM2FWw3VfQyYyhFVQhoISg0Z9_zq--bIq3X1PUtbKuEl9kjZCHG6vJOGf7GdnK-EcmHokixQjbIL84LE_ireNI8hxfNZQqadPKBGOZb2nEPzk0lmwlmw8K8kHuNFz0CJ0n5x1Ar9Q1Rnxpgmd1yE2UmD0DcHFm1b923KW6b97h0a8PE-Eziv9lO5Myd9ztYtKTz-v31jHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adB2u0eHQNitoM8-cGQbwHxQXvnGTbz_X6oGtrNBravNYwZMWzkJAO7iA-ZGt6ysPQTl5xfI-UTtfgXrClcOaIYOcCuTl-sIMIjoWl6_1AeSoxq1Qj7WEbJgFjiQD0VhmU38qd6FQzU7yxqk4y6eLzaulKNUe-SfTQI-4CVgLyMDpRJqU0bytBr21UTBo_o7EvjzzkldnhY6U194cUQmqz8VKdOT_eWu-cPUR6djFLfoKdemUUELANJt3yprPcEg-7kw4OP-Ouzv8TkcITtp-2D0epDQ-j_50sQrszSak4ucq6GrGqTTdOw471u3SHB9AKDxJf8Cdo2gFzs2dvtxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPApEG3XmlwaShABq3hEqHuklQFd2GaS2xtlVpChO_cGgYcsMlD4Sd_lho-NxU9RgMeAXUtiJk4s0LvhQ5mzHfO6zlj-XpLGzLW5N3nzzts741fUPjFc47y6CSmPwmIWLWbv5bWuhNRgCFc1_ge3TqicynW5b7l641wtNDp-WCWmJQEuv3yNSXbz5ytI4KVSWmUfdN4MX_BU2B5OFKw8-sM033q7PG74IhPm3t_vhPxxuY8rh6D_bG7E5U0TNf6UPQwI-hDvZQNPCpHlRxtRPXF2P_bNgNbiTlVd0gfdBez6HuwKpiOf16ZV6kdASb2DUitMl98Z-anspzw0S4gS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2koy7K7wzWvL-Qz6TpCVaCemYmke7usYc2zcxPABhsj5HSgeL5mn06QeLwxtY_yz6q0-IwjSN8xPrCowiIhQpBsgGCdeI3IxNJ5YToUvdW3ETex8_FewOX24BuG87ZmZUSB0UWJe_IiYrV3vtCbe4aY_fSMvMyAwSDib2L-ltKlVODlr6QoctCENXXUajxkEX5OVopPoBihH9Kk1VGByaR35LBmfpCOAEl_9mlONWSh-nERv-CZKp9Fjisl9RRtkz4NykuJ-JRDbg0ZXLpk1I4jgJm5_t4MWRjT0mmatVhS35DZ2NQpbND7cKjl6z3b3CMRm4Gu0J5LtWEpbkHYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwJU43YGmafVg86ci-JWRmK7jWADD30rGrFiDhwSxIebDR44o28i_TgVyI9ReIa9yAjDofKcAkjw4ew3jvt9j8fEokjOwdm3yA_LP_t29V9RE3SvrpJhRxDk6OD9J5jIgIG65OvJqbs9zal9oo1ZwN1h2RL8TdBZ32blreBEupUUfzE8_kCVSsfi-VyYDkBQTEJxTiCIuo0G72n8z2FFaYJIx6fwzYUERxouy2_g0DMxDtpEHsFlUAmsgCJB-xKCZuCazGbp4PnZnt21wT4m75zsbu8w0CzbWm7T4wp1X-unmB4o5GUuYg2e19Xopv6DBlTDvTQ2BPMipSGriqENRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqS8Bhx0IGQK8ktQfP9q1Tz0FLTCRWetg8Z5gBEDz97eV-MjPwVeR0LTSC5qgH06UyTze_ihy0iMtDegPHOhUyqWhgfzZSmrZ8pMcNRz7WWeLnfEuHmtmR6am32rXFdL6D-Bn_BPSZrATFhDTRX4l75hDx2e6lX0xFbT4apCFv6jvoVetV9L7O14g5Msj8DmXs-NdzgziuSeC3766q7SwZrsQGjcfS9qFqcw9eGpneWBBNTix6rimoo6aOV9qQoO-1RY8cQ_wxZ8ZYHC_s1rhQjf1TpCxBPvW4oWMFSL9hkL7T-CzHPAh7mgO63-yxJaRt75p-y8oyzXGr9km5IQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DL_XT9kpXq_ztUQ3JR63bzGlokO1krXt6s-9I9oTpQeplDzZfVdgEvqMT5MSyOmH90JF40EBjvZMLhZIJrIwea6-dZq6Yit4E5sR5OCObGrzMxHi3fiOyrrcoplfOYokd_efLgHwCs5nQlJlOgNz2sflBmGMadpa4_lJVOjk_4l6P3_zAQ1I-RDACZIeKSsqdLx3ZydlDG2adB5WK63owG74K_aArl-nOlVtA6cxpxbPzMw_W76i0qAACdMAKHgzBlA6bkt8ZIktbmVnslIkw5um2hYVBYXGDoTOZOkBZJp3Y0gR-dL_SqJb57va8M6YdZPfBS4t1EP6RzWUa6L6bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های هوایی از بدرقۀ امام شهید انقلاب در خیل عظیم جمعیت مردم قم
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447820" target="_blank">📅 08:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مردم در مسجد جمکران و وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447819" target="_blank">📅 08:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
حضور جمعیت بی‌پایان عاشقان رهبر شهید انقلاب در خیابان‌های اطراف مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447818" target="_blank">📅 07:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHrlKU6IZBZrPZiQyWmFwqMYha1ZF_ilS7UhtqNFlrm6J6KojX4kKYXbq9YfCPx4XKUkJ0VNKqiZ2TgUS50Ol2rcA4bvf9HN390tKLtEeDUlQEq4FBy4hBHhydeNkHl68eTx4jSV-WMqbdufhgAM4byiteiWwrPxusyF-Y9NZqTwJKRFjI9WUS9aWyesuiIEInxa7mDwfavO5-TtN-v7xLeaCCOEF85nWKHuk0Gnrb21msITlmR9oUM2YMU6ATiBzmmiA7QtbmvZFeszZRnFEGE3j8gi-Cae77wn82RLB04VeGCb53ohTp6wTnHLYWpEincrnGlVihX3U75osE2YTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgfT7CZivwVKHa91bM0x69G2jb_96X-0llXhynvP66apFnSDSyEaJtCCVBPilOK_Sr6Frvh3O2lIUKUqGGOmjfE3hIUArPeByYR2xBA6ECsTIPSsqwIDLZZg4yYy4bJxR4f58Pymbt16BW-dBB_n5pvzGXIOlvm0Z28hDuW4LKxdFMfEEnCsdfK9y61s0tn0vDX8MJ8EF7cqSJ4RbtkYav13gFn6V3f8y103ypDhEY8XesY120WiU89moevZxTq-CewFyO7m5AnEKXWYbQjDKRnZ2k_Kfq_auGLjGYa6DFOyC3gAiiIKmlubOKYKFNuCiPCC6jmGhVcelODWN0JYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cWfaM48W0sNmSfNpTN4pbZlgsZaCzx1cqtfMXAJnz342mAK2o5RQI-QgOQ5WYG6zWomdD8nV7ZtdUygEMTYzAXrEff-ndB5YDrLW_gav-g55wTKuHSR9O_sJFK_0ZYu_UWrjlKZ11hqB6v6k0h9pDgwQuu25g6RsAhG0TAdgumAH7oYnOGVOazjKSpd68EBPoa27-Qb6gg_JxPU82r2vAozlA37hL8XvFMrnPP5k7zINjj3QyHEXL0FyXPRUxGamgzHUfiV4xwy-HUXNauQbYvw2XyAdrVxOtQo1ydn5i4RC3wltJmVmNqTfoB4s6Z476y98-jzqNeQmgwrt1Ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZdB8E7D5-gs35Y_rDz1555SninCW7tho8gyxiVdC0kxeqSpfZTLl4E0Cp8hCM4egB9Eo-8P1IJ6_5lOKUxzuyuS_FsZYxhIkw8FSGsZdUj5a8uH3mBgY07DyPDfPPEpmysBaEvNEGScL0uy4ih79D2o_MazCJMy2eyKII9Jls9GRGam8hqYwG4EirJ0X6uGu24NWe_r2LjpOR2HppKL_04sNOGbBARwBT0lBF9gsv2mCrTtl4VK0aKltuYrDz1-m80nzYcMuCrROewk7vVZZMfFdb_kvchOyxCqp5-zIUllNc3FwdIs4ZDEWEPKrY97tvd3MrPabaaEqwkH8zxnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANUigSwW_mkfzvI1xaAwzpQMHDeV2u1PC3IH9jgNBBYK3Jyw7RLELsmZA6zT7bT5UunHqJ8AidF_fjI-SYqQrN4ejIjMP0TjfumJHXN-2yVmuitRiMQHUkjOZEm9xFycoHA0nso9g5xF8dXgv3fV6HkWLJl8Tr9sHqwB_TMSYZNaBRq-T_VdwqCAVJgwOrXrAid3ggH8HtR75eDh6Rylm4cslbpHf3yXA9VjFcFzzoFmofFmDV-_fb-hy-NQUIljoEwlTeEgD16P4sb9X5aj8bIcJTkxlDgcP_iK-PdSXmuMLn-XcWJ5NAmzYT-UHc5k7BAcJvcU5e9AlCUOFBDEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7eVhWVGEh8kvykGQXrClkkhQizy58MsPM5TZuorm7xGcS0Joa88ylsN19uMD_yYZGBofUDJMQb62xR0r4MIF__RH8ugELiNy7uoACdg0KfZZuq9X0X13lGjGcm772a5TMM9dStooKgNoQL4H8Mt_DV-mmpzlgcqepREPD6bokpejxxHjo1F7q_LzZH-Lm7QFztE4NnslTNXOoEPZdyDN6luDrZn550gsNNEXVe0UuoTHHKZFcFYenVPNAi0YaFVqBQ6bo-mHbwTGfF8dNAEaY_2F4Y75qCtpD7Im7DB9rXXIsC-kR5MjCBUL6th5-2FQD4MtIbJQPSRZES3X7KMdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز آخرین زیارت
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447812" target="_blank">📅 07:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8-eSqXSBtmq82Fgyxro3nN7l_qoNPv3WWirXmcgeR_zTu8qJ7CyHiVwXzdOwHilSWA9l5lZp1fjoWNI_Px2C0Jw1bb6ot0g9Xn67DZsYKgWghNRtKy_DYzsk46wwNrQ3MmAyZHVMWfUCFc-T9YcPoypAGarh6Vva-HLIsNviynzZurosfOBQZ7BUs15HWCPrFx49rQKLn5Tqcr2ULChEpLaVkQCgxYLTNABF2wxudOOW-la9TYU_Uyl1e8QRKVwTmlOzGvJwnsiXfNsY9tu3RXCFSXP6-F7N9UaUjFQGHTCihxxY4An9dP6x8sMDzoFsrB00_FmCYt-VmE6IXcyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور خیل عظیم مردم عزادار در مسجد جمکران، برای اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447811" target="_blank">📅 07:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش بی‌پایان مردم برای وداع با رهبر شهیدشان در قم
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447810" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340788de5.mp4?token=pwWnOuDlmhMSPL1tehyeyQoxV8W3WX-vIoJBLNELhmA0YBiKWS5_LyeExu_-61XodkjuAiOS-eGeRmADmiRWdGpK4AGDT9rhrM_4LkxgdFYZkpHE93Y6AbY6Yh46OGrIjVtPChD_GTZHp-aIyTv6IW4L6qlV4QtE1o7m6VIOKq5zlEG0CaVTLT2xdbjLgUukzNYMzBNgCO8qtreqlIWPLuvtx7N4moKc5OD_3BCX_kDVX4RbUTOPWjX35kKvb_eE_m9SVbTOY7fWWcaefDLPwIm2Yd0SxqL2leo2wZqy5UN5qXHCLMkZk1YloARH3ejkD7UtE74ta7JHo4bZ1VYRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340788de5.mp4?token=pwWnOuDlmhMSPL1tehyeyQoxV8W3WX-vIoJBLNELhmA0YBiKWS5_LyeExu_-61XodkjuAiOS-eGeRmADmiRWdGpK4AGDT9rhrM_4LkxgdFYZkpHE93Y6AbY6Yh46OGrIjVtPChD_GTZHp-aIyTv6IW4L6qlV4QtE1o7m6VIOKq5zlEG0CaVTLT2xdbjLgUukzNYMzBNgCO8qtreqlIWPLuvtx7N4moKc5OD_3BCX_kDVX4RbUTOPWjX35kKvb_eE_m9SVbTOY7fWWcaefDLPwIm2Yd0SxqL2leo2wZqy5UN5qXHCLMkZk1YloARH3ejkD7UtE74ta7JHo4bZ1VYRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم تشییع رهبر شهید انقلاب از بلوار پیامبر اعظم(ص) قم به‌سمت حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447809" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447799">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SykI8EZPoTn-74wjN5n5VvzuUQzFVSotXdkqAUWc5sDrqz_y459oHXol-geT7N_x1Dw4y0Y_HE9VwlLD01ionoNzc772zA9FKkTxgpt4zwo0du_hJYgL3p-iFwgkHSOhGDztJ8Xg1PqkuqjWiZOnnNpmXB5_7T83EJSqQz389yhw8zEP-QI7masXWEQh8XtVVIcwHaZusxHNtPxWoTqHSm_v-gOhrecYoBkjcRVRbpHH62fJeAEo14RYSSl7Oknqn9WWG4L_Jtrs8LWae7lWRHMTiQ663zioS8x85NxQRTseUxVzEeZvB794cfApsW76vHqwwHnw1bn7JihG1gSU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvh-ttZAoxUmkez3Z2SXVDKsgTSXwBOV2FPS97fOir_koKO8Pz45pbsTaOHs9PMQ_bUk70myXJwtvJO4ODbL2EuL9fTtsb3wEnvxfa27chdqkOuXNbAMZbyyal3flt3aM8fda7gKDEvQssCzlslBSylThIVMTahyolqDgBsHBNlA289-WP1U0Y4L_d72izHaJyZWJpM5RqQ7OpPnGyoP-9nPl_K2VKKcgdOdSpFgTQ5Zjl9zhfpx0f5PYxk79_a8c9t8WVnkcWFBv6R__gPeOTKNvCQu3rKi0waEnG9llLDruYl0Z6cEM1xEAyE5xhvFgfJSkdrm5BJxiWHORAxYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSpNBjLYSPoGYqfjsKSf9pl3sf8sf9nWgKmC-TM8bfHP_jYULDe59ATgt_YdXPPbxtg5qI1nbl8bMBwCmIGU-wK9RHzvUFDGTiywFvmj9RQ6gwgf6Ys3iSzyaZeu1nlUl63FsOtaajJIts2b4OBwWKnzlTvhG0MhI3eScAq1ewHqS5unse4snLssgZfgayU7nRyHqRL2UVyORI-0maL4wynr_Q661EsdhOSnX2cmEEvqIEZxHdoXjGCwW-Z0oDH45sH9gkySZJSllxiqCa3QhvQSuyf55QRYMNLgFEg0NFRhg3Y98tO5h_9p9rIBIcTS1BhderZkB7plBOwwCie8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7gc2XQ4mm-vbaZs5p9Z1yAa29IFDyPEujak0FSRV3nI0Vve0ImPiIrVNE0zRUH2z7TxWXZgVLgXi9HFOV_cNDgoSUFqfVQ2vl98vZcirRJ9J_3f2gACRuLVAraSBu7HuIGKuHKreA8rWzcU3CGuAevR75igBn827QKBp3TM-h7ymKDnECPTRuBoh1wnsHbjlplrRjJX3nKPdGS8DPQIKEAKhBCZdg0_pC7d5S1qRP-BM3J1PFg4UB5XRz3S2e8-8VUA5cZsNQKJBtkR8SwOkHZQcNSx8-KzNbpT_qLd7koq4Yz8gvCHFu3Y7QdHLoFcfBI6UkO9LzD5oCQWwQwX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P50nrgkVVGKVPqjPw-bvXnJBid4eaZukePlQPaEcVV5tRuO03ddauz8nfCNzHT1xODH3_RnOq3B64ZdOwbDuIwGfkdWTSId6DdLFnTbZKPp6TL-NanmpbQzP4zmiVztZ_TU1K0zU3VCo9cxPTMzhvi4C8ZRvJoG9mSzc4cjEAd2CflU9VzC3pRDhKW65qDgxei5oCq5TQmOfZXUaCzfPI5wsRlKCM8y_KaQA3e0h0ShFVLlwLQ6XJ95ngQCf9BOTehvVa6EK_ckURXMpkVRLAi9VvjskiZo7HcXi907QzYnJA1nwMbsv2JwokwHYdswWYN3T6WmDJnvSxzHTTPggVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiT8f4Q0Ewk1ihCFB0nAunWGkpBGJvnDY1wot0ypqgArS_MXbm68_ixtGPtPZPweLVBmwlK7trD1-Bz6MiSdwDI35Pw0LILkFNMxhojPGMvP72o0kPzJXUwPMUS6M2SyoOH75bDOvqOI1HrAA4xVd3_ytgHVIS8yB3IiZ1asf5kXyMa8GUb1LvCGU7D4saxP7vsPIXhoTVjiLZSAo0Ad3DkYGcOH-eR2bK7Xghcv5V092zGHEhpBe_btkUUik9QXxknBovVibJdSN3npZCk7hOGEM1I3-iGHoa1LkGWmj4alOKMuND-nVX8Ed415LU4CVwOcukXTTsOpJ0aKeEmTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtFxuQVaiZpuey_gwEo0A5M0ap7DgCiWVwJdXWEapJERttkHJKRoMjsyPxusk2KmeX0J0XNwiUwKqEXSQJaXICsl9WbjwyujdZNc1b-4kH8-22dxXaUZR4UVnjTNkVWNPZwqNWv94o1JlLmZNxNlds2R0lvIwS8xOTiUgbGjGdUDQXeUhZgjonwYr5IP3ATWdN68lNmdafzGUJJK3TAIjCsa-pw2hM6E7AIYzpsIWGsLaK3gXXef9M6RRpiJzpgrZluradDlwjrMvmOZxG7FdiAvskXkU9XrW00lFFfg8_M_5j6SuaFy8GaXBoz18vFafQo8YNqebyDui8VAT_ewaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focqv9SIWwUYDjaQgAnCiWXRdiZNKvUvtw0A6jO7Tl6DrCnRaWlXlDQ29G2PI9QFkQY7dY67dS0tKPAK2N7i-uODnq3CVFinnSEV_-TYjL2S6S8gEvDcxjZshOJZrp0JjiJJliMxHTuJJLIewaerRwYdf_sx0fsChrEMrHhHFptK9ZCidV1bA5YAjgW0WIvBI3hsldSsFdtiQJJDWkTWVKnQn-fitTCYxIPIXIwMxaa5YgvOwfX1xLVRkhNtuTpwjy5pVUjPyzp8NuPIa1w4rFm5MEvsLLPvluLe_KpdcpYtrdU1jwIvv2WHEX5hbrpE90hx1eyXEKJv3VSGFYkBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFgl1-H3AN4htTW2xCQ-Orwc7vrOlLgcMx2Hdg6zDKhwl8i35hAE9MDW_Xl37NejV37hXNQrjpFP8BvAd9i4BarHqDiHC0i81IXah3GkeSobwrLtgf_SnOlHpu3nVbPFEfq0HeOQF3Yfw-ac5zqARNASPsMaXeyJdySAuTTnAVwi9hiTOCwr3RieiMDRwOH8cKZr9ihVv4FETOW0dbuH8hU-mTKwxKdYoHXVppT5Ygs8NPjLNDLaTRxQp3pZGLyDmyDLOS4YQj88_GiMsUmTqv_Nw5y-VHYJoSeQWX13fENogqY61dRpV9Poi3bgbp_fXFGFrM3Zs4H0bRl5EXnGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCn73dKVqD5RoT41VxorqvnGe5QxacvrSSQJcBOue7HXoj0zdR3sa1LsH88xomTU5h6iAGJ5xdqkrw52_zucv3uWzahRDHUfOL6KMNnDlWZG4wguwKd2VRAxqJ-rOkUv3fa28QdKo8nke-WnvyWxrGPzT2GQL7MKt-jG-zXReBf0jT5930XcewWr9N6swOaVNNCkGdf3i7Feh5KhBk16J3dOzUye_JQhmF0B-zFbP7tZBJ642FD0F42jE3jqcXO4ldNAuFjclE7U6spY9NLBdPL9emO_aXURkjjUXh-0fAw1Et6r_GSadswzwBd6NRReTBrNHdRy4F2hjqZbUXrmXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیل جمعیت عزادار امام شهید در بزرگراه پیامبر اعظم(ص) قم
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447799" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم  @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/447798" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447797">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/447797" target="_blank">📅 06:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447796">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در جایگاه وداع با مردم در مسجد مقدس جمکران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/447796" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ الله‌اکبر زنان شهیدپرور در بدرقۀ آقای شهید ایران در جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447794" target="_blank">📅 06:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان بر روی دستان مردم عزادار در مسجد مقدس جمکران
@Farana</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/447793" target="_blank">📅 06:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb7089e92.mp4?token=jrHSdKq0-NyiD54fLggdvRA9M80MSo-Oe_ulc_k-JyjXT4fIjRLGxA-kkLqUrSzIMYzjKogVM8cHydloqMIsKo8t-LsIm9TE_Ctb3zgEc5QupK4jYMpQ0dV7g-IUuFIZ7MsapEbwnvBnihKylJLrskFKmh_zQ6RmvmQiRmUDNZtylKHb7ptn18mOZOJ06_oZ9QJjjoJvEUaCL4GxGSO4xwUtMMlD_57EHWk23n46KbxhAkI2bvuKsuJzBKS5yGa5Egvs6EXIoMwxCxtjNWvKUgWqdrPwgZMHsMP_FZd4mdGu7ySn1Ilp9evWEhzl_2fY7--lkYk_QyhJroeZEpF_GR-IwAD-0sZXp3zWNtauKmXMZFSr3JsfBynunnpy7cHg1VymxRjqQkR8DsBeYD3phSmMb0eAthU4dnYsZEdRFxXouJkQlHf71oDqlDJfq5vtfrNEJf78aSS1lahir1WObKWiETnZPbar8FIDuTzU_BPNIM8juDKe7M0W-1Xgza_YFtAaeMm3VjrtNx2a9sR36RuahBquSoVCZE74_6Ne7fKMznoEwNzkLrAVc4oVXceSPEIi12AkFAgnTrmhJquvd92xE6NgH-XPccZHPU0XsEZCCWAVCq8JImsZaG18lZROw-MKQKTZ5dxukwIAZYtQgGgvdWBL9_sqBWzJUATwxU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb7089e92.mp4?token=jrHSdKq0-NyiD54fLggdvRA9M80MSo-Oe_ulc_k-JyjXT4fIjRLGxA-kkLqUrSzIMYzjKogVM8cHydloqMIsKo8t-LsIm9TE_Ctb3zgEc5QupK4jYMpQ0dV7g-IUuFIZ7MsapEbwnvBnihKylJLrskFKmh_zQ6RmvmQiRmUDNZtylKHb7ptn18mOZOJ06_oZ9QJjjoJvEUaCL4GxGSO4xwUtMMlD_57EHWk23n46KbxhAkI2bvuKsuJzBKS5yGa5Egvs6EXIoMwxCxtjNWvKUgWqdrPwgZMHsMP_FZd4mdGu7ySn1Ilp9evWEhzl_2fY7--lkYk_QyhJroeZEpF_GR-IwAD-0sZXp3zWNtauKmXMZFSr3JsfBynunnpy7cHg1VymxRjqQkR8DsBeYD3phSmMb0eAthU4dnYsZEdRFxXouJkQlHf71oDqlDJfq5vtfrNEJf78aSS1lahir1WObKWiETnZPbar8FIDuTzU_BPNIM8juDKe7M0W-1Xgza_YFtAaeMm3VjrtNx2a9sR36RuahBquSoVCZE74_6Ne7fKMznoEwNzkLrAVc4oVXceSPEIi12AkFAgnTrmhJquvd92xE6NgH-XPccZHPU0XsEZCCWAVCq8JImsZaG18lZROw-MKQKTZ5dxukwIAZYtQgGgvdWBL9_sqBWzJUATwxU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض آیت‌الله جوادی آملی هنگام اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447792" target="_blank">📅 06:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=BSdKKoqptb9cj8kuBplZwouAUeOalPs77lEbH_XeobYAIWLuKiGE8RalpxK-NcoNJkLcBvWFJvMJIvoaoag_mosOcd6coq4KG8T_yO0NfpYTNoRW0SSbPoFSp4Lnts0Dy-FXES__gA2uL7S_znLCXIqiVJeiTuNV6aZlipdJOZw1vZVUl0LhBzedAc0NqxUHI3zZSldwLAKZvL8xLT5Y0BdAmDnWw3kaMdMPdNgCCiHWxxa5s7Pz--z6cK2N_4ehn0DyUhso_O0CRxSQQjPEObOLO7tGB-sJKTXzigL3zE2jR-GWTXWkE37Q2iHZTQz3LWWkVjad7KKEehLWsQwjyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=BSdKKoqptb9cj8kuBplZwouAUeOalPs77lEbH_XeobYAIWLuKiGE8RalpxK-NcoNJkLcBvWFJvMJIvoaoag_mosOcd6coq4KG8T_yO0NfpYTNoRW0SSbPoFSp4Lnts0Dy-FXES__gA2uL7S_znLCXIqiVJeiTuNV6aZlipdJOZw1vZVUl0LhBzedAc0NqxUHI3zZSldwLAKZvL8xLT5Y0BdAmDnWw3kaMdMPdNgCCiHWxxa5s7Pz--z6cK2N_4ehn0DyUhso_O0CRxSQQjPEObOLO7tGB-sJKTXzigL3zE2jR-GWTXWkE37Q2iHZTQz3LWWkVjad7KKEehLWsQwjyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
طنین انداز شدن صدای آقای شهید ایران در مسجد جمکران و گریه‌های بی امان مردم عزادار
@rahbari_plus</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447791" target="_blank">📅 06:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5340ada419.mp4?token=EDEs52QUfK6Alpd-dygLRYJvmyJnoKKhFdi_HCZqvasm3sFJUyvs6K_qW_7P7IXrK4SPY_b59LwDE39KmoOHpQ2igwdiCDYl57iPe81T4LjpydfkMSy9VRwhEITIbYbElroAPA2NJNdjWmUMI2Ylim8mhnDesh8r_lhmffoKDdqu1vGwQRQ2rB_XxNoMsyvPOamYifatx9admboiOim38uCf-x4rh4GReun-VxIlt285mH7PFYV6p1j9X7XBcHAVSrlq5L1rRLUrFy_QPgxGWuNNTvvJt-ibZCWAenQZhRL7bZ5KCJGlnfpuW7uMWAcjBRb5tJgrhhbFjLpPu9b_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5340ada419.mp4?token=EDEs52QUfK6Alpd-dygLRYJvmyJnoKKhFdi_HCZqvasm3sFJUyvs6K_qW_7P7IXrK4SPY_b59LwDE39KmoOHpQ2igwdiCDYl57iPe81T4LjpydfkMSy9VRwhEITIbYbElroAPA2NJNdjWmUMI2Ylim8mhnDesh8r_lhmffoKDdqu1vGwQRQ2rB_XxNoMsyvPOamYifatx9admboiOim38uCf-x4rh4GReun-VxIlt285mH7PFYV6p1j9X7XBcHAVSrlq5L1rRLUrFy_QPgxGWuNNTvvJt-ibZCWAenQZhRL7bZ5KCJGlnfpuW7uMWAcjBRb5tJgrhhbFjLpPu9b_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامه نماز بر پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/447790" target="_blank">📅 06:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان توسط آیت‌الله جوادی آملی در مسجد مقدس جمکران  @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/447789" target="_blank">📅 06:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d90e12057.mp4?token=FAdIOYo2ckZDY8DR8pDlwp-if1YWxiKl2mSaUPN8Nk1Sh9m8kA8hEZO9Yfp3Z_SyVRrOexbNG15aqscZB3kIXatB2W2tQDLZ-GcVHIjPOFf85guM6q2RqeroikBJMTxf6z_Ov0eK7bO6t9_sV51Rr9UsyECloJL2IzoI1AbqcpRUH_LB1G2yMZ7Y6bNzzSYQxwRSRle94er217d8-rWAXI4OG_S_xx9HklQLySwR95h4zwXKnXZMemMmxF6EV-7mnlJZd-S8HyMYtNzUAnyMY8de1XPp64b5_ufU6JMHi7aQYnapprwTLyliFbszhzOWNNFr540SUP4dnHdQjwDBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d90e12057.mp4?token=FAdIOYo2ckZDY8DR8pDlwp-if1YWxiKl2mSaUPN8Nk1Sh9m8kA8hEZO9Yfp3Z_SyVRrOexbNG15aqscZB3kIXatB2W2tQDLZ-GcVHIjPOFf85guM6q2RqeroikBJMTxf6z_Ov0eK7bO6t9_sV51Rr9UsyECloJL2IzoI1AbqcpRUH_LB1G2yMZ7Y6bNzzSYQxwRSRle94er217d8-rWAXI4OG_S_xx9HklQLySwR95h4zwXKnXZMemMmxF6EV-7mnlJZd-S8HyMYtNzUAnyMY8de1XPp64b5_ufU6JMHi7aQYnapprwTLyliFbszhzOWNNFr540SUP4dnHdQjwDBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان توسط آیت‌الله جوادی آملی در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/447788" target="_blank">📅 06:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23086ebf39.mp4?token=kOfqVkO8IcCHrKhCaY3ktSodBBhJCvf9t8Gsa-IHcvxy3lmt0F0rn5Z0bS5q7RIJa3BFFwL74j_UL0cetOWNn04S8AfafawHYdeFL8uATUxKN4HWyDmvfRP7gJsChbSQiqX-eGswabQI4Q9C8KDOmwvJJNg-L1ZMlB2fkp4efYRdtC-_vqhgIToiOV5Gp9ZltvZTpM1ZQSAoUvY2bBOIjbO4rnt9yHEgTBb_IiB1P9yyHix0MuLMDBFxFvJBG1LXUzFZaBkRmW3soo-tfEtkK7r4i2QTARSlnhy4AWYi1jz6wgDlnKyOas5vl8at5yQVfO3Dl9ahk1mAClplkdYmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23086ebf39.mp4?token=kOfqVkO8IcCHrKhCaY3ktSodBBhJCvf9t8Gsa-IHcvxy3lmt0F0rn5Z0bS5q7RIJa3BFFwL74j_UL0cetOWNn04S8AfafawHYdeFL8uATUxKN4HWyDmvfRP7gJsChbSQiqX-eGswabQI4Q9C8KDOmwvJJNg-L1ZMlB2fkp4efYRdtC-_vqhgIToiOV5Gp9ZltvZTpM1ZQSAoUvY2bBOIjbO4rnt9yHEgTBb_IiB1P9yyHix0MuLMDBFxFvJBG1LXUzFZaBkRmW3soo-tfEtkK7r4i2QTARSlnhy4AWYi1jz6wgDlnKyOas5vl8at5yQVfO3Dl9ahk1mAClplkdYmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقال پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان به جایگاه اقامۀ نماز در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/447787" target="_blank">📅 06:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de8818c62.mp4?token=RFInRdd7rkt-P0uPPnwDUTjHzEpqKjc2fQ2EE6-7rICVKl9BQ2ZymdghQad2JmYBS1jevbAm7VYks8Pb4KckSAUT6AKSGWBA7wM_qoFa797LQSmol2UL10U9w_N8F3Yca006EX6bb6tN1AjZCq-h_ILWijAbwPxMt9eRlmAUf593y5PPYKYelI6BZ33W9F_v_qncY0m1rzTNZgL5OZknzrvWXFI4ts09KCRZn8meCPL7WRxNEd2Rf8ZmA1xhz3ykmaIQHsmCGInWWCviDplYIRocK_xtCOhE2nykfOabLN85mPU8xVuz9oUNlQwlIFAIzBsg-cYtw6hOwqfUFTDRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de8818c62.mp4?token=RFInRdd7rkt-P0uPPnwDUTjHzEpqKjc2fQ2EE6-7rICVKl9BQ2ZymdghQad2JmYBS1jevbAm7VYks8Pb4KckSAUT6AKSGWBA7wM_qoFa797LQSmol2UL10U9w_N8F3Yca006EX6bb6tN1AjZCq-h_ILWijAbwPxMt9eRlmAUf593y5PPYKYelI6BZ33W9F_v_qncY0m1rzTNZgL5OZknzrvWXFI4ts09KCRZn8meCPL7WRxNEd2Rf8ZmA1xhz3ykmaIQHsmCGInWWCviDplYIRocK_xtCOhE2nykfOabLN85mPU8xVuz9oUNlQwlIFAIzBsg-cYtw6hOwqfUFTDRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت فاتحه توسط آیت‌الله جوادی آملی بر پیکر امام شهید و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/447786" target="_blank">📅 05:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=B6fBPysre92nrnE-Hs6VHIPD5rSwLuuViwFl3yo31O45Dgc2P4QOyM5ixKMWwttL-76ir0vcSeUrsKXP-H5Y04v1FrGecdDWZFD8-lKmVFXfSF2lgNyEzoCPAxZQ5GLQse00TxvpHlBlC_FBnvTyiVIODPuJgxhYlgbda6WTzecEDTxPwpM6TcSanFH9zJm8ejwTD8VZQye7e1H1-y1RoBX25IKKomEM8KwxcLtr6uNPJ5eViRbpn1-r7YPyrI0rr8vKjEr5ErF0tfAjHRNiTso8cilJs-35MGg_r8VbgA4ZnX_ohDiXWvu7qzq83h_xgGeyMlc5DiTPC2f2cDSYfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=B6fBPysre92nrnE-Hs6VHIPD5rSwLuuViwFl3yo31O45Dgc2P4QOyM5ixKMWwttL-76ir0vcSeUrsKXP-H5Y04v1FrGecdDWZFD8-lKmVFXfSF2lgNyEzoCPAxZQ5GLQse00TxvpHlBlC_FBnvTyiVIODPuJgxhYlgbda6WTzecEDTxPwpM6TcSanFH9zJm8ejwTD8VZQye7e1H1-y1RoBX25IKKomEM8KwxcLtr6uNPJ5eViRbpn1-r7YPyrI0rr8vKjEr5ErF0tfAjHRNiTso8cilJs-35MGg_r8VbgA4ZnX_ohDiXWvu7qzq83h_xgGeyMlc5DiTPC2f2cDSYfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع حجت‌الاسلام محمدی گلپایگانی داماد رهبر شهید انقلاب و پدر زهرای ۱۴ ماهه، با دخترش در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/447785" target="_blank">📅 05:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8907b298ac.mp4?token=VekDSk6j1GvkPc2V_JvgffTy1dV5TXWvT_whVVJ4aCd2-SqlT56260LcaCoY_sW0yE0k3mn7QwpUvCq3_aSI4uchWky6OKoY9MmMcHJ0bmgWO7HdOOWOaSadEE1-SFQkB_-2u6iZL8Kl_pVJnpmLhRDvab3vYWI9yik0ui3JcLrXCDp3rUBwrBb__-SLKb6TEQlUm4xUyLXeA-YO5h2XGLDe8Tt-lV3BinhUkvS911jMkxUjdfGFhBjkSjjeypgU0u1nTIiu-5YXMVK74UgbULCyTOLRevsTbQK_iuzJOcM84D0822Qd8oqvC6zol6JfW0iozsNBaxYfeHF4i-9mhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8907b298ac.mp4?token=VekDSk6j1GvkPc2V_JvgffTy1dV5TXWvT_whVVJ4aCd2-SqlT56260LcaCoY_sW0yE0k3mn7QwpUvCq3_aSI4uchWky6OKoY9MmMcHJ0bmgWO7HdOOWOaSadEE1-SFQkB_-2u6iZL8Kl_pVJnpmLhRDvab3vYWI9yik0ui3JcLrXCDp3rUBwrBb__-SLKb6TEQlUm4xUyLXeA-YO5h2XGLDe8Tt-lV3BinhUkvS911jMkxUjdfGFhBjkSjjeypgU0u1nTIiu-5YXMVK74UgbULCyTOLRevsTbQK_iuzJOcM84D0822Qd8oqvC6zol6JfW0iozsNBaxYfeHF4i-9mhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آقای شهید ایران به مسجد مقدس جمکران @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/447784" target="_blank">📅 05:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHRG9TFm_Q_VyVQqAehqhMFSd9ugMSv28MhGxLSncgvutpWTGL4plsZL9qZvY7_kpLGPgDP60rd-wBENxcIAvTwFQ_Y53jC397TJeSQpFbkSsD_tLwSGNzkTNL8_vhBxUVsNlghVPV5cuKTrogXlfNZ05iHWjRzlc9hw--OLho613Xuk_8mp8tNqd8mhhydxqb5v1bveYo__N8w-F26OhmGsVtxv_wwUfE6AEeEjusi-Nm_Br3Vzf1146IRGve4ptxAtDYJ_Aa32IC4auEjs1njnlbHt4LJlcuCy50uRa6klowKqQ3obdBzwdnjZzp4Q_rKSbuksaIVxRKQefSMsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت ترامپ هم مانع شکست آمریکا نشد
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
⚽️
بلژیک ۴ - ۱ آمریکا
@Sportfars</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/447783" target="_blank">📅 05:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c706552831.mp4?token=kv-uvC5_xD1aFI_nyfbq6hZqxx04LaASTbzD-si-l8tyEfCUh5HMOnyKF1alKDzr2gj9edP1RZaXMzxAzl0AgG_m77dn1Osfm-NxMSCVQDJa_ADHrTCzwYTRLS4uHj3Wt8FEMs2_61Y7Ea0IQCmA8DGv7KiKDB0X6SazcJEffFlKDp8DCsz33wgR-OZrVmwqaymb5NAE2K24ph8WTjYZMzJoM6_4L4LZXBBR9T67vllNjQ6Xi18xnv-M5fmH33eZD38CgYyXH5UH-BZbGGy3Gep3Li7jfuoUiYoGqYJ_JmGyDe1O4JTKOK8XbqkJARMN6dQ4vWnY6WJ9YbgMqJjUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c706552831.mp4?token=kv-uvC5_xD1aFI_nyfbq6hZqxx04LaASTbzD-si-l8tyEfCUh5HMOnyKF1alKDzr2gj9edP1RZaXMzxAzl0AgG_m77dn1Osfm-NxMSCVQDJa_ADHrTCzwYTRLS4uHj3Wt8FEMs2_61Y7Ea0IQCmA8DGv7KiKDB0X6SazcJEffFlKDp8DCsz33wgR-OZrVmwqaymb5NAE2K24ph8WTjYZMzJoM6_4L4LZXBBR9T67vllNjQ6Xi18xnv-M5fmH33eZD38CgYyXH5UH-BZbGGy3Gep3Li7jfuoUiYoGqYJ_JmGyDe1O4JTKOK8XbqkJARMN6dQ4vWnY6WJ9YbgMqJjUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آقای شهید ایران به مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/447782" target="_blank">📅 05:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da69444ad.mp4?token=e7cYA-S7DoNrkdF2-T_Y4D8TSD2xyD3NgABCbZv0oIw7zrTikdoFPSIKovdI8Qg9yIm8vD6kL77VCmALjkYP4eWNfTJ2mKTmPWrpdxm5Tbv0Sl9pY8nGUzhiJj1djbd_8EAWHaZTtvDB1xO78OXHGBEG9XJXgIibS1Fr2QpIcqgiPMBVU2QzPa-b7tsEOY7Qz8OpJ7hhGti3uxYwAVo969BY2IjLoOMKmspG8q6L3r-PfhylHaktW9FgUdAz9CEj3K0HwK2i8hqXzSLrPKVR74FIpjXWP6dWBXs9wjQoStFAZ8qgbJeD3jG5j4KtzYaLzdb1tpDx5l0ngNjVWEkR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da69444ad.mp4?token=e7cYA-S7DoNrkdF2-T_Y4D8TSD2xyD3NgABCbZv0oIw7zrTikdoFPSIKovdI8Qg9yIm8vD6kL77VCmALjkYP4eWNfTJ2mKTmPWrpdxm5Tbv0Sl9pY8nGUzhiJj1djbd_8EAWHaZTtvDB1xO78OXHGBEG9XJXgIibS1Fr2QpIcqgiPMBVU2QzPa-b7tsEOY7Qz8OpJ7hhGti3uxYwAVo969BY2IjLoOMKmspG8q6L3r-PfhylHaktW9FgUdAz9CEj3K0HwK2i8hqXzSLrPKVR74FIpjXWP6dWBXs9wjQoStFAZ8qgbJeD3jG5j4KtzYaLzdb1tpDx5l0ngNjVWEkR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت‌الله جوادی آملی بر پیکر رهبر شهید نماز می‌خواند
🔹
کمیته اطلاع‌رسانی ستاد تشییع رهبر شهید انقلاب در قم: نماز بر پیکر مطهر رهبر شهید انقلاب در شهر قم، توسط آیت‌الله جوادی ‌آملی اقامه خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/447781" target="_blank">📅 05:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266863d78c.mp4?token=J3W5_7uh97VTmD1NK7wffCavM5oX7KNN7fJJKDH8h1JtBc5Ah-SrVKU76YbZsBvS4xKtphrb8EQosdBT8rcSZcnp-PVdsWH06IghLWeoTSPuEOhDI_umYHT9Akzx0JkajeDsh5cx8V0s1BZ1fN1yLFWQk4OZRLMuDbthrW-SnrOEGM6yLvNbQmFiXxr-VLMu1l8goYewRbF_s42ER27KGbYvgj0_Bp7T2wDgIABao4xaMwR3saqc8ZbtDiahO0VsgOkdF4ST6fwDLJowtkDotFC_YZQjgdH_1cMKFEHA81lmrYFihDyPqXvpJjCHfOyRk5b4PlVH8R6wvbPIVeYN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266863d78c.mp4?token=J3W5_7uh97VTmD1NK7wffCavM5oX7KNN7fJJKDH8h1JtBc5Ah-SrVKU76YbZsBvS4xKtphrb8EQosdBT8rcSZcnp-PVdsWH06IghLWeoTSPuEOhDI_umYHT9Akzx0JkajeDsh5cx8V0s1BZ1fN1yLFWQk4OZRLMuDbthrW-SnrOEGM6yLvNbQmFiXxr-VLMu1l8goYewRbF_s42ER27KGbYvgj0_Bp7T2wDgIABao4xaMwR3saqc8ZbtDiahO0VsgOkdF4ST6fwDLJowtkDotFC_YZQjgdH_1cMKFEHA81lmrYFihDyPqXvpJjCHfOyRk5b4PlVH8R6wvbPIVeYN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور خیل عظیم عزاداران در مسجد مقدس جمکران و خیابان‌های اطراف
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447780" target="_blank">📅 05:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9a17b8ed.mp4?token=mHWMDagCEGnMLVbOWL2hfgUWVIAFcO-OZQ6_la1uhHFrGybmgPiY2sq75SFwljQ7t0BPcX5ieBpQ0ziGUXfO3pXLqIB8RvXLmw4A6s74QIu-eEcOFaVZmZv9UCkC_kN1LiHEPDVUNd4k8IjV7ZQDziTee5k8xQWRHf65zqBCfAASXhDWwOLhcp4rxeJUrTxtCl4uzWMVws45B2Yg7YGpVk66YZerFmbKkcq1OVxIbEK1uwdBx1zkcL2tQcgZ0DkkT9oqpF4fzBexTHjuOsr2LxzbKjqcSB8be0Ab1MAIsFvfruNrRC9RyE14p3xWPLjrz57Iwuut-7nuVYeA1k2B0iTLyeH5bjMAC_8kc4xewdeU1VsLglkIHO7kjThq94C18AM-7gdR64nWStR81lZnuSzrwOCFkP3y0BGGS1wXIM8WIloI7ZJRnFqtxzjcWvHLuFNKJ31_K-5qaIapizQCuC322Z4ZciCnggt8YqQPazLJpT_6IP-S7Ju8EqG-luDzEoByPEHzgp6HjB4IO7Uz6pSGv_J28k0nOwm40_RqNcji328fL1Y77JV8tmHVcsdDwkrFb2NvhU0f-Mz1vWEqlzRld-Ltm0n66z-qFS4PEwen8aSgV0ZlGNyz_QKYOEMvjQeVuaagxJaYzkn59Rd96pG2Q7s9JIYjw3P75geewUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9a17b8ed.mp4?token=mHWMDagCEGnMLVbOWL2hfgUWVIAFcO-OZQ6_la1uhHFrGybmgPiY2sq75SFwljQ7t0BPcX5ieBpQ0ziGUXfO3pXLqIB8RvXLmw4A6s74QIu-eEcOFaVZmZv9UCkC_kN1LiHEPDVUNd4k8IjV7ZQDziTee5k8xQWRHf65zqBCfAASXhDWwOLhcp4rxeJUrTxtCl4uzWMVws45B2Yg7YGpVk66YZerFmbKkcq1OVxIbEK1uwdBx1zkcL2tQcgZ0DkkT9oqpF4fzBexTHjuOsr2LxzbKjqcSB8be0Ab1MAIsFvfruNrRC9RyE14p3xWPLjrz57Iwuut-7nuVYeA1k2B0iTLyeH5bjMAC_8kc4xewdeU1VsLglkIHO7kjThq94C18AM-7gdR64nWStR81lZnuSzrwOCFkP3y0BGGS1wXIM8WIloI7ZJRnFqtxzjcWvHLuFNKJ31_K-5qaIapizQCuC322Z4ZciCnggt8YqQPazLJpT_6IP-S7Ju8EqG-luDzEoByPEHzgp6HjB4IO7Uz6pSGv_J28k0nOwm40_RqNcji328fL1Y77JV8tmHVcsdDwkrFb2NvhU0f-Mz1vWEqlzRld-Ltm0n66z-qFS4PEwen8aSgV0ZlGNyz_QKYOEMvjQeVuaagxJaYzkn59Rd96pG2Q7s9JIYjw3P75geewUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها در قم پرچم خون‌خواهی رهبر شهید را بلند کردند
@Farsna
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/447779" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f137e1068.mp4?token=lnsygPlTCxwesnYCqFJNMZ25h8RHEFEm2ygmr5hII6LSZ1AySIRTTaEtmnLekkvEf1jv_GNgj2ralLfpn4TkLgppGCZT4hihn0Ae9CrGdvXLxIsndPKv55MBLhSG6b860ZYjCSLuwRWHZYx-RiQyFb7IrRt55U0q3Ix3aNsVUnKNXvf9DOMeHx3kUG4ncI48tVw1vyxT01WTwK4c15tcXYV0KTQpn3gQ3cHH-CAUJLcyfvtWi1bFruIB3SZcYnl99_AtoaOzi5D9MVSZqHnVb6PtyImUhdPB8V9cIhfUY-CCypdSTOsknNmsjihNlQqBoCs8Aixcjwo4Aqtyy7AefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f137e1068.mp4?token=lnsygPlTCxwesnYCqFJNMZ25h8RHEFEm2ygmr5hII6LSZ1AySIRTTaEtmnLekkvEf1jv_GNgj2ralLfpn4TkLgppGCZT4hihn0Ae9CrGdvXLxIsndPKv55MBLhSG6b860ZYjCSLuwRWHZYx-RiQyFb7IrRt55U0q3Ix3aNsVUnKNXvf9DOMeHx3kUG4ncI48tVw1vyxT01WTwK4c15tcXYV0KTQpn3gQ3cHH-CAUJLcyfvtWi1bFruIB3SZcYnl99_AtoaOzi5D9MVSZqHnVb6PtyImUhdPB8V9cIhfUY-CCypdSTOsknNmsjihNlQqBoCs8Aixcjwo4Aqtyy7AefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما از لرستان آمدیم، برای بیعت آمدیم
◾️
مردم هم‌چنان درحال ورود به مسجد مقدس جمکران هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/447778" target="_blank">📅 05:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1013a01b5a.mp4?token=AMc74iB2ICc740Wd-orpOGObk3b52MNKVqvQpGzVh-GP3R4PHwQgTberykHNSLd4QpyWh_nNKzQCcdrGikbO-7AM3HbqqlbTM6tYt-qQCRS2PvO3WOncey_0KSYZwmOxxBumI2ss1YUhonQjSmXX7uTUJGEbb-N_brZA9kWx-fRmeunwnmMKqjBUFLk7GkltdqsV2a_Y26QsB_7q0x0cde7isJFUfZX7XrKdqEZo5Y2oFtYSVttXoBk7nvjfPtOKu4wxrdVhoNStLHJjlpjE7xC7I2N4R4AJWUWDHigkmJCLUM9h1R6-G7eITc-S8sA2rFbNmjn5vf18Iy5AvvH2mGkYSngO8Iq2TEgFCdxOSm6FlYaBqXpLcpT6ocz2ym1bbmxxY4q_7iyrs7WZYGts96ObFxL_XOFqZmYCTbxDEk6uGzKOYgPZm9Lulaz3jExi6uMu7jxGOUFmVFBgTwPPAwjEOX3kYeld-6eCzRA6R9Qx7EaBLsMa40fQlsGwkIR9pdUKDC02C8m1Fy-7D70nPuIFuuR8aGMQxlfEEp1dWDifixnzHIjecZvIRE5zua98UsaoURdCuidT2cpMMND5HhmFyqfAWtaSSKao5_1x_YtDCr_EOErzE-87mrzGXjf715e6foLOF-GiPnN-mpMnqBE2nODv0GjRO8X0BYyQZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1013a01b5a.mp4?token=AMc74iB2ICc740Wd-orpOGObk3b52MNKVqvQpGzVh-GP3R4PHwQgTberykHNSLd4QpyWh_nNKzQCcdrGikbO-7AM3HbqqlbTM6tYt-qQCRS2PvO3WOncey_0KSYZwmOxxBumI2ss1YUhonQjSmXX7uTUJGEbb-N_brZA9kWx-fRmeunwnmMKqjBUFLk7GkltdqsV2a_Y26QsB_7q0x0cde7isJFUfZX7XrKdqEZo5Y2oFtYSVttXoBk7nvjfPtOKu4wxrdVhoNStLHJjlpjE7xC7I2N4R4AJWUWDHigkmJCLUM9h1R6-G7eITc-S8sA2rFbNmjn5vf18Iy5AvvH2mGkYSngO8Iq2TEgFCdxOSm6FlYaBqXpLcpT6ocz2ym1bbmxxY4q_7iyrs7WZYGts96ObFxL_XOFqZmYCTbxDEk6uGzKOYgPZm9Lulaz3jExi6uMu7jxGOUFmVFBgTwPPAwjEOX3kYeld-6eCzRA6R9Qx7EaBLsMa40fQlsGwkIR9pdUKDC02C8m1Fy-7D70nPuIFuuR8aGMQxlfEEp1dWDifixnzHIjecZvIRE5zua98UsaoURdCuidT2cpMMND5HhmFyqfAWtaSSKao5_1x_YtDCr_EOErzE-87mrzGXjf715e6foLOF-GiPnN-mpMnqBE2nODv0GjRO8X0BYyQZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازخوانی مداحی «باید برخاست» در مسجد مقدس جمکران و اهتزاز پرچم‌های سرخ انتقام یالثارات الحسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/447777" target="_blank">📅 04:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4cae73280.mp4?token=E3WDEzsvi-s4mrq0s3rVnEYrwjn_oZ6mTVK_zStkck51QpTkzSsfnDKXXs1OwEOtPw67lEfld5vaeFxqk2ldFzhZMKtJBI6IPm55RmRfYQqElhdL_I_AMtAxWHTKXubelLwGykb2pLCU24EiAHYNQxyoWU32vc3_jU9gDJfPVezMVett6GDYpzoNskphupa5BpDV5fGT5nbJjsBlflThxJA7BPWnGQlKIxazspBjpuUKBoGX9KnV6CTR3jvBUz9MOSdJ-Y9FL8-dK6FUsbPglFZXHb8wDw8HC6SWEbOuuBGLi9cG8vBBoOBgxWJUCrgvwwluJutVdwe6Tlb88-zETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4cae73280.mp4?token=E3WDEzsvi-s4mrq0s3rVnEYrwjn_oZ6mTVK_zStkck51QpTkzSsfnDKXXs1OwEOtPw67lEfld5vaeFxqk2ldFzhZMKtJBI6IPm55RmRfYQqElhdL_I_AMtAxWHTKXubelLwGykb2pLCU24EiAHYNQxyoWU32vc3_jU9gDJfPVezMVett6GDYpzoNskphupa5BpDV5fGT5nbJjsBlflThxJA7BPWnGQlKIxazspBjpuUKBoGX9KnV6CTR3jvBUz9MOSdJ-Y9FL8-dK6FUsbPglFZXHb8wDw8HC6SWEbOuuBGLi9cG8vBBoOBgxWJUCrgvwwluJutVdwe6Tlb88-zETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم، پایتخت موکب‌های خارجی عاشق رهبر شهید انقلاب شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/447776" target="_blank">📅 04:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در آب‌های شمال عمان خبر داد.
🔹
این نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/447775" target="_blank">📅 04:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaclkoNy63701Dqu6iv4hH0ez0i2qRD-irlFS0SHTe_GTVssQKiV6puBCl5k9LOjz77wDdxiAJP8H8yD_55qNBRHqAvdTlp1yD0_rNiJ4AGM65f4P9IDwG0IIw0kIvqVPUu5rXYs9SqQX4AjtFRtgDrMRUaUBNohyvz12uQUk1w_9O-DWGv7SsUyTSPdyCnNLfVAizBm6wvKPvGIXirqg57u_Fop1zYtJQ6Qxj4oh-nH4nBm2uC6Eh9HSQkkiPws--Eb2VostuUVT31csL3X7-b_zBa4RaQU53X_m6vmcf3nDZayUo0neONLhYdkUBy3Lk1W4s1N180a8M7OGRbfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حضور فرزند شهید سیدحسن نصرالله در مراسم وداع با پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/447774" target="_blank">📅 04:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef58706c7.mp4?token=AQ59TJ0HJMugA-hSmaB23NlgatH4rWZYhOZUTHPu-6ralcyt3Ue9gZadhT_upAJkXkBboDYn4jCqSC2LiDXZLsMUUyHTF9qgUTuiI4XUg5EhXLfL49kTMKHH7AU3UIMkmLRmWDIZw6c6ZEXVBTlWzcU5Wb8Gxhkvig8nuIljhwun-hjFxa_AOCmEnIHeUA2RnTBxZ2BWgAq0t5H0AE6IIy1tYmZFEr-GMdEVceO9VvHlBCpTwimoRcUCkXgQZs0E9zfUNfbNJDzWDTaN5exwt24HW0ii2R7JPQRmfMlna0qmC0TLz9PcWRcQ7h9hnp5x09nEtufQQSfM4MuPIc21PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef58706c7.mp4?token=AQ59TJ0HJMugA-hSmaB23NlgatH4rWZYhOZUTHPu-6ralcyt3Ue9gZadhT_upAJkXkBboDYn4jCqSC2LiDXZLsMUUyHTF9qgUTuiI4XUg5EhXLfL49kTMKHH7AU3UIMkmLRmWDIZw6c6ZEXVBTlWzcU5Wb8Gxhkvig8nuIljhwun-hjFxa_AOCmEnIHeUA2RnTBxZ2BWgAq0t5H0AE6IIy1tYmZFEr-GMdEVceO9VvHlBCpTwimoRcUCkXgQZs0E9zfUNfbNJDzWDTaN5exwt24HW0ii2R7JPQRmfMlna0qmC0TLz9PcWRcQ7h9hnp5x09nEtufQQSfM4MuPIc21PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مرگ بر آمریکای عزاداران امام شهید در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/447773" target="_blank">📅 04:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07b7f4c40.mp4?token=enMqnlH5pi7CqwfeLWKAY2nEDBy3aS9Tb3zHW7NyYtUvcssiq9b9ilm_iJeTEPcYZk2ZZGYI_w7lPzZxKJqlENSx2uqyH4fZBtqM5TQxfwJrKr8Cf7-yx1CwxCg3yjN4NkRLD9xRYu23E6h2wVxUHGLMoGN5DVGwc9Ix8mzqrIeSr2nGRAkOHY75b6kqZKFnEGAxEzKd3OYzSlDaO5oA1y6SC19TL0NCnidNsxANH9ecy-E4ccFUK8f4Cz0cBmbOn8K7PQ9RwLF1m3x9zsi_XXD-f009KqmPoQS_rKo4xqdEt5YbXOR8R5i3ekfflHhKL3SFyCiUcB3P0WOCnrwzKw_-bNn4f_Z51HfBY6AwMJPOf1IpP3zWVizvqvYLs1DLa6F650OqfmfK5RbNE_9brPEfqp-RnL7RdN8SXH87HyN1rtEkoXUzW6WZn4o-X98mep4EComRptDJvUuTuyX88zmEkJzuzXgiu8VYg2nHODc4jDJQ0Ap-1dqugNzRAyaSlOckL6oOS02bHyrSApzuEGhCnG1jBiFVfcTWrpRr8fraLPGpjtatiBkDpU3obI6QO4QmVLDjtqfl7Soc-Vd8N22LT7bBk1h8K6XxvWPzvmPaYG3J5G9OTT-9FQxIS3rO_rBx06TJf2zl-SBfIdDlltzQSJR67vBibp2KlEzt9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07b7f4c40.mp4?token=enMqnlH5pi7CqwfeLWKAY2nEDBy3aS9Tb3zHW7NyYtUvcssiq9b9ilm_iJeTEPcYZk2ZZGYI_w7lPzZxKJqlENSx2uqyH4fZBtqM5TQxfwJrKr8Cf7-yx1CwxCg3yjN4NkRLD9xRYu23E6h2wVxUHGLMoGN5DVGwc9Ix8mzqrIeSr2nGRAkOHY75b6kqZKFnEGAxEzKd3OYzSlDaO5oA1y6SC19TL0NCnidNsxANH9ecy-E4ccFUK8f4Cz0cBmbOn8K7PQ9RwLF1m3x9zsi_XXD-f009KqmPoQS_rKo4xqdEt5YbXOR8R5i3ekfflHhKL3SFyCiUcB3P0WOCnrwzKw_-bNn4f_Z51HfBY6AwMJPOf1IpP3zWVizvqvYLs1DLa6F650OqfmfK5RbNE_9brPEfqp-RnL7RdN8SXH87HyN1rtEkoXUzW6WZn4o-X98mep4EComRptDJvUuTuyX88zmEkJzuzXgiu8VYg2nHODc4jDJQ0Ap-1dqugNzRAyaSlOckL6oOS02bHyrSApzuEGhCnG1jBiFVfcTWrpRr8fraLPGpjtatiBkDpU3obI6QO4QmVLDjtqfl7Soc-Vd8N22LT7bBk1h8K6XxvWPzvmPaYG3J5G9OTT-9FQxIS3rO_rBx06TJf2zl-SBfIdDlltzQSJR67vBibp2KlEzt9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض دختر لبنانی وقتی از رهبر شهید حرف می‌زند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447772" target="_blank">📅 04:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6719732a.mp4?token=p2tR-TsaoE8hQFids-H3w6sunY5aDX9cO1hWnR-Ar8_MJ_bcPGFyI1Xpjg_DboD7vK2nrEjs5HJsudhoDAIUKP6SiLJ9h4nEX3dL2hJ5aPsGxgvZHiIFfHz-7A7fk5gXGjO1QQ2SUyj_jQ6Y_6l26m97mVYX-G-ZXVKH9QvKsdl4URV2Ws_dGGZSHmsHRXWhTj9RTLe9dlIUTzE6C3UfjfBmCS4VuVvjIkA-mLxuWXYWbbMe06axxs6xyW6Hpeq14Dyg-FgLdEyv4m-BmCnIEpjoiFnxcVui3hn1IwjQeRWESRa0AJ5m_qL-MyVNUZXxEn_unJ6fFcmJr5YQQEPGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6719732a.mp4?token=p2tR-TsaoE8hQFids-H3w6sunY5aDX9cO1hWnR-Ar8_MJ_bcPGFyI1Xpjg_DboD7vK2nrEjs5HJsudhoDAIUKP6SiLJ9h4nEX3dL2hJ5aPsGxgvZHiIFfHz-7A7fk5gXGjO1QQ2SUyj_jQ6Y_6l26m97mVYX-G-ZXVKH9QvKsdl4URV2Ws_dGGZSHmsHRXWhTj9RTLe9dlIUTzE6C3UfjfBmCS4VuVvjIkA-mLxuWXYWbbMe06axxs6xyW6Hpeq14Dyg-FgLdEyv4m-BmCnIEpjoiFnxcVui3hn1IwjQeRWESRa0AJ5m_qL-MyVNUZXxEn_unJ6fFcmJr5YQQEPGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تمام خیابان‌های قم به سمت جمکران مملو از جمعیت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/447771" target="_blank">📅 04:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6dd50ce2.mp4?token=muEJSmFltckutShxvJAm7PQHchaZvKK5Em_fJTnuAN0SsYFyQY6EIwKLYMxHfLK6hS3esJLQISV-XxS8goIEgfhL1tD6hPb0trDjRq26eS8OCFjLV-KYHmP1CkzA-AtYM3Azld-cqutYijjzXqG-ZScHwWQko8FS1pg-m2n0-na9JI4k4c6sdl7AOm87MjhLM3caLwdNBKMHLHnMw6GgQkjsCsQW1Kono6F3PGbdYEOzFZ6LoXW1OqFcgzStJytMgEbIuHKo8e70DbWqiPeax5LghpMmgubGiOnXA2jcnBH7aaRncijRQP3Qr3hEDFLEl7_Khgpk45FeE-VuJWd8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6dd50ce2.mp4?token=muEJSmFltckutShxvJAm7PQHchaZvKK5Em_fJTnuAN0SsYFyQY6EIwKLYMxHfLK6hS3esJLQISV-XxS8goIEgfhL1tD6hPb0trDjRq26eS8OCFjLV-KYHmP1CkzA-AtYM3Azld-cqutYijjzXqG-ZScHwWQko8FS1pg-m2n0-na9JI4k4c6sdl7AOm87MjhLM3caLwdNBKMHLHnMw6GgQkjsCsQW1Kono6F3PGbdYEOzFZ6LoXW1OqFcgzStJytMgEbIuHKo8e70DbWqiPeax5LghpMmgubGiOnXA2jcnBH7aaRncijRQP3Qr3hEDFLEl7_Khgpk45FeE-VuJWd8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید همچنان در حال ورود به جمکران‌اند  @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/447770" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74704832ef.mp4?token=Lniq_i3hLPGIsU1yV9mXkefbrS7S3o7wXYWmRCqbCeJ8SXrsu_equzAagXi0t0SDnB6VfOxkRk39m7J7v5ZTaCZ_QDNDTxO6F0ntA6C4IQ3eqC5jRfaV5mOWZpo25HdvMbMEzkl_29NoPBictFEA6l1p2QX_G7FjJw2nXcSC70e5JL6mV9ByIlMXGlgFo7Vy6L0J9YbPEfOkmatnq14T9d7_WCF_eFG6hiC_5r3yBYCTt-OvNTuGl8VqI6CUkn45rwIcP1hXqGV1A32qLbe2KbpqAhHOAz5SWJkFCPykYUASBRTx6RsMVAm2D-kcZLi8TLDJGKFpIdDCXFpsvWV8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74704832ef.mp4?token=Lniq_i3hLPGIsU1yV9mXkefbrS7S3o7wXYWmRCqbCeJ8SXrsu_equzAagXi0t0SDnB6VfOxkRk39m7J7v5ZTaCZ_QDNDTxO6F0ntA6C4IQ3eqC5jRfaV5mOWZpo25HdvMbMEzkl_29NoPBictFEA6l1p2QX_G7FjJw2nXcSC70e5JL6mV9ByIlMXGlgFo7Vy6L0J9YbPEfOkmatnq14T9d7_WCF_eFG6hiC_5r3yBYCTt-OvNTuGl8VqI6CUkn45rwIcP1hXqGV1A32qLbe2KbpqAhHOAz5SWJkFCPykYUASBRTx6RsMVAm2D-kcZLi8TLDJGKFpIdDCXFpsvWV8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترکیه‌ای‌ها در قم فریاد خون‌خواهی سردادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/447769" target="_blank">📅 03:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf812dde3.mp4?token=J85PrINIFbizFS2x0XSDETr3P-f5J0W4oNO3IGmFpXsHOk-DQm6BLovVdZSlAArvMpWYybLeMR8ZgeV3et5951ghntK9fGxP1EhW8A30Su5UJ_Tb40w6RG0ISsOgSlOUb9chYQ3DRGMyQi0EDOM3ur7Ut0JNPeWdmqwISM1inUN9TCoqtOQH8iKSYVZqbK8dFLY2phvS8k3Nbj9E__UQQFninqfQa4zeQo8xdqZu8l5xcrO385h2ddiM2Ak7jcRI1aNqRMM0nvK_21QtfmI6mBEnSCimDav8WkZK2TYe5qb3hTaf-LoEUuP1TrUEukHn2XRy4YPXEI1MIGDcuGr5m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf812dde3.mp4?token=J85PrINIFbizFS2x0XSDETr3P-f5J0W4oNO3IGmFpXsHOk-DQm6BLovVdZSlAArvMpWYybLeMR8ZgeV3et5951ghntK9fGxP1EhW8A30Su5UJ_Tb40w6RG0ISsOgSlOUb9chYQ3DRGMyQi0EDOM3ur7Ut0JNPeWdmqwISM1inUN9TCoqtOQH8iKSYVZqbK8dFLY2phvS8k3Nbj9E__UQQFninqfQa4zeQo8xdqZu8l5xcrO385h2ddiM2Ak7jcRI1aNqRMM0nvK_21QtfmI6mBEnSCimDav8WkZK2TYe5qb3hTaf-LoEUuP1TrUEukHn2XRy4YPXEI1MIGDcuGr5m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج حسین یکتا: وداع با پیکر رهبر شهید، آغاز مسئولیتی بزرگ برای انقلابی‌هاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/447768" target="_blank">📅 03:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0c2622f9.mp4?token=krVlI330chWo5x7QR-tCOLPoXyvxLpNWyf7A5NZCV_oD1JzcYdlQ15z9yEDKZtzkR0QyG5P_0GxGIG2NNsKEWjGkucMZ-6aAdW2DqKk7QydZzhIVGt8HV8CsU1CjnkmzSXZ3XYA3g2b1avDP-0zi_Dan_gniG6FvpUiONAX3s96ZwRSUrf-VYgpWXMkb2cvVlqo4cK0NkBf0iX_yTlfIZmVJih9lhrT7DWMxvLMnefucGCSjLjXtbvBaOw3jkz787H3QJ3CWNXx4oBHdIieXDgZBDEHsYZ77uTLdkYyGLGXbNaogSSjRX-k29aoutyhftbRv9iT2uFGisUp8-2VoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0c2622f9.mp4?token=krVlI330chWo5x7QR-tCOLPoXyvxLpNWyf7A5NZCV_oD1JzcYdlQ15z9yEDKZtzkR0QyG5P_0GxGIG2NNsKEWjGkucMZ-6aAdW2DqKk7QydZzhIVGt8HV8CsU1CjnkmzSXZ3XYA3g2b1avDP-0zi_Dan_gniG6FvpUiONAX3s96ZwRSUrf-VYgpWXMkb2cvVlqo4cK0NkBf0iX_yTlfIZmVJih9lhrT7DWMxvLMnefucGCSjLjXtbvBaOw3jkz787H3QJ3CWNXx4oBHdIieXDgZBDEHsYZ77uTLdkYyGLGXbNaogSSjRX-k29aoutyhftbRv9iT2uFGisUp8-2VoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِنْدَ رَبِّهِمْ يُرْزَقُونَ
◾️
ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/447767" target="_blank">📅 03:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d5020c7f.mp4?token=TFQY42ZpF-SkMSeCtiMURNYYYiloUYvZ0YLiLVXx2EfU6HlfIy_AusxdQdQrsbfCXCoukxM-uDN2Bn3ZjL3_xJnpoAmLYraC79yMGl7B7WF5E0pCRW8fNL6F9_mDnXYJkm0G1kS_cIBLwpH3CSKFoPwW8SlcW41VaQPmk0JGRk6_69AmwK6f3xlFkEIitCFxciXZsOWxnt9Ath6EEjFPC0bFf3kzGErejSbZPyAoC5Kl5Q55N3_q13rsNG5QPZNdsHN1PJdUqSfHk2s4ge30XHhqK_PmUAn_nlcHR9L_NqRrsx4ccoBXAba76fmRcPtE02GKj5Og2VlwhKLC4guvCSz7dCAd8pzta_r_HJdxz8zEk7Go6lL_CP8nsxUGlGsFa0tB5YtKUAZ2q2kE5Fz3lSq3-0luJH5HsY4ymkICOjTQBlxPondTxs_9piAK79jJ3ldSDyiGsDl6lQbZNPqLsSocE-SdwiqwTkvqy1n0Cmebx0g6iTE9Lh9Ts5EjthUjyIO6dVgI0hQKwpsLlZLbxE6z9Iupq7DtE8zxClQYmxp3DWn6TooYkriVxdENWlXMS4HM22IxrW0WtXJ2n1knb6TlWgeV3Nc_96gvF4iLrgKX_mUSO_3WRcV-KvXIe3BZMJK9Ru4L0oHNEnrcn0yrT0y5vLNpfZlubmcv8tyqKOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d5020c7f.mp4?token=TFQY42ZpF-SkMSeCtiMURNYYYiloUYvZ0YLiLVXx2EfU6HlfIy_AusxdQdQrsbfCXCoukxM-uDN2Bn3ZjL3_xJnpoAmLYraC79yMGl7B7WF5E0pCRW8fNL6F9_mDnXYJkm0G1kS_cIBLwpH3CSKFoPwW8SlcW41VaQPmk0JGRk6_69AmwK6f3xlFkEIitCFxciXZsOWxnt9Ath6EEjFPC0bFf3kzGErejSbZPyAoC5Kl5Q55N3_q13rsNG5QPZNdsHN1PJdUqSfHk2s4ge30XHhqK_PmUAn_nlcHR9L_NqRrsx4ccoBXAba76fmRcPtE02GKj5Og2VlwhKLC4guvCSz7dCAd8pzta_r_HJdxz8zEk7Go6lL_CP8nsxUGlGsFa0tB5YtKUAZ2q2kE5Fz3lSq3-0luJH5HsY4ymkICOjTQBlxPondTxs_9piAK79jJ3ldSDyiGsDl6lQbZNPqLsSocE-SdwiqwTkvqy1n0Cmebx0g6iTE9Lh9Ts5EjthUjyIO6dVgI0hQKwpsLlZLbxE6z9Iupq7DtE8zxClQYmxp3DWn6TooYkriVxdENWlXMS4HM22IxrW0WtXJ2n1knb6TlWgeV3Nc_96gvF4iLrgKX_mUSO_3WRcV-KvXIe3BZMJK9Ru4L0oHNEnrcn0yrT0y5vLNpfZlubmcv8tyqKOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات ملکوتی اذان صبح در مسجد مقدس جمکران، ساعاتی پیش از اقامۀ نماز بر پیکر مطهر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/447766" target="_blank">📅 03:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04737890b6.mp4?token=GFa96Nvfe3CMd4Lic2lN0EQKfqT2roLQrLDD9qvrAjtQpzn3KEh2UknIio1K6E8wzMFJ1Yjx3FEJ9_yf0R-KUCnTzL5zeklJPRizXxn-0AdSyt5EP9nqmqqZOXR7FuOU1cHcrJ9QpLgUZXa0yU2YIOUHN6_sTwNZYsU70Ph_SyEZysmTGTeEtlXxP7bw5nX8V_npGgzYcO_JQPcfGKwvGjt08EqmUHzHQtEVPyzOHonn5FBEsCjSmT8fhFdfRwF_fKK9UKhShZqGlZgTBgn5RuGwtJqQvT618_z1QTlU8JZ7g3QZtqtPm9A183mIRu4Tk6kqY_4fVMIMNUqrIVhwCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04737890b6.mp4?token=GFa96Nvfe3CMd4Lic2lN0EQKfqT2roLQrLDD9qvrAjtQpzn3KEh2UknIio1K6E8wzMFJ1Yjx3FEJ9_yf0R-KUCnTzL5zeklJPRizXxn-0AdSyt5EP9nqmqqZOXR7FuOU1cHcrJ9QpLgUZXa0yU2YIOUHN6_sTwNZYsU70Ph_SyEZysmTGTeEtlXxP7bw5nX8V_npGgzYcO_JQPcfGKwvGjt08EqmUHzHQtEVPyzOHonn5FBEsCjSmT8fhFdfRwF_fKK9UKhShZqGlZgTBgn5RuGwtJqQvT618_z1QTlU8JZ7g3QZtqtPm9A183mIRu4Tk6kqY_4fVMIMNUqrIVhwCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران هندوستانی در مسیر جمکران برای تشییع امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447765" target="_blank">📅 03:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_DtaI1kqViYMK1dPSEO_lGRPvNjYzqHYrauVW5fi_BzW44dE26CEuDUOsKGEqTka4uH0YvjCy5L-lR4u8hbOcFDtIrVL7DlM4pt2TedCnlsdVvqLkXN_s8C-ikRxEtT7LbgsJGw4QGdANAQ3I12t3RDQY_smYIxHXVNOD6GGVfg94eABWrREvZYCArKlI5rKarR3bLomq3ztNktuWrEjtK7qiFF6ruzR_cKsEGyorcNsnC_VcvPtZf2ixGhPzR-oZhwbtb4qGUIX-wqSqWu3rXImMwTplQMJgf8rMbnySsf9geoqygBEd4Zc_TVMfdVjXsNS6dinMz16CvbP8CX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در آب‌های شمال عمان خبر داد.
🔹
این نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/447764" target="_blank">📅 03:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773824177a.mp4?token=ZF_R7sl237lkFReJdkoY5yM7ea6sJuokm2Wr9JyuHIHb9Dx1adD7bWaOx6ZHovVZDmHpeCv1_FLnbkbJkkSZCWNW-j9UK290RgbGKCNSNyMLSdAZSv-QIdmMmEF3odSdLeVC3h-GgDCtl-usDKJ6SOqRm5rex0AqzWCOL3ZxyQx-oGJlPAjNWqED9Yo-2pn6MLEB5c1Oqcs0y754PU8XqkclywdUrLISA43cLoglgjz-NQ-24UA-2de8CYF9-SHCJ6S9wPC50Bzy0wQZSbgELRGgGg1gPS1B8TMqzL6xY8WfmrhXlAjF8qzqVGXmXDbDZvLY3rwwEjjkPStlnoWp5GuPOFEV9kEfWGBb1jnrO9SK1W2kmWrOEgXdOd0nspt7hntjFkGb39uq_2GA_K8JxvK0lGj7zOx3oLvYdmdQGiyCTZKnRJFLbHNum3mnFQMLm-nfIcimLM1EVhhfLdMkTQkMPUWzWoiSIrkI1nNHSw7iRgTPXUoFgmGA9s9H1x2WUjpwlpReHo_65gUbDkZRa47IEKEbDHj5LBkRwtbVXO9RiqdHlMUiqwkmC2y3w9fIXEjytA0UYBedtHT0vO4Wai7fqHID0Vj9e_s-bM125uuC39w8niQKOhzwMwh66nHSxyqo3hlBh79jWKpSHO94AuoaXyt2MTRXVXvcozu9d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773824177a.mp4?token=ZF_R7sl237lkFReJdkoY5yM7ea6sJuokm2Wr9JyuHIHb9Dx1adD7bWaOx6ZHovVZDmHpeCv1_FLnbkbJkkSZCWNW-j9UK290RgbGKCNSNyMLSdAZSv-QIdmMmEF3odSdLeVC3h-GgDCtl-usDKJ6SOqRm5rex0AqzWCOL3ZxyQx-oGJlPAjNWqED9Yo-2pn6MLEB5c1Oqcs0y754PU8XqkclywdUrLISA43cLoglgjz-NQ-24UA-2de8CYF9-SHCJ6S9wPC50Bzy0wQZSbgELRGgGg1gPS1B8TMqzL6xY8WfmrhXlAjF8qzqVGXmXDbDZvLY3rwwEjjkPStlnoWp5GuPOFEV9kEfWGBb1jnrO9SK1W2kmWrOEgXdOd0nspt7hntjFkGb39uq_2GA_K8JxvK0lGj7zOx3oLvYdmdQGiyCTZKnRJFLbHNum3mnFQMLm-nfIcimLM1EVhhfLdMkTQkMPUWzWoiSIrkI1nNHSw7iRgTPXUoFgmGA9s9H1x2WUjpwlpReHo_65gUbDkZRa47IEKEbDHj5LBkRwtbVXO9RiqdHlMUiqwkmC2y3w9fIXEjytA0UYBedtHT0vO4Wai7fqHID0Vj9e_s-bM125uuC39w8niQKOhzwMwh66nHSxyqo3hlBh79jWKpSHO94AuoaXyt2MTRXVXvcozu9d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری بانوان جاماندۀ دزفولی برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/447763" target="_blank">📅 03:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a66b0e84.mp4?token=giGRLswdvV7wx7fzcENNQO_xlQiKZljXzLo4Pu8qo-d4g_RxBnLNBEHqdBh1-0KkDKYsNFTe7QBjho_rafb9e6UKfvgkXhEtf_k8rPcLN1ptr6PT8W8bSGz1PPp5LVre2PyZZEn5l0yb5qt092pYysUx_CbpF08y3NIt0kri8mrVsOMxBJOK1975QQEoNgF39angOQJSvMhsNFPd1vUupuVZPJNWiXuJPY5BbJSaK3yVl7HpDxLziRH7rdAJ0qykvz9KuCNhw7ATiLBroJdCBWKNhzTAQ6Ehs02E7bvb1N0TuRnIzhXAPakObqVyRdZpWxIHwrOEAQ833GYWXOJycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a66b0e84.mp4?token=giGRLswdvV7wx7fzcENNQO_xlQiKZljXzLo4Pu8qo-d4g_RxBnLNBEHqdBh1-0KkDKYsNFTe7QBjho_rafb9e6UKfvgkXhEtf_k8rPcLN1ptr6PT8W8bSGz1PPp5LVre2PyZZEn5l0yb5qt092pYysUx_CbpF08y3NIt0kri8mrVsOMxBJOK1975QQEoNgF39angOQJSvMhsNFPd1vUupuVZPJNWiXuJPY5BbJSaK3yVl7HpDxLziRH7rdAJ0qykvz9KuCNhw7ATiLBroJdCBWKNhzTAQ6Ehs02E7bvb1N0TuRnIzhXAPakObqVyRdZpWxIHwrOEAQ833GYWXOJycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید همچنان در حال ورود به جمکران‌اند
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/447762" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9060ba02.mp4?token=qL_Rzfudm5v-by5DB0nc3zwjleYaP7f8KKYiyh4H90FKaUbuUfcGSFgxhCFwG9Oini6YhY0PUagJmZgqguCq_EZw1774IONv4gR9b70E6KQDUctrBtzOhfq1VnDXgAFyDp7bcAAltXxyWZe-jY-w0meZ2bLCkNIAWGbZxJ-Tberg-Uz0W4avQ9W3cwFB8z5YQghftqrXel4GuiwHo4VomOXqYYaFTKkebX9RjD_swW4y04jkFNoAFh5fL5WmYsahebflEvP1gtU5wG7qKpYuManr23VRzKjwfpFKWQmbT22A57Mlz0KBwY22en95F2jxmd1ZKwszJOlpZxIdRqDJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9060ba02.mp4?token=qL_Rzfudm5v-by5DB0nc3zwjleYaP7f8KKYiyh4H90FKaUbuUfcGSFgxhCFwG9Oini6YhY0PUagJmZgqguCq_EZw1774IONv4gR9b70E6KQDUctrBtzOhfq1VnDXgAFyDp7bcAAltXxyWZe-jY-w0meZ2bLCkNIAWGbZxJ-Tberg-Uz0W4avQ9W3cwFB8z5YQghftqrXel4GuiwHo4VomOXqYYaFTKkebX9RjD_swW4y04jkFNoAFh5fL5WmYsahebflEvP1gtU5wG7qKpYuManr23VRzKjwfpFKWQmbT22A57Mlz0KBwY22en95F2jxmd1ZKwszJOlpZxIdRqDJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ «محراب جمکران»
🔹
لحظاتی از حضور رهبر شهید انقلاب در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/447761" target="_blank">📅 02:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795c89354d.mp4?token=NCPzxSLzClud3GsoUuyJ-YHm5RaZf7xo_VMXnWXnWPzWLrSoofd1U7pS2wVyDvZV9ntNkQlY6KulpmVh3kKsqtFn06mFXZSXa0ozRtZk1snq7wnxxkFRIrt-DGiD1j43wRPmfTcWk0_TrrlIz3h-goZ0sYBOd9LiPTaAOhRR6D7EDG_VjBdWP2OTWyEcZVwV8PafHWEIH_wq1tFTeqo1yc3Mu2gIlm1CQmI0e79kwGc-AHnu0ygWyqLnie7kpLTe8FzkMQOdBcHvN9ctu9qxeOiH9sBC2ImI4gAQnkkPfgiJrrqmyQI0niHLparsTAWZ-LXfies018SQS3O4RB5aAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795c89354d.mp4?token=NCPzxSLzClud3GsoUuyJ-YHm5RaZf7xo_VMXnWXnWPzWLrSoofd1U7pS2wVyDvZV9ntNkQlY6KulpmVh3kKsqtFn06mFXZSXa0ozRtZk1snq7wnxxkFRIrt-DGiD1j43wRPmfTcWk0_TrrlIz3h-goZ0sYBOd9LiPTaAOhRR6D7EDG_VjBdWP2OTWyEcZVwV8PafHWEIH_wq1tFTeqo1yc3Mu2gIlm1CQmI0e79kwGc-AHnu0ygWyqLnie7kpLTe8FzkMQOdBcHvN9ctu9qxeOiH9sBC2ImI4gAQnkkPfgiJrrqmyQI0niHLparsTAWZ-LXfies018SQS3O4RB5aAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم عزاداران امام شهید در مسجد جمکران، ساعاتی پیش از شروع مراسم
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/447760" target="_blank">📅 02:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری زائران حرم امام‌رضا(ع) برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/447759" target="_blank">📅 02:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikuBquKy13veX30hmoCs9qusJBle72PsOj6ijFGfqvGhliw-rAdo-xHXWZlRMinoDzcprsVeOwZN776nEWrFdHVcPUMnm5fPM50joHemAOuXMwcyTSC2N1e0jwrKeuVUf8oelCL9IFam1vHG0fcd209jOz5iK9v8nHOCSU44nU38eXCcbziybEjV6tcliD1IrpHIqiIJVYylgKDaugjF0XMlOoD9ROSEraSU_lvmPwsD2TMBLAhaN9EmCPjyuBjOtrB6Q5LRxFTXvT3DzgytNvYbV7aKspkV_yfxwhkSbIlnBBe7DDcChpxVLKftxBqXLAsQ3GfVf2yhRf-p1P6aVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس رئیس‌جمهور لبنان به ترامپ برای خارج کردن اسرائیل از این کشور
🔹
رئیس جمهور لبنان شامگاه دیشب ملتمسانه از آمریکا خواست که برای خارج شدن نظامیان صهیونیست از جنوب لبنان، به تل‌آویو فشار بیاورد.
🔹
جوزف عون، که تسلیم‌شدن به آمریکا و اسرائیل را به مقاومت در برابر اشغالگری ترجیح داده، گفت:‌ ادامۀ اشغال، مشروعیت دولت لبنان را تضعیف می‌کند، مانع استقرار نیروهای مسلح [لبنان] در امتداد مرز جنوبی می‌شود و اجرای توافق‌نامۀ امضا شده در واشنگتن را زیر سوال می‌برد.
🔸
پیش از این، دولت عون با
ارائۀ امتیازات بسیار بزرگ به صهیونیست‌ها
ذیل پیوست محرمانۀ توافق بیروت-تل‌آویو موافقت کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/447758" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qArV90BOczv1u-TOFJam6lslv7Ry84d-vRb0b3YCeDHZ6Osi7YuMKiXUmCqQIYQ9i1ULsrDegultl_yM8OhbHuT8Aa9pDwUgoQkGwy-75tf_0Klke81NlJWKqHpyQI-L9c9uLRfdCDFVDSHrbb62GtElzYB5B7M34yBkrd1i3bBHn81wZwEmT21eBHz9YEH5qlR_dPuVP7aZa56-S5Nu2tlk6zegg4Zy7y34wbIT2CHy65jB0635E3qLsCrMZkEDQpAmqbQcwY6GMjpy1F-p9LNCCI3CwwzX5BKNZVUCoJM0UTC7VsZfo90BIp9b2NJSxSYg79L2HA6hIeoP_Wp3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو: این آخرین جام‌جهانی من بود
🎙
کریستیانو رونالدو:
‏
🗣️
من ناراحت هستم، اما تمام تلاشم را کردم. این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ ادامه دهم.
🗣️
پرتغال قبل از من هیچ‌جامی نبرده بود اما حضور من باعث کسب سه جام ملی شد.
🗣️
نمی‌توانم تایید کنم که این آخرین بازی من با تیم ملی است یا خیر. تحت تأثیر لحظه یا احساسات تصمیم نمی‌گیرم.
@Sportfars</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/447757" target="_blank">📅 02:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ممنونم اگر نروی، میمیرم اگر بروی...
◾️
گلباران پیکر مطهر امام مجاهد شهید توسط مردم عزادار در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/447756" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447755">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/447755" target="_blank">📅 01:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زبان، از گفتن حرف دل قاصر بود...
◾️
هر کس، تکه‌ای از دلتنگی‌اش را با گچ بر دیوار سپرد؛ شاید نوشته‌ها، آنچه را اشک‌ها نتوانستند بگویند، روایت کنند. نماهایی از این روایت‌های دلنوشته در مصلای امام خمینی(ره) را ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/447754" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OduDiyp_L5jZJF720nfVH-T7TCY6AQox9qYCysJRDtR5Gfg1TlAH33tXxMJ0F9RfG9EyhIdh4GR1kESmGmTE4ZPwJiQtR9rWFEOCEg7IKpFmLaiU5K1V9HPmEYwRM_j0S0nusfYq_FBA0tKTf71bHy3cYMvykLF-fObSCM96F9voBnou6VMMWDMVZwg8Rm6KNE9ne4FD0AT3fzN8OuBV7rGfzR6mbOP5Y9UqqXxBpu2Y5Ngt8NdGSXoF4u7fFLBx_nEBhkPANIjte_ZIk_INuLWKurhRq4QGOww7ylDHEhdBqQu2JTrpZ4vv8kggT9p1hheq8nkHREPn-efKRKjxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی پس از صعود اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/447753" target="_blank">📅 01:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم  @rahbari_plus</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/447752" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9d3aYsnoOBwazn3E3ROahwqCKx_32tqfWfKcVJCF3C2_8egQY42TaQlmiHRnIInFe6ERGPZ9xxucGrzL4AoV6eL3nIBRhzoobNUnUijfvtGD-Hi83WkeZYD2sEyBeoZtdde3G3ENrybL_qcxmDZC-2tycOu9-6q0Vm9xn-P6vknPa1D5UmhcSyc3MT9KGiMwtksafVDmKG7XbxR49Fgpy2AESI5rXGJCv8wI0R13yr8BxnRzBFCcrWBsf_cynrD79rsjd-SN0N9tt6WWo5n-S3sk0i64VDzQFtnWzmf6-9jUxjK2nD4g86WJADmZXNJ00sqM2uVLQ2Umm9FN93tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استانداری کربلا با عنوان
خیر مقدم به اولین زائر اربعین امسال
به پیشواز تشییع رهبر شهید انقلاب رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/447751" target="_blank">📅 01:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مسجد مقدس جمکران ساعاتی قبل از آغاز مراسم نماز و تشییع قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/447750" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج جهانی دلدادگان رهبر شهید در مسجد مقدس جمکران هر لحظه پرشمارتر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/447749" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم
@rahbari_plus</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/447748" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/447747" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعاتی پیش از آغاز مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید، سیل مردم روانه سمت مسجد مقدس جمکران است.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/447744" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/447743" target="_blank">📅 01:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در مسیر منتهی به مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447742" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447738">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p48h0SsklRIKGxE19JOUR56caC0RxQs3acnewoJcGs5JU_imHo-2YMbt8VkKXwK8supk6IEGjObhprsN62GreDNbhu8x4qI-MUfDqoVYgS2WiH2KHsZ8-xHqSB1ln-hWKRJwQqteuINRD8ahAwlzJrAsLMBSFgNzFeA5UOMMm9ftfzEmGL9Cy0pH8ZSnlWtFBKBw1wb26PEZcniTLwZ1_TB8DRakZnTS2oLzPEkb0YV2bZqSjlJUsi-1C3AnVgAP-5E_p49xfyoQLBRLMX8wEj2S8854Y4YSnsYTwhf9liRUXv_7HCoZS0bTfjEg5rKm_hvot39CV659gubTy9B-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcXZPDm7Ozfv9HWkXdgKOGVAT3eRBc345Oyl3P4onxLELlvlUgZa9FSbwjbJdgHl-f58R5n9paI7Jqd8-P6_cogkLcwZR254PJD-6HgyAlpRo31aqz2K2Jf7LKwppTooz8r2C5xwCsNjRl55SPlRfVkKcI07xFgEcAle_tKkxIhFXhqxbaXQ0DZzwR2oOeKNgS_rP00D_FfjCKGjDsvTc7NTd2bR9tl966L1o6ywzmzuSX1S3Ts6HjFmBHF1VsLT7Hcm_6qf5c3uVVqbv79ixfMHfFe41KflYBR6E71TNyWIBEQ6DbYVuWv2NnUpXhZmDOf7BnWN3K93gtbn-wdMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfAABwvLl5DbbfsjiBRlWb_Uh-pBg2ZlpLxI0sarR_T7x7yujMZZLAoQQnkAkBNdNxSBcZqwoO0Jk5BwNGQySa668fQJHjHkxuiPpOXVz0jF8nxiMvBaj-VFznztA8j3SajeoQw_Q69CUweUPKYhOxlv0AteHuHm-mCJisFnXnm4xKQYMYROFYOq_9pRHX_ZVqZyJ6ZtwfGGnGcXRgUKTlnoEAkHOSggc7u9d6iQbT3kwZu90EnCM9IrJTa6HYUYiuO0U7hlXFLkgD6DsnwU2qG8LoJm8xNOQPh0ViE7MlJkprLPggBXYuuxOMMFE4_V9exXed5H70jsTH9hQ2YXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NulEDn0jEfZUuz7tbYRdbKuehp2lq_KXN5Mfvn_T2ClaO0bIrBpOYniv_TM33ZMlvFCT28l3ATQUCTS4FHN9oXICm-ldxOeeecL3tdYHJgNS9sMds91Yk1OUww4QKcBeEoIcwq8BiwkScilOS9copt8HEGsI5Iy4P4Mvtb5671pAL27DoAeB1Jm9oWPqZBKQoOpCUJfH_7pQmmfHQAoxv3xQBS34wjLn69dpF7xizL8lm773YLuPZpkaPmR9ZFgPqOhTBmviigQBHnAc5tKUauzOXJV2U4Cx7oeCMov937tNZ1d4DxLwYebOK7L8QNQ2xKBG9fnhvtWbExyygAGWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/447738" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwUuBY3ddvD0wcaBCpNojNyycup3384OaZoOtSt3NLyu7O0vXigVQ-QpgN9UW3z07O0X9HNOimQ7mvoJjeHHUa6gPWuUKekYPESKjCnzaYP5R7y5srFxBfkpMDzTD9iKb1zKCdrmclGD9a3nkrAWW3iNSPpFVrtCA4sjg9thND1Vbg2lAbbmSyq-TDZSTGNs88TD8JCvzqzoid8wvQUkfs9x5kdMB0gYQpNmUOhjhxx73UEoxJYixmQ7_-q6vYdDsl6_Xd6GdZVntkjWPC1Z0bLMS4qg-ZQMj6hrI0OQqgSkjxSCzoGOgprEMxKgIrQH7RYceeGhn58fpt5T1qqHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS606CWzhtUCb_48Qgj9enIcl-MZtcagkkEkZiQQ21bH_pwLMUpQuGvgDCcH8Ktk01lDIfK60eHiY8pG4sNA5MYeJagJJscOcGt7-Q-iJaumwUa0R_x6Hkd1T3nLbeoHygzUsz8WknebNDe0eJyJ9bP7EhG66cn2jrNjrpcz-74CnACoYHkztD0cx7DPqqkajwfot3Rcw2ETiEDUwf1k2928P_6PePIpUGrG3Fs__qwZ9O_lyggDhZzeSw_Oa47Eoc9FkR73mBjGJ_vCGP72vPImv86LIhbwfDsqQX94_nmJuGc99IF3V49iZsP5dHXUSfCPsx44d5lTSaAO-RkR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-vcZWDTZ4IE6SBWyaCIwMCnCum-0qTG2veZ5wkAiVVHlAp3B_G2YtAWPGxdzQ5SKt_eZ536DHlsbt_8WDOIHdZd_xU3F6CqQzxWVBjrtNsrdRBURUZY6ZwUet_Y2aH38Np5gyV7wnF5G7wHM8VzX9nlSqzDJI_owvGrZ_vB8wmJtDplc3j44QhW0jCTGJRUs9-yHhG0t_Wpb8ZXQ1VjzZcfx_BCoNBJwRhXhDw_VyZClIQ_lxk-O2sx8dMDKqYMm05lAgHN_Ogv96pVWHpNXNfl_PlI0xbjUO_l2xbfAcYwbIE8jb7qaBvfDJItjGCfN2Wu_ZVxKRW7Z2HjVI_jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQ7bvTI2EmF57X3ZtbYy589YmPhGokyJO3Ty-aM-DIxF6OAe31bWSd0lr-AAbxqRtw9vsfVlereSrznRzqIKIrSOKuOszT-DL3Umitey0sb8drcxHlITrMLriqAhT6KWqCVntysa-L3J7RBh5sqSsGL_FKb7zDSNAueeKf6TePm_ESBd3fjx9HY2RG7gFZOr6AUdZyl3jfnayCgbyvQRXSIIyUyi840bPGoyOv3vRa7xKhCie5fZpytqu4691wS9IsGMMNXxEyRgUpphYLOBvG04q81NClqDtCTXelhFobtyiSLwUXAJyVtP2v_fXGk53i1OtVJ2WKp4g_c_fRBZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoxzLU9mwIPzlvaPvmi_vAynq-7FWm20sYMK9Rexr1QbvCmvkRNR661baKnrE_rVsmCzJQo_I9NqAoxseUcTfDqI7P1RnkiEbwgDL4pi4fxvH0uSjBctOPcDyZz66BYunFxza2X9HquiQ4b7UD_zXLprzpaNW_zUuzkuSNo1MHXJm0DuJJC1kzxjYwPQrwvr_ukByAbXVUyczqyi6_QsEWqnOb_q7pofGaA6kx9AK6gKNVkKrZd55G0S6vPHEk5qT3-Tkslwebnp-Wfajbo2htVJFU5RGqmwteMCzLGX2LBGMTPG5CX32k8Je7XIQyIMqSO_sk_q2LY-WouHyM00XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kx9oEIYdF9KJPBlZVDUdImkyrF0X1K9c3ZCBBWPJvP6A8oUsOzfVV949jSubteSDVbW-xIbLjetDdVQF9bhYqNwoeVKl9uD91-eX2MZ0efXuZjD5qZopz2Zltg70mF_AHleuo6ObRk0_xsavCxf0mUWZJYHd98uHYwpdTZAPiLi7G-TkjssSYM4wGtPqG65deZUAeQb-0oIyXv-ttBBOXH1OpK7fz2SBzbzwDZOvwvbgSQ9Iv9rQzMJc3l20kiDYgIy2OXQE05tZb75iVra-HY_rhWDFOGuHVGWm0_PwNALjlHwEBRT1kH8ZuyF7dwHFq-wIuAjBI71F_CIzzn9-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOv4cZ1zIAn3KN9YPp-_G_CM56jDdPdpiYRy9jv_siFX5qE1PNztoLae_RP7iqoRBH8qy-kZpNuWZlMsGNi23E-hd9gmm89p-y_FxrMp3QaYYY500V1hmryCYu6fEODlydnKXpDIdYY57LjVU5Zv7n5jlFSVgAOiZ1dvi9W8OC4_ZkrQvqT0kfrD5VwEkGbMrrCuOnwLFNKf6EfC7m1dD36fvvWYyUWkDrLV0UUq-yrqFab5jQ0iRUr1uvZR_maxjK28JNAhhDx8RoOHOaEC0wWZdkuOWtTsvITzWInnvJaJhXCIgo43Z0mtRk8t568fxsa7cXJSQ1lUgtg_Zbz4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwa4Vvpq8Ti4HtpVYcxmUHJQMy9HJ1svUmfbwjdRPXANiIJ-KBeKz4cUvaFfrUKOaQ7OykWzE_mf3qeopmEPVNd6i3h9ghBlCOvqOBxk4Eql9mI1zPaTHuCU-KD5Zk26rkgX4XsA0g6ilSQG_X3y1zi7p1OX6Fje-i3bckfXNOMjlEbkaHGFGhV5jsXMrxSDlXiBpeITdQ3fIqm2waPoMqjBmp8vMg9IqDfs1l_81ViJNUy1k9LONrur03TFHt1BvIbN00EyjF7CRoIYoDhCCyNaFcRiBqcwJJeqxVmiUt6in8iZXZAuRE9aOEkGgT-TUUAb19Rtb42l2O2Q3WgpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icdUn6-Z0R-w2irvAew4f6p846X7TvEVz0uzGjvS3xEpkoUEGVeCvTradKGP2wubbOL2hEXo95tTxqUIuknzCetpCm9K3pDsqlwz0cJw_oQ2n8jyrzIo2ULNwqsBpGqfbXjHzoGzbjzPZzEsOZx4jMQwUNV0PjGfL9d3RcmsR1l-UeTUBmmUo4E59YpK-AZanQ39o-gx7qWs2U1uvdVWPm-ou4dHZtDiO8RYKOtotgBD-9FEuA-57Ttx47pfEvth80kqWGXv3GXs0vQrN6kiT5TbsdQbX5s99ycVNDXSPFLjg_ZLUiwX0an4ye_xJ75AGOlQ-hmT_2ojYZU-CYTC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnde7_VrF_fjt02MkJfHmYZSPm4msfZpOdtlSY0RIuhZhfcN-MELo7aS7GY10SX1H0-ciUCSdctXl6PTANhYB-SEmoc92REdbRfz8LwSSdyRxhqO1RTu2vG6H7Ew3CvxWs1BX1cC3Ao5JoccaKRBJmuevay5O1L1divStma1kPoXKDY7QFkVndaMUJjuot9qpaLBXZW4XxFTBXLTQIpB5GOOiB7CfsoOW_2hWNdbfQWp1QwxZf7DQDezy3vkYOWb6Cm4k59daZTX0pwGZ41LgXrLSZ3uP5SozFJMcLAiIfySqzczm_AQ8SuLMks-CT1S8o8JaNbwcHvHD0S3j9zMbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/447728" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdRdy7UAylsgedBtJFchDKj0w0yRButWQK711DNs4VJQ1SSqjDH-kk29lp1omIAjnV9GZr898MrrBjmntZho4Bfj1oYnYYflWFLRRo6yAZJNJWMeEcJd_RRt_Tz2OtjgxiXyBYR-EtpNA0LsLo_TkcttAv3L2y5bKoi_uWcT2Nt5MwVCzDjw2WcvqNTIJM-_DnzZzDkMG8YF2mgc6oXOjWG5VTcizEXrHrCFNPclx4GyLF_XJTCKyjHDlYbfGzGXYohRVQxQKLK1woCbtAlkWXI_j-lOR8o1adJwL3-8HFpNeUagilcc-0YuEBa_NLNMl_dPrt3PuTyyzo5mHwv7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تشکر و قدردانی مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران از مردم ایران
🔹
سردار حسن حسن‌زاده، مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران در پیامی ضمن تشکر از خلق حماسه مردم در بدرقه آقای شهید ایران، نوشت: جلوه‌های اندوه، خشم، حماسه و خونخواهی مردم ایران در روزهای ۱۳، ۱۴ و ۱۵ تیر ماه در تاریخ جهان اسلام ماندگار شد.
🔹
قدردانی از این وفاداری و ولایت مداری ملت عزیز و بزرگ را وظیفه خود می‌دانم گرچه پاداش این حماسه‌سازی تنها نگاه و عنایات حضرت حجت بن الحسن عجل الله تعالی فرجه الشریف است که صاحب اصلی این عزا هستند.
🔹
اینجانب به نمایندگی از همه دست‌اندرکاران و تصمیم گیران برگزاری این مراسم از همکاری و مشارکت مردم در برگزاری این ابر رویداد تاریخ معاصر ایران که نقطه عطف گام دوم انقلاب و شکست توطئه‌های دشمن است تشکر کرده و از صبوری و تحمل آنها در قبال اقداماتی که صرفاً به دلیل اولویت قرار دادن سلامت و امنیت زائرین بوده، قدردانی می‌کنم.
🔹
همچنین از همه دست‌اندرکاران و عوامل اجرایی و خادمان این مراسم عظیم که ابعاد بی‌نظیر اجرایی آن در آینده به ساحت ملت عرضه خواهد شد تشکر می‌کنم.
🔹
برگزاری چهار مراسم مستقل استثنایی از جمله میزبانی از هیئت‌های سران جهان، مراسم وداع و نماز تاریخی در مصلی بزرگ تهران و تشییع بی‌بدیل پیکر مطهر آقای شهید ایران و خانواده ایشان، جز با تلاش‌های شبانه روزی همه مردم و مسئولان میسر نبود.
🔹
امید است همۀ ما مشمول توجهات و عنایات ذوات مقدسه حضرات معصومین(ع) و شفاعت امام شهيدمان قرار بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/447727" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از مسجد مقدس جمکران، ساعاتی پیش از مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/447726" target="_blank">📅 00:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEUe8kpWR3akSeZjMr4LWPTvZGjaNSeAO_Efpt0QF7Fa3lCiPjNKrv2nzdo2jbI7Q5owFm6hwZLtmx9RRElx6YCnDqH6_Et9xOqnDdXOift_4sd6RDWO699EDmqfDCS-UfuV2iGevPPVfwbM851K0iJxK31V8uaDTBsDqrJJZjwXO61qb04tk4PHDPZvD4djBvIVIN9j4ltUnoLvKWKi1xq96HjCbCvHbkXoFuOMhCoMH4scFCXY4YSAOsNHOhr4Fii5pxG0G9bweoZZwpY-36MeM5q15ty3kiSvF2-bFV2N6K7ipfHIQ7pChJTwVH_IxnnEarcNIbQ653QI0mrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: لفاظی‌های وزیر خارجۀ آلمان علیه ایران، فرار رو به جلو و تلاش برای وارونه نشان‌دادن واقعیت‌ها است
🔹
سخنگوی وزارت خارجه: لفاظی‌های وزیر خارجۀ آلمان راجع به تنگۀ هرمز شرم‌آور است و از حیث وارونه‌نشان دادن ماجرا و بازی با کلمات، شخصیت «مفیستوفلس» نمایشنامۀ فاوست گوته را در ذهن تداعی می‌کند.
🔹
آلمان باید به‌طور کامل به‌خاطر همدستی‌اش در تجاوز نظامی علیه ایران پاسخگو باشد و غرامت مترتب بر اقدامات غیرقانونی و مجرمانه‌اش را بپردازد.
🔹
این نوع دست پیش‌گرفتن‌ها نمی‌تواند رژیم حاکم بر برلین را از مسئولیتش به‌خاطر مشارکت در یک جنگ غیرقانونی و جنایات جنگی ارتکابی علیه ایرانیان، مبرا کند.
🔸
وزیر خارجۀ آلمان روز گذشته در ادعایی گفته بود جمهوری اسلامی ایران باید هزینۀ پاکسازی مین‌ها در تنگۀ هرمز را تقبل کند!
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/447725" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خانه میزبان شماست
◾️
طریق‌المهدی آمادۀ میزبانی از زائران و عزاداران امام شهید است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447724" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
