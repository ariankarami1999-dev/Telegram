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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 499K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEA_HyimysYkoN1OPqa-ySsQ4dkk5VklLOUKLtpc1QzG7BmSHptD5U19EcQOu1s6SjdZvyyZQWS1HWYBaOtG1xSIebTkOZnEFVXVro8oB4mHuu8xtgLWBA-IHkWcYg26OOWvb9Ar3zIK9auFYwAaP2I2psR2BrwSRYiJ8kccWVL1OKzL0UvI9I2LW0d1A85ctSWkU1GiO9RYuPNzEsyc-awAS3hya-DES8mwUbxx_XFBlL0OKoKtr5LUOzgJ4gNMr7e0MaUAFX2Gwi27ygNoB7fJjg5EaZQJ2yvh_beT32qtV_3CmwtgZIUB4yv7CnOVQLPItLU1w9-EltcVauYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwJueIpBSmSfl8eoUsIt-zRLfMN4oB8zQuiWMP43Zl2nJYPtRQ6Uq6p810_sF7X3Nrt1GuYB4GwCPLpV9WQtJNQf3R2E5jOZKGWq5mOvJaQJnPghuTmG4M9ix3RzbE86ewLtPtAqo9CVYt_BFH-ctDXgNC-3GdkGQSokDKDQiM21IQoMKkl8yPdeTH852GmO5NRd3gaLdrOmY4BcH58JwnwH0RA4K-eIydwUx0dHRC8YgfApXnO6LZ9ylELxWlXu45xEWk0okOUx_cgrBuFYp4-SammqTjC8AAq6M_4jLX9-0VL_OjTJQcDuaW41f2kTiSzMFb1kYbEjq4iY76ullA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnyKCdiK8cxNLPDT-sk67osyULAR2zL9x8tMjkF0zGr8wuScyby8nG-0-SrZ2V2lUZwPn6mj3lRtJgrCiC1_nFZfi-K58kunEaDJG5ierYotCfOQuoXy06Vos-PtOJ488RAmMklU3S2qVJt_Gz99j2Tzg0637UgCRvWlV_2kAgKs_UM4ufDoWSSeTSCJI-R2eg-eVL8QuzIvK-eMNNiKZQlB2C0THI09aWd66a69WMVwOoCv6ZF7Uc1oq1-OSu2YpGKOJVbIIxDnfTe3qWDkCHhLmAg_nAEHokzuL0rl2znD_r-gcxZFQYGJvRcLMnBPraKQ1-_5K8U22npKoKbfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkR0Ki79ECeVNClilmNuAe_9pBUNs23aF-nB-tSyGtkVU2Rg-FdMEcAI0ALm2UJ8VpcmrSXa5bHJS6_tbqMtGPkkEM5V9tjxg1mGv1TvYuctK_cJvoT9rRWKjuc37yjVh2XbGKXF8zpKh-P7S_EUCJEXaizgEGTQWzU9by86fTfzwQHfSLMUa6-HWraS6TdUS-XgqGD0dqwG2LQHB7cEjsPNT-qTenT04xvEViwZ0x43jaze6HsYt1JD8U5QVBWZmvSaIlUO7K_EMvbz3PF-Ym7BCDZ7GGGC_GUgO-_w4OSe5dBL4iJogotK8qwBd-n-AwaR0oCq6raoqNZycRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2j_5JLWu3ShREelKFxbUNpSKUPq7ksT2BSTLeQFP7Xnw1sn_U6R_Ig52OE6gx2uTTfdRjl5F70GVbuTQ7He-4Nzh_43iGpiMZKj7aXKyq_IQj-BRaNeDCMo-UmQ0H2uL6J04YzAWvFK-hif3rO0KZmGP8TTfe1w5f4P2oXTCLqNHWd2fCoAFaiZZsSs78HaR_C9NGIpeA2hlGqb29-nfdD_UUnWtD8RRk5gMDUNQVUVlbjgEaMeL7-ViEDWNJHnIAKflE7PhgiITqQDoOg_k9wQsUNYaLo-T86eIrIGDwPaC5fAKI04ze_tiT9PEag1HOZUg3EwhKmiaFDEZx6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30fls_VuilR6tSDXxrcEZhtFqqztCGRfLraT8m7ZP3y9F4wsG84_s0h0oqQXbsWgIV9m2FW2JYou26ODDJlOHAtMJ7HjpRSUAaUEojWjke_n57LBS4UzZoCaoiWDrkxoheqcNoTR9qd7IXKtXMecnxnaSTGPiN5zHGmroJ0osANIY7pZLPeG6TwF8_WgNpJ9GCUY0nvyoj_EArXIZAm9ABuYy45UhB4IvCtGpP8ZPwJeh5KhyQiw0d5GwGFncqqGWwydNe5Xs1Y8DMXUNBwp8fGC-kHU0hv_56ILIeUjbjNupRQd7H86dXKmXwFOTpwR8hJdTWnU60v8XXSDpwUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjul3lpHp3q7ENDfyKmZ9RrIwFbbTur56-t1N3olLUO9EhaNJCcoehTtJbjBr8czMXgj1qVa9Yvt0jAwHYlfF_OPlLaIE2N3viOWLbQHBf_i8ftdcPTSHLGqjFcKx1r32qLc7Gl3hwGDf060fUFe9T7iWzvJ1EKNSDwvjDrtKiWkvZrB-27MJCbuRtJXpLa6_s-TBLXlMGYylrJfUX8apAZgcvOKzXxHXHiL0C3h8Qu0Vm6obG9StaS4hLAElthIYyHu-6GL3aISzomcgSOTZ3KDJ0UFPLSfoA-Y00P62Vx6qDFYrrbjmRmopjD5ZSXCUWl5duo12scqQuFTm-M3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUFBCnDvcbB91E7_KyoHpUsZQrVfXsMiIv8ucHrts4Cv_yb8V3Ll5LjdhVj6t1bhbrTuvRUfyCJdhyRJrt48JEKhwLMG9JYAEmR9vkXfkkxjeU1C_2Lp6zWlptbY6tPeg87VSKCPVAajfCfQquoDUsXIU9hyBiuH9KAYYDekf3ohB9FZihlBR0opuIUHJYvLtnzT1vhgjANj9C9LpqNTD43juxzLh72t1yb7rR8obVtGixUshS1Lzfe3cTruUD_dPlR7aDC4ySkBowv2l9_H7hvpX5uI3I_hSmeb4mHfghFzomzVUswjDsLrdEfAQCimYucABbXZXoopBs8FipoPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBZqillcVD2_apzjoS3sxrYxxM5Ol0rGWdn-oS25qFsEM6tHTXXGbmcfa49jwYBe9fk8_m5RooMXkNAj-DDXivLu9NUvTDmX4D4TezlHgSDmnKLL_xRPJSHMYCGl37tjpBRx8ZpRDtKsKLal_XdWDni0VFBKvPVtPaxWJVQUO6tzoL2qf7nlmngLqqx9BLxFwamrw9YK89u-fsHrlRqMQzqxBKV_CrDyEg051_YDQdDAtDYpV_5gMmyi5thBBUSmu2x9oGAhLIRIzTm3rp8iPPUvAL3Jws5vPnk7k_X7v963k1CxVelRb_9nJD0IR0hA49OalXZumDkyPDH31j4LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5GPY5T7G4CTRsrUQlWEvL11gURgwoyhZ0qFAHDt0299BJ3tcipUz2_GrRe0m7fa6ZUDwE5wdqT-hlT7YQf3P1ks4DGW49MPvWsD8rfJGEVJJbhGcqMjOU89HQWWj_9IYnDDiYR3fAfwZwh1ymR98RBrx2T1rhg1qIYy23IDKajGzS4507KjBwVJz8OTnI243eb1FAr98xc8oqCPDQa6ycfTXezjEBY1WobHNYmiOwCYbDBNPf4NV0RWCmAY3FjgnZdp_gJ8j9MlKCK0JCuwAmW1iKwiImDdXOKTAi224-dWDjXV__IYp01FL08UMcIOqr0xo3ZFbL4MQftoQzagXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-OzwQ05mh0nQ-PjOfV-RUyKwLPgsUzFzl6AjF8bZXhgcNfEC-e_gv6A-peld5WUgbmT59QzIErut_NK5YAQIGDjWklwi0oeLciFug3JRRbZ7w4bsTcHw0biW3KwtoqWoSaY---Lz3wa2VMAqzsB1jxf_9KAsFY3qT1qsHN_oQXhLXmnlt9drvYlYRJvqeBuYkyE65bfsLFe6OQEhiZHfR_i2pZ4bC2b5JJZRMoidI3FXUcNXc_OIfN0hngIOgGaMLO7USFfRPptVgSRrOJMCOQdvsW4f_Hhubf0L58gNBMMdTcvOV2nrtjvLDpFp033l9eI2yvnP27we3p7vCzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvoWGrKpkTncmSmE4W5sgwMFwKGWiTvZR74HxxgMJdeUFSwSt5KdsJjoZ-vybcB0gX7pnaF7_JsP4TsCYaJcevCJ5AvqPR5x547u8EtWLXTgnoDra9uc68ILi5zBSKkJNbM3NEkZRZK9YaKyfa4RyWMmKQZCBYGUKf2rsl9wUWRjNYF5IcmbmWUe4zPzBjdFYd9H4Om87QpSbwduqPLM35rkJf-gWre2btEfmdy3CXkGhQ321qB35sfOtQ4Fj1JNwqn0FsVjhLgg86mXfVeLqDl2wotSqbInAbgMd2fWtQlXihAw4qXtWXeMML5gw8Ca8A3pUGZ_qzvdnZBmhGzjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE3ou-csGdduQBcPL3w1dVjemzPn2as8NdND-0mJfm0k0zyEkgOuJeYqLowVZjjYk6pQsdZNeU6JJytnmym0urI6c7_FjAqLxzW4OV_98nIXR3Jb5x6XQZ9MSMmy7VKFRzCccmYoKghLCTULxePCJtMy7jgzgVLEcYnmtT6qk7xa7kWjR85ZX3JdF_0-TDDnVs48HOQ0ockObe6S_CYL9jRtzAJsHBfhz28wVFMoZXdqQy3hdq9qKLScwI_PRgslAVtuuMkRUxGYQQSKrwokmewQjbAqzG9y0wsHfgPIjqLKijeeJbq_AtlxNfJAbcYvdoRtdq50_pK2QjQX0oG5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwrjqzJZLvYeQPrWUrGgVxTc0Q2d8OepgLor2EB05Co-f_AOG9uunLGwD_EKqUXuLIhfDRhFx7HsmHVJ5JivS9qdJ0lQBbVMoOhCvQLCJF17n9AFCpOZJwUoQDAnMnfApfn1OsnwLLbFB0xpsydGEK-HM0GGSotcTxHoXNyLPa0WcLnymWb4ZhemZIcyW_d3LyrJym4uQdms4Oy5gqraQ3eQUCGc-8RtKUfqvfHu8BYV2M_kOLR7NeJs3cIYvY_Qz-FqpL9MQi6Qi0lSfjG7pN5DbbC-yUBSlDioexWekoR30clhH1Aju2S0D31Bp96ih4lK6BpUUzeF1SCObHNGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glryTqvJKAIoCivGtk5cF192CB0_AwtUdhGhBH0Tu3EousB5BpVUSM6aG5eL_UQmjD_dy1kOjKBuLr3WQ1IRoRd0lxeg5KHfJQd2HqDSuMw-l8srTJVdEOPaHjJBYZBOzYy0gQWMr0Llb4AJ3l1naP5UNqZcnB4WGHcoqXLUm1rRNPD_f3AYWKEqJqgnzbaEnO0SfYKAawXe0Uk9brS6keGm8TnJTjQq6rBA6KQUWuJ44mP3S-jQCTEN4NnkmPL41zJ98Fc5Y1bo14qoiMlWgRn6DV6vFoZBXz30Q0yXVoMXszBB3I2thvnU4oM7-6Gd9EsLvdh_zc4k9-lp6yCYkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCgWKCFaaaua0yMM7WwZVZT_LoFmW3gk69Y-KuW0Yq-t2T4YA0P-EN0zaeY79fiHVPjfgxUsj1bH0jUYZ3TYfSlEzw5XRNH-VsLlxbWrimI8YNspLi4BO5M5lPdB0_dJ55c9OuGmf9hrH6O-TWfQbEkAW4gLuneKR_Dpz7fZ8wyhKbuSvJlEf4Gl_ohRa2J1arJ6z3dZaNa3zVFryE9YOALZf7WXiF-k67oVfc0anzPpo2fnjA9D0lXg0_JdoNWeY01nbHmU0oZk3jgBJTT0pvp4vTHlH1RyouGkd84z7jjG3DzVPGNEDpRU60VYAi00y1EcjCaV91aWUZEFN8itYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtBuGxMX4z8Q4-7mtkGA1HK0mvta3V4T2H1bEOhj7v3uQvJ7uGSfSQVMunsTzwxce2-2FsGpNsKRZPp8Z8ts4Mn2ubC5ve6-vh4sf46lCnxoc2v-k59SK4rJ3vB2RZVrZccNsAyWH03Op1SFREfHM4xmUO83-ZUGuLZ-8glWLAAz94xK6DW9iA_Zq9iBdhlRzlUPTj9o9_HC8rKa4Z5Gsh1AGy_G6Gr08y2cIOl1Te9O8znxnpJitgtNVsFB1kCP-QPBOqKuv1PHj_T8iidHqaNIwZvjnDOnyVI4IOzi_pIPa_twOaLG1wdsj0WRfHvc-5v_yvYINnxKVmzs6m6YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuwkUouDRqDTUE1FImiwbLac18WgGcd6Pfywfy49u7T7xbIJ-GqQU0LwuEQofxIGbYR7NdQHd68Xi7Ajc6q5ekwOhjxcTm3wLKKe-aUDLBbf2nqAJCW6vy-1hHVXiXwLSQhftZ5SIeMbk27VzYFVrjfdqP5aIBUpeg43336szcfi7ggSfZ85q1YUSVkjrscMtue9a6fYdQN6TlWP1wsPh1Ja0zPi0CsQh2_F0yy9l5Guehi0SPEnf5Czn45LcXjuzEsIaIJN2cYESh09liW4xvsptHoEclAzP1srLFJa7K2Snqipoxj9Xme54B8o3wwcPqV-p6IcQcOFF4k5TsmFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmJjOyBZ0BmweILxNdcjJGf-C7iBaQqno2sGN-ynGvbJMWxLJeSbqyVgcG3QbPDqP8ZsUCIrOS619BbMJTKFNbVjVEuHOgRmgesIK3e2UWT_M3p7kLPzjXYvG7uAalJm6qbVBJuq9kt4VGCZ0WXGs99WGzPMT-f4g8PUU6Zsx9rWhSkcKvObUAyrr97ejf8l7YiMrK-KohPlNlKddRZtZNYbW_MBBYGICTRITwgFaVndHQz0A-bUCNilOJ3iKl6lTCzDzQWqbx7-lvFLG0OaQHDBuZTPoLDOTyLJErArSq8C0YuEfskUddrXDD9c1jr1-5Sf8BDs47wVbloI4NazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnj4lb_zL-xAEuFrZIfUe6_fEK6Kr4vh99cMIZAtI0KuvFWsRp2Z4Xlld1i1Bq0H8ItlHviSQrkU5Jb-BzPydoNE64Po7mAp04lN6lecGfDFFS09CC4tDsK7Mm_poW5-XHTvJpXO1un97MAMYT_U3V5GFgIHhzSX76fKjbcm3CbGhmMMquyPII4RTSsaleeYaM_HTgl6V3LYuPs6a7h2jdzOnrJbU8QmgC1EkEbEV-apt74ne9ycjIilln_lPxmOwpTx0is73rqboNagw6wTNp_tOXWoKUVJDMVmFtM_2GbvJh03ygTgJ93JlegRqvdbn0uMZIy6CsLtE1kMgL0MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=gEJcZ35HKdBl4XRErWp08Lb2q0z2tSHoMgnZOBTyikvZrp3D9CIp4r8VFfK6Z9vT-Bk4780wl7do8Wn8vvlT9oA5YfM2M8Str3BvUKIpzUu_O-L86_DAjDro4jk-nekiAhdBy27HeLj1ZqVgnF_3AuRPPbkmHqmHG54l_NrvmcQcTBny5Wu4Wcdy8ZdkTYnyetmIGFewvebjArfXoq3-8QuynZ9n3e9PgggW-g7c4vGVDJqAxvyyx2_QYWlr7Zb2wYJqXKY6JYBI5jaEqgeHl022DcVOdh08gMZFiqatDxRsPaNsbwEZMYnB-4xC2Ww3NEm0GVBpFPh1_nSW2l6Zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=gEJcZ35HKdBl4XRErWp08Lb2q0z2tSHoMgnZOBTyikvZrp3D9CIp4r8VFfK6Z9vT-Bk4780wl7do8Wn8vvlT9oA5YfM2M8Str3BvUKIpzUu_O-L86_DAjDro4jk-nekiAhdBy27HeLj1ZqVgnF_3AuRPPbkmHqmHG54l_NrvmcQcTBny5Wu4Wcdy8ZdkTYnyetmIGFewvebjArfXoq3-8QuynZ9n3e9PgggW-g7c4vGVDJqAxvyyx2_QYWlr7Zb2wYJqXKY6JYBI5jaEqgeHl022DcVOdh08gMZFiqatDxRsPaNsbwEZMYnB-4xC2Ww3NEm0GVBpFPh1_nSW2l6Zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=CbiwMxigZQKtbkvSu0tE8HnB2ohDl5wjQoE7Jiavm9toiQp1quGxdECVUSOHUaCyXaKhkiUpLukeYKtV1LCVXNGoDvOLCo0J0yCK_X0KPQs5D8melgoGzPQjvDrtb4Ch8CLEtnqwFaBmsZ3EQDTeTqWb9LaV4o6uc-_DreVYb69Guqm_X3gu7QDgNpJP-mJO7MP7c8GkMzZ-glNfoBP0j9_EL5dH19TolGz3S1_JqV5dNbOFDyFkQz1rvw1bd6tcHT7YOCtbRrAUeIwpT7zvyYc7Tpmb8XBW1RvBhbgap8DjKGbHfuLez2BQBql2tjkdNCxUuv_eK1QDUl1rsnh063SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=CbiwMxigZQKtbkvSu0tE8HnB2ohDl5wjQoE7Jiavm9toiQp1quGxdECVUSOHUaCyXaKhkiUpLukeYKtV1LCVXNGoDvOLCo0J0yCK_X0KPQs5D8melgoGzPQjvDrtb4Ch8CLEtnqwFaBmsZ3EQDTeTqWb9LaV4o6uc-_DreVYb69Guqm_X3gu7QDgNpJP-mJO7MP7c8GkMzZ-glNfoBP0j9_EL5dH19TolGz3S1_JqV5dNbOFDyFkQz1rvw1bd6tcHT7YOCtbRrAUeIwpT7zvyYc7Tpmb8XBW1RvBhbgap8DjKGbHfuLez2BQBql2tjkdNCxUuv_eK1QDUl1rsnh063SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzIUI8wOvHwDAh-7eHa0Cw_qhed5_PnygBGyHlnwvRjuGQkOC-jtre-kJrDa6RUNgxuYy2DwWkpavY4MoOI4Cv6V8kURrQnuT8Fqr1BPwykZ_Nayyhnhfy2nyTvkGS2QSosHeA-MxI0K6qTbO4CfEhKH-_JKhy3xHHW0z3vNic24tmkU4EMjgVf-pwc5_KIBvwDCuAln89_AlA-8naVBVQHKBxYozogdHbND3VH2E2hmCkx23f2JxQsn0NS4tg0SzK5RwEnbj8UsSMfeNerLy2YMvrYEuF3Igk6iDXbMm9XXbAGNpmRMtH947b0bnNw5jPDfztXbzpdNPk4irV8pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otvbaEZu_BJQqJHxnDG5tAvL7Fc6aIcAxXINPfl0nBM6lySLG0NuNaIfMzZKLa-MH7DTCozj8r2QEpP5SdvgVJOs7PpT00jVC8lGB4DAyikEWaopza5CpQ-RwDijbjqy6sOW9B2Ru0f05SKGHbfjRmZ4PX_Po_YaB8gQZfLyLvAD4nwVwPq-J2nnv-mEdjFtC1KkKfo1lFrhLB57TUScCZI64-CJk3BeKY8_HJHWJ-XwPhFMixvk8mY4OqNWU1wEbpV5MdzVzHzxjgF7tIk2QIsTa8c3Ea6Ms54ICrCLIPxBywlq-xVkEpEtQsF7Cb82tgkDHD9PlvI0Gf6Gfi9vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpIfQ_GT7qrU7EH7jDyci5ZkzH0ZluY8vIFWDzsuErCDf_ePXKwpNjhpQl9fv1E3eO6mhKzNe2Op6fbLgWgzAjYSI08JT0hiFkiczU0tHW6QEVs3ba0dtWkQ8xV8BR194hsE-6XagNoLDBIEqhhTolLN4hJvDd3fVRo7FgamjxCRa7fuu_bpbfWFt0-oblVoMc8anPPnKPQxvjAsd4gXgwRdZZy_fYwaE2NM9UuBttZYv80W-Oc_BSU4DEGZpg8qCV8p_qfVu21B9-GcLCXPf5jMQACbQiWW_l7A0AaKAb7AS-OtfL5IaKxjNUSk9x0iH7ohFEKTBcHIul_g0GAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Q7lkR_vpBFRuGp-FBDxPi2JUvalSQUtR_72ZyY7DEWXAmRGN8Sb_jMJDtJ2lg2MdK_qdnsFif8DyQ9qDOHCYC5H0GsdULXnEVRnRTv11dpy-wN9ug7XZo-c8aS5ni7HLRxb-cqzW3W9E51P0WbfUyVx_9YO3-otNeaXOWW1TQR35fMl0Hc06R2FHbs76OxvKtb0ctPTUDqMJzqVP_KMrIo60hWrpRsT7pBD_3tcUY1YuGzdn5-WG0jj1p2fS98Jp9qf_Mnbrlhzxm2G-00tttpA6W4-E6lrJMo6Zgakb49-6oHA-qGi9e6y5Y6ceplJ83EuOUAA1bWa49eSDwknmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Q7lkR_vpBFRuGp-FBDxPi2JUvalSQUtR_72ZyY7DEWXAmRGN8Sb_jMJDtJ2lg2MdK_qdnsFif8DyQ9qDOHCYC5H0GsdULXnEVRnRTv11dpy-wN9ug7XZo-c8aS5ni7HLRxb-cqzW3W9E51P0WbfUyVx_9YO3-otNeaXOWW1TQR35fMl0Hc06R2FHbs76OxvKtb0ctPTUDqMJzqVP_KMrIo60hWrpRsT7pBD_3tcUY1YuGzdn5-WG0jj1p2fS98Jp9qf_Mnbrlhzxm2G-00tttpA6W4-E6lrJMo6Zgakb49-6oHA-qGi9e6y5Y6ceplJ83EuOUAA1bWa49eSDwknmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=gYBVyR2Om4sR1ZHWIPWpM23bOWUrCh3ebVG3pF4kpBudpYjeYD7i1wfnZUCciPkTyNzQ0qM83exxYEvGmvL2xDMz9WMve0XqY_8AgWteCskerWTPxZyord_l2mXosOrq4odU4SMERvObxApvIkwYTy3EIt4zxSFhZ2x0YCRyQ0YyGw4fmmXzQ0sFoAvt1OZKNKzpZgzwluEBpiUCPACbWNuE5rWb24cYSJh0wDEh3JYIHLUO8dCatO-jP8wEmcc9tB4iFgRHCRpxA_vLptCm7OIqLAr_oK_HnyOfTcyEwg3MJ24abE3ERIu0-gOpDPM2PEDmpylYHFGHZiBRu7BBxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=gYBVyR2Om4sR1ZHWIPWpM23bOWUrCh3ebVG3pF4kpBudpYjeYD7i1wfnZUCciPkTyNzQ0qM83exxYEvGmvL2xDMz9WMve0XqY_8AgWteCskerWTPxZyord_l2mXosOrq4odU4SMERvObxApvIkwYTy3EIt4zxSFhZ2x0YCRyQ0YyGw4fmmXzQ0sFoAvt1OZKNKzpZgzwluEBpiUCPACbWNuE5rWb24cYSJh0wDEh3JYIHLUO8dCatO-jP8wEmcc9tB4iFgRHCRpxA_vLptCm7OIqLAr_oK_HnyOfTcyEwg3MJ24abE3ERIu0-gOpDPM2PEDmpylYHFGHZiBRu7BBxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3-zkkGBaNjmKOEBlt_Is1jrC-3aKT7h52Qp6Y3h05oxOF8gt88hIgrz__nTduPyoW2YKH2p3A7DIAGVoQ6i9CBmWmjhEREoI0uEy6NFujQnMUiRaqqgL-YvGk9E2lBj5aYEXG0b5Yrz10R3ydCozPHm158QtedQ7qL8zs2_uLXAsQM4_du7cGOH0FoBq6ZuDQA1gQ9gZoXg7kwZkYr5XJR37qeamYDGYzh-UDby8SxGB69SvcMZQ-Os_yRtTldseW0TmZq43DUBJGRUy7cLqCCMwv_tsnybmkimfiiyV5veVA_9Ec6Gc6cGjbG8vlWRmJmbWlRGWzMD22l2q1ewFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTwV6htuPEGZugzccDFqxkemNcvkcC1HNVprs-gXK08MyyQc_mT-HYZcuBmLjhh-dmxZR8DxdeX2b_ajdKc96rMok8Ns679ulCJIXr8kzyp7JhJ8lGgbDv1-mhlpKykkWOhhzxylCBkCsKqb4sdYdt1AjG3c2oGCG5da0ZPm2nYwlreCxsqDmlj1mtt7kUg0ETj5dBCJ5QXgoYb8YLOrnH5GisAoYMsKVdlm-DQkQIWnElLg2vN0tRZA6081X-sWQ-vuFUNzJWUXg25VF3YNTCX7M_XBAzo8Az1z0lQxYFsfHo1EEWUxOEtWP8r1IiFS2NMHIxfha3DrQz2_irujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYZCnCOUxD771-6j4m4wwvPq2AfRSNuF_yXh7HeFaFvI59XA9XuYeeYH3f2e-Yng4v5Qu4b7NAYMjmEuApaMoTXgHjWWhbErJZOeo7E9jOrg1Yq5xP5XAOhyRKAX5-UxAMvbF-ZHdXdGietod-4yCbDBP9S3KXyXVzJ3gGZxbnBb__bdmA1wF_FRX5u2tTvEvrxfZwO8wXY_Zvoa9OdmYoo36tNr06sdcXH3MPsPJCvHJuB8oY3-J2s8U3qhOqKSvqAKH1Ci9GrGG34IIyHI60AWQL2bCgVljKI9qV-UQLu0fsM4sVyQFT1TLI0uUK-Es2AnQz6lO1x4_2nV3iONRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quZT2WHWpcT1uHxuVgN12DGZPQPiQpT8iKe7kObNsiAlp4-kB7X26JRXiUt53MNXLw87CXd5TjEBz9mhMXMQZS7hc6aKQHl9Veyw5OE1cFqHOVdxAXMnrgvlu-FAy0kZl2LDtuJSezA9UAUINcqRmV415KwgeCTqJXvPLmWAKb5NENO-9C9NZ3XmOVPdasPPCitHt17vDB-yPXeIBBNzBUodjUHfEE4DMvX9BFstTxxlbxrXvS7M4TYX7Hd6TUa0Ledpbi9gAAw7cFhMf-A9mmfclHPy141gAOvnYT08lir5Vyp0ETyTEJko3sICk3RdPGeovX3WEv9VXmPNANjEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=u5yyV3NA_xJ-r9G3nAuGtNDkYStbvMaJf2VObCBsbaPoY2vSki5TA8FFwyFJOJm386TxfPQYzRcfgTHbSqnnhcQS0hQoEOVtuNfA-iwe5bzNZT7mA9cJOIl0nSsOPKaBRLJGE-sbVs-I0Vv8H0m-x5Ox4__cjuUcjlwI4foupi1aKb7UDu-_1E212j5vY4nkakfwRVkKmXcQei_dVvLgX1p2MCUL3TNgNxiCG9fuP6Nw-q5Gbmkv9NV6TXnt_VkRGR1wNzEZCZBodiXGVrr-W4Xos4apQCasH8XDeGbELAZ7eX4ZkGocpi0DlI7EpvEOaCi0klPLL65hqchatB80yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=u5yyV3NA_xJ-r9G3nAuGtNDkYStbvMaJf2VObCBsbaPoY2vSki5TA8FFwyFJOJm386TxfPQYzRcfgTHbSqnnhcQS0hQoEOVtuNfA-iwe5bzNZT7mA9cJOIl0nSsOPKaBRLJGE-sbVs-I0Vv8H0m-x5Ox4__cjuUcjlwI4foupi1aKb7UDu-_1E212j5vY4nkakfwRVkKmXcQei_dVvLgX1p2MCUL3TNgNxiCG9fuP6Nw-q5Gbmkv9NV6TXnt_VkRGR1wNzEZCZBodiXGVrr-W4Xos4apQCasH8XDeGbELAZ7eX4ZkGocpi0DlI7EpvEOaCi0klPLL65hqchatB80yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEm70EA6wvMmFOlHHlJDghO5Fmbwbtbbtcy9bYS9ArQxD-t-4M8TFwH1CP0UlTBRaNquyaYPi0SB3bx5Y0an12pglvWooYvy7Tjll0PSwdoNgbYMTaT9vGz3YBCfuFBN-meEWf54w8IW-TBQsp0hcVDkwUvJ_AAn-ukqW5aTqbIYTBXn0MSqALVc_AJo4OZR80OWbAwI_QCturWuGm6MQKdDDNHDBKFRcFi6ArkC1A4lDufJSSgLMhDpFVRm3R0-OvO48ATBFSF8-AGjSVZa31_GYoWVxY8ivJKunaZi_fInQKiJtVJHPmxYbTBsR0-qP5VGwG-JsOelM6Py87zacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=UYm0kUONrfgPZLcFRL_AZOzITFE7SaWASzy41dh1orzZnly2iu_UbJOWo74wGvOo8LSRUe4Yt7WP8hygjCR8473pEXfOXy1hIWOq_bYubtCcwbm5J5lv0h5HPXXkdcbElo5fMhM2c4_6FaVRuXA575BkTRpiAs9oCIDnRzoO4JZzDEqc17NNJOevSw9Bv-pAE7meV-ZWtmOWu20klqCRHZw9WruDYOm5hu6l5Q5_ecBN3Vw_zhMl3kNV0aJNhBE1xVb72ehAVOeYla7Me_bCXYGdGY6d9aL6wsCUcPcG7cfh3pJe6CSgAs9pWPNtHt21LfznOZRwGUVwt83gXIjooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=UYm0kUONrfgPZLcFRL_AZOzITFE7SaWASzy41dh1orzZnly2iu_UbJOWo74wGvOo8LSRUe4Yt7WP8hygjCR8473pEXfOXy1hIWOq_bYubtCcwbm5J5lv0h5HPXXkdcbElo5fMhM2c4_6FaVRuXA575BkTRpiAs9oCIDnRzoO4JZzDEqc17NNJOevSw9Bv-pAE7meV-ZWtmOWu20klqCRHZw9WruDYOm5hu6l5Q5_ecBN3Vw_zhMl3kNV0aJNhBE1xVb72ehAVOeYla7Me_bCXYGdGY6d9aL6wsCUcPcG7cfh3pJe6CSgAs9pWPNtHt21LfznOZRwGUVwt83gXIjooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkKpVr4toQSYyTRkR_fErirVe6_gWNr0Mi1co-laXece74F-XxRufJx667vSe3eZ2cufeKxsNpJ0ndPpAQl_x0Fw_DmLJdKSCCxQQI88fK-q55EhzEHxS9wsyLLxh3skG582S5e4-DsMoTx-OrAjEsgyIP069b3vjYfmYskeL_zo1qLw9cRUp1ZI4BxR5qDBJu61LSyzc-k40QuTUb0uZRhHAt-nYSA0dnOUXgkLDgAwuPfgRR0zH7cw91eXcKDyos6Jo6LOHK-a77ddMHMYGFVtYChcTrZCMwEtnvbbHQJGmMS1ToajKaP5BbEBqjM4HVM4LifgoHoqLgCsYeHPLems" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkKpVr4toQSYyTRkR_fErirVe6_gWNr0Mi1co-laXece74F-XxRufJx667vSe3eZ2cufeKxsNpJ0ndPpAQl_x0Fw_DmLJdKSCCxQQI88fK-q55EhzEHxS9wsyLLxh3skG582S5e4-DsMoTx-OrAjEsgyIP069b3vjYfmYskeL_zo1qLw9cRUp1ZI4BxR5qDBJu61LSyzc-k40QuTUb0uZRhHAt-nYSA0dnOUXgkLDgAwuPfgRR0zH7cw91eXcKDyos6Jo6LOHK-a77ddMHMYGFVtYChcTrZCMwEtnvbbHQJGmMS1ToajKaP5BbEBqjM4HVM4LifgoHoqLgCsYeHPLems" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1Uk_9QAJCvEfxYP-tz5zeKY8mQjDyPLxaMIdnDUGBgijO1NbYcoyrjO99myY4AJqfs0GWWaVIJdct39qJSIt0FLCVBdIwoya-wDEK30xpplNWJgxpVTrBxHFLWG2ReWAlurP-sMD-xaFAAHDzOEg1Gv2W3_TX9r8WINvmaDcExzp5Au88NwZsJTCDtagv5B3TThqXyx8C5oGOzPkffLl7-Qhv3J3bTqVMuiAoo7jKH_vVpJkF7ieSX_lVTHpnPM9RrR5fIb-y1Gofx2zCwuprvAfXifznOu7aVsT1z1fY04OTZ64cpLwA64CELUGASCBWUuuF9bPkH_2TOcEohEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irgEPkiUliwMn1xH6U8BxNs80ZftVNWBwPb_Y4z4g7Qe_l-c3rbZR-v5pzQARd7aXvkQS_JPBOAJcWvjyngRjOJcPwsE81pVTczObUOuS-DQ0mZTz0VKCWwjoacf8BH2VnOGooQwafiBmhwISaiJg7fXxWE4dzV1fHCv3Oh8BLZN0kMKemXf6gVBegYw2TSPlO3pXtnf3rjgLHg_-7fzqN4HwDw_-TlnbVxbWByssBwRwZqM6vqiK1QhxSLDgfIFPcx9zrZ3Is2wo-plgBzbS39AXXAN1-DqfxeRGN09NU2ENOfQPbOwboXf7TwI8S9zeVgCUP83EoscfitmwXFjZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-_acmYqf2sHhxnJT8XTXWZAvdMhkoR_3PqmeHTRB6xsbItRa1CKZadTM6oji1uLNfC-aBGUv2c4_Se9t1BWwQhCqI3Em5MztlTau9SNFfJONKgASacQmrNzoXGpFtgdP3W92WdZFc2Msenwn6zSOimSvh1hvMtrp2qO7naR8A6NWoyJOCH0CBpmlbiTEpltpE_RSZtcV-QjllAgfKWxcGKqV7GMAD2WT_W_YRSq-hNJ2J8NyDKu4ri0fMR2id05plOPrw-KkWKTZaazUwZD35M9qpZyuMBka4E7PP4k3ugNfhN5rw5bTG8Sa7aX2mF_qBiYRwRTfC64X5t3wMF3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-T6wxikCNLuZYFlO0Hm0_F8k_nteI3p9fufNy8hj1vw9EsEFcjcPX4oCXiAWDDO880UJ848Eck2d_xQvfHHB5QpbK7JY-AQAie8wJQ1RMlqIRGXFS0_ZGeFRSDq4Y1a0zSHk3_CCMfCKsFr4o97fud8yh_x0XPGPXX2WAoB-wj2sgiHf_si1xfNZMDMhOHMy3c8yhzgLSCxe2M0oOiTZm18fWr-aiEjtJPJ2peY3-OjUoXO_2iNZIb6zj2qLJJ8I3u2Uj442GpRAzHwNa00CbFCQAnF5sew1aPk--eUZIYoZMjA-r2A3bu41QGa-5AX2JHPniStDVmJfruHh0Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMOn14awAl5Ultt_8pQdIdjkVEm7d8c5nRye5cSa6zhBhLbC848XBBomiRgEQjnFKW3hoxJcWhPbd-EeyrY0XDMpQfgH3OXDI2k0zKGhdkWt2GP61F6CB3vQF2Xh69S-JZa7qSY6Xt1hRIL-vfqXGnvUb9_0QdY518OanIOvtA3P4OdNLaTg1dBGo_qBqWEqVowoAiTRTn1B35KK-2QMHOkIaWsS2IqrXKImoaamXk6I-_jlSUYjmSUBsIJlQ2icEZunj0ebXE-swLz1hbptMEj4t_hP0QEEZvxRDLX96AYWbsEkq3ZsH8iTH6Qr_pxlxmepGc2Y0O8x2zdWwryajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoiQO89JwFFW4Ebko1wAuKxt_ELgw8EIO-hI1OPP076KNZu1doWS3LR7tctgtV8DwKUOVTow99epr_-XRctz3mkn5i5CET3rvarRH8hbV-ghq-YRi9LXhAu7xw3CmQGHxkDI7ppFvP-2t8fjo4l7ZjymOc7cXUR5TVJZmVMeSRh3shZGB8EXPwaCMbTpGzag9wxkfIhLlfvjUUWsK-UZcN59YHFDn9b-D_9Xn4Omt5RHjwYVsaSNIdsdoseQr_YMUCi6RLCfUWkXf5YC2mPlRcyUMFW1Z_YKYUF10ElogE5UkBtkD_Z5k-69CVj3bFb5nc6nxO3d_yP6pBQ5Dgqd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=VwXy0lYupCBbO0_8G8Pil1m2Bshb8N5WtBvnkndAxYxuSRakk5Tc_74S5Vc_O2YsWda341Qg1YkaF0wPwOXTtvhobYPf9FB19_aNxw7j3JAO0d9uEaZdu1RvR-fkmg2ffZnC6DzNkrr4aQxpvzKRc_ayIi6h15r_Fn8GDJxI9qDXVwifABLDz3bASeFxLgXaGkjcE5F5Ltyx64YBYItCvPPTKPT4_YP2jUskM1mPPGWpOtW4W30D0I5FtqEXR6PyE6QCr10MX0PirNYY8Ko4af3f2yUhiV95VIIe58Qs8_olh_i3ojBnGs4j3qGtvwbvgrqj0eB9o0VvTmVDivJQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=VwXy0lYupCBbO0_8G8Pil1m2Bshb8N5WtBvnkndAxYxuSRakk5Tc_74S5Vc_O2YsWda341Qg1YkaF0wPwOXTtvhobYPf9FB19_aNxw7j3JAO0d9uEaZdu1RvR-fkmg2ffZnC6DzNkrr4aQxpvzKRc_ayIi6h15r_Fn8GDJxI9qDXVwifABLDz3bASeFxLgXaGkjcE5F5Ltyx64YBYItCvPPTKPT4_YP2jUskM1mPPGWpOtW4W30D0I5FtqEXR6PyE6QCr10MX0PirNYY8Ko4af3f2yUhiV95VIIe58Qs8_olh_i3ojBnGs4j3qGtvwbvgrqj0eB9o0VvTmVDivJQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=nFSweD3sFkAswfowla0BDAjJ_NF-ont5XkdB9NDP247cUMAH7XDuGGUid6_B3hETGDJ-re0liKTiU3em6fLh8coxbSfhjXEdyIK_B9K2c2wd3GHJWds9gQM0I_zWHy4Dc4xpBTBpQhsinNvgB25Jdk9-awyE8Ywoc9WlJb6DsR9-40l8vvzhHevr0oN1pSJAfXcduYmGP7-LmkScxWLBUz9TNbat-G74gXzP3cdJWYRUu0NDXu9Amgw3gZ-EiuH6ZvivcIuNR7GbqAhWFjRNJJK4xydabu7f6X8vcxSm_r7ds-bLpnGazKjdULWnSild4T14PM8ygHlvxHeiqLH8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=nFSweD3sFkAswfowla0BDAjJ_NF-ont5XkdB9NDP247cUMAH7XDuGGUid6_B3hETGDJ-re0liKTiU3em6fLh8coxbSfhjXEdyIK_B9K2c2wd3GHJWds9gQM0I_zWHy4Dc4xpBTBpQhsinNvgB25Jdk9-awyE8Ywoc9WlJb6DsR9-40l8vvzhHevr0oN1pSJAfXcduYmGP7-LmkScxWLBUz9TNbat-G74gXzP3cdJWYRUu0NDXu9Amgw3gZ-EiuH6ZvivcIuNR7GbqAhWFjRNJJK4xydabu7f6X8vcxSm_r7ds-bLpnGazKjdULWnSild4T14PM8ygHlvxHeiqLH8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=kSrNps5XwIeT4lnBepAmVukwSa8cu4YV2knMWs50JvLTUeFMB2fk4JKaeAU75Sfl3ymU61lKJgRw4u5tgQButeCC_vpzjKs1D3zf6vRGL4KeLGgDUrSE2RSWBum0FXGC3k87Zg-3weVB27FsCh6OQrAEyQW9qYxIlRIN1FH7b3OTeGINdiPZRBvhjFiAjRA-OZDXZnXxo-qVBsCZy31jmyaJ6Hyh8zfmkYU-Vi6X9n7PSy68s_UDRws6ZGtj1HzJ0EYBPAZI7uN249xm1kSW74KVqn2XTnweyIuxrmKS16GPiXowREix2vhQczO2-gz7UgSgCGU9MSQlQ1vLqmsLWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=kSrNps5XwIeT4lnBepAmVukwSa8cu4YV2knMWs50JvLTUeFMB2fk4JKaeAU75Sfl3ymU61lKJgRw4u5tgQButeCC_vpzjKs1D3zf6vRGL4KeLGgDUrSE2RSWBum0FXGC3k87Zg-3weVB27FsCh6OQrAEyQW9qYxIlRIN1FH7b3OTeGINdiPZRBvhjFiAjRA-OZDXZnXxo-qVBsCZy31jmyaJ6Hyh8zfmkYU-Vi6X9n7PSy68s_UDRws6ZGtj1HzJ0EYBPAZI7uN249xm1kSW74KVqn2XTnweyIuxrmKS16GPiXowREix2vhQczO2-gz7UgSgCGU9MSQlQ1vLqmsLWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=pmvqTR6j3izjDfamwXuAWl6B9FYoebCw3CXpZhZK3oq1IGPSKtOtzjGJeCHAui8_uUvMTIvSS0RHPDZmeXo2LjBx8183nChlRLbM0kVKdH2Vyim5g1jdbMVgyN_nZl8TjOA89cHlS0yF_5DIdSBkKHsZqr3lMadayVrzRqQvMeED1mXhVkN4L8jU5Pf-Zf-f4mnEzBKYPr90FayCx_mN6feuBx7kFl2o755qUCqJRG95cUAXoqyUCZqgYa1aP9Vg3lrUHwURzQNfI_7ejuyIwbMjC4DpWcmK_jpLEmb7eoRpsF_pu6_p_wuOcacf7jjD-zwr2GYuqPa5-hs-mjRo_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=pmvqTR6j3izjDfamwXuAWl6B9FYoebCw3CXpZhZK3oq1IGPSKtOtzjGJeCHAui8_uUvMTIvSS0RHPDZmeXo2LjBx8183nChlRLbM0kVKdH2Vyim5g1jdbMVgyN_nZl8TjOA89cHlS0yF_5DIdSBkKHsZqr3lMadayVrzRqQvMeED1mXhVkN4L8jU5Pf-Zf-f4mnEzBKYPr90FayCx_mN6feuBx7kFl2o755qUCqJRG95cUAXoqyUCZqgYa1aP9Vg3lrUHwURzQNfI_7ejuyIwbMjC4DpWcmK_jpLEmb7eoRpsF_pu6_p_wuOcacf7jjD-zwr2GYuqPa5-hs-mjRo_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=lFe2e0OY25H4e35c890aRCTDAh6DcslFnCqsoz2F5zudO30kg5pYFfahkgxQIHcLoBKQL8UTHqvYlAoTIkmoZ1xA7csrBWJDtIhd0CmE3ySvsgNSU4roWBOtwHXWbgj7mFVuBRPpZb0Fs59fPARQ960K2Qa-l99xk0X4oR77AI0K-j__TyzgJTyMDD8njgsaT5wU9XLBM4IOq2EIl7fmTGxRg7b39qykyMHNeHUMA5X5c7nWxK5TfhHHQ8Zc0pLUF6GP8Exs_G9luqAl20Nv3yg11VcJgEtBKPdTA4zQ8O19ckFeUpbr9bPwV0jIhSItzpVwfp43Ls9qlCTmmByX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=lFe2e0OY25H4e35c890aRCTDAh6DcslFnCqsoz2F5zudO30kg5pYFfahkgxQIHcLoBKQL8UTHqvYlAoTIkmoZ1xA7csrBWJDtIhd0CmE3ySvsgNSU4roWBOtwHXWbgj7mFVuBRPpZb0Fs59fPARQ960K2Qa-l99xk0X4oR77AI0K-j__TyzgJTyMDD8njgsaT5wU9XLBM4IOq2EIl7fmTGxRg7b39qykyMHNeHUMA5X5c7nWxK5TfhHHQ8Zc0pLUF6GP8Exs_G9luqAl20Nv3yg11VcJgEtBKPdTA4zQ8O19ckFeUpbr9bPwV0jIhSItzpVwfp43Ls9qlCTmmByX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=vE6BpOhbcDcUlowSnKGpy-9vA3hwDQzj_Oa0pF1v1TUfB-5sDNtsp5RINE-ZUdeq6wEOlDsd7jcLGXz6YbYhpB4-vgYcKlSNpyU9lZfWF1JR-fhu4cpAU5R2EdeNrM4LhDcOXnUYlLTH_SJ6YLFmm8tZ6UuZjzHztPqwbKbpkxM1PMkIXCgbcckEnPQvty-jDm5jH_L8AYsdXeTx-W3AOsqD3drCQkVbwlSoh-A5LVrNj_0m9vKBm2c4sGg_pIKSx-Hxhx5p0_JGIZx7lps8cwgISIyrNz45WPlvuxDZRNqvE0VppFFQK5eOldNhMIyn3lALLQ3odhpuS6bdASURrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=vE6BpOhbcDcUlowSnKGpy-9vA3hwDQzj_Oa0pF1v1TUfB-5sDNtsp5RINE-ZUdeq6wEOlDsd7jcLGXz6YbYhpB4-vgYcKlSNpyU9lZfWF1JR-fhu4cpAU5R2EdeNrM4LhDcOXnUYlLTH_SJ6YLFmm8tZ6UuZjzHztPqwbKbpkxM1PMkIXCgbcckEnPQvty-jDm5jH_L8AYsdXeTx-W3AOsqD3drCQkVbwlSoh-A5LVrNj_0m9vKBm2c4sGg_pIKSx-Hxhx5p0_JGIZx7lps8cwgISIyrNz45WPlvuxDZRNqvE0VppFFQK5eOldNhMIyn3lALLQ3odhpuS6bdASURrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=FvBfHfqMuDxknZaiI0ZbCAc3NzRdejH1Uu6R9F7DZUB4Med653_CQFKvzKqVi0A99KQYVVDYZ3RM5m8qhn7qAKxNaAHyaVaRPswCS1wTF4l-YHH560nzDkpih2nTxdoFBIh5lnxHLnVwI3pS3aGZr1t2C-1Piu1GjTB13gNuAfAlO523zTBFkJiJS2TQigY9yhvXJOUAgiqJNZEnISCfjgNm_8hf6YRoijqnsNczqh9_Vc96qGXYQtp6gaUGXa6HhHGD7vXSYLM9gthCteiwXiZHzmriuwoPPcR8lyQHFYjSj04WGo1pi_JnflJtMS6rtbSqNeXwu4dNZ01pIGKuew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=FvBfHfqMuDxknZaiI0ZbCAc3NzRdejH1Uu6R9F7DZUB4Med653_CQFKvzKqVi0A99KQYVVDYZ3RM5m8qhn7qAKxNaAHyaVaRPswCS1wTF4l-YHH560nzDkpih2nTxdoFBIh5lnxHLnVwI3pS3aGZr1t2C-1Piu1GjTB13gNuAfAlO523zTBFkJiJS2TQigY9yhvXJOUAgiqJNZEnISCfjgNm_8hf6YRoijqnsNczqh9_Vc96qGXYQtp6gaUGXa6HhHGD7vXSYLM9gthCteiwXiZHzmriuwoPPcR8lyQHFYjSj04WGo1pi_JnflJtMS6rtbSqNeXwu4dNZ01pIGKuew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/im-NedTrCEHYl6aAOOTGVfwN1rxy6pOf-4ogj3wqG3TBag1iqppGYYmQd-UfjZrGWv7C9q8g-2TRVmZQZ74Q0VkDXYvtav1hX1OZVjzFaEZKGII1jRGjoKKojJAlgD8ZNljh4iImiyofNLsSu1TIgPgMpTBp9HUmKdS15c5hB43DADu_fm_dPSGVdbQefdLqQqN1y0XIvOM5wRgxzh-BCJ3CE6piNoQu8ujPtj6seF1RGM6DkJUYr7aOswaQimGUpL4LbOg2XvBr8DSzJ3lZ2_0mYuHN1wE_wQI6a9QNtw2wifToq8_dWODt1bEK2Q7Yj4VqR_kxE6DMbBEVaua_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=L3zOurkkdCUzc4ant6pefbZhh5EkKjY5rnZlDlt2Miap8N_By3PYZteFvisjTQivvlLjFS3_ECe-lLfplhcEwmTq3BeoCNWdKH1LXtoG7ADPAxzYEE0gG2nwfIfa4xYD9saOYqDvKjbjt9V1w75P1nFgSFU8RRsFUH_y0vdS-KB3jT-XkzHhym50Ie-kDQs8WkM-1LD5zy610Dqail1SlgQJRIEz7kf-5n851fKDoNk4-DLFHyP2UMPpP9_IWvEFzcgN3-nuTNJ7W69ZLKUOr0Atvprh_wDVQQVY-yXTDTPtUzyhF-XNl12fKbrdShplPZDeA2qR35GpvOyz0gDFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=L3zOurkkdCUzc4ant6pefbZhh5EkKjY5rnZlDlt2Miap8N_By3PYZteFvisjTQivvlLjFS3_ECe-lLfplhcEwmTq3BeoCNWdKH1LXtoG7ADPAxzYEE0gG2nwfIfa4xYD9saOYqDvKjbjt9V1w75P1nFgSFU8RRsFUH_y0vdS-KB3jT-XkzHhym50Ie-kDQs8WkM-1LD5zy610Dqail1SlgQJRIEz7kf-5n851fKDoNk4-DLFHyP2UMPpP9_IWvEFzcgN3-nuTNJ7W69ZLKUOr0Atvprh_wDVQQVY-yXTDTPtUzyhF-XNl12fKbrdShplPZDeA2qR35GpvOyz0gDFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaMoq6nmdKnzoFrMjdA8aSdrKnGeaMGllKexBXXuPVYcV72e31rcxEg5MIoEqhaivrTEiv8Ed97-nSDz6jYXCRKhpKFkEZTapgDDQ_7qf3U8G0MMQmoFWGRTfeeVq3TXsvj-d1XKn645b46ttXmKOD1ftsSeUv2MBQV-3HuBKtKkGFfigwznAlPJUDNaYqM-cpeo9upqlrt_0RwX1NxhDUt9urrpNTkPaU5e3L0GQNB9K6sYvd2Gs8FJ5qlibIdlO_GH-cahpwSbX08thBPXom-g2MjH0EKlovgii0IcBhkejJDaMuBuTYZVNayh8c3NGbqqkjsN9vQldoBIKKS1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqDzy7vITyDD456ms39laZvNH_gp1HdOCqss6SgQx8lvrDxdlxUytvCQjYqm9M3o32VLIjGc2HX3dtTRRfCV0Bo2uTE_B6CTb9nZEK2RukGBqol_V0eexwmbjv70y81FmvuxhMDkBzvxUiSuJqa0xvbZJLpSf88MS9d5s9u5PFeVjIau1aIdx2B3aEJsr-4I5IpRX10jc5HxNkcQWJaaqO45nvBg33NjXtj0iHhxl2l3g3DaKr6qOKs-DhXNWTP65L3QDbes7m5XPZrQLZdWlhv0PDufGkpKhgu5W-KL5T-OcRUw-6t5PKdJq6FyNrWx-sFm5Bi5T1MX49Qp13mnpQj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqDzy7vITyDD456ms39laZvNH_gp1HdOCqss6SgQx8lvrDxdlxUytvCQjYqm9M3o32VLIjGc2HX3dtTRRfCV0Bo2uTE_B6CTb9nZEK2RukGBqol_V0eexwmbjv70y81FmvuxhMDkBzvxUiSuJqa0xvbZJLpSf88MS9d5s9u5PFeVjIau1aIdx2B3aEJsr-4I5IpRX10jc5HxNkcQWJaaqO45nvBg33NjXtj0iHhxl2l3g3DaKr6qOKs-DhXNWTP65L3QDbes7m5XPZrQLZdWlhv0PDufGkpKhgu5W-KL5T-OcRUw-6t5PKdJq6FyNrWx-sFm5Bi5T1MX49Qp13mnpQj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7BHNopVThcWOoE0OeqJym24PjRmaM29Y86IDDB5wXBDoxkAnuPfCkYB1FmGwCFG91jnnP0lJKtzLuoK-Fne3-SlMXfvbdYSuM3Zi01oKfxb9QuyTDvaVBFP4s7Ih4IstefWYgXqKknaFZAnMFZlRR7Fa7z_ovRFhmxMY1YIycVtePC76BfGaFtqB6Q7ernv5NWe2-43ZcYpLZUrcY1eVeNDafiEAoNqYbOe8eSaDpx60vtCKmz_hHfrdbi0Nfvo8msE14l9Cpjo39R5s7V9wnoYE7pT3Njphos4h6OdFJ4KfSrNIClTBZ9b4eQL42lfSJW8G02SVB1eeKDJVOK1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=KSrosZLvL7YaN6EEkrpiwaRX7_iB-_zE_FcTTS6__N553bHsqN8T4jTKzRFW0objXANi73366NocN9_no8jKzYwDiZTzqKGtlrLWXZc9sppjYMK7135EhDtwXo_6hDYaw1S_P8ghj7sW17qFrqYBn77OdyUMUBoTGp-ALb9bNf1obj9TBUKI7XsAbm5EdMPddSd1aHpLqIaOE7IKPTXamwxS3tYkENjfAe70xdBnpg4Ty4UqtaxzUJMUqsB1-3QO6Yr9Oll0uUAK51BHVqSzmbniQzGqncKJsYR_ZWG3NMOMnP0-74dn-572wsAmPNcOOkBHhRNKEsO7F-yeJcld6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=KSrosZLvL7YaN6EEkrpiwaRX7_iB-_zE_FcTTS6__N553bHsqN8T4jTKzRFW0objXANi73366NocN9_no8jKzYwDiZTzqKGtlrLWXZc9sppjYMK7135EhDtwXo_6hDYaw1S_P8ghj7sW17qFrqYBn77OdyUMUBoTGp-ALb9bNf1obj9TBUKI7XsAbm5EdMPddSd1aHpLqIaOE7IKPTXamwxS3tYkENjfAe70xdBnpg4Ty4UqtaxzUJMUqsB1-3QO6Yr9Oll0uUAK51BHVqSzmbniQzGqncKJsYR_ZWG3NMOMnP0-74dn-572wsAmPNcOOkBHhRNKEsO7F-yeJcld6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFFk8h5KHUHJV_2KG8t_ZAp-N4UpuvGDVY-HrlT9NdXZCJ-qT79_EmZocOQjPiS5TSwxyht3XYc2eSyObvH9pihGgMRiOwaO_vFztZApoIXtLvlgmPh5eHbNNYxcKFYGaoKCQIiMzVFsysC8gkbXjj3VZ2uLD0nB0gdRajbLVGxfbAjysUmWlS_W5UZG04u09GSHTSvK2e-wf4bTt_m9x0a5n3xPJt4KSO1VOdiC7mjHnpNGfdXj1estZtzNcPQusVGRXvrXsGwHt6lyAE6pb1141qnGpnvVONNv-3Q_HikDlxglM-qArXqd6sstknTOTOw7qHc4bFDh8mvJawM9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H21WVUC4QjPsmuT4KI9N7FXSVHbG8A9rpv8iWBe71x81Ao7ChR6PrIsc6W_LGCkjAJBP9aOAh4xua51EpvqT2jTncxu33Wz5wi29tzjN_TqICdUqNA2vnl5ze-AAXMymokVNmqHYViWXiHl2Bxu1VH_TgH1jCCD6l5rMbHdDtM-TBX99VQP0ktIet8BCQbyNEk0S_36PNbKImZM_XkGkOBdfaxdDzIlGIQM-ZMmA8UBSGrn4JvoNVGT8JQXa3It1DVsO4Grerjy2tESlqCZXx2_SZJkWVe0XokmO6w7ukGrYKcoELYFGoqulswoA4NxuawnYxPiyF_Q98hjnS-18lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shoCYXmE1xl1vHXVhXuKMAP-YknjQ7KtPyZ6adySY_a2ruQ8fWrMdlZ7jXBPUvYBGGxudbvfGs6Eq_dhkA2nA3FlTLZ2tg2ss5ANcCtnmYihRt3KHg2GJ9fPUKqDn6i6cgtrPryUzIotKL1nG-bnn0u107SvGPOdbIL2d4_zViwSCz1-fiNm1nDb_bVhnax3BHZ3n-UqawvEU0uVjkn1doGuWOQElcJVrT7oCObXzam-RmQuY9rVCq6t4klXdpU7QoS06isuQL_-qfeD4N4BmQkYV-4bVlmp1yZPfcCDfNTotRS0O7Kcl86lsvWSg4pFBo8zvwq76yNa1mMZk-mO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnNuyHBXRBDRG1ITMFXWNqkqcUO5UOAk2waN5-LzRAvoFlKcnvzKxej9WgrZBGZLGSCjeNEpfdA3b7RObl0jfn7ZTtj7spIJ1WuOfEh_oJQJyZKU5640bKdMzDdiBINxcwn5BvPdoZAB57vgibM-mY5SpQGBuICX02DPk5k8tb11ZXvFVJIiJGcwylRzIc7Tvk1pK1dCBgVlVBvey83QGxCjmNBcsJiZgzvhI9km0FdBNab18JJMdfO2N1LiCyUGTVbVvh6GhWyvqwSXRNRJEU_DTNMB1M6FDyYc_vPHlbRYoLVyt83ZCL66kysJnbh2G9aHi_9tfwtgXPY0Kk_bKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU-YdklFLTBtf0yC8ja-9tS0EtFKgpRcd75KPIu_uSaXXEoda9gWEUTp6QV_RN7-VWIYZoGVLI1GJg-vYt7krdxD4jYZ8XpsrLGOHCOEQf097bS96uYuY_LkSKfKoFNQ8KlpyR2ZLFdlwo8lYJ1sDxjAV3yZokBp9Vscxkqn5wrW0oTcuoWaJkiWHh4Uwyzg3q2MlomwqbsmaDruYwTHU3Ca6bapbxZQA6liEjDqTEJZYNuN0tb6vK4ygYzHvmGCbWDSabwj1ZSv5JfzbqhvrmGTKW3tBWdw2dkLFf8IASLpL3xxupMZD6W2yKCfiwseaO9QnXxznvEHftBJaksSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-9SHPucKVCjd1X-kVEcfGn7kdnJ0tLNqUyzj_eBjmyrQKIauZXncC5Ns8BJY5RZAii-I2XsZmuLh_Ap9bejETVrLqS-Gbr3xA_h7h3ZU0CJtaPwD6urb6t8DwPgJe-G7iBUJXbusvdMCZILPesGlkpC2q6_gAXoUQZ-Cg8bjNtqpNOOK0GGNxZIEpQM6VVvd-XFDPNG8HdoMF2UwEsXcex9Q0dcitW8qdX0LjZyazC0XaoMfoQy7ewcFDiZw_zNIDUOAGesP5x5-xQvbtBxuYydEXLkRUT7p2vWErA5Jcb40Oxg-Av1dCYRs42bA-rlpxMP8c9_adaol7j9qB193w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJls524MGScYg1BZamcz_L0BVz_hDoTaA3vhh88pTjeOyCcZJ9pY85SrBE9iO9YOkK3u6fOqOexgX-u7CvNRHrO1weAPmGwRjYKcYc4tkkz57jr8LVELPcsyk6zH6ue3_ejveTw6__EU5i2gsYUcR1sPgNcHumXOo99Su0xHY1_oE-9sVczrRViGxhutzFNrhoB0JLnzN4RrmD97G3E2qNCXPz83uCf6E5F1k0ClX2n-3AipvGH2hxD4F_Z80n-OiYP6juB2ptlPNNplJlY43YrqxBNriz5x1UDTtsdCzD45U13jSls4AqM82_RWzD1C7q8L-S5CgllPIgu2glrbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kTcGrgmI1vP4xlwFFSUwmy_zHYPpGJjb8emuMJlXrxCnnMvYt7UgbgyO8cj_Dwj2rTsgABXJ3F0Y6wJsfGw-2LW_Icr3aLu3Bhd1UeEK92sft1NoKspXLhlNM5GdHRMtil8eih3IAy2_awfvu92z_qcPfSdSbaM1SAbLBlNLptH1g2wkEbtw009jgNfhBAijdMISdIr2XmDwUZN_BTMsnm7PXRvbxk2aVqJjfBk3msIoOfikNjsKcY4-_ovFMGX9iJf1Z-MLGMgyiCHXw0hQ13Tu0BUUvCXzNI1dMtiNbg_-xdqeNSmaG7s3pWBDDdyFAU8l69sYj64gLQ-E0U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4oyClJ4BGesIetLOhY3dJyGZ0PsXfDzgtpGUTQOUvQe9ZuiytfPDnDgJvPd9OvALAg2BEphr4czqVkW7hYsAtWUfHt5sKrF1e_4LnHsK1Wd7C9GuU_n0odEZmVEV7KYjWkLHegmV3X855786Y3LsDNofMW8p0pcRgFMc7u5g9seCYQkNYSKimy4qhed7AqINIh7OPDPo-MbjpKQnbZXNNS1JAB0G63OsptptrGCoA2doFLbh5WkLvCCV0fk2NlrbPRxnC6ysCKWachCgxWSailfySlJb0FfWvkEn0y-E5Wef36DM7vcvojayTvxh7LomzGMRNO9BfqTbb0JuMAISg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IufPPNEiOXm8Eqzk1DPbPgn7xmtb5nLU-UGrmDAunSzSgSTBWxgoAreo7SFkalpo-mxu1cTS1wvxB1YmyvbSvB4KXmFqcH_EH9RkYJatpB20dD-Xcbtg4APBAcH28okaQJ1NydPg-aKdqDv-BfQdlJKUi1RDQ8kvKYks4BzmkkVp306fgFdS6mcQ6_PGHocVWsIV88sShJksZQCqNSHNmbMvd-Y1NDtgh7Q7hX5KTjUyshoLY3GCoXwDuHx5sdPLGHNFVkL1e5tpchFuM-bTA9Jc7zhQv_ettE6dNJHeuZjwHTAbvrIzzhQKZj1hHL8LjCcS_vOFI4O_2cXoA9LIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltt4m3bTrCfk2SRq2kP8Xvg4A2qzNbKyIBRlGBpFZ3tL_A-iLszvH7GjXL0Q5xk5W6cB7jSKT3-4bQwaimP3Hl65Wk6uf2Fxd51il2nBgqbGeweSfPyClY9rfmJd7X7QkmS0byH7T8JzqHb5yhy1LjePE0euouvlhV9iQDrll69z8WlqZnJQKIu4OAqULtcMvDvdaOZGbg_d9IzG9Rkn00mHyTp4j2U9Yqo_Ii7vReuoAORhvy_xX4EY93Wl2iBM4rt1NJ0OQP46Afrb-wEM5H65HorxIRM-zgZM0avUNRGlfYHr-o2CcMfqQv2QbZiVHm3eWt_9yBQZemJp-HAPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx62OfdDdTf9NBA61mVtwIf36HTgsJ2kRwvtVPzgIs7fzmMrs3gRovpUxYbBaKK_esksUihvoe4o46HIZIK_I06aIOLbV1SeBzeSPH0C8EOjDPz0DQJ-kPmUecsQl6oYu80Q4Xpbg5bUtBsQYxl79Bbf2B4e35CRNUjxTCAnPtOJaJMNdR27EsU5zJ6JanEjB5PXyR85-mWWyjiNxvurs9eEeLpS80kWBn0gu1N26zXOqb-mtXjTnwcDQoxDsEKTi2cJM9aAjsFd8Gju2eB-G7drIrfe4peoZYfCKTQBbMCIz5SD6RnGSCOIkcOGYNezZ3J9dSLGYcctA_Wo0cuBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Fv3kKksj02Ht7uCIeVZ7wzyj0IM3xPYUX7lCgZ80Fvff0OrzCymi5BNC4czFrqPqFsVgnCAbigdkYDIkpiamv-D1HDhdOt1Fq2n-CshTQ4gZBMeUmin1rfpvO6nt5kUeGszHX964gow4KHuyfq2a4Lkf8utOGbr12Nn7I1R1ok3ONoRbCh15BT0Vuq6ms32jmP5Izvt9yrT7Ut6Y8OiMNOS0r-tbmDYbp79sARqjE-N9AmvfU7dTk3G7d8YmHHbec5n57OWaMBGA5cNrTpXH4bKiUqsuO_1uGb_LadwnzYR9G-i9Dabe7R26lnTpsn09BKNCr2WQhFN6QeVXkSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYgB63IPzhq6aZsHlpyhxtzuq3zNtwys7ScUArNpROxiEPxX9CMy5oQeBEIe1FEl-dt9Z5bqmE8MnIQI4B9bbrH_TNoMifxPj8QbWqcnIQBk9dT55dIt7ehk60iddrPWF7xKbzjyk3D3bxqUJAGEcmNMGHbHoOFXJ1Wlsq_W4gLSVIO7ouXecMd4BrLs8LvX5dv6h_fz3lb2hc3JCtQFb1h2cYYmPWefcZ1MiAi-gH2EWA0mwn3Jy2Rel-4gxiMDc0hu7Z4xuzK-v4KxJEXfnBA_ePGV4XcJTkp3y_dpErQZMpvHXpH71UUS_iS2hY4keyxcaJ2Yg5VIr2TpJfq-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9FAb_y_CGRS4-zIiRLP2lzmTnbgktHBe1Ee7jH1jAOsO_V0rhonNhW7-Wi6tz99hzIiHM_ssQ3Tv6O5qg3pPZ0chtphN04EETHDfA1rlZ89DdfJLI4uU4jfOWxwywn6tVLkYcrtXRAxqWEYpP1NArnCQNe3jiLl7h2gtqRgtiCqobnUhX8iCEP3Jo6Cbl_PFNHYLVra0-R7GPP0a87ZO9I_QpaD8OxMqcUUI2h7IwjAIds3bERk-7ulgtW4lG12EPevZVImukXqYABynw5q8Zv1uvUN8vvHBPvkRCVpS0D1KHOUexLyhf84pjpCXmJAFLgnajXbr2bre7C31iXqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj0cgp9uMTNKahE4hPjf1lnfD8yvqosVhYWDhyhiYNJq4d03WxMqs-T8iYPzbq07OM9HXiipyyRTA77jZh0ZbUzvsx63GdPfPCfoyr14Bfj0k62P91xI86UweLMKtrCxQpn_bLi7_qTedH6NTFCk2XPQlwAA76gL7OF3m_BZLqageAzSZ_ciXYzhovJ9690dUNp4mog-BxsbHC6Ky1MuRh351n44gE08J29RM_kXDBCfcEYEeJQo74tsD_2hSuyG4yT_YPaF4_Wy9a-wJZqGeVRyUJyP87PuJapSc8fYy1nSFkgelPWowMmeAlpaEWaLQwR7HpOJ_TW3uYcOTdNWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0yAnMZNeQozU85Ocl1tjxGw9FHkH8cjNxzTeXf7D4ibOxYa0p5zs-MDPvqPGUkvUsIenENFZvF5KkZhu57V7InAz3dxpruZzk-XBexHJLkRwH8bUJGQFTrKa9-Vv13xDA82wMxahdmHCuNrfsdKbEild2a4Y5P2GHnI_psVxS7MXPp0QUcqy4B0e89DP1FUjHxPbaRy6b5rI4DEUmE4rkfrqm0ttdZPacWRDzBt1wIA39KnaBgTYUfzx8wZ3081t88IyVVb3OmsJ_Pda8fwuYzbXN31C3wxLpWhdytqfVA3OyY1uH3Fb7j-q_2x0f-HG-v38sXbV-7WVzE1dFlNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgxT80Yvdi5lPLNRdrDBkcnT1OEq3T5KjscAOJfdTSs1ANgB5qn994JV9L1K0A9MqyYWWWEBnAs11UI7IcHzyeoHHoGKiy1HeV9WQZUCjQNYRBCRJ6HNZl_jvB_nu2NK01gGFWBbainSoerQpn2v9Sz6j8rV8uQYxBLdWkrF5wB2lNDjlcgNGze0GExF24TRqsayjj2UC2umqklphWYt97tvBkPmxXdp-D_oRfK7p5HD3AY0TX3Gf0mY9STb8t6UsIovmsiGdIJeITgFKbjWT6Bg-JruRerOwPVXgA6IxzIJWcCOmgM-a18DByab92T34ACqcs0eC8433vKWHjmQ8ZdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgxT80Yvdi5lPLNRdrDBkcnT1OEq3T5KjscAOJfdTSs1ANgB5qn994JV9L1K0A9MqyYWWWEBnAs11UI7IcHzyeoHHoGKiy1HeV9WQZUCjQNYRBCRJ6HNZl_jvB_nu2NK01gGFWBbainSoerQpn2v9Sz6j8rV8uQYxBLdWkrF5wB2lNDjlcgNGze0GExF24TRqsayjj2UC2umqklphWYt97tvBkPmxXdp-D_oRfK7p5HD3AY0TX3Gf0mY9STb8t6UsIovmsiGdIJeITgFKbjWT6Bg-JruRerOwPVXgA6IxzIJWcCOmgM-a18DByab92T34ACqcs0eC8433vKWHjmQ8ZdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OM-wlnd_aYqxyGjK4xWglQSXzJ58WtMtqWlIt5gTrVZ4jrp7BT8ijAw4fTIh12vV_yjJQCwc3ptfQw6y96g2yshOu_AmU7PT7Bx8ZG17SgV0_zqP8ZGeuGf_WXt7MBsBFi4hJG_L4uuw6yVgBXKFmG-hLkPplbbSFuY3lwRFiryekY3cguhuig4ItxlaZ2JVksz01DGXQjK78hWbjYEFm4utMEbhbnOGGBTQsiiCQTFvubESOZocV4yZMft7ZpwIpy0Xi68afrtKHGJMZizzoyFcJxv6d0M4a4Gkblwe8-giffSAGZnDFJc8NyMEwG5ibabVQJ4vvtM4Xg3DTYCLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEiMNc8TWI8kypm6red8ltg4JTZYZBMhcbnEWPH2VIb1DoF9dE8_oBHvLXDPFFiOoL0UcDICK5VMI-ltD9XgHXaQVdJ2rkGZ4CYzX-4hxEU-VU-0cmXEDQr4v0Yv537-1pMWTO5o-1tpqA0r9hfDTjPxsY04MeMuYJXUDGhZ2sxwt4GdApsWjgYOboYw5wmGyEZ9BCMURp_frA7vHs4Y5hhDXQF0U_V73wjkpHU3hkUBW3H7AqzwWk706vjDtdJNiXm4n_8qo3JRvOzkmeuVfBUzaptKeskvk1s7vBcsIfoqD4yen-9-wEFRUjBzYRnEfpCZvmY6Ja6CLPaDpEi1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAy0ViILEOeWOKtmJEibfUlxXJF3bK_LqXT3hRW3imFew04eQ3WEBioMhyHMbMmc7HTQcHpUjp9vKzkLXhMi0k5fDvwM9BQccsKs4FH1o8La-XJ7zICgs482B2B3Zf8q6XekJumvJT-raJwtXshTR2ajRHmnd4GRf6597rkTkgHrAFWLXbW3a8PNVUnaJ-f3i5Z0mmzlkzDnVw1t6m0RmzfVo7VAM5V0U4FNX8Khpkdw6reJbb1z5rE1saeUJbtHwH6toz5JYAOL6-4xVVu6U0QYxig6QL3bWoPiDZa9-CCeq902XVPmnS8tLIaC0PaNtcZB-Vj33rD6q2Ws_c63dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-uMyQlnksQ11WOfaRL6iILjWHnGbwzpkJ3QgDcbv5tcsNzWpUh71pJBwa5rv4VtSY_Ms1R5cxPKlD3huCo3BmCUYEW3z2YtzPK1Qs9ZOt__WgThn9FQuSMyzsVNvdDe6fBeTXwhofUNEGzXgPxMeYMvVKXhS15YMpsd49CIFsUyJsrqQ5WtP8x4-z6dz4wAVQzp9_mv8uz3BC-sX0pCij0VhOntsn3t2-QsXzqliJB_OBNlxgcBKSQXpfvao55tpsfh6pPCAg76E87YcBjeZFvgApJO6wWWI2KmPhuS2_B1UmbdjhYj3ygxIx353bRb09BDyiawTTb_5nA8AyKXjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdwiD4tlKxd3fqu6E5eevy6p1lI2ojxcK-zSDpxvXq0MM4KmfExP3x0g4FJ3Ea6_7lX3NofhR-nvrvCI1zwhIR7Iispw1tahcuNeHVAxECak-hVUt9mXEYVAu_4HmhpVrab38P40ibMD2oiofMXShON3zIcwkxtU98gkTagXPuLeLn4PqmmQjp7KuxLXsE6imh-SoIYMAeDyXmHdruIClLQ3RXAXmLN_aPkw2nowxsm6FOhSNHDJ8pbbD8hIB3cvnDrfRbweSLjKv8Ia7nhlSk2oizBvU9vA6l_V52-UyMFh4LOvl-6txN6DhFyhevwrDQjDxldWv-KABsn_mXt7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=ph3s_4mvCnVIAHnH3rhRybORSnuA38VnuSH91SvkuayqBIY4v83UHTSnwi8uNoqagMj0FzrhOGLrPPaT_DwjZbu6yOKmkvbWMsGSH8kFF77kyL1j5osolludoI6r7JMDUXWKrVe5SNrpkjqgXSqg8pU_dkPtyzcMm9lqnJvojrGm7FkyI8B-YeYtYFZHkolX0W3Nqk2ZFy2i500FgWSICLbvpOgxiglB0kwX3vabHeCNcnCDFgrcK72UtdflgM58nmSCoRVBxTfuGi4TzEb0bxoorSvSFGPbV2_nnGsYVBxOqj65wZFEMqr34jr-SEBQ0PaHsmIEtm9pURa7jUEfpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=ph3s_4mvCnVIAHnH3rhRybORSnuA38VnuSH91SvkuayqBIY4v83UHTSnwi8uNoqagMj0FzrhOGLrPPaT_DwjZbu6yOKmkvbWMsGSH8kFF77kyL1j5osolludoI6r7JMDUXWKrVe5SNrpkjqgXSqg8pU_dkPtyzcMm9lqnJvojrGm7FkyI8B-YeYtYFZHkolX0W3Nqk2ZFy2i500FgWSICLbvpOgxiglB0kwX3vabHeCNcnCDFgrcK72UtdflgM58nmSCoRVBxTfuGi4TzEb0bxoorSvSFGPbV2_nnGsYVBxOqj65wZFEMqr34jr-SEBQ0PaHsmIEtm9pURa7jUEfpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYbYWv849oxzVHTazk6bm1Uwv0ixnDPetxIhsFib8SWoF21y7ECWbYsME5zycQ8YmUY8UpAtHS9ayM76RewsuzmoMzF9gH4b2Qa71W0TsUj4pK-l9z-NhC6IXSu8FkiXXP4xrOdto0bz1Phv80-Qx5IqBXxtitRwzYgJ1RNxMNvbYaXg6ulmZS6ZfbxD31Hl4BVmTsQS2d4JNThNu5e_xKutBD7yc4Zy0VScXG9RyyqqEd1PNLURyds6tyBVXUHdkDlu9lTtL62ZBBH2eIVp8TjD9EVSVCRAeAZry9qx_BVeJN6kKkk2ONd3UAdFefBhs1HToQX5uFaAvvY9OfHE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
