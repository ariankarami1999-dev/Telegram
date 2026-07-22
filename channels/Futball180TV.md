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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 543K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4bPC8xxw_EulqoYaNzBvIVyExtZ8nkkurUhCK3SvGbJh4btwrl2oVdWEkyaPmpxXOAPcERKvIGc77iI57Rkc1lHatDPQOtXJl6UijhN9EzJ5tgcKZkjkmr1X3UUAewC1NoGyl03wJ7VPca__HGSUkYRQKKWsmCEcgSm7Rhx-XX3FeBkDql2o_O27De9zVg4SJlPXOOk3dIXChQtlvar1NoLwMVb-_EHgG1-Uv2zFANlvNbKhtuWAIfns8fNwz3xcuXRYwa1vcFOFewmHbki7KlNlVoOowKHiIgVgHDd1uGXcsuu7Z_WDVfFGJXpGnTiLTgYZk3a8kwXeYx5XWQOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHs_UZZdbzFIOF6hL4mY96v-H21k7eLU-iXfCtfhefeyXDES9U2lwdOjhfmuRajK3syx8LKG6kTwp8xPpI6PRG5HiSxIpE_JkTzN_eyskb-XoL1tRhUYGFljW_Zk0_Bs1x58O4cemHqYgF1mhlzLtOpdj4cg6SQVpx4fSFPUNiI1LDX9WY1jn1CwTL1PHgHaRzGhMQPcmq-UBcZ9-KnM6b0KnSGtXTZkdkT7Glnhe9qSWZr5valcenBEgzBq78NzBGG7alkZxIjo_BOTqZk5gFn-l5KFXO008v88V5U26nkE0nyNXrXyYu_oIMopEm3izBdA_0g5OZTKFE3Cc3Untg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUrjYJJIfFzLKTgJuTOgyKf3fLwozNg2qtUIkk3nEPhb4QkGaabAGkU68QpZd8yPiEytGHHMeevDy8oXmBYicXpPPx5Na1rbFwKSrzC4gO-Y-WvNG63OALRDyswiSrvJMPlAjr7nynpEHu-pvHhXjNPil8S8DMQBQpWPhqxAzzUiKB7Wa1iRY_qKZ56f6tNmY9yrRK5dKcWIVVXgsYVO-kWEioOcnrH2XNxmp9Tprt03f8qvJ2LPhfVP2HTJ7iWyIqS5gxDLZWiNh_k4iCUF55sNn6-6Ik7tdXnnp1zxniqj0t8nCAsdxICtHCPNc62OIEXwUv4AeorNI64QqKsKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrvebBrGW5flHk0bAmfSjmQM7oURMVZ3x0PU8fB1sdV9bi5Tzgr6IzO9VFWoEFOQykiaSWfqeBmubuFWZ53CLUzefdGNxFUvYYSAJtL8tJmflckGPfVnEC1nvBZ1GFM-hDRTaoMRoXiNvN0Mc0FzHzcZkkIWN_sLM0Urigiw3kEz2Nr1YZrNt39l2s-0sqUNaLXuZ80Ru_OVGVEKmRIXV1xkfEyW_IQU7grJkn6eXeiZSUQnRgQearuE8jETfgU1OyRr_mZSpFgwATljsOzbeKgoCpd8aOC32eES5vOuVir2xrQjPnAZhWRqLcAhsdWKVQlGxFWN084fTf1Ee4ogVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI06vnfyh-9BdNnF5ebUAU_wq7TMVkduXHejz7_6ep5D5CWux4XhpWkwWadJJdx9Jm64oJ_-pTgooquvLXa1oo7X1qiougQtQ2OhYAuoWoNNaQa_KJNga28yrItBc23MpeoL3BD3trZHIjs0RXIkFgVf2XkEv6cm-Xu2WEqBI9RhvIVHwqJS4nCdoUTUfrVV4t_donwYgWcyZdFseNpEWijw4HuF-g5SB0v7ioAAh6cmubqzmxf1L4n9LAjKHs-kyvdLm4jf6FKhRSaQ6PXn7bIjX2wnr9PkriS-f9j3zb5m_hcldlq8zv0pV4crSbkCUrs-HjhEUYH76QGQIhkf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0_MlbDcJWBK-aUJe0qOlywgjgZCsMGFFNdo0e39mIw-FxMnh1bpRKq9m8oewBdTwbQTZz8QY82Vk9jSWsxcwBG3MxGyhAG48D8hP0ho2Gk0hvPGvWSfdn2xyxTBC6_lb6-1ajQAVkPKGrfXMJNygu58fgjjou8cdpacFN1JCWmogdEISkq3unV6mNJ-Dm-UKnaEBgkJaurI8Fi-ogD-x1bMpNHW3VWpQeFTaTp3O9VulfhfD2K5XPsE9jBV5Gcr0q0OaVFR1kkAXzDz5ZQyS8TtgKfqCBQgimwfu8tydZbX7wzh-Yu-PI1HwWUJn0_TAeyLiSPOmJIMnA7w-0R1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlPguFKVFnNEQphagBLqSVEu1GPSrs2KKllNfo54giB5oNvEeiB6M4q9eEzxL810AMEh1i6s7OOelSNyuoY2NSTf7msAzPW-dMb79znVFWMJWyekHNgazf2MhICRlv-MgPH1XkhYVUVQQkikPm3zbiFQfZhSS3EFJH-7LNRwsgYWfTt4vp-V_CecTEe3tYIIU2SGzia3CK62E5hi0Rg2dqNX3zsCbK-EHvBUV4qwz7dykgR6kW5iHqHGEyVewjloSaEQohAFQB9kuHIkTTuWf5yeMqorrvAB9K1d63eiVIcgr2i-X0vaVP8ivP5jItMvyicmz-qOWof0L2_4Zn2-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UntL7sUKiqjF1WdAMXd-83SJV2repKIwJeT7B0c_K-sD_jjjz6hZo9ydDWxTQ6VyQEiwWApC6t5BLr4AP-8-oNRD5-Es3-ZnFyf59J9ltKNQFZ-4uXvZbpevei2uIt7NkicRblQGLFmHYlgXHDNNTi4qUIKYYuNF_sDN1rkcA7wasvfXlOGiQOeHrAON6S2z5CtXKmyuiXURzapZKdNS5_mtLjKctxBcEgKsGEvjhRH_YKIrS_Rh1vh7ZF1wzQ7YoTe6vixp-JJrCBbSS5WJAs62zmLgcpo2kfx1Fk2Sby_czfLAa1TslCRBVmjdLzjBgd-SxluNyGW8JiffwfCXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYDlz1TAvxceBMDoOZS5zFCmQtT4mFzkDBApSaVoTkjR3YEbEO63gG0YOdORovBKHUjA-AiDqdmqVX-NEA0YaWb2zkOfYQzpZgI8_JY9GG6elBT27seXJdej8pwXZZAZLS2eEz8Md1KSO2SUNHaTqjoC8SEkNiH3aNJagvY5LMICefwXy5oFYViONaIqAAgAcmsKmOfPZIiN4GKvWnbNiJXuF4OxqhfKQocOuZZH8b0SYo6xD2FroQacBdb5bfItzhFRhtADQ6DgivYC4JU9eTO6E2gj9CKhLtWA7S4szdne7k9N5Zlzb6eyKTwqa4eMx5DRKbwkFhpp1UZWypk7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glRESzEk3xcRE07uYECnsnZzCJj1BDPeLaWqO6z3oMZOJ1U6BATAAT-dJiOlakHDkjiJr_5zuXtFCxEz2D_N7vgDi5vnHDc3VYhvRKgUrXYDYU5NF6KKuf-y8KsPa0SjNNSTznx93_RJZbqAXsl4z4IKcYvRBpNDlZh5UXQSpGQLCL4VUGwpfO7BpRFUFPGCrtkGuyUGm-bry57MNTQgEve4y-WiaiEpY0H5_nfktWx4SmuU_gvq8a7_mlWxcLc7RroGssSovUqU16ZJ9svA6wJ1S399bjTcGhLugjCrTYVA2B6ztX3yJxsEgiauYHaE5AyTNcEYCVJ5i10JiNATwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovxvhk8mIgsyqcCjDLmAjwJj_1-nWdK-5RT5PcW9vGEejH1GC_-cjxDM-JT3zaJxgtbTMr6CD0W5Dsp4Kg7vEy4fjCB6grPnFGZuLfSv0E83AU2RFs2v5YCbrCN9V92ph7GXyjgUvXc1ESwruZ9HUWDCaYWZ8IQbEblA8sC5gDJbdirhxUNVYfgQTWx7JbufdLzAVzJIEF3l3z4iVlS9R-mrP0k1lpsAu7Jyt5ZW9SrfoSy-pagUnbq0QclepUDPh07844gfj5M8tcwx2bDsYDG7Yo7-JMqhYIq7i92Z3B0YF4zot4i-N9h8cR_Q08cKqAIrLn5o4XQI-oOsAeJx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukY0xtcSdDJMI0rMPE9mGB9MN3DcVd_dkQi4tjZlJEbW210JXg5bBozPTiwzSYV97lFiezuVLrtcO3UQq_FlR-AgFI9-2_WN8q3sD6uHJTubz4tYrA1ln-IlKovfv9DmQqDNXIiCCvgtzapKOOcKCAo4uU1bQUh0eUAt4VdVZB67tBPABapDSdRB0ON1jcgZqKsGhH9XHTVNBzwaUS8ViC5v1Dc1KQDQmJssisGCzOwwM1Dx896X_PVUWBbwUUObP_-sb8p0r-4aHjsArQ2dQHvr_sQHPJakSkLKnj3RsOuLX4cYP4fP-ltaCtBV8gX60z-t6hICsNBb59ciEPn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLDUadm019G0v8bPTwmKxi9HD-5z_XSDKxCAIlXq-MDRA2aeSwBHM47TEqmWd3IvHBtdiMC5vEfdJFSg19XBfb4FSDLwVc1mHQel_V0hhLYswI0Og28VpFiu8uSgqrP1naXYRPX00oXh3Z3hotVzYKTCLph_uKB9_duL1Q_DfZeqAmdjLnaqTMZCjjxoUWOm__VhJPnQz6bL-PzFXNMvOJRVNpjYVMHmGpe5PiFa0mNJuuKYh70UcorIFmRhhh0YAqs4n5Sgfbe1vKMw_-iqe2vjOuzDwcpSsSUYbTof-UJWbW5uCvCViIqqpBRGqrM_FRjfGfjReVDza3-YSZ5rnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiEgM-d7vxL0Vz5mnzRELU7AQ5lLDLtGTz27JeMjzJoUdj0og6vxg_uwtqUxLN3cbHu80RNCGuJzAdn2mdT6dZutJyoCLGETy92W5DcLTaAYOEO8xNI0URoTQ3nb7JnB97wfNZWtu9nbDG0IJ6V9gjwKcRd9wfR5MvZsz5NoqTXF6-nkDknX4bMfORWC5iMvV2pJV_PSZBOLq1sT2GWd20CNjz-WeP-Y-TFXDNeS5P773kAchg7qdPKE67beLA4_-gRlkmRbosk0o_rf-E91-qvgxOVAoC5NEvmXbMAphow4_taMMi9O7o7rmlnmD9X2yoGoMiNpC1tFCMXuPqZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-vkBnVhWthaXyJqWTwvCxDUEhi3IxoVFeNUhfc1b2duF1HtkDeMi_dYBH_uSAiqTCD6My_HwI4zYTuDvaSBTdoVaA-3YfHwIDv1JOcKOhm49I5dd7tA8JxbU937oCTr3B5DOmaWEPx_ZYA-B0t-KY9MIpU742yPW3fksoa1GBuQSJP_FMH3Dj7rxhwXXpaC-YpuB8LfPrCURNHVRNeyv2dqgV95WMYSRPKBSYKgsHewwLad6JfH93zcgoIrfKi-oB9QxNxiISFQxBg_0Iya9xEklcfhHqxBpEIAK32gVfqcURP54aSc8uNtc1_3vkzhx_VVamxbqmS6FZGGU46MCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obim39LVcCFd3Nr2BfyRK6W-Inhbbryl_67rMFSXm8EwqUD-l3a52i213tIFU-sMnlL7i67DPtryPvXrzeSoOsabe6P8yQZhZ9aUg5o-JdNSQ8DXNdKu0pxcPxH5p8bQJKCrYwZpCcWRZmLUmo3tUSRmD6-9j37JgZ1ybmLwUvaa9L0UGFQpNjeT9qa_wHcrJVjIO2P2zyWKGgAME-_VCm3nDK13aVVFj8qxmehXntj5K1ESUWavrzCOf1Ftm812BMAOqjEKKdtxPottOREXXT9qq3C_maOaQ7PQXL_Ucr9rk-F_QuyAWqoMYMAu-WIuQODkkmYoS3ZI6TzLbbDsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMZ5cfgwCf940Ov2GZHLynfGwQ-b3tLNSYFs6rvFht-58ELx9Rz2Qh_tWD6kzSXGK7nLDKA4jr-0r5BIzXiIAS7Md3U3bxaQF-GD7yWzzt01MAWdtHTtZiu0KVNZU9VwHoBbJePcnvoDOe5VYAq7Q0G5utaGBKzEFIqc8vksiklL2oOmF3r9h9VU-V3Nc6iHIq0yOrTggfYHCxPhxb0mR-XUqPhEyIw0MX-BzL1DQMSe8bRA_uc_wCo9YC2mi9N4fricZAs8ZgZ1nyvfldGp110NNBD1IXoydX-OJaOz4WKD1KrXVGRdg0Rik5HOOZ95BDfHW_qpebOC4nJ-QdELzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7DT16PZENmHTdTv_d1UzGWG2i89XUYflRi7OL0-E4PgJWr5GOspYfk28n_wQ2p44nxWEvhuL79-lK5v-krGaaNVYJJ3mRHXu5lUZoxW298zl5PN4Yx7ejBu5WLiyzfCFAqlRe-mXpnZYtDy5j3h3gDu6hwISYkQn2Z6McebBJv5AX5VZjeCjmYn2MVjqNGXJqOSMczrvGsKPWxWaY3TA_AyLxmYuXyjE-MYtE_HBAuF9yd_K6Cx3V4_iEe21U02Fw8DBdr0XKvbftQ766MnXN3t0pa8P3jzmahlOK40-oTUo4E2HHDdPyMvPnvLUgOGB9gB7T0FBP_g48-jBe_WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHDUiLAOA-e_-mL7f3snV7KiTLIyFw7b9LODteljFLFvTwlspx_acYQT1Ba1dQUYsFUXjP8w4DR8_w405hU4bfAsv82fbGYAffbsNzVpeTc6jRjrq_xoGGfPdweLA3qEseA1Okmp8_-stNTNLo5OIi4OnWEvjUS-6h6cZlMXMosLSEVE5mtzInWHy411IXOSHl21ZLmPA3b9nynvl6GKmkGikTs0SoungEiBMlZnRPEirZVot6fhEPQ3CUN9pi7glS9hA0BOdLW5lVPON7lqkCNJOU0RCTXsE4nnQnjBldMPSY59lHZ1Sx3nKBi8lCitW49YZ3YJSI6aa6g_Ugpygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mocsea6HIQuGEVQQgOCWw-Pog949eR6dGc3WiAr1HbVuxcnQ5iErGqOCpWP_2pa0tWl2YeEauKkTvQqyr4mAUSb9fDXY0vuk_OebXfpG_lGpCCap_MIsjJgpzb_7duc6EVYjIMxZzoKKBZzRwkDLMZPQOKbMLdzNCZ8Zb1BBIkwuIFA0melR6wbxqlAF7gTnDnC54Y5vGTvevf2AuCKWWtXH32vT47kHnQrnJ-ZKARrjDIOdtWhZsIcZcyrp4krPuwiG1VJVY41Ifb63jFuVRhUEJWh4GsLZsMj5iw61ks_JxInco4rsJVR_macVcJ1zf_oTle8UQbY-bJ-WY467Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIK2oQe5MF1shfjF1DWHxa9bC_rHMSEjMgpXbzm5JoXMSHDU-SmqxzfF_H44Lr9CJ3ltXm3FzEohQAseXQvGBFv3NUYkl5tt02hOy8gvhas6kKaYFRPqsElKV_b8jRzLLFJs9TZu2ox56nimCekAM-J4HvTMr42TRlleZCsAJEmrOdg_5y2FCt0utJ9Tw0aHrgv6p0cX6ZCFT6zvxaVoDxqbaBsd1GDGiEN3ljLDTixK1MX04xXuXsc1OfmAePFDkdcPIg0Ithnil6Vq8yrJKU0ghdpO6cZH28oPcjCvviyRMvOEC1FTI8FBu0XYuVwHvWLnyTJLlwiNaOd9TvPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVG0NPNbAmhsFr89vLqGfJVEWm95oI6McvtCUiAclUS5LEUT63LqothvarmlfRC_5b1pqRU3k6avb7HBtp0K9dHciPqbRUO0CpCMZzk_fEFUuw0UXbD37LCYjapbkZ0qFwoIfK7b0lq7wYaJW7OdaaxltCC-8dJMuVd2C8JQoP7vRhPws5U8-BN49uDCWhYejzJmUmzudVPf-hmSag6GggIbYXyLUOBYofaReqLW0DhKzz4I6gt9a8w9wfrnlNB-WBfXahgKgN4nicb2z2KvOuF0DuqfLlURnpOECU4fpe8Zo19wStX8cndbqVBLhWdoP5OO_Q7VwAqtz9SlQiIPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNBhMv4ZmWLPfngNjcJ2FrGSxI15EEppBk0k8Gy3Jtdqlay49wt50KvejwZXIkr_4u22XAJ5xly1diMPvdWoB2FpAE-9dcv7MV100Wnw7PjSq0-l9TRPWLwVvVbAibpIeLGqrQ1Hu9poKvEOiNE9OM4osbZ2xlN4iehDwHweuYNrncSv-aY6zkrXbOHMaBs6iOhf_YB7stfCQYe-04nRj5hYGlbsNAeZeifBWkGavf7WhzloE2xAoM8sgbns4t7Yj2ewfzHfNGtITzq-v2rYqRlk6fJ2SB1ucwA_Y-gHapCYKgkD0D5TgXH49i3yadK3kFBpSUbvZMNlFdrS8PYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ArHT6wSn1aJC07fih6HvNjuEYezDdQFyRmUSFDry_GHi6xykDCywQXNGC-u0ZD52w8u0T5IUQdm-LTAtVr22c9OjnTHdWcuEYECKmr92K3a5l1xjT5EjTP4G59hknF1kFYiQxzqgnZJTQYsq9AjcUqga--O2PJXBFjXa5TlxvzypfS7TD7TPSIMPKwrQgp0ZbOHGEy-b_1yh6zAjvF4a7uxpUX0iZzwcRem8I_S-XOVFCaAPiupEu9He37DI46LcKEXfjNBy-nK4ZSHIAxhsNtyX1TcBw_IYQiMCT1JkLp7pfvMjQz_zo6cWKOkby-oXOLlphD1h2IfsmDDxkPvVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJZ7CreKb5xjU4HmpwMGRhuVtLtECGMTgiFDM5kRkew5ZiBl-AowIVijV8fQ3ULCgeNZFO9yKhYrSXto73WbIpTh_HFNFA7FoHP2xrWXx0xPXsGoXM17S7RXvFlXoHQjDPotWBajdZAej2-hmfzvG0_aS_uVSZPilKxgP92kdwnobOu9Y6IdUlwHPPc7orODIGJPxUeq4bR85iqzBCVrnWuECEOF_uo2c0LMSZkQPc1HHIMaXMFSPGLOjmnRmlp_hwf0MXa8B2U-5kKgiTgqr2GU93cT9ugjRLkp4tLP6D3UVhCCWDX8B2MOm5o7OglLbsNxjBTowLp82bqsI8-JqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvryqQ3tAq-ex7rKZhRlKtGruYRbcagknVC4RDjUZx8N3r5BUDNTVzhDVeH__2FU7mYNmymPL7hyhokp-_Pg3PJCBRJv0nOWLZtec7j8cJw7vHMWAuZ0-Jti7fchRPmrWwOBqTMpOXmO1gVkOAcK4_MzLo_EYnxS-hnsbgMmTShNrmZ8GU-PV39RNsGyl_IIyuNGZs_A5zM_LblIT-D_XKIxOmyOW8tAIE-gvl9m5Sh_JzKnMH2oyprMwDSo8jZgiICROebRDCLZvyQEmU-zhXZ5QE_zWNDU_mT6JwsrM2w7-a5F5hqiEDiUWY1yjJjGpOQVEKQxAnjjMLN8tIBI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deGmcBaWZKlpeVBQ5PKBedUZtXX2_IPpWqMwmgo0TbD5gcZpx0iK-B9vqfkTquJHWSwkFx1Zvbl2VRKMf1t2upinlRMOpxW6eqIqCZqmWLSeHeHshonA7vDvHcKkN_WLB7fG5pGkEUUSNjogigULtVh7BM0u2vivooa0Pb57bPc0LgFaWKS1ON3IND_uHJvkewpuJZWPnxYCg7dH3YoE9vG7uD6rvG3GRsyrfn6y5grWEnWtnOgXV7zjsK128Aw3gErZyHwBpjYodd2Oq0ckb0s7DsTMoSGJjObVOxnbT_DjSfHBL8KixXETGOzyrf1_DgXO1SLGVWaK-_Y-bqIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwg9p8p-xbplg0YBtpdCDrRcYEOgJ0qGFTNvZHG1GXefnsYBCTrf2FknG5EHwSJgDcR7hgePyvgSrkPg0RjzOkKs9SvrhzXSXiOwzr7duY4uoQaUO9OW9zTpVZHrmIEUA1LJKgjX2D1hqTi8J9Fu251yOT_cNvZ2EsZYFweipayILYVD-n7twVLATx26A4_IH8cw1Fix-HqBn4YRfIiCYXBmHZDTTay_fqTmgaYYaQOgYpmrRDDLPgVMMZD5NkHc3QvdQ16gfGBkgy1Hc8iGNIqu69SkkCwi_bSpRhSCqwjaEMe6vGS7TscPGzPv3Gu3hFlp8bqhmJIZ4Ic0ecBcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGxfwgWXyRjxhUbj2FVSveo_2XbEeFN_TcA-HnHL2_DiPUg1TwwcbJNwQCeBePPVXmedZBH6tkyiFTy-pfDdgdUrZuE0tzM6JdXGf7Do9I9iVUr6RA5oO4TrORrdAwM9e0DCZlNtMNlJ8ZQ5oTbYhp3uCqtgKGXjrckM5m_xx0YS53pUJJqO4KisQELCHhYMrUl4KFIbIkzRljlVLn4pK_e_F8utG9_-K6ZrVcXBGjHUd4mgN6w7t0nQwYJHhc7ggZrF_Uk0SxhoqP6pCcny3jHZ7O-bALhpjNy0-polKIyGMWaEgunor48EsSpGJ8LYBPehoEAbP8q8apFsk_Dtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWaigHTl-TAP6glF781TMC_J9jBQQi2juJo0mHyqjyLJq7XtXNig1hNWf9bK-YpqpbajzbQ8RBMsmExw8G04UvvDruoHM2dj9QrpfqvzhvjlW7tTvUjHGr64PkHqI0iSGa6hZ_ZhfztuOSy53CJBmQSvv7uH6mI9w8ZHe-ta-1xgakXdoCANSYGFGqoq8UeXe9gvSmmRtftAgyHr-vWs04qLsBR4mZe7_Yuo09WLu-47-DT-UYIvyXE6hU9FT_GgbaUJd__Ufp1_hdhRVhO8tbqzx8DSPf-6IIvorKVh3W9snrEZ44RVQ6Hdlotyb2_iR3DI7qgDg3vkRx4IqWjyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlzMQ3G7p50a7KUiAczKXpEX8ckQ4M9hUyL1T3RBdIFV3G_UTL0t827UM8t1YSdabamUIpJkP9qVsd38nSq2MREReoPBkMn76GUL7lef6N1PIr9o0_sPKkMY26h25AEFgDdmvr0v8TGAYLanzIqh41K4P1wQ5-RGOv31ExgerX2E7cs0UjE1l_oZrO-BLNXPwCjjRbqXLkoF7l2ZscEGJMJWrCXbl4CnkWoI94gGhQF-b0YkAUgPo6dpQ06kLCuezahvUexHpuC_E-eSUBGtWjf08kJMaWoa7Wf13h7VBjpdPwsFwZffXKnscMT86Sry2LYsEA73N206hMEaVV7gAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=PcvTAKjsKWMz_Dxc6mv0btm2FI75JnUJr4FRj07g5xrwA5i2OqWZ8-tLaucqCnfCXFFptIAZvi1DTex3s7AGBSEOpxiOW_c2tz23r3vI4cIOy6olz5qbkQYo2FGY4RQWHISTfU3aRRACQu-THgXAABv-aGpiJ9Ue48jz2Zo6bhjwVjT164bgK340MrwROJ1FamPBEXDqKEl1bKirwt318pDrbDBnbnpEDp86y2JdZ8iVqZk5UrqLcIbwnu_HVXT9uoDnKRYQdw8OUpAmfkul8q9JqHNMu2BQCUOgm1Q9EMdf0IP16RqH2alAyKE6V6YwOwB7J4pDviLZAXYawVDD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=PcvTAKjsKWMz_Dxc6mv0btm2FI75JnUJr4FRj07g5xrwA5i2OqWZ8-tLaucqCnfCXFFptIAZvi1DTex3s7AGBSEOpxiOW_c2tz23r3vI4cIOy6olz5qbkQYo2FGY4RQWHISTfU3aRRACQu-THgXAABv-aGpiJ9Ue48jz2Zo6bhjwVjT164bgK340MrwROJ1FamPBEXDqKEl1bKirwt318pDrbDBnbnpEDp86y2JdZ8iVqZk5UrqLcIbwnu_HVXT9uoDnKRYQdw8OUpAmfkul8q9JqHNMu2BQCUOgm1Q9EMdf0IP16RqH2alAyKE6V6YwOwB7J4pDviLZAXYawVDD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UESc0sWOoucjG3RTHgF8PuqYPrQq_GvpaxUXdUfjWnRz-c8K-RpRLWrriEXmwsvh7qUf_PKjDPWl28kMm6M93Z9cAO9A5UFJ2j90G6mqR6y9o_1vQP4SK9a62ml_hSI28F2JaSulDWgliB8Y2ESD3LGeNOGVzZwDrscwHieZyG37DudIfN67nmJywokdNYulnIfI4QNzxbcenUHkgWRFQWho9OokHnenbYB4Fz-NsJ-qhlq9lrxqVAnXehO_-gabCMLeHtN0GM__tmWO8i5FgAPol59X3f9u4TiB2Lt_gfJF5jbDzaQ_dBHzxPf7rairzNxM9JMStbstrufVb-ynOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=Q2rlpCFWr4YC61Jg2uVpMwQsO5IpQPKPNMijQZr-F_C_yRrfGNxCZAa2AVh9sVBgaMBDw8Y_DQ4H_POqQANVHZow_N_UPFRCqXbTGunWpU31p45N1lzYYyfYqJMcqCSj_D1aYYKAdJhxa55fwJ-rQ6tpxJ_uwZ4HbxYdhjNHPmFxFSPUZ2Iuxk9kouWo4wltkMBzn7NA2cuhqiOu-3Ai98LKjZx6G9jbvbMzz9Rqrik6Kr_gmuODzDRFsBfgMvv6xIssh80-cT1GHkpzWUFSIVHyRYDBWX7e4tpFkPF_BH8mVWXv7qcbh9hpmOWmaimG4Lhu3nsW8SJPFcmRQBHXrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=Q2rlpCFWr4YC61Jg2uVpMwQsO5IpQPKPNMijQZr-F_C_yRrfGNxCZAa2AVh9sVBgaMBDw8Y_DQ4H_POqQANVHZow_N_UPFRCqXbTGunWpU31p45N1lzYYyfYqJMcqCSj_D1aYYKAdJhxa55fwJ-rQ6tpxJ_uwZ4HbxYdhjNHPmFxFSPUZ2Iuxk9kouWo4wltkMBzn7NA2cuhqiOu-3Ai98LKjZx6G9jbvbMzz9Rqrik6Kr_gmuODzDRFsBfgMvv6xIssh80-cT1GHkpzWUFSIVHyRYDBWX7e4tpFkPF_BH8mVWXv7qcbh9hpmOWmaimG4Lhu3nsW8SJPFcmRQBHXrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw0zAlFCdoO7r2kIOV0ZGmaYQJBegUzwO1NiefLw_krEJCM2RlIWThfav95ySESWkUPSGIWMXqo2cRxX6bIIsg1xfc3bsWXsOE0-i-z875saU-FQZ3-unqferOwK21L1hQOlCZ2IPBicnkq50NQsxif5LHWZvRqMVr-7816yoxSWsedG1eowF6RVIBk3dB6hl99dDqz15WvoTT9nQKoCJwvxFmwqGYz-KB8f_zwsoeBt-LL3Zv2-HP9zihn7Z7Mb2sNsYoECBIzTez1p7OfZCZkEDwTEcf06k_UJIUFPx15xGLuiWuGG8X0a-SEpOm-SbtiwIxBh9yOkMGexlU2KhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=jWfyTwPxcQB77byx_WKvB1a28gNFr-0c3zk71nJg7WUPecgDERWfJbJ62qivOCot_eK2D-XlnDk8z1feKCuWW36VoiJ_n-WOhKSr1FFt2Pozt5xmB7pC8nDBAH17tLMX5JQPLNCzPfdSEgB6yTC2WhR2113NDfpgBLzgvKL1NUULEstXJ8kzej2gZGSn5qwXTF3Gc9aH7ul4xFDFK6nUmlgOe55Rzgap1t-PWs5da7hjpbDAz3pNIXE4nxPOaZVkdFc9rPYUCWSioue7Y0v9ZDmaHuV8UXUUtZZXJRof6kU0eNEzDudYvzOX2DdStWCkcKn8b-fqBGEZDTIuj3exfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=jWfyTwPxcQB77byx_WKvB1a28gNFr-0c3zk71nJg7WUPecgDERWfJbJ62qivOCot_eK2D-XlnDk8z1feKCuWW36VoiJ_n-WOhKSr1FFt2Pozt5xmB7pC8nDBAH17tLMX5JQPLNCzPfdSEgB6yTC2WhR2113NDfpgBLzgvKL1NUULEstXJ8kzej2gZGSn5qwXTF3Gc9aH7ul4xFDFK6nUmlgOe55Rzgap1t-PWs5da7hjpbDAz3pNIXE4nxPOaZVkdFc9rPYUCWSioue7Y0v9ZDmaHuV8UXUUtZZXJRof6kU0eNEzDudYvzOX2DdStWCkcKn8b-fqBGEZDTIuj3exfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9vULwbpum6--bCZMnFncbEK2SR_lVEFDpl9N-x1CxNjwX70fXJfuhV2-sEez4s-oQcT6GnZNRRMu5TP1Vm8nw9Dklm4gaf6xXIvexzvk8AyfIPSa9INCDxPscTIIXzJSLo8vRpL_LMgdDuUw4KK9Tm4YcdUn3XUpDNwVmjWUq6CvdIcMsRqTicI4XpsaiSGr0sx_47FXPiv64iTgp2bG3tlooAOy902SMtipt7mjIaDfvE9cXG9wnCf0UpShdOp9eex89MBOZ8grva113tdWqtQqOnVLJM3ykEslathUvEqx5wODoHKfgs6mfGXqzMdq1H3Hz5V2YmZ8H5MIQSq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjNi-w9ChDzAkzeSp2bCKMFq51nAJp3pOYTIb0AZTBZvKaZSkRV4BptyfFuBy4Xjx2yOg128o6RVV4zvt498QvhRrLWyod8izubzTaMVC3c_LdRJo7nZQ0rllOLWlT8JaZr_aRIWbZWraG225qh0W0UhpbBqbbu63nLCrxGuOdvIF6W8dFqryO8iLbB0ovHXhb3_-A7EvkKcEj_TGnsCdQCmyeGQP9j2EnQllREkhA4jh7OSh0IPj94BOWJSFmtqrSOn6FCpvPOmSQlhu-Au9qEv547qoPYqtXFWTHCyOmNrIL8XwX03xexKzXBKqefjfVMTZ54dG-PueNSRIjGCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6YL2dl44I2-EZRNG5tky88C_p53mHQWEvMMNY_8KokgAENgDrjK0XqEVrONnN2lTecl7VqJ1po98NpXI0g-pBhi7Y3DLDhVpzIgZdPL5fjrp_XSVYcM-7FU2suB1Dk9GUIGQqZawcWpucfEtTInw7XIKUj6IveesgpT5gU6JW4btT9Hhlr20OiYagiY7e6ilJXLdlUtEj0r8kQSBIClAWpCkwAoW7tiuPimzrxxtw6z5agsVQ0rXT8E69DLc8U5ziRYTYsy34FK2pCmwA9qAjkaVNmwIvVhHSrEg_FiKH5z5aOFdYloCeHJoOYEC_4XjdTThuX1CmbDyBdmz1yFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv87mLWGMjgbLzlzYqRVfsWHPu5FnyHteCt21AhCeSk9oLzdMM6oklYeO6wP4I4g6hsLSbQ2HcetIBoQmbzjdMzjXaQMSYZ-OfClBsE5p4VJjV7jDkGXSzJOXufx79VBH23af9H_7sp3GMv2n-YrodHLH3eDeFZlEWpMRgkXxet7-Oa01v-5b27aggcAqIEj3YtXnvyJJ5kT_Y42Qezv7goTZLIdxEpT4ujLS_xb4EzkgMW-7_7IJw5kzyaLKBMR1PL-nt3Z8X6PLnr73qVHEQjYrlM8702TyJwyaaGAx3rO6Kblh27rQK305GoaKrYQPQF1x-s1s15cn7hnenc1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNqdIF-a73ApxvGCR3fFoPymwxF6MBtHOs2lZe_8GuDS7vDL_hWFaMmu8oXM5c-oCX_SGmw0dZQDgvKNukJ0Uutikb3aQ9MsSk3YpGC0vHGKJdw5Ga04YAkftbIrdS6-vSavKnpwgAsc65rlfi5kspb8zwkRGXBq3nPL-27_PtGRVJ4BuPW57PqD6fOYyk5YJVXc2_cghLTHcA3hYvLM4pEMycsyV-nc-9XycQWbiN-L9hJqf2TczJF8Xh2vX2_iRQUj5-EB8tjDWesXlbGACpHYGCmp0V8pYoXq9DNVbPa5YwYj30EtL-XSGFurRp8Oj6tFmPa4x9NotFOs4eg2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxVIbglWA_94c7VZnR2gOBjvXyKoAN01kiIYPi2AY6_oeeN91y0qnnN2HEmwABIe9n8lVihC3IjPr61QgCrPnzRbkk6xmgfPWsj0N5z-TvDXuvcN1CDzg-0V6pMCqnw7IlGODcfQp7as1QiZh7UsbAG1vMm6f--p_s50JC_0eHBNGwdMb-6CuCukGk0YvP8e2b0Nq-2o0X42liMfUvCZcT2MAbegIpaWRE8VcPWT5uyGGIqgs8n2TCBYqDVy7nBOnFO3_OB1NRdjTuNZHnfy2NUyRjGRqB4CmxuODavW-LEF9BTW3oe_pcHaOyHaRzUnee45G-wYToTkVp7NhHD9KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=mJFV7pR-3r6ZWMJ0PwJrw_3rCy-a0iQ5iTKDloNQppQre2Cmq-zUrFbWCEDN1MlsAILSonoLxDjKp_uohdJzzs3V34CnQpNDX4UIXHpREe3BBLyEhp40Ct2_N_ccjnYScDEKPi8WEKQvoDn-OOqKenqnEN5Er_zCxT-YwfcmavbDRkfrMod4nHCSFZ4TwlNcumu3LC_J0RPnVCVWcZeWOJSBikO8LEiHJgXeZmNyIsScmDr4Us8uPr73lbuqr3BNvqxLgDdUyTVEimjyw34wdCIjAaX2PKaHJEyKanWg74iD3YKi8Yjv4Nx7qjyTGmIwDZwC6p6Ov43d8Hmy1mr29w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=mJFV7pR-3r6ZWMJ0PwJrw_3rCy-a0iQ5iTKDloNQppQre2Cmq-zUrFbWCEDN1MlsAILSonoLxDjKp_uohdJzzs3V34CnQpNDX4UIXHpREe3BBLyEhp40Ct2_N_ccjnYScDEKPi8WEKQvoDn-OOqKenqnEN5Er_zCxT-YwfcmavbDRkfrMod4nHCSFZ4TwlNcumu3LC_J0RPnVCVWcZeWOJSBikO8LEiHJgXeZmNyIsScmDr4Us8uPr73lbuqr3BNvqxLgDdUyTVEimjyw34wdCIjAaX2PKaHJEyKanWg74iD3YKi8Yjv4Nx7qjyTGmIwDZwC6p6Ov43d8Hmy1mr29w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVwvKY4jdH777ALNsfBLbOcY_VAeIUAxhyOxiG4-eRhlv9eiXCP3YGbc-kqdewiSaySuaTAz6qDoEQsNpTBqbIN1zpxkK_OFo8tJqA3uiySFBIQ3DmPIAoaSYSsX0p09fQzY8r_0ETWF6ncA3k0WLg8MXSQQYR62Ea8fftmtQEvqblmjl0G8G0Fjo6DBErXTK0BY9PEdmwYsdZ2dTHGhZ2G4r-HWKcgKwqTLsxzZI7_lJGmqbsP9XypP77nfgMvR2xKiGyjbRdQUF_Hdb1_GwGciWh9WRKqe6rUEXHRcj6YnkPNZ5eOSPZB1cJCc-2LspI_qakkhfDrXnnksE8wBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm6hKpTDD-jhTnD3kVoJTAeiDpq7AIIUcz1fsgkWGMOpu-V6rGgg7od2qs2GkjZNAjljTvsi-0zOlQUce6SDUtmOclr3oRL9xxi2U_l20wmU0aMm1RuqygeOxkDSijdzhswXETUMXvRMhc7Z0bbyQomj197OKhN6Rc02dVzMMD5XaJf6US6_aP8aTKCjhc1AnCqA71voBFq8eJh0YfIQHxE1ytxkS6wmOPcSu-_sLaRbf4J1PKekpKIzyPDHUH-tLKJATtO6ExEuxizKKRifXTFF3URtHBf1uuOncL_YQolW9CiUAFKTqGpgRMixxEC0de1gh1OABl6JbpZaBXdmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYvPxM1t-6ZlN_VKFjUaCJwekjnbd0A1yubEtjHYDGnp2GhlNb5XoowfqVV1O1tEDzOwwHje6-YaM7LNwdm4DwcuLwwEB8ma-Ihw1nXehrbG3ErVY9xKzFT0a7wBJoPMJK1xmT7WsfUbC2yrcz43VzcZ5pchhJuClNe8zgNNf19gLitDZ3T11x5am2630M1EVrjDckuloBkOVomX2s4Sxm9ycjazQInH_8zrWqu3FBfwk0JH-ExQ3uSNppuTqyGT0mfEP6JC1zMEo_qyagU47DywOeNzuvxKdcRU2ztjV71xr64tsF4dflrb-_qLfOHOoOUmlVCzgawslj14DYmtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATCMBvf_7V-72CtPZ5Owpd5QJHCAqBKbWptHS7A4Tn1PQ51MQV5GXu8PYnXJD06dWP0VoL4bfu9NQq5eJPTgiHwBdZsQlPfPMeSOo8k7goQq8yXexE3dQ_qpgVX3Te9es-w16cCoc7zpWIHOFMGQa0r9w4-B015n-M0X_4ix8aYzV1n0Y7EHPucHngi0RuJ-2VuKyAtl8MHURf1nx1YbEtcCpvUdZXtQoWbBaL482YBKkuQ_Q5F2r6LkYAROaWvx--_ISWToZGEn71YPdYuPaEqBEXZEFEbKyYA3myUMai7xMpJHMbUGTG9XvR9klmTJA2CnJlN6UbQTVcP-YFs_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEbyr0uoyGqjq2a4gZ6zqjzZc3o7koGAWSyZ3Q7XLvqLtj7wOX-w8uXVvXW1DDk0KDOKcqG_M4ecj_V1NTkQ3b2D8-x9yFTsqWiC00O5sKYwJKV2pJVWcZ7r4JE90P9-Mwfhdtq7LwjzDYluwmW1khY55fPDQ2JzMymf9FV83czWYSSL1DiwvXF4vSUZGsY1tsaqW5hhgk0nM8WCHcqGR9-osmbWrPlcnzTdsrBdXe3zbQ-xVVxgXz2ID-trVuZ4l41MviyiNE2eAIiqLY7By4lbvW-beUVPs17x0tifefXl4f1n0dUPfe101bem0YOiJ9PdWy1dtSpAij07kD6C0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSg9giHaGEkk9k_lOAli0dhMWaP4qX-KlEpoJUQqFdQvqIHI0aM4Iwepufs9rg8ZiZOG0zOlXDspsG8ODbBac0d-F7nANDG7qBq2tq5uKpo8gjLIxuiZwEuZQk1UqNNTGw9w2NGIAyj8t-JC4II7X5bjZGycMhoZEGyzg0TnRgTWMe1kRa0hYVFSFCHCXOpfhWWcaiFCjeQTRO5BXGGKQs6x0pgHvaeEHqzzkQTU_pt756K9ROD0xiUMEp11YJVcXodehrayrVPL4l5I4X9PMtUZHNDoP6LABxd6Nd1P6xtg3H_oZo8zXFOSeh_whYUyaoyW9mDfMUpBXsLPoO0GXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLs9fxS94WI4-MFWtfumMqjuTmTvRDpu_8OwfffBPq5OVK15o_mvAjg-DECH81er8C8hD08u_HsC-TiK7-KplLArFOLZdXDFe8fZ4EfaGQlntTREx9SWpKjENaVv4b8iT-zfzsfF1QgNl0duSfhTlmUIaA-HPHe1FUeTjaM05wdl03Bb1XYVkL-Rao_-nP5vhc946p1hYi4JpkX4W4B63NUr9gou7_VDYNsqg1jzWKqukXPZKGhrkUD6gcqmntHsnrhck7ANR50xUVO2aTT9CGRqVUSIRbOz8CeOoRrhPYaasNxkoVIY-wFsTNXmtlOWrsRtufyjDf2ELZt-ho8wKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmzyUavu_QSujzJropIkUgc17cbWsBLd6Q_ry0_TXr7R24nhnZTk8oFvXKx-Y1O7_VkaNynQWtwxcFfLYu9RN4UOzvE4VxNRe8jp6JpC_LUkVIrKIW0d1Mqz28V1tMmeHRuGqEhDxY6LJkAP1QBPtN2O3fYZ3d6lRKdEn1TeRtXS5xL_MKMuODqMd_JgqCcp6inNL5nm1vFnAb073rW9BYzSg0xjPmoUxP8_Pna-zP4B_qEsli6_rGp366LefdOfkR5fCs5ggzqL-aCBmVqqeqTOUpwqhRSb_anKp3l9LBtH4Q6CcMbInlvK2-1RvE1kom_BRTCAXNN-4j5vRIvi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV1Sg0IlU3IqO5CNeww3sZHejBTUH0ag2Md0itawd2Kk_Dr2OE1Zr0MA_2dpxKDIS7s0qnLt4l3i3Pae_-36M3Re7SABisuyUysRebIIoYvjj5Kn0prLpIz9jdTHeLMVsO-HdBjuSdRz6nHRy5uKPeDTfRSfKo6VuHnLhBjGIaTt60l6nS-KFdAchFyaBH1OlKF4gnnkldtp_Bfoznf3wsRp4SHzUutTqg2kLQIcFA109LePeARFHRuRFL43MxvsP9ihefTc0JH0jG7MZckZsiKX-Ll1aR2SRMnYP0RRr6GL2b50fIYCvTTZDedWGSiwkKn6L6f1prQod9HQm7kKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jovusu94TIrMokzsbVtdq-vYOoIn3qUsFpiyT1qhFxo5_Zhrhs98UZYjrCw1xFbLoSDMorIj0ELPUSyT2Uh8ANGEMbZZbMfirCUsxc-v3gEpqCU9216M8BUmizZVZZ4eUalNGl7an7a-Y7zedRchy9MaiAst-QDfO_d1XKIhZgEshEGLWNXxBrk6sof2FjOJFHmoqyrTDLzWpSI6FHBp1keKD8HFVtImU05lOaPwJfM5OrfpuFpZtoPzB7oRGrU6VEddggg3hHGxOMxWZfU0MG910SPGSn81KTZG-UbwNtJh0zpLJtUjkNOT1P0-lm7jgQc4hOoAMQPZwmdaWyEr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=vL37-IrYqDEehkcd03c_WMXCJ2psW6S6xJKx4yrK2re0SdBY31uFXSm_-Or9k7Mksp5gkQyWD4nykfdzwPeuGK13Xwk2MFZjwf1mQYyeFX_jrAtiq9a_n4NKK3MrUyKGVQjY6NXRMXMKvjsMtgWsgOZKw9ouJWFdA0mWy6sGzk4P66ltJa5RrlrB8t-trDg9L1B9IneD100e3aVlIMK-_mvuuNa0wzIc0Dn0pB_sZYC6nZp81coKBfu7wDfAatXUGIlB5sOuGYVLVZNKgH_8B0xQj7H1JODIOeSmFQ278BM0RIjeXpQ1wc5g_ZVflzUMohtdJ5VSvWilQ7dCevTKNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=vL37-IrYqDEehkcd03c_WMXCJ2psW6S6xJKx4yrK2re0SdBY31uFXSm_-Or9k7Mksp5gkQyWD4nykfdzwPeuGK13Xwk2MFZjwf1mQYyeFX_jrAtiq9a_n4NKK3MrUyKGVQjY6NXRMXMKvjsMtgWsgOZKw9ouJWFdA0mWy6sGzk4P66ltJa5RrlrB8t-trDg9L1B9IneD100e3aVlIMK-_mvuuNa0wzIc0Dn0pB_sZYC6nZp81coKBfu7wDfAatXUGIlB5sOuGYVLVZNKgH_8B0xQj7H1JODIOeSmFQ278BM0RIjeXpQ1wc5g_ZVflzUMohtdJ5VSvWilQ7dCevTKNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=rIVw4aHunddOfXAk5w8BC4jfPxl4hwsPgHHfRPar2vOhDCzpejKBT88bAmZDbNNYRG3S-dDTyKZs7mZ29OLdyAucI6lCBLhDs463Mv-DadPubZ4Q7w21_IQPxsVgLzSq1G4F1GRO4J42NegxWI9EYOZsg5OnLUYm7f8PrXF27ZUXOegv78p7jbddRPGLTYCAiVV4Mz_IM1-nq7zab9aqrMU9l5nZDKnoyT7-Z0Xpc1IR4zwnL9VhGBlIXUxgP2gGAVT_Ne9lNi875-3cnA9yg7DTjo8yJaXgi81OYxN1XXjRaXb-8_lM3YuLTlEZ_c3X51TbMy7KRQkspLAoO28JuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=rIVw4aHunddOfXAk5w8BC4jfPxl4hwsPgHHfRPar2vOhDCzpejKBT88bAmZDbNNYRG3S-dDTyKZs7mZ29OLdyAucI6lCBLhDs463Mv-DadPubZ4Q7w21_IQPxsVgLzSq1G4F1GRO4J42NegxWI9EYOZsg5OnLUYm7f8PrXF27ZUXOegv78p7jbddRPGLTYCAiVV4Mz_IM1-nq7zab9aqrMU9l5nZDKnoyT7-Z0Xpc1IR4zwnL9VhGBlIXUxgP2gGAVT_Ne9lNi875-3cnA9yg7DTjo8yJaXgi81OYxN1XXjRaXb-8_lM3YuLTlEZ_c3X51TbMy7KRQkspLAoO28JuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRF3fOLuVNojrj9c8lGXUnIKy2JC-c1RLU6URHNyF_hFlIYFNVlX_2a5F17lS5hlj_80SYxB0dPsJCmgt2CSaekLBI62Ju7thiHte6-Xq2aE4DzavJd9XaP582u41jJvVKCOFO5mzfHq2rrgFuUB0vcJ02Y85yJO9nQK7ISu4gAQstMZPYY7tPFC-HHdi8gvV8hcA3-h2OVNuJzhCn21rl3h-P0AaVMATPrxRNKVvNbiPPxnKB9alosJODVY-Yj5wDHpBWPc6vXI51GcLsBYYoPQgLzqiE3rCz6KhDMZkte71ADl-L97e32mNMDhILbiVM5CJGEd2xCWDSwHtDsvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=OHbHuegP6WkzH5yBZ_jD_gjUQhN0PrjQDrDcg94YNZzx5roQFvfPoMWl2qQj6gm34-cJRHstXQzOgi5RmdGfwLiCWGv_CSreHzTuVLriCQwlEdHapAcMtq8MdvGnVBh-uBYzDIgMN2MLVeOMhpnCuO9Kdv7C_Y7DrVQQWEzbz9mrifj7xTorlT-oBQa_vSDJevBvCIVezL7H_CvmHBPLwm8uQLslDEKyohwOXRCpZZrjRpXTTPM0mrUPhFuPhaL5CluVb33rucPNMPPEYucEIIUvbVsfUeK-88x2VJmT0rKIdNnwvjSbP_JfPFX8U2hVa6NqcVU5g28DCAVpbufm5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=OHbHuegP6WkzH5yBZ_jD_gjUQhN0PrjQDrDcg94YNZzx5roQFvfPoMWl2qQj6gm34-cJRHstXQzOgi5RmdGfwLiCWGv_CSreHzTuVLriCQwlEdHapAcMtq8MdvGnVBh-uBYzDIgMN2MLVeOMhpnCuO9Kdv7C_Y7DrVQQWEzbz9mrifj7xTorlT-oBQa_vSDJevBvCIVezL7H_CvmHBPLwm8uQLslDEKyohwOXRCpZZrjRpXTTPM0mrUPhFuPhaL5CluVb33rucPNMPPEYucEIIUvbVsfUeK-88x2VJmT0rKIdNnwvjSbP_JfPFX8U2hVa6NqcVU5g28DCAVpbufm5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REQr6Cy1KiGf16DQJN26l9d67jJMU8TXZaR69uDGSddXRk7nA3XHpbK5pfChkXzelRyQImwNb7mkYL7JF34W1LGKSsrlEYEFeuC1345dr6IbrDeelYPdHRqyjw-iytEXTqJ72O4UrP1JPL_vOaynmpvfUs8yG3oNWsSESTK5HIoP63Se3vcCuTDuMXM5C6x8D2xDn4R-ESVeB6YLZi9OK4SAgH2vWl3BFJ2J7scqF-iibjsgGEwl1dx9WGVw4tT0-mO22bAQEsNZ8CySn6FIojg2gi6fCeN7YWKB40lWIR9DBLz_x9VPackbzKgZ9IH6XadOKpGntVW_QKeM2AUPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i0MkIKhPJOj58d3HTDk1Hxf2h2Fsad46um7TosaVkvx9Z0p9knywvyaqOh33QKaINZOV5sXcDHnIfTTIdtue-RCPNFIYMsdPucDxSYA1fyTwa9IzdoaFTl939LOhhBT_nqezYUPmwXnMS17GrfY_f7lL0wKQcELZJNerd1uYjVLd7f76ce0PLln3_DLAJNl423hl9r_6Ub_-YZc0nPtdi_8kcuJTtDBMS710C-DzvSoaINv0Oz0gcdvzPFgAwvzFQ_QgZNu_u1PXqwdAkLW4JSmU9TTzamAqoU73WdgGOvy8y9YZAH-wOLI0-wuZShWTUyUpBaGxZnZXEdvnUgnZ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=i0MkIKhPJOj58d3HTDk1Hxf2h2Fsad46um7TosaVkvx9Z0p9knywvyaqOh33QKaINZOV5sXcDHnIfTTIdtue-RCPNFIYMsdPucDxSYA1fyTwa9IzdoaFTl939LOhhBT_nqezYUPmwXnMS17GrfY_f7lL0wKQcELZJNerd1uYjVLd7f76ce0PLln3_DLAJNl423hl9r_6Ub_-YZc0nPtdi_8kcuJTtDBMS710C-DzvSoaINv0Oz0gcdvzPFgAwvzFQ_QgZNu_u1PXqwdAkLW4JSmU9TTzamAqoU73WdgGOvy8y9YZAH-wOLI0-wuZShWTUyUpBaGxZnZXEdvnUgnZ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=ORnindsSncE68ZLuAc4TUTcV96hhEh2NCDl7Xnr1KVxhIlAOJdYdwifp42zJm8h2UO4IksCP0wtJshccQ_tjPd_tandvtfCpkbZV-sKotvEG57FlOzfp1HRhB0ZJsbb6ouq-ZLFI3tN11f9Jxgj-P4obia-b4k8h8lpIPTq_zAjPGLhLU25kY-PkCYtAo-8LEr0InulsP0R_AbACMFdjuRQrLQGCAvIuMtZHFoiXXd4aBmnWuU5nM_o3EgBVn86B2tBXAbSoNBTq7a3WHg_jjZwVDIaNdOHfiAaGUaJYLDEbkOFqW8NEcLEHM3-k4M0UWW14BIj-Ec--YWSEVUTwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=ORnindsSncE68ZLuAc4TUTcV96hhEh2NCDl7Xnr1KVxhIlAOJdYdwifp42zJm8h2UO4IksCP0wtJshccQ_tjPd_tandvtfCpkbZV-sKotvEG57FlOzfp1HRhB0ZJsbb6ouq-ZLFI3tN11f9Jxgj-P4obia-b4k8h8lpIPTq_zAjPGLhLU25kY-PkCYtAo-8LEr0InulsP0R_AbACMFdjuRQrLQGCAvIuMtZHFoiXXd4aBmnWuU5nM_o3EgBVn86B2tBXAbSoNBTq7a3WHg_jjZwVDIaNdOHfiAaGUaJYLDEbkOFqW8NEcLEHM3-k4M0UWW14BIj-Ec--YWSEVUTwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_i54yGb0JMNqHUtsfLqbteLg51cJfiByRNyJRxkAskW1qMVadLyYjMFRhO1BvcqYdwrZLZ91NwftkHFZQk_q56bQOvP6FXEk1k0fT0z6iUgvgz7bYaL7IEGRjlACGB7n8rNYb7xOAFF0RjEvloujDFxQs2wQpDVdhDUiwHV6k24h_-fZg037n3MPpiTy5XiUYuSyQJuBtxosp2pHzdkJYcpgUErPMg7OdsRll8jYyvcw-pxQLY3XBaXmx-2wWJuNApaF98wh2JGMcdGkwUNYrTJc2bz6RklqrHNf0EUBMQMgEBkYc92AszwOfTcXhUHP34c-nigZNrP75r-pshJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=f6IyEBWuRC1goT2OEzslVw5-kCD26NKe_r92PeaWfbN7kidmqKbdx_JlOxOhkPKlh8_PQM4DSR61FQU-jNw2jjLXm4QCCeQUv1ir3mJ_DjsYjDRxFMfqTy9teJQaUNE9Cn8PBQE6ePiRZpeFxaiPFH7KjvpGREoQGNWH2jVIXs07F1BtuhdBUcm1f1HcIpxtfJcRYKo2HNLVsQgDv5O4_SlhkxEw03jDpmy-9l9N35Ghb0qgEn4Kyza8P1UTnOsqlWly7xSEXrwF3APwPR5y8F_gXylnwaOeQrWN2DhWYGr8njxq-471_GY6ypmwwggPkGFmdsG7VsrTNCFAzWe50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=f6IyEBWuRC1goT2OEzslVw5-kCD26NKe_r92PeaWfbN7kidmqKbdx_JlOxOhkPKlh8_PQM4DSR61FQU-jNw2jjLXm4QCCeQUv1ir3mJ_DjsYjDRxFMfqTy9teJQaUNE9Cn8PBQE6ePiRZpeFxaiPFH7KjvpGREoQGNWH2jVIXs07F1BtuhdBUcm1f1HcIpxtfJcRYKo2HNLVsQgDv5O4_SlhkxEw03jDpmy-9l9N35Ghb0qgEn4Kyza8P1UTnOsqlWly7xSEXrwF3APwPR5y8F_gXylnwaOeQrWN2DhWYGr8njxq-471_GY6ypmwwggPkGFmdsG7VsrTNCFAzWe50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY1XHnc2tvz78NdkMgEW73WwGmD_OCJVpnWB85owDIZTP7MCe79F2z2uNbC4ih6a0pjiGi3tosiptfDI2mYdTfHzafS2FF8fq6iduLWttyEhoixH2TMGiWxboiWK3KhVVxeBj5Wrqqb0ytoqt06vngirsAXkK-Y9iZPcjcDLMyOWbkXhTHPELF9lbH7sTr-cmIeZEB4S7YvKoHxTgRsiM95cBiatgVu6N85OhHaWF3aWAY9AQxKyxnB5dFiQPPYNBG9kmx17gcVL_Hmhy4rbDs_i8Cf42lyIcyLcHodWir3jxDZBXKuGSXjfG_tuSIv2ktO7lL3SUPhJghjtpYBxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5hfO7p-P8gO3nW4E4pO-HyG9SU1SQdFB7wx6QzygjEhUQOCFfPG03jIKkrPA0DvgEdumGPJzrYZedpSBOpNy3EFIpSqJkG2TeJEkokn1Ary4VtOH_JQMq8s5qFmv4ZBvec3zafpPqWOXe2qgqZNCd5dd9fiFzUUn0WhFOOLUideosSmWiseuIanb2D5719vnfiTeWjmReSQa7-X234L6yk4YqMgKWENrG5RbCINkcwnugfGvp5-j5RNxzwAF7xGAyZ9CYRNZj8Uy9FDRjomx0VsuzH_LwfIsQ0Ps-Jqu_ZoLxBty4rPcnv8hhJIUfYk_lcp9WZp2Id2_LajQvA3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyfNYVfD343IbDHhbEwg2xUB-7wG2_olno0PHa7wKLq6uS0QBqyjwuv4yQToXq7Fdi-Jw7Q9PyVLf2t4eQv58vJnapLKltzsuVGL_gU-JUkIb3zic_RJxwiz2L-IHBDCuieXAA0QYHXM9bStqwP2VJWpXSC5hWE9z58SSLmtQUcgyEwA4IrrBV9PkdBd5aOYPkg8wah_6I9EaiuPO2KSAoXYWY9-C6YysMWf-WrJsHuPDzU__cnQqNlCi6C9YIXxjh8F7baJftKu-oZZTVCQ_a-ar_2ydfzTWUgOccIYA4b2NlTug8Q-WDTX4onU0-WWUSJp5rPPePcpEkgJMdAEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxVXD965ztqXWNryABXHnaWIA8acDWSVCD-RWoDrnve71BiUrtxEvaoCbyJ8zlajzZ6UWXXdtr_6r3t_DnspEJf6hODO1C8xP7c4vLut-z6o94JokGVnkdQdHQ2KYnypAe6jB6YDc07VPArHZBZRIzTA0BdfDkIrOnYYemHDPTDNWJRy-VQ4XY_2uqYafrWxUDq0G73yzkWkCQzFr-sGRvQXOjRJBcdEbzggx0RESXj7QXtH8nO1I_qG454vP2vSjRfY-z9rxD5tlYaRwFRAKizVDWZfbiN14LHhWub0-rTUG_ql9Zlgi_lnC-m2zIjlPmEayOJf32DblB5waIHFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BdioLlUTt-oZwwkePPXdgX_xlWq_YhH6XEj-JvcR_XBUWludQIJDiFKCb73nVx3YufoE1mwsShV36nFa-ojfto143jJl3L8wNOOAFiktXNVWHbgjhBrbkwwWZgtEVgXcsACl6L_HzL0ZVCeKb1MsXSQIev9iJhiPjfBWVN_b2s3UHqPn5W0P_mt6vUuWziWPoydJUj7PX1vp34Vn1DHd-V9YWB64zyVKvr5gVobaljA6BhEb_mPJbS27G3JPEKIfU3n6gpfi3p1cWHVQddUozRqOj2KUFQfldGsin-Wliws5uWE_Nz0oBlyYCd6pQRg2LpsADDbuePuZgBLKbod6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=BdioLlUTt-oZwwkePPXdgX_xlWq_YhH6XEj-JvcR_XBUWludQIJDiFKCb73nVx3YufoE1mwsShV36nFa-ojfto143jJl3L8wNOOAFiktXNVWHbgjhBrbkwwWZgtEVgXcsACl6L_HzL0ZVCeKb1MsXSQIev9iJhiPjfBWVN_b2s3UHqPn5W0P_mt6vUuWziWPoydJUj7PX1vp34Vn1DHd-V9YWB64zyVKvr5gVobaljA6BhEb_mPJbS27G3JPEKIfU3n6gpfi3p1cWHVQddUozRqOj2KUFQfldGsin-Wliws5uWE_Nz0oBlyYCd6pQRg2LpsADDbuePuZgBLKbod6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMmcrt3xxpPMgCULv6vBsULss7H_AlUqtjywE6BLJZwZUUMnUQwnS-n7M91aQECwAMj5aF18jfxPTL3AlEp6j0UBD84bwRZciYYaFxbzBDhxA_ztcAkKENB-usB9bCUfX1XtVU6gYi2pE1TGC7Qy1BmyESfvzc_u-QLYSbsx1hnpmsQQqxS_tiFxKgucySREvULennWXgVMrV6Bl4kPUecedrp4WHQlnu1bFqFIycaNZR36sP2HBH16TaGOn8BQQwFMWpr7pvXhilGdVOVs4xyqZEmrCeCelrEprpe2_YXmu5zbD9hhh_YrPaXzA0HLd2oreIv9Y6EvasEOvPFU3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAYx-lciUwwmPhSbblWoQENdf0lybhNR8D9tvGtwsZfzq2A8sSwQDgqzfsiHwfObSO2XOVJu7TW6bZRqRoz0_hSivPJp9dZL9HvRd-8sp9bKTOd-B4SFPj2nNlAyxVVHW5HzV5ZjdcFWKzCp4pSI-GMCfZdlaAmKWWyy93QMbPXUbmV8RelLBBdLMbHUFHOoy6OJv5ASVVKtdbRrNBb8gPqkfiOlhNO6LpSrvvC8iPWbRhc1SymAzitAKH7I_Ci-6pBHLCmCxLXfFg18oICdThVu1NLxgpHUUaGXySXrvAPXIYgWzFHXqP_rVw--fBrZ8SvD5IZk1vuHTzmO2Hbeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xe2v6I9m_76o15GKaFaUXoCK0VOPhERmC9ErrJUeLWwMjeHZsuQj5Z72KWEQSwb0hQ_vwrSIXMh_W46Btj9SJ6tqwvUlRZ73AdNTLBrdJxmmC3qQYbKvR9qD1HZ_f-KlTGxrcwh7mUzSfcywEiwJbWBv4jxyud6nv1IWMzw8WtzQ7gUTBC6h-vZBiZPVlMIhBWR9dKSclSKtWk0jMMbLohidKAWnbzH6nKaVVdEw_bczHjnPQdGe2_x93W7U3qV9qwyktCw_IsBYvdyUDfD97lxTsHktAGPsU0IS_yFxJaKSJoAUKg9knmCdjZl-1ZO3804viLMQSzvsgiBr5ixyGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=USQbQeM2CRR5FxUJT978a41a368okPOZmZJEnGHkW9KjX8K95MjYzu77wHpK5nqYJFqQGTIDenSe2fGENVGkFz35cY1LPw2a9gP5FJEu_auKQLGN-SviOsABRfqaxnkPNzJfDUMXrZlG1m_ptJgKszYERXHJmrER3TAVkJ054RxEMfjTaBvhiY5ZFem2IWo2L6bioxVSKv7tQ66OyXKaNBTLVzhCKm6sErNJOUr9ypE6sbZlFsWf9Io_Ni-AQSaLGVY-Ru_yp2cTyyDPZo4r_tQ9o7rieBtocBnhxvJ43eXjdjZf1yOKFaE_xv5xpnCEH4SVDegJ_dS7b8J_7RXWcacAnNEMlSPvSh4rqDE4qNSKcpqsr5RqV8t4YszOiDPyiprmc-U757CQrfTZWL3uhX793XbQoe9anVPV3oQqzRLaRUM8MQ6FOYhb9sXJfYyvz9LCMYvstGSA8gRPSrH9wUG25j9MjeBdxQ2Sw4SBbSDMpUwP8QvqGndiDX9BymeIABd0Oy89Y_wWAv6lfEhLqluqziavGxTWK9EvpP-mmlI5xWWjChOUn98kkUkfwQq5lTRsrpVpZgk5bfht5R_FWPyirxOCZe4PX55ofykyyDOCYYu7XYcs1Qw97AUdw2WsMdkldcBe238NyI9rK7_8t6DKmObOYDcyr6qqkoP5Ufw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=USQbQeM2CRR5FxUJT978a41a368okPOZmZJEnGHkW9KjX8K95MjYzu77wHpK5nqYJFqQGTIDenSe2fGENVGkFz35cY1LPw2a9gP5FJEu_auKQLGN-SviOsABRfqaxnkPNzJfDUMXrZlG1m_ptJgKszYERXHJmrER3TAVkJ054RxEMfjTaBvhiY5ZFem2IWo2L6bioxVSKv7tQ66OyXKaNBTLVzhCKm6sErNJOUr9ypE6sbZlFsWf9Io_Ni-AQSaLGVY-Ru_yp2cTyyDPZo4r_tQ9o7rieBtocBnhxvJ43eXjdjZf1yOKFaE_xv5xpnCEH4SVDegJ_dS7b8J_7RXWcacAnNEMlSPvSh4rqDE4qNSKcpqsr5RqV8t4YszOiDPyiprmc-U757CQrfTZWL3uhX793XbQoe9anVPV3oQqzRLaRUM8MQ6FOYhb9sXJfYyvz9LCMYvstGSA8gRPSrH9wUG25j9MjeBdxQ2Sw4SBbSDMpUwP8QvqGndiDX9BymeIABd0Oy89Y_wWAv6lfEhLqluqziavGxTWK9EvpP-mmlI5xWWjChOUn98kkUkfwQq5lTRsrpVpZgk5bfht5R_FWPyirxOCZe4PX55ofykyyDOCYYu7XYcs1Qw97AUdw2WsMdkldcBe238NyI9rK7_8t6DKmObOYDcyr6qqkoP5Ufw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHU9-pzyTc6DG_eRr87fX3OZouPXNX_dPjgoB-6QyIGvW7oMN3I_AkT19VZRWh0tpzUWM54FnGHh7jsXyfaIs42Jh-lQlUF7pNvqohX48yy9s9kLuwQ_8-RTa13NXvq28Q1EDIuurYIW_8b_1XvZPUw1X0ARstb_7OIICTV5DEicooPP4Ymc9JOTPoRSTJyX7qzSLbx3ExYJcpnw-xB3hsDb_1hiT-uaChYkPPVraAqSTQWzyuuaSjb4_WtscJYH3BP8YCTdJYWwKyKZWsejqp9L-MUxlQIi5_oeXQACIa3Mtn1LCsTYr-oYGBRD0YNtIA0gq9GJwuwui2InkAXaWoaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHU9-pzyTc6DG_eRr87fX3OZouPXNX_dPjgoB-6QyIGvW7oMN3I_AkT19VZRWh0tpzUWM54FnGHh7jsXyfaIs42Jh-lQlUF7pNvqohX48yy9s9kLuwQ_8-RTa13NXvq28Q1EDIuurYIW_8b_1XvZPUw1X0ARstb_7OIICTV5DEicooPP4Ymc9JOTPoRSTJyX7qzSLbx3ExYJcpnw-xB3hsDb_1hiT-uaChYkPPVraAqSTQWzyuuaSjb4_WtscJYH3BP8YCTdJYWwKyKZWsejqp9L-MUxlQIi5_oeXQACIa3Mtn1LCsTYr-oYGBRD0YNtIA0gq9GJwuwui2InkAXaWoaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=m1vPzNaulhNSiM_t9i9yiSboUCu8pu4NHDw_Mfh2xW4tlrSbUZ3qvNOfODLTllDv7fce8Ofb6nFqV5wfOiPGoHNp5oKcsCvu9P4Me39LS7_c-lJS3Lbn7xTvRL3RIBR_JE-IOZoKMuA1YXrPe5jsVk-mM_UtOYZjuP2pLDP0tE6MHOrO9E8IwToB3BKV9td6ctbShkl6bVae22u8FveHHTyCMbh-jIZUrDcVhMfB29nV955GpUcjhXgUJ-lehcKxxykSc4UPRN_5UOguDuri5fLuYWuNvwJBCYdLTb20TY2he7xz6HfS7MIDJk2grpguvFvojnb3qCZveqdavefv8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=m1vPzNaulhNSiM_t9i9yiSboUCu8pu4NHDw_Mfh2xW4tlrSbUZ3qvNOfODLTllDv7fce8Ofb6nFqV5wfOiPGoHNp5oKcsCvu9P4Me39LS7_c-lJS3Lbn7xTvRL3RIBR_JE-IOZoKMuA1YXrPe5jsVk-mM_UtOYZjuP2pLDP0tE6MHOrO9E8IwToB3BKV9td6ctbShkl6bVae22u8FveHHTyCMbh-jIZUrDcVhMfB29nV955GpUcjhXgUJ-lehcKxxykSc4UPRN_5UOguDuri5fLuYWuNvwJBCYdLTb20TY2he7xz6HfS7MIDJk2grpguvFvojnb3qCZveqdavefv8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=VulS_TQiBsBlJ78c17b51Tpml9OS0nrAuNw9_5YgDF4IVNmx8avgHSFMnvfBM3bWm-aFerycSo6JXXVCJTC8XykOPTYKgl8BBwqsD1V9_yR0N6kovs-tGh9L2pxLVVrcozdzTTtCD_4BJZbwNbaXYYfIMruNKMrRGGtsTLr_Av20K1oGeltXA6fzbbdhP-URC6imkFKb5Jloe8G4YFHdf1Vt1B6chizeVs2-oEPpi4kCPUOCT2feIVsvqPOXeL2irH2Gt5isjTOsnuB5Juys8Jj6cIXuInlURXTj43uany4vlLZ-O5B5ciH3DiZyVTrLs8UoVsshtZCFfI-gLZR_hIocVVXojvmVj1AyVnBxIDGrV7ThaZ248cPA6d6FMdlOLNOTFw9L5O_ArKQSGPWeBi3oyk7R6GDdhB1xcZaSHy84CjiDSkhn4OxSLqkT8JUoABYKVwlh9rq1x4ap917dIPMrgNmxKUw5Yd83Guvc7icmqjLzPiF8eVoWSUW15D1NEWe_3wo9qJCNytMvHqjkK1aIask0swX2rzEX5_UXzQ12-44of-7lnkkF_5mTT3-gS606_Fg6CIpHpSwkRn10ZieOsZNwqGjK546lTQxo4Nn5P7lqjG3AnA_QOvAR-gd4_j7muYckL1iDopkY0nXAIFPz0qLJIWuZVcY-MHORLo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=VulS_TQiBsBlJ78c17b51Tpml9OS0nrAuNw9_5YgDF4IVNmx8avgHSFMnvfBM3bWm-aFerycSo6JXXVCJTC8XykOPTYKgl8BBwqsD1V9_yR0N6kovs-tGh9L2pxLVVrcozdzTTtCD_4BJZbwNbaXYYfIMruNKMrRGGtsTLr_Av20K1oGeltXA6fzbbdhP-URC6imkFKb5Jloe8G4YFHdf1Vt1B6chizeVs2-oEPpi4kCPUOCT2feIVsvqPOXeL2irH2Gt5isjTOsnuB5Juys8Jj6cIXuInlURXTj43uany4vlLZ-O5B5ciH3DiZyVTrLs8UoVsshtZCFfI-gLZR_hIocVVXojvmVj1AyVnBxIDGrV7ThaZ248cPA6d6FMdlOLNOTFw9L5O_ArKQSGPWeBi3oyk7R6GDdhB1xcZaSHy84CjiDSkhn4OxSLqkT8JUoABYKVwlh9rq1x4ap917dIPMrgNmxKUw5Yd83Guvc7icmqjLzPiF8eVoWSUW15D1NEWe_3wo9qJCNytMvHqjkK1aIask0swX2rzEX5_UXzQ12-44of-7lnkkF_5mTT3-gS606_Fg6CIpHpSwkRn10ZieOsZNwqGjK546lTQxo4Nn5P7lqjG3AnA_QOvAR-gd4_j7muYckL1iDopkY0nXAIFPz0qLJIWuZVcY-MHORLo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=KLXpCGJQZh7cLNs3MbMZelBo2aAIQkxvmc1tSWDJMqY6DXxwhuAt1hjXm1hmWrlzZBMRkcyFuzklWJqWBjWp1a-_haEvfvGzSNI1DZP8egV9n1ZZIm9m3KZ14tRAz4qt8HT6Np8hJMHrld3EOglTAksxWOlw9tCxHj0lBG6_VI5P32ExIongUo_YJI6jNLuEOKQSWzbNDjCs7VMwM352CTZ8KM4AEw7tKpolIjAtVbRfSEPmJyuqqVFdpQazmYz8UeokXC76ZjJEHZiFxlHrnfxn9hQ71PJLQaZvnDA_QU1snVI6wDVT81LRYJ80N1Quj1rJDjs0quGUC_U1bUGiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=KLXpCGJQZh7cLNs3MbMZelBo2aAIQkxvmc1tSWDJMqY6DXxwhuAt1hjXm1hmWrlzZBMRkcyFuzklWJqWBjWp1a-_haEvfvGzSNI1DZP8egV9n1ZZIm9m3KZ14tRAz4qt8HT6Np8hJMHrld3EOglTAksxWOlw9tCxHj0lBG6_VI5P32ExIongUo_YJI6jNLuEOKQSWzbNDjCs7VMwM352CTZ8KM4AEw7tKpolIjAtVbRfSEPmJyuqqVFdpQazmYz8UeokXC76ZjJEHZiFxlHrnfxn9hQ71PJLQaZvnDA_QU1snVI6wDVT81LRYJ80N1Quj1rJDjs0quGUC_U1bUGiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=qKfdm3BqNTOfDrqXiSPfU-EfazuUaB3e6AIGLMpT1hRTNEfPVFxUFhh6hiRjUwd161e44pD-FNwk2LXxu_8b26M9xHBynuZTTqlODR5fh7NWaEbCIPKOaBfrIjWqOU8VKwtV2AnuAqCUCp2-G2vTCvp_xhwtfJdcPzs-3wS79mqF7v2xLbs6VFQ5qBNsKmvX1gN1ljzFfckg-fEEl-PVGx2BZgO-hROHrsLrSqFN5ks8JS3RCbA-mG9IBnaG5S0LpfgCXh4xPG_pr9M_Ebug8KowVFlw41631UYbTmQnrzp9VFGmczlwrEYkx8yE_FW2Mom2d3Cxw8CBDvFIKjdcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=qKfdm3BqNTOfDrqXiSPfU-EfazuUaB3e6AIGLMpT1hRTNEfPVFxUFhh6hiRjUwd161e44pD-FNwk2LXxu_8b26M9xHBynuZTTqlODR5fh7NWaEbCIPKOaBfrIjWqOU8VKwtV2AnuAqCUCp2-G2vTCvp_xhwtfJdcPzs-3wS79mqF7v2xLbs6VFQ5qBNsKmvX1gN1ljzFfckg-fEEl-PVGx2BZgO-hROHrsLrSqFN5ks8JS3RCbA-mG9IBnaG5S0LpfgCXh4xPG_pr9M_Ebug8KowVFlw41631UYbTmQnrzp9VFGmczlwrEYkx8yE_FW2Mom2d3Cxw8CBDvFIKjdcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_YOdCO-QeYREGV--UBB_qjw90ZjzZcTs3SyzXJyWC8ovQobwd82dqTS0VIsbND0Z_SLIsW33ekfRHtW66-t2Hn7haCQStQcbCXBlp0R8JExbCYDzJsiJS0nugMuL3KTD009JYZnYZSP67zRScO1fRBO55Gbulhez-OQujxVwO2IHRhzxZyHDsBHcQhRf-hT326Q-2YXqIReW3OvzqpXpaPFCfTxIM9zxo1KO0dtIXFQRtOMcjjtpRfnvZpcJX0Lb27nOG0FRJEcCzH6RI1HwjZQTnibRe7OYRxDJFXGQh4LQCVTEsXXgShYHmutuTqgolZSTKBECfDeZQ2rF3PqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uEfRHoez9CDqMNrYuT5t4XdK-UDqPVmJUL5tiUFBYNNh42wx6l_20yWWtvLhbH9D1fRWWQJ1_0NrKwjNDPHpbzUNbNJseU-Uu6tI29IQF3MNZztqqBUo0YrvAfNIL1JF0eMw96HtSccDmhFAZgpM4Oju9-4yRln12kNCnU1uMTqw63deoC13w_hclfZXKO_Rd3j4vW9lwCqJENQ7v_j22zYAzDFF4H5gE8682uXJPkpb2V1I9CGu9-BzP2OcDvx_tyhtPqU6cMnUdC3tDgSxmGXw00CJbkt0C9GxBkLXdZZvfCBc-xvFCSmd_hWKUcnu5eKxf3pnJZlhldmjfhvc7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Wg_XBjcSnlhSwLB0b4rDOQZ2AO8SLDSjWxSPV9pVG4kUstdwBTJwxT5bJUETmFL7YJtJMCC8z4KJ1dq98qFJlmzonUMCmA0j2Qv1-HMykNrxPszA5OdMRzfeQK-Se8SpYKenj9lLzFCqnqCKP3hjWfNCa5EzUmpgwzakUkjp8faHWaWrAhkn-MfoTGirqLiWZVedd0SSc6rXJejuNxB-Av9DvOMr0mZXtN6yDbO43jBacnD4Qj4kmj_8lAkA9-lrPKYQJs-fmMKPbrsjAQwzVR9rdZItH4lxorSj0JA0mQG3lJP2WgJTJe8ZtTPOXAuk16g1Qtkec7N7dmSpE2k1uEfRHoez9CDqMNrYuT5t4XdK-UDqPVmJUL5tiUFBYNNh42wx6l_20yWWtvLhbH9D1fRWWQJ1_0NrKwjNDPHpbzUNbNJseU-Uu6tI29IQF3MNZztqqBUo0YrvAfNIL1JF0eMw96HtSccDmhFAZgpM4Oju9-4yRln12kNCnU1uMTqw63deoC13w_hclfZXKO_Rd3j4vW9lwCqJENQ7v_j22zYAzDFF4H5gE8682uXJPkpb2V1I9CGu9-BzP2OcDvx_tyhtPqU6cMnUdC3tDgSxmGXw00CJbkt0C9GxBkLXdZZvfCBc-xvFCSmd_hWKUcnu5eKxf3pnJZlhldmjfhvc7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTLjhTl9zq3tlTit99QRzU-LzDQ0wsroYW1fUACjd9BdUUOAwbNJt_Fk60LsfofsxFG2MWZQ8al2Xgdof82enkj_0vPeCk_iu29jiEkoAkbZMRSnp2AJujsJsWZKkWqx_Mv63QGUm-4MmLtkH32pQFb7bVgHcnZDBT2XPM_mbo-ptQ5ppMXRYpT0l5pVM2cPvbnG9LqRgRtsIvd6uJhUGuJ_j-7T1DBeDl-GaQ1STtJXE9TmV1FjsKEci66PpTIC2DkzvcC9CRiy4jWrSLntUc-5LAHYF0jd1CFRsMye8bCniGxfTexJ7nLWusENSCJrd90rU-y5xC2haGfZ6Zz0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=h1yHgwS5m9q_Kqq-1TIHQFeBUH9EPjqFeTnzD5wYYVv5CnYkRWOKpk5C1lUyOWEvUOv-chgXuK42QU5s1GL6gz8n7f7esbkiKmiyfvPb_TKfJRKeOOqALRRcyXtT9tbduAfP5vDNMzpWXWUR0q354i4QRBARZSt-hB7bp9o89ulQ8zeMtv22W8ISHFUVK2nGq6n-MCkm7gBh9M-r7ibHFHPHIn1sbcRIH2kM9_mE6Q8rbDw9t1SeCB1o40vX2HOFTzlpAIs-my03gZ5fKHLCDqZYQ9aPrluSJqDEllAsDJipcae9TlR88hdokYs4lVS6E6ir6UazI0Lait7RUZck3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=h1yHgwS5m9q_Kqq-1TIHQFeBUH9EPjqFeTnzD5wYYVv5CnYkRWOKpk5C1lUyOWEvUOv-chgXuK42QU5s1GL6gz8n7f7esbkiKmiyfvPb_TKfJRKeOOqALRRcyXtT9tbduAfP5vDNMzpWXWUR0q354i4QRBARZSt-hB7bp9o89ulQ8zeMtv22W8ISHFUVK2nGq6n-MCkm7gBh9M-r7ibHFHPHIn1sbcRIH2kM9_mE6Q8rbDw9t1SeCB1o40vX2HOFTzlpAIs-my03gZ5fKHLCDqZYQ9aPrluSJqDEllAsDJipcae9TlR88hdokYs4lVS6E6ir6UazI0Lait7RUZck3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
