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
<img src="https://cdn4.telesco.pe/file/ZEsrOZOwbW9Zd-V92GXDi9w3tBrWShkLvCVqBT36BMWaC-wOaieo2KfSm6e_9UE4T0PldMdkuig8IBishZmIte7f-lMvvchPCvap8yMiKapcD-eTQcV4EYjJY3X38XaAd6zAYvpU2ckdg4_0htPjuEG1GRimfKzZlwPYr8Zgz53rw8JEE6aYv2ylVHB9E3hrbMxuaY882fSSNJbGqdxG6G0WxtoTAzbBgeT8YxIjVdxlrjNsaWJsEiwVjxT_8Pq5APKjMydbZdtkxt4dykCwE-DaPUTyHwMZVPZK5bSKHefmwsw-2rY7-eTqXZdE6-Y38cpYrYZPLy_Z1NZSf8OvYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 734 · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71815" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBXGcCRltNh2dRnEbhXBh8jFeapxm1CI8Vws3TlsUv6AOY-AIOa7ITzrHX62X9fYo3FX6jaOSy1-QzFMAM0hFMx2S656cr5yS0aB01vfVAiwDI_vydId-hgmP9-LSpbzHWhCRvYd4KNuVK3jw96jhO3H3BXc1FaaNjWcN2Zbb6W0dHQhqBPFqvugHd8_qGhi-eM7RKN-WcSumFub4wKL73gZJXPhspKTYQupzF914qymnxZTEZHd7UUZ87KHBMO7K9C9lGJJQ4ul22AwzOT43Pdg2ew87kTNwyt1wc9fvzci7V_KAtTTPckYeUOaGlLkjJH39jWjES-jM9D5VKtauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71814" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=cYkVfwHaxcdji7SIuQdpoTA4obm6f_kGFYAeS5QNdL_uZWqvepkk8_A25tkuKOuKsqXiNQV7muj6b6hCyW9o27L8FgopgdbHU8P7lmksjjeg_3TUzN_SC89k7BD9InuR016_ThBUr80mQkPBw3tUtsPXMaVzDoGknYf06nLGljWhIJBL7qi9WaygkjHpAtk4yLrLp2ff26WM3LnYku60lsmm7NRVidSV43o9S04JQw9PYV9LXqUGWB8t7wR4SLzJQk_1tRGLyHUvXhc7xkWUynUvjG0KQ-owvDrZo2gOl50nQffIJfNPB2Giw3DAQYcjjsr3kmmZcklvasPz2tM_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=cYkVfwHaxcdji7SIuQdpoTA4obm6f_kGFYAeS5QNdL_uZWqvepkk8_A25tkuKOuKsqXiNQV7muj6b6hCyW9o27L8FgopgdbHU8P7lmksjjeg_3TUzN_SC89k7BD9InuR016_ThBUr80mQkPBw3tUtsPXMaVzDoGknYf06nLGljWhIJBL7qi9WaygkjHpAtk4yLrLp2ff26WM3LnYku60lsmm7NRVidSV43o9S04JQw9PYV9LXqUGWB8t7wR4SLzJQk_1tRGLyHUvXhc7xkWUynUvjG0KQ-owvDrZo2gOl50nQffIJfNPB2Giw3DAQYcjjsr3kmmZcklvasPz2tM_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9pGGE4p1TkHpsF-pjAaEf1YtbtRB1ViBRcD5mSQqIhcGiSF47jhwwpCFQjQdLZ5bUoWTQKYIoa4uOEyoiIBb1UyMO80ZbSbbiRISOMx4WiZe3nZI12p3oQSsnQXdNuzXlfPPocGhjnV5zVY-Ncgdspyqw-FX_kogDn8cwjxNAJ1wjDXkJMdv3OGln3uMudFUzW0tpnD7lnrAuNuRjGmFA8s-NrHDhY4uuWPhA5H_Gq0aywXwop3T4ung7Wd6ksLFk5hCAgoV5udg7nla3EPyfIjyqgoJljRC1xWYxqkdpV_w17NBCAgsX-Af2lg15-WVubfdTT64Y7pSJhAnlmE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=jruEJ84rPJ36nQeP52H5BW8DvtloNyIokNYSgsZ8xiUYx7dOWidfgcEXEpHXWepoxPUywVsBBvpDvq3Qym2NrxyCPXiqMUXa3lcQZ1gto2UBM4FKPu-5E1e9HYeMNDQyKed-ysmgVoqQK36uO9ZERdE5fBH7Egj1nrGm2GKbkYL-YsMe3Y_BKQczEYgpynMAGpGR3wAwpphecQivklDMGk_lFkKGUKWg4FI1uJUKDztDU-QoeWAM-ShaxDAn2uRsp41uDGa-yAxUXEByXs00yL4tmI-XlkmgKJcKx8YA-pr6bz9H1Yb18zjMW8UOF6ZhOU99dsV-SlEtqru2HBIrMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=jruEJ84rPJ36nQeP52H5BW8DvtloNyIokNYSgsZ8xiUYx7dOWidfgcEXEpHXWepoxPUywVsBBvpDvq3Qym2NrxyCPXiqMUXa3lcQZ1gto2UBM4FKPu-5E1e9HYeMNDQyKed-ysmgVoqQK36uO9ZERdE5fBH7Egj1nrGm2GKbkYL-YsMe3Y_BKQczEYgpynMAGpGR3wAwpphecQivklDMGk_lFkKGUKWg4FI1uJUKDztDU-QoeWAM-ShaxDAn2uRsp41uDGa-yAxUXEByXs00yL4tmI-XlkmgKJcKx8YA-pr6bz9H1Yb18zjMW8UOF6ZhOU99dsV-SlEtqru2HBIrMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7yKNuPd4U44iyv2_D4-sUQcCIyTeJccdOMkZqaIsNtFRZ31ca7xUwhlW5dz090FfYCYR6wogtAPmzHKb2S0YBRMp9TkOchNcypGbBdetcPthN5pxoPCdi4OAoyaKsEvQDM1ahevFzAkaFMaZ-2LgmeEuKozAz2rp3S097sSGFYevWyapBkBnkag3DXNfsc3WnI2EIYD04A4djK_5AVF8Rk_lnhjXxb8TdWOQHdYxf0Pm7thMwK-2s1l7GsXbFxbtmrE2rKXZRjue8TA-bPvNhsMVlL5j4iiJcws_EpDhT7C_yZxLI9ZVFASfFlyufs0Lerv_bRAVFyGEstOAPmU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71802">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71802" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71801">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71801" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8MRiFz2aQFpRIvoFa3HXlz3RFpKr0QNEigLu1-XqnpkFVtw5AnRcFYkz5sanzp2E8rc44xF_g5xYC7yL8aMsapHJOPI4v9RKEc4a0fTxo7rNRfr7Vd8Dn_4_fVI8gv0drnrlO9GGma2nPkihlTCVVbcYfkxrcCKitOmFHbggSfmjVY7znzUYkduapWfA_fJmW0o6dfB-x12rY09nKsCiYazzWS855aGjbMGmszEkPnw9c4RaJwLDcpPqViTR0AIuGvkjZDRjqFPT4kP4M-WwLtsJau2Q2i5oHdrz__vDpRnZQb-NFHmJ0EVC3NiNeu-5MqLIlOg56Dhwrq_yWA33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdAgYTFF4PP4iadqPjsSFBgweefXg1AZhs0UUo0dor__U3LGsT4hikJl3STiRmrcxfCiSTumZv4bPoIBN8BOqsreU0aG1O7nE2oV_49eOMtnV1LVWhAKyhHKD2mim7H1GDfuKd-YRqS8eHvVhz1_fAd7ZbEDvyoY7gIUFbpC4xnsut2NaFCOOzW03a2hkTthrnYX0ilyEM-QXxWJKgF_pDjAgg7Zy4oLNgT5jT9cN0ooVoGyfAtLsl97Vz1c2a9wHuOVxfBXV3SXmxpCXBnumXccw10CCV0pN-htxnRm7Im1itJDHAY91P8aOUvtsyEjkiYWZYr-jOmArosQEy3xIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-rKuGOzkSAphjB3XAXKM2XjUeyP_PnMi_UJ4X96vS0ZAQp32KNtHWa0Ky2VTj07psdJrF1Mc358wdyMw2-GuY_g41x7CsUpj1A-xBcNh0BV1X5ycPwSZilinuj9fp8prQkRPnGKw1zwV_GlWjvoFd571y74oPb870DsMUeV7Sd06PQBWhpJOLm8qiFbl7ugTh1Ks051TWJy2aHBwwDm3L_mbLyZ-CtPvRszsnekmDagN60GbvFH7D5u8sWKvRQPEzD7p6ZEzKp0wT1dm5YsZUVMIKb5lwbsvsWgaoaKRRK4_LYk1b-YcOc-LTXE-VjMpl-R9V1oJoC_urxkG11aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOYphqQUh4YlJYO70cynWHP3VfPcntUW_ajmtjnTISUxxvDap60UIsKC5hPMOmR7zxa1dz8xDYbrZyUtOYuFq-iy_hBjzmGo7bXeiXqYXRgmSv8s3ANbhTaSTLH_67x5C8gwg1Lm5oK0GkYDdWg7iSVk2ID9XKTgZ1hZO_tthInEx35mnhfpJNjjjpzBU-LvjVVb-JR3r2AhESGuEXHD7T714y7k5suJ0_Cyqt6KiYpQWLE2Ymb1G51btDAcs-Gj3EYVzufZj5bW5OjvpkeS-SR2L5bUs2ZJBwKljDVHNf_E4PX2p2O0fsOsuChXTkUOE6SU2QgICs1mLyJb3O9EtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5IgIwDEjIqcapNCY3vIRW5ga8suezmuOnBusjEnH0d1S2LBrJad5LiunghmDz9JpdcvTLHy4ZCAyDRDQ4UR5kEkVVj733wRJLDTI5gXV60wkYt-IDwS6AUXpYF20Y3MM99bi4txQD-UwaT-vm2Rh4G6Rui7Ppm1mbHMEUYuImfMjqjZNQJn4B8FdTxx0qG81oQ_F5JT3cWIYpWPSNmMy6b4EJ7GwPxqpQ8O9QnWaHbmwnZmHXgRcLfMfe6J6VOumsLFtMJ6H9d43aWcnWmNt491U4k-t98QvAtjXwBHhoTt-URHoAjpo0Ae7K_WiORuSFqVToP3NCXEWEkSOvuPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Insrpl6Yj71gNNcbbwEVZRGfTysi-mZ22S0T8WrQ4RUrLe9F3chzB3drwSO7MfWkCZZ2AB7_CT8LwL65XNFURIWLYaoBeY9oia9T9DnOvHe2adokSvZJTTo25ZjO6PNQf_Mhibm3D3HUh8faXTdeLJ2SGvnjsJ2kaqh5pbfw1USfQA2WGi6clQ8R6gFwIthjJqd02YtDDVOcS6BwnJHnbBXJs7KULaUEsxS1QvT--kY5FZ8ebGgjLDbnblOy2bwy7EuHmMPCjeAxcTR3incBLQEzUYK223Ln9lGHFL-AoTzP33qr8f8_ItGoe26yyzUsbc-VOVgPwdrTszxU9FJnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItzsFfGomuUiEoPODSB5txapGYDk8VLgUlPj31ZpwHWHmWqqCfLH5ijjDytpcGr4qrwj1X2_83WcaJaedu6349esnuhNhbsokOjHhpyUFLALa7JjgSqOStVJglD3Au8rg4DTUV0c3N3fZAF4icPvnG_duihKdOMkNnyJ_u5tIcXySEayx68mmviVbflK9dZLq_vB-QTmJKYrdhSM9XTEPuiyP-RAkjLGX1cT1MviXQgN8inQfvJA-VOMmUDMvc4esE3FcD3tPZhjwY6aQPjizQ5OY8ZeVOvhefyFfnl0SRhb3-H5-Fj7uUq0cI7tEAMYBanKnwuKE28vhidTDf2bug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5ticVerR0egxFAZkqgYme_jA5NtTv31qmjTxtHI-wuxUCAZEYA9ngfTt8EqbBv6CAYQRwgTTZvDRHksbj1o4yrvwIUGchbTsFEHKZF9h6yNzrE1bL1hAyMszPFFv1VwYJwPMLznK6XsJYNTQlB0OCpSjRuCw3Vcyt196HnrffdNy8f3Yb_IXilAKwTLBqShXMguAafK_uQMKHWLweOQbj5gI-FyhMKAG73DqvwQFABLHRWz0Y-LGq8d0VYf9LEH15IoO7lLN7juSXJJYvOAaPA5Th7LApDY1rjvxjIbK339gIXpQ4y5IIX90hmMaB9q5j78Gmzt5u4pjW1_852sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tLk_9kqhHxU-9RfumsnyIdSEOITQ1l2InqPI74d9CkLIpTxm94tUyyxXhM1KjYa49Q9UbtHXegaSiaodjqavMvD5pcqFE-FWviK-r976x93wepGpL_5Ek2h3vY5nJe_pL_touij3Qar3AoNC7RHAICqr8pnfZO9Qhxvi5u5eL_WClwwr0zdHC8o71o5Me5Tz5y0v4BidFE_EzLjMdjS4zzC5aZzl6LXFeRd6DSh0NebluN4aAwmzptqKuoZKor_DB-ZcsDn8bYnRUpOROH6CfQ_Tkub_UABU9e6Cs1por4J_Oqx_AK_i9TVgud3ZTXaJBgi5iHvjGNrCrM_wkuN6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC1lkLU0Mjos9n2EPbzOJblOEHYii6Ppbdx_ECBFy9kO-mPYGfDPotDEvLy8S5jBcAqapdu1OavngpI5g-0jrd9NQ3V5hK2baJwifXzgcfO_LUkkh2aQzCDZ38IKj4M-pUlyatCSAzpxteATYqzk5H_lAThczEI6Me9Zewkiwp0kTv_F68FQy9q7Q25KmGsLNXyBEjs5vu65tYhrUVF5_NvLEaIq_dgRlWy4idirVzT5WhVsGGnmfwGX3PDbb_7KJo2Rn6LcxWksQzEhkZY-x1y4swMGt2EUuMYTFRBL2ZDm8soRJSqCoE0YSgmSvrlMetOS9fzPFd5epl5JpanePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=ApPd9LUD0et_a-1oQ4IOMJ9Iu7YEx-szxbTvnz0kzNJEGtFyanT1s4-Jx-8MkwCly-l38ACILCEBDR3_tgT6cBUFIB-6VHO9JaWzzcgGx3sgz23e02ROU33ltwiKe-EGY7QvniiXME3Jy3RWZg_BXoud_-ox8Keb3pkypaovQv6Ts30BuJG5SHFnL0umlbaWuvOjTjGl_vL1NvQw8HF6mEQWniB2Ohqo7RBy6Y6MBI-jfMIinboNI0Am-WGTHFqX_kjpn8etsjTQ9O_G8VaRQRBBSP3JmcmvCO-wBBRowYcN8RK2TYvQwAVa3KeGdkJsjbT6OvU0W7UD89H5_8BJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=hG_IAWaPasMVMsRhcVa-umGLQ9Mz5eLFu_apoSxq3rsF8SVlrwB4HTRYLppjYBXLUMTfvYWx-MHkZulmdK3RkaUjU4FpI5WY2Tu0J-d0hrfNzlwuv82khkAVp5NAic2_b8ggz1LswXPJkEa4XAdE1oyVs-gEvgn_qDya95f4EIereZpg0WXa7JzqEoTN0N4jtpZJXfpZa_BFuHyMPeLQDmuWLT6V3U-znSb753KdiJ6iCSJ5ChbuGvUwRZyTaF2kBVCn_hSWCa4mKjJJypfoAOlUrIcHSQ5tcO4GkVmwsbyIfU0HKjD_FPH-A39u1R8hbgtQWldTnPFaAvYip1oG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=b7_8JdXKo45Jn4FudUaFnxRH_8zch1aPqDQUsreqD9W543anFrHzDmRo9SyBJoh96pqd7Aahnu-G2yS2Uibglz00DTni-uMgtr6y8n5bDSvKcorqmkGiwgRG9M4qnmP8MVkinqWvvMP0SGuEb4DHlT8KX8hh96IiIBuuQk7AHV13UnwIcGDB0Qjlsg_7UAXK2FUbtpp3u1Fj6QwoiYKbB4dRcbr4pZJv_6zIhug4qqHOzWey8opLLJzltV-r_m5AUm8dR_VON27sOoj6gn8pNnCSus4Ztw41ZGjs5tCoNUeATPE6ErGRQSaa3EGoKL_zg-9-jdPz8UUb6BpCPnX2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUqSkFnpYiHV5n_S1wpkXzLAbgLlF8WO5qVlBWfBoZ8IV3nRdy5wUIeJEYK8GcMHhcY3lOR-yUpgqu74n4xqG4G8q6d09ulyz9zorLWYSLsDwBE5wLgKGGurjCux7CFN2Ui_A__9yGT_Mogvbv4K0TP-crqmL90skbKbuPhaV9xiYTYHUeopYRaPinDCzmKausThA0CtPhjYlbYRCnWaIz725eWtu9QkJregGyNvtedo8V4VkP4apcfon0klowVBoDhZWDkt_-9AB5sO2h3LJciEobcmLExk7XrCrERIzNA7uhAfemujqXZEiiEXhGrw5-3kWiwVD0Z3560kpvmRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=rfqMDEhI7OvznA4XP5FzbA3uvegcZPx3UkuCoa3skDzxUH8MUt5SbpLTqMJy9JrWVnOelLuJY0YHVQSvPFSgso8OoC_GSeFkU2G1q0PWKUouYBaDEGvxHYSxfOktv_bMalOWAPcNBTqhNIeNPZlFBDPCd2buXzYTLjniT1O-NyjZ9tZnJMlGAEiHpaw975q0Yz6uUksJPcejaTMb6WqJBwzGl73hkXZECH6fVSOxTP5W6VBiUlKh1kjx-cZv67YJgySZtfg1nDjHxDbJqEH90higObWaSlJe5JdGVcsmLq1dL5z2obxr1P0ky2JL01x-8JDAlz9thtyZPqq3KiN1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=po88ecTCmfFYBTyQkBJ7CPZljYSPjGioknYTf9Q8LOkl58VGfIxlFzhxzBOviszJYM-SXrBl1EVPte2TqZR-XXK5FhWWmNV6sb2judaFfnEX_KPklPD3QUYrYg1oE838eL1PzjsMlKREpBGm5OJPSTrNyoG49ofrvPXR3rwY_17LxdAd37ryTSjfOgKX05KI8m8ok-r6GGEeceszIrl--BYkV0RUQuCBHiXJG585AS_rnKZkTZDx3WN-igVvE5wSu3_sU5GIuo0Jcv4K4HDHV7A0rRrB2WRBeA9wIVFJD0baOkS72We2mSXWpk_Pe-pomcYIpAvU4wYO6ny2NE_gYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=jM8iszzvkv39uVR1EKXRQt69jsKXtmdimTgUTYxXpc_txlj3efs6hjK_EKxdwM_hofE60uMG7LAERR11xWJZlTIXSlV2M-NTa6wqhmAXQ0Nqam4WpkIUGZb78-V7XYbi0E8bglsMUuLsjdkRMkDQWOFkKYlBET9laMu-t2HNf9YX2ppCAVUfZYa7pYxcJ24wtCQMq39F7RPjSvqyNSiEaMj8hVmXUvTSMr_YfunxRZ2EJ9wS93UPdebFuwfA19-6sQGhwjZz3CgYmut94d8lmUSl2O6jeeP9U-w6XhZ_WWW3eC4vWicYKJyvIpKWpsK7LekEa4egk0ygPIgHIveLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=GoLroUNsbk0YCPIZzUfaKiZlq4cOHLhhZalR2thJ_n_tju4WOCsgtTDv4DusHuD-uDR0mdjLBOljLWxDb6rr9W4nGKdkT5IEQe4G3vCavNtTGy9H7BK_hSHiuWh69n0DU-epH07RDJopCpMrB0yStd5sY1rn-9Lmxtq8zePIGlFuFYrQKovKht8Z_Bi9UTX5XCSW_ycAVMiWT28MJUWuubxUaYAejZVoZqGTAnOgMEk1bHg0ozls7e_nqTIuFr4qOE8lI46ChqML5cdn0OTYAJC_PasXfQwyW7vmWuN9wuquwFNLbjGjJC7wG-Ltpc--_e3dpzQAaIqLRmkXhr8vHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=GoLroUNsbk0YCPIZzUfaKiZlq4cOHLhhZalR2thJ_n_tju4WOCsgtTDv4DusHuD-uDR0mdjLBOljLWxDb6rr9W4nGKdkT5IEQe4G3vCavNtTGy9H7BK_hSHiuWh69n0DU-epH07RDJopCpMrB0yStd5sY1rn-9Lmxtq8zePIGlFuFYrQKovKht8Z_Bi9UTX5XCSW_ycAVMiWT28MJUWuubxUaYAejZVoZqGTAnOgMEk1bHg0ozls7e_nqTIuFr4qOE8lI46ChqML5cdn0OTYAJC_PasXfQwyW7vmWuN9wuquwFNLbjGjJC7wG-Ltpc--_e3dpzQAaIqLRmkXhr8vHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=vMDV2TLMqovqtSimddO4p-6sC2e2dPESY0wYtKqL9sUtvPG-ijH-3ArQG6bHuk89LVlum0WiBDyBXb2Gqk9dWx116BFpzCMLB-rMiaDskJpXRN4IFkhRnVoK1UC0CKLJdBnwFeMouZssV9aOcfTpUo9T5NiW_JbnDhvG3aEcc_gaelPr5WXW1hOinACYYOLKe1SoB4Ayxr6tffiVUmDYRRtXnnCT5mrDL7GNadGTkl6TjFcZ1_R-uU5e-9Z5NsCeHZm_-nTfp1kR7u69SZNVisIabJxbk-dvc7NFiDoFIgU0o-cGT0raAV0fuP2aXF0r8EnriA-bpSXs48u3_Ma03w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=vMDV2TLMqovqtSimddO4p-6sC2e2dPESY0wYtKqL9sUtvPG-ijH-3ArQG6bHuk89LVlum0WiBDyBXb2Gqk9dWx116BFpzCMLB-rMiaDskJpXRN4IFkhRnVoK1UC0CKLJdBnwFeMouZssV9aOcfTpUo9T5NiW_JbnDhvG3aEcc_gaelPr5WXW1hOinACYYOLKe1SoB4Ayxr6tffiVUmDYRRtXnnCT5mrDL7GNadGTkl6TjFcZ1_R-uU5e-9Z5NsCeHZm_-nTfp1kR7u69SZNVisIabJxbk-dvc7NFiDoFIgU0o-cGT0raAV0fuP2aXF0r8EnriA-bpSXs48u3_Ma03w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=qKo1vz0PCYJwb24Qi0IKzreW4INBnCTat8Tk4DNz8Iqk1WEUI9tGLb4pyYwRplW4NmJ75EOi2zHtT35Ma-7iYi3hWwA9QxNC415RY9iuIO4zAJtdYdpXUsPb5PeqZHVhSxIZ8xeyOJkEs2rga_kcqgXotWPB5YLbo4-Xx4R2XJkRmJ0CXLA8NaT8voRuOvt3dtGHdzQ_Biq3MmByJjsDRVYF2_QGOWok3S4RKYhpLpU9MgrN8XlM6Hqrv9R6fdZK6HivGd6AFX8GWUazKT0CIDfBSS--Wj4oLWHvMxFt_nCn7VJiZTp2es4xzmqnJZvUo1fTWES9FOpXbjqfkYpULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=qKo1vz0PCYJwb24Qi0IKzreW4INBnCTat8Tk4DNz8Iqk1WEUI9tGLb4pyYwRplW4NmJ75EOi2zHtT35Ma-7iYi3hWwA9QxNC415RY9iuIO4zAJtdYdpXUsPb5PeqZHVhSxIZ8xeyOJkEs2rga_kcqgXotWPB5YLbo4-Xx4R2XJkRmJ0CXLA8NaT8voRuOvt3dtGHdzQ_Biq3MmByJjsDRVYF2_QGOWok3S4RKYhpLpU9MgrN8XlM6Hqrv9R6fdZK6HivGd6AFX8GWUazKT0CIDfBSS--Wj4oLWHvMxFt_nCn7VJiZTp2es4xzmqnJZvUo1fTWES9FOpXbjqfkYpULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc9buxiym751EVsC8HfBZyN4eiXoSXZcS0OfMEtHsbw5xlACj6QwXNXN_og6TR5VFPO1A2e50bh-Q_HxLh1YXI6AdQoLLRz16nsD33b0zYIGOByYjLIDYaptK7P47bZAygGaAgJnX2G1GSIQsqHXD-tZfsSAtokcCoWhRDeuBCOS3CNaTMuLZngFNm6Dnpr03tAeN0Ld79q6I_B4f89fpT0wwRwwXzNIRY4ee4q7NxDexC73xpAgpCl52EOvGgMe4CuZq9UDSJDuqFUal-siACp9noXcsAmHlSDROXNIJa0aXFxkWgCWyvwpQTGSujweWMKekBa_yN_Rg70eBracuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-uUrFiA5TKMWfvqVSNYTd2tVprzZS6i4JwqxOZMcnS9GCD-QBPhiyZ4uh9jKekofHmIW-5EAM-zF-7enB6CUSK5Uy5blr0sZSuywrRUp0aRye0aybjOB7-ylAHOm1G5vYKSFFaSoP8WpVP_Q4X0YsPDsNgfZQaDaVBQ1d1SySKrHQC19xaLET3pRjCjSU7aE3-2WcvoD083xy7oShCIQor7YAymSVH79ccJDtsnBBpwoeEVQWYjxagHyO37exyHLpw_TQU_2_ylVlcD97VHldOe_VgnmZiU15R7bg6mvKzs49dI55YAaisNa66J8KSl1a3GWvzYnINV4J87S9SAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4bvtWkwBgmae3H6whJAQQjrXv4GmiN4ds3fC_dGu7VOnbZU42tnmUg1Md2rTO2vEo4gslLa28PYRtlWA0z6Iy5T88ZPtuIs8w-Qo_kRBjb7_8Sz797g4oChhE7jXTHYcZ7w19uuj5rSigZq9MViZK9_jDGMPWXQ8wdtDuelnOJHs8KjPaUli3KpBsOj3uCDXVIXp3wY0hFEaAEQKkLqlHZ_CE7coEveYOWpdGa9KVfvdSePWmERvNjiDLtgqE40GUE-5Tu9EQsRVQaGPF99Qh8vZqt_GXY8RM1g3ieDATgEgvyzFE4ndKGOZXZVwUQAEAdP4e0fa1kLYbQnlckufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/meHastL8qsBBQqLDzS_4aABlYY97IMyoLMWF42de1zGqp83BZe4V5B8OpW_iBPQeCwYKwtgSWhsCEvroSHxU5f9RemrYwDZ1zuok8wh6saF8qHKExTXnK1NgCeo8lV6Lpvjl4krf90rhYVoorX_7r9dyEZZWQ4xi0cSbL0sm5SHNhN_Xd2lZ4Y9wtG6WTETSTPwTqtZwi0vABEh77tnOHQObMw4CTcnuoNw7p0cBhCLSnB4aWasrcoHh3Ct6VMfs6Y7rpxCjjgDCyhzV66VQoX0s4csxiAzO-e_MovpocKYluRsvqoqJt9hNeC9ytXyoyHXp65ZkCgM97vVQG7gwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWExnU6otaHEeqvYdjP6eKnKuG4fX6fWQcZmhUuJLycYb07JDsVnZ8v20z6dkUdq3yvTS8u7HMwX8hbiDAs8U_C5w5mOAn1OftmC05ZgtS-9BeUoCkUR58Q116un6y66nlYfhsmly9sJMRyO9jtTpooj37NLb8QxRQdzyH2KzCpwWaYDDpSIx0j0vjGQHflfYWCuJrIjY0f0EzWfGeZi-huKCfw527oav0GqJzyVCMSrgATCykUkvgWYeA8GITZTU-4m25jTiMalQ_OI5tTz0I3KRfD1-p_g6QeeuZJq4wTz-tJbABVvLpSjrFd1OOeSZP7PHBO7lmJsOZbrLkV1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZCbw-xRaH6AT-munoGR0hXEaJqGFc0am6AUqkyN_zlkD-MlHzu6ffyp_0CvG8X4N8_jDwSAIF290U_dCSwzoXL0NF_EdqXddepYRQCc9_si6PEFjCOuQAeG1Okm5PSEt1dHel6f3Jiemkd0aRzysSNcjcsEW4H42ZJyzuqLEm0-r92Ixyve6Ar3mHcJvxn8Wfo2JC4xqzMmiWLuWgSZDFLf8usMHMQWJuWIT_q4iU-k5ztYWqovqFJqJ5rPCwhSok1Q5X418-yY0YK9NzGpRd8I4oJ_aWjh5Eis8bTXP1K_jmOgsVqD2sxQDrmbeB666VW7Yum2_LW5lL3NJxmWJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-fiqOS6VNXFlU21dRmzEJ0p-oAKy5qoQ3i07P5f4rUfK_Tg4Cs4fJc5ll_6Gsxadz8w5pPb7CQRxv3_evmmj9AiQNBeu5uJtNIvOeTAUNpr5Vv1m6jmBAfyWQdkfkA-RPipg6WUPemJXNV5f5o7915yppm3uz7tSoXblO32rdgVA1GtRe0wIW8PMXi88jmdairjiaMjnmfhOlLsHOxIGdf5upD_lYnTdG-w4MCM8AQP4KtuxE8zGqzvVV0nL8fYghSLBeLbMC-NOCebfZ7NobeL4BxtTdoFeJXdLEIMpOtrLYhfflZUNwe-DkzUvt8u23l-zt9HPSNsYs0LRkBQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=HoN_nfCyIghW0lH-OjelevP5oxE8fdv7hQ6oUpGRsO3t75sxlSGWG5rgGTbuA1b4uQwC-hVyLciWPY5Xr26P0AChmxpMdCuBhlAy3fMXCvEZ1H5ciSa7FxKZI6OpPgzwYx17IOeSv7gOIwXDOIoVE1V8px7SeXVPaOtHTRYOedkwbed6jr5h4Sd-rW475AuHRzs71gfHHNdj9LhwR5jKoL3O7fDLujiKL6Op8R0Gt_ojTCBQ25kbAT3M9vNggecfK3yJHkcmiIdvFiG_N4grWUmBtifTf1NYC-bKo4xTiI0oKE7nxRDTABdiLhyajGqY4z0bWa-1Zco6AE6RZrvTNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=HoN_nfCyIghW0lH-OjelevP5oxE8fdv7hQ6oUpGRsO3t75sxlSGWG5rgGTbuA1b4uQwC-hVyLciWPY5Xr26P0AChmxpMdCuBhlAy3fMXCvEZ1H5ciSa7FxKZI6OpPgzwYx17IOeSv7gOIwXDOIoVE1V8px7SeXVPaOtHTRYOedkwbed6jr5h4Sd-rW475AuHRzs71gfHHNdj9LhwR5jKoL3O7fDLujiKL6Op8R0Gt_ojTCBQ25kbAT3M9vNggecfK3yJHkcmiIdvFiG_N4grWUmBtifTf1NYC-bKo4xTiI0oKE7nxRDTABdiLhyajGqY4z0bWa-1Zco6AE6RZrvTNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PORy1yytBH9uOzdgny1m9tG3yKSBCEbHtCXd9y6FNS3U9d6ebMrRYoQvow0sqB4C50xaLJ5cb0ekXYxDhZukuEP926zZNsFMnhT8tLLfNWhtELi55DfEwEWU2yDrU1yJQdWOY23cIdOlhlXXRQu3hqLwOVdbra7YAx47wDDqd5QZjesBN2YnUv7eH_bFOsCVoWb014sHj0ZAu0qKJIS66jGJzeYVKT2T4zc-RN8NxVCiQtAgA48Od4Tw9dl012TyiSaEcSP14iBw4H_WHwyx66cMH9svXXsiyUiCXbFwnIVoj0eHPyCVc6kRpvinnuT56dQ-94DaKffKwMJSlJ1SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=BXFdnSG66Y6cn1han-Atsid38z79HFgIkLcb4h8abAoZkQ2Ms8htDlES0NScBI6akPmc1ykQsXc9-PeuOpc6_3L0R1NwPmHC55K37pB49Mr38U7-xqlx2H03jCr8TmtF6UUWbGWg8ofOt9-WlxlHQMISRBuPP4FvFzIabQAR6eKmI4CnwAHxB2pC3MeNtabm5yldp8i68DaEDxWaw4X_zn27fUzu6U2E01r7k6EVAiJic-al2HN4ob1jGwx0naWKwk-jhB4j5lCLx9N12rnnVUa-xe8b3DgJCFZBAe42_aZp8a41svZ3cAsBi1njkZiYJnH_D5YnwMF3KPGZuooXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=BXFdnSG66Y6cn1han-Atsid38z79HFgIkLcb4h8abAoZkQ2Ms8htDlES0NScBI6akPmc1ykQsXc9-PeuOpc6_3L0R1NwPmHC55K37pB49Mr38U7-xqlx2H03jCr8TmtF6UUWbGWg8ofOt9-WlxlHQMISRBuPP4FvFzIabQAR6eKmI4CnwAHxB2pC3MeNtabm5yldp8i68DaEDxWaw4X_zn27fUzu6U2E01r7k6EVAiJic-al2HN4ob1jGwx0naWKwk-jhB4j5lCLx9N12rnnVUa-xe8b3DgJCFZBAe42_aZp8a41svZ3cAsBi1njkZiYJnH_D5YnwMF3KPGZuooXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=nvrab7Y3IlQy3R4rAYsrIs2iWrvhkGaEbHdvHLHoWGHXe18pdGNlS1LvVTR11jrwR4F-o9xP-2ldHbp3IcyuA8A6xByXfomye3qrBijLOb_klX8nOvOdeB3vWM_QkMrFI9jXgtvhPvvatgjEpTD45IHsbJvJ8C9h9-bKuJbtB3xqrH9aYr37OOcFsUf1fkOmbf0jzvpPqXNMXJAfg10hdnU7kWVdriOuQb7tZfo0nrKpG5i3ol52S6ePsnuEzLyaWgMVO1ZK2LSUMDfb_jl0u44gkAZu_3HIpeCr08DZPo279fUYx5RngIXkeA9_4dFU91uUxUOgZA5kfh0zJj4-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=nvrab7Y3IlQy3R4rAYsrIs2iWrvhkGaEbHdvHLHoWGHXe18pdGNlS1LvVTR11jrwR4F-o9xP-2ldHbp3IcyuA8A6xByXfomye3qrBijLOb_klX8nOvOdeB3vWM_QkMrFI9jXgtvhPvvatgjEpTD45IHsbJvJ8C9h9-bKuJbtB3xqrH9aYr37OOcFsUf1fkOmbf0jzvpPqXNMXJAfg10hdnU7kWVdriOuQb7tZfo0nrKpG5i3ol52S6ePsnuEzLyaWgMVO1ZK2LSUMDfb_jl0u44gkAZu_3HIpeCr08DZPo279fUYx5RngIXkeA9_4dFU91uUxUOgZA5kfh0zJj4-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=P2XkVo_kaj4t-fMWnGkhgEtIOGJX75n4o3hHNmwHEmDTKSCioaoafTgGbN0yiyr6z23nTkTNk1w10ojmda-YPpWTCuo2Sds4dl-XOwqWGPZ3wzPrxr6JBFNWg1qmgjje9CEi4dKsBW3kwh1LuquI7LP_TvOCvKMQZBuDsBPkOzZYirMS_Ey68KWvpUKYKN7PHexoVMQaOHXjkKGH90Ayl6RY-JoXTCZoorE33TAd2-zdhLDAEJ-sWm39pK3L66K397ygVH08Sk_sngFwpXCE7Q0els3RAWx73oAzNGGwEz0_o2ETbByAdN3p_rZ17pnJYcfmpbYGyTmimsfE5tmJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=P2XkVo_kaj4t-fMWnGkhgEtIOGJX75n4o3hHNmwHEmDTKSCioaoafTgGbN0yiyr6z23nTkTNk1w10ojmda-YPpWTCuo2Sds4dl-XOwqWGPZ3wzPrxr6JBFNWg1qmgjje9CEi4dKsBW3kwh1LuquI7LP_TvOCvKMQZBuDsBPkOzZYirMS_Ey68KWvpUKYKN7PHexoVMQaOHXjkKGH90Ayl6RY-JoXTCZoorE33TAd2-zdhLDAEJ-sWm39pK3L66K397ygVH08Sk_sngFwpXCE7Q0els3RAWx73oAzNGGwEz0_o2ETbByAdN3p_rZ17pnJYcfmpbYGyTmimsfE5tmJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyFstqKTMevTbzLmfF48PDPFzuS-De4okaWhIOSA_YeKS-6vImgpS3dW-kDw6wg5t4oMTlSRLvUs63qLix6vj08D-T_4-CugqaRyC35yny2jX5yz4k_axSjyQ66ffQRh60v09ka1LDVdc08ivwi441JFXB2frE-PkpNAU-wfSOyoo3nRKaa6IL77WkBBehCceJUirNzZsOoxcUv_yqTctWYo83I6OvdzB22fCI51wHV00ePAUWCNfFDyqhJi9AOjwVqNIvoH0Kf1_Pwtx_ME5wxUOA92Klp9WrstDlQL562qOytQY2VcpScT-fpJjOUtImFn51WZgalRNZPvfR1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=IQlUErrD2xf_0qaiWzpvC2joPf76Kmqdh2K0SMS3DJd5Qdv-1P6EuddxILHxbEwra2b58cPgFmP6z7kJDwlNLsYDiUGKza8tjaegoYJMU5q9f7dGWKhnMlPukvZB4l2XWyacPsmAzRFsEI1KaTqLLqm35yVdGqc6grveS3HCcwGmkeI3FEWWNbpoTNmvMSsSwyeweWF_4gHG4iXo4qnNje8HPucCBhtAB28uwguxLzsb_pq-ZTSkRxdCJUN-mrT2nxLPxcbuG9MwFQSLFcqxNMQ3gnvfUK6SjzAn5ry_9Q2eR_ZHatYWlfXlJMCs1s5hujGZx71DsPGNJ9GBnsvHd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=IQlUErrD2xf_0qaiWzpvC2joPf76Kmqdh2K0SMS3DJd5Qdv-1P6EuddxILHxbEwra2b58cPgFmP6z7kJDwlNLsYDiUGKza8tjaegoYJMU5q9f7dGWKhnMlPukvZB4l2XWyacPsmAzRFsEI1KaTqLLqm35yVdGqc6grveS3HCcwGmkeI3FEWWNbpoTNmvMSsSwyeweWF_4gHG4iXo4qnNje8HPucCBhtAB28uwguxLzsb_pq-ZTSkRxdCJUN-mrT2nxLPxcbuG9MwFQSLFcqxNMQ3gnvfUK6SjzAn5ry_9Q2eR_ZHatYWlfXlJMCs1s5hujGZx71DsPGNJ9GBnsvHd4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rje9IXPEaF4cGOvPEyiaXyCtwE-tgBmwwuliJBHVOpIAwAWd1dB0ufUXguwmTnCn0nop3ed2Z_Tiix9BKt6UnAQwCDsdOuJsmbk0TUVP0ykVr93r9SiJ5RTJjsBVJwKbc_tm0idfEc7kgiKbaONGa8P2FiNA_Qzu-lGRI97HdHSIxEp59D9Wh2owsqGBfGTiKTUEEVl_xxQ8aS3aXfWUiHwKi0WiTBzSMEO8-lCP6mlgdgZld8Wle13uQG7DVlgWbjTgUFHhP1zvrLPEgdBTExD33SXxuw1XCp0JMPQNUMhUbaH4IUG0P7Va5iOvFhJ85AAeIl9aoDlfzlz5hfD6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=ZBSS1LEGBhZV-oN_j8mlBrcHQzTY7S4rhMziypLEPVY19sW3xcqLJt4O02SLlaz01PocoGvCA8Gy0iotpu4P_-W9jlPVbr8WiXSIh3N7E7kZr46JWRJxJI2eUoBR8oOAidY5g75RkrVGBy4GX4AoH5Jh-mPwjSiUHauMTZvXvW4XklHcItuJMyu_dd32yJw7QpeZSRkgmZ2gGZXPKCZ6H4JKQq68q609ytGyxsAO91UIbHrZ3b6G-1aNN5fUEY9U43PJ3cP9GEO9ArQuHYbV3k-zRLmqPdkmKcn6TdqDsP4_EDgzQVXSdyHJHZyzpC6MUFcascGLMN0SQXufdnEIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=ZBSS1LEGBhZV-oN_j8mlBrcHQzTY7S4rhMziypLEPVY19sW3xcqLJt4O02SLlaz01PocoGvCA8Gy0iotpu4P_-W9jlPVbr8WiXSIh3N7E7kZr46JWRJxJI2eUoBR8oOAidY5g75RkrVGBy4GX4AoH5Jh-mPwjSiUHauMTZvXvW4XklHcItuJMyu_dd32yJw7QpeZSRkgmZ2gGZXPKCZ6H4JKQq68q609ytGyxsAO91UIbHrZ3b6G-1aNN5fUEY9U43PJ3cP9GEO9ArQuHYbV3k-zRLmqPdkmKcn6TdqDsP4_EDgzQVXSdyHJHZyzpC6MUFcascGLMN0SQXufdnEIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=byV9YMZPq9JPs6I3x12IVk2nxQOnzRrb1MVDxkvoVmAedUOLoLR39wbNhzmm7PTO6ooEE85O6CLI-Ahaxx2m1uhilbqSFuzmgfDi01V5iIDtqelwI_aLXdrbccePq6RaBuZ6kuWFulJTtPED6VV8Ua5aueIJSMcA3Kb3mABSVX6aDDL_XRECMdJZq56WJ_5jgzBYUqh6dEbzdm-jwWSLYkUzMhnk0ol-DekLTb895zcYaE9wcbxWkQQO9DxfslPuc-zOFPKUkpCcdhn8xjsEGz4SGTJK1IbaWhT73U8v2SsrJdJ3Mo4Om1AAMan-dRhZ7WO5QCRohMTPaIs4Vinxlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=byV9YMZPq9JPs6I3x12IVk2nxQOnzRrb1MVDxkvoVmAedUOLoLR39wbNhzmm7PTO6ooEE85O6CLI-Ahaxx2m1uhilbqSFuzmgfDi01V5iIDtqelwI_aLXdrbccePq6RaBuZ6kuWFulJTtPED6VV8Ua5aueIJSMcA3Kb3mABSVX6aDDL_XRECMdJZq56WJ_5jgzBYUqh6dEbzdm-jwWSLYkUzMhnk0ol-DekLTb895zcYaE9wcbxWkQQO9DxfslPuc-zOFPKUkpCcdhn8xjsEGz4SGTJK1IbaWhT73U8v2SsrJdJ3Mo4Om1AAMan-dRhZ7WO5QCRohMTPaIs4Vinxlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=YcU8ztQX9_RIDvsbwwjzoi-u9eRUAqpnAQ12xWlZxauafkeYaAzDvxdyl5x8Jg-T_yUlfmJcEnJka5sDZK6CN3SZgLYv1pmW_5UHtwntTom1mUQ89BKB4H1VVJTLwZqeErWCEkBL-z8A1XwWoka7Zb8hncPzP89gp6121fDLkXlxE3jPOk5rvDOTzCdtH5ttQ0BhLOBNz7XlYl6xxgqH5sImINcWQ9Mws6jPrEjG0XqggHEUZPPoTCRaC77nzeMl10wDP5AsDiGUK1lhDMw1zs8WRUQIaZ_2oHcEJHTTuDajPDDJ8s6N56mYMXhhYbpJwYI24hhweo_5q0UDo6q2GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=YcU8ztQX9_RIDvsbwwjzoi-u9eRUAqpnAQ12xWlZxauafkeYaAzDvxdyl5x8Jg-T_yUlfmJcEnJka5sDZK6CN3SZgLYv1pmW_5UHtwntTom1mUQ89BKB4H1VVJTLwZqeErWCEkBL-z8A1XwWoka7Zb8hncPzP89gp6121fDLkXlxE3jPOk5rvDOTzCdtH5ttQ0BhLOBNz7XlYl6xxgqH5sImINcWQ9Mws6jPrEjG0XqggHEUZPPoTCRaC77nzeMl10wDP5AsDiGUK1lhDMw1zs8WRUQIaZ_2oHcEJHTTuDajPDDJ8s6N56mYMXhhYbpJwYI24hhweo_5q0UDo6q2GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rtt4st6j2lF_p_yCjvkWvykS4824XMlja746hd06tH0jklMeL7U0Y9gfE0ZeDNU_6SzQ87m_QOje0BrfCV2PsHHqG-u-Liw1tAU1UN9c1JTT4L2VoDy1TrJjh3DnG52nV5XaTIi7cz6g8G5YHjn6-_WMhdUxxaDmnfPPAB2aMj5Z2FVvvnsVaS_4SjQUVS3Ol0J2ijVTBq7oPpTxdJtOSzKrs5kGsPWFKfsJU_0khc1VUKYemgySqoiRIv-bt5DQQPl7rpXCQGv0COgqoU00_3WDE-CooSlPQ-5VL87ZJ4RmsofqYNS0YRlJ_PpVpFU2rqF1fyeiTCMT7DWR1Vdh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=srayeAVcdbaJ9w5NSkbZyXXch2XYd7yLHSdAZWXBUzSI2Y4rvBBq8towOZ0IeZXHnbUfCxT4tLMNy_sSLMH_WFdmCFJ6G-DaXVTlih9LEXUMqFNCb06WZShlxH_NY4ba0Ec_6tQnBaq7P0HWqaPb_iYP_Nu-umHSmcmlPueaxvSjrKshZtRczqjU8F9EHOuIWWvX8tQTC-IB1QnNz5N4V05V6KQQNZzLfgotsoLxI5BkfRW48WwFL9G0rlw3uJeo64OmR8WYACdMPN6eqJkx92GhwP7CKIt9HabyWQxJWRqrTymqhaGZcP4a6ersGF8o85k7hFbaq5gsC46uPxllNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=srayeAVcdbaJ9w5NSkbZyXXch2XYd7yLHSdAZWXBUzSI2Y4rvBBq8towOZ0IeZXHnbUfCxT4tLMNy_sSLMH_WFdmCFJ6G-DaXVTlih9LEXUMqFNCb06WZShlxH_NY4ba0Ec_6tQnBaq7P0HWqaPb_iYP_Nu-umHSmcmlPueaxvSjrKshZtRczqjU8F9EHOuIWWvX8tQTC-IB1QnNz5N4V05V6KQQNZzLfgotsoLxI5BkfRW48WwFL9G0rlw3uJeo64OmR8WYACdMPN6eqJkx92GhwP7CKIt9HabyWQxJWRqrTymqhaGZcP4a6ersGF8o85k7hFbaq5gsC46uPxllNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=Rtw__xx7rskoyCsMt1d-S5f9mD-eElvncXnnti2E6Im7LovsqZHQ_4nunLevGZhx_fhk2mbZIS5o9lKs_OJjYMZFR8zBn73E336os8_bKX1eCfFO1DH7ngFKuo_1AWXzgiwSpbNdU4iQlWF-NY5v9X7T301oUAntYu89WcvMfsnOtnQj6sRNlinOGqlGUhrXkDJpTkBlQEXfyovBanbimPGXxDuTes6rSZaALClYUnHmF9YmqRkB6XRN-FObqPmy8rOmqDYVH4ml7GUMXK-KRKLzw5KTgIXaW0bZpKfLxtD48RwI-G93bCkX63IJ_vNVQqTa2xFPYqM0968zYWlHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=Rtw__xx7rskoyCsMt1d-S5f9mD-eElvncXnnti2E6Im7LovsqZHQ_4nunLevGZhx_fhk2mbZIS5o9lKs_OJjYMZFR8zBn73E336os8_bKX1eCfFO1DH7ngFKuo_1AWXzgiwSpbNdU4iQlWF-NY5v9X7T301oUAntYu89WcvMfsnOtnQj6sRNlinOGqlGUhrXkDJpTkBlQEXfyovBanbimPGXxDuTes6rSZaALClYUnHmF9YmqRkB6XRN-FObqPmy8rOmqDYVH4ml7GUMXK-KRKLzw5KTgIXaW0bZpKfLxtD48RwI-G93bCkX63IJ_vNVQqTa2xFPYqM0968zYWlHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=X__i2O7Vx1a71lRg8L-FNQpoObJvHC06QLG9LP0sYo8xeyiyIDpSA6sBJieY_-TWuXn2j1KN85iuMx-21XdBSU0dCI501FAEKCfK3FB9T6XNX2_XPp9Uc7wvoNA88wZcMltaHtG6IzX0ncHyBlXpGTppHQHFeVVareb616XNHyk1OJalvNHjJAR6hzwsDEIp9ntJ3I-3rtJW5YC2gjfqHpsx-QuiygLRiuz6m1ifiKm88ufjwoF59Frp6gR8QNnGrEvQUO4eLRSJQdlQAn96C6Gu8UYolChCQazYJjyCh8kWN0YGcvyFDL-DngyuEYgFBQvfC-MdTob4q2R1_Rk1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=X__i2O7Vx1a71lRg8L-FNQpoObJvHC06QLG9LP0sYo8xeyiyIDpSA6sBJieY_-TWuXn2j1KN85iuMx-21XdBSU0dCI501FAEKCfK3FB9T6XNX2_XPp9Uc7wvoNA88wZcMltaHtG6IzX0ncHyBlXpGTppHQHFeVVareb616XNHyk1OJalvNHjJAR6hzwsDEIp9ntJ3I-3rtJW5YC2gjfqHpsx-QuiygLRiuz6m1ifiKm88ufjwoF59Frp6gR8QNnGrEvQUO4eLRSJQdlQAn96C6Gu8UYolChCQazYJjyCh8kWN0YGcvyFDL-DngyuEYgFBQvfC-MdTob4q2R1_Rk1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=jmrkJ7F-3FGiQi0bZ6p3KWOuAO1LzEm95BrCGtoxiXi0DvRFKFvHe0rKDLUUui509fTOs4J_Lq6Hib1X8AwuQO9tIO3pxjQ6UuK48_6l5fi8dxuBl48AFKGYaFhzzgez7PSQ1Ygqi6zRCLxr7TnvauNZ9S3qlDOizhObmGMvgvFUmSv9uke2jvB8bRjChMl_LfNqZguQeznil_tOiLfunMokOsK9nCv7yVa8NGn7-9khYMjTrRsbif7Q0OQrCkF81nnnPuCuQwGwVKNgxEBHLxPIB7c3Tan2mB__hWaVZBIHjHRfJjBVuPnQDqHur0Pogf_W4plGLbLFysJ89yzT6pqe2bAYRoeBviHY8MVMFT2Yy271pOXtaFF2XNvuGT0mjoBJSJmzOBIHu6RIYTozQITeFgYw-Ea7qh2LbDKjjHy5dDJcx4c_gJkUGtYtX2qmbaerLOlNflZRIHiyz4khs1KkrwgzDc_mK7VNpwQVqApV6sUB03kBWl9RQrQ-UgqYcIGIbff69G1I63yc_GJytpnRC4VLBJiHojYWYs_ppb7SP7ENVXQ4xw8NnXmi9Q6LYL7OFjwMbVNmNAhXtNj7wp9wT7v4mD8Z5SQXhcPX0qyRROk3vFAxbb7Il3UaZnA3-b74HBp7VNaXUAZlelbdbePJloOiiRbnB2_fDAGDUG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=i_7QK28n7c2H57clAlburZhLyn-Cxg2ZiBy2kh9I2CeRnzI8cEWQHL9CgtBgc0Id1y5yO-v4162ByLawIuuFSvLpY_w7viu2aPvK43eDevptUSUNsB9TB-xMBKaclwdxaGmGQYC3b340YPmhnskN_66PrLReF_klEW35LN6H0IZrVH2LckV4RTUO65piG8bxqn2ALN6fQ4Cjo2Mfc9srB3-8kBZDSwsdnw92AtlRqTBFlMM7l8y1B_1IRSvQTGxFShyiMRuoqW-qUxy433byZK9ncQD1kopyiyjsZr0ozgK1Hlbs4j8tT2Ld5Sb5gthO_QtaOBTV3oOUAuraToBWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=i_7QK28n7c2H57clAlburZhLyn-Cxg2ZiBy2kh9I2CeRnzI8cEWQHL9CgtBgc0Id1y5yO-v4162ByLawIuuFSvLpY_w7viu2aPvK43eDevptUSUNsB9TB-xMBKaclwdxaGmGQYC3b340YPmhnskN_66PrLReF_klEW35LN6H0IZrVH2LckV4RTUO65piG8bxqn2ALN6fQ4Cjo2Mfc9srB3-8kBZDSwsdnw92AtlRqTBFlMM7l8y1B_1IRSvQTGxFShyiMRuoqW-qUxy433byZK9ncQD1kopyiyjsZr0ozgK1Hlbs4j8tT2Ld5Sb5gthO_QtaOBTV3oOUAuraToBWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5izKKw8aWGsdWk0uo0X49MvB6_E-fCQ1uAoITYvVeTG-POxEzEMHSZr6Up7KdJEGfYo9jdPZu3iBJTn_fqwtVc4W-S7lXDyZdI_NAf5g0FYmT904w5TC1HZK7VWRNoVZK-zjHuXd3fuSBR8AeFoklC1J_q9fGqbU3qbXiRDxHyrA104XJdT6-Nz7bIa0HXKQ1Pfl2mocfc3fCPkl3RMY2D0r7IkeXtuegUl3rxoEfdqJUcI6xLTCwK9Fcbc66CXdJ3_rImQORRin0GQGrWLOe2zBf-nzTrWEH9z1smd9r_MQukKR5qicSu17nmhMd6L5CePVrDid1XS-Ikn31rnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBan7KniBG4xtk1IjuFf8UAoCGgiaSABVr0wFtXf3_1POsQHVt-_7wk0t56gW9iYVv8luC89MAO_hHPmyGn2RVYYqhT0W-pU_-LgwdTFTE8rc1oTOaBQRKekmZy52RXojAaMYvxuY6zk-bwbpC7Fd0OS15B66b1g5nb7IeaggpxV_Ctqb78MS2pJ229an5hBBc7KnNdLqx7yYEOo9HS0mRMA7HE3OLtOgO_nv-XxgL_vAX6FU93vVZXcrnCDPhcl6Mzf4BoZgdfEd5F-hKqKsWVZn0_1bpts05WEKFSViwBdAcVDXv-yJj5VrHMxvrE7BZRi-0_ixn1AKlJAVPNstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEHDmKSBl7humrqYwQJ_GVpqT0UUYTOMGfWrqWNL1pOTzHwQIk-2_EuwuCBhE7Qj0B0op82u0r-yozGTLKicLcbZ1iQ9aDIoRsURPLqKFg-OhmZ8CMNHnJuNotu3X9M464JlyDkmwCCCMO5Ul3zqOHhk-JP4j7XZoxWz1tY5eIzeyhsXHtn6brgEa1Xd9yePwBckiiGmX4epNrkkroBuUGZsnEyLCga56WE5ncFENcWq7JJrOKd8vY_YOyHl0lv8AmCKKbDTo5PDitKAHXVDsmcBCpftG3s-h2p6h5J6-rMqWbUVrJVLluXKVpJBY2XpNw1J1HZ8mJPoXclOgIF1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsEDMHaEcXWM4KUZas2xyGsTfYfYS2zkhlDpdj_sjajKMeWDambTkP1fIXPigtSCxVpSopNinrVVXgdyI1rD9Xt_P6GhYEt5XiZxIn19ZlPVv9tMeRJHd_Fnsn-8feVxQN4eF_x6jFpxnmlKhC5C5Wjscd0FPL_VIx1e6kEwEIJFYKBXpli68nileny4fpE329NGUD8E8WZUodpu9vB2J3M10RxN4_QNV4HHVHvAZYSrvG6xqwybH4LkoAUuXZK5GiKMG1HFqfqWpMt7XNcY6TIHigu2VF_dReCSmHEhIyiBrZ7itLkPT_ksBHXnIDJ4AuiF911avuu8qjRsYXKZdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=XJy_-mzcLOJuRF02A2AWqjVbTHhhIsqFKtnBqIBwDHL_V7KoXoKBBwUhG9aTjuiyB6n0-gjGKtYkDnGJ_Vu03ZmU1H2FChTBvPFfpDdZKuyUl0j-srAN7NVPyjIgPtpyCHf4C5mYm3wUPEzrUcZoV3Sydij9JRQZ3U_91uvvmfTF6ssR9w8tbEPj7si-yK4jnlC2d7XibjGELyvq6ZVHxhDVhn66_N-XEoXXamSyr2OHPesluD2agxS03vzKWxTcjrCimAuw4WBKbY7__Z2HovP3gIESPBqhJ_3XotgALcbbxNHipZhGzIvTOoiCzsmYqZqgH5O83C5teol2VSMo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=XJy_-mzcLOJuRF02A2AWqjVbTHhhIsqFKtnBqIBwDHL_V7KoXoKBBwUhG9aTjuiyB6n0-gjGKtYkDnGJ_Vu03ZmU1H2FChTBvPFfpDdZKuyUl0j-srAN7NVPyjIgPtpyCHf4C5mYm3wUPEzrUcZoV3Sydij9JRQZ3U_91uvvmfTF6ssR9w8tbEPj7si-yK4jnlC2d7XibjGELyvq6ZVHxhDVhn66_N-XEoXXamSyr2OHPesluD2agxS03vzKWxTcjrCimAuw4WBKbY7__Z2HovP3gIESPBqhJ_3XotgALcbbxNHipZhGzIvTOoiCzsmYqZqgH5O83C5teol2VSMo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy_Bnr7dqR7ll2k5OMp36tyggIix3EoPOPMrCXh1cbnTKBmwPa7JikIISuqt4_WcIE3dyHs6-viaf2B3mHpawqNf-7lbFeI9HECDn7JtuytyPfiKpc4OuchluL-oPlKS_0d44mue7mctADGMRioCai4TRYDmnRTdJtoaPu1l1M8baXXefTZetD0qgo5lhZPsoB8T26Pey2gq1qSLLK7f5F7GG5VH92JMagY978Z4uvehQfxKh6hcwWK58WOm4YFHgYNg5WRtBcT5ELxwiFLnEfzPmdVCl6GwXKI_x1EgPAo8zwglXBeGh_OhSBJBJ0lk0MBaWAJAoU3qefbnVQnLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=PQZ_TUyCjpgm2lg3VoDkuM-dz05jfT50l_Rer03LMKERFA-e-3mDMpM5iSrMCEbAh1CQGV-CtaMFjDwWacrm9LEn_eAM1hDU5SMzAi_JMnj_ilhyVteaqQ68VBmdHOthmpTrU6ExvfzqEXNvkvHNk1rjEPxos5CrM6No37Cz30B-zKKe52OWzXNlgj34CJP3LTBQatYv2aAiOUCkAcsNo61VppDuxaEeTN_BYa6xqJuQgHn6yOtkAvhj93LGavVg2m2AVqReezyT0wAwOvNMuTImd_8oQPgt5fc1tjglABA0i54wCYHCAhN2lrVEIhjMrNiAuolV_nNBImbdSdAE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=PQZ_TUyCjpgm2lg3VoDkuM-dz05jfT50l_Rer03LMKERFA-e-3mDMpM5iSrMCEbAh1CQGV-CtaMFjDwWacrm9LEn_eAM1hDU5SMzAi_JMnj_ilhyVteaqQ68VBmdHOthmpTrU6ExvfzqEXNvkvHNk1rjEPxos5CrM6No37Cz30B-zKKe52OWzXNlgj34CJP3LTBQatYv2aAiOUCkAcsNo61VppDuxaEeTN_BYa6xqJuQgHn6yOtkAvhj93LGavVg2m2AVqReezyT0wAwOvNMuTImd_8oQPgt5fc1tjglABA0i54wCYHCAhN2lrVEIhjMrNiAuolV_nNBImbdSdAE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctrB4J10jmoagGFAcNnCvl1u_fekrOiQl3rhTH1MYit6gAGrc6gfX35phrVCpnsAWzZeYuLxLWCbYSvO5SuLs02aE9UF6P6gmaZmQ6YbfDI8nGcoptD0nn-VRz2_rymM4Sa6AX1TlSb10cpw-EGIRNIWuZmJh4j_nHb3YMMxlkIK8QD2JzLYwqXGCQeQ3sJ5QJmI-oa1E8WwJWKFrD2iI3LiiKj4DBb_qLKxe8Ey0epp6iJ5yn7dCiRzJ7xx94pCaUZFvD5lRpdgj-K7971Evo9rhn2Lx_r8EfPefyIlEcH4jePx97xabUJBiEP5PSszuteS7RC4Nzj9QKQ8tQwYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=BRBxEWLhHdn_ouGd8TLleVHjXDaYtWZwLMv2Qw3H0JX3U99XryWLMT3c0Ro6XTeV1LstiBrCMGymwhk7NZApSCODHFRGOM8PhSVeHCI9I6JwxR07HcoVMj3e2L1iWYus69Nw2FmCSgoY2kFgq8gp244owB8xSHip7c6TVhkoaGm-ZNqUg1gfI2FTkt-LMbpwwRWa4k3dyFYlBhTGodqM4CW3OsfMwvGUcjVwexpB_3O7SSWPShbS7tqzbDoRAxqGKJ4G1E6FZO5VnpknR8QKJUnvgalP_VeMjbmPNs321ZluS_AmLD7c2V9Qs3omyhqb0Dny-8ibgWnSo-v3ADBLcLo_Me4IrqH4Ni6XlMiYUTOL4P4r4gIJXN6zJBwZy4kcToets_DWEfIosPA7i9jieQDU-zHDVe4ubxrY8i_NHDaXLPJoHkvSx5M5lIarxLXxkIPfBbY5sYHLVRD0vzMxzuearvKC2qc1mczqSMeDeDVU0Z3jLT6JA-LEil7Rfk20HKiYHQJLVSzPKJz5MFAAC7uZgund9smk4JF9iHGtKsz_cxjpuChY62UOYrnHffkXcA3c1BY5qx-5B864xk24s0W_95yzQHHaXlREQNuDF9nTdRtOyJCmw9_8je6x-WjguW_NwPlA0racEn3X_PEbvPJy1RfQS371P-HcuwVuqXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=BRBxEWLhHdn_ouGd8TLleVHjXDaYtWZwLMv2Qw3H0JX3U99XryWLMT3c0Ro6XTeV1LstiBrCMGymwhk7NZApSCODHFRGOM8PhSVeHCI9I6JwxR07HcoVMj3e2L1iWYus69Nw2FmCSgoY2kFgq8gp244owB8xSHip7c6TVhkoaGm-ZNqUg1gfI2FTkt-LMbpwwRWa4k3dyFYlBhTGodqM4CW3OsfMwvGUcjVwexpB_3O7SSWPShbS7tqzbDoRAxqGKJ4G1E6FZO5VnpknR8QKJUnvgalP_VeMjbmPNs321ZluS_AmLD7c2V9Qs3omyhqb0Dny-8ibgWnSo-v3ADBLcLo_Me4IrqH4Ni6XlMiYUTOL4P4r4gIJXN6zJBwZy4kcToets_DWEfIosPA7i9jieQDU-zHDVe4ubxrY8i_NHDaXLPJoHkvSx5M5lIarxLXxkIPfBbY5sYHLVRD0vzMxzuearvKC2qc1mczqSMeDeDVU0Z3jLT6JA-LEil7Rfk20HKiYHQJLVSzPKJz5MFAAC7uZgund9smk4JF9iHGtKsz_cxjpuChY62UOYrnHffkXcA3c1BY5qx-5B864xk24s0W_95yzQHHaXlREQNuDF9nTdRtOyJCmw9_8je6x-WjguW_NwPlA0racEn3X_PEbvPJy1RfQS371P-HcuwVuqXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=vGCBRGNlBvWvjMDWa3eJf8KjGrvnGMkd72-uIfKGwjAYHbqo6sfH9-qx5aCdBwMHgRf9x9p2FNkwxtIwVEvHLnadAP61cBHK66U18_445WUIXbT7v0n8eHHOHvJbz6BVRLL4SjOqozCbEc3N98JCpf84tBYqkB3edTmfisbj9pB9DFZgRlO8NPAnRKC_Y-eHc8HEnCFr-87PqDYqwUsV2a2ko-6YW1f112V5-lAo8TVJbH16UgkpoCh2sNK1fV3S3u1mNIEfTSZ0sl6ccQDUzjyr7GmpWpaxA5pKcx6RYPRlYbvv99dDW5qY8cXt7r6X7UQY7Ky6dGHeEDkp5po2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=vGCBRGNlBvWvjMDWa3eJf8KjGrvnGMkd72-uIfKGwjAYHbqo6sfH9-qx5aCdBwMHgRf9x9p2FNkwxtIwVEvHLnadAP61cBHK66U18_445WUIXbT7v0n8eHHOHvJbz6BVRLL4SjOqozCbEc3N98JCpf84tBYqkB3edTmfisbj9pB9DFZgRlO8NPAnRKC_Y-eHc8HEnCFr-87PqDYqwUsV2a2ko-6YW1f112V5-lAo8TVJbH16UgkpoCh2sNK1fV3S3u1mNIEfTSZ0sl6ccQDUzjyr7GmpWpaxA5pKcx6RYPRlYbvv99dDW5qY8cXt7r6X7UQY7Ky6dGHeEDkp5po2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=pxwyfirgLfYRFicd9VJlXcMm3CbVvO1YZDjN7U9IBhtqU4EJaDZA4zj1obQmUZeck12i4oBaf1EUqFxaJh0trgTyrC1P4jr-16ou5BUl3oES1BpfeW-fKTsXSGwjjilpJ6o9HB6OYN-RsxlBBwNt4yMelB0VSJNfo91Fgo4QY7mNUPF_5RkQqMzZ3AL-x5IKrv-LnWKIjso9CoUwy8pNfSw4ZvQ89jxhAIUCcf-yC_u2Lw0cTBJX4Qop9Sszp2nuK_nzeBEKlI_-BwYUfAKdDR-io_KAyoimtsZwkql18Uu0zgCrN44DfjTCFVf7o0anvQICFQPJtlwO2-4nkoV8Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=pxwyfirgLfYRFicd9VJlXcMm3CbVvO1YZDjN7U9IBhtqU4EJaDZA4zj1obQmUZeck12i4oBaf1EUqFxaJh0trgTyrC1P4jr-16ou5BUl3oES1BpfeW-fKTsXSGwjjilpJ6o9HB6OYN-RsxlBBwNt4yMelB0VSJNfo91Fgo4QY7mNUPF_5RkQqMzZ3AL-x5IKrv-LnWKIjso9CoUwy8pNfSw4ZvQ89jxhAIUCcf-yC_u2Lw0cTBJX4Qop9Sszp2nuK_nzeBEKlI_-BwYUfAKdDR-io_KAyoimtsZwkql18Uu0zgCrN44DfjTCFVf7o0anvQICFQPJtlwO2-4nkoV8Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=eSKgwoEPevlovTU9Fe3DMQtIMbuj4Mm-8gLTv7PYxoCiZyywx4s6AGLf4mdTPC-svpIo30r7XdVsbApa8obZH55Oe068c_kKI5fmxvIRoo0RgPaYuwFgMSiAZ4wFxJfSgS2ED8O7St6eyO2wQxnnvm0v91pw2yWCwN1vjfzB48aS5EUpBTTEakylRFkBNApIhkmyLDfxlFbJbvYeY32HaiEU8bgdW_61ZFBJ-eYsSaR8yU437F6oJNhPvR9oHe0AjgNZuTvHxXDJrZ61XJVKP06dLMgtd4-0gDugKPbeDEqBEK0fck12Nv6UbbH8mz0MTEf4EQhyAmzWycUqJkN-Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=eSKgwoEPevlovTU9Fe3DMQtIMbuj4Mm-8gLTv7PYxoCiZyywx4s6AGLf4mdTPC-svpIo30r7XdVsbApa8obZH55Oe068c_kKI5fmxvIRoo0RgPaYuwFgMSiAZ4wFxJfSgS2ED8O7St6eyO2wQxnnvm0v91pw2yWCwN1vjfzB48aS5EUpBTTEakylRFkBNApIhkmyLDfxlFbJbvYeY32HaiEU8bgdW_61ZFBJ-eYsSaR8yU437F6oJNhPvR9oHe0AjgNZuTvHxXDJrZ61XJVKP06dLMgtd4-0gDugKPbeDEqBEK0fck12Nv6UbbH8mz0MTEf4EQhyAmzWycUqJkN-Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElDFZ93mfl5rOt4E53kvhPWfZXqK2m-OLiHT_j3H0fpacQBHb0vaDmiGx5PPPUqSChQkj2xiuyDaLy6sAKc36yJUPUOYJ3NMxf_kxyLmI-tdTWAkwFcjY1p5oyhf2S7yNAaGwouLG7U_WPvML8N9kCz5IBfcAMLWREYIFgaEgwAXmddU4cjU0McyD8zBbyGkfiS9npHOVW1v9S091al3FFWIlgnLeYr345v537I1uMYY5u9qZ4cf_uy0lDrLa1bnPrAuB2bRDdfIsvPObC8Kqh-1aghKUDwFbcU42xdeuUl_HD3KVXDPtHzJErQ-RO_kz1zljkcayZKMZuNqs-mIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=Uzdw4HYLSjl96663prZmBwKxt6bMRBp-e-1BIp69qCnjnPKHT8O58SKP7AZgyNgtZfvdoFho2rJdx-olVt8WTh2bhzwTJWXWuqIf5K56LtmfzZ54f1els-ST9K9OPDnMiCMTRYRTn2l5jPa6aqdf6xPkOXBRKMfHJqvYFyZxaz6H4m32qzR2NnwbPVGo9S3NT0v5X0RxJCosW-Elw07DE99OdsYA5GlV74kpX2KPs9jjdAWHsfZdobLJUd0IGtjzdmvhPtEhnO5I-sdX-3X_2ZPysdmjd-tnFWtO35ntbnAvydbZIJhiwPbHK06b4SQ9I01_tCBNCCFAt8oh0LwIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=Uzdw4HYLSjl96663prZmBwKxt6bMRBp-e-1BIp69qCnjnPKHT8O58SKP7AZgyNgtZfvdoFho2rJdx-olVt8WTh2bhzwTJWXWuqIf5K56LtmfzZ54f1els-ST9K9OPDnMiCMTRYRTn2l5jPa6aqdf6xPkOXBRKMfHJqvYFyZxaz6H4m32qzR2NnwbPVGo9S3NT0v5X0RxJCosW-Elw07DE99OdsYA5GlV74kpX2KPs9jjdAWHsfZdobLJUd0IGtjzdmvhPtEhnO5I-sdX-3X_2ZPysdmjd-tnFWtO35ntbnAvydbZIJhiwPbHK06b4SQ9I01_tCBNCCFAt8oh0LwIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pM9g4G17-57rMUS-548Fs_fx844akVcDobtvdb0qi5UtqrZbTPC4GKCsKUJkzpSRBqZQVPHw6Nvpueagho7NAkYzXyBQkuZ4--W7qAQtDEov8xpmLrixXKCYKaBr0KQIO4anxVH4n5OieNTSoJfUFE-4H00ezcSCM48P43gj17ZjuOXQPXWVSWPHvNuBrTKeh7TMg41U6gFnpDhFinLDpcZY6a363Nczo7kJzTSlrzq2ZXbwr-JyJaYLYC9vKbNF9Abb0Y9ak09ikzwK8NQt1bDwYbvozHDMdFIknaCZBlAgW4FuF6QzHSX--ZOrICpyJw1Y5O-MlWkVKOAfGsIISg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJBedm2Bw51xFAhvXEfBAikPUI7m3-jRAuWS0Pqt_HBFySxXtn68ft0Zlg9f3TqEshNYfrjtCmc6GqkPQEUib4HMlQD8FA5ObdaihRcteR9BTYxgktkrly2d6GDd5cGxc1ar9JiNcfDcy3soJD9i0J8lyjO3d_vdnTgeI8Ah2IBYm_oA3pj1EaVxgJuDEQQlgXe76TBZnE4QdBCeafyJp_rXz0J7hV_W_JsWgbTyOD6nhmvBhmN4RNfuS1O0s6C-KCr60RrfJVNVOIDQPAC5xqrrRC7j2ervMMCpL7v_wOUosEOuX6WRjiWU4t5qoLi_Ib7Sv5K_Oco8L-zRCGhYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me5HJsy6oCRIp8vNfmulTiihvMyqyjv2b613Rlmgn_1ur1Xxms7OmPGs_0hwuiKo8AfCbC4kAInRyWoq16_XWciUG831gbHiyd06w9S18vOVPbpTi43YSOkumSo60moU4AZ54zibYNCz7B5utnyB5Php8wl2krN1x1_jTY1oGP8jANmuqRS2BXXJ-90vk0-z8lXgSQxzzaBjJ2ZHVFFJAQgtd5fzaEJTHwl4Qhv16WQIA45yjQo-M9fR1hGI6iwOfR9dFWnGRiLiwW8nlVY4D8RD2ayLK91Vpz5QxrtE73j7smWc_71Y7tABzsgQazGvfy3ehCr996IcSR60gUAauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_EFNz4GwOCLG1UuJLjjo7IdiF2TRkguEqe_jqBwLWXgrdyqOhN7gdNzbMIuCmIHEU2sSqA-XvCKmtySav7U19cOvjjpmONJz73NOQyCb6e_2WCK5oB241lqMrh_p24g5KPtsNwLTE3_LvGa8pjEt8vqWwQ_ThTl_VRLcFaq4cYKUyA7MLuUS8Ns2mIyTUdPSXXzCnHegKxyQWeVTyQ2tlkYSTUBjd0uyTCTYCKLPcwuOzKaw6G6YqPG84W70G5vV-w8sidEOTiqV8UYwWYx1ttUaVSKiz5K3dseMJWWmCS1qVahDP9DJLGUoFxOfS5LCQQbd6VVUKUcDOImkRrP8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aczB4TwpzUCaD_PYxSiqBUtlx_xzpeuhZIFd0jP0hudMlsOaQ0BdemJALkP7R05-kl7S3QL5JA5m_3cJhXz9jdTl3w-F9_8ukMs_1Q1BYH8W555cm3BwNSr42SYEG0Z8LvgRUh-7-wxm2vqOaWpG5AU9wIbnZSWM04yjnJIwzaBZ52aC_wtGUcjocOxvjwaToEKUXsVG867XAshnxdGdMRXlJE4gX7-ju2qiuPsXhBCfIResBml0mkEsCBBmbbKL-il3F6ayrHKjvzm3okCZzKCoxlJGyl7iS8aQ5hOSvSyLmuNTJLxiH7hnXN64C6JpeBHYKSkMxAkVxoDGqWKSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=YyyTYeZNmzGXmYZ_ZiP6bQFQLfSYfPqRJPr50UXyI395e-DE9cMEZCkVUSnxPvAUqZ-q9Z8WVzVOBp-o5SLnozoLjY31OME8WYN60vozA_ApRR42NftAiXIm-Vv-NjfArodXvaBVzjrfcC8FVrG8GDqtxzPrj3psibIJnTujsJTpTAKYIUtgsb0HxuJEeeSlm9hzKNzb7JvHimSFNubiPj7hID3l21nejbbYzanjsnvj4pzvp8q4TupCy9IP3Bxfr24ynVT3WwCSn7alCklT5iJTAFIoofU187QX4cleojaj4D9m-zAAlKZ2VrspspTvvu2cVgl7zva3pten5S3xdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=YyyTYeZNmzGXmYZ_ZiP6bQFQLfSYfPqRJPr50UXyI395e-DE9cMEZCkVUSnxPvAUqZ-q9Z8WVzVOBp-o5SLnozoLjY31OME8WYN60vozA_ApRR42NftAiXIm-Vv-NjfArodXvaBVzjrfcC8FVrG8GDqtxzPrj3psibIJnTujsJTpTAKYIUtgsb0HxuJEeeSlm9hzKNzb7JvHimSFNubiPj7hID3l21nejbbYzanjsnvj4pzvp8q4TupCy9IP3Bxfr24ynVT3WwCSn7alCklT5iJTAFIoofU187QX4cleojaj4D9m-zAAlKZ2VrspspTvvu2cVgl7zva3pten5S3xdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFOCdGGV9NCGe9A1e8cr8K6DF2gYICAyQR2q6ICa6dCL6airiN8fSjDmeqEgd-PBIIGt5lMjVzg-e83nPW1lzD_66AUIJ37hInz26EF1f_83C0uFlmKub1AlI1QJkHd0Ua8LHoW5nBAr1YsG2aciyx-YqUGvhg2B65vp0gz0ZLDuarJ2Co_o0fTFYSj7-JDh-KDK8zy-hpVmVB-GTjzm2OGyJBWNtywUC_GpA6FYubfUrE6Z6BBQR0EyCVoReBzAz2DSUBxUHe2UncB1yDgDYwe0hBgo3PeL5itfUUSbnrow9lCJGxMLq1mqyIhI57H1vVkeWLCRHGYNuVvI1OJbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEuSGV_v43THVHsR_sowYZMVfkzBjV45DIqKe2r8I_VUeT9h3-dpeJu9mCOG9PEimE81btMBTWBsrULg0vGel3ewbfsuA4krMEdv45fxeueVhaEO9Mc7gKaR0YsLL9gZYn_XPtZZBjjZDUr_2tD7hV0j56tPleaTyweu0JDp2wxmk4lTBmSUaPIsLDd15SU5EVrGMzskyyofp3KpmDnc-ABXfwqiQxYT3EqLmBa8F9bW42FgnlFUDt5xNivRh8iaqa581gtA2f6BC1IT3lSMKXAn9dHMAdvvkWapdGtWe7oOR9jDtQxzSakkbklih5d7mbMqD-XImKW3pSZdp3DMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=DGe1rREwQueegBt_tHY4jGWHo1rd4OTSMnaH2hgB7XpkjgFZrvj_qpUVGT0Pm8Ln_86AUwMKaIsTPRvpK-g8KBn0m1GlS0bDUUaIaKJGbEL0c0HmeV4H1YHZKwh1prxpTN5SHxwumU649xWdTjdF97bkuzqR0DplaDBkdbzpSATmkDzTZrYiQrhGl4TSQTaiSwje8mqG4TidqGy7awk9mII3GEWdMRig2e3Gv7NZwV5t1wEb1H9Fz2BuypKWbBcR4flhC4387xifjP9ho12ACl23wiywsRL5GZrFcf1aNwA5UwcNNcs3AvMAfymQhJsa9G-1aGhtKPGeD-_Kz74oBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=DGe1rREwQueegBt_tHY4jGWHo1rd4OTSMnaH2hgB7XpkjgFZrvj_qpUVGT0Pm8Ln_86AUwMKaIsTPRvpK-g8KBn0m1GlS0bDUUaIaKJGbEL0c0HmeV4H1YHZKwh1prxpTN5SHxwumU649xWdTjdF97bkuzqR0DplaDBkdbzpSATmkDzTZrYiQrhGl4TSQTaiSwje8mqG4TidqGy7awk9mII3GEWdMRig2e3Gv7NZwV5t1wEb1H9Fz2BuypKWbBcR4flhC4387xifjP9ho12ACl23wiywsRL5GZrFcf1aNwA5UwcNNcs3AvMAfymQhJsa9G-1aGhtKPGeD-_Kz74oBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=g1BPskvGAcUrGtJqVM4XhZZAgbh122wmZwHigGUEz4jEC0iUfzQ75UCBV26xgWh1soRLCpnb799JX21nhIu2Zb7xPni2-nR3PqnmxuCd_x8VPpLZxb-Xa4jR2AT4HNNcx6Q2gKsrazA_HiM2D_y59xDtWJnWMnBnXwP1pw9FmtdpK_FNpBWxHWy26-LEs8_tGSDhOC305Kk2XCRi-WA1xreBYaDIcXgyIGbYHNmVVYBfNPJTt9rH6FDeIcK2gD3Bx7csV39qBT5bU1xHRQA0TB-sf4msrnVY7Jn5sRl67411STOAq2oX-_aKEfbFaPb1n1dKsOuwG2lidsbrpeKxiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=g1BPskvGAcUrGtJqVM4XhZZAgbh122wmZwHigGUEz4jEC0iUfzQ75UCBV26xgWh1soRLCpnb799JX21nhIu2Zb7xPni2-nR3PqnmxuCd_x8VPpLZxb-Xa4jR2AT4HNNcx6Q2gKsrazA_HiM2D_y59xDtWJnWMnBnXwP1pw9FmtdpK_FNpBWxHWy26-LEs8_tGSDhOC305Kk2XCRi-WA1xreBYaDIcXgyIGbYHNmVVYBfNPJTt9rH6FDeIcK2gD3Bx7csV39qBT5bU1xHRQA0TB-sf4msrnVY7Jn5sRl67411STOAq2oX-_aKEfbFaPb1n1dKsOuwG2lidsbrpeKxiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arYCOeHxYviLYEgUdPjUIgxgr2Oph4PXASjkQUKT_BL9piKGOVzEHaxps5g-XfoXREQr5XtLsF_wOhe-q40Ub3fKR9Eo05ExChWytiVb9XP4CrXP7p_gtmadJCT7yZuY17cnO1tF4Cc027ND8LAyXw0ytTo_BlvjsXY7toIahCu63CQhShXgrZeN8erc1LzlneAkrrQNm90rnZMdNtd9TSc3XusCDAMrbUgqD7roRet8TtCvIpiTob6xbQs1y9Iv6vNjdUvXOFUE_gZbcS2q29ThQg0_mbTzyN5zQzakoxSC4vnwGH2f7TN3uYrivQnqjNhFZZdpLRuqeCR8MZvpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=eSQjU77l7aiAmDQV-YLChdL8-joUlVOIzRYghjar00hLcQjQ_WT3Mow7LFH0KI9hiU3PjueTjelJEs5xTHzEKfK5l0zl1Y14rVnFCm-DpBQS5ZBV9jAjXmxuqoZmWVtY_83VMyEm-SUE33-HrOc4ItZWH_kC0cvpDyA89ESdIMOUzXPxK1O2G5wtGMO-ULxrOW1mpyvDxXKagI7rErh9j4VT_HkKEJ94S7lKuIzCFVmOPMtaKI__tW3ulheDluRMxWTLvJgAHl6T6BvwpqXD-JW1c3B1ORT4bEEP6mKjtNEmz_OOPk-hveHo1vXeDQIJibfgEis7gtn2Hh4eHBAToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=eSQjU77l7aiAmDQV-YLChdL8-joUlVOIzRYghjar00hLcQjQ_WT3Mow7LFH0KI9hiU3PjueTjelJEs5xTHzEKfK5l0zl1Y14rVnFCm-DpBQS5ZBV9jAjXmxuqoZmWVtY_83VMyEm-SUE33-HrOc4ItZWH_kC0cvpDyA89ESdIMOUzXPxK1O2G5wtGMO-ULxrOW1mpyvDxXKagI7rErh9j4VT_HkKEJ94S7lKuIzCFVmOPMtaKI__tW3ulheDluRMxWTLvJgAHl6T6BvwpqXD-JW1c3B1ORT4bEEP6mKjtNEmz_OOPk-hveHo1vXeDQIJibfgEis7gtn2Hh4eHBAToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq-YAnWRqeUct3FNgeklULHGX9zlnPuCdHL3rPsCpnTgGXH31EWjr4I-YESxf-glBtfgUatYAf9c9bUJ-lpCyNeKrubgFfEaXF7glnyz0rhfUdT7t61ZK78g-HE0aTotq8VzgBPdMwbPxoWRBmFPzm-TfuY7UG_6JEINPUOvO65rCnHHgyiFjfw-nSg-771fYTwRt31fY3l25Vom0evl-wft97sTLw0o5dFrGF-tZGWBUzvuXW4bYcHBXFLpC_dh2dU-hF1CrbmULhjOg0u7C9cGwzmF_5rUCAwDt8o43kBDZC7jDsOh-wl9uF-xk4pObD7ORqrywcO-3mWTCv7LUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqpZj-TJzQQFb-0JM1Fyq2Noz0CivQ11Tfwtls232JbcS5vNg8D8v3ibnNrjw2VatJKw__BBJ8o_Y2BJ67bzbt-fW4t7d2VWl62kBHFjcUDVjzWvW3nywF44FY0VF0rQiHrq5yOV0yiEguAjlPYPFF9Q8zGZH_jT9TR6d01k373YrwsQKMP6FuxAiSm9jmMdUm8XJVNiSpTan7S2IHmigw4j-yDd87eXjLDxPkIo55VY-1JVWAehreoZ5CTa_-cqFtX-YtGG6Tx6bFHo3_pSNaXJjE1QOTQ3SDNHnDmlkqGaQKGL5-0Ngv9nlev2i7PI5bw3bacnkHcNYaoNP4zvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6a6p3Fr6Hjl8MztbfFo6VgZncte6pLWdR8vM1kOBBbmn_qJ2Ozd5j88L35bjwX70vm_7RPS4ixt8VJqrVbjsC6Z91fiC36ouv86iqBGbD8mf438j6a3TG6_nJnugHgBdcXiJU6doPwI2B8AdzI9HhVtdcWb_n-tlI51FQkhZ5jqoXB9zWnxPVSJhjwf6e2rFOmAi7ikfqm7jhdDvQ12K5Xw_yBK6qsEeOQ2U32hDTPRxGH_c6Cw9cLsRhqJz9s-dlNT8FCrMdtp0rPtLxZpVx1-EvP4nIbGD7Csp9a0C6b84EeRsgRNViEjBDCP4z2FsBiXx02YW-QthlsgrTWscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=jfxDgaHlHjDyXmsnOnfQtLarb1OvWDIRhRdRE2swqlmB6qN5yC6-wuA_WsZnHW0F-00N4g2118tBqzsNcxhoSz_w-AVOuJtcI58cr4R6CFlZYhdgdlABbu3N031XzgPwMf4vTq9V_e4XY2861GAuYz2enoZ6yjgjxGfBUosfWk80D9DyFRvTGi8SGIezAtXQZGZfIn9rKr9HKXDxvMACKA1ZoL4RhpGl8J6j1q6T8WgpajbaCuNwhdUJektqgErXQj0GCEzPwCn64MVN2JqbKDOKEZnMl9F3J08JvHPmmjago805f8PgM-1JhpmkTU-qrEOM0mlK48skL7BK8txnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=jfxDgaHlHjDyXmsnOnfQtLarb1OvWDIRhRdRE2swqlmB6qN5yC6-wuA_WsZnHW0F-00N4g2118tBqzsNcxhoSz_w-AVOuJtcI58cr4R6CFlZYhdgdlABbu3N031XzgPwMf4vTq9V_e4XY2861GAuYz2enoZ6yjgjxGfBUosfWk80D9DyFRvTGi8SGIezAtXQZGZfIn9rKr9HKXDxvMACKA1ZoL4RhpGl8J6j1q6T8WgpajbaCuNwhdUJektqgErXQj0GCEzPwCn64MVN2JqbKDOKEZnMl9F3J08JvHPmmjago805f8PgM-1JhpmkTU-qrEOM0mlK48skL7BK8txnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
