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
<img src="https://cdn4.telesco.pe/file/psBNEYzGOhjKhtYICya7om-37gmzpbKANDXURoXRMeFfAEZF2YOyKiQNskRRB4_DMW3dHM6vEMbfUKP4ti3bVJdJ-FeKkP6vyipk4cSN8f-aNGSliXYFSCoR5NxhUoMff5U57Tf5jc6G_llnDMhts9NA88gBmDt-ut89zdeerCs8uAkSA9foawYYgmMNxLBW98nHK5lg1zZ9HqhFNqkZxbD9UhBgRwkh3gw6BuIrsZdEapD1hzgV9hg5ccQDP-a5qr8mHI-3xv7DfWK_-R7NO0ve59edjAjSq9BFQ7F2MhkhKPp7CmXb6u_urgd-lEatSsNgbiBEoZ-AAnmMXcP0_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 376K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-17738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/boost/withyashar
امکان ترجمه اتوماتیک و ایموجی‌جاوید شاه رو از دست دادیم یه حل بدید ، اگه پرمیوم دارید!
اگه ندارید به دوستانون بگید</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/17738" target="_blank">📅 03:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/17737" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بندر صدای انفجار جدید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/17736" target="_blank">📅 03:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۵ انفجار در خورموج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/17735" target="_blank">📅 03:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری سی‌بی‌اس:  حملات امشب آمریکا علیه ایران تموم شد
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/17734" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8ecf8e41.mp4?token=ORaP1vX3XC2YkJJIrgEbyFrRfv27GQAAQz83ON5l15n9bJwy8v4_r4Sg7HgMiqH9zkCfunuChaDpbqfTZa4Fz0dYGclqN8_fLG-5E5eVQu28ITLmcGPGbwhv0nzDJ2S_6OvvTlrp4OQvbHQjxKKtyMvyZpReIDcbPHkuBtsG5tq48bHcxHIzJXDwJrrztZE8qPz2PX7m3XNK5Pm50nA7nQ6L7LcOmd-xWJ_XXFeDgm5IDZpHvaSLG94l9P--nNlaBJSbIQCZFfG-84MGCxnZYm11B0EVdm6NSp2qdEN3UqKAOdjX2V5awwTTdruYdy_PpUTxUa3L_FQAy_bZzdKqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیدیه @withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/17733" target="_blank">📅 03:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRxUVB4WexyZNO9NdDbCVo2RZ1tzPZy07DSZK2ymm7xAG1iKqPPfKaEUIt_l9lvnwuPjH1jXhgsS_UlKeX0BQ-HYbBiAP9YqcxGw99LqRPmXCel7vhO62tFuBdVyrpGvATdeMHj0F-wMOJTBpJBcL1ai3gx_nGA_AEuuxr2n7LEQh4z37Tjg9JjFb4KMo3t-EnS4QWgqTPoXxoIwlX9EnTT4PaT0dc9CdaL-kCjg1MMmYOh6RwI4SENWdITRYM_Wb44RkiAWHvW2a9S5ZU1qQVWG5J-kSBzzvitN5Jdq2NdYUbKCD0L6dqDmD6-CjWc6CtUs4LMHzt8lXUrTiMvBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۹ سوخت رسان در حال انجام مأموریت
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/17732" target="_blank">📅 03:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAnq4jRl_Jr0UgYqeKOgR9OuS0WUCv6x5Ondy9q-Oj_lGj4QYm1kqY-nQrjaToRSXSluvXDIlH_kYdlebIY8_zQ8XIRH63lboLS3QMQDAFuy9suC2IPBkH1EYR2N0f0iH4_b56al9HCj3m9mHhVlxJuZBWebsxb4PGD3zHWVaAAmAbjqnb61Z0CFJNmq03A_IS6Jy46drwjFytsDmZxBl0Dm60sT8z-sJednlxsh5da_YgTCTRkw-wmUPN6xA6oA6MkVbyy1BX-VUexVJ_4nYi12TPiY5Q9qNrAtyeDWntKtDMl7VMR_GMrUF7zwy9iDNTSJk0iNEQboSXErrCF_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدیه
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/17731" target="_blank">📅 03:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">افشاگری ۸ سال پیش زم
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17730" target="_blank">📅 03:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سوخت رسان جدید از ریاض عربستان بلند شد و به منطقه می آید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/17729" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842f62bc5a.mp4?token=CqKfdrrh7K0onfd6OucBD58KkgQk_SzCSwiakO4aj2WZDEikl1Y8xGh0PpApQKaDk7ABDxxOluIf8yTBLhYZyTMTwzYMIZ4omVexLip4c-3bJpVKPfjPeCHVi1EKa635i-smiE01oGtfsKoTO6OXFx7DPQ2Ie7w0hNCdtqjNXaJQkVTq5EB-KrrIrIJAVnp_UWr72l2EgzWjnRzpE0BZ43BSB8nSXgx-5GddmSfyzYi7qVGZVeOPFF1hsbi5JcU5hR_mk3NiuZdKlwCwMAMu2qqGqnbc7Y_d6e4EtpR5mszS17_RTXJsRQsFMPW15IDvrwnO-JS9URyn9fAHVdN6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی از اهواز، لحظاتی پیش، آتش سنگین را در فاصله‌ای دور از حملات هوایی آمریکا نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/17728" target="_blank">📅 02:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شهر هایی که مورد حمله ارتش ایالات متحده آمریکا قرار گرفته اند
💥
قشم
💥
سیریک
💥
بندرعباس
💥
جاسک
💥
بوشهر
💥
خنداب
💥
بندر ماهشهر
💥
بهبهان
💥
اندیمشک
💥
دزفول
💥
اهواز
💥
آبادان
💥
خرمشهر
گسترده تر شدن حملات ارتش آمریکا نسبت به حملات اخیر
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/17727" target="_blank">📅 02:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی:
باید انتظار حملات گسترده‌تری از سوی ایالات متحده علیه ایران را امروز، نسبت به روزهای گذشته داشته باشیم.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/17726" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۳-۴ سوخت رسان جدید از تل آویو بلند شدند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/17725" target="_blank">📅 02:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برق‌ اهواز رفت
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/17724" target="_blank">📅 02:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حمله به پالایشگاه بهبهان و قطع برق در سراسر شهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/17723" target="_blank">📅 02:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsgrvaL8JBIY8AWXbcfNwXfXXky0oI1ckI8kmBK7DE4YwlPvpNtNRafXSTiblntnSACMli-C2aAdwUO_wnPtiX5qa50HqZCRh2ofHvFDagTvzlAtItcDDXNzTF89WBmswjFY2e315OL7R4jGuqv1X7M3cUQly4nXofhgNbR_yqEJKZSLNwUwvLrOk5adW6MFVT-p6u3BmEc3Xwby4eyHs1Ro1eXce-zmeZ2kEoy1iIFlIrYuXemPNYq1IJp0Kp3ec_YLZRyr2Zj26w2Z6WvFDhkMEzQ77Aafv88r4PNJR61IxfBqWahU2trn88XQLVAXOUwbhnnkVHRdxs-8tmieZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر از پایگاه باکری دزفول
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/17722" target="_blank">📅 02:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دزفول پادگان قدس رو هم زدن
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/17721" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دزفول پایگاه باکری را هم زدند
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/17720" target="_blank">📅 02:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پایگاه شکاری‌ دزفول رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/17719" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">استاندار
اهواز
: به فردوگاه اصابت نکرده، اطراف محدوده شهر بوده
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/17718" target="_blank">📅 02:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جنوب کلا زارتان زورنان شما در نظر بگیرید
🚨
🚨
🚨
🚨
خسته شدم</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/17717" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرنگار المیادین در تهران: حملات آمریکا مناطق صنعتی و اقتصادی از جمله صنایع پتروشیمی را هدف قرار می دهد.
حملات آمریکا خطوط حمل و نقل استراتژیک، بنادر اساسی و زیرساخت های حیاتی را هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/17716" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دزفول الان زدن سنگینم زدن
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/17715" target="_blank">📅 02:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cd857a54.mp4?token=tFDksQdGBbORjjcwkEq9fndghH38C4-oBLiWEvn88syn7OIHzG47Lm5lmF8yEEjXjiyKAwkPp8J15hnmhyKLpem5XqEmOMKvuMY4p-t-qX9IcEUlFPu0wy0UaorWXZp03mb_co3Q6_9rrHrsAOqCo-2ba5u80P9DJF4oFFpnUEUAllCp50KT7z_U43x6UVIFEH6sUM81r_Ghx-oWqyyT80Kfv0FkyTMHP9AiSktFSBoICxePszERhCBPESpE1iEBSX_hWb7qapD9aae26b1EKer8Zv57lTKe_XgVKNGSyaUkOWsq22PxW-u2av7Rl6bpasfbnauAOw-_LQ6ttPk4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cd857a54.mp4?token=tFDksQdGBbORjjcwkEq9fndghH38C4-oBLiWEvn88syn7OIHzG47Lm5lmF8yEEjXjiyKAwkPp8J15hnmhyKLpem5XqEmOMKvuMY4p-t-qX9IcEUlFPu0wy0UaorWXZp03mb_co3Q6_9rrHrsAOqCo-2ba5u80P9DJF4oFFpnUEUAllCp50KT7z_U43x6UVIFEH6sUM81r_Ghx-oWqyyT80Kfv0FkyTMHP9AiSktFSBoICxePszERhCBPESpE1iEBSX_hWb7qapD9aae26b1EKer8Zv57lTKe_XgVKNGSyaUkOWsq22PxW-u2av7Rl6bpasfbnauAOw-_LQ6ttPk4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز رو فک کنم بمب افکن زد بدددددددددد @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/17714" target="_blank">📅 02:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قشم سنگینننننن زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/17713" target="_blank">📅 02:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش‌هایی از انفجار در شهرهای بهبهان و دزفول در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/17712" target="_blank">📅 02:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYanC_pulR9GRsJBysUY3um2b0dTsmgVca_KZXrtHi6Yxu-6BTemPJiSKuXa85DuAVeYFQIaR9jWXcSS9zGfeX-bCDHjmO9vCU_DebrDAmMCozTdMooPFBNkLtGMPstyieetoYqI94v-n9C5KAQEdKRL47XJ1UQ3jgkw7FASBwkKJ7Xm4anJjqM0CSMTTJVaIng8TS1sY95xxpCWcdWOvbkvbpaJBjhHIexX6eBDyZDZ0EtCqv7Z15vNn5hHYvQwfkZzw2ULkGGsTc5fHbMLoRZvyHidTo417g6mbtyds0I-6_t_da6yzowHeM1XNDm0gGrNGLWXF0Yet2WKvnPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتسب به فرودگاه اهواز
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/17711" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مثل همون انفجار  سنگین، این بار در ماهشهر
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17710" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اهواز رو فک کنم بمب افکن زد بدددددددددد
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17709" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک موشک از کویت به سمت ایران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17708" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen.ah ♤6♤</strong></div>
<div class="tg-text">یاشار جان شما بی نظیر هستین
❤️
❤️
❤️
رفیقم جاسک سربازه اگه هشدارهای به موقع شما نبود الان رفیقم در قید حیاط نبود ممنونم از زحماتتون نمیدونم چطور ازتون تشکر کنم
🙏
🙏
🙏
🥹
🥹
🥹</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17707" target="_blank">📅 01:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فرودگاه اهواز
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17706" target="_blank">📅 01:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آکسیوس: ایران به چند کشتی در تنگه هرمز حمله کرده است!
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17705" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار میناب دوباره
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17704" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش ‌انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17703" target="_blank">📅 01:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTArh9HD_vaNOMNQw4ESQClZ1vkr5YvSGuhJo3JPy_C-yDsef8wtMvd76e1T1MQLWdympAjZyIFqvAZFoMdfxfpJPk6dhtWbZdwPcvzVRqri2AlJ4NEtOyiPMyD3xdAWAaStf5nDfCaj_eXWwdoTQMewGeUcm9YypVMe8_WQjKADbByubrM3Ay7Bw4sghjxzjPCWH4aUDoj3sfkmPxfamauRD6OHoOrxOdI6ux3V08b8vOCF4BHD7F2AJi6Wx57o7K-Xb7lLT63GExizY3mwqw2qql_3sNlvCSqR2Q6ljrcZVUOfWEZu0Gfet24G-T-G69lN37W-BBpDGkwKsvr9xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور مک میچ کانل که صبح شایعه شد و گفتن سکته کرده، عکس منتشر کرد و گفت بخاطر زمین خوردن رفته بیمارستان چند هفته و سالمه.
البته من گفتم قبلش به شما
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17702" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17701" target="_blank">📅 01:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17700" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neHtYz3r0ThoXQCcNqi3SIwCeQmEAGX2h7idTBalyaAsqcuh-XWPo5tFzLdAAQGNKh5yJjCdrTr5W358ytGi2DyZz3YEwPTDcmVkNuwTepR83U2l5otxltBlaY33FW9Zyh82ibbpeOK6FOR7e2RB4mS_SZNTWfQSd2OJTGf28WbuCqsr-7kaqTJmIX-va9Cry-9Gjx_cY_7TTSHOfgLDqquT8tCDLys1gXciXokYtbGlFAmJdsnX2rPGV6iLKFRPNthUhZPYYELww-tyUIYlnG37QZIU_bSuJsT-NehQ1CHBAAEMbjYM1aMXqczONHFAqZYllgd6nv8MZvQf3fqPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17699" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارها در جابر، جنوب شرقی ایران!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17698" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شبکه سی‌ان‌ان با استناد به تیم هاوکینز، سخنگوی فرماندهی مرکزی، گزارش می‌دهد که نیروهای آمریکایی یک موشک کروز ضد کشتی و یک پهپاد را که به سمت کشتی‌های در حال عبور از تنگه هرمز شلیک شده بودند، سرنگون کردند.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17697" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">درگیری نیروی دریایی سپاه با یگان های ارتش آمریکا در منطقه تنگه هرمز!
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17696" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=fk8WgHimw1kbTpaCxWCfaQn6vN7zY3naDJ7hs3-bds_-UeyRlZ6dfrAkHwArLU0mmGjCjJV6SxEyrG2ZN7-78zILB8qvOHQerxY8pIhDcG4r-hW5k28Uo27KyBI6eTonvGdpg53O_vF_sAQcc5ueQ78yIerIQfjzvf-wENkSZ68NIxfejl0EzTO0499ty3RxACUA3sjDjVU658xFbdUYSaYUj7Gd21c_yPgY5zOYX5Gz35h2nOuus-sX7TtaDPxDLpPPB-hXil3orFuzDvqzIkDwM4x-rKMlRso54-KC8mlbfpj1IvIXR_4SXnuskxOi1N7o-KkfQLkJD3II8W81Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=fk8WgHimw1kbTpaCxWCfaQn6vN7zY3naDJ7hs3-bds_-UeyRlZ6dfrAkHwArLU0mmGjCjJV6SxEyrG2ZN7-78zILB8qvOHQerxY8pIhDcG4r-hW5k28Uo27KyBI6eTonvGdpg53O_vF_sAQcc5ueQ78yIerIQfjzvf-wENkSZ68NIxfejl0EzTO0499ty3RxACUA3sjDjVU658xFbdUYSaYUj7Gd21c_yPgY5zOYX5Gz35h2nOuus-sX7TtaDPxDLpPPB-hXil3orFuzDvqzIkDwM4x-rKMlRso54-KC8mlbfpj1IvIXR_4SXnuskxOi1N7o-KkfQLkJD3II8W81Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17695" target="_blank">📅 01:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری صدا و سیما: گزارش‌های اولیه حاکی از آن است که حمله امشب یک دکل مخابراتی در نزدیکی روستای طاهرویی در سیریک، استان هرمزگان را هدف قرار داده است - همان مکانی که در حملات قبلی نیز مورد اصابت قرار گرفته بود
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17694" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دکل سیریک رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17693" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50699388f.mp4?token=PFp8zRxz3W22CIoiQe9BS44MTC2XdSvRvGu9YV0MSs0kJqKY6jcnSv7vXJt06O01RBW3Mx1bH6uN_mD0RK8Om5Edlc6rUqYoj1QY8OYIxCT91_eZr6fu8NdSCNbRQmJ3aH-zdS9KXP-tLCmk6sOEDipriuJNdHhwCu9U5QoG5_OCpsYsxlW4ZX6yPXkcUldayqMMpw0ZmyhqK4gtRMsaXqFKeEPIwYzmEO6w9zZQLPaNyYi2x_ECyQySz_IgySDvPyDomELusU_1HlvRJ7Z5Cs7ns5DNx5vyGMewSVItBrJ9twL4DZ74E7XmcRv_JHWrP9TVnJj9To0qI6vuJ9iRGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50699388f.mp4?token=PFp8zRxz3W22CIoiQe9BS44MTC2XdSvRvGu9YV0MSs0kJqKY6jcnSv7vXJt06O01RBW3Mx1bH6uN_mD0RK8Om5Edlc6rUqYoj1QY8OYIxCT91_eZr6fu8NdSCNbRQmJ3aH-zdS9KXP-tLCmk6sOEDipriuJNdHhwCu9U5QoG5_OCpsYsxlW4ZX6yPXkcUldayqMMpw0ZmyhqK4gtRMsaXqFKeEPIwYzmEO6w9zZQLPaNyYi2x_ECyQySz_IgySDvPyDomELusU_1HlvRJ7Z5Cs7ns5DNx5vyGMewSVItBrJ9twL4DZ74E7XmcRv_JHWrP9TVnJj9To0qI6vuJ9iRGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جایی در جنوب الان ، فیلمو داد نتش قطع شد
🥲
💥
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17692" target="_blank">📅 01:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آب سنگین خنداب ‌اراک رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17691" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پایگاه امام علی سپاه در چابهار هدف قرار گرفت  ۴ انفجار سنگین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17690" target="_blank">📅 01:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۲ انفجار بندر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17689" target="_blank">📅 01:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17688" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فقط عکس بدید و فیلم هچ چیزی‌نفرستید
🙌🏾</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17687" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17686" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSEZTnsGmOXyRhqSx6-UYwBb43-lZpJRWhjGfbdVoGLsJ4G0nYXKSpLwIY15y_cG0Vt_xz8JCDmajZ2eEJtxbrQTDOGViLX2zejbsyNBdQ-9PLmY9wVrRA4sqchOKho9Zz27FyVnvTLybO2t7b38hbi5snzyPDBnQUlX0GU_Gf61lK8X-ZzKNHhAPAEqmiFh2yv1So9aX9ySqWr3EAo5mOySg2WtCLw2imgZkmmYk-LVdOKpog6jbTiqtbv7K6HPaq69_dIrgVstZO5iZ30-4gCQQu3a9z30HmH6QT2DeWS7PIE_Rd5W7TZHuGh5wQl5y8X6vxx9FqV9rcTcTscf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار شدید و سنگین سیریک طاهرویی روز شد !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17685" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17684" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همه جارو دارن جنوب میزنند دایرک هنگکرد
😭</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17683" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2qDA5ktPodPH3V1H7Y4JltlZkP1XBz4HmFIny6ZMHk7Ds_39N0WJc5dpQAa61fCnR2JFllnNfdEu12JbzmDDJ3aXQ5nhORu2QRjrHhPeS7n4XLxpWee5ImQDhusOxVlzCYOgxKoEhmjXRPZzFpgsIG7tCHSygQULTz_k8E439FjCiv6hkAn8bf7z0wCkrKvwIqM8OCnzOS1qzcoI9XZoprKfQ2iHqsjo360KBBD3SLVXYiH4oEpVOW_wXghY_HZMr92WarC9yhfM2TRb_OzODFcsAJLxdi3vAqCGy0e40K-gYqtt34z177xFu35c0S_RxBoJzLfLXG_attNlAvykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:ساعت 5 بعدازظهر به وقت شرق آمریکا (ET)، نیروهای فرماندهی مرکزی ایالات متحده دور تازه‌ای از حملات علیه ایران رو آغاز کردن تا توانایی این کشور برای حمله به دریانوردان و کشتی‌های تجاری که به‌طور آزادانه از تنگه هرمز عبور می‌کنن، بیش از پیش تضعیف شود.
این حملات به دستور فرمانده کل قوا انجام شده تا نیروهای ایرانی در قبال اقداماتشان پاسخگو بشن.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17682" target="_blank">📅 00:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17681">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش ۳ انفجار از جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17681" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میناب موج انفجار و لرزش شیشه ها مشاهده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17680" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بوشهر صدای انفجار
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17679" target="_blank">📅 00:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS71TdRH6asOPxUegUbHNFx2mhZ0eNZp-YO0zHfMkscEKqxyqVvqPrx-cqlSf_9AtSDsEBZ-vHBR6YOlqsV4qHxAOMM2p7Q8H8Rd50lYvqxyvnLA2EGeM0LYlvuV5FYIsplHdkO93mu_N931hF3_X9ZnU8F-soAhuM_5-JsMKWel8q53LzGSUt_Bmil6ZtVPHSnlJzPs9LgNvt55tHVA0VjYB8DRaW4Bx1m-YKoM0GNNJboeIeWvPRr7HYDanJy9_rLLX3_nut-nujYxatdugTOVEGIeHekCL_IzDpVpquNS0ZSsiGQuSauaqjq24sxsyUkyZ-Er0RCDux0frLJ2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سوخت رسان از‌ انگلستان نزدیک منطقه داره میشه احتمال داره بمب افکن خاص همراش‌باشه
🚨
🚨
🚨
سوخت رسان های که از اسرائیل بلند شده بودن به سمت عراق میرن ولی حدود ۷-۸ سوخت رسان در خلیج فارس هم اکنون در حال انجام مأموریت هستند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17678" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17676">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجار در کنگان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17676" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17675">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قشم صدای انفجاررررر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17675" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17674">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شروع شددددد
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17674" target="_blank">📅 00:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17673">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۳ انفجار شدید بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17673" target="_blank">📅 00:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17672">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار سیریک در مجموع به ۸ عدد رسید !!!!
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17672" target="_blank">📅 00:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دو انفجار‌ دیگه سیریک (۳تا)
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17671" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار سیریک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17670" target="_blank">📅 00:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سنت‌کام
: رسانه‌های تبلیغاتی ایران امروز مدعی شدند که در حملات ایران به کویت، سه نظامی آمریکایی کشته شده‌اند.
نادرست.
واقعیت
: هیچ گزارشی از کشته یا زخمی شدن نیروهای آمریکایی در منطقه وجود ندارد و تمام نیروهای آمریکایی در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17669" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک مقام آمریکایی: ایالات متحده عصر امروز به یک سامانه دفاعی و قایق‌های سپاه حمله کرد و در حملات اخیر جمهوری اسلامی «هیچ آسیبی به نیروهای آمریکایی وارد نشده است.»
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17668" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWlrsZFqha-NSBV0R84tEFfDTdLG6mX5oPJUt-Ccb0LsL6X1Z_c4up3VSQCPQpbxdh3yYy4XFlj9PZCp8RIiCPbkk0EFmINwYiREGoCXU6KmGQ8cmA1usRpOxm7FTh2kHkKhJsvYw6ZP7Uo2kL92QuQC-hybXVdV64uKMcRASSxnD6wFZRJak2W2OmQWZmzEX2D76NaXaHn2ewX3b-6DLrZ2j2EG4XcwGnZQWfYpJuRvolSVaNm6QqKZdgRx0KgH07ZzfqblBhl20DWLDqASQeGnppynmY2H_w4QRCk7FAWFbJ7lUMteiEiomPiA1ZwDvv0sMu-ljI-e7rRPYJ2egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف برخی اخبار، پرواز های انجام شده به سمت عراق ربطی به گروه مذاکره کننده ایران ندارد و برای بازگرداندن افراد، مقامات و هیأت های شرکت کننده در مراسم تشییع رهبر انقلاب است که در مشهد حضور داشتند
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17667" target="_blank">📅 23:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الکساندر دوگین تئوریسن مخوف پوتین:
مرگ ناگهانی لیندسی گراهام می‌تواند ترامپ را به تجدید جنگ تمام‌عیار با ایران سوق دهد. این به وضوح به این معنی است که "شما نفر بعدی هستید". لیندسی گراهام سایه ترامپ بود.
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17666" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی در یک اطلاعیه رسمی:
به ساکنان کشورهای عربی: از حضور در نزدیکی پایگاه‌های آمریکایی و مناطقی که سامانه‌های موشکی در آنجا مستقر هستند، خودداری کنید، زیرا این مناطق ممکن است هدف حملات قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17665" target="_blank">📅 22:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/17664" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی: به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس، به زودی یک هشدار فوری منتشر خواهد شد، لطفاً کاملا هوشیار باشید. @withyashar</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/17663" target="_blank">📅 22:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی:
به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس،
به زودی یک هشدار فوری منتشر خواهد شد،
لطفاً کاملا هوشیار باشید.
@withyashar</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/17662" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۲ اسرائیل : بنیامین نتانیاهو با اشاره به مرگ سناتور لیندسی گراهام که امروز درگذشت، گفت: اون به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید.
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17661" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آنتونیو گوترش، دبیرکل سازمان ملل متحد، صبح امروز از آمریکا و ایران خواست تا به دور جدید درگیری‌ها پایان دهند و مذاکرات برای خاتمه دادن به آن را از سر گیرند.
این درخواست در حالی مطرح شده که درگیری‌ها عصر امروز از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/17660" target="_blank">📅 22:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snligxLRTMnsdy9hwWT10OAnUhRiDpGhjE7whD0B8yVIgWeCnXZzPidPThehp6-BunAPx2sgqxy8hbKsT7A89NiENT2kebcma33FnL6Fz47uLicE_bccH0sjf-XRaFkWAKNSen2Ngol5_EZPUd-zWUqkDL7mzUMBCULncioE2TwiQ2maX18cwgckedSD6E_LkBSCTrien8LZA2t9gIMQiR8g7BfMiCrI7MwiTxVZOfjq8suTcC9-QMtsWn6QhMY5z4TYw4YdUyjgROazSd6xNItlBA0wqt162FZJsjzTRsebzVnGu3AXGvOGwt3WJOuXFQDU0Qh19AcW2-y3a077_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تریپولی‌رفته و باکسر الان جاش در خاورمیانه است که خیلی امکانات بیشتری داره
تریپولی:
بیشتر یک «مینی ناو هواپیمابر» است و قدرت هوایی بیشتری دارد.
باکسر:
برای تهاجم آبی‌خاکی کلاسیک مناسب‌تر است، چون می‌تواند نیرو، خودرو و تجهیزات را با شناورهای فرود مستقیماً به ساحل برساند.
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/17659" target="_blank">📅 21:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیوزمکس گزارش می‌دهد که ناو یو‌اس‌اس باکسر و یازدهمین واحد اعزامی تفنگداران دریایی (MEU) که ​​در حال حرکت بودند، در طول هفته‌های آغازین درگیری با ایران، پس از آنکه نقص سیستم خنک‌کننده موتور، این کشتی تهاجمی آبی-خاکی را مجبور به تغییر مسیر به دیگو گارسیا برای تعمیرات کرد، موقتاً از خدمت خارج شدند.
طبق گزارش‌ها، این مشکل غیرمنتظره تعمیر و نگهداری، قابلیت کلیدی واکنش سریع ایالات متحده را در زمانی که پنتاگون در حال اعمال محاصره دریایی ایران و بررسی گزینه‌های نظامی اضافی بود، از بین برد. پس از اتمام تعمیرات، گروه آماده آبی-خاکی باکسر عملیات خود را از سر گرفت و اکنون از عملیات جدید ایالات متحده در خاورمیانه پشتیبانی می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17658" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اکسیوس: لیندسی گراهام ساعاتی قبل از مرگ گفت «الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم»
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17657" target="_blank">📅 21:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : این جریان خیلی مشکوکه صدا و سیما داره اینو یهو بولد میکنه مخصوصا این چند روز!  سید علی مصطفوی ، زادهٔ ۲۱ فروردین ۱۳۶۵ (هم سنه منم هست) مشهور به حجت الاسلام والمسلمین سید علی خمینی. وی فرزند سید احمد خمینی و نوه سید روح‌الله خمینی است  از…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17656" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است. من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند. چون آنها هم از او می‌ترسیدند.  او یک ژنرال درخشان بود. او مردی بسیار بیمار…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17655" target="_blank">📅 21:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حالا یه چیز بگم مغزت اتاق جنگی رگ به رگ بشه بری تعویض اتاق کنی؟!</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17654" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد! @withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17653" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بر اساس گزارش‌ها، چندین پهپاد ایرانی به تعدادی از اهداف متعلق به کردها در سلیمانیه، شمال عراق حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17652" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">متیو ویتاکر، سفیر آمریکا در ناتو: معتقدم در صورت برآورده شدن شرایط قانونی، توافق جنگنده‌های اف-۳۵ با ترکیه نهایی خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17651" target="_blank">📅 21:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/17650" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه بیرون میرین پاور بانک امشب فول شارژ همراهتون باشه
😁
کلا کاراتونو انجام بدید</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17649" target="_blank">📅 20:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه های داخلی : گزارشات از اصابت دو پرتابه به جزیره بوموسی
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17648" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو همکنون در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17647" target="_blank">📅 20:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZz96xeGGD10kWfEhgV3sV_N-fidgNCPhWXBuTLT6_rdgXEl4I_oaNYC8FaYODyoF-WOAIiouUenBGufXvZYMQnpThW_CtqYklOTp3DUljX4GK2thNTJlVC5u7k8E9jeyC2mHi1SbEySH4g0aVUv-564PzUuXagKfG63fUqcU8xwgQHiyzNJl6c60lhP9_bBdheitoikux7hdkxhhOSYltEUz-CDWjDywR8-Hif5NFrNs8hqPzex5XoPHyhL8wYmQt59XQqf8DLRvjKqWewtUEAtBUtZ6K_UyVFKoxmcAmgNSamReq68eo3Y6KqVX9o_5P2gpr-pstmNegZsc2BXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ دستور داد تمام پرچم‌های ایالات متحده در ایالات متحده به مدت شش روز آینده به نشانه احترام به لیندزی گراهام به صورت نیمه برافراشته اهتزاز کنند:
به افتخار زندگی و دستاوردهای قابل توجه سناتور لیندزی گراهام، دوست عزیز من، و مردی واقعاً بزرگ که برای کشورمان و ایالت محبوبش کارولینای جنوبی دستاوردهای زیادی کسب کرد، دستور می‌دهم تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا عصر جمعه ساعت ۶ بعد از ظهر پایین آورده شوند. خدای متعال تو را برکت دهد لیندزی.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17646" target="_blank">📅 20:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مسئول آمریکایی : حملات آمریکایی که حدود یک ساعت پیش علیه ایران انجام شد، با هدف تضعیف توانایی تهران در حمله به کشتی‌های تجاری صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17645" target="_blank">📅 20:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17644" target="_blank">📅 20:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل مزاکره با ایران را بررسی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17643" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ولی خوب مشخصه دیگه امشب میترکونن
🫱🏼‍🫲🏽
😂</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17642" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وقتی چیزی ننوشتم یعنی ترامپ چیزی‌ نگفته فیکه ! برو همونا رو دنبال کن  دایرکت منو سوراخ نکن  اه</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17641" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اف بی آی به کمک پلیس محلی در پرونده مرگ لینزی گراهام ملحق شد.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17640" target="_blank">📅 20:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اعزام سه اسکادران جنگنده از انگلستان به منطقه خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17639" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا یک ساعت پیش به سامانه‌ های موشکی، پدافند هوایی و قایق‌های کوچک سپاه پاسداران در دو موقعیت در حوالی تنگه هرمز حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17638" target="_blank">📅 20:09 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
